# Python for Data Analysis: question papers in full

6 unique papers · 2023-24 to 2024-25 · Common (all branches), Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2024-25 · Final-Exam · Sem 2 · paper 226d7a6b397b

- Departments: Common (all branches)
- Programmes: B TECH
- Source: `02_Question_Papers/Legacy/B TECH/1ST YEAR/II SEMESTER/PYTHON FOR DATA ANALYSIS/Python for Data Analysis, Final Exam 2024-25.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 91.1

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025
Program/s: B Tech /MBA Tech Year:I1 Semester II
Stream/s: CSE-DS/ DS

Subject: Python for Data Analysis Time: 3 hrs @:00 pm to 5:00 pm)
Date:_03/ 05 / 2025 No. of Pages: 05"
Marks: 100

Final Examination 2024-25

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 __ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: ; [20]
CO-1; SO-2; Write the python program to demonstrate any five bitwise operators.
BL-2 a.
[05]
CO-2; SO-2; Implement operatioris on NumPy arrays of different dimensions:
BL-2,4 b.- i) Create a 1D array with values from 0 to 8 - [05]
ii) Create a 3x3 matrix of random integers between | and 50
(include)
iii) Demonstrate broadcasting by adding the 1D array to each row of
the matrix
CO-3; SO-2; Given the following Series:
BL-2,3 c. | SI 82 [05]

A 10 A 5
B 20 B 4
Cc 30 ‘cr 6
D 40 Dies
Write the command to find the multiplication of $1 and S2.
--- page 2 ---
CO-3; SO-2; NASA is analyzing fuel consumption data for spacecraft missions. One
BL-2,3 d. | dataset contains spacecraft names and fuel type, while another dataset [05]
contains fuel consumption details. Perform a left join to retain all spacecraft
names, even if fuel consumption data is missing.
Task: F
i) Create two DataFrames — spacecraft_df and fuel_df.
ii) Merge them using a left join on Spacecraft_Name.
iii) Display the merged DataFrame.
Input:
# Spacecraft details
spacecraft_data = {
"Spacecraft_Name': ['Apollo 11', 'Voyager 1', 'Falcon 9’, 'Discovery'],
'Fuel_Type': ['Hydrogen’, 'Plutonium', 'LOX/RP-1', 'Hydrogen']}

# Fuel consumption data

fuel_data = {
'Spacecraft_Name': ['Apollo 11', 'Falcon 9', 'Discovery'],
'Fuel_ Consumption’: [1000, 600, 1100]}

Q2 Write the Python program to create dictionary and perform stated operation
CO-1; $O-2; | a. | on it, display the content of dictionary using for loop, create the list that [10]
BL-4 contains all keys of dictionary, create the list that contains all the values of

dictionary, update the value of particular key, remove elements with
specified key, create the new dictionary using dictionary.comprehension,
creating dictionary using list of tuples.

Q2 You are given a JSON file named Student.json that contains details of
CO-2; SO-2; | b. | multiple students, including their name, age, city, and languages known. [10]
BL-2,4 Perform the following tasks using the JSON module in Python:

Tasks:

i) Read the Student,json file and print all the languages known by the
student named Saniya.

ii) Print the names of all students in the dataset.

iii) Count the total number of students in the dataset.

iv) Print the names of students whose age is above 20 years.

Q3 1) Write a Python program to:
CO-2; SO-2; | a. i) -Accept the name, age, and marks of 3 students from the user. [10]
BL-2,3 ii) Store the collected data in a CSV file, write column headers also

iii) Read the CSV file and display its contents.

I)Read a txt file, text.txt and write the Python Program for the following:
i) Find the number of unique words in the text
ii) Count the number of times the word "book" appears

2
--- page 3 ---
Q3 Write a Python program to print all the perfect numbers in a given range using

CO-1; SO-2; | b. | function. Note: A number is called perfect if the sum of proper divisors of that

BL-4 number is equal to the number. For example, 28 is perfect number, since [10]
14+2+4+7+14=28.

Q4 Create a student performance analysis system using NumPy: Generate a 2D
CO-2; SO-2; | a. | array of shape (20,6) representing scores of 20 students across 6 subjects [10]
BL-4 with random values between 40 and 100.

Calculate the following:
i) Average score for each student and each subject
ii) Standard deviation of scores for each subject
iii) Use cumsum to analyze progressive improvement across subjects

Q4 T) Write a Pandas program to calculate the following for the given
CO-3; SO-2; | b..| exam_data DataFrame: [10]
BL-2,3

i) Find the total score of all students.
ii) Filter and display only the students who qualified for the exam.
iii) Remove the 'attempts' column from the given DataFrame.
exam_data ={
‘name': ['Mike'’, ‘Emily’, ‘Michael’, 'Matthew’, 'Laura’, 'Kevin'],
'score': [9, 20, 14.5, 21, 8, 19],
‘attempts’: [2, 3,.1, 1, 2, 1],
‘qualify’: ['no', 'yes’, 'yes', 'no', 'no’, 'yes']
}
labels = ['e', 'f, 'g', 'h’, ‘i’, 'j']

._. | ID How does _.loc[] differ from .iloc[] in Pandas? Provide an explanation
with examples.

Q5 Given the following DataFrame containing order details, write a Pandas
CO-2,3; SO- | a. | program to perform the following operations: [10]
2;
BL-2,3 i) Drop rows where at least one element is missing.
ii) To identify and display missing values in a given DataFrame. The

program should print True for missing values and False for non-
missing values.

ili) Write a Pandas program to filter and display rows from a given
DataFrame where the 'purch_amt' column has values greater than

1000 and the 'customer_id' column has values less than 3003.
--- page 4 ---
ord_no purch_ amt ord_date customer_id salesman_id

70001.0 L50250 — 2012-10-05 3002 5002.0
NaN 270.65 2012-09-10 3001 5003.0
70002.0 65.26 NaN 3001 5001.0
70004.0 110.50 2012-08-17 3003 NaN
NaN 948.50 2012-09-10 3002 5002.0
70005.0 2400.60 2012-07-27 3001 5001.0
NaN 5760.00. 2012-09-10 3001 5001.0
70010.0 1983.43 Z20Ot2— 0a 0 3004 NaN
70003.0 2480.40 2012-10-10 3003 5003.0
70012.0 250.45 = 20P2-06-27 3002 5002.0
NaN 75.29 2012-08-17 3001 5003.0
70013.0 3045.60 2012-04-25 3001 NaN
5 Create a python code to demonstrate the any five set operations on the 1D
CO-2; SO-2; | b. | array. [10]
BL-2,4
Q6 Consider the following series:
CO-2,3;SO- |a | 0 4.0 [10]
2; 15.0
BL-2,3 Ze eO
3 NaN
4 1.0
ae 10:0
dtype: float64
Write a python code to
i) Add 1 to all the elements.
ii) To replace all NaN with 0
iii) Display the first three elements of the Series.
iv) Find the sum of all the values in the Series.
v) Sort the Series in ascending and descending order.
Q6 You are given three datasets containing employee details and their technical
CO-3; SO-2; | b. | skill scores. Perform the following operations: [10]
BL-2,3

student_df = pd.DataFrame({'Student_ID': [201, 202, 203], 'Name': ['Raj’,
'Meera’, 'Kunal']})
exam_df = pd.DataFrame({'Student_ID': [201, 202, 204], 'Exam_Score': [85,
90, 75]})
new_students_df = pd.DataFrame({'Student_ID': [204, 205], 'Name':
['Sneha', 'Arjun']})
i) Merge two dataframes student_df and exam_df on a common column
ii) Perform an outer join on student_df and exam_df
iii) Do a left join on student_df and exam_df
iv) Do aright join on student_df and exam_df
v) Concatenate student_df and new_students_df and ignore index
--- page 5 ---
Q7 Use the given dataset retail_sales_dataset.csv for solving the following

CO-2; SO-2; questions and also analyse them in brief: [20]
BL-2,4 i) Create a styled line plot for the Total Sales with the following
properties:

Line style should be dashed, and line colour should be blue.
Display the legend at the upper right location.
X-axis label: Transaction ID
Y-axis label: Total Sales Amount
Add square markers.
Line marker colour should be green.
Line width should be 2.5.

ii) Read and display the sales data of Electronics, Clothing eee
using a bar chart. Save this piot as an image file.

iii) Calculate the average sales per product category and plot it using a
scatter plot.

iv) Find and display the top 3 product categories with the highest profit
using a bar chart.
--- page 6 ---

````

## 2024-25 · Re-Exam · Sem 2 · paper 37e362d50b3f

- Departments: Common (all branches)
- Programmes: B TECH
- Source: `02_Question_Papers/Legacy/B TECH/1ST YEAR/II SEMESTER/PYTHON FOR DATA ANALYSIS/Python for Data Analysis, Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 /05 /202
- Text: ocr (2 pages), mean OCR confidence 93.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS EN GINEERING
Academic Year: 2024-2025

