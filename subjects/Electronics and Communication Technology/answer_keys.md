# Electronics and Communication Technology: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 93204484d05d

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Electronics And Communication Technology/ANS_Final-Exam_Electronics And Communication Technology(NHECT168)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 16 Mar 2026
- Text: text (8 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Electronics And Communication Technology
Date: 16 Mar 2026   Time: 08:00 am - 09:00 am (01:00 Hrs.)
Max Marks: 30
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 8 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Assume suitable data wherever required.
5. Draw diagrams wherever necessary.
1.   Answer the following(Attempt Any 2 Questions)   10
a.   5
Feature   Analog   Digital
Signal Type   Continuous   Discrete
Representation   Infinite values   Two levels (0 and 1)
Examples   Microphone, radio   Computer, calculator
Circuits   Amplifiers, filters   Logic gates, microcontrollers
Noise Sensitivity   High   Low
b.   5
1) Octal Addition 657 8 +345 8   (2 marks)
Steps:
7 + 5 = 128 → write 4, carry 1
5 + 4 + 1 = 108 → write 2, carry 1
Page 1 of 8
--- page 2 ---
6 + 3 + 1 = 128 → write 2, carry 1
Answer: 12248
2) Hexadecimal Addition 𝐴7 16 + 3𝐶 16 (2 marks)
Steps:
7 + C(12) = 19 → write 3, carry 1
A(10) + 3 + 1 = 14 → E
Answer: 𝐸3 16
3) 15’s Complement of 23 16 (1 mark)
Step 1: Find 15’s complement
Subtract each digit from F: 2 → F−2 = D 3 → F−3 = C
15’s complement = DC
Answer: DC 16
c. 1M each point   5
1. Meaning of Self-Complementing Property Excess-3 (XS-3) is a non-weighted decimal
code obtained by adding 3 (0011) to the BCD representation of each decimal digit. One of
its most important characteristics is its self-complementing property, which simplifies
decimal subtraction in digital systems. A code is self-complementing if the 1’s
complement of the code represents the 9’s complement of the decimal digit. In Excess-3,
taking the bitwise complement automatically produces the complement needed for
subtraction.
2. How the Property Works
i. Decimal digit → convert to Excess-3
ii. Take 1’s complement of the Excess-3 code
iii. Result corresponds to 9’s complement of the original decimal digit
3. Example
Decimal digit = 4
BCD = 0100
Excess-3 = 0100 + 0011 = 0111
1’s complement of 0111 → 1000
Decimal value of 1000 (Excess-3) = 5
Since 9 – 4 = 5, the complement is correct.
4. Simplifies Decimal Subtraction
In decimal subtraction using complements, normally requires finding 9’s complement.
With Excess-3, simply take 1’s complement, this reduces hardware complexity and
improves efficiency.
5. Importance in Digital Systems
Simplifies arithmetic circuit design
Reduces subtraction logic complexity
Page 2 of 8
--- page 3 ---
Useful in decimal arithmetic circuits and legacy digital systems
2.   Answer the following(Attempt Any 2 Questions)   10
a.   5
Marks:
a) Binary to Gray - 2.5
b) Gray to Binary - 2.5
b.   5
A Demultiplexer (DEMUX) is a combinational logic circuit that takes one input signal and
distributes it to one of several output lines based on the values of the select lines. It acts as a
data distributor, performing the reverse operation of a multiplexer. (1 mark)
1:4 Demultiplexer (Explanation of 1:4 DEMUX concept - 1 mark)
Page 3 of 8

[Text in pictures on this page, read by OCR]
(A) Convert (11010)2 to Gray Code
Rules:
1. The MSB of Gray code = MSB of binary.
2. Each next Gray bit = XOR of current binary bit with previous binary bit.
Binary: 11010
Steps:
e MSB same — 1
« 1@1=0
e 1@0=1
e 0@1=1
e 1@0=1

Gray Code = 10111

(B) Convert (010011) Gray Code to Binary
Rules:

1. The MSB of binary = MSB of Gray code.

2. Each next binary bit = Previous binary bit ® current Gray bit.
Gray:010011
Steps:

e MSB same — 0

e O@G1=1

e« 1@0=1

« 1@0=1

« 1@1=0

e 0@1=1

