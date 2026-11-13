# Compiler Design — syllabus

9 syllabus section(s) for this course in the archive, newest batch first. Text comes from the PDF (OCR for scanned pages; check figures against the source). All programmes' syllabi: [`syllabi/`](../../syllabi/README.md).

## B TECH · Artificial Intelligence · AY 2025-26 · Sem 5

- Course as printed: Compiler Design (code 702AI0E001)
- Source: `04_Syllabi_Archive/B TECH/3RD YEAR/ARTIFICIAL INTELLIGENCE/SEM-V/B Tech, Artificial Intelligence, 3rd Year, Sem V, A Y 2025-26.pdf`, page 13-15

````text
Program: B Tech/MBA Tech Artificial Intelligence,   Semester: V/V-VII
B Tech AI and DS, AI and ML, CSE (DS)
Course: Compiler Design   Code: 702AI0E001
Teaching Scheme   Evaluation Scheme
Lecture   Practical   Tutorial   Internal Continuous   Term End
(Hours per   (Hours   (Hours   Credit   Assessment (ICA)   Examinations (TEE)
week)   per week)   per week)   (Marks - 50)   (Marks - 100)
2   2   0   3   Marks Scaled to 50   Marks Scaled to 50
Prerequisite: Knowledge of Programming
Course Objective
This course provides the foundation of compilers, helps to learn programming language translation
and compiler design concepts. It helps to understand language recognition, symbol table management,
semantic analysis and code generation.
Course Outcomes
After completion of the course, students will be able to -
1. Describe the working of the lexical analyzer
2. Design the functionalities of the syntax and semantic parsers
3. Describe the procedure of symbol table management and code generation
4. Analyze the code optimization techniques
Detailed Syllabus
Unit   Description   Duration
Introduction
Overview of the phases of compiler, Lexical Analysis (scanner): Regular
1.   04
languages, Finite automata, regular expressions, regular expression to finite
automata, scanner generator (lex, flex).
Syntax Analysis (Parser)
Context-free languages and grammars, push-down automata, LL(1) grammars
2.   and top-down parsing, operator grammars, LR(O), SLR(1), LR(1), LALR(1)   08
grammars and bottom-up parsing, ambiguity and LR parsing, LALR(1) parser
generator (yacc, bison)
Semantic Analysis
3.   Attribute grammars, syntax directed definition, evaluation and flow of attribute   06
in a syntax tree.
Symbol Table
Basic structure, symbol attributes and management. Run-time environment:
4.   02
Procedure activation, parameter passing, value return, memory allocation,
scope.
Intermediate Code Generation
5.   03
Translation of different language features, different types of intermediate forms.
Signature
(Head of the Department)
B Tech & MBA Tech AI/Sem V/AY 2025-26/ Page 13 of 16
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Code Improvement (Optimization)
6.   Control-flow,   data-flow dependence, Optimization   techniques:   local   03
optimization, global optimization, loop optimization, peep-hole optimization.
Architecture Dependent Code Improvement
7.   Instruction scheduling (for pipeline), Cache memory optimization, Register   02
allocation and target code generation.
Advanced Topics
8.   Data abstraction, compilation of Object-Oriented features and non-imperative   02
programming languages
Total   30
Text Books
1. V. Aho, R. Sethi and J. Ullman, Compilers: Principles, Techniques and Tools, 2nd Edition, Addison-
Wesley, 2013.
2. Levine R. John, Tony Mason and Doug Brown, Lex & Yacc, 2nd Edition, O’Reilly, 2010 (Classic).
Reference Books
1. Bjarne Stroustrup, The Design and Evolution of C++, 2nd Edition, Addison-Wesley, 2012.
2. K. L. P Mishra, N. Chandrashekaran, Theory of computer science- Automata Languages and
computation, 3rd Edition, Prentice Hall of India, 2013.
3. Andrew W. Appel, Modern Compiler Implementation in C, 1st Edition Cambridge University
Press, 2010 (Classic).
Laboratory Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus.
Signature
(Head of the Department)
B Tech & MBA Tech AI/Sem V/AY 2025-26/ Page 14 of 16
SVKM’s NMIMS   No Change
Mukesh Patel School of Technology Management & Engineering
Program: B Tech & MBA Artificial Intelligence, B Tech AI and ML   Semester : V-VII
````

