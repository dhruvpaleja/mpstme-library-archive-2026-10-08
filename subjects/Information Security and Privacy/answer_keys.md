# Information Security and Privacy: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper a2ca1b502674

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_DS_7009/Information Security and Privacy/ANS_Information Security and Privacy(702DB0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: text (8 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Information Security and Privacy
Date: 05 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Answer Sheet:
Q1 c. State Layers of TCP/IP Model
Q1 b. Features ipv6
********** 1 **********
--- page 2 ---
Ans :
Q1 a. In a Caesar Cipher with a shift of 3, what will be the encrypted message for the plaintext “DATA”?
Options:
A) GDWD
B) ABCD
C) FATA
D) DDTD
ANSWER : A) GDWD
Q1 d. What is encryption?
Encryption is the method by which information is converted into secret code that hides the information's true
meaning. The science of encrypting and decrypting information is called cryptography.
In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext.
********** 2 **********

[Text in pictures on this page, read by OCR]
IPv6

Deployed 1998

128-bit IP address

Alphanumeric hexadecimal notation

50b2:6400::6c3a:b17d:0:10a9

Supports auto configuration
--- page 3 ---
● Cipher : The formulas used to encode and decode messages are called encryption algorithms
● Key : The variable, which is called a key, is what makes a cipher's output unique
Historically, it was used by militaries and governments.
In modern times, encryption is used to protect data stored on computers and storage devices, as well as data in
transit over networks.
Q2. A
Step 1️⃣: Convert plaintext to numbers
Using A=0, B=1, C=2, ..., Z=25
Letter Numeric
D   3
E   4
F   5
So the plaintext vector is:
3
𝑃= [ 4 ]
5
Step 2️⃣: Multiply by key matrix
𝐶= 𝐾× 𝑃
2 4 5   3
= [ 9 2 1 ] × [ 4 ]
3 8 7   5
Compute each element carefully:
1️⃣ 𝐶1 = 2 × 3 + 4 × 4 + 5 × 5 = 6 + 16 + 25 = 47
2️⃣ 𝐶2 = 9 × 3 + 2 × 4 + 1 × 5 = 27 + 8 + 5 = 40
3⃣ 𝐶3 = 3 × 3 + 8 × 4 + 7 × 5 = 9 + 32 + 35 = 76
47
𝐶= [ 40 ]
76
Step 3️⃣: Take mod 26
47mod  26 = 21
40mod  26 = 14
76mod  26 = 24
21
𝐶= [ 14 ]
24
Step 4️⃣: Convert numbers back to letters
Numeric Letter
21   V
14   O
********** 3 **********
--- page 4 ---
Numeric Letter
24   Y
✅ Ciphertext = “VOY”
✅ Final Answer:
Plaintext: DEF
2 4 5
Key Matrix: [ 9 2 1 ]
3 8 7
Ciphertext: VOY
Q2. B
The Hill cipher is a classic method of encryption that uses linear algebra to encipher messages. Invented by
Lester S. Hill in 1929, it's a polygraphic substitution cipher, which means it encrypts multiple letters at once.
This makes it more secure than simple substitution ciphers that encrypt letter by letter.
At its core, the Hill cipher uses a matrix as a key to transform blocks of plaintext letters into ciphertext. All the
mathematical operations are performed modulo 26, corresponding to the 26 letters of the alphabet.
Encryption Example
Let's encrypt the message "ACT" using the key "GYBNQKURP".
1. Assign numerical values to letters: First, we assign a number to each letter of the alphabet, starting
with A = 0, B = 1, and so on.
A B C D E F G H I J K L M
0 1 2 3 4 5 6 7 8 9 10 11 12
2. Export to Sheets
N O P Q R S T U V W X Y Z
13 14 15 16 17 18 19 20 21 22 23 24 25
3. Export to Sheets
4. Create the key matrix: The key "GYBNQKURP" is converted into a 3x3 matrix.
$ K = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} $
5. Convert the plaintext to a vector: The message "ACT" becomes a vector.
$ P = \begin{pmatrix} 0 \ 2 \ 19 \end{pmatrix} $
6. Multiply the key matrix by the plaintext vector:
$ C = K \cdot P = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} \begin{pmatrix} 0 \ 2
\ 19 \end{pmatrix} = \begin{pmatrix} (6 \cdot 0 + 24 \cdot 2 + 1 \cdot 19) \ (13 \cdot 0 + 16 \cdot 2 + 10 \cdot
19) \ (20 \cdot 0 + 17 \cdot 2 + 15 \cdot 19) \end{pmatrix} = \begin{pmatrix} 67 \ 222 \ 319 \end{pmatrix} $
7. Apply modulo 26: We take the result and apply modulo 26 to each element.
$ \begin{pmatrix} 67 \mod 26 \ 222 \mod 26 \ 319 \mod 26 \end{pmatrix} = \begin{pmatrix} 15 \ 14 \ 7
\end{pmatrix} $
8. Convert the numbers back to letters: The resulting numbers correspond to the letters "POH". So, the
ciphertext for "ACT" is "POH".
Decryption Example
********** 4 **********
--- page 5 ---
To decrypt the message, you need the inverse of the key matrix. Let's say we've calculated the inverse key
matrix () to be:
1. Convert the ciphertext to a vector: The ciphertext "POH" becomes a vector.
$ C = \begin{pmatrix} 15 \ 14 \ 7 \end{pmatrix} $
2. Multiply the inverse key matrix by the ciphertext vector:
$ P = K^{-1} \cdot C = \begin{pmatrix} 8 & 5 & 10 \ 21 & 8 & 21 \ 21 & 12 & 8 \end{pmatrix} \begin{pmatrix} 15
\ 14 \ 7 \end{pmatrix} = \begin{pmatrix} (8 \cdot 15 + 5 \cdot 14 + 10 \cdot 7) \ (21 \cdot 15 + 8 \cdot 14 + 21
\cdot 7) \ (21 \cdot 15 + 12 \cdot 14 + 8 \cdot 7) \end{pmatrix} = \begin{pmatrix} 260 \ 574 \ 539 \end{pmatrix}
$
3. Apply modulo 26:
$ \begin{pmatrix} 260 \mod 26 \ 574 \mod 26 \ 539 \mod 26 \end{pmatrix} = \begin{pmatrix} 0 \ 2 \ 19
\end{pmatrix} $
4. Convert the numbers back to letters: The resulting numbers correspond to the letters "ACT", which was
our original plaintext.
It's important to note that for a key to be valid in the Hill cipher, its determinant must not share any common
factors with 26 (other than 1). This ensures that an inverse of the key matrix exists, making decryption possible.
While the Hill cipher was a significant advancement in its time, it is vulnerable to known-plaintext attacks due
to its linear nature.
Q3. A
Q3 b
A symmetric cipher, also known as a symmetric-key algorithm, is a cryptographic system where the same key is
used for both encrypting and decrypting information. This shared secret is what makes the communication
secure. For a symmetric cipher to function, it needs five essential ingredients.
The 5 Essential Ingredients
1. Plaintext: This is the original, readable message or data that needs to be encrypted. It's the input to the
cipher. For example, if you wanted to securely send the message "MEET ME AT DAWN," this would be
your plaintext.
********** 5 **********

[Text in pictures on this page, read by OCR]
A B c

Feature IPv4 IPv6
Address Length 32-bit address 128-bit address
Address Format Decimal format (e.g., 192.168.0.1) Hexadecimal format (e.g., 2001:0db8::1)
Configuration Manual and DHCP configuration Auto-configuration and renumbering supported
Connection Integrity End-to-end integrity is unachievable End-to-end integrity is achievable
Security No builtin sea. extemal tools like IPSec is built-in for encryption and authentication
Fragmentation Performed by sender and routers Performed only by the sender
Flow Identification Not available Uses Flow Label field in header for packet flow
identification
Checksum Field Present Not present
Transmission Scheme Supports broadcast Uses multicast and anycast; no broadcast
Header Size Variable: 20-60 bytes Fixed: 40 bytes
Conversion Can be converted to IPv6 Not all IPV6 addresses can be converted to IPv4
Field Structure 4 fields separated by dots (.) 8 fields separated by colons (:)
Address Classes Has address classes (A, B, C, D, E) No concept of address classes
VLSM Support Supports vocewtst Subnet Does not support VLSM