Binary = 011101
--- page 4 ---
1:4 DEMUX routes a single data input to one of four outputs depending on the select line
values.
Inputs and Outputs
Data input: I
Select lines: S1, S0
Outputs: Y0, Y1, Y2, Y3
2
Since there are 2 select lines → 2 = 4 outputs.
(Diagram - 1 mark)
Truth Table (1 mark)
S1 S0 Y0 Y1 Y2 Y3
0   0   I   0   0   0
0   1   0   I   0   0
1   0   0   0   I   0
1   1   0   0   0   I
Working (1 mark)
When S1S0 = 00, input I goes to Y0
When S1S0 = 01, input I goes to Y1
When S1S0 = 10, input I goes to Y2
When S1S0 = 11, input I goes to Y3
Only one output line is active at a time.
c.   5
Page 4 of 8
--- page 5 ---
Full Subtractor is a combinational logic circuit used to subtract three binary bits: A →
Minuend, B → Subtrahend, Bin → Borrow input (from previous stage) It produces two
outputs: Difference (D) Borrow out (Bout) Unlike a half subtractor, it considers the borrow
from the previous stage, making it suitable for multi-bit subtraction. (Definition - 1 mark)
Working Principle
The full subtractor performs subtraction including borrow handling.
If A ≥ (B + Bin) → subtraction occurs normally.
If A < (B + Bin) → borrow is generated.
Boolean Expressions
D = A \oplus B \oplus Bin
Bout = \overline{A}B + \overline{A}Bin + B \cdot Bin
(Working principle & Boolean expressions - 1 mark)
Truth Table (1 mark)
A B Bin Difference (D) Borrow (Bout)
0 0 0   0   0
0 0 1   1   1
0 1 0   1   1
0 1 1   0   1
1 0 0   1   0
1 0 1   0   0
1 1 0   0   0
1 1 1   1   1
Advantages (1 mark)
Handles borrow input from previous stage
Suitable for multi-bit binary subtraction
Provides accurate subtraction in sequential stages
Used in processors and digital arithmetic circuits
Disadvantages (1 mark)
Page 5 of 8
--- page 6 ---
More complex circuit than half subtractor
Requires more logic gates and hardware
Higher propagation delay compared to half subtractor
Increased power consumption due to additional components
3.   Answer the following(Attempt Any 2 Questions)   10
a.   5
T (Toggle) Flip-Flop is a sequential logic circuit that has one input (T) and a clock input. It
changes its output state based on the value of the T input when the clock pulse is applied. It is
derived from the J–K flip-flop by connecting J and K inputs together, forming a single input T.
Operation of T Flip-Flop
T Present Output Qₙ Next Output Qₙ₊₁ Operation
0 Qₙ   Qₙ   No change
1 0   1   Toggle
1 1   0   Toggle
Characteristic Equation:
Q_{n+1} = Q_n \oplus T
Why It is Called a Toggle Flip-Flop
The T flip-flop is called a Toggle flip-flop because: When T = 1, the output switches (toggles)
to the opposite state on each clock pulse. When T = 0, the output remains unchanged. Example
(T = 1): 0 → 1 → 0 → 1 → 0 → 1 … Thus, it alternates between 0 and 1, which is known as
toggling.
Working Explanation
If T = 0, the flip-flop holds its previous state (memory function). If T = 1, the flip-flop
complements its current state at every clock pulse. This behavior makes it useful for counting
and frequency division.
Definition and construction – 1 mark
Truth table – 1 mark
Characteristic equation – 1 mark
Toggle behavior explanation – 1 mark
Working description – 1 mark
b. 1. Parallel-In Serial-Out (PISO) (2.5 marks)   5
Data Entry: All bits are loaded simultaneously in parallel format into the register.
Page 6 of 8
--- page 7 ---
Data Output: Bits are retrieved one at a time in serial format with each clock pulse.
Use Case: Converting data from parallel to serial format, often used for transmitting parallel
data over serial communication lines.
Example: If 1011 is loaded parallelly, it will be output bit-by-bit (e.g., 1, 0, 1, 1).
2. Parallel-In Parallel-Out (PIPO) (2.5 marks)
Data Entry: All bits are loaded simultaneously in parallel format into the register.
Data Output: All bits are retrieved simultaneously in parallel format.
Use Case: Temporary data storage or transfer between parallel systems.
Example: If 1011 is loaded parallelly, it can be retrieved immediately in parallel without
delay.
c.   5
A 3-bit Up/Down counter is a sequential circuit that can count in ascending (up) or descending
(down) order. It uses three flip-flops to store the count and a control input (U/D) to select the
counting direction. (1 mark)
1. Up Mode Operation (U/D = 1) (2 marks)
In up mode, the counter increments its value by 1 on each clock pulse.
The counter increases sequentially. After reaching 111 (7), it returns to 000, completing one
counting cycle.
2. Down Mode Operation (U/D = 0) (2 marks)
In down mode, the counter decrements its value by 1 on each clock pulse.
Page 7 of 8
--- page 8 ---
The counter decreases sequentially. After reaching 000, it returns to 111, maintaining
continuous cyclic operation.
Page 8 of 8
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 57115990e013

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Electronics And Communication Technology/ANS_Re-Exam_Electronics And Communication Technology(NHECT168)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 18 Jun 2026
- Text: mixed (9 pages), mean OCR confidence 84.1

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Electronics And Communication Technology
Date: 18 Jun 2026   Time: 10:30 am - 11:30 am (01:00 Hrs.)
Max Marks: 30
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 9 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Assume suitable data wherever required.
5. Draw diagrams wherever necessary.
1.   Answer the following(Attempt Any 2 Questions)   10
a. Octal Number System (2 Marks)   5
The octal number system is a base-8 number system that uses digits from 0 to 7.
Each position represents a power of 8
Relationship Between Octal and Binary (3 Marks)
Octal is closely related to binary because: 1 octal digit = 3 binary bits
Binary → Octal Conversion: Group binary digits in sets of 3 (from right). Convert each group
to its octal equivalent. Example: ( 110101 ) 2 = ( 6 5 ) 8
Octal → Binary Conversion: Replace each octal digit with its 3-bit binary equivalent.
Example: ( 527 ) 8 = ( 101 010 111 ) 2
b.   5
Page 1 of 9
--- page 2 ---
Marks:
8’s complement (i) – 1
8’s complement (ii) – 1
Octal addition – 1.5
Octal subtraction – 1.5
c. 1M each code   5
Digital systems use various coding schemes to represent numeric data, ensure accuracy,
and improve reliability.
1. Weighted Codes
Codes in which each bit position has a fixed weight.
Examples: 8421 BCD code, 2421 code, 5211 code
2. Non-Weighted Codes
Codes that do not assign positional weights to bits.
Examples: Excess-3 (XS-3) code, Gray code
3. Alphanumeric Codes
Used to represent letters, numbers, and symbols.
Examples: ASCII, EBCDIC, Unicode
4. Error-Detecting Codes
Used to detect errors during data transmission.
Examples: Parity code, Checksum
5. Error-Correcting Codes
Used to detect and correct errors.
Examples: Hamming code
Page 2 of 9

