# Software Quality Assurance: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper cf758dd9f7eb

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   BL DL Course Marks
outcome
Q1. a   BL1 L   CO-1   5
List the different types of issues in software such as errors, faults, and
failures, and briefly explain their meaning and impact on software
quality.
Solution:
Relevant points: 5 Marks
1. Error (Human Mistake)
An error is a mistake made by a developer, such as wrong logic or
misunderstanding requirements.
Impact: Leads to problems in the system design or code.
2. Fault (Problem in Code)
A fault is the incorrect code or design caused by an error.
Impact: It exists in the system and may cause
incorrect behavior when executed.
3. Failure (System Not Working as Expected)
A failure occurs when the system does not perform as expected
during execution.
Impact: Directly affects users and reduces system reliability.
Q1.b   BL2 M   CO-1   5
********** 1 **********
--- page 2 ---
During requirement analysis, a team maps user needs to quality
attributes.
Explain the need for a comprehensive definition of requirements that will
helps in this process.
Relevant 5 points: 5 Marks
• Need for improving poor requirements documents is well-
known!!
•   Frequently lack quality factors such as: usability, reusability,
maintainability.
•   Software industry groups the long list of related attributes into
what we call quality factors. (Sometimes non-functional
requirements)
• Unequal highlighting on all quality factors.
• Emphasis varies from project to project
o   Scalability; maintainability; reliability; portability; etc.
Need for a comprehensive definition of requirements that will cover all
attributes of software
Q1.c   BL   L   CO-2   5
Apply IEEE 1012 standard concepts to a software project and explain how 3
they help in ensuring effective verification and validation.
Answer:
•   Defines verification and validation processes
•   Ensures software meets requirements
•   Applied throughout lifecycle
• Improves reliability and correctness
•   Supports quality assurance
Rubric:
•   Definition: 2 marks
•   Purpose: 2 marks
•   Benefit: 1 mark
Q1.d   BL H   CO-3   5
4
Analyze the limitations of software quality metrics and explain how these
limitations can impact the evaluation of software quality.
• Budget constraints in allocating the necessary resources
(manpower, funds, etc.) for development of a quality metrics
system and its regular application.
• Human factors, especially opposition of employees to evaluation
of their activities.
•   Uncertainty regarding the data’s validity, rooted in partial and
biased reporting.
The main factors affecting development process parameters
********** 2 **********
--- page 3 ---
• Programming style: strongly affects software volume, where
“wasteful” coding may double the volume of produced code
(KLOC).
• Volume of documentation comments included in the code: affects
volume of the code.
•   Software complexity
•   Percentage of reused code
•   Professionalism and thoroughness of design review and software
testing teams
•   Reporting style of the review and testing results
Relevant 5 points: 5 Marks
Q2.A.   .   BL M   CO-3   10
Solution-   5
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality   Tests internal logic
Definition without knowing internal and structure of
code   code
Control flow, paths,
Focus   Inputs and outputs
conditions
Requires
Knowledge No programming
programming
Required   knowledge
knowledge
Testing   System, acceptance   Unit, integration
Level   testing   testing
Equivalence partitioning, Path testing, loop
Techniques
BVA   testing
Validate functional   Ensure code
Objective
requirements   correctness
Error   Missing/incorrect   Logical errors, dead
Detection   functions   code
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
********** 3 **********
--- page 4 ---
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
********** 4 **********
--- page 5 ---
Correct user-facing results
Q2. B.   Explain the various user difficulties caused due to lack of proper quality BL   L   CO-4   10
assurance maintenance activities, how these difficulties affect user   2
experience and system usability.
Relevant 5 points: 10 Marks
• Code failure (usually termed “software failure”).
• Documentation failure in the user’s manual, help screens or
other form of documentation prepared for the user. In this case,
the support service can provide the user with correct instructions
(although no correction of the software documentation itself is
performed).
•   Incomplete, vague or imprecise documentation.
•   User’s insufficient knowledge of the software system or his or
her failure to use the documentation supplied. In
these situations no software system failure is encountered.
Q3.A.   BL2 M   CO-4   10
Describe the SQA standards, system certification, and assessment
components.
Why is certification critical and what standards/processes are involved?
Solution:
1 Overview of Standards in SQA
SQA standards are documented agreements containing technical
specifications or precise criteria used consistently as guidelines to ensure
materials, products, processes, and services are fit for their purpose. In
software engineering, standards provide a common language and
benchmark for quality across organizations and industries.
2 ISO 9001 in SQA
ISO 9001 is a generic quality management standard applicable to any
industry, including software. It requires organizations to define
processes, measure performance, and continually improve. Software
organizations use ISO 9001 as a foundation for demonstrating that their
development processes are managed and consistent.
3 ISO 9000-3
ISO 9000-3 is specifically tailored guidance for applying ISO 9001 to
software development. It provides interpretations of ISO 9001 clauses in
the context of software, covering areas like design control, product
identification, and testing.
4 CMM and CMMI
The Capability Maturity Model (CMM) and its successor CMMI (Capability
Maturity Model Integration) define five maturity levels (Initial, Managed,
********** 5 **********
--- page 6 ---
Defined, Quantitatively Managed, Optimizing) that measure the maturity
of an organization's software development processes. CMMI is widely
used as both an internal
improvement roadmap and a certification benchmark for government
and defense contracts.
5
IEEE Standards
IEEE STD 12207 defines a framework for software lifecycle processes.
IEEE STD 1012 covers software verification and validation. IEEE STD 1028
covers software reviews and audits. These standards provide prescriptive
guidance for specific SQA activities.
6
Why Certification Is Critical
Certification provides independent verification that an organization's
quality management system meets defined standards. It builds customer
trust, enables entry into regulated markets (healthcare, aerospace,
finance), reduces risk of liability, and drives internal process discipline.
Without certification, organizations have no external validation of their
quality claims.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
Q3. B.   BL4 H   CO-4   10
Prior to testing, a software module had 150 flaws. Thirty defects were
found after deployment, but 105 defects were eliminated during testing.
Calculate the Defect Removal Efficiency and discuss the efficacy of the
testing.
Formula (2 Marks)
DRE=Defects removed during testingTotal defects×100DRE =
\frac{\text{Defects removed during testing}}{\text{Total defects}} \times
100DRE=Total defectsDefects removed during testing×100
Data (1 Mark)
•   Total defects = 150
• Removed in testing = 105
•   Post-release = 30
Calculation (3 Marks)
DRE=105150×100=70%DRE = \frac{105}{150} \times 100 =
70\%DRE=150105×100=70%
Analysis (3 Marks)
• 70% → Moderate effectiveness
• 30 defects escaped → testing not fully effective
• Need stronger test cases
Conclusion (1 Mark)
Testing efficiency is average; improvement required.
********** 6 **********
--- page 7 ---
Q4. A.   BL3 M   CO-1   10
During software development, high complexity and lack of visibility make
it difficult to ensure quality. Explain how these challenges affect software
development and suggest ways to handle them effectively.
Effect of High Complexity
1. Difficult to understand and manage
Complex systems are harder to design, test, and maintain [3].
2. More chances of errors
Increased components and interactions lead to higher risk of
issues.
3. Testing becomes challenging
It is difficult to test all possible scenarios.
Effect of Lack of Visibility
1. Invisible product
Software cannot be physically seen, making it harder to detect
problems early.
2. Late detection of issues
Errors are often found only after execution.
3. Difficult monitoring of progress
Hard to track quality during development.
Ways to Handle These Challenges
1. Modular Design
Break the system into smaller, manageable parts.
2. Proper Documentation
Maintain clear design and requirement documents.
3. Regular Reviews
Conduct code and design reviews to detect issues early.
4. Use of SQA Practices
Apply systematic quality assurance throughout development [1].
5. Automated Tools
Use tools for testing and monitoring.
6. Effective Communication
Ensure coordination among teams to reduce complexity-related
issues [5].
Conclusion
High complexity and lack of visibility make quality assurance difficult, but
with proper design, processes, and tools, these challenges can be
effectively managed.
Q4. B.   BL1 L   CO-1   10
********** 7 **********
--- page 8 ---
Discuss product revision and product transition quality factors. Explain
their role in ensuring maintainability and adaptability of software.
Software quality models such as McCall’s model classify quality factors
into product revision and product transition to address maintenance and
adaptability.
1. Product Revision Quality Factors
These focus on ease of modification and maintenance of software:
1. Maintainability – Ease of identifying and fixing defects
2. Flexibility – Ability to modify software for new requirements
3. Testability – Ease of testing after changes These factors are
crucial for debugging, updating, and enhancing software
efficiently
Role in Maintainability
• Reduces effort and cost of bug fixing
•   Supports continuous improvement and upgrades
•   Ensures reliable performance after modifications
2. Product Transition Quality Factors
These focus on adapting software to new environments:
1. Portability – Ability to run on different platforms
2. Reusability – Components can be reused in other systems
3. Interoperability – Ability to interact with other systems
These factors ensure smooth migration and integration of software
Role in Adaptability
•   Enables deployment across multiple platforms
•   Supports integration with new technologies
•   Extends software lifespan and usability
Conclusion
Product revision factors ensure maintainability, while product transition
factors ensure adaptability, together enabling software to evolve, remain
efficient, and meet changing user and technological needs.
Q5. A   BL4 L   CO-2   10
Analyse the relationship between pre-project and lifecycle components in
SQA. How do gaps in pre-project planning cause quality failures during
development? Justify with examples.
The Relationship Between Pre-Project and Lifecycle Components
Pre-project and lifecycle components in SQA form a cause-and-effect
chain. Pre-project components establish the quality framework
- objectives, standards, plans, and risk assessments. Lifecycle components
execute within that framework. When
********** 8 **********
--- page 9 ---
the framework is weak or missing, lifecycle components operate without
direction, leading to inconsistent quality outcomes.
2
The Cost of Defects Across Phases (Boehm's Rule)
Barry Boehm's research established that the cost of fixing a defect
increases exponentially as it progresses through the lifecycle. A defect
introduced in requirements costs 1x to fix in requirements, 5x in design,
10x in coding, 20x in testing, and 200x in production. Pre-project SQA
components exist to establish the controls that catch defects at the
cheapest possible stage.
3
Gap 1: Missing or Vague Quality Objectives
When pre-project components fail to define clear quality objectives,
lifecycle teams have no measurable target. Example: A government portal
project with no defined performance benchmarks resulted in a system
that met functional requirements but crashed under peak load - a defect
that was never part of the test plan because it was not a defined
quality objective.
4
Gap 2: No Standards Selected Pre-Project
Without pre-project standards selection, each team member applies their
own interpretation of quality. Example: In a multinational software
project, the absence of a pre-agreed coding standard meant that teams
from different countries wrote code with incompatible naming
conventions and error-handling patterns, creating thousands of
integration defects.
5
Gap 3: Inadequate Risk Assessment
Pre-project risk assessment should identify which components carry the
highest quality risk and allocate QA resources accordingly. When this is
skipped, high-risk areas receive the same QA attention as low-risk areas.
Example: The original Healthcare.gov launch failed partly because no pre-
project risk assessment identified
the system integration complexity as a critical quality risk, leading to
under-tested interfaces that failed under real-world load.
6
Conclusion: Pre-Project as Quality Foundation
The analysis shows that pre-project SQA components are not optional
overhead - they are the foundation upon which the entire quality edifice
rests. Lifecycle components cannot compensate for a missing or weak
pre-project framework. Organizations that invest in thorough pre-project
quality planning consistently achieve lower defect rates and higher
delivery predictability.
Marking : Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
********** 9 **********
--- page 10 ---
Q5. B.   BL5 H   CO-3   10
Assess how well defect-removal techniques like testing, inspections, and
reviews improve the overall quality of software.
Introduction (2 Marks)
Defect removal techniques such as testing, inspections, and reviews are
critical to achieving high software quality.
Technique-wise Evaluation (4 Marks)
Technique   Strength
Testing   Detects runtime errors
Inspections   Finds logical/design flaws early
Reviews   Improves requirement clarity
Comparative Analysis (2 Marks)
• Reviews → Early stage, low cost
•   Inspections → Detailed, systematic
•   Testing → Late stage, higher cost
Impact on Quality (1.5 Marks)
• Reduces defect density
• Improves reliability
• Enhances maintainability
Conclusion (0.5 Mark)
Combined use of all techniques ensures maximum defect removal
efficiency.
Q6. A.   Solution-   BL1 L   CO-3   10
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality without   Tests internal logic and
Definition
knowing internal code   structure of code
Control flow, paths,
Focus   Inputs and outputs
conditions
Knowledge   Requires programming
No programming knowledge
Required   knowledge
Testing Level System, acceptance testing   Unit, integration testing
Techniques   Equivalence partitioning, BVA Path testing, loop testing
Validate functional
Objective   Ensure code correctness
requirements
********** 10 **********
--- page 11 ---
Error
Missing/incorrect functions   Logical errors, dead code
Detection
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
********** 11 **********
--- page 12 ---
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
Correct user-facing results
Q6. B.   BL4 M   CO-4   10
Analyze the role of pre-maintenance software quality components in
ensuring effective software maintenance. How do these components
influence long-term system reliability?
Maintenance contract review:
• Customer requirements clarification
• Review of alternative approaches to maintenance provision
• Review of estimates of required maintenance resources
• Review of maintenance services to be provided by subcontractors
and/or the customer
• Review of maintenance costs estimates
Maintenance plan
• A list of the contracted maintenance services (external and
internal customers)
• A description of the maintenance team's organization
• A list of maintenance facilities
• A list of identified maintenance service risks
• A list of required software maintenance procedures and controls
• The software maintenance budget
Q7.A.   BL4 M   CO-4   10
An organization wants to evaluate its software processes
and identify improvement areas:
Explain how a software process assessment (SPICE / ISO 15504) can be
conducted and how the results can be used for process improvement.
Solution:
Answer:
• Conduct process assessment (SPICE / ISO 15504)
•   Evaluate current processes against standard models
•   Identify strengths and weaknesses
********** 12 **********
--- page 13 ---
•   Assign process capability/maturity levels
• Document findings and gaps
• Implement process improvement actions
• Monitor and reassess for continuous improvement
Rubric:
•   Understanding of process assessment : 2 marks
•   Evaluation against standards : 2 marks
•   Identification of gaps : 2 marks
• Improvement actions : 3 marks
•   Clarity / conclusion : 1 mark
Q7.B.   BL1 L   CO-4   10
Explain classification of software quality metrics.
Rubric (10 Marks)
•   Introduction / definition of software metrics → 2 marks
o Clear definition (1 mark)
o Purpose / role (1 mark)
•   Process metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
•   Product metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
Alternate Strict Evaluation (if needed)
•   Definition missing → deduct 1–2 marks
• No examples → deduct up to 2 marks
•   Only one type explained → max 5 marks
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 9bff384ff9d8

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   BL DL Course Marks
outcome
Q1. a   BL1 L   CO-1   5
List the different types of issues in software such as errors, faults, and
failures, and briefly explain their meaning and impact on software
quality.
Solution:
Relevant points: 5 Marks
1. Error (Human Mistake)
An error is a mistake made by a developer, such as wrong logic or
misunderstanding requirements.
Impact: Leads to problems in the system design or code.
2. Fault (Problem in Code)
A fault is the incorrect code or design caused by an error.
Impact: It exists in the system and may cause
incorrect behavior when executed.
3. Failure (System Not Working as Expected)
A failure occurs when the system does not perform as expected
during execution.
Impact: Directly affects users and reduces system reliability.
Q1.b   BL2 M   CO-1   5
********** 1 **********
--- page 2 ---
During requirement analysis, a team maps user needs to quality
attributes.
Explain the need for a comprehensive definition of requirements that will
helps in this process.
Relevant 5 points: 5 Marks
• Need for improving poor requirements documents is well-
known!!
•   Frequently lack quality factors such as: usability, reusability,
maintainability.
•   Software industry groups the long list of related attributes into
what we call quality factors. (Sometimes non-functional
requirements)
• Unequal highlighting on all quality factors.
• Emphasis varies from project to project
o   Scalability; maintainability; reliability; portability; etc.
Need for a comprehensive definition of requirements that will cover all
attributes of software
Q1.c   BL   L   CO-2   5
Apply IEEE 1012 standard concepts to a software project and explain how 3
they help in ensuring effective verification and validation.
Answer:
•   Defines verification and validation processes
•   Ensures software meets requirements
•   Applied throughout lifecycle
• Improves reliability and correctness
•   Supports quality assurance
Rubric:
•   Definition: 2 marks
•   Purpose: 2 marks
•   Benefit: 1 mark
Q1.d   BL H   CO-3   5
4
Analyze the limitations of software quality metrics and explain how these
limitations can impact the evaluation of software quality.
• Budget constraints in allocating the necessary resources
(manpower, funds, etc.) for development of a quality metrics
system and its regular application.
• Human factors, especially opposition of employees to evaluation
of their activities.
•   Uncertainty regarding the data’s validity, rooted in partial and
biased reporting.
The main factors affecting development process parameters
********** 2 **********
--- page 3 ---
• Programming style: strongly affects software volume, where
“wasteful” coding may double the volume of produced code
(KLOC).
• Volume of documentation comments included in the code: affects
volume of the code.
•   Software complexity
•   Percentage of reused code
•   Professionalism and thoroughness of design review and software
testing teams
•   Reporting style of the review and testing results
Relevant 5 points: 5 Marks
Q2.A.   .   BL M   CO-3   10
Solution-   5
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality   Tests internal logic
Definition without knowing internal and structure of
code   code
Control flow, paths,
Focus   Inputs and outputs
conditions
Requires
Knowledge No programming
programming
Required   knowledge
knowledge
Testing   System, acceptance   Unit, integration
Level   testing   testing
Equivalence partitioning, Path testing, loop
Techniques
BVA   testing
Validate functional   Ensure code
Objective
requirements   correctness
Error   Missing/incorrect   Logical errors, dead
Detection   functions   code
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
********** 3 **********
--- page 4 ---
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
********** 4 **********
--- page 5 ---
Correct user-facing results
Q2. B.   Explain the various user difficulties caused due to lack of proper quality BL   L   CO-4   10
assurance maintenance activities, how these difficulties affect user   2
experience and system usability.
Relevant 5 points: 10 Marks
• Code failure (usually termed “software failure”).
• Documentation failure in the user’s manual, help screens or
other form of documentation prepared for the user. In this case,
the support service can provide the user with correct instructions
(although no correction of the software documentation itself is
performed).
•   Incomplete, vague or imprecise documentation.
•   User’s insufficient knowledge of the software system or his or
her failure to use the documentation supplied. In
these situations no software system failure is encountered.
Q3.A.   BL2 M   CO-4   10
Describe the SQA standards, system certification, and assessment
components.
Why is certification critical and what standards/processes are involved?
Solution:
1 Overview of Standards in SQA
SQA standards are documented agreements containing technical
specifications or precise criteria used consistently as guidelines to ensure
materials, products, processes, and services are fit for their purpose. In
software engineering, standards provide a common language and
benchmark for quality across organizations and industries.
2 ISO 9001 in SQA
ISO 9001 is a generic quality management standard applicable to any
industry, including software. It requires organizations to define
processes, measure performance, and continually improve. Software
organizations use ISO 9001 as a foundation for demonstrating that their
development processes are managed and consistent.
3 ISO 9000-3
ISO 9000-3 is specifically tailored guidance for applying ISO 9001 to
software development. It provides interpretations of ISO 9001 clauses in
the context of software, covering areas like design control, product
identification, and testing.
4 CMM and CMMI
The Capability Maturity Model (CMM) and its successor CMMI (Capability
Maturity Model Integration) define five maturity levels (Initial, Managed,
********** 5 **********
--- page 6 ---
Defined, Quantitatively Managed, Optimizing) that measure the maturity
of an organization's software development processes. CMMI is widely
used as both an internal
improvement roadmap and a certification benchmark for government
and defense contracts.
5
IEEE Standards
IEEE STD 12207 defines a framework for software lifecycle processes.
IEEE STD 1012 covers software verification and validation. IEEE STD 1028
covers software reviews and audits. These standards provide prescriptive
guidance for specific SQA activities.
6
Why Certification Is Critical
Certification provides independent verification that an organization's
quality management system meets defined standards. It builds customer
trust, enables entry into regulated markets (healthcare, aerospace,
finance), reduces risk of liability, and drives internal process discipline.
Without certification, organizations have no external validation of their
quality claims.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
Q3. B.   BL4 H   CO-4   10
Prior to testing, a software module had 150 flaws. Thirty defects were
found after deployment, but 105 defects were eliminated during testing.
Calculate the Defect Removal Efficiency and discuss the efficacy of the
testing.
Formula (2 Marks)
DRE=Defects removed during testingTotal defects×100DRE =
\frac{\text{Defects removed during testing}}{\text{Total defects}} \times
100DRE=Total defectsDefects removed during testing×100
Data (1 Mark)
•   Total defects = 150
• Removed in testing = 105
•   Post-release = 30
Calculation (3 Marks)
DRE=105150×100=70%DRE = \frac{105}{150} \times 100 =
70\%DRE=150105×100=70%
Analysis (3 Marks)
• 70% → Moderate effectiveness
• 30 defects escaped → testing not fully effective
• Need stronger test cases
Conclusion (1 Mark)
Testing efficiency is average; improvement required.
********** 6 **********
--- page 7 ---
Q4. A.   BL3 M   CO-1   10
During software development, high complexity and lack of visibility make
it difficult to ensure quality. Explain how these challenges affect software
development and suggest ways to handle them effectively.
Effect of High Complexity
1. Difficult to understand and manage
Complex systems are harder to design, test, and maintain [3].
2. More chances of errors
Increased components and interactions lead to higher risk of
issues.
3. Testing becomes challenging
It is difficult to test all possible scenarios.
Effect of Lack of Visibility
1. Invisible product
Software cannot be physically seen, making it harder to detect
problems early.
2. Late detection of issues
Errors are often found only after execution.
3. Difficult monitoring of progress
Hard to track quality during development.
Ways to Handle These Challenges
1. Modular Design
Break the system into smaller, manageable parts.
2. Proper Documentation
Maintain clear design and requirement documents.
3. Regular Reviews
Conduct code and design reviews to detect issues early.
4. Use of SQA Practices
Apply systematic quality assurance throughout development [1].
5. Automated Tools
Use tools for testing and monitoring.
6. Effective Communication
Ensure coordination among teams to reduce complexity-related
issues [5].
Conclusion
High complexity and lack of visibility make quality assurance difficult, but
with proper design, processes, and tools, these challenges can be
effectively managed.
Q4. B.   BL1 L   CO-1   10
********** 7 **********
--- page 8 ---
Discuss product revision and product transition quality factors. Explain
their role in ensuring maintainability and adaptability of software.
Software quality models such as McCall’s model classify quality factors
into product revision and product transition to address maintenance and
adaptability.
1. Product Revision Quality Factors
These focus on ease of modification and maintenance of software:
1. Maintainability – Ease of identifying and fixing defects
2. Flexibility – Ability to modify software for new requirements
3. Testability – Ease of testing after changes These factors are
crucial for debugging, updating, and enhancing software
efficiently
Role in Maintainability
• Reduces effort and cost of bug fixing
•   Supports continuous improvement and upgrades
•   Ensures reliable performance after modifications
2. Product Transition Quality Factors
These focus on adapting software to new environments:
1. Portability – Ability to run on different platforms
2. Reusability – Components can be reused in other systems
3. Interoperability – Ability to interact with other systems
These factors ensure smooth migration and integration of software
Role in Adaptability
•   Enables deployment across multiple platforms
•   Supports integration with new technologies
•   Extends software lifespan and usability
Conclusion
Product revision factors ensure maintainability, while product transition
factors ensure adaptability, together enabling software to evolve, remain
efficient, and meet changing user and technological needs.
Q5. A   BL4 L   CO-2   10
Analyse the relationship between pre-project and lifecycle components in
SQA. How do gaps in pre-project planning cause quality failures during
development? Justify with examples.
The Relationship Between Pre-Project and Lifecycle Components
Pre-project and lifecycle components in SQA form a cause-and-effect
chain. Pre-project components establish the quality framework
- objectives, standards, plans, and risk assessments. Lifecycle components
execute within that framework. When
********** 8 **********
--- page 9 ---
the framework is weak or missing, lifecycle components operate without
direction, leading to inconsistent quality outcomes.
2
The Cost of Defects Across Phases (Boehm's Rule)
Barry Boehm's research established that the cost of fixing a defect
increases exponentially as it progresses through the lifecycle. A defect
introduced in requirements costs 1x to fix in requirements, 5x in design,
10x in coding, 20x in testing, and 200x in production. Pre-project SQA
components exist to establish the controls that catch defects at the
cheapest possible stage.
3
Gap 1: Missing or Vague Quality Objectives
When pre-project components fail to define clear quality objectives,
lifecycle teams have no measurable target. Example: A government portal
project with no defined performance benchmarks resulted in a system
that met functional requirements but crashed under peak load - a defect
that was never part of the test plan because it was not a defined
quality objective.
4
Gap 2: No Standards Selected Pre-Project
Without pre-project standards selection, each team member applies their
own interpretation of quality. Example: In a multinational software
project, the absence of a pre-agreed coding standard meant that teams
from different countries wrote code with incompatible naming
conventions and error-handling patterns, creating thousands of
integration defects.
5
Gap 3: Inadequate Risk Assessment
Pre-project risk assessment should identify which components carry the
highest quality risk and allocate QA resources accordingly. When this is
skipped, high-risk areas receive the same QA attention as low-risk areas.
Example: The original Healthcare.gov launch failed partly because no pre-
project risk assessment identified
the system integration complexity as a critical quality risk, leading to
under-tested interfaces that failed under real-world load.
6
Conclusion: Pre-Project as Quality Foundation
The analysis shows that pre-project SQA components are not optional
overhead - they are the foundation upon which the entire quality edifice
rests. Lifecycle components cannot compensate for a missing or weak
pre-project framework. Organizations that invest in thorough pre-project
quality planning consistently achieve lower defect rates and higher
delivery predictability.
Marking : Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
********** 9 **********
--- page 10 ---
Q5. B.   BL5 H   CO-3   10
Assess how well defect-removal techniques like testing, inspections, and
reviews improve the overall quality of software.
Introduction (2 Marks)
Defect removal techniques such as testing, inspections, and reviews are
critical to achieving high software quality.
Technique-wise Evaluation (4 Marks)
Technique   Strength
Testing   Detects runtime errors
Inspections   Finds logical/design flaws early
Reviews   Improves requirement clarity
Comparative Analysis (2 Marks)
• Reviews → Early stage, low cost
•   Inspections → Detailed, systematic
•   Testing → Late stage, higher cost
Impact on Quality (1.5 Marks)
• Reduces defect density
• Improves reliability
• Enhances maintainability
Conclusion (0.5 Mark)
Combined use of all techniques ensures maximum defect removal
efficiency.
Q6. A.   Solution-   BL1 L   CO-3   10
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality without   Tests internal logic and
Definition
knowing internal code   structure of code
Control flow, paths,
Focus   Inputs and outputs
conditions
Knowledge   Requires programming
No programming knowledge
Required   knowledge
Testing Level System, acceptance testing   Unit, integration testing
Techniques   Equivalence partitioning, BVA Path testing, loop testing
Validate functional
Objective   Ensure code correctness
requirements
********** 10 **********
--- page 11 ---
Error
Missing/incorrect functions   Logical errors, dead code
Detection
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
********** 11 **********
--- page 12 ---
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
Correct user-facing results
Q6. B.   BL4 M   CO-4   10
Analyze the role of pre-maintenance software quality components in
ensuring effective software maintenance. How do these components
influence long-term system reliability?
Maintenance contract review:
• Customer requirements clarification
• Review of alternative approaches to maintenance provision
• Review of estimates of required maintenance resources
• Review of maintenance services to be provided by subcontractors
and/or the customer
• Review of maintenance costs estimates
Maintenance plan
• A list of the contracted maintenance services (external and
internal customers)
• A description of the maintenance team's organization
• A list of maintenance facilities
• A list of identified maintenance service risks
• A list of required software maintenance procedures and controls
• The software maintenance budget
Q7.A.   BL4 M   CO-4   10
An organization wants to evaluate its software processes
and identify improvement areas:
Explain how a software process assessment (SPICE / ISO 15504) can be
conducted and how the results can be used for process improvement.
Solution:
Answer:
• Conduct process assessment (SPICE / ISO 15504)
•   Evaluate current processes against standard models
•   Identify strengths and weaknesses
********** 12 **********
--- page 13 ---
•   Assign process capability/maturity levels
• Document findings and gaps
• Implement process improvement actions
• Monitor and reassess for continuous improvement
Rubric:
•   Understanding of process assessment : 2 marks
•   Evaluation against standards : 2 marks
•   Identification of gaps : 2 marks
• Improvement actions : 3 marks
•   Clarity / conclusion : 1 mark
Q7.B.   BL1 L   CO-4   10
Explain classification of software quality metrics.
Rubric (10 Marks)
•   Introduction / definition of software metrics → 2 marks
o Clear definition (1 mark)
o Purpose / role (1 mark)
•   Process metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
•   Product metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
Alternate Strict Evaluation (if needed)
•   Definition missing → deduct 1–2 marks
• No examples → deduct up to 2 marks
•   Only one type explained → max 5 marks
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a2532ca61eb2

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   BL DL Course Marks
outcome
Q1. a   BL1 L   CO-1   5
List the different types of issues in software such as errors, faults, and
failures, and briefly explain their meaning and impact on software
quality.
Solution:
Relevant points: 5 Marks
1. Error (Human Mistake)
An error is a mistake made by a developer, such as wrong logic or
misunderstanding requirements.
Impact: Leads to problems in the system design or code.
2. Fault (Problem in Code)
A fault is the incorrect code or design caused by an error.
Impact: It exists in the system and may cause
incorrect behavior when executed.
3. Failure (System Not Working as Expected)
A failure occurs when the system does not perform as expected
during execution.
Impact: Directly affects users and reduces system reliability.
Q1.b   BL2 M   CO-1   5
********** 1 **********
--- page 2 ---
During requirement analysis, a team maps user needs to quality
attributes.
Explain the need for a comprehensive definition of requirements that will
helps in this process.
Relevant 5 points: 5 Marks
• Need for improving poor requirements documents is well-
known!!
•   Frequently lack quality factors such as: usability, reusability,
maintainability.
•   Software industry groups the long list of related attributes into
what we call quality factors. (Sometimes non-functional
requirements)
• Unequal highlighting on all quality factors.
• Emphasis varies from project to project
o   Scalability; maintainability; reliability; portability; etc.
Need for a comprehensive definition of requirements that will cover all
attributes of software
Q1.c   BL   L   CO-2   5
Apply IEEE 1012 standard concepts to a software project and explain how 3
they help in ensuring effective verification and validation.
Answer:
•   Defines verification and validation processes
•   Ensures software meets requirements
•   Applied throughout lifecycle
• Improves reliability and correctness
•   Supports quality assurance
Rubric:
•   Definition: 2 marks
•   Purpose: 2 marks
•   Benefit: 1 mark
Q1.d   BL H   CO-3   5
4
Analyze the limitations of software quality metrics and explain how these
limitations can impact the evaluation of software quality.
• Budget constraints in allocating the necessary resources
(manpower, funds, etc.) for development of a quality metrics
system and its regular application.
• Human factors, especially opposition of employees to evaluation
of their activities.
•   Uncertainty regarding the data’s validity, rooted in partial and
biased reporting.
The main factors affecting development process parameters
********** 2 **********
--- page 3 ---
• Programming style: strongly affects software volume, where
“wasteful” coding may double the volume of produced code
(KLOC).
• Volume of documentation comments included in the code: affects
volume of the code.
•   Software complexity
•   Percentage of reused code
•   Professionalism and thoroughness of design review and software
testing teams
•   Reporting style of the review and testing results
Relevant 5 points: 5 Marks
Q2.A.   .   BL M   CO-3   10
Solution-   5
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality   Tests internal logic
Definition without knowing internal and structure of
code   code
Control flow, paths,
Focus   Inputs and outputs
conditions
Requires
Knowledge No programming
programming
Required   knowledge
knowledge
Testing   System, acceptance   Unit, integration
Level   testing   testing
Equivalence partitioning, Path testing, loop
Techniques
BVA   testing
Validate functional   Ensure code
Objective
requirements   correctness
Error   Missing/incorrect   Logical errors, dead
Detection   functions   code
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
********** 3 **********
--- page 4 ---
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
********** 4 **********
--- page 5 ---
Correct user-facing results
Q2. B.   Explain the various user difficulties caused due to lack of proper quality BL   L   CO-4   10
assurance maintenance activities, how these difficulties affect user   2
experience and system usability.
Relevant 5 points: 10 Marks
• Code failure (usually termed “software failure”).
• Documentation failure in the user’s manual, help screens or
other form of documentation prepared for the user. In this case,
the support service can provide the user with correct instructions
(although no correction of the software documentation itself is
performed).
•   Incomplete, vague or imprecise documentation.
•   User’s insufficient knowledge of the software system or his or
her failure to use the documentation supplied. In
these situations no software system failure is encountered.
Q3.A.   BL2 M   CO-4   10
Describe the SQA standards, system certification, and assessment
components.
Why is certification critical and what standards/processes are involved?
Solution:
1 Overview of Standards in SQA
SQA standards are documented agreements containing technical
specifications or precise criteria used consistently as guidelines to ensure
materials, products, processes, and services are fit for their purpose. In
software engineering, standards provide a common language and
benchmark for quality across organizations and industries.
2 ISO 9001 in SQA
ISO 9001 is a generic quality management standard applicable to any
industry, including software. It requires organizations to define
processes, measure performance, and continually improve. Software
organizations use ISO 9001 as a foundation for demonstrating that their
development processes are managed and consistent.
3 ISO 9000-3
ISO 9000-3 is specifically tailored guidance for applying ISO 9001 to
software development. It provides interpretations of ISO 9001 clauses in
the context of software, covering areas like design control, product
identification, and testing.
4 CMM and CMMI
The Capability Maturity Model (CMM) and its successor CMMI (Capability
Maturity Model Integration) define five maturity levels (Initial, Managed,
********** 5 **********
--- page 6 ---
Defined, Quantitatively Managed, Optimizing) that measure the maturity
of an organization's software development processes. CMMI is widely
used as both an internal
improvement roadmap and a certification benchmark for government
and defense contracts.
5
IEEE Standards
IEEE STD 12207 defines a framework for software lifecycle processes.
IEEE STD 1012 covers software verification and validation. IEEE STD 1028
covers software reviews and audits. These standards provide prescriptive
guidance for specific SQA activities.
6
Why Certification Is Critical
Certification provides independent verification that an organization's
quality management system meets defined standards. It builds customer
trust, enables entry into regulated markets (healthcare, aerospace,
finance), reduces risk of liability, and drives internal process discipline.
Without certification, organizations have no external validation of their
quality claims.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
Q3. B.   BL4 H   CO-4   10
Prior to testing, a software module had 150 flaws. Thirty defects were
found after deployment, but 105 defects were eliminated during testing.
Calculate the Defect Removal Efficiency and discuss the efficacy of the
testing.
Formula (2 Marks)
DRE=Defects removed during testingTotal defects×100DRE =
\frac{\text{Defects removed during testing}}{\text{Total defects}} \times
100DRE=Total defectsDefects removed during testing×100
Data (1 Mark)
•   Total defects = 150
• Removed in testing = 105
•   Post-release = 30
Calculation (3 Marks)
DRE=105150×100=70%DRE = \frac{105}{150} \times 100 =
70\%DRE=150105×100=70%
Analysis (3 Marks)
• 70% → Moderate effectiveness
• 30 defects escaped → testing not fully effective
• Need stronger test cases
Conclusion (1 Mark)
Testing efficiency is average; improvement required.
********** 6 **********
--- page 7 ---
Q4. A.   BL3 M   CO-1   10
During software development, high complexity and lack of visibility make
it difficult to ensure quality. Explain how these challenges affect software
development and suggest ways to handle them effectively.
Effect of High Complexity
1. Difficult to understand and manage
Complex systems are harder to design, test, and maintain [3].
2. More chances of errors
Increased components and interactions lead to higher risk of
issues.
3. Testing becomes challenging
It is difficult to test all possible scenarios.
Effect of Lack of Visibility
1. Invisible product
Software cannot be physically seen, making it harder to detect
problems early.
2. Late detection of issues
Errors are often found only after execution.
3. Difficult monitoring of progress
Hard to track quality during development.
Ways to Handle These Challenges
1. Modular Design
Break the system into smaller, manageable parts.
2. Proper Documentation
Maintain clear design and requirement documents.
3. Regular Reviews
Conduct code and design reviews to detect issues early.
4. Use of SQA Practices
Apply systematic quality assurance throughout development [1].
5. Automated Tools
Use tools for testing and monitoring.
6. Effective Communication
Ensure coordination among teams to reduce complexity-related
issues [5].
Conclusion
High complexity and lack of visibility make quality assurance difficult, but
with proper design, processes, and tools, these challenges can be
effectively managed.
Q4. B.   BL1 L   CO-1   10
********** 7 **********
--- page 8 ---
Discuss product revision and product transition quality factors. Explain
their role in ensuring maintainability and adaptability of software.
Software quality models such as McCall’s model classify quality factors
into product revision and product transition to address maintenance and
adaptability.
1. Product Revision Quality Factors
These focus on ease of modification and maintenance of software:
1. Maintainability – Ease of identifying and fixing defects
2. Flexibility – Ability to modify software for new requirements
3. Testability – Ease of testing after changes These factors are
crucial for debugging, updating, and enhancing software
efficiently
Role in Maintainability
• Reduces effort and cost of bug fixing
•   Supports continuous improvement and upgrades
•   Ensures reliable performance after modifications
2. Product Transition Quality Factors
These focus on adapting software to new environments:
1. Portability – Ability to run on different platforms
2. Reusability – Components can be reused in other systems
3. Interoperability – Ability to interact with other systems
These factors ensure smooth migration and integration of software
Role in Adaptability
•   Enables deployment across multiple platforms
•   Supports integration with new technologies
•   Extends software lifespan and usability
Conclusion
Product revision factors ensure maintainability, while product transition
factors ensure adaptability, together enabling software to evolve, remain
efficient, and meet changing user and technological needs.
Q5. A   BL4 L   CO-2   10
Analyse the relationship between pre-project and lifecycle components in
SQA. How do gaps in pre-project planning cause quality failures during
development? Justify with examples.
The Relationship Between Pre-Project and Lifecycle Components
Pre-project and lifecycle components in SQA form a cause-and-effect
chain. Pre-project components establish the quality framework
- objectives, standards, plans, and risk assessments. Lifecycle components
execute within that framework. When
********** 8 **********
--- page 9 ---
the framework is weak or missing, lifecycle components operate without
direction, leading to inconsistent quality outcomes.
2
The Cost of Defects Across Phases (Boehm's Rule)
Barry Boehm's research established that the cost of fixing a defect
increases exponentially as it progresses through the lifecycle. A defect
introduced in requirements costs 1x to fix in requirements, 5x in design,
10x in coding, 20x in testing, and 200x in production. Pre-project SQA
components exist to establish the controls that catch defects at the
cheapest possible stage.
3
Gap 1: Missing or Vague Quality Objectives
When pre-project components fail to define clear quality objectives,
lifecycle teams have no measurable target. Example: A government portal
project with no defined performance benchmarks resulted in a system
that met functional requirements but crashed under peak load - a defect
that was never part of the test plan because it was not a defined
quality objective.
4
Gap 2: No Standards Selected Pre-Project
Without pre-project standards selection, each team member applies their
own interpretation of quality. Example: In a multinational software
project, the absence of a pre-agreed coding standard meant that teams
from different countries wrote code with incompatible naming
conventions and error-handling patterns, creating thousands of
integration defects.
5
Gap 3: Inadequate Risk Assessment
Pre-project risk assessment should identify which components carry the
highest quality risk and allocate QA resources accordingly. When this is
skipped, high-risk areas receive the same QA attention as low-risk areas.
Example: The original Healthcare.gov launch failed partly because no pre-
project risk assessment identified
the system integration complexity as a critical quality risk, leading to
under-tested interfaces that failed under real-world load.
6
Conclusion: Pre-Project as Quality Foundation
The analysis shows that pre-project SQA components are not optional
overhead - they are the foundation upon which the entire quality edifice
rests. Lifecycle components cannot compensate for a missing or weak
pre-project framework. Organizations that invest in thorough pre-project
quality planning consistently achieve lower defect rates and higher
delivery predictability.
Marking : Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
********** 9 **********
--- page 10 ---
Q5. B.   BL5 H   CO-3   10
Assess how well defect-removal techniques like testing, inspections, and
reviews improve the overall quality of software.
Introduction (2 Marks)
Defect removal techniques such as testing, inspections, and reviews are
critical to achieving high software quality.
Technique-wise Evaluation (4 Marks)
Technique   Strength
Testing   Detects runtime errors
Inspections   Finds logical/design flaws early
Reviews   Improves requirement clarity
Comparative Analysis (2 Marks)
• Reviews → Early stage, low cost
•   Inspections → Detailed, systematic
•   Testing → Late stage, higher cost
Impact on Quality (1.5 Marks)
• Reduces defect density
• Improves reliability
• Enhances maintainability
Conclusion (0.5 Mark)
Combined use of all techniques ensures maximum defect removal
efficiency.
Q6. A.   Solution-   BL1 L   CO-3   10
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality without   Tests internal logic and
Definition
knowing internal code   structure of code
Control flow, paths,
Focus   Inputs and outputs
conditions
Knowledge   Requires programming
No programming knowledge
Required   knowledge
Testing Level System, acceptance testing   Unit, integration testing
Techniques   Equivalence partitioning, BVA Path testing, loop testing
Validate functional
Objective   Ensure code correctness
requirements
********** 10 **********
--- page 11 ---
Error
Missing/incorrect functions   Logical errors, dead code
Detection
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
********** 11 **********
--- page 12 ---
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
Correct user-facing results
Q6. B.   BL4 M   CO-4   10
Analyze the role of pre-maintenance software quality components in
ensuring effective software maintenance. How do these components
influence long-term system reliability?
Maintenance contract review:
• Customer requirements clarification
• Review of alternative approaches to maintenance provision
• Review of estimates of required maintenance resources
• Review of maintenance services to be provided by subcontractors
and/or the customer
• Review of maintenance costs estimates
Maintenance plan
• A list of the contracted maintenance services (external and
internal customers)
• A description of the maintenance team's organization
• A list of maintenance facilities
• A list of identified maintenance service risks
• A list of required software maintenance procedures and controls
• The software maintenance budget
Q7.A.   BL4 M   CO-4   10
An organization wants to evaluate its software processes
and identify improvement areas:
Explain how a software process assessment (SPICE / ISO 15504) can be
conducted and how the results can be used for process improvement.
Solution:
Answer:
• Conduct process assessment (SPICE / ISO 15504)
•   Evaluate current processes against standard models
•   Identify strengths and weaknesses
********** 12 **********
--- page 13 ---
•   Assign process capability/maturity levels
• Document findings and gaps
• Implement process improvement actions
• Monitor and reassess for continuous improvement
Rubric:
•   Understanding of process assessment : 2 marks
•   Evaluation against standards : 2 marks
•   Identification of gaps : 2 marks
• Improvement actions : 3 marks
•   Clarity / conclusion : 1 mark
Q7.B.   BL1 L   CO-4   10
Explain classification of software quality metrics.
Rubric (10 Marks)
•   Introduction / definition of software metrics → 2 marks
o Clear definition (1 mark)
o Purpose / role (1 mark)
•   Process metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
•   Product metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
Alternate Strict Evaluation (if needed)
•   Definition missing → deduct 1–2 marks
• No examples → deduct up to 2 marks
•   Only one type explained → max 5 marks
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 710f898ca314

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   BL DL Course Marks
outcome
Q1. a   BL1 L   CO-1   5
List the different types of issues in software such as errors, faults, and
failures, and briefly explain their meaning and impact on software
quality.
Solution:
Relevant points: 5 Marks
1. Error (Human Mistake)
An error is a mistake made by a developer, such as wrong logic or
misunderstanding requirements.
Impact: Leads to problems in the system design or code.
2. Fault (Problem in Code)
A fault is the incorrect code or design caused by an error.
Impact: It exists in the system and may cause
incorrect behavior when executed.
3. Failure (System Not Working as Expected)
A failure occurs when the system does not perform as expected
during execution.
Impact: Directly affects users and reduces system reliability.
Q1.b   BL2 M   CO-1   5
********** 1 **********
--- page 2 ---
During requirement analysis, a team maps user needs to quality
attributes.
Explain the need for a comprehensive definition of requirements that will
helps in this process.
Relevant 5 points: 5 Marks
• Need for improving poor requirements documents is well-
known!!
•   Frequently lack quality factors such as: usability, reusability,
maintainability.
•   Software industry groups the long list of related attributes into
what we call quality factors. (Sometimes non-functional
requirements)
• Unequal highlighting on all quality factors.
• Emphasis varies from project to project
o   Scalability; maintainability; reliability; portability; etc.
Need for a comprehensive definition of requirements that will cover all
attributes of software
Q1.c   BL   L   CO-2   5
Apply IEEE 1012 standard concepts to a software project and explain how 3
they help in ensuring effective verification and validation.
Answer:
•   Defines verification and validation processes
•   Ensures software meets requirements
•   Applied throughout lifecycle
• Improves reliability and correctness
•   Supports quality assurance
Rubric:
•   Definition: 2 marks
•   Purpose: 2 marks
•   Benefit: 1 mark
Q1.d   BL H   CO-3   5
4
Analyze the limitations of software quality metrics and explain how these
limitations can impact the evaluation of software quality.
• Budget constraints in allocating the necessary resources
(manpower, funds, etc.) for development of a quality metrics
system and its regular application.
• Human factors, especially opposition of employees to evaluation
of their activities.
•   Uncertainty regarding the data’s validity, rooted in partial and
biased reporting.
The main factors affecting development process parameters
********** 2 **********
--- page 3 ---
• Programming style: strongly affects software volume, where
“wasteful” coding may double the volume of produced code
(KLOC).
• Volume of documentation comments included in the code: affects
volume of the code.
•   Software complexity
•   Percentage of reused code
•   Professionalism and thoroughness of design review and software
testing teams
•   Reporting style of the review and testing results
Relevant 5 points: 5 Marks
Q2.A.   .   BL M   CO-3   10
Solution-   5
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality   Tests internal logic
Definition without knowing internal and structure of
code   code
Control flow, paths,
Focus   Inputs and outputs
conditions
Requires
Knowledge No programming
programming
Required   knowledge
knowledge
Testing   System, acceptance   Unit, integration
Level   testing   testing
Equivalence partitioning, Path testing, loop
Techniques
BVA   testing
Validate functional   Ensure code
Objective
requirements   correctness
Error   Missing/incorrect   Logical errors, dead
Detection   functions   code
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
********** 3 **********
--- page 4 ---
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
********** 4 **********
--- page 5 ---
Correct user-facing results
Q2. B.   Explain the various user difficulties caused due to lack of proper quality BL   L   CO-4   10
assurance maintenance activities, how these difficulties affect user   2
experience and system usability.
Relevant 5 points: 10 Marks
• Code failure (usually termed “software failure”).
• Documentation failure in the user’s manual, help screens or
other form of documentation prepared for the user. In this case,
the support service can provide the user with correct instructions
(although no correction of the software documentation itself is
performed).
•   Incomplete, vague or imprecise documentation.
•   User’s insufficient knowledge of the software system or his or
her failure to use the documentation supplied. In
these situations no software system failure is encountered.
Q3.A.   BL2 M   CO-4   10
Describe the SQA standards, system certification, and assessment
components.
Why is certification critical and what standards/processes are involved?
Solution:
1 Overview of Standards in SQA
SQA standards are documented agreements containing technical
specifications or precise criteria used consistently as guidelines to ensure
materials, products, processes, and services are fit for their purpose. In
software engineering, standards provide a common language and
benchmark for quality across organizations and industries.
2 ISO 9001 in SQA
ISO 9001 is a generic quality management standard applicable to any
industry, including software. It requires organizations to define
processes, measure performance, and continually improve. Software
organizations use ISO 9001 as a foundation for demonstrating that their
development processes are managed and consistent.
3 ISO 9000-3
ISO 9000-3 is specifically tailored guidance for applying ISO 9001 to
software development. It provides interpretations of ISO 9001 clauses in
the context of software, covering areas like design control, product
identification, and testing.
4 CMM and CMMI
The Capability Maturity Model (CMM) and its successor CMMI (Capability
Maturity Model Integration) define five maturity levels (Initial, Managed,
********** 5 **********
--- page 6 ---
Defined, Quantitatively Managed, Optimizing) that measure the maturity
of an organization's software development processes. CMMI is widely
used as both an internal
improvement roadmap and a certification benchmark for government
and defense contracts.
5
IEEE Standards
IEEE STD 12207 defines a framework for software lifecycle processes.
IEEE STD 1012 covers software verification and validation. IEEE STD 1028
covers software reviews and audits. These standards provide prescriptive
guidance for specific SQA activities.
6
Why Certification Is Critical
Certification provides independent verification that an organization's
quality management system meets defined standards. It builds customer
trust, enables entry into regulated markets (healthcare, aerospace,
finance), reduces risk of liability, and drives internal process discipline.
Without certification, organizations have no external validation of their
quality claims.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
Q3. B.   BL4 H   CO-4   10
Prior to testing, a software module had 150 flaws. Thirty defects were
found after deployment, but 105 defects were eliminated during testing.
Calculate the Defect Removal Efficiency and discuss the efficacy of the
testing.
Formula (2 Marks)
DRE=Defects removed during testingTotal defects×100DRE =
\frac{\text{Defects removed during testing}}{\text{Total defects}} \times
100DRE=Total defectsDefects removed during testing×100
Data (1 Mark)
•   Total defects = 150
• Removed in testing = 105
•   Post-release = 30
Calculation (3 Marks)
DRE=105150×100=70%DRE = \frac{105}{150} \times 100 =
70\%DRE=150105×100=70%
Analysis (3 Marks)
• 70% → Moderate effectiveness
• 30 defects escaped → testing not fully effective
• Need stronger test cases
Conclusion (1 Mark)
Testing efficiency is average; improvement required.
********** 6 **********
--- page 7 ---
Q4. A.   BL3 M   CO-1   10
During software development, high complexity and lack of visibility make
it difficult to ensure quality. Explain how these challenges affect software
development and suggest ways to handle them effectively.
Effect of High Complexity
1. Difficult to understand and manage
Complex systems are harder to design, test, and maintain [3].
2. More chances of errors
Increased components and interactions lead to higher risk of
issues.
3. Testing becomes challenging
It is difficult to test all possible scenarios.
Effect of Lack of Visibility
1. Invisible product
Software cannot be physically seen, making it harder to detect
problems early.
2. Late detection of issues
Errors are often found only after execution.
3. Difficult monitoring of progress
Hard to track quality during development.
Ways to Handle These Challenges
1. Modular Design
Break the system into smaller, manageable parts.
2. Proper Documentation
Maintain clear design and requirement documents.
3. Regular Reviews
Conduct code and design reviews to detect issues early.
4. Use of SQA Practices
Apply systematic quality assurance throughout development [1].
5. Automated Tools
Use tools for testing and monitoring.
6. Effective Communication
Ensure coordination among teams to reduce complexity-related
issues [5].
Conclusion
High complexity and lack of visibility make quality assurance difficult, but
with proper design, processes, and tools, these challenges can be
effectively managed.
Q4. B.   BL1 L   CO-1   10
********** 7 **********
--- page 8 ---
Discuss product revision and product transition quality factors. Explain
their role in ensuring maintainability and adaptability of software.
Software quality models such as McCall’s model classify quality factors
into product revision and product transition to address maintenance and
adaptability.
1. Product Revision Quality Factors
These focus on ease of modification and maintenance of software:
1. Maintainability – Ease of identifying and fixing defects
2. Flexibility – Ability to modify software for new requirements
3. Testability – Ease of testing after changes These factors are
crucial for debugging, updating, and enhancing software
efficiently
Role in Maintainability
• Reduces effort and cost of bug fixing
•   Supports continuous improvement and upgrades
•   Ensures reliable performance after modifications
2. Product Transition Quality Factors
These focus on adapting software to new environments:
1. Portability – Ability to run on different platforms
2. Reusability – Components can be reused in other systems
3. Interoperability – Ability to interact with other systems
These factors ensure smooth migration and integration of software
Role in Adaptability
•   Enables deployment across multiple platforms
•   Supports integration with new technologies
•   Extends software lifespan and usability
Conclusion
Product revision factors ensure maintainability, while product transition
factors ensure adaptability, together enabling software to evolve, remain
efficient, and meet changing user and technological needs.
Q5. A   BL4 L   CO-2   10
Analyse the relationship between pre-project and lifecycle components in
SQA. How do gaps in pre-project planning cause quality failures during
development? Justify with examples.
The Relationship Between Pre-Project and Lifecycle Components
Pre-project and lifecycle components in SQA form a cause-and-effect
chain. Pre-project components establish the quality framework
- objectives, standards, plans, and risk assessments. Lifecycle components
execute within that framework. When
********** 8 **********
--- page 9 ---
the framework is weak or missing, lifecycle components operate without
direction, leading to inconsistent quality outcomes.
2
The Cost of Defects Across Phases (Boehm's Rule)
Barry Boehm's research established that the cost of fixing a defect
increases exponentially as it progresses through the lifecycle. A defect
introduced in requirements costs 1x to fix in requirements, 5x in design,
10x in coding, 20x in testing, and 200x in production. Pre-project SQA
components exist to establish the controls that catch defects at the
cheapest possible stage.
3
Gap 1: Missing or Vague Quality Objectives
When pre-project components fail to define clear quality objectives,
lifecycle teams have no measurable target. Example: A government portal
project with no defined performance benchmarks resulted in a system
that met functional requirements but crashed under peak load - a defect
that was never part of the test plan because it was not a defined
quality objective.
4
Gap 2: No Standards Selected Pre-Project
Without pre-project standards selection, each team member applies their
own interpretation of quality. Example: In a multinational software
project, the absence of a pre-agreed coding standard meant that teams
from different countries wrote code with incompatible naming
conventions and error-handling patterns, creating thousands of
integration defects.
5
Gap 3: Inadequate Risk Assessment
Pre-project risk assessment should identify which components carry the
highest quality risk and allocate QA resources accordingly. When this is
skipped, high-risk areas receive the same QA attention as low-risk areas.
Example: The original Healthcare.gov launch failed partly because no pre-
project risk assessment identified
the system integration complexity as a critical quality risk, leading to
under-tested interfaces that failed under real-world load.
6
Conclusion: Pre-Project as Quality Foundation
The analysis shows that pre-project SQA components are not optional
overhead - they are the foundation upon which the entire quality edifice
rests. Lifecycle components cannot compensate for a missing or weak
pre-project framework. Organizations that invest in thorough pre-project
quality planning consistently achieve lower defect rates and higher
delivery predictability.
Marking : Award 2 marks per key point (6 points x ~1.5-2 marks). Full
marks require accurate explanation of all major points with relevant
examples where applicable.
********** 9 **********
--- page 10 ---
Q5. B.   BL5 H   CO-3   10
Assess how well defect-removal techniques like testing, inspections, and
reviews improve the overall quality of software.
Introduction (2 Marks)
Defect removal techniques such as testing, inspections, and reviews are
critical to achieving high software quality.
Technique-wise Evaluation (4 Marks)
Technique   Strength
Testing   Detects runtime errors
Inspections   Finds logical/design flaws early
Reviews   Improves requirement clarity
Comparative Analysis (2 Marks)
• Reviews → Early stage, low cost
•   Inspections → Detailed, systematic
•   Testing → Late stage, higher cost
Impact on Quality (1.5 Marks)
• Reduces defect density
• Improves reliability
• Enhances maintainability
Conclusion (0.5 Mark)
Combined use of all techniques ensures maximum defect removal
efficiency.
Q6. A.   Solution-   BL1 L   CO-3   10
5 mark for comparison, and 5 marks for test a program schedule
Software testing is broadly classified into black-box testing and white-box
testing, based on whether the internal structure of the program is
considered. Both approaches are essential for ensuring complete
software quality.
Aspect   Black-Box Testing   White-Box Testing
Tests functionality without   Tests internal logic and
Definition
knowing internal code   structure of code
Control flow, paths,
Focus   Inputs and outputs
conditions
Knowledge   Requires programming
No programming knowledge
Required   knowledge
Testing Level System, acceptance testing   Unit, integration testing
Techniques   Equivalence partitioning, BVA Path testing, loop testing
Validate functional
Objective   Ensure code correctness
requirements
********** 10 **********
--- page 11 ---
Error
Missing/incorrect functions   Logical errors, dead code
Detection
Use of Both Models Together (Combined Approach)
In real-world testing, both models are used complementarily to achieve
complete coverage.
Step-wise Use in Program Testing Schedule
Unit Testing (White-Box)
• Performed by developers
•   Tests:
o   Internal logic
o Code paths
o Conditions
Ensures each module works correctly internally
Integration Testing (White-Box + Black-Box)
• Combines modules
•   White-box: checks internal interactions
•   Black-box: verifies input-output between modules
Ensures modules interact correctly
System Testing (Black-Box)
•   Entire system is tested
•   Focus on:
o Functional requirements
o Performance
o User expectations
Ensures system meets requirements
Acceptance Testing (Black-Box)
• Performed by users/clients
•   Validates:
o Business requirements
o Real-world usage
Ensures customer satisfaction
Both Are Needed Together:-
Complementary Nature
•   Black-box → tests what system does
• White-box → tests how system works
Improved Coverage
• White-box ensures code coverage
•   Black-box ensures requirement coverage
Better Defect Detection
•   Logical errors → detected by white-box
•   Functional errors → detected by black-box
Example (Program Schedule)
********** 11 **********
--- page 12 ---
Consider a banking application:
• White-box testing:
o Check interest calculation logic
o   Verify loops and conditions
•   Black-box testing:
o   Input: deposit amount
o Output: updated balance
Together they ensure:
•   Correct internal processing
Correct user-facing results
Q6. B.   BL4 M   CO-4   10
Analyze the role of pre-maintenance software quality components in
ensuring effective software maintenance. How do these components
influence long-term system reliability?
Maintenance contract review:
• Customer requirements clarification
• Review of alternative approaches to maintenance provision
• Review of estimates of required maintenance resources
• Review of maintenance services to be provided by subcontractors
and/or the customer
• Review of maintenance costs estimates
Maintenance plan
• A list of the contracted maintenance services (external and
internal customers)
• A description of the maintenance team's organization
• A list of maintenance facilities
• A list of identified maintenance service risks
• A list of required software maintenance procedures and controls
• The software maintenance budget
Q7.A.   BL4 M   CO-4   10
An organization wants to evaluate its software processes
and identify improvement areas:
Explain how a software process assessment (SPICE / ISO 15504) can be
conducted and how the results can be used for process improvement.
Solution:
Answer:
• Conduct process assessment (SPICE / ISO 15504)
•   Evaluate current processes against standard models
•   Identify strengths and weaknesses
********** 12 **********
--- page 13 ---
•   Assign process capability/maturity levels
• Document findings and gaps
• Implement process improvement actions
• Monitor and reassess for continuous improvement
Rubric:
•   Understanding of process assessment : 2 marks
•   Evaluation against standards : 2 marks
•   Identification of gaps : 2 marks
• Improvement actions : 3 marks
•   Clarity / conclusion : 1 mark
Q7.B.   BL1 L   CO-4   10
Explain classification of software quality metrics.
Rubric (10 Marks)
•   Introduction / definition of software metrics → 2 marks
o Clear definition (1 mark)
o Purpose / role (1 mark)
•   Process metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
•   Product metrics → 4 marks
o Explanation (2 marks)
o At least 2 relevant examples (2 marks)
Alternate Strict Evaluation (if needed)
•   Definition missing → deduct 1–2 marks
• No examples → deduct up to 2 marks
•   Only one type explained → max 5 marks
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper c53530a14958

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   Module   Marks
Q1. A   Explain how unexpected program behaviour is related to differences from 5
CO-1;   the expected system performance, with examples.
BL1
Solution:
Unexpected program behaviour means the software is not working the way
it was supposed to. This shows a difference between expected
performance (what we want) and actual performance (what happens).
Relationship Between the Two
• Expected Performance:
How the system should behave according to requirements.
Example: A login system should allow valid users to log in.
• Unexpected Behavior:
When the system does something wrong or different.
Example: A valid user cannot log in even with the correct password.
This difference shows that there is a problem in the system.
Examples
1. Login System
o Expected: User logs in successfully with correct details
********** 1 **********
--- page 2 ---
o Actual: Login fails
→ Indicates an issue in authentication logic
2. Banking Application
o Expected: Correct balance is displayed
o Actual: Wrong balance is shown
→ Shows calculation or data error
3. E-commerce Website
o Expected: Order is placed after payment
o Actual: Payment is deducted but order not confirmed
→ Indicates system failure or transaction issue
Conclusion
Whenever a program behaves unexpectedly, it means the system is not
meeting its expected performance. This gap helps identify problems that
need to be fixed.
Q1.b   5
CO-1;   A software system is frequently updated to fix bugs and improve features.
BL2   Explain how product revision quality factors support such activities.
When a software system is frequently updated to fix bugs and enhance
features, the effectiveness of these activities depends on Product Revision
Quality Factors defined in McCall’s Quality Model.
These factors focus on how easily the software can be modified, tested, and
improved.
Product Revision Quality Factors and Their Role
1. Maintainability
Meaning: Ease with which software can be corrected or updated.
Support in this scenario:
• Enables quick bug fixing and issue resolution
• Reduces time and effort required for updates
• Makes code easier to understand and modify
Without maintainability, frequent updates become costly and error-prone.
2. Flexibility
Meaning: Ability of the software to adapt to changes or new requirements.
********** 2 **********
--- page 3 ---
Support in this scenario:
• Allows developers to add new features smoothly
• Supports evolving user needs and business requirements
• Reduces the risk of breaking existing functionality
Ensures the system can grow without major redesign.
3. Testability
Meaning: Ease with which software can be tested after modifications.
Support in this scenario:
• Helps verify that bug fixes and new features work correctly
• Enables faster and more effective testing processes
• Supports automation and regression testing
Prevents introduction of new defects during updates.
Conclusion
Product   revision   quality   factors—maintainability,   flexibility, and
testability—are essential for systems that undergo frequent updates. They
ensure that:
• Changes are implemented efficiently
• New features are integrated smoothly
• Software quality is maintained over time
Thus, these factors play a crucial role in continuous improvement and long-
term sustainability of software systems.
Q1.c   5
CO-   Explain the significance of CMMI in improving software development
2;BL 3   processes.
Answer:
• Provides structured framework for process improvement
• Defines maturity levels
• Helps in reducing defects
• Improves productivity and efficiency
• Enables continuous process improvement
Rubric:
• Concept: 2 marks
•   Significance: 2 marks
********** 3 **********
--- page 4 ---
• Outcome: 1 mark
Q1.d   5
CO-   Analyse product metrics and explain how they are used to evaluate the
3;BL 4   quality of a software product.
Solution:
Product metrics are measures used to evaluate the quality and
performance of a software product.
Analysis of Product Metrics
Product metrics help in understanding how good the software is by
measuring different aspects such as:
1. Size Metrics
o Measure the size of the software (e.g., lines of code)
o Helps estimate complexity and development effort
2. Complexity Metrics
o Measure how complicated the code is
o Example: Cyclomatic complexity
o Higher complexity means higher chances of errors
3. Quality Metrics
o Measure reliability, correctness, and performance
o Example: Number of defects, failure rate
4. Performance Metrics
o Measure how efficiently the system works
o Example: Response time, speed, memory usage
How They Evaluate Software Quality
• Help identify problem areas in the software
• Make it easier to improve performance and reliability
• Provide a quantitative way to compare different products
• Support better decision-making during development and
maintenance
Conclusion
********** 4 **********
--- page 5 ---
Product metrics are important for analyzing and improving software quality,
as they provide measurable data about the system’s performance,
complexity, and reliability.
Q2. A.   10
CO-   Explain the classification of software testing based on:
3;BL 5   a) Testing concepts
b) Requirements classification
Solution-
Marking 5 for testing and 5 for requirement classification
Software test classification
• Software tests may be classified according to the testing concept or
to the requirements classification in effect.
•   Classification according to testing concept:
• Black box (functionality) testing
• White box (structural) testing
Black box and white box testing – IEEE definitions
•   Black box testing:
• Def. 1: Testing that ignores the internal mechanism of a
system or component and focuses solely on the outputs
generated in response to selected inputs and execution
conditions.
• Def. 2: Testing conducted to evaluate the compliance of a
system or component with specified functional requirements.
• White box testing:
• Def. 1: Testing that takes into account the internal
mechanism of a system or component.
• Realization of the white box testing concept requires
verification of every program statement and comment.
• White box testing enables performance of data processing
and calculations correctness tests, software qualification
tests, maintainability tests and reusability tests.
Classification according to requirements
McCall’s classic model for classification of software quality requirements.
• The model has been extended to the classification of the
tests carried out to ensure full coverage of the respective
requirements.
• The requirements and their corresponding tests are shown in Table.
********** 5 **********
--- page 6 ---
Q2. B.   10
CO-   What are the different components of software maintenance? What are the
4;BL 2   infrastructure tools that support maintenance in quality assurance?
********** 6 **********
--- page 7 ---
Components of Software Maintenance
Software maintenance refers to modifications made to a software system
after delivery to keep it useful and efficient.
Main Components / Types of Maintenance
1. Corrective Maintenance
a. Fixes defects or bugs found after deployment.
b. Example: Resolving system crashes or incorrect outputs.
2. Adaptive Maintenance
a. Updates software to work in a changed environment.
b. Example: Modifying software for new OS, hardware, or
regulations.
3. Perfective Maintenance
a. Enhances performance or adds new features based on user
feedback.
b. Example: Improving UI or adding new functionality.
4. Preventive Maintenance
a. Improves maintainability to prevent future issues.
b. Example: Code refactoring, documentation updates.
2. Infrastructure Tools Supporting Maintenance in SQA
Infrastructure tools help ensure that maintenance activities maintain or
improve software quality.
1. Configuration Management Tools
• Track and control changes in software.
• Maintain version history and prevent conflicts.
• Example: Git, SVN.
2. Version Control Systems
• Manage multiple versions of software artifacts.
• Enable rollback and parallel development.
3. Bug Tracking / Issue Tracking Tools
• Record, track, and manage defects.
• Help prioritize and monitor resolution.
• Example: Jira, Bugzilla.
********** 7 **********
--- page 8 ---
4. Automated Testing Tools
• Re-run test cases after changes to ensure no new defects.
• Supports regression testing.
• Example: Selenium, JUnit.
5. Documentation Tools
• Maintain updated system documents.
• Help new developers understand system changes.
6. Reverse Engineering Tools
• Help understand legacy systems by analyzing code structure.
• Useful when documentation is missing.
7. Code Analysis Tools
• Detect code quality issues and vulnerabilities.
• Improve maintainability.
• Example: SonarQube.
8. Build and Deployment Tools
• Automate integration and deployment.
• Ensure consistency in updates.
• Example: Jenkins, Maven.
Conclusion
Software maintenance ensures long-term usability of software through
corrective, adaptive, perfective, and preventive actions. Infrastructure tools
in SQA support these activities by managing changes, detecting defects,
ensuring quality, and automating testing and deployment processes.
If you want, I can also convert this into a 5-mark / 10-mark structured
answer, or short notes format for exams.
Q3.A   10
CO-   Describe the software project lifecycle components in the context of SQA.
4;BL2   Explain how each phase contributes to maintaining software quality.
********** 8 **********
--- page 9 ---
Overview of Lifecycle Components in SQA
Software project lifecycle components in SQA refer to the quality assurance
activities embedded in each phase of the Software Development Life Cycle
(SDLC).
Rather than treating quality as a final checkpoint, SQA distributes quality
activities
across all phases to detect and remove defects as early as possible.
2 Requirements Phase
SQA in this phase involves requirements reviews and traceability matrix
creation.
The goal is to ensure requirements are complete, consistent, unambiguous,
and
testable. Missing or contradictory requirements at this stage are the most
expensive
defects to fix later. SQA activities include formal inspections and customer
walkthroughs.
3 Design Phase
Design reviews and architectural walkthroughs are the primary SQA activities
here.
Design defects - such as poor module coupling, missing error handling, or
scalability
flaws - are identified and corrected before coding begins. SQA ensures that
design
conforms to standards and quality objectives.
4 Coding Phase:
Code reviews, pair programming, static analysis, and adherence to coding
standards
are the SQA activities in this phase. Tools like SonarQube help identify code
smells,
security vulnerabilities, and maintainability issues automatically. SQA
ensures code
quality is verified continuously, not just at delivery.
5 Testing Phase
This phase is the most visible SQA activity. It includes unit, integration,
system, and
acceptance testing. Test plans, test cases, and traceability to requirements
are all SQA
artifacts. The goal is to verify that the software meets specified requirements
and
performs reliably under expected and unexpected conditions.
6 Maintenance Phase
SQA in maintenance focuses on regression testing, change impact analysis,
and
defect tracking. Every change to a deployed system carries the risk of
introducing
new defects (regression). SQA ensures changes are reviewed, tested, and
documented appropriately to maintain the integrity of the system over time.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
********** 9 **********
--- page 10 ---
accurate explanation of all major points with relevant examples where
applicable
Q3. B.   Examine the SQA defect removal effectiveness model and describe how it 10
CO-   facilitates process improvement and methodical defect identification.
4;BL4
Introduction (2 Marks)
The SQA DRE model provides a structured framework to measure and
improve defect removal efficiency across development phases.
Model Components (3 Marks)
• Defect Injection Points: Where defects originate
• Detection Mechanisms: Reviews, testing, inspections
• Defect Tracking System: Logs and monitors defects
• Feedback Loop: Improves processes
Working of Model (3 Marks)
•   Identify defects at each stage
• Measure removal efficiency
• Compare planned vs actual defect removal
• Use feedback to refine processes
Process Improvement Role (1.5 Marks)
•   Identifies weak phases
• Improves testing strategies
• Enhances development practices
Conclusion (0.5 Mark)
The model ensures systematic defect identification and continuous
process improvement.
Q4. A.   10
CO-   A software development team frequently releases updates that introduce
1;BL3   new issues. Examine the root causes behind this recurring problem and
propose a structured approach to improve quality.
Solution:
********** 10 **********
--- page 11 ---
When a software team releases updates that keep introducing new
problems, it usually means there are issues in the development and quality
process.
Possible Reasons (Root Causes)
1. Inadequate Testing
o Updates are not properly tested before release
o Some errors remain undetected
2. Poor Requirement Understanding
o Developers may misunderstand what needs to be built
3. Lack of Regression Testing
o Fixing one issue creates new problems in other parts of the
system
4. Time Pressure / Deadlines
o Rushed development leads to careless mistakes
5. Poor Communication
o Teams working on different modules are not well coordinated
6. Weak Quality Assurance Practices
o No proper review or quality checks before release
Step-by-Step Approach to Improve Quality
1. Clear Requirement Analysis
o Ensure all team members understand the requirements
correctly
2. Implement Proper Testing
o Perform unit testing, integration testing, and system testing
3. Use Regression Testing
o Test the whole system after every update to avoid new issues
4. Code Reviews
o Review code regularly to catch mistakes early
5. Improve Communication
o Ensure proper coordination between teams
6. Use Version Control and CI/CD Tools
o Automate testing and deployment for better consistency
7. Allocate Sufficient Time
o Avoid rushing releases; focus on quality over speed
Q4. B.   10
CO-   Describe how software requirements are classified into software quality
1;BL1   factors. Discuss the benefits of such classification in quality assurance.
********** 11 **********
--- page 12 ---
Classification of Software Requirements into Quality Factors
Software requirements are broadly divided into:
• Functional Requirements – what the system should do
• Non-Functional Requirements (Quality Requirements) – how well
the system should perform
These non-functional requirements are classified into software quality
factors, commonly structured using models like McCall’s Quality Model.
Classification into Quality Factors
A. Product Operation Factors (Run-time behavior)
These define how the system performs during execution:
•   Reliability – consistent and error-free operation
•   Efficiency – optimal use of resources and fast response
• Usability – ease of use and user-friendliness
•   Integrity (Security) – protection against unauthorized access
• Correctness – accuracy of outputs
B. Product Revision Factors (Maintenance aspects)
These define how easily the system can be modified:
• Maintainability – ease of fixing defects
•   Flexibility – ease of adapting to changes
•   Testability – ease of testing the system
C. Product Transition Factors (Adaptability aspects)
These define how well the system adapts to new environments:
•   Portability – ability to run on different platforms
• Reusability – components can be reused
• Interoperability – ability to interact with other systems
Thus, software requirements are systematically mapped into quality factors
to ensure all aspects of software quality are addressed.
********** 12 **********
--- page 13 ---
Q5. A   10
CO-   Analyze the infrastructure components for error prevention and
2;BL4   improvement. Compare with management SQA components and evaluate
their relative impact on defect reduction.
Infrastructure Components Defined
Infrastructure components for error prevention include all the tools,
environments,
processes, and technical mechanisms that reduce the probability of defects
being
introduced. They form the technical backbone of SQA - the systems within
which
quality work is performed.
2 Key Infrastructure Elements
Configuration Management Systems (e.g., Git, SVN) prevent unauthorized
code
changes and version conflicts. Defect Tracking Systems (e.g., Jira, Bugzilla)
ensure
defects are systematically recorded and resolved. Automated build and
CI/CD
pipelines catch integration errors instantly. Coding standards and linting
tools
prevent common programming errors at the point of writing.
3 Management SQA Components Defined
Management components include project planning, resource allocation,
quality
audits, process compliance monitoring, and corrective action management.
They
provide the organizational authority and oversight that ensures SQA
activities are
actually carried out according to plan.
4 Comparative Analysis
Infrastructure components are preventive and automated - they stop defects
from
entering the system. Management components are directive and supervisory
- they
ensure the right processes are followed. Both are essential, but they operate
at
different levels: infrastructure at the technical level, management at the
organizational level.
5 Which Has Greater Impact on Defect Reduction?
Research and industry data suggest that infrastructure components,
particularly
CI/CD pipelines and automated testing, deliver more measurable and
consistent
defect reduction. Automated checks catch defects within seconds of code
commit,
while management oversight operates on a slower cycle. However, without
management enforcing the use of infrastructure tools, adoption falls and
********** 13 **********
--- page 14 ---
effectiveness drops. The conclusion is that infrastructure enables defect
prevention,
but management sustains it.
6 Real-World Evidence
Companies like Google and Microsoft report that continuous integration
combined
with automated test suites catches over 80% of defects before code review.
This
demonstrates the primacy of infrastructure components in large-scale defect
reduction, though management oversight is critical for long-term process
improvement.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
accurate explanation of all major points with relevant examples where
applicable
Q5. B.   10
CO-
3;BL5   A software organization spends the following costs:
• Prevention Cost: ₹40,000
• Appraisal Cost: ₹25,000
•   Internal Failure Cost: ₹20,000
• External Failure Cost: ₹15,000
Determine the Total Cost of Quality and assess if the company is making
enough preventative investments. (CO4; PO5; BL5)
Formula (2 Marks)
CoQ=Prevention+Appraisal+Internal+ExternalCoQ = Prevention +
Appraisal + Internal +
ExternalCoQ=Prevention+Appraisal+Internal+External
Calculation (3 Marks)
CoQ=40000+25000+20000+15000=₹100000CoQ = 40000 + 25000 + 20000
+ 15000 = ₹100000CoQ=40000+25000+20000+15000=₹100000
Analysis (4 Marks)
• Prevention (40%) → good investment
• External failure low → positive sign
• Balanced cost distribution
Conclusion (1 Mark)
Company is investing adequately in prevention.
********** 14 **********
--- page 15 ---
Q6. A.   10
CO-   Describe the software testing process. What are the different stages involved
3;BL1   in testing? Explain each stage with appropriate details.
Solution:
Marking each step of explanation requires 2 marks and Diagram for 2
marks,
Planning, design and performance of testing are carried out throughout the
software development process.
Determine the test methodology:
• The testing strategy: should a big bang or incremental testing
strategy be adopted? If incremental testing is preferable,
should testing be performed bottom-up or top-down?
• Which parts of the testing plan should be performed
according to the white box testing model?
• Which parts of the testing plan should be performed
according to the automated testing model?
Planning the test:
 The tests to be planned include:
 Unit tests
 Integration tests
 System tests.
• While unit tests deal with small units of
software or modules, integration tests deal
with several units that combine into a
subsystem. System tests refer to the entire
software package/system.
Test design:
 The products of the test design stage are:
 Detailed design and procedures for each test
 Test case database/file
********** 15 **********
--- page 16 ---
 The test design is carried out on the basis of the software test
plan as documented by STP.
• Test implementation:
 The testing implementation phase activities consist of a series
of tests, corrections of detected errors
Q6. B.   10
CO-   What are the types of external participants? Explain their contributions.
4;BL4   What are the appropriate SQA tools appropriate for use with external
participants
External participants can be classified into three main groups:
(1) Subcontractors (currently called “outsourcing” organizations) that
undertake to carry out parts of a project, small or large, according to cir
cumstances. Subcontractors usually offer the contractor at least one of the
following benefits: staff availability, special expertise or low prices.
(2) Suppliers of COTS software and reused software modules. The advan
tages of integrating these ready elements are obvious, ranging from
timetable and cost reductions to quality. One expects that integration of
these ready-for-use elements will achieve savings in development resources,
a shorter timetable and higher quality software. Software of higher quality is
expected as these components have already been tested and corrected by
********** 16 **********
--- page 17 ---
the developers as well as corrected according to the faults identified by
previous customers. The characteristics of COTS software and quality
problems involved in their use are discussed by Basili and Boehm (2001).
(3) The customer themselves as participant in performing the project. It is
quite common for a customer to perform parts of the project: to apply the
customers’ special expertise, respond to commercial or other security needs,
keep internal development staff occupied, prevent future mainte nance
problems and so forth. This situation does have drawbacks in terms of the
customer–supplier relationship necessary for successful per formance of a
project, but they are overweighed by the inputs the customer makes. Hence,
the inevitability of this situation has become a standard element of many
software development projects and contrac tual relations.
The main benefits to the contractor of using external organizations are: ■
Overcoming shortages of professional staff by transferring parts of the
project to be carried out to firms employing staff having those skills. ■
Potentially shorter project schedules, achieved by purchasing COTS software
and reused software rather than developing the software. ■ Expertise
acquired in areas that need specialization through the participation of
owners– the subcontractor or the customer’s development department– of
that expertise. ■ Saved budget, achieved when subcontractorsoffer
pricesbelow those incurred by performing the project internally, and by the
use of COTS and reused software.
Marking scheme –
Each type of participants – 1.5 marks
Benefits – 2.5 marks
Q7. a.   10
CO-
4;BL4   Scenario: A mid-sized software company wants to obtain ISO 9000-3
certification.   They   currently   have   informal   processes,   minimal
documentation, and no formal audits.
Question:
As an SQA consultant, explain how the company should align its processes
with ISO 9000-3 requirements. Discuss key steps, challenges, and expected
benefits.
Answer:
• Adopt ISO 9000-3 standards for software processes
• Define and document quality management system (QMS)
• Standardize development procedures & documentation
• Conduct internal audits and reviews
********** 17 **********
--- page 18 ---
• Train staff on quality processes
• Ensure process consistency across teams
• Benefits: improved quality, customer trust, certification readiness
Rubric:
• Understanding of ISO 9000-3 : 2 marks
• QMS & documentation : 2 marks
• Process standardization : 2 marks
• Audits & training : 2 marks
• Benefits / conclusion : 2 marks
Q7. b.   Explain process metrics with suitable examples.   10
CO-
4;BL1   Answer:
• Process metrics measure efficiency of the software development
process
• Types:
 Defect metrics: DRE, defect arrival rate
 Time metrics: development time, testing time
 Effort metrics: person-hours
• Examples:
 DRE measures defect removal effectiveness
 Defect arrival rate measures defects per phase
 Effort is measured in man-hours
 Test coverage shows percentage of code tested
• Helps improve process efficiency and quality
Rubric:
•   Definition: 2 marks
• Types: 3 marks
• Examples: 3 marks
• Importance: 2 marks
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper c47c8375b6f8

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_IT_7001/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   Module   Marks
Q1. A   Explain how unexpected program behaviour is related to differences from 5
CO-1;   the expected system performance, with examples.
BL1
Solution:
Unexpected program behaviour means the software is not working the way
it was supposed to. This shows a difference between expected
performance (what we want) and actual performance (what happens).
Relationship Between the Two
• Expected Performance:
How the system should behave according to requirements.
Example: A login system should allow valid users to log in.
• Unexpected Behavior:
When the system does something wrong or different.
Example: A valid user cannot log in even with the correct password.
This difference shows that there is a problem in the system.
Examples
1. Login System
o Expected: User logs in successfully with correct details
********** 1 **********
--- page 2 ---
o Actual: Login fails
→ Indicates an issue in authentication logic
2. Banking Application
o Expected: Correct balance is displayed
o Actual: Wrong balance is shown
→ Shows calculation or data error
3. E-commerce Website
o Expected: Order is placed after payment
o Actual: Payment is deducted but order not confirmed
→ Indicates system failure or transaction issue
Conclusion
Whenever a program behaves unexpectedly, it means the system is not
meeting its expected performance. This gap helps identify problems that
need to be fixed.
Q1.b   5
CO-1;   A software system is frequently updated to fix bugs and improve features.
BL2   Explain how product revision quality factors support such activities.
When a software system is frequently updated to fix bugs and enhance
features, the effectiveness of these activities depends on Product Revision
Quality Factors defined in McCall’s Quality Model.
These factors focus on how easily the software can be modified, tested, and
improved.
Product Revision Quality Factors and Their Role
1. Maintainability
Meaning: Ease with which software can be corrected or updated.
Support in this scenario:
• Enables quick bug fixing and issue resolution
• Reduces time and effort required for updates
• Makes code easier to understand and modify
Without maintainability, frequent updates become costly and error-prone.
2. Flexibility
Meaning: Ability of the software to adapt to changes or new requirements.
********** 2 **********
--- page 3 ---
Support in this scenario:
• Allows developers to add new features smoothly
• Supports evolving user needs and business requirements
• Reduces the risk of breaking existing functionality
Ensures the system can grow without major redesign.
3. Testability
Meaning: Ease with which software can be tested after modifications.
Support in this scenario:
• Helps verify that bug fixes and new features work correctly
• Enables faster and more effective testing processes
• Supports automation and regression testing
Prevents introduction of new defects during updates.
Conclusion
Product   revision   quality   factors—maintainability,   flexibility, and
testability—are essential for systems that undergo frequent updates. They
ensure that:
• Changes are implemented efficiently
• New features are integrated smoothly
• Software quality is maintained over time
Thus, these factors play a crucial role in continuous improvement and long-
term sustainability of software systems.
Q1.c   5
CO-   Explain the significance of CMMI in improving software development
2;BL 3   processes.
Answer:
• Provides structured framework for process improvement
• Defines maturity levels
• Helps in reducing defects
• Improves productivity and efficiency
• Enables continuous process improvement
Rubric:
• Concept: 2 marks
•   Significance: 2 marks
********** 3 **********
--- page 4 ---
• Outcome: 1 mark
Q1.d   5
CO-   Analyse product metrics and explain how they are used to evaluate the
3;BL 4   quality of a software product.
Solution:
Product metrics are measures used to evaluate the quality and
performance of a software product.
Analysis of Product Metrics
Product metrics help in understanding how good the software is by
measuring different aspects such as:
1. Size Metrics
o Measure the size of the software (e.g., lines of code)
o Helps estimate complexity and development effort
2. Complexity Metrics
o Measure how complicated the code is
o Example: Cyclomatic complexity
o Higher complexity means higher chances of errors
3. Quality Metrics
o Measure reliability, correctness, and performance
o Example: Number of defects, failure rate
4. Performance Metrics
o Measure how efficiently the system works
o Example: Response time, speed, memory usage
How They Evaluate Software Quality
• Help identify problem areas in the software
• Make it easier to improve performance and reliability
• Provide a quantitative way to compare different products
• Support better decision-making during development and
maintenance
Conclusion
********** 4 **********
--- page 5 ---
Product metrics are important for analyzing and improving software quality,
as they provide measurable data about the system’s performance,
complexity, and reliability.
Q2. A.   10
CO-   Explain the classification of software testing based on:
3;BL 5   a) Testing concepts
b) Requirements classification
Solution-
Marking 5 for testing and 5 for requirement classification
Software test classification
• Software tests may be classified according to the testing concept or
to the requirements classification in effect.
•   Classification according to testing concept:
• Black box (functionality) testing
• White box (structural) testing
Black box and white box testing – IEEE definitions
•   Black box testing:
• Def. 1: Testing that ignores the internal mechanism of a
system or component and focuses solely on the outputs
generated in response to selected inputs and execution
conditions.
• Def. 2: Testing conducted to evaluate the compliance of a
system or component with specified functional requirements.
• White box testing:
• Def. 1: Testing that takes into account the internal
mechanism of a system or component.
• Realization of the white box testing concept requires
verification of every program statement and comment.
• White box testing enables performance of data processing
and calculations correctness tests, software qualification
tests, maintainability tests and reusability tests.
Classification according to requirements
McCall’s classic model for classification of software quality requirements.
• The model has been extended to the classification of the
tests carried out to ensure full coverage of the respective
requirements.
• The requirements and their corresponding tests are shown in Table.
********** 5 **********
--- page 6 ---
Q2. B.   10
CO-   What are the different components of software maintenance? What are the
4;BL 2   infrastructure tools that support maintenance in quality assurance?
********** 6 **********
--- page 7 ---
Components of Software Maintenance
Software maintenance refers to modifications made to a software system
after delivery to keep it useful and efficient.
Main Components / Types of Maintenance
1. Corrective Maintenance
a. Fixes defects or bugs found after deployment.
b. Example: Resolving system crashes or incorrect outputs.
2. Adaptive Maintenance
a. Updates software to work in a changed environment.
b. Example: Modifying software for new OS, hardware, or
regulations.
3. Perfective Maintenance
a. Enhances performance or adds new features based on user
feedback.
b. Example: Improving UI or adding new functionality.
4. Preventive Maintenance
a. Improves maintainability to prevent future issues.
b. Example: Code refactoring, documentation updates.
2. Infrastructure Tools Supporting Maintenance in SQA
Infrastructure tools help ensure that maintenance activities maintain or
improve software quality.
1. Configuration Management Tools
• Track and control changes in software.
• Maintain version history and prevent conflicts.
• Example: Git, SVN.
2. Version Control Systems
• Manage multiple versions of software artifacts.
• Enable rollback and parallel development.
3. Bug Tracking / Issue Tracking Tools
• Record, track, and manage defects.
• Help prioritize and monitor resolution.
• Example: Jira, Bugzilla.
********** 7 **********
--- page 8 ---
4. Automated Testing Tools
• Re-run test cases after changes to ensure no new defects.
• Supports regression testing.
• Example: Selenium, JUnit.
5. Documentation Tools
• Maintain updated system documents.
• Help new developers understand system changes.
6. Reverse Engineering Tools
• Help understand legacy systems by analyzing code structure.
• Useful when documentation is missing.
7. Code Analysis Tools
• Detect code quality issues and vulnerabilities.
• Improve maintainability.
• Example: SonarQube.
8. Build and Deployment Tools
• Automate integration and deployment.
• Ensure consistency in updates.
• Example: Jenkins, Maven.
Conclusion
Software maintenance ensures long-term usability of software through
corrective, adaptive, perfective, and preventive actions. Infrastructure tools
in SQA support these activities by managing changes, detecting defects,
ensuring quality, and automating testing and deployment processes.
If you want, I can also convert this into a 5-mark / 10-mark structured
answer, or short notes format for exams.
Q3.A   10
CO-   Describe the software project lifecycle components in the context of SQA.
4;BL2   Explain how each phase contributes to maintaining software quality.
********** 8 **********
--- page 9 ---
Overview of Lifecycle Components in SQA
Software project lifecycle components in SQA refer to the quality assurance
activities embedded in each phase of the Software Development Life Cycle
(SDLC).
Rather than treating quality as a final checkpoint, SQA distributes quality
activities
across all phases to detect and remove defects as early as possible.
2 Requirements Phase
SQA in this phase involves requirements reviews and traceability matrix
creation.
The goal is to ensure requirements are complete, consistent, unambiguous,
and
testable. Missing or contradictory requirements at this stage are the most
expensive
defects to fix later. SQA activities include formal inspections and customer
walkthroughs.
3 Design Phase
Design reviews and architectural walkthroughs are the primary SQA activities
here.
Design defects - such as poor module coupling, missing error handling, or
scalability
flaws - are identified and corrected before coding begins. SQA ensures that
design
conforms to standards and quality objectives.
4 Coding Phase:
Code reviews, pair programming, static analysis, and adherence to coding
standards
are the SQA activities in this phase. Tools like SonarQube help identify code
smells,
security vulnerabilities, and maintainability issues automatically. SQA
ensures code
quality is verified continuously, not just at delivery.
5 Testing Phase
This phase is the most visible SQA activity. It includes unit, integration,
system, and
acceptance testing. Test plans, test cases, and traceability to requirements
are all SQA
artifacts. The goal is to verify that the software meets specified requirements
and
performs reliably under expected and unexpected conditions.
6 Maintenance Phase
SQA in maintenance focuses on regression testing, change impact analysis,
and
defect tracking. Every change to a deployed system carries the risk of
introducing
new defects (regression). SQA ensures changes are reviewed, tested, and
documented appropriately to maintain the integrity of the system over time.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
********** 9 **********
--- page 10 ---
accurate explanation of all major points with relevant examples where
applicable
Q3. B.   Examine the SQA defect removal effectiveness model and describe how it 10
CO-   facilitates process improvement and methodical defect identification.
4;BL4
Introduction (2 Marks)
The SQA DRE model provides a structured framework to measure and
improve defect removal efficiency across development phases.
Model Components (3 Marks)
• Defect Injection Points: Where defects originate
• Detection Mechanisms: Reviews, testing, inspections
• Defect Tracking System: Logs and monitors defects
• Feedback Loop: Improves processes
Working of Model (3 Marks)
•   Identify defects at each stage
• Measure removal efficiency
• Compare planned vs actual defect removal
• Use feedback to refine processes
Process Improvement Role (1.5 Marks)
•   Identifies weak phases
• Improves testing strategies
• Enhances development practices
Conclusion (0.5 Mark)
The model ensures systematic defect identification and continuous
process improvement.
Q4. A.   10
CO-   A software development team frequently releases updates that introduce
1;BL3   new issues. Examine the root causes behind this recurring problem and
propose a structured approach to improve quality.
Solution:
********** 10 **********
--- page 11 ---
When a software team releases updates that keep introducing new
problems, it usually means there are issues in the development and quality
process.
Possible Reasons (Root Causes)
1. Inadequate Testing
o Updates are not properly tested before release
o Some errors remain undetected
2. Poor Requirement Understanding
o Developers may misunderstand what needs to be built
3. Lack of Regression Testing
o Fixing one issue creates new problems in other parts of the
system
4. Time Pressure / Deadlines
o Rushed development leads to careless mistakes
5. Poor Communication
o Teams working on different modules are not well coordinated
6. Weak Quality Assurance Practices
o No proper review or quality checks before release
Step-by-Step Approach to Improve Quality
1. Clear Requirement Analysis
o Ensure all team members understand the requirements
correctly
2. Implement Proper Testing
o Perform unit testing, integration testing, and system testing
3. Use Regression Testing
o Test the whole system after every update to avoid new issues
4. Code Reviews
o Review code regularly to catch mistakes early
5. Improve Communication
o Ensure proper coordination between teams
6. Use Version Control and CI/CD Tools
o Automate testing and deployment for better consistency
7. Allocate Sufficient Time
o Avoid rushing releases; focus on quality over speed
Q4. B.   10
CO-   Describe how software requirements are classified into software quality
1;BL1   factors. Discuss the benefits of such classification in quality assurance.
********** 11 **********
--- page 12 ---
Classification of Software Requirements into Quality Factors
Software requirements are broadly divided into:
• Functional Requirements – what the system should do
• Non-Functional Requirements (Quality Requirements) – how well
the system should perform
These non-functional requirements are classified into software quality
factors, commonly structured using models like McCall’s Quality Model.
Classification into Quality Factors
A. Product Operation Factors (Run-time behavior)
These define how the system performs during execution:
•   Reliability – consistent and error-free operation
•   Efficiency – optimal use of resources and fast response
• Usability – ease of use and user-friendliness
•   Integrity (Security) – protection against unauthorized access
• Correctness – accuracy of outputs
B. Product Revision Factors (Maintenance aspects)
These define how easily the system can be modified:
• Maintainability – ease of fixing defects
•   Flexibility – ease of adapting to changes
•   Testability – ease of testing the system
C. Product Transition Factors (Adaptability aspects)
These define how well the system adapts to new environments:
•   Portability – ability to run on different platforms
• Reusability – components can be reused
• Interoperability – ability to interact with other systems
Thus, software requirements are systematically mapped into quality factors
to ensure all aspects of software quality are addressed.
********** 12 **********
--- page 13 ---
Q5. A   10
CO-   Analyze the infrastructure components for error prevention and
2;BL4   improvement. Compare with management SQA components and evaluate
their relative impact on defect reduction.
Infrastructure Components Defined
Infrastructure components for error prevention include all the tools,
environments,
processes, and technical mechanisms that reduce the probability of defects
being
introduced. They form the technical backbone of SQA - the systems within
which
quality work is performed.
2 Key Infrastructure Elements
Configuration Management Systems (e.g., Git, SVN) prevent unauthorized
code
changes and version conflicts. Defect Tracking Systems (e.g., Jira, Bugzilla)
ensure
defects are systematically recorded and resolved. Automated build and
CI/CD
pipelines catch integration errors instantly. Coding standards and linting
tools
prevent common programming errors at the point of writing.
3 Management SQA Components Defined
Management components include project planning, resource allocation,
quality
audits, process compliance monitoring, and corrective action management.
They
provide the organizational authority and oversight that ensures SQA
activities are
actually carried out according to plan.
4 Comparative Analysis
Infrastructure components are preventive and automated - they stop defects
from
entering the system. Management components are directive and supervisory
- they
ensure the right processes are followed. Both are essential, but they operate
at
different levels: infrastructure at the technical level, management at the
organizational level.
5 Which Has Greater Impact on Defect Reduction?
Research and industry data suggest that infrastructure components,
particularly
CI/CD pipelines and automated testing, deliver more measurable and
consistent
defect reduction. Automated checks catch defects within seconds of code
commit,
while management oversight operates on a slower cycle. However, without
management enforcing the use of infrastructure tools, adoption falls and
********** 13 **********
--- page 14 ---
effectiveness drops. The conclusion is that infrastructure enables defect
prevention,
but management sustains it.
6 Real-World Evidence
Companies like Google and Microsoft report that continuous integration
combined
with automated test suites catches over 80% of defects before code review.
This
demonstrates the primacy of infrastructure components in large-scale defect
reduction, though management oversight is critical for long-term process
improvement.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
accurate explanation of all major points with relevant examples where
applicable
Q5. B.   10
CO-
3;BL5   A software organization spends the following costs:
• Prevention Cost: ₹40,000
• Appraisal Cost: ₹25,000
•   Internal Failure Cost: ₹20,000
• External Failure Cost: ₹15,000
Determine the Total Cost of Quality and assess if the company is making
enough preventative investments. (CO4; PO5; BL5)
Formula (2 Marks)
CoQ=Prevention+Appraisal+Internal+ExternalCoQ = Prevention +
Appraisal + Internal +
ExternalCoQ=Prevention+Appraisal+Internal+External
Calculation (3 Marks)
CoQ=40000+25000+20000+15000=₹100000CoQ = 40000 + 25000 + 20000
+ 15000 = ₹100000CoQ=40000+25000+20000+15000=₹100000
Analysis (4 Marks)
• Prevention (40%) → good investment
• External failure low → positive sign
• Balanced cost distribution
Conclusion (1 Mark)
Company is investing adequately in prevention.
********** 14 **********
--- page 15 ---
Q6. A.   10
CO-   Describe the software testing process. What are the different stages involved
3;BL1   in testing? Explain each stage with appropriate details.
Solution:
Marking each step of explanation requires 2 marks and Diagram for 2
marks,
Planning, design and performance of testing are carried out throughout the
software development process.
Determine the test methodology:
• The testing strategy: should a big bang or incremental testing
strategy be adopted? If incremental testing is preferable,
should testing be performed bottom-up or top-down?
• Which parts of the testing plan should be performed
according to the white box testing model?
• Which parts of the testing plan should be performed
according to the automated testing model?
Planning the test:
 The tests to be planned include:
 Unit tests
 Integration tests
 System tests.