Example 66.94.2913 2001:0000: 3238:DFE1 0063:0000:0000:FEFB
--- page 6 ---
2. Encryption Algorithm: This is the mathematical function or set of rules that transforms the plaintext
into ciphertext. It dictates exactly how the substitution and permutation of the data will occur.
3. Secret Key: The key is a piece of information (typically a string of numbers or characters) that is shared
between the sender and the receiver. It's a critical input to the encryption algorithm, as it determines
the specific transformation of the plaintext. The security of a symmetric cipher rests entirely on the
secrecy of this key.
4. Ciphertext: This is the scrambled, unreadable output from the encryption algorithm. It's the encrypted
version of the plaintext that can be transmitted over an insecure channel. An attacker who intercepts
the ciphertext without the secret key should not be able to understand the original message.
5. Decryption Algorithm: This is essentially the reverse of the encryption algorithm. It's the function that
takes the ciphertext and the same secret key to transform the data back into its original, readable
plaintext form.
In essence, the sender uses the secret key and the encryption algorithm to turn plaintext into ciphertext. The
receiver then uses the same secret key and the decryption algorithm to turn the ciphertext back into the
original plaintext.
Q5.
Feature   Symmetric Cryptography   Asymmetric Cryptography
Uses two keys – a public key for
Uses one single key for both
Definition   encryption and a private key for
encryption and decryption.
decryption.
Number of Keys   One key (shared secret).   Two keys (public & private).
Key   Same key for both encryption and   Different but mathematically
Relationship   decryption.   related keys.
Fast – less computationally   Slow – involves complex mathematical
Speed
intensive.   operations.
Depends on keeping the   Security depends on the difficulty of deriving
Security
shared key secret.   private key from public key.
Key   Needs a secure channel to   No need for secure sharing – public key
Distribution   share the secret key.   can be openly distributed.
Encryption   AES, DES, 3DES, Blowfish, Hill   RSA, DSA, ECC, Diffie-
Example   Cipher.   Hellman.
Data   Suitable for encrypting large   Suitable for small data, key exchange, or
Size   amounts of data.   authentication.
Use   File encryption, database   Digital signatures, key exchange, SSL/TLS,
Cases   encryption, VPNs.   authentication.
Example   Both sender and receiver   Sender encrypts with receiver’s public key,
Working   use the same key “K”.   receiver decrypts with private key.
Q4.
Keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it
determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the
word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
********** 6 **********
--- page 7 ---
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.
Q7.
Layers of the OSI Model
There are 7 layers in the OSI Model and each layer has its specific role in handling data. All the layers are
mentioned below:
● Physical Layer
● Data Link Layer
● Network Layer
● Transport Layer
● Session Layer
● Presentation Layer
● Application Layer
Application Layer: Applications create the data.
Presentation Layer: Data is formatted and encrypted.
Session Layer: Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically
Example:
********** 7 **********

[Text in pictures on this page, read by OCR]
Input :

Keyword : secret

Message : Zombie Here

Output :


Take the first example, we used

Plain Text: ABCDEFGHIJKLMNOPQRSTUVWXYZ

secret" keyword there.

When “secret” keyword is used, the new encrypting text becomes
Encrypting : SECRTABDFGHIJKLMNOPQUVWXYZ

This means ‘A’ means ‘S', 'B' means "E' and ‘'C' means ‘C' and so on.
Lets encode the given message “Zombie Here"

ZOMBIE HERE becomes ZLJEFT DTOT
--- page 8 ---
Step 1: Person A interacts with e-mail application like Gmail, outlook, etc. Writes his email to send. (This
happens at Application Layer).
Step 2: At Presentation Layer, Mail application prepares for data transmission like encrypting data and
formatting it for transmission.
Step 3: At Session Layer, there is a connection established between the sender and receiver on the
internet.
Step 4: At Transport Layer, Email data is broken into smaller segments. It adds sequence number and
error-checking information to maintain the reliability of the information.
Step 5: At Network Layer, addressing of packets is done in order to find the best route for transfer.
Step 6: At Data Link Layer, data packets are encapsulated into frames, then MAC address is added for
local devices and then it checks for error using error detection.
Step 7: At Physical Layer, Frames are transmitted in the form of electrical/ optical signals over a physical
network medium like ethernet cable or WiFi.
Q6.
Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting
a plain text into a cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a
= 0, b = 1️, c = 2️, … z = 2️5).
Method to take key: In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be
equal to the length of the plain text.
Encryption Algorithm:
1. Assign a number to each character of the plain-text and the key according to alphabetical order.
2. Add both the number (Corresponding plain-text character number and Key character number).
3. Subtract the number from 2️6 if the added number is greater than 2️6, if it isn’t then leave it.
********** 8 **********

[Text in pictures on this page, read by OCR]
Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm, we assign a number to each character of our plain text and key.

No: 170 12 18 22 @ 17 20 15 10
KEY; R AN CHO BABA
No: 17 @ 13 27 1410410

Now Bitwise XOR the number of Plain-Text and Key and after doing the XOR operation and subtraction operation (if
required), we will get the corresponding Cipher-Text character number.

CT-NO: @ @ 1 16 17 14 16 20 14 10

Since there are no numbers that are greater than or equal to 26 we do not have to subtract 26 from any of them.

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: A A BQ RO QUO K
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 40680dd9db90

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_DS_7052/Information Security and Privacy/ANS_Information Security and Privacy(702DB0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: text (8 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Information Security and Privacy
Date: 05 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Answer Sheet:
Q1 c. State Layers of TCP/IP Model
Q1 b. Features ipv6
********** 1 **********
--- page 2 ---
Ans :
Q1 a. In a Caesar Cipher with a shift of 3, what will be the encrypted message for the plaintext “DATA”?
Options:
A) GDWD
B) ABCD
C) FATA
D) DDTD
ANSWER : A) GDWD
Q1 d. What is encryption?
Encryption is the method by which information is converted into secret code that hides the information's true
meaning. The science of encrypting and decrypting information is called cryptography.
In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext.
********** 2 **********

[Text in pictures on this page, read by OCR]
IPv6

Deployed 1998

128-bit IP address

Alphanumeric hexadecimal notation

50b2:6400::6c3a:b17d:0:10a9

