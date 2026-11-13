# Introduction to Cryptography: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c9f250f1f1e0

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CyberSecurity_7010/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Semester IV/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q1   Answer in brief:
CO- a. State Shannon’s theorem on perfect secrecy. Using the One-Time Pad, encrypt the [05]
1;   plaintext HELLO with the key XMCKL using A = 0 to Z = 25 and modulo 26
BL-   arithmetic, showing all steps clearly, and justify why the One-Time Pad achieves
2   perfect secrecy.
• Shannon's theorem: a cipher achieves perfect secrecy iff |K| ≥ |P| and each key is
used exactly once with uniform probability.
• OTP encryption of HELLO using key XMCKL: H(7)+X(23)=30mod26=4→E;
E(4)+M(12)=16→Q;   L(11)+C(2)=13→N;   L(11)+K(10)=21→V;
O(14)+L(11)=25→Z → Ciphertext: EQNVZ
• Perfect secrecy justification: for every ciphertext C and plaintext P, P(plaintext=P |
ciphertext=C) = P(plaintext=P) → no information leaked.
• Condition: key must be truly random, at least as long as the message, used only once,
and kept secret.
• Limitation: impractical for large messages due to key length requirement and secure
distribution problem.
CO- b. State Euler's theorem. Using Euler’s theorem, compute 7120 mod 13.   [05]
2;   • Euler's theorem: if gcd (a,n)=1, then aφ(n) ≡ 1 (mod n).
BL-   • φ (13) = 12 (13 is prime). So 712 ≡ 1 (mod 13).
2   • 7120 = 7(12×10) = (712)10 ≡ 110 = 1 (mod 13).
• Final answer: 7120 mod 13 = 1.
• State relationship between Euler's theorem and Fermat's little theorem (special case
when n is prime).
********** 1 **********
--- page 2 ---
CO- c. Differentiate between Rabin and RSA cryptosystems   [05]
2;
BL-   Rabin Cryptosystem   RSA Cryptosystem
2
Based on the difficulty
Based on the difficulty of
of computing the e-th
Mathematical   computing square roots modulo a
root modulo a
Foundation   composite number (equivalent to
composite number
integer factorization)
(RSA problem)
Decryption yields
Decryption produces four possible
a unique
Decryption   plaintexts; requires additional
plaintext when
Uniqueness   redundancy to identify the correct
standard padding is
one
used
Slower encryption
Encryption   Faster encryption (single modular   (exponentiation with
Speed   squaring operation: C=M2mod n   public exponent e,
typically 65537)
No formal proof that
breaking RSA is
Provably reducible to the
Security   equivalent to
factorization problem—breaking
Reduction   factoring; RSA
Rabin is equivalent to factoring nn
problem may be easier
than factoring
Widely deployed in
Rarely used in practice due to   SSL/TLS, PGP, SSH,
Practical   decryption ambiguity and   and digital signatures
Usage   vulnerability to chosen-ciphertext   with standardized
attacks without proper padding   padding (OAEP,
PKCS#1)
CO- d. Explain the Rail Fence cipher with a neat zig-zag diagram. Encrypt the plaintext [05]
1;   “CRYPTOGRAPHY IS FUN” using a 3-rail fence (ignore spaces during encryption)
BL-   and write the resulting ciphertext
2   • Rail Fence cipher: a transposition cipher that writes plaintext diagonally across a
number of 'rails' then reads off row by row.
********** 2 **********
--- page 3 ---
Q2
CO- a. Explain the Simple Substitution Cipher. Using the substitution key table below, [10]
1;   encrypt the plaintext "NETWORK SECURITY" and then decrypt the resulting
BL-   ciphertext to verify the original message. Show all steps.
3   Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
• Simple Substitution Cipher: each plaintext letter is mapped one-to-one to a unique
ciphertext letter using a fixed substitution alphabet.
********** 3 **********
--- page 4 ---
• Award marks for correct key table, encryption steps, and decryption verification.
CO- b. Describe the attacks on block ciphers (any 5)   [10]
3;   1. Differential Cryptanalysis
BL-   Description:
2
A chosen-plaintext attack that analyzes how differences in input pairs affect
differences in output pairs. By tracing the propagation of differences through the
cipher rounds, cryptanalysts can recover key bits.
Method:
- Select pairs of plaintexts with a fixed XOR difference
- Encrypt both and observe the XOR difference of the ciphertexts
- Identify high-probability differential trails through the S-boxes
- Use these characteristics to deduce key information
Target: DES, FEAL (highly effective); modern ciphers like AES are designed to resist
it
2. Linear Cryptanalysis
Description:
A known-plaintext attack that constructs linear approximations between plaintext,
ciphertext, and key bits. It exploits linear relationships in the S-boxes to recover key
material.
Method:
- Find linear equations relating plaintext, ciphertext, and key bits with high probability
bias
- Collect a large number of known plaintext-ciphertext pairs
********** 4 **********
--- page 5 ---
- Use the linear approximations to solve for key bits via maximum likelihood
estimation
Target: DES (requires ~243 known plaintexts); modern ciphers use S-boxes designed
to minimize linear correlations
3. Side-Channel Attack
Description:
An attack that exploits physical characteristics of the implementation rather than
mathematical weaknesses. It does not attack the cipher algorithm itself but the
hardware or software executing it.
Variants:
- Timing attack: Measures encryption time variations to deduce key
- Power analysis: Monitors power consumption fluctuations (Simple Power Analysis,
Differential Power Analysis)
- Electromagnetic analysis: Captures EM emissions during computation
- Cache attack: Observes cache hit/miss patterns
Target: Any implemented cipher; particularly effective against embedded systems and
smart cards
4. Meet-in-the-Middle Attack
Description:
A time-memory trade-off attack that breaks ciphers using multiple independent keys
by storing intermediate values and matching from both ends.
Target: Double DES, 3DES (reduces security significantly); modern ciphers with
sufficient key length mitigate this
5. Padding Oracle Attack
Description:
An attack that exploits how a system responds to invalid padding during decryption.
By observing padding error messages or timing differences, an attacker can decrypt
ciphertexts without knowing the key.
Method:
- Works against CBC mode with PKCS#7 padding
- Attacker modifies ciphertext bytes and sends to the oracle
- Based on whether padding is valid or invalid, the attacker deduces intermediate state
byte by byte
- Once intermediate state is known, plaintext is recovered via XOR with previous
ciphertext block
Target: Systems using CBC mode with improper padding validation (e.g., Lucky13
attack on TLS, POODLE)
Q3
CO- a. Encrypt the message “KNOWLEDGE IS POWER” using the Playfair cipher with the [10]
1;   keyword “DIAMOND”. Construct the complete 5×5 key matrix (combine I/J, remove
BL-   spaces, insert ‘X’ between repeated letters and for padding if required) and show all
3   encryption steps clearly.
********** 5 **********
--- page 6 ---
Original: KNOWLEDGE IS POWER
Prepared: KN OW LE DG EI SP OW ER
Encrypted: GC IZ TL NQ BM UK IZ BT
Ciphertext: GCIZTLNQBMUKIZBT
CO- b. Explain the ElGamal cryptosystem. Given prime p = 31, generator g = 3, and private [10]
2;   key x = 17, compute the public key y. Encrypt the message M = 10 using random k
BL-   = 7. Then demonstrate the complete decryption process to recover M. Show all
3   modular arithmetic steps clearly.
********** 6 **********
--- page 7 ---
Public Key: y = 22
Ciphertext: (17, 24)
Decrypted Message: M = 10
Q4
CO- a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 11:   [10]
2;
i.   Compute n and Euler’s totient function ϕ(n).
BL-
ii.   Determine the private key exponent d using the Extended Euclidean
3   Algorithm.
iii.   Encrypt the message m = 7 to obtain the ciphertext c.
iv.   Decrypt the ciphertext c to recover the original message.
Show all intermediate steps and calculations clearly.
********** 7 **********
--- page 8 ---
CO- b. Encrypt the plaintext "EXAMINATION BEGINS TOMORROW" using the Vigenere [10]
1;   cipher with the keyword "PROTECT". Perform encryption and decryption. (Ignore
BL-   spaces during encryption)
3
Q5
CO- a. Using Elliptic Curve Cryptography, consider the elliptic curve   [10]
2;   E: y2=x3+2x+2 over F17 . Given the point P = (5, 1), compute 2P using point
BL-   doubling. Show all steps clearly.
3
• ECC: public-key cryptography based on algebraic structure of elliptic curves over
finite fields; y²=x³+ax+b over GF(p).
• Curve: y²=x³+x+6 over GF(11); G=(2,7) — verify: 7²=49≡5≡2³+2+6=16≡5 (mod
11) ✓.
• Point doubling 2G: λ = (3x₁²+a) × (2y₁)⁻¹ mod 11 = (3×4+1) × (14)⁻¹ mod 11 =
13×3⁻¹ mod 11 = 2×4=8 mod 11.
• x₃ = λ²−2x₁ mod 11 = 64−4=60 mod 11=5; y₃ = λ(x₁−x₃) −y₁ mod 11 = 8 (2−5) −7
= −31 mod 11 = 2.
• 2G = (5, 2).
• Point addition 3G = 2G + G: λ = (y₂−y₁) (x₂−x₁)⁻¹ mod 11 = (2−7)(5−2)⁻¹ =
(−5)(3⁻¹) = 6×4=24 mod 11=2.
• x₃=4−5−2=−3 mod 11=8; y₃=2(5−8) −2 = −8 mod 11=3.
********** 8 **********
--- page 9 ---
• 3G = (8, 3). Marks should be awarded for correct application of slope formula,
modular inverse, and point computation steps.
CO- b. Describe the Rabin cryptosystem. Explain the key generation, encryption, and [10]
2;   decryption steps with a suitable example.
BL-   • Rabin cryptosystem: public key encryption based on difficulty of computing square
3   roots mod n (equivalent to factoring).
• Key generation: choose large primes p, q with p≡q≡3(mod 4); n=p×q; public key=n,
private key=(p,q).
• Encryption: C = M² mod n.
• Decryption: compute 4 square roots of C mod n using Chinese Remainder Theorem;
correct plaintext identified using redundancy.
• Security: breaking Rabin ≡ factoring n; provably as hard as factoring (unlike RSA
which is unproven equivalent).
• Limitation: 4 possible plaintexts during decryption; redundancy needed to identify
correct one.
Q6
CO- a. Using the Diffie-Hellman key exchange, compute the shared secret key between Alice [10]
2;   and Bob given p = 41 and generator g = 7. Alice selects private key a = 9 and Bob
BL-   selects private key b = 14. Show all intermediate steps clearly and explain why an
3   eavesdropper cannot feasibly compute the shared secret.
CO- b. Describe the structure of the MD5 algorithm. Explain the message padding process, [10]
3;   initialization vector, the four auxiliary functions (F, G, H, I), and the compression
BL-   function. Illustrate the working with a clearly labeled block diagram showing how the
3   128-bit message digest is produced.
• MD5: produces 128-bit (16-byte) digest; designed by Ron Rivest (1992); processes
512-bit blocks.
• Message padding: append single '1' bit, then '0' bits until length ≡ 448 (mod 512);
append original message length as 64-bit little-endian integer.
• Initialization: four 32-bit state variables A, B, C, D initialized to: A=0x67452301,
B=0xEFCDAB89, C=0x98BADCFE, D=0x10325476.
• Four auxiliary functions: F(B, C,D)=(B∧C)∨(¬B∧D); G(B,C,D)=(B∧D)∨(C∧¬D);
H(B,C,D)=B⊕C⊕D; I(B,C,D)=C⊕(B∨¬D).
• 64 rounds in 4 groups of 16: rounds 1–16 use F; 17–32 use G; 33–48 use H; 49–64
use I.
********** 9 **********
--- page 10 ---
• Each round: T = B + left rotate (A + F/G/H/I (B, C, D) + M[k] + T[i], s); then (A,
B, C, D) rotated.
• Constants T[i] = floor(|sin(i+1) | × 2^32); message words M[k] accessed in different
orders per round group.
• Final digest = A||B||C||D (128 bits).
Block diagram showing chaining of 512-bit blocks required.
Q7   Write short notes on the following:
CO- a. Principles of Modern Cryptography (Confusion, Diffusion, Key Avalanche Effect)   [05]
1;   • Confusion: each ciphertext bit should depend on many key bits in a complex way →
BL-   achieved via substitution (S-Boxes).
2   • Diffusion: changing one plaintext bit should change approximately half of the
ciphertext bits → achieved via permutation/transposition (P-Boxes, MixColumns).
• Avalanche effect: small change in input (1 bit) causes ≥50% change in output bits.
• Shannon's two design principles: confusion and diffusion together resist both
differential and linear cryptanalysis.
• Example: AES achieves confusion via SubBytes (S-Box) and diffusion via
ShiftRows + MixColumns.
• Strict Avalanche Criterion (SAC): flipping any single input bit changes each output
bit with probability exactly 1/2.
CO- b. Galois Field GF(2⁸) and its role in AES   [05]
1;   • GF(2⁸): Galois Field with 2⁸=256 elements; elements are 8-bit polynomials over
BL-   GF(2) with coefficients 0 or 1.
2   • Irreducible polynomial used in AES: p(x) = x⁸+x⁴+x³+x+1 (0x11B).
• Addition in GF(2⁸) = XOR of bit patterns.
• Multiplication in GF(2⁸): polynomial multiplication mod p(x); multiply by x (=0x02)
= left shift, XOR 0x1B if carry.
• Role in AES: MixColumns uses GF(2⁸) arithmetic; SubBytes uses multiplicative
inverse in GF(2⁸).
• Example: 0x57 × 0x83 in GF(2⁸) = 0xC1 (show step-by-step polynomial
multiplication).
CO- c. Authority based KDC   [05]
3;   ▪ A trusted authority (e.g., Key Distribution Centre - KDC) generates and
BL-   distributes public keys.
2   ▪ The authority ensures that keys are securely exchanged between users.
Process:
▪ User A requests a public key from the authority.
▪ The authority verifies the request and provides User B’s public key.
▪ User A uses the key for encryption and secure communication.
Advantages:
• The trusted authority ensures the authenticity of the public keys.
• Reduces the risk of man-in-the-middle attacks.
Disadvantages:
********** 10 **********
--- page 11 ---
•   If the authority is compromised, all keys may be exposed.
• Requires a centralized authority that must be highly secure.
CO- d. Quadratic Congruence and Euler's Criterion with examples   [05]
2;
BL-   • Quadratic congruence: equation of form x² ≡ a (mod n); solution exists if a is a
2   quadratic residue mod n.
• Euler's criterion: a is a quadratic residue mod prime p if a ((p-1)/2) ≡ 1 (mod p); non-
residue gives −1.
• Example: Is 7 a QR mod 11
75 mod 11 = 74×7 = (72)2×7 = 49²×7 mod 11 = 4²×7=16×7=112 mod 11=2...
recalc: 75=16807 mod 11=75; 11×1528=16808; 16807mod11=10≡−1
→ 7 is NOT a QR mod 11.
• Example: Is 4 a QR mod 11?
45=1024 mod 11=1024−93×11=1 → yes; x²≡4(mod11) → x = 2 or 9.
• Significance: quadratic residuosity problem underpins Rabin cryptosystem and
Goldwasser-Micali encryption.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper defe276fa166

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Semester IV/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q1   Answer in brief:
CO- a. State Shannon’s theorem on perfect secrecy. Using the One-Time Pad, encrypt the [05]
1;   plaintext HELLO with the key XMCKL using A = 0 to Z = 25 and modulo 26
BL-   arithmetic, showing all steps clearly, and justify why the One-Time Pad achieves
2   perfect secrecy.
• Shannon's theorem: a cipher achieves perfect secrecy iff |K| ≥ |P| and each key is
used exactly once with uniform probability.
• OTP encryption of HELLO using key XMCKL: H(7)+X(23)=30mod26=4→E;
E(4)+M(12)=16→Q;   L(11)+C(2)=13→N;   L(11)+K(10)=21→V;
O(14)+L(11)=25→Z → Ciphertext: EQNVZ
• Perfect secrecy justification: for every ciphertext C and plaintext P, P(plaintext=P |
ciphertext=C) = P(plaintext=P) → no information leaked.
• Condition: key must be truly random, at least as long as the message, used only once,
and kept secret.
• Limitation: impractical for large messages due to key length requirement and secure
distribution problem.
CO- b. State Euler's theorem. Using Euler’s theorem, compute 7120 mod 13.   [05]
2;   • Euler's theorem: if gcd (a,n)=1, then aφ(n) ≡ 1 (mod n).
BL-   • φ (13) = 12 (13 is prime). So 712 ≡ 1 (mod 13).
2   • 7120 = 7(12×10) = (712)10 ≡ 110 = 1 (mod 13).
• Final answer: 7120 mod 13 = 1.
• State relationship between Euler's theorem and Fermat's little theorem (special case
when n is prime).
********** 1 **********
--- page 2 ---
CO- c. Differentiate between Rabin and RSA cryptosystems   [05]
2;
BL-   Rabin Cryptosystem   RSA Cryptosystem
2
Based on the difficulty
Based on the difficulty of
of computing the e-th
Mathematical   computing square roots modulo a
root modulo a
Foundation   composite number (equivalent to
composite number
integer factorization)
(RSA problem)
Decryption yields
Decryption produces four possible
a unique
Decryption   plaintexts; requires additional
plaintext when
Uniqueness   redundancy to identify the correct
standard padding is
one
used
Slower encryption
Encryption   Faster encryption (single modular   (exponentiation with
Speed   squaring operation: C=M2mod n   public exponent e,
typically 65537)
No formal proof that
breaking RSA is
Provably reducible to the
Security   equivalent to
factorization problem—breaking
Reduction   factoring; RSA
Rabin is equivalent to factoring nn
problem may be easier
than factoring
Widely deployed in
Rarely used in practice due to   SSL/TLS, PGP, SSH,
Practical   decryption ambiguity and   and digital signatures
Usage   vulnerability to chosen-ciphertext   with standardized
attacks without proper padding   padding (OAEP,
PKCS#1)
CO- d. Explain the Rail Fence cipher with a neat zig-zag diagram. Encrypt the plaintext [05]
1;   “CRYPTOGRAPHY IS FUN” using a 3-rail fence (ignore spaces during encryption)
BL-   and write the resulting ciphertext
2   • Rail Fence cipher: a transposition cipher that writes plaintext diagonally across a
number of 'rails' then reads off row by row.
********** 2 **********
--- page 3 ---
Q2
CO- a. Explain the Simple Substitution Cipher. Using the substitution key table below, [10]
1;   encrypt the plaintext "NETWORK SECURITY" and then decrypt the resulting
BL-   ciphertext to verify the original message. Show all steps.
3   Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
• Simple Substitution Cipher: each plaintext letter is mapped one-to-one to a unique
ciphertext letter using a fixed substitution alphabet.
********** 3 **********
--- page 4 ---
• Award marks for correct key table, encryption steps, and decryption verification.
CO- b. Describe the attacks on block ciphers (any 5)   [10]
3;   1. Differential Cryptanalysis
BL-   Description:
2
A chosen-plaintext attack that analyzes how differences in input pairs affect
differences in output pairs. By tracing the propagation of differences through the
cipher rounds, cryptanalysts can recover key bits.
Method:
- Select pairs of plaintexts with a fixed XOR difference
- Encrypt both and observe the XOR difference of the ciphertexts
- Identify high-probability differential trails through the S-boxes
- Use these characteristics to deduce key information
Target: DES, FEAL (highly effective); modern ciphers like AES are designed to resist
it
2. Linear Cryptanalysis
Description:
A known-plaintext attack that constructs linear approximations between plaintext,
ciphertext, and key bits. It exploits linear relationships in the S-boxes to recover key
material.
Method:
- Find linear equations relating plaintext, ciphertext, and key bits with high probability
bias
- Collect a large number of known plaintext-ciphertext pairs
********** 4 **********
--- page 5 ---
- Use the linear approximations to solve for key bits via maximum likelihood
estimation
Target: DES (requires ~243 known plaintexts); modern ciphers use S-boxes designed
to minimize linear correlations
3. Side-Channel Attack
Description:
An attack that exploits physical characteristics of the implementation rather than
mathematical weaknesses. It does not attack the cipher algorithm itself but the
hardware or software executing it.
Variants:
- Timing attack: Measures encryption time variations to deduce key
- Power analysis: Monitors power consumption fluctuations (Simple Power Analysis,
Differential Power Analysis)
- Electromagnetic analysis: Captures EM emissions during computation
- Cache attack: Observes cache hit/miss patterns
Target: Any implemented cipher; particularly effective against embedded systems and
smart cards
4. Meet-in-the-Middle Attack
Description:
A time-memory trade-off attack that breaks ciphers using multiple independent keys
by storing intermediate values and matching from both ends.
Target: Double DES, 3DES (reduces security significantly); modern ciphers with
sufficient key length mitigate this
5. Padding Oracle Attack
Description:
An attack that exploits how a system responds to invalid padding during decryption.
By observing padding error messages or timing differences, an attacker can decrypt
ciphertexts without knowing the key.
Method:
- Works against CBC mode with PKCS#7 padding
- Attacker modifies ciphertext bytes and sends to the oracle
- Based on whether padding is valid or invalid, the attacker deduces intermediate state
byte by byte
- Once intermediate state is known, plaintext is recovered via XOR with previous
ciphertext block
Target: Systems using CBC mode with improper padding validation (e.g., Lucky13
attack on TLS, POODLE)
Q3
CO- a. Encrypt the message “KNOWLEDGE IS POWER” using the Playfair cipher with the [10]
1;   keyword “DIAMOND”. Construct the complete 5×5 key matrix (combine I/J, remove
BL-   spaces, insert ‘X’ between repeated letters and for padding if required) and show all
3   encryption steps clearly.
********** 5 **********
--- page 6 ---
Original: KNOWLEDGE IS POWER
Prepared: KN OW LE DG EI SP OW ER
Encrypted: GC IZ TL NQ BM UK IZ BT
Ciphertext: GCIZTLNQBMUKIZBT
CO- b. Explain the ElGamal cryptosystem. Given prime p = 31, generator g = 3, and private [10]
2;   key x = 17, compute the public key y. Encrypt the message M = 10 using random k
BL-   = 7. Then demonstrate the complete decryption process to recover M. Show all
3   modular arithmetic steps clearly.
********** 6 **********
--- page 7 ---
Public Key: y = 22
Ciphertext: (17, 24)
Decrypted Message: M = 10
Q4
CO- a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 11:   [10]
2;
i.   Compute n and Euler’s totient function ϕ(n).
BL-
ii.   Determine the private key exponent d using the Extended Euclidean
3   Algorithm.
iii.   Encrypt the message m = 7 to obtain the ciphertext c.
iv.   Decrypt the ciphertext c to recover the original message.
Show all intermediate steps and calculations clearly.
********** 7 **********
--- page 8 ---
CO- b. Encrypt the plaintext "EXAMINATION BEGINS TOMORROW" using the Vigenere [10]
1;   cipher with the keyword "PROTECT". Perform encryption and decryption. (Ignore
BL-   spaces during encryption)
3
Q5
CO- a. Using Elliptic Curve Cryptography, consider the elliptic curve   [10]
2;   E: y2=x3+2x+2 over F17 . Given the point P = (5, 1), compute 2P using point
BL-   doubling. Show all steps clearly.
3
• ECC: public-key cryptography based on algebraic structure of elliptic curves over
finite fields; y²=x³+ax+b over GF(p).
• Curve: y²=x³+x+6 over GF(11); G=(2,7) — verify: 7²=49≡5≡2³+2+6=16≡5 (mod
11) ✓.
• Point doubling 2G: λ = (3x₁²+a) × (2y₁)⁻¹ mod 11 = (3×4+1) × (14)⁻¹ mod 11 =
13×3⁻¹ mod 11 = 2×4=8 mod 11.
• x₃ = λ²−2x₁ mod 11 = 64−4=60 mod 11=5; y₃ = λ(x₁−x₃) −y₁ mod 11 = 8 (2−5) −7
= −31 mod 11 = 2.
• 2G = (5, 2).
• Point addition 3G = 2G + G: λ = (y₂−y₁) (x₂−x₁)⁻¹ mod 11 = (2−7)(5−2)⁻¹ =
(−5)(3⁻¹) = 6×4=24 mod 11=2.
• x₃=4−5−2=−3 mod 11=8; y₃=2(5−8) −2 = −8 mod 11=3.
********** 8 **********
--- page 9 ---
• 3G = (8, 3). Marks should be awarded for correct application of slope formula,
modular inverse, and point computation steps.
CO- b. Describe the Rabin cryptosystem. Explain the key generation, encryption, and [10]
2;   decryption steps with a suitable example.
BL-   • Rabin cryptosystem: public key encryption based on difficulty of computing square
3   roots mod n (equivalent to factoring).
• Key generation: choose large primes p, q with p≡q≡3(mod 4); n=p×q; public key=n,
private key=(p,q).
• Encryption: C = M² mod n.
• Decryption: compute 4 square roots of C mod n using Chinese Remainder Theorem;
correct plaintext identified using redundancy.
• Security: breaking Rabin ≡ factoring n; provably as hard as factoring (unlike RSA
which is unproven equivalent).
• Limitation: 4 possible plaintexts during decryption; redundancy needed to identify
correct one.
Q6
CO- a. Using the Diffie-Hellman key exchange, compute the shared secret key between Alice [10]
2;   and Bob given p = 41 and generator g = 7. Alice selects private key a = 9 and Bob
BL-   selects private key b = 14. Show all intermediate steps clearly and explain why an
3   eavesdropper cannot feasibly compute the shared secret.
CO- b. Describe the structure of the MD5 algorithm. Explain the message padding process, [10]
3;   initialization vector, the four auxiliary functions (F, G, H, I), and the compression
BL-   function. Illustrate the working with a clearly labeled block diagram showing how the
3   128-bit message digest is produced.
• MD5: produces 128-bit (16-byte) digest; designed by Ron Rivest (1992); processes
512-bit blocks.
• Message padding: append single '1' bit, then '0' bits until length ≡ 448 (mod 512);
append original message length as 64-bit little-endian integer.
• Initialization: four 32-bit state variables A, B, C, D initialized to: A=0x67452301,
B=0xEFCDAB89, C=0x98BADCFE, D=0x10325476.
• Four auxiliary functions: F(B, C,D)=(B∧C)∨(¬B∧D); G(B,C,D)=(B∧D)∨(C∧¬D);
H(B,C,D)=B⊕C⊕D; I(B,C,D)=C⊕(B∨¬D).
• 64 rounds in 4 groups of 16: rounds 1–16 use F; 17–32 use G; 33–48 use H; 49–64
use I.
********** 9 **********
--- page 10 ---
• Each round: T = B + left rotate (A + F/G/H/I (B, C, D) + M[k] + T[i], s); then (A,
B, C, D) rotated.
• Constants T[i] = floor(|sin(i+1) | × 2^32); message words M[k] accessed in different
orders per round group.
• Final digest = A||B||C||D (128 bits).
Block diagram showing chaining of 512-bit blocks required.
Q7   Write short notes on the following:
CO- a. Principles of Modern Cryptography (Confusion, Diffusion, Key Avalanche Effect)   [05]
1;   • Confusion: each ciphertext bit should depend on many key bits in a complex way →
BL-   achieved via substitution (S-Boxes).
2   • Diffusion: changing one plaintext bit should change approximately half of the
ciphertext bits → achieved via permutation/transposition (P-Boxes, MixColumns).
• Avalanche effect: small change in input (1 bit) causes ≥50% change in output bits.
• Shannon's two design principles: confusion and diffusion together resist both
differential and linear cryptanalysis.
• Example: AES achieves confusion via SubBytes (S-Box) and diffusion via
ShiftRows + MixColumns.
• Strict Avalanche Criterion (SAC): flipping any single input bit changes each output
bit with probability exactly 1/2.
CO- b. Galois Field GF(2⁸) and its role in AES   [05]
1;   • GF(2⁸): Galois Field with 2⁸=256 elements; elements are 8-bit polynomials over
BL-   GF(2) with coefficients 0 or 1.
2   • Irreducible polynomial used in AES: p(x) = x⁸+x⁴+x³+x+1 (0x11B).
• Addition in GF(2⁸) = XOR of bit patterns.
• Multiplication in GF(2⁸): polynomial multiplication mod p(x); multiply by x (=0x02)
= left shift, XOR 0x1B if carry.
• Role in AES: MixColumns uses GF(2⁸) arithmetic; SubBytes uses multiplicative
inverse in GF(2⁸).
• Example: 0x57 × 0x83 in GF(2⁸) = 0xC1 (show step-by-step polynomial
multiplication).
CO- c. Authority based KDC   [05]
3;   ▪ A trusted authority (e.g., Key Distribution Centre - KDC) generates and
BL-   distributes public keys.
2   ▪ The authority ensures that keys are securely exchanged between users.
Process:
▪ User A requests a public key from the authority.
▪ The authority verifies the request and provides User B’s public key.
▪ User A uses the key for encryption and secure communication.
Advantages:
• The trusted authority ensures the authenticity of the public keys.
• Reduces the risk of man-in-the-middle attacks.
Disadvantages:
********** 10 **********
--- page 11 ---
•   If the authority is compromised, all keys may be exposed.
• Requires a centralized authority that must be highly secure.
CO- d. Quadratic Congruence and Euler's Criterion with examples   [05]
2;
BL-   • Quadratic congruence: equation of form x² ≡ a (mod n); solution exists if a is a
2   quadratic residue mod n.
• Euler's criterion: a is a quadratic residue mod prime p if a ((p-1)/2) ≡ 1 (mod p); non-
residue gives −1.
• Example: Is 7 a QR mod 11
75 mod 11 = 74×7 = (72)2×7 = 49²×7 mod 11 = 4²×7=16×7=112 mod 11=2...
recalc: 75=16807 mod 11=75; 11×1528=16808; 16807mod11=10≡−1
→ 7 is NOT a QR mod 11.
• Example: Is 4 a QR mod 11?
45=1024 mod 11=1024−93×11=1 → yes; x²≡4(mod11) → x = 2 or 9.
• Significance: quadratic residuosity problem underpins Rabin cryptosystem and
Goldwasser-Micali encryption.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 517cf347be34

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Semester IV/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q1   Answer in brief:
CO- a. State Shannon’s theorem on perfect secrecy. Using the One-Time Pad, encrypt the [05]
1;   plaintext HELLO with the key XMCKL using A = 0 to Z = 25 and modulo 26
BL-   arithmetic, showing all steps clearly, and justify why the One-Time Pad achieves
2   perfect secrecy.
• Shannon's theorem: a cipher achieves perfect secrecy iff |K| ≥ |P| and each key is
used exactly once with uniform probability.
• OTP encryption of HELLO using key XMCKL: H(7)+X(23)=30mod26=4→E;
E(4)+M(12)=16→Q;   L(11)+C(2)=13→N;   L(11)+K(10)=21→V;
O(14)+L(11)=25→Z → Ciphertext: EQNVZ
• Perfect secrecy justification: for every ciphertext C and plaintext P, P(plaintext=P |
ciphertext=C) = P(plaintext=P) → no information leaked.
• Condition: key must be truly random, at least as long as the message, used only once,
and kept secret.
• Limitation: impractical for large messages due to key length requirement and secure
distribution problem.
CO- b. State Euler's theorem. Using Euler’s theorem, compute 7120 mod 13.   [05]
2;   • Euler's theorem: if gcd (a,n)=1, then aφ(n) ≡ 1 (mod n).
BL-   • φ (13) = 12 (13 is prime). So 712 ≡ 1 (mod 13).
2   • 7120 = 7(12×10) = (712)10 ≡ 110 = 1 (mod 13).
• Final answer: 7120 mod 13 = 1.
• State relationship between Euler's theorem and Fermat's little theorem (special case
when n is prime).
********** 1 **********
--- page 2 ---
CO- c. Differentiate between Rabin and RSA cryptosystems   [05]
2;
BL-   Rabin Cryptosystem   RSA Cryptosystem
2
Based on the difficulty
Based on the difficulty of
of computing the e-th
Mathematical   computing square roots modulo a
root modulo a
Foundation   composite number (equivalent to
composite number
integer factorization)
(RSA problem)
Decryption yields
Decryption produces four possible
a unique
Decryption   plaintexts; requires additional
plaintext when
Uniqueness   redundancy to identify the correct
standard padding is
one
used
Slower encryption
Encryption   Faster encryption (single modular   (exponentiation with
Speed   squaring operation: C=M2mod n   public exponent e,
typically 65537)
No formal proof that
breaking RSA is
Provably reducible to the
Security   equivalent to
factorization problem—breaking
Reduction   factoring; RSA
Rabin is equivalent to factoring nn
problem may be easier
than factoring
Widely deployed in
Rarely used in practice due to   SSL/TLS, PGP, SSH,
Practical   decryption ambiguity and   and digital signatures
Usage   vulnerability to chosen-ciphertext   with standardized
attacks without proper padding   padding (OAEP,
PKCS#1)
CO- d. Explain the Rail Fence cipher with a neat zig-zag diagram. Encrypt the plaintext [05]
1;   “CRYPTOGRAPHY IS FUN” using a 3-rail fence (ignore spaces during encryption)
BL-   and write the resulting ciphertext
2   • Rail Fence cipher: a transposition cipher that writes plaintext diagonally across a
number of 'rails' then reads off row by row.
********** 2 **********
--- page 3 ---
Q2
CO- a. Explain the Simple Substitution Cipher. Using the substitution key table below, [10]
1;   encrypt the plaintext "NETWORK SECURITY" and then decrypt the resulting
BL-   ciphertext to verify the original message. Show all steps.
3   Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
• Simple Substitution Cipher: each plaintext letter is mapped one-to-one to a unique
ciphertext letter using a fixed substitution alphabet.
********** 3 **********
--- page 4 ---
• Award marks for correct key table, encryption steps, and decryption verification.
CO- b. Describe the attacks on block ciphers (any 5)   [10]
3;   1. Differential Cryptanalysis
BL-   Description:
2
A chosen-plaintext attack that analyzes how differences in input pairs affect
differences in output pairs. By tracing the propagation of differences through the
cipher rounds, cryptanalysts can recover key bits.
Method:
- Select pairs of plaintexts with a fixed XOR difference
- Encrypt both and observe the XOR difference of the ciphertexts
- Identify high-probability differential trails through the S-boxes
- Use these characteristics to deduce key information
Target: DES, FEAL (highly effective); modern ciphers like AES are designed to resist
it
2. Linear Cryptanalysis
Description:
A known-plaintext attack that constructs linear approximations between plaintext,
ciphertext, and key bits. It exploits linear relationships in the S-boxes to recover key
material.
Method:
- Find linear equations relating plaintext, ciphertext, and key bits with high probability
bias
- Collect a large number of known plaintext-ciphertext pairs
********** 4 **********
--- page 5 ---
- Use the linear approximations to solve for key bits via maximum likelihood
estimation
Target: DES (requires ~243 known plaintexts); modern ciphers use S-boxes designed
to minimize linear correlations
3. Side-Channel Attack
Description:
An attack that exploits physical characteristics of the implementation rather than
mathematical weaknesses. It does not attack the cipher algorithm itself but the
hardware or software executing it.
Variants:
- Timing attack: Measures encryption time variations to deduce key
- Power analysis: Monitors power consumption fluctuations (Simple Power Analysis,
Differential Power Analysis)
- Electromagnetic analysis: Captures EM emissions during computation
- Cache attack: Observes cache hit/miss patterns
Target: Any implemented cipher; particularly effective against embedded systems and
smart cards
4. Meet-in-the-Middle Attack
Description:
A time-memory trade-off attack that breaks ciphers using multiple independent keys
by storing intermediate values and matching from both ends.
Target: Double DES, 3DES (reduces security significantly); modern ciphers with
sufficient key length mitigate this
5. Padding Oracle Attack
Description:
An attack that exploits how a system responds to invalid padding during decryption.
By observing padding error messages or timing differences, an attacker can decrypt
ciphertexts without knowing the key.
Method:
- Works against CBC mode with PKCS#7 padding
- Attacker modifies ciphertext bytes and sends to the oracle
- Based on whether padding is valid or invalid, the attacker deduces intermediate state
byte by byte
- Once intermediate state is known, plaintext is recovered via XOR with previous
ciphertext block
Target: Systems using CBC mode with improper padding validation (e.g., Lucky13
attack on TLS, POODLE)
Q3
CO- a. Encrypt the message “KNOWLEDGE IS POWER” using the Playfair cipher with the [10]
1;   keyword “DIAMOND”. Construct the complete 5×5 key matrix (combine I/J, remove
BL-   spaces, insert ‘X’ between repeated letters and for padding if required) and show all
3   encryption steps clearly.
********** 5 **********
--- page 6 ---
Original: KNOWLEDGE IS POWER
Prepared: KN OW LE DG EI SP OW ER
Encrypted: GC IZ TL NQ BM UK IZ BT
Ciphertext: GCIZTLNQBMUKIZBT
CO- b. Explain the ElGamal cryptosystem. Given prime p = 31, generator g = 3, and private [10]
2;   key x = 17, compute the public key y. Encrypt the message M = 10 using random k
BL-   = 7. Then demonstrate the complete decryption process to recover M. Show all
3   modular arithmetic steps clearly.
********** 6 **********
--- page 7 ---
Public Key: y = 22
Ciphertext: (17, 24)
Decrypted Message: M = 10
Q4
CO- a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 11:   [10]
2;
i.   Compute n and Euler’s totient function ϕ(n).
BL-
ii.   Determine the private key exponent d using the Extended Euclidean
3   Algorithm.
iii.   Encrypt the message m = 7 to obtain the ciphertext c.
iv.   Decrypt the ciphertext c to recover the original message.
Show all intermediate steps and calculations clearly.
********** 7 **********
--- page 8 ---
CO- b. Encrypt the plaintext "EXAMINATION BEGINS TOMORROW" using the Vigenere [10]
1;   cipher with the keyword "PROTECT". Perform encryption and decryption. (Ignore
BL-   spaces during encryption)
3
Q5
CO- a. Using Elliptic Curve Cryptography, consider the elliptic curve   [10]
2;   E: y2=x3+2x+2 over F17 . Given the point P = (5, 1), compute 2P using point
BL-   doubling. Show all steps clearly.
3
• ECC: public-key cryptography based on algebraic structure of elliptic curves over
finite fields; y²=x³+ax+b over GF(p).
• Curve: y²=x³+x+6 over GF(11); G=(2,7) — verify: 7²=49≡5≡2³+2+6=16≡5 (mod
11) ✓.
• Point doubling 2G: λ = (3x₁²+a) × (2y₁)⁻¹ mod 11 = (3×4+1) × (14)⁻¹ mod 11 =
13×3⁻¹ mod 11 = 2×4=8 mod 11.
• x₃ = λ²−2x₁ mod 11 = 64−4=60 mod 11=5; y₃ = λ(x₁−x₃) −y₁ mod 11 = 8 (2−5) −7
= −31 mod 11 = 2.
• 2G = (5, 2).
• Point addition 3G = 2G + G: λ = (y₂−y₁) (x₂−x₁)⁻¹ mod 11 = (2−7)(5−2)⁻¹ =
(−5)(3⁻¹) = 6×4=24 mod 11=2.
• x₃=4−5−2=−3 mod 11=8; y₃=2(5−8) −2 = −8 mod 11=3.
********** 8 **********
--- page 9 ---
• 3G = (8, 3). Marks should be awarded for correct application of slope formula,
modular inverse, and point computation steps.
CO- b. Describe the Rabin cryptosystem. Explain the key generation, encryption, and [10]
2;   decryption steps with a suitable example.
BL-   • Rabin cryptosystem: public key encryption based on difficulty of computing square
3   roots mod n (equivalent to factoring).
• Key generation: choose large primes p, q with p≡q≡3(mod 4); n=p×q; public key=n,
private key=(p,q).
• Encryption: C = M² mod n.
• Decryption: compute 4 square roots of C mod n using Chinese Remainder Theorem;
correct plaintext identified using redundancy.
• Security: breaking Rabin ≡ factoring n; provably as hard as factoring (unlike RSA
which is unproven equivalent).
• Limitation: 4 possible plaintexts during decryption; redundancy needed to identify
correct one.
Q6
CO- a. Using the Diffie-Hellman key exchange, compute the shared secret key between Alice [10]
2;   and Bob given p = 41 and generator g = 7. Alice selects private key a = 9 and Bob
BL-   selects private key b = 14. Show all intermediate steps clearly and explain why an
3   eavesdropper cannot feasibly compute the shared secret.
CO- b. Describe the structure of the MD5 algorithm. Explain the message padding process, [10]
3;   initialization vector, the four auxiliary functions (F, G, H, I), and the compression
BL-   function. Illustrate the working with a clearly labeled block diagram showing how the
3   128-bit message digest is produced.
• MD5: produces 128-bit (16-byte) digest; designed by Ron Rivest (1992); processes
512-bit blocks.
• Message padding: append single '1' bit, then '0' bits until length ≡ 448 (mod 512);
append original message length as 64-bit little-endian integer.
• Initialization: four 32-bit state variables A, B, C, D initialized to: A=0x67452301,
B=0xEFCDAB89, C=0x98BADCFE, D=0x10325476.
• Four auxiliary functions: F(B, C,D)=(B∧C)∨(¬B∧D); G(B,C,D)=(B∧D)∨(C∧¬D);
H(B,C,D)=B⊕C⊕D; I(B,C,D)=C⊕(B∨¬D).
• 64 rounds in 4 groups of 16: rounds 1–16 use F; 17–32 use G; 33–48 use H; 49–64
use I.
********** 9 **********
--- page 10 ---
• Each round: T = B + left rotate (A + F/G/H/I (B, C, D) + M[k] + T[i], s); then (A,
B, C, D) rotated.
• Constants T[i] = floor(|sin(i+1) | × 2^32); message words M[k] accessed in different
orders per round group.
• Final digest = A||B||C||D (128 bits).
Block diagram showing chaining of 512-bit blocks required.
Q7   Write short notes on the following:
CO- a. Principles of Modern Cryptography (Confusion, Diffusion, Key Avalanche Effect)   [05]
1;   • Confusion: each ciphertext bit should depend on many key bits in a complex way →
BL-   achieved via substitution (S-Boxes).
2   • Diffusion: changing one plaintext bit should change approximately half of the
ciphertext bits → achieved via permutation/transposition (P-Boxes, MixColumns).
• Avalanche effect: small change in input (1 bit) causes ≥50% change in output bits.
• Shannon's two design principles: confusion and diffusion together resist both
differential and linear cryptanalysis.
• Example: AES achieves confusion via SubBytes (S-Box) and diffusion via
ShiftRows + MixColumns.
• Strict Avalanche Criterion (SAC): flipping any single input bit changes each output
bit with probability exactly 1/2.
CO- b. Galois Field GF(2⁸) and its role in AES   [05]
1;   • GF(2⁸): Galois Field with 2⁸=256 elements; elements are 8-bit polynomials over
BL-   GF(2) with coefficients 0 or 1.
2   • Irreducible polynomial used in AES: p(x) = x⁸+x⁴+x³+x+1 (0x11B).
• Addition in GF(2⁸) = XOR of bit patterns.
• Multiplication in GF(2⁸): polynomial multiplication mod p(x); multiply by x (=0x02)
= left shift, XOR 0x1B if carry.
• Role in AES: MixColumns uses GF(2⁸) arithmetic; SubBytes uses multiplicative
inverse in GF(2⁸).
• Example: 0x57 × 0x83 in GF(2⁸) = 0xC1 (show step-by-step polynomial
multiplication).
CO- c. Authority based KDC   [05]
3;   ▪ A trusted authority (e.g., Key Distribution Centre - KDC) generates and
BL-   distributes public keys.
2   ▪ The authority ensures that keys are securely exchanged between users.
Process:
▪ User A requests a public key from the authority.
▪ The authority verifies the request and provides User B’s public key.
▪ User A uses the key for encryption and secure communication.
Advantages:
• The trusted authority ensures the authenticity of the public keys.
• Reduces the risk of man-in-the-middle attacks.
Disadvantages:
********** 10 **********
--- page 11 ---
•   If the authority is compromised, all keys may be exposed.
• Requires a centralized authority that must be highly secure.
CO- d. Quadratic Congruence and Euler's Criterion with examples   [05]
2;
BL-   • Quadratic congruence: equation of form x² ≡ a (mod n); solution exists if a is a
2   quadratic residue mod n.
• Euler's criterion: a is a quadratic residue mod prime p if a ((p-1)/2) ≡ 1 (mod p); non-
residue gives −1.
• Example: Is 7 a QR mod 11
75 mod 11 = 74×7 = (72)2×7 = 49²×7 mod 11 = 4²×7=16×7=112 mod 11=2...
recalc: 75=16807 mod 11=75; 11×1528=16808; 16807mod11=10≡−1
→ 7 is NOT a QR mod 11.
• Example: Is 4 a QR mod 11?
45=1024 mod 11=1024−93×11=1 → yes; x²≡4(mod11) → x = 2 or 9.
• Significance: quadratic residuosity problem underpins Rabin cryptosystem and
Goldwasser-Micali encryption.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper cf7f81107fbc

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Semester IV/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q1   Answer in brief:
CO- a. State Shannon’s theorem on perfect secrecy. Using the One-Time Pad, encrypt the [05]
1;   plaintext HELLO with the key XMCKL using A = 0 to Z = 25 and modulo 26
BL-   arithmetic, showing all steps clearly, and justify why the One-Time Pad achieves
2   perfect secrecy.
• Shannon's theorem: a cipher achieves perfect secrecy iff |K| ≥ |P| and each key is
used exactly once with uniform probability.
• OTP encryption of HELLO using key XMCKL: H(7)+X(23)=30mod26=4→E;
E(4)+M(12)=16→Q;   L(11)+C(2)=13→N;   L(11)+K(10)=21→V;
O(14)+L(11)=25→Z → Ciphertext: EQNVZ
• Perfect secrecy justification: for every ciphertext C and plaintext P, P(plaintext=P |
ciphertext=C) = P(plaintext=P) → no information leaked.
• Condition: key must be truly random, at least as long as the message, used only once,
and kept secret.
• Limitation: impractical for large messages due to key length requirement and secure
distribution problem.
CO- b. State Euler's theorem. Using Euler’s theorem, compute 7120 mod 13.   [05]
2;   • Euler's theorem: if gcd (a,n)=1, then aφ(n) ≡ 1 (mod n).
BL-   • φ (13) = 12 (13 is prime). So 712 ≡ 1 (mod 13).
2   • 7120 = 7(12×10) = (712)10 ≡ 110 = 1 (mod 13).
• Final answer: 7120 mod 13 = 1.
• State relationship between Euler's theorem and Fermat's little theorem (special case
when n is prime).
********** 1 **********
--- page 2 ---
CO- c. Differentiate between Rabin and RSA cryptosystems   [05]
2;
BL-   Rabin Cryptosystem   RSA Cryptosystem
2
Based on the difficulty
Based on the difficulty of
of computing the e-th
Mathematical   computing square roots modulo a
root modulo a
Foundation   composite number (equivalent to
composite number
integer factorization)
(RSA problem)
Decryption yields
Decryption produces four possible
a unique
Decryption   plaintexts; requires additional
plaintext when
Uniqueness   redundancy to identify the correct
standard padding is
one
used
Slower encryption
Encryption   Faster encryption (single modular   (exponentiation with
Speed   squaring operation: C=M2mod n   public exponent e,
typically 65537)
No formal proof that
breaking RSA is
Provably reducible to the
Security   equivalent to
factorization problem—breaking
Reduction   factoring; RSA
Rabin is equivalent to factoring nn
problem may be easier
than factoring
Widely deployed in
Rarely used in practice due to   SSL/TLS, PGP, SSH,
Practical   decryption ambiguity and   and digital signatures
Usage   vulnerability to chosen-ciphertext   with standardized
attacks without proper padding   padding (OAEP,
PKCS#1)
CO- d. Explain the Rail Fence cipher with a neat zig-zag diagram. Encrypt the plaintext [05]
1;   “CRYPTOGRAPHY IS FUN” using a 3-rail fence (ignore spaces during encryption)
BL-   and write the resulting ciphertext
2   • Rail Fence cipher: a transposition cipher that writes plaintext diagonally across a
number of 'rails' then reads off row by row.
********** 2 **********
--- page 3 ---
Q2
CO- a. Explain the Simple Substitution Cipher. Using the substitution key table below, [10]
1;   encrypt the plaintext "NETWORK SECURITY" and then decrypt the resulting
BL-   ciphertext to verify the original message. Show all steps.
3   Plaintext: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
• Simple Substitution Cipher: each plaintext letter is mapped one-to-one to a unique
ciphertext letter using a fixed substitution alphabet.
********** 3 **********
--- page 4 ---
• Award marks for correct key table, encryption steps, and decryption verification.
CO- b. Describe the attacks on block ciphers (any 5)   [10]
3;   1. Differential Cryptanalysis
BL-   Description:
2
A chosen-plaintext attack that analyzes how differences in input pairs affect
differences in output pairs. By tracing the propagation of differences through the
cipher rounds, cryptanalysts can recover key bits.
Method:
- Select pairs of plaintexts with a fixed XOR difference
- Encrypt both and observe the XOR difference of the ciphertexts
- Identify high-probability differential trails through the S-boxes
- Use these characteristics to deduce key information
Target: DES, FEAL (highly effective); modern ciphers like AES are designed to resist
it
2. Linear Cryptanalysis
Description:
A known-plaintext attack that constructs linear approximations between plaintext,
ciphertext, and key bits. It exploits linear relationships in the S-boxes to recover key
material.
Method:
- Find linear equations relating plaintext, ciphertext, and key bits with high probability
bias
- Collect a large number of known plaintext-ciphertext pairs
********** 4 **********
--- page 5 ---
- Use the linear approximations to solve for key bits via maximum likelihood
estimation
Target: DES (requires ~243 known plaintexts); modern ciphers use S-boxes designed
to minimize linear correlations
3. Side-Channel Attack
Description:
An attack that exploits physical characteristics of the implementation rather than
mathematical weaknesses. It does not attack the cipher algorithm itself but the
hardware or software executing it.
Variants:
- Timing attack: Measures encryption time variations to deduce key
- Power analysis: Monitors power consumption fluctuations (Simple Power Analysis,
Differential Power Analysis)
- Electromagnetic analysis: Captures EM emissions during computation
- Cache attack: Observes cache hit/miss patterns
Target: Any implemented cipher; particularly effective against embedded systems and
smart cards
4. Meet-in-the-Middle Attack
Description:
A time-memory trade-off attack that breaks ciphers using multiple independent keys
by storing intermediate values and matching from both ends.
Target: Double DES, 3DES (reduces security significantly); modern ciphers with
sufficient key length mitigate this
5. Padding Oracle Attack
Description:
An attack that exploits how a system responds to invalid padding during decryption.
By observing padding error messages or timing differences, an attacker can decrypt
ciphertexts without knowing the key.
Method:
- Works against CBC mode with PKCS#7 padding
- Attacker modifies ciphertext bytes and sends to the oracle
- Based on whether padding is valid or invalid, the attacker deduces intermediate state
byte by byte
- Once intermediate state is known, plaintext is recovered via XOR with previous
ciphertext block
Target: Systems using CBC mode with improper padding validation (e.g., Lucky13
attack on TLS, POODLE)
Q3
CO- a. Encrypt the message “KNOWLEDGE IS POWER” using the Playfair cipher with the [10]
1;   keyword “DIAMOND”. Construct the complete 5×5 key matrix (combine I/J, remove
BL-   spaces, insert ‘X’ between repeated letters and for padding if required) and show all
3   encryption steps clearly.
********** 5 **********
--- page 6 ---
Original: KNOWLEDGE IS POWER
Prepared: KN OW LE DG EI SP OW ER
Encrypted: GC IZ TL NQ BM UK IZ BT
Ciphertext: GCIZTLNQBMUKIZBT
CO- b. Explain the ElGamal cryptosystem. Given prime p = 31, generator g = 3, and private [10]
2;   key x = 17, compute the public key y. Encrypt the message M = 10 using random k
BL-   = 7. Then demonstrate the complete decryption process to recover M. Show all
3   modular arithmetic steps clearly.
********** 6 **********
--- page 7 ---
Public Key: y = 22
Ciphertext: (17, 24)
Decrypted Message: M = 10
Q4
CO- a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 11:   [10]
2;
i.   Compute n and Euler’s totient function ϕ(n).
BL-
ii.   Determine the private key exponent d using the Extended Euclidean
3   Algorithm.
iii.   Encrypt the message m = 7 to obtain the ciphertext c.
iv.   Decrypt the ciphertext c to recover the original message.
Show all intermediate steps and calculations clearly.
********** 7 **********
--- page 8 ---
CO- b. Encrypt the plaintext "EXAMINATION BEGINS TOMORROW" using the Vigenere [10]
1;   cipher with the keyword "PROTECT". Perform encryption and decryption. (Ignore
BL-   spaces during encryption)
3
Q5
CO- a. Using Elliptic Curve Cryptography, consider the elliptic curve   [10]
2;   E: y2=x3+2x+2 over F17 . Given the point P = (5, 1), compute 2P using point
BL-   doubling. Show all steps clearly.
3
• ECC: public-key cryptography based on algebraic structure of elliptic curves over
finite fields; y²=x³+ax+b over GF(p).
• Curve: y²=x³+x+6 over GF(11); G=(2,7) — verify: 7²=49≡5≡2³+2+6=16≡5 (mod
11) ✓.
• Point doubling 2G: λ = (3x₁²+a) × (2y₁)⁻¹ mod 11 = (3×4+1) × (14)⁻¹ mod 11 =
13×3⁻¹ mod 11 = 2×4=8 mod 11.
• x₃ = λ²−2x₁ mod 11 = 64−4=60 mod 11=5; y₃ = λ(x₁−x₃) −y₁ mod 11 = 8 (2−5) −7
= −31 mod 11 = 2.
• 2G = (5, 2).
• Point addition 3G = 2G + G: λ = (y₂−y₁) (x₂−x₁)⁻¹ mod 11 = (2−7)(5−2)⁻¹ =
(−5)(3⁻¹) = 6×4=24 mod 11=2.
• x₃=4−5−2=−3 mod 11=8; y₃=2(5−8) −2 = −8 mod 11=3.
********** 8 **********
--- page 9 ---
• 3G = (8, 3). Marks should be awarded for correct application of slope formula,
modular inverse, and point computation steps.
CO- b. Describe the Rabin cryptosystem. Explain the key generation, encryption, and [10]
2;   decryption steps with a suitable example.
BL-   • Rabin cryptosystem: public key encryption based on difficulty of computing square
3   roots mod n (equivalent to factoring).
• Key generation: choose large primes p, q with p≡q≡3(mod 4); n=p×q; public key=n,
private key=(p,q).
• Encryption: C = M² mod n.
• Decryption: compute 4 square roots of C mod n using Chinese Remainder Theorem;
correct plaintext identified using redundancy.
• Security: breaking Rabin ≡ factoring n; provably as hard as factoring (unlike RSA
which is unproven equivalent).
• Limitation: 4 possible plaintexts during decryption; redundancy needed to identify
correct one.
Q6
CO- a. Using the Diffie-Hellman key exchange, compute the shared secret key between Alice [10]
2;   and Bob given p = 41 and generator g = 7. Alice selects private key a = 9 and Bob
BL-   selects private key b = 14. Show all intermediate steps clearly and explain why an
3   eavesdropper cannot feasibly compute the shared secret.
CO- b. Describe the structure of the MD5 algorithm. Explain the message padding process, [10]
3;   initialization vector, the four auxiliary functions (F, G, H, I), and the compression
BL-   function. Illustrate the working with a clearly labeled block diagram showing how the
3   128-bit message digest is produced.
• MD5: produces 128-bit (16-byte) digest; designed by Ron Rivest (1992); processes
512-bit blocks.
• Message padding: append single '1' bit, then '0' bits until length ≡ 448 (mod 512);
append original message length as 64-bit little-endian integer.
• Initialization: four 32-bit state variables A, B, C, D initialized to: A=0x67452301,
B=0xEFCDAB89, C=0x98BADCFE, D=0x10325476.
• Four auxiliary functions: F(B, C,D)=(B∧C)∨(¬B∧D); G(B,C,D)=(B∧D)∨(C∧¬D);
H(B,C,D)=B⊕C⊕D; I(B,C,D)=C⊕(B∨¬D).
• 64 rounds in 4 groups of 16: rounds 1–16 use F; 17–32 use G; 33–48 use H; 49–64
use I.
********** 9 **********
--- page 10 ---
• Each round: T = B + left rotate (A + F/G/H/I (B, C, D) + M[k] + T[i], s); then (A,
B, C, D) rotated.
• Constants T[i] = floor(|sin(i+1) | × 2^32); message words M[k] accessed in different
orders per round group.
• Final digest = A||B||C||D (128 bits).
Block diagram showing chaining of 512-bit blocks required.
Q7   Write short notes on the following:
CO- a. Principles of Modern Cryptography (Confusion, Diffusion, Key Avalanche Effect)   [05]
1;   • Confusion: each ciphertext bit should depend on many key bits in a complex way →
BL-   achieved via substitution (S-Boxes).
2   • Diffusion: changing one plaintext bit should change approximately half of the
ciphertext bits → achieved via permutation/transposition (P-Boxes, MixColumns).
• Avalanche effect: small change in input (1 bit) causes ≥50% change in output bits.
• Shannon's two design principles: confusion and diffusion together resist both
differential and linear cryptanalysis.
• Example: AES achieves confusion via SubBytes (S-Box) and diffusion via
ShiftRows + MixColumns.
• Strict Avalanche Criterion (SAC): flipping any single input bit changes each output
bit with probability exactly 1/2.
CO- b. Galois Field GF(2⁸) and its role in AES   [05]
1;   • GF(2⁸): Galois Field with 2⁸=256 elements; elements are 8-bit polynomials over
BL-   GF(2) with coefficients 0 or 1.
2   • Irreducible polynomial used in AES: p(x) = x⁸+x⁴+x³+x+1 (0x11B).
• Addition in GF(2⁸) = XOR of bit patterns.
• Multiplication in GF(2⁸): polynomial multiplication mod p(x); multiply by x (=0x02)
= left shift, XOR 0x1B if carry.
• Role in AES: MixColumns uses GF(2⁸) arithmetic; SubBytes uses multiplicative
inverse in GF(2⁸).
• Example: 0x57 × 0x83 in GF(2⁸) = 0xC1 (show step-by-step polynomial
multiplication).
CO- c. Authority based KDC   [05]
3;   ▪ A trusted authority (e.g., Key Distribution Centre - KDC) generates and
BL-   distributes public keys.
2   ▪ The authority ensures that keys are securely exchanged between users.
Process:
▪ User A requests a public key from the authority.
▪ The authority verifies the request and provides User B’s public key.
▪ User A uses the key for encryption and secure communication.
Advantages:
• The trusted authority ensures the authenticity of the public keys.
• Reduces the risk of man-in-the-middle attacks.
Disadvantages:
********** 10 **********
--- page 11 ---
•   If the authority is compromised, all keys may be exposed.
• Requires a centralized authority that must be highly secure.
CO- d. Quadratic Congruence and Euler's Criterion with examples   [05]
2;
BL-   • Quadratic congruence: equation of form x² ≡ a (mod n); solution exists if a is a
2   quadratic residue mod n.
• Euler's criterion: a is a quadratic residue mod prime p if a ((p-1)/2) ≡ 1 (mod p); non-
residue gives −1.
• Example: Is 7 a QR mod 11
75 mod 11 = 74×7 = (72)2×7 = 49²×7 mod 11 = 4²×7=16×7=112 mod 11=2...
recalc: 75=16807 mod 11=75; 11×1528=16808; 16807mod11=10≡−1
→ 7 is NOT a QR mod 11.
• Example: Is 4 a QR mod 11?
45=1024 mod 11=1024−93×11=1 → yes; x²≡4(mod11) → x = 2 or 9.
• Significance: quadratic residuosity problem underpins Rabin cryptosystem and
Goldwasser-Micali encryption.
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 2bacbb4cd516

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CyberSecurity_7010/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Sem 10 Re-exam/Sem 4 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q.No.   Question / Answer   Marks
Q1   Answer in brief:
CO-1; a. Suppose that k = (9, 14) is a key in an Affine Cipher over mod 26. Write the decryption   [05]
BL-2   function in the form dk(y) = r y + s, where r, s ∈ Z₂₆. Show all modular arithmetic
steps clearly to determine r and s, ensuring 0 ≤ r, s ≤ 25
Affine Cipher:
encryption ek(x) = (a·x + b) mod 26 with key (a, b) = (9, 14).
Decryption: dk(y) = a⁻¹ (y − b) mod 26 = r·y + s mod 26.
Step 1 — Find r = a⁻¹ mod 26 = 9⁻¹ mod 26 using Extended Euclidean Algorithm:
26 = 2·9 + 8; 9 = 1·8 + 1; 8 = 8·1
Back-substitute: 1 = 9 − 1·8 = 9 − (26 − 2·9) = 3·9 − 26 → 9·3 ≡ 1 (mod 26) → r =
3.
Step 2 — Find s = −r·b mod 26 = −3·14 mod 26 = −42 mod 26 = −42 + 52 = 10. → s
= 10.
Decryption function: dk(y) = 3y + 10 (mod 26).
Verification: Encrypt x = 5 → e(5) = 9·5 + 14 = 59 mod 26 = 7. Decrypt y = 7 → 3·7
+ 10 = 31 mod 26 = 5.
CO-2; b. Define Euler's totient function ϕ(n). Compute ϕ(36) and ϕ(100), showing all steps   [05]
BL-2   clearly. Explain the significance of ϕ(n) in the RSA algorithm key generation process.
Euler's totient function ϕ(n): count of integers from 1 to n that are coprime to n
(gcd(k,n) = 1).
Formula for prime factorization n = p₁^a₁ · p₂^a₂ … : ϕ(n) = n · ∏(1 − 1/pᵢ)
ϕ(36): 36 = 2² × 3² → ϕ(36) = 36 · (1 − 1/2) · (1 − 1/3) = 36 · 1/2 · 2/3 = 12.
ϕ(100): 100 = 2² × 5² → ϕ(100) = 100 · (1 − 1/2) · (1 − 1/5) = 100 · 1/2 · 4/5 = 40.
********** 1 **********
--- page 2 ---
Significance in RSA: n = p·q (two large primes); ϕ(n) = (p−1)(q−1). Private key d is
found as e·d ≡ 1 (mod ϕ(n)). The security of RSA depends on the difficulty of
computing ϕ(n) without knowing the factorization of n.
CO-2; c. Compare Elliptic Curve Cryptography with the RSA algorithm highlighting at least   [05]
BL-2   five distinct comparison points.
Aspect   ECC   RSA
Mathematical   Elliptic curves over finite   Integer factorization
Basis   fields (ECDLP)   problem
Key Size for   ~256-bit key   ~3072-bit key
~128-bit
security
Performance   Faster computation, less   Slower due to large modular
bandwidth   exponentiation
Power/Memory Suitable for IoT/mobile   Higher resource
Efficiency   devices   requirements
Security Level Higher security per bit   Lower security per bit
per bit
Protocol Usage TLS 1.3, Bitcoin, ECDH,   SSL/TLS, PGP, S/MIME,
ECDSA   SSH
Key Exchange ECDH for key exchange   RSA key exchange (less
common now)
CO-1; d. Explain the Double transposition cipher with an example. Encrypt the plaintext   [05]
BL-2   'ATTACK AT DAWN' using two rounds of columnar transposition with keys 3142
and 2413 respectively, ignoring spaces, using 'X' for padding if required, and arranging
columns in ascending order of key digits. Show all steps clearly.
Double Transposition: applies columnar transposition twice using two keys for
stronger security than a single transposition.
Round 1 Encryption (Key = 3142)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
********** 2 **********
--- page 3 ---
Cipher after Round 1: TKAATNACDTAW
Round 2 Encryption (Key = 2413)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
Final Ciphertext: AAATTDACWKNT
(Award marks for correct grid layout, column ordering, and final ciphertext at each
stage.)
Q2
CO-1; a. The following ciphertext was encrypted using the Vigenere cipher with the keyword   [10]
BL-3   "MASTER": "YCVZM ROEHM CJZEY WMVJJ". Decrypt the message to determine
the original plaintext using A = 0 to Z = 25, ignoring spaces during computation (but
preserving them in the final answer), and show all steps clearly using the formula Di
= (Ci − Ki + 26) mod 26.
Plaintext (restoring spaces): MCDGI ACEPT YSNEG DIEXJ
(Award full marks for correct key alignment, correct application of decryption
formula, and final plaintext with spaces preserved.)
********** 3 **********
--- page 4 ---
CO-3; b. Describe the attacks on Stream ciphers (any 5)   [10]
BL-3   1. Known-Plaintext Attack: Attacker possesses plaintext-ciphertext pairs. XORing
them recovers the keystream directly (C ⊕ P = K). The keystream is then used to
decrypt other messages encrypted with the same key/nonce.
2. Key Reuse (Two-Time Pad) Attack: If the same keystream K is used twice — C1 =
P1⊕K and C2 = P2⊕K — then C1⊕C2 = P1⊕P2. Statistical analysis of natural
language redundancy can recover both plaintexts without knowing K.
3. Correlation Attack: Targets LFSR-based ciphers. Exploits statistical correlation
between individual LFSR outputs and the combined keystream. By testing each LFSR
independently, the attacker recovers initial states one at a time, reducing complexity
from 2(total bits) to sum of 2(LFSR bits).
4. Algebraic Attack: Represents the keystream generator as a system of multivariate
polynomial equations over GF(2). Solving the overdetermined system (using Groebner
bases or XL algorithm) reveals the internal state and secret key.
5. Time-Memory Trade-off Attack (Hellman / BSW): Precomputes a large table of
(keystream segment → initial state) pairs. During the online phase, observed
keystream segments are matched against the table to recover the key. Trades storage
and precomputation time for fast online key recovery.
6. Distinguishing Attack: Demonstrates that the cipher's output is statistically
distinguishable from a truly random sequence. Exploits biases in keystream (e.g.,
RC4's initial byte bias). Does not directly recover the key but breaks the
pseudorandomness security definition.
7. Fault Attack: Deliberately induces hardware or software errors during key stream
generation. Comparing correct and faulty outputs allows deduction of the internal state
or key bits. Particularly effective against hardware-implemented ciphers.
(Award 2 marks each for any 5 well-explained attacks.)
Q3
CO-1; a. The following ciphertext was encrypted using the Playfair cipher with keyword   [10]
BL-3   ‘CRYPTO’: ‘FQAUDKCR’.
Construct the 5×5 key matrix (combine I/J, remove duplicate letters, and fill the
remaining alphabets), then decrypt the message by applying standard Playfair rules,
ignoring spaces and removing filler ‘X’ where appropriate. Show all steps clearly.
Step 1: Preprocess Keyword
CRYPTOGRAPHY → C R Y P T O
Step 2: Construct 5×5 Key Matrix (I/J combined)
Step 3: Prepare Ciphertext
Ciphertext: FQAUDKCR
Digraphs: FQ | AU | DK | CR
********** 4 **********
--- page 5 ---
Step 4: Apply Decryption Rules
• Same row → shift left
• Same column → shift up
• Rectangle → swap columns
Step 5: Decryption Table
Step 6: Combine Plaintext
IL OV EI TC
Final Plaintext: ILOVEITC
(Award 4 marks for correct matrix, 4 marks for correct pairing and rule application, 2
marks for final plaintext.)
CO-2; b. Design a Linear Feedback Shift Register (LFSR) with 4 cells where the feedback   [10]
BL-3   function is: b₄ = b₁ ⊕ b₂ ⊕ b₃. Using initial seed 1011, generate the first twelve output
bits. Display the state of all cells at each clock cycle in a table. Determine the period
of the sequence and comment on whether it is a maximal-length sequence.
LFSR: 4 cells, feedback: b₄ = b₁ ⊕ b₂ ⊕ b₃, initial seed = [b₁,b₂,b₃,b₄] = [1,0,1,1]
At each clock: shift left (b₁←b₂, b₂←b₃, b₃←b₄), compute new b₄ = old b₁ ⊕ b₂ ⊕ b₃,
output = old b₁.
Cycle   b₁   b₂   b₃   b₄   Output
(b₁)
Seed   1   0   1   1   -
1   0   1   1   0   1
2   1   1   0   0   0
3   1   0   0   1   1
4   0   0   1   1   0
5   0   1   1   1   0
6   1   1   1   1   1
7   1   1   1   0   1
8   1   1   0   1   1
9   1   0   1   0   1
10   0   1   0   1   0
11   1   0   1   1   1
12   0   1   1   0   0
Output sequence (first 12 bits): 1 0 1 1 0 1 1 1 1 0 1 0 ...
Period determination: The state [1,0,1,1] recurs after 15 clock cycles → Period = 15.
********** 5 **********
--- page 6 ---
Maximal-length sequence: For a 4-bit LFSR, maximum possible period = 2⁴ − 1 = 15.
Since the observed period equals 15, this IS a maximal-length sequence (m-sequence).
The characteristic polynomial x⁴ + x³ + x² + 1 is primitive over GF(2).
Q4
CO-2; a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 5, compute   [10]
BL-3   n and ϕ(n), determine the private key d using the Extended Euclidean Algorithm,
encrypt the message m = 2, and decrypt the resulting ciphertext to recover the
original message. Show all steps clearly, including verification that ed ≡ 1 mod ϕ(n)
CO-1; b. Explain Hill Cipher. Given a 2×2 key matrix, encrypt the message 'MATH'. Then   [10]
BL-3   demonstrate the complete decryption process to recover the plaintext. Show all matrix
operations and modular arithmetic steps clearly. (Convert letters to numbers with A=0,
B=1, ..., Z=25.)
Hill Cipher: polygraphic substitution cipher using linear algebra. Plaintext is divided
into n-letter blocks and multiplied by an n×n invertible key matrix K mod 26.
Decryption uses K⁻¹ mod 26.
Blocks:
Encryption C = K·P mod 26:
Ciphertext: KYAV
Decryption — Find K⁻¹ mod 26:
det(K) = 3·5 − 3·2 = 9. Find 9⁻¹ mod 26: 9·3 = 27 ≡ 1 (mod 26) → 9⁻¹ = 3.
********** 6 **********
--- page 7 ---
Decrypt
→ M, A
→ T, H
Decrypted plaintext: MATH
Q5
CO-2; a. Explain the ElGamal cryptosystem. Given prime p = 29, generator g = 2, and private   [10]
BL-3   key x = 12, compute the public key y. Encrypt the message M = 6 using random k =
5. Then demonstrate the complete decryption process to recover M. Show all modular
arithmetic steps clearly.
ElGamal cryptosystem: public-key encryption based on the Discrete Logarithm
Problem (DLP). Security relies on the computational difficulty of finding x given g^x
mod p.
CO-2; b. Apply the Extended Euclidean Algorithm to compute gcd(481, 221) and find integers   [10]
BL-3   s and t such that 481s + 221t = gcd(481, 221). Using this result, solve the linear
congruence 221x ≡ 13 (mod 481). Show all steps clearly.
Extended Euclidean Algorithm:
********** 7 **********
--- page 8 ---
Back-substitution:
13 = 39 − 1·26
= 39 − 1·(221 − 5·39) = 6·39 − 221
= 6·(481 − 2·221) − 221 = 6·481 − 13·221
So s = 6, t = −13: 481·(6) + 221·(−13) = 2886 − 2873 = 13. ✓
Solving 221x ≡ 13 (mod 481):
Since gcd(221,481) = 13 and 13 | 13, solutions exist. Number of solutions = 13.
Divide through by 13: 17x ≡ 1 (mod 37).
From above: 221·(−13) ≡ 13 (mod 481), so 17·(−13) ≡ 1 (mod 37), i.e. 17·(37−13) =
17·24 = 408 = 11·37+1 ≡ 1. So 17⁻¹ = 24 mod 37.
One solution: x₀ = 24 (mod 37).
All 13 solutions mod 481: x = 24 + 37k for k = 0, 1, 2, ..., 12.
i.e., x ∈ {24, 61, 98, 135, 172, 209, 246, 283, 320, 357, 394, 431, 468} (mod 481).
Q6
CO-2; a. Using the Diffie-Hellman key exchange, given prime p = 53 and generator g = 3, Party   [10]
BL-3   A selects private key a = 8 and Party B selects private key b = 17. Compute both public
keys and the shared secret key using modular arithmetic and explain the security basis
of the protocol. Show all steps clearly.
Diffie-Hellman allows two parties to establish a shared secret over an insecure channel
without prior key exchange.
Public parameters: prime p = 53, generator g = 3.
Party A's Public Key A = ga mod p = 38 mod 53, A = 42.
Party B's Public Key B = gb mod p = 317 mod 53, B = 45.
Shared Secret (Alice computes): S = Ba mod p = 458 mod 53 = 13.
Shared Secret (Bob computes): S = Ab mod p = 4217 mod 53 = 13.
Shared Secret S = 13. (Both parties compute the same value.)
Security Basis: The Discrete Logarithm Problem — given ga mod p and gb mod p,
computing g (ab) mod p requires solving the Discrete Log Problem, which is
computationally infeasible for large primes (~2048 bits). An eavesdropper seeing
A=42 and B=45 cannot recover a or b efficiently.
CO-3; b. Describe the structure of the SHA-256 algorithm. Explain the message padding   [10]
BL-3   process and the construction of the message schedule, the role of the eight working
variables along with the initial hash values, and the functioning of the 64 rounds.
********** 8 **********
--- page 9 ---
Illustrate the overall working with a clearly labelled block diagram showing how the
final 256-bit message digest is produced.
SHA-256: member of the SHA-2 family; produces a 256-bit (32-byte) message digest;
processes data in 512-bit blocks; widely used in TLS, certificates, and blockchains.
1. Message Padding: Append bit '1' after the message, then '0' bits until message length
≡ 448 (mod 512). Append the original message length as a 64-bit big-endian integer.
Total padded length is a multiple of 512 bits.
2. Message Schedule (W array): Parse each 512-bit block into 16 words W₀–W₁₅ (32
bits each). Extend to 64 words:
Wᵢ = σ₁(Wᵢ₋₂) + Wᵢ₋₇ + σ₀(Wᵢ₋₁₅) + Wᵢ₋₁₆ for i = 16 to 63
σ₀(x) = ROTR²(x) ⊕ ROTR¹⁸(x) ⊕ SHR³(x); σ₁(x) = ROTR¹⁷(x) ⊕ ROTR¹⁹(x) ⊕
SHR¹⁰(x)
3. Initial Hash Values (H₀–H₇): First 32 bits of the fractional parts of the square roots
of the first 8 prime numbers (2, 3, 5, 7, 11, 13, 17, 19).
H₀=6a09e667,   H₁=bb67ae85,   H₂=3c6ef372,   H₃=a54ff53a,   H₄=510e527f,
H₅=9b05688c, H₆=1f83d9ab, H₇=5be0cd19
4. Eight Working Variables a,b,c,d,e,f,g,h initialized to H₀–H₇.
5. 64 Rounds — Each round i uses constant K[i] (first 32 bits of cube roots of first 64
primes) and W[i]:
Ch(e,f,g) = (e∧f)⊕(¬e∧g); Maj(a,b,c) = (a∧b)⊕(a∧c)⊕(b∧c)
Σ₀(a)   =   ROTR²(a)⊕ROTR¹³(a)⊕ROTR²²(a);   Σ₁(e)   =
ROTR⁶(e)⊕ROTR¹¹(e)⊕ROTR²⁵(e)
T₁ = h + Σ₁(e) + Ch(e,f,g) + K[i] + W[i]; T₂ = Σ₀(a) + Maj(a,b,c)
Update: h←g; g←f; f←e; e←d+T₁; d←c; c←b; b←a; a←T₁+T₂
6. Final Digest: After all rounds, add working variables to H₀–H₇. Concatenate
H₀||H₁||...||H₇ → 256-bit digest.
▪ abcde = (e + Process P + S5[a] + W[t] + K[t]),a,S30(b),c,d
where a, b , c , d , e = chaining variables
Process P = non-linear operation
St = Circular left shift of 32-bit sub-block by t bits
W[t] = 32-bit derived from current 32-bit sub-block
K[t] = One of the five additive constants
Block diagram:
********** 9 **********
--- page 10 ---
Q7   Write short notes on the following:
CO-1; a. Goals of Cryptography   [05]
BL-2   1. Confidentiality: Ensures that information is accessible only to those authorized to
access it. Achieved through symmetric (AES) or asymmetric (RSA, ECC) encryption
algorithms.
2. Data Integrity: Guarantees that data has not been altered or tampered with during
transmission or storage. Achieved via cryptographic hash functions (SHA-256) and
MACs (HMAC).
3. Authentication: Verifies the identity of communicating entities. Achieved through
digital signatures (RSA-PSS, ECDSA), certificates (X.509), and challenge-response
protocols.
4. Non-repudiation: Prevents a party from denying having performed an action (e.g.,
sending a message or signing a document). Provided by asymmetric digital signatures
using a private key only the sender holds.
5. Access Control: Ensures only authorized parties can access specific resources.
Supported by key management, capability tokens, and cryptographic access policies.
6. Availability: Guarantees that authorized users can access systems and data when
needed. Cryptography supports this by preventing unauthorized access that could
cause disruption.
CO-2; b. Square Root Test   [05]
BL-2   Square Root Test (Trial Division): A primality testing method based on the fact that if
n is composite, it must have a factor p ≤ √n.
Algorithm:
1. To test if n is prime, check whether n is divisible by any integer d from 2 to ⌊√n⌋.
2. If any such d divides n evenly (n mod d = 0), then n is composite and d is a factor.
3. If no such d is found, n is prime.
Optimisation: Only test prime values of d up to √n (Sieve of Eratosthenes).
********** 10 **********
--- page 11 ---
Example — Test n = 97 for primality:
√97 ≈ 9.85, so check primes ≤ 9: {2, 3, 5, 7}.
97 ÷ 2 = 48.5 (no); 97 ÷ 3 = 32.33 (no); 97 ÷ 5 = 19.4 (no); 97 ÷ 7 = 13.86 (no).
No factor found → 97 is prime. ✓
CO-3; c. HMAC (Hash-Based Message Authentication Code) – construction, security   [05]
BL-2   properties
HMAC: A cryptographic construction that combines a cryptographic hash function H
with a secret key K to provide both message authentication and integrity verification.
Construction: HMAC(K, m) = H( (K ⊕ opad) || H( (K ⊕ ipad) || m ) )
where opad = 0x5c5c...5c (block-size bytes), ipad = 0x3636...36 (block-size bytes).
Steps:
1. Pad key K to the hash block size (or hash K first if K is longer than block size).
2. XOR padded key with ipad; append message m; compute inner hash H₁ = H(K⊕ipad
|| m).
3. XOR padded key with opad; append H₁; compute outer hash = H(K⊕opad || H₁).
This is the HMAC tag.
Security Properties:
• Message Authentication: Only parties holding the secret key K can generate or verify
the tag.
• Integrity: Any modification to message m changes the HMAC tag (with
overwhelming probability).
• Resistance to Length-Extension Attacks: Unlike plain H(K||m), the double-hashing
structure prevents attackers from extending the message without knowing K.
• Provable Security: If H is a pseudorandom function (PRF), HMAC is also a PRF,
providing strong theoretical guarantees.
Applications: TLS/SSL record layer, JWT (JSON Web Tokens), IPsec authentication,
API authentication tokens.
CO-2; d. Fermat's Primality Test – algorithm, example (test n = 97 with base a = 2)   [05]
BL-2   Fermat's Primality Test: A probabilistic primality test based on Fermat's Little
Theorem.
Fermat's Little Theorem: If p is prime and gcd(a,p) = 1, then a(p−1) ≡ 1 (mod p).
Algorithm:
1. Choose a random base a with 1 < a < n−1.
2. Compute a^(n−1) mod n using fast modular exponentiation.
3. If a^(n−1) ≢ 1 (mod n): n is COMPOSITE (Fermat witness found).
4. If a^(n−1) ≡ 1 (mod n): n is probably prime (repeat with different bases to increase
confidence).
Example — Test n = 97 with base a = 2: Compute 296 mod 97:
26=64; 212=642=4096 mod 97=22; 224=222=484 mod 97=96; 248=962=9216 mod 97:
9216−94·97=9216−9118=98 mod 97=1; 296=(248)2=12=1 mod 97.
296 ≡ 1 (mod 97) → 97 is probably prime. (97 is indeed prime.)
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 35077f448c5d

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_IT_7041/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Sem 10 Re-exam/Sem 4 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q.No.   Question / Answer   Marks
Q1   Answer in brief:
CO-1; a. Suppose that k = (9, 14) is a key in an Affine Cipher over mod 26. Write the decryption   [05]
BL-2   function in the form dk(y) = r y + s, where r, s ∈ Z₂₆. Show all modular arithmetic
steps clearly to determine r and s, ensuring 0 ≤ r, s ≤ 25
Affine Cipher:
encryption ek(x) = (a·x + b) mod 26 with key (a, b) = (9, 14).
Decryption: dk(y) = a⁻¹ (y − b) mod 26 = r·y + s mod 26.
Step 1 — Find r = a⁻¹ mod 26 = 9⁻¹ mod 26 using Extended Euclidean Algorithm:
26 = 2·9 + 8; 9 = 1·8 + 1; 8 = 8·1
Back-substitute: 1 = 9 − 1·8 = 9 − (26 − 2·9) = 3·9 − 26 → 9·3 ≡ 1 (mod 26) → r =
3.
Step 2 — Find s = −r·b mod 26 = −3·14 mod 26 = −42 mod 26 = −42 + 52 = 10. → s
= 10.
Decryption function: dk(y) = 3y + 10 (mod 26).
Verification: Encrypt x = 5 → e(5) = 9·5 + 14 = 59 mod 26 = 7. Decrypt y = 7 → 3·7
+ 10 = 31 mod 26 = 5.
CO-2; b. Define Euler's totient function ϕ(n). Compute ϕ(36) and ϕ(100), showing all steps   [05]
BL-2   clearly. Explain the significance of ϕ(n) in the RSA algorithm key generation process.
Euler's totient function ϕ(n): count of integers from 1 to n that are coprime to n
(gcd(k,n) = 1).
Formula for prime factorization n = p₁^a₁ · p₂^a₂ … : ϕ(n) = n · ∏(1 − 1/pᵢ)
ϕ(36): 36 = 2² × 3² → ϕ(36) = 36 · (1 − 1/2) · (1 − 1/3) = 36 · 1/2 · 2/3 = 12.
ϕ(100): 100 = 2² × 5² → ϕ(100) = 100 · (1 − 1/2) · (1 − 1/5) = 100 · 1/2 · 4/5 = 40.
********** 1 **********
--- page 2 ---
Significance in RSA: n = p·q (two large primes); ϕ(n) = (p−1)(q−1). Private key d is
found as e·d ≡ 1 (mod ϕ(n)). The security of RSA depends on the difficulty of
computing ϕ(n) without knowing the factorization of n.
CO-2; c. Compare Elliptic Curve Cryptography with the RSA algorithm highlighting at least   [05]
BL-2   five distinct comparison points.
Aspect   ECC   RSA
Mathematical   Elliptic curves over finite   Integer factorization
Basis   fields (ECDLP)   problem
Key Size for   ~256-bit key   ~3072-bit key
~128-bit
security
Performance   Faster computation, less   Slower due to large modular
bandwidth   exponentiation
Power/Memory Suitable for IoT/mobile   Higher resource
Efficiency   devices   requirements
Security Level Higher security per bit   Lower security per bit
per bit
Protocol Usage TLS 1.3, Bitcoin, ECDH,   SSL/TLS, PGP, S/MIME,
ECDSA   SSH
Key Exchange ECDH for key exchange   RSA key exchange (less
common now)
CO-1; d. Explain the Double transposition cipher with an example. Encrypt the plaintext   [05]
BL-2   'ATTACK AT DAWN' using two rounds of columnar transposition with keys 3142
and 2413 respectively, ignoring spaces, using 'X' for padding if required, and arranging
columns in ascending order of key digits. Show all steps clearly.
Double Transposition: applies columnar transposition twice using two keys for
stronger security than a single transposition.
Round 1 Encryption (Key = 3142)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
********** 2 **********
--- page 3 ---
Cipher after Round 1: TKAATNACDTAW
Round 2 Encryption (Key = 2413)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
Final Ciphertext: AAATTDACWKNT
(Award marks for correct grid layout, column ordering, and final ciphertext at each
stage.)
Q2
CO-1; a. The following ciphertext was encrypted using the Vigenere cipher with the keyword   [10]
BL-3   "MASTER": "YCVZM ROEHM CJZEY WMVJJ". Decrypt the message to determine
the original plaintext using A = 0 to Z = 25, ignoring spaces during computation (but
preserving them in the final answer), and show all steps clearly using the formula Di
= (Ci − Ki + 26) mod 26.
Plaintext (restoring spaces): MCDGI ACEPT YSNEG DIEXJ
(Award full marks for correct key alignment, correct application of decryption
formula, and final plaintext with spaces preserved.)
********** 3 **********
--- page 4 ---
CO-3; b. Describe the attacks on Stream ciphers (any 5)   [10]
BL-3   1. Known-Plaintext Attack: Attacker possesses plaintext-ciphertext pairs. XORing
them recovers the keystream directly (C ⊕ P = K). The keystream is then used to
decrypt other messages encrypted with the same key/nonce.
2. Key Reuse (Two-Time Pad) Attack: If the same keystream K is used twice — C1 =
P1⊕K and C2 = P2⊕K — then C1⊕C2 = P1⊕P2. Statistical analysis of natural
language redundancy can recover both plaintexts without knowing K.
3. Correlation Attack: Targets LFSR-based ciphers. Exploits statistical correlation
between individual LFSR outputs and the combined keystream. By testing each LFSR
independently, the attacker recovers initial states one at a time, reducing complexity
from 2(total bits) to sum of 2(LFSR bits).
4. Algebraic Attack: Represents the keystream generator as a system of multivariate
polynomial equations over GF(2). Solving the overdetermined system (using Groebner
bases or XL algorithm) reveals the internal state and secret key.
5. Time-Memory Trade-off Attack (Hellman / BSW): Precomputes a large table of
(keystream segment → initial state) pairs. During the online phase, observed
keystream segments are matched against the table to recover the key. Trades storage
and precomputation time for fast online key recovery.
6. Distinguishing Attack: Demonstrates that the cipher's output is statistically
distinguishable from a truly random sequence. Exploits biases in keystream (e.g.,
RC4's initial byte bias). Does not directly recover the key but breaks the
pseudorandomness security definition.
7. Fault Attack: Deliberately induces hardware or software errors during key stream
generation. Comparing correct and faulty outputs allows deduction of the internal state
or key bits. Particularly effective against hardware-implemented ciphers.
(Award 2 marks each for any 5 well-explained attacks.)
Q3
CO-1; a. The following ciphertext was encrypted using the Playfair cipher with keyword   [10]
BL-3   ‘CRYPTO’: ‘FQAUDKCR’.
Construct the 5×5 key matrix (combine I/J, remove duplicate letters, and fill the
remaining alphabets), then decrypt the message by applying standard Playfair rules,
ignoring spaces and removing filler ‘X’ where appropriate. Show all steps clearly.
Step 1: Preprocess Keyword
CRYPTOGRAPHY → C R Y P T O
Step 2: Construct 5×5 Key Matrix (I/J combined)
Step 3: Prepare Ciphertext
Ciphertext: FQAUDKCR
Digraphs: FQ | AU | DK | CR
********** 4 **********
--- page 5 ---
Step 4: Apply Decryption Rules
• Same row → shift left
• Same column → shift up
• Rectangle → swap columns
Step 5: Decryption Table
Step 6: Combine Plaintext
IL OV EI TC
Final Plaintext: ILOVEITC
(Award 4 marks for correct matrix, 4 marks for correct pairing and rule application, 2
marks for final plaintext.)
CO-2; b. Design a Linear Feedback Shift Register (LFSR) with 4 cells where the feedback   [10]
BL-3   function is: b₄ = b₁ ⊕ b₂ ⊕ b₃. Using initial seed 1011, generate the first twelve output
bits. Display the state of all cells at each clock cycle in a table. Determine the period
of the sequence and comment on whether it is a maximal-length sequence.
LFSR: 4 cells, feedback: b₄ = b₁ ⊕ b₂ ⊕ b₃, initial seed = [b₁,b₂,b₃,b₄] = [1,0,1,1]
At each clock: shift left (b₁←b₂, b₂←b₃, b₃←b₄), compute new b₄ = old b₁ ⊕ b₂ ⊕ b₃,
output = old b₁.
Cycle   b₁   b₂   b₃   b₄   Output
(b₁)
Seed   1   0   1   1   -
1   0   1   1   0   1
2   1   1   0   0   0
3   1   0   0   1   1
4   0   0   1   1   0
5   0   1   1   1   0
6   1   1   1   1   1
7   1   1   1   0   1
8   1   1   0   1   1
9   1   0   1   0   1
10   0   1   0   1   0
11   1   0   1   1   1
12   0   1   1   0   0
Output sequence (first 12 bits): 1 0 1 1 0 1 1 1 1 0 1 0 ...
Period determination: The state [1,0,1,1] recurs after 15 clock cycles → Period = 15.
********** 5 **********
--- page 6 ---
Maximal-length sequence: For a 4-bit LFSR, maximum possible period = 2⁴ − 1 = 15.
Since the observed period equals 15, this IS a maximal-length sequence (m-sequence).
The characteristic polynomial x⁴ + x³ + x² + 1 is primitive over GF(2).
Q4
CO-2; a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 5, compute   [10]
BL-3   n and ϕ(n), determine the private key d using the Extended Euclidean Algorithm,
encrypt the message m = 2, and decrypt the resulting ciphertext to recover the
original message. Show all steps clearly, including verification that ed ≡ 1 mod ϕ(n)
CO-1; b. Explain Hill Cipher. Given a 2×2 key matrix, encrypt the message 'MATH'. Then   [10]
BL-3   demonstrate the complete decryption process to recover the plaintext. Show all matrix
operations and modular arithmetic steps clearly. (Convert letters to numbers with A=0,
B=1, ..., Z=25.)
Hill Cipher: polygraphic substitution cipher using linear algebra. Plaintext is divided
into n-letter blocks and multiplied by an n×n invertible key matrix K mod 26.
Decryption uses K⁻¹ mod 26.
Blocks:
Encryption C = K·P mod 26:
Ciphertext: KYAV
Decryption — Find K⁻¹ mod 26:
det(K) = 3·5 − 3·2 = 9. Find 9⁻¹ mod 26: 9·3 = 27 ≡ 1 (mod 26) → 9⁻¹ = 3.
********** 6 **********
--- page 7 ---
Decrypt
→ M, A
→ T, H
Decrypted plaintext: MATH
Q5
CO-2; a. Explain the ElGamal cryptosystem. Given prime p = 29, generator g = 2, and private   [10]
BL-3   key x = 12, compute the public key y. Encrypt the message M = 6 using random k =
5. Then demonstrate the complete decryption process to recover M. Show all modular
arithmetic steps clearly.
ElGamal cryptosystem: public-key encryption based on the Discrete Logarithm
Problem (DLP). Security relies on the computational difficulty of finding x given g^x
mod p.
CO-2; b. Apply the Extended Euclidean Algorithm to compute gcd(481, 221) and find integers   [10]
BL-3   s and t such that 481s + 221t = gcd(481, 221). Using this result, solve the linear
congruence 221x ≡ 13 (mod 481). Show all steps clearly.
Extended Euclidean Algorithm:
********** 7 **********
--- page 8 ---
Back-substitution:
13 = 39 − 1·26
= 39 − 1·(221 − 5·39) = 6·39 − 221
= 6·(481 − 2·221) − 221 = 6·481 − 13·221
So s = 6, t = −13: 481·(6) + 221·(−13) = 2886 − 2873 = 13. ✓
Solving 221x ≡ 13 (mod 481):
Since gcd(221,481) = 13 and 13 | 13, solutions exist. Number of solutions = 13.
Divide through by 13: 17x ≡ 1 (mod 37).
From above: 221·(−13) ≡ 13 (mod 481), so 17·(−13) ≡ 1 (mod 37), i.e. 17·(37−13) =
17·24 = 408 = 11·37+1 ≡ 1. So 17⁻¹ = 24 mod 37.
One solution: x₀ = 24 (mod 37).
All 13 solutions mod 481: x = 24 + 37k for k = 0, 1, 2, ..., 12.
i.e., x ∈ {24, 61, 98, 135, 172, 209, 246, 283, 320, 357, 394, 431, 468} (mod 481).
Q6
CO-2; a. Using the Diffie-Hellman key exchange, given prime p = 53 and generator g = 3, Party   [10]
BL-3   A selects private key a = 8 and Party B selects private key b = 17. Compute both public
keys and the shared secret key using modular arithmetic and explain the security basis
of the protocol. Show all steps clearly.
Diffie-Hellman allows two parties to establish a shared secret over an insecure channel
without prior key exchange.
Public parameters: prime p = 53, generator g = 3.
Party A's Public Key A = ga mod p = 38 mod 53, A = 42.
Party B's Public Key B = gb mod p = 317 mod 53, B = 45.
Shared Secret (Alice computes): S = Ba mod p = 458 mod 53 = 13.
Shared Secret (Bob computes): S = Ab mod p = 4217 mod 53 = 13.
Shared Secret S = 13. (Both parties compute the same value.)
Security Basis: The Discrete Logarithm Problem — given ga mod p and gb mod p,
computing g (ab) mod p requires solving the Discrete Log Problem, which is
computationally infeasible for large primes (~2048 bits). An eavesdropper seeing
A=42 and B=45 cannot recover a or b efficiently.
CO-3; b. Describe the structure of the SHA-256 algorithm. Explain the message padding   [10]
BL-3   process and the construction of the message schedule, the role of the eight working
variables along with the initial hash values, and the functioning of the 64 rounds.
********** 8 **********
--- page 9 ---
Illustrate the overall working with a clearly labelled block diagram showing how the
final 256-bit message digest is produced.
SHA-256: member of the SHA-2 family; produces a 256-bit (32-byte) message digest;
processes data in 512-bit blocks; widely used in TLS, certificates, and blockchains.
1. Message Padding: Append bit '1' after the message, then '0' bits until message length
≡ 448 (mod 512). Append the original message length as a 64-bit big-endian integer.
Total padded length is a multiple of 512 bits.
2. Message Schedule (W array): Parse each 512-bit block into 16 words W₀–W₁₅ (32
bits each). Extend to 64 words:
Wᵢ = σ₁(Wᵢ₋₂) + Wᵢ₋₇ + σ₀(Wᵢ₋₁₅) + Wᵢ₋₁₆ for i = 16 to 63
σ₀(x) = ROTR²(x) ⊕ ROTR¹⁸(x) ⊕ SHR³(x); σ₁(x) = ROTR¹⁷(x) ⊕ ROTR¹⁹(x) ⊕
SHR¹⁰(x)
3. Initial Hash Values (H₀–H₇): First 32 bits of the fractional parts of the square roots
of the first 8 prime numbers (2, 3, 5, 7, 11, 13, 17, 19).
H₀=6a09e667,   H₁=bb67ae85,   H₂=3c6ef372,   H₃=a54ff53a,   H₄=510e527f,
H₅=9b05688c, H₆=1f83d9ab, H₇=5be0cd19
4. Eight Working Variables a,b,c,d,e,f,g,h initialized to H₀–H₇.
5. 64 Rounds — Each round i uses constant K[i] (first 32 bits of cube roots of first 64
primes) and W[i]:
Ch(e,f,g) = (e∧f)⊕(¬e∧g); Maj(a,b,c) = (a∧b)⊕(a∧c)⊕(b∧c)
Σ₀(a)   =   ROTR²(a)⊕ROTR¹³(a)⊕ROTR²²(a);   Σ₁(e)   =
ROTR⁶(e)⊕ROTR¹¹(e)⊕ROTR²⁵(e)
T₁ = h + Σ₁(e) + Ch(e,f,g) + K[i] + W[i]; T₂ = Σ₀(a) + Maj(a,b,c)
Update: h←g; g←f; f←e; e←d+T₁; d←c; c←b; b←a; a←T₁+T₂
6. Final Digest: After all rounds, add working variables to H₀–H₇. Concatenate
H₀||H₁||...||H₇ → 256-bit digest.
▪ abcde = (e + Process P + S5[a] + W[t] + K[t]),a,S30(b),c,d
where a, b , c , d , e = chaining variables
Process P = non-linear operation
St = Circular left shift of 32-bit sub-block by t bits
W[t] = 32-bit derived from current 32-bit sub-block
K[t] = One of the five additive constants
Block diagram:
********** 9 **********
--- page 10 ---
Q7   Write short notes on the following:
CO-1; a. Goals of Cryptography   [05]
BL-2   1. Confidentiality: Ensures that information is accessible only to those authorized to
access it. Achieved through symmetric (AES) or asymmetric (RSA, ECC) encryption
algorithms.
2. Data Integrity: Guarantees that data has not been altered or tampered with during
transmission or storage. Achieved via cryptographic hash functions (SHA-256) and
MACs (HMAC).
3. Authentication: Verifies the identity of communicating entities. Achieved through
digital signatures (RSA-PSS, ECDSA), certificates (X.509), and challenge-response
protocols.
4. Non-repudiation: Prevents a party from denying having performed an action (e.g.,
sending a message or signing a document). Provided by asymmetric digital signatures
using a private key only the sender holds.
5. Access Control: Ensures only authorized parties can access specific resources.
Supported by key management, capability tokens, and cryptographic access policies.
6. Availability: Guarantees that authorized users can access systems and data when
needed. Cryptography supports this by preventing unauthorized access that could
cause disruption.
CO-2; b. Square Root Test   [05]
BL-2   Square Root Test (Trial Division): A primality testing method based on the fact that if
n is composite, it must have a factor p ≤ √n.
Algorithm:
1. To test if n is prime, check whether n is divisible by any integer d from 2 to ⌊√n⌋.
2. If any such d divides n evenly (n mod d = 0), then n is composite and d is a factor.
3. If no such d is found, n is prime.
Optimisation: Only test prime values of d up to √n (Sieve of Eratosthenes).
********** 10 **********
--- page 11 ---
Example — Test n = 97 for primality:
√97 ≈ 9.85, so check primes ≤ 9: {2, 3, 5, 7}.
97 ÷ 2 = 48.5 (no); 97 ÷ 3 = 32.33 (no); 97 ÷ 5 = 19.4 (no); 97 ÷ 7 = 13.86 (no).
No factor found → 97 is prime. ✓
CO-3; c. HMAC (Hash-Based Message Authentication Code) – construction, security   [05]
BL-2   properties
HMAC: A cryptographic construction that combines a cryptographic hash function H
with a secret key K to provide both message authentication and integrity verification.
Construction: HMAC(K, m) = H( (K ⊕ opad) || H( (K ⊕ ipad) || m ) )
where opad = 0x5c5c...5c (block-size bytes), ipad = 0x3636...36 (block-size bytes).
Steps:
1. Pad key K to the hash block size (or hash K first if K is longer than block size).
2. XOR padded key with ipad; append message m; compute inner hash H₁ = H(K⊕ipad
|| m).
3. XOR padded key with opad; append H₁; compute outer hash = H(K⊕opad || H₁).
This is the HMAC tag.
Security Properties:
• Message Authentication: Only parties holding the secret key K can generate or verify
the tag.
• Integrity: Any modification to message m changes the HMAC tag (with
overwhelming probability).
• Resistance to Length-Extension Attacks: Unlike plain H(K||m), the double-hashing
structure prevents attackers from extending the message without knowing K.
• Provable Security: If H is a pseudorandom function (PRF), HMAC is also a PRF,
providing strong theoretical guarantees.
Applications: TLS/SSL record layer, JWT (JSON Web Tokens), IPsec authentication,
API authentication tokens.
CO-2; d. Fermat's Primality Test – algorithm, example (test n = 97 with base a = 2)   [05]
BL-2   Fermat's Primality Test: A probabilistic primality test based on Fermat's Little
Theorem.
Fermat's Little Theorem: If p is prime and gcd(a,p) = 1, then a(p−1) ≡ 1 (mod p).
Algorithm:
1. Choose a random base a with 1 < a < n−1.
2. Compute a^(n−1) mod n using fast modular exponentiation.
3. If a^(n−1) ≢ 1 (mod n): n is COMPOSITE (Fermat witness found).
4. If a^(n−1) ≡ 1 (mod n): n is probably prime (repeat with different bases to increase
confidence).
Example — Test n = 97 with base a = 2: Compute 296 mod 97:
26=64; 212=642=4096 mod 97=22; 224=222=484 mod 97=96; 248=962=9216 mod 97:
9216−94·97=9216−9118=98 mod 97=1; 296=(248)2=12=1 mod 97.
296 ≡ 1 (mod 97) → 97 is probably prime. (97 is indeed prime.)
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 003fd5e2e182

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_IT_7037/Introduction to Cryptography/ANS_Introduction to Cryptography(702IT0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: II / III / V/Sem 10 Re-exam/Sem 4 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Cryptography
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q.No.   Question / Answer   Marks
Q1   Answer in brief:
CO-1; a. Suppose that k = (9, 14) is a key in an Affine Cipher over mod 26. Write the decryption   [05]
BL-2   function in the form dk(y) = r y + s, where r, s ∈ Z₂₆. Show all modular arithmetic
steps clearly to determine r and s, ensuring 0 ≤ r, s ≤ 25
Affine Cipher:
encryption ek(x) = (a·x + b) mod 26 with key (a, b) = (9, 14).
Decryption: dk(y) = a⁻¹ (y − b) mod 26 = r·y + s mod 26.
Step 1 — Find r = a⁻¹ mod 26 = 9⁻¹ mod 26 using Extended Euclidean Algorithm:
26 = 2·9 + 8; 9 = 1·8 + 1; 8 = 8·1
Back-substitute: 1 = 9 − 1·8 = 9 − (26 − 2·9) = 3·9 − 26 → 9·3 ≡ 1 (mod 26) → r =
3.
Step 2 — Find s = −r·b mod 26 = −3·14 mod 26 = −42 mod 26 = −42 + 52 = 10. → s
= 10.
Decryption function: dk(y) = 3y + 10 (mod 26).
Verification: Encrypt x = 5 → e(5) = 9·5 + 14 = 59 mod 26 = 7. Decrypt y = 7 → 3·7
+ 10 = 31 mod 26 = 5.
CO-2; b. Define Euler's totient function ϕ(n). Compute ϕ(36) and ϕ(100), showing all steps   [05]
BL-2   clearly. Explain the significance of ϕ(n) in the RSA algorithm key generation process.
Euler's totient function ϕ(n): count of integers from 1 to n that are coprime to n
(gcd(k,n) = 1).
Formula for prime factorization n = p₁^a₁ · p₂^a₂ … : ϕ(n) = n · ∏(1 − 1/pᵢ)
ϕ(36): 36 = 2² × 3² → ϕ(36) = 36 · (1 − 1/2) · (1 − 1/3) = 36 · 1/2 · 2/3 = 12.
ϕ(100): 100 = 2² × 5² → ϕ(100) = 100 · (1 − 1/2) · (1 − 1/5) = 100 · 1/2 · 4/5 = 40.
********** 1 **********
--- page 2 ---
Significance in RSA: n = p·q (two large primes); ϕ(n) = (p−1)(q−1). Private key d is
found as e·d ≡ 1 (mod ϕ(n)). The security of RSA depends on the difficulty of
computing ϕ(n) without knowing the factorization of n.
CO-2; c. Compare Elliptic Curve Cryptography with the RSA algorithm highlighting at least   [05]
BL-2   five distinct comparison points.
Aspect   ECC   RSA
Mathematical   Elliptic curves over finite   Integer factorization
Basis   fields (ECDLP)   problem
Key Size for   ~256-bit key   ~3072-bit key
~128-bit
security
Performance   Faster computation, less   Slower due to large modular
bandwidth   exponentiation
Power/Memory Suitable for IoT/mobile   Higher resource
Efficiency   devices   requirements
Security Level Higher security per bit   Lower security per bit
per bit
Protocol Usage TLS 1.3, Bitcoin, ECDH,   SSL/TLS, PGP, S/MIME,
ECDSA   SSH
Key Exchange ECDH for key exchange   RSA key exchange (less
common now)
CO-1; d. Explain the Double transposition cipher with an example. Encrypt the plaintext   [05]
BL-2   'ATTACK AT DAWN' using two rounds of columnar transposition with keys 3142
and 2413 respectively, ignoring spaces, using 'X' for padding if required, and arranging
columns in ascending order of key digits. Show all steps clearly.
Double Transposition: applies columnar transposition twice using two keys for
stronger security than a single transposition.
Round 1 Encryption (Key = 3142)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
********** 2 **********
--- page 3 ---
Cipher after Round 1: TKAATNACDTAW
Round 2 Encryption (Key = 2413)
Step 1: Matrix Formation
Step 2: Column-wise Extraction (Ascending Key Order: 1 → 2 → 3 → 4)
Final Ciphertext: AAATTDACWKNT
(Award marks for correct grid layout, column ordering, and final ciphertext at each
stage.)
Q2
CO-1; a. The following ciphertext was encrypted using the Vigenere cipher with the keyword   [10]
BL-3   "MASTER": "YCVZM ROEHM CJZEY WMVJJ". Decrypt the message to determine
the original plaintext using A = 0 to Z = 25, ignoring spaces during computation (but
preserving them in the final answer), and show all steps clearly using the formula Di
= (Ci − Ki + 26) mod 26.
Plaintext (restoring spaces): MCDGI ACEPT YSNEG DIEXJ
(Award full marks for correct key alignment, correct application of decryption
formula, and final plaintext with spaces preserved.)
********** 3 **********
--- page 4 ---
CO-3; b. Describe the attacks on Stream ciphers (any 5)   [10]
BL-3   1. Known-Plaintext Attack: Attacker possesses plaintext-ciphertext pairs. XORing
them recovers the keystream directly (C ⊕ P = K). The keystream is then used to
decrypt other messages encrypted with the same key/nonce.
2. Key Reuse (Two-Time Pad) Attack: If the same keystream K is used twice — C1 =
P1⊕K and C2 = P2⊕K — then C1⊕C2 = P1⊕P2. Statistical analysis of natural
language redundancy can recover both plaintexts without knowing K.
3. Correlation Attack: Targets LFSR-based ciphers. Exploits statistical correlation
between individual LFSR outputs and the combined keystream. By testing each LFSR
independently, the attacker recovers initial states one at a time, reducing complexity
from 2(total bits) to sum of 2(LFSR bits).
4. Algebraic Attack: Represents the keystream generator as a system of multivariate
polynomial equations over GF(2). Solving the overdetermined system (using Groebner
bases or XL algorithm) reveals the internal state and secret key.
5. Time-Memory Trade-off Attack (Hellman / BSW): Precomputes a large table of
(keystream segment → initial state) pairs. During the online phase, observed
keystream segments are matched against the table to recover the key. Trades storage
and precomputation time for fast online key recovery.
6. Distinguishing Attack: Demonstrates that the cipher's output is statistically
distinguishable from a truly random sequence. Exploits biases in keystream (e.g.,
RC4's initial byte bias). Does not directly recover the key but breaks the
pseudorandomness security definition.
7. Fault Attack: Deliberately induces hardware or software errors during key stream
generation. Comparing correct and faulty outputs allows deduction of the internal state
or key bits. Particularly effective against hardware-implemented ciphers.
(Award 2 marks each for any 5 well-explained attacks.)
Q3
CO-1; a. The following ciphertext was encrypted using the Playfair cipher with keyword   [10]
BL-3   ‘CRYPTO’: ‘FQAUDKCR’.
Construct the 5×5 key matrix (combine I/J, remove duplicate letters, and fill the
remaining alphabets), then decrypt the message by applying standard Playfair rules,
ignoring spaces and removing filler ‘X’ where appropriate. Show all steps clearly.
Step 1: Preprocess Keyword
CRYPTOGRAPHY → C R Y P T O
Step 2: Construct 5×5 Key Matrix (I/J combined)
Step 3: Prepare Ciphertext
Ciphertext: FQAUDKCR
Digraphs: FQ | AU | DK | CR
********** 4 **********
--- page 5 ---
Step 4: Apply Decryption Rules
• Same row → shift left
• Same column → shift up
• Rectangle → swap columns
Step 5: Decryption Table
Step 6: Combine Plaintext
IL OV EI TC
Final Plaintext: ILOVEITC
(Award 4 marks for correct matrix, 4 marks for correct pairing and rule application, 2
marks for final plaintext.)
CO-2; b. Design a Linear Feedback Shift Register (LFSR) with 4 cells where the feedback   [10]
BL-3   function is: b₄ = b₁ ⊕ b₂ ⊕ b₃. Using initial seed 1011, generate the first twelve output
bits. Display the state of all cells at each clock cycle in a table. Determine the period
of the sequence and comment on whether it is a maximal-length sequence.
LFSR: 4 cells, feedback: b₄ = b₁ ⊕ b₂ ⊕ b₃, initial seed = [b₁,b₂,b₃,b₄] = [1,0,1,1]
At each clock: shift left (b₁←b₂, b₂←b₃, b₃←b₄), compute new b₄ = old b₁ ⊕ b₂ ⊕ b₃,
output = old b₁.
Cycle   b₁   b₂   b₃   b₄   Output
(b₁)
Seed   1   0   1   1   -
1   0   1   1   0   1
2   1   1   0   0   0
3   1   0   0   1   1
4   0   0   1   1   0
5   0   1   1   1   0
6   1   1   1   1   1
7   1   1   1   0   1
8   1   1   0   1   1
9   1   0   1   0   1
10   0   1   0   1   0
11   1   0   1   1   1
12   0   1   1   0   0
Output sequence (first 12 bits): 1 0 1 1 0 1 1 1 1 0 1 0 ...
Period determination: The state [1,0,1,1] recurs after 15 clock cycles → Period = 15.
********** 5 **********
--- page 6 ---
Maximal-length sequence: For a 4-bit LFSR, maximum possible period = 2⁴ − 1 = 15.
Since the observed period equals 15, this IS a maximal-length sequence (m-sequence).
The characteristic polynomial x⁴ + x³ + x² + 1 is primitive over GF(2).
Q4
CO-2; a. Using the RSA algorithm, given p = 13, q = 17, and public exponent e = 5, compute   [10]
BL-3   n and ϕ(n), determine the private key d using the Extended Euclidean Algorithm,
encrypt the message m = 2, and decrypt the resulting ciphertext to recover the
original message. Show all steps clearly, including verification that ed ≡ 1 mod ϕ(n)
CO-1; b. Explain Hill Cipher. Given a 2×2 key matrix, encrypt the message 'MATH'. Then   [10]
BL-3   demonstrate the complete decryption process to recover the plaintext. Show all matrix
operations and modular arithmetic steps clearly. (Convert letters to numbers with A=0,
B=1, ..., Z=25.)
Hill Cipher: polygraphic substitution cipher using linear algebra. Plaintext is divided
into n-letter blocks and multiplied by an n×n invertible key matrix K mod 26.
Decryption uses K⁻¹ mod 26.
Blocks:
Encryption C = K·P mod 26:
Ciphertext: KYAV
Decryption — Find K⁻¹ mod 26:
det(K) = 3·5 − 3·2 = 9. Find 9⁻¹ mod 26: 9·3 = 27 ≡ 1 (mod 26) → 9⁻¹ = 3.
********** 6 **********
--- page 7 ---
Decrypt
→ M, A
→ T, H
Decrypted plaintext: MATH
Q5
CO-2; a. Explain the ElGamal cryptosystem. Given prime p = 29, generator g = 2, and private   [10]
BL-3   key x = 12, compute the public key y. Encrypt the message M = 6 using random k =
5. Then demonstrate the complete decryption process to recover M. Show all modular
arithmetic steps clearly.
ElGamal cryptosystem: public-key encryption based on the Discrete Logarithm
Problem (DLP). Security relies on the computational difficulty of finding x given g^x
mod p.
CO-2; b. Apply the Extended Euclidean Algorithm to compute gcd(481, 221) and find integers   [10]
BL-3   s and t such that 481s + 221t = gcd(481, 221). Using this result, solve the linear
congruence 221x ≡ 13 (mod 481). Show all steps clearly.
Extended Euclidean Algorithm:
********** 7 **********
--- page 8 ---
Back-substitution:
13 = 39 − 1·26
= 39 − 1·(221 − 5·39) = 6·39 − 221
= 6·(481 − 2·221) − 221 = 6·481 − 13·221
So s = 6, t = −13: 481·(6) + 221·(−13) = 2886 − 2873 = 13. ✓
Solving 221x ≡ 13 (mod 481):
Since gcd(221,481) = 13 and 13 | 13, solutions exist. Number of solutions = 13.
Divide through by 13: 17x ≡ 1 (mod 37).
From above: 221·(−13) ≡ 13 (mod 481), so 17·(−13) ≡ 1 (mod 37), i.e. 17·(37−13) =
17·24 = 408 = 11·37+1 ≡ 1. So 17⁻¹ = 24 mod 37.
One solution: x₀ = 24 (mod 37).
All 13 solutions mod 481: x = 24 + 37k for k = 0, 1, 2, ..., 12.
i.e., x ∈ {24, 61, 98, 135, 172, 209, 246, 283, 320, 357, 394, 431, 468} (mod 481).
Q6
CO-2; a. Using the Diffie-Hellman key exchange, given prime p = 53 and generator g = 3, Party   [10]
BL-3   A selects private key a = 8 and Party B selects private key b = 17. Compute both public
keys and the shared secret key using modular arithmetic and explain the security basis
of the protocol. Show all steps clearly.
Diffie-Hellman allows two parties to establish a shared secret over an insecure channel
without prior key exchange.
Public parameters: prime p = 53, generator g = 3.
Party A's Public Key A = ga mod p = 38 mod 53, A = 42.
Party B's Public Key B = gb mod p = 317 mod 53, B = 45.
Shared Secret (Alice computes): S = Ba mod p = 458 mod 53 = 13.
Shared Secret (Bob computes): S = Ab mod p = 4217 mod 53 = 13.
Shared Secret S = 13. (Both parties compute the same value.)
Security Basis: The Discrete Logarithm Problem — given ga mod p and gb mod p,
computing g (ab) mod p requires solving the Discrete Log Problem, which is
computationally infeasible for large primes (~2048 bits). An eavesdropper seeing
A=42 and B=45 cannot recover a or b efficiently.
CO-3; b. Describe the structure of the SHA-256 algorithm. Explain the message padding   [10]
BL-3   process and the construction of the message schedule, the role of the eight working
variables along with the initial hash values, and the functioning of the 64 rounds.
********** 8 **********
--- page 9 ---
Illustrate the overall working with a clearly labelled block diagram showing how the
final 256-bit message digest is produced.
SHA-256: member of the SHA-2 family; produces a 256-bit (32-byte) message digest;
processes data in 512-bit blocks; widely used in TLS, certificates, and blockchains.
1. Message Padding: Append bit '1' after the message, then '0' bits until message length
≡ 448 (mod 512). Append the original message length as a 64-bit big-endian integer.
Total padded length is a multiple of 512 bits.
2. Message Schedule (W array): Parse each 512-bit block into 16 words W₀–W₁₅ (32
bits each). Extend to 64 words:
Wᵢ = σ₁(Wᵢ₋₂) + Wᵢ₋₇ + σ₀(Wᵢ₋₁₅) + Wᵢ₋₁₆ for i = 16 to 63
σ₀(x) = ROTR²(x) ⊕ ROTR¹⁸(x) ⊕ SHR³(x); σ₁(x) = ROTR¹⁷(x) ⊕ ROTR¹⁹(x) ⊕
SHR¹⁰(x)
3. Initial Hash Values (H₀–H₇): First 32 bits of the fractional parts of the square roots
of the first 8 prime numbers (2, 3, 5, 7, 11, 13, 17, 19).
H₀=6a09e667,   H₁=bb67ae85,   H₂=3c6ef372,   H₃=a54ff53a,   H₄=510e527f,
H₅=9b05688c, H₆=1f83d9ab, H₇=5be0cd19
4. Eight Working Variables a,b,c,d,e,f,g,h initialized to H₀–H₇.
5. 64 Rounds — Each round i uses constant K[i] (first 32 bits of cube roots of first 64
primes) and W[i]:
Ch(e,f,g) = (e∧f)⊕(¬e∧g); Maj(a,b,c) = (a∧b)⊕(a∧c)⊕(b∧c)
Σ₀(a)   =   ROTR²(a)⊕ROTR¹³(a)⊕ROTR²²(a);   Σ₁(e)   =
ROTR⁶(e)⊕ROTR¹¹(e)⊕ROTR²⁵(e)
T₁ = h + Σ₁(e) + Ch(e,f,g) + K[i] + W[i]; T₂ = Σ₀(a) + Maj(a,b,c)
Update: h←g; g←f; f←e; e←d+T₁; d←c; c←b; b←a; a←T₁+T₂
6. Final Digest: After all rounds, add working variables to H₀–H₇. Concatenate
H₀||H₁||...||H₇ → 256-bit digest.
▪ abcde = (e + Process P + S5[a] + W[t] + K[t]),a,S30(b),c,d
where a, b , c , d , e = chaining variables
Process P = non-linear operation
St = Circular left shift of 32-bit sub-block by t bits
W[t] = 32-bit derived from current 32-bit sub-block
K[t] = One of the five additive constants
Block diagram:
********** 9 **********
--- page 10 ---
Q7   Write short notes on the following:
CO-1; a. Goals of Cryptography   [05]
BL-2   1. Confidentiality: Ensures that information is accessible only to those authorized to
access it. Achieved through symmetric (AES) or asymmetric (RSA, ECC) encryption
algorithms.
2. Data Integrity: Guarantees that data has not been altered or tampered with during
transmission or storage. Achieved via cryptographic hash functions (SHA-256) and
MACs (HMAC).
3. Authentication: Verifies the identity of communicating entities. Achieved through
digital signatures (RSA-PSS, ECDSA), certificates (X.509), and challenge-response
protocols.
4. Non-repudiation: Prevents a party from denying having performed an action (e.g.,
sending a message or signing a document). Provided by asymmetric digital signatures
using a private key only the sender holds.
5. Access Control: Ensures only authorized parties can access specific resources.
Supported by key management, capability tokens, and cryptographic access policies.
6. Availability: Guarantees that authorized users can access systems and data when
needed. Cryptography supports this by preventing unauthorized access that could
cause disruption.
CO-2; b. Square Root Test   [05]
BL-2   Square Root Test (Trial Division): A primality testing method based on the fact that if
n is composite, it must have a factor p ≤ √n.
Algorithm:
1. To test if n is prime, check whether n is divisible by any integer d from 2 to ⌊√n⌋.
2. If any such d divides n evenly (n mod d = 0), then n is composite and d is a factor.
3. If no such d is found, n is prime.
Optimisation: Only test prime values of d up to √n (Sieve of Eratosthenes).
********** 10 **********
--- page 11 ---
Example — Test n = 97 for primality:
√97 ≈ 9.85, so check primes ≤ 9: {2, 3, 5, 7}.
97 ÷ 2 = 48.5 (no); 97 ÷ 3 = 32.33 (no); 97 ÷ 5 = 19.4 (no); 97 ÷ 7 = 13.86 (no).
No factor found → 97 is prime. ✓
CO-3; c. HMAC (Hash-Based Message Authentication Code) – construction, security   [05]
BL-2   properties
HMAC: A cryptographic construction that combines a cryptographic hash function H
with a secret key K to provide both message authentication and integrity verification.
Construction: HMAC(K, m) = H( (K ⊕ opad) || H( (K ⊕ ipad) || m ) )
where opad = 0x5c5c...5c (block-size bytes), ipad = 0x3636...36 (block-size bytes).
Steps:
1. Pad key K to the hash block size (or hash K first if K is longer than block size).
2. XOR padded key with ipad; append message m; compute inner hash H₁ = H(K⊕ipad
|| m).
3. XOR padded key with opad; append H₁; compute outer hash = H(K⊕opad || H₁).
This is the HMAC tag.
Security Properties:
• Message Authentication: Only parties holding the secret key K can generate or verify
the tag.
• Integrity: Any modification to message m changes the HMAC tag (with
overwhelming probability).
• Resistance to Length-Extension Attacks: Unlike plain H(K||m), the double-hashing
structure prevents attackers from extending the message without knowing K.
• Provable Security: If H is a pseudorandom function (PRF), HMAC is also a PRF,
providing strong theoretical guarantees.
Applications: TLS/SSL record layer, JWT (JSON Web Tokens), IPsec authentication,
API authentication tokens.
CO-2; d. Fermat's Primality Test – algorithm, example (test n = 97 with base a = 2)   [05]
BL-2   Fermat's Primality Test: A probabilistic primality test based on Fermat's Little
Theorem.
Fermat's Little Theorem: If p is prime and gcd(a,p) = 1, then a(p−1) ≡ 1 (mod p).
Algorithm:
1. Choose a random base a with 1 < a < n−1.
2. Compute a^(n−1) mod n using fast modular exponentiation.
3. If a^(n−1) ≢ 1 (mod n): n is COMPOSITE (Fermat witness found).
4. If a^(n−1) ≡ 1 (mod n): n is probably prime (repeat with different bases to increase
confidence).
Example — Test n = 97 with base a = 2: Compute 296 mod 97:
26=64; 212=642=4096 mod 97=22; 224=222=484 mod 97=96; 248=962=9216 mod 97:
9216−94·97=9216−9118=98 mod 97=1; 296=(248)2=12=1 mod 97.
296 ≡ 1 (mod 97) → 97 is probably prime. (97 is indeed prime.)
********** 11 **********
````
