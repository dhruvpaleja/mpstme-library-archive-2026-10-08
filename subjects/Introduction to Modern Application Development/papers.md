# Introduction to Modern Application Development: question papers in full

9 unique papers · 2022-23 to 2025-26 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Exam not stated · Sem 5 · paper a98e1579e763

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/BTech,MBA Tech,BTI, (Data Science), Introduction to Modern Application Developmen_28a944b3.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 77.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program/s: Btech/MBATech/Btech INTG Year: III/ V Semester: V/IX
Stream/s : Data Science ;

Subject: Introduction to Modern App Development Time: 03 hrs(|0:obamto 42 opm)
Date:4__/ 12, / 2025 ~ No. of Pages: 05

Marks: 100.

Final Examination/Re-Exam (2024-25)
QS-26 5
_ Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover .

of the Answer Book, which is provided for their use.

1) Question No. 1. is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql :
Answer briefly: [20]
a. Props vs State — define each and give one classroom example for both (no
CO-2, BL-1; _| code run needed). Also explain when you would use props vs:when you [4]
would use state in a component.
b. When does useEffect run? Give one example each for: after first render;

CO-2, BL - after a particular state changes; cleanup on unmount. Mention the role of [5]
2, $02 the dependency array and what happens if you omit it entirely. ;
Co-4 Bie |% Write an SQL query that lists the top 5 students with marks > 75, ordered

Oe by marks descending. Also write a query to calculate the average marks of | [4]
2, $01

| all students who scored above 75.

Co-3,BL- | d. What does urls.py do? Contrast returning render(request, ...) vs” [4]
2, S02 HttpResponse("...") vs JsonResponse({...}) in 2-3 lines each.
cosa |e Write the CLI to-set a Git remote named origin to 5
a ii https://github.com/user/repo.git, and the CLI to clone a repo from that [2]

: URL. (Commands only.) .
Co-1,BL- | f What is the difference between frontend and backend in aeDR : [1]
1,S01 development? Give one example technology for each.
Q2 A A student's state update doesn't reflect immediately after setState. Explain 8]

CO-2, BL-1; why React batches state updates and when they actually apply. Explain
--- page 2 ---
CO-3,BL- when to use functional updates (prevState => ...) and give two scenarios

1,801 . p.
where functional updates are critical.

B
Q2 A component fetches data in useEffect but forgets to include query in
Co2,BL3, | dependencies. What bug can this cause? How do you fix it? Also explain [6]
sol what happens if you include too many dependencies or wrong dependencies.
c Explain the concept of "lifting state up" in React. Why is it needed? Give a
Qa é aoe ‘
ui practical example of when you would lift state from a child component to (61
02, ;
BLigel a parent component. Also mention one alternative approach to sharing
, state between components.
A In plain words explain:
Q3 - list vs tuple (mutability), give one.example each
- dict vs set, when to use each [10] °
CO-3, BL-1, - purpose of __init__ and what self means
$02 - difference between instance method and class method
- what is a constructor and destructor in Python.
B Code-reading (no execution):
x=[1, 2, 3]
y=x
y.append(4)
Q3 print(x) ;
CO-3, BL- ; : [6]
3,502 z=[5, 6, 7] .
, w = z.copy()
w.append(8)
print(z) oy
What prints in each case and why? Explain aliasing vs copying in detail.
Q3 Cc ‘ . phar .
é a Explain mutable vs immutable objects in Python. Give three examples of 4]
0-3, BL-1, gett .,
don each type. Why does immutability matter for dictionary keys?
A Explain in detail what React Server Components (RSC) are and how they
. differ from traditional Client-Side Rendering (CSR) and Server-Side
Q4 Rendering (SSR). For each approach (RSC, CSR, SSR):
Co3, BL1 - Describe where code runs [10]
- How data is fetched or sent to the client
sol - What gets sent to the browser

- Performance implications
- When to use each approach
--- page 3 ---
B What are the main differences between a Single-Page Application (SPA)

