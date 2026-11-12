# Compiler Design: question papers in full

16 unique papers · 2022-23 to 2025-26 · Computer Science and Business Systems, Computer Engineering, Computer Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 5 · paper 66b6ba2caba6

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Compiler Design/QP_Compiler Design(702CO0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Compiler Design
Date: 08 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1 ;   a.   [5]
Describe the major tasks performed by the front end and back end of a
SO-1 ;   compiler.
BL-1
CO-1 ;   b.   [5]
Explain the rules to compute CLOSURE() and GOTO() functions in LR
SO-1 ; BL-   parsers
2
CO-1 ;   c.   [5]
“SDD is a context-free grammar together with attributes and rules”.
SO-6 ; BL-   Justify the statement with a suitable example.
5
CO-2 ;   d.   [5]
What properties an intermediate representation should satisfy? List some
SO-1 ; BL-   high level and low-level representations
2
A   Illustrate with the help of an example the problem caused due to left
recursive grammar in a recursive descent parser. For the given grammar,
eliminate the left recursion problem.
G→ E
Q2
E→ E+T   [10]
CO-1; SO-
6; BL-3   E → T
T → E * T
T→ id
Q2   B   [10]
Explain any four function preserving optimization techniques with
CO-2; SO-   suitable example for each.
1; BL-2
********** 1 **********
--- page 2 ---
A   Explain how the tokens are specified and recognized in lexical analysis
phase of a compiler? For the given code segment, list down the
lexemes, token class and count the total number of tokens.
main()
{
Q3
char ch=’A’;   [10]
CO-1; SO-
6; BL-4   int x , y;
x=y=20;
x++;
printf (“%d %d”, x, y);
}
B   Define Syntax directed definition and Syntax directed translation.   [10]
Determine whether the given Syntax directed definition is S-attributed
or L-attributed definition. Justify your answer
Production   Semantic Rule
Q3
L.i := f1(A.i)
CO-1; SO-   A   L M   M.i := f2(L.s)
6; BL-5   A.s := f3(M.s)
R.i := f4(A.i)
A   Q R   Q.i := f5(R.s)
A.i := f6(Q.s)
Q4   A
CO-1; SO-   What are top-down parsers? Write the algorithm for constructing the   [10]
Predictive parsing table
1; BL-2
B   Explain how basic blocks and flow graphs help in optimization process?   [10]
Analyze the given code segment and find the basic blocks:
W=0;
X = x + y;
Y = 0;
If( x>z)
Q4   {
CO-2; SO-   Y=x;
X++;
6; BL-4   }
Else
{
Y=z;
Z++;
}
W=x+z;
********** 2 **********
--- page 3 ---
A   Determine whether the given grammar is LR (1) or not
Q5
S → Aa |bAc |Bc |bBa   [10]
CO-1; SO-
6; BL-5   A → d
B → d
Q5   B   [10]
Discuss the structure of an activation record and its role in procedure
CO-3; SO-   activation.
1; BL-2
A   Translate the given expression into three address code. Show the entries
Q6   of data structures: quadruples and triples
[10]
CO-2; SO-   (i)   a+(b-c) + (b-c) * d
6; BL-3
(ii)   x= a+ (b-c) *d +e
Q6   B   [10]
Explain the concept of memory management and instruction selection
CO-2; SO-   with respect to code generation
1; BL-2
A   Consider the following grammar.
Q7   S → AB
A → Aa | a
CO-1; SO-   B → Bb| b   [10]
6; BL-3   Parse the input string “aaabb” using stack implementation of shift-
reduce parser
Q7   B
CO-3; SO-   Write a note on: Compilation of object-oriented features   [10]
1; BL-2
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 5 · paper ebf52af3272f

- Departments: Computer Engineering, Computer Science and Business Systems
- Programmes: B TECH / COMPUTER, B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/COMPILER DESIGN/Compiler Design, Sem-V, Year 2025-26, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: ocr (3 pages), mean OCR confidence 82.9

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: I1/Semester V(Exam Year: 2025-2026) .
Subject: Compiler Design ;
Date: 08 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions: ‘

1. This question paper contains 3 pages.

2. Question No._1___ is compulsory.

3. Out of remaining questions, attempt any 4 _ questions.

4. Inall___5_ questions to be attempted.

5. All questions carry equal marks.

6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right hand side indicate full marks.

8. Assume Suitable data if necessary.

Ql a

Answer briefly: [20]
cO-1; a. . . [5]
50-1: Describe the major tasks performed by the front end and back end of a
BL-1 compiler.
CO-1; b. . . [5]
50-1: BL- Explain the rules to compute CLOSURE() and GOTO() functions in LR
5 , parsers
CO-1; 6 [5]

“SDD is a context-free grammar together with attributes and rules”.

-6 ; BL- : f :
50-6; BL Justify the statement with a suitable example.

CO-2; d. : : . . . , 5
50-1 - BL- What properties an intermediate representation should satisfy? List some [5]

high level and low-level representations

2
A Illustrate with the help of an example the problem caused due to left
recursive grammar in a recursive descent parser. For the given grammar,
eliminate the left recursion problem.
GOE
e E> E+T
+
CO-1; SO- [10]
6; BL-3 EDT
TOE*T
T> id
Q2.. B . * [10]
Explain any four function preserving optimization techniques with
CO-2; SO- suitable example for each.
1; BL-2

SI aR aaa a kee
--- page 2 ---
A Explain how the tokens are specified and recognized in lexical analysis
phase of a compiler? For the given code segment, list down the
lexemes, token class and count the total number of tokens.

main() < ow
Q3 ;
char ch=’A’;
CO-1; SO- (10]
6; BL-4 int X,Y;
x=y=20; . -
xa;
printf (“%d %d”, x, y);
}
B Define Syntax directed definition and Syntax directed translation. [10]
Determine whether the given Syntax directed definition is S-attributed
or L-attributed definition. Justify your answer
Production Semantic Rule
Q3
Li 2= fi(A.i)
CO-1; SO- '-—> :
A LM M.i -= fo(L.s)
6; BL-5 A.s := f3(M.s)
} \ Ri 2= f4(A.i)
A OR Q.i := f5(R.s)
A.i := fo(Q.5)
Q4 A
CO-1; SO- What are top-down parsers? Write the algorithm for constructing the [10]
Predictive parsing table
1; BL-2
B Explain how basic blocks and flow graphs help in optimization process? | [10]
Analyze the given code segment and find the basic blocks:
W=0; ,
X=xty;
Y =0;
If( x>z)
Q4 f
CO-2; SO- Y=x;
X+4;
6; BL-4 }
Else
{
Y=z;
‘ Z++; :
“ }
W=x+z;

