# Theoretical Computer Science: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 535286bd2b43

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSBS_7036/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: mixed (10 pages), mean OCR confidence 41.7
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume data wherever needed.
5. Question No. 1 is compulsory. From remaining 6 questions, attempt any 4 questions.
Q1
Answer briefly:   [20]
a.   Short note on Applications of Automata Theory.
Ans:
5M for listing and briefly explaining any 4-5 applications:
Compiler Design: Finite Automata (FA) are used in lexical analysis
(scanning) to recognize tokens (keywords, identifiers).
Text Processing/Search: Regular expressions (which are based on FA)
CO-1;   are used in search algorithms (like GREP) and pattern matching.   [5]
BL-1
Protocol Verification: State machines (Automata) model and verify the
behavior of communication and system protocols.
Natural Language Processing (NLP): Used for syntactic analysis and
morphological processing.
Digital Circuit Design: FA and state machines are used to design and
model sequential logic circuits.
b.   Design DFA to accept a string over {0,1} which starts at and ends with
same symbol.
CO-1;   [5]
BL-2   Ans:
3M for state machine & tuples, 2M for transition diagram
********** 1 **********
--- page 2 ---
c.   Distinguish between Moore M/C & Mealy M/C.
Ans:
Moore Machine   Mealy Machine
Output depends only upon the   Output depends on the present
present state.   state as well as present input.
Moore machine also places its   Mealy Machine places its
output in the state.   output on the transition.
Less number of states are
More states are required.
required.
Moore machines requires more   Mealy Machines requires less
hardware requirement for   hardware requirement for
circuit implementation.   circuit implementation.
CO-1;   [5]
BL-1
They react slower to
They react faster to inputs.
inputs(One clock cycle later).
Synchronous output and state   Asynchronous output
generation.   generation.
Output is placed on
Output is placed on states.
transitions.
Easy to design.   It is difficult to design.
If input changes, output does
If input changes, output also
not change, as moore machine
changes, because in mealy
is a type of finite state machine
machine output depends on the
where the output is determined
present state as well as present
solely by the current state, not
input.
by the current input.
********** 2 **********
--- page 3 ---
Has more or the same states as   Has fewer or the same states as
that of the Mealy machine.   that of the Moore machine.
d.   Explain halting problem in detail.
Ans:
(2M for definition, 3M for significance/proof idea):
Definition: The Halting Problem asks whether it is possible to determine,
for an arbitrary program (Turing Machine M) and an arbitrary input (w),
whether the program will eventually stop (halt) or run forever (loop).
The Core Question: Can we create an algorithm that determines whether
any given program will halt for a specific input?
Answer: No, it is impossible to design a generalized algorithm that can
accurately determine whether any arbitrary program will halt. The only
way to know if a specific program halts is to run it and observe the
outcome. This makes the Halting Problem an undecidable problem.
Write a Halting Problem:
An example of writing the Halting Problem is as follows −
CO-3;   INPUT − Program P and a string S.   [5]
BL-1   OUTPUT − if P stops on S, it returns 1.
Otherwise, if P enters into an endless loop on S, it returns 0.
Let us consider the Halting Problem called H having the solution.
Now H takes the following two inputs −
• Program P
•   Input S
If P stops on S, then H results in "halt", otherwise H gives the result
"loop".
The diagrammatic representation of H is as follows −
a.   A Moore machine is designed to detect the sequence "101". When the
sequence is detected, it outputs 1; otherwise, it outputs 0. The machine
Q2   resets once the sequence is found. Convert the same machine to it’s
CO-2;   equivalent Mealy machine.   [10]
BL-3   Ans:
State Diagram & Transition Table of Moore (4M); Conversion of Moore to
Mealy (3M); Mealy Machine (3M)
********** 3 **********
--- page 4 ---
b.   Design a DFA having even numbers of “a” & odd numbers of “b” over
{a,b}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Minimize given DFA:
Q3
[10]
CO-2,3;
BL-3
Ans:
2M Transition Table; 2M inaccessible state; 2M for Initial Partition, 2M
for Iterative Partitioning, 2M for Final Minimal DFA
********** 4 **********
--- page 5 ---
b.   Construct a Turing machine to check well formedness of ( )
paranthesis.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Simplify the given grammar having production rules, P:
Q4   S → 0X | 1Y | Z; X → 0S | 00; Y → 1 | X | ꞓ; Z → 01 | ꞓ
CO-2,3;   Ans:   [10]
BL- 4   Elimination of ϵ-productions (4M); Elimination of Unit Productions (4M);
Elimination of Useless Symbols (2M);
********** 5 **********
--- page 6 ---
b.   Construct a PDA that accepts the language L={anbman ∣ n≥0; m≥1}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Simplify the given grammar & then convert it to CNF:
Q5   S→AB ∣ AC; A→a | aA; B→b; C→cC ∣ ϵ; D→d
CO-2;   Ans:   [10]
BL-3
Eliminate ϵ-productions (2M); Eliminate Unit Productions (2M); Eliminate
Useless Symbols (1M); Conversion to CNF (5M).
********** 6 **********
--- page 7 ---
b.   Draw a DFA which accepts a string containing “ing” in it over {a:z}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
Q6   a.   Build a Mealy machine to accept a string having “101” in it over {0,1}.
CO-2,3;   Ans:   [10]
BL- 3   State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
********** 7 **********
--- page 8 ---
b.   Explain in detail: Variations of Turing Machine.
Ans:
1. Multitape Turing Machine (3M): Has multiple tapes, each with its
own head. Each move depends on the input symbols under all heads. It is
equivalent in power to the standard TM (can be simulated by a single-
tape TM with polynomial slowdown).
2. Non-deterministic Turing Machine (NDTM) (3M): Allows multiple
possible transitions for the same state/symbol combination. It is also
[10]
equivalent in power to the standard TM (though the simulation might be
exponentially slower). Used to define the complexity class NP.
3. Multi-track Turing Machine (2M): Has a single tape head but the
tape is viewed as having multiple tracks/channels. It is equivalent in
power to the standard TM.
4. Multi-dimensional Turing Machine (2M): The tape is a two-
dimensional grid or higher dimension. It is equivalent in power to the
standard TM.
a.   Compare & contrast PDA and DFA.
Ans:
Q7   For Comparison and Contrast (5 points for each):
CO- 2,3;   [10]
Deterministic Finite   Pushdown Automaton
BL- 3   Feature
Automaton (DFA)   (PDA)
No additional memory   Has a stack as additional
Memory
beyond finite states   memory
********** 8 **********
--- page 9 ---
Finite number of states plus an
States   Finite number of states
infinite stack
Reads input symbols
Input   Reads input symbols and
and changes states
Processing   manipulates stack (push/pop)
deterministically
Language   Recognizes regular   Recognizes context-free
Recognized languages   languages
Defined by current state Defined by current state, input
Transitions
and input symbol only   symbol, and stack top symbol
Can be deterministic or
Fully deterministic:
Determinis   nondeterministic (usually
exactly one transition
m   nondeterministic for full
per input and state
power)
Uses stack for storing
Stack Usage No stack   symbols, enabling memory
beyond states
Simpler computational   More powerful computational
Complexity
model   model
Parsing of programming
Application Lexical analysis, pattern
languages, especially those
s   matching
with nested structures
Acceptance Final state reached after   Final state or empty stack
criteria   processing input   after processing input
b.   Convert the regular expression ab(ab+ba)*b into an NFA. Convert the
NFA into an equivalent DFA.
[10]
Ans:
5M for RE to NFA, 5M for NFA to DFA
********** 9 **********
--- page 10 ---
RR KR RK ARK KK 10 KAKA KKK
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper fb62bf132184

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSBS_7036/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026_fb62bf1321.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: mixed (10 pages), mean OCR confidence 53.2
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume data wherever needed.
5. Question No. 1 is compulsory. From remaining 6 questions, attempt any 4 questions.
Q1
Answer briefly:   [20]
a.   Short note on Applications of Automata Theory.
Ans:
5M for listing and briefly explaining any 4-5 applications:
Compiler Design: Finite Automata (FA) are used in lexical analysis
(scanning) to recognize tokens (keywords, identifiers).
Text Processing/Search: Regular expressions (which are based on FA)
CO-1;   are used in search algorithms (like GREP) and pattern matching.   [5]
BL-1
Protocol Verification: State machines (Automata) model and verify the
behavior of communication and system protocols.
Natural Language Processing (NLP): Used for syntactic analysis and
morphological processing.
Digital Circuit Design: FA and state machines are used to design and
model sequential logic circuits.
b.   Design DFA to accept a string over {0,1} which starts at and ends with
same symbol.
CO-1;   [5]
BL-2   Ans:
3M for state machine & tuples, 2M for transition diagram
********** 1 **********
--- page 2 ---
c.   Distinguish between Moore M/C & Mealy M/C.
Ans:
Moore Machine   Mealy Machine
Output depends only upon the   Output depends on the present
present state.   state as well as present input.
Moore machine also places its   Mealy Machine places its
output in the state.   output on the transition.
Less number of states are
More states are required.
required.
Moore machines requires more   Mealy Machines requires less
hardware requirement for   hardware requirement for
circuit implementation.   circuit implementation.
CO-1;   [5]
BL-1
They react slower to
They react faster to inputs.
inputs(One clock cycle later).
Synchronous output and state   Asynchronous output
generation.   generation.
Output is placed on
Output is placed on states.
transitions.
Easy to design.   It is difficult to design.
If input changes, output does
If input changes, output also
not change, as moore machine
changes, because in mealy
is a type of finite state machine
machine output depends on the
where the output is determined
present state as well as present
solely by the current state, not
input.
by the current input.
********** 2 **********
--- page 3 ---
Has more or the same states as   Has fewer or the same states as
that of the Mealy machine.   that of the Moore machine.
d.   Explain halting problem in detail.
Ans:
(2M for definition, 3M for significance/proof idea):
Definition: The Halting Problem asks whether it is possible to determine,
for an arbitrary program (Turing Machine M) and an arbitrary input (w),
whether the program will eventually stop (halt) or run forever (loop).
The Core Question: Can we create an algorithm that determines whether
any given program will halt for a specific input?
Answer: No, it is impossible to design a generalized algorithm that can
accurately determine whether any arbitrary program will halt. The only
way to know if a specific program halts is to run it and observe the
outcome. This makes the Halting Problem an undecidable problem.
Write a Halting Problem:
An example of writing the Halting Problem is as follows −
CO-3;   INPUT − Program P and a string S.   [5]
BL-1   OUTPUT − if P stops on S, it returns 1.
Otherwise, if P enters into an endless loop on S, it returns 0.
Let us consider the Halting Problem called H having the solution.
Now H takes the following two inputs −
• Program P
•   Input S
If P stops on S, then H results in "halt", otherwise H gives the result
"loop".
The diagrammatic representation of H is as follows −
a.   A Moore machine is designed to detect the sequence "101". When the
sequence is detected, it outputs 1; otherwise, it outputs 0. The machine
Q2   resets once the sequence is found. Convert the same machine to it’s
CO-2;   equivalent Mealy machine.   [10]
BL-3   Ans:
State Diagram & Transition Table of Moore (4M); Conversion of Moore to
Mealy (3M); Mealy Machine (3M)
********** 3 **********
--- page 4 ---
b.   Design a DFA having even numbers of “a” & odd numbers of “b” over
{a,b}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Minimize given DFA:
Q3
[10]
CO-2,3;
BL-3
Ans:
2M Transition Table; 2M inaccessible state; 2M for Initial Partition, 2M
for Iterative Partitioning, 2M for Final Minimal DFA
********** 4 **********
--- page 5 ---
b.   Construct a Turing machine to check well formedness of ( )
paranthesis.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Simplify the given grammar having production rules, P:
Q4   S → 0X | 1Y | Z; X → 0S | 00; Y → 1 | X | ꞓ; Z → 01 | ꞓ
CO-2,3;   Ans:   [10]
BL- 4   Elimination of ϵ-productions (4M); Elimination of Unit Productions (4M);
Elimination of Useless Symbols (2M);
********** 5 **********
--- page 6 ---
b.   Construct a PDA that accepts the language L={anbman ∣ n≥0; m≥1}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
a.   Simplify the given grammar & then convert it to CNF:
Q5   S→AB ∣ AC; A→a | aA; B→b; C→cC ∣ ϵ; D→d
CO-2;   Ans:   [10]
BL-3   Eliminate ϵ-productions (2M); Eliminate Unit Productions (2M); Eliminate
Useless Symbols (1M); Conversion to CNF (5M).
********** 6 **********
--- page 7 ---
b.   Draw a DFA which accepts a string containing “ing” in it over {a:z}.
Ans:
State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
[10]
Q6   a.   Build a Mealy machine to accept a string having “101” in it over {0,1}.
CO-2,3;   Ans:   [10]
BL- 3   State Diagram & Tuples (4M); Transition Table (3M); Examples (3M)
********** 7 **********
--- page 8 ---
b.   Explain in detail: Variations of Turing Machine.
Ans:
1. Multitape Turing Machine (3M): Has multiple tapes, each with its
own head. Each move depends on the input symbols under all heads. It is
equivalent in power to the standard TM (can be simulated by a single-
tape TM with polynomial slowdown).
2. Non-deterministic Turing Machine (NDTM) (3M): Allows multiple
possible transitions for the same state/symbol combination. It is also
[10]
equivalent in power to the standard TM (though the simulation might be
exponentially slower). Used to define the complexity class NP.
3. Multi-track Turing Machine (2M): Has a single tape head but the
tape is viewed as having multiple tracks/channels. It is equivalent in
power to the standard TM.
4. Multi-dimensional Turing Machine (2M): The tape is a two-
dimensional grid or higher dimension. It is equivalent in power to the
standard TM.
a.   Compare & contrast PDA and DFA.
Ans:
Q7   For Comparison and Contrast (5 points for each):
CO- 2,3;   [10]
Deterministic Finite   Pushdown Automaton
BL- 3   Feature
Automaton (DFA)   (PDA)
No additional memory Has a stack as additional
Memory
beyond finite states   memory
********** 8 **********
--- page 9 ---
Finite number of states plus an
States   Finite number of states
infinite stack
Reads input symbols
Input   Reads input symbols and
and changes states
Processing   manipulates stack (push/pop)
deterministically
Language   Recognizes regular   Recognizes context-free
Recognized languages   languages
Defined by current state Defined by current state, input
Transitions
and input symbol only   symbol, and stack top symbol
Can be deterministic or
Fully deterministic:
Determinis   nondeterministic (usually
exactly one transition
m   nondeterministic for full
per input and state
power)
Uses stack for storing
Stack Usage No stack   symbols, enabling memory
beyond states
Simpler computational More powerful computational
Complexity
model   model
Parsing of programming
Application Lexical analysis, pattern
languages, especially those
s   matching
with nested structures
Acceptance Final state reached after Final state or empty stack
criteria   processing input   after processing input
b.   Convert the regular expression ab(ab+ba)*b into an NFA. Convert the
NFA into an equivalent DFA.
[10]
Ans:
5M for RE to NFA, 5M for NFA to DFA
********** 9 **********
--- page 10 ---
RK KKK RK KK 10 2h KKK RK Kk KK
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ab0d8e9a6840

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CS_7055/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   The applications of automata theory in compiler design:   [5]
BL-2
SO-2   Lexical Analysis: Uses Finite Automata to recognize tokens.
Syntax Analysis: Uses Context-Free Grammars for parsing.
Parser Design: PDA-based parsing techniques (LL, LR).
Pattern Matching: Regular expressions for token identification.
Code Optimization & Translation: Formal models help in structured
translation.
1 Mark for each Application - Explanation expected in brief
CO-2   b   Transition function DFA : δ:Q×Σ→Q (exactly one state)   [5]
BL-2   Transition function NFA : δ:Q×ΣU{ ℇ }→2Q (the transition function gives
SO-2   a set of possible next states.)
For every:
•   current state 𝑞∈𝑄
•   input symbol 𝑎∈Σ
Tuples of the machine to be mentioned
********** 1 **********
--- page 2 ---
Transition function difference – 2 marks
Design of a DFA – 2 Marks
Tuple specification – 1 mark
CO-3   c   [5]
BL-2,3   LMD (2.5 M)   Parse Tree (2.5 M)
SO-2
S   ⇒bSaS (Using S→ bSaS)
⇒bεaS (Using S→ ε )
⇒baS
⇒baaSbS (Using S→ aSbS)
⇒baabS (Using S→ ε )
⇒baabaSbS (Using S→ aSbS)
⇒baababS (Using S→ ε )
⇒baabab (Using S→ ε )
LMD – 2.5 marks
Parse Tree – 2.5 Marks
CO-1   d   [5]
BL-2   Church-Turing Hypothesis
SO-2   -   This is also known as Church-Turing Conjecture, Church Thesis or
Church’s Conjecture
-   It is essentially states that everything that is algorithmically
computable is computable by a TM.
-   American mathematician, Alonzo Church, created a method called
Lambda Calculus for defining functions.
-   It is an equivalent computational model of the UTM.
-   Hypothesis: - The intuitive notion of a computable function can be
identified with the class of partial recursive functions. In other
words, every problem having an algorithmic solution can be solved
using a machine having the foregoing set of instructions.
Explanation – 5 Marks
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Tuples Q={q0, q1, q2, q3, q4}
∑ ={0,1}
Δ ={N, Y}
δ : δ
𝜆→ Q X ∑ → Δ
Tuples to be specified
Design of the Moore Machine – 4 Marks, Tuples- 1 Mark
********** 2 **********
--- page 3 ---
CO-3   b   No, it is not always possible to determine whether a given program will   [10]
BL-3   halt for a specific input.
SO-2   This is explained by the Halting Problem, a fundamental concept in
computability theory.
Halting Problem:
The halting problem was proposed by Alan Turing in 1936. The halting
problem is a fundamental issue in theoretical and computational complexity.
The halting problem is the problem of determining whether a computer
program will halt or run forever.
Input − A Turing machine and an input string w.
Problem − Does the Turing machine finish computing of the string w in a
finite number of steps? The answer must be either yes or no.
Proof − At first, we will assume that such a Turing machine exists to solve
this problem and then we will show it is contradicting itself. We will call
this Turing machine as a Halting machine that produces a ‘yes’ or ‘no’ in a
finite amount of time. If the halting machine finishes in a finite amount of
time, the output comes as ‘yes’, otherwise as ‘no’. The following is the
block diagram of a Halting machine −
Now we will design an inverted halting machine (HM)’ as –
-   If H returns YES, then loop forever.
-   If H returns NO, then halt.
The following is the block diagram of an ‘Inverted halting machine’ −
Further, a machine (HM)2 which input itself is constructed as follows −
-   If (HM)2 halts on input, loop forever.
-   Else, halt.
Here, we have got a contradiction. Hence, the halting problem is
undecidable.
Design of the Turing Machine:
********** 3 **********
--- page 4 ---
Correct answer of “NO” – 1 Mark
Proper justification with Halting Problem explained –4 marks
Tuple Machine Design– 5 Marks (If logic explained- 2 Marks, if
designed fully 5 marks)
CO-3   c   An 𝜖-NFA is a Non-deterministic Finite Automaton with epsilon   [5]
BL-3   transitions.
SO-2   It is an NFA in which the machine can change from one state to another
without reading any input symbol. Such transitions are called 𝜖-transitions.
An 𝜖-NFA is defined as:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
where the transition function is:
𝛿: 𝑄× (Σ ∪{𝜖}) →2𝑄
This means the transition function may take:
•   an input symbol from Σ, or
•   𝜖
Design of an NFA:
𝜖-NFA – 2 marks
Design of an NFA – 3 Marks
Q-3
CO-2   a   Final Minimized DFA:   [10]
BL-3
SO-2
********** 4 **********
--- page 5 ---
Step Marking to be done – 10 Marks
CO-3   b   If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is also a   [10]
BL-3,4   CFL
SO-2   Let us take a CFL:
𝐿1 = {𝑎𝑛𝑏𝑛∣𝑛≥0}
This is a Context-Free Language.
L1∗=(anbn)∗   i.e Zero or more repetitions of strings from 𝐿1
Original grammar for 𝐿1: S1→aS1b∣ϵ
Grammar for 𝐿1 ∗
S→SS1∣ϵ
S1→aS1b∣ϵ
This is also a Context-Free Language
Hence If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is
also a CFL
No, A single stack Pushdown Automaton (PDA):
• Has only one stack
• Can handle one level of counting/dependency
In 𝑎𝑛𝑏𝑛𝑐𝑛, we need to ensure:
• Number of a = number of b
• Number of b = number of c
That means:
• Two independent comparisons:
o 𝑎↔𝑏
o 𝑏↔𝑐
Therefore, this language cannot be accepted by a single stack PDA.
Closure property of CFL with Example– 5 marks
Explanation about the language – 5 marks
Q-4
CO-2   a   Arden’s Theorem simplifies regular expressions by providing a systematic   [10]
BL-3   approach to solving equations of the form X = AX + B. By applying the
SO-2   theorem, complex regular expressions can be rewritten in a more concise
form using concatenation and the Kleene closure operation, resulting in
simplified expressions.
Arden’s theorem Solution for generating regular expression –
********** 5 **********
--- page 6 ---
How can Arden’s Theorem simplify regular expressions – 2 Marks
Construction of RE - 8 Marks (equation generation – 2 Marks,
q2 substitution – 2 Marks, q1 substitution -3 Marks,
final answer – 1 Mark)
CO-3   b   [10]
BL-3,4
SO-2
********** 6 **********
--- page 7 ---
Logic Explained – 3 Marks
TM Design – 5 Marks
String Tracing – 2 Marks
Q-5
CO-3   a   A Context-Free Grammar (CFG) is said to be ambiguous if:   [10]
BL-3   There exists at least one string in the language generated by the grammar
SO-2   that has more than one distinct parse tree (or equivalently, more than one
leftmost or rightmost derivation).
What makes a grammar ambiguous – 2 Marks
Identifying String for proving Ambiguity – 2 Marks
Atleast 2 derivations – 3 marks each (6 marks)
********** 7 **********
--- page 8 ---
CO-3   b   [10]
BL-3,4
SO-2
c) Moore Machine – If input sequence is of length n, then output
sequence if of length n+1
Mealy Machine – If input sequence is of length n, then output sequence if
of length n
a) 3 Marks
b) 5 Marks
c) 2 Marks
Q-6
CO-2   a   [10]
BL-3,4   Step 1: Remove Unit Productions   (3 Marks)
SO-2   Unit production:
• S → C
• B → A
Replace S → C using C → 01:
• S → 0A | 1B | 01
Replace B → A using A → 0S | 000:
• B → 11 | 0S | 000
Updated Grammar:
• S → 0A | 1B | 01
• A → 0S | 000
• B → 11 | 0S | 000
• C → 01
Step 2: Replace Terminals in Mixed Productions   (3 Marks)
Introduce new variables:
• X → 0
• Y → 1
********** 8 **********
--- page 9 ---
Replace terminals:
• 0A → XA
• 1B → YB
• 0S → XS
• 01 → XY
• 11 → YY
• 000 → XXX
Updated Grammar:
• S → XA | YB | XY
• A → XS | XXX
• B → YY | XS | XXX
• C → XY
• X → 0
• Y → 1
Step 3: Convert Long Productions (>2 symbols)   (3 Marks)
Break 3-length productions:
For XXX:
Introduce new variable:
• D → XX
So:
• XXX → XD
Updated Grammar:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Step 4: Final CNF Grammar   (1Mark)
Productions:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Stepwise marking – Total 10 marks
CO-2   b   Design logic -   [5]
BL-3   Read a’s
SO-2   → Push one symbol (X) for each a
Read b’s (first n b’s)
→ Pop one X for each b
After stack becomes empty (only 𝑍0remains)
→ Read exactly 2 extra b’s
Accept if input ends after those 2 extra b’s
Design of the PDA-
M=(Q,Σ,Γ,δ,q0,Z0,F)
𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
Σ = {𝑎, 𝑏}
********** 9 **********
--- page 10 ---
Γ = {𝑋, 𝑍0}
Start state: 𝑞0
Initial stack symbol: 𝑍0
Final state: 𝐹= {𝑞𝑓}
Transition functions
δ(𝑞0,a,Z0)=(q0,XZ0)
δ(q0,a,X)=(q0,XX)
δ(q0,b,X)=(q1,ϵ)
δ(q1,b,X)=(q1,ϵ)
δ(q1,b, Z0)=(q2, Z0)
δ(q2,b, Z0)=(q3, Z0)
δ(q3,ϵ, Z0)=(qf, Z0)
Logic Design – 2 Marks
PDA Design and tuples– 3 Marks
CO-1   c   [5]
BL-2
SO-2
Production rules – 1 Mark
Language recognized - 1 Mark
Machine – 1 Mark
Closed under properties -2 Marks
Q-7
CO-2,3   a   1   [10]
BL-3   NFA (2 Marks)
SO-2   State   a   b
A (initial)   {A, B} A
B   C   C
C (Final)   -   -
2 DFA (3 Marks)
State   a   b
{A} (initial)   {A,B} {A}
{A,B}   {A,B,C} {A,C}
{A,B,C} (Final) {A,B,C} {A,C}
{A,C}(Final)   {A,B} {A}
3 Minimization [3 Marks]
********** 10 **********
--- page 11 ---
Step 1 Reachability Check: All states are reachable. No state will be
eliminated.
Step 2 Equivalence test
a) 0-equivalent: {{A},{A,B}} {{A,B,C},{A,C}}
b) 1-equivalent: {A}{A,B}{A,B,C}{A,C}
c) 2-equivalent: {A}{A,B}{A,B,C}{A,C}
All states are distinguishable. DFA is already minimized
4 Regular Expression [2 Marks]
(a+b)* a (a+b)
1.NFA -2 Marks
2.DFA-3 Marks
3.Minimized DFA 3 Marks
4.Regular Expression-2 Marks
CO-1   b   a)Non-terminals: {S}, Terminals: {a, b}   [5]
BL-2   b) Example strings: ε, ab, aabb, abab
SO-2   c) L(G) = { w ∈ {a, b}* | number of a’s = number of b’s }
d) The grammar is Context-Free (Type 2) as productions are of the
for V->(VUT)* and generates a Context-Free Language.
a) 2 Marks
b) 1 Mark
c) 1 Mark
d) 1 Mark
CO-3   c   Logic: The language requires at least one ‘a’ anywhere in the string.   [5]
BL-3   We only need to check presence, not count or match.
SO-2   So:
•   Stay in initial state while reading 𝑏's
• Move to accepting state when first 𝑎is seen
•   After that, accept any combination of 𝑎and 𝑏
Let the PDA be, M=(Q,Σ,Γ,δ,q0,Z0,F)
Components
• 𝑄= {𝑞0, 𝑞1}
• Σ = {𝑎, 𝑏}
• Γ = {𝑍0}(stack symbol, but unused)
•   Start state: 𝑞0
•   Initial stack symbol: 𝑍0
•   Final states: 𝐹= {𝑞1}
•   𝛿:
δ(𝑞0,b, 𝑍0) ={(𝑞0,𝑍0)}
𝛿(𝑞0, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑏, 𝑍0) = {(𝑞1,𝑍0)}
As The language only requires checking:
presence of at least a single “a”, This can be done using a Finite
Automaton (FA) since:
********** 11 **********
--- page 12 ---
• No counting or memory of arbitrary size is required
Hence, Stack implementation through PDA is not required.
PDA Design – 2 Marks
determine whether the use of a stack is necessary for
PDA this design language, : 3 Marks giving reason. – 3 Marks
Tuples writing : 1 Mark
Justification : 1 Mark
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper e3cd190a3013

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Computer_7002/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   The applications of automata theory in compiler design:   [5]
BL-2
SO-2   Lexical Analysis: Uses Finite Automata to recognize tokens.
Syntax Analysis: Uses Context-Free Grammars for parsing.
Parser Design: PDA-based parsing techniques (LL, LR).
Pattern Matching: Regular expressions for token identification.
Code Optimization & Translation: Formal models help in structured
translation.
1 Mark for each Application - Explanation expected in brief
CO-2   b   Transition function DFA : δ:Q×Σ→Q (exactly one state)   [5]
BL-2   Transition function NFA : δ:Q×ΣU{ ℇ }→2Q (the transition function gives
SO-2   a set of possible next states.)
For every:
•   current state 𝑞∈𝑄
•   input symbol 𝑎∈Σ
Tuples of the machine to be mentioned
********** 1 **********
--- page 2 ---
Transition function difference – 2 marks
Design of a DFA – 2 Marks
Tuple specification – 1 mark
CO-3   c   [5]
BL-2,3   LMD (2.5 M)   Parse Tree (2.5 M)
SO-2
S   ⇒bSaS (Using S→ bSaS)
⇒bεaS (Using S→ ε )
⇒baS
⇒baaSbS (Using S→ aSbS)
⇒baabS (Using S→ ε )
⇒baabaSbS (Using S→ aSbS)
⇒baababS (Using S→ ε )
⇒baabab (Using S→ ε )
LMD – 2.5 marks
Parse Tree – 2.5 Marks
CO-1   d   [5]
BL-2   Church-Turing Hypothesis
SO-2   -   This is also known as Church-Turing Conjecture, Church Thesis or
Church’s Conjecture
-   It is essentially states that everything that is algorithmically
computable is computable by a TM.
-   American mathematician, Alonzo Church, created a method called
Lambda Calculus for defining functions.
-   It is an equivalent computational model of the UTM.
-   Hypothesis: - The intuitive notion of a computable function can be
identified with the class of partial recursive functions. In other
words, every problem having an algorithmic solution can be solved
using a machine having the foregoing set of instructions.
Explanation – 5 Marks
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Tuples Q={q0, q1, q2, q3, q4}
∑ ={0,1}
Δ ={N, Y}
δ : δ
𝜆→ Q X ∑ → Δ
Tuples to be specified
Design of the Moore Machine – 4 Marks, Tuples- 1 Mark
********** 2 **********
--- page 3 ---
CO-3   b   No, it is not always possible to determine whether a given program will   [10]
BL-3   halt for a specific input.
SO-2   This is explained by the Halting Problem, a fundamental concept in
computability theory.
Halting Problem:
The halting problem was proposed by Alan Turing in 1936. The halting
problem is a fundamental issue in theoretical and computational complexity.
The halting problem is the problem of determining whether a computer
program will halt or run forever.
Input − A Turing machine and an input string w.
Problem − Does the Turing machine finish computing of the string w in a
finite number of steps? The answer must be either yes or no.
Proof − At first, we will assume that such a Turing machine exists to solve
this problem and then we will show it is contradicting itself. We will call
this Turing machine as a Halting machine that produces a ‘yes’ or ‘no’ in a
finite amount of time. If the halting machine finishes in a finite amount of
time, the output comes as ‘yes’, otherwise as ‘no’. The following is the
block diagram of a Halting machine −
Now we will design an inverted halting machine (HM)’ as –
-   If H returns YES, then loop forever.
-   If H returns NO, then halt.
The following is the block diagram of an ‘Inverted halting machine’ −
Further, a machine (HM)2 which input itself is constructed as follows −
-   If (HM)2 halts on input, loop forever.
-   Else, halt.
Here, we have got a contradiction. Hence, the halting problem is
undecidable.
Design of the Turing Machine:
********** 3 **********
--- page 4 ---
Correct answer of “NO” – 1 Mark
Proper justification with Halting Problem explained –4 marks
Tuple Machine Design– 5 Marks (If logic explained- 2 Marks, if
designed fully 5 marks)
CO-3   c   An 𝜖-NFA is a Non-deterministic Finite Automaton with epsilon   [5]
BL-3   transitions.
SO-2   It is an NFA in which the machine can change from one state to another
without reading any input symbol. Such transitions are called 𝜖-transitions.
An 𝜖-NFA is defined as:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
where the transition function is:
𝛿: 𝑄× (Σ ∪{𝜖}) →2𝑄
This means the transition function may take:
•   an input symbol from Σ, or
•   𝜖
Design of an NFA:
𝜖-NFA – 2 marks
Design of an NFA – 3 Marks
Q-3
CO-2   a   Final Minimized DFA:   [10]
BL-3
SO-2
********** 4 **********
--- page 5 ---
Step Marking to be done – 10 Marks
CO-3   b   If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is also a   [10]
BL-3,4   CFL
SO-2   Let us take a CFL:
𝐿1 = {𝑎𝑛𝑏𝑛∣𝑛≥0}
This is a Context-Free Language.
L1∗=(anbn)∗   i.e Zero or more repetitions of strings from 𝐿1
Original grammar for 𝐿1: S1→aS1b∣ϵ
Grammar for 𝐿1 ∗
S→SS1∣ϵ
S1→aS1b∣ϵ
This is also a Context-Free Language
Hence If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is
also a CFL
No, A single stack Pushdown Automaton (PDA):
• Has only one stack
• Can handle one level of counting/dependency
In 𝑎𝑛𝑏𝑛𝑐𝑛, we need to ensure:
• Number of a = number of b
• Number of b = number of c
That means:
• Two independent comparisons:
o 𝑎↔𝑏
o 𝑏↔𝑐
Therefore, this language cannot be accepted by a single stack PDA.
Closure property of CFL with Example– 5 marks
Explanation about the language – 5 marks
Q-4
CO-2   a   Arden’s Theorem simplifies regular expressions by providing a systematic   [10]
BL-3   approach to solving equations of the form X = AX + B. By applying the
SO-2   theorem, complex regular expressions can be rewritten in a more concise
form using concatenation and the Kleene closure operation, resulting in
simplified expressions.
Arden’s theorem Solution for generating regular expression –
********** 5 **********
--- page 6 ---
How can Arden’s Theorem simplify regular expressions – 2 Marks
Construction of RE - 8 Marks (equation generation – 2 Marks,
q2 substitution – 2 Marks, q1 substitution -3 Marks,
final answer – 1 Mark)
CO-3   b   [10]
BL-3,4
SO-2
********** 6 **********
--- page 7 ---
Logic Explained – 3 Marks
TM Design – 5 Marks
String Tracing – 2 Marks
Q-5
CO-3   a   A Context-Free Grammar (CFG) is said to be ambiguous if:   [10]
BL-3   There exists at least one string in the language generated by the grammar
SO-2   that has more than one distinct parse tree (or equivalently, more than one
leftmost or rightmost derivation).
What makes a grammar ambiguous – 2 Marks
Identifying String for proving Ambiguity – 2 Marks
Atleast 2 derivations – 3 marks each (6 marks)
********** 7 **********
--- page 8 ---
CO-3   b   [10]
BL-3,4
SO-2
c) Moore Machine – If input sequence is of length n, then output
sequence if of length n+1
Mealy Machine – If input sequence is of length n, then output sequence if
of length n
a) 3 Marks
b) 5 Marks
c) 2 Marks
Q-6
CO-2   a   [10]
BL-3,4   Step 1: Remove Unit Productions   (3 Marks)
SO-2   Unit production:
• S → C
• B → A
Replace S → C using C → 01:
• S → 0A | 1B | 01
Replace B → A using A → 0S | 000:
• B → 11 | 0S | 000
Updated Grammar:
• S → 0A | 1B | 01
• A → 0S | 000
• B → 11 | 0S | 000
• C → 01
Step 2: Replace Terminals in Mixed Productions   (3 Marks)
Introduce new variables:
• X → 0
• Y → 1
********** 8 **********
--- page 9 ---
Replace terminals:
• 0A → XA
• 1B → YB
• 0S → XS
• 01 → XY
• 11 → YY
• 000 → XXX
Updated Grammar:
• S → XA | YB | XY
• A → XS | XXX
• B → YY | XS | XXX
• C → XY
• X → 0
• Y → 1
Step 3: Convert Long Productions (>2 symbols)   (3 Marks)
Break 3-length productions:
For XXX:
Introduce new variable:
• D → XX
So:
• XXX → XD
Updated Grammar:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Step 4: Final CNF Grammar   (1Mark)
Productions:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Stepwise marking – Total 10 marks
CO-2   b   Design logic -   [5]
BL-3   Read a’s
SO-2   → Push one symbol (X) for each a
Read b’s (first n b’s)
→ Pop one X for each b
After stack becomes empty (only 𝑍0remains)
→ Read exactly 2 extra b’s
Accept if input ends after those 2 extra b’s
Design of the PDA-
M=(Q,Σ,Γ,δ,q0,Z0,F)
𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
Σ = {𝑎, 𝑏}
********** 9 **********
--- page 10 ---
Γ = {𝑋, 𝑍0}
Start state: 𝑞0
Initial stack symbol: 𝑍0
Final state: 𝐹= {𝑞𝑓}
Transition functions
δ(𝑞0,a,Z0)=(q0,XZ0)
δ(q0,a,X)=(q0,XX)
δ(q0,b,X)=(q1,ϵ)
δ(q1,b,X)=(q1,ϵ)
δ(q1,b, Z0)=(q2, Z0)
δ(q2,b, Z0)=(q3, Z0)
δ(q3,ϵ, Z0)=(qf, Z0)
Logic Design – 2 Marks
PDA Design and tuples– 3 Marks
CO-1   c   [5]
BL-2
SO-2
Production rules – 1 Mark
Language recognized - 1 Mark
Machine – 1 Mark
Closed under properties -2 Marks
Q-7
CO-2,3   a   1   [10]
BL-3   NFA (2 Marks)
SO-2   State   a   b
A (initial)   {A, B} A
B   C   C
C (Final)   -   -
2 DFA (3 Marks)
State   a   b
{A} (initial)   {A,B} {A}
{A,B}   {A,B,C} {A,C}
{A,B,C} (Final) {A,B,C} {A,C}
{A,C}(Final)   {A,B} {A}
3 Minimization [3 Marks]
********** 10 **********
--- page 11 ---
Step 1 Reachability Check: All states are reachable. No state will be
eliminated.
Step 2 Equivalence test
a) 0-equivalent: {{A},{A,B}} {{A,B,C},{A,C}}
b) 1-equivalent: {A}{A,B}{A,B,C}{A,C}
c) 2-equivalent: {A}{A,B}{A,B,C}{A,C}
All states are distinguishable. DFA is already minimized
4 Regular Expression [2 Marks]
(a+b)* a (a+b)
1.NFA -2 Marks
2.DFA-3 Marks
3.Minimized DFA 3 Marks
4.Regular Expression-2 Marks
CO-1   b   a)Non-terminals: {S}, Terminals: {a, b}   [5]
BL-2   b) Example strings: ε, ab, aabb, abab
SO-2   c) L(G) = { w ∈ {a, b}* | number of a’s = number of b’s }
d) The grammar is Context-Free (Type 2) as productions are of the
for V->(VUT)* and generates a Context-Free Language.
a) 2 Marks
b) 1 Mark
c) 1 Mark
d) 1 Mark
CO-3   c   Logic: The language requires at least one ‘a’ anywhere in the string.   [5]
BL-3   We only need to check presence, not count or match.
SO-2   So:
•   Stay in initial state while reading 𝑏's
• Move to accepting state when first 𝑎is seen
•   After that, accept any combination of 𝑎and 𝑏
Let the PDA be, M=(Q,Σ,Γ,δ,q0,Z0,F)
Components
• 𝑄= {𝑞0, 𝑞1}
• Σ = {𝑎, 𝑏}
• Γ = {𝑍0}(stack symbol, but unused)
•   Start state: 𝑞0
•   Initial stack symbol: 𝑍0
•   Final states: 𝐹= {𝑞1}
•   𝛿:
δ(𝑞0,b, 𝑍0) ={(𝑞0,𝑍0)}
𝛿(𝑞0, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑏, 𝑍0) = {(𝑞1,𝑍0)}
As The language only requires checking:
presence of at least a single “a”, This can be done using a Finite
Automaton (FA) since:
********** 11 **********
--- page 12 ---
• No counting or memory of arbitrary size is required
Hence, Stack implementation through PDA is not required.
PDA Design – 2 Marks
determine whether the use of a stack is necessary for
PDA this design language, : 3 Marks giving reason. – 3 Marks
Tuples writing : 1 Mark
Justification : 1 Mark
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c6eef828d5b4

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_Computer_7047/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   The applications of automata theory in compiler design:   [5]
BL-2
SO-2   Lexical Analysis: Uses Finite Automata to recognize tokens.
Syntax Analysis: Uses Context-Free Grammars for parsing.
Parser Design: PDA-based parsing techniques (LL, LR).
Pattern Matching: Regular expressions for token identification.
Code Optimization & Translation: Formal models help in structured
translation.
1 Mark for each Application - Explanation expected in brief
CO-2   b   Transition function DFA : δ:Q×Σ→Q (exactly one state)   [5]
BL-2   Transition function NFA : δ:Q×ΣU{ ℇ }→2Q (the transition function gives
SO-2   a set of possible next states.)
For every:
•   current state 𝑞∈𝑄
•   input symbol 𝑎∈Σ
Tuples of the machine to be mentioned
********** 1 **********
--- page 2 ---
Transition function difference – 2 marks
Design of a DFA – 2 Marks
Tuple specification – 1 mark
CO-3   c   [5]
BL-2,3   LMD (2.5 M)   Parse Tree (2.5 M)
SO-2
S   ⇒bSaS (Using S→ bSaS)
⇒bεaS (Using S→ ε )
⇒baS
⇒baaSbS (Using S→ aSbS)
⇒baabS (Using S→ ε )
⇒baabaSbS (Using S→ aSbS)
⇒baababS (Using S→ ε )
⇒baabab (Using S→ ε )
LMD – 2.5 marks
Parse Tree – 2.5 Marks
CO-1   d   [5]
BL-2   Church-Turing Hypothesis
SO-2   -   This is also known as Church-Turing Conjecture, Church Thesis or
Church’s Conjecture
-   It is essentially states that everything that is algorithmically
computable is computable by a TM.
-   American mathematician, Alonzo Church, created a method called
Lambda Calculus for defining functions.
-   It is an equivalent computational model of the UTM.
-   Hypothesis: - The intuitive notion of a computable function can be
identified with the class of partial recursive functions. In other
words, every problem having an algorithmic solution can be solved
using a machine having the foregoing set of instructions.
Explanation – 5 Marks
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Tuples Q={q0, q1, q2, q3, q4}
∑ ={0,1}
Δ ={N, Y}
δ : δ
𝜆→ Q X ∑ → Δ
Tuples to be specified
Design of the Moore Machine – 4 Marks, Tuples- 1 Mark
********** 2 **********
--- page 3 ---
CO-3   b   No, it is not always possible to determine whether a given program will   [10]
BL-3   halt for a specific input.
SO-2   This is explained by the Halting Problem, a fundamental concept in
computability theory.
Halting Problem:
The halting problem was proposed by Alan Turing in 1936. The halting
problem is a fundamental issue in theoretical and computational complexity.
The halting problem is the problem of determining whether a computer
program will halt or run forever.
Input − A Turing machine and an input string w.
Problem − Does the Turing machine finish computing of the string w in a
finite number of steps? The answer must be either yes or no.
Proof − At first, we will assume that such a Turing machine exists to solve
this problem and then we will show it is contradicting itself. We will call
this Turing machine as a Halting machine that produces a ‘yes’ or ‘no’ in a
finite amount of time. If the halting machine finishes in a finite amount of
time, the output comes as ‘yes’, otherwise as ‘no’. The following is the
block diagram of a Halting machine −
Now we will design an inverted halting machine (HM)’ as –
-   If H returns YES, then loop forever.
-   If H returns NO, then halt.
The following is the block diagram of an ‘Inverted halting machine’ −
Further, a machine (HM)2 which input itself is constructed as follows −
-   If (HM)2 halts on input, loop forever.
-   Else, halt.
Here, we have got a contradiction. Hence, the halting problem is
undecidable.
Design of the Turing Machine:
********** 3 **********
--- page 4 ---
Correct answer of “NO” – 1 Mark
Proper justification with Halting Problem explained –4 marks
Tuple Machine Design– 5 Marks (If logic explained- 2 Marks, if
designed fully 5 marks)
CO-3   c   An 𝜖-NFA is a Non-deterministic Finite Automaton with epsilon   [5]
BL-3   transitions.
SO-2   It is an NFA in which the machine can change from one state to another
without reading any input symbol. Such transitions are called 𝜖-transitions.
An 𝜖-NFA is defined as:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
where the transition function is:
𝛿: 𝑄× (Σ ∪{𝜖}) →2𝑄
This means the transition function may take:
•   an input symbol from Σ, or
•   𝜖
Design of an NFA:
𝜖-NFA – 2 marks
Design of an NFA – 3 Marks
Q-3
CO-2   a   Final Minimized DFA:   [10]
BL-3
SO-2
********** 4 **********
--- page 5 ---
Step Marking to be done – 10 Marks
CO-3   b   If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is also a   [10]
BL-3,4   CFL
SO-2   Let us take a CFL:
𝐿1 = {𝑎𝑛𝑏𝑛∣𝑛≥0}
This is a Context-Free Language.
L1∗=(anbn)∗   i.e Zero or more repetitions of strings from 𝐿1
Original grammar for 𝐿1: S1→aS1b∣ϵ
Grammar for 𝐿1 ∗
S→SS1∣ϵ
S1→aS1b∣ϵ
This is also a Context-Free Language
Hence If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is
also a CFL
No, A single stack Pushdown Automaton (PDA):
• Has only one stack
• Can handle one level of counting/dependency
In 𝑎𝑛𝑏𝑛𝑐𝑛, we need to ensure:
• Number of a = number of b
• Number of b = number of c
That means:
• Two independent comparisons:
o 𝑎↔𝑏
o 𝑏↔𝑐
Therefore, this language cannot be accepted by a single stack PDA.
Closure property of CFL with Example– 5 marks
Explanation about the language – 5 marks
Q-4
CO-2   a   Arden’s Theorem simplifies regular expressions by providing a systematic   [10]
BL-3   approach to solving equations of the form X = AX + B. By applying the
SO-2   theorem, complex regular expressions can be rewritten in a more concise
form using concatenation and the Kleene closure operation, resulting in
simplified expressions.
Arden’s theorem Solution for generating regular expression –
********** 5 **********
--- page 6 ---
How can Arden’s Theorem simplify regular expressions – 2 Marks
Construction of RE - 8 Marks (equation generation – 2 Marks,
q2 substitution – 2 Marks, q1 substitution -3 Marks,
final answer – 1 Mark)
CO-3   b   [10]
BL-3,4
SO-2
********** 6 **********
--- page 7 ---
Logic Explained – 3 Marks
TM Design – 5 Marks
String Tracing – 2 Marks
Q-5
CO-3   a   A Context-Free Grammar (CFG) is said to be ambiguous if:   [10]
BL-3   There exists at least one string in the language generated by the grammar
SO-2   that has more than one distinct parse tree (or equivalently, more than one
leftmost or rightmost derivation).
What makes a grammar ambiguous – 2 Marks
Identifying String for proving Ambiguity – 2 Marks
Atleast 2 derivations – 3 marks each (6 marks)
********** 7 **********
--- page 8 ---
CO-3   b   [10]
BL-3,4
SO-2
c) Moore Machine – If input sequence is of length n, then output
sequence if of length n+1
Mealy Machine – If input sequence is of length n, then output sequence if
of length n
a) 3 Marks
b) 5 Marks
c) 2 Marks
Q-6
CO-2   a   [10]
BL-3,4   Step 1: Remove Unit Productions   (3 Marks)
SO-2   Unit production:
• S → C
• B → A
Replace S → C using C → 01:
• S → 0A | 1B | 01
Replace B → A using A → 0S | 000:
• B → 11 | 0S | 000
Updated Grammar:
• S → 0A | 1B | 01
• A → 0S | 000
• B → 11 | 0S | 000
• C → 01
Step 2: Replace Terminals in Mixed Productions   (3 Marks)
Introduce new variables:
• X → 0
• Y → 1
********** 8 **********
--- page 9 ---
Replace terminals:
• 0A → XA
• 1B → YB
• 0S → XS
• 01 → XY
• 11 → YY
• 000 → XXX
Updated Grammar:
• S → XA | YB | XY
• A → XS | XXX
• B → YY | XS | XXX
• C → XY
• X → 0
• Y → 1
Step 3: Convert Long Productions (>2 symbols)   (3 Marks)
Break 3-length productions:
For XXX:
Introduce new variable:
• D → XX
So:
• XXX → XD
Updated Grammar:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Step 4: Final CNF Grammar   (1Mark)
Productions:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Stepwise marking – Total 10 marks
CO-2   b   Design logic -   [5]
BL-3   Read a’s
SO-2   → Push one symbol (X) for each a
Read b’s (first n b’s)
→ Pop one X for each b
After stack becomes empty (only 𝑍0remains)
→ Read exactly 2 extra b’s
Accept if input ends after those 2 extra b’s
Design of the PDA-
M=(Q,Σ,Γ,δ,q0,Z0,F)
𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
Σ = {𝑎, 𝑏}
********** 9 **********
--- page 10 ---
Γ = {𝑋, 𝑍0}
Start state: 𝑞0
Initial stack symbol: 𝑍0
Final state: 𝐹= {𝑞𝑓}
Transition functions
δ(𝑞0,a,Z0)=(q0,XZ0)
δ(q0,a,X)=(q0,XX)
δ(q0,b,X)=(q1,ϵ)
δ(q1,b,X)=(q1,ϵ)
δ(q1,b, Z0)=(q2, Z0)
δ(q2,b, Z0)=(q3, Z0)
δ(q3,ϵ, Z0)=(qf, Z0)
Logic Design – 2 Marks
PDA Design and tuples– 3 Marks
CO-1   c   [5]
BL-2
SO-2
Production rules – 1 Mark
Language recognized - 1 Mark
Machine – 1 Mark
Closed under properties -2 Marks
Q-7
CO-2,3   a   1   [10]
BL-3   NFA (2 Marks)
SO-2   State   a   b
A (initial)   {A, B} A
B   C   C
C (Final)   -   -
2 DFA (3 Marks)
State   a   b
{A} (initial)   {A,B} {A}
{A,B}   {A,B,C} {A,C}
{A,B,C} (Final) {A,B,C} {A,C}
{A,C}(Final)   {A,B} {A}
3 Minimization [3 Marks]
********** 10 **********
--- page 11 ---
Step 1 Reachability Check: All states are reachable. No state will be
eliminated.
Step 2 Equivalence test
a) 0-equivalent: {{A},{A,B}} {{A,B,C},{A,C}}
b) 1-equivalent: {A}{A,B}{A,B,C}{A,C}
c) 2-equivalent: {A}{A,B}{A,B,C}{A,C}
All states are distinguishable. DFA is already minimized
4 Regular Expression [2 Marks]
(a+b)* a (a+b)
1.NFA -2 Marks
2.DFA-3 Marks
3.Minimized DFA 3 Marks
4.Regular Expression-2 Marks
CO-1   b   a)Non-terminals: {S}, Terminals: {a, b}   [5]
BL-2   b) Example strings: ε, ab, aabb, abab
SO-2   c) L(G) = { w ∈ {a, b}* | number of a’s = number of b’s }
d) The grammar is Context-Free (Type 2) as productions are of the
for V->(VUT)* and generates a Context-Free Language.
a) 2 Marks
b) 1 Mark
c) 1 Mark
d) 1 Mark
CO-3   c   Logic: The language requires at least one ‘a’ anywhere in the string.   [5]
BL-3   We only need to check presence, not count or match.
SO-2   So:
•   Stay in initial state while reading 𝑏's
• Move to accepting state when first 𝑎is seen
•   After that, accept any combination of 𝑎and 𝑏
Let the PDA be, M=(Q,Σ,Γ,δ,q0,Z0,F)
Components
• 𝑄= {𝑞0, 𝑞1}
• Σ = {𝑎, 𝑏}
• Γ = {𝑍0}(stack symbol, but unused)
•   Start state: 𝑞0
•   Initial stack symbol: 𝑍0
•   Final states: 𝐹= {𝑞1}
•   𝛿:
δ(𝑞0,b, 𝑍0) ={(𝑞0,𝑍0)}
𝛿(𝑞0, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑏, 𝑍0) = {(𝑞1,𝑍0)}
As The language only requires checking:
presence of at least a single “a”, This can be done using a Finite
Automaton (FA) since:
********** 11 **********
--- page 12 ---
• No counting or memory of arbitrary size is required
Hence, Stack implementation through PDA is not required.
PDA Design – 2 Marks
determine whether the use of a stack is necessary for
PDA this design language, : 3 Marks giving reason. – 3 Marks
Tuples writing : 1 Mark
Justification : 1 Mark
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper b9b374ca66b6

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_Computer_7032/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C011)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 14 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   The applications of automata theory in compiler design:   [5]
BL-2
SO-2   Lexical Analysis: Uses Finite Automata to recognize tokens.
Syntax Analysis: Uses Context-Free Grammars for parsing.
Parser Design: PDA-based parsing techniques (LL, LR).
Pattern Matching: Regular expressions for token identification.
Code Optimization & Translation: Formal models help in structured
translation.
1 Mark for each Application - Explanation expected in brief
CO-2   b   Transition function DFA : δ:Q×Σ→Q (exactly one state)   [5]
BL-2   Transition function NFA : δ:Q×ΣU{ ℇ }→2Q (the transition function gives
SO-2   a set of possible next states.)
For every:
•   current state 𝑞∈𝑄
•   input symbol 𝑎∈Σ
Tuples of the machine to be mentioned
********** 1 **********
--- page 2 ---
Transition function difference – 2 marks
Design of a DFA – 2 Marks
Tuple specification – 1 mark
CO-3   c   [5]
BL-2,3   LMD (2.5 M)   Parse Tree (2.5 M)
SO-2
S   ⇒bSaS (Using S→ bSaS)
⇒bεaS (Using S→ ε )
⇒baS
⇒baaSbS (Using S→ aSbS)
⇒baabS (Using S→ ε )
⇒baabaSbS (Using S→ aSbS)
⇒baababS (Using S→ ε )
⇒baabab (Using S→ ε )
LMD – 2.5 marks
Parse Tree – 2.5 Marks
CO-1   d   [5]
BL-2   Church-Turing Hypothesis
SO-2   -   This is also known as Church-Turing Conjecture, Church Thesis or
Church’s Conjecture
-   It is essentially states that everything that is algorithmically
computable is computable by a TM.
-   American mathematician, Alonzo Church, created a method called
Lambda Calculus for defining functions.
-   It is an equivalent computational model of the UTM.
-   Hypothesis: - The intuitive notion of a computable function can be
identified with the class of partial recursive functions. In other
words, every problem having an algorithmic solution can be solved
using a machine having the foregoing set of instructions.
Explanation – 5 Marks
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Tuples Q={q0, q1, q2, q3, q4}
∑ ={0,1}
Δ ={N, Y}
δ : δ
𝜆→ Q X ∑ → Δ
Tuples to be specified
Design of the Moore Machine – 4 Marks, Tuples- 1 Mark
********** 2 **********
--- page 3 ---
CO-3   b   No, it is not always possible to determine whether a given program will   [10]
BL-3   halt for a specific input.
SO-2   This is explained by the Halting Problem, a fundamental concept in
computability theory.
Halting Problem:
The halting problem was proposed by Alan Turing in 1936. The halting
problem is a fundamental issue in theoretical and computational complexity.
The halting problem is the problem of determining whether a computer
program will halt or run forever.
Input − A Turing machine and an input string w.
Problem − Does the Turing machine finish computing of the string w in a
finite number of steps? The answer must be either yes or no.
Proof − At first, we will assume that such a Turing machine exists to solve
this problem and then we will show it is contradicting itself. We will call
this Turing machine as a Halting machine that produces a ‘yes’ or ‘no’ in a
finite amount of time. If the halting machine finishes in a finite amount of
time, the output comes as ‘yes’, otherwise as ‘no’. The following is the
block diagram of a Halting machine −
Now we will design an inverted halting machine (HM)’ as –
-   If H returns YES, then loop forever.
-   If H returns NO, then halt.
The following is the block diagram of an ‘Inverted halting machine’ −
Further, a machine (HM)2 which input itself is constructed as follows −
-   If (HM)2 halts on input, loop forever.
-   Else, halt.
Here, we have got a contradiction. Hence, the halting problem is
undecidable.
Design of the Turing Machine:
********** 3 **********
--- page 4 ---
Correct answer of “NO” – 1 Mark
Proper justification with Halting Problem explained –4 marks
Tuple Machine Design– 5 Marks (If logic explained- 2 Marks, if
designed fully 5 marks)
CO-3   c   An 𝜖-NFA is a Non-deterministic Finite Automaton with epsilon   [5]
BL-3   transitions.
SO-2   It is an NFA in which the machine can change from one state to another
without reading any input symbol. Such transitions are called 𝜖-transitions.
An 𝜖-NFA is defined as:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
where the transition function is:
𝛿: 𝑄× (Σ ∪{𝜖}) →2𝑄
This means the transition function may take:
•   an input symbol from Σ, or
•   𝜖
Design of an NFA:
𝜖-NFA – 2 marks
Design of an NFA – 3 Marks
Q-3
CO-2   a   Final Minimized DFA:   [10]
BL-3
SO-2
********** 4 **********
--- page 5 ---
Step Marking to be done – 10 Marks
CO-3   b   If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is also a   [10]
BL-3,4   CFL
SO-2   Let us take a CFL:
𝐿1 = {𝑎𝑛𝑏𝑛∣𝑛≥0}
This is a Context-Free Language.
L1∗=(anbn)∗   i.e Zero or more repetitions of strings from 𝐿1
Original grammar for 𝐿1: S1→aS1b∣ϵ
Grammar for 𝐿1 ∗
S→SS1∣ϵ
S1→aS1b∣ϵ
This is also a Context-Free Language
Hence If 𝐿is a Context-Free Language (CFL), then its Kleene star 𝐿∗is
also a CFL
No, A single stack Pushdown Automaton (PDA):
• Has only one stack
• Can handle one level of counting/dependency
In 𝑎𝑛𝑏𝑛𝑐𝑛, we need to ensure:
• Number of a = number of b
• Number of b = number of c
That means:
• Two independent comparisons:
o 𝑎↔𝑏
o 𝑏↔𝑐
Therefore, this language cannot be accepted by a single stack PDA.
Closure property of CFL with Example– 5 marks
Explanation about the language – 5 marks
Q-4
CO-2   a   Arden’s Theorem simplifies regular expressions by providing a systematic   [10]
BL-3   approach to solving equations of the form X = AX + B. By applying the
SO-2   theorem, complex regular expressions can be rewritten in a more concise
form using concatenation and the Kleene closure operation, resulting in
simplified expressions.
Arden’s theorem Solution for generating regular expression –
********** 5 **********
--- page 6 ---
How can Arden’s Theorem simplify regular expressions – 2 Marks
Construction of RE - 8 Marks (equation generation – 2 Marks,
q2 substitution – 2 Marks, q1 substitution -3 Marks,
final answer – 1 Mark)
CO-3   b   [10]
BL-3,4
SO-2
********** 6 **********
--- page 7 ---
Logic Explained – 3 Marks
TM Design – 5 Marks
String Tracing – 2 Marks
Q-5
CO-3   a   A Context-Free Grammar (CFG) is said to be ambiguous if:   [10]
BL-3   There exists at least one string in the language generated by the grammar
SO-2   that has more than one distinct parse tree (or equivalently, more than one
leftmost or rightmost derivation).
What makes a grammar ambiguous – 2 Marks
Identifying String for proving Ambiguity – 2 Marks
Atleast 2 derivations – 3 marks each (6 marks)
********** 7 **********
--- page 8 ---
CO-3   b   [10]
BL-3,4
SO-2
c) Moore Machine – If input sequence is of length n, then output
sequence if of length n+1
Mealy Machine – If input sequence is of length n, then output sequence if
of length n
a) 3 Marks
b) 5 Marks
c) 2 Marks
Q-6
CO-2   a   [10]
BL-3,4   Step 1: Remove Unit Productions   (3 Marks)
SO-2   Unit production:
• S → C
• B → A
Replace S → C using C → 01:
• S → 0A | 1B | 01
Replace B → A using A → 0S | 000:
• B → 11 | 0S | 000
Updated Grammar:
• S → 0A | 1B | 01
• A → 0S | 000
• B → 11 | 0S | 000
• C → 01
Step 2: Replace Terminals in Mixed Productions   (3 Marks)
Introduce new variables:
• X → 0
• Y → 1
********** 8 **********
--- page 9 ---
Replace terminals:
• 0A → XA
• 1B → YB
• 0S → XS
• 01 → XY
• 11 → YY
• 000 → XXX
Updated Grammar:
• S → XA | YB | XY
• A → XS | XXX
• B → YY | XS | XXX
• C → XY
• X → 0
• Y → 1
Step 3: Convert Long Productions (>2 symbols)   (3 Marks)
Break 3-length productions:
For XXX:
Introduce new variable:
• D → XX
So:
• XXX → XD
Updated Grammar:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Step 4: Final CNF Grammar   (1Mark)
Productions:
• S → XA | YB | XY
• A → XS | XD
• B → YY | XS | XD
• C → XY
• D → XX
• X → 0
• Y → 1
Stepwise marking – Total 10 marks
CO-2   b   Design logic -   [5]
BL-3   Read a’s
SO-2   → Push one symbol (X) for each a
Read b’s (first n b’s)
→ Pop one X for each b
After stack becomes empty (only 𝑍0remains)
→ Read exactly 2 extra b’s
Accept if input ends after those 2 extra b’s
Design of the PDA-
M=(Q,Σ,Γ,δ,q0,Z0,F)
𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
Σ = {𝑎, 𝑏}
********** 9 **********
--- page 10 ---
Γ = {𝑋, 𝑍0}
Start state: 𝑞0
Initial stack symbol: 𝑍0
Final state: 𝐹= {𝑞𝑓}
Transition functions
δ(𝑞0,a,Z0)=(q0,XZ0)
δ(q0,a,X)=(q0,XX)
δ(q0,b,X)=(q1,ϵ)
δ(q1,b,X)=(q1,ϵ)
δ(q1,b, Z0)=(q2, Z0)
δ(q2,b, Z0)=(q3, Z0)
δ(q3,ϵ, Z0)=(qf, Z0)
Logic Design – 2 Marks
PDA Design and tuples– 3 Marks
CO-1   c   [5]
BL-2
SO-2
Production rules – 1 Mark
Language recognized - 1 Mark
Machine – 1 Mark
Closed under properties -2 Marks
Q-7
CO-2,3   a   1   [10]
BL-3   NFA (2 Marks)
SO-2   State   a   b
A (initial)   {A, B} A
B   C   C
C (Final)   -   -
2 DFA (3 Marks)
State   a   b
{A} (initial)   {A,B} {A}
{A,B}   {A,B,C} {A,C}
{A,B,C} (Final) {A,B,C} {A,C}
{A,C}(Final)   {A,B} {A}
3 Minimization [3 Marks]
********** 10 **********
--- page 11 ---
Step 1 Reachability Check: All states are reachable. No state will be
eliminated.
Step 2 Equivalence test
a) 0-equivalent: {{A},{A,B}} {{A,B,C},{A,C}}
b) 1-equivalent: {A}{A,B}{A,B,C}{A,C}
c) 2-equivalent: {A}{A,B}{A,B,C}{A,C}
All states are distinguishable. DFA is already minimized
4 Regular Expression [2 Marks]
(a+b)* a (a+b)
1.NFA -2 Marks
2.DFA-3 Marks
3.Minimized DFA 3 Marks
4.Regular Expression-2 Marks
CO-1   b   a)Non-terminals: {S}, Terminals: {a, b}   [5]
BL-2   b) Example strings: ε, ab, aabb, abab
SO-2   c) L(G) = { w ∈ {a, b}* | number of a’s = number of b’s }
d) The grammar is Context-Free (Type 2) as productions are of the
for V->(VUT)* and generates a Context-Free Language.
a) 2 Marks
b) 1 Mark
c) 1 Mark
d) 1 Mark
CO-3   c   Logic: The language requires at least one ‘a’ anywhere in the string.   [5]
BL-3   We only need to check presence, not count or match.
SO-2   So:
•   Stay in initial state while reading 𝑏's
• Move to accepting state when first 𝑎is seen
•   After that, accept any combination of 𝑎and 𝑏
Let the PDA be, M=(Q,Σ,Γ,δ,q0,Z0,F)
Components
• 𝑄= {𝑞0, 𝑞1}
• Σ = {𝑎, 𝑏}
• Γ = {𝑍0}(stack symbol, but unused)
•   Start state: 𝑞0
•   Initial stack symbol: 𝑍0
•   Final states: 𝐹= {𝑞1}
•   𝛿:
δ(𝑞0,b, 𝑍0) ={(𝑞0,𝑍0)}
𝛿(𝑞0, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑎, 𝑍0) = {(𝑞1,𝑍0)}
𝛿(𝑞1, 𝑏, 𝑍0) = {(𝑞1,𝑍0)}
As The language only requires checking:
presence of at least a single “a”, This can be done using a Finite
Automaton (FA) since:
********** 11 **********
--- page 12 ---
• No counting or memory of arbitrary size is required
Hence, Stack implementation through PDA is not required.
PDA Design – 2 Marks
determine whether the use of a stack is necessary for
PDA this design language, : 3 Marks giving reason. – 3 Marks
Tuples writing : 1 Mark
Justification : 1 Mark
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper cbeeeeae932b

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSBS_7036/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: mixed (11 pages), mean OCR confidence 52.9
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume data wherever needed.
5. Question No. 1 is compulsory. From remaining 6 questions, attempt any 4 questions.
Q1
Answer briefly:   [20]
a.   Write about Grammar and its type in automata theory.
Ans:
Grammar Definition (1M): A formal system G=(V,Σ,P,S), where V are
non-terminals, Σ are terminals, P are production rules, and S is the start
symbol. Types (4M for Chomsky Hierarchy - 1M each):
CO-1;   Type 0 (Unrestricted): Recursively Enumerable Languages (Turing [5]
BL-1
Machines).
Type 1 (Context-Sensitive): Context-Sensitive Languages (Linear
Bounded Automata).
Type 2 (Context-Free): Context-Free Languages (Pushdown Automata).
Type 3 (Regular): Regular Languages (Finite Automata).
b.   Distinguish between DFA & NFA.
Ans:
5M for 8 distinct points of difference:
CO-1;   DFA   NFA   [5]
BL-1
NFA stands for
DFA stands for Deterministic Finite
Nondeterministic Finite
Automata.
Automata.
********** 1 **********
--- page 2 ---
For each symbolic representation of   No need to specify how does
the alphabet, there is only one state   the NFA react according to
transition in DFA.   some symbol.
DFA cannot use Empty String   NFA can use Empty String
transition.   transition.
NFA can be understood as
DFA can be understood as one
multiple little machines
machine.
computing at the same time.
In NFA, each pair of state and
In DFA, the next possible state is
input symbol can have many
distinctly set.
possible next states.
DFA is more difficult to construct.   NFA is easier to construct.
DFA rejects the string in case it   NFA rejects the string in the
terminates in a state that is different   event of all branches dying or
from the accepting state.   refusing the string.
Time needed for executing an input   Time needed for executing an
string is less.   input string is more.
All DFA are NFA.   Not all NFA are DFA.
NFA requires less space then
DFA requires more space.
DFA.
Dead configuration is allowed.
Dead configuration is not allowed.
eg: if we give input as 0 on q0
eg: if we give input as 0 on q0 state
state so we can give next input
so we must give 1 as input to q0 as
1 on q1 which will go to next
self loop.
state.
δ: Qx(Σ U ε) -> 2^Q i.e. next
δ: QxΣ -> Q i.e. next possible state
possible state belongs to power
belongs to Q.
set of Q.
********** 2 **********
--- page 3 ---
Conversion of Regular
Conversion of Regular expression
expression to NFA is simpler
to DFA is difficult.
compared to DFA.
Epsilon move is not allowed in   Epsilon move is allowed in
DFA   NFA
In an NFA, there can
In a DFA, there is only one possible
be multiple transitions for a
transition for each input symbol
single input symbol from a
from any given state.
given state.
c.   For the following Moore Machine the input alphabet is Σ {a,b} & output
is ∆ {0,1}. Draw state diagram & then run the following input sequence
&   find   the   respective   output:
i. aabab   ii. abbb   iii. ababb
States   a   b   Output
Q0   Q1   Q2   0
Q1   Q2   Q3   0
Q2   Q3   Q4   1
Q3   Q4   Q4   0
Q4   Q0   Q0   0
Ans:
5M for running 3 sequences (2M State Diagram, 1M for i, 1M for ii,
CO-1;   1M for iii):   [5]
BL-3
CO-3;   d.   Write a short note on Church Turing Hypothesis.   [5]
********** 3 **********
--- page 4 ---
BL-1   Ans:
5M for detailed explanation:
Hypothesis: The Church-Turing Thesis states that any function that can
be computed by an algorithm (using any computation model like a human
with paper, a modern computer, etc.) can also be computed by a Turing
Machine.
Significance: It establishes the Turing Machine as the ultimate
theoretical model of computation. If a problem cannot be solved by a
Turing Machine, it cannot be solved by any known algorithm or
computer. It links the informal notion of "effective computability" with
the formal notion of "Turing machine computability."
a.   Design a Mealy machine controls traffic lights based on sensors detecting
vehicle presence. If a car is detected (input 1), it changes light from Red
to Green and outputs G. If no car is present (input 0), it stays Red and
outputs R.
Convert the machine to Moore machine.
Ans:
Mealy Machine Design (3M), Transition Table (2M), Conversion of
Mealy to Moore (5M)
[10]
Q2
CO-2;
BL-3
b.   Design a DFA having even numbers of “a” & even numbers of “b” over
{a,b}.   [10]
Ans:
********** 4 **********
--- page 5 ---
4M for state Diagram & Tuples, 3M for transitions and 3M for
Examples
a.   Minimize given DFA:
Q3
[10]
CO-2,3;
BL-3
Ans:
2M Transition Table, 2M Identification of inaccessible states, 2M for
Initial Partition, 2M for Iterative Partitioning, 2M for Final Minimal
DFA
********** 5 **********
--- page 6 ---
b.   Design a Turing machine that computes a function f(m,n) = m+n which
does addition of two integers.
Ans:
4M for state Diagram & Tuples, 3M for transitions and 3M for Examples
[10]
a.   Simplify the given grammar having production rules, P:
Q4   S → AC | B; A → a | ꞓ; C → c | BC ; E → aA | b
CO-2,3;   Ans:   [10]
BL-3   Eliminate ϵ-productions (3M); Eliminate Unit Productions (4M); Eliminate
Useless Symbols (3M)
********** 6 **********
--- page 7 ---
b.   Construct a PDA that accepts the language of palindromes over {a,b}:
L={wCwR ∣ w∈{a,b}∗}
Ans:
4M for state Diagram & Tuples, 3M for transitions and 3M for Examples
[10]
a.   Simplify the given grammar and then convert it to CNF.
Q5   S→ASA ∣ aB; A→B ∣ a ; B→b | ϵ
CO-2;   Ans:   [10]
BL- 3   Eliminate ϵ-productions (2M); Eliminate Unit Productions (2M); Eliminate
Useless Symbols (1M); Conversion of CFG to CNF (5M)
********** 7 **********
--- page 8 ---
b.   Construct a DFA which accepts a language of all decimal numbers
divisible by 4.
Ans:
4M for state Diagram & Tuples, 3M for transitions and 3M for Examples
[10]
a.   Build a Moore machine to accept a string starts with “011” and ends at
Q6
“00”.
CO-2,3;   [10]
Ans:
BL-
4M for state Diagram & Tuples, 3M for transitions and 3M for Examples
********** 8 **********
--- page 9 ---
b.   Explain in detail: Universal Turing Machine.
Ans:
Definition (3M): A Universal Turing Machine (UTM) is a special
Turing Machine that acts as a simulator. It takes an encoded description
of an arbitrary Turing Machine M and its input w on its tape, and then
simulates the exact sequence of moves that M would make on w. Inputs:
The UTM's tape is divided into sections, typically holding: 1. The
encoded description of the machine M. 2. The simulated tape content of
M. 3. The current state of M.   [10]
Significance (4M): The UTM is the theoretical precursor to the modern,
stored-program computer (Von Neumann Architecture). It demonstrates
that a single, fixed-structure machine can perform any computable task,
simply by changing the program (encoding) provided as input.
Process (3M): The UTM cyclically reads the current state (from section
3) and the current tape symbol (from section 2), looks up the
corresponding transition in the encoded δ function (section 1), updates
the tape symbol and the state, and moves the simulated tape head.
a.   Compare and contrast PDA & Turing Machine.
Ans:
(5 points for comparison, 5 for contrast)
Q7
CO-3,2;   • Pushdown Automaton (PDA): A PDA is a computational model [10]
BL-   that is similar to a finite automaton but with an additional stack-
based memory. It can recognize context-free languages (CFLs)
and is equipped with a finite state machine (FSM) along with a
stack that can store an arbitrary amount of information. The PDA
operates by reading input symbols, transitioning between states,
and modifying the stack according to predefined rules.
********** 9 **********
--- page 10 ---
• Turing Machine (TM): A Turing Machine is a more powerful
computational model, consisting of a tape (which can be infinitely
long), a tape head (which can read, write, and move left or right),
and a finite control. A Turing Machine can recognize recursively
enumerable languages (RE) and can simulate any algorithmic
process.
Pushdown Automaton
Aspect   Turing Machine (TM)
(PDA)
An infinite tape. The tape is
A single stack. The stack
Memory   used for both reading and
allows LIFO (Last In, First
Structure   writing, and the head can
Out) operations.
move left or right.
Recursively Enumerable
Languages (RE), which
Accepted   Context-Free Languages
include all languages that a
Languages   (CFLs).
computer can decide (or
semi-decide).
Less powerful. Can’t   More powerful. It can
compute certain types of   simulate any algorithm or
Computatio
languages like those that   computational process,
nal Power
require more than one   making it a general-purpose
stack of memory.   model of computation.
Has an infinite tape and a
No tape. It only has a finite
Tape/Storag   tape head, which can
state and a stack. The stack
e   read/write at any position on
allows for limited memory
Mechanism   the tape and move in both
operations.
directions.
Finite set of states, but the
Finite set of states.
machine can perform a
Transitions depend on the
wider range of operations,
States   current state, the current
including modifying the
input symbol, and the top
tape and moving the tape
of the stack.
head.
Acceptance is based on
whether the PDA ends in a Acceptance is based on
Accepting
particular state and the   whether the machine halts
Conditions
stack being empty or in a   in an accepting state.
particular configuration.
PDAs can be deterministic TMs can also be
Determinism (DPDA) or non-   deterministic (DTM) or
deterministic (NPDA).   non-deterministic (NTM).
b.   Convert the regular expression (a+b) *aa(b+c) into an NFA. Convert
the NFA into an equivalent DFA.
[10]
Ans:
4M for RE to NFA, 6M for NFA to DFA
********** 10 **********
--- page 11 ---
RK KKK RK KK 11 2h KKK RK Kk KK
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper d4e102309d2d

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CS_7055/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   In Formal Language Theory, a string is a finite sequence of symbols chosen from   [5]
BL-2   a given alphabet. (2 Marks)
SO-2   •   Alphabet: Σ = {a, b}
• Examples of strings: a, b, ab, ba, aab
• The empty string is denoted by ε and has length 0
All strings of length ≤ 3: (2 Marks)
{ ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb }
Strings belonging to L: (1 Mark)
{ ab, aab, abb }
CO-2   b   [5]
BL-2   i) Language- (2 Mark)
SO-2   (010)* - All strings that consist of zero or more repetitions of the substring “010”.
(0*10*)* - L is the set of all strings over the alphabet {0,1} that are formed by
concatenating zero or more blocks, where each block contains exactly one ‘1’
surrounded by any number of ‘0’s.
ii) Key Property of the recognized language- (2 Marks)
(010)*- Here pattern is strictly repeated and Length of the string is always a
multiple of 3
(0*10*)* - Every non-empty string in the language must contain at least one 1.
iii)Example –(1 Mark)
(e.g) (010)*- 010010 , 010010010
(0*10*)* - 1001,1010
CO-3   c A nullable variable in a Context-Free Grammar (CFG) is a variable that can   [5]
BL-2,3   derive the empty string 𝜖.
SO-2   𝐴⇒∗𝜖
********** 1 **********
--- page 2 ---
That is, if a variable can produce 𝜖 either directly or through a sequence of
productions, it is called nullable. (1 Mark)
For the given grammar two non-terminals are nullable P and T
Elimination of 𝜖 productions (4 Marks)
The nullable variables are P and T
Hence after removing 𝜖 productions , grammar takes the form
𝑆→PPRT∣PRT∣RT∣PPR∣PR∣R
𝑃→𝑎𝑃𝑏| ab
𝑅→𝑎𝑅∣𝑎
𝑇→𝑎𝑇𝑎∣𝑏𝑇𝑏∣𝑎𝑎∣𝑏𝑏
CO-1   d Defining an appropriate Function like 𝑓(𝑛) = 𝑛+ 1(Unary Representation) (1   [5]
BL-2   Mark)
SO-2   Final tuples and design of Turing machine (4 Marks)
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Design of the Moore Machine – (4 Marks)
Checking the machine with a sample string – (1 Mark)
CO-3   b Recursive and Recursively Enumerable   [10]
BL-3
SO-2   There are two types of TMs (based on halting):
Recursive
- TMs that always   halt, no matter accepting or non-accepting 
DECIDABLE PROBLEMS
- Any TM for a Recursive language is going to look like this:
Recursively enumerable
- TMs that are guaranteed to halt only on acceptance. If non-accepting, it
may or may not halt (i.e., could loop forever).
- Any TM for a recursively enumerable (RE) language is going to look like
this:
********** 2 **********
--- page 3 ---
Turing Machine to find the value of log2 (n)
Recursive and Recursively Enumerable – (05 Marks)
Turing Machine Design– (05 Marks)
CO-3   c   [5]
BL-3
SO-2
Q = {0,1,2,3,4,5} ⅀ = {0,1} q0 = 0 F={5}
[3 marks DFA + 2 Marks Tuples]
Q-3
CO-2   a Proof (Using Finite Automata Construction)   [10]
BL-3   Step 1: Given (2 Mark)
SO-2   Since 𝐿1and 𝐿2are regular, there exist DFAs:
********** 3 **********
--- page 4 ---
𝑀2 = (𝑄2, Σ, 𝛿2, 𝑞2, 𝐹2)
Step 2: Construct a New DFA (4 Marks)
We construct a new DFA 𝑀 such that:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
Where:
• 𝑄= 𝑄1 × 𝑄2(Cartesian product of states)
• 𝑞0 = (𝑞1, 𝑞2)
•   Transition function:
𝛿((𝑝, 𝑞), 𝑎) = (𝛿1(𝑝, 𝑎), 𝛿2(𝑞, 𝑎))
Step 3: Define Final States (2 Marks)
For union, a string is accepted if it is accepted by either M1or M2.
So,
F = {(p, q) ∣p ∈F1 OR q ∈F2}
Step 4: Working Explanation (2 Marks)
• The new DFA simulates both machines simultaneously.
•   If either machine reaches a final state, the combined machine
accepts the string.
• Hence, it accepts all strings in:
L1 ∪L2
Step 5: Conclusion
Since we constructed a DFA for L1 ∪L2,
L1 ∪L2 is regular.
CO-3   b A Pushdown Automaton (PDA) extends a Finite Automaton by adding a stack.   [10]
BL-3,4   This single addition makes a big difference: (3 Marks)
SO-2   • Memory:
Finite Automata have only finite control (no memory of unbounded size).
PDAs have a stack, allowing them to remember an arbitrary amount of
information.
• Language class:
Finite Automata recognize regular languages.
PDAs recognize context-free languages (CFLs).
•   Capability difference:
PDAs can handle nested and matching patterns, e.g.:
o 0𝑛1𝑛
o balanced parentheses
These cannot be recognized by any finite automaton.
Let PDA be:
𝑀= (𝑄, Σ, Γ,𝛿, 𝑞0, 𝑍0, 𝐹)
Components
• 𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
• Σ = {0,1,2}
• Γ = {𝑍0, 𝑋}(Z₀ = initial stack symbol)
•   Start state = 𝑞0
•   Final state = 𝑞𝑓
δ(q₀, 0, Z₀) → (q₁, Z₀) (Reading zero)
δ(q₁, 1, Z₀) → (q₁, XZ₀)
δ(q₁, 1, X) → (q₁, XX)
δ(q₁, 0, X) → (q₂, X)
δ(q₂, 2, X) → (q₃, X)
********** 4 **********
--- page 5 ---
δ(q₃, 0, X) → (q₃, X)
δ(q₃, 1, X) → (q₃, ε) (Match 1ⁿ and pop)
δ(q₃, 0, Z₀) → (qf, Z₀)
Tuples of PDA (2 Marks)
Transition Function (5 Marks)
Q-4
CO-2   a The pumping lemma is a fundamental property of all regular languages. It is   [10]
BL-3   mainly used to prove that a language is NOT regular. (1 Mark)
SO-2   Pumping lemma states that
If L is a regular language, then there exists a constant p such that every string w ∈
L, of length p or more can be written as w = xyz, where
1.   |y| > 0
2. |xy| ≤ p
3. xyiz ∈ L for all i (2 Marks)
NO, Never use pumping lemma to prove a language regular. Pumping property is
necessary but not sufficient for regularity. (2 Marks)
The language L = { an : n is prime } is not regular.
Lets assume L is regular. Let p be the pumping length. Let q ≥ p be a prime
number (since we cannot assume that pumping length p will be prime).
Consider the string w = aa....a such that |w| = q ≥ p.
We know that w can be broken into three terms xyz such that y ≠ ε and xyiz ∈ L
⇒ xyq+1z must belong to L
⇒ |xyq+1z| must be prime
|xyq+1z| = |xyzyq|
= |xyz| + |yq|
= q + q.|y|
= q(1 + |y|) which is a composite number.
Therefore, xyq+1z cannot belong to L. Hence, L is not regular. (5 Marks)
CO-3   b   [10]
BL-3,4
SO-2
********** 5 **********
--- page 6 ---
Logic – 01 Mark
Tuples – 02 Marks
Turing Machine – 07 Marks
Q-5
CO-3   a CNF definition – 2 Marks   [10]
BL-3   GNF definition – 2 Marks
SO-2
Step 1: Eliminate terminals from long productions (2 Marks)
In CNF, productions must be of the form:
• 𝐴→𝐵𝐶 OR
• 𝐴→𝑎
So replace terminals in mixed strings.
Introduce new variables:
𝐶𝑎→𝑎, 𝐶𝑏→𝑏
Now rewrite:
𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
𝐴→𝐴𝐶𝑏∣𝑏
𝐵→𝐵𝐶𝑎∣𝑎
Step 2: Break long productions into binary form (2 Marks)
For 𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
Break stepwise:
1. Let 𝑋1 →𝐶𝑎𝐴
2. Let 𝑋2 →𝐶𝑏𝐵
Then: 𝑆→𝑋1𝑋2
Final Grammar in CNF (2 Marks)
S→X1X2
X1→CaA
X2→CbB
A→ACb∣b
B→BCa∣a
Ca→a
Cb→b
********** 6 **********
--- page 7 ---
CO-3   b   [10]
BL-3,4
SO-2
Mealy Machine design – 6 Marks
Tuples – 2 Marks
Sample String verification – 2 Marks
Q-6
CO-2   a   [10]
BL-3,4
SO-2   LMD:   RMD:
S ⇒aSc   S⇒aSc
⇒aaScc   ⇒aaScc
⇒aabSdcc   ⇒aabSdcc
⇒aabbSddcc   ⇒aabbSddcc
⇒aabbTddcc   ⇒aabbTddcc
⇒aabbeTfddcc   ⇒aabbeTfddcc
⇒aabbeeTffddcc   ⇒aabbeeTffddcc
⇒aabbeeeTfffddcc   ⇒aabbeeeTfffddcc
⇒aabbeeefffddcc   ⇒aabbeeefffddcc
LMD + Parse Tree– (3 +2 Marks)
RMD + Parse Tree – (3+2 Marks)
CO-2   b   [5]
BL-3
SO-2
Design of the PDA – (3 Marks)
Verification of the string – (2 Marks)
********** 7 **********
--- page 8 ---
CO-1   c   Difference between Formal Grammar and Formal Language (2.5 Marks)   [5]
BL-2
SO-2   Feature   Formal Grammar   Formal Language
A set of rules used to generate A set of strings formed using
Definition
strings   symbols
(G = (V, T, P, S)) where rules   Represents all possible strings
Components
define generation   over alphabet
Nature   Generative mechanism   Result/output of grammar
Describes how strings are   Describes what strings are
Purpose
formed   valid
Example   S → aS   b
Difference between Empty String (ε) and Empty Set (∅) (2.5 Marks)
Feature   Empty String (ε)   Empty Set (∅)
Definition   A string with no symbols A set with no elements
Type   String   Set
Length   Length = 0   Not applicable
Belongs to language? Yes, can be an element No elements at all
Example   ε ∈ {ε, a, aa}   ∅ has no elements
Q-7
CO-2,3   a   [10]
BL-3   Limitations of Finite Automata – (2 Marks)
SO-2   1.No Memory (Beyond Finite States) - No Auxiliary Storage.
2. Cannot Handle Matching or Nesting
3.FSM recognizes only regular languages.
4. Limited Computational Power
Minimization of DFA –
Equivalences – (4 Marks)
0 equivalence ={{q4} ,{q1,q2,q3,q5,q6,q7,q8}}
1 equivalence ={{q4} ,{q1,q2,q6,q7},{q3,q5},{q8}}
2 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
3 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
The minimum state automata is reached and is given by:
Q’ = {{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}(1 Mark tuples)
q1’= [q1,q7] initial state
F’ = {q4} final state
Transition Table (2 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
********** 8 **********
--- page 9 ---
[q4] (final state)   [q4]   [q1,q7]
[q8]   [q1,q7]   [q4]
As [q8] is unreachable from initial state so the final table is: (1 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
[q4] (final state)   [q4]   [q1,q7]
CO-1   b Definition along with tuples– (2 Marks)   [5]
BL-2   A formal grammar is a mathematical model used to describe how strings in a
SO-2   language are formed.
A grammar is defined as:
𝐺= (𝑉, 𝑇, 𝑃, 𝑆)
where:
• V → set of variables (non-terminals)
• T → set of terminals
• P → set of production rules
• S → start symbol
Example of Grammar   (1 Mark)
𝑆→𝑎𝑆∣𝑏
This grammar generates strings like:
b, ab, aab, aaab, …
Difference between Terminals and non-terminals (2 Marks)
Feature   Terminals   Non-terminals
Symbols that form the final Symbols used to generate
Definition
strings   strings
Can be replaced using
Role   Cannot be replaced further
production rules
Lowercase letters, digits,
Representation   Uppercase letters
symbols
Appear in
Yes   No
output?
Example   a, b, 0, 1   S, A, B
CO-3   c A Non-deterministic Pushdown Automaton (NPDA) is an extension of a finite   [5]
BL-3   automaton with a stack memory. It can have multiple possible moves for the same
SO-2   input, stack symbol, and state.
NPDA is defined as: (Q, Σ, Γ, δ, q₀, Z₀, F)
· Q: Set of states
· Σ: Input symbols
· Γ: Stack symbols
· δ: Transition function
· q₀: Start state
********** 9 **********
--- page 10 ---
· Z₀: Initial stack symbol
· F: Final states
The NPDA can choose between multiple possible moves at any step (non-
determinism). It may:
• Push symbols onto the stack
• Pop symbols from the stack
•   Ignore input using ε-transitions
(3 Marks)
Specific Example of language (2 Marks)
Consider the language:
𝐿= {𝑤𝑤𝑅∣𝑤∈{𝑎, 𝑏}∗}
(i.e., palindromes)
Deterministic PDA (DPDA) Fails in this scenario
• A DPDA cannot determine the middle of the string.
•   It does not know when to stop pushing and start popping.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper b5b44554a3b2

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Computer_7002/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   In Formal Language Theory, a string is a finite sequence of symbols chosen from   [5]
BL-2   a given alphabet. (2 Marks)
SO-2   •   Alphabet: Σ = {a, b}
• Examples of strings: a, b, ab, ba, aab
• The empty string is denoted by ε and has length 0
All strings of length ≤ 3: (2 Marks)
{ ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb }
Strings belonging to L: (1 Mark)
{ ab, aab, abb }
CO-2   b   [5]
BL-2   i) Language- (2 Mark)
SO-2   (010)* - All strings that consist of zero or more repetitions of the substring “010”.
(0*10*)* - L is the set of all strings over the alphabet {0,1} that are formed by
concatenating zero or more blocks, where each block contains exactly one ‘1’
surrounded by any number of ‘0’s.
ii) Key Property of the recognized language- (2 Marks)
(010)*- Here pattern is strictly repeated and Length of the string is always a
multiple of 3
(0*10*)* - Every non-empty string in the language must contain at least one 1.
iii)Example –(1 Mark)
(e.g) (010)*- 010010 , 010010010
(0*10*)* - 1001,1010
CO-3   c A nullable variable in a Context-Free Grammar (CFG) is a variable that can   [5]
BL-2,3   derive the empty string 𝜖.
SO-2   𝐴⇒∗𝜖
********** 1 **********
--- page 2 ---
That is, if a variable can produce 𝜖 either directly or through a sequence of
productions, it is called nullable. (1 Mark)
For the given grammar two non-terminals are nullable P and T
Elimination of 𝜖 productions (4 Marks)
The nullable variables are P and T
Hence after removing 𝜖 productions , grammar takes the form
𝑆→PPRT∣PRT∣RT∣PPR∣PR∣R
𝑃→𝑎𝑃𝑏| ab
𝑅→𝑎𝑅∣𝑎
𝑇→𝑎𝑇𝑎∣𝑏𝑇𝑏∣𝑎𝑎∣𝑏𝑏
CO-1   d Defining an appropriate Function like 𝑓(𝑛) = 𝑛+ 1(Unary Representation) (1   [5]
BL-2   Mark)
SO-2   Final tuples and design of Turing machine (4 Marks)
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Design of the Moore Machine – (4 Marks)
Checking the machine with a sample string – (1 Mark)
CO-3   b Recursive and Recursively Enumerable   [10]
BL-3
SO-2   There are two types of TMs (based on halting):
Recursive
- TMs that always   halt, no matter accepting or non-accepting 
DECIDABLE PROBLEMS
- Any TM for a Recursive language is going to look like this:
Recursively enumerable
- TMs that are guaranteed to halt only on acceptance. If non-accepting, it
may or may not halt (i.e., could loop forever).
- Any TM for a recursively enumerable (RE) language is going to look like
this:
********** 2 **********
--- page 3 ---
Turing Machine to find the value of log2 (n)
Recursive and Recursively Enumerable – (05 Marks)
Turing Machine Design– (05 Marks)
CO-3   c   [5]
BL-3
SO-2
Q = {0,1,2,3,4,5} ⅀ = {0,1} q0 = 0 F={5}
[3 marks DFA + 2 Marks Tuples]
Q-3
CO-2   a Proof (Using Finite Automata Construction)   [10]
BL-3   Step 1: Given (2 Mark)
SO-2   Since 𝐿1and 𝐿2are regular, there exist DFAs:
********** 3 **********
--- page 4 ---
𝑀2 = (𝑄2, Σ, 𝛿2, 𝑞2, 𝐹2)
Step 2: Construct a New DFA (4 Marks)
We construct a new DFA 𝑀 such that:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
Where:
• 𝑄= 𝑄1 × 𝑄2(Cartesian product of states)
• 𝑞0 = (𝑞1, 𝑞2)
•   Transition function:
𝛿((𝑝, 𝑞), 𝑎) = (𝛿1(𝑝, 𝑎), 𝛿2(𝑞, 𝑎))
Step 3: Define Final States (2 Marks)
For union, a string is accepted if it is accepted by either M1or M2.
So,
F = {(p, q) ∣p ∈F1 OR q ∈F2}
Step 4: Working Explanation (2 Marks)
• The new DFA simulates both machines simultaneously.
•   If either machine reaches a final state, the combined machine
accepts the string.
• Hence, it accepts all strings in:
L1 ∪L2
Step 5: Conclusion
Since we constructed a DFA for L1 ∪L2,
L1 ∪L2 is regular.
CO-3   b A Pushdown Automaton (PDA) extends a Finite Automaton by adding a stack.   [10]
BL-3,4   This single addition makes a big difference: (3 Marks)
SO-2   • Memory:
Finite Automata have only finite control (no memory of unbounded size).
PDAs have a stack, allowing them to remember an arbitrary amount of
information.
• Language class:
Finite Automata recognize regular languages.
PDAs recognize context-free languages (CFLs).
•   Capability difference:
PDAs can handle nested and matching patterns, e.g.:
o 0𝑛1𝑛
o balanced parentheses
These cannot be recognized by any finite automaton.
Let PDA be:
𝑀= (𝑄, Σ, Γ,𝛿, 𝑞0, 𝑍0, 𝐹)
Components
• 𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
• Σ = {0,1,2}
• Γ = {𝑍0, 𝑋}(Z₀ = initial stack symbol)
•   Start state = 𝑞0
•   Final state = 𝑞𝑓
δ(q₀, 0, Z₀) → (q₁, Z₀) (Reading zero)
δ(q₁, 1, Z₀) → (q₁, XZ₀)
δ(q₁, 1, X) → (q₁, XX)
δ(q₁, 0, X) → (q₂, X)
δ(q₂, 2, X) → (q₃, X)
********** 4 **********
--- page 5 ---
δ(q₃, 0, X) → (q₃, X)
δ(q₃, 1, X) → (q₃, ε) (Match 1ⁿ and pop)
δ(q₃, 0, Z₀) → (qf, Z₀)
Tuples of PDA (2 Marks)
Transition Function (5 Marks)
Q-4
CO-2   a The pumping lemma is a fundamental property of all regular languages. It is   [10]
BL-3   mainly used to prove that a language is NOT regular. (1 Mark)
SO-2   Pumping lemma states that
If L is a regular language, then there exists a constant p such that every string w ∈
L, of length p or more can be written as w = xyz, where
1.   |y| > 0
2. |xy| ≤ p
3. xyiz ∈ L for all i (2 Marks)
NO, Never use pumping lemma to prove a language regular. Pumping property is
necessary but not sufficient for regularity. (2 Marks)
The language L = { an : n is prime } is not regular.
Lets assume L is regular. Let p be the pumping length. Let q ≥ p be a prime
number (since we cannot assume that pumping length p will be prime).
Consider the string w = aa....a such that |w| = q ≥ p.
We know that w can be broken into three terms xyz such that y ≠ ε and xyiz ∈ L
⇒ xyq+1z must belong to L
⇒ |xyq+1z| must be prime
|xyq+1z| = |xyzyq|
= |xyz| + |yq|
= q + q.|y|
= q(1 + |y|) which is a composite number.
Therefore, xyq+1z cannot belong to L. Hence, L is not regular. (5 Marks)
CO-3   b   [10]
BL-3,4
SO-2
********** 5 **********
--- page 6 ---
Logic – 01 Mark
Tuples – 02 Marks
Turing Machine – 07 Marks
Q-5
CO-3   a CNF definition – 2 Marks   [10]
BL-3   GNF definition – 2 Marks
SO-2
Step 1: Eliminate terminals from long productions (2 Marks)
In CNF, productions must be of the form:
• 𝐴→𝐵𝐶 OR
• 𝐴→𝑎
So replace terminals in mixed strings.
Introduce new variables:
𝐶𝑎→𝑎, 𝐶𝑏→𝑏
Now rewrite:
𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
𝐴→𝐴𝐶𝑏∣𝑏
𝐵→𝐵𝐶𝑎∣𝑎
Step 2: Break long productions into binary form (2 Marks)
For 𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
Break stepwise:
1. Let 𝑋1 →𝐶𝑎𝐴
2. Let 𝑋2 →𝐶𝑏𝐵
Then: 𝑆→𝑋1𝑋2
Final Grammar in CNF (2 Marks)
S→X1X2
X1→CaA
X2→CbB
A→ACb∣b
B→BCa∣a
Ca→a
Cb→b
********** 6 **********
--- page 7 ---
CO-3   b   [10]
BL-3,4
SO-2
Mealy Machine design – 6 Marks
Tuples – 2 Marks
Sample String verification – 2 Marks
Q-6
CO-2   a   [10]
BL-3,4
SO-2   LMD:   RMD:
S ⇒aSc   S⇒aSc
⇒aaScc   ⇒aaScc
⇒aabSdcc   ⇒aabSdcc
⇒aabbSddcc   ⇒aabbSddcc
⇒aabbTddcc   ⇒aabbTddcc
⇒aabbeTfddcc   ⇒aabbeTfddcc
⇒aabbeeTffddcc   ⇒aabbeeTffddcc
⇒aabbeeeTfffddcc   ⇒aabbeeeTfffddcc
⇒aabbeeefffddcc   ⇒aabbeeefffddcc
LMD + Parse Tree– (3 +2 Marks)
RMD + Parse Tree – (3+2 Marks)
CO-2   b   [5]
BL-3
SO-2
Design of the PDA – (3 Marks)
Verification of the string – (2 Marks)
********** 7 **********
--- page 8 ---
CO-1   c   Difference between Formal Grammar and Formal Language (2.5 Marks)   [5]
BL-2
SO-2   Feature   Formal Grammar   Formal Language
A set of rules used to generate A set of strings formed using
Definition
strings   symbols
(G = (V, T, P, S)) where rules   Represents all possible strings
Components
define generation   over alphabet
Nature   Generative mechanism   Result/output of grammar
Describes how strings are   Describes what strings are
Purpose
formed   valid
Example   S → aS   b
Difference between Empty String (ε) and Empty Set (∅) (2.5 Marks)
Feature   Empty String (ε)   Empty Set (∅)
Definition   A string with no symbols A set with no elements
Type   String   Set
Length   Length = 0   Not applicable
Belongs to language? Yes, can be an element No elements at all
Example   ε ∈ {ε, a, aa}   ∅ has no elements
Q-7
CO-2,3   a   [10]
BL-3   Limitations of Finite Automata – (2 Marks)
SO-2   1.No Memory (Beyond Finite States) - No Auxiliary Storage.
2. Cannot Handle Matching or Nesting
3.FSM recognizes only regular languages.
4. Limited Computational Power
Minimization of DFA –
Equivalences – (4 Marks)
0 equivalence ={{q4} ,{q1,q2,q3,q5,q6,q7,q8}}
1 equivalence ={{q4} ,{q1,q2,q6,q7},{q3,q5},{q8}}
2 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
3 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
The minimum state automata is reached and is given by:
Q’ = {{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}(1 Mark tuples)
q1’= [q1,q7] initial state
F’ = {q4} final state
Transition Table (2 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
********** 8 **********
--- page 9 ---
[q4] (final state)   [q4]   [q1,q7]
[q8]   [q1,q7]   [q4]
As [q8] is unreachable from initial state so the final table is: (1 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
[q4] (final state)   [q4]   [q1,q7]
CO-1   b Definition along with tuples– (2 Marks)   [5]
BL-2   A formal grammar is a mathematical model used to describe how strings in a
SO-2   language are formed.
A grammar is defined as:
𝐺= (𝑉, 𝑇, 𝑃, 𝑆)
where:
• V → set of variables (non-terminals)
• T → set of terminals
• P → set of production rules
• S → start symbol
Example of Grammar   (1 Mark)
𝑆→𝑎𝑆∣𝑏
This grammar generates strings like:
b, ab, aab, aaab, …
Difference between Terminals and non-terminals (2 Marks)
Feature   Terminals   Non-terminals
Symbols that form the final Symbols used to generate
Definition
strings   strings
Can be replaced using
Role   Cannot be replaced further
production rules
Lowercase letters, digits,
Representation   Uppercase letters
symbols
Appear in
Yes   No
output?
Example   a, b, 0, 1   S, A, B
CO-3   c A Non-deterministic Pushdown Automaton (NPDA) is an extension of a finite   [5]
BL-3   automaton with a stack memory. It can have multiple possible moves for the same
SO-2   input, stack symbol, and state.
NPDA is defined as: (Q, Σ, Γ, δ, q₀, Z₀, F)
· Q: Set of states
· Σ: Input symbols
· Γ: Stack symbols
· δ: Transition function
· q₀: Start state
********** 9 **********
--- page 10 ---
· Z₀: Initial stack symbol
· F: Final states
The NPDA can choose between multiple possible moves at any step (non-
determinism). It may:
• Push symbols onto the stack
• Pop symbols from the stack
•   Ignore input using ε-transitions
(3 Marks)
Specific Example of language (2 Marks)
Consider the language:
𝐿= {𝑤𝑤𝑅∣𝑤∈{𝑎, 𝑏}∗}
(i.e., palindromes)
Deterministic PDA (DPDA) Fails in this scenario
• A DPDA cannot determine the middle of the string.
•   It does not know when to stop pushing and start popping.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 89327407226c

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_Computer_7047/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C058)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   In Formal Language Theory, a string is a finite sequence of symbols chosen from   [5]
BL-2   a given alphabet. (2 Marks)
SO-2   •   Alphabet: Σ = {a, b}
• Examples of strings: a, b, ab, ba, aab
• The empty string is denoted by ε and has length 0
All strings of length ≤ 3: (2 Marks)
{ ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb }
Strings belonging to L: (1 Mark)
{ ab, aab, abb }
CO-2   b   [5]
BL-2   i) Language- (2 Mark)
SO-2   (010)* - All strings that consist of zero or more repetitions of the substring “010”.
(0*10*)* - L is the set of all strings over the alphabet {0,1} that are formed by
concatenating zero or more blocks, where each block contains exactly one ‘1’
surrounded by any number of ‘0’s.
ii) Key Property of the recognized language- (2 Marks)
(010)*- Here pattern is strictly repeated and Length of the string is always a
multiple of 3
(0*10*)* - Every non-empty string in the language must contain at least one 1.
iii)Example –(1 Mark)
(e.g) (010)*- 010010 , 010010010
(0*10*)* - 1001,1010
CO-3   c A nullable variable in a Context-Free Grammar (CFG) is a variable that can   [5]
BL-2,3   derive the empty string 𝜖.
SO-2   𝐴⇒∗𝜖
********** 1 **********
--- page 2 ---
That is, if a variable can produce 𝜖 either directly or through a sequence of
productions, it is called nullable. (1 Mark)
For the given grammar two non-terminals are nullable P and T
Elimination of 𝜖 productions (4 Marks)
The nullable variables are P and T
Hence after removing 𝜖 productions , grammar takes the form
𝑆→PPRT∣PRT∣RT∣PPR∣PR∣R
𝑃→𝑎𝑃𝑏| ab
𝑅→𝑎𝑅∣𝑎
𝑇→𝑎𝑇𝑎∣𝑏𝑇𝑏∣𝑎𝑎∣𝑏𝑏
CO-1   d Defining an appropriate Function like 𝑓(𝑛) = 𝑛+ 1(Unary Representation) (1   [5]
BL-2   Mark)
SO-2   Final tuples and design of Turing machine (4 Marks)
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Design of the Moore Machine – (4 Marks)
Checking the machine with a sample string – (1 Mark)
CO-3   b Recursive and Recursively Enumerable   [10]
BL-3
SO-2   There are two types of TMs (based on halting):
Recursive
- TMs that always   halt, no matter accepting or non-accepting 
DECIDABLE PROBLEMS
- Any TM for a Recursive language is going to look like this:
Recursively enumerable
- TMs that are guaranteed to halt only on acceptance. If non-accepting, it
may or may not halt (i.e., could loop forever).
- Any TM for a recursively enumerable (RE) language is going to look like
this:
********** 2 **********
--- page 3 ---
Turing Machine to find the value of log2 (n)
Recursive and Recursively Enumerable – (05 Marks)
Turing Machine Design– (05 Marks)
CO-3   c   [5]
BL-3
SO-2
Q = {0,1,2,3,4,5} ⅀ = {0,1} q0 = 0 F={5}
[3 marks DFA + 2 Marks Tuples]
Q-3
CO-2   a Proof (Using Finite Automata Construction)   [10]
BL-3   Step 1: Given (2 Mark)
SO-2   Since 𝐿1and 𝐿2are regular, there exist DFAs:
********** 3 **********
--- page 4 ---
𝑀2 = (𝑄2, Σ, 𝛿2, 𝑞2, 𝐹2)
Step 2: Construct a New DFA (4 Marks)
We construct a new DFA 𝑀 such that:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
Where:
• 𝑄= 𝑄1 × 𝑄2(Cartesian product of states)
• 𝑞0 = (𝑞1, 𝑞2)
•   Transition function:
𝛿((𝑝, 𝑞), 𝑎) = (𝛿1(𝑝, 𝑎), 𝛿2(𝑞, 𝑎))
Step 3: Define Final States (2 Marks)
For union, a string is accepted if it is accepted by either M1or M2.
So,
F = {(p, q) ∣p ∈F1 OR q ∈F2}
Step 4: Working Explanation (2 Marks)
• The new DFA simulates both machines simultaneously.
•   If either machine reaches a final state, the combined machine
accepts the string.
• Hence, it accepts all strings in:
L1 ∪L2
Step 5: Conclusion
Since we constructed a DFA for L1 ∪L2,
L1 ∪L2 is regular.
CO-3   b A Pushdown Automaton (PDA) extends a Finite Automaton by adding a stack.   [10]
BL-3,4   This single addition makes a big difference: (3 Marks)
SO-2   • Memory:
Finite Automata have only finite control (no memory of unbounded size).
PDAs have a stack, allowing them to remember an arbitrary amount of
information.
• Language class:
Finite Automata recognize regular languages.
PDAs recognize context-free languages (CFLs).
•   Capability difference:
PDAs can handle nested and matching patterns, e.g.:
o 0𝑛1𝑛
o balanced parentheses
These cannot be recognized by any finite automaton.
Let PDA be:
𝑀= (𝑄, Σ, Γ,𝛿, 𝑞0, 𝑍0, 𝐹)
Components
• 𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
• Σ = {0,1,2}
• Γ = {𝑍0, 𝑋}(Z₀ = initial stack symbol)
•   Start state = 𝑞0
•   Final state = 𝑞𝑓
δ(q₀, 0, Z₀) → (q₁, Z₀) (Reading zero)
δ(q₁, 1, Z₀) → (q₁, XZ₀)
δ(q₁, 1, X) → (q₁, XX)
δ(q₁, 0, X) → (q₂, X)
δ(q₂, 2, X) → (q₃, X)
********** 4 **********
--- page 5 ---
δ(q₃, 0, X) → (q₃, X)
δ(q₃, 1, X) → (q₃, ε) (Match 1ⁿ and pop)
δ(q₃, 0, Z₀) → (qf, Z₀)
Tuples of PDA (2 Marks)
Transition Function (5 Marks)
Q-4
CO-2   a The pumping lemma is a fundamental property of all regular languages. It is   [10]
BL-3   mainly used to prove that a language is NOT regular. (1 Mark)
SO-2   Pumping lemma states that
If L is a regular language, then there exists a constant p such that every string w ∈
L, of length p or more can be written as w = xyz, where
1.   |y| > 0
2. |xy| ≤ p
3. xyiz ∈ L for all i (2 Marks)
NO, Never use pumping lemma to prove a language regular. Pumping property is
necessary but not sufficient for regularity. (2 Marks)
The language L = { an : n is prime } is not regular.
Lets assume L is regular. Let p be the pumping length. Let q ≥ p be a prime
number (since we cannot assume that pumping length p will be prime).
Consider the string w = aa....a such that |w| = q ≥ p.
We know that w can be broken into three terms xyz such that y ≠ ε and xyiz ∈ L
⇒ xyq+1z must belong to L
⇒ |xyq+1z| must be prime
|xyq+1z| = |xyzyq|
= |xyz| + |yq|
= q + q.|y|
= q(1 + |y|) which is a composite number.
Therefore, xyq+1z cannot belong to L. Hence, L is not regular. (5 Marks)
CO-3   b   [10]
BL-3,4
SO-2
********** 5 **********
--- page 6 ---
Logic – 01 Mark
Tuples – 02 Marks
Turing Machine – 07 Marks
Q-5
CO-3   a CNF definition – 2 Marks   [10]
BL-3   GNF definition – 2 Marks
SO-2
Step 1: Eliminate terminals from long productions (2 Marks)
In CNF, productions must be of the form:
• 𝐴→𝐵𝐶 OR
• 𝐴→𝑎
So replace terminals in mixed strings.
Introduce new variables:
𝐶𝑎→𝑎, 𝐶𝑏→𝑏
Now rewrite:
𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
𝐴→𝐴𝐶𝑏∣𝑏
𝐵→𝐵𝐶𝑎∣𝑎
Step 2: Break long productions into binary form (2 Marks)
For 𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
Break stepwise:
1. Let 𝑋1 →𝐶𝑎𝐴
2. Let 𝑋2 →𝐶𝑏𝐵
Then: 𝑆→𝑋1𝑋2
Final Grammar in CNF (2 Marks)
S→X1X2
X1→CaA
X2→CbB
A→ACb∣b
B→BCa∣a
Ca→a
Cb→b
********** 6 **********
--- page 7 ---
CO-3   b   [10]
BL-3,4
SO-2
Mealy Machine design – 6 Marks
Tuples – 2 Marks
Sample String verification – 2 Marks
Q-6
CO-2   a   [10]
BL-3,4
SO-2   LMD:   RMD:
S ⇒aSc   S⇒aSc
⇒aaScc   ⇒aaScc
⇒aabSdcc   ⇒aabSdcc
⇒aabbSddcc   ⇒aabbSddcc
⇒aabbTddcc   ⇒aabbTddcc
⇒aabbeTfddcc   ⇒aabbeTfddcc
⇒aabbeeTffddcc   ⇒aabbeeTffddcc
⇒aabbeeeTfffddcc   ⇒aabbeeeTfffddcc
⇒aabbeeefffddcc   ⇒aabbeeefffddcc
LMD + Parse Tree– (3 +2 Marks)
RMD + Parse Tree – (3+2 Marks)
CO-2   b   [5]
BL-3
SO-2
Design of the PDA – (3 Marks)
Verification of the string – (2 Marks)
********** 7 **********
--- page 8 ---
CO-1   c   Difference between Formal Grammar and Formal Language (2.5 Marks)   [5]
BL-2
SO-2   Feature   Formal Grammar   Formal Language
A set of rules used to generate A set of strings formed using
Definition
strings   symbols
(G = (V, T, P, S)) where rules   Represents all possible strings
Components
define generation   over alphabet
Nature   Generative mechanism   Result/output of grammar
Describes how strings are   Describes what strings are
Purpose
formed   valid
Example   S → aS   b
Difference between Empty String (ε) and Empty Set (∅) (2.5 Marks)
Feature   Empty String (ε)   Empty Set (∅)
Definition   A string with no symbols A set with no elements
Type   String   Set
Length   Length = 0   Not applicable
Belongs to language? Yes, can be an element No elements at all
Example   ε ∈ {ε, a, aa}   ∅ has no elements
Q-7
CO-2,3   a   [10]
BL-3   Limitations of Finite Automata – (2 Marks)
SO-2   1.No Memory (Beyond Finite States) - No Auxiliary Storage.
2. Cannot Handle Matching or Nesting
3.FSM recognizes only regular languages.
4. Limited Computational Power
Minimization of DFA –
Equivalences – (4 Marks)
0 equivalence ={{q4} ,{q1,q2,q3,q5,q6,q7,q8}}
1 equivalence ={{q4} ,{q1,q2,q6,q7},{q3,q5},{q8}}
2 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
3 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
The minimum state automata is reached and is given by:
Q’ = {{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}(1 Mark tuples)
q1’= [q1,q7] initial state
F’ = {q4} final state
Transition Table (2 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
********** 8 **********
--- page 9 ---
[q4] (final state)   [q4]   [q1,q7]
[q8]   [q1,q7]   [q4]
As [q8] is unreachable from initial state so the final table is: (1 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
[q4] (final state)   [q4]   [q1,q7]
CO-1   b Definition along with tuples– (2 Marks)   [5]
BL-2   A formal grammar is a mathematical model used to describe how strings in a
SO-2   language are formed.
A grammar is defined as:
𝐺= (𝑉, 𝑇, 𝑃, 𝑆)
where:
• V → set of variables (non-terminals)
• T → set of terminals
• P → set of production rules
• S → start symbol
Example of Grammar   (1 Mark)
𝑆→𝑎𝑆∣𝑏
This grammar generates strings like:
b, ab, aab, aaab, …
Difference between Terminals and non-terminals (2 Marks)
Feature   Terminals   Non-terminals
Symbols that form the final Symbols used to generate
Definition
strings   strings
Can be replaced using
Role   Cannot be replaced further
production rules
Lowercase letters, digits,
Representation   Uppercase letters
symbols
Appear in
Yes   No
output?
Example   a, b, 0, 1   S, A, B
CO-3   c A Non-deterministic Pushdown Automaton (NPDA) is an extension of a finite   [5]
BL-3   automaton with a stack memory. It can have multiple possible moves for the same
SO-2   input, stack symbol, and state.
NPDA is defined as: (Q, Σ, Γ, δ, q₀, Z₀, F)
· Q: Set of states
· Σ: Input symbols
· Γ: Stack symbols
· δ: Transition function
· q₀: Start state
********** 9 **********
--- page 10 ---
· Z₀: Initial stack symbol
· F: Final states
The NPDA can choose between multiple possible moves at any step (non-
determinism). It may:
• Push symbols onto the stack
• Pop symbols from the stack
•   Ignore input using ε-transitions
(3 Marks)
Specific Example of language (2 Marks)
Consider the language:
𝐿= {𝑤𝑤𝑅∣𝑤∈{𝑎, 𝑏}∗}
(i.e., palindromes)
Deterministic PDA (DPDA) Fails in this scenario
• A DPDA cannot determine the middle of the string.
•   It does not know when to stop pushing and start popping.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 6673f2237508

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_Computer_7032/Theoretical Computer Science/ANS_Theoretical Computer Science(702CO0C011)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Theoretical Computer Science
Date: 10 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q-1
CO-1   a   In Formal Language Theory, a string is a finite sequence of symbols chosen from   [5]
BL-2   a given alphabet. (2 Marks)
SO-2   •   Alphabet: Σ = {a, b}
• Examples of strings: a, b, ab, ba, aab
• The empty string is denoted by ε and has length 0
All strings of length ≤ 3: (2 Marks)
{ ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb }
Strings belonging to L: (1 Mark)
{ ab, aab, abb }
CO-2   b   [5]
BL-2   i) Language- (2 Mark)
SO-2   (010)* - All strings that consist of zero or more repetitions of the substring “010”.
(0*10*)* - L is the set of all strings over the alphabet {0,1} that are formed by
concatenating zero or more blocks, where each block contains exactly one ‘1’
surrounded by any number of ‘0’s.
ii) Key Property of the recognized language- (2 Marks)
(010)*- Here pattern is strictly repeated and Length of the string is always a
multiple of 3
(0*10*)* - Every non-empty string in the language must contain at least one 1.
iii)Example –(1 Mark)
(e.g) (010)*- 010010 , 010010010
(0*10*)* - 1001,1010
CO-3   c A nullable variable in a Context-Free Grammar (CFG) is a variable that can   [5]
BL-2,3   derive the empty string 𝜖.
SO-2   𝐴⇒∗𝜖
********** 1 **********
--- page 2 ---
That is, if a variable can produce 𝜖 either directly or through a sequence of
productions, it is called nullable. (1 Mark)
For the given grammar two non-terminals are nullable P and T
Elimination of 𝜖 productions (4 Marks)
The nullable variables are P and T
Hence after removing 𝜖 productions , grammar takes the form
𝑆→PPRT∣PRT∣RT∣PPR∣PR∣R
𝑃→𝑎𝑃𝑏| ab
𝑅→𝑎𝑅∣𝑎
𝑇→𝑎𝑇𝑎∣𝑏𝑇𝑏∣𝑎𝑎∣𝑏𝑏
CO-1   d Defining an appropriate Function like 𝑓(𝑛) = 𝑛+ 1(Unary Representation) (1   [5]
BL-2   Mark)
SO-2   Final tuples and design of Turing machine (4 Marks)
Q-2
CO-3   a   [5]
BL-3,4
SO-2
Design of the Moore Machine – (4 Marks)
Checking the machine with a sample string – (1 Mark)
CO-3   b Recursive and Recursively Enumerable   [10]
BL-3
SO-2   There are two types of TMs (based on halting):
Recursive
- TMs that always   halt, no matter accepting or non-accepting 
DECIDABLE PROBLEMS
- Any TM for a Recursive language is going to look like this:
Recursively enumerable
- TMs that are guaranteed to halt only on acceptance. If non-accepting, it
may or may not halt (i.e., could loop forever).
- Any TM for a recursively enumerable (RE) language is going to look like
this:
********** 2 **********
--- page 3 ---
Turing Machine to find the value of log2 (n)
Recursive and Recursively Enumerable – (05 Marks)
Turing Machine Design– (05 Marks)
CO-3   c   [5]
BL-3
SO-2
Q = {0,1,2,3,4,5} ⅀ = {0,1} q0 = 0 F={5}
[3 marks DFA + 2 Marks Tuples]
Q-3
CO-2   a Proof (Using Finite Automata Construction)   [10]
BL-3   Step 1: Given (2 Mark)
SO-2   Since 𝐿1and 𝐿2are regular, there exist DFAs:
********** 3 **********
--- page 4 ---
𝑀2 = (𝑄2, Σ, 𝛿2, 𝑞2, 𝐹2)
Step 2: Construct a New DFA (4 Marks)
We construct a new DFA 𝑀 such that:
𝑀= (𝑄, Σ, 𝛿, 𝑞0, 𝐹)
Where:
• 𝑄= 𝑄1 × 𝑄2(Cartesian product of states)
• 𝑞0 = (𝑞1, 𝑞2)
•   Transition function:
𝛿((𝑝, 𝑞), 𝑎) = (𝛿1(𝑝, 𝑎), 𝛿2(𝑞, 𝑎))
Step 3: Define Final States (2 Marks)
For union, a string is accepted if it is accepted by either M1or M2.
So,
F = {(p, q) ∣p ∈F1 OR q ∈F2}
Step 4: Working Explanation (2 Marks)
• The new DFA simulates both machines simultaneously.
•   If either machine reaches a final state, the combined machine
accepts the string.
• Hence, it accepts all strings in:
L1 ∪L2
Step 5: Conclusion
Since we constructed a DFA for L1 ∪L2,
L1 ∪L2 is regular.
CO-3   b A Pushdown Automaton (PDA) extends a Finite Automaton by adding a stack.   [10]
BL-3,4   This single addition makes a big difference: (3 Marks)
SO-2   • Memory:
Finite Automata have only finite control (no memory of unbounded size).
PDAs have a stack, allowing them to remember an arbitrary amount of
information.
• Language class:
Finite Automata recognize regular languages.
PDAs recognize context-free languages (CFLs).
•   Capability difference:
PDAs can handle nested and matching patterns, e.g.:
o 0𝑛1𝑛
o balanced parentheses
These cannot be recognized by any finite automaton.
Let PDA be:
𝑀= (𝑄, Σ, Γ,𝛿, 𝑞0, 𝑍0, 𝐹)
Components
• 𝑄= {𝑞0, 𝑞1, 𝑞2, 𝑞3, 𝑞𝑓}
• Σ = {0,1,2}
• Γ = {𝑍0, 𝑋}(Z₀ = initial stack symbol)
•   Start state = 𝑞0
•   Final state = 𝑞𝑓
δ(q₀, 0, Z₀) → (q₁, Z₀) (Reading zero)
δ(q₁, 1, Z₀) → (q₁, XZ₀)
δ(q₁, 1, X) → (q₁, XX)
δ(q₁, 0, X) → (q₂, X)
δ(q₂, 2, X) → (q₃, X)
********** 4 **********
--- page 5 ---
δ(q₃, 0, X) → (q₃, X)
δ(q₃, 1, X) → (q₃, ε) (Match 1ⁿ and pop)
δ(q₃, 0, Z₀) → (qf, Z₀)
Tuples of PDA (2 Marks)
Transition Function (5 Marks)
Q-4
CO-2   a The pumping lemma is a fundamental property of all regular languages. It is   [10]
BL-3   mainly used to prove that a language is NOT regular. (1 Mark)
SO-2   Pumping lemma states that
If L is a regular language, then there exists a constant p such that every string w ∈
L, of length p or more can be written as w = xyz, where
1.   |y| > 0
2. |xy| ≤ p
3. xyiz ∈ L for all i (2 Marks)
NO, Never use pumping lemma to prove a language regular. Pumping property is
necessary but not sufficient for regularity. (2 Marks)
The language L = { an : n is prime } is not regular.
Lets assume L is regular. Let p be the pumping length. Let q ≥ p be a prime
number (since we cannot assume that pumping length p will be prime).
Consider the string w = aa....a such that |w| = q ≥ p.
We know that w can be broken into three terms xyz such that y ≠ ε and xyiz ∈ L
⇒ xyq+1z must belong to L
⇒ |xyq+1z| must be prime
|xyq+1z| = |xyzyq|
= |xyz| + |yq|
= q + q.|y|
= q(1 + |y|) which is a composite number.
Therefore, xyq+1z cannot belong to L. Hence, L is not regular. (5 Marks)
CO-3   b   [10]
BL-3,4
SO-2
********** 5 **********
--- page 6 ---
Logic – 01 Mark
Tuples – 02 Marks
Turing Machine – 07 Marks
Q-5
CO-3   a CNF definition – 2 Marks   [10]
BL-3   GNF definition – 2 Marks
SO-2
Step 1: Eliminate terminals from long productions (2 Marks)
In CNF, productions must be of the form:
• 𝐴→𝐵𝐶 OR
• 𝐴→𝑎
So replace terminals in mixed strings.
Introduce new variables:
𝐶𝑎→𝑎, 𝐶𝑏→𝑏
Now rewrite:
𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
𝐴→𝐴𝐶𝑏∣𝑏
𝐵→𝐵𝐶𝑎∣𝑎
Step 2: Break long productions into binary form (2 Marks)
For 𝑆→𝐶𝑎𝐴𝐶𝑏𝐵
Break stepwise:
1. Let 𝑋1 →𝐶𝑎𝐴
2. Let 𝑋2 →𝐶𝑏𝐵
Then: 𝑆→𝑋1𝑋2
Final Grammar in CNF (2 Marks)
S→X1X2
X1→CaA
X2→CbB
A→ACb∣b
B→BCa∣a
Ca→a
Cb→b
********** 6 **********
--- page 7 ---
CO-3   b   [10]
BL-3,4
SO-2
Mealy Machine design – 6 Marks
Tuples – 2 Marks
Sample String verification – 2 Marks
Q-6
CO-2   a   [10]
BL-3,4
SO-2   LMD:   RMD:
S ⇒aSc   S⇒aSc
⇒aaScc   ⇒aaScc
⇒aabSdcc   ⇒aabSdcc
⇒aabbSddcc   ⇒aabbSddcc
⇒aabbTddcc   ⇒aabbTddcc
⇒aabbeTfddcc   ⇒aabbeTfddcc
⇒aabbeeTffddcc   ⇒aabbeeTffddcc
⇒aabbeeeTfffddcc   ⇒aabbeeeTfffddcc
⇒aabbeeefffddcc   ⇒aabbeeefffddcc
LMD + Parse Tree– (3 +2 Marks)
RMD + Parse Tree – (3+2 Marks)
CO-2   b   [5]
BL-3
SO-2
Design of the PDA – (3 Marks)
Verification of the string – (2 Marks)
********** 7 **********
--- page 8 ---
CO-1   c   Difference between Formal Grammar and Formal Language (2.5 Marks)   [5]
BL-2
SO-2   Feature   Formal Grammar   Formal Language
A set of rules used to generate A set of strings formed using
Definition
strings   symbols
(G = (V, T, P, S)) where rules   Represents all possible strings
Components
define generation   over alphabet
Nature   Generative mechanism   Result/output of grammar
Describes how strings are   Describes what strings are
Purpose
formed   valid
Example   S → aS   b
Difference between Empty String (ε) and Empty Set (∅) (2.5 Marks)
Feature   Empty String (ε)   Empty Set (∅)
Definition   A string with no symbols A set with no elements
Type   String   Set
Length   Length = 0   Not applicable
Belongs to language? Yes, can be an element No elements at all
Example   ε ∈ {ε, a, aa}   ∅ has no elements
Q-7
CO-2,3   a   [10]
BL-3   Limitations of Finite Automata – (2 Marks)
SO-2   1.No Memory (Beyond Finite States) - No Auxiliary Storage.
2. Cannot Handle Matching or Nesting
3.FSM recognizes only regular languages.
4. Limited Computational Power
Minimization of DFA –
Equivalences – (4 Marks)
0 equivalence ={{q4} ,{q1,q2,q3,q5,q6,q7,q8}}
1 equivalence ={{q4} ,{q1,q2,q6,q7},{q3,q5},{q8}}
2 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
3 equivalence ={{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}
The minimum state automata is reached and is given by:
Q’ = {{q4} ,{q1,q7},{q2,q6},{q3,q5},{q8}}(1 Mark tuples)
q1’= [q1,q7] initial state
F’ = {q4} final state
Transition Table (2 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
********** 8 **********
--- page 9 ---
[q4] (final state)   [q4]   [q1,q7]
[q8]   [q1,q7]   [q4]
As [q8] is unreachable from initial state so the final table is: (1 Marks)
Present State   Next State
a   b
[q1,q7](start state)   [q2,q6]   [q1,q7]
[q2,q6]   [q1,q7]   [q3,q5]
[q3,q5]   [q4]   [q2,q6]
[q4] (final state)   [q4]   [q1,q7]
CO-1   b Definition along with tuples– (2 Marks)   [5]
BL-2   A formal grammar is a mathematical model used to describe how strings in a
SO-2   language are formed.
A grammar is defined as:
𝐺= (𝑉, 𝑇, 𝑃, 𝑆)
where:
• V → set of variables (non-terminals)
• T → set of terminals
• P → set of production rules
• S → start symbol
Example of Grammar   (1 Mark)
𝑆→𝑎𝑆∣𝑏
This grammar generates strings like:
b, ab, aab, aaab, …
Difference between Terminals and non-terminals (2 Marks)
Feature   Terminals   Non-terminals
Symbols that form the final Symbols used to generate
Definition
strings   strings
Can be replaced using
Role   Cannot be replaced further
production rules
Lowercase letters, digits,
Representation   Uppercase letters
symbols
Appear in
Yes   No
output?
Example   a, b, 0, 1   S, A, B
CO-3   c A Non-deterministic Pushdown Automaton (NPDA) is an extension of a finite   [5]
BL-3   automaton with a stack memory. It can have multiple possible moves for the same
SO-2   input, stack symbol, and state.
NPDA is defined as: (Q, Σ, Γ, δ, q₀, Z₀, F)
· Q: Set of states
· Σ: Input symbols
· Γ: Stack symbols
· δ: Transition function
· q₀: Start state
********** 9 **********
--- page 10 ---
· Z₀: Initial stack symbol
· F: Final states
The NPDA can choose between multiple possible moves at any step (non-
determinism). It may:
• Push symbols onto the stack
• Pop symbols from the stack
•   Ignore input using ε-transitions
(3 Marks)
Specific Example of language (2 Marks)
Consider the language:
𝐿= {𝑤𝑤𝑅∣𝑤∈{𝑎, 𝑏}∗}
(i.e., palindromes)
Deterministic PDA (DPDA) Fails in this scenario
• A DPDA cannot determine the middle of the string.
•   It does not know when to stop pushing and start popping.
********** 10 **********
````