Program: BTech/MBATech Stream ; DS / CSE-DS (7057) /CSE-DS Year: | Semester: 2
Subject: Python for Data Analysis Time: 3 hrs (2:00pm to: oopry)
Date: 03 /05 /202S .

No. of Pages: 2
Marks: 100

Re-Examination (Batch 2023-2024)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 __ questions.

3) In all__5_ questions to be attempted:

4) All questions carry equal marks. ;

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi (a) Explain the difference between if, elif, and else statements in Python with suitable
examples.
(b) What is the significance of exception handling in Python? Explain with an example. 20
marks
c)What are lists in Python? How do they differ from tuples? Provide an example for each.
(d) Write a Python program to check if two strings are anagrams.
Q2 (a) Differentiate between while and for loops with examples.
(b) Write a Python program to generate the Fibonacci series up to n terms using loops.
20
marks
Q3 (a) Explain how to read and write CSV files using Pandas with examples.
(b) Write a Python program to filter rows in a Pandas DataFrame based ona condition.
20

marks
--- page 2 ---
a4

(a) What are subplots in Matplotlib? Explain with an example.

(b) Write a Python program to create a scatter plot using Matplotlib. 20
marks
Q5 (a) Explain the difference between find(), index(), and count() string functions with examples.
(b) Write a Python program to remove all duplicate characters from a given string.
20
marks
Q6 (a) Explain the difference between append(), extend(), and insert() methods in lists with
examples.
(b) Write a Python program to find the second largest number in a list. 20
marks
Q7 (a) Explain how to iterate over dictionary keys and values using loops with examples.
(b) Write a Python program to count the frequency of each word in a given text using dictionaries.
20

