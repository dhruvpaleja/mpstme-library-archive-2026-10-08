# Object Oriented Programming and Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper a8abe3901ca2

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/BTech_CSE_DS_7011/Object Oriented Programming and Design/ANS_Object Oriented Programming and Design(702CO0C005)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2025
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Object Oriented Programming and Design
Date: 08 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume Suitable data if necessary.
5. Draw Neat and clean diagram wherever necessary.
6. Question 1 is Compulsory
7. Answer any 4 out of rest questions.
Q1   Answer all
A -   List down at least 5 different features of object-oriented programming [05]
CO-1   paradigm which is not common with procedural programming language.
BL-1   [01 Mark
The following features of OOP Paradigm are not common with procedural per
language.   point]
1. Polymorphism
2. Inheritance
3. Class and Objects
4. Operator Overloading
5. Data Hiding
B   Describe at least 5 advantages of using Object oriented programming   [05]
CO-2   paradigm.
BL-2   1 mark
Students may write 5 valid benefits:   per point
1.   It is possible that multiple instances of objects co-exist without any
interference,
2.   It is very easy to partition the work in a project based on objects.
3.   It is possible to map the objects in problem domain to those in the
program.
4. The principle of data hiding helps the programmer to build secure
programs which cannot be invaded by the code in other parts of the
program
5. The data-centered design approach enables us to capture more details
of the model in an implementable form.
C   [05]
CO-3   Write program in C++ to demonstrate the usage of friend class and friend
BL-4   function.   2.5
Marks for
Sample code for friend class:   each sub
question
********** 1 **********
--- page 2 ---
// C++ Program to demonstrate the
// functioning of a friend class
#include <iostream>
using namespace std;
class GFG {
private:
int private_variable;
protected:
int protected_variable;
public:
GFG()
{
private_variable = 10;
protected_variable = 99;
}
// friend class declaration
friend class F;
};
// Here, class F is declared as a
// friend inside class GFG. Therefore,
// F is a friend of class GFG. Class F
// can access the private members of
// class GFG.
class F {
public:
void display(GFG& t)
{
cout << "The value of Private Variable = "
<< t.private_variable << endl;
cout << "The value of Protected Variable = "
<< t.protected_variable;
}
};
// Driver code
int main()
{
GFG g;
F fri;
fri.display(g);
return 0;
}
Sample code for Friend function
// C++ program to create a global function as a friend
// function of some class
#include <iostream>
using namespace std;
class base {
private:
int private_variable;
********** 2 **********
--- page 3 ---
protected:
int protected_variable;
public:
base()
{
private_variable = 10;
protected_variable = 99;
}
// friend function declaration
friend void friendFunction(base& obj);
};
// friend function definition
void friendFunction(base& obj)
{
cout << "Private Variable: " << obj.private_variable
<< endl;
cout << "Protected Variable: " <<
obj.protected_variable;
}
// driver code
int main()
{
base object1;
friendFunction(object1);
return 0;
}
D   [05]
CO-3   Write a program in C++ to override a function.
BL-4
Students may write a code exhibiting the use of virtual functions.
Example code is given below
#include<iostream>
using namespace std;
class B
{ public: int b;
};
class D1 : virtual public B {
public: int d1;
};
class D2 : virtual public B {
public: int d2;
********** 3 **********
--- page 4 ---
};
class D3 : public D1, public D2 { public: int d3;
};
int main() {
D3 obj;
obj.b = 40; // statement 3
obj.b = 30; // statement 4
obj.d1 = 60;
obj.d2 = 70;
obj.d3 = 80;
cout<< "\n B : "<< obj.b;
cout<< "\n D1 : "<< obj.d1;
cout<< "\n D2 : "<< obj.d2;
cout<< "\n D3 : "<< obj.d3;
Q2
A   [10]
CO-1   Differentiate between inline function and normal functions used in C++
BL-1   Programming language.
When the program executes the function call instruction, the CPU
perform following task
Stores the memory address of the instruction following the function call
Copies the arguments of the function on the stack and finally transfers
control to the specified function.
The CPU then executes the function code.
Stores the function return value in a predefined memory location/register
and returns control to the calling function.
This can become overhead if the execution time of function is less than
the switching time from the caller function to called function.
For functions that are large and / or perform complex tasks, the overhead
of the function call is usually insignificant compared to the amount of
time the function takes to run.
However, for small, commonly used functions, the time needed to make
the function call is often a lot more than the time needed to actually
execute the function’s code.
This overhead occurs for small functions because execution time of small
function is less than the switching time.
C++ provides an inline function to reduce the function call overhead.
#include<iostream.h>
inline void add (int a, int b)
{ int c = a+ b; cout<<c; }
int main()
{
int x, y, z;
cin>>x>>y;
********** 4 **********
--- page 5 ---
add(x , y);
}
B   [10]
CO-2   Take an Example code of C++ and describe “Runtime Polymorphism”. Is it
BL-2   similar to compile time polymorphism? Justify
Compile-Time Polymorphism
Also known as early binding and static polymorphism, in compile-time
polymorphism, the compiler determines how the function or operator will
work depending on the context. This type of polymorphism is achieved by
function overloading or operator overloading.
#include <bits/stdc++.h>
using namespace std;
class abc {
public:
// Function to add two integers
void add(int a, int b) {
cout << "Integer Sum = " << a + b
<< endl;
}
// Function to add two floating point values
void add(double a, double b) {
cout << "Float Sum = " << a + b
<< endl ;
}
};
int main() {
abc gfg;
// add() called with int values
gfg.add(10, 2);
// add() called with double value
gfg.add(5.3, 6.2);
The function call in runtime polymorphism is resolved at runtime in
contrast with compile time polymorphism, where the compiler determines
which function call to bind at compilation. Runtime polymorphism is
implemented using function overriding with virtual functions.
#include <bits/stdc++.h>
using namespace std;
class Base {
public:
// Virtual function
virtual void display() {
********** 5 **********
--- page 6 ---
cout << "Base class function";
}
};
class Derived : public Base {
public:
// Overriding the base class function
void display() override {
cout << "Derived class function";
}
};
int main() {
// Creating a pointer of type Base
Base* basePtr;
// Creating an object of Derived class
Derived derivedObj;
// Pointing base class pointer to
// derived class object
basePtr = &derivedObj;
// Calling the display function
// using base class pointer
basePtr->display();
Q3
A   [10]
CO-3   Write a program in C++ to demonstrate the usage of Hierarchical
BL-4   inheritance.
// C++ program for Hierarchical Inheritance
#include<iostream>
using namespace std;
class A //superclass A
{
public:
void show_A() {
cout<<"class A"<<endl;
}
********** 6 **********
--- page 7 ---
};
class B : public A //subclass B
{
public:
void show_B() {
cout<<"class B"<<endl;
}
};
class C : public A //subclass C
{
public:
void show_C() {
cout<<"class C"<<endl;
}
};
int main() {
B b; // b is object of class B
cout<<"calling from B: "<<endl;
b.show_B();
b.show_A();
C c; // c is object of class C
cout<<"calling from C: "<<endl;
c.show_C();
c.show_A();
return 0;
}
B   [10]
UN-4   Write a program in C++ to discuss Hybrid inheritance in detail. Why is it
CO-3   referred to as Hybrid inheritance?
BL-4
In hybrid inheritance, within the same class, we can
have elements of single inheritance, multiple
inheritance, multilevel inheritance, and hierarchical
inheritance.
********** 7 **********
--- page 8 ---
Implementation of Virtual Base class concept
class Bank { }
class Life : public virtual Bank
{
}
class Car : public virtual Bank
{
}
class Claim : public Life, public Car
{
}
Q4
A   [10]
CO-3   Write C++ code for demonstrating the usage of function Template. Is it
BL-4   useful in generic programming? Why?
A significant benefit of object oriented programming is reusability of the
code which eliminates redundant coding.
Functions
Classes
The method of Generic Programming is implemented to increase the
efficiency of the code.
Generic Programming enables the programmer to write a general
algorithm which will work with all data types.
It eliminates the need to create different algorithms if the data type is an
integer, string or a character.
The advantages of Generic Programming are
Code Reusability
Avoid Function Overloading
Once written it can be used for multiple times and cases.
C++ routines work on specific types.
We often need to write different routines to perform the same operation
on different data types.
int maximum (int a, int b, int c)
{
if(a>b)
{ if (a>c) return a;
********** 8 **********
--- page 9 ---
else return c; }
else {
if (b > c) return b;
else return c; }
}
We often need to write different routines to perform the same operation
on different data types.
float maximum(float a, float b, float c)
{
if(a>b)
{ if (a>c) return a;
else return c; }
else {
if (b > c) return b;
else return c; }
The logic is exactly the same, but the data type is different.
Function templates allow the logic to be written once and used for all
data types – generic function.
//Generic function to find a maximum value
#include<iostream>
using namespace std;
template <typename T>
T maximum(T a, T b, T c)
{
if(a>b)
{ if (a>c) return a;
else return c; }
else {
if (b > c) return b;
else return c; }
B   [10]
CO-2   Explain following with C++ code example: fstream, ofstream, ifstream,
BL-2   iostream, cin, cout, namespace std, ios::app, ios::in, ios::out.
fstream- Library defining the clases, functions related file manipulation
ofstream,- output file stream class used for file manipulation for writing
into the file in c++
Ifstream- input file stream class used for file manipulation for reading
from the file in c++
Iostream – Input output stream library defining the I/O related classes,
objects
Cin – input stream object of istream, used for collecting input from
keyboard.
cout,- output stream object of ostream, used for displaying output on
monitor.
namespace std- in C++, a namespace is a declarative region that
provides a scope to the identifiers (names of functions, variables, or
********** 9 **********
--- page 10 ---
other user-defined data types) inside it. The std namespace is a
standard namespace that contains all the identifiers of the C++
Standard Library, such as functions, classes, and object
ios::app- used for opening the file in append mode.
ios::in – used to open file in input mode
ios::out – used to open the file in output mode
Object.open(“abc.txt”, ios::app)
Object.open(“abc.txt”, ios::in)
Object.open(“abc.txt”, ios::out)
Q5
A   [10]
CO-4   Design sequence Diagram and activity Diagram for following storyline.
BL-4   “Faculty maintains the student's attendance” of his class. He also maintains
the grades for following assessment tools: Lab, assignment, Mini project,
practical exam. Students can access his grades by requesting it to grade
class.”
Students are expected to identify classes and objects and draw a sequence
diagram depicting the sequence of communication among objects as per
the storyline given. Diagram must follow standard notations. [5 Marks]
Activity diagram depicting the sequence of steps taken to solve the
problem given in the storyline. Students must draw it as per the standard
notations followed. [5 Marks]
B   [10]
CO-1   Differentiate between following programming constructs w.r.t.
BL-1   Procedural and Object Oriented.
a. Structure variable and objects and its usage in code [5 Marks]
b. Inline function and macro. [5 Marks]
struct myStructure {
int myNum;
char myLetter;
};
int main() {
struct myStructure s1;
return 0;
}
/ C++ program to demonstrate accessing of data members
#include <bits/stdc++.h>
using namespace std;
class GS {
private:
string geename;
// Access specifier
public:
// Member Functions()
void setName(string name) { geename = name; }
void printname() { cout << "Geename is:" <<
geekname; }
********** 10 **********
--- page 11 ---
};
int main()
{
// Declare an object of class geeks
GS obj1;
// accessing data member
// cannot do it like: obj1.geekname = "Abhi";
obj1.setName("Abhi");
// accessing member function
obj1.printname();
return 0;
}
B. Macro in c
/ Macro definition
#define DATE 31
int main()
{
// Print the message
printf("Lockdown will be extended" " upto %d-MAY-2020",
DATE);
#include <stdio.h>
#define PI 3.14159
int main()
{
printf("The value of PI is: %f\n", PI);
return 0;
}
Inline function in c++
#include <iostream>
using namespace std;
class A {
public:
// declare inline
inline int square(int x);
};
// Define the function
inline int A::square(int x) {
return x*x;
}
int main() {
A obj;
cout << obj.square(3);
return 0;
}
Students can explain the differences among codes and
its advantages and disadvantages
********** 11 **********
--- page 12 ---
Q6
A   [10]
CO-3   Write a program and explain the concept: array of objects and pointer of
BL-4   objects.
Array of objects:
#include<iostream>
using namespace std;
class Employee
{
int id;
char name[30];
public:
// Declaration of function
void getdata();
// Declaration of function
void putdata();
};
// Defining the function outside
// the class
void Employee::getdata()
{
cout << "Enter Id : ";
cin >> id;
cout << "Enter Name : ";
cin >> name;
}
// Defining the function outside
// the class
void Employee::putdata()
{
cout << id << " ";
cout << name << " ";
cout << endl;
}
// Driver code
int main()
{
// This is an array of objects having
// maximum limit of 30 Employees
Employee emp[30];
int n, i;
cout << "Enter Number of Employees - ";
cin >> n;
// Accessing the function
for(i = 0; i < n; i++)
emp[i].getdata();
cout << "Employee Data - " << endl;
// Accessing the function
for(i = 0; i < n; i++)
********** 12 **********
--- page 13 ---
emp[i].putdata();
}
Pointer of Object:
#include <iostream>
using namespace std;
class My_Class {
int num;
public:
void set_number(int value) {num = value;}
void show_number();
};
void My_Class::show_number()
{
cout << num << "\n";
}
int main()
{
My_Class object, *p; // an object is declared and a pointer to it
object.set_number(1); // object is accessed directly
object.show_number();
p = &object; // the address of the object is assigned to p
p->show_number(); // object is accessed using the pointer
return 0;
}
B   [10]
CO-2   Explain following in C++ Code: Attributes, Behavior, Relation between
BL-2   two classes, Communication between two classes, Security of data in the
class. [2 Marks each]
Attributes: These are data members of the class, depicting relevant and
related data of the class used by member functions.
Behavior: Member function of the class. These are actions what any
object can perform.
Relation between two classes: Two classes can be related by means of
three main relationships:
•   Association
•   Aggregation
•   Specialization
Communication between two classes:
Two classes can pass data to each other through their member functions
(methods)
Security of data in the class: Data members are private by default in the
class. Such data members are accessible only to member function of that
********** 13 **********
--- page 14 ---
class. Other outside functions cannot have access of these private data
elements.
Students are expected to write a code snippet to explain them.
********** 14 **********
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper 148c8de0afeb

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/BTech_CSE_DS_7011/Object Oriented Programming and Design/ANS_Object Oriented Programming and Design(702CO0C005)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2025
- Text: mixed (11 pages), mean OCR confidence 42.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Object Oriented Programming and Design
Date: 10 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume Suitable data if necessary.
5. Draw Neat and clean diagram wherever necessary.
6. Question 1 is Compulsory
7. Answer any 4 out of rest questions.
Q1   Answer all
A -   “Object Oriented Programming paradigm   is   different than [05]
UN-1   Procedural Language” Justify this statement with five distinct
CO-1   points.
BL-1
•   Procedure Oriented Programming   1 mark per
•   Emphasis is on doing things (algorithms), so procedures (Functions) are important   point.
•   Large programs are divided into smaller programs known as functions
•   Most of the functions share global data, may be facing issue of Data Inconsistency
•   Function can communicate with each other through parameters, so data can flow freely between functions
•   Data security is not possible
•   Uses top-down approach in the program design
•   Object Oriented Programming
•   Emphasis is on using things (data), so data is important than functions
•   Programs are divided into objects rather than functions
•   Data is hidden and cannot be accessed by unauthorised function (External function), maintain data
consistency
•   Objects communicate with each other so, data cannot move freely between all the functions
•   Data security has utmost importance
•   Uses bottom –up approach in program design
B   Describe various methods of securing data in object-oriented   [05]
UN-2   programming. Compare “Private” “Public” and “Protected” mode of
CO-2   accessibility for the same.
BL-2   3 marks for
Private data is accessible only to the member functions of the   explanation
class in which the data is declared as member data.   and 2
marks for
Public data is accessible to all functions outside the class in which code
it is declared as member data.
********** 1 **********
--- page 2 ---
Protected data is accessible to member functions of child class of
the parent class in which the data is declared as protected.
Students are expected to write a code snippet to explain it.
C   [05]
UN-3   Write program in C++ and demonstrate various usage of scope
CO-3   resolution operator ( : : ).   1 mark
BL-4   each point
Usage:
1. Declaration of member function outside the class
2. Differentiating between local and global variables declared
with same name.
3. Avoiding usage of “using namespace std” and accessing
the cin and cout – std::cin
4. Using the file manipulation mode while opening the file i.e.
ios::in
5. Differentiating between variables with same name in
different blocks.
D   [05]
UN-4   Write a program in C++ to overload any mathematical operator.
CO-3
BL-4   Students can write any code related to the concept. A sample
code is given below:
class complex {
double real, imag;
public:
complex() { }
complex(double r, double i)
{ real = r ; imag = i;}
complex operator+(complex a);
complex operator*(complex a);
void printComplex()
{
cout<<real<<“+I” <<imag;
}
};
complex complex :: operator + (complex c)
{ complex c1;
c1.real = real + c.real;
c1.imag = imag + c.imag;
return c1; }
int main()
{
complex a (2.3, 3.4);
complex b (2.8, 3.6);
complex c, d;
c = a + b; //invoking + operator function
c.printComplex();
d = c * b; //invoking * operator function
d.printComplex();
}
********** 2 **********
--- page 3 ---
Q2
A   [10]
UN-1   Differentiate between Pass by Value and Pass by reference with
CO-1   an example code in C and C++.
BL-1
B   [10]
UN-2   Take an Example code of C++ and describe “Encapsulation”. Can
CO-2   two objects of the same class have the same copy of their
BL-2   attributes? Justify.
Encapsulation is a process of combing data and function into single
unit called class
Data is only accessible through the functions present inside the
class
Hiding the implementation details from external entity, led data
abstraction
Encapsulation led to the important concept of data hiding
Implemented by defining class
Only public members are accessible for external entity like main ()
and non-member functions [2.5 Marks]
class student
{
private: // Access modifier
char name[20];
int total_Marks;
float Percentage;
public: // Access modifier
void readData()
calculate_Per()
void Printdata()
}s1,s2; //Global declaration of objects. [2.5 Marks]
two objects of the same class do not have the same copy of their
attributes.
objects are the basic run time entities in an object-oriented system
Member objects constructed in the order they declared
Each object has its own copy of data
May be objects of any type
Member functions are operated on calling object (current)
Each object shares same copy of functions
Initially object have no values while declaring:
They need to initialize by using following
Member Functions
Constructor
[5 Marks]
Q3
A   [10]
UN-3   Write a program in C++ to demonstrate the usage of constructor
CO-3   and Destructor. Why is the use of these two constructs
BL-4   considered good programming habits?
********** 3 **********
--- page 4 ---
5 Marks for
class add   code
{
int m, n ;   5 Marks for
public :   sub
add ()   question
{
m=100;
n=50
}
------
};
class add
{
int m, n ;
public :
add ( ) {m = 0 ; n = 0 ;}
add (int a, int b)
{m = a ; n = b ;}
add (add &obj)
{m = obj.m ; n = obj.n ;}
};
int main()
{
add o1;
add o2(10,20);
add obj (o2);
o1.print();
o2.print();
obj.print();
}
#include<iostream>
using namespace std;
class Bank_Account
{
char cust_name[30];
long int account_No;
public:
Bank_Account()
{
cout<<"enter details of the customers :"<<endl;
cin>>cust_name;
cin>>account_No;
}
void print()
{
cout<<"details of the customers are:"<<endl;
cout<<cust_name<<endl;
cout<<account_No<<endl;
}
********** 4 **********
--- page 5 ---
~Bank_Account()
{
cout<<"Destructor has been called"<<endl;
cout<<"Removed object (customer) from the
memory :"<<account_No<<endl;
}
};
int main()
{
Bank_Account C1;
C1.print();
{
Bank_Account C2;
C2.print();
}
{
Bank_Account C3;
C3.print();
}
Bank_Account C4,C5;
C4.print();
C5.print();
}
Constructors should be declared in the public section.
They are invoked automatically when the objects are created.
They do not have return types, not even void and they cannot
return values.
They cannot be inherited, though a derived class can call the base
class constructor.
Like other C++ functions, Constructors can have default
arguments.
Constructors cannot be virtual.
They make ‘implicit calls’ to the operators new and delete when
memory allocation is required.
When a constructor is declared for a class initialization of the class
objects becomes mandatory.
Avoids garbage values in the data members.
B   [10]
UN-4   Write a program in C++ to differentiate between single level
CO-3   inheritance and multiple inheritance.
BL-4
Single Level [5 marks]
#include <iostream>
class BaseClass {
Data members;
public:
********** 5 **********
--- page 6 ---
Members functions;
};
class DerivedClass : public BaseClass
{
Data members:
public:
Member function;
};
int main( )
{
DerivedClass D1,D2;
}
Multiple Inheritance [5 marks]
class ABC
{
int a, b;
public:
ABC(int a1,int b1){a=a1; b=b1;}
void putab(){cout<<"ABC class"<<endl;
cout<<a<<endl<<b;}
~ABC(){cout<<endl;
cout<<"ABC class destructor";}
};
class XYZ
{
int x, y;
public:
XYZ(int x1,int y1){ x=x1; y=y1;}
void putxy(){cout<<endl<<"XYZ class";
cout<<endl<<x<<endl<<y;}
~XYZ(){cout<<endl;
cout<<"XYZ class destructor";}
};
class ABC1 : public ABC, public XYZ
{
int x1, y1;
public:
ABC1(int x2, int y2) : ABC(x2,y2), XYZ(x2,y2)
{ x1=x2; y1=y2;}
void putx1y1(){ cout<<endl<<"ABC1 class";
cout<<endl<<x1<<endl<<y1;}
~ABC1(){cout<<endl;
cout<<"Derived class destructor";}
};
int main()
{
ABC1 X(10,20);
X.putab();
X.putxy();
********** 6 **********
--- page 7 ---
X.putx1y1();
}
Q4
A   [10]
UN-5   Write C++ code for demonstrating the usage of Class Template.
CO-3   Why is such generic programming useful in optimal coding?
BL-4
[5 Marks for code]
template <typename T>
class Array {
private:
T* ptr;
int size;
public:
Array(T arr[], int s)
{
ptr = new T[s];
size = s;
for (int i = 0; i < size; i++)
ptr[i] = arr[i];
}
void print()
{
for (int i = 0; i < size; i++)
cout << " " << *(ptr + i);
cout << endl;
}
};
int main()
{
int arr[5] = { 1, 2, 3, 4, 5 };
Array <int> a(arr, 5);
a.print();
float arr1[] = {2.3, 2.4, 3.4, 4.5, 5.6};
Array <float> a1(arr1,5);
a1.print();
return 0;
}
[5 Marks for logical explanation] Sample answer is given below.
Templates are used to parameterize classes and functions with
different types
Function templates allow writing generic functions that work on
many types.
Function templates do not require explicit declaration of
parameterized types when called
E.g., maximum(i, j, k);
********** 7 **********
--- page 8 ---
Same idea applies to defining generic classes that work with many
types -- extract the type to be a template to make a generic
classes.
Classes require explicit declaration of parameterized types when
instantiated
E.g., vector <int> v;
B   [10]
UN-6   Explain. 7 different steps mandatorily to be used while writing the
CO-2   C++ code to implement reading data from file.   1 mark per
BL-2   step and 3
1. #include <fstream>   marks for
2. Ifstream ifile; // object declaration in read mode   accurate
3. Ifile.open(“abc.txt”) //open the file in read mode   explanation
4. Ifile.fail() // check for failure to open the file.   ]
5. Ifile>>name //Read the data from file
6. Cout<<name //display the read data.
7. Ifile.close() // close the file
Q5
A   [10]
UN-7   Design Use Case Diagram and Class Diagram for following
CO-4   storyline. “Library maintains the record of students [name, roll no,
BL-4   class, email etc. It also maintains the records of books i.e. Book title,
Author name, ISBN, Publisher etc. Student can request for the book
from the records wherein list of books can be displayed by system”
B   [10]
UN-1   Differentiate between following programming constructs w.r.t.
CO-1   Procedural and Object Oriented.
BL-1   a. Structure and Class. [5 Marks]
b. Accessing Local and Global Variables
a. Structure in C /C++ :
struct {   // Structure declaration
int myNum;   // Member (int variable)
string myString;   // Member (string variable)
} myStructure;   // Structure variable
class ThisClass {
public:
int var;   // data member
void print() {   // member method
cout << "Hello";
}
};
Valid differentiating points are expected.
b. void myFunction() {
// Local variable that belongs to myFunction
********** 8 **********
--- page 9 ---
int x = 5;
// Print the variable x
printf("%d", x);
}
int main() {
myFunction();
return 0;
}
#include <iostream>
using namespace std;
// Declaring first variable
int a = 10;
int main() {
// Declaring second variable
int b = 9;
// Accessing a and b variable in their scope
cout << a << " " << b;
return 0;
}
Q6
A   [10]
UN-2   Write a program and explain the concept of Class, Object,
CO-3   Member function, Data Member, Access Specifier. [2 Marks per
BL-4   point]
Class: In C++, a class is a user-defined data type that
encapsulates data (attributes or variables) and functions (methods
or operations) that act on that data, serving as a blueprint for
creating objects
Object: n C++, an object is a concrete instance of a class,
representing a self-contained entity with data (attributes) and
behavior (methods).
Member function : In C++, a member function is a function
declared inside a class definition, and it operates on the data
members of that class, allowing access to and manipulation of the
class's data
Data Member: Data members include members that are declared
with any of the fundamental types, as well as other types,
including pointer, reference, array types, bit fields, and user-
defined types.
Access Specifier: n C++, access specifiers (public, private,
protected) control the visibility and accessibility of class members,
********** 9 **********
--- page 10 ---
determining how and where they can be accessed, crucial for
encapsulation and data hiding.
Code snippet:
class MyClass {
public:   // Public access specifier
int x;   // Public attribute
private:   // Private access specifier
int y;   // Private attribute
};
int main() {
MyClass myObj;
myObj.x = 25; // Allowed (public)
myObj.y = 50; // Not allowed (private)
return 0;
}
B   [10]
UN-3   Explain multiple usage of this-> operator in C++ Code.
CO-2   Distinguishing Member and Local Variables: When a member
BL-2   variable and a local variable (inside a function) have the same
name, this-> clarifies which one you're referring to.
class MyClass {
public:
int value; // Member variable
void setValue(int value) { // Member function
this->value = value; // Accessing the member variable
}
};
Returning the Current Object: Member functions can return the
current object using this.
class MyClass {
public:
MyClass& increment() {
// ... some logic to increment the object ...
return *this; // Return a reference to the current object
}
};
Accessing Member Variables and Functions: this-> provides a way
to access and manipulate data members and member functions
within other member functions.
class MyClass {
public:
int value;
void printValue() {
std::cout << this->value << std::endl; // Accessing member
********** 10 **********
--- page 11 ---
Variable

}

2

FRI ICR 7 FI OH
````
