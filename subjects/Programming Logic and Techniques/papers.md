# Programming Logic and Techniques: question papers in full

5 unique papers · 2025-26 to 2025-26 · B.Sc Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 1 · paper a68f66f608bf

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Programming Logic And Techniques/QP_Final-Exam_Programming Logic And Techniques(NHPLT101)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 13 Oct 2025
- Text: text (4 pages)

````text
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Programming Logic and Techniques/Programming Logic And Techniques
Date: 13 Oct 2025   Time: 11:30 am - 01:30 pm (02:00 Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This question paper contains 4 pages
2. Each question carries equal marks
3. Answer to each new question to be started on a fresh page
4. Draw neat and clear diagrams wherever required
5. Students may add pseudocode or code snippet to the answer where relevant
6. For any psuedocode-based question, ensure to describe clearly
7. Figure on the right-hand side indicates full marks
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. 1.   Define a programming language. Explain with one example why it is needed for   5
communication with a computer
b. 1.   Describe the importance of programming languages in automating tasks and reducing   5
manual effort. Support your answer with an example of a task that was done manually in the
past but is now automated by computers
c. 1.   Analyze and explain the concept of modularity in object-oriented programming with its   5
components, Give an example scenario where classes can be used
d. 1. A teacher needs to grade 200 multiple-choice answer sheets. The grading can be done   5
either by following a strict step-by-step marking scheme or by quickly estimating scores based
on patterns noticed in the answers. Examine this scenario and identify whether an algorithmic
or heuristic approach would be more effective. Justify your choice
Page 1 of 4
--- page 2 ---
e. 1.   Netflix manages a huge content library, including Movies, TV Shows, and   5
Documentaries, with millions of users tracking their viewing habits. To maintain an efficient
pltatform, Netflix needs a well-structured system to manage its content and track user
interactions. Your task is to design a hierarchical decomposition tree for the Netflix Content &
Recommendation Management System.
The system should include the following aspects:
·   Organize the library into 3 main content types i.e. Movies, TV Shows, and
Documentaries, each containing thousands of titles
·   For TV Shows, manage multiple seasons and episodes for each title (e.g., a show with 1
seasons, each having 2 episodes)
·   For each movie, there will be a genre
·   Track ratings for each record in the watchlist history for each user
·   Use ratings to suggest content tailored to each user’s preferences
Identify the root node, child nodes, leaf nodes, and specify the level of the tree
f. A lab records experiment counts that grow roughly but they’re unaware of the exact pattern   5
followed in increase. The experiments recorded for the past 6 days are 2, 3, 8, 27, 124. Identify
the rule and predict the number of lab experiment count for the next 3 days respectively
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. 1.   Describe why an algorithm is considered independent of any programming language   5
b. 1.   Explain how AND, OR, and NOT operators are used in logic programming to make   5
decisions. Give an example
c. 1.   Consider the following algorithm:   5
Step 1: Input current temperature, desired temperature, room occupancy
Step 2: If current < desired AND room occupied, turn heater ON
Step 3: Else if current > desired OR room unoccupied, turn AC ON
Step 4: Else maintain current state
Step 5: Print device status
Examine if this algorithm maintains room temperature correctly in all cases. Identify the issues
and rewrite the correct algorithm
d. 1.   Explain what problem this algorithm is designed to solve   5
Input: n_days
Page 2 of 4
--- page 3 ---
Output: total_travel_hours
BEGIN
total_travel_hours ← 0
FOR i ← 1 TO n_days DO
Input travel_start_time[i], travel_end_time[i]
daily_hours[i] ← travel_end_time[i] - travel_start_time[i]
total_travel_hours ← total_travel_hours + daily_hours[i]
ENDFOR
DISPLAY total_travel_hours
END
e. Develop a flowchart that find all divisors of a number given by user   5
f. 1. A mobile health app wants to alert users if they meet their daily activity goal: at least   5
10,000 steps and 30 minutes of exercise. The app should notify the user only if both conditions
are satisfied. Develop an algorithm to check whether the user has completed 10,000 steps,
check whether the user has completed 30 minutes of activity, and trigger the alert only if both
conditions are true
Q3. Answer the following questions(Attempt Any 4 Questions)   20
a. Define a variable and explain what an assignment statement does. Give an example.   5
b. The pseudocode below is written to calculate Simple Interest, but there are mistakes. Find   5
mistakes stating reasons and rewrite the correct pseudocode.
DISPLAY "Enter Principal, Rate, Time:"
INPUT P, R, T
// Calculate simple interest
SET SI = P * R * T / 1000
DISPLAY "Simple Interest is:" + P
SET TotalAmount = P - SI
DISPLAY "Total Amount (Principal + Interest) is:" + TotalAmount
c. Two pseudocode versions sum even numbers ≤ N. Which approach is more efficient and why?   5
Page 3 of 4
--- page 4 ---
Variant A (Check inside loop):
DISPLAY "Enter N:"
INPUT N
SET sum = 0
FOR i = 1 TO N
IF i % 2 = 0 THEN
SET sum = sum + i
END IF
END FOR
DISPLAY "Sum of even numbers is:"+ sum
Variant B (Increment by 2):
DISPLAY "Enter N:"
INPUT N
SET sum = 0
SET i = 2
WHILE i <= N
SET sum = sum + i
SET i = i + 2
END WHILE
DISPLAY "Sum of even numbers is:" + sum
d. Perform dry run and present the execution in the tabulated form for the following pseudocode.   5
SET sum = 0
FOR i = -2 TO 5
IF i > 0 AND i MOD 2 <> 0 THEN
SET sum = sum + i
ENDIF
DISPLAY “i = “ + i + “Sum = “ + sum
ENDFOR
e. Create a module FindMin that finds the smallest of three numbers. Call the module in the main   5
pseudocode and display the result.
f. Design a pseudocode that prints numbers from 1 to 15 that are divisible by 3 OR greater than   5
12 AND are even.
Page 4 of 4
````

## 2025-26 · Re-Exam · Sem 1 · paper b61c248712f1

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Programming Logic And Techniques/QP_Re-Exam_Programming Logic And Techniques(NHPLT101)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 19 Jan 2026
- Text: text (5 pages)

````text
SVKM
Narsee Monjee College of Com. & Eco.
Programme: B.Sc. (IT)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Programming Logic and Techniques/Programming Logic And Techniques
Date: 19 Jan 2026   Time: 11:00 am - 01:00 pm (02:00 Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This question paper contains 5 pages
2. Each question carries equal marks
3. Answer to each new question to be started on a fresh page
4. Draw neat and clear diagrams wherever required
5. Students may add pseudocode or code snippet to the answer where relevant
6. For any psuedocode-based question, ensure to describe clearly
7. Figure on the right-hand side indicates full marks
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. 1.   State the differences between high-level and low-level languages. Include their   5
advantages and disadvantages
b. 1.   Explain the role of programming languages in software development. Give two examples   5
of programming language with their domain of software development
c. 1.   Explain the functional programming paradigm. Demonstrate it with the help of a suitable   5
example
d. 1. What is an algorithm? Describe the steps involved in a structured problem-solving by   5
describing its importance for effectiveness.
e. Emirates Airline operates a complex network of domestic and international flights, serving   5
millions of passengers annually. To ensure efficient operations, passenger satisfaction, and
Page 1 of 5
--- page 2 ---
safety, the airline requires a well-organized system to manage flights, crew, passengers, and
aircraft services. Your task is to design a hierarchical decomposition tree for the Emirates
Airline Flight and Operations Management System.
The system should include the following aspects:
·   Organize flights under domestic and international routes, with each route having multiple
daily flights
·   Assign different aircraft types to each flight, ensuring optimal capacity and utilization i.e.
either Boeing or Airbus
·   Each flight has classes like Economy, Business, and First Class, along with passengers
booked in associated class along with such as seat number, ticket type, and special requests
·   Assign staff such as pilots and cabin staff to each flight
Identify the root node, 3 child nodes, and leaf nodes, and specify the level of the tree
f. Energy meter readings are recorded each hour. The six readings for today’s day taken from   5
10am to 3pm are 3, 8, 15, 24, 35, 48. Find the underlying mathematical rule and give the next 3
expected readings for the coming hours
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. Describe why algorithms need to be adaptable to handle different but similar types of problems   5
b. 1.   Explain how computational thinking can be applied in everyday life, like organizing tasks   5
or planning an event. Give an example in support of your answer
c. 1.   Consider the following algorithm:   5
Step 1: Input total_accounts
Step 2: For each account i = 1 to total_accounts
Input principal, rate, time
amount = principal * (1 + rate/100)^time
interest = amount - principal
Print account ID, interest, amount
Discuss what happens if interest calculation is done before amount calculation inside the loop
d. 1.   Explain what problem this algorithm is designed to solve.   5
Input: n_taxpayers
Output: tax_amount[i]
BEGIN
Page 2 of 5
--- page 3 ---
FOR i ← 1 TO n_taxpayers DO
Input annual_income[i]
IF annual_income[i] ≤ 500000 THEN
tax_amount[i] ← 0
ELSE IF annual_income[i] ≤ 1000000 THEN
tax_amount[i] ← 0.1 * (annual_income[i] - 500000)
ELSE
tax_amount[i] ← 0.1*500000 + 0.2*(annual_income[i] - 1000000)
ENDIF
DISPLAY taxpayer_ID[i], tax_amount[i]
ENDFOR
END
e. Draw a flowchart to convert hours into minutes and seconds. Check if the input is a positive   5
number, if not ask to re-enter
f. 1. A small classroom wants to record attendance and calculate the percentage of students   5
present each day. Each student can be marked either “Present” or “Absent.” The teacher also
wants to identify students with attendance below 75%. Design an algorithm to track attendance
and compute percentages for each student, calculate the percentage of students present, and
identify students with attendance below 75%
Q3. Answer the following questions(Attempt Any 4 Questions)   20
a. Explain the evolution of programming languages.   5
b. The pseudocode below computes the average of marks of 5 students, but it contains errors.   5
Identify and state why they are errors and rewrite the correct pseudocode.
SET sum = 0
FOR i = 1 TO 5
PRINT "Enter mark:"
INPUT mark
SET sum = sum - mark
END FOR
average = sum / 5
PRINT "The average mark is: " + mark
Page 3 of 5
--- page 4 ---
c. A pseudocode assigns grades based on marks using CASE and Nested IF. Compare the two   5
approaches.
Variant A (CASE):
DISPLAY "Enter marks:"
INPUT marks
SELECT CASE
CASE marks >= 90: DISPLAY "Grade A"
CASE marks >= 75: DISPLAY "Grade B"
CASE marks >= 50: DISPLAY "Grade C"
CASE ELSE: DISPLAY "Fail"
END SELECT
Variant B (Nested IF):
DISPLAY "Enter marks:"
INPUT marks
IF marks >= 90 THEN
DISPLAY "Grade A"
ELSE
IF marks >= 75 THEN
DISPLAY "Grade B"
ELSE
IF marks >= 50 THEN
DISPLAY "Grade C"
ELSE
DISPLAY "Fail"
END IF
END IF
END IF
d. Perform dry run for the following pseudocode and trace for x = -5, 7, -3, 10, 1 and tabulate the   5
execution.
Declare Integer sum = 0
FOR i = 1 TO 5
Input x
If x > 0 Then
SET sum = sum + x
Page 4 of 5
--- page 5 ---
End If
End FOR
Display "Sum of positive numbers: "+ sum
e. Create a module/function ConvertToFahrenheit that converts a given Celsius temperature to   5
Fahrenheit. Call the module/function in the main body and display the output (Formula:
Fahrenheit=(Celsius×9/5)+32)
f. Design a pseudocode to find the largest even numbers from 8 numbers entered by user.   5
Page 5 of 5
````