marks
````

## 2023-24 · Final-Exam · Sem 2 · paper c951b76e1cdf

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/1ST YEAR/II SEMESTER/PYTHON FOR DATA ANALYSIS/Python for Data Analysis, Sem-II, Final Exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 89.5

````text
SVKM?S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

* Program/s: B. Tech / MBA Tech Year: 1 Semester: II
Stream/s : DS / CSEDS | .
Subject: Python for Data Analysis : Time: 3 hrs (2: 00pmto 5? 00pm)
Date:_3_/ 05/2024 No. of-Pages: 4
Marks: 100
Final Examination "

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary. .

Qi . :
Answer briefly: [20]
Cco-1,2; a.
SO-1; Write a Python program to convert alternate letters to uppercase in a string. 5
BL- 1
CO-2; b.
S0-1; Write a Python Program to count the number of times an item appears in the list. | 5
BL-1
CO-1,2 ; Ce . at
50-1: Explain the following dictionary methods with an example. 5
BL-2 ~ a) keys() b) pop() c) update() d) values() e) items()
CO- 2; d. . : ’
50-1: Write a python code to read the text file — file11D.txt and replace the word 5
BL 1 “school” to “college”. Print the replaced lines.
Q2 a.) Explain the Identifiers, Keywords, Statements, Expressioris, aiid Variables in
CO-2; SO- Python programming language with examples. [20]
1;
b.) Write a Python Program to reverse a number and also find the Sum of digits
BL-1,2
in the reversed number. Prompt the user for input.
Q3 a.) Write a Python program to find the GCD of the given two positive numbers. - [20]
568 and 992
--- page 2 ---
1; BL- 1 b.) Write a Python program to count the total number of vowels, consonants
and blanks in the below String.

- “The quick brown fox jumped over the wooden beige fence.”

CO-2; SO- 3 ae

