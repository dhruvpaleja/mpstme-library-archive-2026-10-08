# Application Security Testing: question papers in full

9 unique papers · 2022-23 to 2025-26 · Cyber Security

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 0cb6b7039ed0

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Application Security Testing/QP_Application Security Testing(702IT0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Application Security Testing
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Figure in right hand side indicates full marks.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:
CO-1; SO-1;   a.
Explain Application Security Architecture and its key components.   [05]
BL-2; U1
CO-1; SO-1;   b.
Infer the need for adaptation of SecSDL to Agile Software Development.   [05]
BL-2; U2
CO-3; SO-4;   c.
Explain memory management vulnerability.   [05]
BL-3; U3
CO-2; SO-1;   d.
Explain Agent Smith Attack.   [05]
BL-2; U5
Q2   a.
Working and Significance of MVC Architecture compared with Serverless
CO-1; SO-1;   [10]
Architecture.
BL-1; U1
b. Consider the following HTTP request header template:
POST /order HTTP/1.1
Host: quickbite-website
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: ______
Transfer-Encoding: ______
Q2   i) Craft an HTTP POST request that attempts to poison the back-end server
CO-2; SO-1;   with the string "MALICIOUS" by exploiting a TE.CL vulnerability. Write the   [10]
BL-4; U4   request using explicit \r\n line breaks.
ii) Analyze how the front-end proxy and back-end server interpret the
request differently in a TE.CL vulnerability. Explain how the string
"MALICIOUS" can affect subsequent requests.
iii) Briefly explain the following request smuggling vulnerabilities in one line
each: CL.TE, TE.CL , TE.TE
iv) Construct an HTTP POST request that introduces a processing delay using
the string "MALICIOUS", exploiting a CL.TE vulnerability. Use explicit \r\n
line breaks.
********** 1 **********
--- page 2 ---
v) Craft an HTTP POST request containing the string "MALICIOUS" exploiting
a TE.TE vulnerability, where the front-end processes Transfer-Encoding
and the back-end relies on Content-Length. Use explicit \r\n line breaks.
Q3   a.
Comment on Dynamic Detection techniques and relate to how and which
CO-2; SO-1;   [10]
vulnerability it helps in detecting.
BL-3; U3
b. A web application SecureLogin.com provides a login feature where users   [10]
enter their username and password. The server constructs the following SQL
query:
SELECT * FROM users WHERE username = 'input1' AND
password = 'input2';
The application does not display database errors or query results, but the
attacker can observe differences in response time or login success/failure
messages.
i) Identify the type of SQL Injection attack that can be performed in this
Q3
scenario. Explain how it works. Compare it with: In-band SQL Injection and
CO-3; SO-4;
Out-of-band SQL Injection
BL-4; U4
ii) Write a malicious payload that allows an attacker to test true/false
conditions using Blind SQL Injection.
iii) How can an attacker determine whether the application is vulnerable to
Blind SQL Injection, based on response behavior?
iv) What conditions must exist in the application for this vulnerability to be
successfully exploited?
v) Suggest appropriate defensive coding practices, input validation
methods, and database security mechanisms to prevent such SQL
Injection attacks.
Q4   a.   [10]
CO-1; SO-1;   Explain the Secure Software Lifecycle process of Touchpoints.
BL-2; U2
Q4   b.   [10]
CO-2; SO-1;   Explain Bluesnarfing and Bluebugging with example.
BL-1; U5
Q5   a.   [10]
CO-2; SO-1;   Explain Side-channel vulnerabilities.
BL-2; U3
b. An attacker wants to increase the popularity of a post on a social media   [10]
platform called ShareZone by tricking users into clicking the “Like” or
“Follow” button without their knowledge.
Questions:
i.   Explain how a clickjacking attack can be used to artificially increase
Q5   likes or followers on a social media platform.
CO-3; SO-1;   ii.   Design a malicious web page that hides the “Like” or “Follow” button
BL-4; U5   of ShareZone using an iframe. Explain the important parts of the
code used in the attack.
iii. Why does allowing the social media page to be embedded within
another website make this attack feasible?
iv.   Analyze the potential impact of such attacks on user trust, platform
integrity, and content credibility.
********** 2 **********
--- page 3 ---
v.   Suggest suitable security headers, browser protections, and UI
design practices that ShareZone should implement to prevent
clickjacking attacks.
Q6   a.   [10]
Compare between SAST, RASP and DAST application security tools and
CO-1; SO-1;
solutions.
BL-1; U1
b. A web application DocPreviewer.com allows users to preview documents by   [10]
providing a URL. The server fetches the document from the given URL and
displays a preview:
POST /previewDocument HTTP/1.1
Host: docpreviewer.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 85
docUrl=http://files.docpreviewer.com/docs/sample.pdf
An attacker suspects that the server can be tricked into accessing internal
Q6
network resources.
CO-2; SO-1;
i) Identify the type of attack that can be performed to access an internal
BL-4; U4
resource such as http://localhost:8080/admin. Explain how the attack
works.
ii) Rewrite the HTTP request to craft a malicious request that forces the
server to access the internal resource.
iii) What sensitive information or advantages could the attacker gain by
successfully exploiting this vulnerability?
iv) What defensive mechanisms and validation techniques should the
application implement to prevent such attacks?
v) Explain the different types or variations of this attack (e.g., basic SSRF,
blind SSRF, etc.).
Q7   a.   [10]
CO-2; SO-1;   Explain one of the Framework to assess the secure software lifecycle.
BL-1; U2
b. A travel booking platform TripNest.com allows users to leave feedback   [10]
about hotels. The feedback message is displayed dynamically using a server-
side template engine.
Example template rendering code:
Welcome {{ user_name }}! Your feedback has been recorded:
{{ feedback_message }}
The application directly inserts user-supplied input into the template before
Q7   rendering it.
CO-3; SO-4;   i)   Identify the type of vulnerability that can arise from this
BL-4; U4   implementation. Explain how an attacker can exploit it.
ii) Write a malicious template payload that can be injected into the
feedback_message field to test whether the server evaluates template
expressions.
iii) If the attack is successful, what kind of information disclosure or system-
level access could the attacker achieve?
iv) What conditions or misconfigurations must exist in the application for
this attack to be possible?
********** 3 **********
--- page 4 ---
v) Recommend appropriate secure coding practices, input handling
techniques, and template engine configurations that should be
implemented to prevent such vulnerabilities.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 4454cc6b7278

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CyberSecurity_7010/Application Security Testing/QP_Application Security Testing(702IT0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Application Security Testing
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Figure in right hand side indicates full marks.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:
CO-1; SO-1;   a.   Infer the need for securing information and comment on Information Security
[05]
BL-2; U1   Attack Vectors (ANY TWO).
CO-1; SO-1;   b.
Infer the need for adaptation of SecSDL to Internet of Things (IoT).   [05]
BL-2; U2
CO-3; SO-4;   c.
Jot down the reasons for API Vulnerability.   [05]
BL-3; U3
CO-2; SO-1;   d.
Infer BYOD Benefits.   [05]
BL-2; U5
Q2   a.
Working and Significance of Serverless Architecture compared with Single-
CO-1; SO-1;   [10]
page Architecture.
BL-1; U1
b. Consider the following HTTP request header template:
POST /transfer HTTP/1.1
Host: securebank.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: ______
Transfer-Encoding: ______
i) Craft an HTTP POST request that poisons the back-end server with the
Q2
string "POISON" by exploiting a TE.CL vulnerability. Write the request
CO-2; SO-1;   [10]
using explicit \r\n line breaks.
BL-4; U4
ii) Compare the request smuggling variants CL.TE, TE.CL, and TE.TE,
highlighting how each attack works and how the mismatch between
Content-Length and Transfer-Encoding enables request smuggling.
iii) Craft an HTTP POST request that introduces a time delay on the back-end
server while sending the string "POISON", exploiting a CL.TE vulnerability.
Write the request using explicit \r\n line breaks.
iv) Craft an HTTP POST request containing the string "POISON" that exploits
a TE.TE vulnerability. Use explicit \r\n line breaks.
********** 1 **********
--- page 2 ---
v) Analyze the TE.TE attack, explaining how the front-end and back-end
servers interpret the request differently and how the string POISON is
injected into the back-end request queue.
Q3   a.
How would sandboxing help in mitigating race condition vulnerability and
CO-2; SO-1;   [10]
memory management vulnerability?
BL-3; U3
b. A web application displays user profile information based on a user ID   [10]
entered in the URL:
http://example.com/profile?id=10
The server executes the following query:
SELECT name, email FROM users WHERE id = 'id';
The application directly displays the query results on the webpage.
Q3   i) Identify the type of SQL injection attack and explain how it works.
CO-3; SO-4;   Compare it with Blind SQL injection and Out-of-band SQL injection.
BL-4; U4   ii) Write a malicious input that exploits the vulnerability to retrieve
username, password from login using a UNION-based SQL injection.
iii) How can the attacker determine whether the application is vulnerable to
In-band SQL injection?
iv) What conditions must exist in the application for this attack to succeed?
v) What defensive techniques should developers implement to prevent this
attack?
Q4   a.   [10]
Explain the SDL practices incorporated by Microsoft to improve the security
CO-1; SO-1;
of their products.
BL-2; U2
Q4   b.   [10]
CO-2; SO-1;   Describe Mobile Attack Vectors/Vulnerabilities.
BL-1; U5
Q5   a.   [10]
Comment on Dynamic Detection techniques and relate to how and which
CO-2; SO-1;
vulnerability it helps in detecting.
BL-2; U3
b. An attacker wants to trick users into unknowingly clicking the “Confirm   [10]
Transfer” button on an OnlineBank website using clickjacking.
i) Explain the process of clickjacking in this banking scenario.
ii) Design the attacker’s malicious web page that hides the “Confirm
Q5   Transfer” button. Explain the significant code.
CO-3; SO-1;   iii) Why does the browser allow the banking page to be embedded inside
BL-4; U5   another page?
iv) What financial risks and security implications could result from this
attack?
v) What defensive techniques should the OnlineBank server implement to
prevent such attacks?
Q6   a.   [10]
Compare between SAST, DAST and IAST application security tools and
CO-1; SO-1;
solutions.
BL-1; U1
********** 2 **********
--- page 3 ---
b. A user is logged into an e-commerce website ShopEasy. The website allows   [10]
users to change their delivery address using the following request:
GET http://shopeasy.com/changeAddress?addr=NewAddress
HTTP/1.1
An attacker wants to change the victim’s delivery address to their own
Q6
location.
CO-2; SO-1;
i) Identify the attack type and explain how the attacker exploits the
BL-4; U4
vulnerability.
ii) What steps could the attacker take to deliver the malicious request to
the victim?
iii) What conditions must be present for the attack to successfully execute?
iv) What security practices should users follow to avoid such attacks?
v) What server-side protections should ShopEasy implement to defend
against CSRF?
Q7   a.   [10]
CO-2; SO-1;   Describe the BSIMM Framework for assessing the Secure Software Lifecycle.
BL-1; U2
b. An e-commerce website ShopReview.com allows users to submit product   [10]
reviews. The review text is dynamically rendered on the webpage using a
template engine.
Example template rendering code:
Hello {{ username }}, thank you for reviewing this product!
The application directly inserts user input into the template before
Q7   rendering the page.
CO-3; SO-4;   i) Identify the type of attack that an attacker can exploit by injecting
BL-4; U4   malicious template expressions. Explain the attack.
ii) Write a malicious input payload that could be injected into the template
to test whether the server processes template expressions.
iii) What information or capabilities could the attacker gain if the attack is
successful?
iv) What conditions must exist in the application for this attack to be
successful?
v) What secure coding practices and defensive mechanisms should
developers implement to prevent this vulnerability?
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper e0fd340d8c10

