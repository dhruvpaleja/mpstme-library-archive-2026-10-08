# Blockchain Security and Forensics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 03fefc7ada55

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Blockchain Security and Forensics/ANS_Blockchain Security and Forensics(702IT0E021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (7 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Blockchain Security and Forensics
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   • An individual ledger is used for maintaining information about ownership,
which is equivalent to one blockchain-data structure storing ownership-
related data.
• The individual ledgers are stored on the computers (nodes) of a peer-to-peer
system.
CO-1;
• The blockchain-algorithm is responsible for letting the individual nodes
BL-
collectively arrive at one consistent version of the state of ownership on
2
which the final verdict is based.
•   Integrity in this system is its ability to make true statements about ownership.
• Cryptography is necessary for creating a trustworthy means of identification,
authentication, and authorization and ensuring data security.
b. ECC is a public-key cryptography method based on elliptic curves.
Advantages:
CO-1
• Smaller key size
BL-2
• High security
•   Faster computation
c.
Feature   Partitioning Attack   Delay Attack
CO-2
BL-2
Split network   into   isolated   Slow/block   delivery   of
Goal
groups   transactions/blocks
********** 1 **********
--- page 2 ---
Targeted nodes or subset of
Scope   Entire groups of nodes
nodes
Forks,   double-spending, Temporary   forks,   slower
Impact
consensus disruption   confirmations, miner advantage
Network   isolation   (BGP,   Traffic manipulation, selective
Method
eclipse)   delays
d. A seed phrase, also known as a recovery or mnemonic phrase, is a set of 12 to 24
simple words (e.g., "apple," "globe," "zebra") that acts as the master key to a
cryptocurrency wallet. It is a human-readable backup of a wallet’s complex
cryptographic keys, allowing users to recover their funds if their device is lost or
stolen.
Role in Blockchain Forensics
• In blockchain forensics, seed phrases are critical digital artifacts that
investigators look for to gain access to illicit assets. Their primary roles
include:
• Wallet Recovery and Access: Investigators search for seed phrases written
on paper, stored in digital files, or even engraved on metal during field
CO-3   operations. If a seed phrase is recovered, law enforcement can restore the
BL-2   suspect's wallet on a controlled device to view balances and transaction
history.
• Asset Seizure: Once access is gained via the seed phrase, investigators can
move illicit funds to a controlled address (a government-held wallet) to
prevent them from being "swept" or moved by the suspect or accomplices.
• Generating Investigative Leads: Forensic tools like TRM Labs' Seed
Analysis can convert a recovered seed phrase into public keys across multiple
blockchains. This reveals a suspect’s entire network of linked wallets,
uncovering previously unknown assets and transaction trails.
• Chain of Custody: Documenting the discovery and use of a seed phrase is
vital for proving the integrity of evidence in court. This includes recording
the date, time, and exact steps taken to transfer funds to a controlled wallet.
a.   • Public blockchain – open to all   [10]
• Private blockchain – controlled by one entity
• Consortium blockchain – controlled by a group
• Hybrid blockchain – mix of public & private
Q2
CO-1
BL-2
********** 2 **********

[Text in pictures on this page, read by OCR]
4 main types of blockchain technology

Public Private Hybrid Consortium

(permissionless) (permissioned)
Independence Access control Access control Access control

ADVANTAGES Transparency Performance Performance Scalability

Trust Scalability Security

= Performance = Trust = Transparency = Transparency

DISADVANTAGES = Scalability = Auditability = Upgrading

= Security

Cryptocurrency Supply chain Medical records Banking
USE CASES Document validation Asset ownership Real estate Research

Supply chain

--- page 3 ---
b. A Sybil attack uses a single node to operate many active fake identities (or Sybil   [10]
identities) simultaneously, within a peer-to-peer network.
This type of attack aims to undermine the authority or power in a reputable system
by gaining the majority of influence in the network. The fake identities serve to
provide this influence.
Sybil attack may block user’s from the network or may be used to carry out 51%
CO-2   attack.
BL-2
Mitigations:
•   Identity Validation
• Social Trust Graphs
• Economic Costs
a. λ = (3-1)/(6-5) = 2/1 = 2 mod 17   [10]
Q3   λ = 2
CO- 1   x₃ = 2² −5-6 = 4−11= -7 mod17= 10 mod 17 = 10
BL-3   y₃ = 2(5−10)−1 = -11 mod17=6
P+Q = (10,6)
b. The ECDSA (Elliptic Curve Digital Signature Algorithm) is a cryptographically [10]
secure digital signature scheme, based on the elliptic-curve cryptography (ECC).
A 256-bit ECDSA signature has the same security strength like 3072-bit RSA
signature.
Key Generation
The ECDSA key-pair consists of:
Private key (integer): privKey. The private key is generated as a random
integer in the range [0...n-1].
Public key (EC point): pubKey = privKey * G
The public key pubKey is a point on the elliptic curve, calculated by the EC
point multiplication.
ECDSA Sign
1. Calculate the message hash, using a cryptographic hash function like SHA-
256: h = hash(msg).
2. Generate securely a random number k in the range [1..n-1].
CO-1
3. Calculate the random point R = k * G and take its x-coordinate: r = R.x
BL-2
4. Calculate the signature proof: s = k−1∗(h+r∗privKey)(mod n) .
5. Return the signature {r, s}.
ECDSA signatures are 2 times longer than the signer's private key for the curve
used during the signing process.
ECDSA Sign Verification
The algorithm to verify a ECDSA signature takes as input the signed
message msg + the signature {r, s} produced from the signing algorithm +
the public key pubKey, corresponding to the signer's private key. The output
is boolean value: valid or invalid signature.
1. Calculate the message hash, with the same cryptographic hash function used
during the signing: h = hash(msg).
2. Calculate the modular inverse of the signature proof: s1 = s−1(mod n)
3. Recover the random point used during the signing: R' = (h * s1) * G + (r *
s1) * pubKey
4. Take from R' its x-coordinate: r' = R’.x
********** 3 **********
--- page 4 ---
5. Calculate the signature validation result by comparing whether r' == r.
The general idea of the signature verification is to recover the point R' using the
public key and check whether it is same point R, generated randomly during the
signing process.
a. The account-based transaction model represents assets as balances within [10]
accounts, similar to bank accounts. Ethereum uses this transaction model. There
are two different types of accounts:
Private key controlled user accounts and Contract code-controlled accounts.
When you create an Ether wallet and receive your first transaction, a private key
controlled account is added to the global state and stored across all nodes on the
network. Deploying a smart contract leads to the creation of a code controlled
account. Smart contracts can hold funds themselves, which they can redistribute
according to the conditions defined in the contract logic. Every account in Ethereum
has a balance, storage, and code-space for calling other accounts or addresses.
Q4
CO-2
BL-2
b. Wallets:   [10]
Crypto wallets hold users' private keys and information where the public keys
are located on the blockchain.
A wallet doesn’t store your bitcoin, and because it doesn’t store them, it can’t send
or receive them!
The wallet can examine what transactions exist on the blockchain that is already
locked with a Bitcoin address that the wallet controls and create a balance. In
addition, a wallet may store a local list of transactions it’s been involved in as well
as user preferences and the constantly updated balance.
CO-1
WIF:
BL-2
A WIF key is just your private key in a format that’s easier to copy and retype. It is
51 character long and in base 58 format.
Generating WIF key from private key.
1. Start with your 64-character private key
2. Add 0x80 to the front of the key
3. SHA256 the new key from step 2
4. Run SHA256 over the key from step 3
5. Take the first 4 bytes from step 4. This is your checksum
6. Add the checksum to the end of the key from step 2
********** 4 **********

[Text in pictures on this page, read by OCR]
Feature & UTXO Model (e.g., Bitcoin) Account Model (e.g., Ethereum)

Analogy Physical cash / individual bills Bank ledger / digital balance

Balance Tracking Sum of unspent outputs Single balance per address

Transaction Parallelizable Sequential (linear)

Processing

Privacy High (through address rotation) Low (all history tied to one

address)

Complexity High (management of multiple Low (user-friendly and intuitive)

outputs)

Smart Contracts Challenging/Limited Flexible and robust
--- page 5 ---
7. Base58-encode the result from step 6
a. The ERC-20 token standard can be described as a blueprint for creating fungible [10]
tokens on the Ethereum network.
Fungible means that each token (or a fraction of a token) is equivalent to and
indistinguishable from another. For example, Alice’s US$1 is equal to Bob’s US$1.
Both of them can swap their US dollar because it has the same value.
There are six primary functions an ERC-20 token must implement:
TotalSupply – Used to derive the total token supply of a specific ERC-20
Q5   token
CO-1   BalanceOf – Used to derive the token balance in an Ethereum wallet
BL-2   Transfer – Allows the user to transfer the ownership of a token to another
TransferFrom – Works similarly to transfer function with the added
advantage of allowing contracts to transfer tokens on the user’s behalf
Approve – Used to set a limit on the number of tokens a smart contract can
withdraw
Allowance – Grants external addresses the access and permit to spend the
tokens from a certain balance
b.   PBFT is a lightweight blockchain algorithm that solves the Byzantine [10]
General’s problems by letting users confirm the messages that have been
delivered to them by performing a computation to evaluate the decision about
the message’s validity.
PBFT relies on a state machine replication model where nodes are ordered in
a sequence. One node acts as the Primary (leader), while the others are
Backups. The system transitions through several phases to reach an
agreement
The party then announces its decision to other nodes who ultimately process
a decision over it. This way, the final decision relies upon the decisions
retrieved from the other nodes.
Stellar, Ripple, and Hyperledger Fabric are some use cases of this blockchain
consensus mechanism.
1) Request: The client sends a request to the master server node or primary
node, the master node gives the request a timestamp.
2) Pre-prepare: The master server node records the request message and
CO-1
gives it an order number. Then the master node broadcasts a pre-prepare
BL-2
message to the other following server or backup nodes. The other server
nodes initially determine whether to accept the request or not.
3) Prepare: If a server node chooses to accept the request, it broadcasts a
prepare message to all the other server nodes and receives the prepare
messages from the other nodes. After having collected 2f+1 messages, if a
majority of nodes choose to accept the request, then it will enter the commit
state.
4) Commit: Each node in commit state sends a commit message to all the
other nodes in the server. At the same time, if a server node receives 2f+1
commit messages, it could believe that most nodes reach a consensus to
accept the request. Then the node executes the instructions in the request
message.
5) Reply: the server nodes reply to the client. If the client does not receive a
reply because of the network delay, the request is resent to the server nodes.
If the request has been executed, the server nodes only need to send the reply
message repeatedly.
********** 5 **********
--- page 6 ---
a. The curve has 18 points (including the point at infinity).   [10]
Q6
CO-1
BL-3
b. Coinbase transaction: In the context of blockchain technology, a coinbase [10]
transaction is a special type of transaction that creates new coins and awards them
to the miner who successfully adds a new block to the blockchain.
Not related to the coinbase cryptocurrency exchange.
•   First transaction in every block
•   Creates new BTC
• Pays mining reward
• Has no inputs
Created by miners on the network.
CO-3
BL-3   1. bc1p5d7rjq7g6rdk2yhzks9smlaqtedr4dekq08ge8ztwac72sfr9rusxg3297   –
Valid bitcoin address. Taproot (P2TR)
2. bc1q42lja79elem0anu8q8s3h2n687re9jax556pcc - Valid bitcoin address
Native SegWit (Bech32)
3. b1qarsrrr7ASHy5643ydab9re59gtzzwfrah – invalid. Wrong prefix
4. 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045-   valid Ethereum
address
5. 0x71c7656ec7ab88b098defb751b7401b5f6d8976g   -   Invalid   (invalid
character, only hexadecimal characters permitted)
a. Step 1: Gas Fee = 100,000 × 40 Gwei = 0.004 ETH   [10]
Step 2: Total Sent = 0.5 + 0.7 + 0.3 = 1.5 ETH
Q7
CO-3
Step 3: Total Deduction = 1.5 + 0.004 = 1.504 ETH
BL-4
Step 4: Remaining Balance = 3.0 − 1.504 = 1.496 ETH
********** 6 **********
--- page 7 ---
1. Change Address? None
2. Primary Payments: 3
3. Who shows this behavior?
• DeFi platforms
• Payment batching services
• Smart contract-based wallets
Benefit:
• Automation
• Reduced manual transactions
•   Efficient multi-party payments
b. Change Address: Addr_D (2.249 BTC)   [10]
Reasoning: It is the "remainder" left over after several specific payments are
subtracted from the Input.
Primary Payments: Three (Addr_A through Addr_C).
Type of Organizations
• Cryptocurrency exchanges
• Payment processors
• Mining pools
Justification:
These entities often:
CO-3   • Bundle multiple payments into one transaction
BL-4   • Use one large input and distribute funds to many users
• Generate a change address for leftover funds.
Primary Benefit of This Behaviour
Transaction efficiency and cost reduction
Justification:
• Combining multiple payments into one transaction:
• Reduces transaction fees per payment
• Improves block space efficiency
• Also provides some privacy benefits by making tracing slightly more
complex (though not foolproof)
********** 7 **********
````