• While unit tests deal with small units of
software or modules, integration tests deal
with several units that combine into a
subsystem. System tests refer to the entire
software package/system.
Test design:
 The products of the test design stage are:
 Detailed design and procedures for each test
 Test case database/file
********** 15 **********
--- page 16 ---
 The test design is carried out on the basis of the software test
plan as documented by STP.
• Test implementation:
 The testing implementation phase activities consist of a series
of tests, corrections of detected errors
Q6. B.   10
CO-   What are the types of external participants? Explain their contributions.
4;BL4   What are the appropriate SQA tools appropriate for use with external
participants
External participants can be classified into three main groups:
(1) Subcontractors (currently called “outsourcing” organizations) that
undertake to carry out parts of a project, small or large, according to cir
cumstances. Subcontractors usually offer the contractor at least one of the
following benefits: staff availability, special expertise or low prices.
(2) Suppliers of COTS software and reused software modules. The advan
tages of integrating these ready elements are obvious, ranging from
timetable and cost reductions to quality. One expects that integration of
these ready-for-use elements will achieve savings in development resources,
a shorter timetable and higher quality software. Software of higher quality is
expected as these components have already been tested and corrected by
********** 16 **********
--- page 17 ---
the developers as well as corrected according to the faults identified by
previous customers. The characteristics of COTS software and quality
problems involved in their use are discussed by Basili and Boehm (2001).
(3) The customer themselves as participant in performing the project. It is
quite common for a customer to perform parts of the project: to apply the
customers’ special expertise, respond to commercial or other security needs,
keep internal development staff occupied, prevent future mainte nance
problems and so forth. This situation does have drawbacks in terms of the
customer–supplier relationship necessary for successful per formance of a
project, but they are overweighed by the inputs the customer makes. Hence,
the inevitability of this situation has become a standard element of many
software development projects and contrac tual relations.
The main benefits to the contractor of using external organizations are: ■
Overcoming shortages of professional staff by transferring parts of the
project to be carried out to firms employing staff having those skills. ■
Potentially shorter project schedules, achieved by purchasing COTS software
and reused software rather than developing the software. ■ Expertise
acquired in areas that need specialization through the participation of
owners– the subcontractor or the customer’s development department– of
that expertise. ■ Saved budget, achieved when subcontractorsoffer
pricesbelow those incurred by performing the project internally, and by the
use of COTS and reused software.
Marking scheme –
Each type of participants – 1.5 marks
Benefits – 2.5 marks
Q7. a.   10
CO-
4;BL4   Scenario: A mid-sized software company wants to obtain ISO 9000-3
certification.   They   currently   have   informal   processes,   minimal
documentation, and no formal audits.
Question:
As an SQA consultant, explain how the company should align its processes
with ISO 9000-3 requirements. Discuss key steps, challenges, and expected
benefits.
Answer:
• Adopt ISO 9000-3 standards for software processes
• Define and document quality management system (QMS)
• Standardize development procedures & documentation
• Conduct internal audits and reviews
********** 17 **********
--- page 18 ---
• Train staff on quality processes
• Ensure process consistency across teams
• Benefits: improved quality, customer trust, certification readiness
Rubric:
• Understanding of ISO 9000-3 : 2 marks
• QMS & documentation : 2 marks
• Process standardization : 2 marks
• Audits & training : 2 marks
• Benefits / conclusion : 2 marks
Q7. b.   Explain process metrics with suitable examples.   10
CO-
4;BL1   Answer:
• Process metrics measure efficiency of the software development
process
• Types:
 Defect metrics: DRE, defect arrival rate
 Time metrics: development time, testing time
 Effort metrics: person-hours