Supports auto configuration
--- page 3 ---
● Cipher : The formulas used to encode and decode messages are called encryption algorithms
● Key : The variable, which is called a key, is what makes a cipher's output unique
Historically, it was used by militaries and governments.
In modern times, encryption is used to protect data stored on computers and storage devices, as well as data in
transit over networks.
Q2. A
Step 1️⃣: Convert plaintext to numbers
Using A=0, B=1, C=2, ..., Z=25
Letter Numeric
D   3
E   4
F   5
So the plaintext vector is:
3
𝑃= [ 4 ]
5
Step 2️⃣: Multiply by key matrix
𝐶= 𝐾× 𝑃
2 4 5   3
= [ 9 2 1 ] × [ 4 ]
3 8 7   5
Compute each element carefully:
1️⃣ 𝐶1 = 2 × 3 + 4 × 4 + 5 × 5 = 6 + 16 + 25 = 47
2️⃣ 𝐶2 = 9 × 3 + 2 × 4 + 1 × 5 = 27 + 8 + 5 = 40
3⃣ 𝐶3 = 3 × 3 + 8 × 4 + 7 × 5 = 9 + 32 + 35 = 76
47
𝐶= [ 40 ]
76
Step 3️⃣: Take mod 26
47mod  26 = 21
40mod  26 = 14
76mod  26 = 24
21
𝐶= [ 14 ]
24
Step 4️⃣: Convert numbers back to letters
Numeric Letter
21   V
14   O
********** 3 **********
--- page 4 ---
Numeric Letter
24   Y
✅ Ciphertext = “VOY”
✅ Final Answer:
Plaintext: DEF
2 4 5
Key Matrix: [ 9 2 1 ]
3 8 7
Ciphertext: VOY
Q2. B
The Hill cipher is a classic method of encryption that uses linear algebra to encipher messages. Invented by
Lester S. Hill in 1929, it's a polygraphic substitution cipher, which means it encrypts multiple letters at once.
This makes it more secure than simple substitution ciphers that encrypt letter by letter.
At its core, the Hill cipher uses a matrix as a key to transform blocks of plaintext letters into ciphertext. All the
mathematical operations are performed modulo 26, corresponding to the 26 letters of the alphabet.
Encryption Example
Let's encrypt the message "ACT" using the key "GYBNQKURP".
1. Assign numerical values to letters: First, we assign a number to each letter of the alphabet, starting
with A = 0, B = 1, and so on.
A B C D E F G H I J K L M
0 1 2 3 4 5 6 7 8 9 10 11 12
2. Export to Sheets
N O P Q R S T U V W X Y Z
13 14 15 16 17 18 19 20 21 22 23 24 25
3. Export to Sheets
4. Create the key matrix: The key "GYBNQKURP" is converted into a 3x3 matrix.
$ K = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} $
5. Convert the plaintext to a vector: The message "ACT" becomes a vector.
$ P = \begin{pmatrix} 0 \ 2 \ 19 \end{pmatrix} $
6. Multiply the key matrix by the plaintext vector:
$ C = K \cdot P = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} \begin{pmatrix} 0 \ 2
\ 19 \end{pmatrix} = \begin{pmatrix} (6 \cdot 0 + 24 \cdot 2 + 1 \cdot 19) \ (13 \cdot 0 + 16 \cdot 2 + 10 \cdot
19) \ (20 \cdot 0 + 17 \cdot 2 + 15 \cdot 19) \end{pmatrix} = \begin{pmatrix} 67 \ 222 \ 319 \end{pmatrix} $
7. Apply modulo 26: We take the result and apply modulo 26 to each element.
$ \begin{pmatrix} 67 \mod 26 \ 222 \mod 26 \ 319 \mod 26 \end{pmatrix} = \begin{pmatrix} 15 \ 14 \ 7
\end{pmatrix} $
8. Convert the numbers back to letters: The resulting numbers correspond to the letters "POH". So, the
ciphertext for "ACT" is "POH".
Decryption Example
********** 4 **********
--- page 5 ---
To decrypt the message, you need the inverse of the key matrix. Let's say we've calculated the inverse key
matrix () to be:
1. Convert the ciphertext to a vector: The ciphertext "POH" becomes a vector.
$ C = \begin{pmatrix} 15 \ 14 \ 7 \end{pmatrix} $
2. Multiply the inverse key matrix by the ciphertext vector:
$ P = K^{-1} \cdot C = \begin{pmatrix} 8 & 5 & 10 \ 21 & 8 & 21 \ 21 & 12 & 8 \end{pmatrix} \begin{pmatrix} 15
\ 14 \ 7 \end{pmatrix} = \begin{pmatrix} (8 \cdot 15 + 5 \cdot 14 + 10 \cdot 7) \ (21 \cdot 15 + 8 \cdot 14 + 21
\cdot 7) \ (21 \cdot 15 + 12 \cdot 14 + 8 \cdot 7) \end{pmatrix} = \begin{pmatrix} 260 \ 574 \ 539 \end{pmatrix}
$
3. Apply modulo 26:
$ \begin{pmatrix} 260 \mod 26 \ 574 \mod 26 \ 539 \mod 26 \end{pmatrix} = \begin{pmatrix} 0 \ 2 \ 19
\end{pmatrix} $
4. Convert the numbers back to letters: The resulting numbers correspond to the letters "ACT", which was
our original plaintext.
It's important to note that for a key to be valid in the Hill cipher, its determinant must not share any common
factors with 26 (other than 1). This ensures that an inverse of the key matrix exists, making decryption possible.
While the Hill cipher was a significant advancement in its time, it is vulnerable to known-plaintext attacks due
to its linear nature.
Q3. A
Q3 b
A symmetric cipher, also known as a symmetric-key algorithm, is a cryptographic system where the same key is
used for both encrypting and decrypting information. This shared secret is what makes the communication
secure. For a symmetric cipher to function, it needs five essential ingredients.
The 5 Essential Ingredients
1. Plaintext: This is the original, readable message or data that needs to be encrypted. It's the input to the
cipher. For example, if you wanted to securely send the message "MEET ME AT DAWN," this would be
your plaintext.
********** 5 **********

[Text in pictures on this page, read by OCR]
A B c

Feature IPv4 IPv6
Address Length 32-bit address 128-bit address
Address Format Decimal format (e.g., 192.168.0.1) Hexadecimal format (e.g., 2001:0db8::1)
Configuration Manual and DHCP configuration Auto-configuration and renumbering supported
Connection Integrity End-to-end integrity is unachievable End-to-end integrity is achievable
Security No builtin sea. extemal tools like IPSec is built-in for encryption and authentication
Fragmentation Performed by sender and routers Performed only by the sender
Flow Identification Not available Uses Flow Label field in header for packet flow
identification
Checksum Field Present Not present
Transmission Scheme Supports broadcast Uses multicast and anycast; no broadcast
Header Size Variable: 20-60 bytes Fixed: 40 bytes
Conversion Can be converted to IPv6 Not all IPV6 addresses can be converted to IPv4
Field Structure 4 fields separated by dots (.) 8 fields separated by colons (:)
Address Classes Has address classes (A, B, C, D, E) No concept of address classes
VLSM Support Supports vocewtst Subnet Does not support VLSM

Example 66.94.2913 2001:0000: 3238:DFE1 0063:0000:0000:FEFB
--- page 6 ---
2. Encryption Algorithm: This is the mathematical function or set of rules that transforms the plaintext
into ciphertext. It dictates exactly how the substitution and permutation of the data will occur.
3. Secret Key: The key is a piece of information (typically a string of numbers or characters) that is shared
between the sender and the receiver. It's a critical input to the encryption algorithm, as it determines
the specific transformation of the plaintext. The security of a symmetric cipher rests entirely on the
secrecy of this key.
4. Ciphertext: This is the scrambled, unreadable output from the encryption algorithm. It's the encrypted
version of the plaintext that can be transmitted over an insecure channel. An attacker who intercepts
the ciphertext without the secret key should not be able to understand the original message.
5. Decryption Algorithm: This is essentially the reverse of the encryption algorithm. It's the function that
takes the ciphertext and the same secret key to transform the data back into its original, readable
plaintext form.
In essence, the sender uses the secret key and the encryption algorithm to turn plaintext into ciphertext. The
receiver then uses the same secret key and the decryption algorithm to turn the ciphertext back into the
original plaintext.
Q5.
Feature   Symmetric Cryptography   Asymmetric Cryptography
Uses two keys – a public key for
Uses one single key for both
Definition   encryption and a private key for
encryption and decryption.
decryption.
Number of Keys   One key (shared secret).   Two keys (public & private).
Key   Same key for both encryption and   Different but mathematically
Relationship   decryption.   related keys.
Fast – less computationally   Slow – involves complex mathematical
Speed
intensive.   operations.
Depends on keeping the   Security depends on the difficulty of deriving
Security
shared key secret.   private key from public key.
Key   Needs a secure channel to   No need for secure sharing – public key
Distribution   share the secret key.   can be openly distributed.
Encryption   AES, DES, 3DES, Blowfish, Hill   RSA, DSA, ECC, Diffie-
Example   Cipher.   Hellman.
Data   Suitable for encrypting large   Suitable for small data, key exchange, or
Size   amounts of data.   authentication.
Use   File encryption, database   Digital signatures, key exchange, SSL/TLS,
Cases   encryption, VPNs.   authentication.
Example   Both sender and receiver   Sender encrypts with receiver’s public key,
Working   use the same key “K”.   receiver decrypts with private key.
Q4.
Keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it
determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the
word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
********** 6 **********
--- page 7 ---
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.
Q7.
Layers of the OSI Model
There are 7 layers in the OSI Model and each layer has its specific role in handling data. All the layers are
mentioned below:
● Physical Layer
● Data Link Layer
● Network Layer
● Transport Layer
● Session Layer
● Presentation Layer
● Application Layer
Application Layer: Applications create the data.
Presentation Layer: Data is formatted and encrypted.
Session Layer: Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically
Example:
********** 7 **********

[Text in pictures on this page, read by OCR]
Input :

Keyword : secret

Message : Zombie Here

Output :


Take the first example, we used

Plain Text: ABCDEFGHIJKLMNOPQRSTUVWXYZ

secret" keyword there.

When “secret” keyword is used, the new encrypting text becomes
Encrypting : SECRTABDFGHIJKLMNOPQUVWXYZ

This means ‘A’ means ‘S', 'B' means "E' and ‘'C' means ‘C' and so on.
Lets encode the given message “Zombie Here"

