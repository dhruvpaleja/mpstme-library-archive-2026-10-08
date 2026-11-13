# Java and Web Technologies: question papers in full

5 unique papers · 2008-09 to 2012-13 · Computer Applications (MCA)

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2012-13 · Re-Exam · Trim 5 · paper d36f058720b5

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/TRIM V/JAVA AND WEB TECHNOLOGIES/JAVA & WEB TECHNOLOGIES V MCA 2012-13 RE EXAM(1).pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15/6/2013
- Text: text (3 pages)

````text
- -   ,   . -- f,,.-*m!l& --   -   . ~~,
SVKM's ImpIs   -.
:b"' .9rM
Muhesh - Patel . . . . Scho6l . ~   of Technology Manascement & Engjneering   P
ogramrue:   I.CA~-   ,--- . .   Year:   I1   Trimester: V   iI   ,   ,   ., , Y
'. , .: . Academic Year :2012-2013   /$c   R A
Batch:   2012-13 '.: ;,;.;   .   , .   \$Cr& b
1 ,   Subject:   .   Java &   %&%nologies c .   Marks:   100
I   Time:   2.00prn To 5.00pm. -
Date:   15/6/2013 '   : ' .   "'1   '   Duration:   3hrs.
$   .   .   Re - Examination'
-. @ :..   .   .   ....   .. .
' Instructions: Candidates should read carefully the instructions printed on the question paper and on the
Cover of the Answer Book, which is provided for their use.
NB:   1.Question No. 1 is compulsory.
2. Out of remaining 5 questions, attempt any 4 questions. In all attempt 5 questions.
3. All questions cany equal marks.
4. Answer to each new question to be started on a fresh page.
5. Figure in brackets indicates full marks.
6. Give examples wherever required.
. .   Q. l(a) Find the output. Give justification for your answer.   [lo]
-
1) class ExcO extends Exception { }   2) class MyThread extends Thread
class Excl extends ExcO { ) I* Line 2 *I   {public static void main(String   args) {
public class Test {   MyThread t =new MyThreadO;
public static void main(String argso) {   t.start0;
W (   System.out.print("one. ");
throw new Exclo;} I* Lime 9 *I   t.start0;
catch (ExcO eO){ I* L i e 11 *I   System.out.print("two. ");I
System.out.println("Ex0 caught"); }   public void run0 {
catch (Exception e) {   System.out.print("Thread ");))
System.outprintln("exception
-   caught"); ) 11   (a) Compilation fails
(a) Ex0 caught   (b) An exception occurs at runtime.
@) Exception caught   (c) It prints "Thread one. Thread two".
(c) Compilation fails because of an   '   (d) The output cannot be determined.
error at line 2.
I   (d) Compilation fails because of an
a   error at line 9.
3) class Equals   4) interface x{void show();]
{public static void main(String [I args) {   class y implements x{
int x = 100;   void   B
double y = 100.1;   show~{System.out.println("show");} 1
I   .   . .   boolean b = (x =y); I*'Line 7 *I   (a) run time error
Syskm.out.println(b); )}   (b) compile time error
1   (a) true   (c) will compile hut not execute
I   (b) false   (d) will compile and execute
(c) compilation fails
I   (d) an exception is thrown at tuntime
5) String x =new String("xyz");
I   Stringy = "abc";
I   x=x+y;
i \   How many String objects have been created?
'   (a) 2   @) 3   (c) 4   (d) 5
I
Q. 1@) Attempt the following   wl
1 Which method is used to know the current state of a thread?
(a) getThreadState0   (b) getstate0   (c) get0   (d) getThreadCurrentStateO
* +\3
--- page 2 ---
..   -   .,* .. :7;   .   . .   .   ,   ,:"
.- .   .   ' ... ' t . ;:s::. C < 8   ?*>'L -   i :.';.   ,   :
---   ...- .-
Which of the following statements are true?
(a) If a class has abstract methods, it must be declared as abstract.
(b) If the abstract methods are not overridden, the subclass need not be declared as
abstract.
(c) A fmal class cannot be subclassed.
(d) All methods in an abstract class must be declared as abstract.
What will happen when you try to compile the following code?
interface test {staticvoid show0;)
(a) runtime error   (b) compile time error
(c) will compile but not execute   (d) will compile and execute.
4 Which of the following is not a property of the window object in DOM?
(a) title   (b) location   (c) history   (d) document
5 Which method is used to know the directory name from where the applet class is
loaded?
(a)getCodeBaseO   (b)getDocumentBaseQ
(c) getClassNameO   (d) getAppletLoadClass()
6 Which of the following attributes of the QcripP tag refers to an external JavaScript
source file?
(a) src   (b) ~~   (c) link   (d) href
7 How can you create an e-mail link?
(a) -ahref;"a@b>   (b) <mail>a@b4mail>
(c) a hreP"mailto:a@b.com">   (d) <mail href='a@b">
8 Which of the following is an invalid CSS selector?
(a) title   (b) table   (c) bgcolor   ( 4 body
9 What will be the output if the following declarations are there in a given sequence? If it
is not correct, what isthe correct sequence?
classx u
package y; import a,b;
(a) run time error   (b) compile time error
(c) will compile but not execute   (d) will compile and execute
10 Which of the followingproperties retums the number of elements in an array?
(a) length   (b) size   (c) elements   (d) indexes
Q. 2 Answer the following(Any 2)   1201
1 Explain method overriding concept with example. Compare it with method overloading.
2 Create a class named Employee with following details Data member (name, address,
age, gender) method (display). Create another class Manager that inherits the Employee
class having data member salary, incentive bonus (which is 20 % of salary), total salary,
method displaywhich calculate total salary and print all #he details. Create another class
Worker that inherits the Employee class having data member working hours, rate per
hour. It has method display which calculates pay and displays all details. Create objects
of derived classes and test it. Use appropriateconstructors.
3 Explain the use of super keyword with example.
3(a) Answer the following (Any 2)
1 Explain Frame tag with example.
2 Write an HTML page to createthe followinglist
BCA
B Tech
1. Chemical
2. C6mputer
3. Electronics
B Sc
--- page 3 ---
/   3 Distinguish between get and post method of form tag.
Q. 3@) Answer the following   [I41
/   1 Explain use of fmlkeyword with example.
2 Write a p r o p to cheek string is palindrome or not. Inp~t should be using command
line argument.
Q. 4 Answer the followiag (Any 2)
1 Write e program that uses thread synchronization to guarantee data integrity in a
multithreaded applicaf.ion.
2 What is an interhe? Explain its use with example? How is it different from an abstract
class?
3 Explain the concept of exception handling by writing example for handling Arithmetic
Exception.
Q. 5 (a) What is r\ Package? Explain the use of package with example. What is the difference [08]
between private, protected, default and public?
Q. 5 (b) Attempt the following (Any 1)   [I21
Explain life cycle of applet? How it is different from an application? Create an applet
which will set background color and draw circle, rectangle, and line with different calors
and reads a message from PARAM tag and display it.
Create a form with header "Process Discount for Order". It should contain a text boxes
to accept user name, email address, total order amount and a payment selection with
optionsoash on delivery, credit card, Net baaking, a text area, a reset button "Clear" & a
button "Calculate". When calculate is clicked it should provide discount on following
basis. If dicard is selected 10 % discount of total order amount, if net banking then 5
% discount of total order amount and cash on delivery no discount. Calculate payable
amountafter discmt and display the details in text area
Provide following JavaScript Validations:   .
a, The name textbox should not be left blank.
b. Validate email address.
c. If no menu selection is made then by default cash ondelivery should be selected.
Answer the fonowing (Any 2)
1 Explain client smer interaction   I
2 Explain lTRv% W M in detail
3 Create the following HTML page with font as Times Roman size 12. The table contents
should be center justified The first column and fust row filled with red color.
Innova
Seor 'o   Mahindra
Q. 6 @) Answer the following (Any 1)
1. What is Cascading Style sheet? Its types? Explain it with example.
2. What is XhfL? Compare itwith HTML.Create an XML file which stores Teacher detail
(Teacher code, name, qualification, Specialization, salary). Write DTD for the same.
313
````

## 2011-12 · Exam not stated · Trim 5 · paper 9951a1911b77

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/TRIM V/JAVA AND WEB TECHNOLOGIES/JAVA AND WEB TECHNOLOGIES 201112.pdf`
- Printed on paper: exam date: 04/02/2012
- Text: ocr (3 pages), mean OCR confidence 91.4

````text
\ — SVKM’s NMIMS
Mukesh Patel School Of Technology Management & Eng

Programme: MCA Year: Il Trimester:f f ¢
i Academic Year : 2011-2012 f3 ;
: *{ NMPir > UA versity iF
j ¥ = 1L0@vns 26.
ti JAVA & WEB TECHNOLOGIES Marks: {t g
sil Time: |, (2. ooh hint 5. 0
Date: 04/02/2012 Duration:\ eS, a J
Final - Examination on han et '4

Instructions: Candidates should read carefully the instructions printed on the question paper and on the

Cover of the Answer Book, which is provided for their use.
NB: 1. Question No. | is compulsory.

2. Out of remaining 5 questions, attempt any 4 questions. In all attempt 5 questions,
3. All questions carry equal marks.
4. Answer to each new question to be started on a fresh page.
5. Figure in brackets indicates full marks.
6. Give examples wherever required.

Q.1(a) Attempt the following [10]
1 Which type of exception does a sleep() method throw?
(a) ArithmeticException (b) NullPointerException
(c) ArrayIndexOutOfBoundsException (d) InterruptedException

2 Where do you place the onsubmit event handler?

(a) Ina submit <input> element.

(b) In the closing </form> tag

(c) In the form control that calls the submit event.

(d) In the opening <form> tag.
3 What will happen when you try to compile the following code?
i Interface test {int CHECK;}

} (a) run time error (b) compile time error
(c) will compile but not execute (d) will compile and execute.
4 Which methods are called as soon as an applet is loaded?
(a) init, start, paint (b) init, start (c) init (d) start, paint, stop
5 What are the two types of exceptions available in Java?
(a)checked and compiled (b) uncheck and compiled
(c) checked and unchecked (d) compiled and non compiled
6 Java does not support
(a) Operator overloading (b) Pointers
@ Global variables (d) All of the above
\ 7 Jfyou create a data member or method that is___, it can be used within its own class
ran any classes extended from that class.
(a) private (b) public (c) protected * (d) both b and c
.8 Which of the following tag is not written in the <head>
(a) title (b) table (c) script (d) meta

9 Which of the following syntax is used to include DTD in your XML document?
(a) <DOCTYPE root-elementfelelment-declarations]>
(b) <DOCTYPE root-element(elelment-declarations)>
(c) <!DOCTYPE root-element[elelment-declarations]>
(d) <!DOCTYPE [elelment-declarations]>
10 Which of the following properties is used to change the background color?
(a) bgcolor: red —_(b) color: red (c) background: red (d) background-color: red

Ys
--- page 2 ---
Q. 3a)

~
Answer the following (Any 5)

Distinguish between get and post method of form tag.

What is thread priority? How can it be set for a thread?

Explain the use of this keyword.

Explain the difference between instance variable and class variable.
With example explain any | way of taking input from the user.
Explain anchor tag with example

Explain any two attribute of body tag.

Answer the following (Any 2)

What are constructors used for? Can constructors be overloaded? Write a program in
support of your answer.

Create a class named Employee with following details Data member (name, address,
age, gender) method (display). Create another class FullTimeEmployee that inherits the
Employee glass having data member salary, bonus (which is 20 % of salary ),
designation, total salary, method display which calculate total salary and print all the
details. Create another class PartTimeEmployee that inherits the Employee class having
data member working hours, rateperhour. It has method display which calculate pay and
display all details. Create objects of derived classes and test it. Use appropriate
constructors. :

Explain object oriented concepts with respect to java. What makes java a platform
independent language? Give steps for how to compile and run java program.

Answer the following (Any 2)

Write an HTML page to create the following list

e MCA
e MBA
1, HR
2. Systems
3. Finance
e MSc

Distinguish between String and StringBuffer class.
Explain the use of final keyword with example.

Answer the following (Any 2)

What is an interface? Explain its use with example? How is it different from an abstract
class? :

Explain nested class with example.

Write a program to generate power Series 1, 4, 9, 16, 25...till n°, using command line
argument.

Answer the following (Any 2)

Explain thread life cycle. Which are two ways to implement multi threading concept in
java explain any 1 with example.

Explain the concept of exception handling with example.

Explain how the concept of overriding of method with example. How it is different from
overloading.

b

[20]

[06]

[14]

[20]
--- page 3 ---
a) Answer the following (Any 2) {08}

} What is the use of final keyword? Explain it.

2 What is a Package? Why package is needed? Give syntax for how to include a package
and create a package.

3 Explain image tag and frame tag with example

Q.5(b) Attempt the following (Any 1) [12]

1 What is an applet? Explain life cycle of applet? How it is different from an application?
Create an applet which will draw any 3 shapes and display message on the screen.

2. Create a form with header “Calculating Area/Perimeter of Selected Figure” a text box to
accept your name, a menu selection with options circle, rectangle & square, two
textboxes to accept two numbers labeled num! & num2, a text area, a reset button
“Clear” & a button “Calculate”.

JavaScript Validations:

a, The name textbox should not be left blank.

b. The textbox num] should not be left blank.

c. Ifno menu selection is made then by default square should be selected.

d. The textbox num2 should not to be left blank only when circle or rectangle menu
selection made.

e. The textboxes num! & num2 should accept only positive nonzero numeric values.

f. When all validations correct then display the following in the textarea.

Name :

Menu selected option :

Num! : Num2 ;

Area : Perimeter :

Q.6(a) Answer the following (Any 2) {10]

1 Explain HTML DOM in detail.

\2 Explain Web Browser Architecture.

}3 Create the following on First Page with font as Times Roman size 10. The table contents
should be center justified , The first column and first row filled with red color, text
Black & the rest of the table should be blue and text color white :

Flowers | Colors; Petals | Thorns

Rose Five Bight Yes
Pituna Six No
Sunflower Nine
Q. 6 (b) Answer the following (Any 1) [10]

‘I Wet is XML? Explain how XML is different than HTML. Create an XML file which
stores Employee detail (SSN number, name, age, qualification, salary). Write DTD for
the same. :

2 What is Cascading Style sheet? Its types? Explain it with example.

<——

3
````

## 2010-11 · Exam not stated · Trim 5 · paper 8cbfebf1f484

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/TRIM V/JAVA AND WEB TECHNOLOGIES/2010-2011(1).pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10/02/2011
- Text: ocr (3 pages), mean OCR confidence 93.9

````text
ae

SVKM’s NMIMS

Mukesh Patel School Of Technology Management & Engineering
Programme: MCA Year: II Trimester: V

Academic Year : 2010-2011

Subject: JAVA & WEB TECHNOLOGIES Marks: 100 j

Time: 2.00 PM TO 5.00 PM ‘
Date: 10/02/2011. Duration: 3hrs.

Final - Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the

Cover of the Answer Book, which is provided for their use.
NB: _ 1. Question No. | is compulsory.

2. Out of remaining 5 questions, attempt any 4 questions. In all attempt 5 questions.
3. All questions carry equal marks.
4, Answer to each new question to be started on a fresh page.
5. Figure in brackets indicates full marks.
6. Give examples wherever required.

Q.1(a) Attempt the following [10]
1 What is not true about applet?
(a) Applets do not need a main() method
(b) Applets should be run under a Java-compatible browser
(c) Applet uses the interface provided by AWT
(d) User I/O is accomplished with Java’s Stream I/O Classes
2 Web pages are created in the language
3 When no specific buffer length is requested, StringBuffer allocates room for how many
additional characters
(a) 8 (b) 16 (c) 0 (d) Not fixed
4 Complete the following code with given choices such that the method would calculate
“the sum of all the elements in an array of integers.
public int total (int [ ] x)

{
inti,t=0
{
t=t+x[it]
}
return t ;
}

(a) for (int i= 0; i1<x. length ;)
(b) for (i= 0; i<x. length ;)
(c) for (i = 0; i<x. length ;i++)
(d) for (i= 1; i<=x. length ;i ++)
5 Select the valid statement
(a) the class Thread is abstract
(b) Classes implementing the Runnable interface must define a method called start()
(c) Wait() is the method of class Thread.
(d) The class Thread implements Runnable.
6 Method overriding is associated with
(a) Run time polymorphism (b) Inheritance
(c) Methods with same name, same arguments and same return type _(d) all the above
7 To make a member of a class visible in all subclasses regardless of what package they
are in, which one of the following keywords can be used?

(a) private (b) public (c) protected (d) default
8 Which package is implicitly imported in every Java Program?
(a) java.awt (b) java.net (c)java.lang (d) java.util

4
--- page 2 ---
9 The setForeground() method is part of the class
(a) Graphics (b) Applet (c) Component (d) Container
10 is the Internet Protocol used to communicate between Web clients and servers

Q.1(b) Attempt the-following [05]

1 To change web page background colors you use the attribute in the <Body>
tag

2 An is an abnormal condition that disrupts the normal program flow.

3 Arrays are passed to method by :

4 The method invokes the applet’s update method.

5 Graphics class is defined in package

Q.1(c) State whether the statement is True or False (Justify your answer) [05]

1 In Java a class can have more than one super class.

2 HTTP can preserve state of transaction

3 Acatch can have comma separated multiple arguments.

4 Tables simply arrange multiple Web pages within a single document window

5 The finally block is always executed, even though if an exception is not thrown.

Q.2 Answer the following (Any 2) [20]

1 What is an interface? Why it is used? Explain with an example
2 Assume that a bank maintains two kinds of account for its customers, one called saving
and other current account. The saving account provides interest and withdrawal facilities
but no cheque book facility. The current account provides cheque book facility but no
interest. Current account holders should also maintain a minimum balance of rupees
1000, and if the balance falls below this level, a service charge is imposed.
Create a class Account that stores customer name, account number and type of account.
From this derive the class current-act and saving-act to make them more specific to their
requirements. Include the necessary methods in order to achieve the following task
(a) accept deposit and update balance
(b) display the balance
(c) compute and deposit interest
(d) permit withdrawal and update the balance
(e) Check for the minimum balance, impose penalty, if necessary, and update the
balance.
3 Explain the concept of overloading of method and constructor with example

Q.3(a) Distinguish between the following (Any 2) ; [06]

(a) String and StringBuffer classes (b) Class and Interface
(c) Method and Constructor

Q.3(b) Answer the following (Any 2) [14]
1 Explain the concept of inner class with example.
2 Explain two uses of super keyword with example.

3 Write a program to generate Fibonacci Series 1, 1, 2, 3, 5, 8...till n, using command line
argument.

%
--- page 3 ---
Q. 6 (a)

Answer the following (Any 2)

Explain Exception Handling with example

Explain concept of Multi-threading in Java with example

Explain life cycle of applet? Create an applet which will draw any 3 shapes and display
message on the screen.

Answer the following (Any 2)

Explain the use of this keyword.
What is a Package? Why package is needed? Give syntax for how to include a package.
Explain applet tag used for including applet in HTML file.

Attempt the following

Develop an HTML page for DTech- computer’s hardware selling company. It should
contain the moving text “Weicome to DTech”. It should have logo of company and
details regarding company. It should also have list of all the products provided by the
company. Link for feedback form.

Design the feedback form which accepts username, contact details. The form should
contain rating for products (Excellent, good, average and bad). It should have multiple
line text input for comment and submit button.

Answer the following (Any 2)

Write a note on 2 tier and 3 tier architecture

What is XML? Explain how XML is-different than HTML.
Explain Web Browser working.

Answer the following (Any 1)

Explain the use of Client side scripting with example.
What is Cascading Style sheet? Its types? Explain it with example.

[20]

[06] -

[14]

[10}

[10]
````

## 2009-10 · Exam not stated · Trim 5 · paper 71551dbd1803

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/TRIM V/JAVA AND WEB TECHNOLOGIES/2009-2010(17).pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 90.6

````text
SVKM’s NMIMS .é
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT AND EN!

MCA (SECOND YEAR)
TRIMESTER — V, 2009 — 10
Find Flow
SUBJECT : JAVA AND WEB TECHNOLOGY MAXIMUM MARKS : 100
Date: 2Ofo,/29\o C2.009m lo S.0ORPm 7] DURATION: 3HRS.

INSTRUCTIONS: Candidates should read carefully the instructions printed on question paper and on the cover

of the Answer Book.

NB:

1. Question — 1 is compulsory.

2. Attempt any four out of remaining six questions.

3. figure in bracket indicates marks

4. Answer to each new question to be started from fresh page and its parts should be written under that
question only.

Ques — 1 Part — A: Multiple Choice: [10]

1. You want a class to have access to members of another class in the same package. Which is the
most restrictive access that accomplishes this objective?
A. public B. private E. default access
C. protected D. transient

2. What can cause a thread to become non-runnable?
a. Exiting from a synchronized block.
b. Calling the wait method on an object.
c. Calling the notify method on an object.
d. Calling the notifyAll method on an object.

3. Which two are reserved words in the Java programming language? (Choose two)
A. run B. import C. default D. implement

4. Given:
class BaseClass{
private float x= 1.0f;
protected void setVar (float f) {x = f;}
}
class SubClass extends BaseClass {
private float x = 2.0f;
//insert code here }
Which two are valid examples of method overriding? (Choose Two)
a. Void setVar(float f) {x = f}
b. Public void setVar(int f) {x = f3}
c. Public void setVar(float f) {x = f}
d. Public double setVar(float f) {x = f;}
e. Public final void setVar(float f) {x = f;}
f. Protected float setVar() {x=3.0f; return 3.0f; }

CP. T2)

Page-!

fre TRY XN
--- page 2 ---
5. Given:

Zu

class Super {
public float getNum() { return 3.0f; }

}

public class Sub extends Super {

}

Which method, placed at line6, causes compilation to fail?

a.
b.
c.
d.

Ques- 1

public void getNum() { }

public void getNum(double d) { }

public float getNum() { return 4.0f; }

public double getNum(float d) { return 4.0d; }

Part — B True / False

Objects that have finalize() methods always have their finalize() methods called before

the program ends.

Any statement that can throw an Error must be enclosed in a try block. ~
If a class lacks a no-arg constructor, the compiler always creates a default constructor.
catch(X x) can catch subclasses of X.

An encapsulated class allows a programmer to change an implementation without

affecting outside code.

Ques — 1 Part -C [10]

Explain the following (with Syntax/Example)—

2.
3.
4.
5.
1.
wn
3.
4.
5.
Ques - 2

Nested and Inner Classes
Interface

Try, catch and finally
Passing parameter to applets.
Types of CSS.

i, Create a Package Company, which has class Employee (code, name) and class [ 12 ]
Scientist (area, no. of projects, projmoney) which is inherited from Employee. L
Employee class should have constructor, and display method. Scientist class

should have constructor, display calculate salary methods (no. of

projects* projmoney).

Create other Package Person, which has class Engineer (dept, basic, incentive)
which is inherited from Employee class. It should have constructor, display and
calculate salary method (basic+incentive).

Create a class Test which will create object of Scientist and Engineer and check
the program (class test should be outside the package)

ii, Difference between constructor and method [04]

4
iii, Why super and this is used. [04]

Ce. T8:)
Page-2
--- page 3 ---
Ques -3

Ques— 4

Ques -5

Ques - 6

Ques -7

<\ NG,
si Ye
—— 2 or Ns,
je’ uestMe yu
i, Difference between ‘ dE
cA

a. Packages and classes.

b. Method overloading and Method overriding.
ii, Write the use and syntax of command line argument with example.
iii, Write the syntax of multi — level inheritance. Explain why multiple
inheritance is not in java.

i. Certified Carriers is an institute that conducts various computer courses. John,
the instructor at the institute teaches Java language to students. After the
completion of the Java course, John gives a home assignment to the students to
create a Java program that draws a figure using various shapes taught in the
lecture. Help students to create the application.

ii. Explain the life cycle of applet.

iii, What are types of exception and its use?

i. Write a program to check whether a given string is exactly same on reversing
as the original one.

ii, Explain thread priority and it is set.

iii, What is the difference between Thread and runnable. Give Syntax for both and
how you can call it in main.

i. What are CSS? Illustrate uses of CSS reference to Dimension, Classification &
Positioning. Write CSS for a HTML page to
a. Set background color.
b. Left indent text.
c. Set size of the font.
d. Increase spacing between lines.
e. Change the cursor.
ii, Explain the following(with example) —
a. anchor
b. table(row, description, heading)
c. font
d. image
e. frameset

i, List two major advantages of XML over HTML and explain about reason for
each advantage.
ii, Explain XML, XSL with example.

[05]
[05 ]

[07]
[05 ]
[08]

[10]

[10]

[10]

[10]
````

## 2008-09 · Exam not stated · Trim 5 · paper aee622aca530

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/TRIM V/JAVA AND WEB TECHNOLOGIES/JAVA AND WEB TECHNOLOGIES TRIM V 2008-2009.pdf`
- Printed on paper: duration hours: 3; exam date: 14-01-09
- Text: ocr (3 pages), mean OCR confidence 90.4

````text
SVKM’S NMIMS UNIVERSITY

MUKESH PATEL SCHOOL OF TECHNOLOGY & ENGINEE Mumbai - 56,

{ LIBRARY
A

MCA Programme II Year
Trimester V, 2008-09
\ Cop ee
Subject: Java and Web Technologies Max. mando
Date: 14-01-09 Time Allowed: 3Hrs.

200-5: CO P™
Instructions: Candidates should read carefully the instructions printed on the question paper and on the
Cover of the Answer Book, which is provided for their use.
NB:
1. Question No. 1 is compulsory.
2. Out of remaining 6 questions, attempt any 4 questions. In all attempt 5 questions.
3. All questions carry equal marks.
4. Answer to each new question to be started on a fresh page.
5. Figure in brackets indicates full marks.
6. Make suitable assumptions if necessary.

Q.1(a) Attempt the following [10]

1 Which method of the Thread class should be defined?
(a) run() (b) start( ) (c) both a and b (d) yield( )
2 The tags can be used to create hyper links
(a) anchor (b) arrow (c) link (d) pointer
3 Which of the following keyword should be used to make a variable defined in a class
accessible only to methods defined in the classes in same package
(a) By using the keyword package before the variable
(b) By using the keyword private before the variable
(c) By using the keyword protected before the variable
(d) The variable should not be preceded by any of the above mentioned keywords.
4 Find out the incorrect statement
(a) A subclass can call a constructor defined by its super class by use of super‘ ).
(b) super( ) must not always be the first statement executed inside a subclass
constructor.
(c) super( ) always refers to the super class immediately above the calling class.
(d) Super class has no knowledge of wht a subclass adds to it.

5 The command allows a client to remove a file from a Web Server
using HTTP.

) (a)GET (b) POST (c) UNLINK —(d) DELETE

6 A throws clause listing of exceptions is necessary for all exceptions except those of type

, (a) IlegalAccessException (b)Error or RuntimeException and their subclasses
( (c) Subclass of Throwable (d) All the above

7 Method overriding is associated with

(a) Run time polymorphism (b) Inheritance

(c) Methods with same name, same arguments and same return type (d) All of the above
8 Concept of multiple inheritance is implemented in Java by?

(a) Extending two or more classes (b) Implementing two or more interface

(c) Extending one class and implementing one interface (d) All of the above
9 Which package is implicitly imported in every Java program?

(a) java.awt (b) java.net (c) java.lang (d)java.util
10 The setForeground( ) method is part of the class
(a) Graphics (b) Applet (c) Component (d) Container

-1-

PTO

fC er Tt BY \
--- page 2 ---
Q

Q.1(b) Attempt the following [5]
1 The tag is used to start an applet from both an HTML document & from an
applet viewer.
2 The method suspends the current thread until that thread object dies.
3 Exception is a subclass of class.
4 All command line arguments are objects.
5 Web pages are created in the language.
Q.1(c) State whether the statement is True or False. (Justify your answer) [5]

1 Acclass that is abstract may not be instantiated.

2 The keyword extends indicates that an interface inherits from another.
3 drawstring( ) is a method defined in the String class.

4 HTTP is called stateful protocol.

5 Members of a class specified as private are accessible to its subclass.

Q.2 (a) Distinguish between the following (any 2) [6]

1. Class and Package 2. Applet and Application
3. HTML and XML

Q.2(b) Answer the following (any 2) [14]

1 Discuss the role of inheritance in Object- oriented programming. A class that has been
declared as private is not accessible by any code outside its class, including subclass.
Explain this with the help of coding.

2 Explain the difference between overloading & overriding methods using example.

3 Describe any 7 HTML tags

Q.3(a) Answer the following (any 2) [10]
1 Describe any 5 HTTP command.

2 Write a program to find the factorial of a number inputted by command line argument.
3 What is thread priority and explain how thread priority is set in Java.

Q.3(b) Explain any 5 methods of String class with example. [10] ~
; OR

Q. 3 (b) ! Explain how does a web browser work. [10]

Q. 4 ay — the following (any 2) . [6]

1 What does the static keyword mean in front of a variable, a method and a class?
2 Explain the prototype of main method in java
3 Explain 3 use of super keyword.

Q.4(b) Attempt the following (any 2) [14]

1 Write a short note on Proxy Server

2 Write a note on package with example

3 Write a program in java to check the input character for uppercase, lowercase, number
and other characters.

-2-

PTO
--- page 3 ---
a el gr 2 IN
3 i ro No N
; SVK™’"S \
Q.5(a) Answer the following (any 2) . *( pe ee) B
\\ ( LIBRARY
1 Explain a Cascading style sheet with example \3
2 Describe the complete life cycle of thread. %, ee, es

3 Write a note on Constructors in Java and explain copy constructor with exShiple, AGES

Q.5(b) Explain Exception handling with example. [10]
OR
Q.5(b) What is applet? Explain the Life cycle of applet. Why does applet class need to be [10]
declared as public.

Q.6(a) Attempt the following (any 1) [5]

1 Write a note on Client side scripting languages.
2 Write a note on | tier, 2 tier and 3 tier architectures.

Q.6(b) Develop an HTML page for Techmedia- library for books, music and movies. It should [15]
contain the moving text “Welcome to Techmedia”. It should have logo of company and
details regarding company. It should also have list of all the products provided by the
company. Link for feedback form. Also design the feedback form which accepts
username, contact detail. The form should contain rating for products (i.e. very good,
average or bad). It should have multiple line text input for comment and submit button.

Q.7(a) Distinguish between the following (any 2) [6]
1. start and init methods of applet 2. equals( ) function and = =
3. GET and POST methods for form tag.
Q.7(b) Write an applet that will draw rectangle, circle, line, write text and fill the background [14]
with color.
OR

Q.7(b) Write a program of threads in Java showing interleaving of actions from two threads: tl [14]
and t2 synchronizing on a shared object.
Let tl print message “ping->” and t2 print message “<-pong”.
Take as command line arguments, the following inputs to the program:
Sleep interval for thread tl and t2. Message per cycle and No. of cycle.

x oe

~~
````