• Examples:
 DRE measures defect removal effectiveness
 Defect arrival rate measures defects per phase
 Effort is measured in man-hours
 Test coverage shows percentage of code tested
• Helps improve process efficiency and quality
Rubric:
•   Definition: 2 marks
• Types: 3 marks
• Examples: 3 marks
• Importance: 2 marks
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper d58b15a516c7

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Software Quality Assurance/ANS_Software Quality Assurance(702IT0E022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Software Quality Assurance
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question no.1 is compulsory.
3. Attempt any 4 questions from question no. 2-7
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. The figure on the right-hand side indicates full marks
7. Assume suitable data if necessary.
Q.No.   Module   Marks
Q1. A   Explain how unexpected program behaviour is related to differences from 5
CO-1;   the expected system performance, with examples.
BL1
Solution:
Unexpected program behaviour means the software is not working the way
it was supposed to. This shows a difference between expected
performance (what we want) and actual performance (what happens).
Relationship Between the Two
• Expected Performance:
How the system should behave according to requirements.
Example: A login system should allow valid users to log in.
• Unexpected Behavior:
When the system does something wrong or different.
Example: A valid user cannot log in even with the correct password.
This difference shows that there is a problem in the system.
Examples
1. Login System
o Expected: User logs in successfully with correct details
********** 1 **********
--- page 2 ---
o Actual: Login fails
→ Indicates an issue in authentication logic
2. Banking Application
o Expected: Correct balance is displayed
o Actual: Wrong balance is shown
→ Shows calculation or data error
3. E-commerce Website
o Expected: Order is placed after payment
o Actual: Payment is deducted but order not confirmed
→ Indicates system failure or transaction issue
Conclusion
Whenever a program behaves unexpectedly, it means the system is not
meeting its expected performance. This gap helps identify problems that
need to be fixed.
Q1.b   5
CO-1;   A software system is frequently updated to fix bugs and improve features.
BL2   Explain how product revision quality factors support such activities.
When a software system is frequently updated to fix bugs and enhance
features, the effectiveness of these activities depends on Product Revision
Quality Factors defined in McCall’s Quality Model.
These factors focus on how easily the software can be modified, tested, and
improved.
Product Revision Quality Factors and Their Role
1. Maintainability
Meaning: Ease with which software can be corrected or updated.
Support in this scenario:
• Enables quick bug fixing and issue resolution
• Reduces time and effort required for updates
• Makes code easier to understand and modify
Without maintainability, frequent updates become costly and error-prone.
2. Flexibility
Meaning: Ability of the software to adapt to changes or new requirements.
********** 2 **********
--- page 3 ---
Support in this scenario:
• Allows developers to add new features smoothly
• Supports evolving user needs and business requirements
• Reduces the risk of breaking existing functionality
Ensures the system can grow without major redesign.
3. Testability
Meaning: Ease with which software can be tested after modifications.
Support in this scenario:
• Helps verify that bug fixes and new features work correctly
• Enables faster and more effective testing processes
• Supports automation and regression testing
Prevents introduction of new defects during updates.
Conclusion
Product   revision   quality   factors—maintainability,   flexibility, and
testability—are essential for systems that undergo frequent updates. They
ensure that:
• Changes are implemented efficiently
• New features are integrated smoothly
• Software quality is maintained over time
Thus, these factors play a crucial role in continuous improvement and long-
term sustainability of software systems.
Q1.c   5
CO-   Explain the significance of CMMI in improving software development
2;BL 3   processes.
Answer:
• Provides structured framework for process improvement
• Defines maturity levels
• Helps in reducing defects
• Improves productivity and efficiency
• Enables continuous process improvement
Rubric:
• Concept: 2 marks
•   Significance: 2 marks
********** 3 **********
--- page 4 ---
• Outcome: 1 mark
Q1.d   5
CO-   Analyse product metrics and explain how they are used to evaluate the
3;BL 4   quality of a software product.
Solution:
Product metrics are measures used to evaluate the quality and
performance of a software product.
Analysis of Product Metrics
Product metrics help in understanding how good the software is by
measuring different aspects such as:
1. Size Metrics
o Measure the size of the software (e.g., lines of code)
o Helps estimate complexity and development effort
2. Complexity Metrics
o Measure how complicated the code is
o Example: Cyclomatic complexity
o Higher complexity means higher chances of errors
3. Quality Metrics
o Measure reliability, correctness, and performance
o Example: Number of defects, failure rate
4. Performance Metrics
o Measure how efficiently the system works
o Example: Response time, speed, memory usage
How They Evaluate Software Quality
• Help identify problem areas in the software
• Make it easier to improve performance and reliability
• Provide a quantitative way to compare different products
• Support better decision-making during development and
maintenance
Conclusion
********** 4 **********
--- page 5 ---
Product metrics are important for analyzing and improving software quality,
as they provide measurable data about the system’s performance,
complexity, and reliability.
Q2. A.   10
CO-   Explain the classification of software testing based on:
3;BL 5   a) Testing concepts
b) Requirements classification
Solution-
Marking 5 for testing and 5 for requirement classification
Software test classification
• Software tests may be classified according to the testing concept or
to the requirements classification in effect.
•   Classification according to testing concept:
• Black box (functionality) testing
• White box (structural) testing
Black box and white box testing – IEEE definitions
•   Black box testing:
• Def. 1: Testing that ignores the internal mechanism of a
system or component and focuses solely on the outputs
generated in response to selected inputs and execution
conditions.
• Def. 2: Testing conducted to evaluate the compliance of a
system or component with specified functional requirements.
• White box testing:
• Def. 1: Testing that takes into account the internal
mechanism of a system or component.
• Realization of the white box testing concept requires
verification of every program statement and comment.
• White box testing enables performance of data processing
and calculations correctness tests, software qualification
tests, maintainability tests and reusability tests.
Classification according to requirements
McCall’s classic model for classification of software quality requirements.
• The model has been extended to the classification of the
tests carried out to ensure full coverage of the respective
requirements.
• The requirements and their corresponding tests are shown in Table.
********** 5 **********
--- page 6 ---
Q2. B.   10
CO-   What are the different components of software maintenance? What are the
4;BL 2   infrastructure tools that support maintenance in quality assurance?
********** 6 **********
--- page 7 ---
Components of Software Maintenance
Software maintenance refers to modifications made to a software system
after delivery to keep it useful and efficient.
Main Components / Types of Maintenance
1. Corrective Maintenance
a. Fixes defects or bugs found after deployment.
b. Example: Resolving system crashes or incorrect outputs.
2. Adaptive Maintenance
a. Updates software to work in a changed environment.
b. Example: Modifying software for new OS, hardware, or
regulations.
3. Perfective Maintenance
a. Enhances performance or adds new features based on user
feedback.
b. Example: Improving UI or adding new functionality.
4. Preventive Maintenance
a. Improves maintainability to prevent future issues.
b. Example: Code refactoring, documentation updates.
2. Infrastructure Tools Supporting Maintenance in SQA
Infrastructure tools help ensure that maintenance activities maintain or
improve software quality.
1. Configuration Management Tools
• Track and control changes in software.
• Maintain version history and prevent conflicts.
• Example: Git, SVN.
2. Version Control Systems
• Manage multiple versions of software artifacts.
• Enable rollback and parallel development.
3. Bug Tracking / Issue Tracking Tools
• Record, track, and manage defects.
• Help prioritize and monitor resolution.
• Example: Jira, Bugzilla.
********** 7 **********
--- page 8 ---
4. Automated Testing Tools
• Re-run test cases after changes to ensure no new defects.
• Supports regression testing.
• Example: Selenium, JUnit.
5. Documentation Tools
• Maintain updated system documents.
• Help new developers understand system changes.
6. Reverse Engineering Tools
• Help understand legacy systems by analyzing code structure.
• Useful when documentation is missing.
7. Code Analysis Tools
• Detect code quality issues and vulnerabilities.
• Improve maintainability.
• Example: SonarQube.
8. Build and Deployment Tools
• Automate integration and deployment.
• Ensure consistency in updates.
• Example: Jenkins, Maven.
Conclusion
Software maintenance ensures long-term usability of software through
corrective, adaptive, perfective, and preventive actions. Infrastructure tools
in SQA support these activities by managing changes, detecting defects,
ensuring quality, and automating testing and deployment processes.
If you want, I can also convert this into a 5-mark / 10-mark structured
answer, or short notes format for exams.
Q3.A   10
CO-   Describe the software project lifecycle components in the context of SQA.
4;BL2   Explain how each phase contributes to maintaining software quality.
********** 8 **********
--- page 9 ---
Overview of Lifecycle Components in SQA
Software project lifecycle components in SQA refer to the quality assurance
activities embedded in each phase of the Software Development Life Cycle
(SDLC).
Rather than treating quality as a final checkpoint, SQA distributes quality
activities
across all phases to detect and remove defects as early as possible.
2 Requirements Phase
SQA in this phase involves requirements reviews and traceability matrix
creation.
The goal is to ensure requirements are complete, consistent, unambiguous,
and
testable. Missing or contradictory requirements at this stage are the most
expensive
defects to fix later. SQA activities include formal inspections and customer
walkthroughs.
3 Design Phase
Design reviews and architectural walkthroughs are the primary SQA activities
here.
Design defects - such as poor module coupling, missing error handling, or
scalability
flaws - are identified and corrected before coding begins. SQA ensures that
design
conforms to standards and quality objectives.
4 Coding Phase:
Code reviews, pair programming, static analysis, and adherence to coding
standards
are the SQA activities in this phase. Tools like SonarQube help identify code
smells,
security vulnerabilities, and maintainability issues automatically. SQA
ensures code
quality is verified continuously, not just at delivery.
5 Testing Phase
This phase is the most visible SQA activity. It includes unit, integration,
system, and
acceptance testing. Test plans, test cases, and traceability to requirements
are all SQA
artifacts. The goal is to verify that the software meets specified requirements
and
performs reliably under expected and unexpected conditions.
6 Maintenance Phase
SQA in maintenance focuses on regression testing, change impact analysis,
and
defect tracking. Every change to a deployed system carries the risk of
introducing
new defects (regression). SQA ensures changes are reviewed, tested, and
documented appropriately to maintain the integrity of the system over time.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
********** 9 **********
--- page 10 ---
accurate explanation of all major points with relevant examples where
applicable
Q3. B.   Examine the SQA defect removal effectiveness model and describe how it 10
CO-   facilitates process improvement and methodical defect identification.
4;BL4
Introduction (2 Marks)
The SQA DRE model provides a structured framework to measure and
improve defect removal efficiency across development phases.
Model Components (3 Marks)
• Defect Injection Points: Where defects originate
• Detection Mechanisms: Reviews, testing, inspections
• Defect Tracking System: Logs and monitors defects
• Feedback Loop: Improves processes
Working of Model (3 Marks)
•   Identify defects at each stage
• Measure removal efficiency
• Compare planned vs actual defect removal
• Use feedback to refine processes
Process Improvement Role (1.5 Marks)
•   Identifies weak phases
• Improves testing strategies
• Enhances development practices
Conclusion (0.5 Mark)
The model ensures systematic defect identification and continuous
process improvement.
Q4. A.   10
CO-   A software development team frequently releases updates that introduce
1;BL3   new issues. Examine the root causes behind this recurring problem and
propose a structured approach to improve quality.
Solution:
********** 10 **********
--- page 11 ---
When a software team releases updates that keep introducing new
problems, it usually means there are issues in the development and quality
process.
Possible Reasons (Root Causes)
1. Inadequate Testing
o Updates are not properly tested before release
o Some errors remain undetected
2. Poor Requirement Understanding
o Developers may misunderstand what needs to be built
3. Lack of Regression Testing
o Fixing one issue creates new problems in other parts of the
system
4. Time Pressure / Deadlines
o Rushed development leads to careless mistakes
5. Poor Communication
o Teams working on different modules are not well coordinated
6. Weak Quality Assurance Practices
o No proper review or quality checks before release
Step-by-Step Approach to Improve Quality
1. Clear Requirement Analysis
o Ensure all team members understand the requirements
correctly
2. Implement Proper Testing
o Perform unit testing, integration testing, and system testing
3. Use Regression Testing
o Test the whole system after every update to avoid new issues
4. Code Reviews
o Review code regularly to catch mistakes early
5. Improve Communication
o Ensure proper coordination between teams
6. Use Version Control and CI/CD Tools
o Automate testing and deployment for better consistency
7. Allocate Sufficient Time
o Avoid rushing releases; focus on quality over speed
Q4. B.   10
CO-   Describe how software requirements are classified into software quality
1;BL1   factors. Discuss the benefits of such classification in quality assurance.
********** 11 **********
--- page 12 ---
Classification of Software Requirements into Quality Factors
Software requirements are broadly divided into:
• Functional Requirements – what the system should do
• Non-Functional Requirements (Quality Requirements) – how well
the system should perform
These non-functional requirements are classified into software quality
factors, commonly structured using models like McCall’s Quality Model.
Classification into Quality Factors
A. Product Operation Factors (Run-time behavior)
These define how the system performs during execution:
•   Reliability – consistent and error-free operation
•   Efficiency – optimal use of resources and fast response
• Usability – ease of use and user-friendliness
•   Integrity (Security) – protection against unauthorized access
• Correctness – accuracy of outputs
B. Product Revision Factors (Maintenance aspects)
These define how easily the system can be modified:
• Maintainability – ease of fixing defects
•   Flexibility – ease of adapting to changes
•   Testability – ease of testing the system
C. Product Transition Factors (Adaptability aspects)
These define how well the system adapts to new environments:
•   Portability – ability to run on different platforms
• Reusability – components can be reused
• Interoperability – ability to interact with other systems
Thus, software requirements are systematically mapped into quality factors
to ensure all aspects of software quality are addressed.
********** 12 **********
--- page 13 ---
Q5. A   10
CO-   Analyze the infrastructure components for error prevention and
2;BL4   improvement. Compare with management SQA components and evaluate
their relative impact on defect reduction.
Infrastructure Components Defined
Infrastructure components for error prevention include all the tools,
environments,
processes, and technical mechanisms that reduce the probability of defects
being
introduced. They form the technical backbone of SQA - the systems within
which
quality work is performed.
2 Key Infrastructure Elements
Configuration Management Systems (e.g., Git, SVN) prevent unauthorized
code
changes and version conflicts. Defect Tracking Systems (e.g., Jira, Bugzilla)
ensure
defects are systematically recorded and resolved. Automated build and
CI/CD
pipelines catch integration errors instantly. Coding standards and linting
tools
prevent common programming errors at the point of writing.
3 Management SQA Components Defined
Management components include project planning, resource allocation,
quality
audits, process compliance monitoring, and corrective action management.
They
provide the organizational authority and oversight that ensures SQA
activities are
actually carried out according to plan.
4 Comparative Analysis
Infrastructure components are preventive and automated - they stop defects
from
entering the system. Management components are directive and supervisory
- they
ensure the right processes are followed. Both are essential, but they operate
at
different levels: infrastructure at the technical level, management at the
organizational level.
5 Which Has Greater Impact on Defect Reduction?
Research and industry data suggest that infrastructure components,
particularly
CI/CD pipelines and automated testing, deliver more measurable and
consistent
defect reduction. Automated checks catch defects within seconds of code
commit,
while management oversight operates on a slower cycle. However, without
management enforcing the use of infrastructure tools, adoption falls and
********** 13 **********
--- page 14 ---
effectiveness drops. The conclusion is that infrastructure enables defect
prevention,
but management sustains it.
6 Real-World Evidence
Companies like Google and Microsoft report that continuous integration
combined
with automated test suites catches over 80% of defects before code review.
This
demonstrates the primacy of infrastructure components in large-scale defect
reduction, though management oversight is critical for long-term process
improvement.
Marking: Award 2 marks per key point (6 points x ~1.5-2 marks). Full marks
require
accurate explanation of all major points with relevant examples where
applicable
Q5. B.   10
CO-
3;BL5   A software organization spends the following costs:
• Prevention Cost: ₹40,000
• Appraisal Cost: ₹25,000
•   Internal Failure Cost: ₹20,000
• External Failure Cost: ₹15,000
Determine the Total Cost of Quality and assess if the company is making
enough preventative investments. (CO4; PO5; BL5)
Formula (2 Marks)
CoQ=Prevention+Appraisal+Internal+ExternalCoQ = Prevention +
Appraisal + Internal +
ExternalCoQ=Prevention+Appraisal+Internal+External
Calculation (3 Marks)
CoQ=40000+25000+20000+15000=₹100000CoQ = 40000 + 25000 + 20000
+ 15000 = ₹100000CoQ=40000+25000+20000+15000=₹100000
Analysis (4 Marks)
• Prevention (40%) → good investment
• External failure low → positive sign
• Balanced cost distribution
Conclusion (1 Mark)
Company is investing adequately in prevention.
********** 14 **********
--- page 15 ---
Q6. A.   10
CO-   Describe the software testing process. What are the different stages involved
3;BL1   in testing? Explain each stage with appropriate details.
Solution:
Marking each step of explanation requires 2 marks and Diagram for 2
marks,
Planning, design and performance of testing are carried out throughout the
software development process.
Determine the test methodology:
• The testing strategy: should a big bang or incremental testing
strategy be adopted? If incremental testing is preferable,
should testing be performed bottom-up or top-down?
• Which parts of the testing plan should be performed
according to the white box testing model?
• Which parts of the testing plan should be performed
according to the automated testing model?
Planning the test:
 The tests to be planned include:
 Unit tests
 Integration tests
 System tests.
