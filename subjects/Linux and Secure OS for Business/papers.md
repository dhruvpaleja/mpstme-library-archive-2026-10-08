# Linux and Secure OS for Business: question papers in full

9 unique papers · 2023-24 to 2025-26 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 4 · paper 62207043789d

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/QP_Linux and Secure OS for Business(702CO0C069)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Linux and Secure OS for Business
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question number 1 is compulsory
5. Attempt any 4 from the rest
1. All question are compulsory   20M
a) List and explain any four compression commands available in Linux. 5M
b) List four common Linux file systems. Describe the key characteristics and suitable use case for any two of
them.5M
c) What is package management in Linux? Compare apt and yum/dnf package managers with suitable
commands for installing, updating, and removing packages.5M
d) What is an Access Control List (ACL) in Linux? Explain the getfacl and setfacl commands.5M
2.   20M
A user needs to organize files in a directory using Linux CLI.
• Write commands to: create a directory named projects, move a file into it, copy the file, delete
the copied file. (8 Marks)
• Explain the purpose of each command used. (6 Marks)
• Write a command to display file contents and create an empty file. (6 Marks)
3.   20M
A company needs to take a backup of a live database without stopping services.
• Explain LVM architecture. 10M
• Write steps to create a snapshot of a Logical Volume.5M
• Describe how to mount and take backup from the snapshot.5M
4.   20M
A software development company maintains a shared project directory where multiple developers need
access. All files must inherit group ownership, only owners can delete their files, and certain scripts run
with elevated privileges.
Write a comprehensive note explaining how SUID, SGID, Sticky Bit, and ACLs can be used to
implement this requirement. Include commands and examples.
********** 1 **********
--- page 2 ---
5.   20M
A user reports that they cannot access a remote server, while others can access it successfully.
• Demonstrate how to troubleshoot using ping, traceroute, netstat, ss, nslookup, and dig.10M
• Explain how each command helps diagnose the problem.5M
• Propose solutions based on possible causes (DNS issue, firewall restriction, routing
problem).5M
6.   20M
You are a system administrator responsible for monitoring a Linux server.
Scenario: Write a shell script that:
• Uses proper shebang and comments
• Accepts a CPU usage threshold from the user using read
• Uses if-elif-else to display Normal / Warning / Critical
• Stores logs in a file if usage exceeds threshold
• Uses file test operators to check if log file exists; create if not
• Schedules the script to run every 5 minutes using cron
Tasks:
• Write the complete script 10M
• Explain each part of the script 5M
• Write the crontab entry and explain cron fields 5M
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 059a2c246eff

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/QP_Linux and Secure OS for Business(702CO0C069)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Linux and Secure OS for Business
Date: 01 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question number 1 is compulsory
5. Attempt any 4 from the rest
1. All question are compulsory   20M
a) Describe the File and Directory Management and File Manipulation commands. 5M
b) Explain the concept of disk partitioning in Linux. What are primary, extended, and logical partitions? 5M
c) Explain the Linux booting process from BIOS/UEFI to the login prompt in sequence.5M
d) Describe the process of managing file permissions and ownership in Linux 5M
2.   20M
A system admin needs to analyze a log file and extract specific patterns.
Tasks:
a) Explain the purpose of the grep command. (5)
b) Write commands to:
•   Find lines containing a 3-digit number
•   Find lines starting with ‘A’ or ‘a’ (10)
c) Differentiate between any two distributions based on stability and usability. (5)
3.   20M
An organization has multiple small disks (10GB each) and wants to combine them into a single large storage
pool for flexibility.
Tasks:
•   Explain how LVM can solve this problem. 2M
•   Describe steps to create Physical Volumes, Volume Group, and Logical Volume. 10M
•   Explain advantages of LVM over traditional partitioning. 2M
•   Discuss how storage can be extended dynamically. 2M
• Compare LVM with normal disk partitioning. 2M
4.   20M
A system administrator in a financial organization is responsible for securing sensitive data stored on a Linux
server. Multiple users from different departments need controlled access to files and directories. Some files
must be executable with elevated privileges, shared directories must prevent accidental deletion of others'
files, and fine-grained permissions are required beyond standard user-group access. Additionally, the
administrator must optimize file storage using links.
Based on the above scenario, write a comprehensive note on Linux security addressing the following:
1. SUID, SGID, and Sticky Bit 5M
********** 1 **********
--- page 2 ---
o Define each term
o   Explain their purpose in system security
o Describe how they are configured using commands
o Provide suitable examples for each
2. Access Control Lists (ACLs) 10M
o   Explain the need for ACLs over traditional permissions
o Describe the use of getfacl and setfacl commands
o   Illustrate how ACLs can be used to provide specific permissions to multiple users
3. File Links in Linux 5M
o   Explain hard links and symbolic links
o   Differentiate between them
o Describe their role in file management and security
5.   20M
A company’s internal network is experiencing intermittent slowdowns and suspected unauthorized data
transfers. As a network administrator:
•   Explain how you would use tools like tcpdump and Wireshark to capture and analyze network traffic.
5M
•   Describe the steps to identify suspicious packets or abnormal traffic patterns. 10M
•   Suggest preventive measures to secure the network after identifying the issue.5M
6.   20M
You are managing multiple user accounts on a Linux system.
Scenario:
Write a script that:
•   Takes a username as input using read
• Checks if user exists using /etc/passwd and command substitution
• Uses if-else conditions to display result
• Uses while loop to allow repeated checking until user exits
•   Checks:
o   If home directory exists (-d)
o   If user has execute permission (-x)
• Uses functions for modular design
•   Logs results into a file
Tasks:
1. Write the complete script 10M
2. Explain the working of loops and conditions 5M
3. Describe how input/output is handled 5M
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper f74938ae1c4a