ZOMBIE HERE becomes ZLJEFT DTOT
--- page 8 ---
Step 1: Person A interacts with e-mail application like Gmail, outlook, etc. Writes his email to send. (This
happens at Application Layer).
Step 2: At Presentation Layer, Mail application prepares for data transmission like encrypting data and
formatting it for transmission.
Step 3: At Session Layer, there is a connection established between the sender and receiver on the
internet.
Step 4: At Transport Layer, Email data is broken into smaller segments. It adds sequence number and
error-checking information to maintain the reliability of the information.
Step 5: At Network Layer, addressing of packets is done in order to find the best route for transfer.
Step 6: At Data Link Layer, data packets are encapsulated into frames, then MAC address is added for
local devices and then it checks for error using error detection.
Step 7: At Physical Layer, Frames are transmitted in the form of electrical/ optical signals over a physical
network medium like ethernet cable or WiFi.
Q6.
Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting
a plain text into a cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a
= 0, b = 1️, c = 2️, … z = 2️5).
Method to take key: In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be
equal to the length of the plain text.
Encryption Algorithm:
1. Assign a number to each character of the plain-text and the key according to alphabetical order.
2. Add both the number (Corresponding plain-text character number and Key character number).
3. Subtract the number from 2️6 if the added number is greater than 2️6, if it isn’t then leave it.
********** 8 **********

[Text in pictures on this page, read by OCR]
Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm, we assign a number to each character of our plain text and key.

No: 170 12 18 22 @ 17 20 15 10
KEY; R AN CHO BABA
No: 17 @ 13 27 1410410

Now Bitwise XOR the number of Plain-Text and Key and after doing the XOR operation and subtraction operation (if
required), we will get the corresponding Cipher-Text character number.

CT-NO: @ @ 1 16 17 14 16 20 14 10

Since there are no numbers that are greater than or equal to 26 we do not have to subtract 26 from any of them.

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: A A BQ RO QUO K
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e432c4113a69

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/Integrated_DS_7038/Information Security and Privacy/ANS_Information Security and Privacy(702DB0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: text (8 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II / IV/Semester III/Semester VII(Exam Year: 2025-2026)
Subject: Information Security and Privacy
Date: 05 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Answer Sheet:
Q1 c. State Layers of TCP/IP Model
Q1 b. Features ipv6
********** 1 **********
--- page 2 ---
Ans :
Q1 a. In a Caesar Cipher with a shift of 3, what will be the encrypted message for the plaintext “DATA”?
Options:
A) GDWD
B) ABCD
C) FATA
D) DDTD
ANSWER : A) GDWD
Q1 d. What is encryption?
Encryption is the method by which information is converted into secret code that hides the information's true
meaning. The science of encrypting and decrypting information is called cryptography.
In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext.
********** 2 **********

[Text in pictures on this page, read by OCR]
IPv6

Deployed 1998

128-bit IP address

Alphanumeric hexadecimal notation

50b2:6400::6c3a:b17d:0:10a9

Supports auto configuration
--- page 3 ---
● Cipher : The formulas used to encode and decode messages are called encryption algorithms
● Key : The variable, which is called a key, is what makes a cipher's output unique
Historically, it was used by militaries and governments.
In modern times, encryption is used to protect data stored on computers and storage devices, as well as data in
transit over networks.
Q2. A
Step 1️⃣: Convert plaintext to numbers
Using A=0, B=1, C=2, ..., Z=25
Letter Numeric
D   3
E   4
F   5
So the plaintext vector is:
3
𝑃= [ 4 ]
5
Step 2️⃣: Multiply by key matrix
𝐶= 𝐾× 𝑃
2 4 5   3
= [ 9 2 1 ] × [ 4 ]
3 8 7   5
Compute each element carefully:
1️⃣ 𝐶1 = 2 × 3 + 4 × 4 + 5 × 5 = 6 + 16 + 25 = 47
2️⃣ 𝐶2 = 9 × 3 + 2 × 4 + 1 × 5 = 27 + 8 + 5 = 40
3⃣ 𝐶3 = 3 × 3 + 8 × 4 + 7 × 5 = 9 + 32 + 35 = 76
47
𝐶= [ 40 ]
76
Step 3️⃣: Take mod 26
47mod  26 = 21
40mod  26 = 14
76mod  26 = 24
21
𝐶= [ 14 ]
24
Step 4️⃣: Convert numbers back to letters
Numeric Letter
21   V
14   O
********** 3 **********
--- page 4 ---
Numeric Letter
24   Y
✅ Ciphertext = “VOY”
✅ Final Answer:
Plaintext: DEF
2 4 5
Key Matrix: [ 9 2 1 ]
3 8 7
Ciphertext: VOY
Q2. B
The Hill cipher is a classic method of encryption that uses linear algebra to encipher messages. Invented by
Lester S. Hill in 1929, it's a polygraphic substitution cipher, which means it encrypts multiple letters at once.
This makes it more secure than simple substitution ciphers that encrypt letter by letter.
At its core, the Hill cipher uses a matrix as a key to transform blocks of plaintext letters into ciphertext. All the
mathematical operations are performed modulo 26, corresponding to the 26 letters of the alphabet.
Encryption Example
Let's encrypt the message "ACT" using the key "GYBNQKURP".
1. Assign numerical values to letters: First, we assign a number to each letter of the alphabet, starting
with A = 0, B = 1, and so on.
A B C D E F G H I J K L M
0 1 2 3 4 5 6 7 8 9 10 11 12
2. Export to Sheets
N O P Q R S T U V W X Y Z
13 14 15 16 17 18 19 20 21 22 23 24 25
3. Export to Sheets
4. Create the key matrix: The key "GYBNQKURP" is converted into a 3x3 matrix.
$ K = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} $
5. Convert the plaintext to a vector: The message "ACT" becomes a vector.
$ P = \begin{pmatrix} 0 \ 2 \ 19 \end{pmatrix} $
6. Multiply the key matrix by the plaintext vector:
$ C = K \cdot P = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} \begin{pmatrix} 0 \ 2
\ 19 \end{pmatrix} = \begin{pmatrix} (6 \cdot 0 + 24 \cdot 2 + 1 \cdot 19) \ (13 \cdot 0 + 16 \cdot 2 + 10 \cdot
19) \ (20 \cdot 0 + 17 \cdot 2 + 15 \cdot 19) \end{pmatrix} = \begin{pmatrix} 67 \ 222 \ 319 \end{pmatrix} $
7. Apply modulo 26: We take the result and apply modulo 26 to each element.
$ \begin{pmatrix} 67 \mod 26 \ 222 \mod 26 \ 319 \mod 26 \end{pmatrix} = \begin{pmatrix} 15 \ 14 \ 7
\end{pmatrix} $
8. Convert the numbers back to letters: The resulting numbers correspond to the letters "POH". So, the
ciphertext for "ACT" is "POH".
Decryption Example
********** 4 **********
--- page 5 ---
To decrypt the message, you need the inverse of the key matrix. Let's say we've calculated the inverse key
matrix () to be:
1. Convert the ciphertext to a vector: The ciphertext "POH" becomes a vector.
$ C = \begin{pmatrix} 15 \ 14 \ 7 \end{pmatrix} $
2. Multiply the inverse key matrix by the ciphertext vector:
$ P = K^{-1} \cdot C = \begin{pmatrix} 8 & 5 & 10 \ 21 & 8 & 21 \ 21 & 12 & 8 \end{pmatrix} \begin{pmatrix} 15
\ 14 \ 7 \end{pmatrix} = \begin{pmatrix} (8 \cdot 15 + 5 \cdot 14 + 10 \cdot 7) \ (21 \cdot 15 + 8 \cdot 14 + 21
\cdot 7) \ (21 \cdot 15 + 12 \cdot 14 + 8 \cdot 7) \end{pmatrix} = \begin{pmatrix} 260 \ 574 \ 539 \end{pmatrix}
$
3. Apply modulo 26:
$ \begin{pmatrix} 260 \mod 26 \ 574 \mod 26 \ 539 \mod 26 \end{pmatrix} = \begin{pmatrix} 0 \ 2 \ 19
\end{pmatrix} $
4. Convert the numbers back to letters: The resulting numbers correspond to the letters "ACT", which was
our original plaintext.
It's important to note that for a key to be valid in the Hill cipher, its determinant must not share any common
factors with 26 (other than 1). This ensures that an inverse of the key matrix exists, making decryption possible.
While the Hill cipher was a significant advancement in its time, it is vulnerable to known-plaintext attacks due
to its linear nature.
Q3. A
Q3 b
A symmetric cipher, also known as a symmetric-key algorithm, is a cryptographic system where the same key is
used for both encrypting and decrypting information. This shared secret is what makes the communication
secure. For a symmetric cipher to function, it needs five essential ingredients.
The 5 Essential Ingredients
1. Plaintext: This is the original, readable message or data that needs to be encrypted. It's the input to the
cipher. For example, if you wanted to securely send the message "MEET ME AT DAWN," this would be
your plaintext.
********** 5 **********