- Departments: Cyber Security
- Programmes: B TECH / CSE CYBER SECURITY
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSE CYBER SECURITY/SEM-VI/APPLICATION SECURITY TESTING/B Tech, Applications Security Testing, Sem-VI, Batch 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: ocr (3 pages), mean OCR confidence 87.1

````text
SVKMs NMIMS ~
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Application Security Testing

Date: 03 Jul 2026 Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100

RE EXAMINATION (Acad. Year:2025-2026)
Instructions:

I. This question paper contains 3 pages.

2. Question No.1 is compulsory.

3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.

5. Figure in right hand side indicates full marks.

6. All questions carry equal marks.

7. Assume Suitable data if necessary.

MPSTME
us LIBRARY

wh,

Or LS

xy 42
MIMS UNIVERSES.

¢ Qi Answer briefly:
CO-1;SO-1; a. Infer the need for securing information and comment on Information Security [05]
BL-2; U1 Attack Vectors (ANY TWO). ,
CO-1;SO-1; b. : - ;
BL-2: U2 Infer the need for adaptation of SecSDL to Internet of Things (loT). [05]
CO-3; SO-4;   c. a -
BL-3: U3 Jot down the reasons for API Vulnerability. {05]
CO-2;SO-1;   d. , ;
BL-2: US Infer BYOD Benefits. [05]
Q2 a. . wip : . :
CO-1: 0-1: Working and Significance of Serverless Architecture compared with Single- [10]
BL-1: U1 , page Architecture.

