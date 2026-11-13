# Software Testing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper a5da64cdf66b

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_IT_7001/Software Testing/ANS_Software Testing(702IT0E035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Software Testing
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Answer briefly:   [20]
a.   Correct explanation of Errors, Defects, Failure in a software project
5Marks
The Error is a human mistake. An Error appears not only due to the
logical mistake in the code made by the developer
A Software Defect is a condition in a software product that does not
meet a software requirement (as stated in the requirement
specifications) or end-user expectations
Q1
CO-   Failure is a consequence of a Defect. It is the observable incorrect
1,2,3;   behavior of the system. Failure occurs when the software fails to
SO- 2;   perform in the real environment.   [5]
BL-
-
Analyse,   error – a human mistake made by the developer while implementing
explain   the coupon calculation logic, for example, using the wrong formula or
forgetting to apply a tax rule after discount.
defect (bug) – the incorrect code or logic in the program caused by
that error, such as the function applying the coupon twice or ignoring
the coupon cap limit.
failure – the visible incorrect behavior in the running system, where
the customer sees a wrong total price displayed or charged at checkout
because the defect was executed during use.
********** 1 **********
--- page 2 ---
b.   Mutation Testing:
•   Introduces small changes (mutants) in the code to simulate
typical developer mistakes.
•   Similar idea to error seeding: introduce defects and verify that
test cases are comprehensive enough to 'catch' the defects
(called mutants).
• This method is more systematic--all single modifications to the   [5]
code are generated--each single modification yields a new
mutant.
• The idea is that test suite is adequate when it suffices to
distinguish between the original and any
non-equivalent mutant.
c.   Alpha testing
conducted within the development environment before the portal’s
public release. testers, faculty representatives, and qa engineers
simulate real exam conditions.
steps:
• test all core modules—login, question navigation, timer, autosave,
and submission.
• check load handling, browser compatibility, and network
interruptions.
• identify and fix functional and usability issues before students access
the system.
outcome: internal validation that the portal is stable and meets
university requirements.
[5]
beta testing
performed by a limited group of real users (students and invigilators)
in an actual university setting.
steps:
• release a pre-production version for a mock test session.
• collect user feedback on performance, interface clarity, and issue
reports.
• monitor real-world factors like internet reliability, device diversity,
and user errors.
outcome: ensures the portal performs correctly under real conditions,
and feedback is used for final refinements before the official rollout.
d.   Discuss the significance of naming and structuring test cases within a [5]
project lifecycle.
• clarity and understanding – descriptive names help testers and
developers quickly identify the purpose and scope of each test.
• traceability – structured test cases link directly to specific
********** 2 **********
--- page 3 ---
requirements or user stories, supporting requirement coverage and
auditability.
• reusability – organized test cases can be reused across versions,
saving time in regression and maintenance testing.
Q2   a.   Consider an online shopping cart that applies discounts based on [10]
CO-3,2;
membership type, cart value, and coupon validity. Apply Cause Effect
SO-2;
Graphing Technique to identify all possible combinations and derive
BL-
minimal test cases.   - 6m
Design,
Apply
Explain steps of decision table testing. 4m
•   membership:   none,   silver,   gold   (exclusive)
• coupon: valid or invalid;
valid may   have   min_cart ≥   x   and   max_discount   cap
• discount policy
• identify conditions and their possible values (true/false or
enumerations)
•   identify   all   actions/effects   that   the   system   can   take
• construct the decision table by listing every meaningful combination
of   conditions   and   mapping   to   actions
• apply constraints to eliminate impossible combinations and merge
equivalent columns
b.   Explain ECP technique.   - 5M   [10]
Consider a file uploader that allows sizes from 1 mb to 25 mb inclusive
and rejects anything outside. Apply boundary value analysis to derive
test cases at and around these limits. – 5M
********** 3 **********
--- page 4 ---
concept:
equivalence class partitioning is a black-box testing technique used to
divide input data into groups (classes) that are expected to produce
similar behavior. instead of testing every possible input, representative
values are chosen from each class to reduce the total number of test
cases while maintaining good coverage.
steps:
1. identify valid and invalid input ranges or conditions.
2. divide inputs into partitions (classes) where the system is
expected to behave the same.
3. select one representative value from each class for testing.
advantages:
• minimizes the number of test cases.
• ensures all input categories are tested once.
• improves efficiency and detects boundary-related errors early.
requirement:
file uploader accepts sizes from 1 mb to 25 mb inclusive, rejects
outside this range.
boundaries:
lower boundary = 1 mb
upper boundary = 25 mb
a.   Integration test techniques :
Diagram : 2Marks
Correct explanation : 8M
❑ There are different strategies for integration testing
Q3   ❑ Within incremental integration testing a range of possibilities
CO-2,3;   exist, partly depending on the system architecture:
SO-2;   [10]
BL-   ❑ Top-down: testing takes place from top to bottom,
Design   following the control flow or architectural structure
Analyse
(e.g. starting from the GUI or main menu). Components
or systems are substituted by stubs.
❑ Bottom-up: testing takes place from the bottom of the
control flow upwards. Components or systems are
substituted by drivers.
********** 4 **********
--- page 5 ---
❑ Functional incremental: integration and testing takes
place on the basis of the functions or functionality, as
documented in the functional specification.
❑ tests interfaces between components, interactions to different
parts of a system such as an operating system, file system and
hardware or interfaces between systems.
❑ Integration means building up groups of components
❑ Integration tests examine component interactions against the
specification of interfaces
❑ Integrating sub-systems (they consist of integrated
components) is also a form of integration
i. Bottom-Up Integration Testing
•   Starts with lower-level modules and integrates upwards.
• Requires drivers to simulate higher modules.
•   Effective when lower modules are critical or stable.
ii. Big Bang Integration Testing
•   All modules integrated simultaneously after development.
• High risk of failure isolation; useful for small systems.
• Needs extensive debugging if failure occurs
‘Big-bang' integration testing - one extreme - all components or
systems are integrated simultaneously, after which everything is tested
as a whole.
Big-bang testing has the advantage that everything is finished before
integration testing starts.
There is no need to simulate (as yet unfinished) parts
The major disadvantage of the big-bang is that in general it is time
consuming and difficult to trace the cause of failures with this late
integration.
b.   Explain error guessing technique 5M
Apply compute cyclomatic complexity
and list independent paths on this test scenario: -5M
1. def k(s):
2.   try:   [10]
3.   n = int(s)
4.   except ValueError:
5.   return "bad"
6.   else:
return "neg" if n < 0 else "ok"
********** 5 **********
--- page 6 ---
formula:
v(g)   =   number   of   decisions   +   1
=   2   +   1
= 3
a.   Regression Testing
Q4
CO-2,3;
SO-6;
BL-
[10]
Evaluate
Understa
❑ Repeating a test of functionality that has already been
nd
verified is called a regression test.
❑ The scope of the regression test depends on the risk, that
the newly implemented functionality (extension or error
fix) imposes to the system.
❑ Analyzing this risk can be done with an impact analysis
❑ Change related testing may be performed at all test
levels.
❑ Typical tests after changes are:
❑ Re-testing ( = Testing after correction of errors )
❑ Regression testing ( = Testing to uncover newly
introduced defects)
********** 6 **********
--- page 7 ---
b.   Contrast White Box testing and Black Box testing.
❑ The tester knows the internal structure of the
program/code
❑ i.e. component hierarchy, control flow, data flow,
etc.
❑ Test   cases are   selected   on   the   basis
of   internal   program code/program structure
❑ During testing, interference with the test
execution is possible
[10]
❑ Structure of the program is the focus of attention!
❑ White-box technique is also called structure-
based testing or control flow based testing
❑ Test cases can be designed using different methods
❑ If specification functionality is the focus of testing, the
methods used are called
❑ specification oriented methods or black-box methods.
❑ If the internal structure of an object is investigated, the
methods used are called structure oriented methods or
white-box methods.
********** 7 **********

[Text in pictures on this page, read by OCR]
Identification of Bugs

Identification of

Program failure Debugging

bugs
Modification {
Modification
of source code
to make it bug free
Selection & Execution of Test Cases
Select en test Generate new test Execute test cases to
covering the modified and [>| _,, a8 [2] (pettoraregression:
if required testing

affected parts of the code
--- page 8 ---
Examples:
❑ Equivalence partitioning
❑ Boundary value analysis
❑ Decision table testing and cause-effect graphing
❑ State transition testing
a.   Consider an AI-powered healthcare monitoring system that tracks
patient vitals, alerts caregivers, and predicts emergencies. Identify the
need for system testing - 4M
and apply four suitable system testing techniques for given scenario -
6m
test cases:
[10]
1. Security Testing
2. Performance Testing
3. Load Testing
Q5
CO-2,3;
SO-2;
BL-
Apply
Discuss
b.   Consider a mobile wallet that moves through idle, authentication,
authorized, processing, paid/declined, and locked states based on
biometric results, timeouts, and payment outcomes. Apply state
transition testing to validate behavior, illustrate states and transitions,
and design test cases.
[10]
idle → authentication → authorized → processing → paid → idle
(successful payment).
idle → authentication → locked (three wrong fingerprints).
authorized → processing → declined → idle (insufficient balance).
********** 8 **********
--- page 9 ---
idle – waiting for user input.
authentication – verifying user via pin or biometric.
authorized – user validated, ready for payment.
processing – payment being sent to bank.
a.   Explain the following styles of software testing:
i.   Mockist Style
ii.   Classic Style
i. Mockist Style:
• Uses mock objects to simulate dependencies.
• Focus on interaction testing.
• Popular in TDD and Agile environments.
Mockist TDD promotes a style called need-driven development. We
first develop from the
outside of the system (UI for example).
We then think about expectations and interactions between the
Software and collaborators.
Q6   It makes us think ahead with the implementation of the production
CO-2;   code through the mocks.
SO-6;   The expectations/assumptions, about mocks created, become the   [10]
BL-   starting points for our other
Understa   tests.
ii. Classic Style:
nd,Analy   •   Relies on real implementations or stubs.
ze   • Focus on state testing and logic verification.
• Often used in traditional unit testing setups.
The classical TDD style tests system boundaries.
It might use mock if the collaboration between the software and the
collaborator make state
verification impossible.
slow to run, or
a production service that cannot be used for testing, or
unreliable.
[10]
b.
********** 9 **********
--- page 10 ---
path   testing   in   brief
path testing is a white-box technique that targets execution paths
through a module’s control flow graph (cfg) to achieve strong logic
coverage.
the common variant, basis path testing, uses cyclomatic complexity
V(g)
= P+1
= R
=E-N+2
a.   Correct explanation of how software testing is applied across different [10]
industries to ensure product reliability and performance.
Few Applications are explained below:
Healthcare: Verifies life-critical systems like
patient records,
diagnosis tools ( security testing).
Banking & Finance: Ensures secure,
Q7
accurate transaction processing
CO-3;
SO-6;   and fraud detection
BL-
Discuss,   E-commerce:
Apply   Tests user experience,
payment gateway,
and inventory logic
(e.g., usability, load, and functional testing).
b.   Explain the concept of Loop Testing. – 5M
[10]
Apply Loop Testing for scenario explained in Q5a)   - 5M
********** 10 **********
--- page 11 ---
loop testing – explanation (5m)
loop testing is a white-box testing technique used to validate the
correctness of looping constructs (for, while, do-while) in a program. it
focuses on ensuring that loops execute the correct number of times,
handle boundary conditions properly, and terminate as expected.
objectives
• verify that the loop initializes correctly and terminates at the right
condition.
• detect infinite loops or skipped iterations due to incorrect loop
control.
• confirm that performance is acceptable for large iteration counts.
types of loop testing
1. simple loops – test with zero, one, typical, and maximum
iterations.
2. nested loops – test inner loops while keeping outer loops at
minimum, then incrementally expand.
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 8f956baaf124

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_IT_7001/Software Testing/ANS_Software Testing(702IT0E035)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Software Testing
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
SYNOPTIC SOLUTION
Answer briefly:   [20]
a.   Traditional testing and Agile testing process.
5 points of valid differentiation
• Traditional:
o Testing is a separate phase after development.
[5]
o Testers work independently; limited collaboration.
Q1
•   Agile:
CO-   o Testing is continuous and integrated within sprints.
1,2,3;
SO- 2;   Emphasis on collaboration, TDD, automation, and early
BL-   feedback
-Apply,
understa   b.   Error guessing is a software testing technique based on the tester’s
nd   experience, intuition, and domain knowledge to anticipate areas where
defects are most likely to occur.
instead of following formal test design methods, the tester uses
insights from similar past failures, known problem patterns, or typical   [5]
user mistakes to create targeted test cases.
Examples include testing for null inputs, boundary violations, invalid
formats, or missing configurations. this approach complements
structured testing
********** 1 **********
--- page 2 ---
c.   Acceptance testing is the final level of software testing performed to
determine whether a system meets business requirements and is ready
for deployment. it focuses on validating the software from the end
user’s perspective rather than finding defects.
purpose
• to confirm the software fulfills functional and non-functional
requirements.   [5]
• to ensure readiness for release and user satisfaction.
Correct application -5M
d.   software testing plays a crucial role in the project lifecycle by ensuring [5]
that the developed system meets its requirements, functions reliably, and
delivers quality to end users. it acts as a quality gate at every stage of
development.
Significance
•   Validate that the software meets user and business
requirements.
• Detect defects early to reduce post-release cost.
• Ensure functional and non-functional correctness.
Q2   a.   Explain the steps of Boundary Value Analysis. – 4M   [10]
CO-3,2;
SO-2;
BL-
Suppose an api provides a per-user limit of 100 requests per minute.
Design,
Apply boundary value analysis to design tests .- 6M
Apply
Justification
- Each partition represents a logically distinct input category, allowing
selection   of   a   single   test   case   from   each.
- Ensures meaningful coverage with fewer test cases than testing all
possible ages.
b.   Explanation of the Unit Testing framework.   – 5M   [10]
********** 2 **********
--- page 3 ---
also known as unit, module or program
test of each software component after its realization
searches for defects in, and verifies the functioning of software (e.g.
modules, programs, objects, classes, etc.) that are separately testable
Design Unit test cases for the above scenario.—5M
a.   Integration test techniques :
Diagram : 2Marks
Correct explanation : 8M
❑ There are different strategies for integration testing
❑ Within incremental integration testing a range of possibilities
exist, partly depending on the system architecture:
❑ Top-down: testing takes place from top to bottom,
following the control flow or architectural structure
Q3   (e.g. starting from the GUI or main menu). Components
CO-2,3;   or systems are substituted by stubs.
SO-2;   [10]
BL-   ❑ Bottom-up: testing takes place from the bottom of the
Design
Analyse   control flow upwards. Components or systems are
substituted by drivers.
❑ Functional incremental: integration and testing takes
place on the basis of the functions or functionality, as
documented in the functional specification.
❑ tests interfaces between components, interactions to different
parts of a system such as an operating system, file system and
hardware or interfaces between systems.
❑ Integration means building up groups of components
********** 3 **********
--- page 4 ---
❑ Integration tests examine component interactions against the
specification of interfaces
❑ Integrating sub-systems (they consist of integrated
components) is also a form of integration
i. Bottom-Up Integration Testing
•   Starts with lower-level modules and integrates upwards.
• Requires drivers to simulate higher modules.
•   Effective when lower modules are critical or stable.
ii. Big Bang Integration Testing
•   All modules integrated simultaneously after development.
• High risk of failure isolation; useful for small systems.
• Needs extensive debugging if failure occurs
• stubs – dummy modules that simulate the behavior of lower-level
components called by the module under test; used in top-down testing.
example: a payment gateway stub that returns a fixed transaction
response.
• drivers – temporary modules that call and test lower-level
components; used in bottom-up testing.
example: a test driver that invokes account validation functions with
predefined inputs.
b.   Explain basic path testing   - 4M
Apply Basic Path testing and compute
cyclomatic complexity on this test scenario – 6Marks
◦ The cyclomatic number can be used as a target value for code
reviews
◦ The cyclomatic number can also be calculated as the number   [10]
of independent decisions plus one.
Example
◦ v(G) = e-n + 2p
Q4   a.   Different levels of software testing with suitable example.   [10]
********** 4 **********
--- page 5 ---
CO-2,3;
SO-6;
Unit
BL-
Integration
Evaluate
System
Understa
Acceptance
nd
unit testing – verifies each small module or function independently to
ensure internal logic correctness.
integration testing – checks how multiple modules interact and
exchange data to confirm proper interface behavior.
system testing – validates the entire integrated system against
functional and non-functional requirements.
acceptance testing – confirms that the complete system meets user
needs and business requirements before release.
Description – 8M
Example – 2M
b.   causes (boolean)
c1: credit high
c2: credit mid
c3: income high
c4: income mid
c5: history good
c6: history risky
effects
e1: approve
e2: approve with conditions (reduced limit/higher rate)   [10]
e3: manual review
e4: reject
Sample Test cases
t1 approve: score 780, income ₹95k, history good → e1
t2 conditional: score 770, income ₹60k, history good → e2
t3 conditional: score 700, income ₹100k, history good → e2
********** 5 **********
--- page 6 ---
a.   Role of system testing in a software development process –3M
Apply system testing on a software application for self-driving car
entertainment system combining voice input, hand gestures, and touch
controls. – 7M
performance testing – test response speed; commands should be
recognized quickly without delays or freezing.
usability testing – ensure controls are easy to use while driving   [10]
and not distracting for the driver.
safety testing – check that unsafe actions (like typing while
moving) are blocked.
stress testing – run tests with background noise, poor lighting, or
multiple inputs at once to check reliability.
b.   Regression Testing
Q5
CO-2,3;
SO-2;
BL-
Apply
Discuss
[10]
❑ Repeating a test of functionality that has already been
verified is called a regression test.
❑ The scope of the regression test depends on the risk, that
the newly implemented functionality (extension or error
fix) imposes to the system.
❑ Analyzing this risk can be done with an impact analysis
********** 6 **********
--- page 7 ---
❑ Change related testing may be performed at all test
levels.
❑ Typical tests after changes are:
❑ Re-testing ( = Testing after correction of errors )
❑ Regression testing ( = Testing to uncover newly
introduced defects)
a.   Correct explanation of how software testing is applied across different
industries to ensure product reliability and performance.
Few Applications are explained below:
Healthcare: Verifies life-critical systems like
Q6
CO-2;   patient records,
SO-6;
BL-   diagnosis tools ( security testing).
[10]
Understa
Banking & Finance: Ensures secure,
nd,
accurate transaction processing
Analyze
and fraud detection
E-commerce:
Tests user experience,
********** 7 **********

[Text in pictures on this page, read by OCR]
Identification of Bugs

Identification of

Program failure Debugging

bugs
Modification f
Modification
of source code
to make it bug free
Selection & Execution of Test Cases
Select ——— test Generate new test Execute test cases to
covering the modified and ka poe [>| perform Tegression
if required testing

affected parts of the code
--- page 8 ---
payment gateway,
and inventory logic
(e.g., usability, load, and functional testing).
b.   Explain the process of state transition testing – 4 marks
Apply state transition testing for correct functional behavior.- 6Marks
Ensures the system behaves correctly through all valid and invalid
state changes.
Usefulness: Effective for systems like vending machines, login
systems, and protocol testing where flow changes based on input
conditions.
[10]
Test cases can be :
initiated → authenticated → authorized → queued → processing →
succeeded
processing → failed
authorized → canceled
succeeded → refunded | reversed | disputed
any → on_hold (fraud/risk) → authorized/failed
a.   Explain the following styles of software testing:   [10]
i.   Mockist Style
ii.   Classic Style
Q7
CO-3;   i. Mockist Style:
SO-6;   • Uses mock objects to simulate dependencies.
BL-
• Focus on interaction testing.
Discuss,   • Popular in TDD and Agile environments.
Apply   Mockist TDD promotes a style called need-driven development. We
first develop from the
outside of the system (UI for example).
We then think about expectations and interactions between the
Software and collaborators.
********** 8 **********
--- page 9 ---
It makes us think ahead with the implementation of the production
code through the mocks.
The expectations/assumptions, about mocks created, become the
starting points for our other
tests.
b.   Discuss the terms Loop Testing and Mutation Testing in testing and its
application in software projects.
LOOP testing – 5M
Mutation Testing – 5M
loop testing – focuses on validating all looping constructs (for, while,
do-while) to ensure correct entry, iteration count, and exit conditions.
it checks initialization, boundary, and termination paths to avoid
infinite   loops   or   skipped   iterations.
applications: used in modules with iterative logic such as billing cycles,
sensor data collection,
or search algorithms to confirm stability and performance under varying
loop counts.   [10]
Mutation Testing:
•   Introduces small changes (mutants) in the code to simulate
typical developer mistakes.
•   Similar idea to error seeding: introduce defects and verify that
test cases are comprehensive enough to 'catch' the defects
(called mutants).
• This method is more systematic--all single modifications to the
code are generated--each single modification yields a new
mutant.
********** 9 **********
--- page 10 ---
• The idea is that test suite is adequate when it suffices to
distinguish between the original and any
non-equivalent mutant.
********** 10 **********
````