FRR ICR FO OK
--- page 3 ---
A Determine whether the given grammar is LR (1) or not

Q5
CO-1: 50- S > Aa |bAc |Bc |bBa [10]
6; BL-5 Add . ,
Bod a
B : woe : . 10
a: so- Discuss the structure of an activation record and its role in procedure [10]
1: BL2 activation.
A Translate the given expression into three address code. Show the entries
Q6 of data structures: quadruples and triples ~ |,
: 10
CO-2; SO- (i) at+(b-c) + (b-c) * d no)
6; BL-3
(ii) x=a+t (b-c) *d+e
Q6 B [10]
Explain the concept of memory management and instruction selection
CO-2; SO- with respect to code generation
lon 1; BL-2
A Consider the following grammar.
Q7 S> AB
A> Aala .
CO-1; SO- B> Bb| b [10]
6; BL-3 Parse the input string “aaabb” using stack implementation of shift-
reduce parser
Q7 B
CO-3; SO- Write a note on: Compilation of object-oriented features [10]
1; BL-2

FIO GARR ee
````

## 2025-26 · Re-Exam · Sem 5 · paper e6f45eaddf8d

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSBS_7036/Compiler Design/QP_Compiler Design(702CO0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Compiler Design
Date: 11 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1 ;   a.
Describe the major tasks performed during the analysis and synthesis [5]
SO-1 ;   phases of compilation.
BL-1
CO-1 ;   b.   [5]
Explain the rules to compute FIRST() and FOLLOW() sets on grammar
SO-1 ; BL-   symbols?
2
CO-1 ;   c.   [5]
“Every S-attributed definition is also L-attributed definition” Justify the
SO-6 ; BL-   statement with a suitable example.
5
CO-2 ;   d.   [5]
SO-1 ; BL-   Show the need for an Intermediate code generator phase in compilers.
2
A   Illustrate with the help of an example the problem caused due to a non-
deterministic grammar. For the given grammar, apply left factoring to
eliminate non-determinism
E → T + E
Q2
E → T
[10]
CO-1; SO-
6; BL-3   T → int
T → int * T
T → ( E )
Q2   B   Explain any four loop optimization techniques with suitable example   [10]
CO-2; SO-   for each.
1; BL-2
********** 1 **********
--- page 2 ---
A   Explain the role of regular expressions and finite automata in lexical [10]
analysis phase of a compiler? For the given code segment, list down the
lexemes, token class and count the total number of tokens.
Q3
CO-1; SO-   int a = 10;
6; BL-4
Float b = 20.5;
printf (“C=%d, d=%”, ++a, b++);
B   Define synthesized and inherited attributes. Identify whether the given   [10]
Syntax directed definition is S-attributed or L-attributed definition.
Justify your answer
Q3
CO-1; SO-
6; BL-5
Q4   A   [10]
Explain in brief the different types of top-down parsers? Describe the
CO-1; SO-   role of different components of predictive parser model
1; BL-2
B   Write the algorithm to find the basic blocks in a program. Analyze the [10]
given three address code and find the basic blocks:
1. i=1
2. If i<= n goto 4
3. Goto 9
Q4
4. R1= a *b
CO-2; SO-
6; BL-4   5. R2= r1+c
6. X=r2
7. J=j+1
8. Goto 2
9. K=k*2
********** 2 **********
--- page 3 ---
A   Determine whether the given grammar is LR (1) or not.   [10]
Q5
S → Aa |bAc |dc |bda
CO-1; SO-
6; BL-5   A → d
Q5   B   Discuss the various data structures used for implementing a symbol   [10]
CO-3; SO-   table in a compiler.
1; BL-2
A   Translate the given expressions into three address code. Show the   [10]
Q6   entries of data structures: quadruples and triples
CO-2; SO-   (i)   a+b*c-d/(b*c)
6; BL-3
(ii)   a = (-b + c*d) + (c*d)
Q6   B   Explain the concept of register allocation and evaluation order with   [10]
CO-2; SO-   respect to code generation
1; BL-2
A   Consider the following grammar:
S→ aABe
Q7
A → Abc |b   [10]
CO-1; SO-   B → d
6; BL-3   Parse the input string “abbcde” using stack implementation of shift-
reduce parser
Q7   B   Write a note on: Imperative and Non-imperative programming
[10]
CO-3; SO-   languages
1; BL-2
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 41007857fc71

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CS_7055/Compiler Design/QP_Compiler Design(702CS0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (4 pages), mean OCR confidence 82.4

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Compiler Design
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
Section A
Q1
CO-1 A What is a compiler? Which is the optional phase of the compiler? What will be   [5]
BL-2   the output of each phase of the compiler for the expression, R = (a + b - c) / 2
CO-2 B What is a backtracking parser? Consider the following grammar to parse the   [5]
BL-4   string ‘aaba’ and demonstrate how a backtracking parser works. It always
attempts all productions in order.
A→ abC | aBd |aAD
B→ bB | ϵ
C→d | ϵ
D→a | b | ϵ
CO-3 C   Construct a DAG and three-address code for the following expression.   [5]
BL-3   x+x*(y-z)+(y-z)*a
CO-3 D Explain the allocation strategies, viz, heap, static, and stack.   [5]
BL-3
Section B
Q2
CO-2 A What is an LR parser? Explain how it works. How are they categorized?
BL-4   Comment on the power of the LR parser.   [10]
********** 1 **********
--- page 2 ---
B Give a syntax-directed definition for constructing a syntax tree, and build a syntax
CO-3   tree using semantic rules for the expression x/y + 10-z by considering the
BL-3   following grammar. Comment on S tributed or L attributed grammar.
[10]
E → E+T| E-T |T
T → T*F | T/F |F
F → id | num
Q3
CO-2 A Analyze how the lexical analysis phase of a compiler works by examining the
BL-4   given C++ program. Identify the actions it takes and the errors it finds, explaining
why these errors occurred. Also, describe the roles of the lexical analyzer.
/* Test Code*/
int main( ){
int num1,num 2, a d d, float;   // variable declaration   [10]
cin>>num1>>num2;
add = num1++ num2;
cout<<"add = "<<add;
return 0;
}
CO-3 B What is Peephole Optimization? Explain how it involves eliminating redundant
BL-3   instructions, flow-of-control optimizations such as multiple jumps, algebraic
[10]
simplifications, use of machine idioms, and elimination of unreachable code, with
suitable examples.
Q4
CO-2 A Construct a Simple LR Parsing Table for Grammar A→ aAa | bAb | ba
[10]
BL-4
CO-3 B The following code is meant to be input for the compiler's code optimization
BL-3   phase. What various optimization techniques should the optimization phase apply
to the given code, and what will be the resulting optimized code?
int main( ) {
int a = 10, b = 20, c = 30, x, y, z;   [10]
x = (a * b) + (a * b) +(a * b) ;
y = c * 5;
z = y / 5;
for (int i = 0; i < 10; i++) {
********** 2 **********
--- page 3 ---
int t = a * b;
cout << t << endl;
}
for (int i = 0; i < 5; i++) {
int p = i + 1;
int q = i + 2;
cout << p + q << endl;
}
int m = 5 * 3;
int n = m * 2;
cout<<m<<n;
int unused = n + 100;
return 0;
}
Q5
CO-3 A
List the sources of optimization and explain the optimization of basic blocks.   [10]
BL-3
CO-3 B Explain the topics related to run-time storage management: subdividing run-time
[10]
BL-3   memory, activation records, and activation trees.
Q6
CO-3 A What are Flow-of-Control Statements and Control-Flow Translation of Boolean
[10]
BL-3   Expressions concerning control flow?
CO-2 B Show that the following grammar is LL(1) but not LR(0).
BL-4   S → AaAb | BbBa
[10]
A → ϵ
B → ϵ
Q7
CO-1 A
What is a language processing system? Explain.   [5]
BL-2
CO-2 B   Differentiate between token specification and token recognition in lexical   [5]
BL-4   analysis. Analyze how regular expressions and finite automata are used to
recognize identifiers.
CO-2 C   Construct the table for the operator precedence parser   [5]
BL-4   S → (L) | a
L → L,S | S
********** 3 **********
--- page 4 ---
CO-3 | D | What are Type Inference and Polymorphic Functions? Explain [5]
BL-3

FIC 7) IC HOH
````

## 2024-25 · Final-Exam · Sem 5 · paper 1ab68855d104

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/COMPILER DESIGN/Compiler Design, Sem-V, Final Exam 2024-25.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 81.8

````text
MPSTM®
SVKM’S NMIMS L IBRARY

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS E
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

¥

,

Program/s: B.Tech (CSBS) Year: I[L___ Semester: __V.
Stream/s ;_ Computer

Subject: Compiler Design : Time: 3 hrs (2:00 pm to_5:00 pm)
Date:_27/ 11/2024 No. of Pages: 3-0

Marks: 100

Final Examination (2024 -25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

(©) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4 __ questions. ~
3) Inall___5_ questions to be attempted. "ey
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql .
Answer briefly: ‘ [20]
a. Which phase(phases) of a compiler {5]
CO-3 ; i) Is/are considered backend of a compiler -
SO-1; : ii) Checks for type mismatches
BL-2 iii) Access(es) the symbol table
iv) Is/are independent of the underlying machine
|CO-1 ; b. : ; (5]
30-1; What is recursive descent parser? List the problems faced in designing such
BL-3 a parser.
at a e Give the algorithm for identifying leaders and partition the code into basic [5]
BL2- blocks
CO-2 ; d. . ; : : . .
SO-1: List the different intermediate code representations. Justify the role of [5]
BL- 4 Intermediate code generator phase in compiler design
Q2 A [10]
CO-1; ___| Discuss in detail the actions performed by a Shift-reduce parser. What are
SO-1; the common conflicts encountered in a Shift reduce parser?
BL-2