b. Consider the following HTTP request header template:
| POST /transfer HTTP/1.1
Host: securebank.com
d Connection: keep-alive

Content-Type: application/x-www-form-urlencoded
_| Content-Length:

Q2 i) Craft an HTTP POST request that poisons the back-end server with the
CO-2; $0-1; string "POISON" by exploiting a TE.CL vulnerability. Write the request [10]
BL-4: U4 using explicit \r\n line breaks.
ii) Compare the request smuggling variants CL.TE, TE.CL, and TE.TE,
Tl Ps highlighting how each attack works and how the mismatch between
- Content-Length and Transfer-Encoding enables request smuggling.

iii) Craft an HTTP POST request that introduces a time delay on the back-end
server while sending the string "POISON", exploiting a CL.TE vulnerability.
Write the request using explicit \r\n line breaks.
iv) Craft an HTTP POST request containing the string "POISON" that exploits
- * - a TE.TE vulnerability. Use explicit \r\n line breaks.

FOR ORR RE

nin
--- page 2 ---
v) Analyze the TE.TE attack, explaining how the front-end and back-end

servers interpret the request differently and how the string POISON is
injected into the back-end request queue.

oe. SOx1; a How would sandboxing help in mitigating race condition Vulnerability and [10]
BL-3; U3 memory management vulnerability?
b. A web application displays user profile information based on a user ID {10]
entered in the URL: :
| http://example.com/profile?id=10 |
The server executes the following query:
| SELECT name, email FROM users WHERE id = ‘id'; |
The application directly displays the query results on the webpage.
Q3 i) Identify the type of SQL injection attack and explain how it works.
CO-3; SO-4; Compare it with Blind SQL injection and Out-of-band SQL injection.
BL-4; U4 ii) Write a malicious input that exploits the vulnerability to retrieve
username, password from login using a UNION-based SQL injection.
iii) How can the attacker determine whether the application is vulnerable to a
In-band SQL injection? )
iv) What conditions must exist in the application for this attack to succeed?
v) What defensive techniques should developers implement to prevent this
a attack?
a4 a. ; oo. ; ; [10]
CO-1; $0-1; Explain the SDL practices incorporated by Microsoft to improve the security
BL-2: U2 of their products.
Q4 b. [10]
CO-2; SO-1; Describe Mobile Attack Vectors/Vulnerabilities.
BL-1; US
Qs . . . . {10]
CO-2; 50-1; COMIEHE an Dynansie Detection techniques and relate to how and which
BL-2: U3 vulnerability it helps in detecting.
b. An attacker wants to trick users into unknowingly clicking the “Confirm {10]
Transfer” button on an OnlineBank website using clickjacking.
i) Explain the process of clickjacking in this banking scenario.
ii) Design the attacker’s malicious web page that hides the “Confirm
Qs ” Transfer” button. Explain the significant code.
CO-3; SO-1; _lii) Why does the browser allow the banking page to be embedded inside
BL-4; US ; another page?
iv) What financial risks and security implications could result from this
; attack?
-_ v) What defensive techniques should the OnlineBank server implement to
ee e prevent such attacks? ee
se
: an 50-1; ° Compare between SAST, DAST and IAST application security tools and [10]
BL-1: U1 solutions.

