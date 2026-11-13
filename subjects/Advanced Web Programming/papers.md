# Advanced Web Programming: question papers in full

5 unique papers · 2021-22 to 2024-25 · Computer Engineering, Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2024-25 · Final + Re-Exam · Sem 6 · paper 5d6c2d219661

- Departments: Information Technology
- Programmes: B TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/I T/VI SEMESTER/ADVANCED WEB PROGRAMMING/Advanced Web Programming, Sem-VI, Final Exam 2024-25 & Re Exam 2024-25.pdf`
- Printed on paper: duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 91.0
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B.Tech /MBA.Tech Year: III] Semester: VI
Stream/s :IT

Subject: Advanced Web Programming Time: 3 hrs (10:00 to 1:00 PM)
Date: K#2025 (9 | 05 \ 9025 No. of Pages:5

Marks: __ 100

Final Examination/Re-Examination (2024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

8) choice between Q2 and Q6; pick any one of them.

9) choice between Q4 and Q7; pick any one of them.

Ql
‘| Answer briefly: [20]

Create a Website which will be hosted by the “Indian Railways” using ASP.NET
CSS, data validation, and database integration for the citizens of India. The
purpose of the website is to provide railway-related information and services to
the people. The website should have a minimum of 6 pages:

a. Home Page — Contains the links to the internal pages.

2

“Mention the Importance of Railways in India and Services Provided
by Indian Railways” using basic ASP.NET, HTML, and CSS
Co- 1;
SO- 2; e Background color: Yellow (3M)
BL+1 &2 e Heading 1 centered with "Times New Roman" font (2M)
e Paragraph font: Courier New, size 12px (3M)
e Text color: Dark Blue with center alignment (2M)

10
--- page 2 ---
Internal Page 1 — Train Data Table & Info on Indian Railway Board

Show the average number of passengers per train using recent data.
Display a table with the following columns

2 Arrival
Trai 5 Departure z
Train ‘ ; Station 5
n Station with Fi Train Route
Name . With Date
No. Date and Time P
and Time
1702 | Vande Delhi, 15Sep , LTT, l6sep, | Delhi ,Gujarat
2 | bharat 09:30 AM 18:00 PM fo LLE
1703 | Paragati Indore, 15 Sep, | Dadar, 16 Indore, Delhi
3 | Express 17:30 PM sep 22:00PM | and MP
CO- 1; Cochin ,
50-2 7 1600 | LTT Karanatak, 15 CST ,16 sep | chiplun and
, 7 | Special sep ,16:40PM 05:00 AM CSE 10
8 | Express Sep 18:00 PM 04:00 AM and Panvel
1890 | cochin
0 | Express Cancelled

*Display the Mountain Railways of India is made up of the following ordered
list with upper case roman numbers.

II.Nilgiri Mountain Railways (NMR) inscribed in 2005.


Internal Page 2:- choice between Q2 and Q6; pick any one of them.
Internal Page 2 — Passenger Registration Form [10M]
Inputs:

Railway ID, Name, Age (Calendar), State (DropDownList), City (Dynamic based

Q2 on State), Password, Confirm Password

CO-1 &2; : ee

50-2: On Submit: [20]
BL-2 e Generate and display a unique Booking-ID on the same page

Internal Page 3 — Data Display [10M]
Retrieve Railway ID, Name, Password

Assign Booking-ID to a hidden label

Store all data as session variables
--- page 3 ---
Validations + SQL DB Integration
[20 Marks]

On the same registration page, apply these validations: [10M]

e RequiredFieldValidator for all inputs
e CompareValidator for Password and Confirm Password
e RangeValidator for Age (<5 = Not Eligible for individual ticket)
e Regular Expressions:
o Email: *[\w\.-1]+@[\w\.-]+\.\w{2,4}$
o Railway ID (5-digit): *\a{5}s
o Name (7-10 characters, alphabets only):

*[A-Za-z]{7,10}$
Note: Validations must occur on TextChanged event (not on submit)

Jquery Setting

Q3
CO-2 & 3: protected void Page _Load(object sender, EventArgs e) 120]
SO-2; BL-
2&3 this. Unobtrusive ValidationMode =
System. Web.UI.UnobtrusiveValidationMode.None;
}
SQL Integration
Create an SQL Server table named passengerTable with the following
columns:[10M]
e RailwayID (int)
e PassengerName (varchar)
e Age (int)
e State (varchar)
e City (varchar)
e Password (varchar)
e ConfirmPassword (varchar)
Q4 choice between Q4 and Q7; pick any one of them.
CO-3; SO-
2; Page 3 — GridView Operations [10M] 20]
BL-4

e _ Display, Select, Insert, Update, Delete records using GridView
--- page 4 ---
e Data fetched from passengerTable
e . Trigger operations via Submit Button
e Bind GridView on Page_Load or Submit_Click

Internal Page 4 — Login Page [10M]

e Input: Username, Password

e On success — Redirect to Page 5 with Username
e On failure — Show “Forgot Password” link

e Allow password reset after username validation.

[Note]below is the brief about Login page —Page[4]

The login page allows users to enter their username and password. If
correct, they are redirected to the next page. If incorrect, a "Forgot
Password?" link appears. Clicking it lets users reset their password by
entering their username and new password. If Password is valid, the
password is updated, and they can log in again with new Password.

[20 Marks]
3 e Use a ListView to display: Railway ID, Name, Age, State, City
Q e Enable the user to Modify, Remove, and Add values.[10M]
CO-2,3; [20]
SO-2; Create a Pie Chart showing City-wise Train Booking Count using chart
BL-3 controls. [10M]
Internal Page 2:- choice between Q2 and Q6; pick any one of them.
Internal Page 2 — Advanced Registration Form [10M]
Q6 Inputs:
eee e Railway ID, Name, Age (Date Picker), Gender (Radio Buttons) (20]
SO-2; e State (DropDown), City (Checkbox based on State)
BL-2 e Password, Confirm Password

On Submit: Generate a unique Booking-ID

Internal Page 3 — Display Info [10M]

e Retrieve and display Railway ID, Name, Password, Booking-ID
--- page 5 ---
e Store all values in global variables

(Alternate to Q4) (FormView Version)

Page 3 — FormView Operations [10M]

e Display, Select, Insert, Update, Delete records using FormView
e Data fetched from passengerTable

e Operations triggered using Submit Button Click

e Bind FormView on Page_Load

Q7
CO-3; SO- Internal Page 4 — Login Page [10M] 120]
2;
e Input: Username, Password
BL-2 & 3

e On success — Redirect to Page 5 with Username
e On failure — Show “Forgot Password” link
e Allow password reset after validating username

[Note]below is the brief about Login page —Page[4]

The login page allows users to enter their username and password. If correct, they
are redirected to the next page. If incorrect, a "Forgot Password?" link appears.
Clicking it lets users reset their password by entering their username and new
password. If Password is valid, the password is updated, and they can log in
again with new Password.
````

## 2023-24 · Final-Exam · Sem 5 · paper 74d8361aa687

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/ADVANCED WEB PROGRAMMING/Advanced Web Programming,Final 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 /12/ 2023
- Text: ocr (4 pages), mean OCR confidence 90.8

````text
SVKM’S NMIMS :
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/ .
SCHOOL OF TECHNOLOGY MANAGEMENT ieee
Academic Year: 2023-2024

Program/s: B. Tech and MBA Tech/B Tech Computer Science Year Semester: Vv

Stream/s : Computer Engineering :

Subject: Advanced Web Programming Time: 3 hrs (10:00 am to 1:00 pm)
Date: 06 /12/ 2023 No. of Pages:4

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]

Coe 9 a. Write Angular JS code to bind the value of input field to application

ae , variable and display using angular JS expression inside <p> tag.

aoit . be Create JSON string from Javascript object obj = {name: "John", age: 30,
BL-3 > city: "New York"} and display inside <h1> tag.

CO- 4; om Design node JS server to read Sample.txt file. The contents of Sample.txt

SO-1,2 ; file as given below

BL-3 “Welcome to Node JS server”

CO- 1,2; | d. Write the meaning of the following terms.

SO-1,2 ; 1. Parse() 2. ng-click 3. getElementByldQ) 4. readyState 5. collection

BL-2 in MongoDB.

Q2 a.

CO-1,2; Design the angular JS form as shown below and bind the data enter in the [10]

SO-1,2; form to the <table> tag when clicked on Submit button.

BL-3

1/4
--- page 2 ---
Enter your user name :
Enter your password :
Enter your email :
Enter your age :

/ submit |

b Create Ajax application to read array
Books= (“HTML”,”XML”,”JSP”,”Servlet”) from PHP server and display | [10]
the contents of array inside <ul> tag at client side.

a. Design Math Angular JS dependency service as shown below.

AngularJs Math Services

Q3
CO- ; ,
1.2.3.4: First Value: [10 | [10]
SO-1,2; Second Value: [30 |
BL-3 Result is : -20
{ Addition || Substraction |{ Multiply | { Division |
b. ;
Implement following Node JS script on mysql database.
1. Node JS script to create table Customer with fields like custid, [10]
fname,Iname, income in MyDB database.
2. Node JS script to Insert 5 records in Customer table.
a. Design Registration Course Enrolment System using Ajax that as autofill
Q4 functionality to fetch up relevant courses from server for selected degree
CO-1.2: program as BTech/MBA Tech as shown below.
SO-1 on For Degree BTech Courses offered are {Machine Learning, Database, [20]
‘“ A}
BL-3

For Degree MBA Tech Courses offered are {Computer Network, Deep
Learning, Management Information System}

2/4
--- page 3 ---
Registration Course Enrolment

System
Username:{Smith _|
_Password;[--- ]
"Degree:

Course: [MachineLearning v

CO-1,2,4; Create user defined Node JS module to check whether given number is
SO-1,2; even, odd or prime.
BL-3

[10]

b. Create a GUI based application for E-Commerce Rating using Node JS
Express, which accepts Product ID, Product name, Product Rating with
value ranging from 10 to 50 as (Rating1, Rating 2 and Rating 3) and
calculates mean of product rating as Rating Score and displays all the
details along with Rating Rank has below.

If Rating Score is less, then equal to 20 then Rating Rank= “Low
Quality”
If Rating Score is >20 and <=40, then Rating Rank= “Medium Quality.
If Rating Score >40, then Rating Rank= “High Quality”
[10]
E-Commerce Product Rating

Product id| |

Product Name | |

Product Rating-1 | | Enter value between 10-50
Product Rating-2 | | Enter value between 10-50
Product Rating-3 L | Enter value between 10-50

[ Submit

3/4
--- page 4 ---
Q6 a. | Design following routes to access following resources and display

co- client side using Node JS Express.

1.2.3.4: 1. Create URL schema route get_user_details to access JSON user [10]
50.1.2: detail object as {id:10, name:”Mike”, age:30}

BL-3 > 2. Create URL schema route read_all_products to access array

product= ["Pen”, “CD”. “Book”]

b. | Write Node JS Script to perform following operation on MongoDB
database. Assume necessary data in collection.
a. Designed a Node JS script to create a collection Customer in
database MyDB. [10]
b. Designed a Node JS script to insert 5 documents in collection
Customer with following information such as name, age, email

and income.
Q7 a.
CO-1,3; Demonstrate the concept with implementation of following directives. [10]
SO-1,2; a) Model b) Bind c) ng-repeat d) ng-pristine e) ng-dirty-
BL-3
b Consider a scenario to capture the post and likes done by user on social
networking sites. For the above scenario create mongo DB database
SocialDB and perform following operation:
a. Create database SocialDB.
b. Create a collection Userpost in SocialDB database
c. Insert at least 5 documents with the following information.
Assume Necessary data in 5 documents with sample data as shown
below.
{
subject: "Current Affairs", [10]
theme: "Event",
likes: 2,

tweets: ["news", "events"],
date: Date()

d
d. Display all documents in Collection based on filter criteria as
theme.
e. Delete the specific documents from collection whose likes are less
than 2.

4/4
````

## 2023-24 · Re-Exam · Sem 5 · paper bd9e79fd0f8f

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/ADVANCED WEB PROGRAMMING/Advanced Web Programming , Re-exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15/02/2024
- Text: ocr (4 pages), mean OCR confidence 87.8

````text
Ke VoL, se

[iKcr—

Sem
_ I5 [oth x"2%00 an
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT ve
Academic Year: 2023-2024 -
Program/s: B. Tech and MBA Tech / B Tech Computer Science Year: Semester: Vv
Stream/s : Computer Engineering
Subject: Advanced Web Programming Time: 3 hrs(2-00 pm to 5-00 pm)
Date: 15/02/2024 No. of Pages:4
Marks: 100
Ré Examination

>, Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks. -

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: (20]
a. Write AngularJS code to accept username and display the “Welcome
<username>”.
CO-1; Output: ‘
@ | SO-1,2;

BL-3 , Username:

Welcame Ram

b. Write program to display the given JSON string in the given format.
CO- 1; ‘{"name":"Varun", "age":30, "city":"Mumbai"}'
SO-1,2 ; Output:
BL-3

The data received is: Varun, 3@, Mumbai

Sot 5 . ° Create NodeJS program to append content: “ New record added” to an
BL-3 > existing file.
CO- 3,4; | d. Briefly explain the following terms:
SO-1,2 ; 1. JSON. stringify(), 2. Ng-model, 3. db.createCollection(),
BL-2 4. Onreadystatechange, 5. require(‘http’)

1/4
--- page 2 ---
Write a program using AngularJS to display following student datawin
Q2 tabular form vas

CO-1,2; Roll_no | Name Course [10]
SO-1,2; lll Ram Computer
BL-3 112 Meenu_| IT

113 Rénu Mech

b. | Create application to send the form data to the server and to store in a json
format and display JSON object. The form data on server is processed

using PHP script.
Use ao)
Rata

Using NodeJS and MySQL, create following form to accept user details
and store in MySQL table. Note: Student has to create a table User in
03 MySQL database.

Co- Nene [|

1,2,3,4; Pons [| [10]
SO-1,2; cy [7

BL3 st: [|

b

Create a Express.js based Web Application using NodeJS to store the ‘

given data in the server and display the form data.

sme

oe Co | _
Q4 a. . . . . . .
COLD: Design registration form using AJAX and PHP that will auto-check if the
S O-1 >. username filled by the user exists or not, and the country name are auto- [20]
BL-3 > fetched and included in the drop-down list.

2/4
--- page 3 ---
Username: aaroon

Username does not exist

Phone no:
Country: I v
| India
oa
Q5 a.
CO-1.2.4; Design the script to perform following NodeJS file operation: Copy the [10]
SO-1,2; data from one file to another file.
BL-3 -
b. Design a registration form to accept Name, Phone number, Email id using
AngularJS. Following validation needs to be done-

1. All fields are required

2. Phone number should be of 10 digits [10]

3. Email id should be valid

4. Initially the text input field are in grey color till they are touched.

Once the data is entered the color changes to blue if valid or else it
changes to red if invalid.
5. Ifthe form is invalid, submit button is disabled. ‘
(26 a.
CO- Create an application using NodeJS and MySQL to :
1,2,3,4; i. Create a database Supermart ; [10]
SO-1,2; ii. Create a table product (id, item_name, quantity, price)
BL-3
b Create Angular JS dependency service as to calculate average and highest [10]

marks shown below:

3/4
--- page 4 ---
Student marks ;

Studentl: 10
Student2: 6
Student3: 5

The average is: 7

a. Create mongo DB database College and perform following operation on
database.

a. Create database College
b. Create a collection Students in College database

c. Insert at least 5 documents with the following information. Assume
Necessary data in 5 documents.

Q7 {“id?:123, -
CO- “name”:”Reena”,
1,2,3,4; “Scores”: [ [10]
SO-1,2; {“course”:”maths”, “marks”: 10},
BL-3 {“course“:”physics”, “marks’:15},

“course”:“chemistry”, “marks’:20}

1

age:16

}

d. Display the documents in collection based on criteria age>18.

a
e. Update a record to change the name.

b Write Node JS Script to perform following operation on MongoDB
database.

a. Design a Node JS script to create a collection Employee in
database MyDB. ;
b. Design a Node JS script to insert 5 documents in collection

Employee with following information such as name, age, email and ha
salary.

c. Design a Node JS script to display all documents from collection
Employee.

4/4
````

## 2022-23 · Exam not stated · Sem 6 · paper 1b04019fb0bc

- Departments: Computer Engineering
- Programmes: MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/Computer/SEM VI/ADVANCED WEB PROGRAMMING/Advanced Web Programming.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 89.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program: MBA Tech Stream : Computer Year: III Semester: VI

Subject: Advanced Web Programming Time: 3 hrs (2: @opmto 51G0pm)

Date:_02 (Mog! 2023.. No. of Pages:02

Marks: 100

Re-Examination (Batch 2021-22 )

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. .
1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Ql .
Answer briefly: [20]
CO-1;SO- | a. ; ;
1; Explain the use of $scope in AngularJS.
BL-2
CO-3 ;SO- | b. . . . oo.
1; Explain the advantages of using Ajax in web applications?
BL-1
CO-2;SO- |e. ; ;
2; Differentiate between JSON and XML.
BL-2
CO-1;SO- | d. . a —
1; Demonstrate the role of the ng-app directive in an Angular application?
BL-2
a. Create angular JS form consisting First_name, Last_name, radio button
2
S for gender, checkbox for different Subjects and submit and cancel button.
CO-1; SO- ; [20]
1,2,7; Perform the following constraints on the form
BL-2,3

a. Accept the form only after all the fields are valid
--- page 2 ---
b. The first name and last name should accept minimum 4 characters
and maximum 26 characters otherwise populate message too small
and too big.

c. The submit button gets enabled only if the form contains valid data.

Note: AnglarJS directives validation should be used
b. Explain MVC in AngularJs.

a. Create an XML file that represents a list of books. Each book should

Q3 have a title, author, and publication date. Write AJAX code to read the

CO-2; SO- above xml file and print details for all the books in HTML table. [20]
1,2,7; BL- 7 , . : a

23 b. Explain the process of creating a basic web server in Node.js using the

HTTP module.

Q4 a. Explain the difference between one-way binding and two-way binding in
CO-1; SO- AngularJS. [20]
ee b. Write a script to create a file and write data to it using the fs module.

a. Write an AngularJS program which has check box and edit fields. When
Q5 the checkbox is checked, the edit fields are visible. When it is not
So. checked, the edit fields are hidden. Use ng-model and ng-show [20]
BL-1,2 Assume necessary details.

b. Differentiate between Mongo DB and RDBMS.
oe a. Explain the difference between synchronous and asynchronous Ajax
CO-1,3; requests. [20]
ats b. Explain Dependency Injection in AngularJS
````

## 2021-22 · Re-Exam · Sem 6 · paper 0d7a55a69120

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/ADVANCED WEB PROGRAMMING/Advanced web programming , Re-exam 2021-2022.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 June 2022
- Text: ocr (2 pages), mean OCR confidence 89.1

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2021-22

Programme: B. Tech / MBA Tech (Computer) Year: ITI Semester: VI
- oa
Subject: Advanced Web Programming “
: 4 Marks: 100 -
Date: 09 June 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (Hrs)   ~
No. of Pages: 2
Re-Examination (2021-22)

oa

Instructions: Candidates should. eead carefully the tusteustions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
CO-1 ; a.
SO-1; Explain any 1 event of Angular JS with example. [5]
BL-2
C02; |b. —
SO- 1; Explain the use of JSON and how it is different from XML. [5]
BL-2
CO-2 ; Cc: Write node JS program to create web server and print “welcome to Node JS” 3
So message using Http module. B]
CO-3 ; d. .
SO- 1; Explain the terms Collection and Document with respect to MongoDB. [5]
BL-2
a. Create an AngularJS form consisting of First Name, Last Name, Age, Email

address, radio button for gender and a submit button. Perform following

constraints on the form
Q2 a. Accept the form only after all the fields are valid
CO-1; SO- b. The First Name and Last Name field should accept minimum 3 10
1,2,7; character and maximum 26 characters otherwise populate message [10]
BL-2,3 too small and too big.

c. Ifemail is invalid populate message “Please Enter Correct Email”.
d. The Submit button gets enabled only if all form contains valid data.
Note: AngularJS directive validation should be used.

fz
--- page 2 ---
b. What is Data- Binding in AngularJS? Explain different types of Data-Binding in 110]
AngularJS with suitable example.

a. What is the use of following functions?
(i) JSON. parse()
(ii) JSON. stringifyO
iii) json_encode()
Q3 vcon decode , [10]
CO-1,2; Design JSON file which stores the details about IT Employees. It should store
SO-1; He emp_id, name, designation, salary, projects. Each employee is assigned atleast

two projects. Store the details for 4 employees.

b. Explain different ways to create service in Angular JS. Write a program which

accepts a number for the user and using custom service finds the factorial of the [10]

number.
a. Create an XML file which stores the details for 4 products. It should store
Q4 product ID, Product name, unit price and quantity for each product. Write AJAX | [10]
CO-2; SO- code to read the above xml file and print details for all the products in html table. a:
cai | 3 b. Explain Node JS Architecture in detail. Compare it with Traditional web server 110]
model.
a. Assume there is MYSQL database named company having table Employee with

Qs fields- Employee_id, Employee_name, Department, Salary. Write a Node JS 110]

program to accept the above fields and insert the details into the above mentioned

- 80° table. If insertion is successful then print all the records from Employee table.
BL-1,2)4 Explain advantages of MongoDB over RDBMS. List various types of Data
Modeling and explain any 1 in detail. + 00]
Write Short on
Q6 a. Dependency Injection in Angular JS
nd se b. Ajax Working [20]
BL-f;2 c. Exception handling in node JS

d. MongoDB-Insert Document

2/2
````