Q4 and the newer RSC architecture? Explain conceptually how each handles:
- Initial page load ,
Coes - Navigation between pages [6]
BL2,SO2 - Data fetching and state management
Compare their pros and cons (speed, SEO, scalability, developer control).
Q4 Cc Briefly describe how a Django-based backend would interact with each
Co3, BL3 approach (SPA vs RSC). What kind of responses does Django send in each | [4]
sol case? Which approach requires more API endpoints?
A Compare SQL and NoSQL databases in detail. Explain how relational
databases like PostgreSQL differ from document-based databases like
MongoDB in terms of:
Q5 - Data structure and schema ;
CO-4, BL-2 - Scalability (vertical vs horizontal) [10]
- Query language and style
SO1 - ACID properties vs BASE model
- Relationships between data.
Use shiort examples to illustrate when each is better suited (e.g., banking vs
social media).
B Discuss how Django's ORM interacts differently with SQL and NoSQL
Qs systems. Explain conceptually: 9
- How Django models translate to relational tables [6]
Co3 BL3 - Why integration with NoSQL databases can be more complex
- What trade-offs exist when using Django with MongoDB
- One advantage and one limitation of using ORM vs raw queries
Do C
2 Explain database normalization. What are the first three normal forms (1NF,
CO-4, BL-1 2NF, 3NF)? Why is normalization important in relational databases? Give [4]
Sol one example of:denormalization and when it might be beneficial.
Q6 A Explain in detail what Git is and why developers use it. Describe at least
CO-5, BL-3 four key advantages of using Git in software projects — for example,. 18]
sO1 collaboration, version history, branching, and backup/recovery. Support
each point with a short, practical example.
B: Explain what a branch represents in Git and how it helps developers work
Q6 on multiple features at once. Describe the typical workflow for:
- Creating afeature branch’ - ; [6]
Co5 BL1 - Making changes and commits :

- Merging back to main branch
- Handling merge conflicts
--- page 4 ---
In contrast, describe what a tag is and why it's often used when marking

software releases.

Q c Explain the difference between git merge and git rebase. When would you
6 .

use each? What are the pros and cons of each approach? Also explain what | [6]
Co5 BLS :

git cherry-pick does and give one use case for it.

You are tasked with designing a simple Enrollments feature for a
university website using Django's Model—View—Template (MVT)

Q7 architecture. The system should allow linking Students to:Courses through
an Enrollment model. Answer the following sub-questions clearly using
short paragraphs, bullet points, or neat diagrams where appropriate:

A Describe how you would define the Django models — Student, Course,
and Enrollment. For each model:
Q7 - Specify the fields with appropriate data types |
- Identify primary keys and foreign keys [6]
CO-3, BL-3 - Define any uniqueness constraints or validation tules
, - Explain the relationship type (one-to-many, many-to-many)
- Mention any methods you would add to the models (__str__, custom
methods)

‘B Define three URL—View mappings:
1. Endpoint to list all courses a student is enrolled in
2. Endpoint to enroll a student into a new course (form submission)
Q7 3. Endpoint to unenroll/drop a student from a course
€0-3;B1.2 For each, explain:
eae - The URL pattern (e.g., /student/<id>/courses/)
- HTTP method (GET/POST/DELETE)
- What the corresponding view should do (query logic, validation,
response) :

[6]

Cc Explain what the template should display on the course listing page.
Mention: ; .
- What information should be rendered (student details, course list,
Q7 enrollment dates) ;
60-4 BEA - What user actions should be available (enroll, unenroll buttons) [4]
, - What type of logic should NOT be written inside the template (business
logic, complex queries)
- How to pass data from view to template

D Write a numbered sequence describing the complete request-response flow
when a user submits a form to enroll in a new course (POST request).
Q7 Include:
_1. Browser form submission [4]

CO-3, BL-4 2. Django receives request :
. 3. URL routing and view execution

4. Form validation

5. Database operations
--- page 5 ---
6. Response generation
7. Redirect or error handling
(Aim for 7-9 detailed steps)
--- page 6 ---
: : : - BREN : -
_ oe
````

## 2025-26 · Final + Re-Exam · Sem 5 · paper e70533c26eb8

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, B.TECH INTEGRATED / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Introduction to Modern App Development 2025-26 Final Batch 2024-25 Re Exam.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 88.4

````text
/ MPSTME

LIBRARY
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENG
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2025-2026
Program/s: Btech/MBATech/Btech INTG Year: III/ V Semester: V/IX
Stream/s : Data Science .
Subject: Introduction to Modern App Development Time: _03 hrs(|o:ooawm to 4¢ 00pm)
Date:4__/ 12/2025 No. of Pages: _05___ ,

