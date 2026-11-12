# Data Analysis with Python: question papers in full

3 unique papers · 2023-24 to 2024-25 · Computer Applications (MCA)

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2024-25 · Final + Re-Exam · Sem 2 · paper 3bedc9f4847e

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/1ST YEAR/II SEMESTER/Data Analysis with Python/Data Analysis with Python Batch 2024-25 Final Batch 2023 Re Exam.pdf`
- Printed on paper: max marks: 50; duration hours: 2
- Text: ocr (4 pages), mean OCR confidence 87.4

````text
E
} an
/. 8

LIBRARY
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN

Academic Year: 2024-2025
Program/s: MCA Year: I

Stream/s ;MCA

4 _—
ff ey
Wty

ERIN@VERS
*

Semester? II

Subject: Data Analysis with Python Time: 2 hrs (10 AM to 12 PM)
Date:_05/05 /2025 : No. of Pages:4
Marks: 50

Final Examination/Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer should be marked properly on jupiter notebook for each new question.

6) Screenshot of all codes should be taken in word document with proper labelling of question number
6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

8)You will be provided with two csv files for this paper

Ql Answer briefly: [10]

co-1; Bl. | 9. Given a list of numbers: . 2
numbers = [3, 14, 17, 21, 36, 42, 49] :
Write a Python program using filter() and a lambda function to keep only

the numbers that are divisible by 7.

Print the resulting list.

Given the following two lists: 2
students = ["Amit", "Neha", "Rohan", "Priya", "Soham"]

marks = [85, 92, 78, 88, 76]

CO-1; BL-1 b.

Write a Python program to create a dictionary where student names are
the keys,marks are the values and print the final dictionary.

CO-3 ;BL-2 G Generate 10 random values for x and y (both between 1 and 5) and plot | 2

them using a line plot.

co-3;B-2 | gq.

Using Python, load the "penguins" dataset from the seaborn library and
obtain its metadata, including Column names and total number of rows and
columns

C0-2; BL-1 e Write a python program to create a SQLite database and connect with the | 2

database and print the version of SQLite database.
--- page 2 ---
Lea
Q2

CO-1:BL-1 Write a Python program that takes a sentence from the user and appends a ba
, user-specified symbol to each word. Additionally, each word should be
capitalized before appending the symbol.
Requirements:
1. Define a function modify_sentence(sentence, symbol) that:
a. Accepts a sentence and a symbol from the user.
b. Capitalize each word.
c. Appends the symbol to every word, keeping punctuation
intact. _
d. Returns the modified sentence.
2. Call the function using user input and print the final modified
sentence.
Q [5]
CO-L:BL2 A contractor needs to process weekly wages for employees. Write a Python

program that retrieves employee details based on a fixed employee ID list.
Requirements:
Define a function empdetails() that:

a. Uses a fixed dictionary of 5 employees with the following

details:
Employee ID Name Weekly Salary (®)
101 Rajesh 15,000
102 Priya 18,000
103 Ananya 20,000
104 Vikram 22,000
105 Sandeep 25,000

b. Accepts an employee ID as input from the user.
c. Retrieves and returns the corresponding employee's name
and salary.

d. Ifthe ID does not exist, it should display an error message.
--- page 3 ---
Q3 1. Create and display a database table: ne [10]
0-2: BL3 a. Create a database named "OfficeDB.db" Lol
, b. Create a table called "staff" with columns:

¢ Staff_ID (Primary Key)

¢ Full_Name (Text) |

° Role (Text)

e Salary (Integer)

¢ Years_of_Experience (Integer)

c. Insert the following records:

Staff_ID |Full_Name|} Role || Salary Years_of Expe

[ 1 al Karan |[Developer|| 80000 L 6 |
|__2 || Meera || Analyst || 70000 || 4 |
[3 _||_ Rohit || Manager'| 95000 | 10 |
[4 __|L_ Sanva [Developer] 85000 | 7 |
[5s __ [| Aditya [ aR | coo00| 3 |

2. Write an SQL query to fetch the Full_ Name and Role of all staff
members.

3. Find all employees who have more than 5 years of experience and display
their details.

4.Remove the staff member with Staff_ID = 2 from the table and display the
updated records after deletion.
--- page 4 ---
Q4

_ [10]
a A company organizes three technical training programs for employees:

¢ Machine Learning (ML)
¢ Cloud Computing (CC)
¢ Cybersecurity (CS)

Each employee can enroll in one, two, or all three programs.

You are provided with a CSV file named "
contains employee details and their
attended, @ = not attended).

employee_skills.esv", which
participation in each program (1 =

(a) Find and print the total number of employees who attended at least
one training program.

(b) Find the department with the least number of participants.

(c) List employees who attended exactly two training programs.

(d) Identify the most popular training program based on the number of
attendees.

ro

: = ig aes ee ee eres 3 bs
a Perform an initial exploration of the supermarket_sales.csv dataset, [5]
Co-3: Classify the features into numerical, categorical, and datetime types. Handle
BL-S missing values appropriately and format data types where necessary to ensure

| consistency in analysis.
Q5 b

aos Clean the dataset by removing duplicate entries and addressing | [5]

BL3 inconsistencies in data. Create new relevant features to enhance analysis.

Detect and remove outliers to improve data quality. Summarize your
observations.

Q6 a Perform a detailed statistical analysis of the feature distributions in the [5]
co. supermarket_sales_missing.csv dataset by examining skewness, the impact of
BL-4 outliers etc. Standardize numerical features to ensure uniformity across
different scales. Provide meaningful insights based on your findings.
CO-3; b Analyse the relationships between different features using Pivot tables, [5]
BL-3 Crosstab/groupby ete and provide key observations from the analysis.
Pe
eo
Q7 Analyse univariate, bivariate, and multivariate analysis on the | [10]
cO-u: supermarket_sales_missing.csv dataset using appropriate visualizations such
BLS. as bar charts, histograms, scatter plots, and heatmaps. Validate your findings

and provide key observations based on the visual insights.
````

## 2023-24 · Final-Exam · Sem 2 · paper 07141edce60c

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/1ST YEAR/II SEMESTER/Data Analysis with Python/Data Analysis with Python Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 50; duration hours: 2
- Text: ocr (2 pages), mean OCR confidence 89.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

¥

Program/s: MCA . Year:1 Semester: II
Stream/s ; .
Subject: Data Analysis with Python - Time: ©2 hrs (/Ogmto/2 noon)

Date:_93/65/2024 No. of Pages
Marks: 50 _

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question Paper | and « on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is eoiapalaory.
2) Out of remaining questions, attempt any 4 Gueasions
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to all questions in one Jupiter notebook labelled properly.
” 6) Screenshot of all codes should be taken in word document with proper labelling of question number
6) Figures in brackets on the right-hand side indicate full marks. ;
7) Use cars_data dataset for questions 5,6,7. Assume Suitable data if necessary.

Ql . Answer briefly: [10]
a. Write two functions sub and mul.
co-t: BLS I. Mul function will take any number; multiply it by 3 and return. 2

I. sub function will take an integer as an input, multiply that number
by 3 by calling mul function, subtract 2 from it and return the value

ods LS b. Teacher has to select all the students having roll numbers that are multiple | 9
, of 5. Help the teacher in displaying it. Use list data structure.
Gia <ni3 & Create a scatter plot presenting the relationship between two random | 7
, variables.
co-3-BL-1 d. Use titanic dataset from SNS library and find out the percentage of male | 9
‘ and female survived.
coos e | Write a python program to create a SQLite database and connect with the | 2
_ database and print the version of SQLite database.
Write a Python code snippet to analyze the distribution of vowels in a given —
string. :
Q2 |. Create a frequency dictionary (vowel_freq) for the vowels. [10]
CO-1;BL-3 ; ll. Print the dictionary and then iterate over the dictionary to display the

percentage of each vowel's occurrence in the given string, ensuring
accurate calculations by dividing by the total number of vowels.
--- page 2 ---
Perform CRUD operations using SQLite3 for managing employee data”.
with the following attributes:
I. Create a database for employees with the following attributes:

Name: John, Alice, Bob, Emily, David

Employee ID: E001, E002, E003, E004, E005 ; ;
Q3 _ Department: HR, Finance, IT, Marketing, Operations [10]
Position: Manager, Analyst, Developer, Coordinator, Specialist

CO-2; BL-2
Salary: 50000, 60000, 70000, 55000, 65000
Status (‘Active’ or ‘Inactive’): Active, Active, Inactive, Active, Inactive
Il. Insert data for 5 employees dynamically as given above.
| III. Search employees with name and Employee ID.
IV. Update salary with Name and Employee ID for an employee Bob and
display the updated database. ;
An organization manages sport events for their employees for the
following sports
A. sporti B. sport2 .C. sport3
Q4 It maintains data of their employee in the Master_Data Table and [10]
CO-1,3;BL- separately as per participation in the events. Find
I. How many employees have participated in‘only one sport with
Name and id? ;
Il. Which city has maximum participation?
Q5 a To explore and analyse the cars_data dataset using Python. This includes
cO-3; "| analyzing each features (columns)in the dataset [5]
BL-2 :
CO-3; b Do the needed data treatments and create any additional columns [5]
BL-3 accordingly. (Data Cleaning). Comment Down your observations

To find the distribution and relationships between different features in

CO-3: your dataset. Also, comment for each distribution and relationships [5]
BL3 between different features.

CO-3; b Create pivots/data frames aggregating the features. Also, comment for [5]
BL-l each Pivot Table

Q7 Create charts to visualize the analyzed results. Validate the output and

0-3; comment down your observations for each visualization. [10]
BL-1
````

## 2023-24 · Re-Exam · Sem 2 · paper 12e84d6179d6

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/1ST YEAR/II SEMESTER/Data Analysis with Python/Data Analysis with Python Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 50
- Text: ocr (2 pages), mean OCR confidence 87.5

````text
SVKM’S NMIMS

Program/s: MCA

Subject: Data Analysis with Python - : Time: _Z _hrs (o:opamto 12 nom)

Date:.2 /7 /2024 : No. of Pages:2
Marks: 50
Ré. Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

~ 1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.”

3) In all 5 questions to be attempted. :

4) All questions carry equal marks.

5) Answer to all questions in one Jupiter notebook labelled properly.

6) Screenshot of all codes should be taken in word document with proper labelling of question number
- 6) Figures in brackets on the right hand side indicate full marks..

7) Use Cuisine_rating dataset for questions 5,6,7 .Assume Suitable data if necessary.

Qi :

: Answer briefly: [10]
Cs a. Create a function name student with his default information as his standard
BLS and school name with provision that if student wants can change default 2

information(exp5) “_
CO-1; b. Teacher has entered math marks for all the students in a list’ Help her to | 9
BL-3 __| display the second highest and second lowest marks. Use list data structure
ry c. Plot the histogram of randomly generated 1000 values. 2
rir qd. Read the given Image and convert it into NumPy array and print its shape. 2
CO-2; e Write a python program to connect a database and create a SQLite table | 2
BL-1 base.{assume table attributes)

Write a python code to extract individual alphabetical characters from a given
string and create a frequency dictionary (character_freq)

Q2 : I. _ Print the dictionary.
0-1: ll. Also, create a loop to iterate over key and value of frequency dictionary [10]
BL3. and print the percentage of each character’s frequency in a.list, ensuring _—

correct calculation by dividing by the total number of characters.
--- page 2 ---
Perform CRUD operations using SQLite3 and perform following
task .
I. Create a database for student with following attributes:
Name :Armaan,Amit,Arya,Aryan,Aman
Roll Number :1,2,3,4,5

Q3 . SAP ID :A001,A002,A.003,a004,A005
2 Program :DS,CS,IT,EXTC,MXTC ~ : [10]
CO-2; BL- Semester :LILULLI

2 Marks :80,90,70,20,10
j ; Result (‘Pass’ or ‘Fail’) -Pass,Pass,Pass,Fail,Fail
Il. Insert data for 5’students dynamically as given above
Ill. Search students with name and sap id
IV. Update marks with Name and'sap id for a student Aryan and display
updated

An organization manages sport events for their employees for.the following

sports
1Qa A. Cricket —_B. Volleyball C. Hockey
coi: It maintains data of their employee in the Master_data Table and. [10]
BL3 separately as per participation in the events.

I. Find the list of employees who participated in all the Sports with
complete information.
I. Find the most active department i in sports

Qs a To explore and analyse the Cuisine Rating dataset using Python. This
CO-3; includes analyzing each features (columns)in the dataset [5]
BL-2 ; ;

CO-3; b Do the needed data treatments and create any additional columns | [5]
a accordingly. (Data Cleaning). Comment Down your observations

Q6 a To find the distribution and relationships between different features in
co-3 your dataset. Also, comment for each distribution and relationships | [5]
Bt) between different features.

cO-3; b Analyse the data and create pivots/data frames aggregating the features. | [5]
BLS Also, comment for each Pivot Table.

Q7 Create charts to visualize the analyzed results. Validate the output and
c0-3: comment down your observations. for each visualization. {10}
BL-1

2.
````