1/3
--- page 2 ---
¥ [10]
(i) | Write TAC for the given (a+b)/(c-d) *(e+f)

statement along with quadruple

and triples representation

CO-2: (ii) | Write TAC for the code: if(p>q) {
BL ee
: } else if (p =q) {
r=p+q
} else {
r=p*q;
; }
Q3 A Explain the role of each phase of the compiler in brief and show the output [10]
CO-3; of each phase for the given expression:
SO-4; q = (x2 - x1).+ (y2-ylV/a
BL-4 .
B Distinguish between machine dependent optimization and machine [10]
CO-2; independent optimization? Explain the following techniques with an
SO-2; example: :
(i) Code motion ;
BL-4 . oo. *
(ii) Induction variable elimination
Q4 A ; [10]
CO-1: Differentiate between tokens, lexemes and patterns. Discuss how regular
SO. 6 expressions and finite automata is used to represent tokens and perform
BL- 4 Lexical analysis with examples
B Explain the two notations used to provide semantic information and [10]
annotated parse tree.
For the given Grammar, determine whethier it is L-attributed or S-attributed
grammar with reasons. Here, t and b are the attributes
= Production rule Semantic Rules
-1; a
SO-6; TD BC T.t= Ct
BL-4 | | C.b=Bt
B > INT B.t= Integer
res B>REAL | Bt=Real
C > [NUM]C, Ci.b = C.b

2/3
--- page 3 ---
ii) Data abstraction