Marks: 100
Final Examination/Re-Exam (2024-25)
WS-26 J
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1____ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions:
3)Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
a. Props vs State — define each and give one classroom example for both (no
CO-2, BL-1; code run needed). Also explain when you would use props vs:when you [4]
would use state in a component.
b. When does useEffect run? Give one example each for: after first render;
CO-2, BL - after a particular state changes; cleanup on unmount. Mention the role of [5]
~ | 2,802 the dependency array and what happens if you omit it entirely.
G Write an SQL query that lists the top 5 students with marks > 75, ordered
Cont jBie by marks descending. Also write a query to calculate the average marks of [4]
2,S01 . :
all students who scored above 75.
Co-3, BL- | d. What does urls.py do? Contrast returning render(request, ...) vs [4]
2, S02 HttpResponse("...") vs JsonResponse({...}) in 2-3 lines each.
co-5. pL. |& Write the CLI to set a Git remote named origin to 7
2s o1 https://github.com/user/repo.git, and the CLI to clone a repo from that [2]
’ URL. (Commands only.)
Co-1,BL- | f What is the difference between frontend and backend in web [1]
1,SO01 development? Give one example technology for each.
Q2 A , | A student's state update doesn't reflect immediately after setState. Explain 8]
e
° co-2, BLA; why React batches state updates and when they actually apply. Explain
--- page 2 ---
CO-3,BL- when to use functional updates (prevState => ...) and give two, scenarios
1,501 a oe
where functional updates are critical.
Q2 A component fetches data in useEffect but forgets to include query in
Co2,BL3, dependencies. What’ bug can this cause? How do you fix it? Also explain | [6]
SOl what happens if you include too many dependencies or wrong dependencies.
2 Explain the concept of "lifting state up" in React. Why is it needed? Give a
Bok practical example of when you would lift state from a child component to (61
02,
Bist a parent component. Also mention one alternative approach to sharing
, state between components.
In plain words explain: ;
Q3 - list vs tuple (mutability), give one example each
- dict vs set, when to use each [10]
CO-3, BL-1, - purpose of __init__ and what self means
$02 - difference between instance method and class method
- what is a constructor and destructor in Python.
Code-reading (no execution):
x=[l, 2,3]
y=x
y.append(4)
o print(x)
CO-3, BL- . [6]
3,502 z=[5, 6, 7]
w = z.copy()
w.append(8)
print(z)
What prints in each case and why? Explain aliasing vs copying in detail.
Q3 . . oo, : P
Explain mutabie vs immutable objects in Python. Give three exampies of (4)
CO-3, BL-1,
= each type. Why does immutability matter for dictionary keys?
Explain in detail what React Server Components (RSC) are and how they
differ from traditional Client-Side Rendering (CSR) and Server-Side
Q4 Rendering (SSR). For each approach (RSC, CSR, SSR):
Co3, BL1 - Describe where code runs ; [10]
- How data is fetched or sent to the client
sol 4

- What gets sent to the browser ,
~ Performance implications
- When to use each approach
--- page 3 ---
« x

B What are the main differences between a Single-Page Application (SPA)

Q4 and the newer RSC architecture? Explain conceptually how each handles:
- Initial page load

Co2, - Navigation between pages [6]
BL2,SO2 - Data fetching and’ state management

Compare their pros and cons (speed, SEO, scalability, developer control).
Q4 Cc Briefly describe how a Django-based backend would interact with each
Co3, BL3 approach (SPA vs RSC). What kind of responses does Django send in each | [4]
S01 case? Which approach requires more API endpoints?

A Compare SQL and NoSQL databases in detail. Explain how relational

databases like PostgreSQL differ from document-based databases like
MongoDB in terms of:

Qs - Data structure and schema

0-4, BL-2 - Scalability (vertical vs horizontal) ” [10]
- Query language and style

S01 - ACID properties vs BASE model

- Relationships between data
Use short examples to illustrate when each is better suited (e.g., banking vs
social media).

B Discuss how Django's ORM interacts differently with SQL and NoSQL
systems. Explain conceptually: ; :

Q5

- How Django models translate to relational tables [6]
Co3 BL3 ‘- Why integration with NoSQL databases can be more complex
- What trade-offs exist when using Django with MongoDB
- One advantage and one limitation of using ORM vs raw queries
Q5 Cc
Explain database normalization. What are the first three normal forms (1 NF,
CO-4, BL-1 2NF, 3NF)? Why is normalization important in relational databases? Give | [4]
So1 | one example of denormalization and when it might be beneficial.
Q6 A Explain in detail what Git is and why developers use it. Describe at least
CO-5, BL-3 four key advantages of using Git in software projects — for example, 18]
so1 collaboration, version history, branching, and backup/recovery. Support
each point with a short, practical example.
B Explain what a branch represents in Git and how it helps developers work
on multiple features at once. Describe the typical workflow for:
Q6 P yp
- Creating a feature branch ; [6]

CoS BLI i - Making changes and commits
. - Merging back to main branch *

‘ - Handling merge conflicts
--- page 4 ---
In contrast, describe what a tag is and why it's often used when marking

software releases.

Cc Explain the difference between git merge and git rebase. When would you

Q6
Co5 BLS

use each? What are the pros and cons of each approach? Also explain what | [6]

git cherry-pick does and give one use case for it.

You are tasked with designing a simple Enrollments feature for a
university website using Django's Model-View-Template (MVT)

Q7 architecture. The system should allow linking Students to Courses through
an Enrollment model. Answer the following sub-questions clearly using
short paragraphs, bullet points, or neat diagrams where appropriate:

