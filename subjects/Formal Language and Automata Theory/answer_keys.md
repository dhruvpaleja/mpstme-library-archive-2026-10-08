# Formal Language and Automata Theory: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 996de773b96b

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Formal Language and Automata Theory/ANS_Formal Language and Automata Theory(702CO0C043)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (29 pages), mean OCR confidence 80.1
- 3 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Formal Language and Automata Theory
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 29 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q.1 is Compulsory
5. Attempt any four questions from the remaining questions
6. Assume suitable data if necessary
Q1   Attempt all Sub-questions   Marks
CO-1 a   Given sets A={pq,qr} B={01,23} Estimate the followings A.A, A.B, A+B, (A+B).A,   5
BL-2   A.(A+B)
Ans:   (1 Mark each)
A.A={pqpq, pqqr, qrpq, qrqr}
AB = {pq01, pq23, qr01, qr23}
A+B = {pq, qr, 01, 23}
(A+B).A= {pq, qr, 01, 23}.{pq, qr}= {pqpq, pqqr, qrpq, qrqr, 01pq, 01qr, 23pq, 23qr}
A.(A+B)= {pq, qr}. {pq, qr, 01, 23}= { pqpq, pqqr, pq01, pq23, qrpq, qrqr, qr01, qr23}
b   Discuss and simulate Deterministic Finite Automata for string containing with abb over   5
Σ={a,b}
Ans:
1. Problem Understanding   (1 Mark)
Design a DFA that accepts all strings containing substring “abb”.
✔ Examples:
• Accepted: abb, aabb, abba, babb
CO–2,   •   Rejected: ab, aba, baa
BL-2
2. Idea of DFA   (1 Mark)
Track progress of substring “abb”:
• q0 → Start state
• q1 → String ‘a’
• q2 → seen ‘ab’
• q3 → seen ‘abb’ (final state)
********** 1 **********
--- page 2 ---
3. DFA Transition Table and Graph   (2 Marks)
State   a   b
→ q0   q1   q0
q1   q1   q2
q2   q1   q3
*q3   q3   q3
✔ q3 is the accepting state
4. Simulation (Example: aabb)   (1 Mark)
Step Input State
Start —   q0
a   q1
a   q1
b   q2
b   q3
String accepted
c   Discuss NP-Complete problems with suitable example.   5
Ans:
1. Definition   (2 Marks)
A problem is NP-Complete if:
1. It belongs to NP (solution can be verified in polynomial time)
2. It is NP-hard (every NP problem can be reduced to it in polynomial time)
CO-4,
BL-2 ✔ These are the hardest problems in NP
2. Key Idea   (1 Mark)
•   If any NP-Complete problem is solved in polynomial time, then P = NP
• No polynomial-time solution is known so far
3. Example   (1 Marks)
********** 2 **********
--- page 3 ---
Boolean Satisfiability Problem (SAT)
• Given a Boolean formula, determine if there exists an assignment of variables
that makes it true
Example:
(x + y')(x' + z)
Check if some assignment satisfies it
SAT was the first NP-Complete problem
4. Significance ( 1 Mark)
• Helps classify computational problems
• Widely used in optimization, cryptography, and AI
d   Discuss the Universal Language (Lᵤ) and explain why it is recursively enumerable but   5
not decidable.
Ans:
1. Definition   (1.5 Marks)
The Universal Language is defined as:
Lu = { (M, w )| M is a TM and accepts w }
• ⟨M, w⟩ represents encoding of a Turing Machine M and input w
2. Lu is Recursively Enumerable   (1.5 Marks)
CO-4,
BL-2   • A Universal Turing Machine (UTM) can simulate M on input w
•   If M accepts w → UTM accepts
•   If M does not accept → UTM may run forever
✔ Hence, Lu is recursively enumerable (RE)
3. Lu is NOT Decidable   (2 Marks)
• Assume Lu is decidable
• Then we could determine whether M accepts w for all inputs
• This would solve the Halting Problem, which is impossible
✔ Therefore, contradiction → Lu is not decidable
Lu is RE but not decidable, showing limits of computation
Q.2 Attempt any four questions (Attempt Any 4)
1.   a   Convert following Context Free Grammar to Chomsky Normal Form:   5
CO-3,   S → AACD
BL-3   A → aAb | ε
********** 3 **********
--- page 4 ---
C >aCla
D > aDa|bDb |e
Ans:

Given Grammar (0.5 Mark)

S — AACD
A aAb le
C-aCla
D— aDa|bDb|le

Step 1: Remove €-productions (1 Mark)
Nullable variables: A, D

Modify productions:

e¢ S—AACDJACD|AAC|AC|CD|C
e A-—aAb|ab

e C-aCla

e D-aDa|bDb|aa| bb

Step 2: Remove Unit Productions (0.5 Mark)
¢ S$ —+C= replace with C’s productions

So:

e¢ S—AACD]ACD|AAC|AC|CD|aC|a