## B TECH · Computer Science and Business Systems · AY 2025-26 · Sem 5

- Course as printed: Compiler Design (code 702CO0C028)
- Source: `04_Syllabi_Archive/B TECH/3RD YEAR/CSBS/SEM V/B Tech, CSBS, 3rd Year, Sem-V, A Y 2025-26.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course - Compiler Design   Code: 702CO0C028
Teaching Scheme   Evaluation Scheme
Lecture   Practical
Tutorial   Internal Continuous Term   End
(Hours   (Hours
(Hours   Credit   Assessment (ICA)   Examinations (TEE)
per   per
per week)   (Marks-50)   (Marks-100 )
week)   week)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Course Objective -To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design concepts,
understand language recognition, symbol table management, semantic analysis and code
generation.
Course Outcomes- After completion of the course, students will be able to
1. Comprehend the working of lexical analysis, parsing,
2. Understand the significance of code generation and code optimization,
3. Implement working module of compiler.
Detailed Syllabus:
Unit   Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis (scanner):   07
Regular languages, finite automata, regular expressions, regular expression to
finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars, push-down   10
automata, LL(1) grammars and top-down parsing, operator grammars, LR(O),
SLR(1), LR(1), LALR(1) grammars and bottom-up parsing, ambiguity and LR
parsing, LALR(1) parser generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed definition,   05
evaluation and flow of attribute in a syntax tree.
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
4.   Symbol Table: Basic structure, symbol attributes and management. Run-time   05
environment: Procedure activation, parameter passing, value return, memory
allocation, scope.
5.   Intermediate Code Generation: Translation of different language features,   04
different types of intermediate forms.
6.   Code Improvement (optimization): control-flow, data-flow dependence, local   05
optimization, global optimization, loop optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling (for   05
pipeline), loop optimization (for cache memory), Register allocation and
target code generation.
8.   Advanced topics: Type systems, data abstraction, compilation of Object   04
Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman, “Compilers: Principles, Techniques and Tools”, 2nd Edition,
Addison-Wesley, 2023.
2. Levine R. John, Tony Mason and Doug Brown, “Lex & Yacc”, 2nd Edition, O’Reilly media,
2007.
Reference Books:
1. Bjarne Stroustrup, “The Design and Evolution of C++” 2nd Edition, Addison-Wesley, 2007.
Laboratory Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management & Engineering
Program: B Tech/MBA Tech (IT, Computer Engineering), BTI (IT,   Semester : V, IX
Computer Engineering), B Tech (CSE-Cybersecurity, CSBS,
Computer Science, CSEDS)
````

## B TECH · Computer Science and Business Systems · AY 2024-25 · Sem 5

- Course as printed: Compiler Design (code 702CO0C028)
- Source: `04_Syllabi_Archive/B TECH/3RD YEAR/CSBS/SEM V/B Tech, CSBS, 3rd Year, Sem-V, A Y 2024-25.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course - Compiler Design   Code: 702CO0C028
Teaching Scheme   Evaluation Scheme
Lecture   Practical
Tutorial   Internal Continuous Term   End
(Hours   (Hours
(Hours   Credit   Assessment (ICA)   Examinations (TEE)
per   per
per week)   (Marks-50)   (Marks-100 )
week)   week)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Course Objective -To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design concepts,
understand language recognition, symbol table management, semantic analysis and code
generation.
Course Outcomes- After completion of the course, students will be able to
1. Comprehend the working of lexical analysis, parsing,
2. Understand the significance of code generation and code optimization,
3. Implement working module of compiler.
Detailed Syllabus:
Unit   Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis (scanner):   07
Regular languages, finite automata, regular expressions, regular expression to
finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars, push-down   10
automata, LL(1) grammars and top-down parsing, operator grammars, LR(O),
SLR(1), LR(1), LALR(1) grammars and bottom-up parsing, ambiguity and LR
parsing, LALR(1) parser generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed   definition,   05
evaluation and flow of attribute in a syntax tree.
Signature
(Prepared by Concerned Faculty/HOD)   AY 2024-25
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
4.   Symbol Table: Basic structure, symbol attributes and management. Run-time   05
environment: Procedure activation, parameter passing, value return, memory
allocation, scope.
5.   Intermediate Code Generation: Translation of different language features,   04
different types of intermediate forms.
6.   Code Improvement (optimization): control-flow, data-flow dependence, local   05
optimization, global optimization, loop optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling (for   05
pipeline), loop optimization (for cache memory), Register allocation and
target code generation.
8.   Advanced topics: Type systems, data abstraction, compilation of Object   04
Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman, “Compilers: Principles, Techniques and Tools”, 2nd Edition,
Addison-Wesley, 2023.
2. Levine R. John, Tony Mason and Doug Brown, “Lex & Yacc”, 2nd Edition, O’Reilly media,
2007.
Reference Books:
1. Bjarne Stroustrup, “The Design and Evolution of C++” 2nd Edition, Addison-Wesley, 2007.
Laboratory Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus
Signature
(Prepared by Concerned Faculty/HOD)   AY 2024-25
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Computer Science and Business Systems)   Semester: V / / III III
````