[Text in pictures on this page, read by OCR]
1. 8's Complement

a) 352
7's complement > 425,
Add 1 — 4263

b) 7042
7's complement > 0735¢
Add 1 — 0736.

2. Octal Addition
A73s + 256s — 751s

3. Octal Subtraction
7T03g-145s = 536,
--- page 3 ---
2.

Answer the following(Attempt Any 2 Questions)

a. 2.5M each
1) Convert (0011 1000 0101)BCD into Binary

Step 1: Split into BCD digits
0011-3
1000 - 8
0101-5

Decimal number = 385

Step 2: Convert Decimal — Binary

Division by 2 Quotient
385 +2 192
192 +2 96

96+ 2 48
48-2 24
24+2 12
l2+2 6

6+2 3

3-2 1

1+2 0

Binary (bottom — top) = 110000001,

Page 3 of 9

Remainder

10
--- page 4 ---
b.   5
Definition and Working Principle (2 marks)
BCD to Decimal decoder is a combinational logic circuit that converts a 4-bit BCD input into
ten unique outputs, where only one output is HIGH corresponding to the decimal digit
represented by the input. The decoder reads the 4-bit BCD input and activates the output line
representing that decimal number.
Inputs and Outputs
Inputs: B3 B2 B1 B0 (BCD input bits)
Outputs: D0 – D9 (decimal outputs) Only one output is active at a time.
Page 4 of 9

[Text in pictures on this page, read by OCR]
2) Convert (101010). into Excess-3 Code

Step 1: Binary — Decimal
(101010); = 42

Step 2: Decimal — BCD
4—0100
2 > 0010

BCD = 0100 0010

Step 3: Add 3 (0011) to each BCD digit

BCD Digit + 0011 Excess-3
0100 +0011 0111
0010 +0011 0101