Step 3: Replace Terminals in Long Productions (1 Mark)

Introduce new variables:

e X-a
e Yb

FIC 7) IC HOH
--- page 5 ---
b   Describe the process of verifying a solution in polynomial time. How does it relate to   10
1.   NP?
CO-4,
BL-4   Ans:
********** 5 **********
--- page 6 ---
1. Definition of Verification (2 Marks)

Verification means checking whether a given solution (certificate) to a problem is correct.

e Input: instance x and certificate y

e Averifier algorithm checks if y proves that z is a valid solution

v The key requirement: verification must be done in polynomial time

2. Polynomial-Time Verifier (2 Marks)
A verifier V (a, y) is a deterministic algorithm such that:

¢ Runs in time O(n*) for some constant k
e Accepts if y is a correct solution for x

v |f such a verifier exists - problem is efficiently checkable

3. Example (3 Marks)

Boolean Satisfiability Problem (SAT)

e Input: Boolean formula
© Certificate: assignment of variables

wv Verification:
e Substitute values into formula

e Evaluate in polynomial time

Example:

Formula: (2 + y’)(2’ + z)
Assignment: z = lry—0,z—1
wv Evaluate - TRUE — accepted

FIC 6 I HF
--- page 7 ---
4. Relation to NP (2 Marks)

A problem belongs to NP (Nondeterministic Polynomial time) if:

e Asolution can be verified in polynomial time

Formally:
xe L => dysuch that V(z,y) = 1

wv NP = class of problems with efficient verification

5. Key Insight (1 Mark)

e Finding solution may be hard

e Verifying solution is easy

w& Example: solving SAT is hard, but checking a solution is easy

ic. {Construct a minimum state automaton for the following DFA

a b
—>4q
1] q2
» ja\4
1. ql | q2 | g3
CO-2,
BL-3 q2 | q2 | q4
*q3 | q3 | g3
*q4 | q4 | q4
q5_| 45 | a4

Ans:

FIC 7 IC OHH
--- page 8 ---
1. Given DFA (0.5 Mark)

States: {q0, q1, q2, 43, 94, q5}
Final states: {q3, q4}

2. Remove Unreachable States (0.5 Mark)
¢ From qO, reachable states: q1, q2, q3, q4

e q5 is unreachable — remove it

Remaining states: {q0, q1, q2, q3, q4}

3. Initial Partition (1 Mark)

e Final states: {q3, q4}
e Non-final states: {q0, q1, q2}

4. State Equivalence (2 Marks)

Check Final States (q3, q4):
* q3 — (a-q3, b-q3)
« 4 — (a-a4, b-q4)
w Same behavior — q3 = q4

Check Non-Final States:
* qi — (a-q2, b-q3)
® q2 — (a-q2, b-+q4)
w Since q3 = g4 = transitions equivalent

+ ql=q2