Q4 a.) Given a point(x, y), write Python program to find whether it lies in the
CO-2; 50- First, Second, Third or Fourth Quadrant of x - y Plane. [20]
a * b.) Explain the following list functions
BL-2 a)len() b)sum() c)any() d)all()_ e) sorted()
Use the pandas library and import the dataset — ds_salaries.csv
Carry out the below mentioned EDA steps.
1) Fill/drop all missing values for “salary” column
Q5 2) Calculate the value counts for the “work_year” column
CO-1,2.3: 3) Calculate the average of “salary_in_usd” column for Full time [20]
S0-2: employees — (employment_type = FT)
BL- 3 4) Calculate the percent of hybrid employees (remote_ratio = 50) for
the work_year = 2021 and 2022
5) What is the difference of average “salary_in_usd” between
“company_size” = M and “company_size” = eS
a.) Write a Python program that takes a text file as input and returns the
number of spaces in each line of a given text file. The outputs should. be
Q6 stored and printed ina list.
b.) Answer the below 2 questions :
CO-2,3; ) 4 [20]
SO-2; - What is the difference between loc and iloc
BL- 1,2 - Explain with suitable code different ways to create a pandas
DataFrame - Using Python Dictionary, Using Python Lists
Use the dataset —- company_sales_data.csv for solving the below questions.
a) Read Total profit of all months and show it using a line plot
b) Get total profit of all months and show line plot with the following
Q7 Style properties
Generated line plot must include following Style properties: —
CO-3; SO- - Line Style dotted and Line-color should be red [20]
23 - Show legend at the lower right location. ;
BL- 3 - label name = Month Number

- Y label name = Sold units number ‘
- Add acircle marker.

- Line marker color as read

-__Line width should be 3
--- page 3 ---
c)

d)

Calculate total sale data for last year for each product and show it .
using a Pie chart

Read sales data of bathing soap of all months and show it using a
bar chart. Save this plot on the system.
````

## 2023-24 · Final-Exam · Sem 3 · paper b8850068f591

- Departments: Data Science
- Programmes: MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/MBA TECH/2ND YEAR/DATA SCIENCE/Semester 3/Python for Data Analysis/Python for Data Analysis , Final 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 89.2

````text
SVKM’S NMIMS 5 Ns
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
Academic Year: 2023-2024

Program/s: MBA Tech Year: IL _ Seniester: WN
Stream/s ;_Data Science

Subject: Python for Data Analysis Time: 3 hrs (10:00 am to 1:00 pm)
Date:_8 / 12   /2023 No. of Pages: 3

Marks: 100,

Final Examination(2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1). Question No. _1___ is compulsory.
¢>, 2) Out of remaining questions, attempt any _4 questions.
3) In all__5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql A
[20/20]
CO-1; i
SO- 2; Plot the histogram of randomly generated 1000 random numbers. [5]
BL-1I
ii Create a scatter plot presenting the relationship between two random [5]
variables. ;
B Assume s is a string of uppercase characters. Write a program that prints
wz | CO-2; the number of times the string 'BDA' occurs in s. For example, if s =
SO-2; ‘SHALJNILYABDAJHOIUYTBDA ’, then your program should print [10]
BL-3 Number of times BDA occurs is 2
Q2 A
Ban Create two random array A and B through numpy, check if they are equal [10]
50-3: or not
BL-4
B Create two random array A and B through numpy and compute [10]
((A+B)*(-A/2))
Q3 Create a 20x20 array with random values and find the minimum and [10]
A maximum and mean values
--- page 2 ---
CO-3;

SO-4; Te
BL-5
B Write a function to print the output as [10]
array([ 5, 8, 11, 14, 17, 20, 23, 26, 29, 32])
Q4 A
ce Compute the maximum for each row in the given array [10]
BL-4
Write a Python program to count the number of characters (character [10]
B frequency) in a string. Sample String: google.com'.
A Write down the code Create below two data frame and after that concat
both the data frame.
Dataframe-1
Name Age Address Qualification
0 Jay 23 Nagpur Msc
1 Prine 24 Kanpur MA
5 2 Gaurav 22 Allahabad MCA
Q 3 Anuj 20 Kannuaj Phd
CO-3; [10]
SO-3;
BL-4 Dataframe-2
Name Age Address Qualification
4 Abhi 17 Nagpur Btech
5 Ayushi 14 Kanpur B.A
6 Dhiraj 12 Allahabad Bcom *
7 Hitesh 52 Kannuaj B.hons
B Create a list then convert into data frame in python [10]
A
06 df= { 'G1': [10, 20,30,40],
'G2': [25, np.NaN, np.NaN, 29],
Co-2; (25, np P [10]
SO-4; 'G3': [15, 14, 17, 11],
BL-3

'G4': [21, 22, 23, 25]}

~~
--- page 3 ---
SO =

# Create a DataFrame from dictionary
df = pd.DataFrame(df)

Replace np.NaN value in df with mean

B # importing pandas

import pandas as pd

# Using DataFrame() method from pandas module

dfl = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7],
"b": [2, 3, 4, 2, 3, 4, 5],
"ec": [3, 4, 5, 2, 3, 4, 5], [10]
"d": [4, 5, 6, 2, 3, 4, 5],
"e": [5, 6, 7, 2, 3, 4, 5]})