For the given grammar: [10]
S + AcB
Qs A> aA
CO-1; A>e
SO-6;
BL-4 B>bBS
Boe
Determine whether the grammar is LL(1) or not
Co-2; Discuss the following: [10]
SO-1;, (i) Storage allocation strategies
BL? (ii) Parameter passing methods
Q6 y
CO-1; “, : . [10]
SO-1: What are LL(1) grammars? Write the LL (1) parsing algorithm
BL-2 :
: . Discuss the following:
CO-2; i Input to code generator
| SO-1; m . ert [10]
BL-2 (ii) Instruction selection
(iii) . Target program .
Consider the grammar G
Q7 S > Aa| bAc| Bc |bBa L
CO-1; ; 5 : [10]
SO-6; .
BL- 4 . i) Construct the DFA for LR(0) items
_ ii) Differentiate among the LR parser types
CO-3: Write short notes on: _
SO-1; i) Type systems [10]
BL-2 ;

3/3
````

## 2024-25 · Re-Exam · Sem 5 · paper 8a75367cdfc3

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/COMPILER DESIGN/Compiler Design, Sem-V, Batch 2024-25, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 87.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
Academic Year: 2024-2025

Program/s: B. Tech Year: III Semester: V
Stream/s : Computer Science

Subject: Compiler Design Time: 03:00 hrs(02:00pm to 05:00pm)
Date: 14 [2/25- No. of Pages:03
Marks: 100

ReExamination (24-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Solve the following

a. What are the responsibilities of the lexical analyzer? Provide the list and
count of tokens in the following C++ program.
//Program to display welcome message

CO-2 ; int main() { [05]
BL-2,4 float c= 0; //variable initialization
cout<< “Compiler Design”;
return 0;
}
CO-2; b. Consider the following LL (1) table and give the steps involved in parsing
BL-4 string w = ‘acdb’.
a b c d $ [05]
Ss S—aABb
A A~éE Ac Ae
B Bre Bd
CO-3; c. Generate the three-address code, quadruples, and triples for the following
BL- 2 expression. [05]
a=b*%(ct+d)* :
CO-3; d. What is code optimization? Why is it necessary? obtain the optimized code
BL-2 for the following. [05]
a=10
a=b*ctg;

Page 1/3
--- page 2 ---
d=100
d=b*c*e;

Q2
a. List the various phases of a compiler. Consider the statement
COl; itn, se 110]
BL-2 10
Give the output of each phase after compilation.
CO-1; b. How is memory divided into subdivisions? and outline the different fields [10]
BL-2 in the activation records?
Q3
CO-3; a. Write a note on types and declarations. [10]
BL-2
b. List the responsibilities of the parser and differentiate between the
CO-2; following.
BL-2 i Top-down parser and Bottom-up parser [10]
ii. Recursive decent parser and Predictive parser
iii. LR parser and Operator precedence parser
Q4
a. Outline the algorithm for a Recursive Decent Parser based on the provided
grammar G:
S—id=E ;
CO-2; E—- TPE’ [10]
BL-3 p’— +TE’ | €
T= FT’
T’ *FT’ |e
F—> id|(@)
CO-2; b. What is control flow? Explain the following with respect to the control flow: | [10]
BL-3 Boolean Expression, Short-Circuit Code, and Flow of Control Statement.
Q5
a. Using appropriate programming examples, explain how code
optimizations can be applied to the following:
CO-3; i. Loop invariant optimization
BL-2 ii. Loop Unrolling [10]
iii. Induction variable elimination
iv. Loop Jamming
v. _ Strength Reduction
b. Give syntax directed translation for the following grammar.
CO-3; D—-TL
BL-4 T= int|float [05]
LL, id
Lid

Page 2/3
--- page 3 ---
CO-1; c.

BL2 Discuss various strategies for storage allocation. [05]
Q6
a. Consider the following grammar
CO-2; G: . [10]
SAA
BL-4 pteren
Construct LALR(1) parsing table.
b. Consider the following source code for the dot product of two vectors and
provide the basic blocks and flowgraphs.
begin
prod =0
CO-2; i=l 6
BL-2,3 sOREES sere a
prod = prod + afi]*b[i]
i+=1]
end
while i<=20
end
Q7
CO-2; a. :
res Explain the buffer pair and sentinels concerning the input buffering. [10]
CO-3; b.
ae Write a brief explanation of the problems with the code generator. [05]
(ey Refer to the operator precedence relationship table below and use it to

calculate the precedence function.

eae: ia | + | * $ [05]
BL-4 id 7 = = =
+ < > < >
* < > > >
$ < < < -
x xX

Page 3/3
--- page 4 ---

````

## 2024-25 · Re-Exam · Sem 5 · paper 148864e54c4b

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/COMPILER DESIGN/Compiler Design, Sem-V, Batch 2024-25, Re Exam_148864e54c.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 86.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025

Program/s: B.Tech (CSBS) Year: III___ Semester: _V

Stream/s ;__ Computer
Subject: Compiler Design Time: 3 hrs (2:00 pm to_5:00 pm)
Date:_45 / 02/2025 No. of Pages: 3

Marks: 100

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
a. Which phase(phases) of a compiler [5]
CO-3 ; i) Is/are considered frontend of a compiler
SO-1 ; ii) Checks for scope
BL-2 ili) Have error handling routines
iv) Is/are dependent of the underlying machine
CO-1; b. [5]
SO- 1; Distinguish between LL and LR parsers
BL-3
CO-2 ; ch 7 : . P ; . [5]
SO- 1: Give the need for symbol table in compiler. Explain the different attributes
BL2. of a symboi table.
ie 2 a. What is a flow graph? Justify the role of flow graphs in optimization phase 5]
BL-4 of a compiler
Q2 A
CO-1; What is an Operator grammar? Explain the Operator precedence parsing [10]
SO-l; algorithm
BL-2
--- page 2 ---
B [10]
(i) | Write TAC for the given a*(b+c* (d—-e))