[Text in pictures on this page, read by OCR]
A B c

Feature IPv4 IPv6
Address Length 32-bit address 128-bit address
Address Format Decimal format (e.g., 192.168.0.1) Hexadecimal format (e.g., 2001:0db8::1)
Configuration Manual and DHCP configuration Auto-configuration and renumbering supported
Connection Integrity End-to-end integrity is unachievable End-to-end integrity is achievable
Security No builtin sea. extemal tools like IPSec is built-in for encryption and authentication
Fragmentation Performed by sender and routers Performed only by the sender
Flow Identification Not available Uses Flow Label field in header for packet flow
identification
Checksum Field Present Not present
Transmission Scheme Supports broadcast Uses multicast and anycast; no broadcast
Header Size Variable: 20-60 bytes Fixed: 40 bytes
Conversion Can be converted to IPv6 Not all IPV6 addresses can be converted to IPv4
Field Structure 4 fields separated by dots (.) 8 fields separated by colons (:)
Address Classes Has address classes (A, B, C, D, E) No concept of address classes
VLSM Support Supports vocewtst Subnet Does not support VLSM

Example 66.94.2913 2001:0000: 3238:DFE1 0063:0000:0000:FEFB
--- page 6 ---
2. Encryption Algorithm: This is the mathematical function or set of rules that transforms the plaintext
into ciphertext. It dictates exactly how the substitution and permutation of the data will occur.
3. Secret Key: The key is a piece of information (typically a string of numbers or characters) that is shared
between the sender and the receiver. It's a critical input to the encryption algorithm, as it determines
the specific transformation of the plaintext. The security of a symmetric cipher rests entirely on the
secrecy of this key.
4. Ciphertext: This is the scrambled, unreadable output from the encryption algorithm. It's the encrypted
version of the plaintext that can be transmitted over an insecure channel. An attacker who intercepts
the ciphertext without the secret key should not be able to understand the original message.
5. Decryption Algorithm: This is essentially the reverse of the encryption algorithm. It's the function that
takes the ciphertext and the same secret key to transform the data back into its original, readable
plaintext form.
In essence, the sender uses the secret key and the encryption algorithm to turn plaintext into ciphertext. The
receiver then uses the same secret key and the decryption algorithm to turn the ciphertext back into the
original plaintext.
Q5.
Feature   Symmetric Cryptography   Asymmetric Cryptography
Uses two keys – a public key for
Uses one single key for both
Definition   encryption and a private key for
encryption and decryption.
decryption.
Number of Keys   One key (shared secret).   Two keys (public & private).
Key   Same key for both encryption and   Different but mathematically
Relationship   decryption.   related keys.
Fast – less computationally   Slow – involves complex mathematical
Speed
intensive.   operations.
Depends on keeping the   Security depends on the difficulty of deriving
Security
shared key secret.   private key from public key.
Key   Needs a secure channel to   No need for secure sharing – public key
Distribution   share the secret key.   can be openly distributed.
Encryption   AES, DES, 3DES, Blowfish, Hill   RSA, DSA, ECC, Diffie-
Example   Cipher.   Hellman.
Data   Suitable for encrypting large   Suitable for small data, key exchange, or
Size   amounts of data.   authentication.
Use   File encryption, database   Digital signatures, key exchange, SSL/TLS,
Cases   encryption, VPNs.   authentication.
Example   Both sender and receiver   Sender encrypts with receiver’s public key,
Working   use the same key “K”.   receiver decrypts with private key.
Q4.
Keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it
determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the
word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
********** 6 **********
--- page 7 ---
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.
Q7.
Layers of the OSI Model
There are 7 layers in the OSI Model and each layer has its specific role in handling data. All the layers are
mentioned below:
● Physical Layer
● Data Link Layer
● Network Layer
● Transport Layer
● Session Layer
● Presentation Layer
● Application Layer
Application Layer: Applications create the data.
Presentation Layer: Data is formatted and encrypted.
Session Layer: Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically
Example:
********** 7 **********

[Text in pictures on this page, read by OCR]
Input :

Keyword : secret

Message : Zombie Here

Output :


Take the first example, we used

Plain Text: ABCDEFGHIJKLMNOPQRSTUVWXYZ

secret" keyword there.

When “secret” keyword is used, the new encrypting text becomes
Encrypting : SECRTABDFGHIJKLMNOPQUVWXYZ

This means ‘A’ means ‘S', 'B' means "E' and ‘'C' means ‘C' and so on.
Lets encode the given message “Zombie Here"

ZOMBIE HERE becomes ZLJEFT DTOT
--- page 8 ---
Step 1: Person A interacts with e-mail application like Gmail, outlook, etc. Writes his email to send. (This
happens at Application Layer).
Step 2: At Presentation Layer, Mail application prepares for data transmission like encrypting data and
formatting it for transmission.
Step 3: At Session Layer, there is a connection established between the sender and receiver on the
internet.
Step 4: At Transport Layer, Email data is broken into smaller segments. It adds sequence number and
error-checking information to maintain the reliability of the information.
Step 5: At Network Layer, addressing of packets is done in order to find the best route for transfer.
Step 6: At Data Link Layer, data packets are encapsulated into frames, then MAC address is added for
local devices and then it checks for error using error detection.
Step 7: At Physical Layer, Frames are transmitted in the form of electrical/ optical signals over a physical
network medium like ethernet cable or WiFi.
Q6.
Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting
a plain text into a cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a
= 0, b = 1️, c = 2️, … z = 2️5).
Method to take key: In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be
equal to the length of the plain text.
Encryption Algorithm:
1. Assign a number to each character of the plain-text and the key according to alphabetical order.
2. Add both the number (Corresponding plain-text character number and Key character number).
3. Subtract the number from 2️6 if the added number is greater than 2️6, if it isn’t then leave it.
********** 8 **********

[Text in pictures on this page, read by OCR]
Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm, we assign a number to each character of our plain text and key.

No: 170 12 18 22 @ 17 20 15 10
KEY; R AN CHO BABA
No: 17 @ 13 27 1410410

Now Bitwise XOR the number of Plain-Text and Key and after doing the XOR operation and subtraction operation (if
required), we will get the corresponding Cipher-Text character number.

CT-NO: @ @ 1 16 17 14 16 20 14 10

Since there are no numbers that are greater than or equal to 26 we do not have to subtract 26 from any of them.

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: A A BQ RO QUO K
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 33210dfca3c8

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_DS_7009/Information Security and Privacy/ANS_Information Security and Privacy(702DB0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (8 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Information Security and Privacy
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Answer Sheet:
Q1 a. State Layers of TCP/IP Model
Q1 b. Features ipv6
********** 1 **********
--- page 2 ---
Ans :
Q1 c. In a Caesar Cipher with a shift of 3, what will be the encrypted message for the plaintext “DATA”?
Options:
A) GDWD
B) ABCD
C) FATA
D) DDTD
ANSWER : A) GDWD
Q1 d. What is encryption?
Encryption is the method by which information is converted into secret code that hides the information's true
meaning. The science of encrypting and decrypting information is called cryptography.
In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext.
********** 2 **********

[Text in pictures on this page, read by OCR]
IPv6

Deployed 1998

128-bit IP address

Alphanumeric hexadecimal notation

50b2:6400::6c3a:b17d:0:10a9