• While unit tests deal with small units of
software or modules, integration tests deal
with several units that combine into a
subsystem. System tests refer to the entire
software package/system.
Test design:
 The products of the test design stage are:
 Detailed design and procedures for each test
 Test case database/file
********** 15 **********
--- page 16 ---
 The test design is carried out on the basis of the software test
plan as documented by STP.
• Test implementation:
 The testing implementation phase activities consist of a series
of tests, corrections of detected errors
Q6. B.   10
CO-   What are the types of external participants? Explain their contributions.
4;BL4   What are the appropriate SQA tools appropriate for use with external
participants
External participants can be classified into three main groups:
(1) Subcontractors (currently called “outsourcing” organizations) that
undertake to carry out parts of a project, small or large, according to cir
cumstances. Subcontractors usually offer the contractor at least one of the
following benefits: staff availability, special expertise or low prices.
(2) Suppliers of COTS software and reused software modules. The advan
tages of integrating these ready elements are obvious, ranging from
timetable and cost reductions to quality. One expects that integration of
these ready-for-use elements will achieve savings in development resources,
a shorter timetable and higher quality software. Software of higher quality is
expected as these components have already been tested and corrected by
********** 16 **********
--- page 17 ---
the developers as well as corrected according to the faults identified by
previous customers. The characteristics of COTS software and quality
problems involved in their use are discussed by Basili and Boehm (2001).
(3) The customer themselves as participant in performing the project. It is
quite common for a customer to perform parts of the project: to apply the
customers’ special expertise, respond to commercial or other security needs,
keep internal development staff occupied, prevent future mainte nance
problems and so forth. This situation does have drawbacks in terms of the
customer–supplier relationship necessary for successful per formance of a
project, but they are overweighed by the inputs the customer makes. Hence,
the inevitability of this situation has become a standard element of many
software development projects and contrac tual relations.
The main benefits to the contractor of using external organizations are: ■
Overcoming shortages of professional staff by transferring parts of the
project to be carried out to firms employing staff having those skills. ■
Potentially shorter project schedules, achieved by purchasing COTS software
and reused software rather than developing the software. ■ Expertise
acquired in areas that need specialization through the participation of
owners– the subcontractor or the customer’s development department– of
that expertise. ■ Saved budget, achieved when subcontractorsoffer
pricesbelow those incurred by performing the project internally, and by the
use of COTS and reused software.
Marking scheme –
Each type of participants – 1.5 marks
Benefits – 2.5 marks
Q7. a.   10
CO-
4;BL4   Scenario: A mid-sized software company wants to obtain ISO 9000-3
certification.   They   currently   have   informal   processes,   minimal
documentation, and no formal audits.
Question:
As an SQA consultant, explain how the company should align its processes
with ISO 9000-3 requirements. Discuss key steps, challenges, and expected
benefits.
Answer:
• Adopt ISO 9000-3 standards for software processes
• Define and document quality management system (QMS)
• Standardize development procedures & documentation
• Conduct internal audits and reviews
********** 17 **********
--- page 18 ---
• Train staff on quality processes
• Ensure process consistency across teams
• Benefits: improved quality, customer trust, certification readiness
Rubric:
• Understanding of ISO 9000-3 : 2 marks
• QMS & documentation : 2 marks
• Process standardization : 2 marks
• Audits & training : 2 marks
• Benefits / conclusion : 2 marks
Q7. b.   Explain process metrics with suitable examples.   10
CO-
4;BL1   Answer:
• Process metrics measure efficiency of the software development
process
• Types:
 Defect metrics: DRE, defect arrival rate
 Time metrics: development time, testing time
 Effort metrics: person-hours
• Examples:
 DRE measures defect removal effectiveness
 Defect arrival rate measures defects per phase
 Effort is measured in man-hours
 Test coverage shows percentage of code tested
• Helps improve process efficiency and quality
Rubric:
•   Definition: 2 marks
• Types: 3 marks
• Examples: 3 marks
• Importance: 2 marks
********** 18 **********
````