statement along with

quadruple and triples

CO-2; representation
SO-6;
ii) | Write TAC for the code: .
ee . a if(a+b>c) {
x=a*b;
} else {
x=c-(atb);
}
Q3 A Give the objective of each phase of the compiler and show the output of [10]
CO-3; each phase for the given expression:
SO-4; p=(atbtc) /(atb)
BL-4
CO-2; |B Distinguish between local optimization and global optimization. Explain [10]
the following techniques with an example:
SO-2; (i) Common sub-expression elimination
BL-4 (ii) Copy propagation
A Define tokens, lexemes and patterns. Give the regular expression for an | [10]
Identifier and an integer constant. And for the given code fragment, identify
Q4 ; the tokens and lexemes.
CO-1: switch({inputvalue)
SO-6; {
BL-4 case 1: b=c*d; break;
default : b = b++; break;
}
B Explain the role of dependency graph and the two type of attributes. [10]
For the given Grammar, determine whether it is L-attributed or S-attributed
grammar with reasons. Here, i and s are the attributes
Production rule Semantic Rules
CO-1; A> PQ P.i=A.it2
i Qi=PitAi
A.s = P.s +Q.s
A> XY Xi=Ait+Y.s
Yi=Xst+Ai
--- page 3 ---
A For the given grammar: [10]

Q5 S > AB |eDa
A> ab |c

CO-1; B> dc

SO-6; CPeCl[€

BL-4 D>fDI€

Determine whether the grammar is LL(1) or not

CO-2; B [10]
SO-I; What is runtime environment in compiler? Explain the structure of an

BL-2 activation record in detail

Q6 A [10]
CO-1; What does LR(k) parser mean? Write the algorithm for the construction of

SO-1; LR (0) parsing table

BL-2

B Discuss the following:

CO-2; i Memory management

SO-1; ° Poe [10]
BL-2 (ii) Register allocation

(iii) | Evaluation order
A Consider the Grammar G [10]

Q7 S>L=R[R
CO-1; L>*R|id
SO-6: ROL

BL- 4 (i) Explain the CLOSURE and GOTO functions

(ii) Construct the DFA for LR(0) items

CO-3: B Write short notes on: [10]
SO-1; i) Static and Dynamic Type systems

BL-2

ii) Imperative and Non-Imperative programming languages
--- page 4 ---

````

## 2023-24 · Final-Exam · Sem 5 · paper b1ffea1252bd

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/COMPILER DESIGN/Compiler Design, Sem-V, A Y 2023-24, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 21/11/2023
- Text: ocr (3 pages), mean OCR confidence 86.9

````text
|

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
Academic Year: 2023-2024

Program/s: B. Tech Year: HI Seiester: Vv

Stream/s : Computer Science

Subject: Compiler Design Time: 03 hrs (02:00pm to 05: Ope)
_ Date: 21/11/2023 . No. of Pages:03

Marks: 100

Final Examination, _

Instructions: Candidates should read carefully the instructions printed on _ question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
_ 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Solve the following.
oy } a How does the compiler translate statement a= b + c * 100? Write the output [05]
BL2 of each phase of the compiler.
CO-2 ; b.
SO-1; Define tokens, patterns, and lexemes, and provide an illustrative example (05]
BL-1
CO-3 ; c. What are the roles of a syntax analyzer? Explain
SO-1; [05]
BL-2 . *
id. Consider the following switch-case statement and convert it into three
address code. ;

CO-3; Switch(i+j){
SO-1; case 1:x=y+2 ; [05]
BL-3 default: p=q+r

case 2: v=u+w

}