## B TECH · Computer Science and Business Systems · AY 2023-24 · Sem 5

- Course as printed: Compiler Design (code 702CO0C028)
- Source: `00_Original_Downloads/SYLLABUS/B TECH/11961__3RD YEAR.zip :: CSBS/SEM V/B_Tech__CSBS__3rd_Year__Sem-V__A_Y_2023-24_qbUHNhefOT.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course - Compiler Design   Code: 702CO0C028
Teaching Scheme   Evaluation Scheme
Lecture   Practical
Tutorial   Internal Continuous Term   End
(Hours   (Hours
(Hours   Credit   Assessment (ICA)   Examinations (TEE)
per   per
per week)   (Marks-50)   (Marks-100 )
week)   week)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Course Objective -To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design concepts,
understand language recognition, symbol table management, semantic analysis and code
generation.
Course Outcomes- After completion of the course, students will be able to
1. Comprehend the working of lexical analysis, parsing,
2. Understand the significance of code generation and code optimization,
3. Implement working module of compiler.
Detailed Syllabus:
Unit   Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis (scanner):   07
Regular languages, finite automata, regular expressions, regular expression to
finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars, push-down   10
automata, LL(1) grammars and top-down parsing, operator grammars, LR(O),
SLR(1), LR(1), LALR(1) grammars and bottom-up parsing, ambiguity and LR
parsing, LALR(1) parser generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed   definition,   05
evaluation and flow of attribute in a syntax tree.
Signature
(Prepared by Concerned Faculty/HOD)   AY 2023-24
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
4.   Symbol Table: Basic structure, symbol attributes and management. Run-time   05
environment: Procedure activation, parameter passing, value return, memory
allocation, scope.
5.   Intermediate Code Generation: Translation of different language features,   04
different types of intermediate forms.
6.   Code Improvement (optimization): control-flow, data-flow dependence, local   05
optimization, global optimization, loop optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling (for   05
pipeline), loop optimization (for cache memory), Register allocation and
target code generation.
8.   Advanced topics: Type systems, data abstraction, compilation of Object   04
Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman, “Compilers: Principles, Techniques and Tools”, 2nd Edition,
Addison-Wesley, 2006.
2. Levine R. John, Tony Mason and Doug Brown, “Lex & Yacc”, 2nd Edition, O’Reilly media,
2007.
Reference Books:
1. Bjarne Stroustrup, “The Design and Evolution of C++” 2nd Edition, Addison-Wesley, 2007.
Laboratory Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus
Signature
(Prepared by Concerned Faculty/HOD)   AY 2023-24
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Computer Science and Business Systems)   Semester: V
````

## B TECH · Computer Science and Business Systems · AY 2021-22 · Sem 5

- Course as printed: Compiler Design (code BTCS05004)
- Source: `04_Syllabi_Archive/B TECH/3RD YEAR/CSBS/SEM V/B. Tech CSBS, 3rd Yrar, Sem V, A.Y 2021-22.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course - Compiler Design   Code: BTCS05004
Teaching Scheme   Evaluation Scheme
Lecture   Practical Tutorial   Internal   Term   End
(Hours   (Hours   (Hours   Continuous   Examinations (TEE)
Credit
per   per   per   Assessment (ICA)   (Marks-100
week)   week)   week)   (Marks-50)   in Question Paper)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Objectives -To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design concepts,
understand language recognition, symbol table management, semantic analysis and
code generation.
Course Outcomes- After completion of the course, students will be able to
1. Comprehend the working of lexical analysis, parsing,
2. Understand the significance of code generation and code optimization,
3. Implement working module of compiler.
Detailed Syllabus:
Unit Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis   07
(scanner): Regular languages, finite automata, regular expressions,
regular expression to finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars,   10
push-down automata, LL(1) grammars and top-down parsing,
operator grammars, LR(O), SLR(1), LR(1), LALR(1) grammars and
bottom-up parsing, ambiguity and LR parsing, LALR(1) parser
generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed definition,   05
evaluation and flow of attribute in a syntax tree.
4. Symbol Table: Basic structure, symbol attributes and management.   05
Run-time environment: Procedure activation, parameter passing,
value return, memory allocation, scope.
B. Tech CSBS /Sem V /A.Y 2021-22 /Page 3
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
5.   Intermediate Code Generation: Translation of different language   04
features, different types of intermediate forms.
6. Code   Improvement   (optimization):   control-flow,   data-flow   05
dependence,   local   optimization,   global   optimization,   loop
optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling   05
(for pipeline), loop optimization (for cache memory), Register
allocation and target code generation.
8. Advanced topics: Type systems, data abstraction, compilation of   04
Object Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman, “Compilers: Principles, Techniques and Tools”,
2nd Edition, Addison-Wesley, 2006.
2. Levine R. John, Tony Mason and Doug Brown, “Lex & Yacc”, 2nd Edition,
O’Reilly media, 2007.
Reference Books:
1. Bjarne Stroustrup, “The Design and Evolution of C++” 2nd Edition, Addison-
Wesley, 2007.
Any other information:
Details of Internal Continuous Assessment (ICA)
Total Marks of Internal Continuous Assessment (ICA) : 50 Marks
Distribution of ICA Marks :
Description of ICA   Marks
Test   20
Term Work   30
Total Marks   50
_________   ____________
Signature   Signature
(Prepared by Concerned Faculty/HOD)   (Approved by Dean)
B. Tech CSBS /Sem V /A.Y 2021-22 /Page 4
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Computer Science and Business   Semester: V
Systems)
````