- Departments: Data Science
- Programmes: B TECH / CSEDS-311
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSEDS-311/SEM-IV/LINUX AND SECURE OS FOR BUSINESS/B Tech, Linux and Secure OS for Business, Sem-IV, Batch 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: ocr (2 pages), mean OCR confidence 91.9

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIEN
ENGINEERING (DATA SCIENCE) °
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Linux and Secure OS for Business
Date: 01 Jul 2026 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100 :

RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question number | is compulsory
5. Attempt any 4 from the rest

1. All question are compulsory 20M

a) Describe the File and Directory Management and File Manipulation commands. 5M

b) Explain the concept of disk partitioning in Linux. What are primary, extended, and logical partitions? 5M
c) Explain the Linux booting process from BIOS/UEFI to the login prompt in sequence.5M

d) Describe the process of managing file permissions and ownership in Linux 5M

2: 20M
A system admin needs to analyze a log file and extract specific patterns.
Tasks:
a) Explain the purpose of the grep command. (5)
b) Write commands to:
e Find lines containing a 3-digit number
e Find lines starting with ‘A’ or ‘a’ (10)
c) Differentiate between any two distributions based on stability and usability. (5)

3. 20M
An organization has multiple small disks (10GB each) and wants to combine them into a single-large storage
pool for flexibility.
Tasks:

e Explain how LVM can solve this problem. 2M

e Describe steps to create Physical Volumes, Volume Group, and Logical Volume. 10M

e Explain advantages of LVM over traditional partitioning. 2M

e Discuss how storage can be extended dynamically. 2M

e Compare LVM with normal disk partitioning. 2M
4. . 20M
A system administrator in a financial organization is responsible for securing sensitive data stored ona Linux
server. Multiple users from different departments need controlled access to files and directories. Some files
must be executable with elevated privileges, shared directories must prevent accidental deletion of others'
files, and fine-grained permissions are required beyond standard user-group access. Additionally, the
administrator must optimize file storage using links.
Based on the above scenario, write a comprehensive note on Linux security addressing the following:

1. SUID, SGID, and Sticky Bit 5M

FRR RRR 7 RR
--- page 2 ---
o Define each term

co Explain their purpose in system security

o Describe how they are configured using commands

o Provide suitable examples for each
2. Access Control Lists (ACLs) 10M

co Explain the need for ACLs over traditional permissions

co Describe the use of getfacl and setfacl commands

o ° Illustrate how ACLs can be used to provide specific permissions to multiple users
3. File Links in Linux 5M

o Explain hard links and symbolic links

o Differentiate between them

o Describe their role in file management and security

5. 20M
A company’s internal network is experiencing intermittent slowdowns and suspected unauthorized data
transfers. As a network administrator:
e Explain how you would use tools like tcpdump and Wireshark to capture and analyze network traffic.
5M
e Describe the steps to identify suspicious packets or abnormal traffic patterns. 10M
e Suggest preventive measures to secure the network after identifying the issue.5M

6. 20M
You are managing multiple user accounts on a Linux system.
Scenario:
Write a script that:
e Takes a username as input using read
e Checks if user exists using /etc/passwd and command substitution
e Uses if-else conditions to display result
e Uses while loop to allow repeated checking until user exits
e Checks:
o If home directory exists (-d)
co If user has-execute permission (-x)
e Uses functions for modular design
* Logs results into a file

1. Write the complete script 10M

2. Explain the working of loops and conditions 5M
3. Describe how input/output is handled 5M

FR
````