Q2 a. Consider the grammar G
CO-2; ae
SO-1; eta a [10]
BL-3 ae

Show the top-down backtracking parser moves for input string ‘aaaaaa’
each. Parser tries production ‘aSa’ before ‘aa’.

1/3
--- page 2 ---
Translate the arithmetic expression: a* -(b+c) +d into on

CO-3; i. Syntax tree
SO-1; ii.   Quadruples [10]
BL-4 iii. Triples
iv. _ Indirect Triples
Q3 Create an LR(0) parsing table for the grammar below
CO-2; E> E+T|T [10]
SO-l; TD T*F/F
BL-6 F > (E)|id
CO-3: Define code generator and generate the code for the following statements
a2 for the target language : [10]
SO-1; : _
BL-6 i. X=a*btc
ii. X= f+(xt+y)*(atb)/(c-d)
Q4
Son What is the specification of a token? Explain it in details [10]
BL-2
CO-3; Provide a brief explanation of the specified optimization technique.
SO-1; i. Loop Unrolling [10]
BL-2 il. Elimination of Common Sub expression
iii. Dead Code Elimination
Q5 Give the pros and cons of an operator precedence parser. Examine the
CO-2; provided operator precedence table and create a graph depicting the
SO-1; precedence function and corresponding table.
BL-3
a -| / $ [10]
a - > > >
7 < > % > *
/ < > > >
$ < < < -
Consider following grammar:
CO-3; D OTL
SO-1; Tint {float [10]
BL-3 LOL, id |id
Construct syntax-directed translation scheme with inherited attribute and
show parse tree for input int x,y,z.
Q6 Describe the following allocation strategies.
CO-1; i. Static Allocation [10]
SO-1; ii. Stack Allocation
BL-2 iii. | Heap Allocation
eich Consider the following code fragment: [10]

2/3
--- page 3 ---
BL-4 f= ls
i=2;
while( i <= x){
f fi;
i++;
}
fact = f;

Obtain the basic block and flow graph for above code fragment, by

converting it to three address code first.

Q7 a. Distinguish between LL and LR parsers.

CO-2; [05]
SO-l; :

BL-4

CO-1; b.

SO-1; Write note on compiler construction tools [05]
BL-2

CO-3; i

ae What do you understand by Peephole Optimization? Explain [05]

CO-1; d.
SO-1; What is the subdivision of runtime memory? Describe in brief [05]

3/3

BL-2
````

## 2023-24 · Final-Exam · Sem 5 · paper 1bbb61270433

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/COMPILER DESIGN/Compiler Desing, Sem-V, Final Exam, A Y 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 86.3

````text
SVKM’S NMIMS oN
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE [
SCHOOL OF TECHNOLOGY MANAGEMENT }

Academic Year: 2023-2024 oe
Program/s: _B.Tech (CSBS) Year: m_ Semester: _V.
Stream/s ;__ Computer
Subject: Compiler Design_ : Time: _3 hrs (Zis0pmto S? oop ma)
Date:_24 /|{ /2023 No. of Pages:_3_

Marks: 100.

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

>) 1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any__4 _ questions.
3) In all__5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]

a. Differentiate between Token, Patterns and Lexemes. Further consider the
following code that is fed to an Lexical Analyzer, identify the tokens that
are created

# include <stdio.h>

Co- 1; int minimum [int a, int b} {
SO-1; if {acb} [5]
BL-4 return a; *
else {
i return b;
} :
}
b. What is left recursive grammar? Eliminate left recursion from the grammar
gs g

CO- 1;
S0-6; X— XSb|Sa|b (5]
BL S— Sb| Xala
CO-1: c. A Compiler can choose one of the following options (1st option) Translate

, the input source into intermediate code and then convert it to final machine
SO-1; P } ; [5]
BL-3. code. (2nd option) Directly generate the final machine code from the input

source, what is the preferred option and why?

CO-2 ; d.
SO-1; Explain broad classification of optimization techniques [5]
BL-2
--- page 2 ---
ES) Fe

Distinguish between top-down parser and bottom-up parser. Consider

oF grammar E > E+E|E*E|(E)|id. [10]
von ae Reduce the string id * (id + id) and show the handle at each step.
Write the three address code (TAC) for the following expression
CO-2; SO- -(a*b)+(c+d)—(at+b+e¢+d), also implement the generated [10]
6;BL-4 TAC in form of quadruples, triples and indirect triples. e
Q3 . oes
Summarize the purpose of each phase of compiler in brief. Demonstrate
CO-1; the output for all the phases of the compilation process by taking the case | [10]
a of translation of the statement a = (b+c) * (b+c) *2
CO-1;
SO-1; Explain with the help of suitable example, any four loop optimization [10]
BL-2 techniques.
Q4
Discuss the structure of a LEX File and the steps involved in execution of [10]
Lene SO- a LEX file. Relate the significance of LEX tool in compiler design
Consider the following production rules of a Context Free Grammar
S->E
E->E+T | T
CO-1; SO- T->T*F |F «| [10]
6;BL-4 F->(E) | digit
With context to the above CFG, carry out the computation of S-attributed
definition for the string 8*6+7
Determine whether the given grammar is LL(1) or not
EDT+E
Q5 EST
CO-1; SO- T > int {10}
6;BL-4 T > int* T
TO(E)
CO-1; SO- Explain suitable data structures for symbol table implementation and [10]
1; BL-2 justify your answer.

>
--- page 3 ---
Q6

Construct the SLR parsing table for the grammar:

SP(L)la [10]
CO-1; SO- LOL,S|S
6;BL-4
Discuss the following:
CO-2; SO- (i) Instruction scheduling [10]
1;BL-2 (ii) | Two code optimization techniques with example
With reference to LR parser, answer the following questions:
Loz 0 Need for LR parser
J ii) Model of LR parser
; : . [10]
CO-1; SO- iii) Define LR(0) item and LR(1) item
1; BL-2 iv) Compare the types of LR parsers
CO-2; SO- ompare non -imperative programming and imperative programming [10]
1: BLA anguage
i
````

## 2023-24 · Re-Exam · Sem 5 · paper 9bb03056e67e

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/COMPILER DESIGN/Compiler Design, Sem-V, Year 2023-24, Re Exam.pdf`
- Printed on paper: duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 86.2

````text
MPSTM:
LIBRARY

SVKM’S NMIMS ;

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024 wt

Program/s: B.Tech (CSBS) Year: Tn” ‘Semester: _V

Stream/s ;__ Computer

Subject: Compiler Design_ Time: 3 hrs (2__paato v pm )

Date: OF / 02/2024 No. of Pages:_3

Marks: __ 100

*Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

(> 2) Out of remaining questions, attempt any __4 questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
Answer briefly: [20]
CO-1 ; a. . . . F (5]
SO-1- Explain the role of Pre-processors, Assembler, Linker, Loader and compiler
BL2 to create an executable program
b. What is Ambiguous grammar? Consider the string "3 * 2 + 5" and | [5]
determine whether the given grammar is ambiguous or not.
CO-1; E~I
@) |SO-1; E—E+E
BL-2 E->E*E
I>e|0|1|2]...|9
CO-2 ; c. A : : % [5]
S0-1 - What is Intermediate Code generator? J ustify the need of Intermediate code
BL3 , generator phase in a compiler design.
d. [5]
CO-2 ; Discuss peephole optimization in brief
SO- 1;
BL-2
--- page 2 ---
Q2 a. Distinguish between a parse tree and a syntax tree. Consider grammar
o

CO-1; S > SS+|SS*]a al [10]
SO-1;

BL-4 Show the derivation steps for the string aat+a* and construct parse tree

CO-2: b. Write the three address code for the following expression

60.8. a=(b+c) *(a+b+c), also implement the generated TAC in form of

quadruples, triples and indirect triples. Compare the representations of [10]

BL-4 Three Address code (TAC) on the following parameters (i) Indirections (ii)
Space requirement

3 a.
Q Discuss in brief the purpose of each phase. of compiler. Demonstrate the
CO-1; output for all the phases of the compilation process by taking the case of _| [10]

SOI-; translation of an assignment statement a=b+c*30

BL-3 .
CO-2; b. Explain with the help of suitable example, any four code optimization [10]
a techniques. -
Q4 a.
oe) Justify the role of regular expressions for token specification in lexical [10]
SO-1: analysis. Also explain how lexical analyzer is generated using LEX
BL-4
b. Consider the following production rules of a Context Free Grammar
S->E
E->E+T
é

E->E-T

E->T
CO-1; T->T*F
SO-6; [10]
BL-4 T->T/F

T->F

F->(E)

F->digit

With context to the above CFG, carry out the computation of S-attributed
definition for the string 5*6+7
--- page 3 ---
Define LL (1) grammar. Determine whether the given grammar is LL(1) or

Q5
CO-1 not. oe
hs S > iEtS | iEts , 10
50.6; | eS|a [10]
BL-4 Eb
Justify the role of a Symbol Fable in compiler. With respect to symbol
CO-I1: table, answer following questions:
SO-1; i) What are the general attributes associated with a symbol [10]
cae ii) What are the operations possible with symbol tables
iii) How is a data structure selected for a symbol table
Construct the Canonical LR parsing table for the grammar:
Q6
S > Aa|bAc| Be | bBa
CO-1; [10]
SO-6; Avdd
BL-4
Bod
Co-2; Discuss the following:
SO-1; (i) Issues in code generation [10]
= (ii) Two loop optimization techniques with example
Q7 With reference to top-down parser, answer the following questions:
i) Role of Grammar in parsers
CO-1; PA . . [10]
S0-1: ii) Classification of top-down parsers ‘
BL-2 iii) Type of grammars suitable for LL(1) parsing
iv) Model of LL(1) parser
CO-2;
SO-1; Explain the type systems: untyped , statically typed and Dynamically typed | [10]
BL-2
````

## 2022-23 · Final-Exam · Sem 5 · paper b417487dc660

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/COMPILER DESIGN/Compiler Design, 3rd Year, Sem-V, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 17 November 2022
- Text: ocr (3 pages), mean OCR confidence 82.3

````text
- SVKM’s NMIMS.
_MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /
“SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2022-23

Programme: B. Tech (CSBS ) Year: Ill Semester: V

Subject: Compiler Design ,
. Marks: 100 -
Date: 17 November 2022 . Time: 10.00 am- 1.00pm _

Durations: 3 (Hrs).
No. of Pages: >

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on 1 the « cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi

Answer briefly: [20]
a - Compare Single-pass and multi-pass compiler. [5]
She b. Classify various types of Optimizations. [5]
era C. Differentiate between Parse tree and Syntax tree. [5]
be d. Describe various types of data structure used for Symbol Table. [5]
a. Find out all precedence relations between various operators and symbols in
Q2 following grammar: _
CO-1 E->E+E/E*E/id ie
BL-6 . ;
; construct precedence graph and precedence function for above grammar.
b. Define types of syntax directed translation schemes? Write down syntax-
directed definition for the given Grammar. Construct parse tree and
Q2 complete parse tree for string 5+6+7. :
CO-1 E>E+T/T [10]
BL3 ToT * E/E
F — digit

4/3
--- page 2 ---
a. State the function of Intermediate code generation. Evaluate Quadruples,

oo triples and indirect triples for the expression: © [10]
BL-5 _{a=b*-ctb*-c
o ti “What are storage allocation strategies? Write down its advantages and
Seo disadvantages. [0]
04 Consider the grammar
CO-1 ne | [15]
BL-6 A->aA|b
Construct CLR parsing table for the given context free grammar.
Q5 a.
CO-1, Define various phases of compiler.in detail. [10]
BL-1
b. Consider the grammar:
0s S->(Ly/a . |
ent L->L, S/S r10]
a8 Construct predictive parser for the above grammar ;
Is this grammar LL(1)?
Q6 a. : * :
6-1 Design NFA for regular expression (a+b)"abb and convert this NFA to 110]
prs DFA. se :
b. Convert the following Three. Adress Code statement into Basic Block and
design. its flow graph: °
1. 1
Q6 ‘2. i=1
CO-1 3. ifi<=10 goto (5) ; [10]
BL-6 4. goto (8)
5. ffi
, o iFitl
7. goto (3)

2/3
--- page 3 ---
8. end

Q7 ota
CO-3 Explain Instruction scheduling (for pipeline) in deatil. [10]
BL-2 ;

Q7 b.
CO-3
BL-5

How compilation of object oriented features work explain the help of —

[10]
example. :

2

3)

[RB

3
````

## 2022-23 · Re-Exam · Sem 5 · paper 90f93aeaeade

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/COMPILER DESIGN/Compiler Design, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 January 2023
- Text: ocr (2 pages), mean OCR confidence 85.9

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Program: B. Tech (CSBS )- Year: Ill © Semester: V ~

AcademicyY ear: 2022-2023

* Subject: Compiler Design
al Marks: 100

Date : 27 January 2023 - Time: 10.00 am - 1.00 pm’
Durations: 3 (Hrs)

No. of Pages: o2-
Re-Examination (2022-23)

———— ——

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.

3) Inall__5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

QI la. Write the FIRST and FOLLOW sets of each variable in the below CFG: [5]
me S — aBDh B-—cC C>dbC/e
BL-5 D— EF E—g/e F-f/e
Sot Ab. Explain the role of a lexical analyser in a compiler - [5]
BL-1
Soe Je. Explain code motion and loop splitting with suitable examples 6)
BL-5 : -
or Ad. Write a short note on the rules for construction of a DAG. Explain with examples. [5]
BL-2
Q2 2a. Below are the production rules of a Context Free Grammar G [10]
50-6 ‘SiEtSeA/a
BL-5 :

7 A~>eS/e

E~>b

i. Is Gin LL(1)? If not, convert it.
ii. Show the FIRST() and FOLLOW( sets of each variable.
ili. Construct the LL(1) parsing table for G
iv. Are there any conflicts? If yes, how many?
v. Show the step-wise parsing of o = “ibtaea” along with a parse tree

o3 2b. Compare Static and Dynamic memory allocations. [10]
BL-1

Q3 3a. Give the three address code for the below expression: [12]
Sad a = (b-c) * (c+d) + (b-cte)

BL-4 Represent 3AC as quadruples, triples, indirect triples and DAG.

CO- 1;

so; 3b. Design a DFA to recognize the keyword “while” in a source program. [8]

Ve
--- page 2 ---
Q4 4a. Compile: “a=b/e+d“ [10]
oa Q Explain how each phase of compiler will process this expression along with
BL-4 appropriate representations.
Sag 4b. Below are the productions of a CFG [10]
BL-6 S-Aa|bAc .
A—bA|e
i. Design the goto graph of LR(0) items for G
li. Construct the SLR(1) parsing table for G
ili. Will there be any conflicts in LR(0) parsing table? If yes, how many SR, RR?
iv. Show the step-wise parsing of w = “bbc” along with a parse tree.
Q5 5a. Below are the production rules of a CFG that checks syntax of pointers in C [10]
$0.1 S—A=P/P
BL-S
A> *P/id
P-A
. Construct an Operator Precedence Parser (OPP) for this grammar. |
ii. Show the step-wise parsing of w = “id = *id” along with a parse tree.
iii. Is the given grammar ambiguous?
So 5b. Write the three address code for the below C program. Identify the basic blocks and [10]
BL-2 their leaders, and show the transitions as a flow graph.
int n = 10;
double f=1, s=0;
while (n > 1)
f= f * n--;
z=s t+ £7
Q6 6a. Below are the productions of a CFG, where n = newline. [10]
50.2: L-En
BL-5 E->E+T|T
T—T*tF|F
F = digit
Write the semantic rules to convert expressions parsed by this grammar from infix
to postfix. Construct the annotated parse tree for@=3+4*6+9 :
6b. Explain the following with suitable examples: [10]
_ i. Dead code elimination iii. Sub-expression elimination
BL-2 il. Constant propagation iv. Algebraic simplification & strength reduction
Q7 Write short notes on any FOUR. Support your answer with suitable examples [20]
“oO   ©67a ~-Lexemes, tokens, and patterns in compilers
BL-2 7b. Ambiguous grammars
7c. S-attributed and L-attributed grammars
7d. Register allocation during code generation. *
Te.

Instruction pipeline

2h

*** ALL THE BEST ***
````