A Describe how you would define the Django models — Student, Course,
and Enrollment. For each model:
Q7 - Specify the fields with appropriate data types
- Identify primary keys and foreign.keys [6]
CO-3, BL-3 - Define any uniqueness constraints or validation rules
- Explain the relationship type (oné-to-many, many-to-many)
- Mention any methods you would add to the models (__str__, custom
methods)

B Define three URL—View mappings:
1. Endpoint to list all courses a student is enrolled in
2. Endpoint to enroll a student into a new course (form submission)
Q7 3. Endpoint to unenroll/drop a student from a course
For each, explain:
- The URL pattern (e.g., /student/<id>/courses/)
- HTTP method (GET/POST/DELETE)
- What the corresponding view should do (query logic, validation,
response)

[6]
CO-3, BL-2

Cc Explain what the template should display on the course listing page.
Mention:
z - What information should be rendered (student details, course list,
Q7 enrollment dates) .
CO-3; Bist - What user actions should be available (enroll, unenroll buttons) [4]
, - What type of logic should NOT be written inside the template (business
logic, complex queries)
- How to pass data from view to template

D Write a numbered sequence describing the complete request-response flow
when a user submits a form to enroll in a new course (POST request).
Q7 Include:
1. Browser form submission [4]
CO-3, BL-4 2. Django receives request
, 3. URL routing and view execaition
. 4. Form validation
5. Database operations
--- page 5 ---
6. Response generation
7. Redirect or error handling
(Aim for 7-9 detailed steps)

«

Pe

ve
````

## 2024-25 · Final + Re-Exam · Sem 5 · paper 3cda7971fec6

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Introduction to Modern Application Development, Sem-V, Final Exam 2024-25 & Re Ex_ea01fd8e.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 5/12/24
- Text: ocr (4 pages), mean OCR confidence 91.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
Academic Year: 2024-2025

Program: B.Tech/MBA TECH Stream: Data science Year: III Sémester: Vv
Subject: Introduction to Modern Application Development Time: 3 hrs (2 pm to 5 pm)
Date: 5/12/24 No. of Pages 4

Marks:100

Final Examination(2024- 25) )Re- Exam (2028 ~ 24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _l__is compulsory.

2) Out of remaining questions, attempt any 4 __ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks. -

5) Answer to each new question to be started on a frésh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary. .

Q.1 Answer briefly: 20
a) | What is JSX? What are its Key Features? 5
b) | What are Digital Ocean’s Droplets. . . 5
c) | Explain with code inline, internal, and external CSS styles* 5
d) | Write a short note on promises. 5

Q. 2(a) 10

Given a package delivery process which follows sequential execution with callbacks:
Step 1: Placing the order for a package.

Step 2: Processing the payment for the order.

Step 3: Preparing the package in the warehouse.

Final Step: Delivering the package to the customer.

Problem 1: Convert the above package delivery process using Promises to handle the
asynchronous flow.

Problem 2: Using the solution from Problem 1 where Promises were used, now
convert the package delivery scenario using Asyne/Await for better readability and
easier handling of asynchronous tasks.
function step 1 (callback) {
setTimeout(function () {
console.log(""Step 1: Order placed for the package");
callback();
}, 2000);
--- page 2 ---
}
function step2(callback) {

setTimeout(function () {
console.log("Step 2: Payment processed for ‘the package");
callback();
}, 4000);
}
function step3(callback) {
setTimeout(function () {
console.log("Step 3: Package is being prepared in the warehouse");
callback();
}, 3000);
}
function finalStepQ) {
console.log("Step 4: Package delivered to the customer! Enjoy your item.");
} -
// Using callbacks to ensure steps are executed in sequence
step1(Q => { oo
step2(() => { /
step3(() => {
finalStepQ);
})3
})
})

console.log("Other services are running in the background... bye!");

Q.2(b)

How do you create an HTML form with JavaScript validation for the fields: name,
salary, and email? Please provide the code for both index.html (HTML form) and
test.js (JavaScript validation logic) that checks the validity of each field (name, salary,
email) and handles user input validation. :

10

Q. 3(a)

What is a Callback function? What are the different types of JavaScript functions
explaining with sample code in brief?

10

Q.3(b)

Write the code for creating an Employee model and answer the following queries using
the Django shell:

1. How do you create employees (Insert Operation)?

2. How can you retrieve all employees (Select Operation)?

3. How do you retrieve employees ordered by salary?

4. How can you filter employees by salary range?

5. How do you retrieve the first and last employee?

6. How can you count the number of employees?

7. How do you perform aggregation on salaries?

8. How do you retrieve employees with selected fields?

10

Q 4(a)

What is AWS? Explain any 5 AWS services that you are familiar with.

10

2

_
--- page 3 ---
Q. 4b)

