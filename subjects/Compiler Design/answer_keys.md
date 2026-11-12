# Compiler Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 421f8342db28

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Compiler Design/ANS_Compiler Design(702CO0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (9 pages)

````text
SYNOPTICS
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
1. This question paper contains 9 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
**For theory questions, students may answer in their own words. The answer provided here is for
reference.
Q1
Answer briefly:   [20]
a.   Describe the major tasks performed by the front end and back end of a
compiler.
CO- ;
SO- ;   Front end [2.5 marks]: lexical analysis, syntax and semantic analysis
BL-   Back end [2.5 marks]: intermediate code generator, code optimization
and code generator
b.   Write the rules used to compute CLOSURE() and GOTO() functions in
LR parsers
CLOSURE[2.5 marks]
If I is a set of items for a grammar G, then CLOSURE(I) is the set
of items constructed from I by the two rules.
• Initially, add every item I to CLOSURE(I).
CO- ;
• If A —> αB,β is in CLOSURE(I) and B —> ɣ is a production,
SO- ;
then add the item B —> • ɣ to CLOSURE(i), if it is not already
BL-   there. Apply this rule until no more items can be added
to CLOSURE (!).
GOTO[2.5 marks]
GOTO(Ii , X) -> Ij where Ii -> input set of items X -> terminal/non-
terminal symbol Ij -> output set of items. Now if there is an item of the
form A->B.XD in Ii then add the item A->BX.D to Ij and then compute
********** 1 **********
--- page 2 ---
the CLOSURE of the item. GOTO function moves the dot one symbol
forward.
c.
“SDD is a context-free grammar together with attributes and rules”.
Justify the statement with a suitable example.
Definition of SDD [2 marks]
A CFG with attributes and rules is called a syntax-directed definition
(SDD). The properties are linked to the grammar symbols in an
extended CFG (i.e. nodes of the parse tree). The rules are associated
with grammar production.
Inherited and Synthesised Attribute
For a non-terminal symbol (node) N, we can declare the value of a
synthesized attribute:
• The attribute value of children.
• The total attribute values of N.
S --> S1 + T { S.val = S1.val + T.val}
CO- ;   For a non-terminal symbol (node) N, we can declare the value of an
SO- ;   inherited attribute:
BL-   •   N's parent's attribute values.
•   N's Siblings' attribute values.
•   Total attribute values of N.
S --> TUV   { U.in = S.in, U.type = T.type }
Justification with example [3 marks]
Example:
d.   What properties an intermediate representation should satisfy? List some
high level and low-level representations
The below five are the properties of IRs:
1. Ease of generation
2. Ease of manipulation
CO- ;
3. Freedom of expression
SO- ;   4. Size of the procedure
BL-   5. Level of abstraction
High Level Representations (e.g., syntax trees, DAG):
closer to the source language
easy to generate from an input program
code optimizations may not be straightforward.
********** 2 **********
--- page 3 ---
Low Level Representations (e.g., 3-address code):
closer to the target machine;
easier for optimizations, final code generation;
A   Illustrate with the help of an example the problem caused due to left
recursive grammar in a recursive descent parser. For the given grammar,
eliminate the left recursion problem.
G→ E
E→ E+T
E → T
T → E * T
T→ id
Problem caused [ 5 marks]: infinite looping
For E → Ei | i
And the procedure for non-terminal as below:
Q2   Procedure for E:   Procedure for match and m
[20]
CO-; SO-;
E()   Match(char t)
BL-
{   {
E ( )   If(la==t)
If (la ==‘i’){   La = getchar();
match (‘i’);   Else
}   printf(“error”);
Else{   }
If (la ==‘i’){   main()
match (‘i’);   { E();
}   If(l==‘$’)
}   Printf(Parsing successful)
}
Removal of left recursion with proper steps [ 5 marks]
********** 3 **********
--- page 4 ---
B   Explain any four function preserving optimization techniques with
suitable example
Any four techniques can be explained along with example. Each carry
2.5 marks
Common sub expression elimination,
Copy propagation,
Dead-code elimination,
Constantfolding
Strength   reduction
Explain how the tokens are specified and recognized in lexical analysis
phase of a compiler? For the given code segment, list down the
lexemes, token class and count the total number of tokens.
[5 marks]
tokens specification: regular expressions
recognition of tokens- Finite automata
listing of tokens , lexemes and count: 5 marks
Q3
main()   [20]
CO-; SO-;
BL-   {
char ch=’A’;
int x , y;
x=y=20;
x++;
printf (“%d %d”, x, y);
}
Total count of tokens= 33
********** 4 **********
--- page 5 ---
Define Syntax directed definition and Syntax directed translation.
Determine whether the given Syntax directed definition is S-attributed
or L-attributed grammar. Justify your answer
SDD and SDT [ 4 marks]
correct identification of definition [2 marks]: not an L-attributed
definition
justification [ 4 marks]
it should include determining the type of each attribute in the semantic
rules
Production   Semantic Rule
L.i := f1(A.i)
A   L M   M.i := f2(L.s)
A.s := f3(M.s)
R.i := f4(A.i)
A   Q R   Q.i := f5(R.s)
A.i := f6(Q.s)
A
What are top-down parsers? Write the algorithm for constructing the
Predictive parsing table
Top down parser [5 marks]
Algorithm: Construction of predictive parsing table
Q4   Input: Grammar G
CO-; SO-;   Output: Parsing table M   [20]
BL-
Method:
Explain how basic blocks and flow graphs help in optimization process?
Analyze the given three address code and find the basic blocks:
W=0;
X = x + y;
Y = 0;
If( x>z)
********** 5 **********
--- page 6 ---
{
Y=x;
X++;
}
Else
{
Y=z;
Z++;
}
W=x+z;
What are basic blocks, flow graphs and its use in optimization [ 5
marks]
Basic blocks [ 5 marks]
B1:   W=0;
X = x + y;
Y = 0;
If( x>z)
B2:   Y=x;
X++;
B3:   Y=z;
Z++;
B4:   W=x+z;
Determine whether the following grammar is LR(1) or not
S → Aa |bAc |Bc |bBa
A → d
B → d
Q5
CO-; SO-;   [20]
Augmented grammar [1 mark]
BL-
Finding closure and goto with DFA [ 4 marks]
Parsing table [4 marks]
Final answer [1 mark] ---it is LR(1) grammar
********** 6 **********
--- page 7 ---
B   Discuss the structure of an activation record and its role in procedure
activation.
An activation record is a contiguous block of storage that manages
information required by a single execution of a procedure. When you
enter a procedure, you allocate an activation record, and when you exit
that procedure, you de-allocate it. Basically, it stores the status of the
current activation function. So, whenever a function call occurs, then a
new activation record is created and it will be pushed onto the top of the
stack. It will remain in stack till the execution of that function. So, once
the procedure is completed and it is returned to the calling function, this
activation function will be popped out of the stack.
If a procedure is called, an activation record is pushed into the stack, and
it is popped when the control returns to the calling function.
Activation Record includes some fields which are -
Return values, parameter list, control links, access links, saved machine
status, local data, and temporaries.
********** 7 **********
--- page 8 ---
Explain each field of the activation record
A
Translate the given expression into three address code. Show the entries
of data structures: quadruples and triples
(i)   a+(b-c) + (b-c) * d [ 5marks]
Q6   (ii) x= a+ (b-c) *d +e [ 5marks]
CO-; SO-;   [20]
BL-
B   Discuss the concept of memory management and instruction selection
with respect to code generation
Memory management [5 marks]
Mapping the names in the source program to addresses of data objects is
done by the front end
and the code generator. A name in the three address statement refers to
the symbol table entry
for name. Then from the symbol table entry, a relative address can be
determined for the name.
Instruction selection [5 marks]
Selecting best instructions will improve the efficiency of the program. It
includes the instructions that
should be complete and uniform. Instruction speeds and machine idioms
also plays a major role when
********** 8 **********
--- page 9 ---
efficiency is considered. But if we do not care about the efficiency of
the target program then
instruction selection is straight-forward.
A   Consider the following grammar.
S → AB
A → Aa | a
B → Bb| b
Parse the input string “aaabb” using stack implementation of shift-
reduce parser
Rightmost derivation in reverse [2 marks]
Stack implementation steps [ 8 marks]
The given string is accepted
Q7
CO-; SO-;   [10]
BL-
B   Write a note on: Compilation of object-oriented features
[10]
Students can write about any two features. Each feature carry 5 marks
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper ee093fc0bed0

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Compiler Design/ANS_Compiler Design(702CO0C028)_2025-2026_ee093fc0be.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (15 pages), mean OCR confidence 91.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Semester V(Exam Year: NA)
Subject: Compiler Design
Date: NA   Time: NA to NA (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 1 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Describe the major tasks performed by the front end and back end of a
compiler.
Front end [2.5 marks]: lexical analysis, syntax and semantic analysis,
intermediate code generator
Back end [2.5 marks]: code optimization and code generator
Each phase to be described in brief.
Lexical analysis: The stream of characters are read from left-to-right
and grouped into tokens.
CO- ;
Syntax analysis: It involves grouping of tokens of SP into grammatical   [5]
SO- ;
phrases. Then they are represented by a parse tree.
BL-   Semantic analysis: It involves checking the SP for semantic errors and
gathers type information.
ICG: intermediate code must have 2 properties: easy to produce and
easy to translate. It can be in different forms: One such form is “three-
address code
Code Optimization: Attempts to improve the intermediate code
Code generator: Deals with generation of target code, consisting of
relocatable machine code or assembly code
b.   Write the rules used to compute CLOSURE() and GOTO() functions in
CO- ;
LR parsers   [5]
SO- ;
BL-   CLOSURE function [2.5 marks]
********** 1 **********
--- page 2 ---
If I is a set of items for a grammar G, then CLOSURE(I) is the set
of items constructed from I by the two rules.
• Initially, add every item I to CLOSURE(I).
• If A —> αB,β is in CLOSURE(I) and B —> ɣ is a production,
then add the item B —> • ɣ to CLOSURE(i), if it is not already
there. Apply this rule until no more items can be added
to CLOSURE (!).
GOTO function[2.5 marks]
GOTO(Ii , X) -> Ij where Ii -> input set of items X -> terminal/non-
terminal symbol Ij -> output set of items. Now if there is an item of the
form A->B.XD in Ii then add the item A->BX.D to Ij and then compute
the CLOSURE of the item. GOTO function moves the dot one symbol
forward.
The rules can be explained with the help of an example as well.
c.
“SDD is a context-free grammar together with attributes and rules”.
Justify the statement with a suitable example.
Definition of SDD [2 marks]
A CFG with attributes and rules is called a syntax-directed definition
(SDD). The properties are linked to the grammar symbols in an
extended CFG (i.e. nodes of the parse tree). The rules are associated
with grammar production.
Inherited and Synthesised Attributes
For a non-terminal symbol (node) N, we can declare the value of a
synthesized attribute:
• The attribute value of children.
• The total attribute values of N.
S --> S1 + T { S.val = S1.val + T.val}
CO- ;   For a non-terminal symbol (node) N, we can declare the value of an
SO- ;   inherited attribute:   [5]
BL-   •   N's parent's attribute values.
•   N's Siblings' attribute values.
•   Total attribute values of N.
S --> TUV   { U.in = S.in, U.type = T.type }
Justification with example [3 marks]
Example:
********** 2 **********
--- page 3 ---
d.   What properties an intermediate representation should satisfy? List some
high level and low-level representations
The below five are the properties of IRs:
1. Ease of generation
2. Ease of manipulation
3. Freedom of expression
4. Size of the procedure
CO- ;   5. Level of abstraction
SO- ;   Any 3 properties can be mentioned and explained in brief (3 marks)   [5]
BL-
Representations (2 marks)
High Level Representations (e.g., syntax trees, DAG):
closer to the source language
easy to generate from an input program
code optimizations may not be straightforward.
Low Level Representations (e.g., 3-address code):
closer to the target machine;
easier for optimizations, final code generation;
A   Illustrate with the help of an example the problem caused due to left
recursive grammar in a recursive descent parser. For the given grammar,
eliminate the left recursion problem.
G→ E
E→ E+T
E → T
T → E * T
T→ id
Q2   Problem caused [ 5 marks]: infinite looping problem along with an
[10]
CO-; SO-;   example
BL-
For E → Ei | i
And the procedure for non-terminal as below:
Procedure for E:   Procedure for match and m
E()   Match(char t)
{   {
E ( )   If(la==t)
If (la ==‘i’){   La = getchar();
match (‘i’);   Else
}   printf(“error”);
********** 3 **********
--- page 4 ---
Else{   }
If (la ==‘i’){   main()
match (‘i’);   { E();
}   If(l==‘$’)
}   Printf(Parsing successful)
}
Removal of left recursion with proper steps [ 5 marks]
Rule to be written, Step by step working
A left-recursive pair of productions A → Aα| β could be replaced by the
non-left-recursive productions.
A → βA'
A' → α A'| ε
Final grammar:
B   Explain any four function preserving optimization techniques with
suitable example
Any four techniques can be explained along with an example. Each
technique carry 2.5 marks
Common sub expression elimination:
[10]
********** 4 **********
--- page 5 ---
Copy propagation
Dead-code elimination:
Constant folding
eg., an assignment a=3.14/2
can be replaced by a=1.57 thereby eliminating division
operation.
e., x = 2*3 +y;   x = 6 + y
Strengthreduction
********** 5 **********
--- page 6 ---
Explain how the tokens are specified and recognized in lexical analysis
phase of a compiler? For the given code segment, list down the
lexemes, token class and count the total number of tokens.
[5 marks]
tokens specification: regular expressions
An identifier is a letter followed by zero or more letters or digits
The expression:   letter (letter | digit)*
The | here means “union” , the parentheses are used to group sub
expressions, the star means “ zero or more instances of” the
parenthesized expression, and the juxtaposition of letter with remainder
of the expression means concatenation.
A regular expression is built up out of simpler regular expressions using
set of defining rules.
Each regular expression r denotes a language L(r).
Consider the set of strings of letters and digits beginning with a letter.
The regular definition for the set is
letter → A|B|…|Z|a|b|…z
Q3
digit → 0|1|2|…|9
[10]
CO-; SO-;
id → letter ( letter | digit ) *
BL-
recognition of tokens- Finite automata
A recognizer for a language is a program that takes as input a string x
and answers ‘yes’ if x is a sentence of the language and ‘no’ otherwise.
A finite automaton can be deterministic or non deterministic.
They are represented by transition graphs/ diagrams
listing of tokens, lexemes (4 marks) and count (1 mark)
main()
{
char ch=’A’;
********** 6 **********
--- page 7 ---
int x , y;
x=y=20;
x++;
printf (“%d %d”, x, y);
}
Total count of tokens= 33
B   Define Syntax directed definition and Syntax directed translation.
Determine whether the given Syntax directed definition is S-attributed
or L-attributed grammar. Justify your answer
SDD and SDT [ 4 marks]
•   Syntax-directed definition: it specifies the values of attributes by
associating semantic rules with the grammar productions
•   It is used for specifications
• Used to compute the attribute values
•   a semantic rule is associated with production where the attribute
name is associated with the grammar symbol, also called
attribute grammars
•   for example:
• E → E + T   E.val = E.val + T.val   [10]
• An attribute is a property of a programming language construct
•   E.val denote the value of attribute “val” at a particular node “E”
in the parse tree
•   Syntax-directed Translation: it associates semantic actions with
the grammar productions
•   It is more implementation oriented
•   Indicates the order in which semantic rules to be evaluated
• Example of SDD:
•   Here, E and T have string valued attribute code. The semantic
rule specifies that the string E.code is formed by concatenating
E1.code, T.code and the character “+”
•   Example of SDT: It embeds program fragments called semantic
actions with production
********** 7 **********
--- page 8 ---
• Semantic actions are enclosed within curly braces. The position
of a semantic action in a production body determines the order in
which the action is executed
correct identification of definition [2 marks]: not an S-attributed
and L-attributed definition
justification [ 4 marks]
it should include determining the type of each attribute in the semantic
rules and finally summarizing why it is not an S-attributed and L-
attributed grammar
Production   Semantic Rule
L.i := f1(A.i)   i → inherited
A   L M   M.i := f2(L.s)   i→ inherited
A.s := f3(M.s)   s→ synthesized
R.i := f4(A.i)   i → inherited
A   Q R   Q.i := f5(R.s)   i→ inherited
A.i := f6(Q.s)   i→ inherited
A   What are top-down parsers? Write the algorithm for constructing the
Predictive parsing table
Top down parser [5 marks]
In top-down parsing, you start with the start symbol and apply
the productions until you arrive at the desired string.
It is an attempt to find the leftmost derivation for an input string
start with the start symbol and apply the productions until you
Q4   arrive at the desired string
CO-; SO-;   In creating a parser for a compiler, we normally have to place   [10]
BL-   some restrictions on how we process the input. In the above
example, it was easy for us to see which productions were
appropriate because we could see the entire string aaab.
In a compiler’s parser, however, we don’t have long-distance
vision. We are usually limited to just one-symbol of lookahead.
Top-down parsers come in two forms :
•   Recursive-descent parser
********** 8 **********
--- page 9 ---
•   Predictive parser
Recursive Descent Parsing
Recursive Descent Parsing is a top-down parsing technique used to
analyze the syntax of a given input string based on a set of grammar
rules. It uses a set of recursive procedures (or functions) to process each
non-terminal in the grammar and try to match the input string.
Here's how it works:
1. Start with a Non-terminal.
2. Check the first possible option (alternative) for the Non-
terminal and try to match it with the input string.
3. If it doesn’t match, move to the second option and try again.
4. Continue this process for each option until you find a match.
5. If at least one option matches the input string, the parsing is
successful.
LL(1) or Table Driver or Predictive Parser
LL(1) parsing is a way to analyze a sentence in a programming language
and check if it follows the correct structure. The name LL(1) has a
meaning:
• The first L means reading the input from Left to Right.
• The second L means creating the Left-most Derivation
(building the structure step by step from the left side).
• The 1 means looking one step ahead in the input to decide
what to do next.
Rules for LL(1) Parsing
To work properly, an LL(1) parser needs clear and simple grammar:
• No left recursion (rules must not refer to themselves at the
beginning).
• No common prefixes (if two rules start the same way, they
should be rewritten to avoid confusion).
• No ambiguity (there must be only one way to build the
sentence).
Algorithm: Construction of predictive parsing table [ 5 marks]
Input: Grammar G
Output: Parsing table M
Method:
B   Explain how basic blocks and flow graphs help in optimization process?
Analyze the given three address code and find the basic blocks:
W=0;   [10]
X = x + y;
Y = 0;
If( x>z)
********** 9 **********
--- page 10 ---
Y=z;
Z++;

}

W=x+4+z;

What are basic blocks, flow graphs and its use in optimization [ 5
marks]

Basic Blocks & Flow graphs

The representation is constructed as follows:

1. Partition the intermediate code into basic blocks, which are maximal se-
quences of consecutive three-address instructions with the properties that

(a) The flow of control can only enter the basic block through the first

instruction in the block. That is, there are no jumps into the middle
of the block.

(b) Control will leave the block without halting or branching, except
possibly at the last instruction in the block.

2. The basic blocks become the nodes of a flow graph, whose edges indicate
which blocks can follow which other blocks.

Basic Blocks - Leaders

1. The first three-address instruction in the intermediate code is a leader.

2. Any instruction that is the target of a conditional or unconditional jump
is a leader.

3. Any instruction that immediately follows a conditional or unconditional
jump is a leader.

FEA AO CIC 7] QR ok ok ok ak
--- page 11 ---
Basic blocks [ 5 marks]
B1:   W=0;
X = x + y;
Y = 0;
If( x>z)
B2:   Y=x;
X++;
B3:   Y=z;
Z++;
B4:   W=x+z;
Determine whether the following grammar is LR(1) or not
S → Aa |bAc |Bc |bBa
A → d
B → d
Q5
CO-; SO-;   [10]
Augmented grammar [1 mark]
BL-
Finding closure and goto with DFA [ 4 marks]
Parsing table [4 marks]
Final answer [1 mark] ---it is LR(1) grammar
********** 11 **********
--- page 12 ---
B   Discuss the structure of an activation record and its role in procedure
activation.
An activation record is a contiguous block of storage that manages
information required by a single execution of a procedure. When you
enter a procedure, you allocate an activation record, and when you exit
that procedure, you de-allocate it. Basically, it stores the status of the
current activation function. So, whenever a function call occurs, then a
new activation record is created and it will be pushed onto the top of the   [10]
stack. It will remain in stack till the execution of that function. So, once
the procedure is completed and it is returned to the calling function, this
activation function will be popped out of the stack.
If a procedure is called, an activation record is pushed into the stack, and
it is popped when the control returns to the calling function.
Activation Record includes some fields which are -
Return values, parameter list, control links, access links, saved machine
status, local data, and temporaries.
********** 12 **********
--- page 13 ---
Explain each field of the activation record
A
Translate the given expression into three address code. Show the entries
of data structures: quadruples and triples
(i)   a+(b-c) + (b-c) * d [ TAC 2 marks + quadruples and
triple 3 marks]
(ii) x= a+ (b-c) *d +e [ TAC 2 marks + quadruples and
Q6
triple 3 marks]
CO-; SO-;   [10]
BL-
(I )   (ii )
T1 = b-c   t1 = b-c
T2 = t1*d   t2 = t1 * d
T3 = a + t1   t3 = a + t2
T4 = t3 +t2   t4 = t3 +e
x = t4
B   Discuss the concept of memory management and instruction selection
with respect to code generation   [10]
Memory management [5 marks]
********** 13 **********
--- page 14 ---
Instruction selection [5 marks]
A   Consider the following grammar.
S → AB
A → Aa | a
B → Bb| b
Q7   Parse the input string “aaabb” using stack implementation of shift-
CO-; SO-;   reduce parser   [10]
BL-   Rightmost derivation in reverse [2 marks]
Stack implementation steps [ 8 marks]
The given string is accepted
********** 14 **********
--- page 15 ---
B   Write a note on: Compilation of object-oriented features
[10]
Students can write about any two features. Each feature carry 5 marks
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 297bd2786836

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSBS_7036/Compiler Design/ANS_Compiler Design(702CO0C028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (9 pages)

````text
SYNOPTICS
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
1. This question paper contains 9 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
**For theory questions, students may answer in their own words. The answer provided here is for
reference.
Q1
Answer briefly:   [20]
a.   Describe the major tasks performed during the analysis and synthesis
phases of compilation?
Analysis [2.5 marks]- lexical analysis, syntax analysis and semantic
[5]
analysis
Synthesis [2.5 marks]- intermediate code generator, code optimization
and code generation
b.   Explain the rules to compute FIRST() and FOLLOW() sets on grammar
symbols?
First: [2.5 marks]
•   If X is a terminal, then First(X) is {X}.
•   If X is a non-terminal and X tends to aα is production, then
add ‘a’ to the first of X. if X->ε, then add null to the
First(X).   [5]
•   If X_>YZ then if First(Y)=ε, then First(X) = { First(Y)-ε}
U First(Z).
•   If X->YZ, then if First(X)=Y, then First(Y)=terminal but
null then First(X)=First(Y)=terminals.
Follow: [2.5 marks]
• $ is a follow of ‘S’(start symbol).
********** 1 **********
--- page 2 ---
•   If A->αBβ,β!=ε, then first(β) is in follow(B).
•   If A->αB or A->αBβ where First(β)=ε, then everything in
Follow(A) is a Follow(B).
c.   “Every S-attributed definition is also L-attributed definition” Justify the
statement with a suitable example.
Explain S-attributed definition and L-attributed definition [2 marks]
S-attribute is a syntax-directed definition that uses synthesized attributes
only.
L-attribute is an attributed definition in which:   [5]
Each attribute in each semantic rule for the production A→X1,X2,..Xn is
either a synthesized attribute or an inherited attribute Xj which depends only
on the inherited attribute of A and/or the attributes of X1,…Xj-1.
Independent of the evaluation order.
Justification with example [ 3 marks]
d.   Show the need for an Intermediate code generator phase in compilers.
[5]
A   Illustrate with the help of an example the problem caused due to a non-
deterministic grammar. For the given grammar, apply left factoring to
eliminate non-determinism
Q2   E → T + E
[10]
E → T
T → int
T → int * T
********** 2 **********
--- page 3 ---
T → ( E )
Problem with example: 5 marks
Grammar having common prefixes is called non-deterministic grammar.
Such grammar requires backtracking due to confusion, which is actually
a costly process. Top-Down Parsers don’t prefer to parse Non-
Deterministic Grammar. The process of removing this confusion is
called eliminating non-determinism or Left Factoring. It is a procedure
of factoring out common prefixes as long as possible. It is generally
used in case when it’s not clear which of two available options should
be used to expand LHS non-terminal. This grammar that is obtained
after left-factoring is known as Left Factored Grammar.
Example: S → cAd
A → ab|a
Input string w = cad
Elimination – 5 marks
Resultant grammar after Left factoring. Here the new non terminals can
be any variable assumed by the student
E → T X
X → + E
X → 
T → ( E )
T → int Y
Y → * T
Y → 
B   Explain any four loop optimization techniques with suitable example   [10]
********** 3 **********
--- page 4 ---
Student can explain any four loop optimization techniques. Each
carry 2.5 marks for explanation and suitable example
1. Code motion (frequency reduction)
2. Induction variable elimination
3. Strength reduction
4. loop unrolling
5. Loop merge (loop jamming)
A   Explain the role of regular expressions and finite automata in lexical
analysis phase of a compiler?
For the given code segment, list down the lexemes, token class and
count the total number of tokens.
Q3   Regular Expression and Finite Automata - [ 5 marks]
CO-; SO-;   Listing of tokens, lexemes and count [ 5 marks]   [10]
BL-   int a = 10;
Float b = 20.5;
Printf(“C=%d, d=%”, ++a, b++);
Total number of tokens-= 21
B   Define synthesized and inherited attributes.
Identify whether the given Syntax directed definition is S-attributed or
L-attributed definition. Justify your answer
[10]
synthesized and inherited attributes. [ 4 marks]
Synthesized : These attributes derive their values from the child nodes. Let's
use the example of the language P->QR. If an attribute P depends on attribute
Q or R, it will be a synthesized attribute.
An inherited attribute belongs to a nonterminal on the right side of a
production. These characteristics borrow values from their siblings or parents.
********** 4 **********
--- page 5 ---
As long as the production at the parent has the non-terminal in its body, a
semantic rule connected to the production at the parent defines them.
correct identification of definition [2 marks]: L-attributed
definition
justification [ 4 marks]
it should include determining the type of each attribute in the semantic
rules
A   Explain in brief the different types of top-down parsers? Show the
working predictive parser
Types of top-down parser: [5 marks]
Recursive descent parser
Predictive parser
working [5 marks]
Input buffer:
it contains the string to be parsed, followed by $.
$, symbol used to indicate the end of the input string
Stack:
It contains a sequence of grammar symbols with $ on the
bottom.
Q4
Initially, it contains the start symbol of the grammar on
CO-; SO-;   [10]
top of $.
BL-
Parsing table:
It is a 2-D array M[A,a] where A is a nonterminal, a is a
terminal or symbol $.
The parser is controlled by a program as follows
The program considers X, the symbol on top of the stack and a ,
the current i/p symbol.
These 2 symbols determine the actions. There are 3
possibilities:
If X= a=$, the parser halts and announces successful
completion
If X=a!=$, the parser pops X off the stack and advances
the input pointer to the next input symbol.
********** 5 **********
--- page 6 ---
If X is a nonterminal, the program consults entry M[X, a]
of the parsing table M. This entry will be either an X-
production of the grammar or an error entry.
If, for example, M[X, a]={X->UVW}, the parser replaces X on top
of the stack by WVU( with U on top).
If M[X, a]=error, the parser calls an error recovery routine.
B   Write the algorithm to find the basic blocks in a program.
Analyze the given three address code and find the basic blocks:
1. i=1
2. If i<= n goto 4
3. Goto 9
4. R1= a *b
5. R2= r1+c
6. X=r2
7. J=j+1
8. Goto 2
9. K=k*2
Algorithm [ 5 marks]
[10]
Algorithm: Partitioning three-address code into basic blocks.
Input: A sequence of three address instructions.
Process: Instructions from intermediate code which are leaders are
determined. The following are the rules used for finding a leader:
1. The first three-address instruction of the intermediate code is a
leader.
2. Instructions that are targets of unconditional or conditional
jump/goto statements are leaders.
3. Instructions that immediately follow unconditional or
conditional jump/goto statements are considered leaders.
Each leader thus determined its basic block contains itself and all
instructions up to excluding the next leader.
Basic blocks [ 5 marks]
B1: 1, 2
B2: 3
********** 6 **********
--- page 7 ---
B3: 4,5,6,7, 8
B4: 9
A   Determine whether the following grammar is LR(1) or not
S → Aa |bAc |dc |bda
A → d
Augmented grammar [1 mark]
Finding closure and goto with DFA [ 4 marks]
Parsing table [4 marks]
Final answer [1 mark] ---it is LR(1) grammar
Q5
CO-; SO-;   [10]
BL-
B   Discuss the various data structures used for creating the symbol table.
There are a number of data structures that can be used to implement a
symbol table:
[10]
Linear List
Search trees
Hash Tables
Q6   A   Translate the given expression into three address code. Show the entries
of data structures: quadruples and triples   [10]
CO-; SO-;
BL-   (i)   a+b*c-d/(b*c) [5 marks]
********** 7 **********
--- page 8 ---
(ii)   a = (-b + c*d) + (c*d) [5 marks]
B   Discuss the concept of register allocation and evaluation order with
respect to code generation
Register allocation [5 marks]
Use of registers makes the computations faster in comparison to that of
memory, so efficient utilization
of registers is important. The use of registers is subdivided into two sub
problems:
1. During Register allocation – we select only those set of variables that
will reside in the
[10]
registers at each point in the program.
2. During a subsequent Register assignment phase, the specific register
is picked to access the
variable.
Evaluation Order[ 5 marks]
The code generator decides the order in which the instruction will be
executed. The order of
computations affects the efficiency of the target code. Among many
computational orders, some will
require only fewer registers to hold the intermediate results.
A   Consider the following grammar.
S → aABe
A → Abc | b
B → d
Parse the input string “abbcde” using stack implementation of shift-
reduce parser
Rightmost derivation in reverse [2 marks]
Q7
CO-; SO-;   [10]
BL-
Stack implementation steps [ 8 marks]
********** 8 **********
--- page 9 ---
The given string is accepted
B   Write a note on imperative and non-imperative programming
languages
Control Flow:
Imperative: Focuses on specifying step-by-step instructions on how to
achieve a task.
Non-Imperative: Focuses on specifying the desired outcome or
properties, allowing the language to handle control flow internally.
Mutability:
Imperative: Often involves changing the state of variables and data [10]
structures.
Non-Imperative: Prefers immutability, where data is not modified but
rather new objects are created.
Side Effects:
Imperative: Allows side effects like modifying global state, I/O
operations, and altering variables beyond returning values.
Non-Imperative: Minimizes or eliminates side effects, promoting a
more predictable and functional approach.
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 1044b245a3d0

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CS_7055/Compiler Design/ANS_Compiler Design(702CS0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (21 pages), mean OCR confidence 75.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Compiler Design
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks.
8. Assume suitable data if necessary.
Section A
Q1
CO-1 A 2 Marks – Compiler definition and optional Phase   [5]
BL-2   3 Marks - Output of each phase
- Compiler is translator, which translate code in HLL to LLL
-   Optional Phase – Code Optimization
Lexical Analysis – id1 = ( id2 + id3 – id4)/2
Syntax Analysis
=
/ \
R   /
/ \
- 2
/ \
+ c
/ \
a b
Semantic Analysis
The semantic analyzer checks the AST for logical consistency and type
compatibility.
Intermediate Code Generator
********** 1 **********
--- page 2 ---
1. t1 := a + b
2. t2 := t1 - c
3. t3 := t2 / 2
4. R := t3
Code Generator
LOAD R1, a
LOAD R2, b
ADD R1, R2
LOAD R2, c
SUB R1, R2
DIV R1, #2
STORE R, R1
CO-2 B 2 Mark – Backtracking & working   [5]
BL-4   3 marks - Parsing string ‘aaba’ using backtracking
Backtracking
Parsing String using bactracking
********** 2 **********
--- page 3 ---
CO-3 | C | 3 Marks -DAG [5]
BL-3 2 Marks - TAC

RK KKK RK KK 3 2h KKK RK Kk KK
--- page 4 ---
CO-3 D 2 Marks – Heap   [5]
BL-3   2 Marks – Static
1 Marks – Stack
Static Allocation:
-   Storage is allocated at compile time
-   Static storage has fixed allocation that does not change during program
execution
- As bindings do not change at runtime, no runtime support is required
- At compile time, compiler can fill the address at which the target code
can find the data it operates on
- FORTRAN uses the static allocation strategy
Limitations
-   Size of data objects should be known at compile time
-   Recursion is not supported
- Data structures cannot be created at runtime
Stack Allocation
-   Stack allocation manages the runtime storage as a stack, i.e., control
stack
-   Activation records are pushed and popped as activation begins and end
respectively
-   Locals are always bound to fresh storage in each activation, because a
new activation is onto a stack when a call is made
-   Values of locals are deleted as activation ends
- The data structure can be created dynamically for stack allocation
Limitations
-   Values of locals cannot be retained once activation ends
********** 4 **********
--- page 5 ---
- The memory addressing can be done using pointers and indexed
registers
-   This type of allocation is slower than static allocation
Heap allocation
-   Storage can be allocated and deallocated in any order
-   If the values of non-local variables must be retained even after the
activation record then such a retaining is not possible by stack allocation
-   It is used for retaining of local variables
- The heap allocation allocates the continuous block of memory when
required for storage of activation records. This allocated memory can be
deallocated when activation ends
-   Free space can be further reused by heap manager
-   It supports for recursion and data structures can be created at runtime
Limitation
Heap manages overhead.
Section B
Q2
CO-2 A 3 Marks – LR Parser & its working
BL-4   3 Marks – Classification
4 Marks – LR parser power and description
[10]
********** 5 **********
--- page 6 ---
B 4 Marks - Syntax-directed definition
CO-3   4 Marks – Syntax Tree   [10]
BL-3   2 Marks – S attributed and L attributed grammar
********** 6 **********
--- page 7 ---
Q3
CO-2 A 3 Marks – Roles of lexical analysis
BL-4   2 Marks – Eliminating comments   [10]
3 Marks – lexical error – num 1, a d d, float
********** 7 **********
--- page 8 ---
2 Marks – reason for the errors
Roles of Lexical Analysis
- Removal Comment
- Removal of white spaces (unwanted spaces)
-   Generating Tokens
- Symbol Table Preparation
-   Error recovery
Action Performed
- No unwanted spaces to remove
- Removal of comments /* Test Code*/ and // variable declaration
-   Lexical error – a d d (spaces) and space in num 2
-   Invalid variable name – float
-   Error recovery
Why Error
- RE or FA of token recognition not followed
CO-3 B   10 Marks – 02 marks to each optimization
BL-3
Peephole Optimization
- A statement-by-statement code-generations strategy often produces
target code that contains redundant instructions and suboptimal
constructs. The quality of such target code can be improved by applying
“optimizing” transformations to the target program.
[10]
- A simple but effective technique for improving the target code is
peephole optimization, a method for trying to improving the
performance of the target program by examining a short sequence of
target instructions (called the peephole) and replacing these instructions
by a shorter or faster sequence, whenever possible.
- The peephole is a small, moving window on the target program. The
code in the peephole need not be contiguous, although some
implementations do require this. It is characteristic of peephole
********** 8 **********
--- page 9 ---
optimization that each improvement may spawn opportunities for
additional improvements.
- During Peephole Optimization we perform following operations:
→ Redundant-instructions elimination
→ Flow-of-control optimizations (multiple jumps)
→ Algebraic simplifications
→ Use of machine idioms
→ Elimination of Unreachable code
There are various peephole optimization techniques.
Redundant Load and Store
The redundant operations are removed.
For example, loading and storing values on registers can be optimized.
For example,
a= b+c
d= a+e
It is implemented on the register(R0) as
MOV b, R0;
ADD c, R0;
MOV R0, a;
MOV a, R0;
ADD e, R0;
MOV R0, d;
This can be optimized by removing load and store operation, like in third
instruction value in register R0 is copied to a, and it again loaded to R0 in
the next step for further operation.
The optimized implementation will be:
MOV b, R0; instruction to Copy b to the register
ADD c, R0; instruction to Add c to the register, which is now b+c (a)
MOV R0, a; instruction to Copy the register to a
ADD e, R0; instruction to Add e to the register, now b+c+e [(a)+e]
MOV R0, d; instruction to Copy the register to d
Strength Reduction
********** 9 **********
--- page 10 ---
In strength reduction optimization, operators that consume higher execution
time are replaced by the operators consuming less execution time.
Like multiplication and division, operators can be replaced by shift
operators.
Initial code:
n = a * 2;
Optimized code:
b= a << 1;
//left shifting the bit
Initial code:
b = a / 2;
Optimized code:
b = a >> 1;
// right shifting the bit by one will give the same result
Simply Algebraic Expressions
The algebraic expressions that are useless or written inefficiently are
transformed.
For example:
a=a+0
a=a*1
a=a/1
a=a-0
//All these above expression are causing calculation overhead.
// These can be removed for optimization
Replace Slower Instructions with Faster
Slower instructions can be replaced with faster ones, and registers play an
important role. For example, a register supporting unit increment operation
will perform better than adding one to the register. The same can be done
with many other operations, like multiplication.
Add #1
SUB #1
//The above instruction can be replaced with
// INC R
// DEC R
********** 10 **********
--- page 11 ---
//If the register supports increment and decrement
Here X is loaded on ‘a’ twice and then multiplied. We can use dup function,
it will copy the value on the top of the stack( ‘X’ need not be loaded again),
and then we can perform our operation. It works faster and can be preferred
over slower operations.
a load X
a load X
Mul
// The above instructions can be replaced with
a load X
dup
Mul
Dead code Elimination
The dead code can be eliminated to improve the system's performance;
resources will be free and less memory will be needed.
int dead(void)
{
int a=1;
int b=5;
int c=a+b;
return c;
// c will be returned
// The remaining part of code is dead code, never reachable
int k=1;
k=k*2;
k=k+b;
return k;
// This dead code can be removed for optimization
}
Q4
CO-2 A 1 Mark – Augmented grammar
BL-4   1 Mark – Follow
5 Marks – LR(0) Items   [10]
3 Marks – SLR(1) table
A→aAa|bAb|ba   Goto(I0,b)   Goto(I4,a)
********** 11 **********
--- page 12 ---
Augmented Grammar G’   I3:   I7:
is:-   A→b.Ab   A→aAa.
A’→A   A→.aAb
A→aAa   A→.ba
A→bAb   A→b.a
A→ba
Closure of(A’→.A)   Goto(I2,A)   Goto(I5,b)
I0:   I4:   I8:
A’→.A   A→aA.a   A→bAb.
A→.aAa
A→.bAb   Goto(I2,a)------- I2
A→.ba   Goto(I2,b)------- I3
Goto(I0,A)   Goto(I3,A)   Goto(I6,A)---- I4
I1:   I5:   Goto(I6,b)----- I3
A’→A.   A→bA.b   Gotot(I6,a)------I2
Goto(I3,b)--------I3
Goto(I0,a)   Goto(I3,a)   Production
I2:   I6:   Numbering
A→a.Aa   A→a.Aa   A→aAa------------
A→.aAa   A→.aAa   1
A→.bAb   A→.bAb   A→bAb-----------
A→.ba   A→.ba   2
A→ba.   A→ba-----------3
Follow(A)={a,b,$
}
ACTION   GOTO
a   b   $   A
I0   S2   S3   1
I1
I2   S2   S3   4
I3   S6   S3   5
I4   S7
I5   S8
I6   S2/R3   S3/R3   R3   4
I7   R1   R1   R1
I8   R2   R2   R2
CO-3 B 5 Marks - optimization techniques applied
BL-3   5 Marks - Optimized code
int main() {
int a = 10, b = 20, c = 30, x, y, z;
[10]
int temp = a * b;   // Common subexpression
x = temp + temp + temp;
y = c * 5;
z = c;   // Constant propagation
********** 12 **********
--- page 13 ---
int t = a * b;   // Code motion (moved outside)
for (int i = 0; i < 10; i ++) {   // Loop unrolling
cout << t << endl;
i++;
cout << t << endl;
}
for (int i = 0; i < 5; i++) {
int p = i + 1;
int q = i + 2;
cout << p + q << endl;
}
int m = 15;   // Constant folding
int n = 30;   // Constant propagation
// Dead code eliminated (unused variable removed)
return 0;
}
Q5
CO-3 A 4 Marks – Sources of optimization
BL-3   6 Marks – Optimization of basic blocks
List the sources of optimization and explain the optimization of basic blocks.
Sources of optimization
Common sub-expression elimination
Copy propagation,
Dead-code elimination
Constant folding
Code Motion
Induction Variables
[10]
Reduction In Strength
Copy Propagation
Constant Folding
Optimization Of Basic Blocks
There are two types of basic block optimizations. They are :
-   Structure-Preserving Transformations
-   Algebraic Transformations
Structure-Preserving Transformations:
The primary Structure-Preserving Transformation on basic blocks are:
- Common sub-expression elimination
- Dead code elimination
- Renaming of temporary variables
********** 13 **********
--- page 14 ---
-   Interchange of two independent adjacent statements.
Common sub-expression elimination:
Common sub expressions need not be computed over and over again. Instead
they can be computed once and kept in store from where it’s referenced.
Example:
a: =b+c
b: =a-d
c: =b+c
d: =a-d
The 2nd and 4th statements compute the same expression: b+c and a-d
A basic block can be transformed to
a: = b+c
b: = a-d
c: = a
d: = b
Dead code elimination:
-   It is possible that a large amount of dead (useless) code may exist in the
program.
-   This might be especially caused when introducing variables and
procedures as part of construction or error-correction of a program -
once declared and defined, one forgets to remove them in case they
serve no purpose.
-   Eliminating these will definitely optimize the code.
Renaming of temporary variables:
- A statement t:=b+c where t is a temporary name can be changed to
u:=b+c where u is another temporary name, and change all uses of t to u.
-   In this a basic block is transformed to its equivalent block called normal-
form block.
Interchange of two independent adjacent statements:
• Two statements
t1:=b+c
t2:=x+y
can be interchanged or reordered in its computation in the basic block when
value of t1 does not affect the value of t2.
Algebraic Transformations:
-   Algebraic identities represent another important class of optimizations
on basic blocks.
-   This includes simplifying expressions or replacing expensive operation
by cheaper ones i.e. reduction in strength.
- Another class of related optimizations is constant folding. Here we
evaluate constant expressions at compile time and replace the constant
expressions by their values.
- The relational operators <=, >=, <, >, + and = sometimes generate
unexpected common sub expressions. Associative laws may also be
********** 14 **********
--- page 15 ---
applied to expose common sub expressions. For example, if the source
code has the assignments
a :=b+c
e :=c+d+b
the following intermediate code may be generated: a :=b+c
t :=c+d e :=t+b
Example:
x:=x+0 can be removed
x:=y**2 can be replaced by a cheaper statement x:=y*y
- The compiler writer should examine the language specification carefully
to determine what rearrangements of computations are permitted, since
computer arithmetic does not always obey the algebraic identities of
mathematics.
-   Thus, a compiler may evaluate x*y-x*z as x*(y-z) but it may not
evaluate a+(b-c) as (a+b)-c.
CO-3 B 4 Marks - subdivision of run time memory
BL-3   4 Marks - activation record
2 marks – activation tree
Subdivision of runtime memory
[10]
********** 15 **********
--- page 16 ---
Activation Record:
The contents of Activation records .
Return value:- it is used by called procedure to return a value to calling
procedure.
Actual Parameters -it is used by calling procedure to supply parameters to called
procedure.
Control Link - it points to activation record of the caller.
Access Link - it is used to refer to nonlocal data held in other activation
records
Saved machine status - it hold the information about status of machine before
the procedure is called.
Local Data - it hold the data that is local to the execution of the procedure.
Temporaries - it stores the value that arises in the evaluation of an expression
Activation Tree:
Q6
********** 16 **********
--- page 17 ---
CO-3 A 5 Marks – Flow control statements
BL-3   5 Marks – Control Flow translation of Boolean Expression
Flow Control Statements
-   These statements control the order of program execution.
Types:
-   Sequential – Statements execute in order.
-   Selection – if, if-else, switch
-   Iteration – for, while, do-while
- Jump – break, continue, return, goto
- We now consider the translation of Boolean expressions into three-
address code in the context of statements such as those generated by the
following grammar:
In these productions, nonterminal B represents a boolean expression and non-
terminal S represents a statement.
[10]
Control Flow translation of Boolean Expression
- When compiling, Boolean expressions are translated into conditional
jump instructions that control the flow of execution.
Example 6.22 : Consider again the following statement from Example 6.21:
Using the syntax-directed definitions in Figs. 6.36 and 6.37 we would obtain the code
in Fig. 6.38.
********** 17 **********
--- page 18 ---
if x < 100 goto Ly

goto L3

Lg: if x > 200 goto Ly
goto L;

Lq4: if x != y goto Lp
goto Li

Le: x=0

ly:

Figure 6.38: Control-flow translation of a simple if-statement

CO-2 |B | 5 Marks - LL(1)
BL-4 5 Marks — LR(0)

[10]

The given grammar is LL(1)

RK KKK RK KK 18 2h KKK RK Kk KK
--- page 19 ---
As there are Reduce-Reduce conflict in I0, the given grammar is not LR(0).
Q7
CO-1 A 5 Marks – diagram and language processing system
BL-2   - The Terms ‘cousins of compiler’ refers to the type of program which are
required for execution of the source program.
- There are programs with which compiler operates these are cousins of
compiler.
[5]
o Preprocessors
o Assembles
o Linker
o Loader
-   Preprocessors:-
********** 19 **********
--- page 20 ---
o Before compilation, the source program in processed by
preprocessor to prepare it for compilation
o   It replaces preprocessor directives with suitable contents and gives
modified source code.
o   It performs
▪   It permits user to include header files.
▪   It permits user to use Macros.
-   Assembler:-
o Compiler produces target program in assembly language
o Assembly language program is given as input to assembler
o Assembler translates that in machine level language.
-   Linkers and Loaders:-
o The largest programs are compiled in small pieces by the
compiler.
o To create target machine code of any source program successfully,
library files and other relocatable files are linked together by
linker.
o Loader reads the relocatable machine code and alter the
relocatable addresses.
o Then, Loader loads target file to memory for execution.
CO-2 B 2 Marks – Difference (2-3 differences)   [5]
BL-4   3 Marks – RE and FA for identifiers
Specification is defining what a token is (e.g., using regular expressions), while
recognition   is the process of finding those tokens in a character
stream. Specification creates the rules, and recognition uses those rules to scan
code and build tokens.
digit → [0-9]
digits → digits+
letter → [A-Za-z]
id → letter ( letter | digit )*
********** 20 **********
--- page 21 ---
CO-2 C 5 Marks - operator precedence table   [5]
BL-4
CO-3 D 3 Marks – Type Inference   [5]
BL-3   2 Marks - Polymorphic function
- Type inference means the compiler automatically determines the data
type of a variable.
- Example – C++ 11
o auto x = 10; // x is inferred as int
o auto y = 3.5; // y is inferred as double
- Example – Java 10 with var
o var name = "B Tech"; // inferred as String
o var number = 42; // inferred as int
- Polymorphic Functions: Functions that can work with multiple types.
-   Exaple (Java Generic/C++ Template)
public <T> void print(T value) {
System.out.println(value);
}
-   print(10) and print("Hello") both work — compiler determines type T at
compile-time.
- Type inference is helpful for a language like ML, which is strongly
typed, but does not require names to be declared before they are used.
Type inference ensures that names are used consistently.
X---------------------------------------------------------------------------------------------------------------------X
********** 21 **********
````