## 2024-25 · Final-Exam · Sem 4 · paper b24eba7e8abd

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_04/Final-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/QP_Linux and Secure OS for Business(702CO0C052)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2024-2025)
Subject: Linux and Secure OS for Business
Date: 28 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory.
3. Figure in right handout of remaining questions, attempt any 4 questions. side indicates full marks
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1.
CO:1 A. What is the difference between ls -a and ls -l commands?   5 M
SO:1
BL:1
CO:1 B. What are the key components of LVM, and what role does each component   5 M
SO:1   play?
BL:1
CO:1 C. What is the purpose of cron and at commands in job scheduling, and   5 M
SO:1   how do they differ?
BL:1
CO:1 D. What is the difference between the usermod, useradd, and userdel   5 M
SO:1   commands?
BL:2
Q2
CO:1 A. Explain the steps involved in installing a Linux OS and setting up   10 M
SO:1   environment variables.
BL:2
CO:1 B. Describe the steps involved in mounting and unmounting file systems in   10 M
SO:1   Linux. Why is mounting necessary?
BL:2
Q3
CO:1 A. Apply package management commands to install, update, and remove   10 M
SO:1   software on a Linux system.
BL:3
********** 1 **********
--- page 2 ---
CO:1 B. Apply the necessary commands to create a new user, assign the user to a   10 M
SO:1   group, and set a password.
BL:3
Q4
CO:2 A. Encrypt a disk partition using cryptsetup and demonstrate the process   10 M
SO:2   of mounting and accessing it.
BL:3
CO:2 B. Configure a network interface with a static IP address and verify the   10 M
SO:2   connection.
BL:3
Q5
CO:2 A. Analyze a scenario where improper file permissions led to a security   10 M
SO:2   breach. How would you correct and prevent such issues?
BL:4
CO:3 B. Write a BASH script that takes two integers as input, compares them using   10 M
SO:2   conditional expressions, and prints whether the first is greater, smaller, or
BL:3
equal to the second.
Q6
CO:2 A. Describe how Access Control Lists (ACLs) extend traditional file permissions 10 M
SO:2   in Linux. When would you use ACLs?
BL:2
CO:3 B. Create a script to check if a file exists, is readable, and is executable.   10 M
SO:3   Display appropriate messages based on the results.
BL:3
Q7
CO:2 A. Describe how to install and configure the Apache web server in Linux.   10 M
SO:2   What configuration files are involved?
BL:2
CO:3 B. Write a BASH script that automates daily system updates using cron and   10 M
SO:3   logs the results in a file.
BL:3
********** 2 **********
````

## 2023-24 · Final-Exam · Sem 4 · paper 91c4ddd5cf29

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/DATA SCIENCE/SEM IV/LINUX & SECURE OS FOR BUSINESS/Linux and Secure OS for Business, Sem-IV, Final Exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 88.8

````text
~

SVKM’S NMIMS i!
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN!

SCHOOL OF TECHNOLOGY MANAGEMENT a
Academic Year: 2023-2024
Program: B.Tech Computer Science and Engineering Year: IJ Semester: IV

Stream; (Data Science)

Subject: Linux and Secure OS for Business «Time: 3 hrs @o-am to_ 4+ pm _)
Date:_A7_/ 04 / 2024 No. of Pages:_ 3
Marks: 100

Final Examination(2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any _4 _ questions.
> 3)Inall_"_5_ questions to be attempted.
4) All questions carry équal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks,
7) Assume Suitable data if necessary.

Ql
Answer briefly: .
a. Can you walk me through the step-by-step process of installing Linux on a
CO-1; [05]
BL-3 virtual machine?
CO-1: b. What are the steps involved in mounting and unmounting disk devices in a [05]
BL-2 Linux system?
G How do | install, update, and remove packages using the package
CO-1; [05]
BI-2 management system in my Linux distribution?
>
; . d. What command do | use to modify user account properties such as’
CO-1; [05]
BL-3 username, home directory, or login shell?
Q2 a. How can you customize the output of the grep command in Linux to
co-3: display line numbers alongside matching lines, perform case-insensitive [10]
BL-4 searches, and count the number of lines that match a specified pattern?
— CO-3; b. Write a shell script to count the characters, lines and words in a particular [10]
BL-4 file.

oe Fe
ZGWUTE OF fz.

™

uP}