Supports auto configuration
--- page 3 ---
● Cipher : The formulas used to encode and decode messages are called encryption algorithms
● Key : The variable, which is called a key, is what makes a cipher's output unique
Historically, it was used by militaries and governments.
In modern times, encryption is used to protect data stored on computers and storage devices, as well as data in
transit over networks.
Q2. A
Step 1️⃣: Convert plaintext to numbers
Using A=0, B=1, C=2, ..., Z=25
Letter Numeric
D   3
E   4
F   5
So the plaintext vector is:
3
𝑃= [ 4 ]
5
Step 2️⃣: Multiply by key matrix
𝐶= 𝐾× 𝑃
2 4 5   3
= [ 9 2 1 ] × [ 4 ]
3 8 7   5
Compute each element carefully:
1️⃣ 𝐶1 = 2 × 3 + 4 × 4 + 5 × 5 = 6 + 16 + 25 = 47
2️⃣ 𝐶2 = 9 × 3 + 2 × 4 + 1 × 5 = 27 + 8 + 5 = 40
3⃣ 𝐶3 = 3 × 3 + 8 × 4 + 7 × 5 = 9 + 32 + 35 = 76
47
𝐶= [ 40 ]
76
Step 3️⃣: Take mod 26
47mod  26 = 21
40mod  26 = 14
76mod  26 = 24
21
𝐶= [ 14 ]
24
Step 4️⃣: Convert numbers back to letters
Numeric Letter
21   V
14   O
********** 3 **********
--- page 4 ---
Numeric Letter
24   Y
✅ Ciphertext = “VOY”
✅ Final Answer:
Plaintext: DEF
2 4 5
Key Matrix: [ 9 2 1 ]
3 8 7
Ciphertext: VOY
Q2. B
The Hill cipher is a classic method of encryption that uses linear algebra to encipher messages. Invented by
Lester S. Hill in 1929, it's a polygraphic substitution cipher, which means it encrypts multiple letters at once.
This makes it more secure than simple substitution ciphers that encrypt letter by letter.
At its core, the Hill cipher uses a matrix as a key to transform blocks of plaintext letters into ciphertext. All the
mathematical operations are performed modulo 26, corresponding to the 26 letters of the alphabet.
Encryption Example
Let's encrypt the message "ACT" using the key "GYBNQKURP".
1. Assign numerical values to letters: First, we assign a number to each letter of the alphabet, starting
with A = 0, B = 1, and so on.
A B C D E F G H I J K L M
0 1 2 3 4 5 6 7 8 9 10 11 12
2. Export to Sheets
N O P Q R S T U V W X Y Z
13 14 15 16 17 18 19 20 21 22 23 24 25
3. Export to Sheets
4. Create the key matrix: The key "GYBNQKURP" is converted into a 3x3 matrix.
$ K = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} $
5. Convert the plaintext to a vector: The message "ACT" becomes a vector.
$ P = \begin{pmatrix} 0 \ 2 \ 19 \end{pmatrix} $
6. Multiply the key matrix by the plaintext vector:
$ C = K \cdot P = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} \begin{pmatrix} 0 \ 2
\ 19 \end{pmatrix} = \begin{pmatrix} (6 \cdot 0 + 24 \cdot 2 + 1 \cdot 19) \ (13 \cdot 0 + 16 \cdot 2 + 10 \cdot
19) \ (20 \cdot 0 + 17 \cdot 2 + 15 \cdot 19) \end{pmatrix} = \begin{pmatrix} 67 \ 222 \ 319 \end{pmatrix} $
7. Apply modulo 26: We take the result and apply modulo 26 to each element.
$ \begin{pmatrix} 67 \mod 26 \ 222 \mod 26 \ 319 \mod 26 \end{pmatrix} = \begin{pmatrix} 15 \ 14 \ 7
\end{pmatrix} $
8. Convert the numbers back to letters: The resulting numbers correspond to the letters "POH". So, the
ciphertext for "ACT" is "POH".
Decryption Example
********** 4 **********
--- page 5 ---
To decrypt the message, you need the inverse of the key matrix. Let's say we've calculated the inverse key
matrix () to be:
1. Convert the ciphertext to a vector: The ciphertext "POH" becomes a vector.
$ C = \begin{pmatrix} 15 \ 14 \ 7 \end{pmatrix} $
2. Multiply the inverse key matrix by the ciphertext vector:
$ P = K^{-1} \cdot C = \begin{pmatrix} 8 & 5 & 10 \ 21 & 8 & 21 \ 21 & 12 & 8 \end{pmatrix} \begin{pmatrix} 15
\ 14 \ 7 \end{pmatrix} = \begin{pmatrix} (8 \cdot 15 + 5 \cdot 14 + 10 \cdot 7) \ (21 \cdot 15 + 8 \cdot 14 + 21
\cdot 7) \ (21 \cdot 15 + 12 \cdot 14 + 8 \cdot 7) \end{pmatrix} = \begin{pmatrix} 260 \ 574 \ 539 \end{pmatrix}
$
3. Apply modulo 26:
$ \begin{pmatrix} 260 \mod 26 \ 574 \mod 26 \ 539 \mod 26 \end{pmatrix} = \begin{pmatrix} 0 \ 2 \ 19
\end{pmatrix} $
4. Convert the numbers back to letters: The resulting numbers correspond to the letters "ACT", which was
our original plaintext.
It's important to note that for a key to be valid in the Hill cipher, its determinant must not share any common
factors with 26 (other than 1). This ensures that an inverse of the key matrix exists, making decryption possible.
While the Hill cipher was a significant advancement in its time, it is vulnerable to known-plaintext attacks due
to its linear nature.
Q3. A
Q3 b
A symmetric cipher, also known as a symmetric-key algorithm, is a cryptographic system where the same key is
used for both encrypting and decrypting information. This shared secret is what makes the communication
secure. For a symmetric cipher to function, it needs five essential ingredients.
The 5 Essential Ingredients
1. Plaintext: This is the original, readable message or data that needs to be encrypted. It's the input to the
cipher. For example, if you wanted to securely send the message "MEET ME AT DAWN," this would be
your plaintext.
********** 5 **********

[Text in pictures on this page, read by OCR]
A B c

Feature IPv4 IPv6
Address Length 32-bit address 128-bit address
Address Format Decimal format (e.g., 192.168.0.1) Hexadecimal format (e.g., 2001:0db8::1)
Configuration Manual and DHCP configuration Auto-configuration and renumbering supported
Connection Integrity End-to-end integrity is unachievable End-to-end integrity is achievable
Security No builtin sea. extemal tools like IPSec is built-in for encryption and authentication
Fragmentation Performed by sender and routers Performed only by the sender
Flow Identification Not available Uses Flow Label field in header for packet flow
identification
Checksum Field Present Not present
Transmission Scheme Supports broadcast Uses multicast and anycast; no broadcast
Header Size Variable: 20-60 bytes Fixed: 40 bytes
Conversion Can be converted to IPv6 Not all IPV6 addresses can be converted to IPv4
Field Structure 4 fields separated by dots (.) 8 fields separated by colons (:)
Address Classes Has address classes (A, B, C, D, E) No concept of address classes
VLSM Support Supports vocewtst Subnet Does not support VLSM

Example 66.94.2913 2001:0000: 3238:DFE1 0063:0000:0000:FEFB
--- page 6 ---
2. Encryption Algorithm: This is the mathematical function or set of rules that transforms the plaintext
into ciphertext. It dictates exactly how the substitution and permutation of the data will occur.
3. Secret Key: The key is a piece of information (typically a string of numbers or characters) that is shared
between the sender and the receiver. It's a critical input to the encryption algorithm, as it determines
the specific transformation of the plaintext. The security of a symmetric cipher rests entirely on the
secrecy of this key.
4. Ciphertext: This is the scrambled, unreadable output from the encryption algorithm. It's the encrypted
version of the plaintext that can be transmitted over an insecure channel. An attacker who intercepts
the ciphertext without the secret key should not be able to understand the original message.
5. Decryption Algorithm: This is essentially the reverse of the encryption algorithm. It's the function that
takes the ciphertext and the same secret key to transform the data back into its original, readable
plaintext form.
In essence, the sender uses the secret key and the encryption algorithm to turn plaintext into ciphertext. The
receiver then uses the same secret key and the decryption algorithm to turn the ciphertext back into the
original plaintext.
Q4.
Feature   Symmetric Cryptography   Asymmetric Cryptography
Uses two keys – a public key for
Uses one single key for both
Definition   encryption and a private key for
encryption and decryption.
decryption.
Number of Keys   One key (shared secret).   Two keys (public & private).
Key   Same key for both encryption and   Different but mathematically
Relationship   decryption.   related keys.
Fast – less computationally   Slow – involves complex mathematical
Speed
intensive.   operations.
Depends on keeping the   Security depends on the difficulty of deriving
Security
shared key secret.   private key from public key.
Key   Needs a secure channel to   No need for secure sharing – public key
Distribution   share the secret key.   can be openly distributed.
Encryption   AES, DES, 3DES, Blowfish, Hill   RSA, DSA, ECC, Diffie-
Example   Cipher.   Hellman.
Data   Suitable for encrypting large   Suitable for small data, key exchange, or
Size   amounts of data.   authentication.
Use   File encryption, database   Digital signatures, key exchange, SSL/TLS,
Cases   encryption, VPNs.   authentication.
Example   Both sender and receiver   Sender encrypts with receiver’s public key,
Working   use the same key “K”.   receiver decrypts with private key.
Q5.
Keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it
determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the
word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
********** 6 **********
--- page 7 ---
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.
Q6.
Layers of the OSI Model
There are 7 layers in the OSI Model and each layer has its specific role in handling data. All the layers are
mentioned below:
● Physical Layer
● Data Link Layer
● Network Layer
● Transport Layer
● Session Layer
● Presentation Layer
● Application Layer
Application Layer: Applications create the data.
Presentation Layer: Data is formatted and encrypted.
Session Layer: Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically
Example:
********** 7 **********