’

FORK DORR RK KEE
--- page 3 ---
>)

A user is logged into an e-commerce website ShopEasy. The welfsite allows
users to change their delivery address using the following request:.

GET http://shopeasy.com/changeAddress ?addr=NewAddress
HTTP/1.1

An attacker wants to change the victim’s delivery address to their own

[10]

Q6 -
CO-2; SO-1; location.
BL-4; U4 i) Identify the attack type and explain how the attacker exploits the
vulnerability.
ii) What steps could the attacker take to deliver the malicious request to
the victim?
iii) What conditions must be present for the attack to successfully execute?
iv) What security practices should users follow to avoid such attacks?
v) What server-side protections should ShopEasy implement to defend
against CSRF?
Q7 ; ; [10]
CO-2; SO-1; Describe the BSIMM Framework for assessing the Secure Software Lifecycle.
BL-1; U2 .
An e-commerce website ShopReview.com allows users to submit product {10]
reviews. The review text is dynamically rendered on the webpage using a
template engine.
Example template rendering code:
| Hello {{ username }}, thank you for reviewing this product!
The application directly inserts user input into the template before
Q7 rendering the page.
CO-3; SO-4; i) Identify the type of attack that an attacker can exploit by injecting
BL-4; U4 malicious template expressions. Explain the attack. .

