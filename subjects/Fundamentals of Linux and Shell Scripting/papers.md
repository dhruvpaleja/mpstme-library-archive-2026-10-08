# Fundamentals of Linux and Shell Scripting: question papers in full

1 unique papers · 2025-26 to 2025-26 · Electronics and Telecommunication

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Re-Exam · Sem 4 · paper 22d2dbf43dee

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/EXTC/SEM IV/FUNDAMENTALS OF LINUX AND SHELL SCRIPTING/Fundamentals of Linux and Shell Scripting, Sem-IV, Batch 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 /July / 2026
- Text: ocr (3 pages), mean OCR confidence 91.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program/s: B Tech Year: I] Sefftester: IV .
Stream/s; EXTC :

Subject: Fundamentals of Linux and Shell Scripting Time: 3 hrs. (02:00 pm to 05:00 pm)
Date: 07 /July / 2026 No. of Pages: 3
Marks: 100

Re-Examination 2025-26

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Save all scripts in your home directory using the naming convention: Q<no>_<part>.sh (e.g., Q2_a.sh)
> 6) Allscripts must begin with a proper shebang line (#!/bin/bash) and include comments.

Ql Answer briefly: ; [20]
CO-1; SO- | a. Open a terminal in Linux. Write one pipeline command to view all files
hia including hidden files from the present working directory, sort the list [04]
alphabetically, save it into output.txt, and print only the first 10 lines.
CO- 1; b. Create a text file containing 8 lines of data. Write Linux commands to display [04]
a the first 3 lines using head and the last 3 lines using tail.
CO-2; SO- | c. Write a shell script using a for loop to print even numbers from 2 to 20. [04]
1;
BL-3
CO-3; SO- | d. Create an array containing five city names and display all elements using a [04]
1; :
BL3 loop.
wm | CO-3; SO- | € Explain the purpose of grep, sed and awk commands with one example each. [04]
1; .
BL-2
Q2 a “File Permission Manager: Write a script perm_manager.sh that: (i) Lists all
. files in the current directory with their permissions using ls -1. (ii) Accepts a
CO-2; SO- ; a ole ie
1: filename and desired permission (e.g., 755) as arguments and applies it using
BL-l 3 chmod. (iii) Changes the ownership of a specified file to a given user: group [10]
> using chown. (iv) Verifies and prints the updated permissions after changes.
(v) Demonstrates creation, copying, moving, and deletion of files using cp,
my, rm with appropriate flags. Demonstrate with at least two files.
CO-3; SO- | b Answer the following theory questions: (i) What is a shell? List and describe
1; four types of shells in Linux. Which is the default shell in Ubuntu and why? [10]
BL-2 (ii) Explain the set command in shell. What do set -x and set -e do? How are
7 they useful in debugging shell scripts?
Q3 £ ia Write a shell script employee_mgmt.sh that: [10]

Page 1 of 3
--- page 2 ---
CO-1; SO- (i) Declares an associative array employee where keys are employee IDs and
ig values are employee names.(ii) Declares another associative array salary for
BL-3 the same employee IDs storing their monthly salaries.(iii) Uses a for loop to
iterate through the arrays and display a formatted report: ;
Emp ID | Name | Salary | Category, where: :
e Salary > 80,000 - High
e 50,000-79,999 - Medium
e Below 50,000 - Low
(iv) Calculates and prints:
e Average salary
e Highest salary
e Lowest salary
CO-2; SO- | b Answer the following theory questions:
i; (i) What is the difference between cat, more, and less commands? When would
BL-1,2 h? [10]
you use each?
(ii) Explain the grep command with the -i, -v, and -c flags. Give one example
for each flag.
Q4 a Demonstrate the following Linux operations in the terminal: (i) Create a
CO-3: SO- directory structure: projects/linux/scripts/ using a single mkdir -p command.
1: > (ii) Create three files: intro.txt, notes.txt, run.sh inside scripts/. (iii) Use Is -IR [10]
BL-3 to recursively list the directory. (iv,) Use find to search for all .sh files in the
projects directory..(v) Use chmod to make run.sh executable and verify with Is
-l.
CO-3; SO- | b Write separate scripts to demonstrate For loop, while’loop, if-elif-else and
1; Nested loop. [10]
BL-3
Q5 a Debugging Lab: The following shell script contains intentional errors. Copy it [10]
: into a file execute it using set -x and set -e, identify all errors, correct them,
CO-4; SO- .
l: and demonstrate successful execution.
BL-3 .
#!/bin/bash
read -p "Enter directory name: " dname
if [-d $dname ]
then
echo "Directory exists"
ls $dname
mkdir $dname/new_folder
else
7 echo "Directory does not exist
, mkdir $dname
of echo Directory created successfully
— fi
Ab Answer the following theory questions: (i) What are cron jobs in Linux?
CO-3: SO- Explain the cron syntax (* * * * * command) field by field. Write cron entries
_ 1; , for: (a) every Monday at 9 AM, (b) Ist of every month at midnight, (c) every [10]
: BL-3 30 minutes. (ii) What are best practices for writing shell scripts? Explain any
five: (shebang, comments, error handling, exit codes, input validation, use of
functions, etc.).
Q6 a, Student Marks Management using Arrays: Write a script student_mgmt.sh [10]

that:

Page 2 of 3

)
--- page 3 ---
>

CO-3; SO-
I:

(i) Declares an associative array student where keys are roll numbers and
values are names. .

BL-3 (ii) Declares a second associative array marks for the same roll numbers with
their marks (0-50). #
(iii) Uses a for loop to iterate and print a formatted report: Roll No | Name |
Marks | Grade.
(iv) Calculates and prints the class average, highest mark, and lowest mark
using arithmetic in the script.
CO-4; SO- | b Answer the following theory questions: [10]
iF (i) What is version control? What is Git? Explain the following Git commands:
BL-l init, add, commit, status, log.
Q7 ;
To automate a system administration task using a shell script that monitors
CO-3; SO- | a disk usage, memory usage, and running processes then logs the results. [10]
1; Schedule this script using a cron job for automatic execution and manage the
entire project using Git version control.
BL-3
Q7
Cie ey |b a) Explain best practices for writing efficient shell scripts. Lee
SO-1; b) Explain any two.real-world applications of shell scripting.
BL-2

Page 3 of 3
````
