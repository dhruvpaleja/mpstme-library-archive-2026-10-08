# Principles of Compiler Design: question papers in full

2 unique papers · 2015-16 to 2015-16 · Computer Engineering

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2015-16 · Final-Exam · Sem 6 · paper 014e0c873f7d

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/PRINCIPLES OF COMPILER DESIGN/PRINCIPLES OF COMPILER DESIGN B TECH (COMPUTER), 15-16 FINAL EXAM.pdf`
- Printed on paper: max marks: 60; duration hours: 3; exam date: 14/05/2016
- Text: ocr (3 pages), mean OCR confidence 86.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT 8 ENGINEERING

Programme: B. Tech (COMPUTER) Year: III Semester: VI

Academic Year: 2015-2016

Subject : Principles of Compiler Design
Marks: 60

Time : 2.00 pm to 5.00 pm
Durations: 3 (hrs)
Final-Examination

Date : 14/05/2016

cover of the answer book , which is provided for the use.

1. Question 1 is compulsory

2. Out of remaining question, attempt any 4 questions

3. In all 5 question to be attempted.

4. All question carry equal marks.
5. Answer to each new question to be started on afresh page.
6. Figure to the right indicate full marks.

7. Assume suitable data whenever necessary
Q.1 a. Explain Language processing system in detail. [5]
b. Explain the role of lexical analyzer. [3]
c. Eliminate Non-Determinism from the grammar. [2]

S-->aSSbS/aSaSb/abb/b

d. Eliminate Left Recursion from the grammar. [2]
S-->(L)/x
L-->L,S/S

Q.2, a. What is Symbol table and how it is maintained. Create a symbol table for a given code, [6]
int x;
void A( )
{
int a;
{
int b;
}
{
int d;
}
int y;
}
void B( )
t
int f;
}

b. What is Input Buffering? Explain techniques of buffer pair and sentinels,

[6]

'/3
--- page 2 ---
Q.3. a. Construct LL(1) parsing table for the following grammar and parse the string dbb [6]
S--> A
A-->BC | DBC
B -->bB’ | €
B’-->bB’ |e
C -->c |e
D-->a | d

b. Create a Recursive decent parser for the following grammar and parse the string abe. [6]

S-->ABd/aBc
A-->€
B-->b/c

Q.4 a. Construct CLR item set and parsing table for the following grammar. [6]
S-->L=R/R
L-->*R/id
R-->L

b. Construct SLR parsing table for the following grammar and parse the string id+id*id. [6]

E-->E+T/T
T-->T*F/F
F-->(E)/id

Q.5 a. Consider the grammar with the following translation rules and E as the start symbol. [6]

E— El # T { E.value = El.value * T.value }
| T{ E.value = T.value }

T— T1 & F {T.value = Tl.value + F.value }
| F{ T.value = F.value }

F > num {F.value = num.value }

Construct the parse tree and compute E.value for the root of the parse tree for the

expression: 243 &5#6&4.

[6]
b. Explain the Different Parameter passing techniques. With respect to dynamic and static
scoping.
catia
Q.6 a. Explain code optimization techniques in detail. [6]
pai b. Translate the input using following grammar. [3]
S->TR

2/3
--- page 3 ---
R->+T {Print (‘+’);R}/ €
T->num { print(num.val); }

Input: 9+5+2

c. Explain three address code and generate it for the following code. [3]
a=-b*d+c+(-b)*d

Q.7 a. Simplified the given code using DAG. [6]
Bl: tl=itj
t2=tl+k
k=t2
k=k+10;
t3=i+j;
t4=t3+20;
b=t4;
i=i+1;
J=i+4;
if i<=1000 goto Bl
b. Create a control flow graph for the following code.
begin [6]
i=0;
sum=0O;
while(i<=100)

sum=sum+i*i;
i=i+1;

end

3/3
````

## 2015-16 · Re-Exam · Sem 6 · paper 91d7f63159f0

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/PRINCIPLES OF COMPILER DESIGN/PRINCIPLES OF COMPILER DESIGN B TECH (COMPUTER) BATCH 2015-16 RE EXAM.pdf`
- Printed on paper: duration hours: 3; exam date: 05 July 2016
- Text: ocr (3 pages), mean OCR confidence 86.0

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY M.