ii) Write a malicious input payload that could be injected into the template
to test whether the server processes template expressions.
iii) What information or capabilities could the attacker gain if the attack is
_ successful?
iv) What conditions must exist in the application for this attack to be
successful?
v) What secure coding practices and defensive mechanisms should

developers implement to prevent this vulnerability?

FORE 2 OR RR
````

## 2024-25 · Final-Exam · Sem 6 · paper 02c8df301b0b

- Departments: Cyber Security
- Programmes: B TECH / CYBER SECURITY
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CYBER SECURITY/SEM VI/APPLICATION SECURITY TESTING/Application Security Testing, Sem-VI, Year 2024-25, Final Exam.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 86.0

````text
SVKM’'S NMIMS
» MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGINEERING
Academic Year: 2024-2025

Program: BTech (CSE) Stream: CyberSecurity Year: 2024-35 Semesier:
Subject: Application Security Testing Time: 3:hrs (2:to Spm
Date:.4 (Apel / 2025 No. of Pages: 03 |
Marks: 100

Final Examination.(24-25)
Instructions: Candidates should read carefully the instructions printed on. the question
paper and.on the.cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 —_ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started-on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

vl

Qi Answer briefly:
CO-1;,SO-1; | a. | How is motive, goal and objective related to Information Security Attacks [05]
BL-2; U4 and comment on any TWO Information Security Attack Vectors.
CO-1; SO-1; | b..| Describe the SAMM Framework for assessing the Secure. Software 105]
BL-2; U2 Lifecycle.
Soe ® | Jot down the reasons for AP! Vulnerability, [05]
CO-2; SO-1; | d. .
BL-2: US Infer BYOD Benefits. [05]
Q2 . . a Working and Significance of MVC. Architecture compared with Single-
CO-1; SO-1; , {10}
BL-4: Ut page Architecture,
b. | A web application executes the following query when retrieving user

details:

SELECT * FROM users WHERE username="'username’;
OF. $0-4: The attacker cannot see query results but can infer delays in execution: 10]
BL-4 U4 : A web application contains-a login page where users enter their

username and password. The seiver-sidé query executes:

SELECT * FROM users WHERE username='username' AND
Password="password';

1|Page
--- page 2 ---
The attacker cannot'see direct SQL errors or outputs but can infer

database responses based on application behaviour.

i) Identify the type of SQL injection attack and explain the attack
comparing to other types of SQL query injection attacks.

ii) Write the. modified query after the attacker inputs the payload the
username field with a time delay of 5 seconds.