FIC QF EH 1
--- page 9 ---
2.   a   Apply concept of Turing machine to perform subtraction operation. Simulate the   10
CO-4,   machine with following example:4-5
BL-3
Ans:
1. Concept   (1 Marks)
We perform subtraction using unary representation:
• 4 → 1111
• 5 → 11111
•   Input format:
[
1111 # 11111
]
✔ Idea:
• Cancel one 1 from both sides repeatedly
•   If left side becomes empty first → result is negative
********** 9 **********
--- page 10 ---
2. Idea of Turing Machine   (2 Marks)
• Scan leftmost 1 and mark it (X)
• Move right of # and cancel one 1 (mark X)
• Repeat process
•   If right side still has 1 after left is empty → negative result
3. Formal Definition   (2 Marks)
M = (Q, Σ, Γ, δ, q0, B, F)
• Q = {q0, q1, q2, q3, qf}
• Σ = {1, #}
• Γ = {1, X, #, B}
• q0 = start state
• F = {qf}
4. Transition Function   (3 Marks)
State   Symbol   Next   Write   Move
q0   1   q1   X   R
q1   1   q1   1   R
q1   #   q2   #   R
q2   1   q3   X   L
q3   1/X   q3   same   L
q3   #   q0   #   R
q0   #   qf   #   S
5. Simulation for 4 – 5   (2 Marks)
Initial Tape:
1111#11111
Stepwise Cancellation:
1. Cancel one pair →
X111#X1111
2. Cancel second pair →
XX11#XX111
3. Cancel third pair →
XXX1#XXX11
4. Cancel fourth pair →
XXXX#XXXX1
Final Observation:
•   Left side empty
• Right side still has 1
✔ Result is negative (−1)
********** 10 **********
--- page 11 ---
b   Explain the concept of reduction between languages. Using this concept, prove that the   10
emptiness problem is undecidable.
Ans:
2.
CO-4,
BL-2
********** 11 **********
--- page 12 ---
3.   a   Apply concept of Turing machine to decrement the binary number by 1.   10
CO-4   Simulate the machine with following example:1010
BL-3   Ans:
********** 12 **********
--- page 13 ---
1. Concept (2 Marks)

To decrement a binary number by 1:
e Start from the rightmost bit (LSB)
e Rules:
e If bit = 1— change to 0 and stop
e If bit = 0 > change to 1 and move left (borrow)

wv Example:
1010 - 1 = 1001

2. Idea of Turing Machine (2 Marks)

¢ Move to the right end of the binary number
e Traverse left performing subtraction:

e Flip 0 > 1 until first 1 is found

e Change that 1 — 0 and halt

3. Formal Definition (2 Marks)

© Q= {q0, q1, gf}

e ={0,1}

© 1 = {0,1,B}

e qO = start state

e qf = final state

FIR ICR 7] QI HO
--- page 14 ---
b   Explain the restrictions on productions in Context-Sensitive Grammars with suitable   10
3.   examples.
CO-3,
BL-2   Ans:
********** 14 **********
--- page 15 ---
1. Introduction (2 Marks)

A Context-Sensitive Grammar (CSG) is a grammar in which productions are applied depending on the
context of a non-terminal.

e It generates context-sensitive languages
¢ Equivalent computational model: Linear Bounded Automaton (LBA)

2. General Form of Productions (2 Marks)

A production in CSG has the form:
aAB > ay8

Where:
e A=non-terminal
e a, = context (strings of terminals/non-terminals)
©   =non-empty string

@ The replacement of A depends on its surrounding context

3. Restrictions on Productions (4 Marks)

(i) Non-contracting Property

|RHS| > |LHS|
e Length of RHS must be greater than or equal to LHS
e Ensures no shrinking of strings

wv Example:

e Valid: aA — abA
e Invalid: AB + A

FRR IC 7 DA HOH
--- page 16 ---
(ii) No €-productions (except special case)

¢ Productions like A — € are not allowed

w Exception:

* S — € allowed only if:
® «ee language

® § does not appear on RHS

(iii) Context Dependency

¢ Replacement depends on surrounding symbols

wf Example:
« aAb— aBb

(Here A changes only when between a and b)

(iv) Single Non-terminal Replacement in Context

* Only one non-terminal is replaced at a time

w Example:

¢ Valid: aAb > aBb
« Invalid: AB + CD (not context-sensitive form)

FRR ICR 7 6 AC OH
--- page 17 ---
4, Example of CSG (1 Mark)
Language: L = {a"b"c" | n > 1}

Sample rules:

e aA-aa
« aB—-ab
« bB- bb

w Requires context — cannot be generated by CFG

5. Conclusion (1 Mark)
¢ CSG productions are strictly controlled
« They ensure no reduction in string length and context-based rewriting

e This makes them more powerful than CFGs

4.
CO-3,
BL-2

la

Show that the language:

IL={ww | wE{a,b}*} is context-sensitive. Justify your answer.
Ans:

10

FRR ICR] AC OH
--- page 18 ---
1. Understanding the Language (2 Marks)

e The language consists of any string followed by itself
e Examples:

® ee

® ab — abab

e aab — aabaab

w Requires copying and matching arbitrary strings

2. Not Context-Free (1 Mark)

* This language cannot be generated by a Context-Free Grarmmar (CFG)

e Because CFGs cannot compare two arbitrary substrings

w Hence, we need a more powerful model

3. Context-Sensitive Nature (4 Marks)

To show L is context-sensitive, we justify using:

Linear Bounded Automaton (LBA)

« ACSG is equivalent to LBA
« LBA works with limited tape (linear to input size)

Working Idea of LBA for ww:
1. Divide string into two halves
2. Mark first symbol in first half
3. Match with corresponding symbol in second half
4. Repeat for all symbols
5. Accept if all symbols match

# This requires context-sensitive checking L

FR ICR 7] QA HH
--- page 19 ---
4. Justification (2 Marks)

e¢ The machine must remember and compare positions
e Requires context and length control

e LBA can perform this using bounded memory

@v Therefore,

L = {ww} € Context-Sensitive Languages

5. Conclusion (1 Mark)

e Language is not context-free but context-sensitive

e Can be recognized by Linear Bounded Automaton

4.
CO-3,
BL-3