[Text in pictures on this page, read by OCR]
Input :

Keyword : secret

Message : Zombie Here

Output :


Take the first example, we used

Plain Text: ABCDEFGHIJKLMNOPQRSTUVWXYZ

secret" keyword there.

When “secret” keyword is used, the new encrypting text becomes
Encrypting : SECRTABDFGHIJKLMNOPQUVWXYZ

This means ‘A’ means ‘S', 'B' means "E' and ‘'C' means ‘C' and so on.
Lets encode the given message “Zombie Here"

ZOMBIE HERE becomes ZLJEFT DTOT
--- page 8 ---
Step 1: Person A interacts with e-mail application like Gmail, outlook, etc. Writes his email to send. (This
happens at Application Layer).
Step 2: At Presentation Layer, Mail application prepares for data transmission like encrypting data and
formatting it for transmission.
Step 3: At Session Layer, there is a connection established between the sender and receiver on the
internet.
Step 4: At Transport Layer, Email data is broken into smaller segments. It adds sequence number and
error-checking information to maintain the reliability of the information.
Step 5: At Network Layer, addressing of packets is done in order to find the best route for transfer.
Step 6: At Data Link Layer, data packets are encapsulated into frames, then MAC address is added for
local devices and then it checks for error using error detection.
Step 7: At Physical Layer, Frames are transmitted in the form of electrical/ optical signals over a physical
network medium like ethernet cable or WiFi.
Q7.
Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting
a plain text into a cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a
= 0, b = 1️, c = 2️, … z = 2️5).
Method to take key: In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be
equal to the length of the plain text.
Encryption Algorithm:
1. Assign a number to each character of the plain-text and the key according to alphabetical order.
2. Add both the number (Corresponding plain-text character number and Key character number).
3. Subtract the number from 2️6 if the added number is greater than 2️6, if it isn’t then leave it.
********** 8 **********

[Text in pictures on this page, read by OCR]
Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm, we assign a number to each character of our plain text and key.

No: 170 12 18 22 @ 17 20 15 10
KEY; R AN CHO BABA
No: 17 @ 13 27 1410410

Now Bitwise XOR the number of Plain-Text and Key and after doing the XOR operation and subtraction operation (if
required), we will get the corresponding Cipher-Text character number.

CT-NO: @ @ 1 16 17 14 16 20 14 10

Since there are no numbers that are greater than or equal to 26 we do not have to subtract 26 from any of them.

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: A A BQ RO QUO K
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7a4c0eca9c17

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_DS_7052/Information Security and Privacy/ANS_Information Security and Privacy(702DB0C037)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (9 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (DATA SCIENCE)/MBA Tech (DS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Information Security and Privacy
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Answer Sheet:
Q1 a. State Layers of TCP/IP Model
********** 1 **********
--- page 2 ---
Q1 b. Features ipv6
Ans :
Q1 c. In a Caesar Cipher with a shift of 3, what will be the encrypted message for the plaintext “DATA”?
Options:
A) GDWD
B) ABCD
C) FATA
D) DDTD
ANSWER : A) GDWD
Q1 d. What is encryption?
Encryption is the method by which information is converted into secret code that hides the information's true
meaning. The science of encrypting and decrypting information is called cryptography.
In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext.
********** 2 **********

[Text in pictures on this page, read by OCR]
IPv6

Deployed 1998

128-bit IP address

Alphanumeric hexadecimal notation

50b2:6400::6c3a:b17d:0:10a9

Supports auto configuration
--- page 3 ---
● Cipher : The formulas used to encode and decode messages are called encryption algorithms
● Key : The variable, which is called a key, is what makes a cipher's output unique
Historically, it was used by militaries and governments.
In modern times, encryption is used to protect data stored on computers and storage devices, as well as data in
transit over networks.
Q2. A
Step 1️⃣: Convert plaintext to numbers
Using A=0, B=1, C=2, ..., Z=25
Letter Numeric
D   3
E   4
F   5
So the plaintext vector is:
3
𝑃= [ 4 ]
5
Step 2️⃣: Multiply by key matrix
𝐶= 𝐾× 𝑃
2 4 5   3
= [ 9 2 1 ] × [ 4 ]
3 8 7   5
Compute each element carefully:
1️⃣ 𝐶1 = 2 × 3 + 4 × 4 + 5 × 5 = 6 + 16 + 25 = 47
2️⃣ 𝐶2 = 9 × 3 + 2 × 4 + 1 × 5 = 27 + 8 + 5 = 40
3⃣ 𝐶3 = 3 × 3 + 8 × 4 + 7 × 5 = 9 + 32 + 35 = 76
47
𝐶= [ 40 ]
76
********** 3 **********
--- page 4 ---
Step 3️⃣: Take mod 26
47mod  26 = 21
40mod  26 = 14
76mod  26 = 24
21
𝐶= [ 14 ]
24
Step 4️⃣: Convert numbers back to letters
Numeric Letter
21   V
14   O
24   Y
✅ Ciphertext = “VOY”
✅ Final Answer:
Plaintext: DEF
2 4 5
Key Matrix: [ 9 2 1 ]
3 8 7
Ciphertext: VOY
Q2. B
The Hill cipher is a classic method of encryption that uses linear algebra to encipher messages. Invented by
Lester S. Hill in 1929, it's a polygraphic substitution cipher, which means it encrypts multiple letters at once.
This makes it more secure than simple substitution ciphers that encrypt letter by letter.
At its core, the Hill cipher uses a matrix as a key to transform blocks of plaintext letters into ciphertext. All the
mathematical operations are performed modulo 26, corresponding to the 26 letters of the alphabet.
Encryption Example
Let's encrypt the message "ACT" using the key "GYBNQKURP".
1. Assign numerical values to letters: First, we assign a number to each letter of the alphabet, starting
with A = 0, B = 1, and so on.
A B C D E F G H I J K L M
0 1 2 3 4 5 6 7 8 9 10 11 12
2. Export to Sheets
N O P Q R S T U V W X Y Z
13 14 15 16 17 18 19 20 21 22 23 24 25
3. Export to Sheets
4. Create the key matrix: The key "GYBNQKURP" is converted into a 3x3 matrix.
$ K = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} $
5. Convert the plaintext to a vector: The message "ACT" becomes a vector.
$ P = \begin{pmatrix} 0 \ 2 \ 19 \end{pmatrix} $
********** 4 **********
--- page 5 ---
6. Multiply the key matrix by the plaintext vector:
$ C = K \cdot P = \begin{pmatrix} 6 & 24 & 1 \ 13 & 16 & 10 \ 20 & 17 & 15 \end{pmatrix} \begin{pmatrix} 0 \ 2
\ 19 \end{pmatrix} = \begin{pmatrix} (6 \cdot 0 + 24 \cdot 2 + 1 \cdot 19) \ (13 \cdot 0 + 16 \cdot 2 + 10 \cdot
19) \ (20 \cdot 0 + 17 \cdot 2 + 15 \cdot 19) \end{pmatrix} = \begin{pmatrix} 67 \ 222 \ 319 \end{pmatrix} $
7. Apply modulo 26: We take the result and apply modulo 26 to each element.
$ \begin{pmatrix} 67 \mod 26 \ 222 \mod 26 \ 319 \mod 26 \end{pmatrix} = \begin{pmatrix} 15 \ 14 \ 7
\end{pmatrix} $
8. Convert the numbers back to letters: The resulting numbers correspond to the letters "POH". So, the
ciphertext for "ACT" is "POH".
Decryption Example
To decrypt the message, you need the inverse of the key matrix. Let's say we've calculated the inverse key
matrix () to be:
1. Convert the ciphertext to a vector: The ciphertext "POH" becomes a vector.
$ C = \begin{pmatrix} 15 \ 14 \ 7 \end{pmatrix} $
2. Multiply the inverse key matrix by the ciphertext vector:
$ P = K^{-1} \cdot C = \begin{pmatrix} 8 & 5 & 10 \ 21 & 8 & 21 \ 21 & 12 & 8 \end{pmatrix} \begin{pmatrix} 15
\ 14 \ 7 \end{pmatrix} = \begin{pmatrix} (8 \cdot 15 + 5 \cdot 14 + 10 \cdot 7) \ (21 \cdot 15 + 8 \cdot 14 + 21
\cdot 7) \ (21 \cdot 15 + 12 \cdot 14 + 8 \cdot 7) \end{pmatrix} = \begin{pmatrix} 260 \ 574 \ 539 \end{pmatrix}
$
3. Apply modulo 26:
$ \begin{pmatrix} 260 \mod 26 \ 574 \mod 26 \ 539 \mod 26 \end{pmatrix} = \begin{pmatrix} 0 \ 2 \ 19
\end{pmatrix} $
4. Convert the numbers back to letters: The resulting numbers correspond to the letters "ACT", which was
our original plaintext.
It's important to note that for a key to be valid in the Hill cipher, its determinant must not share any common
factors with 26 (other than 1). This ensures that an inverse of the key matrix exists, making decryption possible.
While the Hill cipher was a significant advancement in its time, it is vulnerable to known-plaintext attacks due
to its linear nature.
Q3. A
********** 5 **********
--- page 6 ---
Q3 b
A symmetric cipher, also known as a symmetric-key algorithm, is a cryptographic system where the same key is
used for both encrypting and decrypting information. This shared secret is what makes the communication
secure. For a symmetric cipher to function, it needs five essential ingredients.
The 5 Essential Ingredients
1. Plaintext: This is the original, readable message or data that needs to be encrypted. It's the input to the
cipher. For example, if you wanted to securely send the message "MEET ME AT DAWN," this would be
your plaintext.
2. Encryption Algorithm: This is the mathematical function or set of rules that transforms the plaintext
into ciphertext. It dictates exactly how the substitution and permutation of the data will occur.
3. Secret Key: The key is a piece of information (typically a string of numbers or characters) that is shared
between the sender and the receiver. It's a critical input to the encryption algorithm, as it determines
the specific transformation of the plaintext. The security of a symmetric cipher rests entirely on the
secrecy of this key.
4. Ciphertext: This is the scrambled, unreadable output from the encryption algorithm. It's the encrypted
version of the plaintext that can be transmitted over an insecure channel. An attacker who intercepts
the ciphertext without the secret key should not be able to understand the original message.
5. Decryption Algorithm: This is essentially the reverse of the encryption algorithm. It's the function that
takes the ciphertext and the same secret key to transform the data back into its original, readable
plaintext form.
In essence, the sender uses the secret key and the encryption algorithm to turn plaintext into ciphertext. The
receiver then uses the same secret key and the decryption algorithm to turn the ciphertext back into the
original plaintext.
Q4.
Feature   Symmetric Cryptography   Asymmetric Cryptography
Uses two keys – a public key for
Uses one single key for both
Definition   encryption and a private key for
encryption and decryption.
decryption.
********** 6 **********