iit) How does the attacker determine if the application is vulnerable?

iv) What are the requirements for this attack to be successful?

v) How can this attack be prevented?

Co: 0-1 4. | Comment on:static detection techniques and relate to how and which 110]
BL-3: U3 ' vulnerability they help detect.
b. | A financial web application allows users to fetch stock market data from [10]
external APIs. The API request is sent from the:client’s browser to. the
server, which fetches data from the provided URL.
POST /finance/marketData HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 90
Q3 stockApi=http://data.marketfinance.com:8080/inance/marketData
CO-3; SO-4; /checkcurrentDateTime
BL-4; U4
i) Identify which type of attack can be crafted by the attacker to
check the contents of /etc/passwd on the server side. Explain the
attack:
ii) Rewrite the HTTP request to create an attack request.
iii) What insight the attacker gains through the attack?
iv) Ways to mitigate this attack.
v) Explain types of the identified attack.
a4 a. [10]
CO-1; SO-1; Explain the Objéctive and Applicability of NIST.
BL:2; U2
b. | An attacker wants to'trick users.into accidentally “Like” a post on [10]
SocialHub by exploiting-a clickjacking vulnerability. The attacker
creates a malicious page which contains the ability to click the “Like”
Q4 button from SocialHub.
CO-2; SO-1; i) What would be the Attacker's Page Design (Malicious). Explain only
BL-1; U5 the significant code.
ii) What should be the design of web page on the server side
(defensive page design of SocialHub). Explain only the significant
code.
Qs a. | How would runtime detection help in mitigating structured output [10]

generation vulnerabilities?

2|Page
--- page 3 ---
CO-2; SO-1;

BL-2; U3

Q5 b, [10]
CO-3; SO-1; Describe SS7 Vulnerability and Smishing.

BL-1; U5

Cot: $0-1: a. Compare between DAST, IAST and SAST application security tools [10]

BL-4: Ut and solutions:

b. | Consider the HTTP Request Headers: ; [10]

POST? HTTP/1.1
Host: vulnerable-website
Gonnection:.keep-alive

Q6 Content-Type: applicatian/x-www-form-urlencoded
CO-2; SO-1; Content-Length:
BL-1; U4. Transfer-Encoding:

i) Craft a HTTP post request.which poisoris the back-end server with
the string “SMUGGLED” exploiting CL.TE vulnerability.

if) Write your analysis.

iii) Compare between CL.TE, TE.CL and TE.TE.

Q7 a. [10]
CO-1; SO-1; Explain the Objective and Applicability of NIST.
BL-1; U2

b. | A user is logged into their email service. provider (e.g., [10]

MaiiSecure.com) and is composing an important email. The-email
service allows users to update their password through a simple web
form. The password change request is processed using the following

URL:

GET
Q7 Attp://mailsecure.com/updatePassword.do ?newpassword=Attacke
CO-3; SO-4; £123 HTTP/1.1

BL-4; U4
An attacker wants to change the victim’s password to “Attacker123”,
thereby locking the victim ‘out of their own email account.
i) Identify the attack-and explain the attack.
ii) What. steps did the attacker incorporate to devise this attack?
iii) What are the requirements for this attack io be successful?
iv) What knowledge should a victim have to avoid such an attack?
v) How can the bank prevent this attack?

3] Page
--- page 4 ---

````

## 2023-24 · Re-Exam · Sem 6 · paper 6af22684337f

- Departments: Cyber Security
- Programmes: B TECH / CSE CYBER SECURITY
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSE CYBER SECURITY/SEM-VI/APPLICATION SECURITY TESTING/Application Security Testing, Sem-VI, A Y 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 87.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT.

Academic Year: 2023-2024

Program: BTech (CSE) Stream: CyberSecurity Year: 202 24 Semester: VI
Subject: Application Security Testing Time: 3 hrs (2 to 5pm )
Date: 28/ Fame! 2024 No. of Pages: 02

Marks: 100 °

ReExamination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. _1___- is compulsory.