lb {Apply Push Down Automata concept and recognize L={a"b*" |n>=1 }
Ans:

10

FRR ICR 7 QI OR
--- page 20 ---
1. Understanding the Language (2 Marks)
e Number of b’s is twice the number of a's

e Structure:

2
ab"

w Examples:

* Accepted: abb, aabbbb, aaabbbbbb
« Rejected: ab, aabb, aaabbbb

2. Idea of PDA (2 Marks)

* For each a, push two symbols (A A) onto stack
« For each b, pop one symbol

« If stack becomes empty exactly at end — accept

w Ensures: number of b's = 2 x number of a's

3. Formal Definition (2 Marks)

© Q= {g0, q1, qf}

e = {a,b}

e [={A, ZO}

® q0O = start state

« ZO = initial stack symbol

e F = {qf}

FRI ICR DO) A RH
--- page 21 ---
5.   a   Describe symbol, alphabet, string, language, string operations including union and   10
CO-1,   concatenation, Kleene closure and positive closure with following example: A= {a,b}
BL-2   B= {c,d}.
Ans:
********** 21 **********
--- page 22 ---
Given:

e A= {a,b}, B = {c,d}

1. Symbol (1 Mark)

A symbol is the smallest unit in a language.
wv Examples: a, b, c, d

2. Alphabet (1 Mark)

An alphabet is a finite set of symbols.

3. String (1 Mark)

A string is a finite sequence of symbols from an alphabet.
& Examples:

e From A: a, ab, ba
e From B:c, cd
e Mixed: abcd

4. Language (1 Mark)

A language is a set of strings over an alphabet.
wv Examples:

e L, = {a,b, ab}
e Ly = {c,d,cd} V

FIR ICR DAC HH
--- page 23 ---
b   Discuss Church-Turing thesis with Example.   5
Ans:
1. Definition   (2 Marks)
The Church–Turing Thesis states that:
Any function that can be effectively computed by an algorithm can be computed by a
5.   Turing Machine.
CO-4, ✔ It connects the informal notion of algorithm/computation with the formal model
BL-2
of a Turing Machine (TM)
2. Key Idea   (1 Mark)
•   All reasonable models of computation (algorithms, programs) have equivalent
power
• Examples of equivalent models:
********** 23 **********
--- page 24 ---
o Turing Machine
o Lambda Calculus
o Recursive functions
✔ Hence, TM captures the limits of computation
3. Example   (2 Marks)
Consider computing the addition of two numbers:
•   Input: 2 + 3
• Any algorithm (manual or program) can compute it
• A Turing Machine can also perform addition using symbols on tape
✔ Therefore, addition is Turing-computable
• Church–Turing Thesis defines what is computable
•   It is a theoretical principle, not a formal theorem
c   Apply Regular Expression concept to convert RE to NFA for following   5
5.   i)   String ends with 011
CO-2,   ii)   Strings having exactly two 0’s.
BL-3
Ans:
********** 24 **********
--- page 25 ---
6.   a   Apply Mealy Machine concept to design a machine that generates 2’s   10
CO-2,   complement of binary number and convert it into Moore machine.
BL-3   Ans:
1. Concept of 2’s Complement (2 Marks)
Steps to compute 2’s complement of a binary number:
********** 25 **********
--- page 26 ---
1. Traverse from right to left
2. Copy bits unchanged until first ‘1’
3. After first ‘1’, flip all remaining bits (0↔1)
✔ Example:
10100 → 01100
2. Idea of Mealy Machine (2 Marks)
• Output is produced on transitions
• Use two states:
o q0 → before first ‘1’ (copy bits)
o q1 → after first ‘1’ (complement bits)
3. Mealy Machine Design (3 Marks)
States:
• q0 (start state)
• q1
Transition Table (Mealy Machine)
State   Input   Next State   Output
→ q0   0   q0   0
q0   1   q1   1
q1   0   q1   1
q1   1   q1   0
✔ q0: copy bits until first ‘1’
✔ q1: complement all bits
4. Explanation (1 Mark)
•   First ‘1’ triggers transition from q0 → q1
•   After that, all bits are flipped
✔ Thus, correct 2’s complement is generated
5. Conversion to Moore Machine (2 Marks)
Key Rule:
• Output depends only on state, not transition
• May require additional states
********** 26 **********
--- page 27 ---
Moore States:
• A (q0, output 0)
• B (q1, output 1)
• C (q1, output 0)
Moore Transition Table
State Output Input 0 Input 1
A   0   A   B
B   1   B   C
C   0   B   C
b   Discuss Ambiguity in the Grammar with suitable example.   10
Ans:
6.
CO-3,
BL-2
********** 27 **********
--- page 28 ---
Two Different Interpretations:
Parse 1:

id + (id * id)
Parse 2:

(id + id) * id

v Both are valid derivations - grammar is ambiguous

Leftmost Derivations:

Derivation 1:
E>E+E=>id+E>id+E*E = id+idxid
Derivation 2:
E> E*E>E+E+E=>id+id*id

v Different derivations — same string

4. Causes of Ambiguity (1 Mark)

e Lack of operator precedence

e Lack of associativity rules

FI ICR 2 QA HH
--- page 29 ---
5. Removing Ambiguity (1 Mark)

Use separate non-terminals to enforce precedence:

E>E+T\|T
TsoT*F\|F
F = (EB) | id

w Ensures:

e « has higher precedence than +

* Grammar becomes unambiguous

6. Conclusion (1 Mark)
« Ambiguity causes multiple interpretations
e Itis undesirable in compiler design

® Must be removed for deterministic parsing