Explain Docker Architecture? A short note on Docker Container?

10

Q. 5(a)

Write SQL code for the following operations- ,

1. Create a table Contact with following fields — ID, firstName, LastName, Email,
Salary with appropriate data type for the respective field.

2. Insert five records in the Contact table.

3. Add one more column “Address” in to this table.

4. Update 3rd record with new values.

5. Delete any one record from it.

10

Q.50)

What is the difference between state and hooks in React?
Build a React application to implement components that utilize state and hooks through
a counter program.

10

| Q 6a)

Write a Django code to perform Create and Read operations on the Employee model
(id, name, salary) using Django REST Framework (DRF):

1. models.py: Create the Employee model.

2. serializers.py: Create a serializer for the Employee model.

3. views.py: Create API views for CRUD operations on employee data.

4. urls.py: Define URL patterns for employee CRUD operations.

5. API Endpoints: Specify the URLs that can be accessed via Postman or

Thunder Client for performing Create and Read operations.
For Reference, Use the Table Below for Import Statements:
File Import Statements
models.py from django.db import models
serializers py from rest_framework import serializers
: from .models import Employee

from rest_framework import viewsets
views.py from .models import Employee
from .serializers import EmployeeSerializer
from django.urls import path
untsny tnayapp) from . import views
from django.contrib import admin
urls.py (main project) from django.urls import path, include

10

Q. 6(b)

How Docker does differ from traditional virtualization? Write any 3 Docker commands
dealing with container. What are the limitations of Docker container?

10

Q. 7(a)

How can you integrate a machine learning model with a Django project to perform
predictions? Specifically, use the Iris dataset to train a classification model, create a
Django form to accept user input, and display the predicted class of the Iris flower.
Provide the steps and code examples for training the model, saving it, and integrating it
into a Django project for real-time prediction.

For reference, use the table below for import statements:

10

3
--- page 4 ---
Import Statements on
import pandas as pd
. / oe
from sklearn.datasets import load_iris
train_model.py from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import joblib
forms.py from django import forms

from django.shortcuts import render
views.py import joblib

from .forms import IrisForm

from django.urls import path
from .views import predict

from django.contrib import admin
from django.urls import path, include

A

urls.py (ml_app)

urls.py (project)

Q.7(b) | What are props in React?Develop a simple*React.js application that displays a list of 10
your favourite movies using components and props.
````

## 2024-25 · Re-Exam · Sem 5 · paper 3fb0a252b24c