[Text in pictures on this page, read by OCR]
A B c

Feature IPv4 IPv6
Address Length 32-bit address 128-bit address
Address Format Decimal format (e.g., 192.168.0.1) Hexadecimal format (e.g., 2001:0db8::1)
Configuration Manual and DHCP configuration Auto-configuration and renumbering supported
Connection Integrity End-to-end integrity is unachievable End-to-end integrity is achievable
Security No builtin sea. extemal tools like IPSec is built-in for encryption and authentication
Fragmentation Performed by sender and routers Performed only by the sender
Flow Identification Not available Uses Flow Label field in header for packet flow
identification
Checksum Field Present Not present
Transmission Scheme Supports broadcast Uses multicast and anycast; no broadcast
Header Size Variable: 20-60 bytes Fixed: 40 bytes
Conversion Can be converted to IPv6 Not all IPV6 addresses can be converted to IPv4
Field Structure 4 fields separated by dots (.) 8 fields separated by colons (:)
Address Classes Has address classes (A, B, C, D, E) No concept of address classes
VLSM Support Supports vocewtst Subnet Does not support VLSM

Example 66.94.2913 2001:0000: 3238:DFE1 0063:0000:0000:FEFB
--- page 7 ---
Number of Keys   One key (shared secret).   Two keys (public & private).
Key   Same key for both encryption and   Different but mathematically
Relationship   decryption.   related keys.
Fast – less computationally   Slow – involves complex mathematical
Speed
intensive.   operations.
Depends on keeping the   Security depends on the difficulty of deriving
Security
shared key secret.   private key from public key.
Key   Needs a secure channel to   No need for secure sharing – public key
Distribution   share the secret key.   can be openly distributed.
Encryption   AES, DES, 3DES, Blowfish, Hill   RSA, DSA, ECC, Diffie-
Example   Cipher.   Hellman.
Data   Suitable for encrypting large   Suitable for small data, key exchange, or
Size   amounts of data.   authentication.
Use   File encryption, database   Digital signatures, key exchange, SSL/TLS,
Cases   encryption, VPNs.   authentication.
Example   Both sender and receiver   Sender encrypts with receiver’s public key,
Working   use the same key “K”.   receiver decrypts with private key.
Q5.
Keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it
determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the
word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc.
until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.
********** 7 **********

[Text in pictures on this page, read by OCR]
Input :

Keyword : secret

Message : Zombie Here

Output :


Take the first example, we used "secret" keyword there.

Plain Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
When “secret” keyword is used, the new encrypting text becomes
Encrypting : SECRTABDFGHIJKLMNOPQUVWXYZ
This means 'A' means 'S', '"B' means ‘E' and 'C' means 'C' and so on.
Lets encode the given message “Zombie Here"

ZOMBIE HERE becomes ZLJEFT DTOT
--- page 8 ---
Q6.
Layers of the OSI Model
There are 7 layers in the OSI Model and each layer has its specific role in handling data. All the layers are
mentioned below:
● Physical Layer
● Data Link Layer
● Network Layer
● Transport Layer
● Session Layer
● Presentation Layer
● Application Layer
Application Layer: Applications create the data.
Presentation Layer: Data is formatted and encrypted.
Session Layer: Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically
Example:
Step 1: Person A interacts with e-mail application like Gmail, outlook, etc. Writes his email to send. (This
happens at Application Layer).
Step 2: At Presentation Layer, Mail application prepares for data transmission like encrypting data and
formatting it for transmission.
Step 3: At Session Layer, there is a connection established between the sender and receiver on the
internet.
Step 4: At Transport Layer, Email data is broken into smaller segments. It adds sequence number and
error-checking information to maintain the reliability of the information.
Step 5: At Network Layer, addressing of packets is done in order to find the best route for transfer.
Step 6: At Data Link Layer, data packets are encapsulated into frames, then MAC address is added for
local devices and then it checks for error using error detection.
Step 7: At Physical Layer, Frames are transmitted in the form of electrical/ optical signals over a physical
network medium like ethernet cable or WiFi.
Q7.
Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting
a plain text into a cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a
= 0, b = 1️, c = 2️, … z = 2️5).
Method to take key: In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be
equal to the length of the plain text.
Encryption Algorithm:
1. Assign a number to each character of the plain-text and the key according to alphabetical order.
********** 8 **********
--- page 9 ---
2. Add both the number (Corresponding plain-text character number and Key character number).
3. Subtract the number from 2️6 if the added number is greater than 2️6, if it isn’t then leave it.
********** 9 **********

[Text in pictures on this page, read by OCR]
Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm, we assign a number to each character of our plain text and key.

No: 170 12 18 22 © 17 20 15 10
Key: R AN CHO BABA
No: 17 @ 13.27 141010

Now Bitwise XOR the number of Plain-Text and Key and after doing the XOR operation and subtraction operation (if
required), we will get the corresponding Cipher-Text character number.

CT-NO: @ @ 1 16 17 14 16 20 14 10

Since there are no numbers that are greater than or equal to 26 we do not have to subtract 26 from any of them.

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: A A BQ RO QUO K
````