B
<%,
--- page 2 ---
3a. With respect to user management, what are the steps involved its the
following tasks:
Q3 i. Creating a user.
CO-2: BL- ii. Setting User Password. [10]
3 iii. Modifying User Password.
iv. Viewing User Information.
v. Deleting a user.
CO-2; BL- How can disk decryption be performed on Unix-based systems, and what
are the step-by-step procedures involved in decrypting a disk using tools [10]
: like cryptsetup and dm-crypt?
Q4 a. What is the typical directory hierarchy of a Unix file system, and which
CO-2; essential system directories are commonly present in most Unix [10]
BL-2 implementations?
CO-3; b. Write a shell script to convert all the content into upper case ina
BL-4 particular file. ms
- ed What are the SetUID bits in Linux, and how can they be applied or
CO-2; - [10]
BL-3 removed using the chmod command?
b. How can the Apache web server be configured on Unix-based systems,
CO-2; and what are the essential steps involved in the configuration process,
BL-3 including setting up virtual hosts, enabling modules, and ensuring Ho]
security?
Q6 a. Write a shell Script to display the digits in a given 8 digit number.
CO-3; i. Odd Position [10]
BL-4 ii. Even Position
x b. What is “at” job scheduling in Unix systems, and how do we submit a job
7 ove. using "at" when specifying the date variable to the -t flag which format is | [10]

required?
--- page 3 ---
¥

a. With respect to password management, what are the steps involved in
the following tasks:
i. User Creation ;
Q7 ii. Changing Password

CO-2; [10]
, iii. Setting Password Expiry

BL-2
iv. Forcing Password Change on Next Login
v. Locking and Unlocking the Password
b. Write a shell Script to accept a word from the user and display whether
CO-3; —
BL-4. the word starts with a vowel, digit, ends with digit or it is four digit [10]

number.
````

## 2023-24 · Re-Exam · Sem 4 · paper 5aecb067ebcf

- Departments: Data Science
- Programmes: B TECH / CSE DATA SCIENCE, B TECH / CSEDS-311
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/CSE DATA SCIENCE/SEM-IV/LINUX & SECURE OS FOR BUSINESS/Linux and Secure OS for Business, Batch 2023-24, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 88.9

````text
SVKM’S NMIMS : ee
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program: B.Tech Computer Science and Engineering Year: II Semester: IV

Stream; (Data Science) CSEDS

Subject: Linux and Secure OS for Business Time: 3 hrs (toam to_7 py )
Date:_25 / °6/2024 No. of Pages:_“3 _

Marks: 100

ff Ae- Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly:
cO-1: a. Can | install Linux on a virtual machine, and if so, what are the steps
(> 0-1; ; [05]
BL-3 involved?
. b. What is disk partitioning, and how do | create, resize, or delete partitions
CO-1; a {05}
BL-2 ona disk device in Linux?
0-1: Cc. What are the steps involved in utilizing the package management system [05]
“ar : 05
BL-2 of my Linux distribution to install, update, and uninstall software packages?
CO-1: d. How do | create a new user account in Linux, and what are the essential 5]
-1; [0
BL-3 user attributes to consider?
Q2 a

What is the purpose of the grep command in Linux, and how is it used? [10]
CO-3; . oo. sos
BL-4 What is the purpose of the -v and -n option in grep, and how is it used?
--- page 2 ---
Write a menu driven shell script to do the following task: i

i. Display all the files in the current working directory. :
cO-3; ii. Display all the directory files in the current working directory. [10]
BL-4 iii. Display all the running processes in the system.
iv. Display the current year calendar.
Display the current date.
With respect to group management, what are the steps involved in the
following tasks:
Q3 i. Creating a group.
CO-2; BL- ii. Adding a user to a group. [10]
3 iii. Listing users in a group.
iv. Changing group ownership.
v. Deleting a group.
; How can disk encryption be implemented on Unix-based systems, and
c02; Be what are the step-by-step procedures involved in encrypting a disk using | [10]
; tools like dm-crypt and cryptsetup?
Q4 What is Logical Volume Management (LVM) in the context of Linux, and
CO-2; how does it facilitate disk management? Explain it with the help of neat [10]
BL-2 diagram.
CO-3; . " . a
BL-4 Write a shell script to generate Fibonacci series. [10]
me What are the SetGID bits in Linux, and how can they be applied or
na removed using the chmod command? Hol
How can network interfaces be configured on Unix-based systems, and
oe what are the steps involved in both temporary and permanent [10]
configurations?
a6 Write a shell script to exchange the values of two variable with and
a cO-3; without using third variable. ey
BL-4
. :
--- page 3 ---
CO-2; b. What is “cron” job scheduling in Unix systems, and how do we seta,

BL-3 _ ae [10]
crontab entry consisting of six fields?
a. With respect to password management, how can we get the following
details:
Q7 1. Password Policies
CO-2; 2. Fail Log Attempts [10]
BL-2 3. Password Aging Policies
4. Password History
5. How can we secure “passwd” and “shadow” file.
* b. Write a shell script to accept the character from the user and display
ie whether the character is alphabet, digit, special character or user has [10]

entered more than one character.
````