- Departments: Data Science
- Programmes: MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/DATA SCIENCE/SEM V/Introduction to Modern Application Development/Modern Appl development , Re-exam 2023-24,2024-25.PDF`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 78.7

````text
=

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2024-2025
Program: B.Tech/MBA TECH Stream: Data science Year: IJ Semester: V
Subject: Introduction to Modern Application Development
Date: 24foe}eo9s
Marks: 100

Time: 3 hrs (2 pm to 5 pm)
No. of Pages 3

Re-Examination (2028- oh | 2024-25.)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | Write a note on Droplet? 5
b) | Explain the types of CSS with example 5
c) | A note on Django Architecture 5
d) | Comparison between DBMS and NoSQL Databases 5)

Q. 2(a) Create an HTML form with JavaScript validation for customerName, phoneNo and_ | 10
email fields? Please provide both the HTML code (index.html) and the JavaScript
code (test,js) for the form validation, and write the code for validation of each field.

Q. 2(b) Explain Docker Architecture? Write Docker File for deploying a Django application | 10
with all the required steps to run it as container.

Q 3a) What is Async Await? What are the different types of JavaScript functions 10

explaining explain any three with code?

Q. 3(b) Given a food ordering process which follows of sequential execution with callbacks | 10
Step 1: Placing the food order.

Step 2: Processing the payment.
Step 3: Preparing the order in the kitchen.
Final Step: Delivering the order to the customer..

Problem1: convert the above food ordering process using Promises to handle the
asynchronous flow:

Problem2: By using the solution of Promlem1 where promise was used now
--- page 2 ---
convert the food ordering scenario using async/await for better readability and easier

handling of asynchronous tasks:
function step1(callback) {
setTimeout(function () {
console.log("Step 1: Order placed successfully");
callbackQ;
}, 2000);
}
function step2(callback) {
setTimeout(function () {
console.log("Step 2: Payment processed");
callback(Q);
}, 4000);
}
function step3(callback) {
setTimeout(function () {
console.log("Step 3: Order being prepared"),
callback);
}, 3000);

function finalStepQ {
console.log("Step 4: Order delivered! Enjoy your meal!");

}

// Using callbacks to ensure steps are executed in sequence
step1(Q => {
step2(() => {
step3(() => {

finalStepQ;
3);
})
3);
console.log("Other services are running in the background... bye!");

Q. 4(a) Create a Registration Form Component in React that includes input fields for name, | 10
password, and email. Demonstrate event handling by capturing and displaying the
entered values in the console as the user types. The form should validate that all
fields are filled in before submission.

Q. 4(b) What is AWS? Explain Amazon Lambda, Data Storage, Data Processing & 10
Analytics, Machine Learning, Model Deployment & Serving

Q. 5(a) :| Write SQL code for the following operations- 10

1. Create a table Emp with following fields - F_ Name, L_Name , Job Title, Salary

with appropriate data type for the respective field.
2. Insert five records in the emp table.
3. Add one more column “Contact_No” in to this table.
--- page 3 ---
Q. 5(b)

4. Update 3rd record with new values.
5. Delete any one record from it.

Write the code for creating a Product model
using the Django shell:
1. How do you create products (Insert Operation)?
2. How can you retrieve all products (Select Operation)?
3. How do you retrieve products ordered by price?
4. How can you filter products by price range?
5. How do you retrieve the first and last product?
6. How can you count the number of products?
How do you perform aggregation on prices?
8. How do you retrieve products with selected fields?

and answer the following queries

10

Q. 6(a)

What are React components?

Create a simple React.js application to render a list of

your favourite books using
components and props.

10

Q. 6(b)

Explain difference between Docker and Virtual Machine?

Write Docker commands dealing with deploying mysql from docker hub. How will
you enter into the container and how to check the logs.

10

Q. 7(a)

What are Props? Write a
another component usin
demonstrate the same.

program to show how to pass data from one component to
& props. Create a simple react form with 3 fields to

10

Q. 7(b)

Write a Django code to
(id, name, salary):
1. models.py (Create the Employee model)
2. forms.py (Create the EmployeeForm form)
3. views.py (Create views for inserting and viewing employee data)
4. urls.py (Define URL patterns for employee insert and list operations)
5. employee_create.html (Template for employee data input form)
6. employee_list.html (Template to display the list of employees)
For reference, use the table below for import statements:
File import Statements
models.py from django.db import models

fone from django import forms
‘PY ' from .models import Employee
from django.shortcuts import render, redirect
views.py from .models import Employee
from .forms import EmployeeForm ~

from django.urls import path
urls-py (myapp) from . import views

perform Create and Read Operations on the Employee model

urls.py (main project) from django.contrib import admin

10

from django.urls import path, include
--- page 4 ---
co)
````

## 2023-24 · Final-Exam · Sem 5 · paper c2ddfe28bb44

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Introduction to Modern Application Development, Sem-V, A Y 2023-24, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25/11/23
- Text: ocr (3 pages), mean OCR confidence 91.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEM
Academic Year: 2023-2024

-

Program: B.Tech/MBA TECH Stream: Data science Year: IIT Semester: V
Subject: Introduction to Modern Application Development Time: 3 hrs (2 pm to 5 pm)
Date: 25/11/23 No. of Pages 3

Marks:100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.
3)Inali___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: 20
a) | Explain with code inline, internal, and external CSS styles 5
b) | Write a short program to demonstrate React States b)
c) | What is a Asyn and Await in Javascript? P)
d) | Write a note on Droplet? 5

Q. 2(a) | Create an HTML form with JavaScript validation for name, age and email fields? 10

Please provide both the HTML code (home.html) and the JavaScript code «
(validation.js) for the form validation, and write the code for validation of each field.
--- page 2 ---
Q. 2(b)

Design a HTML page to display given below as it is on

——————

[= Male.
sex @ Female

Eye color ferent i

Check all that apply|| Over on cea

Describe your athletic ability:

a:

10

Q. 3(a)

What is a Callback function? What are the different types of JavaScript functions
explaining with sample code in brief?

10

Q. 3(b)

What is Django Architecture? Explain the project structures of Django Framework.

10

Q. 4(a)

What is AWS? Explain AWS services that you are familiar with

10

Q. 4(b)

Explain Docker Architecture? Write frequently used Docker commands.

10

Q. S(a)

Write SQL code for the following operations-

1. Create a table Contact with following fields ~ ID, firs'Name,LastName, Email, Salary
with appropriate data type for the respective field.

2. Insert five records in the Contact table. ;

3. Add one more column “Address” in to this table. *

4. Update 3rd record with new values.

5. Delete any one record from it.

10

Q. 5(b)

Create a Class and Function Component in React and use it in App.js

10

Q. 6(a)

Explain is Django MVT? Write down the steps for creating the following
1. A new Django project with name “mywebsiste”
2. An app named “mywebapp”
3. How to activate the Admin console?
4. Write the sample code for Creating a View and sample of urls.py of admin
5. Write the sample code for create a simple model

10

Q. 6(b)

How Docker does it differ from traditional virtualization?
Write any 5 Docker commands dealing with images

10
--- page 3 ---
HT

Q. 7(a) | What are Django Models?

“ 10
How can you insert and view the records into a Django model named "Géntact" with
fields "srno" and "name," and ensure they are stored in the database using the Django
ORM? Please provide the necessary steps and code example to achieve this.
Q. 7(b) | What is the difference between state and props in react? 10
Write a program to demonstra

te with sample code how to the states using Hooks
````

## 2023-24 · Final-Exam · Sem 5 · paper a896186cc07b

- Departments: Data Science
- Programmes: MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/DATA SCIENCE/SEM V/Introduction to Modern Application Development/Modern Application Development, Final 23-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25/11/23
- Text: ocr (3 pages), mean OCR confidence 90.1

````text
x
MPSTME \4
LIBRARY

vic OF MA >
yy Mags
7 \
/ wp

SVKM’S NMIMS

Academic Year: 2023-2024

¥

Program: B.Tech/MBA TECH Stream: Data science Year: III Semester: V
Subject: Introduction to Modern Application Development Time: 3 hrs (2 pm to 5 pm)
Date: 25/11/23 No. of Pages 3

Marks: 100 .

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

_~ 3)Iaali__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: . 20
a) | Explain with code inline, internal, and external CSS styles 5
b) | Write a short program to demonstrate React States 5
c) | What is a Asyn and Await in Javascript? 5
d) | Write a note on Droplet? 5

Q. 2(a) | Create an HTML form with JavaScript validation for name, age and email fields?«. 10

Please provide both the HTML code (home.html) and the JavaScript code
_ (validation.js) for the form validation, and write the code for validation of each field.
--- page 2 ---
Q. 2(b)

Design a HTML page to display given below as it is re

[onc Nemec Bae
[Name —_ _ ___

ina Male
__.|€& Female

Sex

[Eye < color _ ; oe fs green ~fo

Check all that apply Ire I Sal |

Describe your athletic ability:

i Enter my information |

10

Q. 3(a)

What is a Callback function? What are the different types of JavaScript functions
explaining with sample code in brief?

10

Q. 3(b)

What is Django Architecture? Explain the project structures of Django Framework.

10

Q. 4(a)

What is AWS? Explain AWS services that you are familiar with

10

Q. 4(0)

Explain Docker Architecture? Write frequently used Docker commands.

10

Q. 5S(a)

Write SQL code for the following operations-

1. Create a table Contact with following fields — ID,firstName,LastName, Email, Salary
with appropriate data type for the respective field.

2. Insert five records in the Contact table. *

3. Add one more column “Address” in to this table.

4. Update 3rd record with new values.

5. Delete any one record from it.

10

Q. 5(b)

Create a Class and Function Component in React and use it in App.js

10

Q. 6(a)

Explain is Django MVT? Write down the steps for creating the following
1. A new Django project with name “mywebsiste”
2. An app named “mywebapp”
3. How to activate the Admin console?
4. Write the sample code for Creating a View and sample of urls.py of admin
5. Write the sample code for create a simple model

10

Q. 6(b)

How Docker does it differ from traditional virtualization?
Write any 5 Docker commands dealing with images

10
--- page 3 ---
Q. 7(a) | What are Django Models? 10
How can you insert and view the records into a Django model named "Contact" with
fields "srno" and "name," and ensure they are stored in the database using the Django
ORM? Please provide the necessary steps and code example to achieve this.

Q.7(b) | What is the difference between state and props in react? 10

Write a program to demonstrate with sample code how to the states using Hooks
````

## 2023-24 · Re-Exam · Sem 5 · paper f999b122edf8

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Intr to Modern Application Development , Re-exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08/02/2024
- Text: ocr (2 pages), mean OCR confidence 92.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

¥

Program: B.Tech/MBA TECH Stream: Data science Year: III Semester: V
Subject: Introduction to Modern Application Development Time: 3 hrs (2 pm to 5 pm)
Date: 08/02/2024 No. of Pages 2
Marks: 100

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | What are Promises in Javascript? 5
l b) | Explain the types of CSS with example 5
c) | Write a short program to demonstrate React Hooks 5
d) | What is Digital Ocean? Write a note on Droplets 5

| Q. 2(a) Create an HTML form with JavaScript validation for name, age and email fields? 10

Please provide both the HTML code (index.html) and the JavaScript code (test.js)
for the form validation, and write the code for validation of each field.

Q. 2(b) Explain Docker Architecture? Write frequently used Docker commands. 10

Q. 3(a) 10

What is Asyne Await? What are the different types of JavaScript functions

explaining explain any three with code?

- 3(b 10
2 300) Create a HTML Page to display a form given below as it is
--- page 2 ---
This is Web Page Main title

[Main M
{HTML
PHP
PERL...
Ss

enu Navigation ne

Q 4(a)

What is Django MVT? Explain the project structures of Django Framework.

10

Q 40)

What is AWS? Explain any 5 AWS services that you are familiar with

10

Q. S(a)

Write SQL code for the following operations-

1. Create a table Emp with following fields - F_ Name, L_Name , Job —Title, Salary
with appropriate data type for the respective field.

2. Insert five records in the emp table.

3. Add one more column “Contact_No” in to this table.

4. Update 3rd record with new values.

5. Delete any one record from it.

10

Q 5(b)

What is Django? Write down the steps for creating the following
1. A new Django project with name “myproject”
2. An app named “myapp”
3. How to activate the Admin console?
4. Write the sample code for create a simple model and register with Admin
5. Write the sample code for Creating a View ‘

10

Q. 6(a)

What are React components? Explain Class component and Function component
with coding example.

10

Q. 6(b)

Explain difference between Docker and Virtual Machine?
Write Docker commands dealing with images

10

Q 7a)

What are Props? Write a program to show how to pass data from one component to
another component using props.

10

Q. 7(b)

What are Django Model?
How can you insert and view the records into a Django model named "Employee"
with fields "srno" and "name," and ensure they are stored in the database using the

Django ORM? Please provide the necessary steps and code example to achieve this.

10
````

## 2022-23 · Final-Exam · Sem 5 · paper c22258ac01d4

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Introduction to Modern Application Development, 3rd Year, Sem-V, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 17 November 2022
- Text: ocr (1 page), mean OCR confidence 87.5

````text
\ SVKM’s NMIMS
fEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

OL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2022-23

Programme: B. Tech (Data Science), Year: HI Semester: V -
’ . HO 7Z
Subject: Introduction to Modern Application Development
- Marks: 100
Date: 17 November 2022 . Time: 10.00 am - 1.00 pm-

Durations: 3 (Hrs).
No. of Pages: 1
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) All questions are compulsory.

2) Figure on the right indicate marks

3)° Student laptop is allowed. °

4) Internet is allowed.

5) Zip all code with your roll no. and SAP-ID.

Ql. | Write a Python program to reverse a tuple. i [10]

Q2 | Write a Python program to print a tuple with string formatting.
Sample tuple: (100, 200, 300) [10]
Output: This is a tuple (100, 200, 300)

Q3 Write a Python program to print a specified list after removing the Oth, 4th

and 5th elements.

Sample List: ['Red’, 'Green', 'White', 'Black', Pink’, 'Yellow’] 00)
Expected Output: ['Green!, 'White', 'Black’]
C Q4 Write a Python program to get the difference between the two lists. Assume 110]
dummy data according to you.
Q5 Create Inventory Management Django project perform following task: - [60]

A Fields of inventory app: - Categdry Name, product Name, Stock, Product-
Id, mrp, offer Price.

B Perform CRUD of Inventory module.

c Design API of Inventory module.

Page of/4
````

## 2022-23 · Re-Exam · Sem 5 · paper 6a506d398301

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM V/INTRODUCTION TO MODERN APPLICATION DEVELOPMENT/Introduction to Modern Application Development, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf`
- Printed on paper: duration hours: 3; exam date: 27 January 2023
- Text: ocr (2 pages), mean OCR confidence 89.2

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Z Program: B. Tech (Data Science) Year: Ill . Semester: V

AcademicY ear: 2022-2023

Subject: Introduction to Modern Application Development -
ubject: Introduction to Modern Application p hedke: 108

Date : 27 January 2023 - Time: 10.00 am - 1.00 pm
Durations: 3 (Hrs)
No. of Pages: O2-
Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) All questions are compulsory. *
2) Figures on the right indicate marks
3) Student laptop is allowed. °
4) Internet is allowed.
5) Zip aii code with your roll no. and SAP-ID.
Ql We are given a string and we need to reverse words of a given string?
Ex: - Input: - "my name is Laxmi" [10]
Output: - “Laxmi is name my”
Q2. | Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1':['a’,'b'], '2':['c','d']}} .
Expected Output: (10)
ac
ad
be
bd
Q3 Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30,.'item4':55, ‘item5':
24}
Expected Output: [10]
item4 55
- item] 45.5
item3 41.3

page oY/2-
--- page 2 ---
.

Q4

Write a Python program to get the difference between the two lists. Assume

dummy data according to you.

[10]

Page © fr

Q5 Create Inventory Management Django project perform following task: - [60]
A Fields of inventory app: - Category Name, product Name, Stock, Product-
Id, mrp, offer Price.
B Perform CRUD of Inventory module.
c Design API of Inventory module.
~
pe
````