## MBA Tech · Artificial Intelligence · batch 2021-2026 · Sem 5

- Course as printed: Compiler Design (code 702AI0E001)
- Source: `04_Syllabi_Archive/MBA Tech/ARTIFICIAL INTELLIGENCE/BATCH (2021-2026)/Semester 5.pdf`, page 7-9

````text
Program: B Tech/MBA Tech Artificial Intelligence,   Semester: V
B Tech AI and DS
Course: Compiler Design   Code: 702AI0E001
Teaching Scheme   Evaluation Scheme
Lecture Practical Tutorial   Internal Continuous   Term End Examinations
(Hours   (Hours   (Hours   Credit   Assessment (ICA)   (TEE)
per   per   per
week)   week)   week)   (Marks - 50)   (Marks - 100)
2   2   0   3   Marks Scaled to 50   Marks Scaled to 50
Prerequisite: Knowledge of Programming
Course Objective
This course provides the foundation of compilers, helps to learn programming language
translation and compiler design concepts. It helps to understand language recognition, symbol
table management, semantic analysis and code generation.
Course Outcomes
After completion of the course, students will be able to -
1. Describe the working of the lexical analyzer.
2. Design the functionalities of the syntax and semantic parsers.
3. Describe the procedure of symbol table management and code generation.
4. Analyze the code optimization techniques.
Detailed Syllabus
Unit   Description   Duration
1   Introduction   04
Overview of the phases of compiler, Lexical Analysis (scanner): Regular
languages, Finite automata, regular expressions, regular expression to
finite automata, scanner generator (lex, flex).
2   Syntax Analysis (Parser)   08
Context-free languages and grammars, push-down automata, LL(1)
grammars and top-down parsing, operator grammars, LR(O), SLR(1),
LR(1), LALR(1) grammars and bottom-up parsing, ambiguity and LR
parsing, LALR(1) parser generator (yacc, bison)
3   Semantic Analysis   06
Attribute grammars, syntax directed definition, evaluation and flow of
attribute in a syntax tree.
4   Symbol Table   02
Basic structure, symbol attributes and management. Run-time
environment: Procedure activation, parameter passing, value return,
memory allocation, scope.
Signature
(Prepared by Concerned Faculty/HOD)
B Tech AI / Semester-V / AY 2023-24 / Page 7
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
5   Intermediate Code Generation   03
Translation of different language features, different types of
intermediate forms.
6   Code Improvement (optimization)   03
Control-flow, data-flow dependence, Optimization techniques: local
optimization, global optimization, loop optimization, peep-hole
optimization.
7   Architecture dependent code improvement   02
Instruction scheduling (for pipeline), Cache memory optimization,
Register allocation and target code generation.
8   Advanced topics   02
Data abstraction, compilation of Object-Oriented features and non-
imperative programming languages
Total   30
Text Books
1. V. Aho, R. Sethi and J. Ullman, Compilers: Principles, Techniques and Tools, 2nd Edition,
Addison-Wesley, 2013.
2. Levine R. John, Tony Mason and Doug Brown, Lex & Yacc, 2nd Edition, O’Reilly, 2010
(Classic)
Reference Books
1. Bjarne Stroustrup, The Design and Evolution of C++, 2nd edition, Addison-Wesley, 2012.
2. K. L. P Mishra, N. Chandrashekaran, Theory of computer science- Automata Languages and
computation, 3rd edition, Prentice Hall of India, 2013
3. Andrew W. Appel, Modern Compiler Implementation in C, 1st edition Cambridge
University Press, 2010 (Classic)
Laboratory/ Tutorial Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus.
Signature
(Prepared by Concerned Faculty/HOD)
B Tech AI / Semester-V / AY 2023-24 / Page 8
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Artificial Intelligence, Data Science, Semester: IV/V/VI
Computer Engineering, Information Technology, CSE
(Cyber), AI and ML, AI and DS, CSE (DS))
MBA Tech All Programs
````