Excess-3 Code = 01110101
--- page 5 ---
(Diagram 1 mark)
Logical Expressions (1 mark)
Each output is a minterm of the BCD inputs.
D0 = B3' B2' B1' B0'
D1 = B3' B2' B1' B0
D2 = B3' B2' B1 B0'
D3 = B3' B2' B1 B0
D4 = B3' B2 B1' B0'
D5 = B3' B2 B1' B0
D6 = B3' B2 B1 B0'
D7 = B3' B2 B1 B0
D8 = B3 B2' B1' B0'
D9 = B3 B2' B1' B0
Applications (1 mark)
Memory selection
Display and indicator systems
Address decoding
Page 5 of 9
--- page 6 ---
Digital control circuits
c.   5
Full Adder is a combinational logic circuit that performs the addition of three binary inputs and
produces two outputs. It overcomes the limitation of a half adder by including a carry input.
Inputs: A, B (significant bits), Cin (carry input)
Outputs: Sum (S), Carry out (Cout) (Definition- 1 mark)
Working Principle
The full adder adds A, B, and Cin. The Sum output represents the least significant bit of the
result. The Carry out represents the carry generated to the next higher stage.
Boolean Expressions
S=A⊕B⊕Cin   Cout =AB+BCin +ACin
A full adder can be implemented using two half adders and one OR gate. (Working principle &
Boolean expressions – 1 mark)
Truth Table (1 mark)
A B Cin Sum (S) Cout
0 0 0   0   0
0 0 1   1   0
0 1 0   1   0
0 1 1   0   1
1 0 0   1   0
1 0 1   0   1
1 1 0   0   1
1 1 1   1   1
Advantages (1 mark)
Adds three input bits including carry-in
Suitable for multi-bit addition by cascading stages
More functional and flexible than a half adder
Widely used in processors and digital arithmetic circuits
Disadvantages (1 mark)
More complex circuit than a half adder
Page 6 of 9
--- page 7 ---
Requires more logic gates and hardware
Higher propagation delay due to carry processing
Consumes more power compared to simpler circuits
3.   Answer the following(Attempt Any 2 Questions)   10
a.   5
SR flip-flop is a basic bistable sequential circuit used to store one bit of data. It has two inputs:
S (Set), R (Reset) and two outputs: Q, Q′ (complement of Q) The outputs are always
complementary. SR flip-flop stores its state based on the inputs applied. Characteristic
equation: Qₙ₊₁ = QₙR′ + SR′ This shows the next state depends on the present state and inputs.
Input Conditions and Operation:
S R Q (Next State) Operation
0 0 No change   Memory / Hold state
1 0 1   Set state
0 1 0   Reset state
1 1   Undefined   Invalid state
1. Set Condition (S=1, R=0)
Q becomes 1
Q′ becomes 0
Flip-flop is set
2. Reset Condition (S=0, R=1)
Q becomes 0
Q′ becomes 1
Flip-flop is reset
3. No Change Condition (S=0, R=0)
Output retains previous state
4. Invalid Condition (S=1, R=1)
Both set and reset activated simultaneously
Outputs may become equal (Q = Q′)
Leads to logical contradiction
Final state unpredictable after inputs return to 0. Therefore, this state is not allowed
Page 7 of 9
--- page 8 ---
Why the Invalid State Occurs
When both inputs are HIGH: Both outputs are forced to the same level. Complementary nature
of outputs is violated. When inputs return LOW, the circuit may settle unpredictably.
Definition & basic concept – 1 mark
Characteristic equation – 1 mark
Explanation of input conditions – 2 marks
Invalid state explanation – 1 mark
b. 1. Serial-In Serial-Out (SISO) (2.5 marks)   5
Data Entry: Bits are entered one at a time in serial format (bit-by-bit) into the register with
each clock pulse.
Data Output: Bits are retrieved one at a time in serial format.
Use Case: Data transmission where serial communication is required, such as shifting data
across circuits.
Example: A sequence of 4 bits (e.g., 1011) enters the register serially, and after a few clock
cycles, it exits in the same order.
2. Serial-In Parallel-Out (SIPO) (2.5 marks)
Data Entry: Bits are entered one at a time in serial format into the register.
Data Output: All bits are retrieved simultaneously in parallel format after they are stored in
the register.
Use Case: Converting data from serial to parallel format, useful in communication systems
where serial data needs to be processed in parallel.
Example: If 1011 is entered serially, after four clock cycles, all bits are available at the
parallel outputs simultaneously.
c. Synchronous counters are designed to reduce propagation delay by ensuring that all flip-flops   5
receive the same clock pulse simultaneously. This allows all state changes to occur at the same
time, improving speed and accuracy compared to asynchronous (ripple) counters. [1 mark]
How Synchronous Counters Reduce Delay [1 mark]
In asynchronous counters, each flip-flop is triggered by the output of the previous one, creating
a ripple effect. This introduces cumulative propagation delay.
In synchronous counters:
Page 8 of 9
--- page 9 ---
All flip-flops are clocked together.
State transitions occur simultaneously.
Ripple delay is eliminated.
Do They Completely Eliminate Delay? [3 marks]
No, synchronous counters do not completely eliminate delay. They significantly reduce delay,
but some delay sources still exist:
1. Gate Propagation Delay
Logic gates controlling flip-flop inputs require time to compute next states.
Delay depends on gate complexity.
2. Setup and Hold Time Requirements
Flip-flops require stable inputs before and after clock edges.
Violations can cause incorrect counting.
3. Clock Distribution Delay (Clock Skew)
Clock signals may not reach all flip-flops at exactly the same time.
This can introduce timing errors in high-speed circuits.
4. Increased Logic Complexity
Additional combinational logic increases overall propagation time.
More bits → more logic → potential delay.
Page 9 of 9
````