2) Out of remaining questions, attempt any _4__ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly:
CO-1; SO-1; a. | Infer the need for securing information and comment on any TWO Information [05]
BL-2; U1 | Security Attack Vectors.
CO-1;S0-1; | b. ;
BL-2: U2 Describe the BSIMM Framework for assessing the Secure Software Lifecycle. [05]
senus “ | Comment on the reasons for Race Condition Vulnerability. [05]
CO-2; SO-1; d. .
BL-2: US Infer BYOD Risks. [05]
Q2 a. . ae . ' 7
C0-1:S0-1: Working and Significance of MVC Architecture compared with Single-page (10)
BL-4; U1 Architecture.
Q2 b. . F aa .
Specify the three types of XSS attacks and specify the distinct steps of their

CO-2; SO-1; working? [10]
BL-1; U4 8

1|Page
--- page 2 ---
i

Q3 a.
CO-2; SO-1;
BL-3; U3

Comment on Static Detection techniques and relate to how ang which

10
vulnerability it helps in detecting. [10]

Q3 b. [10]
CO-3; SO-4; Difference between CSRF and SSRF attacks wrt their working.
BL-4; U4 "

Q4 a. [10]
CO-1; SO-1; Infer the need for adaptation of SecSDL to Payment Card Industry (PCI).
BL-2; U2

Q4 b. [10]
CO-2; SO-1; Explain Smishing and its reasons of being effective. What is Mobile Spam?
BL-1; U5

Qs a. . . a [10]
CO-2; $0-1; How would runtime detection help in mitigating structured output

BL-2: U3 generation vulnerabilities.

Q5 b. [10]
CO-3; SO-1; Describe general guidelines for Mobile Platform Security.
BL-1; U5

6 ; 0
oo. 50-1: a Compare between WAF, RASP, CNAPP application security tools and [10]

BL-4; U1 solutions.

Q6 b. [10]
CO-2; SO-1; Explain FIVE types of SQLi Injection.
BL-1; U4

7 3
a 50-1: a Explain the SDL practices incorporated by Microsoft to improve the security [Ae]

BL-1; U2 of their products.

7 ‘ 1
no: 50-4: Differentiate Bluesnarfing and Bluebugging and describe advantages of Multi- [10]

BL-4; U4 factor Authentication.

2|Page
````

## 2022-23 · Final-Exam · Sem 6 · paper b6a32199cb17

- Departments: Cyber Security
- Programmes: B TECH / CSE CYBER SECURITY
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSE CYBER SECURITY/SEM-VI/APPLICATION SECURITY TESTING/Application Security Testing, Sem-VI, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 / April / 2023
- Text: ocr (2 pages), mean OCR confidence 84.5

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN

Academic Year: 2022-2023

Program: BTech (CSE) Stream: CyberSecurity Year: 2039.58 heneater Ml
Subject: APPLICATION CecuRiTY TESTINGT Time: 3 hrs (2 to Spm )
Date: 24 / April / 2023 No. of Pages: 02

Marks: 100

Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. 1 _ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly:

CO-1; SO-1; a. | Infer the need for securing information and comment on any TWO Information [05]

BL-2; U1 Security Attack Vectors.

CO-1; SO-1; b. . . .

BL-2: U2 Describe the SAMM Framework for assessing the Secure Software Lifecycle. [05]

CO-3; SO-4; . a -_

BL-3: U3 c Comment on the reasons for Race Condition Vulnerability. [05]

CO-2; SO-1; d. | Infer and describe the technique for stealing information from mobile device [05]

BL-2; U5 via Bluetooth.

Q2 a. : 4 naif . . .

C0-1: $0-1: Working and Significance of Serverless Architecture compared with Single- [10]

BL-4: U page Architecture.

Q2 b. . . _ A
Specify the three types of XSS attacks and specify the distinct steps of their

CO-2; SO-1; working? {10}

BL-1; U4 Se

1|Page
--- page 2 ---
Q3 a.