## B TECH WORK IN PROCESS · Artificial Intelligence · batch 2020-2024 · Sem 5

- Course as printed: Compiler Design
- Source: `04_Syllabi_Archive/B TECH WORK IN PROCESS/Artificial Intelligence/Batch 2020 - 2024/Semester - 5.pdf`, page 7-9

````text
Program: B Tech Artificial Intelligence   Semester: V
Course: Compiler Design   Code:
Teaching Scheme   Evaluation Scheme
Lecture Practical Tutorial   Internal Continuous   Term End Examinations
(Hours   (Hours   (Hours   Credit   Assessment (ICA)   (TEE)
per   per   per
week)   week)   week)   (Marks - 50)   (Marks - 100)
2   2   0   3   Marks Scaled to 50   Marks Scaled to 50
Prerequisite: Knowledge of Programming
Course Objective
This course provides the foundation of compilers, helps to learn programming language
translation and compiler design concepts. It helps to understand language recognition, symbol
table management, semantic analysis and code generation.
Course Outcomes
After completion of the course, students will be able to -
1. Describe the working of the lexical analyzer.
2. Design the functionalities of the syntax and semantic parsers.
3. Describe the procedure of symbol table management and code generation.
4. Analyze the code optimization techniques.
Detailed Syllabus
Unit   Description   Duration
1   Introduction   04
Overview of the phases of compiler, Lexical Analysis (scanner): Regular
languages, Finite automata, regular expressions, regular expression to
finite automata, scanner generator (lex, flex).
2   Syntax Analysis (Parser)   08
Context-free languages and grammars, push-down automata, LL(1)
grammars and top-down parsing, operator grammars, LR(O), SLR(1),
LR(1), LALR(1) grammars and bottom-up parsing, ambiguity and LR
parsing, LALR(1) parser generator (yacc, bison)
3   Semantic Analysis   06
Attribute grammars, syntax directed definition, evaluation and flow of
attribute in a syntax tree.
4   Symbol Table   02
Basic structure, symbol attributes and management. Run-time
environment: Procedure activation, parameter passing, value return,
memory allocation, scope.
Signature
(Head of the Department)
B Tech AI / Semester-V / 2022-23 / Page 7
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
5   Intermediate Code Generation   03
Translation of different language features, different types of
intermediate forms.
6   Code Improvement (optimization)   03
Control-flow, data-flow dependence, Optimization techniques: local
optimization, global optimization, loop optimization, peep-hole
optimization.
7   Architecture dependent code improvement   02
Instruction scheduling (for pipeline), Cache memory optimization,
Register allocation and target code generation.
8   Advanced topics   02
Data abstraction, compilation of Object-Oriented features and non-
imperative programming languages
Total   30
Text Books
1. V. Aho, R. Sethi and J. Ullman, Compilers: Principles, Techniques and Tools, 2nd Edition,
Addison-Wesley, 2013.
2. Levine R. John, Tony Mason and Doug Brown, Lex & Yacc, 2nd Edition, O’Reilly, 2010
(Classic)
Reference Books
1. Bjarne Stroustrup, The Design and Evolution of C++, 2nd edition, Addison-Wesley, 2012.
2. K. L. P Mishra, N. Chandrashekaran, Theory of computer science- Automata Languages and
computation, 3rd edition, Prentice Hall of India, 2013
3. Andrew W. Appel, Modern Compiler Implementation in C, 1st edition Cambridge
University Press, 2010 (Classic)
Laboratory/ Tutorial Work
8 to 10 experiments (and a practicum where applicable) based on the syllabus.
Signature
(Head of the Department)
B Tech AI / Semester-V / 2022-23 / Page 8
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech Artificial Intelligence   Semester: V
B Tech and MBA Tech Computer Engineering   V
````