FAR ICR QA HH
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 622446935eef

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Formal Language and Automata Theory/ANS_Formal Language and Automata Theory(702CO0C043)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2025
- Text: mixed (13 pages), mean OCR confidence 56.5
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Formal Language and Automata Theory
Date: 09 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory...
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain Church Turing Thesis.
Any computation that can be performed by a human following
an algorithm can also be performed by a Turing machine..In
1930, this statement was first formulated by Alonzo Church
and is usually referred to as Church’s thesis, or the Church-
Turing thesis. However, this hypothesis cannot be proved.
The recursive functions can be computable after taking
following assumptions:
CO-4 ;   5
1. Each and every function must be computable.
BL-1
2. Let ‘F’ be the computable function and after performing
some elementary operations to ‘F’, it will transform a new
function ‘G’ then this function ‘G’ automatically becomes
the computable function.
3. If any functions that follow above two assumptions must
be states as computable function.
********** 1 **********
--- page 2 ---
b.   Identify a CFG for the languages defined by the following
expression
2.5 Marks
1. L={aibjck | i,j,k>= 0, and i =j or j= k}
S->S1|S2
S1->AB
CO-3 ;   A->aAb|ab   5
BL-3   B->Bc|c
S2->A1B1
A1->aA1|a
B1->bB1C|bC
2.5 Marks
2. L={wϵ{0,1}| w=wR and |w| is even}
S->0S1|1S0|10||01
c.   Construct DFA which accept a binary number not divisible by
3.
Language- 1Marks
Machine- 4 marks
Tansition Table -1 Marks
∑={0,1}
CO-2 ;   5
BL-3
d.   Discuss power of Turing Machine over Push Down Automata
5
CO-3;   with example
BL-3
Discussion- 2.5 Marks
********** 2 **********
--- page 3 ---
TMs can recognize any language, including those that PDAs
cannot, due to their ability to store and manipulate an infinite
amount of memory on a tape, whereas PDAs are limited by a
stack.
Example :2.5 Marks
CO-   Compare NFA and DFA. Convert Following NFA into DFA
2;   [Write solutions with all steps also represent tuples of NFA
BL-3 and DFA]
Q2
[10]
********** 3 **********
--- page 4 ---
Table – 6 Marks
Diagram -4 Marks
CO-   Convert the following grammar G to Griebach Normal Form.
3;
G={(A1,A2,A3),(a,b),P,A1}, where P consists of the following
BL-3
productions:
A1->A2A3
A2->A3A1|b
A3->A1A2|a
[10]
Q3   CO-   Compare Type-0, Type-1, Type-2,Type-3
1;   [10]
BL-2 (Grammars,Languages and Automata) in term of Chomsky
********** 4 **********
--- page 5 ---
Hierarchy.
The Chomsky Hierarchy categorizes grammars, languages, and
automata into four types: Type-0 (Unrestricted), Type-1
(Context-Sensitive), Type-2 (Context-Free), and Type-3
(Regular), with each level representing a restriction in
generative power.
Here's a comparison of the four types:
Type-0 (Unrestricted Grammar/Languages):
Grammar: The most general type, with no restrictions on
production rules.
Language: Recursively enumerable languages, recognized by
Turing machines.
Automata: Turing machine.
Example: Any language that can be generated by a Turing
machine.
Type-1 (Context-Sensitive Grammar/Languages):
Grammar: Production rules must have the form αAβ → αγβ,
where A is a non-terminal, and α, β, γ are strings of terminals
and non-terminals.
Language: Context-sensitive languages, recognized by linear
bounded automata.
Automata: Linear bounded automaton.
Example: Languages like {a^n b^n c^n | n >= 0}.
Type-2 (Context-Free Grammar/Languages):
Grammar: Production rules have the form A → γ, where A is a
non-terminal and γ is a string of terminals and non-terminals.
Language: Context-free languages, recognized by pushdown
automata.
Automata: Pushdown automaton.
Example: Languages like {a^n b^n | n >= 0}.
Type-3 (Regular Grammar/Languages):
Grammar: Production rules must have the form A → a or A →
aB, where A and B are non-terminals, and a is a terminal.
Language: Regular languages, recognized by finite state
automata.
Automata: Finite state automaton.
Example: Languages like {a^n | n >= 0}.
********** 5 **********
--- page 6 ---
CO-   Design a DFA where ∑=(a,b) such a way that Let string is w,
2;
Number of a(w) mod 2= 0 and Number of b(w) mod 4= 1
BL-3
[10]
Q4   CO-   Define Arden’s Theorem.
2;   Convert the given DFA to Regular Expression using Arden’s   [10]
BL-3 Theorem:
********** 6 **********
--- page 7 ---
a cl
jn - qi uct »
wiy rdun's Th.
ak g, 1 CO”
m ¢ 3,07 9,0 + &,
= Got G00 7 <
a sy. gna”
--- page 8 ---
Re Dit Fa.
(1 +000)"