Programme: B.Tech (Computer) Year: III.

Academic Year: 2015-16 t

i Batch: 2015-16

Subject: Principles of Compiler Design

Time: 2.00 pm - 5.00 pm

Date: 05 July 2016 Durations: 3 (hrs)

Re-Examination

Instructions — Candidates should read carefully the instructions printed on the question paper

and on the cover of the Answer Book, which is provided for their use.
NB: |

1) Question No. 01 is compulsory.

2) Out of remaining questions, attempt any four questions.

3) In all five questions to be attempted.

4) All questions carry equal marks.

_5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Q.1 a) Which one of the following is FALSE? [02]
a) basic block is a sequence of instructions where control enters the sequence at
the beginning and exits at the end.
b) Available expression analysis can be used for common subexpression
elimination.
c) Live variable analysis can be used for dead code elimination.
d) x=4* 5 = x= 20 is an example of common subexpression elimination.

b) Fora C program accessing X[i]fj][k], the following intermediate code is generated bya [02]
co compiler. Assume that the size of an integer is 32 bits and the size of a character is 8 bits.
t0=i+1024
tl=j*32
t2=k+4
t3=t1+t0
t4=t3 +42

tS = X[t4]
Which one of the following statements about the source code for the C program
| is CORRECT?
a) X is declared as “int X[32][32][8]”.
pa b) X is declared as “int X[4][1024][32]”.
c) X is declared as “char X[4][32][8]”.
d) X is declared as “char X[32][16][2]”.
--- page 2 ---
c) Substitution of values for names whose values are constant, is done in

[02]
a) local optimization

b) loop optimization

c).. constant folding

d) none of these
d) For the grammar below, a partial LL(1) parsing table is also presented along with the [02]

grammar. Entries that need to be filled are indicated as E] , E2, and E3. ¢ is the empty
string, $ indicates end of input, and, | separates alternate right hand sides of

productions.
S—>aAbB/|bAaBle
AS
B->S >
A b $
Ss El E2 SP «
A ADS ADS Error
|B B>S BSS E3 |
The FIRST and FOLLOW sets for the non-terminals A and B are .
(A) FIRST(A) = {a, b, ¢} = (B) _ FIRST(A) = fa, b, $}
FIRST(B) FIRST(B) = {a, b, s}
FOLLOW(A) = {a, b} FOLLOW(A) = {a, b}
FOLLOW(B) = {a, b, $} FOLLOW(B) = {$$}
© riksiie, ees _ FIRST(A) = {a, b} = FIRST(B)
FoLLowy-iay ———FOLEOMY fo
FOLLOW(B) = @ ;
e) The grammar S — aSa|bS |cis [02]
(A) LL(1) but not LR(1) (B) LR(1) but not LR(1)
(C) Both LL(1) and LR(1) ~~ (D) Neither LL(1) nor LR(1)
f) Inacompiler, keywords of a language are recognized during [02]
(A) parsing of the program
(B) the code generation
(C) the lexical analysis of the program
(D) dataflow analysis
Q.2 Draw and explain phases of compiler with an example. [12]
— Q.3 a) Explain Input buffering. Justify can we run out of buffer space? [06]
= b) Construct NFA from (0+1)"(00+11) and draw minimize DFA. [06]
Q.4 a) Explain Three address code with an example. Also justify why do we need copy [06]
instruction?
b) Explain Type checking. [06]

3

DB
--- page 3 ---
Q.5 Explain issues in design of code generator. [12]
Q.6 a) Design predictive parser for following grammar [06]
EX E+T|T
TOTFVIV
V> id
b) Design LR[0] parser for given grammar [06]
S>aSblab
Q.7 a) Explain Switch statement with example. [06]
b) Explain static verses Dynamic Storage allocation. [06]
x ’
lax
````