## B TECH WORK IN PROCESS · Computer Science and Business Systems · batch 2020-2024 · Sem 5

- Course as printed: Compiler Design (code 702CO0C028)
- Source: `04_Syllabi_Archive/B TECH WORK IN PROCESS/Computer Science and Business Systems/Batch 2020 - 2024/Semester - 5.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course - Compiler Design   Code: 702CO0C028
Teaching Scheme   Evaluation Scheme
Lecture   Practical Tutorial   Internal   Term   End
(Hours   (Hours   (Hours   Continuous   Examinations (TEE)
Credit
per   per   per   Assessment (ICA)   (Marks-100
week)   week)   week)   (Marks-50)   in Question Paper)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Objectives -To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design concepts,
understand language recognition, symbol table management, semantic analysis and
code generation.
Course Outcomes- After completion of the course, students will be able to
1. Comprehend the working of lexical analysis, parsing,
2. Understand the significance of code generation and code optimization,
3. Implement working module of compiler.
Detailed Syllabus:
Unit Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis   07
(scanner): Regular languages, finite automata, regular expressions,
regular expression to finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars,   10
push-down automata, LL(1) grammars and top-down parsing,
operator grammars, LR(O), SLR(1), LR(1), LALR(1) grammars and
bottom-up parsing, ambiguity and LR parsing, LALR(1) parser
generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed definition,   05
evaluation and flow of attribute in a syntax tree.
4. Symbol Table: Basic structure, symbol attributes and management.   05
Run-time environment: Procedure activation, parameter passing,
value return, memory allocation, scope.
B. Tech CSBS /Sem V /A.Y 2022-23 /Page 3
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
5.   Intermediate Code Generation: Translation of different language   04
features, different types of intermediate forms.
6. Code   Improvement   (optimization):   control-flow,   data-flow   05
dependence,   local   optimization,   global   optimization,   loop
optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling   05
(for pipeline), loop optimization (for cache memory), Register
allocation and target code generation.
8. Advanced topics: Type systems, data abstraction, compilation of   04
Object Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman, “Compilers: Principles, Techniques and Tools”,
2nd Edition, Addison-Wesley, 2006.
2. Levine R. John, Tony Mason and Doug Brown, “Lex & Yacc”, 2nd Edition,
O’Reilly media, 2007.
Reference Books:
1. Bjarne Stroustrup, “The Design and Evolution of C++” 2nd Edition, Addison-
Wesley, 2007.
Laboratory Work
8 to 10 experiments ( and a practicum where applicable) based on the syllabus
_________   ____________
Signature   Signature
(Prepared by Concerned Faculty/HOD)   (Approved by Dean)
B. Tech CSBS /Sem V /A.Y 2022-23 /Page 4
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Computer Science and Business   Semester: V
Systems)
````

## B TECH WORK IN PROCESS · Computer Science and Business Systems · batch 2019-2023 · Sem 5

- Course as printed: Compiler Design (code BTCS05004)
- Source: `04_Syllabi_Archive/B TECH WORK IN PROCESS/Computer Science and Business Systems/Batch 2019 - 2023/Semester - 5.pdf`, page 3-5

````text
Program: B Tech (Computer Science and Business Systems)   Semester: V
Course: Compiler Design   Code: BTCS05004
Teaching Scheme   Evaluation Scheme
Lecture   Practical Tutorial   Internal   Term   End
(Hours   (Hours   (Hours   Continuous   Examinations (TEE)
Credit
per   per   per   Assessment (ICA)   (Marks-100
week)   week)   week)   (Marks-50)   in Question Paper)
3   2   0   4   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Formal language and automata theory (BTCS01001)
Objectives:
1. To Provide the foundation for understanding the theory and practice of
compilers, learn programming language translation and compiler design
concepts,
2. Understand language recognition, symbol table management, semantic analysis
and code generation.
Outcomes: After completion of the course, students will be able to:
1. Comprehend the working of lexical analysis, parsing.
2. Understand the significance of code generation and code optimization.
3. Implement working module of compiler
Detailed Syllabus: ( per session plan )
Unit Description   Duration
1.   Introduction: Phases of compilation and overview. Lexical Analysis   07
(scanner): Regular languages, finite automata, regular expressions,
regular expression to finite automata, scanner generator (lex, flex).
2.   Syntax Analysis (Parser): Context-free languages and grammars,   10
push-down automata, LL(1) grammars and top-down parsing,
operator grammars, LR(O), SLR(1), LR(1), LALR(1) grammars and
bottom-up parsing, ambiguity and LR parsing, LALR(1) parser
generator (yacc, bison)
3.   Semantic Analysis: Attribute grammars, syntax directed definition,   05
evaluation and flow of attribute in a syntax tree.
B. Tech CSBS /Sem V /A.Y 2021-22 /Page 3
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
4. Symbol Table: Basic structure, symbol attributes and management.   05
Run-time environment: Procedure activation, parameter passing,
value return, memory allocation, scope.
5.   Intermediate Code Generation: Translation of different language   04
features, different types of intermediate forms.
6. Code   Improvement   (optimization):   control-flow,   data-flow   05
dependence,   local   optimization,   global   optimization,   loop
optimization, peep-hole optimization.
7.   Architecture dependent code improvement: instruction scheduling   05
(for pipeline), loop optimization (for cache memory), Register
allocation and target code generation.
8. Advanced topics: Type systems, data abstraction, compilation of   04
Object Oriented features and non-imperative programming languages
Total   45
Text Books:
1. V. Aho, R. Sethi and J. Ullman “Compilers: Principles, Techniques and Tools”,
2nd Edition, Boston, Massachusetts, USA: Addison-Wesley, 2006.
2. Levine R. John, Tony Mason and Doug Brown “Lex & Yacc”, 2nd Edition,
O’Reilly media, 2007.
Reference Books:
1. Bjarne Stroustrup “The Design and Evolution of C++” 2nd edition, Addison-
Wesley, 2007.
Any other information :
Total Marks of Internal Continuous Assessment (ICA) : 50 Marks
Distribution of ICA Marks :
Description of ICA   Marks
Test 1   10
Test 2   10
Term Work   30
Total Marks   50
_________   ____________
Signature   Signature
(Prepared by Concerned Faculty/HOD)   (Approved by Dean)
B. Tech CSBS /Sem V /A.Y 2021-22 /Page 4
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech (Computer Science and Business   Semester: V
Systems)
````
