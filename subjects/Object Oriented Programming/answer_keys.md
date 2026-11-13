# Object Oriented Programming: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper db4158a4e783

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/BTech_CSBS_7036/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1   A.   What are primitive data types? Provide an appropriate programming   [05]
BL-3   example to illustrate the use of a primitive data type.
02 Marks – Primitive Data Types
03 Marks – programming example
Primitive Data Types: -
Data types specify the type of data stored in a variable.
The eight primitive data types.
S. N. Data Type   Example
1.   boolean   boolean status=true;
2.   char   char ch=’a’
3.   byte   byte b=87
4.   short   short s=512
5.   int   int i=45000
6.   long   Long l=20L
7.   float   float r=33.5f;
8.   double   double d=3.147
Programming Example:
class PrimitiveDemo {
public static void main(String[] args) {
char a = 'A';
byte b = 10;
********** 1 **********
--- page 2 ---
short c = 1000;
System.out.println(a);
System.out.println(b);
System.out.println(c);
int a1 = 50000;
float b1 = 5.5f;
double c1 = 99.99;
System.out.println(a1);
System.out.println(b1);
System.out.println(c1);
}
}
CO-2   B.   Create a class named ShapeArea to calculate the area of a circle and a square   [05]
BL-3   using method overloading. Define the main( ) method to create an object of
ShapeArea and invoke both methods.
02 Mark – Class Definition, Main Method & Object Creation in main
03 Marks –Code for Method Overloading
class ShapeArea {
static final float PI = 3.14f;
void area(float radius) {
System.out.println(PI * radius * radius)
}
void area(double side) {
System.out.println(side * side);
}
static public void main(String[] args) {
ShapeArea calc = new ShapeArea ();
calc.area(5.0);
calc.area(4.0);
}
}
CO-4   C.   Use your knowledge of abstract classes and interfaces to explain how they   [05]
BL-3   differ. Provide a suitable programming example.
03 Marks – At least 3-4 Differences
02 Marks – Programming example
Abstract Class   Interface
Definition   A class declared using   A reference type that
the abstract keyword that contains abstract methods
may contain abstract and and constants
concrete methods
Keyword   abstract class   interface
Used
Method Type Can have abstract and   Methods are abstract by
non-abstract methods   default (can also have
default/static methods)
********** 2 **********
--- page 3 ---
Variables   Can have instance   Variables are public static
variables   final by default
Access   Methods can be private,   Methods are public by
Modifiers   protected, public   default
Keyword for   extends   implements
Inheritance
Multiple   Not supported   Supported
Inheritance
Example   IS-A with shared   Contract-based design
Relationship   implementation
Example:Abstract Class
abstract class Animal {
abstract void sound();
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {
System.out.println("Dog barks");
}
}
Example: Interface
interface Animal {
void sound();
}
class Dog implements Animal {
public void sound() {
System.out.println("Dog barks");
}
}
CO-5   D.   What is a generic method? Use the idea of a generic method to write a   [05]
BL-3   suitable programming example.
02 Marks – Generic Method
03 Marks - Programming Example
- A generic method declares a type parameter in its method
signature.
-   It can be called with different types of arguments based on the type
of arguments passed to the generic method
- Programming Example:
- Code reuse and type safety are the advantages of the generic
class Test {
static <T> void genericDisplay(T element){
System.out.println(element);
********** 3 **********
--- page 4 ---
}
public static void main(String[] args) {
// Calling generic method with Integer argument
genericDisplay(110);   // passing Integer argument
genericDisplay("OOP and OOPL"); //passing String Argument
genericDisplay(110.0);   //Passing Double argument
}
}
Section- B
Q2
CO-2 A   What is polymorphism? How does static polymorphism differ from   [10]
dynamic polymorphism? Demonstrate it with a programming example.
BL-3
01 Marks Polymorphism
05 Marks – Difference between polymorphism
04 Marks – Programming example
Static Polymorphism   Dynamic Polymorphism
Also known as compile-time Also known as run-time
polymorphism   polymorphism
Achieved   by   method Achieved   by   method
overloading   overriding.
Uses the concept of compile- Uses   the concept   of
time binding(or early binding) . runtime binding (or late
Connecting a method call to the binding).
method body   is known as
binding.
Slower   than   Dynamic Faster   than   static
polymorphism   polymorphism.
To   implement   static To implement dynamic
polymorphism, inheritance is polymorphism,
not necessary   inheritance is necessary.
********** 4 **********
--- page 5 ---
Static Polymorphism :
class Student {
String name;
int age;
Student() {
name = "Unknown";
age = 0;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Rahul", 20);
a.display();
b.display();
}
}
Dynamic Polymorphism:
class Printer {
void print() {
System.out.println("Printing");
}
}
class InkjetPrinter extends Printer {
void print() {
System.out.println("Printing using Inkjet");
}
}
class LaserPrinter extends Printer {
void print() {
System.out.println("Printing using Laser");
}
}
public class Main {
public static void main(String[] args) {
********** 5 **********
--- page 6 ---
Printer p;
p = new InkjetPrinter();
p.print();
p = new LaserPrinter();
p.print();
}
}
CO-4 B   An electricity department needs a billing system that handles different   [10]
consumer types with varying rates. Design a program using object-oriented
BL-3
principles where ElectricityBill is an abstract class containing consumerId
(int), consumerName (String), and unitsConsumed (double) as data
members. Include a constructor to   initialize these fields and a
displayDetails( ) method to show the consumer's information. The abstract
method calculateBill( ) must be implemented by subclasses. Create
DomesticBill subclass with a ₹5 per unit rate and a CommercialBill subclass
with a ₹8 per unit rate. In the main method, demonstrate the bill calculation
and display for both consumer types. The total bill is calculated by
multiplying the units consumed by the unit rate.
03 Marks – Code for Abstract class & method
05 Marks - code for Subclasses & methods
02 Marks – Main & execution
abstract class ElectricityBill {
int consumerId;
String consumerName;
double unitsConsumed;
ElectricityBill(int cId, String cName, double unitsConsumed) {
this.consumerId = cId;
this.consumerName = cName;
this.unitsConsumed = unitsConsumed;
}
void displayDetails() {
System.out.println("ID: " + consumerId + ", Name: " +
consumerName + ", Units: " + unitsConsumed);
}
abstract double calculateBill();
}
class DomesticBill extends ElectricityBill {
DomesticBill(int id, String name, double units) {
super(id, name, units);
}
double calculateBill() {
return 5 * unitsConsumed;
}
}
class CommercialBill extends ElectricityBill {
CommercialBill(int id, String name, double units) {
super(id, name, units);
********** 6 **********
--- page 7 ---
}
double calculateBill() {
return 8 * unitsConsumed;
}
}
public class Main {
public static void main(String[] args) {
ElectricityBill domestic = new DomesticBill(101, "Ram", 150.0);
ElectricityBill commercial = new CommercialBill(201, "ABC Corp",
250.0);
domestic.displayDetails();
System.out.println("Bill: " + domestic.calculateBill() + "\n");
commercial.displayDetails();
System.out.println("Bill: " + commercial.calculateBill());
}
}
Q3
CO-3 A   Write an object-oriented program to demonstrate nested try–catch blocks.   [10]
The outer try block should handle an arithmetic exception for a division,
BL-3
while the inner try block should manage an array index out of bounds
exception when accessing index 5 of an array of size 3.
03 Marks – Code for Divide & Array of size 3.
02 Marks – main method
05 Marks – Appropriate code for Nested Try-Catch blocks
public class NestedTryDemo {
public static void main(String[] args) {
try {
int a = 10;
int b = 0;
try {
int arr[] = {1,2,3};
System.out.println(arr[4]);
}
catch(ArrayIndexOutOfBoundsException e) {
System.out.println("Array index error.");
}
int result = a / b;
}
catch(ArithmeticException e) {
System.out.println("Division by zero error.");
}
System.out.println("Program continues...");
}
}
CO-5 B   Demonstrate how the Composite design pattern works by implementing a   [10]
suitable program.
BL-3
05 Marks - Demonstration of Composite design pattern
05 Marks – Suitable programming example
Composite
********** 7 **********
--- page 8 ---
- Composite pattern is used where we need to treat a group of objects
in a similar way as a single object.
- Composite pattern composes objects in terms of a tree structure to
represent the part as well as the whole hierarchy.
-   This type of design pattern comes under a structural pattern as this
pattern creates a tree structure of a group of objects.
- Allows you to treat individual objects (leaf) and groups of objects
(composite) uniformly
-   Organizes objects into a tree structure (hierarchy)
Program :
import java.util.*;
class CompositePatternDemo {
public static void main(String ... args) {
Employee CEO = new Employee("Rohit","CEO", 30000);
Employee headSales = new Employee("Virat","Head Sales", 20000);
Employee headMarketing = new Employee("Surya","Head
Marketing", 20000);
Employee clerk1 = new Employee("Japrit","Marketing", 10000);
Employee clerk2 = new Employee("Hardik","Marketing", 10000);
Employee salesExecutive1 = new Employee("Abhishek","Sales",
10000);
Employee salesExecutive2 = new Employee("Ishan","Sales", 10000);
CEO.add(headSales);
********** 8 **********
--- page 9 ---
CEO.add(headMarketing);
headSales.add(salesExecutive1);
headSales.add(salesExecutive2);
headMarketing.add(clerk1);
headMarketing.add(clerk2);
System.out.println(CEO);
for (Employee headEmployee : CEO.getSubordinates()) {
System.out.println(headEmployee);
for (Employee employee : headEmployee.getSubordinates()) {
System.out.println(employee);
}
}
}
}
class Employee {
private String name;
private String dept;
private int salary;
private List<Employee> subordinates;
public Employee(String name,String dept, int sal) {
this.name = name;
this.dept = dept;
this.salary = sal;
subordinates = new ArrayList<Employee>();
}
public void add(Employee e) {
subordinates.add(e);
}
public void remove(Employee e) {
subordinates.remove(e);
}
public List<Employee> getSubordinates(){
return subordinates;
}
public String toString(){
return ("Employee :--> Name : " + name + ", dept : " + dept + ",
salary :" + salary+" <--");
}
}
Q4
CO-2 A   Implement an object-oriented program to define a class Distance with feet   [10]
and inches as instance variables and assign beginning values using a
BL-3
parameterized constructor. Define addDistances( ) to add two distances
passed as objects to the method & display the addition in the same method.
Test your program with 1-2 inputs, and it should find and display the correct
addition of two distances.
********** 9 **********
--- page 10 ---
02 Marks - class Distance & instance variables
02 Marks - Parameterised constructor
04 Marks – addDistanc() method
02 Marks – Main method, object creation, and call to methods
import java.util.*;
class Distance{
int f,i;
Distance(int f,int i){
this.f=f;
this.i=i;
}
void addDistances(Distance a, Distance b){
int in,ft=0;
in=a.i+b.i;
if(in>11){
ft=in/12;
in=in-ft*12;
}
ft+=a.f+b.f;
System.out.println("Distance is "+ft+"ft "+in+"in");
}
public static void main(String...args){
Distance d1 =new Distance(12,9);
Distance d2 =new Distance(9,8);
d1.addDistances(d1,d2);
}
}
CO-1 B   What are the different types of decision-making statements? Use decision-   [10]
BL-3   making statements in a program to explain it.
02 Marks – If Else
02 Marks – Nested if-else or ladder
02 Marks – Switch-case
04 Marks – Programming example
Decision-making statements in Java are fundamental constructs that allow
programmers to control the flow of their code based on certain conditions.
Decision-Making Statements
a) if statement
b) if-else statement
c) if-else-if ladder
d) Nested if statements
e) switch statement
********** 10 **********
--- page 11 ---
if...else statement
An if statement can be followed by an optional else statement, which
executes when the boolean expression is false.
Syntax
if(condition)
{
//code to be executed if the condition is true
}
else
{
//code to be executed if the condition is false
}
Nested if statement
You can use one if or else if statement inside another if or else
Syntax:
if statement(s).
if(condition)
{
//code to be executed
if(condition)
{
//code to be executed
}
}
Switch statement
A switch statement allows a variable to be tested for equality against a list
of values.
Syntax:
switch(expression)
{
case <value1>:
//code to be executed
break;
case <value2>:
//code to be executed
break;
default:
//code to be defaultly executed
}
********** 11 **********
--- page 12 ---
Example:
class Test {
public static void main(String[] args) {
int choice = 1;
int num = 5;
switch (choice) {
case 1:
if (num > 0) {
if (num % 2 == 0)
System.out.println("Positive Even");
else
System.out.println("Positive Odd");
} else {
System.out.println("Not Positive");
}
break;
default:
System.out.println("Invalid choice");
}
}
}
Q5
CO-1 A   Create a class called FibboTest that includes a method dispFibo(int n). This   [10]
method should accept a number and output the Nth Fibonacci number.
BL-3
Develop a   full object-oriented program (OOP) to   illustrate   this
functionality.
02 Mark –FibboTest
02 Marks – dispFibo function
04 Marks – Logic of finding Fibonacci number
02 Marks – main, object creation and method call
class FibboTest {
public int dispFibo(int n) {
if (n <= 0) return 0;
if (n == 1) return 1;
int a = 0, b = 1, c;
for (int i = 2; i <= n; i++) {
c = a + b;
a = b;
b = c;
}
return b;
}
public static void main(String[] args) {
System.out.println(new FibboTest().dispFibo(6));
}
}
********** 12 **********
--- page 13 ---
CO-4 B   What is an inner class? Explain the different types of inner classes. Write a   [10]
program demonstrating:
BL-3
→ Inner class
→ Local inner class
02 Marks – Inner Classes
03 Marks – Types of inner classes
05 Marks – Programming example
- An Inner Class is a class defined inside another class.
-   It helps in logically grouping related classes and improving
encapsulation.
Types of Inner Classes
• Inner Class: A class declared inside another class but outside any
method.
Ex.
class Out{
class In{
}
}
•   Static Nested Class: An inner class declared with the static
keyword.
Ex.
class Out{
static class In{
}
}
•   Method-Local Inner Class : A class declared inside a method of
another class.
Ex.
class Out{
void fun(){
class In{
}
}
}
• Anonymous Inner Class: An Anonymous Inner Class is a class
without a name that is declared and instantiated at the same time.It
is mainly used when a class is required only once for a short
implementation.
Ex.
abstractClass obj = new abstractClass() {
void methods() {
// code
}
};
Inner class:
class Outer {
private String msg = "Member Inner Class";
********** 13 **********
--- page 14 ---
class Inner {
void display() {
System.out.println(msg);
}
}
}
class TestMember {
public static void main(String[] args) {
Outer obj = new Outer();
Outer.Inner in = obj.new Inner();
in.display();
}
}
Local inner class:
class OuterMethod {
void display() {
class Inner {
void message() {
System.out.println("Method Local Inner Class");
}
}
Inner obj = new Inner();
obj.message();
}
}
class TestMethodLocal {
public static void main(String[] args) {
OuterMethod obj = new OuterMethod();
obj.display();
}
}
Q6
CO-5 A   Create a class Date with day, month and year as instance variables to   [10]
represent a Date. Write an object-oriented program that uses a generic class
BL-3
DateTest to store, read, and display a date using a user-defined Date class.
Use the constructor to store today's date, provide methods to read your date
of birth, and a display method to display the date.
02 Marks – Date Class
02 Marks – Generic Class Definition & constructor
02 Marks – Read Date in the generic class
02 Marks – Display Date in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class Date {
int day;
int month;
int year;
}
class DateTest<T> {
T d;
********** 14 **********
--- page 15 ---
DateTest(T d, int day, int month, int year) {
this.d = d;
Date temp = (Date) d;
temp.day = day;
temp.month = month;
temp.year = year;
}
void readDate() {
Scanner sc = new Scanner(System.in);
Date temp = (Date) d;
System.out.print("Enter Day: ");
temp.day = sc.nextInt();
System.out.print("Enter Month: ");
temp.month = sc.nextInt();
System.out.print("Enter Year: ");
temp.year = sc.nextInt();
}
void displayDate() {
Date temp = (Date) d;
System.out.println("Date: " + temp.day + "/" + temp.month + "/" +
temp.year);
}
}
class Main {
public static void main(String[] args) {
Date today = new Date();
DateTest<Date> obj = new DateTest<>(today, 28, 4, 2026);
System.out.println("Today's Date:");
obj.displayDate();
System.out.println("\nEnter your Date of Birth:");
obj.readDate();
System.out.println("Your Date of Birth:");
obj.displayDate();
}
}
CO-2 B   Define constructors and explain their purpose. Identify which constructor is   [10]
added automatically by the compiler. Describe the different types of
BL-3
constructors and provide a programming example.
02 Marks Constructor
01 Mark – constructor added by compiler
02 Marks Types of Constructors
05 Marks – Programming example
Constructor and its Purpose
- A constructor is a special method with the same name as the class that
initializes an object of that class.
-   It is called a constructor because it sets the values of the class’s data
members.
-   Properties/characteristics of a constructor
1. The constructor has the same name as the class.
2. The constructor does not have a return value (not even void).
********** 15 **********
--- page 16 ---
3. We cannot call the constructor directly. It is called automatically
when the object is created.
- Whenever an object is created, the constructor is invoked automatically.
- A constructor enables an object to initialise itself at the time of its
creation without the need to make a separate call to the instance
methods.
- The return type concept is not applicable to a constructor, even void. If
we accidentally declare a return type for the constructor, we won’t get
any compile-time or runtime error; the compiler simply treats it as a
normal method.
Types of Constructors:
Default Constructor
- A default constructor is an automatically created no-argument
constructor provided by the compiler if no constructors are explicitly
defined in the class.
- The programmer explicitly writes user-defined constructors and may
include custom initialization logic.
- The key difference is that default constructors rely on standard, default
values for object fields, while user-defined constructors give developers
control over initialization.
Parameterized Constructor
- A parameterised constructor accepts parameters to provide specific
values during object creation, allowing for more flexibility and control
over the object's initial state.
Programming Example:
class Student {
String name;
int age;
Student() {
name = "Sachin";
age = 45;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Tendulkar", 50);
a.display();
b.display();
********** 16 **********
--- page 17 ---
}
}
Q7
CO-3 A   Implement an object-oriented program using character-oriented streams.   [10]
The program should read a text file, convert all lowercase letters to
BL-3
uppercase, and write the modified content back to the file. Your program
should handle exceptions and ensure the proper closing of the file.
02 Marks - File Opening in Read mode & closing
02 Marks – File Opening in Write mode & closing
05 Marks – lowercase to uppercase & writing to file
01 Mark – Exception Handling
import java.io.*;
class LowerToUpper {
public static void main(String[] args) throws IOException {
FileReader fr = null;
FileWriter fw = null;
try{
fr = new FileReader("input.txt");
fw = new FileWriter("output.txt");
int ch;
while ((ch = fr.read()) != -1) {
if (Character.isLowerCase((char) ch)) {
ch = Character.toUpperCase((char) ch);
}
fw.write(ch);
}
System.out.println("Conversion completed.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
finally{
if(fr!=null) fr.close();
if(fw!=null) fw.close();
}
}
}
CO-1 B   Create an object-oriented program that determines if a number is even or   [05]
odd.
BL-3
02 Marks – Class & main method
03 Marks – Checking number is even or odd
class EvenOddChecker {
public void checkEvenOdd(int number) {
System.out.print(number + " ");
if (number % 2 == 0) {
System.out.println("is EVEN");
} else {
System.out.println("is ODD");
}
********** 17 **********
--- page 18 ---
}
public static void main(String[] args) {
EvenOddChecker obj = new EvenOddChecker();
obj.checkEvenOdd(80);
}
}
CO-2 C   Apply the concept of abstraction by explaining its meaning with an   [05]
appropriate example.
BL-3
02 Marks – Abstraction
03 Marks – Programming Example
-   Abstraction means hiding the implementation details
-   Abstraction = User knows what to do, not how it is done
- Ex: We operate the TV using a remote, but we do not know how it
works.
-   Abstraction means showing only the essential features to the user
and hiding the internal implementation details.
Programming example:
class AbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void dispMethod( ){
System.out.println(data);
}
}
class MainTest{
public static void main(String args[ ]){
AbstractionTest eat = new AbstractionTest( );
eat.setterMethod( );
eat.dispMethod( );
}
}
The user of the AbstractionTest class does not need to know how these
methods are implemented—only that setterMethod( ) and dispMethod( ) do
not accept any arguments and do not return any values. The user is unaware
of how data is stored or displayed. In the main method, an AbstractionTest
object is created, and the setter and getter methods are called, demonstrating
abstraction. Thus, implementation details are hidden, and only method
interfaces are exposed.
X----------------------------------------------------------------------------------------------------------------- X
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 3fb5e9d1893d

- Departments: Computer Engineering, Data Science
- Programmes: BTech Computer 7002, BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/BTech_CSE_DS_7057/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1   A.   What are primitive data types? Provide an appropriate programming   [05]
BL-3   example to illustrate the use of a primitive data type.
02 Marks – Primitive Data Types
03 Marks – programming example
Primitive Data Types: -
Data types specify the type of data stored in a variable.
The eight primitive data types.
S. N. Data Type   Example
1.   boolean   boolean status=true;
2.   char   char ch=’a’
3.   byte   byte b=87
4.   short   short s=512
5.   int   int i=45000
6.   long   Long l=20L
7.   float   float r=33.5f;
8.   double   double d=3.147
Programming Example:
class PrimitiveDemo {
public static void main(String[] args) {
char a = 'A';
byte b = 10;
********** 1 **********
--- page 2 ---
short c = 1000;
System.out.println(a);
System.out.println(b);
System.out.println(c);
int a1 = 50000;
float b1 = 5.5f;
double c1 = 99.99;
System.out.println(a1);
System.out.println(b1);
System.out.println(c1);
}
}
CO-2   B.   Create a class named ShapeArea to calculate the area of a circle and a square   [05]
BL-3   using method overloading. Define the main( ) method to create an object of
ShapeArea and invoke both methods.
02 Mark – Class Definition, Main Method & Object Creation in main
03 Marks –Code for Method Overloading
class ShapeArea {
static final float PI = 3.14f;
void area(float radius) {
System.out.println(PI * radius * radius)
}
void area(double side) {
System.out.println(side * side);
}
static public void main(String[] args) {
ShapeArea calc = new ShapeArea ();
calc.area(5.0);
calc.area(4.0);
}
}
CO-4   C.   Use your knowledge of abstract classes and interfaces to explain how they   [05]
BL-3   differ. Provide a suitable programming example.
03 Marks – At least 3-4 Differences
02 Marks – Programming example
Abstract Class   Interface
Definition   A class declared using   A reference type that
the abstract keyword that contains abstract methods
may contain abstract and and constants
concrete methods
Keyword   abstract class   interface
Used
Method Type Can have abstract and   Methods are abstract by
non-abstract methods   default (can also have
default/static methods)
********** 2 **********
--- page 3 ---
Variables   Can have instance   Variables are public static
variables   final by default
Access   Methods can be private,   Methods are public by
Modifiers   protected, public   default
Keyword for   extends   implements
Inheritance
Multiple   Not supported   Supported
Inheritance
Example   IS-A with shared   Contract-based design
Relationship   implementation
Example:Abstract Class
abstract class Animal {
abstract void sound();
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {
System.out.println("Dog barks");
}
}
Example: Interface
interface Animal {
void sound();
}
class Dog implements Animal {
public void sound() {
System.out.println("Dog barks");
}
}
CO-5   D.   What is a generic method? Use the idea of a generic method to write a   [05]
BL-3   suitable programming example.
02 Marks – Generic Method
03 Marks - Programming Example
- A generic method declares a type parameter in its method
signature.
-   It can be called with different types of arguments based on the type
of arguments passed to the generic method
- Programming Example:
- Code reuse and type safety are the advantages of the generic
class Test {
static <T> void genericDisplay(T element){
System.out.println(element);
********** 3 **********
--- page 4 ---
}
public static void main(String[] args) {
// Calling generic method with Integer argument
genericDisplay(110);   // passing Integer argument
genericDisplay("OOP and OOPL"); //passing String Argument
genericDisplay(110.0);   //Passing Double argument
}
}
Section- B
Q2
CO-2 A   What is polymorphism? How does static polymorphism differ from   [10]
dynamic polymorphism? Demonstrate it with a programming example.
BL-3
01 Marks Polymorphism
05 Marks – Difference between polymorphism
04 Marks – Programming example
Static Polymorphism   Dynamic Polymorphism
Also known as compile-time Also known as run-time
polymorphism   polymorphism
Achieved   by   method Achieved   by   method
overloading   overriding.
Uses the concept of compile- Uses   the concept   of
time binding(or early binding) . runtime binding (or late
Connecting a method call to the binding).
method body   is known as
binding.
Slower   than   Dynamic Faster   than   static
polymorphism   polymorphism.
To   implement   static To implement dynamic
polymorphism, inheritance is polymorphism,
not necessary   inheritance is necessary.
********** 4 **********
--- page 5 ---
Static Polymorphism :
class Student {
String name;
int age;
Student() {
name = "Unknown";
age = 0;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Rahul", 20);
a.display();
b.display();
}
}
Dynamic Polymorphism:
class Printer {
void print() {
System.out.println("Printing");
}
}
class InkjetPrinter extends Printer {
void print() {
System.out.println("Printing using Inkjet");
}
}
class LaserPrinter extends Printer {
void print() {
System.out.println("Printing using Laser");
}
}
public class Main {
public static void main(String[] args) {
********** 5 **********
--- page 6 ---
Printer p;
p = new InkjetPrinter();
p.print();
p = new LaserPrinter();
p.print();
}
}
CO-4 B   An electricity department needs a billing system that handles different   [10]
consumer types with varying rates. Design a program using object-oriented
BL-3
principles where ElectricityBill is an abstract class containing consumerId
(int), consumerName (String), and unitsConsumed (double) as data
members. Include a constructor to   initialize these fields and a
displayDetails( ) method to show the consumer's information. The abstract
method calculateBill( ) must be implemented by subclasses. Create
DomesticBill subclass with a ₹5 per unit rate and a CommercialBill subclass
with a ₹8 per unit rate. In the main method, demonstrate the bill calculation
and display for both consumer types. The total bill is calculated by
multiplying the units consumed by the unit rate.
03 Marks – Code for Abstract class & method
05 Marks - code for Subclasses & methods
02 Marks – Main & execution
abstract class ElectricityBill {
int consumerId;
String consumerName;
double unitsConsumed;
ElectricityBill(int cId, String cName, double unitsConsumed) {
this.consumerId = cId;
this.consumerName = cName;
this.unitsConsumed = unitsConsumed;
}
void displayDetails() {
System.out.println("ID: " + consumerId + ", Name: " +
consumerName + ", Units: " + unitsConsumed);
}
abstract double calculateBill();
}
class DomesticBill extends ElectricityBill {
DomesticBill(int id, String name, double units) {
super(id, name, units);
}
double calculateBill() {
return 5 * unitsConsumed;
}
}
class CommercialBill extends ElectricityBill {
CommercialBill(int id, String name, double units) {
super(id, name, units);
********** 6 **********
--- page 7 ---
}
double calculateBill() {
return 8 * unitsConsumed;
}
}
public class Main {
public static void main(String[] args) {
ElectricityBill domestic = new DomesticBill(101, "Ram", 150.0);
ElectricityBill commercial = new CommercialBill(201, "ABC Corp",
250.0);
domestic.displayDetails();
System.out.println("Bill: " + domestic.calculateBill() + "\n");
commercial.displayDetails();
System.out.println("Bill: " + commercial.calculateBill());
}
}
Q3
CO-3 A   Write an object-oriented program to demonstrate nested try–catch blocks.   [10]
The outer try block should handle an arithmetic exception for a division,
BL-3
while the inner try block should manage an array index out of bounds
exception when accessing index 5 of an array of size 3.
03 Marks – Code for Divide & Array of size 3.
02 Marks – main method
05 Marks – Appropriate code for Nested Try-Catch blocks
public class NestedTryDemo {
public static void main(String[] args) {
try {
int a = 10;
int b = 0;
try {
int arr[] = {1,2,3};
System.out.println(arr[4]);
}
catch(ArrayIndexOutOfBoundsException e) {
System.out.println("Array index error.");
}
int result = a / b;
}
catch(ArithmeticException e) {
System.out.println("Division by zero error.");
}
System.out.println("Program continues...");
}
}
CO-5 B   Demonstrate how the Composite design pattern works by implementing a   [10]
suitable program.
BL-3
05 Marks - Demonstration of Composite design pattern
05 Marks – Suitable programming example
Composite
********** 7 **********
--- page 8 ---
- Composite pattern is used where we need to treat a group of objects
in a similar way as a single object.
- Composite pattern composes objects in terms of a tree structure to
represent the part as well as the whole hierarchy.
-   This type of design pattern comes under a structural pattern as this
pattern creates a tree structure of a group of objects.
- Allows you to treat individual objects (leaf) and groups of objects
(composite) uniformly
-   Organizes objects into a tree structure (hierarchy)
Program :
import java.util.*;
class CompositePatternDemo {
public static void main(String ... args) {
Employee CEO = new Employee("Rohit","CEO", 30000);
Employee headSales = new Employee("Virat","Head Sales", 20000);
Employee headMarketing = new Employee("Surya","Head
Marketing", 20000);
Employee clerk1 = new Employee("Japrit","Marketing", 10000);
Employee clerk2 = new Employee("Hardik","Marketing", 10000);
Employee salesExecutive1 = new Employee("Abhishek","Sales",
10000);
Employee salesExecutive2 = new Employee("Ishan","Sales", 10000);
CEO.add(headSales);
********** 8 **********
--- page 9 ---
CEO.add(headMarketing);
headSales.add(salesExecutive1);
headSales.add(salesExecutive2);
headMarketing.add(clerk1);
headMarketing.add(clerk2);
System.out.println(CEO);
for (Employee headEmployee : CEO.getSubordinates()) {
System.out.println(headEmployee);
for (Employee employee : headEmployee.getSubordinates()) {
System.out.println(employee);
}
}
}
}
class Employee {
private String name;
private String dept;
private int salary;
private List<Employee> subordinates;
public Employee(String name,String dept, int sal) {
this.name = name;
this.dept = dept;
this.salary = sal;
subordinates = new ArrayList<Employee>();
}
public void add(Employee e) {
subordinates.add(e);
}
public void remove(Employee e) {
subordinates.remove(e);
}
public List<Employee> getSubordinates(){
return subordinates;
}
public String toString(){
return ("Employee :--> Name : " + name + ", dept : " + dept + ",
salary :" + salary+" <--");
}
}
Q4
CO-2 A   Implement an object-oriented program to define a class Distance with feet   [10]
and inches as instance variables and assign beginning values using a
BL-3
parameterized constructor. Define addDistances( ) to add two distances
passed as objects to the method & display the addition in the same method.
Test your program with 1-2 inputs, and it should find and display the correct
addition of two distances.
********** 9 **********
--- page 10 ---
02 Marks - class Distance & instance variables
02 Marks - Parameterised constructor
04 Marks – addDistanc() method
02 Marks – Main method, object creation, and call to methods
import java.util.*;
class Distance{
int f,i;
Distance(int f,int i){
this.f=f;
this.i=i;
}
void addDistances(Distance a, Distance b){
int in,ft=0;
in=a.i+b.i;
if(in>11){
ft=in/12;
in=in-ft*12;
}
ft+=a.f+b.f;
System.out.println("Distance is "+ft+"ft "+in+"in");
}
public static void main(String...args){
Distance d1 =new Distance(12,9);
Distance d2 =new Distance(9,8);
d1.addDistances(d1,d2);
}
}
CO-1 B   What are the different types of decision-making statements? Use decision-   [10]
BL-3   making statements in a program to explain it.
02 Marks – If Else
02 Marks – Nested if-else or ladder
02 Marks – Switch-case
04 Marks – Programming example
Decision-making statements in Java are fundamental constructs that allow
programmers to control the flow of their code based on certain conditions.
Decision-Making Statements
a) if statement
b) if-else statement
c) if-else-if ladder
d) Nested if statements
e) switch statement
********** 10 **********
--- page 11 ---
if...else statement
An if statement can be followed by an optional else statement, which
executes when the boolean expression is false.
Syntax
if(condition)
{
//code to be executed if the condition is true
}
else
{
//code to be executed if the condition is false
}
Nested if statement
You can use one if or else if statement inside another if or else
Syntax:
if statement(s).
if(condition)
{
//code to be executed
if(condition)
{
//code to be executed
}
}
Switch statement
A switch statement allows a variable to be tested for equality against a list
of values.
Syntax:
switch(expression)
{
case <value1>:
//code to be executed
break;
case <value2>:
//code to be executed
break;
default:
//code to be defaultly executed
}
********** 11 **********
--- page 12 ---
Example:
class Test {
public static void main(String[] args) {
int choice = 1;
int num = 5;
switch (choice) {
case 1:
if (num > 0) {
if (num % 2 == 0)
System.out.println("Positive Even");
else
System.out.println("Positive Odd");
} else {
System.out.println("Not Positive");
}
break;
default:
System.out.println("Invalid choice");
}
}
}
Q5
CO-1 A   Create a class called FibboTest that includes a method dispFibo(int n). This   [10]
method should accept a number and output the Nth Fibonacci number.
BL-3
Develop a   full object-oriented program (OOP) to   illustrate   this
functionality.
02 Mark –FibboTest
02 Marks – dispFibo function
04 Marks – Logic of finding Fibonacci number
02 Marks – main, object creation and method call
class FibboTest {
public int dispFibo(int n) {
if (n <= 0) return 0;
if (n == 1) return 1;
int a = 0, b = 1, c;
for (int i = 2; i <= n; i++) {
c = a + b;
a = b;
b = c;
}
return b;
}
public static void main(String[] args) {
System.out.println(new FibboTest().dispFibo(6));
}
}
********** 12 **********
--- page 13 ---
CO-4 B   What is an inner class? Explain the different types of inner classes. Write a   [10]
program demonstrating:
BL-3
→ Inner class
→ Local inner class
02 Marks – Inner Classes
03 Marks – Types of inner classes
05 Marks – Programming example
- An Inner Class is a class defined inside another class.
-   It helps in logically grouping related classes and improving
encapsulation.
Types of Inner Classes
• Inner Class: A class declared inside another class but outside any
method.
Ex.
class Out{
class In{
}
}
•   Static Nested Class: An inner class declared with the static
keyword.
Ex.
class Out{
static class In{
}
}
•   Method-Local Inner Class : A class declared inside a method of
another class.
Ex.
class Out{
void fun(){
class In{
}
}
}
• Anonymous Inner Class: An Anonymous Inner Class is a class
without a name that is declared and instantiated at the same time.It
is mainly used when a class is required only once for a short
implementation.
Ex.
abstractClass obj = new abstractClass() {
void methods() {
// code
}
};
Inner class:
class Outer {
private String msg = "Member Inner Class";
********** 13 **********
--- page 14 ---
class Inner {
void display() {
System.out.println(msg);
}
}
}
class TestMember {
public static void main(String[] args) {
Outer obj = new Outer();
Outer.Inner in = obj.new Inner();
in.display();
}
}
Local inner class:
class OuterMethod {
void display() {
class Inner {
void message() {
System.out.println("Method Local Inner Class");
}
}
Inner obj = new Inner();
obj.message();
}
}
class TestMethodLocal {
public static void main(String[] args) {
OuterMethod obj = new OuterMethod();
obj.display();
}
}
Q6
CO-5 A   Create a class Date with day, month and year as instance variables to   [10]
represent a Date. Write an object-oriented program that uses a generic class
BL-3
DateTest to store, read, and display a date using a user-defined Date class.
Use the constructor to store today's date, provide methods to read your date
of birth, and a display method to display the date.
02 Marks – Date Class
02 Marks – Generic Class Definition & constructor
02 Marks – Read Date in the generic class
02 Marks – Display Date in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class Date {
int day;
int month;
int year;
}
class DateTest<T> {
T d;
********** 14 **********
--- page 15 ---
DateTest(T d, int day, int month, int year) {
this.d = d;
Date temp = (Date) d;
temp.day = day;
temp.month = month;
temp.year = year;
}
void readDate() {
Scanner sc = new Scanner(System.in);
Date temp = (Date) d;
System.out.print("Enter Day: ");
temp.day = sc.nextInt();
System.out.print("Enter Month: ");
temp.month = sc.nextInt();
System.out.print("Enter Year: ");
temp.year = sc.nextInt();
}
void displayDate() {
Date temp = (Date) d;
System.out.println("Date: " + temp.day + "/" + temp.month + "/" +
temp.year);
}
}
class Main {
public static void main(String[] args) {
Date today = new Date();
DateTest<Date> obj = new DateTest<>(today, 28, 4, 2026);
System.out.println("Today's Date:");
obj.displayDate();
System.out.println("\nEnter your Date of Birth:");
obj.readDate();
System.out.println("Your Date of Birth:");
obj.displayDate();
}
}
CO-2 B   Define constructors and explain their purpose. Identify which constructor is   [10]
added automatically by the compiler. Describe the different types of
BL-3
constructors and provide a programming example.
02 Marks Constructor
01 Mark – constructor added by compiler
02 Marks Types of Constructors
05 Marks – Programming example
Constructor and its Purpose
- A constructor is a special method with the same name as the class that
initializes an object of that class.
-   It is called a constructor because it sets the values of the class’s data
members.
-   Properties/characteristics of a constructor
1. The constructor has the same name as the class.
2. The constructor does not have a return value (not even void).
********** 15 **********
--- page 16 ---
3. We cannot call the constructor directly. It is called automatically
when the object is created.
- Whenever an object is created, the constructor is invoked automatically.
- A constructor enables an object to initialise itself at the time of its
creation without the need to make a separate call to the instance
methods.
- The return type concept is not applicable to a constructor, even void. If
we accidentally declare a return type for the constructor, we won’t get
any compile-time or runtime error; the compiler simply treats it as a
normal method.
Types of Constructors:
Default Constructor
- A default constructor is an automatically created no-argument
constructor provided by the compiler if no constructors are explicitly
defined in the class.
- The programmer explicitly writes user-defined constructors and may
include custom initialization logic.
- The key difference is that default constructors rely on standard, default
values for object fields, while user-defined constructors give developers
control over initialization.
Parameterized Constructor
- A parameterised constructor accepts parameters to provide specific
values during object creation, allowing for more flexibility and control
over the object's initial state.
Programming Example:
class Student {
String name;
int age;
Student() {
name = "Sachin";
age = 45;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Tendulkar", 50);
a.display();
b.display();
********** 16 **********
--- page 17 ---
}
}
Q7
CO-3 A   Implement an object-oriented program using character-oriented streams.   [10]
The program should read a text file, convert all lowercase letters to
BL-3
uppercase, and write the modified content back to the file. Your program
should handle exceptions and ensure the proper closing of the file.
02 Marks - File Opening in Read mode & closing
02 Marks – File Opening in Write mode & closing
05 Marks – lowercase to uppercase & writing to file
01 Mark – Exception Handling
import java.io.*;
class LowerToUpper {
public static void main(String[] args) throws IOException {
FileReader fr = null;
FileWriter fw = null;
try{
fr = new FileReader("input.txt");
fw = new FileWriter("output.txt");
int ch;
while ((ch = fr.read()) != -1) {
if (Character.isLowerCase((char) ch)) {
ch = Character.toUpperCase((char) ch);
}
fw.write(ch);
}
System.out.println("Conversion completed.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
finally{
if(fr!=null) fr.close();
if(fw!=null) fw.close();
}
}
}
CO-1 B   Create an object-oriented program that determines if a number is even or   [05]
odd.
BL-3
02 Marks – Class & main method
03 Marks – Checking number is even or odd
class EvenOddChecker {
public void checkEvenOdd(int number) {
System.out.print(number + " ");
if (number % 2 == 0) {
System.out.println("is EVEN");
} else {
System.out.println("is ODD");
}
********** 17 **********
--- page 18 ---
}
public static void main(String[] args) {
EvenOddChecker obj = new EvenOddChecker();
obj.checkEvenOdd(80);
}
}
CO-2 C   Apply the concept of abstraction by explaining its meaning with an   [05]
appropriate example.
BL-3
02 Marks – Abstraction
03 Marks – Programming Example
-   Abstraction means hiding the implementation details
-   Abstraction = User knows what to do, not how it is done
- Ex: We operate the TV using a remote, but we do not know how it
works.
-   Abstraction means showing only the essential features to the user
and hiding the internal implementation details.
Programming example:
class AbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void dispMethod( ){
System.out.println(data);
}
}
class MainTest{
public static void main(String args[ ]){
AbstractionTest eat = new AbstractionTest( );
eat.setterMethod( );
eat.dispMethod( );
}
}
The user of the AbstractionTest class does not need to know how these
methods are implemented—only that setterMethod( ) and dispMethod( ) do
not accept any arguments and do not return any values. The user is unaware
of how data is stored or displayed. In the main method, an AbstractionTest
object is created, and the setter and getter methods are called, demonstrating
abstraction. Thus, implementation details are hidden, and only method
interfaces are exposed.
X----------------------------------------------------------------------------------------------------------------- X
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 00027e8c7617

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/BTech_CS_7055/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1   A.   What are primitive data types? Provide an appropriate programming   [05]
BL-3   example to illustrate the use of a primitive data type.
02 Marks – Primitive Data Types
03 Marks – programming example
Primitive Data Types: -
Data types specify the type of data stored in a variable.
The eight primitive data types.
S. N. Data Type   Example
1.   boolean   boolean status=true;
2.   char   char ch=’a’
3.   byte   byte b=87
4.   short   short s=512
5.   int   int i=45000
6.   long   Long l=20L
7.   float   float r=33.5f;
8.   double   double d=3.147
Programming Example:
class PrimitiveDemo {
public static void main(String[] args) {
char a = 'A';
byte b = 10;
********** 1 **********
--- page 2 ---
short c = 1000;
System.out.println(a);
System.out.println(b);
System.out.println(c);
int a1 = 50000;
float b1 = 5.5f;
double c1 = 99.99;
System.out.println(a1);
System.out.println(b1);
System.out.println(c1);
}
}
CO-2   B.   Create a class named ShapeArea to calculate the area of a circle and a square   [05]
BL-3   using method overloading. Define the main( ) method to create an object of
ShapeArea and invoke both methods.
02 Mark – Class Definition, Main Method & Object Creation in main
03 Marks –Code for Method Overloading
class ShapeArea {
static final float PI = 3.14f;
void area(float radius) {
System.out.println(PI * radius * radius)
}
void area(double side) {
System.out.println(side * side);
}
static public void main(String[] args) {
ShapeArea calc = new ShapeArea ();
calc.area(5.0);
calc.area(4.0);
}
}
CO-4   C.   Use your knowledge of abstract classes and interfaces to explain how they   [05]
BL-3   differ. Provide a suitable programming example.
03 Marks – At least 3-4 Differences
02 Marks – Programming example
Abstract Class   Interface
Definition   A class declared using   A reference type that
the abstract keyword that contains abstract methods
may contain abstract and and constants
concrete methods
Keyword   abstract class   interface
Used
Method Type Can have abstract and   Methods are abstract by
non-abstract methods   default (can also have
default/static methods)
********** 2 **********
--- page 3 ---
Variables   Can have instance   Variables are public static
variables   final by default
Access   Methods can be private,   Methods are public by
Modifiers   protected, public   default
Keyword for   extends   implements
Inheritance
Multiple   Not supported   Supported
Inheritance
Example   IS-A with shared   Contract-based design
Relationship   implementation
Example:Abstract Class
abstract class Animal {
abstract void sound();
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {
System.out.println("Dog barks");
}
}
Example: Interface
interface Animal {
void sound();
}
class Dog implements Animal {
public void sound() {
System.out.println("Dog barks");
}
}
CO-5   D.   What is a generic method? Use the idea of a generic method to write a   [05]
BL-3   suitable programming example.
02 Marks – Generic Method
03 Marks - Programming Example
- A generic method declares a type parameter in its method
signature.
-   It can be called with different types of arguments based on the type
of arguments passed to the generic method
- Programming Example:
- Code reuse and type safety are the advantages of the generic
class Test {
static <T> void genericDisplay(T element){
System.out.println(element);
********** 3 **********
--- page 4 ---
}
public static void main(String[] args) {
// Calling generic method with Integer argument
genericDisplay(110);   // passing Integer argument
genericDisplay("OOP and OOPL"); //passing String Argument
genericDisplay(110.0);   //Passing Double argument
}
}
Section- B
Q2
CO-2 A   What is polymorphism? How does static polymorphism differ from   [10]
dynamic polymorphism? Demonstrate it with a programming example.
BL-3
01 Marks Polymorphism
05 Marks – Difference between polymorphism
04 Marks – Programming example
Static Polymorphism   Dynamic Polymorphism
Also known as compile-time Also known as run-time
polymorphism   polymorphism
Achieved   by   method Achieved   by   method
overloading   overriding.
Uses the concept of compile- Uses   the concept   of
time binding(or early binding) . runtime binding (or late
Connecting a method call to the binding).
method body   is known as
binding.
Slower   than   Dynamic Faster   than   static
polymorphism   polymorphism.
To   implement   static To implement dynamic
polymorphism, inheritance is polymorphism,
not necessary   inheritance is necessary.
********** 4 **********
--- page 5 ---
Static Polymorphism :
class Student {
String name;
int age;
Student() {
name = "Unknown";
age = 0;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Rahul", 20);
a.display();
b.display();
}
}
Dynamic Polymorphism:
class Printer {
void print() {
System.out.println("Printing");
}
}
class InkjetPrinter extends Printer {
void print() {
System.out.println("Printing using Inkjet");
}
}
class LaserPrinter extends Printer {
void print() {
System.out.println("Printing using Laser");
}
}
public class Main {
public static void main(String[] args) {
********** 5 **********
--- page 6 ---
Printer p;
p = new InkjetPrinter();
p.print();
p = new LaserPrinter();
p.print();
}
}
CO-4 B   An electricity department needs a billing system that handles different   [10]
consumer types with varying rates. Design a program using object-oriented
BL-3
principles where ElectricityBill is an abstract class containing consumerId
(int), consumerName (String), and unitsConsumed (double) as data
members. Include a constructor to   initialize these fields and a
displayDetails( ) method to show the consumer's information. The abstract
method calculateBill( ) must be implemented by subclasses. Create
DomesticBill subclass with a ₹5 per unit rate and a CommercialBill subclass
with a ₹8 per unit rate. In the main method, demonstrate the bill calculation
and display for both consumer types. The total bill is calculated by
multiplying the units consumed by the unit rate.
03 Marks – Code for Abstract class & method
05 Marks - code for Subclasses & methods
02 Marks – Main & execution
abstract class ElectricityBill {
int consumerId;
String consumerName;
double unitsConsumed;
ElectricityBill(int cId, String cName, double unitsConsumed) {
this.consumerId = cId;
this.consumerName = cName;
this.unitsConsumed = unitsConsumed;
}
void displayDetails() {
System.out.println("ID: " + consumerId + ", Name: " +
consumerName + ", Units: " + unitsConsumed);
}
abstract double calculateBill();
}
class DomesticBill extends ElectricityBill {
DomesticBill(int id, String name, double units) {
super(id, name, units);
}
double calculateBill() {
return 5 * unitsConsumed;
}
}
class CommercialBill extends ElectricityBill {
CommercialBill(int id, String name, double units) {
super(id, name, units);
********** 6 **********
--- page 7 ---
}
double calculateBill() {
return 8 * unitsConsumed;
}
}
public class Main {
public static void main(String[] args) {
ElectricityBill domestic = new DomesticBill(101, "Ram", 150.0);
ElectricityBill commercial = new CommercialBill(201, "ABC Corp",
250.0);
domestic.displayDetails();
System.out.println("Bill: " + domestic.calculateBill() + "\n");
commercial.displayDetails();
System.out.println("Bill: " + commercial.calculateBill());
}
}
Q3
CO-3 A   Write an object-oriented program to demonstrate nested try–catch blocks.   [10]
The outer try block should handle an arithmetic exception for a division,
BL-3
while the inner try block should manage an array index out of bounds
exception when accessing index 5 of an array of size 3.
03 Marks – Code for Divide & Array of size 3.
02 Marks – main method
05 Marks – Appropriate code for Nested Try-Catch blocks
public class NestedTryDemo {
public static void main(String[] args) {
try {
int a = 10;
int b = 0;
try {
int arr[] = {1,2,3};
System.out.println(arr[4]);
}
catch(ArrayIndexOutOfBoundsException e) {
System.out.println("Array index error.");
}
int result = a / b;
}
catch(ArithmeticException e) {
System.out.println("Division by zero error.");
}
System.out.println("Program continues...");
}
}
CO-5 B   Demonstrate how the Composite design pattern works by implementing a   [10]
suitable program.
BL-3
05 Marks - Demonstration of Composite design pattern
05 Marks – Suitable programming example
Composite
********** 7 **********
--- page 8 ---
- Composite pattern is used where we need to treat a group of objects
in a similar way as a single object.
- Composite pattern composes objects in terms of a tree structure to
represent the part as well as the whole hierarchy.
-   This type of design pattern comes under a structural pattern as this
pattern creates a tree structure of a group of objects.
- Allows you to treat individual objects (leaf) and groups of objects
(composite) uniformly
-   Organizes objects into a tree structure (hierarchy)
Program :
import java.util.*;
class CompositePatternDemo {
public static void main(String ... args) {
Employee CEO = new Employee("Rohit","CEO", 30000);
Employee headSales = new Employee("Virat","Head Sales", 20000);
Employee headMarketing = new Employee("Surya","Head
Marketing", 20000);
Employee clerk1 = new Employee("Japrit","Marketing", 10000);
Employee clerk2 = new Employee("Hardik","Marketing", 10000);
Employee salesExecutive1 = new Employee("Abhishek","Sales",
10000);
Employee salesExecutive2 = new Employee("Ishan","Sales", 10000);
CEO.add(headSales);
********** 8 **********
--- page 9 ---
CEO.add(headMarketing);
headSales.add(salesExecutive1);
headSales.add(salesExecutive2);
headMarketing.add(clerk1);
headMarketing.add(clerk2);
System.out.println(CEO);
for (Employee headEmployee : CEO.getSubordinates()) {
System.out.println(headEmployee);
for (Employee employee : headEmployee.getSubordinates()) {
System.out.println(employee);
}
}
}
}
class Employee {
private String name;
private String dept;
private int salary;
private List<Employee> subordinates;
public Employee(String name,String dept, int sal) {
this.name = name;
this.dept = dept;
this.salary = sal;
subordinates = new ArrayList<Employee>();
}
public void add(Employee e) {
subordinates.add(e);
}
public void remove(Employee e) {
subordinates.remove(e);
}
public List<Employee> getSubordinates(){
return subordinates;
}
public String toString(){
return ("Employee :--> Name : " + name + ", dept : " + dept + ",
salary :" + salary+" <--");
}
}
Q4
CO-2 A   Implement an object-oriented program to define a class Distance with feet   [10]
and inches as instance variables and assign beginning values using a
BL-3
parameterized constructor. Define addDistances( ) to add two distances
passed as objects to the method & display the addition in the same method.
Test your program with 1-2 inputs, and it should find and display the correct
addition of two distances.
********** 9 **********
--- page 10 ---
02 Marks - class Distance & instance variables
02 Marks - Parameterised constructor
04 Marks – addDistanc() method
02 Marks – Main method, object creation, and call to methods
import java.util.*;
class Distance{
int f,i;
Distance(int f,int i){
this.f=f;
this.i=i;
}
void addDistances(Distance a, Distance b){
int in,ft=0;
in=a.i+b.i;
if(in>11){
ft=in/12;
in=in-ft*12;
}
ft+=a.f+b.f;
System.out.println("Distance is "+ft+"ft "+in+"in");
}
public static void main(String...args){
Distance d1 =new Distance(12,9);
Distance d2 =new Distance(9,8);
d1.addDistances(d1,d2);
}
}
CO-1 B   What are the different types of decision-making statements? Use decision-   [10]
BL-3   making statements in a program to explain it.
02 Marks – If Else
02 Marks – Nested if-else or ladder
02 Marks – Switch-case
04 Marks – Programming example
Decision-making statements in Java are fundamental constructs that allow
programmers to control the flow of their code based on certain conditions.
Decision-Making Statements
a) if statement
b) if-else statement
c) if-else-if ladder
d) Nested if statements
e) switch statement
********** 10 **********
--- page 11 ---
if...else statement
An if statement can be followed by an optional else statement, which
executes when the boolean expression is false.
Syntax
if(condition)
{
//code to be executed if the condition is true
}
else
{
//code to be executed if the condition is false
}
Nested if statement
You can use one if or else if statement inside another if or else
Syntax:
if statement(s).
if(condition)
{
//code to be executed
if(condition)
{
//code to be executed
}
}
Switch statement
A switch statement allows a variable to be tested for equality against a list
of values.
Syntax:
switch(expression)
{
case <value1>:
//code to be executed
break;
case <value2>:
//code to be executed
break;
default:
//code to be defaultly executed
}
********** 11 **********
--- page 12 ---
Example:
class Test {
public static void main(String[] args) {
int choice = 1;
int num = 5;
switch (choice) {
case 1:
if (num > 0) {
if (num % 2 == 0)
System.out.println("Positive Even");
else
System.out.println("Positive Odd");
} else {
System.out.println("Not Positive");
}
break;
default:
System.out.println("Invalid choice");
}
}
}
Q5
CO-1 A   Create a class called FibboTest that includes a method dispFibo(int n). This   [10]
method should accept a number and output the Nth Fibonacci number.
BL-3
Develop a   full object-oriented program (OOP) to   illustrate   this
functionality.
02 Mark –FibboTest
02 Marks – dispFibo function
04 Marks – Logic of finding Fibonacci number
02 Marks – main, object creation and method call
class FibboTest {
public int dispFibo(int n) {
if (n <= 0) return 0;
if (n == 1) return 1;
int a = 0, b = 1, c;
for (int i = 2; i <= n; i++) {
c = a + b;
a = b;
b = c;
}
return b;
}
public static void main(String[] args) {
System.out.println(new FibboTest().dispFibo(6));
}
}
********** 12 **********
--- page 13 ---
CO-4 B   What is an inner class? Explain the different types of inner classes. Write a   [10]
program demonstrating:
BL-3
→ Inner class
→ Local inner class
02 Marks – Inner Classes
03 Marks – Types of inner classes
05 Marks – Programming example
- An Inner Class is a class defined inside another class.
-   It helps in logically grouping related classes and improving
encapsulation.
Types of Inner Classes
• Inner Class: A class declared inside another class but outside any
method.
Ex.
class Out{
class In{
}
}
•   Static Nested Class: An inner class declared with the static
keyword.
Ex.
class Out{
static class In{
}
}
•   Method-Local Inner Class : A class declared inside a method of
another class.
Ex.
class Out{
void fun(){
class In{
}
}
}
• Anonymous Inner Class: An Anonymous Inner Class is a class
without a name that is declared and instantiated at the same time.It
is mainly used when a class is required only once for a short
implementation.
Ex.
abstractClass obj = new abstractClass() {
void methods() {
// code
}
};
Inner class:
class Outer {
private String msg = "Member Inner Class";
********** 13 **********
--- page 14 ---
class Inner {
void display() {
System.out.println(msg);
}
}
}
class TestMember {
public static void main(String[] args) {
Outer obj = new Outer();
Outer.Inner in = obj.new Inner();
in.display();
}
}
Local inner class:
class OuterMethod {
void display() {
class Inner {
void message() {
System.out.println("Method Local Inner Class");
}
}
Inner obj = new Inner();
obj.message();
}
}
class TestMethodLocal {
public static void main(String[] args) {
OuterMethod obj = new OuterMethod();
obj.display();
}
}
Q6
CO-5 A   Create a class Date with day, month and year as instance variables to   [10]
represent a Date. Write an object-oriented program that uses a generic class
BL-3
DateTest to store, read, and display a date using a user-defined Date class.
Use the constructor to store today's date, provide methods to read your date
of birth, and a display method to display the date.
02 Marks – Date Class
02 Marks – Generic Class Definition & constructor
02 Marks – Read Date in the generic class
02 Marks – Display Date in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class Date {
int day;
int month;
int year;
}
class DateTest<T> {
T d;
********** 14 **********
--- page 15 ---
DateTest(T d, int day, int month, int year) {
this.d = d;
Date temp = (Date) d;
temp.day = day;
temp.month = month;
temp.year = year;
}
void readDate() {
Scanner sc = new Scanner(System.in);
Date temp = (Date) d;
System.out.print("Enter Day: ");
temp.day = sc.nextInt();
System.out.print("Enter Month: ");
temp.month = sc.nextInt();
System.out.print("Enter Year: ");
temp.year = sc.nextInt();
}
void displayDate() {
Date temp = (Date) d;
System.out.println("Date: " + temp.day + "/" + temp.month + "/" +
temp.year);
}
}
class Main {
public static void main(String[] args) {
Date today = new Date();
DateTest<Date> obj = new DateTest<>(today, 28, 4, 2026);
System.out.println("Today's Date:");
obj.displayDate();
System.out.println("\nEnter your Date of Birth:");
obj.readDate();
System.out.println("Your Date of Birth:");
obj.displayDate();
}
}
CO-2 B   Define constructors and explain their purpose. Identify which constructor is   [10]
added automatically by the compiler. Describe the different types of
BL-3
constructors and provide a programming example.
02 Marks Constructor
01 Mark – constructor added by compiler
02 Marks Types of Constructors
05 Marks – Programming example
Constructor and its Purpose
- A constructor is a special method with the same name as the class that
initializes an object of that class.
-   It is called a constructor because it sets the values of the class’s data
members.
-   Properties/characteristics of a constructor
1. The constructor has the same name as the class.
2. The constructor does not have a return value (not even void).
********** 15 **********
--- page 16 ---
3. We cannot call the constructor directly. It is called automatically
when the object is created.
- Whenever an object is created, the constructor is invoked automatically.
- A constructor enables an object to initialise itself at the time of its
creation without the need to make a separate call to the instance
methods.
- The return type concept is not applicable to a constructor, even void. If
we accidentally declare a return type for the constructor, we won’t get
any compile-time or runtime error; the compiler simply treats it as a
normal method.
Types of Constructors:
Default Constructor
- A default constructor is an automatically created no-argument
constructor provided by the compiler if no constructors are explicitly
defined in the class.
- The programmer explicitly writes user-defined constructors and may
include custom initialization logic.
- The key difference is that default constructors rely on standard, default
values for object fields, while user-defined constructors give developers
control over initialization.
Parameterized Constructor
- A parameterised constructor accepts parameters to provide specific
values during object creation, allowing for more flexibility and control
over the object's initial state.
Programming Example:
class Student {
String name;
int age;
Student() {
name = "Sachin";
age = 45;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Tendulkar", 50);
a.display();
b.display();
********** 16 **********
--- page 17 ---
}
}
Q7
CO-3 A   Implement an object-oriented program using character-oriented streams.   [10]
The program should read a text file, convert all lowercase letters to
BL-3
uppercase, and write the modified content back to the file. Your program
should handle exceptions and ensure the proper closing of the file.
02 Marks - File Opening in Read mode & closing
02 Marks – File Opening in Write mode & closing
05 Marks – lowercase to uppercase & writing to file
01 Mark – Exception Handling
import java.io.*;
class LowerToUpper {
public static void main(String[] args) throws IOException {
FileReader fr = null;
FileWriter fw = null;
try{
fr = new FileReader("input.txt");
fw = new FileWriter("output.txt");
int ch;
while ((ch = fr.read()) != -1) {
if (Character.isLowerCase((char) ch)) {
ch = Character.toUpperCase((char) ch);
}
fw.write(ch);
}
System.out.println("Conversion completed.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
finally{
if(fr!=null) fr.close();
if(fw!=null) fw.close();
}
}
}
CO-1 B   Create an object-oriented program that determines if a number is even or   [05]
odd.
BL-3
02 Marks – Class & main method
03 Marks – Checking number is even or odd
class EvenOddChecker {
public void checkEvenOdd(int number) {
System.out.print(number + " ");
if (number % 2 == 0) {
System.out.println("is EVEN");
} else {
System.out.println("is ODD");
}
********** 17 **********
--- page 18 ---
}
public static void main(String[] args) {
EvenOddChecker obj = new EvenOddChecker();
obj.checkEvenOdd(80);
}
}
CO-2 C   Apply the concept of abstraction by explaining its meaning with an   [05]
appropriate example.
BL-3
02 Marks – Abstraction
03 Marks – Programming Example
-   Abstraction means hiding the implementation details
-   Abstraction = User knows what to do, not how it is done
- Ex: We operate the TV using a remote, but we do not know how it
works.
-   Abstraction means showing only the essential features to the user
and hiding the internal implementation details.
Programming example:
class AbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void dispMethod( ){
System.out.println(data);
}
}
class MainTest{
public static void main(String args[ ]){
AbstractionTest eat = new AbstractionTest( );
eat.setterMethod( );
eat.dispMethod( );
}
}
The user of the AbstractionTest class does not need to know how these
methods are implemented—only that setterMethod( ) and dispMethod( ) do
not accept any arguments and do not return any values. The user is unaware
of how data is stored or displayed. In the main method, an AbstractionTest
object is created, and the setter and getter methods are called, demonstrating
abstraction. Thus, implementation details are hidden, and only method
interfaces are exposed.
X----------------------------------------------------------------------------------------------------------------- X
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 87da8ec5c5aa

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MBATech_Computer_7047/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1   A.   What are primitive data types? Provide an appropriate programming   [05]
BL-3   example to illustrate the use of a primitive data type.
02 Marks – Primitive Data Types
03 Marks – programming example
Primitive Data Types: -
Data types specify the type of data stored in a variable.
The eight primitive data types.
S. N. Data Type   Example
1.   boolean   boolean status=true;
2.   char   char ch=’a’
3.   byte   byte b=87
4.   short   short s=512
5.   int   int i=45000
6.   long   Long l=20L
7.   float   float r=33.5f;
8.   double   double d=3.147
Programming Example:
class PrimitiveDemo {
public static void main(String[] args) {
char a = 'A';
byte b = 10;
********** 1 **********
--- page 2 ---
short c = 1000;
System.out.println(a);
System.out.println(b);
System.out.println(c);
int a1 = 50000;
float b1 = 5.5f;
double c1 = 99.99;
System.out.println(a1);
System.out.println(b1);
System.out.println(c1);
}
}
CO-2   B.   Create a class named ShapeArea to calculate the area of a circle and a square   [05]
BL-3   using method overloading. Define the main( ) method to create an object of
ShapeArea and invoke both methods.
02 Mark – Class Definition, Main Method & Object Creation in main
03 Marks –Code for Method Overloading
class ShapeArea {
static final float PI = 3.14f;
void area(float radius) {
System.out.println(PI * radius * radius)
}
void area(double side) {
System.out.println(side * side);
}
static public void main(String[] args) {
ShapeArea calc = new ShapeArea ();
calc.area(5.0);
calc.area(4.0);
}
}
CO-4   C.   Use your knowledge of abstract classes and interfaces to explain how they   [05]
BL-3   differ. Provide a suitable programming example.
03 Marks – At least 3-4 Differences
02 Marks – Programming example
Abstract Class   Interface
Definition   A class declared using   A reference type that
the abstract keyword that contains abstract methods
may contain abstract and and constants
concrete methods
Keyword   abstract class   interface
Used
Method Type Can have abstract and   Methods are abstract by
non-abstract methods   default (can also have
default/static methods)
********** 2 **********
--- page 3 ---
Variables   Can have instance   Variables are public static
variables   final by default
Access   Methods can be private,   Methods are public by
Modifiers   protected, public   default
Keyword for   extends   implements
Inheritance
Multiple   Not supported   Supported
Inheritance
Example   IS-A with shared   Contract-based design
Relationship   implementation
Example:Abstract Class
abstract class Animal {
abstract void sound();
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {
System.out.println("Dog barks");
}
}
Example: Interface
interface Animal {
void sound();
}
class Dog implements Animal {
public void sound() {
System.out.println("Dog barks");
}
}
CO-5   D.   What is a generic method? Use the idea of a generic method to write a   [05]
BL-3   suitable programming example.
02 Marks – Generic Method
03 Marks - Programming Example
- A generic method declares a type parameter in its method
signature.
-   It can be called with different types of arguments based on the type
of arguments passed to the generic method
- Programming Example:
- Code reuse and type safety are the advantages of the generic
class Test {
static <T> void genericDisplay(T element){
System.out.println(element);
********** 3 **********
--- page 4 ---
}
public static void main(String[] args) {
// Calling generic method with Integer argument
genericDisplay(110);   // passing Integer argument
genericDisplay("OOP and OOPL"); //passing String Argument
genericDisplay(110.0);   //Passing Double argument
}
}
Section- B
Q2
CO-2 A   What is polymorphism? How does static polymorphism differ from   [10]
dynamic polymorphism? Demonstrate it with a programming example.
BL-3
01 Marks Polymorphism
05 Marks – Difference between polymorphism
04 Marks – Programming example
Static Polymorphism   Dynamic Polymorphism
Also known as compile-time Also known as run-time
polymorphism   polymorphism
Achieved   by   method Achieved   by   method
overloading   overriding.
Uses the concept of compile- Uses   the concept   of
time binding(or early binding) . runtime binding (or late
Connecting a method call to the binding).
method body   is known as
binding.
Slower   than   Dynamic Faster   than   static
polymorphism   polymorphism.
To   implement   static To implement dynamic
polymorphism, inheritance is polymorphism,
not necessary   inheritance is necessary.
********** 4 **********
--- page 5 ---
Static Polymorphism :
class Student {
String name;
int age;
Student() {
name = "Unknown";
age = 0;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Rahul", 20);
a.display();
b.display();
}
}
Dynamic Polymorphism:
class Printer {
void print() {
System.out.println("Printing");
}
}
class InkjetPrinter extends Printer {
void print() {
System.out.println("Printing using Inkjet");
}
}
class LaserPrinter extends Printer {
void print() {
System.out.println("Printing using Laser");
}
}
public class Main {
public static void main(String[] args) {
********** 5 **********
--- page 6 ---
Printer p;
p = new InkjetPrinter();
p.print();
p = new LaserPrinter();
p.print();
}
}
CO-4 B   An electricity department needs a billing system that handles different   [10]
consumer types with varying rates. Design a program using object-oriented
BL-3
principles where ElectricityBill is an abstract class containing consumerId
(int), consumerName (String), and unitsConsumed (double) as data
members. Include a constructor to   initialize these fields and a
displayDetails( ) method to show the consumer's information. The abstract
method calculateBill( ) must be implemented by subclasses. Create
DomesticBill subclass with a ₹5 per unit rate and a CommercialBill subclass
with a ₹8 per unit rate. In the main method, demonstrate the bill calculation
and display for both consumer types. The total bill is calculated by
multiplying the units consumed by the unit rate.
03 Marks – Code for Abstract class & method
05 Marks - code for Subclasses & methods
02 Marks – Main & execution
abstract class ElectricityBill {
int consumerId;
String consumerName;
double unitsConsumed;
ElectricityBill(int cId, String cName, double unitsConsumed) {
this.consumerId = cId;
this.consumerName = cName;
this.unitsConsumed = unitsConsumed;
}
void displayDetails() {
System.out.println("ID: " + consumerId + ", Name: " +
consumerName + ", Units: " + unitsConsumed);
}
abstract double calculateBill();
}
class DomesticBill extends ElectricityBill {
DomesticBill(int id, String name, double units) {
super(id, name, units);
}
double calculateBill() {
return 5 * unitsConsumed;
}
}
class CommercialBill extends ElectricityBill {
CommercialBill(int id, String name, double units) {
super(id, name, units);
********** 6 **********
--- page 7 ---
}
double calculateBill() {
return 8 * unitsConsumed;
}
}
public class Main {
public static void main(String[] args) {
ElectricityBill domestic = new DomesticBill(101, "Ram", 150.0);
ElectricityBill commercial = new CommercialBill(201, "ABC Corp",
250.0);
domestic.displayDetails();
System.out.println("Bill: " + domestic.calculateBill() + "\n");
commercial.displayDetails();
System.out.println("Bill: " + commercial.calculateBill());
}
}
Q3
CO-3 A   Write an object-oriented program to demonstrate nested try–catch blocks.   [10]
The outer try block should handle an arithmetic exception for a division,
BL-3
while the inner try block should manage an array index out of bounds
exception when accessing index 5 of an array of size 3.
03 Marks – Code for Divide & Array of size 3.
02 Marks – main method
05 Marks – Appropriate code for Nested Try-Catch blocks
public class NestedTryDemo {
public static void main(String[] args) {
try {
int a = 10;
int b = 0;
try {
int arr[] = {1,2,3};
System.out.println(arr[4]);
}
catch(ArrayIndexOutOfBoundsException e) {
System.out.println("Array index error.");
}
int result = a / b;
}
catch(ArithmeticException e) {
System.out.println("Division by zero error.");
}
System.out.println("Program continues...");
}
}
CO-5 B   Demonstrate how the Composite design pattern works by implementing a   [10]
suitable program.
BL-3
05 Marks - Demonstration of Composite design pattern
05 Marks – Suitable programming example
Composite
********** 7 **********
--- page 8 ---
- Composite pattern is used where we need to treat a group of objects
in a similar way as a single object.
- Composite pattern composes objects in terms of a tree structure to
represent the part as well as the whole hierarchy.
-   This type of design pattern comes under a structural pattern as this
pattern creates a tree structure of a group of objects.
- Allows you to treat individual objects (leaf) and groups of objects
(composite) uniformly
-   Organizes objects into a tree structure (hierarchy)
Program :
import java.util.*;
class CompositePatternDemo {
public static void main(String ... args) {
Employee CEO = new Employee("Rohit","CEO", 30000);
Employee headSales = new Employee("Virat","Head Sales", 20000);
Employee headMarketing = new Employee("Surya","Head
Marketing", 20000);
Employee clerk1 = new Employee("Japrit","Marketing", 10000);
Employee clerk2 = new Employee("Hardik","Marketing", 10000);
Employee salesExecutive1 = new Employee("Abhishek","Sales",
10000);
Employee salesExecutive2 = new Employee("Ishan","Sales", 10000);
CEO.add(headSales);
********** 8 **********
--- page 9 ---
CEO.add(headMarketing);
headSales.add(salesExecutive1);
headSales.add(salesExecutive2);
headMarketing.add(clerk1);
headMarketing.add(clerk2);
System.out.println(CEO);
for (Employee headEmployee : CEO.getSubordinates()) {
System.out.println(headEmployee);
for (Employee employee : headEmployee.getSubordinates()) {
System.out.println(employee);
}
}
}
}
class Employee {
private String name;
private String dept;
private int salary;
private List<Employee> subordinates;
public Employee(String name,String dept, int sal) {
this.name = name;
this.dept = dept;
this.salary = sal;
subordinates = new ArrayList<Employee>();
}
public void add(Employee e) {
subordinates.add(e);
}
public void remove(Employee e) {
subordinates.remove(e);
}
public List<Employee> getSubordinates(){
return subordinates;
}
public String toString(){
return ("Employee :--> Name : " + name + ", dept : " + dept + ",
salary :" + salary+" <--");
}
}
Q4
CO-2 A   Implement an object-oriented program to define a class Distance with feet   [10]
and inches as instance variables and assign beginning values using a
BL-3
parameterized constructor. Define addDistances( ) to add two distances
passed as objects to the method & display the addition in the same method.
Test your program with 1-2 inputs, and it should find and display the correct
addition of two distances.
********** 9 **********
--- page 10 ---
02 Marks - class Distance & instance variables
02 Marks - Parameterised constructor
04 Marks – addDistanc() method
02 Marks – Main method, object creation, and call to methods
import java.util.*;
class Distance{
int f,i;
Distance(int f,int i){
this.f=f;
this.i=i;
}
void addDistances(Distance a, Distance b){
int in,ft=0;
in=a.i+b.i;
if(in>11){
ft=in/12;
in=in-ft*12;
}
ft+=a.f+b.f;
System.out.println("Distance is "+ft+"ft "+in+"in");
}
public static void main(String...args){
Distance d1 =new Distance(12,9);
Distance d2 =new Distance(9,8);
d1.addDistances(d1,d2);
}
}
CO-1 B   What are the different types of decision-making statements? Use decision-   [10]
BL-3   making statements in a program to explain it.
02 Marks – If Else
02 Marks – Nested if-else or ladder
02 Marks – Switch-case
04 Marks – Programming example
Decision-making statements in Java are fundamental constructs that allow
programmers to control the flow of their code based on certain conditions.
Decision-Making Statements
a) if statement
b) if-else statement
c) if-else-if ladder
d) Nested if statements
e) switch statement
********** 10 **********
--- page 11 ---
if...else statement
An if statement can be followed by an optional else statement, which
executes when the boolean expression is false.
Syntax
if(condition)
{
//code to be executed if the condition is true
}
else
{
//code to be executed if the condition is false
}
Nested if statement
You can use one if or else if statement inside another if or else
Syntax:
if statement(s).
if(condition)
{
//code to be executed
if(condition)
{
//code to be executed
}
}
Switch statement
A switch statement allows a variable to be tested for equality against a list
of values.
Syntax:
switch(expression)
{
case <value1>:
//code to be executed
break;
case <value2>:
//code to be executed
break;
default:
//code to be defaultly executed
}
********** 11 **********
--- page 12 ---
Example:
class Test {
public static void main(String[] args) {
int choice = 1;
int num = 5;
switch (choice) {
case 1:
if (num > 0) {
if (num % 2 == 0)
System.out.println("Positive Even");
else
System.out.println("Positive Odd");
} else {
System.out.println("Not Positive");
}
break;
default:
System.out.println("Invalid choice");
}
}
}
Q5
CO-1 A   Create a class called FibboTest that includes a method dispFibo(int n). This   [10]
method should accept a number and output the Nth Fibonacci number.
BL-3
Develop a   full object-oriented program (OOP) to   illustrate   this
functionality.
02 Mark –FibboTest
02 Marks – dispFibo function
04 Marks – Logic of finding Fibonacci number
02 Marks – main, object creation and method call
class FibboTest {
public int dispFibo(int n) {
if (n <= 0) return 0;
if (n == 1) return 1;
int a = 0, b = 1, c;
for (int i = 2; i <= n; i++) {
c = a + b;
a = b;
b = c;
}
return b;
}
public static void main(String[] args) {
System.out.println(new FibboTest().dispFibo(6));
}
}
********** 12 **********
--- page 13 ---
CO-4 B   What is an inner class? Explain the different types of inner classes. Write a   [10]
program demonstrating:
BL-3
→ Inner class
→ Local inner class
02 Marks – Inner Classes
03 Marks – Types of inner classes
05 Marks – Programming example
- An Inner Class is a class defined inside another class.
-   It helps in logically grouping related classes and improving
encapsulation.
Types of Inner Classes
• Inner Class: A class declared inside another class but outside any
method.
Ex.
class Out{
class In{
}
}
•   Static Nested Class: An inner class declared with the static
keyword.
Ex.
class Out{
static class In{
}
}
•   Method-Local Inner Class : A class declared inside a method of
another class.
Ex.
class Out{
void fun(){
class In{
}
}
}
• Anonymous Inner Class: An Anonymous Inner Class is a class
without a name that is declared and instantiated at the same time.It
is mainly used when a class is required only once for a short
implementation.
Ex.
abstractClass obj = new abstractClass() {
void methods() {
// code
}
};
Inner class:
class Outer {
private String msg = "Member Inner Class";
********** 13 **********
--- page 14 ---
class Inner {
void display() {
System.out.println(msg);
}
}
}
class TestMember {
public static void main(String[] args) {
Outer obj = new Outer();
Outer.Inner in = obj.new Inner();
in.display();
}
}
Local inner class:
class OuterMethod {
void display() {
class Inner {
void message() {
System.out.println("Method Local Inner Class");
}
}
Inner obj = new Inner();
obj.message();
}
}
class TestMethodLocal {
public static void main(String[] args) {
OuterMethod obj = new OuterMethod();
obj.display();
}
}
Q6
CO-5 A   Create a class Date with day, month and year as instance variables to   [10]
represent a Date. Write an object-oriented program that uses a generic class
BL-3
DateTest to store, read, and display a date using a user-defined Date class.
Use the constructor to store today's date, provide methods to read your date
of birth, and a display method to display the date.
02 Marks – Date Class
02 Marks – Generic Class Definition & constructor
02 Marks – Read Date in the generic class
02 Marks – Display Date in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class Date {
int day;
int month;
int year;
}
class DateTest<T> {
T d;
********** 14 **********
--- page 15 ---
DateTest(T d, int day, int month, int year) {
this.d = d;
Date temp = (Date) d;
temp.day = day;
temp.month = month;
temp.year = year;
}
void readDate() {
Scanner sc = new Scanner(System.in);
Date temp = (Date) d;
System.out.print("Enter Day: ");
temp.day = sc.nextInt();
System.out.print("Enter Month: ");
temp.month = sc.nextInt();
System.out.print("Enter Year: ");
temp.year = sc.nextInt();
}
void displayDate() {
Date temp = (Date) d;
System.out.println("Date: " + temp.day + "/" + temp.month + "/" +
temp.year);
}
}
class Main {
public static void main(String[] args) {
Date today = new Date();
DateTest<Date> obj = new DateTest<>(today, 28, 4, 2026);
System.out.println("Today's Date:");
obj.displayDate();
System.out.println("\nEnter your Date of Birth:");
obj.readDate();
System.out.println("Your Date of Birth:");
obj.displayDate();
}
}
CO-2 B   Define constructors and explain their purpose. Identify which constructor is   [10]
added automatically by the compiler. Describe the different types of
BL-3
constructors and provide a programming example.
02 Marks Constructor
01 Mark – constructor added by compiler
02 Marks Types of Constructors
05 Marks – Programming example
Constructor and its Purpose
- A constructor is a special method with the same name as the class that
initializes an object of that class.
-   It is called a constructor because it sets the values of the class’s data
members.
-   Properties/characteristics of a constructor
1. The constructor has the same name as the class.
2. The constructor does not have a return value (not even void).
********** 15 **********
--- page 16 ---
3. We cannot call the constructor directly. It is called automatically
when the object is created.
- Whenever an object is created, the constructor is invoked automatically.
- A constructor enables an object to initialise itself at the time of its
creation without the need to make a separate call to the instance
methods.
- The return type concept is not applicable to a constructor, even void. If
we accidentally declare a return type for the constructor, we won’t get
any compile-time or runtime error; the compiler simply treats it as a
normal method.
Types of Constructors:
Default Constructor
- A default constructor is an automatically created no-argument
constructor provided by the compiler if no constructors are explicitly
defined in the class.
- The programmer explicitly writes user-defined constructors and may
include custom initialization logic.
- The key difference is that default constructors rely on standard, default
values for object fields, while user-defined constructors give developers
control over initialization.
Parameterized Constructor
- A parameterised constructor accepts parameters to provide specific
values during object creation, allowing for more flexibility and control
over the object's initial state.
Programming Example:
class Student {
String name;
int age;
Student() {
name = "Sachin";
age = 45;
}
Student(String n, int a) {
name = n;
age = a;
}
void display() {
System.out.println("Name: " + name + ", Age: " + age);
}
}
public class Main {
public static void main(String[] args) {
Student a = new Student();
Student b = new Student("Tendulkar", 50);
a.display();
b.display();
********** 16 **********
--- page 17 ---
}
}
Q7
CO-3 A   Implement an object-oriented program using character-oriented streams.   [10]
The program should read a text file, convert all lowercase letters to
BL-3
uppercase, and write the modified content back to the file. Your program
should handle exceptions and ensure the proper closing of the file.
02 Marks - File Opening in Read mode & closing
02 Marks – File Opening in Write mode & closing
05 Marks – lowercase to uppercase & writing to file
01 Mark – Exception Handling
import java.io.*;
class LowerToUpper {
public static void main(String[] args) throws IOException {
FileReader fr = null;
FileWriter fw = null;
try{
fr = new FileReader("input.txt");
fw = new FileWriter("output.txt");
int ch;
while ((ch = fr.read()) != -1) {
if (Character.isLowerCase((char) ch)) {
ch = Character.toUpperCase((char) ch);
}
fw.write(ch);
}
System.out.println("Conversion completed.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
finally{
if(fr!=null) fr.close();
if(fw!=null) fw.close();
}
}
}
CO-1 B   Create an object-oriented program that determines if a number is even or   [05]
odd.
BL-3
02 Marks – Class & main method
03 Marks – Checking number is even or odd
class EvenOddChecker {
public void checkEvenOdd(int number) {
System.out.print(number + " ");
if (number % 2 == 0) {
System.out.println("is EVEN");
} else {
System.out.println("is ODD");
}
********** 17 **********
--- page 18 ---
}
public static void main(String[] args) {
EvenOddChecker obj = new EvenOddChecker();
obj.checkEvenOdd(80);
}
}
CO-2 C   Apply the concept of abstraction by explaining its meaning with an   [05]
appropriate example.
BL-3
02 Marks – Abstraction
03 Marks – Programming Example
-   Abstraction means hiding the implementation details
-   Abstraction = User knows what to do, not how it is done
- Ex: We operate the TV using a remote, but we do not know how it
works.
-   Abstraction means showing only the essential features to the user
and hiding the internal implementation details.
Programming example:
class AbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void dispMethod( ){
System.out.println(data);
}
}
class MainTest{
public static void main(String args[ ]){
AbstractionTest eat = new AbstractionTest( );
eat.setterMethod( );
eat.dispMethod( );
}
}
The user of the AbstractionTest class does not need to know how these
methods are implemented—only that setterMethod( ) and dispMethod( ) do
not accept any arguments and do not return any values. The user is unaware
of how data is stored or displayed. In the main method, an AbstractionTest
object is created, and the setter and getter methods are called, demonstrating
abstraction. Thus, implementation details are hidden, and only method
interfaces are exposed.
X----------------------------------------------------------------------------------------------------------------- X
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 955caf338b45

- Departments: Computer Science
- Programmes: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE) - 7055
- Source: `00_Original_Downloads/2025/Semester II/75268__Re-Exam.zip :: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE) - 7055/OBJECT ORIENTED PROGRAMMING/ANS_Re-Exam_OBJECT ORIENTED PROGRAMMING(702CO0C075)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1 A.   What are the key paradigms of object-oriented programming? List and   [05]
BL-3   demonstrate each one with an example.
02 Marks – Key Paradigms
03 Marks – Description with programming example
If any programming language supports Encapsulation, Polymorphism,
Inheritance and Abstraction etc. is called as OOP
Encapsulation: -
- Binding/Wrapping of data to its related functions into a single unit
-   In OOP, we can achieve encapsulation by creating classes and
objects.
Abstraction: -
-   It hides the implementation details.
- A Class can decide which member will be visible to the outside of
the class
Polymorphism (many forms):-
-   Defining multiple functions with the same name
- These functions with same name will show different behaviours
- There are two types of polymorphism → Static(Overloading) &
Dynamic(Overriding)
Inheritance:-
-   Inherence is reusability (of encapsulation).
********** 1 **********
--- page 2 ---
-   Child/Derived/ Sub Class inherits the properties of Parent/Base/
Super Class.
Example:
class Person {
private String name;
void work() {
System.out.println("Person works");
}
}  Encapsulation (name + work)
class Teacher extends Person { Inheritance
Teacher(String name) {
this.name=name;
}
void work() {  Dynamic Polymorphism
System.out.println(name + " teaches");
}
}
Class Test{
public static void main(String[] args) {
Teacher t = new Teacher("Paavan");
t.work();  Abstraction
}
}
CO-2   B.   Consider a product class with only one data member, discount. Apply the   [05]
BL-3   concept of constructor overloading to write an object-oriented program,
such that one constructor initializes the discount to 5 and another
parameterized constructor initializes it to 10 by accepting the discount as a
parameter. Create two objects by invoking both the constructors and
displaying the discount.
03 Marks – Code for Constructor Overloading
02 Mark – Class Definition, Main Method & Object Creation in main
public class Product {
private double discount;
public Product( ) {
this.discount = 5.0;
System.out.println("Discount set to: " + discount + "%");
}
public Product(double discount) {
this.discount = discount;
System.out.println("Discount set to: " + discount + "%");
}
public static void main(String[] args) {
Product product1 = new Product();
Product product2 = new Product(10.0);
}
}
CO-4   C.   What is an abstract class? Utilize the concept of abstract to explain its   [05]
BL-3   working with a programming example.
********** 2 **********
--- page 3 ---
02 Marks – Abstract Class
03 Marks - Programming Example
Abstract Class:
- An abstract class is a class declared with the abstract keyword
-   cannot be instantiated directly.
-   serves as a blueprint for subclasses/supports inheritance
- Can contain abstract and non-abstract methods
- Can have constructors
- Can contain variables and static methods
abstract class Animal {
abstract void sound(); // abstract method
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {   // Implementation of abstract method
System.out.println("Dog barks");
}
public static void main(String[] args) {
Animal a = new Dog(); // abstract class reference
a.sound();
a.eat();
}
}
CO-5 D.   What is a generic class? Demonstrate its implementation with an   [05]
BL-3   appropriate programming example?
02 Marks – Generic Class
03 Marks - Programming Example
Generic Class:
- A generic class in Java is a class that can operate on objects of
various types while providing compile-time type safety and code
reusability.
-   Instead of writing a class for each data type, you define the class
with a type parameter that is replaced by a concrete type when an
instance of the class is created.
-   This approach avoids the need for manual type casting and helps
catch type-mismatch errors during compilation rather than at
runtime.
- Type parameters must be reference types (not primitives)
Example:
public class GenericBox<T> {
private T t;
public void set(T t) {
this.t = t;
}
********** 3 **********
--- page 4 ---
public T get() {
return t;
}
}
class Test{
public static void main(String ...a){
GenericBox<Integer> integerBox = new GenericBox<Integer>();
integerBox.set(10);
int i = integerBox.get();
GenericBox<String> stringBox = new GenericBox<String>();
stringBox.set("Hello World");
String s = stringBox.get();
}
}
Section- B
Q2
CO-2 A   What is Inheritance? What are its types? Develop a program that explains   [10]
the concept of multilevel inheritance.
BL-3
02 Marks – Inheritance
04 Marks – Types of Inheritance
04 Marks – Programming Example of Multilevel Inheritance
Inheritance:
-   Inheritance is a mechanism in which a derived object acquires all
the properties and behaviours of a base object. [Reusability of
Encapsulation]
- Using inheritance, one can reuse methods and fields of the
superclass in the subclass.
- Why Inheritance?
- Reuse
- Avoid redundant coding
- Allow function Overriding.
- Syntax of Java Inheritance
class Superclass_Name{
//methods and fields
}
class Subclass_Name extends Superclass_Name {
}
********** 4 **********
--- page 5 ---
Types of Inheritance:
Multilevel Inheritance:
-   Multilevel inheritance is a concept where a class inherits from a
class that is already a subclass of another class, forming a chain of
inheritance (e.g., Class A → Class B → Class C).
- The child class has access to methods and properties from all its
ancestor classes.
- Example :
Shape
Rectangle
Square
class Shape extents Object {
void draw() {
System.out.println("Drawing shape");
}
}
class Rectangle extends Shape {
void calculateArea() {
System.out.println("Rectangle area calculated");
}
}
class Square extends Rectangle {
void display() {
draw();
calculateArea();
System.out.println("Square displayed");
}
public static void main(String[] args) {
Square s = new Square();
********** 5 **********
--- page 6 ---
s.display();
}
}
CO-4 B   A library maintains various types of items, such as Books and Magazines.   [10]
Each item calculates its late fee differently. Write an object-oriented
BL-3
program to create an abstract class LibraryItem, which includes an abstract
method calculateLateFee( ). The class LibraryItem has subclasses Book and
Magazine. Both subclasses implement calculateLateFee( ) and display the
late fees for each item. Create a main class to execute the program. Consider
late fees of Rs. 3 per day for Magazines and Rs. 5 per day for books.
03 Marks – Code for Abstract class & method definitions
05 Marks – code for Subclasses & its methods
02 Marks – Main & execution
abstract class LibraryItem {
int daysLate;
LibraryItem(int daysLate) {
this.daysLate = daysLate;
}
abstract double calculateLateFee( );
}
class Book extends LibraryItem {
Book(int daysLate) {
super(daysLate);
}
double calculateLateFee( ) {
return daysLate*5;
}
}
class Magazine extends LibraryItem {
Magazine(int daysLate) {
super(daysLate);
}
double calculateLateFee() {
return daysLate*3;
}
}
class Main {
public static void main(String[ ] args) {
LibraryItem b = new Book(4);
LibraryItem m = new Magazine(4);
System.out.println("Book late fee = " + b.calculateLateFee());
System.out.println("Magazine late fee = " + m.calculateLateFee());
}
}
********** 6 **********
--- page 7 ---
Q3
CO-3 A   Write an object-oriented program that defines a method divide(int a, int b),   [10]
which throws an arithmetic exception if division by zero occurs. Call this
BL-3
method from the main( ) method and handle the exception.
04 Marks – Code for Divide method & throws exception
04 Marks – Appropriate code for Exception Handling in main
02 Marks – main method & call to divide
class ThrowsDivision {
static int divide(int a, int b) throws ArithmeticException {
return a / b;
}
public static void main(String[] args) {
try {
int result = divide(10,0);
System.out.println("Result = " + result);
}
catch(ArithmeticException e) {
System.out.println("Cannot divide by zero.");
}
}
}
CO-5 B   What is the Singleton design pattern? Use the Singleton design pattern to   [10]
create a program that creates only one instance.
BL-3
05 Marks – Description of Singleton
05 Marks – Suitable programming example
Singleton
-   Singleton is a creational design pattern
-   It ensures a class has only one instance
-   It provides a global access point to that instance
-   Singleton design pattern ensures that only one instance of the class
will be created and that instance will have global access within the
application.
- The Singleton pattern works by:
o Making the constructor private
▪ Prevents object creation from outside the class
o Creating a static instance variable
▪ Holds the single object of the class
o Providing a public static method (getInstance())
▪ Returns the same instance every time
- Programming Example
Singleton
-instance:Singleton
-Singleton( )
+getInstance()
********** 7 **********
--- page 8 ---
class Singleton {
private static Singleton instance;
private Singleton( ) {
System.out.println("Singleton Instance Created");
}
public static Singleton getInstance( ) {
if (instance == null) {
instance = new Singleton( ); // created only once
}
return instance;
}
}
class Main {
public static void main(String[ ] args) {
Singleton s1 = Singleton.getInstance();
Singleton s2 = Singleton.getInstance();
System.out.println(s1);
System.out.println(s2);
// Checking if it is one object or two different Objects
if (s1 == s2) {
System.out.println("Only one instance exists!");
}
}
}
Q4
CO-2 A   Develop an Object-oriented program to maintain a database of employees   [10]
for an educational institution. The Staff class has instance variables such as
BL-3
id and name. The Teacher and Officer are inherited from Staff. The Teacher
class has an instance variable subject taught, and the Officer class has a
work type as an instance variable. Each class will have instance methods
read ( ) and show ( ). Specify all the classes and define methods to create
the database described above and to retrieve individual information.
02 Marks - Staff class, attributes & methods
02 Marks - Teacher class, attributes & methods
02 Marks - Officer class, attributes & methods
02Marks – Implementation of Inheritance
02Marks – Main, subclass object creation, and call to methods
class Staff
{
int id;
String name;
public void read(int id, String name)
{
this.id = id;
this.name=name;
}
public void show()
{
System.out.println(id);
System.out.println(name);
}
********** 8 **********
--- page 9 ---
}
class Teacher extends Staff
{
String sub_taught;
public void read( String sub_taught)
{
super.read( );
this.sub_taught=sub_taught;
}
public void show()
{
super.show( );
System.out.println(sub_taught);
}
}
class Officer extends Staff
{
String work_type;
public void read(String work_type)
{
super.read( );
this.work_type=work_type;
}
public void show()
{
super.show( );
System.out.println(work_type);
}
}
class Retreive
{
public static void main(String args[])
{
Officer of=new Officer();
of.read(10, "Rohit");
of.read("Lab Manager");
of.show();
Teacher t=new Teacher();
t.read(20, "Virat");
t.read("physics");
t.show();
}
}
CO-1 B   What are arrays? Explain how to declare, initialise, and create them with a   [10]
BL-3   programming example.
02 Marks – Array
01 Mark – Declaration
01 Marks – Initialisation
01 Mark – Creation
05 Mark- Programming Example
********** 9 **********
--- page 10 ---
- An array is a collection of a fixed number of elements of the same
type. There are situations where we might wish to store a group of
similar type of values in a variable.
- An array is a memory space allocated that can store multiple values
of the same data type, in contiguous locations.
-   This memory space, which can be perceived to have many logical
contiguous locations, can be accessed with a common name.
- A specific element in an array is accessed by the use of a subscript
or index used in brackets, along with the name of the array.
- For example, marks[5]would mean marks of 5th student.
- While the complete set of values is called an array, the individual
values are known as elements.
- Arrays can be of two types:
o one-dimensional array
o multi-dimensional array
Declaring an array
•   Declaring an array is the same as declaring a normal variable, except
that you must use a set of square brackets with the variable type.
• There can be two ways [Syntax] in which an array can be declared.
– type arrayname[ ];
– type[ ] arrayname;
• For e.g.
int marks[ ]; or
int[ ] marks;
Creating memory locations
• An array is more complex than a normal variable, so we have to
assign memory to the array when we declare it.
• We can assign memory to an array by specifying its size.
Interestingly, our same old new operator helps in doing the job, just
as shown below:
– Arrayname = new type [size];
•   So, allocating space and size for the array named marks can be done
as,
– marks = new int[5];
Initialising an array
• Assignment of values to an array, which can also be termed as
initialisation of an array, can be done as follows,
– Arrayname[index] = {list of values}
– Ex int a[ ] = {1,2,3,4,5}
class ArrayTest {
public static void main(String[ ] args) {
int a[]; // Declaration
a = new int [5]; //creation
for(int e:a)
System.out.print(e+ " " ); //displays 0 0 0 0 0
System.out.println( );
int[ ] marks = new int[ ]{12,45,67,89,90}; // initialization
for(int i=0;i<marks.length;i++)
System.out.print(marks[i]+ " ");
********** 10 **********
--- page 11 ---
}
}
Q5
CO-1 A   Define a class named GradeTest with a method gradeCheck(int) that accepts   [10]
marks as a parameter and classifies the score based on the range: display A
BL-3
if 90-100, B for 80-90, C for 70-80, D for 60-70, E for 50-60, F for 0-50,
and indicate invalid otherwise. Write a complete object-oriented
programming (OOP) program to demonstrate this scenario.
02 Mark – GradeTest class
02 Marks – gradeCheck method
04 Marks -Grade Check Logic
02 Marks – main, object creation and method call
class GradeTest {
void gradeCheck(int marks) {
if (marks >= 90 && marks <= 100) {
System.out.println("Grade: A");
}
else if (marks >= 80 && marks < 90) {
System.out.println("Grade: B");
}
else if (marks >= 70 && marks < 80) {
System.out.println("Grade: C");
}
else if (marks >= 60 && marks < 70) {
System.out.println("Grade: D");
}
else if (marks >= 50 && marks < 60) {
System.out.println("Grade: E");
}
else if (marks >= 0 && marks < 50) {
System.out.println("Grade: F");
}
else {
System.out.println("Invalid Marks");
}
}
public static void main(String[] args) {
GradeTest obj = new GradeTest();
int marks = 85;
obj.gradeCheck(marks);
}
}
********** 11 **********
--- page 12 ---
CO-4 B   What are wrapper classes? Explain how wrapper classes assist with data   [10]
conversion. Develop a program that reads three numbers as Strings,
BL-3
converts them into integers using wrapper class methods, and calculates the
sum and average.
02 Marks – Wrapper class
03 Marks – List of wrapper classes
05 Marks – Program to read three numbers & its conversion
Wrapper Classes
- Wrapper classes are predefined classes in Java.
- Wrapper classes are used to convert between primitive data types
and objects.
- Wrapper classes provide a way to use primitive data types (int,
boolean, etc..) as objects
- Each primitive type has a corresponding wrapper class.
List of Wrapper classes:
Primitive Data Type Wrapper Class
byte   Byte
short   Short
int   Integer
long   Long
float   Float
double   Double
boolean   Boolean
char   Character
Wrapper classes provide methods that make conversion easy:
String → Primitive Conversion
Using methods like:
- Integer.parseInt()
- Double.parseDouble()
import java.util.Scanner;
class WrapperDemo {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int sum = 0;
for(int i = 1; i <= 3; i++) {
System.out.print("Enter number " + i + " (as String): ");
String input = sc.nextLine();
// String to integer conversion using wrapper class
int num = Integer.parseInt(input);
********** 12 **********
--- page 13 ---
sum += num;
}
double average = (double) sum / 3;
System.out.println("Sum = " + sum);
System.out.println("Average = " + average);
}
}
Q6
CO-5 A   Create a class ComplexNumber with real and imaginary parts as instance   [10]
variables to represent a complex number (a + bi). Develop an object-
BL-3
oriented program that utilizes a generic class StoreComplexNumber to
store, input, and output a complex number using a user-defined Complex
class. Use the constructor to store the number, and provide methods to read
and
display it.
02 Marks – Complex Number Class
02 Marks – Generic Class Definition
02 Marks – Read Complex no in generic class
02 Marks – Display Complex no in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class ComplexNumber {
double real;
double imaginary;
}
class StoreComplexNumber<T> {
private T obj;
public StoreComplexNumber(T obj) {
this.obj = obj;
}
public void read() {
Scanner sc = new Scanner(System.in);
ComplexNumber c = (ComplexNumber) obj;
System.out.print("Enter real part: ");
c.real = sc.nextDouble();
System.out.print("Enter imaginary part: ");
c.imaginary = sc.nextDouble();
}
public void display() {
ComplexNumber c = (ComplexNumber) obj;
System.out.println("CompNo: " + c.real + " + " + c.imaginary + "i");
}
********** 13 **********
--- page 14 ---
}
class Main {
public static void main(String[] args) {
ComplexNumber c1 = new ComplexNumber();
StoreComplexNumber<ComplexNumber> store = new
StoreComplexNumber<>(c1);
store.read();
store.display();
}
}
CO-2 B   Use your knowledge of Object-Oriented Programming to distinguish [10]
BL-3   between the following.
- Methods and Constructors
-   Encapsulation and Abstraction
05 Marks – Method and Constructor - at least 4 valid points &
example
05 Marks - Encapsulation and Abstraction – at least 2-3 valid points
and example
Constructor   Method
It is a special method having the   It can have any name
same name as the class
Used to create an object and   It shows the behavior of an object
initializes an instance variable
To invoke the constructor, the   An object or class is required
new operator is required
It is not static   It is static or non-static
It is not inherited   It is inherited
Constructor overriding is not   Overriding is possible
possible
class Student {   Example:
private String name;   public class Calculator {
public Student() {   public int add(int a, int b) {
System.out.println("Default");   return a + b;
}   }
public double add(double a, double
public Student(String name) {   b) {
System.out.println("Parameterized");   return a + b;
}   }
public static void main(String[] args)   public static void main(String[]
{   args) {
new Student();   Calculator calc = new
new Student(" ");   Calculator();
}
}   calc.add(2, 3);
calc.add(2.5, 3.7);
}
}
********** 14 **********
--- page 15 ---
Encapsulation and Abstraction
Abstraction:
- Abstraction means hiding the implementation details
- Abstraction = User knows what to do, not how it is done
- Abstraction means showing only the essential features to the user and
hiding the internal implementation details.
Encapsulation:
- Encapsulation involves bundling data and methods (functions) into a
single unit.
- The term 'Encapsulation' is similar to enclosing something inside a
capsule.
- This process involves concealing all internal details of an object from the
external environment.
- Encapsulation = Data   is hidden + accessed only through
methods/functions
-
Example:
class EncapsulationAbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void getterMethod( ){
System.out.println(data);
}
} //Encapsulation
class MainTest{
public static void main(String args[ ]){
EncapsulationAbstractionTest eat = new
EncapsulationAbstractionTest( );
eat.setterMethod( ); //abstraction
eat.getterMethod( );
}
}
Q7
CO-3 A   Write an object-oriented program that copies a file's contents to another   [10]
using byte streams. The program should prompt the user for source and
BL-3
destination filenames, manage exceptions properly, and display a success
message upon completion.
01 Marks – Reading file names from user
02 Marks - File Opening in Read mode
02 Marks – File Opening in Write mode
04 Marks – Copying File Contents
01 Mark – Appropriate Exception Handling
********** 15 **********
--- page 16 ---
import java.io.*;
import java.util.Scanner;
class FileCopyByte {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter source file: ");
String source = sc.nextLine();
System.out.print("Enter destination file: ");
String dest = sc.nextLine();
try{
FileInputStream fis = new FileInputStream(source);
FileOutputStream fos = new FileOutputStream(dest);
int data;
while ((data = fis.read()) != -1) {
fos.write(data);
}
System.out.println("File copied successfully.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
}
}
CO-1 B   Build an object-oriented program to determine whether a specified number   [05]
lies within the range of 50 to 100 (inclusive)
BL-3
02 Marks – Class & main method
03 Marks – Code for Checking number between 50 and 100
public class NumberRangeChecker {
public void checkRange(int number) {
System.out.print(number + " ");
if (number >= 50 && number <= 100) {
System.out.println("is WITHIN range 50-100");
} else {
System.out.println("is OUTSIDE range 50-100");
}
}
public static void main(String[] args) {
NumberRangeChecker obj = new NumberRangeChecker( )
obj.checkRange(75);
}
}
CO-2 C   Apply your understanding of Polymorphism to explain run-time   [05]
polymorphism with a suitable programming example.
********** 16 **********
--- page 17 ---
BL-3
02 Marks – Run Time Polymorphism
03 Marks – Programming Example
- Runtime polymorphism, also known as dynamic method
dispatch or late binding, is a core object-oriented programming
concept where an overridden method's call is resolved at runtime,
rather than compile time.
-   This mechanism allows a single action to be performed in different
ways depending on the actual type of the object
- Runtime polymorphism requires an "is-a" relationship
(inheritance) between classes, where a subclass extends a
superclass.
-   It involves a superclass reference variable pointing to a subclass
object. The type of reference is the parent class, but
the object instance is of the child class. (upcasting)
Example:
class Animal {
void sound( ) {
System.out.println("Animal sound");
}
}
class Cat extends Animal {
void sound( ) {
System.out.println("Cat meows");
}
}
class Main {
public static void main(String[] args) {
Animal a = new Cat( );
a.sound( );
}
}
X------------------------------------------------------------------------------------------------------------X
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 4b4b5f4392e9

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_CSBS_7036/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1 A.   What are the key paradigms of object-oriented programming? List and   [05]
BL-3   demonstrate each one with an example.
02 Marks – Key Paradigms
03 Marks – Description with programming example
If any programming language supports Encapsulation, Polymorphism,
Inheritance and Abstraction etc. is called as OOP
Encapsulation: -
- Binding/Wrapping of data to its related functions into a single unit
-   In OOP, we can achieve encapsulation by creating classes and
objects.
Abstraction: -
-   It hides the implementation details.
- A Class can decide which member will be visible to the outside of
the class
Polymorphism (many forms):-
-   Defining multiple functions with the same name
- These functions with same name will show different behaviours
- There are two types of polymorphism → Static(Overloading) &
Dynamic(Overriding)
Inheritance:-
-   Inherence is reusability (of encapsulation).
********** 1 **********
--- page 2 ---
-   Child/Derived/ Sub Class inherits the properties of Parent/Base/
Super Class.
Example:
class Person {
private String name;
void work() {
System.out.println("Person works");
}
}  Encapsulation (name + work)
class Teacher extends Person { Inheritance
Teacher(String name) {
this.name=name;
}
void work() {  Dynamic Polymorphism
System.out.println(name + " teaches");
}
}
Class Test{
public static void main(String[] args) {
Teacher t = new Teacher("Paavan");
t.work();  Abstraction
}
}
CO-2   B.   Consider a product class with only one data member, discount. Apply the   [05]
BL-3   concept of constructor overloading to write an object-oriented program,
such that one constructor initializes the discount to 5 and another
parameterized constructor initializes it to 10 by accepting the discount as a
parameter. Create two objects by invoking both the constructors and
displaying the discount.
03 Marks – Code for Constructor Overloading
02 Mark – Class Definition, Main Method & Object Creation in main
public class Product {
private double discount;
public Product( ) {
this.discount = 5.0;
System.out.println("Discount set to: " + discount + "%");
}
public Product(double discount) {
this.discount = discount;
System.out.println("Discount set to: " + discount + "%");
}
public static void main(String[] args) {
Product product1 = new Product();
Product product2 = new Product(10.0);
}
}
CO-4   C.   What is an abstract class? Utilize the concept of abstract to explain its   [05]
BL-3   working with a programming example.
********** 2 **********
--- page 3 ---
02 Marks – Abstract Class
03 Marks - Programming Example
Abstract Class:
- An abstract class is a class declared with the abstract keyword
-   cannot be instantiated directly.
-   serves as a blueprint for subclasses/supports inheritance
- Can contain abstract and non-abstract methods
- Can have constructors
- Can contain variables and static methods
abstract class Animal {
abstract void sound(); // abstract method
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {   // Implementation of abstract method
System.out.println("Dog barks");
}
public static void main(String[] args) {
Animal a = new Dog(); // abstract class reference
a.sound();
a.eat();
}
}
CO-5 D.   What is a generic class? Demonstrate its implementation with an   [05]
BL-3   appropriate programming example?
02 Marks – Generic Class
03 Marks - Programming Example
Generic Class:
- A generic class in Java is a class that can operate on objects of
various types while providing compile-time type safety and code
reusability.
-   Instead of writing a class for each data type, you define the class
with a type parameter that is replaced by a concrete type when an
instance of the class is created.
-   This approach avoids the need for manual type casting and helps
catch type-mismatch errors during compilation rather than at
runtime.
- Type parameters must be reference types (not primitives)
Example:
public class GenericBox<T> {
private T t;
public void set(T t) {
this.t = t;
}
********** 3 **********
--- page 4 ---
public T get() {
return t;
}
}
class Test{
public static void main(String ...a){
GenericBox<Integer> integerBox = new GenericBox<Integer>();
integerBox.set(10);
int i = integerBox.get();
GenericBox<String> stringBox = new GenericBox<String>();
stringBox.set("Hello World");
String s = stringBox.get();
}
}
Section- B
Q2
CO-2 A   What is Inheritance? What are its types? Develop a program that explains   [10]
the concept of multilevel inheritance.
BL-3
02 Marks – Inheritance
04 Marks – Types of Inheritance
04 Marks – Programming Example of Multilevel Inheritance
Inheritance:
-   Inheritance is a mechanism in which a derived object acquires all
the properties and behaviours of a base object. [Reusability of
Encapsulation]
- Using inheritance, one can reuse methods and fields of the
superclass in the subclass.
- Why Inheritance?
- Reuse
- Avoid redundant coding
- Allow function Overriding.
- Syntax of Java Inheritance
class Superclass_Name{
//methods and fields
}
class Subclass_Name extends Superclass_Name {
}
********** 4 **********
--- page 5 ---
Types of Inheritance:
Multilevel Inheritance:
-   Multilevel inheritance is a concept where a class inherits from a
class that is already a subclass of another class, forming a chain of
inheritance (e.g., Class A → Class B → Class C).
- The child class has access to methods and properties from all its
ancestor classes.
- Example :
Shape
Rectangle
Square
class Shape extents Object {
void draw() {
System.out.println("Drawing shape");
}
}
class Rectangle extends Shape {
void calculateArea() {
System.out.println("Rectangle area calculated");
}
}
class Square extends Rectangle {
void display() {
draw();
calculateArea();
System.out.println("Square displayed");
}
public static void main(String[] args) {
Square s = new Square();
********** 5 **********
--- page 6 ---
s.display();
}
}
CO-4 B   A library maintains various types of items, such as Books and Magazines.   [10]
Each item calculates its late fee differently. Write an object-oriented
BL-3
program to create an abstract class LibraryItem, which includes an abstract
method calculateLateFee( ). The class LibraryItem has subclasses Book and
Magazine. Both subclasses implement calculateLateFee( ) and display the
late fees for each item. Create a main class to execute the program. Consider
late fees of Rs. 3 per day for Magazines and Rs. 5 per day for books.
03 Marks – Code for Abstract class & method definitions
05 Marks – code for Subclasses & its methods
02 Marks – Main & execution
abstract class LibraryItem {
int daysLate;
LibraryItem(int daysLate) {
this.daysLate = daysLate;
}
abstract double calculateLateFee( );
}
class Book extends LibraryItem {
Book(int daysLate) {
super(daysLate);
}
double calculateLateFee( ) {
return daysLate*5;
}
}
class Magazine extends LibraryItem {
Magazine(int daysLate) {
super(daysLate);
}
double calculateLateFee() {
return daysLate*3;
}
}
class Main {
public static void main(String[ ] args) {
LibraryItem b = new Book(4);
LibraryItem m = new Magazine(4);
System.out.println("Book late fee = " + b.calculateLateFee());
System.out.println("Magazine late fee = " + m.calculateLateFee());
}
}
********** 6 **********
--- page 7 ---
Q3
CO-3 A   Write an object-oriented program that defines a method divide(int a, int b),   [10]
which throws an arithmetic exception if division by zero occurs. Call this
BL-3
method from the main( ) method and handle the exception.
04 Marks – Code for Divide method & throws exception
04 Marks – Appropriate code for Exception Handling in main
02 Marks – main method & call to divide
class ThrowsDivision {
static int divide(int a, int b) throws ArithmeticException {
return a / b;
}
public static void main(String[] args) {
try {
int result = divide(10,0);
System.out.println("Result = " + result);
}
catch(ArithmeticException e) {
System.out.println("Cannot divide by zero.");
}
}
}
CO-5 B   What is the Singleton design pattern? Use the Singleton design pattern to   [10]
create a program that creates only one instance.
BL-3
05 Marks – Description of Singleton
05 Marks – Suitable programming example
Singleton
-   Singleton is a creational design pattern
-   It ensures a class has only one instance
-   It provides a global access point to that instance
-   Singleton design pattern ensures that only one instance of the class
will be created and that instance will have global access within the
application.
- The Singleton pattern works by:
o Making the constructor private
▪ Prevents object creation from outside the class
o Creating a static instance variable
▪ Holds the single object of the class
o Providing a public static method (getInstance())
▪ Returns the same instance every time
- Programming Example
Singleton
-instance:Singleton
-Singleton( )
+getInstance()
********** 7 **********
--- page 8 ---
class Singleton {
private static Singleton instance;
private Singleton( ) {
System.out.println("Singleton Instance Created");
}
public static Singleton getInstance( ) {
if (instance == null) {
instance = new Singleton( ); // created only once
}
return instance;
}
}
class Main {
public static void main(String[ ] args) {
Singleton s1 = Singleton.getInstance();
Singleton s2 = Singleton.getInstance();
System.out.println(s1);
System.out.println(s2);
// Checking if it is one object or two different Objects
if (s1 == s2) {
System.out.println("Only one instance exists!");
}
}
}
Q4
CO-2 A   Develop an Object-oriented program to maintain a database of employees   [10]
for an educational institution. The Staff class has instance variables such as
BL-3
id and name. The Teacher and Officer are inherited from Staff. The Teacher
class has an instance variable subject taught, and the Officer class has a
work type as an instance variable. Each class will have instance methods
read ( ) and show ( ). Specify all the classes and define methods to create
the database described above and to retrieve individual information.
02 Marks - Staff class, attributes & methods
02 Marks - Teacher class, attributes & methods
02 Marks - Officer class, attributes & methods
02Marks – Implementation of Inheritance
02Marks – Main, subclass object creation, and call to methods
class Staff
{
int id;
String name;
public void read(int id, String name)
{
this.id = id;
this.name=name;
}
public void show()
{
System.out.println(id);
System.out.println(name);
}
********** 8 **********
--- page 9 ---
}
class Teacher extends Staff
{
String sub_taught;
public void read( String sub_taught)
{
super.read( );
this.sub_taught=sub_taught;
}
public void show()
{
super.show( );
System.out.println(sub_taught);
}
}
class Officer extends Staff
{
String work_type;
public void read(String work_type)
{
super.read( );
this.work_type=work_type;
}
public void show()
{
super.show( );
System.out.println(work_type);
}
}
class Retreive
{
public static void main(String args[])
{
Officer of=new Officer();
of.read(10, "Rohit");
of.read("Lab Manager");
of.show();
Teacher t=new Teacher();
t.read(20, "Virat");
t.read("physics");
t.show();
}
}
CO-1 B   What are arrays? Explain how to declare, initialise, and create them with a   [10]
BL-3   programming example.
02 Marks – Array
01 Mark – Declaration
01 Marks – Initialisation
01 Mark – Creation
05 Mark- Programming Example
********** 9 **********
--- page 10 ---
- An array is a collection of a fixed number of elements of the same
type. There are situations where we might wish to store a group of
similar type of values in a variable.
- An array is a memory space allocated that can store multiple values
of the same data type, in contiguous locations.
-   This memory space, which can be perceived to have many logical
contiguous locations, can be accessed with a common name.
- A specific element in an array is accessed by the use of a subscript
or index used in brackets, along with the name of the array.
- For example, marks[5]would mean marks of 5th student.
- While the complete set of values is called an array, the individual
values are known as elements.
- Arrays can be of two types:
o one-dimensional array
o multi-dimensional array
Declaring an array
•   Declaring an array is the same as declaring a normal variable, except
that you must use a set of square brackets with the variable type.
• There can be two ways [Syntax] in which an array can be declared.
– type arrayname[ ];
– type[ ] arrayname;
• For e.g.
int marks[ ]; or
int[ ] marks;
Creating memory locations
• An array is more complex than a normal variable, so we have to
assign memory to the array when we declare it.
• We can assign memory to an array by specifying its size.
Interestingly, our same old new operator helps in doing the job, just
as shown below:
– Arrayname = new type [size];
•   So, allocating space and size for the array named marks can be done
as,
– marks = new int[5];
Initialising an array
• Assignment of values to an array, which can also be termed as
initialisation of an array, can be done as follows,
– Arrayname[index] = {list of values}
– Ex int a[ ] = {1,2,3,4,5}
class ArrayTest {
public static void main(String[ ] args) {
int a[]; // Declaration
a = new int [5]; //creation
for(int e:a)
System.out.print(e+ " " ); //displays 0 0 0 0 0
System.out.println( );
int[ ] marks = new int[ ]{12,45,67,89,90}; // initialization
for(int i=0;i<marks.length;i++)
System.out.print(marks[i]+ " ");
********** 10 **********
--- page 11 ---
}
}
Q5
CO-1 A   Define a class named GradeTest with a method gradeCheck(int) that accepts   [10]
marks as a parameter and classifies the score based on the range: display A
BL-3
if 90-100, B for 80-90, C for 70-80, D for 60-70, E for 50-60, F for 0-50,
and indicate invalid otherwise. Write a complete object-oriented
programming (OOP) program to demonstrate this scenario.
02 Mark – GradeTest class
02 Marks – gradeCheck method
04 Marks -Grade Check Logic
02 Marks – main, object creation and method call
class GradeTest {
void gradeCheck(int marks) {
if (marks >= 90 && marks <= 100) {
System.out.println("Grade: A");
}
else if (marks >= 80 && marks < 90) {
System.out.println("Grade: B");
}
else if (marks >= 70 && marks < 80) {
System.out.println("Grade: C");
}
else if (marks >= 60 && marks < 70) {
System.out.println("Grade: D");
}
else if (marks >= 50 && marks < 60) {
System.out.println("Grade: E");
}
else if (marks >= 0 && marks < 50) {
System.out.println("Grade: F");
}
else {
System.out.println("Invalid Marks");
}
}
public static void main(String[] args) {
GradeTest obj = new GradeTest();
int marks = 85;
obj.gradeCheck(marks);
}
}
********** 11 **********
--- page 12 ---
CO-4 B   What are wrapper classes? Explain how wrapper classes assist with data   [10]
conversion. Develop a program that reads three numbers as Strings,
BL-3
converts them into integers using wrapper class methods, and calculates the
sum and average.
02 Marks – Wrapper class
03 Marks – List of wrapper classes
05 Marks – Program to read three numbers & its conversion
Wrapper Classes
- Wrapper classes are predefined classes in Java.
- Wrapper classes are used to convert between primitive data types
and objects.
- Wrapper classes provide a way to use primitive data types (int,
boolean, etc..) as objects
- Each primitive type has a corresponding wrapper class.
List of Wrapper classes:
Primitive Data Type Wrapper Class
byte   Byte
short   Short
int   Integer
long   Long
float   Float
double   Double
boolean   Boolean
char   Character
Wrapper classes provide methods that make conversion easy:
String → Primitive Conversion
Using methods like:
- Integer.parseInt()
- Double.parseDouble()
import java.util.Scanner;
class WrapperDemo {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int sum = 0;
for(int i = 1; i <= 3; i++) {
System.out.print("Enter number " + i + " (as String): ");
String input = sc.nextLine();
// String to integer conversion using wrapper class
int num = Integer.parseInt(input);
********** 12 **********
--- page 13 ---
sum += num;
}
double average = (double) sum / 3;
System.out.println("Sum = " + sum);
System.out.println("Average = " + average);
}
}
Q6
CO-5 A   Create a class ComplexNumber with real and imaginary parts as instance   [10]
variables to represent a complex number (a + bi). Develop an object-
BL-3
oriented program that utilizes a generic class StoreComplexNumber to
store, input, and output a complex number using a user-defined Complex
class. Use the constructor to store the number, and provide methods to read
and
display it.
02 Marks – Complex Number Class
02 Marks – Generic Class Definition
02 Marks – Read Complex no in generic class
02 Marks – Display Complex no in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class ComplexNumber {
double real;
double imaginary;
}
class StoreComplexNumber<T> {
private T obj;
public StoreComplexNumber(T obj) {
this.obj = obj;
}
public void read() {
Scanner sc = new Scanner(System.in);
ComplexNumber c = (ComplexNumber) obj;
System.out.print("Enter real part: ");
c.real = sc.nextDouble();
System.out.print("Enter imaginary part: ");
c.imaginary = sc.nextDouble();
}
public void display() {
ComplexNumber c = (ComplexNumber) obj;
System.out.println("CompNo: " + c.real + " + " + c.imaginary + "i");
}
********** 13 **********
--- page 14 ---
}
class Main {
public static void main(String[] args) {
ComplexNumber c1 = new ComplexNumber();
StoreComplexNumber<ComplexNumber> store = new
StoreComplexNumber<>(c1);
store.read();
store.display();
}
}
CO-2 B   Use your knowledge of Object-Oriented Programming to distinguish [10]
BL-3   between the following.
- Methods and Constructors
-   Encapsulation and Abstraction
05 Marks – Method and Constructor - at least 4 valid points &
example
05 Marks - Encapsulation and Abstraction – at least 2-3 valid points
and example
Constructor   Method
It is a special method having the   It can have any name
same name as the class
Used to create an object and   It shows the behavior of an object
initializes an instance variable
To invoke the constructor, the   An object or class is required
new operator is required
It is not static   It is static or non-static
It is not inherited   It is inherited
Constructor overriding is not   Overriding is possible
possible
class Student {   Example:
private String name;   public class Calculator {
public Student() {   public int add(int a, int b) {
System.out.println("Default");   return a + b;
}   }
public double add(double a, double
public Student(String name) {   b) {
System.out.println("Parameterized");   return a + b;
}   }
public static void main(String[] args)   public static void main(String[]
{   args) {
new Student();   Calculator calc = new
new Student(" ");   Calculator();
}
}   calc.add(2, 3);
calc.add(2.5, 3.7);
}
}
********** 14 **********
--- page 15 ---
Encapsulation and Abstraction
Abstraction:
- Abstraction means hiding the implementation details
- Abstraction = User knows what to do, not how it is done
- Abstraction means showing only the essential features to the user and
hiding the internal implementation details.
Encapsulation:
- Encapsulation involves bundling data and methods (functions) into a
single unit.
- The term 'Encapsulation' is similar to enclosing something inside a
capsule.
- This process involves concealing all internal details of an object from the
external environment.
- Encapsulation = Data   is hidden + accessed only through
methods/functions
-
Example:
class EncapsulationAbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void getterMethod( ){
System.out.println(data);
}
} //Encapsulation
class MainTest{
public static void main(String args[ ]){
EncapsulationAbstractionTest eat = new
EncapsulationAbstractionTest( );
eat.setterMethod( ); //abstraction
eat.getterMethod( );
}
}
Q7
CO-3 A   Write an object-oriented program that copies a file's contents to another   [10]
using byte streams. The program should prompt the user for source and
BL-3
destination filenames, manage exceptions properly, and display a success
message upon completion.
01 Marks – Reading file names from user
02 Marks - File Opening in Read mode
02 Marks – File Opening in Write mode
04 Marks – Copying File Contents
01 Mark – Appropriate Exception Handling
********** 15 **********
--- page 16 ---
import java.io.*;
import java.util.Scanner;
class FileCopyByte {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter source file: ");
String source = sc.nextLine();
System.out.print("Enter destination file: ");
String dest = sc.nextLine();
try{
FileInputStream fis = new FileInputStream(source);
FileOutputStream fos = new FileOutputStream(dest);
int data;
while ((data = fis.read()) != -1) {
fos.write(data);
}
System.out.println("File copied successfully.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
}
}
CO-1 B   Build an object-oriented program to determine whether a specified number   [05]
lies within the range of 50 to 100 (inclusive)
BL-3
02 Marks – Class & main method
03 Marks – Code for Checking number between 50 and 100
public class NumberRangeChecker {
public void checkRange(int number) {
System.out.print(number + " ");
if (number >= 50 && number <= 100) {
System.out.println("is WITHIN range 50-100");
} else {
System.out.println("is OUTSIDE range 50-100");
}
}
public static void main(String[] args) {
NumberRangeChecker obj = new NumberRangeChecker( )
obj.checkRange(75);
}
}
CO-2 C   Apply your understanding of Polymorphism to explain run-time   [05]
polymorphism with a suitable programming example.
********** 16 **********
--- page 17 ---
BL-3
02 Marks – Run Time Polymorphism
03 Marks – Programming Example
- Runtime polymorphism, also known as dynamic method
dispatch or late binding, is a core object-oriented programming
concept where an overridden method's call is resolved at runtime,
rather than compile time.
-   This mechanism allows a single action to be performed in different
ways depending on the actual type of the object
- Runtime polymorphism requires an "is-a" relationship
(inheritance) between classes, where a subclass extends a
superclass.
-   It involves a superclass reference variable pointing to a subclass
object. The type of reference is the parent class, but
the object instance is of the child class. (upcasting)
Example:
class Animal {
void sound( ) {
System.out.println("Animal sound");
}
}
class Cat extends Animal {
void sound( ) {
System.out.println("Cat meows");
}
}
class Main {
public static void main(String[] args) {
Animal a = new Cat( );
a.sound( );
}
}
X------------------------------------------------------------------------------------------------------------X
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper db7d22df1711

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_CSE_DS_7057/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Data Structures and Algorithms
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume Suitable data if necessary.
5. Draw neat diagram and write Code snippet wherever necessary.
6. Question number 1 is Compulsory
7. Attempt any 4 from remaining questions
Q1 All questions are compulsory
Q1 All questions are compulsory.   [20]
A “Effective and Efficient programming solution is not possible without using suitable data structure”
justify this statement.
Students are expected to: [ 1 mark for each point]
1. Explain attributes of effective and efficient programming solution.
2. Explain how effectiveness of the solution gets impacted without using data structure with
example.
3. Explain the Efficiency of the code: space and time complexity
4. Explain the impact of using suitable data structure on space and time complexity
for the same example.
5. Explain the real-life software applications developed with suitable data structures.
B “Usage of Array is suitable solution to achieve better space complexity in the code” justify this
statement with example.
Students are expected to: [ 1 mark for each point]
1. Take an example of looping code without array
2. Discuss its space and time complexity
3. Re Write same example with array
4. Discuss the space and time complexity after using array
5. Summary of impact its effect on overall real-life solutions.
C Compare Adjacency list and Adjacency Matrix.
Students are expected to: [ 1 mark for each point]
1. Take an example and draw Graph.
2. Design it’s adjacency list
3. Design it’s adjacency matrix
4. Compare both list and matrix
5. Discuss the effectiveness of dynamic memory allocation.
********** 1   **********
--- page 2 ---
D List down different categories of algorithms and explain each in brief.
Students are expected to: [ 2.5 marks for each point]
1. List categories of algorithms: Divide and Conquer, Backtracking, genetic, Greedy,
Trial and Error
2. Explain each in brief
Q2   [20]
A List down all possible operations applicable for any data structure. Explain it with suitable examples
Students are expected to: [ 5 marks for each point]
1. List of all operations: insertion, deletion, traversing, searching, sorting,
2. Explain each of these operations applying any one data structure diagrammatically/coding.
B Write brief note on Time and Space complexity.
Time Complexity [5 Marks]
• What it is:
A measure of how the runtime of an algorithm increases with the input size.
• How it's used:
To understand how an algorithm will perform as the data it processes gets larger.
•   Example:
An algorithm with
𝑶(𝟏)
𝑂(1)
complexity takes a constant amount of time regardless of input size, while an algorithm with
𝑶(𝒏𝟐)
𝑂(𝑛2)
complexity will take a time that grows quadratically with the input size.
Space Complexity [5 Marks]
• What it is:
A measure of how the memory usage of an algorithm increases with the input size.
• How it's used:
To understand the memory footprint of an algorithm and ensure it doesn't exceed available memory for
large inputs.
• Components:
It includes both the fixed space for variables and constants and the variable space that depends on the
input size, such as for dynamic memory allocation or recursion stacks.
Q3.   [20]
A “Railway ticket counter serves customers and issues ticket to them” Suggest suitable data
structure for this case study. Write program in C/C++ to demonstrate its working.
Students are expected to :
1. Discuss the given case study scenario and corelate the operation of serving customers standing
in queue to be serviced in First Come First Serve basis. [1 Mark]
2. Corelate this discussion with QUEUE data structure operation. [1 Mark]
3. Write c/c++ code for insertion and deletion operation of queue for case study problem. [8
Marks]
B Write a program in C++ for following operations of STACK 1. Insertion 2. Deletion
1. Stack push code [5 MARKS]
2. Stack pop code [5 marks]
#include <stdio.h>
********** 2   **********
--- page 3 ---
#define MAXSIZE 5 // Define the maximum size of the stack
int stack[MAXSIZE];
int top = -1; // Initialize top to -1 indicating an empty stack
// Function to check if the stack is full
int isFull() {
return top == MAXSIZE - 1;
}
// Function to push an element onto the stack
void push(int data) {
if (isFull()) {
printf("Stack Overflow! Cannot push %d.\n", data);
} else {
top++;
stack[top] = data;
printf("%d pushed to stack.\n", data);
}
}
int main() {
push(10);
push(20);
push(30);
push(40);
push(50);
push(60); // This will cause a Stack Overflow
return 0;
}
#include <stdio.h>
#include <stdlib.h> // For exit()
#define MAX_SIZE 10 // Maximum size of the stack
int stack[MAX_SIZE];
int top = -1; // Initialize top to -1 indicating an empty stack
// Function to check if the stack is empty
int isEmpty() {
return top == -1;
}
// Function to perform the pop operation
int pop() {
if (isEmpty()) {
printf("Stack Underflow: Cannot pop from an empty stack.\n");
exit(1); // Exit the program or handle the error appropriately
} else {
int popped_element = stack[top];
top--; // Decrement top to remove the element
return popped_element;
}
}
// Example usage (for demonstration)
int main() {
// Push some elements (assuming a push function exists)
// For simplicity, let's manually add some elements for this example
stack[++top] = 10;
stack[++top] = 20;
stack[++top] = 30;
********** 3   **********
--- page 4 ---
printf("Popped element: %d\n", pop()); // Should print 30
printf("Popped element: %d\n", pop()); // Should print 20
printf("Popped element: %d\n", pop()); // Should print 10
pop(); // Attempt to pop from an empty stack, will cause underflow
return 0;
}
Q4.   [20]
A Compare step by step working of PRIM’S and KRUSHKAL’s algorithms with suitable example
Students are expected to… [4 marks for point 1 and 2]
1. Take an example graph and show case step by step working of PRIM’S algorithm on that
2. Showcase step by step working of KRUSHKAL’s algorithm on same example
3. Differentiate both with respect to time complexity [2 Marks]
B Generate a BST and demonstrate working of all types of traversals for the same.
Students are expected to…
1. Draw a Binary Search Tree [1 mark]
2. Showcase step by step working of in order traversal [3 marks]
3. Showcase step by step working of pre order traversal [3 marks]
4. Showcase step by step working of post order traversal [3 marks]
Q5.   [20]
A Explain the Divide and Conquer algorithm with example.
The Divide and Conquer algorithm is a problem-solving paradigm that involves breaking down a large problem
into smaller, similar subproblems, solving these subproblems independently, and then combining their solutions
to solve the original problem. This approach typically involves three main steps:
•   Divide:
The original problem is divided into several smaller subproblems that are similar in nature to the original
problem but smaller in size. This division often continues recursively until the subproblems become small
enough to be solved directly (the base case).
•   Conquer:
The subproblems are solved recursively. If a subproblem is small enough, it is solved directly. Otherwise, it
is further divided.
• Combine:
The solutions to the subproblems are combined to form the solution to the original problem.
Example: Merge Sort
Merge Sort is a classic example of a Divide and Conquer algorithm used for sorting an array.
Let's sort the array [38, 27, 43, 3, 9, 82, 10] using Merge Sort:
•   Divide:
o The array is split into two halves: [38, 27, 43] and [3, 9, 82, 10].
o Each half is further divided until individual elements are reached:
▪   [38, 27, 43]becomes [38], [27], [43].
▪   [3, 9, 82, 10]becomes [3], [9], [82], [10].
********** 4   **********
--- page 5 ---
o At this stage, each sub-array contains only one element, which is considered sorted.
•   Conquer:
o The single-element arrays are the base case and are inherently sorted.
• Combine:
o Sorted single-element arrays are merged back together in sorted order:
▪   [27]and [43] merge to [27, 43].
▪   [38]and [27, 43] merge to [27, 38, 43].
▪   Similarly, [3] and [9] merge to [3, 9].
▪   [82]and [10] merge to [10, 82].
▪   [3, 9]and [10, 82] merge to [3, 9, 10, 82].
o   Finally, the two sorted halves [27, 38, 43] and [3, 9, 10, 82] are merged to produce the fully sorted
array: [3, 9, 10, 27, 38, 43, 82].
B. “N Queen problem is Backtracking algorithm” justify with algorithmic steps
The N-Queens problem is a classic example of a backtracking algorithm because it systematically searches
for a solution by building a candidate step-by-step and "backtracks" (reverts its choices) when it determines
that a partial solution cannot be completed
. This trial-and-error approach, combined with pruning invalid paths early, is the core of backtracking.
Why N-Queens is a backtracking problem
The problem is to place N queens on NXN chessboard so that no two queens can attack each other. This
means no two queens can share the same row, column, or diagonal.
Backtracking is a natural fit for this problem for the following reasons:
•   Sequential decision-making: You can build the solution incrementally by placing one queen at a time,
typically one per row, starting from the first row.
•   Constraint satisfaction: After placing each queen, you can check if the placement is "safe" by ensuring it
doesn't conflict with any previously placed queens.
•   State-space pruning: If a queen cannot be placed in a safe position in the current row, there is no need to
explore any further placements for that row. The algorithm can "prune" this invalid path and backtrack to
the previous row to change the position of the last queen placed.
•   Systematic exploration: The method exhaustively explores the solution space by trying every possible valid
placement, guaranteeing that all solutions (or a single solution) will be found if they exist.
Backtracking algorithm steps for the N-Queens problem
The general algorithm for the N-Queens problem using backtracking involves a recursive function that attempts to
place a queen in each row.
Main function
1. Initialize an empty NXN chessboard, typically represented by a 2D array or matrix.
2. Call a recursive helper function, solveNQueens(row), starting with row = 0.
********** 5   **********
--- page 6 ---
3.   If the helper function returns a successful solution, print or store the board configuration.
Recursive helper function solveNQueens(row)
1. Base case: If row >= N, it means all N queens have been successfully placed in rows O TO n-1
. A solution has been found. Return true.
2. Recursive step: Iterate through each column from 0 to N-1 for the current row:
a. Check for safety: Check if placing a queen at board[row][column] is safe from attack by queens in
previous rows. This involves checking the current column, and both diagonals (upper-left and upper-right).
b. Place the queen (Choose): If the position is safe, place a queen at board[row][column].
c. Recur for next row (Explore): Recursively call solveNQueens(row + 1) to place the next queen.
d. Check the result:
* If the recursive call returns true, it means a full solution was found. Return true to pass the success back
up the call stack.
* If the recursive call returns false, it means a dead end was reached.
e. Remove the queen (Backtrack): Reset board[row][column] to empty. This "un-places" the queen and
backtracks to try the next possible column in the current row.
3. No solution in this row: If the loop finishes without finding a safe placement for a queen in the current
row, return false. This triggers the backtracking step in the previous recursive call.
Q6.   [20]
A Write a program to create doubly linked list and traverse it.
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a doubly linked list node
struct Node {
int data;
struct Node* prev;
struct Node* next;
};
// Global pointer to the head of the list
struct Node* head = NULL;
// Function to insert a new node at the end of the list
void insert(int new_data) {
// 1. Allocate node
struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
// 2. Put in the data
new_node->data = new_data;
new_node->next = NULL;
// 3. If the list is empty, make the new node the head
if (head == NULL) {
new_node->prev = NULL;
head = new_node;
return;
}
********** 6   **********
--- page 7 ---
// 4. Else, traverse to the last node
struct Node* last = head;
while (last->next != NULL) {
last = last->next;
}
// 5. Change the next of the last node
last->next = new_node;
// 6. Make the last node the previous of the new node
new_node->prev = last;
}
// Function to print the doubly linked list
void display() {
struct Node* temp = head;
printf("Doubly Linked List: ");
while (temp != NULL) {
printf("%d ", temp->data);
temp = temp->next;
}
printf("\n");
}
// Main function to demonstrate the doubly linked list
int main() {
// Insert some elements
insert(10);
insert(20);
insert(30);
insert(40);
// Display the list
display();
return 0;
}
B Take an example and explain step by step working of shorted path algorithm
Students are expected to…
1. Design a directed weighted graph [2 Marks]
2. Apply Dijkstra’s shorted path finding algorithm on it and show step by step working of the same.
[8 marks]
Q7.   [20]
A “Divide and Conquer is different than Backtracking approach” Justify with example.
Students are expected to.. [1 mark each]
1. Explain steps of divide and Conquer algorithm
2. Explain steps of Backtracking algorithm
3. Compare both based on its operational differences, Complexity differences
4. Example of divide and conquer algorithm
5. Example of Backtracking algorithm
B Explain following terms: Tree, Siblings, Height of tree, Decedents, Ancestors
********** 7   **********
--- page 8 ---
Students are expected to…[1 mark for each correct explanation of these terms]
1. Draw a tree with at least 3 levels and explain these terms with the help of the tree.
C “Search time complexity of right skewed tree is similar to linear search approach” justify.
Students are expected to…[1 mark for each point]
1. Draw right skewed binary search tree
2. Discuss best and worst case of searching element in skewed tree.
3. Discuss the linear search algorithm using array example
4. Discuss best and worst case of searching element in linear search algorithm.
5. Corelate point number 2 and 4.
D Explain Genetic algorithmic steps and it’s application.
Genetic Algorithm [3 Marks]
Steps of a genetic algorithm
1. Initialization:
Create an initial population of candidate solutions, often represented as "chromosomes" (strings of data),
by generating them randomly.
2. Fitness Evaluation:
Score each individual in the population using a fitness function. This score represents how good a solution
is for the problem you are trying to solve.
3. Selection:
Choose parents from the current population based on their fitness. Individuals with higher fitness have a
greater chance of being selected to reproduce. Common methods include roulette wheel
selection and tournament selection.
4. Crossover (Recombination):
Create new "offspring" solutions by combining the genetic material of selected parents. This is often done
by swapping parts of the parent chromosomes at a random point.
5. Mutation:
Introduce small, random changes to the new offspring's chromosomes. This ensures genetic diversity and
prevents the algorithm from getting stuck in a local optimum.
6. Replacement:
Create the next generation by replacing the old population with the new offspring. This new population
will then go through the evaluation and selection process again.
7. Termination:
Repeat the process of evaluation, selection, crossover, and mutation until a stopping criterion is met, such
as reaching a satisfactory fitness level, a maximum number of generations, or when the population
converges.
********** 8   **********
--- page 9 ---
Application [2 marks]
Applications of genetic algorithms
•   Optimization: Finding the best solution from a large set of possibilities, such as in engineering design,
financial modeling, and hyperparameter tuning.
• Machine Learning: Used for tasks like neural network training, feature selection, and data mining.
•   Robotics: Optimizing robot behavior and motion planning.
• Computer Science: Solving complex problems like the Traveling Salesman Problem (TSP), scheduling, and
Sudoku puzzles.
•   Signal and Image Processing: For tasks like feature extraction and image restoration.
********** 9   **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper d9efce0a5a94

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/BTech_Computer_7002/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1 A.   What are the key paradigms of object-oriented programming? List and   [05]
BL-3   demonstrate each one with an example.
02 Marks – Key Paradigms
03 Marks – Description with programming example
If any programming language supports Encapsulation, Polymorphism,
Inheritance and Abstraction etc. is called as OOP
Encapsulation: -
- Binding/Wrapping of data to its related functions into a single unit
-   In OOP, we can achieve encapsulation by creating classes and
objects.
Abstraction: -
-   It hides the implementation details.
- A Class can decide which member will be visible to the outside of
the class
Polymorphism (many forms):-
-   Defining multiple functions with the same name
- These functions with same name will show different behaviours
- There are two types of polymorphism → Static(Overloading) &
Dynamic(Overriding)
Inheritance:-
-   Inherence is reusability (of encapsulation).
********** 1 **********
--- page 2 ---
-   Child/Derived/ Sub Class inherits the properties of Parent/Base/
Super Class.
Example:
class Person {
private String name;
void work() {
System.out.println("Person works");
}
}  Encapsulation (name + work)
class Teacher extends Person { Inheritance
Teacher(String name) {
this.name=name;
}
void work() {  Dynamic Polymorphism
System.out.println(name + " teaches");
}
}
Class Test{
public static void main(String[] args) {
Teacher t = new Teacher("Paavan");
t.work();  Abstraction
}
}
CO-2   B.   Consider a product class with only one data member, discount. Apply the   [05]
BL-3   concept of constructor overloading to write an object-oriented program,
such that one constructor initializes the discount to 5 and another
parameterized constructor initializes it to 10 by accepting the discount as a
parameter. Create two objects by invoking both the constructors and
displaying the discount.
03 Marks – Code for Constructor Overloading
02 Mark – Class Definition, Main Method & Object Creation in main
public class Product {
private double discount;
public Product( ) {
this.discount = 5.0;
System.out.println("Discount set to: " + discount + "%");
}
public Product(double discount) {
this.discount = discount;
System.out.println("Discount set to: " + discount + "%");
}
public static void main(String[] args) {
Product product1 = new Product();
Product product2 = new Product(10.0);
}
}
CO-4   C.   What is an abstract class? Utilize the concept of abstract to explain its   [05]
BL-3   working with a programming example.
********** 2 **********
--- page 3 ---
02 Marks – Abstract Class
03 Marks - Programming Example
Abstract Class:
- An abstract class is a class declared with the abstract keyword
-   cannot be instantiated directly.
-   serves as a blueprint for subclasses/supports inheritance
- Can contain abstract and non-abstract methods
- Can have constructors
- Can contain variables and static methods
abstract class Animal {
abstract void sound(); // abstract method
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {   // Implementation of abstract method
System.out.println("Dog barks");
}
public static void main(String[] args) {
Animal a = new Dog(); // abstract class reference
a.sound();
a.eat();
}
}
CO-5 D.   What is a generic class? Demonstrate its implementation with an   [05]
BL-3   appropriate programming example?
02 Marks – Generic Class
03 Marks - Programming Example
Generic Class:
- A generic class in Java is a class that can operate on objects of
various types while providing compile-time type safety and code
reusability.
-   Instead of writing a class for each data type, you define the class
with a type parameter that is replaced by a concrete type when an
instance of the class is created.
-   This approach avoids the need for manual type casting and helps
catch type-mismatch errors during compilation rather than at
runtime.
- Type parameters must be reference types (not primitives)
Example:
public class GenericBox<T> {
private T t;
public void set(T t) {
this.t = t;
}
********** 3 **********
--- page 4 ---
public T get() {
return t;
}
}
class Test{
public static void main(String ...a){
GenericBox<Integer> integerBox = new GenericBox<Integer>();
integerBox.set(10);
int i = integerBox.get();
GenericBox<String> stringBox = new GenericBox<String>();
stringBox.set("Hello World");
String s = stringBox.get();
}
}
Section- B
Q2
CO-2 A   What is Inheritance? What are its types? Develop a program that explains   [10]
the concept of multilevel inheritance.
BL-3
02 Marks – Inheritance
04 Marks – Types of Inheritance
04 Marks – Programming Example of Multilevel Inheritance
Inheritance:
-   Inheritance is a mechanism in which a derived object acquires all
the properties and behaviours of a base object. [Reusability of
Encapsulation]
- Using inheritance, one can reuse methods and fields of the
superclass in the subclass.
- Why Inheritance?
- Reuse
- Avoid redundant coding
- Allow function Overriding.
- Syntax of Java Inheritance
class Superclass_Name{
//methods and fields
}
class Subclass_Name extends Superclass_Name {
}
********** 4 **********
--- page 5 ---
Types of Inheritance:
Multilevel Inheritance:
-   Multilevel inheritance is a concept where a class inherits from a
class that is already a subclass of another class, forming a chain of
inheritance (e.g., Class A → Class B → Class C).
- The child class has access to methods and properties from all its
ancestor classes.
- Example :
Shape
Rectangle
Square
class Shape extents Object {
void draw() {
System.out.println("Drawing shape");
}
}
class Rectangle extends Shape {
void calculateArea() {
System.out.println("Rectangle area calculated");
}
}
class Square extends Rectangle {
void display() {
draw();
calculateArea();
System.out.println("Square displayed");
}
public static void main(String[] args) {
Square s = new Square();
********** 5 **********
--- page 6 ---
s.display();
}
}
CO-4 B   A library maintains various types of items, such as Books and Magazines.   [10]
Each item calculates its late fee differently. Write an object-oriented
BL-3
program to create an abstract class LibraryItem, which includes an abstract
method calculateLateFee( ). The class LibraryItem has subclasses Book and
Magazine. Both subclasses implement calculateLateFee( ) and display the
late fees for each item. Create a main class to execute the program. Consider
late fees of Rs. 3 per day for Magazines and Rs. 5 per day for books.
03 Marks – Code for Abstract class & method definitions
05 Marks – code for Subclasses & its methods
02 Marks – Main & execution
abstract class LibraryItem {
int daysLate;
LibraryItem(int daysLate) {
this.daysLate = daysLate;
}
abstract double calculateLateFee( );
}
class Book extends LibraryItem {
Book(int daysLate) {
super(daysLate);
}
double calculateLateFee( ) {
return daysLate*5;
}
}
class Magazine extends LibraryItem {
Magazine(int daysLate) {
super(daysLate);
}
double calculateLateFee() {
return daysLate*3;
}
}
class Main {
public static void main(String[ ] args) {
LibraryItem b = new Book(4);
LibraryItem m = new Magazine(4);
System.out.println("Book late fee = " + b.calculateLateFee());
System.out.println("Magazine late fee = " + m.calculateLateFee());
}
}
********** 6 **********
--- page 7 ---
Q3
CO-3 A   Write an object-oriented program that defines a method divide(int a, int b),   [10]
which throws an arithmetic exception if division by zero occurs. Call this
BL-3
method from the main( ) method and handle the exception.
04 Marks – Code for Divide method & throws exception
04 Marks – Appropriate code for Exception Handling in main
02 Marks – main method & call to divide
class ThrowsDivision {
static int divide(int a, int b) throws ArithmeticException {
return a / b;
}
public static void main(String[] args) {
try {
int result = divide(10,0);
System.out.println("Result = " + result);
}
catch(ArithmeticException e) {
System.out.println("Cannot divide by zero.");
}
}
}
CO-5 B   What is the Singleton design pattern? Use the Singleton design pattern to   [10]
create a program that creates only one instance.
BL-3
05 Marks – Description of Singleton
05 Marks – Suitable programming example
Singleton
-   Singleton is a creational design pattern
-   It ensures a class has only one instance
-   It provides a global access point to that instance
-   Singleton design pattern ensures that only one instance of the class
will be created and that instance will have global access within the
application.
- The Singleton pattern works by:
o Making the constructor private
▪ Prevents object creation from outside the class
o Creating a static instance variable
▪ Holds the single object of the class
o Providing a public static method (getInstance())
▪ Returns the same instance every time
- Programming Example
Singleton
-instance:Singleton
-Singleton( )
+getInstance()
********** 7 **********
--- page 8 ---
class Singleton {
private static Singleton instance;
private Singleton( ) {
System.out.println("Singleton Instance Created");
}
public static Singleton getInstance( ) {
if (instance == null) {
instance = new Singleton( ); // created only once
}
return instance;
}
}
class Main {
public static void main(String[ ] args) {
Singleton s1 = Singleton.getInstance();
Singleton s2 = Singleton.getInstance();
System.out.println(s1);
System.out.println(s2);
// Checking if it is one object or two different Objects
if (s1 == s2) {
System.out.println("Only one instance exists!");
}
}
}
Q4
CO-2 A   Develop an Object-oriented program to maintain a database of employees   [10]
for an educational institution. The Staff class has instance variables such as
BL-3
id and name. The Teacher and Officer are inherited from Staff. The Teacher
class has an instance variable subject taught, and the Officer class has a
work type as an instance variable. Each class will have instance methods
read ( ) and show ( ). Specify all the classes and define methods to create
the database described above and to retrieve individual information.
02 Marks - Staff class, attributes & methods
02 Marks - Teacher class, attributes & methods
02 Marks - Officer class, attributes & methods
02Marks – Implementation of Inheritance
02Marks – Main, subclass object creation, and call to methods
class Staff
{
int id;
String name;
public void read(int id, String name)
{
this.id = id;
this.name=name;
}
public void show()
{
System.out.println(id);
System.out.println(name);
}
********** 8 **********
--- page 9 ---
}
class Teacher extends Staff
{
String sub_taught;
public void read( String sub_taught)
{
super.read( );
this.sub_taught=sub_taught;
}
public void show()
{
super.show( );
System.out.println(sub_taught);
}
}
class Officer extends Staff
{
String work_type;
public void read(String work_type)
{
super.read( );
this.work_type=work_type;
}
public void show()
{
super.show( );
System.out.println(work_type);
}
}
class Retreive
{
public static void main(String args[])
{
Officer of=new Officer();
of.read(10, "Rohit");
of.read("Lab Manager");
of.show();
Teacher t=new Teacher();
t.read(20, "Virat");
t.read("physics");
t.show();
}
}
CO-1 B   What are arrays? Explain how to declare, initialise, and create them with a   [10]
BL-3   programming example.
02 Marks – Array
01 Mark – Declaration
01 Marks – Initialisation
01 Mark – Creation
05 Mark- Programming Example
********** 9 **********
--- page 10 ---
- An array is a collection of a fixed number of elements of the same
type. There are situations where we might wish to store a group of
similar type of values in a variable.
- An array is a memory space allocated that can store multiple values
of the same data type, in contiguous locations.
-   This memory space, which can be perceived to have many logical
contiguous locations, can be accessed with a common name.
- A specific element in an array is accessed by the use of a subscript
or index used in brackets, along with the name of the array.
- For example, marks[5]would mean marks of 5th student.
- While the complete set of values is called an array, the individual
values are known as elements.
- Arrays can be of two types:
o one-dimensional array
o multi-dimensional array
Declaring an array
•   Declaring an array is the same as declaring a normal variable, except
that you must use a set of square brackets with the variable type.
• There can be two ways [Syntax] in which an array can be declared.
– type arrayname[ ];
– type[ ] arrayname;
• For e.g.
int marks[ ]; or
int[ ] marks;
Creating memory locations
• An array is more complex than a normal variable, so we have to
assign memory to the array when we declare it.
• We can assign memory to an array by specifying its size.
Interestingly, our same old new operator helps in doing the job, just
as shown below:
– Arrayname = new type [size];
•   So, allocating space and size for the array named marks can be done
as,
– marks = new int[5];
Initialising an array
• Assignment of values to an array, which can also be termed as
initialisation of an array, can be done as follows,
– Arrayname[index] = {list of values}
– Ex int a[ ] = {1,2,3,4,5}
class ArrayTest {
public static void main(String[ ] args) {
int a[]; // Declaration
a = new int [5]; //creation
for(int e:a)
System.out.print(e+ " " ); //displays 0 0 0 0 0
System.out.println( );
int[ ] marks = new int[ ]{12,45,67,89,90}; // initialization
for(int i=0;i<marks.length;i++)
System.out.print(marks[i]+ " ");
********** 10 **********
--- page 11 ---
}
}
Q5
CO-1 A   Define a class named GradeTest with a method gradeCheck(int) that accepts   [10]
marks as a parameter and classifies the score based on the range: display A
BL-3
if 90-100, B for 80-90, C for 70-80, D for 60-70, E for 50-60, F for 0-50,
and indicate invalid otherwise. Write a complete object-oriented
programming (OOP) program to demonstrate this scenario.
02 Mark – GradeTest class
02 Marks – gradeCheck method
04 Marks -Grade Check Logic
02 Marks – main, object creation and method call
class GradeTest {
void gradeCheck(int marks) {
if (marks >= 90 && marks <= 100) {
System.out.println("Grade: A");
}
else if (marks >= 80 && marks < 90) {
System.out.println("Grade: B");
}
else if (marks >= 70 && marks < 80) {
System.out.println("Grade: C");
}
else if (marks >= 60 && marks < 70) {
System.out.println("Grade: D");
}
else if (marks >= 50 && marks < 60) {
System.out.println("Grade: E");
}
else if (marks >= 0 && marks < 50) {
System.out.println("Grade: F");
}
else {
System.out.println("Invalid Marks");
}
}
public static void main(String[] args) {
GradeTest obj = new GradeTest();
int marks = 85;
obj.gradeCheck(marks);
}
}
********** 11 **********
--- page 12 ---
CO-4 B   What are wrapper classes? Explain how wrapper classes assist with data   [10]
conversion. Develop a program that reads three numbers as Strings,
BL-3
converts them into integers using wrapper class methods, and calculates the
sum and average.
02 Marks – Wrapper class
03 Marks – List of wrapper classes
05 Marks – Program to read three numbers & its conversion
Wrapper Classes
- Wrapper classes are predefined classes in Java.
- Wrapper classes are used to convert between primitive data types
and objects.
- Wrapper classes provide a way to use primitive data types (int,
boolean, etc..) as objects
- Each primitive type has a corresponding wrapper class.
List of Wrapper classes:
Primitive Data Type Wrapper Class
byte   Byte
short   Short
int   Integer
long   Long
float   Float
double   Double
boolean   Boolean
char   Character
Wrapper classes provide methods that make conversion easy:
String → Primitive Conversion
Using methods like:
- Integer.parseInt()
- Double.parseDouble()
import java.util.Scanner;
class WrapperDemo {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int sum = 0;
for(int i = 1; i <= 3; i++) {
System.out.print("Enter number " + i + " (as String): ");
String input = sc.nextLine();
// String to integer conversion using wrapper class
int num = Integer.parseInt(input);
********** 12 **********
--- page 13 ---
sum += num;
}
double average = (double) sum / 3;
System.out.println("Sum = " + sum);
System.out.println("Average = " + average);
}
}
Q6
CO-5 A   Create a class ComplexNumber with real and imaginary parts as instance   [10]
variables to represent a complex number (a + bi). Develop an object-
BL-3
oriented program that utilizes a generic class StoreComplexNumber to
store, input, and output a complex number using a user-defined Complex
class. Use the constructor to store the number, and provide methods to read
and
display it.
02 Marks – Complex Number Class
02 Marks – Generic Class Definition
02 Marks – Read Complex no in generic class
02 Marks – Display Complex no in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class ComplexNumber {
double real;
double imaginary;
}
class StoreComplexNumber<T> {
private T obj;
public StoreComplexNumber(T obj) {
this.obj = obj;
}
public void read() {
Scanner sc = new Scanner(System.in);
ComplexNumber c = (ComplexNumber) obj;
System.out.print("Enter real part: ");
c.real = sc.nextDouble();
System.out.print("Enter imaginary part: ");
c.imaginary = sc.nextDouble();
}
public void display() {
ComplexNumber c = (ComplexNumber) obj;
System.out.println("CompNo: " + c.real + " + " + c.imaginary + "i");
}
********** 13 **********
--- page 14 ---
}
class Main {
public static void main(String[] args) {
ComplexNumber c1 = new ComplexNumber();
StoreComplexNumber<ComplexNumber> store = new
StoreComplexNumber<>(c1);
store.read();
store.display();
}
}
CO-2 B   Use your knowledge of Object-Oriented Programming to distinguish [10]
BL-3   between the following.
- Methods and Constructors
-   Encapsulation and Abstraction
05 Marks – Method and Constructor - at least 4 valid points &
example
05 Marks - Encapsulation and Abstraction – at least 2-3 valid points
and example
Constructor   Method
It is a special method having the   It can have any name
same name as the class
Used to create an object and   It shows the behavior of an object
initializes an instance variable
To invoke the constructor, the   An object or class is required
new operator is required
It is not static   It is static or non-static
It is not inherited   It is inherited
Constructor overriding is not   Overriding is possible
possible
class Student {   Example:
private String name;   public class Calculator {
public Student() {   public int add(int a, int b) {
System.out.println("Default");   return a + b;
}   }
public double add(double a, double
public Student(String name) {   b) {
System.out.println("Parameterized");   return a + b;
}   }
public static void main(String[] args)   public static void main(String[]
{   args) {
new Student();   Calculator calc = new
new Student(" ");   Calculator();
}
}   calc.add(2, 3);
calc.add(2.5, 3.7);
}
}
********** 14 **********
--- page 15 ---
Encapsulation and Abstraction
Abstraction:
- Abstraction means hiding the implementation details
- Abstraction = User knows what to do, not how it is done
- Abstraction means showing only the essential features to the user and
hiding the internal implementation details.
Encapsulation:
- Encapsulation involves bundling data and methods (functions) into a
single unit.
- The term 'Encapsulation' is similar to enclosing something inside a
capsule.
- This process involves concealing all internal details of an object from the
external environment.
- Encapsulation = Data   is hidden + accessed only through
methods/functions
-
Example:
class EncapsulationAbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void getterMethod( ){
System.out.println(data);
}
} //Encapsulation
class MainTest{
public static void main(String args[ ]){
EncapsulationAbstractionTest eat = new
EncapsulationAbstractionTest( );
eat.setterMethod( ); //abstraction
eat.getterMethod( );
}
}
Q7
CO-3 A   Write an object-oriented program that copies a file's contents to another   [10]
using byte streams. The program should prompt the user for source and
BL-3
destination filenames, manage exceptions properly, and display a success
message upon completion.
01 Marks – Reading file names from user
02 Marks - File Opening in Read mode
02 Marks – File Opening in Write mode
04 Marks – Copying File Contents
01 Mark – Appropriate Exception Handling
********** 15 **********
--- page 16 ---
import java.io.*;
import java.util.Scanner;
class FileCopyByte {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter source file: ");
String source = sc.nextLine();
System.out.print("Enter destination file: ");
String dest = sc.nextLine();
try{
FileInputStream fis = new FileInputStream(source);
FileOutputStream fos = new FileOutputStream(dest);
int data;
while ((data = fis.read()) != -1) {
fos.write(data);
}
System.out.println("File copied successfully.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
}
}
CO-1 B   Build an object-oriented program to determine whether a specified number   [05]
lies within the range of 50 to 100 (inclusive)
BL-3
02 Marks – Class & main method
03 Marks – Code for Checking number between 50 and 100
public class NumberRangeChecker {
public void checkRange(int number) {
System.out.print(number + " ");
if (number >= 50 && number <= 100) {
System.out.println("is WITHIN range 50-100");
} else {
System.out.println("is OUTSIDE range 50-100");
}
}
public static void main(String[] args) {
NumberRangeChecker obj = new NumberRangeChecker( )
obj.checkRange(75);
}
}
CO-2 C   Apply your understanding of Polymorphism to explain run-time   [05]
polymorphism with a suitable programming example.
********** 16 **********
--- page 17 ---
BL-3
02 Marks – Run Time Polymorphism
03 Marks – Programming Example
- Runtime polymorphism, also known as dynamic method
dispatch or late binding, is a core object-oriented programming
concept where an overridden method's call is resolved at runtime,
rather than compile time.
-   This mechanism allows a single action to be performed in different
ways depending on the actual type of the object
- Runtime polymorphism requires an "is-a" relationship
(inheritance) between classes, where a subclass extends a
superclass.
-   It involves a superclass reference variable pointing to a subclass
object. The type of reference is the parent class, but
the object instance is of the child class. (upcasting)
Example:
class Animal {
void sound( ) {
System.out.println("Animal sound");
}
}
class Cat extends Animal {
void sound( ) {
System.out.println("Cat meows");
}
}
class Main {
public static void main(String[] args) {
Animal a = new Cat( );
a.sound( );
}
}
X------------------------------------------------------------------------------------------------------------X
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper c6ca9d62223b

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MBATech_Computer_7047/OBJECT ORIENTED PROGRAMMING/ANS_OBJECT ORIENTED PROGRAMMING(702CO0C075)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE - DS)/MBA Tech
(Comp)
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: OBJECT ORIENTED PROGRAMMING
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1 A.   What are the key paradigms of object-oriented programming? List and   [05]
BL-3   demonstrate each one with an example.
02 Marks – Key Paradigms
03 Marks – Description with programming example
If any programming language supports Encapsulation, Polymorphism,
Inheritance and Abstraction etc. is called as OOP
Encapsulation: -
- Binding/Wrapping of data to its related functions into a single unit
-   In OOP, we can achieve encapsulation by creating classes and
objects.
Abstraction: -
-   It hides the implementation details.
- A Class can decide which member will be visible to the outside of
the class
Polymorphism (many forms):-
-   Defining multiple functions with the same name
- These functions with same name will show different behaviours
- There are two types of polymorphism → Static(Overloading) &
Dynamic(Overriding)
Inheritance:-
-   Inherence is reusability (of encapsulation).
********** 1 **********
--- page 2 ---
-   Child/Derived/ Sub Class inherits the properties of Parent/Base/
Super Class.
Example:
class Person {
private String name;
void work() {
System.out.println("Person works");
}
}  Encapsulation (name + work)
class Teacher extends Person { Inheritance
Teacher(String name) {
this.name=name;
}
void work() {  Dynamic Polymorphism
System.out.println(name + " teaches");
}
}
Class Test{
public static void main(String[] args) {
Teacher t = new Teacher("Paavan");
t.work();  Abstraction
}
}
CO-2   B.   Consider a product class with only one data member, discount. Apply the   [05]
BL-3   concept of constructor overloading to write an object-oriented program,
such that one constructor initializes the discount to 5 and another
parameterized constructor initializes it to 10 by accepting the discount as a
parameter. Create two objects by invoking both the constructors and
displaying the discount.
03 Marks – Code for Constructor Overloading
02 Mark – Class Definition, Main Method & Object Creation in main
public class Product {
private double discount;
public Product( ) {
this.discount = 5.0;
System.out.println("Discount set to: " + discount + "%");
}
public Product(double discount) {
this.discount = discount;
System.out.println("Discount set to: " + discount + "%");
}
public static void main(String[] args) {
Product product1 = new Product();
Product product2 = new Product(10.0);
}
}
CO-4   C.   What is an abstract class? Utilize the concept of abstract to explain its   [05]
BL-3   working with a programming example.
********** 2 **********
--- page 3 ---
02 Marks – Abstract Class
03 Marks - Programming Example
Abstract Class:
- An abstract class is a class declared with the abstract keyword
-   cannot be instantiated directly.
-   serves as a blueprint for subclasses/supports inheritance
- Can contain abstract and non-abstract methods
- Can have constructors
- Can contain variables and static methods
abstract class Animal {
abstract void sound(); // abstract method
void eat() {
System.out.println("Animal eats food");
}
}
class Dog extends Animal {
void sound() {   // Implementation of abstract method
System.out.println("Dog barks");
}
public static void main(String[] args) {
Animal a = new Dog(); // abstract class reference
a.sound();
a.eat();
}
}
CO-5 D.   What is a generic class? Demonstrate its implementation with an   [05]
BL-3   appropriate programming example?
02 Marks – Generic Class
03 Marks - Programming Example
Generic Class:
- A generic class in Java is a class that can operate on objects of
various types while providing compile-time type safety and code
reusability.
-   Instead of writing a class for each data type, you define the class
with a type parameter that is replaced by a concrete type when an
instance of the class is created.
-   This approach avoids the need for manual type casting and helps
catch type-mismatch errors during compilation rather than at
runtime.
- Type parameters must be reference types (not primitives)
Example:
public class GenericBox<T> {
private T t;
public void set(T t) {
this.t = t;
}
********** 3 **********
--- page 4 ---
public T get() {
return t;
}
}
class Test{
public static void main(String ...a){
GenericBox<Integer> integerBox = new GenericBox<Integer>();
integerBox.set(10);
int i = integerBox.get();
GenericBox<String> stringBox = new GenericBox<String>();
stringBox.set("Hello World");
String s = stringBox.get();
}
}
Section- B
Q2
CO-2 A   What is Inheritance? What are its types? Develop a program that explains   [10]
the concept of multilevel inheritance.
BL-3
02 Marks – Inheritance
04 Marks – Types of Inheritance
04 Marks – Programming Example of Multilevel Inheritance
Inheritance:
-   Inheritance is a mechanism in which a derived object acquires all
the properties and behaviours of a base object. [Reusability of
Encapsulation]
- Using inheritance, one can reuse methods and fields of the
superclass in the subclass.
- Why Inheritance?
- Reuse
- Avoid redundant coding
- Allow function Overriding.
- Syntax of Java Inheritance
class Superclass_Name{
//methods and fields
}
class Subclass_Name extends Superclass_Name {
}
********** 4 **********
--- page 5 ---
Types of Inheritance:
Multilevel Inheritance:
-   Multilevel inheritance is a concept where a class inherits from a
class that is already a subclass of another class, forming a chain of
inheritance (e.g., Class A → Class B → Class C).
- The child class has access to methods and properties from all its
ancestor classes.
- Example :
Shape
Rectangle
Square
class Shape extents Object {
void draw() {
System.out.println("Drawing shape");
}
}
class Rectangle extends Shape {
void calculateArea() {
System.out.println("Rectangle area calculated");
}
}
class Square extends Rectangle {
void display() {
draw();
calculateArea();
System.out.println("Square displayed");
}
public static void main(String[] args) {
Square s = new Square();
********** 5 **********
--- page 6 ---
s.display();
}
}
CO-4 B   A library maintains various types of items, such as Books and Magazines.   [10]
Each item calculates its late fee differently. Write an object-oriented
BL-3
program to create an abstract class LibraryItem, which includes an abstract
method calculateLateFee( ). The class LibraryItem has subclasses Book and
Magazine. Both subclasses implement calculateLateFee( ) and display the
late fees for each item. Create a main class to execute the program. Consider
late fees of Rs. 3 per day for Magazines and Rs. 5 per day for books.
03 Marks – Code for Abstract class & method definitions
05 Marks – code for Subclasses & its methods
02 Marks – Main & execution
abstract class LibraryItem {
int daysLate;
LibraryItem(int daysLate) {
this.daysLate = daysLate;
}
abstract double calculateLateFee( );
}
class Book extends LibraryItem {
Book(int daysLate) {
super(daysLate);
}
double calculateLateFee( ) {
return daysLate*5;
}
}
class Magazine extends LibraryItem {
Magazine(int daysLate) {
super(daysLate);
}
double calculateLateFee() {
return daysLate*3;
}
}
class Main {
public static void main(String[ ] args) {
LibraryItem b = new Book(4);
LibraryItem m = new Magazine(4);
System.out.println("Book late fee = " + b.calculateLateFee());
System.out.println("Magazine late fee = " + m.calculateLateFee());
}
}
********** 6 **********
--- page 7 ---
Q3
CO-3 A   Write an object-oriented program that defines a method divide(int a, int b),   [10]
which throws an arithmetic exception if division by zero occurs. Call this
BL-3
method from the main( ) method and handle the exception.
04 Marks – Code for Divide method & throws exception
04 Marks – Appropriate code for Exception Handling in main
02 Marks – main method & call to divide
class ThrowsDivision {
static int divide(int a, int b) throws ArithmeticException {
return a / b;
}
public static void main(String[] args) {
try {
int result = divide(10,0);
System.out.println("Result = " + result);
}
catch(ArithmeticException e) {
System.out.println("Cannot divide by zero.");
}
}
}
CO-5 B   What is the Singleton design pattern? Use the Singleton design pattern to   [10]
create a program that creates only one instance.
BL-3
05 Marks – Description of Singleton
05 Marks – Suitable programming example
Singleton
-   Singleton is a creational design pattern
-   It ensures a class has only one instance
-   It provides a global access point to that instance
-   Singleton design pattern ensures that only one instance of the class
will be created and that instance will have global access within the
application.
- The Singleton pattern works by:
o Making the constructor private
▪ Prevents object creation from outside the class
o Creating a static instance variable
▪ Holds the single object of the class
o Providing a public static method (getInstance())
▪ Returns the same instance every time
- Programming Example
Singleton
-instance:Singleton
-Singleton( )
+getInstance()
********** 7 **********
--- page 8 ---
class Singleton {
private static Singleton instance;
private Singleton( ) {
System.out.println("Singleton Instance Created");
}
public static Singleton getInstance( ) {
if (instance == null) {
instance = new Singleton( ); // created only once
}
return instance;
}
}
class Main {
public static void main(String[ ] args) {
Singleton s1 = Singleton.getInstance();
Singleton s2 = Singleton.getInstance();
System.out.println(s1);
System.out.println(s2);
// Checking if it is one object or two different Objects
if (s1 == s2) {
System.out.println("Only one instance exists!");
}
}
}
Q4
CO-2 A   Develop an Object-oriented program to maintain a database of employees   [10]
for an educational institution. The Staff class has instance variables such as
BL-3
id and name. The Teacher and Officer are inherited from Staff. The Teacher
class has an instance variable subject taught, and the Officer class has a
work type as an instance variable. Each class will have instance methods
read ( ) and show ( ). Specify all the classes and define methods to create
the database described above and to retrieve individual information.
02 Marks - Staff class, attributes & methods
02 Marks - Teacher class, attributes & methods
02 Marks - Officer class, attributes & methods
02Marks – Implementation of Inheritance
02Marks – Main, subclass object creation, and call to methods
class Staff
{
int id;
String name;
public void read(int id, String name)
{
this.id = id;
this.name=name;
}
public void show()
{
System.out.println(id);
System.out.println(name);
}
********** 8 **********
--- page 9 ---
}
class Teacher extends Staff
{
String sub_taught;
public void read( String sub_taught)
{
super.read( );
this.sub_taught=sub_taught;
}
public void show()
{
super.show( );
System.out.println(sub_taught);
}
}
class Officer extends Staff
{
String work_type;
public void read(String work_type)
{
super.read( );
this.work_type=work_type;
}
public void show()
{
super.show( );
System.out.println(work_type);
}
}
class Retreive
{
public static void main(String args[])
{
Officer of=new Officer();
of.read(10, "Rohit");
of.read("Lab Manager");
of.show();
Teacher t=new Teacher();
t.read(20, "Virat");
t.read("physics");
t.show();
}
}
CO-1 B   What are arrays? Explain how to declare, initialise, and create them with a   [10]
BL-3   programming example.
02 Marks – Array
01 Mark – Declaration
01 Marks – Initialisation
01 Mark – Creation
05 Mark- Programming Example
********** 9 **********
--- page 10 ---
- An array is a collection of a fixed number of elements of the same
type. There are situations where we might wish to store a group of
similar type of values in a variable.
- An array is a memory space allocated that can store multiple values
of the same data type, in contiguous locations.
-   This memory space, which can be perceived to have many logical
contiguous locations, can be accessed with a common name.
- A specific element in an array is accessed by the use of a subscript
or index used in brackets, along with the name of the array.
- For example, marks[5]would mean marks of 5th student.
- While the complete set of values is called an array, the individual
values are known as elements.
- Arrays can be of two types:
o one-dimensional array
o multi-dimensional array
Declaring an array
•   Declaring an array is the same as declaring a normal variable, except
that you must use a set of square brackets with the variable type.
• There can be two ways [Syntax] in which an array can be declared.
– type arrayname[ ];
– type[ ] arrayname;
• For e.g.
int marks[ ]; or
int[ ] marks;
Creating memory locations
• An array is more complex than a normal variable, so we have to
assign memory to the array when we declare it.
• We can assign memory to an array by specifying its size.
Interestingly, our same old new operator helps in doing the job, just
as shown below:
– Arrayname = new type [size];
•   So, allocating space and size for the array named marks can be done
as,
– marks = new int[5];
Initialising an array
• Assignment of values to an array, which can also be termed as
initialisation of an array, can be done as follows,
– Arrayname[index] = {list of values}
– Ex int a[ ] = {1,2,3,4,5}
class ArrayTest {
public static void main(String[ ] args) {
int a[]; // Declaration
a = new int [5]; //creation
for(int e:a)
System.out.print(e+ " " ); //displays 0 0 0 0 0
System.out.println( );
int[ ] marks = new int[ ]{12,45,67,89,90}; // initialization
for(int i=0;i<marks.length;i++)
System.out.print(marks[i]+ " ");
********** 10 **********
--- page 11 ---
}
}
Q5
CO-1 A   Define a class named GradeTest with a method gradeCheck(int) that accepts   [10]
marks as a parameter and classifies the score based on the range: display A
BL-3
if 90-100, B for 80-90, C for 70-80, D for 60-70, E for 50-60, F for 0-50,
and indicate invalid otherwise. Write a complete object-oriented
programming (OOP) program to demonstrate this scenario.
02 Mark – GradeTest class
02 Marks – gradeCheck method
04 Marks -Grade Check Logic
02 Marks – main, object creation and method call
class GradeTest {
void gradeCheck(int marks) {
if (marks >= 90 && marks <= 100) {
System.out.println("Grade: A");
}
else if (marks >= 80 && marks < 90) {
System.out.println("Grade: B");
}
else if (marks >= 70 && marks < 80) {
System.out.println("Grade: C");
}
else if (marks >= 60 && marks < 70) {
System.out.println("Grade: D");
}
else if (marks >= 50 && marks < 60) {
System.out.println("Grade: E");
}
else if (marks >= 0 && marks < 50) {
System.out.println("Grade: F");
}
else {
System.out.println("Invalid Marks");
}
}
public static void main(String[] args) {
GradeTest obj = new GradeTest();
int marks = 85;
obj.gradeCheck(marks);
}
}
********** 11 **********
--- page 12 ---
CO-4 B   What are wrapper classes? Explain how wrapper classes assist with data   [10]
conversion. Develop a program that reads three numbers as Strings,
BL-3
converts them into integers using wrapper class methods, and calculates the
sum and average.
02 Marks – Wrapper class
03 Marks – List of wrapper classes
05 Marks – Program to read three numbers & its conversion
Wrapper Classes
- Wrapper classes are predefined classes in Java.
- Wrapper classes are used to convert between primitive data types
and objects.
- Wrapper classes provide a way to use primitive data types (int,
boolean, etc..) as objects
- Each primitive type has a corresponding wrapper class.
List of Wrapper classes:
Primitive Data Type Wrapper Class
byte   Byte
short   Short
int   Integer
long   Long
float   Float
double   Double
boolean   Boolean
char   Character
Wrapper classes provide methods that make conversion easy:
String → Primitive Conversion
Using methods like:
- Integer.parseInt()
- Double.parseDouble()
import java.util.Scanner;
class WrapperDemo {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int sum = 0;
for(int i = 1; i <= 3; i++) {
System.out.print("Enter number " + i + " (as String): ");
String input = sc.nextLine();
// String to integer conversion using wrapper class
int num = Integer.parseInt(input);
********** 12 **********
--- page 13 ---
sum += num;
}
double average = (double) sum / 3;
System.out.println("Sum = " + sum);
System.out.println("Average = " + average);
}
}
Q6
CO-5 A   Create a class ComplexNumber with real and imaginary parts as instance   [10]
variables to represent a complex number (a + bi). Develop an object-
BL-3
oriented program that utilizes a generic class StoreComplexNumber to
store, input, and output a complex number using a user-defined Complex
class. Use the constructor to store the number, and provide methods to read
and
display it.
02 Marks – Complex Number Class
02 Marks – Generic Class Definition
02 Marks – Read Complex no in generic class
02 Marks – Display Complex no in generic class
02 Marks – main method, generic class object and method call
import java.util.Scanner;
class ComplexNumber {
double real;
double imaginary;
}
class StoreComplexNumber<T> {
private T obj;
public StoreComplexNumber(T obj) {
this.obj = obj;
}
public void read() {
Scanner sc = new Scanner(System.in);
ComplexNumber c = (ComplexNumber) obj;
System.out.print("Enter real part: ");
c.real = sc.nextDouble();
System.out.print("Enter imaginary part: ");
c.imaginary = sc.nextDouble();
}
public void display() {
ComplexNumber c = (ComplexNumber) obj;
System.out.println("CompNo: " + c.real + " + " + c.imaginary + "i");
}
********** 13 **********
--- page 14 ---
}
class Main {
public static void main(String[] args) {
ComplexNumber c1 = new ComplexNumber();
StoreComplexNumber<ComplexNumber> store = new
StoreComplexNumber<>(c1);
store.read();
store.display();
}
}
CO-2 B   Use your knowledge of Object-Oriented Programming to distinguish [10]
BL-3   between the following.
- Methods and Constructors
-   Encapsulation and Abstraction
05 Marks – Method and Constructor - at least 4 valid points &
example
05 Marks - Encapsulation and Abstraction – at least 2-3 valid points
and example
Constructor   Method
It is a special method having the   It can have any name
same name as the class
Used to create an object and   It shows the behavior of an object
initializes an instance variable
To invoke the constructor, the   An object or class is required
new operator is required
It is not static   It is static or non-static
It is not inherited   It is inherited
Constructor overriding is not   Overriding is possible
possible
class Student {   Example:
private String name;   public class Calculator {
public Student() {   public int add(int a, int b) {
System.out.println("Default");   return a + b;
}   }
public double add(double a, double
public Student(String name) {   b) {
System.out.println("Parameterized");   return a + b;
}   }
public static void main(String[] args)   public static void main(String[]
{   args) {
new Student();   Calculator calc = new
new Student(" ");   Calculator();
}
}   calc.add(2, 3);
calc.add(2.5, 3.7);
}
}
********** 14 **********
--- page 15 ---
Encapsulation and Abstraction
Abstraction:
- Abstraction means hiding the implementation details
- Abstraction = User knows what to do, not how it is done
- Abstraction means showing only the essential features to the user and
hiding the internal implementation details.
Encapsulation:
- Encapsulation involves bundling data and methods (functions) into a
single unit.
- The term 'Encapsulation' is similar to enclosing something inside a
capsule.
- This process involves concealing all internal details of an object from the
external environment.
- Encapsulation = Data   is hidden + accessed only through
methods/functions
-
Example:
class EncapsulationAbstractionTest{
private int data;
public void setterMethod( ){
data = 100;
}
public void getterMethod( ){
System.out.println(data);
}
} //Encapsulation
class MainTest{
public static void main(String args[ ]){
EncapsulationAbstractionTest eat = new
EncapsulationAbstractionTest( );
eat.setterMethod( ); //abstraction
eat.getterMethod( );
}
}
Q7
CO-3 A   Write an object-oriented program that copies a file's contents to another   [10]
using byte streams. The program should prompt the user for source and
BL-3
destination filenames, manage exceptions properly, and display a success
message upon completion.
01 Marks – Reading file names from user
02 Marks - File Opening in Read mode
02 Marks – File Opening in Write mode
04 Marks – Copying File Contents
01 Mark – Appropriate Exception Handling
********** 15 **********
--- page 16 ---
import java.io.*;
import java.util.Scanner;
class FileCopyByte {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter source file: ");
String source = sc.nextLine();
System.out.print("Enter destination file: ");
String dest = sc.nextLine();
try{
FileInputStream fis = new FileInputStream(source);
FileOutputStream fos = new FileOutputStream(dest);
int data;
while ((data = fis.read()) != -1) {
fos.write(data);
}
System.out.println("File copied successfully.");
} catch (IOException e) {
System.out.println("Error: " + e.getMessage());
}
}
}
CO-1 B   Build an object-oriented program to determine whether a specified number   [05]
lies within the range of 50 to 100 (inclusive)
BL-3
02 Marks – Class & main method
03 Marks – Code for Checking number between 50 and 100
public class NumberRangeChecker {
public void checkRange(int number) {
System.out.print(number + " ");
if (number >= 50 && number <= 100) {
System.out.println("is WITHIN range 50-100");
} else {
System.out.println("is OUTSIDE range 50-100");
}
}
public static void main(String[] args) {
NumberRangeChecker obj = new NumberRangeChecker( )
obj.checkRange(75);
}
}
CO-2 C   Apply your understanding of Polymorphism to explain run-time   [05]
polymorphism with a suitable programming example.
********** 16 **********
--- page 17 ---
BL-3
02 Marks – Run Time Polymorphism
03 Marks – Programming Example
- Runtime polymorphism, also known as dynamic method
dispatch or late binding, is a core object-oriented programming
concept where an overridden method's call is resolved at runtime,
rather than compile time.
-   This mechanism allows a single action to be performed in different
ways depending on the actual type of the object
- Runtime polymorphism requires an "is-a" relationship
(inheritance) between classes, where a subclass extends a
superclass.
-   It involves a superclass reference variable pointing to a subclass
object. The type of reference is the parent class, but
the object instance is of the child class. (upcasting)
Example:
class Animal {
void sound( ) {
System.out.println("Animal sound");
}
}
class Cat extends Animal {
void sound( ) {
System.out.println("Cat meows");
}
}
class Main {
public static void main(String[] args) {
Animal a = new Cat( );
a.sound( );
}
}
X------------------------------------------------------------------------------------------------------------X
********** 17 **********
````