print(df1)

Slicing column from ‘a’ to ‘d’ in the dataframe df]

Q7 A
Ein Write down the Python program to create matrix [10]
BL-3
B import numpy as np
df = np.array([[1, 2, 3], re
[4, 5, 6],
(7, 8, 91) [10]
Write down the code to slicing the df array to display below array
([2 3]
[5 6]
````

## 2023-24 · Re-Exam · Sem 2 · paper 294495261fb0

- Departments: Common (all branches)
- Programmes: B TECH
- Source: `02_Question_Papers/Legacy/B TECH/1ST YEAR/II SEMESTER/PYTHON FOR DATA ANALYSIS/Python for Data Analysis, Re-exam 2023-20240001.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 90.0

````text
SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program/s: B. Tech / MBA Tech Year: 1 Semester: II
Stream/s : DS / CSE DS \
Subject: Python for Data Analysis : : Time: 3 hrs Zope 5: ‘eaPre Pn)
Date:_5_/ 7 _/ 202% No. of Pages: 3
Marks: 100
' Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary. ;

Qi ;

Answer briefly: : [20]
CO-1,2; a.
SO- 1; Write a Python code to find the sum of the factorial of a number sequence. [3,5,2] | 5
BL- 1
CO-2; b.
SO-1; Write a Python code to check if a given year is a leap year or not. 5

@®) | BL-1
CO-1,2 ; G:
SO- 1; Explain the relation between tuples, lists and dictionaries in detail. 5
BL-2
CO- 2; d. . , ' ,
50-1: Write a python code to read the text file — file21D.txt and replace the word 5
BL-1 7 “college” to “school”. Print the replaced lines.
a.) Describe Arithmetic Operators, Assignment Operators, Comparison
Operators, Logical Operators and Bitwise Operators in detail with

Q2 examples.
CO-2; SO- [20]
1: b.) Write a Program to Prompt for a Score between 0.@ and 1.0. If the Score
BL-12 is out of range, print an error. If the score is between 0.0 and 1.0, print a

grade using the following table
--- page 2 ---
Score Grade

>= 0.9 A
>= 0.8 B
>= OF Cc
P= 0.6 D
<0.6 F
; a.) Write a Python program to check if a 3-digit number is Armstrong
Q3 number or not.
CO-2; SO: (20)
"e, b.) Write a Python program that calculates the number of words, digits,
1; BL-1 uppercase letters and lowercase letters in the string given below:
-“ThE quick brOWn fox jUm6ed OvEr Th3 wOod3n GeiGe f3NcE.”
a.) Write a Python program to check the validity of a password given by the
user.
The Password should satisfy the following criteria:
1. Contain at least 1 letter between a and z
Q4 2. Contain at least 1 number between 0 and 9
3. Contain at least 1 letter between A and Z
CO-2; SO- 4. Contain at least 1 character from $, #, @ [20]
1; 5. Minimum length of password: 6
BL- 2 6. Maximum length of password: 12
b.) Explain the following list methods with an example.
a) append() b)extend() c)insert()_ d) index() _e) sort()
Use the pandas library and import the dataset — ds_salaries.csv
Carry out the below mentioned EDA steps.
Q5 1) Fill/drop all missing values for “salary” column
2) Calculate the value counts for the “job_title” column
CO-1,2,3; 3) Calculate the average of “salary_in_usd” column for Part time and. [20]
SO-2; CT employees.— (employment_type = PT and CT)
BL- 3 4) Calculate the percent of work from office employees (remote_ratio
= 0) for the work_year = 2020 and 2021
5) What is the difference of average “salary_in_usd” between
“company_size” = Land “company_size” =S
a.) Write a Python program that takes a text file as input and returns the
Q6 number of words of a given text file.
Son b.) Answer the below 2 questions: — s [20]

- What is the difference between loc and iloc
- Explain with suitable code different ways to create a pandas °.
DataFrame - Using Python Dictionary, Using Python Lists

BL- 1,2

2
--- page 3 ---
Use the dataset — company_sales_data.csv for solving the below questions.
a) Read all product sales data and show it using a multiline plot
b) Read toothpaste sales data of each month and show it using a

Q7 scatter plot
c) Read face cream and facewash product sales data and show it using
CO-3; SO- the bar chart 7 [20]
2; d) Read the total profit of each month and show it using the histogram
BL- 3 to see the most common profit ranges
e) Calculate total sale data for last year for each product and show it
using a Pie chart :
a
oO
````

## 2023-24 · Re-Exam · Sem 3 · paper f46af349917d

- Departments: Data Science
- Programmes: MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/MBA TECH/2ND YEAR/DATA SCIENCE/Semester 3/Python for Data Analysis/Python for Data Analysis , Re-exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 87.9

````text
SVKM’S NMIMS =F
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024 an
Program/s: MBA Tech Year: IL _ Semester: TL
Stream/s ; Data Science
Subject: Python for Data Analysis . Time: 3 hrs (10:00 am to 1:00 pm)
Date:__I9 / 02 /2024 No. of Pages: 3

Marks: 100
Re Examination(2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

> 1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4 _ questions.
3) In all__5__ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary. -
Qi A
[20/20]
CO-1; i Write a NumPy program to create a 5x5 zero matrix with elements on the
SO- 2; Lo. [5]
BL-1 main diagonal equal to 1, 2, 3, 4, 5
ii Plot the line chart of randomly generated 1000 random numbers. [5]
CO-2: B Write a Python function that accepts a ‘
S0-2 2 string=”KLADsbhahdUYUMNkayj” and counts the number of upper and [10]
oO , lower case letters
BL-3
Q2 A a . ea
Create a list(iterable) of the scores of 10 students in a Chemistry exam and
CO-2; filter out those who passed with scores more than 75 using filter [10]
SO-3;
BL-4
B Create two random array A and B through numpy and compute [10]
((A+B)*(-A/2))
Q3
Create a 20x20 array with random values and find the minimum and
CO-3; A : [10]
SO-4; maximum and mean values
BL-5
B import pandas as pd [10]
--- page 2 ---
# creating dictionary of lists

data= {'name': ["sohom", "rakesh", "rajshekhar", "sumit"],
‘department’: ["ECE", "CSE", "EE", "MCA"],
'CGPA': [9.2, 8.7, 8.6, 7.7]}

# creating a dataframe ,

df = pd.DataFrame(data)

Add a new column with all zeroes in the df dataframe

# importing pandas
A import pandas as pd
# Using DataFrame() method from pandas module

dfl = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7],

Q4 "b": [2, 3, 4, 2, 3, 4, 5],

CO3-; "eo": [3, 4, 5, 2, 3, 4, 5], [10]
SO-3;

BL-4 "d": [4, 5, 6, 2, 3, 4, 5],

"e": [5, 6, 7, 2, 3, 4, 5]})
print(df1)

Slicing column from ‘c’ to ‘d’ in the above data frame df

B Create an array then convert into data frame in python 7 [10]
Q5
CO-3; A Write the Python program to create Dictionary [10]
SO-3;
BL-4

B Write down the code to create a 3D array with shape (2, 3, 4) [10]
06 A import numpy as np

df= np.array([[1, 2, 3],
co-2: p.array({[1, 2, 3] 10
SO-4; [4, 5, 6],
BL-3
[7, 8, 9]])
--- page 3 ---
Write down the code to slicing the df array to display below array
[2]
[5]
[8]]

ron

Write down the code to compute the minimum for each row in the given

; [10]
array in python
Q7.
CO-2 ; Write a python function to print the output as [10]
SO-2 ; [18, 10, 15, 13, 8]
BL-3 ‘
Generate two random variable X and Y then plot the histogram of botii [10]
Y ae’

through matplotlib library
````