CO-2: 50-1; aint and relate to how and which [10]
BL-3; U3 ve nee 8:
Q3 b. {10]
CO-3; SO-4; Difference between CSRF and SSRF attacks wrt their working.
BL-4; U4
Q4 a. [10]
CO-1; SO-1; Infer the need for adaptation of SecSDL to mobile environment.
BL-2; U2
Q4 b. [10]
CO-2; SO-i; Explain Simjacker and Agent Smith Attack and its working.
BL-1; US
: . 10
oo. 50-1: a How would runtime detection help in mitigating structured output {10]
| BL-2; U3 generation vulnerabilities.
Qs b. [10]
CO-3; SO-1; Describe general guidelines for Mobile Platform Security.
BL-1; U5
a6 a. _ . [10]
CO-1: $0-1: Compare between SAST, DAST and IAST application security tools and
BL-4: U1 solutions.
Qé6 b. [10]
CO-2; SO-1; Explain the FIVE defenses wrt preventing SQLi Vulnerabilities.
BL-1; U4
Q7 a. ; i. . : , [10]
CO-2: S0-1: Explain the SDL practices incorporated by Microsoft to improve the security
BL-1: U2 of their products.
Q7 b. [10]
CO-3; SO-4; Differentiate OAuth with SAML and describe the working of OAuth.
BL-4; U4
2[Page
````

## 2022-23 · Re-Exam · Sem 6 · paper 021d83f37368

- Departments: Cyber Security
- Programmes: B TECH / CSE CYBER SECURITY
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSE CYBER SECURITY/SEM-VI/APPLICATION SECURITY TESTING/Application Security Testing, Sem-VI, Year 2022-23, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 87.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& E
Academic Year: 2022-2023

Program: BTech (CSE) . Stream: CyberSecurity Year: Tir a! | Semester: VI
Subject: Appitcetsoy, . 5 Time: 3 hrs (2 to 5pm )
ee waeechey Testa 8

Date: 2% /June/ 2023 No. of Pages: 02

Marks: 100

“Re- Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:
CO-1; SO-1; . . . . . .
3 How is motive, goal and objective related to Information Security Attacks and [05]

BL-2; U1 comment on any TWO Information Security Attack Vectors.
CO-2; SO-1; | b.
BL-1: U2 Describe the BSIMM Framework for assessing the Secure Software Lifecycle. [05]
CO-3; SO-4; | c.
BL-2: U3 Jot down the reasons for Memory Management Vulnerability. . [05]
CO-2; SO-1; | d.

~ BL-2: US Infer and describe the technique for taking over a mobile device via Bluetooth. | [05]
Q2 a.
CO-1; SO-1; Working and Significance of MVC Architecture compared with Micro Services [10]
BL-3; U1 Architecture.
Q2 b.
CO-2; SO-1; Specify three attack techniques of HTTP Request Smuggling with example. [10]
BL-2; U4

1|Page
--- page 2 ---
;

ae a Comment on Dynamic Detection techniques and relate to how and which

-2; SO-1; 10
satus 1; vulnerability it helps in detecting. [10]
Q3 bo}. re . a k [10]
CO-3: 0-4: Difference between Server Side Injection and Cross Site Scripting attacks wrt
BL-4: U4 , their working.

Q4 a. [10]
CO-1; SO-1; Infer the need for adaptation of SecSDL to cloud environment.
BL-2; U2 :
Q4 b. [10]
CO-2; SO-1; Explain any FIVE OWASP Mobile Top10 Testing with an example for each.
BL-1; U5
Qs a. [10]
CO-2; SO-1; How would sandboxing help in mitigating race condition vulnerability and
BL-2: U3 memory management vulnerability.
Q5 b. [10]
CO-3; SO-4; Describe Mobile Attack Vectors/Vulnerabilities.
BL-1; US
Qé6 a. [10]
CO-1; SO-1; Compare between WAF, RASP and CNAPP application security tools and
BL-4: U1 solutions.
Qé6 b. {10]
CO-2; SO-1; Explain FIVE types of SQLi vulnerabilities with example.
BL-2; U4
Q7 a. [10]
CO-2; SO-1; Explain the SDL practices outlined by SAFECode to increase trust in information
BL-2: U2 and communication technology.
Q7 b. [10]
CO-3; SO-4; Comment on ways to mitigate Broken Authentication Vulnerability and
differentiate between Single-factor and Multi-factor Authentication.
BL-4; U4
2|Page
````