(o+l (r0n"00} 1
‘to. 0)

“x, (ars
astooy Cet! (ive) °).

_ (or (4

CO- | Compare PDA with NPDA.

BL3 | Construct PDA for L= {a'bickd! | iz=k or j==I such that i,j,k,]
>=1}
DFA NDFA
The transition from a state is to a single The transition from a state can be to
particular next state for each input multiple next states for each input symbol.
symbol. Hence it is called deterministic. Hence it is called non-deterministic.
Empty string transitions are not seen in NDFA permits empty string transitions.
DFA
[10]
Backtracking is allowed in DFA In NDFA, backtracking is not always
possible
Requires more space Requires less space.

Astring is accepted by a DFA, if it transits | A string is accepted by a NDFA, if at least
to a final state. one of all possible transitions ends in a
final state.

FIC QF EH 1
--- page 9 ---
CO-   Explain ambiguous grammar. Convert the following grammar
2;
into Chowmsky normal form.
BL-3
S->bA|aB
A->bAA|aS|a   [10]
Q5
B->aBB|bS|b
• Ambiguous grammars: These grammars can create more
than one derivation tree for the same string. This means that
a string can have different meanings or interpretations
depending on how it’s parsed.
********** 9 **********
--- page 10 ---
CO-   Design a Turing Machine to find the value of log2(n), where n
3;
is any binary number and perfect power of 2.   [10]
BL-5
********** 10 **********
--- page 11 ---
CO-   Design a Turing Machine that recognizes binary palindromes.
3;
BL-3
[10]
Q6
CO-   Prove ‘Regular sets are closed under
2;   1. Union
BL-2   2. Concatenation
3. Complement   [10]
4. Difference
Closure properties on regular languages are defined as certain
********** 11 **********
--- page 12 ---
operations on regular language that are guaranteed to produce
regular language. Closure refers to some operation on a
language, resulting in a new language that is of the same
“type” as originally operated on   i.e., regular. Regular
languages are closed under the following operations:
Consider that L and M are regular languages
Complement: The complement of a language L (with
respect to an alphabet E E such that E∗ E∗ contains L)
is E∗ E∗ –L. Since E∗ E∗ is surely regular, the
complement of a regular language is always regular.
Union: Let L and M be the languages of regular
expressions R and S, respectively.Then R+S is a regular
expression whose language is(L U M).
Set Difference operator: If L and M are regular languages,
then so is L – M = strings in L but not M. Proof: Let A and
B be DFA’s whose languages are L and M, respectively.
Construct C, the product automaton of A and B make the
final states of C be the pairs, where A-state is final but B-
state is not.
CO-   Write short notes: (Any 2)
4;
1. P and NP, NP-completeness
BL-2
In computer science, P and NP are complexity classes,
with P representing problems solvable in polynomial
time, and NP representing problems where solutions
can be verified in polynomial time. NP-completeness
identifies the "hardest" problems in NP, where solving
Q7   one would lead to polynomial-time solutions for all NP
[20]
problems.
2. Rice’s Theorem
Rice's Theorem, a cornerstone of computability theory,
states that all non-trivial semantic properties of
programs (or Turing machines) are undecidable,
meaning there's no general algorithm to determine if a
program possesses a given semantic property.
3. Universal Turing Machine
********** 12 **********
--- page 13 ---
A Universal Turing Machine (UTM) is a theoretical computer
model that can simulate the behavior of any other Turing
machine by reading its description and input, making it a
programmable, universal computational device.
********** 13 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 23112131bb2a

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_CSE_DS_7011/Formal Language and Automata Theory/ANS_Formal Language and Automata Theory(702CO0C043)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Jul 2025
- Text: mixed (9 pages), mean OCR confidence 58.4
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Formal Language and Automata Theory
Date: 11 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory...
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Universal Turing Machine
A Universal Turing Machine (UTM) is a theoretical computer model
that can simulate the behavior of any other Turing machine by reading
CO-4 ;   its description and input, making it a programmable, universal   5
BL-1
computational device.
b.   Identify a CFG for the languages defined by the following
expression
2.5 Marks Each
CO-3 ;   5
1. L=(baa+abb)*
BL-3
S->AS|BS|epsilon
A->baa
B->abb
********** 1 **********
--- page 2 ---
2. Language containing words that have different first and last
letters
a (a+b)*b+b(a+b)*a
S->aAb|bAa
A->aA|bA|Epsilon
c.   Construct DFA in which every 'a' should never followed by 'bb'
Given: Input alphabet, Σ={a, b}
Language- 1Marks
Machine- 4 marks
Tansition Table -1 Marks
CO-2 ;   5
BL-3
d.   Discuss power of Push Down Automata over Finite State Machine
with example   5
Discussion- 2.5 Marks
The Pushdown Automata (PDA) is more powerful than a Finite State
CO-3;
Machine (FSM) because it has an additional memory component — a
BL-3   stack — which allows it to recognize a broader class of languages:
Context-Free Languages (CFLs), whereas FSMs can only recognize
Regular Languages.
Example :2.5 Marks
CO-   Compare NFA and DFA. Convert Following NFA into DFA [Write
2;   solutions with all steps also represent tuples of NFA and DFA]
BL-3
Q2
[10]
********** 2 **********
--- page 3 ---
Table — 6 Marks
Diagram -4 Marks

CO-

BL-3

Convert the following grammar G to Griebach Normal

Form.
jelutien: since {Cave is ho Wul) production Ne Unit predaction and he
Zz production, So Geto nant Step Baler
In GNF ADA TIT) —@O
AD aR
A> aABco— (era Teta NT
a> AABC CR —————————
A>, AA BCD
\ ave alleoed
SPAR fer AD SS Se - - saeel
> AAO. Trev ——
an sa bA-@e=—]| A> as -—© S24

[10]

FC QI a iar
--- page 4 ---
CO-   (Grammars,Languages and Automata) in term of Chomsky
1;
Hierarchy.
BL-2
The Chomsky Hierarchy categorizes grammars, languages, and automata into
four types: Type-0 (Unrestricted), Type-1 (Context-Sensitive), Type-2
(Context-Free), and Type-3 (Regular), with each level representing a restriction
in generative power.
Here's a comparison of the four types:
Type-0 (Unrestricted Grammar/Languages):
Grammar: The most general type, with no restrictions on production rules.
Language: Recursively enumerable languages, recognized by Turing machines.
Automata: Turing machine.
Example: Any language that can be generated by a Turing machine.
Type-1 (Context-Sensitive Grammar/Languages):
Grammar: Production rules must have the form αAβ → αγβ, where A is a non-
terminal, and α, β, γ are strings of terminals and non-terminals.
Language: Context-sensitive languages, recognized by linear bounded
automata.
Automata: Linear bounded automaton.
Example: Languages like {a^n b^n c^n | n >= 0}.
Type-2 (Context-Free Grammar/Languages):
Grammar: Production rules have the form A → γ, where A is a non-terminal
and γ is a string of terminals and non-terminals.
Language: Context-free languages, recognized by pushdown automata.   [10]
Q3
Automata: Pushdown automaton.
Example: Languages like {a^n b^n | n >= 0}.
Type-3 (Regular Grammar/Languages):
Grammar: Production rules must have the form A → a or A → aB, where A
and B are non-terminals, and a is a terminal.
Language: Regular languages, recognized by finite state automata.
Automata: Finite state automaton.
Example: Languages like {a^n | n >= 0}.
CO-   Design a DFA where ∑=(a,b) such a way that, Number of a(w) mod
[10]
2;   3= 0 and Number of b(w) mod 3= 0
********** 4 **********
--- page 5 ---
BL-3
CO-   Define Arden’s Theorem.
2;   Convert the given DFA to Regular Expression using Arden’s
BL-3 Theorem:
Q4
[10]
********** 5 **********
--- page 6 ---
Q= WO [ai Citol*] 00+ €
= 4 ot MU \( j+o1 P00 F €
= 4 (Ot! (isoyto0 ) +

Gis € (ot! CH oi)"00)" r
= (0+! (140100)

PQ. Corre [rory' 00)"

CO- | Compare PDA with NPDA.
3;
BL-3 Construct PDA for L= { a*b*c"d" njm>1}

ve have designed the PDA for the problem:
(a,a/aa)
(a, Z/aZ) (b, a/epsilon) (c, c/cc)

$
| Dy
60) | 110

STACK Transiton Function

6(q®, a, Z) = (q@, aZ)
6(q®, a, a) = (q@, aa)
6(q@, b, a) = (qi, £)
6(q1, b, a) = (qi, €)

6(q1, c, Z) = (q2, cZ)
6(q2, c, c) = (q2, cc)
6(q2, d, c) = (q3, £)
6(q3, d, c) = (q3, €)

6(q1, €, Z) = (qf, Z)

FIC 6 I HF
--- page 7 ---
CO-   Explain simplification rules for grammar. Convert the
2;
following grammar into Chowmsky normal form.
BL-3
S->aSa|bSb|a|b|aa|bb
[10]
Rules -5 Marks
Conversion 2.5 Marks
Q5
CO-   Design a Turing Machine as transducer for 2's complement
3;
BL-5
[10]
CO-   Design a Turing Machine that recognizes binary
3;
palindromes.
BL-3
[10]
Q6
CO-   Explain closure properties of Context Free Language
2;   Properties of Context Free Languages
BL-2 CFLs are closed under the following operations:
1. Union
If L and M are two context-free languages, then their union L ∪ M is also a   [10]
CFL.
Construction:
1. Consider two context-free grammars, G and H, for L and M respectively.
2. Assume that G and H have no common variables (this can be ensured by
renaming variables if needed).
********** 7 **********
--- page 8 ---
3. Introduce a new start symbol S and add the rule: S → S₁ |
S₂ Here, S₁ and S₂ are the start symbols of G and H, respectively.
4. The resulting grammar generates L ∪ M, proving that CFLs are closed
under union.
Example: Let L₁ = { aⁿbⁿcᵐ | m ≥ 0, n ≥ 0 } and L₂ = { aⁿbᵐcᵐ | n ≥ 0, m ≥ 0 }.
• L₁ enforces that the number of a’s equals the number of b’s.
• L₂ enforces that the number of b’s equals the number of c’s.
•   Their union states that either of these conditions must be satisfied,
making the resulting language context-free.
Note: So CFL are closed under Union.
2. Concatenation
If L and M are CFLs, then their concatenation LM is also a CFL.
Construction:
1. Let G and H be the context-free grammars for L and M, respectively.
2. Assume that G and H have no common variables.
3. Introduce a new start symbol S and add the production:S → S₁
S₂Here, S₁ and S₂ are the start symbols of G and H, respectively.
4. This ensures that any derivation from S will first generate a string in L and
then a string in M, proving that CFLs are closed under concatenation.
Example
L1 =   { anbn   | n >= 0   } and L2 =   { cmdm   | m >= 0   }
L3 = L1.L2 = { anbncmdm | m >= 0 and n >= 0} is also context free.
L1 says number of a’s should be equal to number of b’s and L2 says number of
c’s should be equal to number of d’s. Their concatenation says first number of
a’s should be equal to number of b’s, then number of c’s should be equal to
number of d’s. So, we can create a PDA which will first push for a’s, pop for b’s,
push for c’s then pop for d’s. So it can be accepted by pushdown automata,
hence context free.
Note: So CFL are closed under Concatenation.
3. Kleene Closure
If L is a CFL, then its Kleene closure L* (zero or more repetitions of strings
in L) is also a CFL.
Construction:
1. Let G be the context-free grammar for L with start symbol S₁.
2. Introduce a new start symbol S and add the rule:S → S₁ S | εThis rule
ensures that S can derive zero or more copies of S₁, proving closure
under the Kleene star.
Example
L1 = { anbn | n >= 0 }
L1* = { anbn | n >= 0 }* is also context free.
Note :So CFL are closed under Kleen Closure.
4. Intersection and complementation
If L1 and If L2 are two context free languages, their intersection L1 ? L2 need
not be context free.
Example
L1 = { anbncm | n >= 0 and m >= 0 } and L2 = (ambncn | n >= 0 and m >= 0 }
L3 = L1 ? L2 = { anbncn   | n >= 0 } need not be context free.
L1 says number of a’s should be equal to number of b’s and L2 says number of
b’s should be equal to number of c’s. Their intersection says both conditions
need to be true, but push down automata can compare only two. So it cannot
be accepted by pushdown   automata, hence   not   context   free.
Similarly, complementation of context free language L1 which is ?* – L1, need
not be context free.
Note : So CFL are not closed under Intersection and Complementation.
5. Reversal
If L is a CFL, then its reversal L^R (where each string is reversed) is also a
CFL.
Construction:
1. Take the context-free grammar G for L.
2. Modify each production so that the right-hand side of every rule is
reversed.
3. The resulting grammar generates L^R, proving that CFLs are closed
under reversal.
Example:
********** 8 **********
--- page 9 ---
•   Original Grammar: S → 0S1 | 01
• Reversed Grammar: S → 1S0 | 10
CO-   Write short notes: (Any 2)
4;
1. P and NP, NP-completeness
BL-2
In computer science, P and NP are complexity classes, with P
representing problems solvable in polynomial time, and NP
representing problems where solutions can be verified in
polynomial time. NP-completeness identifies the "hardest"
problems in NP, where solving one would lead to polynomial-
time solutions for all NP problems.
2. Church Turing Thesis.
Any computation that can be performed by a human following an
algorithm can also be performed by a Turing machine..In 1930, this
statement was first formulated by Alonzo Church and is usually referred
to as Church’s thesis, or the Church-Turing thesis. However, this
hypothesis cannot be proved. The recursive functions can be
computable after taking following assumptions:
1. Each and every function must be computable.
Q7   2. Let ‘F’ be the computable function and after performing some
elementary operations to ‘F’, it will transform a new function ‘G’ [20]
then this function ‘G’ automatically becomes the computable
function.
3. If any functions that follow above two assumptions must be states
as computable function.
Context Sensitive Language
A Context Sensitive Language is a formal language that can be generated by
a context-sensitive grammar (CSG).
A grammar is context-sensitive if all its production rules are of the form:
α → β, where
•   |β| ≥ |α| (i.e., right-hand side is at least as long as the left-hand
side)
•   Except for the rule S → ε, which is allowed only if ε is part of
the language.
********** 9 **********
````
