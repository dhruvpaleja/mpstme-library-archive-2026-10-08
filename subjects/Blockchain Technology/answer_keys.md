# Blockchain Technology: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 99d421f7b88e

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ;   a.   Explain the limitations of traditional Distributed DBMS.   [5]
SO-2 ;
BL-1   Answer:
Limitation   Description
Design, deployment, and maintenance are
Complexity
difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Fault tolerance and transaction rollback are
Recovery
complex
Concurrency   Synchronizing access is difficult and error-prone
High due to software, hardware, and expertise
Cost
needs
CO-2 ;   b.   Differentiate between tokenized and tokenless blockchains with suitable   [5]
SO-2 ;   examples.
BL-2
Answer: A tokenized blockchain uses a native digital token (cryptocurrency)
to power the network, incentivize participants, and validate transactions.
A tokenless blockchain operates without any native cryptocurrency and
focuses mainly on data sharing and enterprise applications.
Presence of Cryptocurrency
Tokenized: Has its own cryptocurrency (e.g., Bitcoin, Ethereum).
Tokenless: No native cryptocurrency is used.
Incentive Mechanism
********** 1 **********
--- page 2 ---
Tokenized: Participants (miners/validators) are rewarded with
tokens for validating transactions.
Tokenless: No financial incentives; participants are usually
authorized entities working collaboratively.
Network Type
Tokenized: Mostly used in public or open blockchains.
Tokenless: Common in private or permissioned blockchains.
Use Cases
Tokenized:
Cryptocurrencies
Decentralized finance (DeFi)
Digital payments
Tokenless:
Supply chain management
Banking systems
Enterprise data sharing
CO-2 ;   c. What is contractual confidentiality in blockchain systems? Why is it   [5]
SO-2 ;   important?
BL-1
Answer: Contractual confidentiality refers to the ability to keep the details of
a contract (such as terms, conditions, and participant data) private and
accessible only to authorized parties, even when the contract is executed on a
blockchain network.
In blockchain systems—especially when using Smart Contracts—transactions
are typically transparent. However, not all business agreements can be
publicly visible. Contractual confidentiality ensures that sensitive information
is protected while still benefiting from blockchain features like security and
immutability.
Why is it Important?
1. Protection of Sensitive Data
2. Privacy in Transparent Systems
3. Regulatory Compliance
4. Secure Business Transactions
5. Trust Among Participants
CO-3 ;   d.   Explain the importance of Turing-Completeness with an appropriate   [5]
SO-2 ;   example.
BL-2
Answer: Turing-Completeness is a property of a computational system that
indicates it can perform any computation or solve any problem that a Turing
Machine can, provided sufficient time and memory.
Importance:
1. Flexibility in Programming:
A Turing-complete system can implement complex logic, algorithms, and
computations, making it highly versatile.
2. Smart Contract Capability:
In blockchain, Turing-completeness allows developers to write advanced
smart contracts with conditional logic, loops, and functions.
3. Automation of Complex Processes:
It enables automation of real-world agreements and workflows without
intermediaries.
********** 2 **********
--- page 3 ---
4. Wide Range of Applications:
Supports development of decentralized applications (dApps), games,
financial systems, and more.
Example:
Ethereum is a Turing-complete blockchain. Its smart contract language
(Solidity) allows developers to write complex programs—for example, a
decentralized lending system that automatically calculates interest, checks
conditions, and executes transactions based on predefined rules.
Attempt any 4
Q2   a. Draw and explain generic structure of Blockchain. Explain in details the   [10]
elements of Blockchain.
CO-1 ;
SO-2 ;
BL-2
Answer:
Address: Addresses are unique identifiers used in a blockchain transaction to
denote senders and recipients. An address is usually a public key or derived
from a public key. While addresses can be reused by the same user, addresses
themselves are unique. In practice, however, a single user may not use the
same address again and generate a new one for each transaction. This newly-
created address will be unique. A good practice is for users to generate a new
address for each transaction in order to avoid linking transactions to the
common owner, thus preventing identification.
Transaction: A transaction is the fundamental unit of a blockchain. A
transaction represents a transfer of value from one address to another. Block:
A block is composed of multiple transactions and other elements, such as the
previous block hash (hash pointer), timestamp, and nonce.
Peer-to-peer network: As the name implies, a peer-to-peer network is a
network topology wherein all peers can communicate with each other and
send and receive messages.
Scripting or programming language: Scripts or programs perform various
operations on a transaction in order to facilitate various functions. For
example, in Bitcoin, transaction scripts are predefined in a language called
Script, which consist of sets of commands that allow nodes to transfer tokens
from one address to another.
Bitcoins scripting language
Ethereum solidity language (Turing Complete)
Q2   b.   Explain the difference between Sybil attacks and Selfish Mining in   [10]
blockchain.
CO-3 ;
SO-2 ;
Answer:
BL-2
Basis   Sybil Attack   Selfish Mining
An attack where a single   A strategy where a miner or group
entity creates multiple fake   of miners withhold mined blocks to
Definition
identities (nodes) to gain   gain an unfair advantage and
control over the network.   increase their rewards.
To manipulate network
Main   operations like voting,   To maximize mining rewards by
Objective   consensus, or reputation   controlling the release of blocks.
systems.
********** 3 **********
--- page 4 ---
Creating numerous fake
Method   Keeping mined blocks private and
nodes to dominate the
Used   releasing them strategically.
network.
Can disrupt consensus,
Impact on   Leads to unfair reward distribution
reduce trust, and enable
Network   and reduces network efficiency.
double-spending.
Target Area Peer-to-peer network layer.   Mining and consensus mechanism.
An attacker flooding a
A miner in Bitcoin hiding blocks to
Example   blockchain network with fake
outperform honest miners.
nodes to influence decisions.
Q3   a. What are oracles in blockchain? Explain their types and their role in smart   [10]
contracts.
CO-3 ;
SO-2 ;
BL-2
Answer: Oracles are third-party services that act as a bridge between a
blockchain and the outside world. Since blockchains cannot directly access
external data (due to security and determinism constraints), oracles provide
real-world data to smart contracts and also send data from smart contracts
to external systems.
Types of Oracles
1. Software Oracles
• Provide data from online sources such as websites, APIs, and
databases.
• Examples: weather data, stock prices, sports results.
• Widely used in financial and prediction-based smart contracts.
2. Hardware Oracles
•   Collect data from physical devices and sensors.
• Examples: RFID sensors, temperature sensors, barcode scanners.
•   Useful in supply chain systems where physical events must be
recorded on blockchain.
3. Inbound Oracles
•   Bring external data into the blockchain.
• Example: Sending current market price of a commodity to a smart
contract for futures trading.
4. Outbound Oracles
• Send data from blockchain to the outside world.
• Example: A smart contract triggers a bank payment or sends a
notification after conditions are met.
Role of Oracles in Smart Contracts
• Data Feeding: Provide real-time and accurate external data required
for contract execution.
********** 4 **********
--- page 5 ---
• Automation: Enable smart contracts to execute automatically when
predefined real-world conditions are met.
•   Interoperability: Allow blockchain systems to interact with external
systems such as banking networks, IoT devices, and APIs.
• Use in Futures Systems: In blockchain-based futures trading, oracles
supply market prices, enabling automatic settlement of contracts.
Q3   b.   Explain the types of Ethereum accounts and the working mechanism of the   [10]
CO-2 ;   Ethereum blockchain.
SO-2 ;
BL-2   Answer: Types of Ethereum Accounts
In Ethereum, there are mainly two types of accounts:
a) Externally Owned Accounts (EOAs)
•   Controlled by users through private keys.
• Used to send and receive Ether and initiate transactions.
• Do not contain executable code.
• Example: A user wallet used for transferring ETH.
b) Contract Accounts
•   Controlled by smart contract code, not by private keys.
• Created when a smart contract is deployed on the blockchain.
•   Automatically execute predefined functions when triggered.
• Used in applications like DeFi, voting systems, etc
Working Mechanism of Ethereum Blockchain
The working of Ethereum involves several steps:
Step 1: Transaction Initiation
• A user (via EOA) creates a transaction (sending Ether or interacting
with a smart contract).
• The transaction is signed using the user’s private key.
Step 2: Transaction Broadcasting
• The transaction is broadcast to the Ethereum network and enters the
mempool (pending transactions).
Step 3: Validation by Nodes
• Nodes verify the transaction for correctness (valid signature,
sufficient balance, etc.).
Step 4: Block Creation
•   Validators/miners collect valid transactions and group them into a
block.
Step 5: Consensus Mechanism
• Ethereum uses Proof of Stake (PoS) (earlier Proof of Work).
•   Validators stake Ether and are chosen to validate and add new blocks.
********** 5 **********
--- page 6 ---
Step 6: Execution of Smart Contracts
•   If the transaction involves a contract, the code is executed on the
Ethereum Virtual Machine (EVM).
Step 7: Block Addition
• The validated block is added to the blockchain.
• The ledger is updated across all nodes.
Step 8: Transaction Confirmation
• The transaction becomes immutable and is confirmed after multiple
blocks are added.
Q4   a. What is Ethereum? Explain its key benefits and discuss the limitations of the   [10]
CO-3 ;   Ethereum platform.
SO-2 ;
BL-3   Answer: Ethereum is a decentralized, open-source blockchain platform that
enables developers to build and deploy smart contracts and decentralized
applications (dApps).
Unlike traditional blockchains that mainly support digital currency
transactions, Ethereum allows programmable logic through its Ethereum
Virtual Machine (EVM).
Key Benefits of Ethereum
1. Decentralization
o No central authority controls the network.
o Reduces risk of censorship and single point of failure.
2. Smart Contracts
o Self-executing contracts that run automatically when
conditions are met.
o Eliminates intermediaries and increases efficiency.
3. Transparency and Security
o   All transactions are recorded on a public ledger.
o Data is secure and tamper-resistant.
4. Programmability
o Developers can build a wide range of applications (DeFi, NFTs,
gaming, etc.).
5. Global Accessibility
o Anyone with internet access can participate in the network.
6. Tokenization
o Supports creation of custom tokens (ERC-20, NFTs), enabling
digital assets and fundraising.
Limitations of Ethereum
1. Scalability Issues
o Limited transactions per second (TPS), leading to network
congestion.
2. High Gas Fees
o Transaction costs can become very high during peak usage.
3. Complexity
o Development and usage require technical knowledge.
4. Security Risks in Smart Contracts
o Bugs in contract code can lead to financial losses.
********** 6 **********
--- page 7 ---
5. Energy Consumption (Earlier)
o Previously used Proof of Work, which consumed high energy
(now improved with Proof of Stake).
6. Network Congestion
o Heavy usage can slow down transaction processing.
Q4   b.   Explain 51% attacks in blockchain. Discuss real-world cases of 51% attacks   [10]
CO-1 ;   and explain possible mitigation strategies in detail.
SO-2 ;
BL-2   Answer: A 51% attack occurs when a single entity or group gains control of
more than 50% of a blockchain network’s mining or validation power.
This allows the attacker to manipulate the blockchain by:
•   Reversing transactions (double spending)
•   Preventing new transactions from being confirmed
•   Blocking or modifying transaction order
It mainly affects Proof of Work (PoW) blockchains.
Real-World Cases of 51% Attacks
a) Ethereum Classic (2019, 2020)
• Attacked multiple times.
• Hackers reorganized the blockchain and performed double-spending
attacks.
•   Millions of dollars worth of ETC were lost.
b) Bitcoin Gold (2018)
•   Attackers gained majority hash power.
• Double-spent coins worth over $18 million.
• Exchanges suffered significant losses.
c) Vertcoin (2018, 2019)
•   Suffered repeated 51% attacks.
•   Attackers reorganized blocks and executed double spending.
Mitigation Strategies
a) Increase Network Hash Power
• A larger and more decentralized network makes attacks expensive
and difficult.
b) Transition to Proof of Stake (PoS)
•   In PoS, attackers need to control a majority of staked coins, which is
costly.
• Example: Ethereum moved from PoW to PoS.
c) Confirmation Delays
• Exchanges can require more confirmations before accepting
transactions, reducing double-spending risk.
********** 7 **********
--- page 8 ---
d) Mining Pool Decentralization
• Avoid concentration of mining power in a few pools.
e) Checkpointing
• Hard-code checkpoints in the blockchain to prevent deep chain
reorganizations.
f) Hybrid Consensus Mechanisms
• Combine PoW with PoS or other methods to improve security.
g) Monitoring and Alerts
•   Detect unusual hash rate spikes or suspicious chain reorganizations.
Q5   a. What are the steps involved in blockchain development and deployment?   [10]
CO-3 ;   Explain in detail.
SO-2 ;
BL-2   Answer: 1. Problem Identification and Use Case Definition
•   Clearly define the problem you want to solve.
• Determine whether blockchain is actually needed (e.g., need for
decentralization, trust, transparency).
•   Identify the use case such as supply chain, finance, healthcare, etc.
2. Choosing the Right Blockchain Platform
•   Select an appropriate platform based on requirements:
o Ethereum – for smart contracts and dApps
o Hyperledger Fabric – for permissioned enterprise solutions
o Corda – for financial applications
3. Designing the Architecture
• Decide the type of blockchain: public, private, or consortium.
•   Define network structure, nodes, consensus mechanism, and data
flow.
• Plan security, scalability, and privacy requirements.
4. Smart Contract Development
• Write smart contracts (business logic) using appropriate languages
(e.g., Solidity).
•   Define rules, conditions, and workflows.
• Ensure proper coding practices to avoid vulnerabilities.
5. Frontend and Backend Development
• Develop user interface (UI) for interaction.
•   Build backend systems to connect blockchain with applications (APIs,
databases).
• Use tools like Web3.js or similar libraries.
********** 8 **********
--- page 9 ---
6. Testing
• Perform unit testing, integration testing, and system testing.
• Use test networks (testnets) to simulate real-world scenarios.
•   Identify and fix bugs or vulnerabilities.
7. Security Auditing
• Conduct thorough smart contract audits.
• Check for issues like reentrancy, overflow, and access control flaws.
• May involve third-party security audits.
8. Deployment
• Deploy smart contracts on the main network (mainnet).
•   Configure nodes and network settings.
• Ensure proper gas fees and deployment parameters.
9. Monitoring and Mainenance
• Continuously monitor performance and transactions.
•   Fix bugs, upgrade contracts (if possible), and optimize performance.
• Ensure network security and handle updates.
10. Scaling and Optimization
• Improve performance using Layer 2 solutions, sharding, or
sidechains.
• Optimize transaction speed and cost.
Q5   b.   Explain how blockchain technology is evolving in the field of finance. Discuss   [10]
CO-2 ;   its benefits and challenges with suitable examples.
SO-2 ;
BL-2   Answer: Evolution of Blockchain in Finance
Blockchain technology has significantly transformed the financial sector by
introducing decentralization, transparency, and automation.
a) Digital Payments and Cryptocurrencies
• Blockchain enables peer-to-peer transactions without intermediaries.
• Example: Bitcoin allows global payments with lower fees and faster
processing.
b) Smart Contracts and DeFi
•   Platforms like Ethereum enable Decentralized Finance (DeFi).
•   Services such as lending, borrowing, and trading are automated using
smart contracts.
c) Cross-Border Payments
•   Traditional international transfers are slow and expensive.
• Blockchain solutions reduce transaction time from days to minutes.
********** 9 **********
--- page 10 ---
d) Tokenization of Assets
• Real-world assets (stocks, real estate) are converted into digital
tokens.
• Enables fractional ownership and increased liquidity.
e) Clearing and Settlement
• Blockchain reduces settlement time in financial markets (T+2 → near
real-time).
•   Eliminates intermediaries like clearing houses.
2. Benefits of Blockchain in Finance
1. Transparency
o   All transactions are recorded on a shared ledger.
o Reduces fraud and increases trust.
2. Security
o Cryptographic techniques ensure data integrity and
protection.
3. Cost Reduction
o Removes intermediaries, lowering transaction and operational
costs.
4. Speed and Efficiency
o Faster transactions, especially in cross-border payments.
5. Financial Inclusion
o Provides access to financial services for unbanked
populations.
6. Automation
o Smart contracts automate processes, reducing human error.
3. Challenges of Blockchain in Finance
1. Regulatory Uncertainty
o Governments are still developing laws for blockchain and
cryptocurrencies.
2. Scalability Issues
o Networks may struggle with high transaction volumes.
3. Security Risks
o Smart contract bugs and cyberattacks can lead to losses.
4. High Implementation Cost
o   Initial setup and integration with existing systems can be
expensive.
5. Energy Consumption (Earlier Systems)
o Some blockchains (PoW-based) consume high energy.
6. Lack of Awareness and Adoption
o Limited understanding slows adoption in traditional finance.
Q6   a.   Differentiate between Public Blockchain and Private Blockchain. Discuss their [10]
CO-3 ;   suitability for financial applications.
SO-2 ;
BL-2   Answer:
Basis   Public Blockchain   Private Blockchain
Restricted to authorized
Open to anyone
Access   participants
(permissionless)
(permissioned)
********** 10 **********
--- page 11 ---
Controlled by a single
Fully decentralized (no
Control   organization or
single authority)
consortium
Limited – only selected
High – all transactions
Transparency   participants can view
are visible
data
Very high (due to large   High, but depends on
Security
distributed network)   internal controls
Slower (due to
Faster (fewer nodes and
Speed   consensus mechanisms
simplified consensus)
like PoW/PoS)
Higher transaction cost Lower cost (no mining
Cost
(fees, energy use)   required)
Hyperledger Fabric, R3
Examples   Bitcoin, Ethereum
Corda
Public blockchains are ideal for open, trustless financial ecosystems, while
private blockchains are more suitable for controlled, secure, and regulation-
compliant financial environments. In practice, many financial institutions
prefer private or hybrid models to balance efficiency, privacy, and control.
Q6   b.   Explain how decentralization, transparency, and immutability contribute to   [10]
CO-2 ;   the evolution of futures trading using blockchain technology.
SO-2 ;
BL-2   Answer: 1. Decentralization
Decentralization means that control is not held by a single authority (like an
exchange or clearing house). Instead, the blockchain network is maintained by
multiple nodes.
Impact on Futures Trading:
Eliminates intermediaries such as brokers and clearing houses
Reduces transaction costs and delays
Minimizes single points of failure and manipulation
Enables peer-to-peer futures contracts using Smart Contracts
2. Transparency
All transactions on a blockchain are recorded on a shared ledger and are
visible to participants (depending on the type of blockchain).
Impact on Futures Trading:
Improves trust among traders due to open access to transaction history
Reduces fraud and market manipulation
Enhances auditability and regulatory oversight
Provides real-time tracking of futures contracts and settlements
3. Immutability
Once data is recorded on the blockchain, it cannot be altered or deleted due to
cryptographic linking of blocks.
Impact on Futures Trading:
Ensures integrity of contract terms and transaction records
Prevents disputes and tampering with trade data
Provides a reliable and permanent audit trail
Strengthens trust in automated settlement systems
Q7   a. Compare different consensus mechanisms (PoW, PoS, BFT, PoA, PoET) based   [10]
on energy efficiency, security, and scalability.
********** 11 **********
--- page 12 ---
CO-3 ;
SO-2 ;   Answer:
BL-2   Consensus
Energy Efficiency   Security   Scalability
Mechanism
Very high (strong Low (slow
Very low (high
Proof of Work   against attacks   transaction speed,
energy consumption
(PoW)   like double   limited
due to mining)
spending)   throughput)
High (no heavy
Proof of Stake   High (depends on Medium to High
computation
(PoS)   stake distribution) (faster than PoW)
required)
Byzantine   Very high   Medium (works
High (minimal
Fault   (tolerates   well in smaller
computational
Tolerance   malicious nodes   networks, limited
work)
(BFT)   effectively)   scalability)
Proof of   Medium to High   High (fast
Very high (low
Authority   (depends on   transaction
resource usage)
(PoA)   trusted validators) processing)
Very high (efficient High (secure if   High (good
Proof of
use of waiting time trusted execution performance in
Elapsed Time
via trusted   environment is   permissioned
(PoET)
hardware)   reliable)   systems)
Q7   b. What is a blockchain platform? Explain Hyperledger Fabric and Corda in   [10]
CO-1 ;   detail.
SO-2 ;   Answer: A blockchain platform is a digital infrastructure that allows
BL-2   developers and organizations to build, run, and manage blockchain-based
applications such as smart contracts and decentralized systems.
It provides tools, protocols, and frameworks to create secure, transparent,
and distributed networks.
Hyperledger Fabric is an open-source, permissioned blockchain platform
developed under the Linux Foundation.
Key Features:
• Permissioned Network:
Only authorized participants can join and perform transactions.
• Modular Architecture:
Components like consensus and membership services can be
customized.
• No Native Cryptocurrency:
It is a tokenless blockchain, mainly used for enterprise applications.
• Smart Contracts (Chaincode):
Written in languages like Go, Java, or Node.js.
• Channels for Privacy:
Allows private communication between specific participants.
Working:
1. A transaction is proposed by a client.
2. Endorsing peers validate the transaction.
3. The ordering service orders transactions into blocks.
4. Blocks are distributed and validated across the network.
5. Ledger is updated.
********** 12 **********
--- page 13 ---
Use Cases:
• Supply chain management
• Banking and finance
•   Healthcare systems
3. Corda
Corda is a distributed ledger platform designed mainly for financial
institutions, developed by the R3.
Key Features:
• Permissioned Network:
Only trusted parties can participate.
• No Global Broadcast:
Transactions are shared only with relevant parties (privacy-focused).
• No Native Cryptocurrency:
Designed for real-world financial agreements rather than tokens.
• Smart Contracts:
Written in Java or Kotlin.
• Notary Service:
• Ensures transaction uniqueness and prevents double-spending.
Working:
1. Parties involved agree on a transaction.
2. Transaction is verified using smart contract rules.
3. Notary validates uniqueness.
4. Transaction is recorded only by relevant participants.
Use Cases:
• Banking and financial services
• Trade finance
• Insurance
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper fa24ddaa67f6

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ;   a.   Explain the limitations of traditional Distributed DBMS.   [5]
SO-2 ;
BL-1   Answer:
Limitation   Description
Design, deployment, and maintenance are
Complexity
difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Fault tolerance and transaction rollback are
Recovery
complex
Concurrency   Synchronizing access is difficult and error-prone
High due to software, hardware, and expertise
Cost
needs
CO-2 ;   b.   Differentiate between tokenized and tokenless blockchains with suitable   [5]
SO-2 ;   examples.
BL-2
Answer: A tokenized blockchain uses a native digital token (cryptocurrency)
to power the network, incentivize participants, and validate transactions.
A tokenless blockchain operates without any native cryptocurrency and
focuses mainly on data sharing and enterprise applications.
Presence of Cryptocurrency
Tokenized: Has its own cryptocurrency (e.g., Bitcoin, Ethereum).
Tokenless: No native cryptocurrency is used.
Incentive Mechanism
********** 1 **********
--- page 2 ---
Tokenized: Participants (miners/validators) are rewarded with
tokens for validating transactions.
Tokenless: No financial incentives; participants are usually
authorized entities working collaboratively.
Network Type
Tokenized: Mostly used in public or open blockchains.
Tokenless: Common in private or permissioned blockchains.
Use Cases
Tokenized:
Cryptocurrencies
Decentralized finance (DeFi)
Digital payments
Tokenless:
Supply chain management
Banking systems
Enterprise data sharing
CO-2 ;   c. What is contractual confidentiality in blockchain systems? Why is it   [5]
SO-2 ;   important?
BL-1
Answer: Contractual confidentiality refers to the ability to keep the details of
a contract (such as terms, conditions, and participant data) private and
accessible only to authorized parties, even when the contract is executed on a
blockchain network.
In blockchain systems—especially when using Smart Contracts—transactions
are typically transparent. However, not all business agreements can be
publicly visible. Contractual confidentiality ensures that sensitive information
is protected while still benefiting from blockchain features like security and
immutability.
Why is it Important?
1. Protection of Sensitive Data
2. Privacy in Transparent Systems
3. Regulatory Compliance
4. Secure Business Transactions
5. Trust Among Participants
CO-3 ;   d.   Explain the importance of Turing-Completeness with an appropriate   [5]
SO-2 ;   example.
BL-2
Answer: Turing-Completeness is a property of a computational system that
indicates it can perform any computation or solve any problem that a Turing
Machine can, provided sufficient time and memory.
Importance:
1. Flexibility in Programming:
A Turing-complete system can implement complex logic, algorithms, and
computations, making it highly versatile.
2. Smart Contract Capability:
In blockchain, Turing-completeness allows developers to write advanced
smart contracts with conditional logic, loops, and functions.
3. Automation of Complex Processes:
It enables automation of real-world agreements and workflows without
intermediaries.
********** 2 **********
--- page 3 ---
4. Wide Range of Applications:
Supports development of decentralized applications (dApps), games,
financial systems, and more.
Example:
Ethereum is a Turing-complete blockchain. Its smart contract language
(Solidity) allows developers to write complex programs—for example, a
decentralized lending system that automatically calculates interest, checks
conditions, and executes transactions based on predefined rules.
Attempt any 4
Q2   a. Draw and explain generic structure of Blockchain. Explain in details the   [10]
elements of Blockchain.
CO-1 ;
SO-2 ;
BL-2
Answer:
Address: Addresses are unique identifiers used in a blockchain transaction to
denote senders and recipients. An address is usually a public key or derived
from a public key. While addresses can be reused by the same user, addresses
themselves are unique. In practice, however, a single user may not use the
same address again and generate a new one for each transaction. This newly-
created address will be unique. A good practice is for users to generate a new
address for each transaction in order to avoid linking transactions to the
common owner, thus preventing identification.
Transaction: A transaction is the fundamental unit of a blockchain. A
transaction represents a transfer of value from one address to another. Block:
A block is composed of multiple transactions and other elements, such as the
previous block hash (hash pointer), timestamp, and nonce.
Peer-to-peer network: As the name implies, a peer-to-peer network is a
network topology wherein all peers can communicate with each other and
send and receive messages.
Scripting or programming language: Scripts or programs perform various
operations on a transaction in order to facilitate various functions. For
example, in Bitcoin, transaction scripts are predefined in a language called
Script, which consist of sets of commands that allow nodes to transfer tokens
from one address to another.
Bitcoins scripting language
Ethereum solidity language (Turing Complete)
Q2   b.   Explain the difference between Sybil attacks and Selfish Mining in   [10]
blockchain.
CO-3 ;
SO-2 ;
Answer:
BL-2
Basis   Sybil Attack   Selfish Mining
An attack where a single   A strategy where a miner or group
entity creates multiple fake   of miners withhold mined blocks to
Definition
identities (nodes) to gain   gain an unfair advantage and
control over the network.   increase their rewards.
To manipulate network
Main   operations like voting,   To maximize mining rewards by
Objective   consensus, or reputation   controlling the release of blocks.
systems.
********** 3 **********
--- page 4 ---
Creating numerous fake
Method   Keeping mined blocks private and
nodes to dominate the
Used   releasing them strategically.
network.
Can disrupt consensus,
Impact on   Leads to unfair reward distribution
reduce trust, and enable
Network   and reduces network efficiency.
double-spending.
Target Area Peer-to-peer network layer.   Mining and consensus mechanism.
An attacker flooding a
A miner in Bitcoin hiding blocks to
Example   blockchain network with fake
outperform honest miners.
nodes to influence decisions.
Q3   a. What are oracles in blockchain? Explain their types and their role in smart   [10]
contracts.
CO-3 ;
SO-2 ;
BL-2
Answer: Oracles are third-party services that act as a bridge between a
blockchain and the outside world. Since blockchains cannot directly access
external data (due to security and determinism constraints), oracles provide
real-world data to smart contracts and also send data from smart contracts
to external systems.
Types of Oracles
1. Software Oracles
• Provide data from online sources such as websites, APIs, and
databases.
• Examples: weather data, stock prices, sports results.
• Widely used in financial and prediction-based smart contracts.
2. Hardware Oracles
•   Collect data from physical devices and sensors.
• Examples: RFID sensors, temperature sensors, barcode scanners.
•   Useful in supply chain systems where physical events must be
recorded on blockchain.
3. Inbound Oracles
•   Bring external data into the blockchain.
• Example: Sending current market price of a commodity to a smart
contract for futures trading.
4. Outbound Oracles
• Send data from blockchain to the outside world.
• Example: A smart contract triggers a bank payment or sends a
notification after conditions are met.
Role of Oracles in Smart Contracts
• Data Feeding: Provide real-time and accurate external data required
for contract execution.
********** 4 **********
--- page 5 ---
• Automation: Enable smart contracts to execute automatically when
predefined real-world conditions are met.
•   Interoperability: Allow blockchain systems to interact with external
systems such as banking networks, IoT devices, and APIs.
• Use in Futures Systems: In blockchain-based futures trading, oracles
supply market prices, enabling automatic settlement of contracts.
Q3   b.   Explain the types of Ethereum accounts and the working mechanism of the   [10]
CO-2 ;   Ethereum blockchain.
SO-2 ;
BL-2   Answer: Types of Ethereum Accounts
In Ethereum, there are mainly two types of accounts:
a) Externally Owned Accounts (EOAs)
•   Controlled by users through private keys.
• Used to send and receive Ether and initiate transactions.
• Do not contain executable code.
• Example: A user wallet used for transferring ETH.
b) Contract Accounts
•   Controlled by smart contract code, not by private keys.
• Created when a smart contract is deployed on the blockchain.
•   Automatically execute predefined functions when triggered.
• Used in applications like DeFi, voting systems, etc
Working Mechanism of Ethereum Blockchain
The working of Ethereum involves several steps:
Step 1: Transaction Initiation
• A user (via EOA) creates a transaction (sending Ether or interacting
with a smart contract).
• The transaction is signed using the user’s private key.
Step 2: Transaction Broadcasting
• The transaction is broadcast to the Ethereum network and enters the
mempool (pending transactions).
Step 3: Validation by Nodes
• Nodes verify the transaction for correctness (valid signature,
sufficient balance, etc.).
Step 4: Block Creation
•   Validators/miners collect valid transactions and group them into a
block.
Step 5: Consensus Mechanism
• Ethereum uses Proof of Stake (PoS) (earlier Proof of Work).
•   Validators stake Ether and are chosen to validate and add new blocks.
********** 5 **********
--- page 6 ---
Step 6: Execution of Smart Contracts
•   If the transaction involves a contract, the code is executed on the
Ethereum Virtual Machine (EVM).
Step 7: Block Addition
• The validated block is added to the blockchain.
• The ledger is updated across all nodes.
Step 8: Transaction Confirmation
• The transaction becomes immutable and is confirmed after multiple
blocks are added.
Q4   a. What is Ethereum? Explain its key benefits and discuss the limitations of the   [10]
CO-3 ;   Ethereum platform.
SO-2 ;
BL-3   Answer: Ethereum is a decentralized, open-source blockchain platform that
enables developers to build and deploy smart contracts and decentralized
applications (dApps).
Unlike traditional blockchains that mainly support digital currency
transactions, Ethereum allows programmable logic through its Ethereum
Virtual Machine (EVM).
Key Benefits of Ethereum
1. Decentralization
o No central authority controls the network.
o Reduces risk of censorship and single point of failure.
2. Smart Contracts
o Self-executing contracts that run automatically when
conditions are met.
o Eliminates intermediaries and increases efficiency.
3. Transparency and Security
o   All transactions are recorded on a public ledger.
o Data is secure and tamper-resistant.
4. Programmability
o Developers can build a wide range of applications (DeFi, NFTs,
gaming, etc.).
5. Global Accessibility
o Anyone with internet access can participate in the network.
6. Tokenization
o Supports creation of custom tokens (ERC-20, NFTs), enabling
digital assets and fundraising.
Limitations of Ethereum
1. Scalability Issues
o Limited transactions per second (TPS), leading to network
congestion.
2. High Gas Fees
o Transaction costs can become very high during peak usage.
3. Complexity
o Development and usage require technical knowledge.
4. Security Risks in Smart Contracts
o Bugs in contract code can lead to financial losses.
********** 6 **********
--- page 7 ---
5. Energy Consumption (Earlier)
o Previously used Proof of Work, which consumed high energy
(now improved with Proof of Stake).
6. Network Congestion
o Heavy usage can slow down transaction processing.
Q4   b.   Explain 51% attacks in blockchain. Discuss real-world cases of 51% attacks   [10]
CO-1 ;   and explain possible mitigation strategies in detail.
SO-2 ;
BL-2   Answer: A 51% attack occurs when a single entity or group gains control of
more than 50% of a blockchain network’s mining or validation power.
This allows the attacker to manipulate the blockchain by:
•   Reversing transactions (double spending)
•   Preventing new transactions from being confirmed
•   Blocking or modifying transaction order
It mainly affects Proof of Work (PoW) blockchains.
Real-World Cases of 51% Attacks
a) Ethereum Classic (2019, 2020)
• Attacked multiple times.
• Hackers reorganized the blockchain and performed double-spending
attacks.
•   Millions of dollars worth of ETC were lost.
b) Bitcoin Gold (2018)
•   Attackers gained majority hash power.
• Double-spent coins worth over $18 million.
• Exchanges suffered significant losses.
c) Vertcoin (2018, 2019)
•   Suffered repeated 51% attacks.
•   Attackers reorganized blocks and executed double spending.
Mitigation Strategies
a) Increase Network Hash Power
• A larger and more decentralized network makes attacks expensive
and difficult.
b) Transition to Proof of Stake (PoS)
•   In PoS, attackers need to control a majority of staked coins, which is
costly.
• Example: Ethereum moved from PoW to PoS.
c) Confirmation Delays
• Exchanges can require more confirmations before accepting
transactions, reducing double-spending risk.
********** 7 **********
--- page 8 ---
d) Mining Pool Decentralization
• Avoid concentration of mining power in a few pools.
e) Checkpointing
• Hard-code checkpoints in the blockchain to prevent deep chain
reorganizations.
f) Hybrid Consensus Mechanisms
• Combine PoW with PoS or other methods to improve security.
g) Monitoring and Alerts
•   Detect unusual hash rate spikes or suspicious chain reorganizations.
Q5   a. What are the steps involved in blockchain development and deployment?   [10]
CO-3 ;   Explain in detail.
SO-2 ;
BL-2   Answer: 1. Problem Identification and Use Case Definition
•   Clearly define the problem you want to solve.
• Determine whether blockchain is actually needed (e.g., need for
decentralization, trust, transparency).
•   Identify the use case such as supply chain, finance, healthcare, etc.
2. Choosing the Right Blockchain Platform
•   Select an appropriate platform based on requirements:
o Ethereum – for smart contracts and dApps
o Hyperledger Fabric – for permissioned enterprise solutions
o Corda – for financial applications
3. Designing the Architecture
• Decide the type of blockchain: public, private, or consortium.
•   Define network structure, nodes, consensus mechanism, and data
flow.
• Plan security, scalability, and privacy requirements.
4. Smart Contract Development
• Write smart contracts (business logic) using appropriate languages
(e.g., Solidity).
•   Define rules, conditions, and workflows.
• Ensure proper coding practices to avoid vulnerabilities.
5. Frontend and Backend Development
• Develop user interface (UI) for interaction.
•   Build backend systems to connect blockchain with applications (APIs,
databases).
• Use tools like Web3.js or similar libraries.
********** 8 **********
--- page 9 ---
6. Testing
• Perform unit testing, integration testing, and system testing.
• Use test networks (testnets) to simulate real-world scenarios.
•   Identify and fix bugs or vulnerabilities.
7. Security Auditing
• Conduct thorough smart contract audits.
• Check for issues like reentrancy, overflow, and access control flaws.
• May involve third-party security audits.
8. Deployment
• Deploy smart contracts on the main network (mainnet).
•   Configure nodes and network settings.
• Ensure proper gas fees and deployment parameters.
9. Monitoring and Mainenance
• Continuously monitor performance and transactions.
•   Fix bugs, upgrade contracts (if possible), and optimize performance.
• Ensure network security and handle updates.
10. Scaling and Optimization
• Improve performance using Layer 2 solutions, sharding, or
sidechains.
• Optimize transaction speed and cost.
Q5   b.   Explain how blockchain technology is evolving in the field of finance. Discuss   [10]
CO-2 ;   its benefits and challenges with suitable examples.
SO-2 ;
BL-2   Answer: Evolution of Blockchain in Finance
Blockchain technology has significantly transformed the financial sector by
introducing decentralization, transparency, and automation.
a) Digital Payments and Cryptocurrencies
• Blockchain enables peer-to-peer transactions without intermediaries.
• Example: Bitcoin allows global payments with lower fees and faster
processing.
b) Smart Contracts and DeFi
•   Platforms like Ethereum enable Decentralized Finance (DeFi).
•   Services such as lending, borrowing, and trading are automated using
smart contracts.
c) Cross-Border Payments
•   Traditional international transfers are slow and expensive.
• Blockchain solutions reduce transaction time from days to minutes.
********** 9 **********
--- page 10 ---
d) Tokenization of Assets
• Real-world assets (stocks, real estate) are converted into digital
tokens.
• Enables fractional ownership and increased liquidity.
e) Clearing and Settlement
• Blockchain reduces settlement time in financial markets (T+2 → near
real-time).
•   Eliminates intermediaries like clearing houses.
2. Benefits of Blockchain in Finance
1. Transparency
o   All transactions are recorded on a shared ledger.
o Reduces fraud and increases trust.
2. Security
o Cryptographic techniques ensure data integrity and
protection.
3. Cost Reduction
o Removes intermediaries, lowering transaction and operational
costs.
4. Speed and Efficiency
o Faster transactions, especially in cross-border payments.
5. Financial Inclusion
o Provides access to financial services for unbanked
populations.
6. Automation
o Smart contracts automate processes, reducing human error.
3. Challenges of Blockchain in Finance
1. Regulatory Uncertainty
o Governments are still developing laws for blockchain and
cryptocurrencies.
2. Scalability Issues
o Networks may struggle with high transaction volumes.
3. Security Risks
o Smart contract bugs and cyberattacks can lead to losses.
4. High Implementation Cost
o   Initial setup and integration with existing systems can be
expensive.
5. Energy Consumption (Earlier Systems)
o Some blockchains (PoW-based) consume high energy.
6. Lack of Awareness and Adoption
o Limited understanding slows adoption in traditional finance.
Q6   a.   Differentiate between Public Blockchain and Private Blockchain. Discuss their [10]
CO-3 ;   suitability for financial applications.
SO-2 ;
BL-2   Answer:
Basis   Public Blockchain   Private Blockchain
Restricted to authorized
Open to anyone
Access   participants
(permissionless)
(permissioned)
********** 10 **********
--- page 11 ---
Controlled by a single
Fully decentralized (no
Control   organization or
single authority)
consortium
Limited – only selected
High – all transactions
Transparency   participants can view
are visible
data
Very high (due to large   High, but depends on
Security
distributed network)   internal controls
Slower (due to
Faster (fewer nodes and
Speed   consensus mechanisms
simplified consensus)
like PoW/PoS)
Higher transaction cost Lower cost (no mining
Cost
(fees, energy use)   required)
Hyperledger Fabric, R3
Examples   Bitcoin, Ethereum
Corda
Public blockchains are ideal for open, trustless financial ecosystems, while
private blockchains are more suitable for controlled, secure, and regulation-
compliant financial environments. In practice, many financial institutions
prefer private or hybrid models to balance efficiency, privacy, and control.
Q6   b.   Explain how decentralization, transparency, and immutability contribute to   [10]
CO-2 ;   the evolution of futures trading using blockchain technology.
SO-2 ;
BL-2   Answer: 1. Decentralization
Decentralization means that control is not held by a single authority (like an
exchange or clearing house). Instead, the blockchain network is maintained by
multiple nodes.
Impact on Futures Trading:
Eliminates intermediaries such as brokers and clearing houses
Reduces transaction costs and delays
Minimizes single points of failure and manipulation
Enables peer-to-peer futures contracts using Smart Contracts
2. Transparency
All transactions on a blockchain are recorded on a shared ledger and are
visible to participants (depending on the type of blockchain).
Impact on Futures Trading:
Improves trust among traders due to open access to transaction history
Reduces fraud and market manipulation
Enhances auditability and regulatory oversight
Provides real-time tracking of futures contracts and settlements
3. Immutability
Once data is recorded on the blockchain, it cannot be altered or deleted due to
cryptographic linking of blocks.
Impact on Futures Trading:
Ensures integrity of contract terms and transaction records
Prevents disputes and tampering with trade data
Provides a reliable and permanent audit trail
Strengthens trust in automated settlement systems
Q7   a. Compare different consensus mechanisms (PoW, PoS, BFT, PoA, PoET) based   [10]
on energy efficiency, security, and scalability.
********** 11 **********
--- page 12 ---
CO-3 ;
SO-2 ;   Answer:
BL-2   Consensus
Energy Efficiency   Security   Scalability
Mechanism
Very high (strong Low (slow
Very low (high
Proof of Work   against attacks   transaction speed,
energy consumption
(PoW)   like double   limited
due to mining)
spending)   throughput)
High (no heavy
Proof of Stake   High (depends on Medium to High
computation
(PoS)   stake distribution) (faster than PoW)
required)
Byzantine   Very high   Medium (works
High (minimal
Fault   (tolerates   well in smaller
computational
Tolerance   malicious nodes   networks, limited
work)
(BFT)   effectively)   scalability)
Proof of   Medium to High   High (fast
Very high (low
Authority   (depends on   transaction
resource usage)
(PoA)   trusted validators) processing)
Very high (efficient High (secure if   High (good
Proof of
use of waiting time trusted execution performance in
Elapsed Time
via trusted   environment is   permissioned
(PoET)
hardware)   reliable)   systems)
Q7   b. What is a blockchain platform? Explain Hyperledger Fabric and Corda in   [10]
CO-1 ;   detail.
SO-2 ;   Answer: A blockchain platform is a digital infrastructure that allows
BL-2   developers and organizations to build, run, and manage blockchain-based
applications such as smart contracts and decentralized systems.
It provides tools, protocols, and frameworks to create secure, transparent,
and distributed networks.
Hyperledger Fabric is an open-source, permissioned blockchain platform
developed under the Linux Foundation.
Key Features:
• Permissioned Network:
Only authorized participants can join and perform transactions.
• Modular Architecture:
Components like consensus and membership services can be
customized.
• No Native Cryptocurrency:
It is a tokenless blockchain, mainly used for enterprise applications.
• Smart Contracts (Chaincode):
Written in languages like Go, Java, or Node.js.
• Channels for Privacy:
Allows private communication between specific participants.
Working:
1. A transaction is proposed by a client.
2. Endorsing peers validate the transaction.
3. The ordering service orders transactions into blocks.
4. Blocks are distributed and validated across the network.
5. Ledger is updated.
********** 12 **********
--- page 13 ---
Use Cases:
• Supply chain management
• Banking and finance
•   Healthcare systems
3. Corda
Corda is a distributed ledger platform designed mainly for financial
institutions, developed by the R3.
Key Features:
• Permissioned Network:
Only trusted parties can participate.
• No Global Broadcast:
Transactions are shared only with relevant parties (privacy-focused).
• No Native Cryptocurrency:
Designed for real-world financial agreements rather than tokens.
• Smart Contracts:
Written in Java or Kotlin.
• Notary Service:
• Ensures transaction uniqueness and prevents double-spending.
Working:
1. Parties involved agree on a transaction.
2. Transaction is verified using smart contract rules.
3. Notary validates uniqueness.
4. Transaction is recorded only by relevant participants.
Use Cases:
• Banking and financial services
• Trade finance
• Insurance
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 819fbb879cc2

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ;   a.   Explain the limitations of traditional Distributed DBMS.   [5]
SO-2 ;
BL-1   Answer:
Limitation   Description
Design, deployment, and maintenance are
Complexity
difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Fault tolerance and transaction rollback are
Recovery
complex
Concurrency   Synchronizing access is difficult and error-prone
High due to software, hardware, and expertise
Cost
needs
CO-2 ;   b.   Differentiate between tokenized and tokenless blockchains with suitable   [5]
SO-2 ;   examples.
BL-2
Answer: A tokenized blockchain uses a native digital token (cryptocurrency)
to power the network, incentivize participants, and validate transactions.
A tokenless blockchain operates without any native cryptocurrency and
focuses mainly on data sharing and enterprise applications.
Presence of Cryptocurrency
Tokenized: Has its own cryptocurrency (e.g., Bitcoin, Ethereum).
Tokenless: No native cryptocurrency is used.
Incentive Mechanism
********** 1 **********
--- page 2 ---
Tokenized: Participants (miners/validators) are rewarded with
tokens for validating transactions.
Tokenless: No financial incentives; participants are usually
authorized entities working collaboratively.
Network Type
Tokenized: Mostly used in public or open blockchains.
Tokenless: Common in private or permissioned blockchains.
Use Cases
Tokenized:
Cryptocurrencies
Decentralized finance (DeFi)
Digital payments
Tokenless:
Supply chain management
Banking systems
Enterprise data sharing
CO-2 ;   c. What is contractual confidentiality in blockchain systems? Why is it   [5]
SO-2 ;   important?
BL-1
Answer: Contractual confidentiality refers to the ability to keep the details of
a contract (such as terms, conditions, and participant data) private and
accessible only to authorized parties, even when the contract is executed on a
blockchain network.
In blockchain systems—especially when using Smart Contracts—transactions
are typically transparent. However, not all business agreements can be
publicly visible. Contractual confidentiality ensures that sensitive information
is protected while still benefiting from blockchain features like security and
immutability.
Why is it Important?
1. Protection of Sensitive Data
2. Privacy in Transparent Systems
3. Regulatory Compliance
4. Secure Business Transactions
5. Trust Among Participants
CO-3 ;   d.   Explain the importance of Turing-Completeness with an appropriate   [5]
SO-2 ;   example.
BL-2
Answer: Turing-Completeness is a property of a computational system that
indicates it can perform any computation or solve any problem that a Turing
Machine can, provided sufficient time and memory.
Importance:
1. Flexibility in Programming:
A Turing-complete system can implement complex logic, algorithms, and
computations, making it highly versatile.
2. Smart Contract Capability:
In blockchain, Turing-completeness allows developers to write advanced
smart contracts with conditional logic, loops, and functions.
3. Automation of Complex Processes:
It enables automation of real-world agreements and workflows without
intermediaries.
********** 2 **********
--- page 3 ---
4. Wide Range of Applications:
Supports development of decentralized applications (dApps), games,
financial systems, and more.
Example:
Ethereum is a Turing-complete blockchain. Its smart contract language
(Solidity) allows developers to write complex programs—for example, a
decentralized lending system that automatically calculates interest, checks
conditions, and executes transactions based on predefined rules.
Attempt any 4
Q2   a. Draw and explain generic structure of Blockchain. Explain in details the   [10]
elements of Blockchain.
CO-1 ;
SO-2 ;
BL-2
Answer:
Address: Addresses are unique identifiers used in a blockchain transaction to
denote senders and recipients. An address is usually a public key or derived
from a public key. While addresses can be reused by the same user, addresses
themselves are unique. In practice, however, a single user may not use the
same address again and generate a new one for each transaction. This newly-
created address will be unique. A good practice is for users to generate a new
address for each transaction in order to avoid linking transactions to the
common owner, thus preventing identification.
Transaction: A transaction is the fundamental unit of a blockchain. A
transaction represents a transfer of value from one address to another. Block:
A block is composed of multiple transactions and other elements, such as the
previous block hash (hash pointer), timestamp, and nonce.
Peer-to-peer network: As the name implies, a peer-to-peer network is a
network topology wherein all peers can communicate with each other and
send and receive messages.
Scripting or programming language: Scripts or programs perform various
operations on a transaction in order to facilitate various functions. For
example, in Bitcoin, transaction scripts are predefined in a language called
Script, which consist of sets of commands that allow nodes to transfer tokens
from one address to another.
Bitcoins scripting language
Ethereum solidity language (Turing Complete)
Q2   b.   Explain the difference between Sybil attacks and Selfish Mining in   [10]
blockchain.
CO-3 ;
SO-2 ;
Answer:
BL-2
Basis   Sybil Attack   Selfish Mining
An attack where a single   A strategy where a miner or group
entity creates multiple fake   of miners withhold mined blocks to
Definition
identities (nodes) to gain   gain an unfair advantage and
control over the network.   increase their rewards.
To manipulate network
Main   operations like voting,   To maximize mining rewards by
Objective   consensus, or reputation   controlling the release of blocks.
systems.
********** 3 **********
--- page 4 ---
Creating numerous fake
Method   Keeping mined blocks private and
nodes to dominate the
Used   releasing them strategically.
network.
Can disrupt consensus,
Impact on   Leads to unfair reward distribution
reduce trust, and enable
Network   and reduces network efficiency.
double-spending.
Target Area Peer-to-peer network layer.   Mining and consensus mechanism.
An attacker flooding a
A miner in Bitcoin hiding blocks to
Example   blockchain network with fake
outperform honest miners.
nodes to influence decisions.
Q3   a. What are oracles in blockchain? Explain their types and their role in smart   [10]
contracts.
CO-3 ;
SO-2 ;
BL-2
Answer: Oracles are third-party services that act as a bridge between a
blockchain and the outside world. Since blockchains cannot directly access
external data (due to security and determinism constraints), oracles provide
real-world data to smart contracts and also send data from smart contracts
to external systems.
Types of Oracles
1. Software Oracles
• Provide data from online sources such as websites, APIs, and
databases.
• Examples: weather data, stock prices, sports results.
• Widely used in financial and prediction-based smart contracts.
2. Hardware Oracles
•   Collect data from physical devices and sensors.
• Examples: RFID sensors, temperature sensors, barcode scanners.
•   Useful in supply chain systems where physical events must be
recorded on blockchain.
3. Inbound Oracles
•   Bring external data into the blockchain.
• Example: Sending current market price of a commodity to a smart
contract for futures trading.
4. Outbound Oracles
• Send data from blockchain to the outside world.
• Example: A smart contract triggers a bank payment or sends a
notification after conditions are met.
Role of Oracles in Smart Contracts
• Data Feeding: Provide real-time and accurate external data required
for contract execution.
********** 4 **********
--- page 5 ---
• Automation: Enable smart contracts to execute automatically when
predefined real-world conditions are met.
•   Interoperability: Allow blockchain systems to interact with external
systems such as banking networks, IoT devices, and APIs.
• Use in Futures Systems: In blockchain-based futures trading, oracles
supply market prices, enabling automatic settlement of contracts.
Q3   b.   Explain the types of Ethereum accounts and the working mechanism of the   [10]
CO-2 ;   Ethereum blockchain.
SO-2 ;
BL-2   Answer: Types of Ethereum Accounts
In Ethereum, there are mainly two types of accounts:
a) Externally Owned Accounts (EOAs)
•   Controlled by users through private keys.
• Used to send and receive Ether and initiate transactions.
• Do not contain executable code.
• Example: A user wallet used for transferring ETH.
b) Contract Accounts
•   Controlled by smart contract code, not by private keys.
• Created when a smart contract is deployed on the blockchain.
•   Automatically execute predefined functions when triggered.
• Used in applications like DeFi, voting systems, etc
Working Mechanism of Ethereum Blockchain
The working of Ethereum involves several steps:
Step 1: Transaction Initiation
• A user (via EOA) creates a transaction (sending Ether or interacting
with a smart contract).
• The transaction is signed using the user’s private key.
Step 2: Transaction Broadcasting
• The transaction is broadcast to the Ethereum network and enters the
mempool (pending transactions).
Step 3: Validation by Nodes
• Nodes verify the transaction for correctness (valid signature,
sufficient balance, etc.).
Step 4: Block Creation
•   Validators/miners collect valid transactions and group them into a
block.
Step 5: Consensus Mechanism
• Ethereum uses Proof of Stake (PoS) (earlier Proof of Work).
•   Validators stake Ether and are chosen to validate and add new blocks.
********** 5 **********
--- page 6 ---
Step 6: Execution of Smart Contracts
•   If the transaction involves a contract, the code is executed on the
Ethereum Virtual Machine (EVM).
Step 7: Block Addition
• The validated block is added to the blockchain.
• The ledger is updated across all nodes.
Step 8: Transaction Confirmation
• The transaction becomes immutable and is confirmed after multiple
blocks are added.
Q4   a. What is Ethereum? Explain its key benefits and discuss the limitations of the   [10]
CO-3 ;   Ethereum platform.
SO-2 ;
BL-3   Answer: Ethereum is a decentralized, open-source blockchain platform that
enables developers to build and deploy smart contracts and decentralized
applications (dApps).
Unlike traditional blockchains that mainly support digital currency
transactions, Ethereum allows programmable logic through its Ethereum
Virtual Machine (EVM).
Key Benefits of Ethereum
1. Decentralization
o No central authority controls the network.
o Reduces risk of censorship and single point of failure.
2. Smart Contracts
o Self-executing contracts that run automatically when
conditions are met.
o Eliminates intermediaries and increases efficiency.
3. Transparency and Security
o   All transactions are recorded on a public ledger.
o Data is secure and tamper-resistant.
4. Programmability
o Developers can build a wide range of applications (DeFi, NFTs,
gaming, etc.).
5. Global Accessibility
o Anyone with internet access can participate in the network.
6. Tokenization
o Supports creation of custom tokens (ERC-20, NFTs), enabling
digital assets and fundraising.
Limitations of Ethereum
1. Scalability Issues
o Limited transactions per second (TPS), leading to network
congestion.
2. High Gas Fees
o Transaction costs can become very high during peak usage.
3. Complexity
o Development and usage require technical knowledge.
4. Security Risks in Smart Contracts
o Bugs in contract code can lead to financial losses.
********** 6 **********
--- page 7 ---
5. Energy Consumption (Earlier)
o Previously used Proof of Work, which consumed high energy
(now improved with Proof of Stake).
6. Network Congestion
o Heavy usage can slow down transaction processing.
Q4   b.   Explain 51% attacks in blockchain. Discuss real-world cases of 51% attacks   [10]
CO-1 ;   and explain possible mitigation strategies in detail.
SO-2 ;
BL-2   Answer: A 51% attack occurs when a single entity or group gains control of
more than 50% of a blockchain network’s mining or validation power.
This allows the attacker to manipulate the blockchain by:
•   Reversing transactions (double spending)
•   Preventing new transactions from being confirmed
•   Blocking or modifying transaction order
It mainly affects Proof of Work (PoW) blockchains.
Real-World Cases of 51% Attacks
a) Ethereum Classic (2019, 2020)
• Attacked multiple times.
• Hackers reorganized the blockchain and performed double-spending
attacks.
•   Millions of dollars worth of ETC were lost.
b) Bitcoin Gold (2018)
•   Attackers gained majority hash power.
• Double-spent coins worth over $18 million.
• Exchanges suffered significant losses.
c) Vertcoin (2018, 2019)
•   Suffered repeated 51% attacks.
•   Attackers reorganized blocks and executed double spending.
Mitigation Strategies
a) Increase Network Hash Power
• A larger and more decentralized network makes attacks expensive
and difficult.
b) Transition to Proof of Stake (PoS)
•   In PoS, attackers need to control a majority of staked coins, which is
costly.
• Example: Ethereum moved from PoW to PoS.
c) Confirmation Delays
• Exchanges can require more confirmations before accepting
transactions, reducing double-spending risk.
********** 7 **********
--- page 8 ---
d) Mining Pool Decentralization
• Avoid concentration of mining power in a few pools.
e) Checkpointing
• Hard-code checkpoints in the blockchain to prevent deep chain
reorganizations.
f) Hybrid Consensus Mechanisms
• Combine PoW with PoS or other methods to improve security.
g) Monitoring and Alerts
•   Detect unusual hash rate spikes or suspicious chain reorganizations.
Q5   a. What are the steps involved in blockchain development and deployment?   [10]
CO-3 ;   Explain in detail.
SO-2 ;
BL-2   Answer: 1. Problem Identification and Use Case Definition
•   Clearly define the problem you want to solve.
• Determine whether blockchain is actually needed (e.g., need for
decentralization, trust, transparency).
•   Identify the use case such as supply chain, finance, healthcare, etc.
2. Choosing the Right Blockchain Platform
•   Select an appropriate platform based on requirements:
o Ethereum – for smart contracts and dApps
o Hyperledger Fabric – for permissioned enterprise solutions
o Corda – for financial applications
3. Designing the Architecture
• Decide the type of blockchain: public, private, or consortium.
•   Define network structure, nodes, consensus mechanism, and data
flow.
• Plan security, scalability, and privacy requirements.
4. Smart Contract Development
• Write smart contracts (business logic) using appropriate languages
(e.g., Solidity).
•   Define rules, conditions, and workflows.
• Ensure proper coding practices to avoid vulnerabilities.
5. Frontend and Backend Development
• Develop user interface (UI) for interaction.
•   Build backend systems to connect blockchain with applications (APIs,
databases).
• Use tools like Web3.js or similar libraries.
********** 8 **********
--- page 9 ---
6. Testing
• Perform unit testing, integration testing, and system testing.
• Use test networks (testnets) to simulate real-world scenarios.
•   Identify and fix bugs or vulnerabilities.
7. Security Auditing
• Conduct thorough smart contract audits.
• Check for issues like reentrancy, overflow, and access control flaws.
• May involve third-party security audits.
8. Deployment
• Deploy smart contracts on the main network (mainnet).
•   Configure nodes and network settings.
• Ensure proper gas fees and deployment parameters.
9. Monitoring and Mainenance
• Continuously monitor performance and transactions.
•   Fix bugs, upgrade contracts (if possible), and optimize performance.
• Ensure network security and handle updates.
10. Scaling and Optimization
• Improve performance using Layer 2 solutions, sharding, or
sidechains.
• Optimize transaction speed and cost.
Q5   b.   Explain how blockchain technology is evolving in the field of finance. Discuss   [10]
CO-2 ;   its benefits and challenges with suitable examples.
SO-2 ;
BL-2   Answer: Evolution of Blockchain in Finance
Blockchain technology has significantly transformed the financial sector by
introducing decentralization, transparency, and automation.
a) Digital Payments and Cryptocurrencies
• Blockchain enables peer-to-peer transactions without intermediaries.
• Example: Bitcoin allows global payments with lower fees and faster
processing.
b) Smart Contracts and DeFi
•   Platforms like Ethereum enable Decentralized Finance (DeFi).
•   Services such as lending, borrowing, and trading are automated using
smart contracts.
c) Cross-Border Payments
•   Traditional international transfers are slow and expensive.
• Blockchain solutions reduce transaction time from days to minutes.
********** 9 **********
--- page 10 ---
d) Tokenization of Assets
• Real-world assets (stocks, real estate) are converted into digital
tokens.
• Enables fractional ownership and increased liquidity.
e) Clearing and Settlement
• Blockchain reduces settlement time in financial markets (T+2 → near
real-time).
•   Eliminates intermediaries like clearing houses.
2. Benefits of Blockchain in Finance
1. Transparency
o   All transactions are recorded on a shared ledger.
o Reduces fraud and increases trust.
2. Security
o Cryptographic techniques ensure data integrity and
protection.
3. Cost Reduction
o Removes intermediaries, lowering transaction and operational
costs.
4. Speed and Efficiency
o Faster transactions, especially in cross-border payments.
5. Financial Inclusion
o Provides access to financial services for unbanked
populations.
6. Automation
o Smart contracts automate processes, reducing human error.
3. Challenges of Blockchain in Finance
1. Regulatory Uncertainty
o Governments are still developing laws for blockchain and
cryptocurrencies.
2. Scalability Issues
o Networks may struggle with high transaction volumes.
3. Security Risks
o Smart contract bugs and cyberattacks can lead to losses.
4. High Implementation Cost
o   Initial setup and integration with existing systems can be
expensive.
5. Energy Consumption (Earlier Systems)
o Some blockchains (PoW-based) consume high energy.
6. Lack of Awareness and Adoption
o Limited understanding slows adoption in traditional finance.
Q6   a.   Differentiate between Public Blockchain and Private Blockchain. Discuss their [10]
CO-3 ;   suitability for financial applications.
SO-2 ;
BL-2   Answer:
Basis   Public Blockchain   Private Blockchain
Restricted to authorized
Open to anyone
Access   participants
(permissionless)
(permissioned)
********** 10 **********
--- page 11 ---
Controlled by a single
Fully decentralized (no
Control   organization or
single authority)
consortium
Limited – only selected
High – all transactions
Transparency   participants can view
are visible
data
Very high (due to large   High, but depends on
Security
distributed network)   internal controls
Slower (due to
Faster (fewer nodes and
Speed   consensus mechanisms
simplified consensus)
like PoW/PoS)
Higher transaction cost Lower cost (no mining
Cost
(fees, energy use)   required)
Hyperledger Fabric, R3
Examples   Bitcoin, Ethereum
Corda
Public blockchains are ideal for open, trustless financial ecosystems, while
private blockchains are more suitable for controlled, secure, and regulation-
compliant financial environments. In practice, many financial institutions
prefer private or hybrid models to balance efficiency, privacy, and control.
Q6   b.   Explain how decentralization, transparency, and immutability contribute to   [10]
CO-2 ;   the evolution of futures trading using blockchain technology.
SO-2 ;
BL-2   Answer: 1. Decentralization
Decentralization means that control is not held by a single authority (like an
exchange or clearing house). Instead, the blockchain network is maintained by
multiple nodes.
Impact on Futures Trading:
Eliminates intermediaries such as brokers and clearing houses
Reduces transaction costs and delays
Minimizes single points of failure and manipulation
Enables peer-to-peer futures contracts using Smart Contracts
2. Transparency
All transactions on a blockchain are recorded on a shared ledger and are
visible to participants (depending on the type of blockchain).
Impact on Futures Trading:
Improves trust among traders due to open access to transaction history
Reduces fraud and market manipulation
Enhances auditability and regulatory oversight
Provides real-time tracking of futures contracts and settlements
3. Immutability
Once data is recorded on the blockchain, it cannot be altered or deleted due to
cryptographic linking of blocks.
Impact on Futures Trading:
Ensures integrity of contract terms and transaction records
Prevents disputes and tampering with trade data
Provides a reliable and permanent audit trail
Strengthens trust in automated settlement systems
Q7   a. Compare different consensus mechanisms (PoW, PoS, BFT, PoA, PoET) based   [10]
on energy efficiency, security, and scalability.
********** 11 **********
--- page 12 ---
CO-3 ;
SO-2 ;   Answer:
BL-2   Consensus
Energy Efficiency   Security   Scalability
Mechanism
Very high (strong Low (slow
Very low (high
Proof of Work   against attacks   transaction speed,
energy consumption
(PoW)   like double   limited
due to mining)
spending)   throughput)
High (no heavy
Proof of Stake   High (depends on Medium to High
computation
(PoS)   stake distribution) (faster than PoW)
required)
Byzantine   Very high   Medium (works
High (minimal
Fault   (tolerates   well in smaller
computational
Tolerance   malicious nodes   networks, limited
work)
(BFT)   effectively)   scalability)
Proof of   Medium to High   High (fast
Very high (low
Authority   (depends on   transaction
resource usage)
(PoA)   trusted validators) processing)
Very high (efficient High (secure if   High (good
Proof of
use of waiting time trusted execution performance in
Elapsed Time
via trusted   environment is   permissioned
(PoET)
hardware)   reliable)   systems)
Q7   b. What is a blockchain platform? Explain Hyperledger Fabric and Corda in   [10]
CO-1 ;   detail.
SO-2 ;   Answer: A blockchain platform is a digital infrastructure that allows
BL-2   developers and organizations to build, run, and manage blockchain-based
applications such as smart contracts and decentralized systems.
It provides tools, protocols, and frameworks to create secure, transparent,
and distributed networks.
Hyperledger Fabric is an open-source, permissioned blockchain platform
developed under the Linux Foundation.
Key Features:
• Permissioned Network:
Only authorized participants can join and perform transactions.
• Modular Architecture:
Components like consensus and membership services can be
customized.
• No Native Cryptocurrency:
It is a tokenless blockchain, mainly used for enterprise applications.
• Smart Contracts (Chaincode):
Written in languages like Go, Java, or Node.js.
• Channels for Privacy:
Allows private communication between specific participants.
Working:
1. A transaction is proposed by a client.
2. Endorsing peers validate the transaction.
3. The ordering service orders transactions into blocks.
4. Blocks are distributed and validated across the network.
5. Ledger is updated.
********** 12 **********
--- page 13 ---
Use Cases:
• Supply chain management
• Banking and finance
•   Healthcare systems
3. Corda
Corda is a distributed ledger platform designed mainly for financial
institutions, developed by the R3.
Key Features:
• Permissioned Network:
Only trusted parties can participate.
• No Global Broadcast:
Transactions are shared only with relevant parties (privacy-focused).
• No Native Cryptocurrency:
Designed for real-world financial agreements rather than tokens.
• Smart Contracts:
Written in Java or Kotlin.
• Notary Service:
• Ensures transaction uniqueness and prevents double-spending.
Working:
1. Parties involved agree on a transaction.
2. Transaction is verified using smart contract rules.
3. Notary validates uniqueness.
4. Transaction is recorded only by relevant participants.
Use Cases:
• Banking and financial services
• Trade finance
• Insurance
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 59544c1fdc1f

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ;   a.   Explain the limitations of traditional Distributed DBMS.   [5]
SO-2 ;
BL-1   Answer:
Limitation   Description
Design, deployment, and maintenance are
Complexity
difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Fault tolerance and transaction rollback are
Recovery
complex
Concurrency   Synchronizing access is difficult and error-prone
High due to software, hardware, and expertise
Cost
needs
CO-2 ;   b.   Differentiate between tokenized and tokenless blockchains with suitable   [5]
SO-2 ;   examples.
BL-2
Answer: A tokenized blockchain uses a native digital token (cryptocurrency)
to power the network, incentivize participants, and validate transactions.
A tokenless blockchain operates without any native cryptocurrency and
focuses mainly on data sharing and enterprise applications.
Presence of Cryptocurrency
Tokenized: Has its own cryptocurrency (e.g., Bitcoin, Ethereum).
Tokenless: No native cryptocurrency is used.
Incentive Mechanism
********** 1 **********
--- page 2 ---
Tokenized: Participants (miners/validators) are rewarded with
tokens for validating transactions.
Tokenless: No financial incentives; participants are usually
authorized entities working collaboratively.
Network Type
Tokenized: Mostly used in public or open blockchains.
Tokenless: Common in private or permissioned blockchains.
Use Cases
Tokenized:
Cryptocurrencies
Decentralized finance (DeFi)
Digital payments
Tokenless:
Supply chain management
Banking systems
Enterprise data sharing
CO-2 ;   c. What is contractual confidentiality in blockchain systems? Why is it   [5]
SO-2 ;   important?
BL-1
Answer: Contractual confidentiality refers to the ability to keep the details of
a contract (such as terms, conditions, and participant data) private and
accessible only to authorized parties, even when the contract is executed on a
blockchain network.
In blockchain systems—especially when using Smart Contracts—transactions
are typically transparent. However, not all business agreements can be
publicly visible. Contractual confidentiality ensures that sensitive information
is protected while still benefiting from blockchain features like security and
immutability.
Why is it Important?
1. Protection of Sensitive Data
2. Privacy in Transparent Systems
3. Regulatory Compliance
4. Secure Business Transactions
5. Trust Among Participants
CO-3 ;   d.   Explain the importance of Turing-Completeness with an appropriate   [5]
SO-2 ;   example.
BL-2
Answer: Turing-Completeness is a property of a computational system that
indicates it can perform any computation or solve any problem that a Turing
Machine can, provided sufficient time and memory.
Importance:
1. Flexibility in Programming:
A Turing-complete system can implement complex logic, algorithms, and
computations, making it highly versatile.
2. Smart Contract Capability:
In blockchain, Turing-completeness allows developers to write advanced
smart contracts with conditional logic, loops, and functions.
3. Automation of Complex Processes:
It enables automation of real-world agreements and workflows without
intermediaries.
********** 2 **********
--- page 3 ---
4. Wide Range of Applications:
Supports development of decentralized applications (dApps), games,
financial systems, and more.
Example:
Ethereum is a Turing-complete blockchain. Its smart contract language
(Solidity) allows developers to write complex programs—for example, a
decentralized lending system that automatically calculates interest, checks
conditions, and executes transactions based on predefined rules.
Attempt any 4
Q2   a. Draw and explain generic structure of Blockchain. Explain in details the   [10]
elements of Blockchain.
CO-1 ;
SO-2 ;
BL-2
Answer:
Address: Addresses are unique identifiers used in a blockchain transaction to
denote senders and recipients. An address is usually a public key or derived
from a public key. While addresses can be reused by the same user, addresses
themselves are unique. In practice, however, a single user may not use the
same address again and generate a new one for each transaction. This newly-
created address will be unique. A good practice is for users to generate a new
address for each transaction in order to avoid linking transactions to the
common owner, thus preventing identification.
Transaction: A transaction is the fundamental unit of a blockchain. A
transaction represents a transfer of value from one address to another. Block:
A block is composed of multiple transactions and other elements, such as the
previous block hash (hash pointer), timestamp, and nonce.
Peer-to-peer network: As the name implies, a peer-to-peer network is a
network topology wherein all peers can communicate with each other and
send and receive messages.
Scripting or programming language: Scripts or programs perform various
operations on a transaction in order to facilitate various functions. For
example, in Bitcoin, transaction scripts are predefined in a language called
Script, which consist of sets of commands that allow nodes to transfer tokens
from one address to another.
Bitcoins scripting language
Ethereum solidity language (Turing Complete)
Q2   b.   Explain the difference between Sybil attacks and Selfish Mining in   [10]
blockchain.
CO-3 ;
SO-2 ;
Answer:
BL-2
Basis   Sybil Attack   Selfish Mining
An attack where a single   A strategy where a miner or group
entity creates multiple fake   of miners withhold mined blocks to
Definition
identities (nodes) to gain   gain an unfair advantage and
control over the network.   increase their rewards.
To manipulate network
Main   operations like voting,   To maximize mining rewards by
Objective   consensus, or reputation   controlling the release of blocks.
systems.
********** 3 **********
--- page 4 ---
Creating numerous fake
Method   Keeping mined blocks private and
nodes to dominate the
Used   releasing them strategically.
network.
Can disrupt consensus,
Impact on   Leads to unfair reward distribution
reduce trust, and enable
Network   and reduces network efficiency.
double-spending.
Target Area Peer-to-peer network layer.   Mining and consensus mechanism.
An attacker flooding a
A miner in Bitcoin hiding blocks to
Example   blockchain network with fake
outperform honest miners.
nodes to influence decisions.
Q3   a. What are oracles in blockchain? Explain their types and their role in smart   [10]
contracts.
CO-3 ;
SO-2 ;
BL-2
Answer: Oracles are third-party services that act as a bridge between a
blockchain and the outside world. Since blockchains cannot directly access
external data (due to security and determinism constraints), oracles provide
real-world data to smart contracts and also send data from smart contracts
to external systems.
Types of Oracles
1. Software Oracles
• Provide data from online sources such as websites, APIs, and
databases.
• Examples: weather data, stock prices, sports results.
• Widely used in financial and prediction-based smart contracts.
2. Hardware Oracles
•   Collect data from physical devices and sensors.
• Examples: RFID sensors, temperature sensors, barcode scanners.
•   Useful in supply chain systems where physical events must be
recorded on blockchain.
3. Inbound Oracles
•   Bring external data into the blockchain.
• Example: Sending current market price of a commodity to a smart
contract for futures trading.
4. Outbound Oracles
• Send data from blockchain to the outside world.
• Example: A smart contract triggers a bank payment or sends a
notification after conditions are met.
Role of Oracles in Smart Contracts
• Data Feeding: Provide real-time and accurate external data required
for contract execution.
********** 4 **********
--- page 5 ---
• Automation: Enable smart contracts to execute automatically when
predefined real-world conditions are met.
•   Interoperability: Allow blockchain systems to interact with external
systems such as banking networks, IoT devices, and APIs.
• Use in Futures Systems: In blockchain-based futures trading, oracles
supply market prices, enabling automatic settlement of contracts.
Q3   b.   Explain the types of Ethereum accounts and the working mechanism of the   [10]
CO-2 ;   Ethereum blockchain.
SO-2 ;
BL-2   Answer: Types of Ethereum Accounts
In Ethereum, there are mainly two types of accounts:
a) Externally Owned Accounts (EOAs)
•   Controlled by users through private keys.
• Used to send and receive Ether and initiate transactions.
• Do not contain executable code.
• Example: A user wallet used for transferring ETH.
b) Contract Accounts
•   Controlled by smart contract code, not by private keys.
• Created when a smart contract is deployed on the blockchain.
•   Automatically execute predefined functions when triggered.
• Used in applications like DeFi, voting systems, etc
Working Mechanism of Ethereum Blockchain
The working of Ethereum involves several steps:
Step 1: Transaction Initiation
• A user (via EOA) creates a transaction (sending Ether or interacting
with a smart contract).
• The transaction is signed using the user’s private key.
Step 2: Transaction Broadcasting
• The transaction is broadcast to the Ethereum network and enters the
mempool (pending transactions).
Step 3: Validation by Nodes
• Nodes verify the transaction for correctness (valid signature,
sufficient balance, etc.).
Step 4: Block Creation
•   Validators/miners collect valid transactions and group them into a
block.
Step 5: Consensus Mechanism
• Ethereum uses Proof of Stake (PoS) (earlier Proof of Work).
•   Validators stake Ether and are chosen to validate and add new blocks.
********** 5 **********
--- page 6 ---
Step 6: Execution of Smart Contracts
•   If the transaction involves a contract, the code is executed on the
Ethereum Virtual Machine (EVM).
Step 7: Block Addition
• The validated block is added to the blockchain.
• The ledger is updated across all nodes.
Step 8: Transaction Confirmation
• The transaction becomes immutable and is confirmed after multiple
blocks are added.
Q4   a. What is Ethereum? Explain its key benefits and discuss the limitations of the   [10]
CO-3 ;   Ethereum platform.
SO-2 ;
BL-3   Answer: Ethereum is a decentralized, open-source blockchain platform that
enables developers to build and deploy smart contracts and decentralized
applications (dApps).
Unlike traditional blockchains that mainly support digital currency
transactions, Ethereum allows programmable logic through its Ethereum
Virtual Machine (EVM).
Key Benefits of Ethereum
1. Decentralization
o No central authority controls the network.
o Reduces risk of censorship and single point of failure.
2. Smart Contracts
o Self-executing contracts that run automatically when
conditions are met.
o Eliminates intermediaries and increases efficiency.
3. Transparency and Security
o   All transactions are recorded on a public ledger.
o Data is secure and tamper-resistant.
4. Programmability
o Developers can build a wide range of applications (DeFi, NFTs,
gaming, etc.).
5. Global Accessibility
o Anyone with internet access can participate in the network.
6. Tokenization
o Supports creation of custom tokens (ERC-20, NFTs), enabling
digital assets and fundraising.
Limitations of Ethereum
1. Scalability Issues
o Limited transactions per second (TPS), leading to network
congestion.
2. High Gas Fees
o Transaction costs can become very high during peak usage.
3. Complexity
o Development and usage require technical knowledge.
4. Security Risks in Smart Contracts
o Bugs in contract code can lead to financial losses.
********** 6 **********
--- page 7 ---
5. Energy Consumption (Earlier)
o Previously used Proof of Work, which consumed high energy
(now improved with Proof of Stake).
6. Network Congestion
o Heavy usage can slow down transaction processing.
Q4   b.   Explain 51% attacks in blockchain. Discuss real-world cases of 51% attacks   [10]
CO-1 ;   and explain possible mitigation strategies in detail.
SO-2 ;
BL-2   Answer: A 51% attack occurs when a single entity or group gains control of
more than 50% of a blockchain network’s mining or validation power.
This allows the attacker to manipulate the blockchain by:
•   Reversing transactions (double spending)
•   Preventing new transactions from being confirmed
•   Blocking or modifying transaction order
It mainly affects Proof of Work (PoW) blockchains.
Real-World Cases of 51% Attacks
a) Ethereum Classic (2019, 2020)
• Attacked multiple times.
• Hackers reorganized the blockchain and performed double-spending
attacks.
•   Millions of dollars worth of ETC were lost.
b) Bitcoin Gold (2018)
•   Attackers gained majority hash power.
• Double-spent coins worth over $18 million.
• Exchanges suffered significant losses.
c) Vertcoin (2018, 2019)
•   Suffered repeated 51% attacks.
•   Attackers reorganized blocks and executed double spending.
Mitigation Strategies
a) Increase Network Hash Power
• A larger and more decentralized network makes attacks expensive
and difficult.
b) Transition to Proof of Stake (PoS)
•   In PoS, attackers need to control a majority of staked coins, which is
costly.
• Example: Ethereum moved from PoW to PoS.
c) Confirmation Delays
• Exchanges can require more confirmations before accepting
transactions, reducing double-spending risk.
********** 7 **********
--- page 8 ---
d) Mining Pool Decentralization
• Avoid concentration of mining power in a few pools.
e) Checkpointing
• Hard-code checkpoints in the blockchain to prevent deep chain
reorganizations.
f) Hybrid Consensus Mechanisms
• Combine PoW with PoS or other methods to improve security.
g) Monitoring and Alerts
•   Detect unusual hash rate spikes or suspicious chain reorganizations.
Q5   a. What are the steps involved in blockchain development and deployment?   [10]
CO-3 ;   Explain in detail.
SO-2 ;
BL-2   Answer: 1. Problem Identification and Use Case Definition
•   Clearly define the problem you want to solve.
• Determine whether blockchain is actually needed (e.g., need for
decentralization, trust, transparency).
•   Identify the use case such as supply chain, finance, healthcare, etc.
2. Choosing the Right Blockchain Platform
•   Select an appropriate platform based on requirements:
o Ethereum – for smart contracts and dApps
o Hyperledger Fabric – for permissioned enterprise solutions
o Corda – for financial applications
3. Designing the Architecture
• Decide the type of blockchain: public, private, or consortium.
•   Define network structure, nodes, consensus mechanism, and data
flow.
• Plan security, scalability, and privacy requirements.
4. Smart Contract Development
• Write smart contracts (business logic) using appropriate languages
(e.g., Solidity).
•   Define rules, conditions, and workflows.
• Ensure proper coding practices to avoid vulnerabilities.
5. Frontend and Backend Development
• Develop user interface (UI) for interaction.
•   Build backend systems to connect blockchain with applications (APIs,
databases).
• Use tools like Web3.js or similar libraries.
********** 8 **********
--- page 9 ---
6. Testing
• Perform unit testing, integration testing, and system testing.
• Use test networks (testnets) to simulate real-world scenarios.
•   Identify and fix bugs or vulnerabilities.
7. Security Auditing
• Conduct thorough smart contract audits.
• Check for issues like reentrancy, overflow, and access control flaws.
• May involve third-party security audits.
8. Deployment
• Deploy smart contracts on the main network (mainnet).
•   Configure nodes and network settings.
• Ensure proper gas fees and deployment parameters.
9. Monitoring and Mainenance
• Continuously monitor performance and transactions.
•   Fix bugs, upgrade contracts (if possible), and optimize performance.
• Ensure network security and handle updates.
10. Scaling and Optimization
• Improve performance using Layer 2 solutions, sharding, or
sidechains.
• Optimize transaction speed and cost.
Q5   b.   Explain how blockchain technology is evolving in the field of finance. Discuss   [10]
CO-2 ;   its benefits and challenges with suitable examples.
SO-2 ;
BL-2   Answer: Evolution of Blockchain in Finance
Blockchain technology has significantly transformed the financial sector by
introducing decentralization, transparency, and automation.
a) Digital Payments and Cryptocurrencies
• Blockchain enables peer-to-peer transactions without intermediaries.
• Example: Bitcoin allows global payments with lower fees and faster
processing.
b) Smart Contracts and DeFi
•   Platforms like Ethereum enable Decentralized Finance (DeFi).
•   Services such as lending, borrowing, and trading are automated using
smart contracts.
c) Cross-Border Payments
•   Traditional international transfers are slow and expensive.
• Blockchain solutions reduce transaction time from days to minutes.
********** 9 **********
--- page 10 ---
d) Tokenization of Assets
• Real-world assets (stocks, real estate) are converted into digital
tokens.
• Enables fractional ownership and increased liquidity.
e) Clearing and Settlement
• Blockchain reduces settlement time in financial markets (T+2 → near
real-time).
•   Eliminates intermediaries like clearing houses.
2. Benefits of Blockchain in Finance
1. Transparency
o   All transactions are recorded on a shared ledger.
o Reduces fraud and increases trust.
2. Security
o Cryptographic techniques ensure data integrity and
protection.
3. Cost Reduction
o Removes intermediaries, lowering transaction and operational
costs.
4. Speed and Efficiency
o Faster transactions, especially in cross-border payments.
5. Financial Inclusion
o Provides access to financial services for unbanked
populations.
6. Automation
o Smart contracts automate processes, reducing human error.
3. Challenges of Blockchain in Finance
1. Regulatory Uncertainty
o Governments are still developing laws for blockchain and
cryptocurrencies.
2. Scalability Issues
o Networks may struggle with high transaction volumes.
3. Security Risks
o Smart contract bugs and cyberattacks can lead to losses.
4. High Implementation Cost
o   Initial setup and integration with existing systems can be
expensive.
5. Energy Consumption (Earlier Systems)
o Some blockchains (PoW-based) consume high energy.
6. Lack of Awareness and Adoption
o Limited understanding slows adoption in traditional finance.
Q6   a.   Differentiate between Public Blockchain and Private Blockchain. Discuss their [10]
CO-3 ;   suitability for financial applications.
SO-2 ;
BL-2   Answer:
Basis   Public Blockchain   Private Blockchain
Restricted to authorized
Open to anyone
Access   participants
(permissionless)
(permissioned)
********** 10 **********
--- page 11 ---
Controlled by a single
Fully decentralized (no
Control   organization or
single authority)
consortium
Limited – only selected
High – all transactions
Transparency   participants can view
are visible
data
Very high (due to large   High, but depends on
Security
distributed network)   internal controls
Slower (due to
Faster (fewer nodes and
Speed   consensus mechanisms
simplified consensus)
like PoW/PoS)
Higher transaction cost Lower cost (no mining
Cost
(fees, energy use)   required)
Hyperledger Fabric, R3
Examples   Bitcoin, Ethereum
Corda
Public blockchains are ideal for open, trustless financial ecosystems, while
private blockchains are more suitable for controlled, secure, and regulation-
compliant financial environments. In practice, many financial institutions
prefer private or hybrid models to balance efficiency, privacy, and control.
Q6   b.   Explain how decentralization, transparency, and immutability contribute to   [10]
CO-2 ;   the evolution of futures trading using blockchain technology.
SO-2 ;
BL-2   Answer: 1. Decentralization
Decentralization means that control is not held by a single authority (like an
exchange or clearing house). Instead, the blockchain network is maintained by
multiple nodes.
Impact on Futures Trading:
Eliminates intermediaries such as brokers and clearing houses
Reduces transaction costs and delays
Minimizes single points of failure and manipulation
Enables peer-to-peer futures contracts using Smart Contracts
2. Transparency
All transactions on a blockchain are recorded on a shared ledger and are
visible to participants (depending on the type of blockchain).
Impact on Futures Trading:
Improves trust among traders due to open access to transaction history
Reduces fraud and market manipulation
Enhances auditability and regulatory oversight
Provides real-time tracking of futures contracts and settlements
3. Immutability
Once data is recorded on the blockchain, it cannot be altered or deleted due to
cryptographic linking of blocks.
Impact on Futures Trading:
Ensures integrity of contract terms and transaction records
Prevents disputes and tampering with trade data
Provides a reliable and permanent audit trail
Strengthens trust in automated settlement systems
Q7   a. Compare different consensus mechanisms (PoW, PoS, BFT, PoA, PoET) based   [10]
on energy efficiency, security, and scalability.
********** 11 **********
--- page 12 ---
CO-3 ;
SO-2 ;   Answer:
BL-2   Consensus
Energy Efficiency   Security   Scalability
Mechanism
Very high (strong Low (slow
Very low (high
Proof of Work   against attacks   transaction speed,
energy consumption
(PoW)   like double   limited
due to mining)
spending)   throughput)
High (no heavy
Proof of Stake   High (depends on Medium to High
computation
(PoS)   stake distribution) (faster than PoW)
required)
Byzantine   Very high   Medium (works
High (minimal
Fault   (tolerates   well in smaller
computational
Tolerance   malicious nodes   networks, limited
work)
(BFT)   effectively)   scalability)
Proof of   Medium to High   High (fast
Very high (low
Authority   (depends on   transaction
resource usage)
(PoA)   trusted validators) processing)
Very high (efficient High (secure if   High (good
Proof of
use of waiting time trusted execution performance in
Elapsed Time
via trusted   environment is   permissioned
(PoET)
hardware)   reliable)   systems)
Q7   b. What is a blockchain platform? Explain Hyperledger Fabric and Corda in   [10]
CO-1 ;   detail.
SO-2 ;   Answer: A blockchain platform is a digital infrastructure that allows
BL-2   developers and organizations to build, run, and manage blockchain-based
applications such as smart contracts and decentralized systems.
It provides tools, protocols, and frameworks to create secure, transparent,
and distributed networks.
Hyperledger Fabric is an open-source, permissioned blockchain platform
developed under the Linux Foundation.
Key Features:
• Permissioned Network:
Only authorized participants can join and perform transactions.
• Modular Architecture:
Components like consensus and membership services can be
customized.
• No Native Cryptocurrency:
It is a tokenless blockchain, mainly used for enterprise applications.
• Smart Contracts (Chaincode):
Written in languages like Go, Java, or Node.js.
• Channels for Privacy:
Allows private communication between specific participants.
Working:
1. A transaction is proposed by a client.
2. Endorsing peers validate the transaction.
3. The ordering service orders transactions into blocks.
4. Blocks are distributed and validated across the network.
5. Ledger is updated.
********** 12 **********
--- page 13 ---
Use Cases:
• Supply chain management
• Banking and finance
•   Healthcare systems
3. Corda
Corda is a distributed ledger platform designed mainly for financial
institutions, developed by the R3.
Key Features:
• Permissioned Network:
Only trusted parties can participate.
• No Global Broadcast:
Transactions are shared only with relevant parties (privacy-focused).
• No Native Cryptocurrency:
Designed for real-world financial agreements rather than tokens.
• Smart Contracts:
Written in Java or Kotlin.
• Notary Service:
• Ensures transaction uniqueness and prevents double-spending.
Working:
1. Parties involved agree on a transaction.
2. Transaction is verified using smart contract rules.
3. Notary validates uniqueness.
4. Transaction is recorded only by relevant participants.
Use Cases:
• Banking and financial services
• Trade finance
• Insurance
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 3bfef4766ed6

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIDS_7056/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Authority (PoA) and
Proof of Elapsed Time (PoET)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Authority (PoA)   Proof of Elapsed Time
(PoET)
1   Consensus mechanism where   Consensus mechanism
pre-approved validators   where trusted hardware
(authorities) are responsible   (such as Intel SGX) ensures
for creating new blocks.   that block creation is based
on random wait time.
2   Blocks are created by pre-   Blocks are created by any
CO-1 ;
selected, verified validators   node, but the node with the
SO-1,2 ;
(known identities).   shortest randomly assigned
BL-4
wait time creates the next
block.
3   Validators are known and   Validators can be
verified (reputation-based).   anonymous, as selection is
random and hardware-
based.
4   Trust is placed in the   Trust is placed in the
validators’ identity and   hardware and cryptographic
reputation.   proof of fairness (TEE like
Intel SGX).
5   Ethereum (private networks),   Hyperledger Sawtooth
VeChain, Binance Smart   (Intel).
Chain.
b.   Explain standard mechanics of how oracles work.
CO-2 ;
Solution:
SO-1,2 ;
The standard mechanics of how oracles work is presented here:
BL-2
1. A smart contract sends a request for data to an oracle.
********** 1 **********
--- page 2 ---
2. The request is executed, and the required data is requested from the
source. There are various methods of requesting data from the source.
These methods usually involve invoking APIs provided by the data
provider, calling a web service, reading from a database or requesting
data from another blockchain. Sources can be any external off-chain
data provider on the internet or in an internal enterprise network.
3. The data is sent to a notary to generate cryptographic proof (usually a
digital signature) of the requested data to prove its validity
(authenticity).
4. The data with the proof of validity is sent to the oracle.
5. The requested data with its proof of authenticity can be optionally
saved on a decentralized storage system, such as Swarm or IPFS, and
can be used by the smart contract/blockchain for verification. This is
especially useful when the proofs of authenticity are large and sending
them to the requesting smart contracts (storing them on the chain) is not
feasible.
6. Finally, the data, with the proof of validity, is sent to the smart contract.
c.   Explain the Turing-complete property of smart contracts.
Solution:
Turing-completeness in blockchain technology refers to the ability of a
blockchain’s smart contract platform to support complex computations
and logic, similar to how a general-purpose computer can execute any
algorithm. This capability significantly expands what can be achieved
CO-2 ;
on the blockchain beyond simple transactions.
SO-1,2 ;
Memory and Storage: The ability to store and manipulate data as
BL-2
needed for complex computations.
Conditional Statements: Support for conditional logic (e.g., if-else
statements) to make decisions based on various inputs.
Loops and Iteration: The capability to execute repetitive tasks or
loops, which are essential for many algorithms and processes.
d.   Why can’t we store large data directly on blockchains like Ethereum or
Bitcoin?
Solution:
1. Nodes Must Store Entire Blockchain Copy
• Blockchains rely on nodes (computers) to maintain the network.
•   Full nodes store the entire history of the blockchain for
verification and security.
•   If large files were stored on-chain, every node would need to
store those files, making it extremely heavy and impractical.
CO-3 ;
2. Immutable Nature → No Deletion
SO-1,2 ;
• Blockchain is immutable, meaning data cannot be deleted or
BL-3
changed.
• Once large files are added, they stay forever, causing unlimited
growth in storage requirements.
• Over time, this would make running a node impossible for most
users.
3. Large Files Slow Down the Network
• Blockchains are optimized for small transactions (like hashes
and smart contracts).
• Adding large files would:
********** 2 **********
--- page 3 ---
o Increase block size.
o Slow down transaction processing.
o Cause network congestion and higher fees.
4. Nodes Must Remain Lightweight for Decentralization
•   Decentralization works only if many people can run nodes.
•   If storage requirements become huge, only big companies could
afford to run nodes → centralization risk.
• Keeping nodes lightweight ensures accessibility and security.
a.   Illustrate the operation of proof of work (PoW) mechanism in validating
blockchain transactions and demonstrate it through an appropriate
example.
Solution:
PoW operation 6 marks and example 4 marks
▪   Operation: In PoW, “proof” is a solution to a computationally
difficult puzzle; “work” is expended computing that solution. Miners
compete to solve a cryptographic puzzle (find a nonce so that the
block’s hash meets a target). The first miner to solve it earns the right
to append the block and collect the mining reward/fees. Nodes then
verify the solution cheaply by hashing the block with the nonce. PoW
secures the network by making block reorganization or fraudulent
rewriting extremely costly.
▪ Steps :
▪   Puzzle: Miners compete to solve a mathematical puzzle. This
puzzle is difficult and requires a lot of computing power.
▪ Broadcast: The first miner to solve the puzzle shares the
solution with the network.
▪   Verification: Other nodes (computers) on the network check
Q2   if the solution is correct.
CO-2;   ▪ Block Added: If the solution is valid, the new block (which [10]
SO-1,2;   contains transactions) is added to the blockchain.
BL-3   ▪ Reward: The miner who solved the puzzle is rewarded,
typically with cryptocurrency (e.g., new Bitcoin).
▪ Working steps
▪ Example : Bitcoin solving SHA 256 hash lets a miner add the block
and gain coin rewards
********** 3 **********

[Text in pictures on this page, read by OCR]
|

Puzzle

Send Puzzle

xt

x2

Send Solutions

[BPI send award

Network server

Checks solutions

y=ton) = wrong
y=f(x2) © correct
y=£(x3) © wrong
--- page 4 ---
b.   What are the limitations of distributed database and how it is overcome
in blockchain?
Solution:
limitations of distributed database – 5 marks
how it is overcome in blockchain- 5 marks
A distributed database is a collection of interrelated data stored across
multiple computers (nodes) connected by a network.
It focuses on data availability, fault tolerance, and performance, but it
still relies on a central authority or administrator for control and
validation.
Admins or compromised nodes can modify or delete records without
detection. Users cannot independently verify data changes or history —
logs are maintained by the administrator. Central coordinator or master
CO-1;
node failure can affect the entire system’s availability or consistency.
SO-1,2;   [10]
Audit trails are not inherently built-in; need external logging
BL-3
mechanisms.
Blockchain-
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
This means that there is no central controller in the network, and all
participants talk to each other directly. consensus mechanisms (like
Proof of Work, Proof of Stake) ensure trust through decentralized
validation. Blockchain uses cryptographic hashing (each block
references the previous one). Any data change breaks the hash chain,
making tampering easily detectable. Blockchain provides transparency
— every transaction is visible to all participants and verifiable on a
shared ledger.
a.   Explain types of blockchain. Identify and justify the type of blockchain
that may be used for the given scenario: A company called AgriChain
Pvt. Ltd. wants to implement a system to track the journey of
Q3   agricultural products from farmers to supermarkets.
CO-1;   Solution:
[10]
SO-1,2;   Types of blockchain- 8 marks
BL-3   Public blockchains- As the name suggests, public blockchains are not
owned by anyone.
They are open to the public, and anyone can participate as a node in the
decision-making process.
********** 4 **********
--- page 5 ---
Users may or may not be rewarded for their participation.
All users of these permissionless or unpermissioned ledgers maintain a
copy of the ledger on their local nodes and use a distributed consensus
mechanism to decide the eventual state of the ledger.
Bitcoin and Ethereum are both considered public blockchains.
Private blockchain/ Consortium Blockchain - As the name implies,
private blockchains are just that—private.
That is, they are open only to a consortium or group of individuals or
organizations who have decided to share the ledger among themselves.
There are various blockchains now available in this category, such as
HydraChain and Quorum.
Optionally, both of these blockchains can also run in public mode if
required, but their primary purpose is to provide a private blockchain.
Semiprivate blockchains or Hybrid: With semiprivate blockchains, part
of the blockchain is private and part of it is public.
With a semi-private blockchain, the private part is controlled by a group
of individuals, while the public part is open for participation by anyone.
This hybrid model can be used in scenarios where the private part of the
blockchain remains internal and shared among known participants,
while the public part of the blockchain can still be used by anyone,
optionally allowing mining to secure the blockchain.
Multiple trusted entities share access
Scenario- Private or consortium with justification: Shared responsibility
among selected organizations like farmers, govt agencies and suppliers.
Public will not have access to this data.
b.   What is Contractual Confidentiality? Explain role of Smart contracts in
digitization of legal contracts with an example.
Solution:
What is Contractual Confidentiality- 5 marks
Explain role of Smart contracts in digitization of legal contracts with an
example- 5 marks
Contractual confidentiality is a fundamental obligation to protect parties
who disclose information, and smart contracts are transaction protocols
that automate agreements. Confidential smart contracts are a type of
smart contract that use cryptographic techniques to protect data and
execution logic on public blockchains.
CO-2;   Smart contracts are self-executing contracts, encoded on blockchain
SO-1,2;   platforms, automate and enforce contract terms without the need for   [10]
BL-3   intermediaries.
A smart contract is a secure and unstoppable computer program
representing an agreement that is automatically executable and
enforceable.
A smart contract is an electronic transaction protocol that executes the
terms of a contract. The general objectives are to satisfy common
contractual conditions (such as payment terms, liens, confidentiality,
and even enforcement), minimize exceptions both malicious and
accidental, and minimize the need for trusted intermediaries. Related
economic goals include lowering fraud loss, arbitrations and
enforcement costs, and other transaction costs.
a.   Explain the working and impact of Sybil attacks and Selfish mining
Q4   [10]
with suitable examples.
********** 5 **********
--- page 6 ---
CO-2;   Solution:
SO-1,2;   Explain sybil attack- 5 marks
BL-3   Explain selfish attack- 5 marks
•   Sybil attack- A Sybil attack is a type of network attack in which
an attacker creates and uses multiple fake identities, or “Sybil
nodes,” to gain an unfair advantage or perform malicious actions
within a network.
• This can be accomplished by creating multiple fake identities
and using them to gain a disproportionate level of influence
within the network, such as by participating in a consensus
process or voting system.
• The goal of a Sybil attack is to manipulate the network or disrupt
its normal operation, often for personal or financial gain.
•   If enough fake identities are created, this attack can be used to
outvote the honest nodes on the network.
•   If attackers manage to control more than 51% of the hash rate,
then they can reorder the transactions, censor transactions, and
effectively take over the entire network.
Selfish mining: This occurs when a miner withholds the blocks they
mine from the network in order to increase their chances of finding the
next block and earning the block reward.
• A selfish mining attack can occur when an attacker manages to
solve the PoW and mine a block but instead of announcing it to
the network, they withhold it from the public chain.
• This would create a fork, and the attacker can then keep mining
on the new forked chain, albeit only known to them, to build an
alternative chain and get ahead of the public blockchain.
• When this malicious chain is ahead of the honest public chain,
the latest block can be released to the network.
• As the network is programmed to accept the most recent block,
the malicious fork will overwrite the honest/original chain.
• This attack can result in achieving virtually any type of
malicious goal, including double-spending, stealing
cryptocurrency, censoring transactions, and similar goals.
b.   What is blockchain storage? Discuss its design, challenges, and
relevance in the context of Web3.
Solution:
CO-3;   What is blockchain storage?- 5 marks
SO-1,2;   Discuss its design, challenges, and relevance in the context of Web3- 5   [10]
BL-3   marks.
Blockchain storage refers to a decentralized method of storing data
where users retain true ownership, and data is distributed across a
network of nodes rather than being stored on a centralized server. Unlike
********** 6 **********
--- page 7 ---
traditional cloud services like Google Cloud or Dropbox, blockchain
storage eliminates the need for trust in a central authority, aligning with
Web3 principles of transparency, immutability, and decentralization.
Design of Blockchain Storage:
• Decentralized Architecture: Data is stored across multiple
nodes, ensuring no single point of failure.
• Content Addressing: Systems like IPFS use cryptographic
hashes (CIDs) to locate data based on content rather than location.
• Smart Contracts: Used to manage access and permissions.
• Off-chain Storage: Large files (e.g., videos, documents) are
stored off-chain, while blockchain stores metadata or hashes for
verification.
Challenges:
1. Scalability: Blockchains like Ethereum and Bitcoin are not
designed to store large files due to size and cost limitations.
2. Node Storage Limits: Full nodes must store the entire
blockchain, making it impractical to store extensive data directly
on-chain.
3. Immutability: Once data is added, it cannot be deleted, which can
lead to bloating.
4. Decentralization vs. Accessibility: Ensuring nodes remain
lightweight enough to maintain decentralization.
Relevance in Web3:
• Blockchain storage supports data sovereignty, allowing users to
control their own data.
•   It reduces reliance on centralized entities, enhancing privacy and
security.
Projects like IPFS, Filecoin, Arweave, Sia, Storj, and Crust Network
are pioneering decentralized storage solutions.
a.   Analyse the phases of the practical byzantine fault tolerance (PBFT)
algorithm and discuss how it mitigates the challenges of the Byzantine
Fault Problem.
Solution:
the phases with diagram 5 marks and mitigation challenges 5 marks
• Pre-prepare phase: The leader node sends out a pre-prepared
Q5
message to each backup node.
CO-2;
• Prepare: after receiving the pre-prepared message from the [10]
SO-1,2;
leader, the backup nodes send the prepared message as a reply to
BL-4
all other nodes including the leader. A node is considered prepared
only if it has received pre-prepared by the leader and seen (2f +
1) number of prepared messages from other nodes.
• Commit: If the nodes are prepared, they send a commit message.
If a node receives (f + 1) commit messages, they carry out the
client’s request.
********** 7 **********
--- page 8 ---
Mitigation of Byzantine challenges:
• Leader-based coordination provides an orderly proposal flow
while backups cross-check messages.
• Message quorums (2f+1, f+1 thresholds) ensure that even with
up to f malicious nodes, honest nodes reach consistent state and
cannot be permanently prevented from committing.
• Digital signatures & sequence numbers prevent message
tampering and replay; authenticity and ordering are enforced.
• Tolerates malicious behaviour as long as faulty nodes < 1/3 of
total, preventing conflicting decisions and ensuring safety and
liveness in presence of Byzantine faults.
• Trade-offs: PBFT is energy-efficient and fast for permissioned
networks but suffers from high communication overhead (O(n²)
messages), limiting scalability to modest node counts.
b.   Explain the role of oracles in bridging blockchain systems with real-
world data. Explain any two ues-cases of oracles in blockchain.
Solution:
Explain role of oracle- 4 marks
Two use-cases- 6 marks
Role of Oracle-
Blockchain systems are inherently deterministic and isolated. Smart
contracts execute exactly as coded but cannot access external
information (like market prices, sensor readings, or weather data) on
their own. This is where oracles come in:
CO-2;   • Data Provision: Feeds information like stock prices, commodity
SO-1,2;   [10]
rates, sensor readings, or identity verification data into smart
BL-3
contracts.
• Triggering Smart Contracts: Allows contracts to execute actions
automatically when specific conditions occur (e.g., paying insurance
claims after a weather event).
• Bridging Different Systems: Connects off-chain systems (like IoT
devices, APIs, or databases) with on-chain logic, enabling
blockchain to interact with the real world.
• Validation & Trust: Some oracles provide cryptographic proofs or
multi-source aggregation to ensure the accuracy and reliability of
external data.
********** 8 **********
--- page 9 ---
Example Use Cases of Oracles
1. Price Feeds (DeFi): Provide real-time cryptocurrency or fiat
currency prices. A DeFi lending protocol (like Aave or Compound) uses
a price oracle to get ETH/USD rates. To calculate collateral values and
prevent liquidation errors.
2. Weather Data (Insurance): Weather-based crop insurance for
farmers. A smart contract pays compensation automatically if rainfall is
below a certain level, based on data from a weather oracle. To bring off-
chain weather data (temperature, rainfall, etc.) onto the blockchain.
3. Sports/Prediction Markets: Fetch results of real-world events such
as football matches or elections. A prediction market uses oracles to
determine the outcome of a bet. To bring verified event results on-
chain.
a.   Differentiate between tokenized and tokenless blockchains. What role
does a shared ledger play in both models?
(10)
Solution:
Differentiate between tokenized and tokenless blockchains- 6 marks
Role of shared ledger- 4 marks
Tokenized Blockchains: A tokenized blockchain uses digital tokens as
the fundamental unit of value or incentive within the network. These
tokens may represent cryptocurrencies, digital assets, or utility tokens
that participants use for transactions, rewards, or governance. Tokenized
blockchains rely on economic incentives to secure the network and ensure
honesty in consensus mechanisms.
Key Features:
Operates on a public or permissionless network. Tokens are used to
reward miners or validators (e.g., Proof of Work or Proof of Stake). The
blockchain often supports smart contracts and decentralized applications
(DApps).
Role of Shared Ledger:
Q6   In tokenized blockchains, the shared ledger acts as a transparent and
CO-1;   immutable record of all token transactions, ownerships, and smart
[10]
SO-1,2;   contract executions. It ensures trustless verification — every participant
BL-4   can independently validate balances and transfers without intermediaries.
The ledger essentially serves as the backbone of the token economy.
2. Tokenless Blockchains: A tokenless blockchain does not involve any
native cryptocurrency or tradeable token. Instead, it focuses on data
integrity, transparency, and secure record-keeping among authorized
participants. Tokenless systems are typically permissioned or private,
managed by enterprises or consortiums where participants are already
known and trusted.
Key Features:
Operates on a private or consortium network. No need for mining or
staking; consensus is achieved through known nodes using algorithms
like Practical Byzantine Fault Tolerance (PBFT) or Raft. Focuses on
business process automation, data sharing, and auditability rather than
financial incentives.
Role of Shared Ledger:
In tokenless blockchains, the shared ledger serves as a trusted, tamper-
proof record of all transactions or data exchanges among participants. It
ensures that all authorized parties maintain a synchronized and verifiable
********** 9 **********
--- page 10 ---
view of shared information, enabling transparency, traceability, and
accountability without the need for tokens or financial rewards.
b.   Explain following elements of Ethereum Blockchain:
i.   Nodes
ii.   Ethereum network
iii.   Gas
iv.   Wallets
Solution: Explanation of each element – 2 marks *5=10 marks
• Node is any computer that participates in the Ethereum network
by running the Ethereum software (client). Each node maintains
a copy of the blockchain, verifies transactions, and helps
propagate data across the network.
Types of Ethereum Nodes
Full Node- Stores the entire blockchain and validates all
transactions and smart contracts independently.
Light Node- Stores only block headers (summaries) and relies on
full nodes for transaction data. Suitable for mobile or lightweight
devices.
CO-2;
• The Ethereum network is the global system of interconnected
SO-1,2;   [10]
nodes that collectively maintain the Ethereum blockchain. It is a
BL-3
peer-to-peer (P2P) network — meaning there is no central
server; every node communicates directly with others.
• Gas is required to be paid for every operation performed on the
Ethereum blockchain. This is a mechanism that ensures that
infinite loops cannot cause the whole blockchain to stall due to
the Turing-complete nature of the EVM. A transaction fee is
charged as an amount of Ether and is taken from the account
balance of the transaction originator. Gas is charged in three
scenarios as a prerequisite to the execution of an operation:
• The computation of an operation
• For contract creation or message calls
• An increase in the use of memory
• An Ethereum wallet is a software or hardware tool that stores
your cryptographic keys and allows you to send, receive, and
manage Ether (ETH) and interact with smart contracts.
a.   What is sharding? How does sharding mitigate the vulnerabilities of
different types of attacks.
Solution:
What is sharding- 4 marks
How does sharding mitigate the vulnerabilities of different types of
Q7   attacks- 6 marks
CO-3;
[10]
SO-1,2;   Sharding is a technique used to improve the scalability and performance
BL-3   of decentralized systems, particularly in blockchain networks.
It involves dividing the network into smaller parts called "shards," where
each shard processes only a subset of the overall network's transactions,
rather than having every node process every transaction.
This drastically reduces the computational burden and allows the system
to scale efficiently.
********** 10 **********
--- page 11 ---
In the context of consensus algorithms, sharding can also help in
preventing attacks, especially those that target the network's consensus
mechanism, such as Sybil attacks, 51% attacks, and Denial of Service
(DoS) attacks.
Below is an outline of how sharding-based consensus algorithms can
mitigate these types of attacks:
Sybil Attacks Prevention
In a Sybil attack, a malicious entity creates multiple fake identities
(nodes) to take control of a significant portion of the network.
Sharding prevents this by randomly assigning nodes to different shards.
Even if an attacker creates several fake identities, the probability of all
those identities ending up in the same shard is low. This fragmentation
makes it harder for the attacker to gain majority control in any shard.
51% Attack Mitigation
A 51% attack occurs when an entity gains control of the majority of the
network's mining or validation power, allowing it to rewrite the
blockchain and double-spend tokens.
Sharding mitigates this by spreading the network's computational or
validation power across multiple independent shards. An attacker would
have to control the majority in every shard simultaneously, which is far
more difficult and resource-intensive than controlling 51% of a single
network.
b.   Discuss any two applications of Blockchain technology in the government
sector. Explain and justify why the use of Blockchain is essential in these
applications.
Solution:
Each application with justification- 5 marks*2=10 marks.
Elections: Voting in any government is a key function and allows
citizens to participate in the democratic election process. Usually, the
limitations in current voting systems revolve around fraud, weaknesses
in operational processes, and especially transparency.
Blockchain-based voting systems can resolve these issues by
introducing end-to-end security and transparency into the process.
Security is provided in the form of the guaranteed integrity and
CO-3;
authenticity of votes by using public key cryptography, which comes as
SO-1,2;   [10]
standard in a blockchain. Moreover, the immutability guaranteed by a
BL-3
blockchain ensures that votes cast once cannot be cast again.
Border control: Automated border control systems have been in use for
decades now to thwart illegal entry into countries and prevent terrorism
and human trafficking.
Blockchain technology can provide a solution to this problem by
maintaining a blacklist in a smart contract that can be updated as
required. Any changes will be immediately visible to all agencies and
border control points, thus enabling immediate control over the
movement of a suspected travel document.
The full database of all travel documents may not be stored on the
blockchain currently due to inherent storage limitations, but a backend
distributed database such as BigchainDB, IPFS, or Swarm can be used
for that purpose.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e2ee5e2e54c7

- Departments: Computer Engineering, Data Science
- Programmes: BTech Computer 7002, BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7011/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Authority (PoA) and
Proof of Elapsed Time (PoET)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Authority (PoA)   Proof of Elapsed Time
(PoET)
1   Consensus mechanism where   Consensus mechanism
pre-approved validators   where trusted hardware
(authorities) are responsible   (such as Intel SGX) ensures
for creating new blocks.   that block creation is based
on random wait time.
2   Blocks are created by pre-   Blocks are created by any
CO-1 ;
selected, verified validators   node, but the node with the
SO-1,2 ;
(known identities).   shortest randomly assigned
BL-4
wait time creates the next
block.
3   Validators are known and   Validators can be
verified (reputation-based).   anonymous, as selection is
random and hardware-
based.
4   Trust is placed in the   Trust is placed in the
validators’ identity and   hardware and cryptographic
reputation.   proof of fairness (TEE like
Intel SGX).
5   Ethereum (private networks),   Hyperledger Sawtooth
VeChain, Binance Smart   (Intel).
Chain.
b.   Explain standard mechanics of how oracles work.
CO-2 ;
Solution:
SO-1,2 ;
The standard mechanics of how oracles work is presented here:
BL-2
1. A smart contract sends a request for data to an oracle.
********** 1 **********
--- page 2 ---
2. The request is executed, and the required data is requested from the
source. There are various methods of requesting data from the source.
These methods usually involve invoking APIs provided by the data
provider, calling a web service, reading from a database or requesting
data from another blockchain. Sources can be any external off-chain
data provider on the internet or in an internal enterprise network.
3. The data is sent to a notary to generate cryptographic proof (usually a
digital signature) of the requested data to prove its validity
(authenticity).
4. The data with the proof of validity is sent to the oracle.
5. The requested data with its proof of authenticity can be optionally
saved on a decentralized storage system, such as Swarm or IPFS, and
can be used by the smart contract/blockchain for verification. This is
especially useful when the proofs of authenticity are large and sending
them to the requesting smart contracts (storing them on the chain) is not
feasible.
6. Finally, the data, with the proof of validity, is sent to the smart contract.
c.   Explain the Turing-complete property of smart contracts.
Solution:
Turing-completeness in blockchain technology refers to the ability of a
blockchain’s smart contract platform to support complex computations
and logic, similar to how a general-purpose computer can execute any
algorithm. This capability significantly expands what can be achieved
CO-2 ;
on the blockchain beyond simple transactions.
SO-1,2 ;
Memory and Storage: The ability to store and manipulate data as
BL-2
needed for complex computations.
Conditional Statements: Support for conditional logic (e.g., if-else
statements) to make decisions based on various inputs.
Loops and Iteration: The capability to execute repetitive tasks or
loops, which are essential for many algorithms and processes.
d.   Why can’t we store large data directly on blockchains like Ethereum or
Bitcoin?
Solution:
1. Nodes Must Store Entire Blockchain Copy
• Blockchains rely on nodes (computers) to maintain the network.
•   Full nodes store the entire history of the blockchain for
verification and security.
•   If large files were stored on-chain, every node would need to
store those files, making it extremely heavy and impractical.
CO-3 ;
2. Immutable Nature → No Deletion
SO-1,2 ;
• Blockchain is immutable, meaning data cannot be deleted or
BL-3
changed.
• Once large files are added, they stay forever, causing unlimited
growth in storage requirements.
• Over time, this would make running a node impossible for most
users.
3. Large Files Slow Down the Network
• Blockchains are optimized for small transactions (like hashes
and smart contracts).
• Adding large files would:
********** 2 **********
--- page 3 ---
o Increase block size.
o Slow down transaction processing.
o Cause network congestion and higher fees.
4. Nodes Must Remain Lightweight for Decentralization
•   Decentralization works only if many people can run nodes.
•   If storage requirements become huge, only big companies could
afford to run nodes → centralization risk.
• Keeping nodes lightweight ensures accessibility and security.
a.   Illustrate the operation of proof of work (PoW) mechanism in validating
blockchain transactions and demonstrate it through an appropriate
example.
Solution:
PoW operation 6 marks and example 4 marks
▪   Operation: In PoW, “proof” is a solution to a computationally
difficult puzzle; “work” is expended computing that solution. Miners
compete to solve a cryptographic puzzle (find a nonce so that the
block’s hash meets a target). The first miner to solve it earns the right
to append the block and collect the mining reward/fees. Nodes then
verify the solution cheaply by hashing the block with the nonce. PoW
secures the network by making block reorganization or fraudulent
rewriting extremely costly.
▪ Steps :
▪   Puzzle: Miners compete to solve a mathematical puzzle. This
puzzle is difficult and requires a lot of computing power.
▪ Broadcast: The first miner to solve the puzzle shares the
solution with the network.
▪   Verification: Other nodes (computers) on the network check
Q2   if the solution is correct.
CO-2;   ▪ Block Added: If the solution is valid, the new block (which [10]
SO-1,2;   contains transactions) is added to the blockchain.
BL-3   ▪ Reward: The miner who solved the puzzle is rewarded,
typically with cryptocurrency (e.g., new Bitcoin).
▪ Working steps
▪ Example : Bitcoin solving SHA 256 hash lets a miner add the block
and gain coin rewards
********** 3 **********

[Text in pictures on this page, read by OCR]
|

Puzzle

Send Puzzle

xt

x2

Send Solutions

[BPI send award

Network server

Checks solutions

y=ton) = wrong
y=f(x2) © correct
y=£(x3) © wrong
--- page 4 ---
b.   What are the limitations of distributed database and how it is overcome
in blockchain?
Solution:
limitations of distributed database – 5 marks
how it is overcome in blockchain- 5 marks
A distributed database is a collection of interrelated data stored across
multiple computers (nodes) connected by a network.
It focuses on data availability, fault tolerance, and performance, but it
still relies on a central authority or administrator for control and
validation.
Admins or compromised nodes can modify or delete records without
detection. Users cannot independently verify data changes or history —
logs are maintained by the administrator. Central coordinator or master
CO-1;
node failure can affect the entire system’s availability or consistency.
SO-1,2;   [10]
Audit trails are not inherently built-in; need external logging
BL-3
mechanisms.
Blockchain-
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
This means that there is no central controller in the network, and all
participants talk to each other directly. consensus mechanisms (like
Proof of Work, Proof of Stake) ensure trust through decentralized
validation. Blockchain uses cryptographic hashing (each block
references the previous one). Any data change breaks the hash chain,
making tampering easily detectable. Blockchain provides transparency
— every transaction is visible to all participants and verifiable on a
shared ledger.
a.   Explain types of blockchain. Identify and justify the type of blockchain
that may be used for the given scenario: A company called AgriChain
Pvt. Ltd. wants to implement a system to track the journey of
Q3   agricultural products from farmers to supermarkets.
CO-1;   Solution:
[10]
SO-1,2;   Types of blockchain- 8 marks
BL-3   Public blockchains- As the name suggests, public blockchains are not
owned by anyone.
They are open to the public, and anyone can participate as a node in the
decision-making process.
********** 4 **********
--- page 5 ---
Users may or may not be rewarded for their participation.
All users of these permissionless or unpermissioned ledgers maintain a
copy of the ledger on their local nodes and use a distributed consensus
mechanism to decide the eventual state of the ledger.
Bitcoin and Ethereum are both considered public blockchains.
Private blockchain/ Consortium Blockchain - As the name implies,
private blockchains are just that—private.
That is, they are open only to a consortium or group of individuals or
organizations who have decided to share the ledger among themselves.
There are various blockchains now available in this category, such as
HydraChain and Quorum.
Optionally, both of these blockchains can also run in public mode if
required, but their primary purpose is to provide a private blockchain.
Semiprivate blockchains or Hybrid: With semiprivate blockchains, part
of the blockchain is private and part of it is public.
With a semi-private blockchain, the private part is controlled by a group
of individuals, while the public part is open for participation by anyone.
This hybrid model can be used in scenarios where the private part of the
blockchain remains internal and shared among known participants,
while the public part of the blockchain can still be used by anyone,
optionally allowing mining to secure the blockchain.
Multiple trusted entities share access
Scenario- Private or consortium with justification: Shared responsibility
among selected organizations like farmers, govt agencies and suppliers.
Public will not have access to this data.
b.   What is Contractual Confidentiality? Explain role of Smart contracts in
digitization of legal contracts with an example.
Solution:
What is Contractual Confidentiality- 5 marks
Explain role of Smart contracts in digitization of legal contracts with an
example- 5 marks
Contractual confidentiality is a fundamental obligation to protect parties
who disclose information, and smart contracts are transaction protocols
that automate agreements. Confidential smart contracts are a type of
smart contract that use cryptographic techniques to protect data and
execution logic on public blockchains.
CO-2;   Smart contracts are self-executing contracts, encoded on blockchain
SO-1,2;   platforms, automate and enforce contract terms without the need for   [10]
BL-3   intermediaries.
A smart contract is a secure and unstoppable computer program
representing an agreement that is automatically executable and
enforceable.
A smart contract is an electronic transaction protocol that executes the
terms of a contract. The general objectives are to satisfy common
contractual conditions (such as payment terms, liens, confidentiality,
and even enforcement), minimize exceptions both malicious and
accidental, and minimize the need for trusted intermediaries. Related
economic goals include lowering fraud loss, arbitrations and
enforcement costs, and other transaction costs.
a.   Explain the working and impact of Sybil attacks and Selfish mining
Q4   [10]
with suitable examples.
********** 5 **********
--- page 6 ---
CO-2;   Solution:
SO-1,2;   Explain sybil attack- 5 marks
BL-3   Explain selfish attack- 5 marks
•   Sybil attack- A Sybil attack is a type of network attack in which
an attacker creates and uses multiple fake identities, or “Sybil
nodes,” to gain an unfair advantage or perform malicious actions
within a network.
• This can be accomplished by creating multiple fake identities
and using them to gain a disproportionate level of influence
within the network, such as by participating in a consensus
process or voting system.
• The goal of a Sybil attack is to manipulate the network or disrupt
its normal operation, often for personal or financial gain.
•   If enough fake identities are created, this attack can be used to
outvote the honest nodes on the network.
•   If attackers manage to control more than 51% of the hash rate,
then they can reorder the transactions, censor transactions, and
effectively take over the entire network.
Selfish mining: This occurs when a miner withholds the blocks they
mine from the network in order to increase their chances of finding the
next block and earning the block reward.
• A selfish mining attack can occur when an attacker manages to
solve the PoW and mine a block but instead of announcing it to
the network, they withhold it from the public chain.
• This would create a fork, and the attacker can then keep mining
on the new forked chain, albeit only known to them, to build an
alternative chain and get ahead of the public blockchain.
• When this malicious chain is ahead of the honest public chain,
the latest block can be released to the network.
• As the network is programmed to accept the most recent block,
the malicious fork will overwrite the honest/original chain.
• This attack can result in achieving virtually any type of
malicious goal, including double-spending, stealing
cryptocurrency, censoring transactions, and similar goals.
b.   What is blockchain storage? Discuss its design, challenges, and
relevance in the context of Web3.
Solution:
CO-3;   What is blockchain storage?- 5 marks
SO-1,2;   Discuss its design, challenges, and relevance in the context of Web3- 5   [10]
BL-3   marks.
Blockchain storage refers to a decentralized method of storing data
where users retain true ownership, and data is distributed across a
network of nodes rather than being stored on a centralized server. Unlike
********** 6 **********
--- page 7 ---
traditional cloud services like Google Cloud or Dropbox, blockchain
storage eliminates the need for trust in a central authority, aligning with
Web3 principles of transparency, immutability, and decentralization.
Design of Blockchain Storage:
• Decentralized Architecture: Data is stored across multiple
nodes, ensuring no single point of failure.
• Content Addressing: Systems like IPFS use cryptographic
hashes (CIDs) to locate data based on content rather than location.
• Smart Contracts: Used to manage access and permissions.
• Off-chain Storage: Large files (e.g., videos, documents) are
stored off-chain, while blockchain stores metadata or hashes for
verification.
Challenges:
1. Scalability: Blockchains like Ethereum and Bitcoin are not
designed to store large files due to size and cost limitations.
2. Node Storage Limits: Full nodes must store the entire
blockchain, making it impractical to store extensive data directly
on-chain.
3. Immutability: Once data is added, it cannot be deleted, which can
lead to bloating.
4. Decentralization vs. Accessibility: Ensuring nodes remain
lightweight enough to maintain decentralization.
Relevance in Web3:
• Blockchain storage supports data sovereignty, allowing users to
control their own data.
•   It reduces reliance on centralized entities, enhancing privacy and
security.
Projects like IPFS, Filecoin, Arweave, Sia, Storj, and Crust Network
are pioneering decentralized storage solutions.
a.   Analyse the phases of the practical byzantine fault tolerance (PBFT)
algorithm and discuss how it mitigates the challenges of the Byzantine
Fault Problem.
Solution:
the phases with diagram 5 marks and mitigation challenges 5 marks
• Pre-prepare phase: The leader node sends out a pre-prepared
Q5
message to each backup node.
CO-2;
• Prepare: after receiving the pre-prepared message from the [10]
SO-1,2;
leader, the backup nodes send the prepared message as a reply to
BL-4
all other nodes including the leader. A node is considered prepared
only if it has received pre-prepared by the leader and seen (2f +
1) number of prepared messages from other nodes.
• Commit: If the nodes are prepared, they send a commit message.
If a node receives (f + 1) commit messages, they carry out the
client’s request.
********** 7 **********
--- page 8 ---
Mitigation of Byzantine challenges:
• Leader-based coordination provides an orderly proposal flow
while backups cross-check messages.
• Message quorums (2f+1, f+1 thresholds) ensure that even with
up to f malicious nodes, honest nodes reach consistent state and
cannot be permanently prevented from committing.
• Digital signatures & sequence numbers prevent message
tampering and replay; authenticity and ordering are enforced.
• Tolerates malicious behaviour as long as faulty nodes < 1/3 of
total, preventing conflicting decisions and ensuring safety and
liveness in presence of Byzantine faults.
• Trade-offs: PBFT is energy-efficient and fast for permissioned
networks but suffers from high communication overhead (O(n²)
messages), limiting scalability to modest node counts.
b.   Explain the role of oracles in bridging blockchain systems with real-
world data. Explain any two ues-cases of oracles in blockchain.
Solution:
Explain role of oracle- 4 marks
Two use-cases- 6 marks
Role of Oracle-
Blockchain systems are inherently deterministic and isolated. Smart
contracts execute exactly as coded but cannot access external
information (like market prices, sensor readings, or weather data) on
their own. This is where oracles come in:
CO-2;   • Data Provision: Feeds information like stock prices, commodity
SO-1,2;   [10]
rates, sensor readings, or identity verification data into smart
BL-3
contracts.
• Triggering Smart Contracts: Allows contracts to execute actions
automatically when specific conditions occur (e.g., paying insurance
claims after a weather event).
• Bridging Different Systems: Connects off-chain systems (like IoT
devices, APIs, or databases) with on-chain logic, enabling
blockchain to interact with the real world.
• Validation & Trust: Some oracles provide cryptographic proofs or
multi-source aggregation to ensure the accuracy and reliability of
external data.
********** 8 **********
--- page 9 ---
Example Use Cases of Oracles
1. Price Feeds (DeFi): Provide real-time cryptocurrency or fiat
currency prices. A DeFi lending protocol (like Aave or Compound) uses
a price oracle to get ETH/USD rates. To calculate collateral values and
prevent liquidation errors.
2. Weather Data (Insurance): Weather-based crop insurance for
farmers. A smart contract pays compensation automatically if rainfall is
below a certain level, based on data from a weather oracle. To bring off-
chain weather data (temperature, rainfall, etc.) onto the blockchain.
3. Sports/Prediction Markets: Fetch results of real-world events such
as football matches or elections. A prediction market uses oracles to
determine the outcome of a bet. To bring verified event results on-
chain.
a.   Differentiate between tokenized and tokenless blockchains. What role
does a shared ledger play in both models?
(10)
Solution:
Differentiate between tokenized and tokenless blockchains- 6 marks
Role of shared ledger- 4 marks
Tokenized Blockchains: A tokenized blockchain uses digital tokens as
the fundamental unit of value or incentive within the network. These
tokens may represent cryptocurrencies, digital assets, or utility tokens
that participants use for transactions, rewards, or governance. Tokenized
blockchains rely on economic incentives to secure the network and ensure
honesty in consensus mechanisms.
Key Features:
Operates on a public or permissionless network. Tokens are used to
reward miners or validators (e.g., Proof of Work or Proof of Stake). The
blockchain often supports smart contracts and decentralized applications
(DApps).
Role of Shared Ledger:
Q6   In tokenized blockchains, the shared ledger acts as a transparent and
CO-1;   immutable record of all token transactions, ownerships, and smart
[10]
SO-1,2;   contract executions. It ensures trustless verification — every participant
BL-4   can independently validate balances and transfers without intermediaries.
The ledger essentially serves as the backbone of the token economy.
2. Tokenless Blockchains: A tokenless blockchain does not involve any
native cryptocurrency or tradeable token. Instead, it focuses on data
integrity, transparency, and secure record-keeping among authorized
participants. Tokenless systems are typically permissioned or private,
managed by enterprises or consortiums where participants are already
known and trusted.
Key Features:
Operates on a private or consortium network. No need for mining or
staking; consensus is achieved through known nodes using algorithms
like Practical Byzantine Fault Tolerance (PBFT) or Raft. Focuses on
business process automation, data sharing, and auditability rather than
financial incentives.
Role of Shared Ledger:
In tokenless blockchains, the shared ledger serves as a trusted, tamper-
proof record of all transactions or data exchanges among participants. It
ensures that all authorized parties maintain a synchronized and verifiable
********** 9 **********
--- page 10 ---
view of shared information, enabling transparency, traceability, and
accountability without the need for tokens or financial rewards.
b.   Explain following elements of Ethereum Blockchain:
i.   Nodes
ii.   Ethereum network
iii.   Gas
iv.   Wallets
Solution: Explanation of each element – 2 marks *5=10 marks
• Node is any computer that participates in the Ethereum network
by running the Ethereum software (client). Each node maintains
a copy of the blockchain, verifies transactions, and helps
propagate data across the network.
Types of Ethereum Nodes
Full Node- Stores the entire blockchain and validates all
transactions and smart contracts independently.
Light Node- Stores only block headers (summaries) and relies on
full nodes for transaction data. Suitable for mobile or lightweight
devices.
CO-2;
• The Ethereum network is the global system of interconnected
SO-1,2;   [10]
nodes that collectively maintain the Ethereum blockchain. It is a
BL-3
peer-to-peer (P2P) network — meaning there is no central
server; every node communicates directly with others.
• Gas is required to be paid for every operation performed on the
Ethereum blockchain. This is a mechanism that ensures that
infinite loops cannot cause the whole blockchain to stall due to
the Turing-complete nature of the EVM. A transaction fee is
charged as an amount of Ether and is taken from the account
balance of the transaction originator. Gas is charged in three
scenarios as a prerequisite to the execution of an operation:
• The computation of an operation
• For contract creation or message calls
• An increase in the use of memory
• An Ethereum wallet is a software or hardware tool that stores
your cryptographic keys and allows you to send, receive, and
manage Ether (ETH) and interact with smart contracts.
a.   What is sharding? How does sharding mitigate the vulnerabilities of
different types of attacks.
Solution:
What is sharding- 4 marks
How does sharding mitigate the vulnerabilities of different types of
Q7   attacks- 6 marks
CO-3;
[10]
SO-1,2;   Sharding is a technique used to improve the scalability and performance
BL-3   of decentralized systems, particularly in blockchain networks.
It involves dividing the network into smaller parts called "shards," where
each shard processes only a subset of the overall network's transactions,
rather than having every node process every transaction.
This drastically reduces the computational burden and allows the system
to scale efficiently.
********** 10 **********
--- page 11 ---
In the context of consensus algorithms, sharding can also help in
preventing attacks, especially those that target the network's consensus
mechanism, such as Sybil attacks, 51% attacks, and Denial of Service
(DoS) attacks.
Below is an outline of how sharding-based consensus algorithms can
mitigate these types of attacks:
Sybil Attacks Prevention
In a Sybil attack, a malicious entity creates multiple fake identities
(nodes) to take control of a significant portion of the network.
Sharding prevents this by randomly assigning nodes to different shards.
Even if an attacker creates several fake identities, the probability of all
those identities ending up in the same shard is low. This fragmentation
makes it harder for the attacker to gain majority control in any shard.
51% Attack Mitigation
A 51% attack occurs when an entity gains control of the majority of the
network's mining or validation power, allowing it to rewrite the
blockchain and double-spend tokens.
Sharding mitigates this by spreading the network's computational or
validation power across multiple independent shards. An attacker would
have to control the majority in every shard simultaneously, which is far
more difficult and resource-intensive than controlling 51% of a single
network.
b.   Discuss any two applications of Blockchain technology in the government
sector. Explain and justify why the use of Blockchain is essential in these
applications.
Solution:
Each application with justification- 5 marks*2=10 marks.
Elections: Voting in any government is a key function and allows
citizens to participate in the democratic election process. Usually, the
limitations in current voting systems revolve around fraud, weaknesses
in operational processes, and especially transparency.
Blockchain-based voting systems can resolve these issues by
introducing end-to-end security and transparency into the process.
Security is provided in the form of the guaranteed integrity and
CO-3;
authenticity of votes by using public key cryptography, which comes as
SO-1,2;   [10]
standard in a blockchain. Moreover, the immutability guaranteed by a
BL-3
blockchain ensures that votes cast once cannot be cast again.
Border control: Automated border control systems have been in use for
decades now to thwart illegal entry into countries and prevent terrorism
and human trafficking.
Blockchain technology can provide a solution to this problem by
maintaining a blacklist in a smart contract that can be updated as
required. Any changes will be immediately visible to all agencies and
border control points, thus enabling immediate control over the
movement of a suspected travel document.
The full database of all travel documents may not be stored on the
blockchain currently due to inherent storage limitations, but a backend
distributed database such as BigchainDB, IPFS, or Swarm can be used
for that purpose.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper c9e830b61a8a

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Authority (PoA) and
Proof of Elapsed Time (PoET)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Authority (PoA)   Proof of Elapsed Time
(PoET)
1   Consensus mechanism where   Consensus mechanism
pre-approved validators   where trusted hardware
(authorities) are responsible   (such as Intel SGX) ensures
for creating new blocks.   that block creation is based
on random wait time.
2   Blocks are created by pre-   Blocks are created by any
CO-1 ;
selected, verified validators   node, but the node with the
SO-1,2 ;
(known identities).   shortest randomly assigned
BL-4
wait time creates the next
block.
3   Validators are known and   Validators can be
verified (reputation-based).   anonymous, as selection is
random and hardware-
based.
4   Trust is placed in the   Trust is placed in the
validators’ identity and   hardware and cryptographic
reputation.   proof of fairness (TEE like
Intel SGX).
5   Ethereum (private networks),   Hyperledger Sawtooth
VeChain, Binance Smart   (Intel).
Chain.
b.   Explain standard mechanics of how oracles work.
CO-2 ;
Solution:
SO-1,2 ;
The standard mechanics of how oracles work is presented here:
BL-2
1. A smart contract sends a request for data to an oracle.
********** 1 **********
--- page 2 ---
2. The request is executed, and the required data is requested from the
source. There are various methods of requesting data from the source.
These methods usually involve invoking APIs provided by the data
provider, calling a web service, reading from a database or requesting
data from another blockchain. Sources can be any external off-chain
data provider on the internet or in an internal enterprise network.
3. The data is sent to a notary to generate cryptographic proof (usually a
digital signature) of the requested data to prove its validity
(authenticity).
4. The data with the proof of validity is sent to the oracle.
5. The requested data with its proof of authenticity can be optionally
saved on a decentralized storage system, such as Swarm or IPFS, and
can be used by the smart contract/blockchain for verification. This is
especially useful when the proofs of authenticity are large and sending
them to the requesting smart contracts (storing them on the chain) is not
feasible.
6. Finally, the data, with the proof of validity, is sent to the smart contract.
c.   Explain the Turing-complete property of smart contracts.
Solution:
Turing-completeness in blockchain technology refers to the ability of a
blockchain’s smart contract platform to support complex computations
and logic, similar to how a general-purpose computer can execute any
algorithm. This capability significantly expands what can be achieved
CO-2 ;
on the blockchain beyond simple transactions.
SO-1,2 ;
Memory and Storage: The ability to store and manipulate data as
BL-2
needed for complex computations.
Conditional Statements: Support for conditional logic (e.g., if-else
statements) to make decisions based on various inputs.
Loops and Iteration: The capability to execute repetitive tasks or
loops, which are essential for many algorithms and processes.
d.   Why can’t we store large data directly on blockchains like Ethereum or
Bitcoin?
Solution:
1. Nodes Must Store Entire Blockchain Copy
• Blockchains rely on nodes (computers) to maintain the network.
•   Full nodes store the entire history of the blockchain for
verification and security.
•   If large files were stored on-chain, every node would need to
store those files, making it extremely heavy and impractical.
CO-3 ;
2. Immutable Nature → No Deletion
SO-1,2 ;
• Blockchain is immutable, meaning data cannot be deleted or
BL-3
changed.
• Once large files are added, they stay forever, causing unlimited
growth in storage requirements.
• Over time, this would make running a node impossible for most
users.
3. Large Files Slow Down the Network
• Blockchains are optimized for small transactions (like hashes
and smart contracts).
• Adding large files would:
********** 2 **********
--- page 3 ---
o Increase block size.
o Slow down transaction processing.
o Cause network congestion and higher fees.
4. Nodes Must Remain Lightweight for Decentralization
•   Decentralization works only if many people can run nodes.
•   If storage requirements become huge, only big companies could
afford to run nodes → centralization risk.
• Keeping nodes lightweight ensures accessibility and security.
a.   Illustrate the operation of proof of work (PoW) mechanism in validating
blockchain transactions and demonstrate it through an appropriate
example.
Solution:
PoW operation 6 marks and example 4 marks
▪   Operation: In PoW, “proof” is a solution to a computationally
difficult puzzle; “work” is expended computing that solution. Miners
compete to solve a cryptographic puzzle (find a nonce so that the
block’s hash meets a target). The first miner to solve it earns the right
to append the block and collect the mining reward/fees. Nodes then
verify the solution cheaply by hashing the block with the nonce. PoW
secures the network by making block reorganization or fraudulent
rewriting extremely costly.
▪ Steps :
▪   Puzzle: Miners compete to solve a mathematical puzzle. This
puzzle is difficult and requires a lot of computing power.
▪ Broadcast: The first miner to solve the puzzle shares the
solution with the network.
▪   Verification: Other nodes (computers) on the network check
Q2   if the solution is correct.
CO-2;   ▪ Block Added: If the solution is valid, the new block (which [10]
SO-1,2;   contains transactions) is added to the blockchain.
BL-3   ▪ Reward: The miner who solved the puzzle is rewarded,
typically with cryptocurrency (e.g., new Bitcoin).
▪ Working steps
▪ Example : Bitcoin solving SHA 256 hash lets a miner add the block
and gain coin rewards
********** 3 **********

[Text in pictures on this page, read by OCR]
|

Puzzle

Send Puzzle

xt

x2

Send Solutions

[BPI send award

Network server

Checks solutions

y=ton) = wrong
y=f(x2) © correct
y=£(x3) © wrong
--- page 4 ---
b.   What are the limitations of distributed database and how it is overcome
in blockchain?
Solution:
limitations of distributed database – 5 marks
how it is overcome in blockchain- 5 marks
A distributed database is a collection of interrelated data stored across
multiple computers (nodes) connected by a network.
It focuses on data availability, fault tolerance, and performance, but it
still relies on a central authority or administrator for control and
validation.
Admins or compromised nodes can modify or delete records without
detection. Users cannot independently verify data changes or history —
logs are maintained by the administrator. Central coordinator or master
CO-1;
node failure can affect the entire system’s availability or consistency.
SO-1,2;   [10]
Audit trails are not inherently built-in; need external logging
BL-3
mechanisms.
Blockchain-
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
This means that there is no central controller in the network, and all
participants talk to each other directly. consensus mechanisms (like
Proof of Work, Proof of Stake) ensure trust through decentralized
validation. Blockchain uses cryptographic hashing (each block
references the previous one). Any data change breaks the hash chain,
making tampering easily detectable. Blockchain provides transparency
— every transaction is visible to all participants and verifiable on a
shared ledger.
a.   Explain types of blockchain. Identify and justify the type of blockchain
that may be used for the given scenario: A company called AgriChain
Pvt. Ltd. wants to implement a system to track the journey of
Q3   agricultural products from farmers to supermarkets.
CO-1;   Solution:
[10]
SO-1,2;   Types of blockchain- 8 marks
BL-3   Public blockchains- As the name suggests, public blockchains are not
owned by anyone.
They are open to the public, and anyone can participate as a node in the
decision-making process.
********** 4 **********
--- page 5 ---
Users may or may not be rewarded for their participation.
All users of these permissionless or unpermissioned ledgers maintain a
copy of the ledger on their local nodes and use a distributed consensus
mechanism to decide the eventual state of the ledger.
Bitcoin and Ethereum are both considered public blockchains.
Private blockchain/ Consortium Blockchain - As the name implies,
private blockchains are just that—private.
That is, they are open only to a consortium or group of individuals or
organizations who have decided to share the ledger among themselves.
There are various blockchains now available in this category, such as
HydraChain and Quorum.
Optionally, both of these blockchains can also run in public mode if
required, but their primary purpose is to provide a private blockchain.
Semiprivate blockchains or Hybrid: With semiprivate blockchains, part
of the blockchain is private and part of it is public.
With a semi-private blockchain, the private part is controlled by a group
of individuals, while the public part is open for participation by anyone.
This hybrid model can be used in scenarios where the private part of the
blockchain remains internal and shared among known participants,
while the public part of the blockchain can still be used by anyone,
optionally allowing mining to secure the blockchain.
Multiple trusted entities share access
Scenario- Private or consortium with justification: Shared responsibility
among selected organizations like farmers, govt agencies and suppliers.
Public will not have access to this data.
b.   What is Contractual Confidentiality? Explain role of Smart contracts in
digitization of legal contracts with an example.
Solution:
What is Contractual Confidentiality- 5 marks
Explain role of Smart contracts in digitization of legal contracts with an
example- 5 marks
Contractual confidentiality is a fundamental obligation to protect parties
who disclose information, and smart contracts are transaction protocols
that automate agreements. Confidential smart contracts are a type of
smart contract that use cryptographic techniques to protect data and
execution logic on public blockchains.
CO-2;   Smart contracts are self-executing contracts, encoded on blockchain
SO-1,2;   platforms, automate and enforce contract terms without the need for   [10]
BL-3   intermediaries.
A smart contract is a secure and unstoppable computer program
representing an agreement that is automatically executable and
enforceable.
A smart contract is an electronic transaction protocol that executes the
terms of a contract. The general objectives are to satisfy common
contractual conditions (such as payment terms, liens, confidentiality,
and even enforcement), minimize exceptions both malicious and
accidental, and minimize the need for trusted intermediaries. Related
economic goals include lowering fraud loss, arbitrations and
enforcement costs, and other transaction costs.
a.   Explain the working and impact of Sybil attacks and Selfish mining
Q4   [10]
with suitable examples.
********** 5 **********
--- page 6 ---
CO-2;   Solution:
SO-1,2;   Explain sybil attack- 5 marks
BL-3   Explain selfish attack- 5 marks
•   Sybil attack- A Sybil attack is a type of network attack in which
an attacker creates and uses multiple fake identities, or “Sybil
nodes,” to gain an unfair advantage or perform malicious actions
within a network.
• This can be accomplished by creating multiple fake identities
and using them to gain a disproportionate level of influence
within the network, such as by participating in a consensus
process or voting system.
• The goal of a Sybil attack is to manipulate the network or disrupt
its normal operation, often for personal or financial gain.
•   If enough fake identities are created, this attack can be used to
outvote the honest nodes on the network.
•   If attackers manage to control more than 51% of the hash rate,
then they can reorder the transactions, censor transactions, and
effectively take over the entire network.
Selfish mining: This occurs when a miner withholds the blocks they
mine from the network in order to increase their chances of finding the
next block and earning the block reward.
• A selfish mining attack can occur when an attacker manages to
solve the PoW and mine a block but instead of announcing it to
the network, they withhold it from the public chain.
• This would create a fork, and the attacker can then keep mining
on the new forked chain, albeit only known to them, to build an
alternative chain and get ahead of the public blockchain.
• When this malicious chain is ahead of the honest public chain,
the latest block can be released to the network.
• As the network is programmed to accept the most recent block,
the malicious fork will overwrite the honest/original chain.
• This attack can result in achieving virtually any type of
malicious goal, including double-spending, stealing
cryptocurrency, censoring transactions, and similar goals.
b.   What is blockchain storage? Discuss its design, challenges, and
relevance in the context of Web3.
Solution:
CO-3;   What is blockchain storage?- 5 marks
SO-1,2;   Discuss its design, challenges, and relevance in the context of Web3- 5   [10]
BL-3   marks.
Blockchain storage refers to a decentralized method of storing data
where users retain true ownership, and data is distributed across a
network of nodes rather than being stored on a centralized server. Unlike
********** 6 **********
--- page 7 ---
traditional cloud services like Google Cloud or Dropbox, blockchain
storage eliminates the need for trust in a central authority, aligning with
Web3 principles of transparency, immutability, and decentralization.
Design of Blockchain Storage:
• Decentralized Architecture: Data is stored across multiple
nodes, ensuring no single point of failure.
• Content Addressing: Systems like IPFS use cryptographic
hashes (CIDs) to locate data based on content rather than location.
• Smart Contracts: Used to manage access and permissions.
• Off-chain Storage: Large files (e.g., videos, documents) are
stored off-chain, while blockchain stores metadata or hashes for
verification.
Challenges:
1. Scalability: Blockchains like Ethereum and Bitcoin are not
designed to store large files due to size and cost limitations.
2. Node Storage Limits: Full nodes must store the entire
blockchain, making it impractical to store extensive data directly
on-chain.
3. Immutability: Once data is added, it cannot be deleted, which can
lead to bloating.
4. Decentralization vs. Accessibility: Ensuring nodes remain
lightweight enough to maintain decentralization.
Relevance in Web3:
• Blockchain storage supports data sovereignty, allowing users to
control their own data.
•   It reduces reliance on centralized entities, enhancing privacy and
security.
Projects like IPFS, Filecoin, Arweave, Sia, Storj, and Crust Network
are pioneering decentralized storage solutions.
a.   Analyse the phases of the practical byzantine fault tolerance (PBFT)
algorithm and discuss how it mitigates the challenges of the Byzantine
Fault Problem.
Solution:
the phases with diagram 5 marks and mitigation challenges 5 marks
• Pre-prepare phase: The leader node sends out a pre-prepared
Q5
message to each backup node.
CO-2;
• Prepare: after receiving the pre-prepared message from the [10]
SO-1,2;
leader, the backup nodes send the prepared message as a reply to
BL-4
all other nodes including the leader. A node is considered prepared
only if it has received pre-prepared by the leader and seen (2f +
1) number of prepared messages from other nodes.
• Commit: If the nodes are prepared, they send a commit message.
If a node receives (f + 1) commit messages, they carry out the
client’s request.
********** 7 **********
--- page 8 ---
Mitigation of Byzantine challenges:
• Leader-based coordination provides an orderly proposal flow
while backups cross-check messages.
• Message quorums (2f+1, f+1 thresholds) ensure that even with
up to f malicious nodes, honest nodes reach consistent state and
cannot be permanently prevented from committing.
• Digital signatures & sequence numbers prevent message
tampering and replay; authenticity and ordering are enforced.
• Tolerates malicious behaviour as long as faulty nodes < 1/3 of
total, preventing conflicting decisions and ensuring safety and
liveness in presence of Byzantine faults.
• Trade-offs: PBFT is energy-efficient and fast for permissioned
networks but suffers from high communication overhead (O(n²)
messages), limiting scalability to modest node counts.
b.   Explain the role of oracles in bridging blockchain systems with real-
world data. Explain any two ues-cases of oracles in blockchain.
Solution:
Explain role of oracle- 4 marks
Two use-cases- 6 marks
Role of Oracle-
Blockchain systems are inherently deterministic and isolated. Smart
contracts execute exactly as coded but cannot access external
information (like market prices, sensor readings, or weather data) on
their own. This is where oracles come in:
CO-2;   • Data Provision: Feeds information like stock prices, commodity
SO-1,2;   [10]
rates, sensor readings, or identity verification data into smart
BL-3
contracts.
• Triggering Smart Contracts: Allows contracts to execute actions
automatically when specific conditions occur (e.g., paying insurance
claims after a weather event).
• Bridging Different Systems: Connects off-chain systems (like IoT
devices, APIs, or databases) with on-chain logic, enabling
blockchain to interact with the real world.
• Validation & Trust: Some oracles provide cryptographic proofs or
multi-source aggregation to ensure the accuracy and reliability of
external data.
********** 8 **********
--- page 9 ---
Example Use Cases of Oracles
1. Price Feeds (DeFi): Provide real-time cryptocurrency or fiat
currency prices. A DeFi lending protocol (like Aave or Compound) uses
a price oracle to get ETH/USD rates. To calculate collateral values and
prevent liquidation errors.
2. Weather Data (Insurance): Weather-based crop insurance for
farmers. A smart contract pays compensation automatically if rainfall is
below a certain level, based on data from a weather oracle. To bring off-
chain weather data (temperature, rainfall, etc.) onto the blockchain.
3. Sports/Prediction Markets: Fetch results of real-world events such
as football matches or elections. A prediction market uses oracles to
determine the outcome of a bet. To bring verified event results on-
chain.
a.   Differentiate between tokenized and tokenless blockchains. What role
does a shared ledger play in both models?
(10)
Solution:
Differentiate between tokenized and tokenless blockchains- 6 marks
Role of shared ledger- 4 marks
Tokenized Blockchains: A tokenized blockchain uses digital tokens as
the fundamental unit of value or incentive within the network. These
tokens may represent cryptocurrencies, digital assets, or utility tokens
that participants use for transactions, rewards, or governance. Tokenized
blockchains rely on economic incentives to secure the network and ensure
honesty in consensus mechanisms.
Key Features:
Operates on a public or permissionless network. Tokens are used to
reward miners or validators (e.g., Proof of Work or Proof of Stake). The
blockchain often supports smart contracts and decentralized applications
(DApps).
Role of Shared Ledger:
Q6   In tokenized blockchains, the shared ledger acts as a transparent and
CO-1;   immutable record of all token transactions, ownerships, and smart
[10]
SO-1,2;   contract executions. It ensures trustless verification — every participant
BL-4   can independently validate balances and transfers without intermediaries.
The ledger essentially serves as the backbone of the token economy.
2. Tokenless Blockchains: A tokenless blockchain does not involve any
native cryptocurrency or tradeable token. Instead, it focuses on data
integrity, transparency, and secure record-keeping among authorized
participants. Tokenless systems are typically permissioned or private,
managed by enterprises or consortiums where participants are already
known and trusted.
Key Features:
Operates on a private or consortium network. No need for mining or
staking; consensus is achieved through known nodes using algorithms
like Practical Byzantine Fault Tolerance (PBFT) or Raft. Focuses on
business process automation, data sharing, and auditability rather than
financial incentives.
Role of Shared Ledger:
In tokenless blockchains, the shared ledger serves as a trusted, tamper-
proof record of all transactions or data exchanges among participants. It
ensures that all authorized parties maintain a synchronized and verifiable
********** 9 **********
--- page 10 ---
view of shared information, enabling transparency, traceability, and
accountability without the need for tokens or financial rewards.
b.   Explain following elements of Ethereum Blockchain:
i.   Nodes
ii.   Ethereum network
iii.   Gas
iv.   Wallets
Solution: Explanation of each element – 2 marks *5=10 marks
• Node is any computer that participates in the Ethereum network
by running the Ethereum software (client). Each node maintains
a copy of the blockchain, verifies transactions, and helps
propagate data across the network.
Types of Ethereum Nodes
Full Node- Stores the entire blockchain and validates all
transactions and smart contracts independently.
Light Node- Stores only block headers (summaries) and relies on
full nodes for transaction data. Suitable for mobile or lightweight
devices.
CO-2;
• The Ethereum network is the global system of interconnected
SO-1,2;   [10]
nodes that collectively maintain the Ethereum blockchain. It is a
BL-3
peer-to-peer (P2P) network — meaning there is no central
server; every node communicates directly with others.
• Gas is required to be paid for every operation performed on the
Ethereum blockchain. This is a mechanism that ensures that
infinite loops cannot cause the whole blockchain to stall due to
the Turing-complete nature of the EVM. A transaction fee is
charged as an amount of Ether and is taken from the account
balance of the transaction originator. Gas is charged in three
scenarios as a prerequisite to the execution of an operation:
• The computation of an operation
• For contract creation or message calls
• An increase in the use of memory
• An Ethereum wallet is a software or hardware tool that stores
your cryptographic keys and allows you to send, receive, and
manage Ether (ETH) and interact with smart contracts.
a.   What is sharding? How does sharding mitigate the vulnerabilities of
different types of attacks.
Solution:
What is sharding- 4 marks
How does sharding mitigate the vulnerabilities of different types of
Q7   attacks- 6 marks
CO-3;
[10]
SO-1,2;   Sharding is a technique used to improve the scalability and performance
BL-3   of decentralized systems, particularly in blockchain networks.
It involves dividing the network into smaller parts called "shards," where
each shard processes only a subset of the overall network's transactions,
rather than having every node process every transaction.
This drastically reduces the computational burden and allows the system
to scale efficiently.
********** 10 **********
--- page 11 ---
In the context of consensus algorithms, sharding can also help in
preventing attacks, especially those that target the network's consensus
mechanism, such as Sybil attacks, 51% attacks, and Denial of Service
(DoS) attacks.
Below is an outline of how sharding-based consensus algorithms can
mitigate these types of attacks:
Sybil Attacks Prevention
In a Sybil attack, a malicious entity creates multiple fake identities
(nodes) to take control of a significant portion of the network.
Sharding prevents this by randomly assigning nodes to different shards.
Even if an attacker creates several fake identities, the probability of all
those identities ending up in the same shard is low. This fragmentation
makes it harder for the attacker to gain majority control in any shard.
51% Attack Mitigation
A 51% attack occurs when an entity gains control of the majority of the
network's mining or validation power, allowing it to rewrite the
blockchain and double-spend tokens.
Sharding mitigates this by spreading the network's computational or
validation power across multiple independent shards. An attacker would
have to control the majority in every shard simultaneously, which is far
more difficult and resource-intensive than controlling 51% of a single
network.
b.   Discuss any two applications of Blockchain technology in the government
sector. Explain and justify why the use of Blockchain is essential in these
applications.
Solution:
Each application with justification- 5 marks*2=10 marks.
Elections: Voting in any government is a key function and allows
citizens to participate in the democratic election process. Usually, the
limitations in current voting systems revolve around fraud, weaknesses
in operational processes, and especially transparency.
Blockchain-based voting systems can resolve these issues by
introducing end-to-end security and transparency into the process.
Security is provided in the form of the guaranteed integrity and
CO-3;
authenticity of votes by using public key cryptography, which comes as
SO-1,2;   [10]
standard in a blockchain. Moreover, the immutability guaranteed by a
BL-3
blockchain ensures that votes cast once cannot be cast again.
Border control: Automated border control systems have been in use for
decades now to thwart illegal entry into countries and prevent terrorism
and human trafficking.
Blockchain technology can provide a solution to this problem by
maintaining a blacklist in a smart contract that can be updated as
required. Any changes will be immediately visible to all agencies and
border control points, thus enabling immediate control over the
movement of a suspected travel document.
The full database of all travel documents may not be stored on the
blockchain currently due to inherent storage limitations, but a backend
distributed database such as BigchainDB, IPFS, or Swarm can be used
for that purpose.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper bbccd8064f98

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CS_7055/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Authority (PoA) and
Proof of Elapsed Time (PoET)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Authority (PoA)   Proof of Elapsed Time
(PoET)
1   Consensus mechanism where   Consensus mechanism
pre-approved validators   where trusted hardware
(authorities) are responsible   (such as Intel SGX) ensures
for creating new blocks.   that block creation is based
on random wait time.
2   Blocks are created by pre-   Blocks are created by any
CO-1 ;
selected, verified validators   node, but the node with the
SO-1,2 ;
(known identities).   shortest randomly assigned
BL-4
wait time creates the next
block.
3   Validators are known and   Validators can be
verified (reputation-based).   anonymous, as selection is
random and hardware-
based.
4   Trust is placed in the   Trust is placed in the
validators’ identity and   hardware and cryptographic
reputation.   proof of fairness (TEE like
Intel SGX).
5   Ethereum (private networks),   Hyperledger Sawtooth
VeChain, Binance Smart   (Intel).
Chain.
b.   Explain standard mechanics of how oracles work.
CO-2 ;
Solution:
SO-1,2 ;
The standard mechanics of how oracles work is presented here:
BL-2
1. A smart contract sends a request for data to an oracle.
********** 1 **********
--- page 2 ---
2. The request is executed, and the required data is requested from the
source. There are various methods of requesting data from the source.
These methods usually involve invoking APIs provided by the data
provider, calling a web service, reading from a database or requesting
data from another blockchain. Sources can be any external off-chain
data provider on the internet or in an internal enterprise network.
3. The data is sent to a notary to generate cryptographic proof (usually a
digital signature) of the requested data to prove its validity
(authenticity).
4. The data with the proof of validity is sent to the oracle.
5. The requested data with its proof of authenticity can be optionally
saved on a decentralized storage system, such as Swarm or IPFS, and
can be used by the smart contract/blockchain for verification. This is
especially useful when the proofs of authenticity are large and sending
them to the requesting smart contracts (storing them on the chain) is not
feasible.
6. Finally, the data, with the proof of validity, is sent to the smart contract.
c.   Explain the Turing-complete property of smart contracts.
Solution:
Turing-completeness in blockchain technology refers to the ability of a
blockchain’s smart contract platform to support complex computations
and logic, similar to how a general-purpose computer can execute any
algorithm. This capability significantly expands what can be achieved
CO-2 ;
on the blockchain beyond simple transactions.
SO-1,2 ;
Memory and Storage: The ability to store and manipulate data as
BL-2
needed for complex computations.
Conditional Statements: Support for conditional logic (e.g., if-else
statements) to make decisions based on various inputs.
Loops and Iteration: The capability to execute repetitive tasks or
loops, which are essential for many algorithms and processes.
d.   Why can’t we store large data directly on blockchains like Ethereum or
Bitcoin?
Solution:
1. Nodes Must Store Entire Blockchain Copy
• Blockchains rely on nodes (computers) to maintain the network.
•   Full nodes store the entire history of the blockchain for
verification and security.
•   If large files were stored on-chain, every node would need to
store those files, making it extremely heavy and impractical.
CO-3 ;
2. Immutable Nature → No Deletion
SO-1,2 ;
• Blockchain is immutable, meaning data cannot be deleted or
BL-3
changed.
• Once large files are added, they stay forever, causing unlimited
growth in storage requirements.
• Over time, this would make running a node impossible for most
users.
3. Large Files Slow Down the Network
• Blockchains are optimized for small transactions (like hashes
and smart contracts).
• Adding large files would:
********** 2 **********
--- page 3 ---
o Increase block size.
o Slow down transaction processing.
o Cause network congestion and higher fees.
4. Nodes Must Remain Lightweight for Decentralization
•   Decentralization works only if many people can run nodes.
•   If storage requirements become huge, only big companies could
afford to run nodes → centralization risk.
• Keeping nodes lightweight ensures accessibility and security.
a.   Illustrate the operation of proof of work (PoW) mechanism in validating
blockchain transactions and demonstrate it through an appropriate
example.
Solution:
PoW operation 6 marks and example 4 marks
▪   Operation: In PoW, “proof” is a solution to a computationally
difficult puzzle; “work” is expended computing that solution. Miners
compete to solve a cryptographic puzzle (find a nonce so that the
block’s hash meets a target). The first miner to solve it earns the right
to append the block and collect the mining reward/fees. Nodes then
verify the solution cheaply by hashing the block with the nonce. PoW
secures the network by making block reorganization or fraudulent
rewriting extremely costly.
▪ Steps :
▪   Puzzle: Miners compete to solve a mathematical puzzle. This
puzzle is difficult and requires a lot of computing power.
▪ Broadcast: The first miner to solve the puzzle shares the
solution with the network.
▪   Verification: Other nodes (computers) on the network check
Q2   if the solution is correct.
CO-2;   ▪ Block Added: If the solution is valid, the new block (which [10]
SO-1,2;   contains transactions) is added to the blockchain.
BL-3   ▪ Reward: The miner who solved the puzzle is rewarded,
typically with cryptocurrency (e.g., new Bitcoin).
▪ Working steps
▪ Example : Bitcoin solving SHA 256 hash lets a miner add the block
and gain coin rewards
********** 3 **********

[Text in pictures on this page, read by OCR]
|

Puzzle

Send Puzzle

xt

x2

Send Solutions

[BPI send award

Network server

Checks solutions

y=ton) = wrong
y=f(x2) © correct
y=£(x3) © wrong
--- page 4 ---
b.   What are the limitations of distributed database and how it is overcome
in blockchain?
Solution:
limitations of distributed database – 5 marks
how it is overcome in blockchain- 5 marks
A distributed database is a collection of interrelated data stored across
multiple computers (nodes) connected by a network.
It focuses on data availability, fault tolerance, and performance, but it
still relies on a central authority or administrator for control and
validation.
Admins or compromised nodes can modify or delete records without
detection. Users cannot independently verify data changes or history —
logs are maintained by the administrator. Central coordinator or master
CO-1;
node failure can affect the entire system’s availability or consistency.
SO-1,2;   [10]
Audit trails are not inherently built-in; need external logging
BL-3
mechanisms.
Blockchain-
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
This means that there is no central controller in the network, and all
participants talk to each other directly. consensus mechanisms (like
Proof of Work, Proof of Stake) ensure trust through decentralized
validation. Blockchain uses cryptographic hashing (each block
references the previous one). Any data change breaks the hash chain,
making tampering easily detectable. Blockchain provides transparency
— every transaction is visible to all participants and verifiable on a
shared ledger.
a.   Explain types of blockchain. Identify and justify the type of blockchain
that may be used for the given scenario: A company called AgriChain
Pvt. Ltd. wants to implement a system to track the journey of
Q3   agricultural products from farmers to supermarkets.
CO-1;   Solution:
[10]
SO-1,2;   Types of blockchain- 8 marks
BL-3   Public blockchains- As the name suggests, public blockchains are not
owned by anyone.
They are open to the public, and anyone can participate as a node in the
decision-making process.
********** 4 **********
--- page 5 ---
Users may or may not be rewarded for their participation.
All users of these permissionless or unpermissioned ledgers maintain a
copy of the ledger on their local nodes and use a distributed consensus
mechanism to decide the eventual state of the ledger.
Bitcoin and Ethereum are both considered public blockchains.
Private blockchain/ Consortium Blockchain - As the name implies,
private blockchains are just that—private.
That is, they are open only to a consortium or group of individuals or
organizations who have decided to share the ledger among themselves.
There are various blockchains now available in this category, such as
HydraChain and Quorum.
Optionally, both of these blockchains can also run in public mode if
required, but their primary purpose is to provide a private blockchain.
Semiprivate blockchains or Hybrid: With semiprivate blockchains, part
of the blockchain is private and part of it is public.
With a semi-private blockchain, the private part is controlled by a group
of individuals, while the public part is open for participation by anyone.
This hybrid model can be used in scenarios where the private part of the
blockchain remains internal and shared among known participants,
while the public part of the blockchain can still be used by anyone,
optionally allowing mining to secure the blockchain.
Multiple trusted entities share access
Scenario- Private or consortium with justification: Shared responsibility
among selected organizations like farmers, govt agencies and suppliers.
Public will not have access to this data.
b.   What is Contractual Confidentiality? Explain role of Smart contracts in
digitization of legal contracts with an example.
Solution:
What is Contractual Confidentiality- 5 marks
Explain role of Smart contracts in digitization of legal contracts with an
example- 5 marks
Contractual confidentiality is a fundamental obligation to protect parties
who disclose information, and smart contracts are transaction protocols
that automate agreements. Confidential smart contracts are a type of
smart contract that use cryptographic techniques to protect data and
execution logic on public blockchains.
CO-2;   Smart contracts are self-executing contracts, encoded on blockchain
SO-1,2;   platforms, automate and enforce contract terms without the need for   [10]
BL-3   intermediaries.
A smart contract is a secure and unstoppable computer program
representing an agreement that is automatically executable and
enforceable.
A smart contract is an electronic transaction protocol that executes the
terms of a contract. The general objectives are to satisfy common
contractual conditions (such as payment terms, liens, confidentiality,
and even enforcement), minimize exceptions both malicious and
accidental, and minimize the need for trusted intermediaries. Related
economic goals include lowering fraud loss, arbitrations and
enforcement costs, and other transaction costs.
a.   Explain the working and impact of Sybil attacks and Selfish mining
Q4   [10]
with suitable examples.
********** 5 **********
--- page 6 ---
CO-2;   Solution:
SO-1,2;   Explain sybil attack- 5 marks
BL-3   Explain selfish attack- 5 marks
•   Sybil attack- A Sybil attack is a type of network attack in which
an attacker creates and uses multiple fake identities, or “Sybil
nodes,” to gain an unfair advantage or perform malicious actions
within a network.
• This can be accomplished by creating multiple fake identities
and using them to gain a disproportionate level of influence
within the network, such as by participating in a consensus
process or voting system.
• The goal of a Sybil attack is to manipulate the network or disrupt
its normal operation, often for personal or financial gain.
•   If enough fake identities are created, this attack can be used to
outvote the honest nodes on the network.
•   If attackers manage to control more than 51% of the hash rate,
then they can reorder the transactions, censor transactions, and
effectively take over the entire network.
Selfish mining: This occurs when a miner withholds the blocks they
mine from the network in order to increase their chances of finding the
next block and earning the block reward.
• A selfish mining attack can occur when an attacker manages to
solve the PoW and mine a block but instead of announcing it to
the network, they withhold it from the public chain.
• This would create a fork, and the attacker can then keep mining
on the new forked chain, albeit only known to them, to build an
alternative chain and get ahead of the public blockchain.
• When this malicious chain is ahead of the honest public chain,
the latest block can be released to the network.
• As the network is programmed to accept the most recent block,
the malicious fork will overwrite the honest/original chain.
• This attack can result in achieving virtually any type of
malicious goal, including double-spending, stealing
cryptocurrency, censoring transactions, and similar goals.
b.   What is blockchain storage? Discuss its design, challenges, and
relevance in the context of Web3.
Solution:
CO-3;   What is blockchain storage?- 5 marks
SO-1,2;   Discuss its design, challenges, and relevance in the context of Web3- 5   [10]
BL-3   marks.
Blockchain storage refers to a decentralized method of storing data
where users retain true ownership, and data is distributed across a
network of nodes rather than being stored on a centralized server. Unlike
********** 6 **********
--- page 7 ---
traditional cloud services like Google Cloud or Dropbox, blockchain
storage eliminates the need for trust in a central authority, aligning with
Web3 principles of transparency, immutability, and decentralization.
Design of Blockchain Storage:
• Decentralized Architecture: Data is stored across multiple
nodes, ensuring no single point of failure.
• Content Addressing: Systems like IPFS use cryptographic
hashes (CIDs) to locate data based on content rather than location.
• Smart Contracts: Used to manage access and permissions.
• Off-chain Storage: Large files (e.g., videos, documents) are
stored off-chain, while blockchain stores metadata or hashes for
verification.
Challenges:
1. Scalability: Blockchains like Ethereum and Bitcoin are not
designed to store large files due to size and cost limitations.
2. Node Storage Limits: Full nodes must store the entire
blockchain, making it impractical to store extensive data directly
on-chain.
3. Immutability: Once data is added, it cannot be deleted, which can
lead to bloating.
4. Decentralization vs. Accessibility: Ensuring nodes remain
lightweight enough to maintain decentralization.
Relevance in Web3:
• Blockchain storage supports data sovereignty, allowing users to
control their own data.
•   It reduces reliance on centralized entities, enhancing privacy and
security.
Projects like IPFS, Filecoin, Arweave, Sia, Storj, and Crust Network
are pioneering decentralized storage solutions.
a.   Analyse the phases of the practical byzantine fault tolerance (PBFT)
algorithm and discuss how it mitigates the challenges of the Byzantine
Fault Problem.
Solution:
the phases with diagram 5 marks and mitigation challenges 5 marks
• Pre-prepare phase: The leader node sends out a pre-prepared
Q5
message to each backup node.
CO-2;
• Prepare: after receiving the pre-prepared message from the [10]
SO-1,2;
leader, the backup nodes send the prepared message as a reply to
BL-4
all other nodes including the leader. A node is considered prepared
only if it has received pre-prepared by the leader and seen (2f +
1) number of prepared messages from other nodes.
• Commit: If the nodes are prepared, they send a commit message.
If a node receives (f + 1) commit messages, they carry out the
client’s request.
********** 7 **********
--- page 8 ---
Mitigation of Byzantine challenges:
• Leader-based coordination provides an orderly proposal flow
while backups cross-check messages.
• Message quorums (2f+1, f+1 thresholds) ensure that even with
up to f malicious nodes, honest nodes reach consistent state and
cannot be permanently prevented from committing.
• Digital signatures & sequence numbers prevent message
tampering and replay; authenticity and ordering are enforced.
• Tolerates malicious behaviour as long as faulty nodes < 1/3 of
total, preventing conflicting decisions and ensuring safety and
liveness in presence of Byzantine faults.
• Trade-offs: PBFT is energy-efficient and fast for permissioned
networks but suffers from high communication overhead (O(n²)
messages), limiting scalability to modest node counts.
b.   Explain the role of oracles in bridging blockchain systems with real-
world data. Explain any two ues-cases of oracles in blockchain.
Solution:
Explain role of oracle- 4 marks
Two use-cases- 6 marks
Role of Oracle-
Blockchain systems are inherently deterministic and isolated. Smart
contracts execute exactly as coded but cannot access external
information (like market prices, sensor readings, or weather data) on
their own. This is where oracles come in:
CO-2;   • Data Provision: Feeds information like stock prices, commodity
SO-1,2;   [10]
rates, sensor readings, or identity verification data into smart
BL-3
contracts.
• Triggering Smart Contracts: Allows contracts to execute actions
automatically when specific conditions occur (e.g., paying insurance
claims after a weather event).
• Bridging Different Systems: Connects off-chain systems (like IoT
devices, APIs, or databases) with on-chain logic, enabling
blockchain to interact with the real world.
• Validation & Trust: Some oracles provide cryptographic proofs or
multi-source aggregation to ensure the accuracy and reliability of
external data.
********** 8 **********
--- page 9 ---
Example Use Cases of Oracles
1. Price Feeds (DeFi): Provide real-time cryptocurrency or fiat
currency prices. A DeFi lending protocol (like Aave or Compound) uses
a price oracle to get ETH/USD rates. To calculate collateral values and
prevent liquidation errors.
2. Weather Data (Insurance): Weather-based crop insurance for
farmers. A smart contract pays compensation automatically if rainfall is
below a certain level, based on data from a weather oracle. To bring off-
chain weather data (temperature, rainfall, etc.) onto the blockchain.
3. Sports/Prediction Markets: Fetch results of real-world events such
as football matches or elections. A prediction market uses oracles to
determine the outcome of a bet. To bring verified event results on-
chain.
a.   Differentiate between tokenized and tokenless blockchains. What role
does a shared ledger play in both models?
(10)
Solution:
Differentiate between tokenized and tokenless blockchains- 6 marks
Role of shared ledger- 4 marks
Tokenized Blockchains: A tokenized blockchain uses digital tokens as
the fundamental unit of value or incentive within the network. These
tokens may represent cryptocurrencies, digital assets, or utility tokens
that participants use for transactions, rewards, or governance. Tokenized
blockchains rely on economic incentives to secure the network and ensure
honesty in consensus mechanisms.
Key Features:
Operates on a public or permissionless network. Tokens are used to
reward miners or validators (e.g., Proof of Work or Proof of Stake). The
blockchain often supports smart contracts and decentralized applications
(DApps).
Role of Shared Ledger:
Q6   In tokenized blockchains, the shared ledger acts as a transparent and
CO-1;   immutable record of all token transactions, ownerships, and smart
[10]
SO-1,2;   contract executions. It ensures trustless verification — every participant
BL-4   can independently validate balances and transfers without intermediaries.
The ledger essentially serves as the backbone of the token economy.
2. Tokenless Blockchains: A tokenless blockchain does not involve any
native cryptocurrency or tradeable token. Instead, it focuses on data
integrity, transparency, and secure record-keeping among authorized
participants. Tokenless systems are typically permissioned or private,
managed by enterprises or consortiums where participants are already
known and trusted.
Key Features:
Operates on a private or consortium network. No need for mining or
staking; consensus is achieved through known nodes using algorithms
like Practical Byzantine Fault Tolerance (PBFT) or Raft. Focuses on
business process automation, data sharing, and auditability rather than
financial incentives.
Role of Shared Ledger:
In tokenless blockchains, the shared ledger serves as a trusted, tamper-
proof record of all transactions or data exchanges among participants. It
ensures that all authorized parties maintain a synchronized and verifiable
********** 9 **********
--- page 10 ---
view of shared information, enabling transparency, traceability, and
accountability without the need for tokens or financial rewards.
b.   Explain following elements of Ethereum Blockchain:
i.   Nodes
ii.   Ethereum network
iii.   Gas
iv.   Wallets
Solution: Explanation of each element – 2 marks *5=10 marks
• Node is any computer that participates in the Ethereum network
by running the Ethereum software (client). Each node maintains
a copy of the blockchain, verifies transactions, and helps
propagate data across the network.
Types of Ethereum Nodes
Full Node- Stores the entire blockchain and validates all
transactions and smart contracts independently.
Light Node- Stores only block headers (summaries) and relies on
full nodes for transaction data. Suitable for mobile or lightweight
devices.
CO-2;
• The Ethereum network is the global system of interconnected
SO-1,2;   [10]
nodes that collectively maintain the Ethereum blockchain. It is a
BL-3
peer-to-peer (P2P) network — meaning there is no central
server; every node communicates directly with others.
• Gas is required to be paid for every operation performed on the
Ethereum blockchain. This is a mechanism that ensures that
infinite loops cannot cause the whole blockchain to stall due to
the Turing-complete nature of the EVM. A transaction fee is
charged as an amount of Ether and is taken from the account
balance of the transaction originator. Gas is charged in three
scenarios as a prerequisite to the execution of an operation:
• The computation of an operation
• For contract creation or message calls
• An increase in the use of memory
• An Ethereum wallet is a software or hardware tool that stores
your cryptographic keys and allows you to send, receive, and
manage Ether (ETH) and interact with smart contracts.
a.   What is sharding? How does sharding mitigate the vulnerabilities of
different types of attacks.
Solution:
What is sharding- 4 marks
How does sharding mitigate the vulnerabilities of different types of
Q7   attacks- 6 marks
CO-3;
[10]
SO-1,2;   Sharding is a technique used to improve the scalability and performance
BL-3   of decentralized systems, particularly in blockchain networks.
It involves dividing the network into smaller parts called "shards," where
each shard processes only a subset of the overall network's transactions,
rather than having every node process every transaction.
This drastically reduces the computational burden and allows the system
to scale efficiently.
********** 10 **********
--- page 11 ---
In the context of consensus algorithms, sharding can also help in
preventing attacks, especially those that target the network's consensus
mechanism, such as Sybil attacks, 51% attacks, and Denial of Service
(DoS) attacks.
Below is an outline of how sharding-based consensus algorithms can
mitigate these types of attacks:
Sybil Attacks Prevention
In a Sybil attack, a malicious entity creates multiple fake identities
(nodes) to take control of a significant portion of the network.
Sharding prevents this by randomly assigning nodes to different shards.
Even if an attacker creates several fake identities, the probability of all
those identities ending up in the same shard is low. This fragmentation
makes it harder for the attacker to gain majority control in any shard.
51% Attack Mitigation
A 51% attack occurs when an entity gains control of the majority of the
network's mining or validation power, allowing it to rewrite the
blockchain and double-spend tokens.
Sharding mitigates this by spreading the network's computational or
validation power across multiple independent shards. An attacker would
have to control the majority in every shard simultaneously, which is far
more difficult and resource-intensive than controlling 51% of a single
network.
b.   Discuss any two applications of Blockchain technology in the government
sector. Explain and justify why the use of Blockchain is essential in these
applications.
Solution:
Each application with justification- 5 marks*2=10 marks.
Elections: Voting in any government is a key function and allows
citizens to participate in the democratic election process. Usually, the
limitations in current voting systems revolve around fraud, weaknesses
in operational processes, and especially transparency.
Blockchain-based voting systems can resolve these issues by
introducing end-to-end security and transparency into the process.
Security is provided in the form of the guaranteed integrity and
CO-3;
authenticity of votes by using public key cryptography, which comes as
SO-1,2;   [10]
standard in a blockchain. Moreover, the immutability guaranteed by a
BL-3
blockchain ensures that votes cast once cannot be cast again.
Border control: Automated border control systems have been in use for
decades now to thwart illegal entry into countries and prevent terrorism
and human trafficking.
Blockchain technology can provide a solution to this problem by
maintaining a blacklist in a smart contract that can be updated as
required. Any changes will be immediately visible to all agencies and
border control points, thus enabling immediate control over the
movement of a suspected travel document.
The full database of all travel documents may not be stored on the
blockchain currently due to inherent storage limitations, but a backend
distributed database such as BigchainDB, IPFS, or Swarm can be used
for that purpose.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 49aaa4dcd575

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech_Computer_7047/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Authority (PoA) and
Proof of Elapsed Time (PoET)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Authority (PoA)   Proof of Elapsed Time
(PoET)
1   Consensus mechanism where   Consensus mechanism
pre-approved validators   where trusted hardware
(authorities) are responsible   (such as Intel SGX) ensures
for creating new blocks.   that block creation is based
on random wait time.
2   Blocks are created by pre-   Blocks are created by any
CO-1 ;
selected, verified validators   node, but the node with the
SO-1,2 ;
(known identities).   shortest randomly assigned
BL-4
wait time creates the next
block.
3   Validators are known and   Validators can be
verified (reputation-based).   anonymous, as selection is
random and hardware-
based.
4   Trust is placed in the   Trust is placed in the
validators’ identity and   hardware and cryptographic
reputation.   proof of fairness (TEE like
Intel SGX).
5   Ethereum (private networks),   Hyperledger Sawtooth
VeChain, Binance Smart   (Intel).
Chain.
b.   Explain standard mechanics of how oracles work.
CO-2 ;
Solution:
SO-1,2 ;
The standard mechanics of how oracles work is presented here:
BL-2
1. A smart contract sends a request for data to an oracle.
********** 1 **********
--- page 2 ---
2. The request is executed, and the required data is requested from the
source. There are various methods of requesting data from the source.
These methods usually involve invoking APIs provided by the data
provider, calling a web service, reading from a database or requesting
data from another blockchain. Sources can be any external off-chain
data provider on the internet or in an internal enterprise network.
3. The data is sent to a notary to generate cryptographic proof (usually a
digital signature) of the requested data to prove its validity
(authenticity).
4. The data with the proof of validity is sent to the oracle.
5. The requested data with its proof of authenticity can be optionally
saved on a decentralized storage system, such as Swarm or IPFS, and
can be used by the smart contract/blockchain for verification. This is
especially useful when the proofs of authenticity are large and sending
them to the requesting smart contracts (storing them on the chain) is not
feasible.
6. Finally, the data, with the proof of validity, is sent to the smart contract.
c.   Explain the Turing-complete property of smart contracts.
Solution:
Turing-completeness in blockchain technology refers to the ability of a
blockchain’s smart contract platform to support complex computations
and logic, similar to how a general-purpose computer can execute any
algorithm. This capability significantly expands what can be achieved
CO-2 ;
on the blockchain beyond simple transactions.
SO-1,2 ;
Memory and Storage: The ability to store and manipulate data as
BL-2
needed for complex computations.
Conditional Statements: Support for conditional logic (e.g., if-else
statements) to make decisions based on various inputs.
Loops and Iteration: The capability to execute repetitive tasks or
loops, which are essential for many algorithms and processes.
d.   Why can’t we store large data directly on blockchains like Ethereum or
Bitcoin?
Solution:
1. Nodes Must Store Entire Blockchain Copy
• Blockchains rely on nodes (computers) to maintain the network.
•   Full nodes store the entire history of the blockchain for
verification and security.
•   If large files were stored on-chain, every node would need to
store those files, making it extremely heavy and impractical.
CO-3 ;
2. Immutable Nature → No Deletion
SO-1,2 ;
• Blockchain is immutable, meaning data cannot be deleted or
BL-3
changed.
• Once large files are added, they stay forever, causing unlimited
growth in storage requirements.
• Over time, this would make running a node impossible for most
users.
3. Large Files Slow Down the Network
• Blockchains are optimized for small transactions (like hashes
and smart contracts).
• Adding large files would:
********** 2 **********
--- page 3 ---
o Increase block size.
o Slow down transaction processing.
o Cause network congestion and higher fees.
4. Nodes Must Remain Lightweight for Decentralization
•   Decentralization works only if many people can run nodes.
•   If storage requirements become huge, only big companies could
afford to run nodes → centralization risk.
• Keeping nodes lightweight ensures accessibility and security.
a.   Illustrate the operation of proof of work (PoW) mechanism in validating
blockchain transactions and demonstrate it through an appropriate
example.
Solution:
PoW operation 6 marks and example 4 marks
▪   Operation: In PoW, “proof” is a solution to a computationally
difficult puzzle; “work” is expended computing that solution. Miners
compete to solve a cryptographic puzzle (find a nonce so that the
block’s hash meets a target). The first miner to solve it earns the right
to append the block and collect the mining reward/fees. Nodes then
verify the solution cheaply by hashing the block with the nonce. PoW
secures the network by making block reorganization or fraudulent
rewriting extremely costly.
▪ Steps :
▪   Puzzle: Miners compete to solve a mathematical puzzle. This
puzzle is difficult and requires a lot of computing power.
▪ Broadcast: The first miner to solve the puzzle shares the
solution with the network.
▪   Verification: Other nodes (computers) on the network check
Q2   if the solution is correct.
CO-2;   ▪ Block Added: If the solution is valid, the new block (which [10]
SO-1,2;   contains transactions) is added to the blockchain.
BL-3   ▪ Reward: The miner who solved the puzzle is rewarded,
typically with cryptocurrency (e.g., new Bitcoin).
▪ Working steps
▪ Example : Bitcoin solving SHA 256 hash lets a miner add the block
and gain coin rewards
********** 3 **********

[Text in pictures on this page, read by OCR]
|

Puzzle

Send Puzzle

xt

x2

Send Solutions

[BPI send award

Network server

Checks solutions

y=ton) = wrong
y=f(x2) © correct
y=£(x3) © wrong
--- page 4 ---
b.   What are the limitations of distributed database and how it is overcome
in blockchain?
Solution:
limitations of distributed database – 5 marks
how it is overcome in blockchain- 5 marks
A distributed database is a collection of interrelated data stored across
multiple computers (nodes) connected by a network.
It focuses on data availability, fault tolerance, and performance, but it
still relies on a central authority or administrator for control and
validation.
Admins or compromised nodes can modify or delete records without
detection. Users cannot independently verify data changes or history —
logs are maintained by the administrator. Central coordinator or master
CO-1;
node failure can affect the entire system’s availability or consistency.
SO-1,2;   [10]
Audit trails are not inherently built-in; need external logging
BL-3
mechanisms.
Blockchain-
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
This means that there is no central controller in the network, and all
participants talk to each other directly. consensus mechanisms (like
Proof of Work, Proof of Stake) ensure trust through decentralized
validation. Blockchain uses cryptographic hashing (each block
references the previous one). Any data change breaks the hash chain,
making tampering easily detectable. Blockchain provides transparency
— every transaction is visible to all participants and verifiable on a
shared ledger.
a.   Explain types of blockchain. Identify and justify the type of blockchain
that may be used for the given scenario: A company called AgriChain
Pvt. Ltd. wants to implement a system to track the journey of
Q3   agricultural products from farmers to supermarkets.
CO-1;   Solution:
[10]
SO-1,2;   Types of blockchain- 8 marks
BL-3   Public blockchains- As the name suggests, public blockchains are not
owned by anyone.
They are open to the public, and anyone can participate as a node in the
decision-making process.
********** 4 **********
--- page 5 ---
Users may or may not be rewarded for their participation.
All users of these permissionless or unpermissioned ledgers maintain a
copy of the ledger on their local nodes and use a distributed consensus
mechanism to decide the eventual state of the ledger.
Bitcoin and Ethereum are both considered public blockchains.
Private blockchain/ Consortium Blockchain - As the name implies,
private blockchains are just that—private.
That is, they are open only to a consortium or group of individuals or
organizations who have decided to share the ledger among themselves.
There are various blockchains now available in this category, such as
HydraChain and Quorum.
Optionally, both of these blockchains can also run in public mode if
required, but their primary purpose is to provide a private blockchain.
Semiprivate blockchains or Hybrid: With semiprivate blockchains, part
of the blockchain is private and part of it is public.
With a semi-private blockchain, the private part is controlled by a group
of individuals, while the public part is open for participation by anyone.
This hybrid model can be used in scenarios where the private part of the
blockchain remains internal and shared among known participants,
while the public part of the blockchain can still be used by anyone,
optionally allowing mining to secure the blockchain.
Multiple trusted entities share access
Scenario- Private or consortium with justification: Shared responsibility
among selected organizations like farmers, govt agencies and suppliers.
Public will not have access to this data.
b.   What is Contractual Confidentiality? Explain role of Smart contracts in
digitization of legal contracts with an example.
Solution:
What is Contractual Confidentiality- 5 marks
Explain role of Smart contracts in digitization of legal contracts with an
example- 5 marks
Contractual confidentiality is a fundamental obligation to protect parties
who disclose information, and smart contracts are transaction protocols
that automate agreements. Confidential smart contracts are a type of
smart contract that use cryptographic techniques to protect data and
execution logic on public blockchains.
CO-2;   Smart contracts are self-executing contracts, encoded on blockchain
SO-1,2;   platforms, automate and enforce contract terms without the need for   [10]
BL-3   intermediaries.
A smart contract is a secure and unstoppable computer program
representing an agreement that is automatically executable and
enforceable.
A smart contract is an electronic transaction protocol that executes the
terms of a contract. The general objectives are to satisfy common
contractual conditions (such as payment terms, liens, confidentiality,
and even enforcement), minimize exceptions both malicious and
accidental, and minimize the need for trusted intermediaries. Related
economic goals include lowering fraud loss, arbitrations and
enforcement costs, and other transaction costs.
a.   Explain the working and impact of Sybil attacks and Selfish mining
Q4   [10]
with suitable examples.
********** 5 **********
--- page 6 ---
CO-2;   Solution:
SO-1,2;   Explain sybil attack- 5 marks
BL-3   Explain selfish attack- 5 marks
•   Sybil attack- A Sybil attack is a type of network attack in which
an attacker creates and uses multiple fake identities, or “Sybil
nodes,” to gain an unfair advantage or perform malicious actions
within a network.
• This can be accomplished by creating multiple fake identities
and using them to gain a disproportionate level of influence
within the network, such as by participating in a consensus
process or voting system.
• The goal of a Sybil attack is to manipulate the network or disrupt
its normal operation, often for personal or financial gain.
•   If enough fake identities are created, this attack can be used to
outvote the honest nodes on the network.
•   If attackers manage to control more than 51% of the hash rate,
then they can reorder the transactions, censor transactions, and
effectively take over the entire network.
Selfish mining: This occurs when a miner withholds the blocks they
mine from the network in order to increase their chances of finding the
next block and earning the block reward.
• A selfish mining attack can occur when an attacker manages to
solve the PoW and mine a block but instead of announcing it to
the network, they withhold it from the public chain.
• This would create a fork, and the attacker can then keep mining
on the new forked chain, albeit only known to them, to build an
alternative chain and get ahead of the public blockchain.
• When this malicious chain is ahead of the honest public chain,
the latest block can be released to the network.
• As the network is programmed to accept the most recent block,
the malicious fork will overwrite the honest/original chain.
• This attack can result in achieving virtually any type of
malicious goal, including double-spending, stealing
cryptocurrency, censoring transactions, and similar goals.
b.   What is blockchain storage? Discuss its design, challenges, and
relevance in the context of Web3.
Solution:
CO-3;   What is blockchain storage?- 5 marks
SO-1,2;   Discuss its design, challenges, and relevance in the context of Web3- 5   [10]
BL-3   marks.
Blockchain storage refers to a decentralized method of storing data
where users retain true ownership, and data is distributed across a
network of nodes rather than being stored on a centralized server. Unlike
********** 6 **********
--- page 7 ---
traditional cloud services like Google Cloud or Dropbox, blockchain
storage eliminates the need for trust in a central authority, aligning with
Web3 principles of transparency, immutability, and decentralization.
Design of Blockchain Storage:
• Decentralized Architecture: Data is stored across multiple
nodes, ensuring no single point of failure.
• Content Addressing: Systems like IPFS use cryptographic
hashes (CIDs) to locate data based on content rather than location.
• Smart Contracts: Used to manage access and permissions.
• Off-chain Storage: Large files (e.g., videos, documents) are
stored off-chain, while blockchain stores metadata or hashes for
verification.
Challenges:
1. Scalability: Blockchains like Ethereum and Bitcoin are not
designed to store large files due to size and cost limitations.
2. Node Storage Limits: Full nodes must store the entire
blockchain, making it impractical to store extensive data directly
on-chain.
3. Immutability: Once data is added, it cannot be deleted, which can
lead to bloating.
4. Decentralization vs. Accessibility: Ensuring nodes remain
lightweight enough to maintain decentralization.
Relevance in Web3:
• Blockchain storage supports data sovereignty, allowing users to
control their own data.
•   It reduces reliance on centralized entities, enhancing privacy and
security.
Projects like IPFS, Filecoin, Arweave, Sia, Storj, and Crust Network
are pioneering decentralized storage solutions.
a.   Analyse the phases of the practical byzantine fault tolerance (PBFT)
algorithm and discuss how it mitigates the challenges of the Byzantine
Fault Problem.
Solution:
the phases with diagram 5 marks and mitigation challenges 5 marks
• Pre-prepare phase: The leader node sends out a pre-prepared
Q5
message to each backup node.
CO-2;
• Prepare: after receiving the pre-prepared message from the [10]
SO-1,2;
leader, the backup nodes send the prepared message as a reply to
BL-4
all other nodes including the leader. A node is considered prepared
only if it has received pre-prepared by the leader and seen (2f +
1) number of prepared messages from other nodes.
• Commit: If the nodes are prepared, they send a commit message.
If a node receives (f + 1) commit messages, they carry out the
client’s request.
********** 7 **********
--- page 8 ---
Mitigation of Byzantine challenges:
• Leader-based coordination provides an orderly proposal flow
while backups cross-check messages.
• Message quorums (2f+1, f+1 thresholds) ensure that even with
up to f malicious nodes, honest nodes reach consistent state and
cannot be permanently prevented from committing.
• Digital signatures & sequence numbers prevent message
tampering and replay; authenticity and ordering are enforced.
• Tolerates malicious behaviour as long as faulty nodes < 1/3 of
total, preventing conflicting decisions and ensuring safety and
liveness in presence of Byzantine faults.
• Trade-offs: PBFT is energy-efficient and fast for permissioned
networks but suffers from high communication overhead (O(n²)
messages), limiting scalability to modest node counts.
b.   Explain the role of oracles in bridging blockchain systems with real-
world data. Explain any two ues-cases of oracles in blockchain.
Solution:
Explain role of oracle- 4 marks
Two use-cases- 6 marks
Role of Oracle-
Blockchain systems are inherently deterministic and isolated. Smart
contracts execute exactly as coded but cannot access external
information (like market prices, sensor readings, or weather data) on
their own. This is where oracles come in:
CO-2;   • Data Provision: Feeds information like stock prices, commodity
SO-1,2;   [10]
rates, sensor readings, or identity verification data into smart
BL-3
contracts.
• Triggering Smart Contracts: Allows contracts to execute actions
automatically when specific conditions occur (e.g., paying insurance
claims after a weather event).
• Bridging Different Systems: Connects off-chain systems (like IoT
devices, APIs, or databases) with on-chain logic, enabling
blockchain to interact with the real world.
• Validation & Trust: Some oracles provide cryptographic proofs or
multi-source aggregation to ensure the accuracy and reliability of
external data.
********** 8 **********
--- page 9 ---
Example Use Cases of Oracles
1. Price Feeds (DeFi): Provide real-time cryptocurrency or fiat
currency prices. A DeFi lending protocol (like Aave or Compound) uses
a price oracle to get ETH/USD rates. To calculate collateral values and
prevent liquidation errors.
2. Weather Data (Insurance): Weather-based crop insurance for
farmers. A smart contract pays compensation automatically if rainfall is
below a certain level, based on data from a weather oracle. To bring off-
chain weather data (temperature, rainfall, etc.) onto the blockchain.
3. Sports/Prediction Markets: Fetch results of real-world events such
as football matches or elections. A prediction market uses oracles to
determine the outcome of a bet. To bring verified event results on-
chain.
a.   Differentiate between tokenized and tokenless blockchains. What role
does a shared ledger play in both models?
(10)
Solution:
Differentiate between tokenized and tokenless blockchains- 6 marks
Role of shared ledger- 4 marks
Tokenized Blockchains: A tokenized blockchain uses digital tokens as
the fundamental unit of value or incentive within the network. These
tokens may represent cryptocurrencies, digital assets, or utility tokens
that participants use for transactions, rewards, or governance. Tokenized
blockchains rely on economic incentives to secure the network and ensure
honesty in consensus mechanisms.
Key Features:
Operates on a public or permissionless network. Tokens are used to
reward miners or validators (e.g., Proof of Work or Proof of Stake). The
blockchain often supports smart contracts and decentralized applications
(DApps).
Role of Shared Ledger:
Q6   In tokenized blockchains, the shared ledger acts as a transparent and
CO-1;   immutable record of all token transactions, ownerships, and smart
[10]
SO-1,2;   contract executions. It ensures trustless verification — every participant
BL-4   can independently validate balances and transfers without intermediaries.
The ledger essentially serves as the backbone of the token economy.
2. Tokenless Blockchains: A tokenless blockchain does not involve any
native cryptocurrency or tradeable token. Instead, it focuses on data
integrity, transparency, and secure record-keeping among authorized
participants. Tokenless systems are typically permissioned or private,
managed by enterprises or consortiums where participants are already
known and trusted.
Key Features:
Operates on a private or consortium network. No need for mining or
staking; consensus is achieved through known nodes using algorithms
like Practical Byzantine Fault Tolerance (PBFT) or Raft. Focuses on
business process automation, data sharing, and auditability rather than
financial incentives.
Role of Shared Ledger:
In tokenless blockchains, the shared ledger serves as a trusted, tamper-
proof record of all transactions or data exchanges among participants. It
ensures that all authorized parties maintain a synchronized and verifiable
********** 9 **********
--- page 10 ---
view of shared information, enabling transparency, traceability, and
accountability without the need for tokens or financial rewards.
b.   Explain following elements of Ethereum Blockchain:
i.   Nodes
ii.   Ethereum network
iii.   Gas
iv.   Wallets
Solution: Explanation of each element – 2 marks *5=10 marks
• Node is any computer that participates in the Ethereum network
by running the Ethereum software (client). Each node maintains
a copy of the blockchain, verifies transactions, and helps
propagate data across the network.
Types of Ethereum Nodes
Full Node- Stores the entire blockchain and validates all
transactions and smart contracts independently.
Light Node- Stores only block headers (summaries) and relies on
full nodes for transaction data. Suitable for mobile or lightweight
devices.
CO-2;
• The Ethereum network is the global system of interconnected
SO-1,2;   [10]
nodes that collectively maintain the Ethereum blockchain. It is a
BL-3
peer-to-peer (P2P) network — meaning there is no central
server; every node communicates directly with others.
• Gas is required to be paid for every operation performed on the
Ethereum blockchain. This is a mechanism that ensures that
infinite loops cannot cause the whole blockchain to stall due to
the Turing-complete nature of the EVM. A transaction fee is
charged as an amount of Ether and is taken from the account
balance of the transaction originator. Gas is charged in three
scenarios as a prerequisite to the execution of an operation:
• The computation of an operation
• For contract creation or message calls
• An increase in the use of memory
• An Ethereum wallet is a software or hardware tool that stores
your cryptographic keys and allows you to send, receive, and
manage Ether (ETH) and interact with smart contracts.
a.   What is sharding? How does sharding mitigate the vulnerabilities of
different types of attacks.
Solution:
What is sharding- 4 marks
How does sharding mitigate the vulnerabilities of different types of
Q7   attacks- 6 marks
CO-3;
[10]
SO-1,2;   Sharding is a technique used to improve the scalability and performance
BL-3   of decentralized systems, particularly in blockchain networks.
It involves dividing the network into smaller parts called "shards," where
each shard processes only a subset of the overall network's transactions,
rather than having every node process every transaction.
This drastically reduces the computational burden and allows the system
to scale efficiently.
********** 10 **********
--- page 11 ---
In the context of consensus algorithms, sharding can also help in
preventing attacks, especially those that target the network's consensus
mechanism, such as Sybil attacks, 51% attacks, and Denial of Service
(DoS) attacks.
Below is an outline of how sharding-based consensus algorithms can
mitigate these types of attacks:
Sybil Attacks Prevention
In a Sybil attack, a malicious entity creates multiple fake identities
(nodes) to take control of a significant portion of the network.
Sharding prevents this by randomly assigning nodes to different shards.
Even if an attacker creates several fake identities, the probability of all
those identities ending up in the same shard is low. This fragmentation
makes it harder for the attacker to gain majority control in any shard.
51% Attack Mitigation
A 51% attack occurs when an entity gains control of the majority of the
network's mining or validation power, allowing it to rewrite the
blockchain and double-spend tokens.
Sharding mitigates this by spreading the network's computational or
validation power across multiple independent shards. An attacker would
have to control the majority in every shard simultaneously, which is far
more difficult and resource-intensive than controlling 51% of a single
network.
b.   Discuss any two applications of Blockchain technology in the government
sector. Explain and justify why the use of Blockchain is essential in these
applications.
Solution:
Each application with justification- 5 marks*2=10 marks.
Elections: Voting in any government is a key function and allows
citizens to participate in the democratic election process. Usually, the
limitations in current voting systems revolve around fraud, weaknesses
in operational processes, and especially transparency.
Blockchain-based voting systems can resolve these issues by
introducing end-to-end security and transparency into the process.
Security is provided in the form of the guaranteed integrity and
CO-3;
authenticity of votes by using public key cryptography, which comes as
SO-1,2;   [10]
standard in a blockchain. Moreover, the immutability guaranteed by a
BL-3
blockchain ensures that votes cast once cannot be cast again.
Border control: Automated border control systems have been in use for
decades now to thwart illegal entry into countries and prevent terrorism
and human trafficking.
Blockchain technology can provide a solution to this problem by
maintaining a blacklist in a smart contract that can be updated as
required. Any changes will be immediately visible to all agencies and
border control points, thus enabling immediate control over the
movement of a suspected travel document.
The full database of all travel documents may not be stored on the
blockchain currently due to inherent storage limitations, but a backend
distributed database such as BigchainDB, IPFS, or Swarm can be used
for that purpose.
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 51895d9bbfab

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO-1 ;   a.   Explain the limitations of traditional Distributed DBMS.   [5]
SO-2 ;
BL-1   Answer:
Limitation   Description
Design, deployment, and maintenance are
Complexity
difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Fault tolerance and transaction rollback are
Recovery
complex
Concurrency   Synchronizing access is difficult and error-prone
High due to software, hardware, and expertise
Cost
needs
CO-2 ;   b.   Differentiate between tokenized and tokenless blockchains with suitable   [5]
SO-2 ;   examples.
BL-2
Answer: A tokenized blockchain uses a native digital token (cryptocurrency)
to power the network, incentivize participants, and validate transactions.
A tokenless blockchain operates without any native cryptocurrency and
focuses mainly on data sharing and enterprise applications.
Presence of Cryptocurrency
Tokenized: Has its own cryptocurrency (e.g., Bitcoin, Ethereum).
Tokenless: No native cryptocurrency is used.
Incentive Mechanism
********** 1 **********
--- page 2 ---
Tokenized: Participants (miners/validators) are rewarded with
tokens for validating transactions.
Tokenless: No financial incentives; participants are usually
authorized entities working collaboratively.
Network Type
Tokenized: Mostly used in public or open blockchains.
Tokenless: Common in private or permissioned blockchains.
Use Cases
Tokenized:
Cryptocurrencies
Decentralized finance (DeFi)
Digital payments
Tokenless:
Supply chain management
Banking systems
Enterprise data sharing
CO-2 ;   c. What is contractual confidentiality in blockchain systems? Why is it   [5]
SO-2 ;   important?
BL-1
Answer: Contractual confidentiality refers to the ability to keep the details of
a contract (such as terms, conditions, and participant data) private and
accessible only to authorized parties, even when the contract is executed on a
blockchain network.
In blockchain systems—especially when using Smart Contracts—transactions
are typically transparent. However, not all business agreements can be
publicly visible. Contractual confidentiality ensures that sensitive information
is protected while still benefiting from blockchain features like security and
immutability.
Why is it Important?
1. Protection of Sensitive Data
2. Privacy in Transparent Systems
3. Regulatory Compliance
4. Secure Business Transactions
5. Trust Among Participants
CO-3 ;   d.   Explain the importance of Turing-Completeness with an appropriate   [5]
SO-2 ;   example.
BL-2
Answer: Turing-Completeness is a property of a computational system that
indicates it can perform any computation or solve any problem that a Turing
Machine can, provided sufficient time and memory.
Importance:
1. Flexibility in Programming:
A Turing-complete system can implement complex logic, algorithms, and
computations, making it highly versatile.
2. Smart Contract Capability:
In blockchain, Turing-completeness allows developers to write advanced
smart contracts with conditional logic, loops, and functions.
3. Automation of Complex Processes:
It enables automation of real-world agreements and workflows without
intermediaries.
********** 2 **********
--- page 3 ---
4. Wide Range of Applications:
Supports development of decentralized applications (dApps), games,
financial systems, and more.
Example:
Ethereum is a Turing-complete blockchain. Its smart contract language
(Solidity) allows developers to write complex programs—for example, a
decentralized lending system that automatically calculates interest, checks
conditions, and executes transactions based on predefined rules.
Attempt any 4
Q2   a. Draw and explain generic structure of Blockchain. Explain in details the   [10]
elements of Blockchain.
CO-1 ;
SO-2 ;
BL-2
Answer:
Address: Addresses are unique identifiers used in a blockchain transaction to
denote senders and recipients. An address is usually a public key or derived
from a public key. While addresses can be reused by the same user, addresses
themselves are unique. In practice, however, a single user may not use the
same address again and generate a new one for each transaction. This newly-
created address will be unique. A good practice is for users to generate a new
address for each transaction in order to avoid linking transactions to the
common owner, thus preventing identification.
Transaction: A transaction is the fundamental unit of a blockchain. A
transaction represents a transfer of value from one address to another. Block:
A block is composed of multiple transactions and other elements, such as the
previous block hash (hash pointer), timestamp, and nonce.
Peer-to-peer network: As the name implies, a peer-to-peer network is a
network topology wherein all peers can communicate with each other and
send and receive messages.
Scripting or programming language: Scripts or programs perform various
operations on a transaction in order to facilitate various functions. For
example, in Bitcoin, transaction scripts are predefined in a language called
Script, which consist of sets of commands that allow nodes to transfer tokens
from one address to another.
Bitcoins scripting language
Ethereum solidity language (Turing Complete)
Q2   b.   Explain the difference between Sybil attacks and Selfish Mining in   [10]
blockchain.
CO-3 ;
SO-2 ;
Answer:
BL-2
Basis   Sybil Attack   Selfish Mining
An attack where a single   A strategy where a miner or group
entity creates multiple fake   of miners withhold mined blocks to
Definition
identities (nodes) to gain   gain an unfair advantage and
control over the network.   increase their rewards.
To manipulate network
Main   operations like voting,   To maximize mining rewards by
Objective   consensus, or reputation   controlling the release of blocks.
systems.
********** 3 **********
--- page 4 ---
Creating numerous fake
Method   Keeping mined blocks private and
nodes to dominate the
Used   releasing them strategically.
network.
Can disrupt consensus,
Impact on   Leads to unfair reward distribution
reduce trust, and enable
Network   and reduces network efficiency.
double-spending.
Target Area Peer-to-peer network layer.   Mining and consensus mechanism.
An attacker flooding a
A miner in Bitcoin hiding blocks to
Example   blockchain network with fake
outperform honest miners.
nodes to influence decisions.
Q3   a. What are oracles in blockchain? Explain their types and their role in smart   [10]
contracts.
CO-3 ;
SO-2 ;
BL-2
Answer: Oracles are third-party services that act as a bridge between a
blockchain and the outside world. Since blockchains cannot directly access
external data (due to security and determinism constraints), oracles provide
real-world data to smart contracts and also send data from smart contracts
to external systems.
Types of Oracles
1. Software Oracles
• Provide data from online sources such as websites, APIs, and
databases.
• Examples: weather data, stock prices, sports results.
• Widely used in financial and prediction-based smart contracts.
2. Hardware Oracles
•   Collect data from physical devices and sensors.
• Examples: RFID sensors, temperature sensors, barcode scanners.
•   Useful in supply chain systems where physical events must be
recorded on blockchain.
3. Inbound Oracles
•   Bring external data into the blockchain.
• Example: Sending current market price of a commodity to a smart
contract for futures trading.
4. Outbound Oracles
• Send data from blockchain to the outside world.
• Example: A smart contract triggers a bank payment or sends a
notification after conditions are met.
Role of Oracles in Smart Contracts
• Data Feeding: Provide real-time and accurate external data required
for contract execution.
********** 4 **********
--- page 5 ---
• Automation: Enable smart contracts to execute automatically when
predefined real-world conditions are met.
•   Interoperability: Allow blockchain systems to interact with external
systems such as banking networks, IoT devices, and APIs.
• Use in Futures Systems: In blockchain-based futures trading, oracles
supply market prices, enabling automatic settlement of contracts.
Q3   b.   Explain the types of Ethereum accounts and the working mechanism of the   [10]
CO-2 ;   Ethereum blockchain.
SO-2 ;
BL-2   Answer: Types of Ethereum Accounts
In Ethereum, there are mainly two types of accounts:
a) Externally Owned Accounts (EOAs)
•   Controlled by users through private keys.
• Used to send and receive Ether and initiate transactions.
• Do not contain executable code.
• Example: A user wallet used for transferring ETH.
b) Contract Accounts
•   Controlled by smart contract code, not by private keys.
• Created when a smart contract is deployed on the blockchain.
•   Automatically execute predefined functions when triggered.
• Used in applications like DeFi, voting systems, etc
Working Mechanism of Ethereum Blockchain
The working of Ethereum involves several steps:
Step 1: Transaction Initiation
• A user (via EOA) creates a transaction (sending Ether or interacting
with a smart contract).
• The transaction is signed using the user’s private key.
Step 2: Transaction Broadcasting
• The transaction is broadcast to the Ethereum network and enters the
mempool (pending transactions).
Step 3: Validation by Nodes
• Nodes verify the transaction for correctness (valid signature,
sufficient balance, etc.).
Step 4: Block Creation
•   Validators/miners collect valid transactions and group them into a
block.
Step 5: Consensus Mechanism
• Ethereum uses Proof of Stake (PoS) (earlier Proof of Work).
•   Validators stake Ether and are chosen to validate and add new blocks.
********** 5 **********
--- page 6 ---
Step 6: Execution of Smart Contracts
•   If the transaction involves a contract, the code is executed on the
Ethereum Virtual Machine (EVM).
Step 7: Block Addition
• The validated block is added to the blockchain.
• The ledger is updated across all nodes.
Step 8: Transaction Confirmation
• The transaction becomes immutable and is confirmed after multiple
blocks are added.
Q4   a. What is Ethereum? Explain its key benefits and discuss the limitations of the   [10]
CO-3 ;   Ethereum platform.
SO-2 ;
BL-3   Answer: Ethereum is a decentralized, open-source blockchain platform that
enables developers to build and deploy smart contracts and decentralized
applications (dApps).
Unlike traditional blockchains that mainly support digital currency
transactions, Ethereum allows programmable logic through its Ethereum
Virtual Machine (EVM).
Key Benefits of Ethereum
1. Decentralization
o No central authority controls the network.
o Reduces risk of censorship and single point of failure.
2. Smart Contracts
o Self-executing contracts that run automatically when
conditions are met.
o Eliminates intermediaries and increases efficiency.
3. Transparency and Security
o   All transactions are recorded on a public ledger.
o Data is secure and tamper-resistant.
4. Programmability
o Developers can build a wide range of applications (DeFi, NFTs,
gaming, etc.).
5. Global Accessibility
o Anyone with internet access can participate in the network.
6. Tokenization
o Supports creation of custom tokens (ERC-20, NFTs), enabling
digital assets and fundraising.
Limitations of Ethereum
1. Scalability Issues
o Limited transactions per second (TPS), leading to network
congestion.
2. High Gas Fees
o Transaction costs can become very high during peak usage.
3. Complexity
o Development and usage require technical knowledge.
4. Security Risks in Smart Contracts
o Bugs in contract code can lead to financial losses.
********** 6 **********
--- page 7 ---
5. Energy Consumption (Earlier)
o Previously used Proof of Work, which consumed high energy
(now improved with Proof of Stake).
6. Network Congestion
o Heavy usage can slow down transaction processing.
Q4   b.   Explain 51% attacks in blockchain. Discuss real-world cases of 51% attacks   [10]
CO-1 ;   and explain possible mitigation strategies in detail.
SO-2 ;
BL-2   Answer: A 51% attack occurs when a single entity or group gains control of
more than 50% of a blockchain network’s mining or validation power.
This allows the attacker to manipulate the blockchain by:
•   Reversing transactions (double spending)
•   Preventing new transactions from being confirmed
•   Blocking or modifying transaction order
It mainly affects Proof of Work (PoW) blockchains.
Real-World Cases of 51% Attacks
a) Ethereum Classic (2019, 2020)
• Attacked multiple times.
• Hackers reorganized the blockchain and performed double-spending
attacks.
•   Millions of dollars worth of ETC were lost.
b) Bitcoin Gold (2018)
•   Attackers gained majority hash power.
• Double-spent coins worth over $18 million.
• Exchanges suffered significant losses.
c) Vertcoin (2018, 2019)
•   Suffered repeated 51% attacks.
•   Attackers reorganized blocks and executed double spending.
Mitigation Strategies
a) Increase Network Hash Power
• A larger and more decentralized network makes attacks expensive
and difficult.
b) Transition to Proof of Stake (PoS)
•   In PoS, attackers need to control a majority of staked coins, which is
costly.
• Example: Ethereum moved from PoW to PoS.
c) Confirmation Delays
• Exchanges can require more confirmations before accepting
transactions, reducing double-spending risk.
********** 7 **********
--- page 8 ---
d) Mining Pool Decentralization
• Avoid concentration of mining power in a few pools.
e) Checkpointing
• Hard-code checkpoints in the blockchain to prevent deep chain
reorganizations.
f) Hybrid Consensus Mechanisms
• Combine PoW with PoS or other methods to improve security.
g) Monitoring and Alerts
•   Detect unusual hash rate spikes or suspicious chain reorganizations.
Q5   a. What are the steps involved in blockchain development and deployment?   [10]
CO-3 ;   Explain in detail.
SO-2 ;
BL-2   Answer: 1. Problem Identification and Use Case Definition
•   Clearly define the problem you want to solve.
• Determine whether blockchain is actually needed (e.g., need for
decentralization, trust, transparency).
•   Identify the use case such as supply chain, finance, healthcare, etc.
2. Choosing the Right Blockchain Platform
•   Select an appropriate platform based on requirements:
o Ethereum – for smart contracts and dApps
o Hyperledger Fabric – for permissioned enterprise solutions
o Corda – for financial applications
3. Designing the Architecture
• Decide the type of blockchain: public, private, or consortium.
•   Define network structure, nodes, consensus mechanism, and data
flow.
• Plan security, scalability, and privacy requirements.
4. Smart Contract Development
• Write smart contracts (business logic) using appropriate languages
(e.g., Solidity).
•   Define rules, conditions, and workflows.
• Ensure proper coding practices to avoid vulnerabilities.
5. Frontend and Backend Development
• Develop user interface (UI) for interaction.
•   Build backend systems to connect blockchain with applications (APIs,
databases).
• Use tools like Web3.js or similar libraries.
********** 8 **********
--- page 9 ---
6. Testing
• Perform unit testing, integration testing, and system testing.
• Use test networks (testnets) to simulate real-world scenarios.
•   Identify and fix bugs or vulnerabilities.
7. Security Auditing
• Conduct thorough smart contract audits.
• Check for issues like reentrancy, overflow, and access control flaws.
• May involve third-party security audits.
8. Deployment
• Deploy smart contracts on the main network (mainnet).
•   Configure nodes and network settings.
• Ensure proper gas fees and deployment parameters.
9. Monitoring and Mainenance
• Continuously monitor performance and transactions.
•   Fix bugs, upgrade contracts (if possible), and optimize performance.
• Ensure network security and handle updates.
10. Scaling and Optimization
• Improve performance using Layer 2 solutions, sharding, or
sidechains.
• Optimize transaction speed and cost.
Q5   b.   Explain how blockchain technology is evolving in the field of finance. Discuss   [10]
CO-2 ;   its benefits and challenges with suitable examples.
SO-2 ;
BL-2   Answer: Evolution of Blockchain in Finance
Blockchain technology has significantly transformed the financial sector by
introducing decentralization, transparency, and automation.
a) Digital Payments and Cryptocurrencies
• Blockchain enables peer-to-peer transactions without intermediaries.
• Example: Bitcoin allows global payments with lower fees and faster
processing.
b) Smart Contracts and DeFi
•   Platforms like Ethereum enable Decentralized Finance (DeFi).
•   Services such as lending, borrowing, and trading are automated using
smart contracts.
c) Cross-Border Payments
•   Traditional international transfers are slow and expensive.
• Blockchain solutions reduce transaction time from days to minutes.
********** 9 **********
--- page 10 ---
d) Tokenization of Assets
• Real-world assets (stocks, real estate) are converted into digital
tokens.
• Enables fractional ownership and increased liquidity.
e) Clearing and Settlement
• Blockchain reduces settlement time in financial markets (T+2 → near
real-time).
•   Eliminates intermediaries like clearing houses.
2. Benefits of Blockchain in Finance
1. Transparency
o   All transactions are recorded on a shared ledger.
o Reduces fraud and increases trust.
2. Security
o Cryptographic techniques ensure data integrity and
protection.
3. Cost Reduction
o Removes intermediaries, lowering transaction and operational
costs.
4. Speed and Efficiency
o Faster transactions, especially in cross-border payments.
5. Financial Inclusion
o Provides access to financial services for unbanked
populations.
6. Automation
o Smart contracts automate processes, reducing human error.
3. Challenges of Blockchain in Finance
1. Regulatory Uncertainty
o Governments are still developing laws for blockchain and
cryptocurrencies.
2. Scalability Issues
o Networks may struggle with high transaction volumes.
3. Security Risks
o Smart contract bugs and cyberattacks can lead to losses.
4. High Implementation Cost
o   Initial setup and integration with existing systems can be
expensive.
5. Energy Consumption (Earlier Systems)
o Some blockchains (PoW-based) consume high energy.
6. Lack of Awareness and Adoption
o Limited understanding slows adoption in traditional finance.
Q6   a.   Differentiate between Public Blockchain and Private Blockchain. Discuss their [10]
CO-3 ;   suitability for financial applications.
SO-2 ;
BL-2   Answer:
Basis   Public Blockchain   Private Blockchain
Restricted to authorized
Open to anyone
Access   participants
(permissionless)
(permissioned)
********** 10 **********
--- page 11 ---
Controlled by a single
Fully decentralized (no
Control   organization or
single authority)
consortium
Limited – only selected
High – all transactions
Transparency   participants can view
are visible
data
Very high (due to large   High, but depends on
Security
distributed network)   internal controls
Slower (due to
Faster (fewer nodes and
Speed   consensus mechanisms
simplified consensus)
like PoW/PoS)
Higher transaction cost Lower cost (no mining
Cost
(fees, energy use)   required)
Hyperledger Fabric, R3
Examples   Bitcoin, Ethereum
Corda
Public blockchains are ideal for open, trustless financial ecosystems, while
private blockchains are more suitable for controlled, secure, and regulation-
compliant financial environments. In practice, many financial institutions
prefer private or hybrid models to balance efficiency, privacy, and control.
Q6   b.   Explain how decentralization, transparency, and immutability contribute to   [10]
CO-2 ;   the evolution of futures trading using blockchain technology.
SO-2 ;
BL-2   Answer: 1. Decentralization
Decentralization means that control is not held by a single authority (like an
exchange or clearing house). Instead, the blockchain network is maintained by
multiple nodes.
Impact on Futures Trading:
Eliminates intermediaries such as brokers and clearing houses
Reduces transaction costs and delays
Minimizes single points of failure and manipulation
Enables peer-to-peer futures contracts using Smart Contracts
2. Transparency
All transactions on a blockchain are recorded on a shared ledger and are
visible to participants (depending on the type of blockchain).
Impact on Futures Trading:
Improves trust among traders due to open access to transaction history
Reduces fraud and market manipulation
Enhances auditability and regulatory oversight
Provides real-time tracking of futures contracts and settlements
3. Immutability
Once data is recorded on the blockchain, it cannot be altered or deleted due to
cryptographic linking of blocks.
Impact on Futures Trading:
Ensures integrity of contract terms and transaction records
Prevents disputes and tampering with trade data
Provides a reliable and permanent audit trail
Strengthens trust in automated settlement systems
Q7   a. Compare different consensus mechanisms (PoW, PoS, BFT, PoA, PoET) based   [10]
on energy efficiency, security, and scalability.
********** 11 **********
--- page 12 ---
CO-3 ;
SO-2 ;   Answer:
BL-2   Consensus
Energy Efficiency   Security   Scalability
Mechanism
Very high (strong Low (slow
Very low (high
Proof of Work   against attacks   transaction speed,
energy consumption
(PoW)   like double   limited
due to mining)
spending)   throughput)
High (no heavy
Proof of Stake   High (depends on Medium to High
computation
(PoS)   stake distribution) (faster than PoW)
required)
Byzantine   Very high   Medium (works
High (minimal
Fault   (tolerates   well in smaller
computational
Tolerance   malicious nodes   networks, limited
work)
(BFT)   effectively)   scalability)
Proof of   Medium to High   High (fast
Very high (low
Authority   (depends on   transaction
resource usage)
(PoA)   trusted validators) processing)
Very high (efficient High (secure if   High (good
Proof of
use of waiting time trusted execution performance in
Elapsed Time
via trusted   environment is   permissioned
(PoET)
hardware)   reliable)   systems)
Q7   b. What is a blockchain platform? Explain Hyperledger Fabric and Corda in   [10]
CO-1 ;   detail.
SO-2 ;   Answer: A blockchain platform is a digital infrastructure that allows
BL-2   developers and organizations to build, run, and manage blockchain-based
applications such as smart contracts and decentralized systems.
It provides tools, protocols, and frameworks to create secure, transparent,
and distributed networks.
Hyperledger Fabric is an open-source, permissioned blockchain platform
developed under the Linux Foundation.
Key Features:
• Permissioned Network:
Only authorized participants can join and perform transactions.
• Modular Architecture:
Components like consensus and membership services can be
customized.
• No Native Cryptocurrency:
It is a tokenless blockchain, mainly used for enterprise applications.
• Smart Contracts (Chaincode):
Written in languages like Go, Java, or Node.js.
• Channels for Privacy:
Allows private communication between specific participants.
Working:
1. A transaction is proposed by a client.
2. Endorsing peers validate the transaction.
3. The ordering service orders transactions into blocks.
4. Blocks are distributed and validated across the network.
5. Ledger is updated.
********** 12 **********
--- page 13 ---
Use Cases:
• Supply chain management
• Banking and finance
•   Healthcare systems
3. Corda
Corda is a distributed ledger platform designed mainly for financial
institutions, developed by the R3.
Key Features:
• Permissioned Network:
Only trusted parties can participate.
• No Global Broadcast:
Transactions are shared only with relevant parties (privacy-focused).
• No Native Cryptocurrency:
Designed for real-world financial agreements rather than tokens.
• Smart Contracts:
Written in Java or Kotlin.
• Notary Service:
• Ensures transaction uniqueness and prevents double-spending.
Working:
1. Parties involved agree on a transaction.
2. Transaction is verified using smart contract rules.
3. Notary validates uniqueness.
4. Transaction is recorded only by relevant participants.
Use Cases:
• Banking and financial services
• Trade finance
• Insurance
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 8a42773b50c2

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AI_7012/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
Q1   Compulsory Questions:
CO a What is a Distributed Database Management System (DDBMS)? Explain its limitations.   [5]
-   .
1 ;   Answer: A Distributed Database Management System (DDBMS) is a software system that manages a
SO   database distributed across multiple physical locations (computers or sites) connected via a
-   network. It allows users to access and manipulate data as if it were stored in a single centralized
2 ;   database, even though the data is actually spread across different locations.
BL
-1   Limitation   Description
Complexity   Design, deployment, and maintenance are difficult
Consistency   Hard to maintain ACID properties globally
Latency   Communication overhead between sites
Security   More attack vectors and risks
Recovery   Fault tolerance and transaction rollback are complex
Concurrency   Synchronizing access is difficult and error-prone
Cost   High due to software, hardware, and expertise needs
CO b What is Byzantine Fault Tolerance (BFT)?   [5]
-   .
2 ;   Answer: Byzantine Fault Tolerance (BFT) is a mechanism that enables a distributed network to
SO   successfully reach consensus even when some nodes behave incorrectly.
-
2 ;   •   In a distributed system, not all nodes can be trusted:
BL
-2   ❑ Some nodes may fail suddenly
❑ Some may send wrong or conflicting information
❑ Some may act maliciously on purpose to disrupt the system
********** 1 **********
--- page 2 ---
• BFT ensures that honest nodes can still agree on the correct state of the system, without
being affected by these faulty or malicious nodes.
•   The system works by communication and majority agreement.
•   Nodes exchange messages, verify information with each other, and make decisions based
on what most nodes agree is correct.
•   Because of this property, BFT is very important in blockchains and distributed systems,
where participants may not trust each other, but the system must still remain secure,
consistent, and reliable.
Example: Hyperledger Fabric (PBFT), Banking Consortium
CO   c   Explain the steps involved in deploying smart contracts on a blockchain in detail.   [5]
-   .
2 ;   Answer: Steps to Deploy a Smart Contract:
SO
-   1. Write the Smart Contract
2 ;   The contract is written using a programming language like Solidity (for Ethereum). It includes
the rules, conditions, and logic of the agreement.
BL   2. Compile the Code
-2   The written code is compiled using a compiler (e.g., Solidity compiler) to convert it into
bytecode, which the blockchain can understand. Errors are also checked at this stage.
3. Deploy to Blockchain
The compiled contract is sent to the blockchain network using a wallet or deployment tool (like
Remix or Truffle). A transaction is created and a deployment fee (gas) is paid.
4. Transaction Confirmation
The network validates the transaction through consensus mechanisms. Once confirmed, the
contract is assigned a unique address on the blockchain.
5. Contract Execution
After deployment, users can interact with the contract using its address. It automatically
executes predefined functions when conditions are met.
CO d   Explain the features of Ethereum in detail.   [5]
-   .
3 ;   Answer: Features of Ethereum
SO
-   1. Smart Contracts
2 ;   Ethereum allows developers to create smart contracts, which are programs that run automatically
when certain conditions are met. They are usually written using Solidity, an easy-to-learn
BL   programming language.
-2
2. Ethereum Virtual Machine (EVM)
The Ethereum Virtual Machine (EVM) is the system that runs and executes smart contracts on the
Ethereum network.
3. Ether (ETH)
Ether (ETH) is the cryptocurrency of Ethereum. It is used to pay transaction fees and run services
on the network.
4. Decentralized Applications (DApps)
Decentralized application (DApps) are applications that run on a decentralized network instead of
a single server. They work on Ethereum and can be accessed through a user interface.
5. Decentralized Autonomous Organizations (DAOs)
Decentralized autonomous organization (DAO) is a digital organization that works without central
control. Decisions are made through smart contracts and voting by members.
Attempt any 4
Q2 a What is blockchain? Explain the key elements of blockchain technology and describe how it works [10
.   with a suitable example.   ]
CO
-
********** 2 **********
--- page 3 ---
2 ;
SO   Answer: Blockchain technology is a decentralized, distributed, and digital ledger or digital database
-   that securely records transactions across a network of computers.
2 ;
•   It creates a transparent, immutable, and tamper-proof record of data that is shared and
BL   updated simultaneously across multiple participants.
-1   •   This system uses cryptographic linking and a consensus mechanism for validation, which
eliminates the need for a central authority and ensures data integrity and trust.
Key Components –
•   Cryptography
• P2P Network
•   Immutability
•   Transparency
•   Distributed Ledger
•   Smart Contracts
How It Works
• A transaction is requested (e.g. sending money).
• The transaction is broadcast to a network of computers (nodes).
• The nodes verify and validate the transaction using special rules.
• Once approved, the transaction is added to a block.
•   This block is linked to previous blocks, forming a chain.
• The updated chain is shared with all nodes in the network.
Q2 b What is a Sybil attack in blockchain? Explain its different types with relevant examples.   [10
.   ]
CO
-   Answer: Sybil Attacks - In a Sybil attack, one entity creates multiple fake identities (nodes) called
3 ;   as sybils to gain disproportionate influence over the network.
SO
-   Types:
2 ;
Direct Sybil attack happens when a malicious node interacts directly with the honest nodes within
BL   the protocol.
-2
◦   Such types of attacks are more effective as the authentic nodes cannot detect the
fake nodes.
◦ On top of it, attackers could manipulate genuine nodes to take actions that could
align with the self-interests of attackers.
Indirect Sybil attacks occur when the fake nodes interact with one or multiple nodes associated
with the authentic nodes.
◦   hackers would utilize intermediary or proxy nodes for launching indirect attacks.
◦   The intermediary nodes in between the authentic nodes and Sybil node would
serve as representatives of a single point of failure.
◦   Hackers could exploit the intermediary nodes and launch an attack on honest
nodes.
◦   They cannot be detected as easily as direct Sybil attacks.
Examples:
1. Sybil attack in blockchain in 2020, as hackers compromised the network with a different motive.
The attackers focused on Bitcoin owners who use Tor network. The hacker gained control over
majority of fake Tor relays and intercepted Bitcoin transactions by users. Subsequently, the
attacker used the information to strip Bitcoin owners of their funds.
********** 3 **********
--- page 4 ---
2. P2P file-sharing networks (Gnutella, BitTorrent)-
How: Attacker spins up many fake peers and advertises bogus files or floods the network with false
routing info.
Impact: Poisoned search results, denial of service for honest peers, or prevention of content
discovery.
Why it works: Peer selection is often blind and inexpensive to join.
Q3 a   Explain the key elements of blockchain technology in detail.   [10
.   ]
CO
-   Answer:
1 ;
SO   1.Cryptography
-
2 ;   •   All transactions and blocks in the blockchain are cryptographically safe and sealed on the
network.
BL   • To maintain security, integrity and verification, the blockchain’s mechanism generates two
-2   keys for network members – a public key and a private key.
2.P2P Network
•   Blockchains are peer-to-peer (P2P) networks, a decentralised mechanism to conduct
transactions between members on the chain without the need for a third-party or central
server.
•   Contrary to the regular client/server model where the client makes a request like
executing a transaction, and the server works to fulfill it, on P2P networks each party acts
as both – the client and the server. What this technically means is that every member owns
a copy of the ledger once the network is formed, which can be used to store and share
information without the need for an intermediary.
3. Immutability: Once data is added to the blockchain, it cannot be changed or deleted, which
makes it very secure and trustworthy.
4. Transparency: Every participant can view the history of transactions, ensuring full transparency.
Giving members the power to scrutinize records creates transparency and leaves no room to hide
data. Even in the case of private blockchains where transparency is lower, there is always an
auditable trail of data.
5.Distributed Ledger: Blockchain networks are based on distributed ledger technology. Distributed
ledgers are basically shared databases that maintain a record of all transactions that can be
accessed by all network participants. You could think of it as a shared document that all members
of a team can edit. Blockchains being shared immutable ledgers will not allow you to delete an
entry once recorded.
6.Smart Contracts: A smart contract is a set of rules stored on the blockchain that executes
automatically once the predetermined conditions of the contract have been met. The types of
transactions that can be carried out on the blockchain are agreed between participants through
these ‘smart contracts’, which helps ensure everyone is sticking to the set rules. These contracts
come in handy when businesses need to self-manage contracts in the absence of a third party.
An example could be a logistics company automatically executing a payment once goods are
delivered at the port through a smart contract.
Q3 b Compare Ethereum and Bitcoin with respect to Turing-Completeness based on the following   [10
CO   .   features: main purpose, programming capability, execution environment, loops and conditions, and   ]
-   security approach.
********** 4 **********
--- page 5 ---
3 ;
SO   Answer:
-
2 ;
Feature   Ethereum   Bitcoin
BL
-   Building
1,   decentralized   Mainly used for digital currency
Main Purpose
2   applications   transactions
(DApps)
Supports
complex
Programming Capability   Limited scripting language
programming
logic
Runs on
Execution Environment   Ethereum Virtual   Uses Bitcoin Script
Machine (EVM)
Allows loops,
conditions, and   Loops are restricted to prevent infinite
Loops & Conditions
complex   execution
algorithms
Uses Gas to limit
Security Approach   Uses restricted scripting for security
computation
Q4 a   Explain how smart contracts enforce legal agreements. Illustrate your answer with suitable   [10
CO   .   examples, and discuss the advantages and challenges of legal contract enforcement using smart   ]
-   contracts.
3 ;
SO   Answer:
-
2 ;   1. Agreement Creation – The terms of the legal contract are written into code.
2. Deployment – The smart contract is stored on the blockchain.
BL   3. Condition Monitoring – The contract checks whether conditions are met.
-2   4. Automatic Execution – Once conditions are satisfied, the contract performs the action
automatically.
Examples of Legal Contract Enforcement:
❑ Real Estate Transactions – Ownership transfers automatically after payment.
❑ Insurance Claims – Insurance payout happens automatically when conditions are met.
❑ Supply Chain Agreements – Payment is released when goods are delivered.
❑ Rental Agreements – Digital access to property is granted after rent payment.
Advantages:
✓ Automation – No need for intermediaries.
✓ Transparency – All transactions are recorded on the blockchain.
✓ Security – Data is difficult to alter.
✓ Efficiency – Faster execution compared to traditional legal processes.
Challenges:
********** 5 **********
--- page 6 ---
•   Different countries have different laws regarding smart contracts.
•   Coding errors may cause problems in contract execution.
•   Complex legal language is sometimes difficult to convert into code.
•   Smart contracts cannot easily handle subjective legal decisions.
Q4 b   Explain the concepts of anonymity and pseudo-anonymity in blockchain. Discuss their differences   [10
CO   .   and give suitable examples.   ]
-
3 ;   Answer:
SO
-   1. Anonymity in Blockchain
2 ;   Anonymity means that the real identity of a user is completely hidden, and transactions cannot be
linked back to the individual.
BL
-
1,   •   In a truly anonymous system, no personal information (name, address, IP, etc.) is revealed.
2   •   It is very difficult or nearly impossible to trace the sender or receiver.
•   Special cryptographic techniques are used to hide transaction details.
2. Pseudo-anonymity in Blockchain
Pseudo-anonymity means that users are identified by a pseudonym (like a public key or wallet
address) instead of their real identity.
•   Transactions are publicly visible on the blockchain.
•   Users are not directly identified, but their transaction history can be tracked.
•   If the identity behind a wallet address is discovered, all related transactions can be linked.
Feature   Anonymity   Pseudo-anonymity
Identity Visibility   Completely hidden   Hidden but can be traced
Traceability   Very difficult   Possible through analysis
Transparency   Low   High (public ledger)
Privacy Level   High   Moderate
Linking Transactions   Not easily linkable   Easily linkable via address
Examples   Monero, Zcash   Bitcoin, Ethereum
Q5 a   Explain the phases of blockchain implementation in detail.   [10
CO   .   ]
-   Answer:
3 ;
SO   1. Ideation
-
2 ;
•   Identify the problem or requirement
********** 6 **********
--- page 7 ---
•   Decide if blockchain is really needed
BL
-2
2. Proof of Concept (PoC)
•   Build a small test model
•   Check if the idea works in real life
•   Can be a prototype or MVP
3. Design
•   Plan how the system will work
•   Decide:
•   Architecture
•   Data flow
•   Smart contract logic
4. Development
•   Build the actual application
•   Write smart contracts
•   Create user interface
•   Use platforms like Ethereum or Hyperledger Fabric
5. Testing
•   Check for bugs and errors
•   Test security and performance
6. Deployment
•   Launch the application on blockchain network
• Make it available to users
7. Maintenance
•   Monitor the system
•   Fix issues and bugs
•   Update features over time
Q5 b   Explain how blockchain technology is evolving in the healthcare sector. Discuss its benefits and   [10
CO   .   challenges with examples.   ]
-   Answer:
3 ;   Evolution of Blockchain in Healthcare:
SO
-   1. Secure Medical Records: Blockchain enables the creation of secure, shared patient records that can be
2 ;   accessed by authorized doctors and patients from anywhere, ensuring data integrity.
2. Drug Supply Chain Management: It helps track pharmaceuticals from production to delivery,
BL   preventing counterfeit drugs and ensuring authenticity.
-   3. Clinical Trials and Research: Blockchain ensures data transparency and prevents manipulation of
1,   clinical trial results.
2   4. Insurance and Billing: Smart contracts on blockchain automate insurance claims and reduce fraud in
healthcare payments.
5. COVID-19 and Vaccination Records: Recently, blockchain has been used to store and verify
vaccination data and digital health certificates.
Potential Benefits of Blockchain in Healthcare:
********** 7 **********
--- page 8 ---
1.Data Security and Privacy: Patient data is encrypted and stored across decentralized systems,
reducing the risk of hacking.
2. Transparency: Every transaction or change in data is traceable, which builds trust among patients
and providers.
3. Improved Data Sharing: Authorized stakeholders can easily access medical data, improving
collaboration and patient care.
4. Reduced Fraud: Blockchain minimizes fraudulent activities in drug supply, billing, and insurance.
5. Patient Empowerment: Patients have more control over who accesses their medical data.
Challenges of Implementing Blockchain in Healthcare:
1.High Implementation Cost: Setting up blockchain systems requires significant investment in
infrastructure and training.
2. Scalability Issues: Large volumes of medical data can slow down blockchain performance.
3. Lack of Standardization: Different hospitals and regions use different systems, making integration
difficult.
4. Regulatory and Legal Challenges: Lack of clear government policies on blockchain use in healthcare.
Q6 a   Explain different types of Blockchain: Public, Private, and Consortium with examples.   [10
CO   .   ]
-   Answer: Public Blockchain
1 ;
SO   These blockchains are completely open to following the idea of decentralization. They don't have
-   any restrictions, anyone having a computer and internet can participate in the network.
2 ;
BL   4. As the name is public this blockchain is open to the public, which means it is not owned by
-2   anyone.
5. Anyone having internet and a computer with good hardware can participate in this public
blockchain.
6.   All the computers in the network hold the copy of other nodes or blocks present in the
network
7. In this public blockchain, we can also perform verification of transactions or records.
Advantages:
8. High transparency
9. Very secure (many participants validate data)
Disadvantages:
10. Slower transactions
11. Requires a lot of computing power
Examples: Bitcoin, Ethereum.
Private Blockchain: These blockchains are not as decentralized as the public blockchain only
selected nodes can participate in the process, making it more secure than the others.
12. These are not as open as a public blockchain.
13. They are open to some authorized users only.
14. These blockchains are operated in a closed network.
15. In this few people are allowed to participate in a network within a company/organization.
Advantages:
•   Faster transactions
• More privacy
Disadvantages:
•   Less decentralized (single authority can change rules)
********** 8 **********
--- page 9 ---
•   Requires trust in the central authority
Examples: Walmart uses it to track food products from farms to stores.
Consortium Blockchain: It is a creative approach that solves the needs of the organization. This
blockchain validates the transaction and also initiates or receives transactions.
This type of blockchain network controlled by a group of pre-selected organizations rather than a
single entity or the public.
It offers a middle ground between the transparency of public blockchains and the control of
private blockchains.
1. Also known as Federated Blockchain.
2. This is an innovative method to solve the organization's needs.
3. Some part is public and some part is private.
4. In this type, more than one organization manages the blockchain.
Advantages:
•   Shared control (more trust than private)
•   More efficient than public
Disadvantages:
•   More complex to set up and manage
•   Less transparent than public blockchains
Examples: Consortium of international banks and trading companies
Q6 b   Describe different types of blockchain oracles and their working mechanisms.   [10
CO   .   ]
-   Answer:
2 ;
SO   1. Data Oracles
-   Data oracles transfer information between the blockchain and external systems such as bank
2 ;   systems, payment networks, websites, or cloud services. They allow smart contracts to receive
real-world data and send instructions to external systems.
BL
-
1,   2. Cross-Chain Oracles
2   Cross-chain oracles allow different blockchains to communicate and share data or tokens with each
other. This helps in transferring assets or information between different blockchain networks.
3. Compute Oracles
Compute oracles perform complex calculations outside the blockchain and send the verified results
back to the smart contract. This helps when the computation is too expensive or difficult to
perform directly on the blockchain.
working mechanisms:
1. Push-Based Oracle
In this mechanism, the oracle automatically sends (pushes) data to the blockchain at regular
intervals.
Smart contracts can then use this already available data when needed.
********** 9 **********
--- page 10 ---
•   Example:
A cryptocurrency price oracle updates the price on the blockchain every few minutes.
2. Pull-Based Oracle
In this mechanism, the smart contract requests (pulls) data from the oracle only when it is needed.
The oracle then fetches the data and sends it to the blockchain.
•   Example:
A smart contract requests the latest stock price when a trade needs to be executed.
Q7 a   Explain the concept of Proof of Work (PoW) and Proof of Stake (PoS) with suitable example. Compare [10
CO   .   their advantages and disadvantages.   ]
-
2 ;   Answer:
SO
-   Proof of Work (PoW): It is used in famous cryptocurrency called bitcoin.
2 ;
BL   ▪   It requires network participants to spend time-solving an unpredictable mathematical
-2   puzzle in order to prevent the system from being hacked.
▪   In cryptocurrency mining proof of work is commonly employed to validate transactions
and mine new tokens.
Example: Bitcoin (BTC): Miners use powerful hardware (ASICs) to solve cryptographic puzzles and
earn BTC rewards.
Advantages of PoW:
•   Highly secure and proven mechanism
•   Prevents double-spending
•   Decentralized (anyone with hardware can participate)
Disadvantages of PoW:
•   Very high energy consumption
•   Requires expensive hardware
•   Slower transaction processing
•   Environmental concerns
Proof of Stake (PoS): It is a system where users lock their coins to become validators.
▪   Validators are randomly chosen to verify transactions and add blocks.
▪   It uses less energy than Proof of Work because it depends on staking coins, not powerful
computers.
Example: Ethereum , Solana, Cardano
Advantages of PoS:
•   Energy efficient
•   Faster transaction processing
• Lower hardware requirements
• More environmentally friendly
********** 10 **********
--- page 11 ---
Disadvantages of PoS:
•   Wealth concentration (rich get richer)
•   Less proven compared to PoW
•   Potential security concerns (e.g., nothing-at-stake problem)
Q7 b   Explain the difference between IPFS and BigchainDB.   [10
CO   .   ]
-   Answer:
3 ;
SO
-   Feature   IPFS   BigchainDB
2 ;
BL   Type   Decentralized file storage system Blockchain-based database
-2
Store and manage
Purpose   Store and share files
structured data/assets
Uses content-based addressing   Uses database +
Working Method
(hash)   blockchain technology
Files (images, videos,   Structured data (records,
Data Type
documents)   transactions)
Speed   Fast file retrieval   High transaction speed
Highly scalable database
Scalability   Good for file distribution
system
Files are content-addressed   Data is fully immutable
Immutability
(hard to change)   like blockchain
Limited (not for complex   Supports rich queries like
Query Support
queries)   databases
Distributed but database-
Decentralization   Fully peer-to-peer network
oriented
File sharing, media storage,   Asset management, supply
Use Cases
decentralized web   chain, data systems
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 9b0a2fd9d294

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION IN
TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (Comp)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Work (PoW) and Proof of
Stake (PoS)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Work   Proof of Stake
1   Miners don’t need to hold any of the Requires validators
blockchain’s assets, and only need   to hold some of the
computing power to validate a   blockchain’s token or
transaction.   cryptocurrency.
2   May use a very significant amount   Doesn’t require
of electricity.   significant computing
power for transaction
CO-1 ;
validation.
SO-1,2 ;
3   Proof of work has a longer proven   It’s a newer approach
BL-3
history of use as a blockchain   than proof of work,
consensus mechanism.   with less adoption as
a consensus
mechanism.
4   Cryptos using proof of work are   Cryptos that use
often excluded from ESG portfolios   proof of stake might
because of the energy demands.   be more attractive for
an ESG portfolio
because 5of the lower
environmental
impact.
5   Used in Bitcoin   Used in Ethereum
b.   Explain the term contractual confidentiality? Identify the solutions to
CO-2 ;
achieve confidentiality.
SO-1,2 ;
Solution:
BL-2
<Definition – 2M, Solutions – 3M>
********** 1 **********
--- page 2 ---
While transparency is beneficial, certain futures contract details must
remain confidential to prevent front-running, strategy leakage, or
commercial espionage. The Challenges are -
1. Blockchain is a public ledger → default state is transparent.
2. Traders may not want asset quantity, strike price, or leverage
exposed.
Solutions –
1. Zero-Knowledge Proofs (zk-SNARKs / zk-STARKs)-Prove that
contract conditions are met without revealing sensitive values.
Example: Verify settlement eligibility without showing
exact strike price.
2. Confidential Transactions-Use cryptographic commitments
(Pedersen commitments) to hide amounts but allow verification.
3. Permissioned Blockchains-Access restricted to authorized
entities (Hyperledger Fabric, Quorum).
4. Off-Chain Storage with On-Chain Hashes-Sensitive contract
terms stored securely off-chain; only the hash is on-chain for
integrity checks.
5. Data Encryption on Chain-Store encrypted fields in the contract;
keys shared only between counterparties.
c.   Differentiate between Bitcoin Scripting and Ethereum Smart Contracts.
Solution: Any five valid points- 5 marks
Bitcoin   Ethereum
Generation 1   blockchain   Generation 1 blockchain(2015)
(2009)
Programming   lang   used: Programming lang used: Solidity
Scripts   is used Ethereum
Consensus alg: PoW   PoS
CO-2 ;
SO-1,2 ;   Scalability: 3-7 transactions   Eht- 30-50 trans per sec
BL-4   per sec
Block size: 1 mb in Bitcoin   0.1 mb in Ethereum
Only   cryptocurrency   Real life solutions are supported
applications are supported in   in Ethereum
Bitcoin
Bitcoin   limiting   the Etherum has more functionality
functionality to increase the
security
d.   Explain the key features of the InterPlanetary File System (IPFS) that
CO-3 ;   differentiate it from traditional HTTP-based systems?
SO-1,2 ;   Solution:
BL-3   • The InterPlanetary File System (IPFS) is a distributed storage
protocol developed by Protocol Labs for uploading, storing, and
********** 2 **********
--- page 3 ---
accessing data, files, websites, and applications in a decentralized
manner.
• Unlike traditional HTTP-based systems, which use location-based
addressing (such as URLs), IPFS uses content-based addressing.
In this system, each file is assigned a unique Content Identifier
(CID) generated through cryptographic hashing. This ensures that
the content can be retrieved from any node that stores it,
regardless of its physical location.
• IPFS operates on a peer-to-peer (P2P) network, where users share
and host portions of data. This decentralized approach enhances
data availability, reduces dependency on centralized servers, and
improves fault tolerance.
• Additionally, IPFS uses IPLD Merkle Directed Acyclic Graphs
(DAGs) to link pieces of content together. This structure ensures
data integrity, supports efficient versioning, and allows for
deduplication of data.
• IPFS offers a more secure, efficient, and resilient alternative to
traditional web protocols by leveraging content addressing and
decentralized storage.
a.   Explain the role of consensus algorithms in blockchain technology and
illustrate the working process of a consensus algorithm with a neat
diagram.
Solution:
Role 3 marks, working process explanation 5 m and diagram 2marks
The role of consensus is an attaining agreement common state or value
among multiple nodes despite the failure of some nodes. A consensus
mechanism is a set of steps that are taken by most or all nodes in a
blockchain to agree on a proposed state or value. Further, various
Q2   requirements must be met to provide the desired results in a consensus
CO-2;   mechanism.   [10]
SO-1,2;   The following describes these requirements:
BL-3   • Agreement: All honest nodes decide on the same value
• Termination: All honest nodes terminate execution of the consensus
process and eventually reach a decision.
• Validity: The value agreed upon by all honest nodes must be the same
as the initial value proposed by at least one honest node
• Fault-tolerant: The consensus algorithm should be able to run in the
presence of faulty or malicious nodes (Byzantine nodes)
• Integrity: This is a requirement that no node can make the decision
more than once in a single consensus cycle
********** 3 **********
--- page 4 ---
Working process
Transaction Verification: Nodes validate digital signatures and confirm
sufficient sender balance.
Miner or Validator Selection: Miners compete solving cryptographic
puzzles using Proof of Work.
Block Verification & Validation: Network nodes verify block hash,
structure, and transaction integrity.
Updating Blockchain: Verified block is appended to distributed ledger
across all nodes.
Incentive Miner or Validator: Successful miner rewarded with new
bitcoins and transaction fees.
b.   Define blockchain. Explain the main features of Blockchain.
Solution
Definition- 2 marks
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
Explain features- 8 marks.
Peer-to-peer- This means that there is no central controller in the
network, and all participants talk to each other directly. This property
allows for cash transactions to be exchanged directly among the peers
without a third-party involvement, such as by a bank.
Distributed ledger- which simply means that a ledger is spread across
CO-1;
the network among all peers in the network, and each peer holds a copy
SO-1,2;   [10]
of the complete ledger.
BL-3
Cryptographically-secure- which means that cryptography has been
used to provide security services which make this ledger secure against
tampering and misuse. These services include non-repudiation, data
integrity, and data origin authentication.
Append-only, which means that data can only be added to the
blockchain in time-ordered sequential order
Updateable only via consensus- This is what gives it the power of
decentralization. In this scenario, no central authority is in control of
updating the ledger. Instead, any update made to the blockchain is
validated against strict criteria defined by the blockchain protocol and
added to the blockchain only after a consensus has been reached among
all participating peers/nodes on the network.
********** 4 **********
--- page 5 ---
a.   Draw and explain block structure in Blockchain.
Solution
Diagram- 4 marks
Q3
CO-1;
[10]
SO-1,2;
BL-3
Explain- 6 marks
attributes of a block: the block header, which is composed of pointer to
previous block, the timestamp, nonce, Merkle root, and the block body
that contains transactions.
A nonce is a number that is generated and used only once. A nonce is
used extensively in many cryptographic operations to provide replay
protection, authentication, and encryption. In blockchain, it's used in
PoW consensus algorithms and for transaction replay protection.
Merkle root is a hash of all of the nodes of a Merkle tree. Merkle trees
are widely used to validate the large data structures securely and
efficiently.
b.   Explain Ethereum accounts and their types in detail.
Solution:
Accounts are one of the main building blocks of the Ethereum
blockchain. The state is created or updated as a result of the interaction
between accounts. Operations performed between and on the accounts
represent state transitions. State transition is achieved using what's
called the Ethereum state transition function, which works as follows:
1. Confirm the transaction validity by checking the syntax, signature
CO-2;
validity, and nonce.
SO-1,2;   [10]
2. Transaction fee is calculated and the sending address is resolved
BL-3
using the signature. Furthermore, sender's account balance is checked
and subtracted accordingly and nonce is incremented. An error is
returned if the account balance is not enough.
3. Provide enough ether (gas price) to cover the cost of the transaction.
This is charged per byte incrementally according to the size of the
transaction.
4. In this step, the actual transfer of value occurs. The flow is from the
sender's account to receiver's account. The account is created
********** 5 **********

[Text in pictures on this page, read by OCR]
POINTER TO PREVIOUS BLOCK’S HASH
NONCE

TIME STAMP
MERKLE ROOT

LIST OF TRANSACTIONS

The generic structure of a block.
--- page 6 ---
automatically if the destination account specified in the transaction does
not exist yet. Moreover, if the destination account is a contract, then the
contract code is executed. This also depends on the amount of gas
available. If enough gas is available, then the contract code will be
executed fully; otherwise, it will run up to the point where it runs out of
gas.
5. In cases of transaction failure due to insufficient account balance or
gas, all state changes are rolled back with the exception of fee payment,
which is paid to the miners.
6. Finally, the remainder (if any) of the fee is sent back to the sender as
change and fee is paid to the miners accordingly. At this point, the
function returns the resulting state.
There are two types of accounts in Ethereum:
Externally owned accounts
Contract accounts
The first is externally owned accounts (EOAs) and the other is contract
accounts. EOAs are similar to accounts that are controlled by a private
key in bitcoin. Contract accounts are the accounts that have code
associated with them along with the private key. An EOA has ether
balance, is able to send transactions, and has no associated code,
whereas a Contract Account (CA) has ether balance, associated code,
and the ability to get triggered and execute code in response to a
transaction or a message. It is worth noting that due to the Turing-
completeness property of the Ethereum blockchain, the code within
contract accounts can be of any level of complexity. The code is
executed by EVM by each mining node on the Ethereum network. In
addition, contract accounts are able to maintain their own permanent
state and can call other contracts. It is envisaged that in the serenity
release, the distinction between externally owned accounts and contract
accounts may be eliminated.
a.   Explain pseudo-anonymity and anonymity in blockchain systems and
differentiate. Illustrate your answer with appropriate examples?
Solution:
Explain with example- 6 marks
Q4   Differentiate- 4 marks
CO-2;   Anonymity means that the identity of a person is unknown and its
[10]
SO-1,2;   actions are not trackable. Pseudonymity, however, is a much weaker
BL-3   form. It means that a person’s identity is unknown, but it is possible to
assign actions to the same person.
The first figure shows a situation where the person’s identity is
unknown. But all the actions the person made can be linked to this
person.
********** 6 **********
--- page 7 ---
The second figure shows a situation where a person’s identity is
unknown and it is impossible to link any transaction to a specific
person.
Blockchains like Bitcoin or Ethereum are pseudonymous instead of
anonymous. The address is a pseudonym for the person holding the
corresponding private key.
Every action done with this address can be traced back to this person,
although its identity might be unknown. And since all transactions are
stored in the blockchain, it is possible for everybody to trace them back,
even though this transaction lies long in the past.
There are so-called privacy coins like Monero or ZCash that allow for
real anonymity through cryptography. Here, transactions cannot be
linked to individual addresses.
b.   Explain the key steps involved in implementing blockchain technology.
Solution:
Implementing blockchain technology involves a series of well-defined
steps to ensure successful deployment and integration. The key steps are:
1. Conduct a Feasibility Study
• Assess whether blockchain is suitable for the business case.
• Analyze technical and economic viability (usually 2–4 weeks).
CO-3;
SO-1,2;   [10]
2. Create a Business Case
BL-3
• Document functional and non-functional requirements.
•   Identify risks, including regulatory compliance.
3. Conceptualize the Blockchain
• Decide on:
o Blockchain type: Public, private, or hybrid.
o Consensus mechanism: Proof of Stake, Proof of
Authority, etc.
********** 7 **********
--- page 8 ---
o Implementation approach: Build from scratch or fork an
existing protocol.
4. Scope the Project
• Define objectives, deliverables, and boundaries.
• Assign roles, estimate budget, timeline, and resources.
• Assess risks and compliance needs.
5. Design the Blockchain Solution
• Prepare feature list and prioritize based on cost-benefit analysis.
• Design UX/UI for user applications (web, mobile, desktop).
•   Include cybersecurity features.
6. Select the Tech Stack
• Choose appropriate tools, frameworks, and platforms.
• Compare options based on scalability and business needs.
7. Develop and Deploy the Solution
• Develop:
o Blockchain network (from scratch or modified protocol).
o Smart contracts for automation.
o Oracles for external data integration.
o User-facing apps and backend APIs.
• Perform QA testing and deploy to production with backup and
recovery setup.
8. Integrate with Existing Systems
• Ensure smooth integration with enterprise systems and enable
interoperability.
9. Provide After-Launch Support
• Monitor performance, fix bugs, and maintain uptime.
• Apply security patches and updates.
• Offer user support and training.
10. Continuously Evolve the Solution
• Update smart contracts, improve scalability, and enhance security.
• Add new features based on user feedback and regulatory changes.
a.   Explain working of mining algorithm in Proof of Work (PoW).
Solution:
The mining algorithm in Proof of Work (PoW) algorithm consists of the
following steps.
1. The previous block's header is retrieved from the bitcoin
network.
Q5
2. Assemble a set of transactions broadcasted on the network into
CO-2;
a block to be proposed.   [10]
SO-1,2;
3. Compute the double hash of the previous block's header
BL-3
combined with a nonce and the newly proposed block using the
SHA-256 algorithm.
4. Check if the resultant hash is lower than the current difficulty
level (target) then PoW is solved. As a result of successful PoW
the discovered block is broadcasted to the network and miners
fetch the reward.
********** 8 **********
--- page 9 ---
5. If the resultant hash is not less than the current difficulty level
(target), then repeat the process after incrementing the nonce.
This process can be visualized by using the following flowchart:
b.   What are smart contracts? Discuss different ways to deploy smart
contracts on the blockchain network.
Solution:
<Definition 2M, Different ways 8M>
A smart contract is a secure and unstoppable computer program
representing an agreement that   is automatically executable and
enforceable. It is a computer program that is written in a language that a
computer or target machine can understand. It encompasses agreements
between parties in the form of business logic.
<any 4 out of 5 ways>
1. Direct Deployment via Wallets and Blockchain Explorers – Write
CO-2;   compile and deploy directly from crypto wallet
SO-1,2;   2. Development Frameworks and Toolkits – Use Hardhat, Remix, [10]
BL-3   Truffle etc.
3. Cloud & Blockchain Platform Integration- Cloud-hosted endpoints
allow deployment via API or framework scripts without running a full
blockchain node.
4. Programmatic and Scripting Approaches - Write deployment scripts
(JS, Python, etc.) to automate deployments, especially for complex
upgradeable/proxy   patterns, batch deployments, and CI/CD
integration
5. On-Chain/Off-Chain Hybrid and Multi-Chain Deployment - Deploy
the same contract logic across different blockchains, sometimes via
platform tools or by configuring deployment scripts for multi-
network support.
********** 9 **********
--- page 10 ---
a.   Explain different types of blockchains in detail with use-case examples
for each type?
Solution:
Four types with example- 2.5 marks *4=10 marks
Blockchains can be broadly categorized into four main types Public,
Private, Consortium (Federated), and Hybrid blockchains. Each type
differs in its level of decentralization, access control, and use-case
suitability. Below is a detailed summary of each type along with
practical examples.
1. Public Blockchain
A public blockchain is a completely open and decentralized network
where anyone can join, participate in the consensus process, and verify
transactions. It operates on a permissionless model, meaning there is no
restriction on who can read or write to the network. Public blockchains
are secured through consensus mechanisms such as Proof of Work
(PoW) or Proof of Stake (PoS).
Use-case Example:
Bitcoin (BTC): The first and most prominent public blockchain, used
for peer-to-peer digital currency transactions without any intermediary.
Ethereum (ETH): A public blockchain enabling smart contracts and
decentralized applications (DApps) in finance (DeFi), NFTs, and
gaming sectors.
Advantages: Transparency, immutability, and high security.
Limitations: Slower transaction speed and high energy consumption in
Q6   some consensus mechanisms.
CO-1;   2. Private Blockchain
[10]
SO-1,2;   A private blockchain is a permissioned network controlled by a single
BL-3   organization or authority. Only authorized participants can access,
validate, and audit the blockchain. While it lacks the full
decentralization of public blockchains, it provides better privacy,
control, and efficiency.
Use-case Example:
Hyperledger Fabric (by IBM): Used by enterprises for supply chain
management, trade finance, and asset tracking. For instance, Walmart
uses Hyperledger Fabric to trace food products from farm to shelf for
enhanced food safety.
Advantages: High transaction throughput, strong privacy, and
controlled participation.
Limitations: Reduced decentralization and possible single point of
failure.
3. Consortium (Federated) Blockchain
A consortium blockchain (or federated blockchain) is a semi-
decentralized system managed by a group of pre-selected organizations
instead of a single entity. It combines the benefits of both public
transparency and private control. Each member organization operates
one or more nodes, and decisions are made collectively.
Advantages: Improved scalability, better governance, and trust among
known parties.
Limitations: Requires coordination between organizations and limited
public transparency.
********** 10 **********
--- page 11 ---
4. Hybrid Blockchain
A hybrid blockchain combines features of both public and private
blockchains. It allows organizations to keep certain data private while
enabling limited public access to ensure transparency and verifiability.
Hybrid models are ideal where data sensitivity and public accountability
must coexist.
Advantages: Flexible design, customizable transparency, and controlled
data exposure.
Limitations: Complex architecture and partial reliance on centralized
entities.
b.   Explain following elements of Ethereum Blockchain:
•   Ether cryptocurrency/tokens
• Addresses
•   Transactions
• The EVM
Solution: Explanation of each element – 2 marks *5=10 marks
• Cryptocurrency: As an incentive to the miners, Ethereum
rewards its own native currency, called ether (abbreviated as
ETH).
• Keys and addresses: Keys and addresses are used in the
Ethereum blockchain to represent ownership and transfer ether.
The keys used are made up of pairs of private and public parts.
The private key is generated randomly and is kept secret,
whereas the public key is derived from the private key.
CO-2;
Addresses are derived from public keys and are 20-byte codes
SO-1,2;   [10]
used to identify accounts.
BL-3
Address: x71C7656EC7ab88b098defB751B7401B5f6d8976F.
• Transaction in Ethereum is a digitally signed (using a private
key) data packet that contains the instructions that, when
completed, either result in a message call or contract creation.
Transactions are constructed by an actor external to the
Ethereum blockchain or some external software tool.
Smart contracts cannot send a transaction
• EVM is a simple stack-based execution machine that runs
bytecode instructions to transform the system state from one
state to another.
The EVM is a Turing-complete machine but is limited by the
amount of gas that is required to run any instruction.
a.   What do you mean by 51% attack. How does a 51% Attack Work.
Briefly explain the risks and consequences Of A 51% Attack in detail.
Solution:
What do you mean by 51% attack- 2 marks
Q7
How does a 51% Attack Work- 5 marks
CO-3;
Briefly explain the risks and consequences Of A 51% Attack in detail- 3 [10]
SO-1,2;
marks
BL-3
A 51% attack is an attack on a blockchain network where a single entity
gains control of more than half (51%) of its staking or computational
power.
********** 11 **********
--- page 12 ---
This disproportionate control allows them to implement substantial
changes, contravening the decentralization principle fundamental to the
blockchain. In other words, a 51% attack gives the power to rewrite tx
history, prevent tx completion, stop rewards to validators, and double
spend.
It's important to note that a 51% attack is among the most significant
security threats to blockchains, particularly those utilizing Proof-of-
Work and Delegated Proof-of-Stake consensus algorithms. One
alarming outcome of such an attack is a double-spending, where the
same coins are spent more than once, damaging the trust and reliability
of the blockchain.
How Does A 51% Attack Work
Diving deeper into the mechanics of a 51% attack, let's explore the step-
by-step process an attacker follows to gain and exploit control over a
blockchain network. While the exact specifics of an attack can vary
depending on several factors, here’s a simplified, general sequence of
events that typically characterizes such an attack:
Accumulate Power: The first step involves the attacker accumulating
more than half (51%) of the network's computational or hashing power.
This could be accomplished by acquiring substantial hardware resources
or convincing a large number of miners to join a pool under the attacker's
control.
Partitioning: The attacker, now commanding a majority of the network's
hashing power, effectively segregates their group from the main network
while still maintaining internal communication. Despite this separation,
the hacking group proceeds with mining operations but refrains from
sharing their progress with the primary network or receiving updates
from it. Consequently, two parallel versions of the blockchain start
evolving independently.
Fast-Paced Mining: Due to their superior hashing power, the attacker's
group is able to add blocks to their version of the blockchain faster than
the rest of the network. Over time, the difference in length between the
two versions of the chain becomes statistically proportional to the
difference in hashing power between the two groups.
Reintegration and Dominance: Once the hacking group rejoins the
network, the two competing versions of the blockchain propagate through
the entire network. According to the consensus protocol's rules, the nodes
keep the longest blockchain, and the shorter one is discarded.
Potential Threats: Upon successful execution, a 51% attack can open
Pandora's box of threats that can significantly impact a blockchain
network and its participants. These threats range from financial fraud in
the form of double-spending to outright denial of service attacks that
paralyze network functionality.
Risks And Consequences Of A 51% Attack
A successful attack can have significant implications for a blockchain
network and its users. Here's what happens:
Double-Spending: This is the most feared consequence. The attacker
could spend their money twice first, they perform a regular transaction
and then change the blockchain to show they never used the money at all.
Denial-of-Service (DoS) Attack: The hacker takes over and blocks the
addresses of other miners for a while. This stops the good guys - the
honest miners - from getting back control of the network. As a result, the
attacker's false chain of transactions can become permanent.
********** 12 **********
--- page 13 ---
Transaction Reversal: The attacker can block payments between some or
all users. This disrupts the normal operation of the network and can lead
to significant delays in transaction confirmations, undermining
confidence in the network's reliability.
Damage to Reputation: Also, the attack can severely damage a
blockchain's reputation. This can lead to a loss of trust among current and
potential users, resulting in a significant drop in the value of the
associated cryptocurrency and deterring new users or investors from
joining the network.
b.   Discuss in detail the key challenges faced by the education sector and
explain how Blockchain Technology provides effective solutions to
overcome these challenges.
Solution:
The education sector plays a vital role in the development of industries
such as medicine, agriculture, science, and technology. However,
managing educational institutions—from pre-kindergarten to PhD
level—is a complex task. The sector faces several major challenges:
Challenges in the Education Sector:
1. Record Maintenance:
Every year, billions of students enroll in various institutions.
Maintaining their personal and academic records in paper format
is a huge task. Retrieving data of students who graduated 4–5
years ago becomes time-consuming and inefficient.
2. Certificate Security:
Storing student certificates securely is difficult. Paper-based
certificates are prone to damage, loss, and falsification. Ensuring
their authenticity requires manpower and resources.
3. Accounting and Finance Management:
Educational institutions need to manage finances such as staff
CO-3;   salaries, student fees, maintenance, and operational costs. This
SO-1,2;   process is labor-intensive and requires accurate calculations.   [10]
BL-3   4. Scholarship Monitoring:
With a growing number of students and scholarship programs,
tracking and managing scholarships has become increasingly
difficult.
These challenges affect the overall performance and efficiency of the
education system.
Role of Blockchain Technology in Overcoming Challenges:
Blockchain Technology offers innovative solutions to address these
issues:
1. Digital Record Keeping:
Blockchain replaces paper documents with secure digital
records. Student and staff data can be stored in a decentralized
ledger, making it easy to access and verify without the risk of
tampering or loss.
2. Cost and Effort Saving:
By eliminating the need for physical documents, blockchain
reduces costs related to paper, printing, and manpower. It also
saves time spent on manual record maintenance.
3. Transparency and Security:
Blockchain provides a transparent and tamper-proof system for
storing student records. Since it is decentralized, ownership and
********** 13 **********
--- page 14 ---
access are distributed among authorized individuals, ensuring
data integrity.
4. Simplified Financial Processes:
Blockchain simplifies accounting tasks such as calculating staff
salaries and student scholarships. Some institutions even accept
cryptocurrencies like Bitcoin for fee payments, making
transactions faster and more transparent.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 99536d71b8ce

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Work (PoW) and Proof of
Stake (PoS)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Work   Proof of Stake
1   Miners don’t need to hold any of the Requires validators
blockchain’s assets, and only need   to hold some of the
computing power to validate a   blockchain’s token or
transaction.   cryptocurrency.
2   May use a very significant amount   Doesn’t require
of electricity.   significant computing
power for transaction
CO-1 ;
validation.
SO-1,2 ;
3   Proof of work has a longer proven   It’s a newer approach
BL-3
history of use as a blockchain   than proof of work,
consensus mechanism.   with less adoption as
a consensus
mechanism.
4   Cryptos using proof of work are   Cryptos that use
often excluded from ESG portfolios   proof of stake might
because of the energy demands.   be more attractive for
an ESG portfolio
because 5of the lower
environmental
impact.
5   Used in Bitcoin   Used in Ethereum
b.   Explain the term contractual confidentiality? Identify the solutions to
CO-2 ;
achieve confidentiality.
SO-1,2 ;
Solution:
BL-2
<Definition – 2M, Solutions – 3M>
********** 1 **********
--- page 2 ---
While transparency is beneficial, certain futures contract details must
remain confidential to prevent front-running, strategy leakage, or
commercial espionage. The Challenges are -
1. Blockchain is a public ledger → default state is transparent.
2. Traders may not want asset quantity, strike price, or leverage
exposed.
Solutions –
1. Zero-Knowledge Proofs (zk-SNARKs / zk-STARKs)-Prove that
contract conditions are met without revealing sensitive values.
Example: Verify settlement eligibility without showing
exact strike price.
2. Confidential Transactions-Use cryptographic commitments
(Pedersen commitments) to hide amounts but allow verification.
3. Permissioned Blockchains-Access restricted to authorized
entities (Hyperledger Fabric, Quorum).
4. Off-Chain Storage with On-Chain Hashes-Sensitive contract
terms stored securely off-chain; only the hash is on-chain for
integrity checks.
5. Data Encryption on Chain-Store encrypted fields in the contract;
keys shared only between counterparties.
c.   Differentiate between Bitcoin Scripting and Ethereum Smart Contracts.
Solution: Any five valid points- 5 marks
Bitcoin   Ethereum
Generation 1   blockchain   Generation 1 blockchain(2015)
(2009)
Programming   lang   used: Programming lang used: Solidity
Scripts   is used Ethereum
Consensus alg: PoW   PoS
CO-2 ;
SO-1,2 ;   Scalability: 3-7 transactions   Eht- 30-50 trans per sec
BL-4   per sec
Block size: 1 mb in Bitcoin   0.1 mb in Ethereum
Only   cryptocurrency   Real life solutions are supported
applications are supported in   in Ethereum
Bitcoin
Bitcoin   limiting   the Etherum has more functionality
functionality to increase the
security
d.   Explain the key features of the InterPlanetary File System (IPFS) that
CO-3 ;   differentiate it from traditional HTTP-based systems?
SO-1,2 ;   Solution:
BL-3   • The InterPlanetary File System (IPFS) is a distributed storage
protocol developed by Protocol Labs for uploading, storing, and
********** 2 **********
--- page 3 ---
accessing data, files, websites, and applications in a decentralized
manner.
• Unlike traditional HTTP-based systems, which use location-based
addressing (such as URLs), IPFS uses content-based addressing.
In this system, each file is assigned a unique Content Identifier
(CID) generated through cryptographic hashing. This ensures that
the content can be retrieved from any node that stores it,
regardless of its physical location.
• IPFS operates on a peer-to-peer (P2P) network, where users share
and host portions of data. This decentralized approach enhances
data availability, reduces dependency on centralized servers, and
improves fault tolerance.
• Additionally, IPFS uses IPLD Merkle Directed Acyclic Graphs
(DAGs) to link pieces of content together. This structure ensures
data integrity, supports efficient versioning, and allows for
deduplication of data.
• IPFS offers a more secure, efficient, and resilient alternative to
traditional web protocols by leveraging content addressing and
decentralized storage.
a.   Explain the role of consensus algorithms in blockchain technology and
illustrate the working process of a consensus algorithm with a neat
diagram.
Solution:
Role 3 marks, working process explanation 5 m and diagram 2marks
The role of consensus is an attaining agreement common state or value
among multiple nodes despite the failure of some nodes. A consensus
mechanism is a set of steps that are taken by most or all nodes in a
blockchain to agree on a proposed state or value. Further, various
Q2   requirements must be met to provide the desired results in a consensus
CO-2;   mechanism.   [10]
SO-1,2;   The following describes these requirements:
BL-3   • Agreement: All honest nodes decide on the same value
• Termination: All honest nodes terminate execution of the consensus
process and eventually reach a decision.
• Validity: The value agreed upon by all honest nodes must be the same
as the initial value proposed by at least one honest node
• Fault-tolerant: The consensus algorithm should be able to run in the
presence of faulty or malicious nodes (Byzantine nodes)
• Integrity: This is a requirement that no node can make the decision
more than once in a single consensus cycle
********** 3 **********
--- page 4 ---
Working process
Transaction Verification: Nodes validate digital signatures and confirm
sufficient sender balance.
Miner or Validator Selection: Miners compete solving cryptographic
puzzles using Proof of Work.
Block Verification & Validation: Network nodes verify block hash,
structure, and transaction integrity.
Updating Blockchain: Verified block is appended to distributed ledger
across all nodes.
Incentive Miner or Validator: Successful miner rewarded with new
bitcoins and transaction fees.
b.   Define blockchain. Explain the main features of Blockchain.
Solution
Definition- 2 marks
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
Explain features- 8 marks.
Peer-to-peer- This means that there is no central controller in the
network, and all participants talk to each other directly. This property
allows for cash transactions to be exchanged directly among the peers
without a third-party involvement, such as by a bank.
Distributed ledger- which simply means that a ledger is spread across
CO-1;
the network among all peers in the network, and each peer holds a copy
SO-1,2;   [10]
of the complete ledger.
BL-3
Cryptographically-secure- which means that cryptography has been
used to provide security services which make this ledger secure against
tampering and misuse. These services include non-repudiation, data
integrity, and data origin authentication.
Append-only, which means that data can only be added to the
blockchain in time-ordered sequential order
Updateable only via consensus- This is what gives it the power of
decentralization. In this scenario, no central authority is in control of
updating the ledger. Instead, any update made to the blockchain is
validated against strict criteria defined by the blockchain protocol and
added to the blockchain only after a consensus has been reached among
all participating peers/nodes on the network.
********** 4 **********
--- page 5 ---
a.   Draw and explain block structure in Blockchain.
Solution
Diagram- 4 marks
Q3
CO-1;
[10]
SO-1,2;
BL-3
Explain- 6 marks
attributes of a block: the block header, which is composed of pointer to
previous block, the timestamp, nonce, Merkle root, and the block body
that contains transactions.
A nonce is a number that is generated and used only once. A nonce is
used extensively in many cryptographic operations to provide replay
protection, authentication, and encryption. In blockchain, it's used in
PoW consensus algorithms and for transaction replay protection.
Merkle root is a hash of all of the nodes of a Merkle tree. Merkle trees
are widely used to validate the large data structures securely and
efficiently.
b.   Explain Ethereum accounts and their types in detail.
Solution:
Accounts are one of the main building blocks of the Ethereum
blockchain. The state is created or updated as a result of the interaction
between accounts. Operations performed between and on the accounts
represent state transitions. State transition is achieved using what's
called the Ethereum state transition function, which works as follows:
1. Confirm the transaction validity by checking the syntax, signature
CO-2;
validity, and nonce.
SO-1,2;   [10]
2. Transaction fee is calculated and the sending address is resolved
BL-3
using the signature. Furthermore, sender's account balance is checked
and subtracted accordingly and nonce is incremented. An error is
returned if the account balance is not enough.
3. Provide enough ether (gas price) to cover the cost of the transaction.
This is charged per byte incrementally according to the size of the
transaction.
4. In this step, the actual transfer of value occurs. The flow is from the
sender's account to receiver's account. The account is created
********** 5 **********

[Text in pictures on this page, read by OCR]
POINTER TO PREVIOUS BLOCK’S HASH
NONCE

TIME STAMP
MERKLE ROOT

LIST OF TRANSACTIONS

The generic structure of a block.
--- page 6 ---
automatically if the destination account specified in the transaction does
not exist yet. Moreover, if the destination account is a contract, then the
contract code is executed. This also depends on the amount of gas
available. If enough gas is available, then the contract code will be
executed fully; otherwise, it will run up to the point where it runs out of
gas.
5. In cases of transaction failure due to insufficient account balance or
gas, all state changes are rolled back with the exception of fee payment,
which is paid to the miners.
6. Finally, the remainder (if any) of the fee is sent back to the sender as
change and fee is paid to the miners accordingly. At this point, the
function returns the resulting state.
There are two types of accounts in Ethereum:
Externally owned accounts
Contract accounts
The first is externally owned accounts (EOAs) and the other is contract
accounts. EOAs are similar to accounts that are controlled by a private
key in bitcoin. Contract accounts are the accounts that have code
associated with them along with the private key. An EOA has ether
balance, is able to send transactions, and has no associated code,
whereas a Contract Account (CA) has ether balance, associated code,
and the ability to get triggered and execute code in response to a
transaction or a message. It is worth noting that due to the Turing-
completeness property of the Ethereum blockchain, the code within
contract accounts can be of any level of complexity. The code is
executed by EVM by each mining node on the Ethereum network. In
addition, contract accounts are able to maintain their own permanent
state and can call other contracts. It is envisaged that in the serenity
release, the distinction between externally owned accounts and contract
accounts may be eliminated.
a.   Explain pseudo-anonymity and anonymity in blockchain systems and
differentiate. Illustrate your answer with appropriate examples?
Solution:
Explain with example- 6 marks
Q4   Differentiate- 4 marks
CO-2;   Anonymity means that the identity of a person is unknown and its
[10]
SO-1,2;   actions are not trackable. Pseudonymity, however, is a much weaker
BL-3   form. It means that a person’s identity is unknown, but it is possible to
assign actions to the same person.
The first figure shows a situation where the person’s identity is
unknown. But all the actions the person made can be linked to this
person.
********** 6 **********
--- page 7 ---
The second figure shows a situation where a person’s identity is
unknown and it is impossible to link any transaction to a specific
person.
Blockchains like Bitcoin or Ethereum are pseudonymous instead of
anonymous. The address is a pseudonym for the person holding the
corresponding private key.
Every action done with this address can be traced back to this person,
although its identity might be unknown. And since all transactions are
stored in the blockchain, it is possible for everybody to trace them back,
even though this transaction lies long in the past.
There are so-called privacy coins like Monero or ZCash that allow for
real anonymity through cryptography. Here, transactions cannot be
linked to individual addresses.
b.   Explain the key steps involved in implementing blockchain technology.
Solution:
Implementing blockchain technology involves a series of well-defined
steps to ensure successful deployment and integration. The key steps are:
1. Conduct a Feasibility Study
• Assess whether blockchain is suitable for the business case.
• Analyze technical and economic viability (usually 2–4 weeks).
CO-3;
SO-1,2;   [10]
2. Create a Business Case
BL-3
• Document functional and non-functional requirements.
•   Identify risks, including regulatory compliance.
3. Conceptualize the Blockchain
• Decide on:
o Blockchain type: Public, private, or hybrid.
o Consensus mechanism: Proof of Stake, Proof of
Authority, etc.
********** 7 **********
--- page 8 ---
o Implementation approach: Build from scratch or fork an
existing protocol.
4. Scope the Project
• Define objectives, deliverables, and boundaries.
• Assign roles, estimate budget, timeline, and resources.
• Assess risks and compliance needs.
5. Design the Blockchain Solution
• Prepare feature list and prioritize based on cost-benefit analysis.
• Design UX/UI for user applications (web, mobile, desktop).
•   Include cybersecurity features.
6. Select the Tech Stack
• Choose appropriate tools, frameworks, and platforms.
• Compare options based on scalability and business needs.
7. Develop and Deploy the Solution
• Develop:
o Blockchain network (from scratch or modified protocol).
o Smart contracts for automation.
o Oracles for external data integration.
o User-facing apps and backend APIs.
• Perform QA testing and deploy to production with backup and
recovery setup.
8. Integrate with Existing Systems
• Ensure smooth integration with enterprise systems and enable
interoperability.
9. Provide After-Launch Support
• Monitor performance, fix bugs, and maintain uptime.
• Apply security patches and updates.
• Offer user support and training.
10. Continuously Evolve the Solution
• Update smart contracts, improve scalability, and enhance security.
• Add new features based on user feedback and regulatory changes.
a.   Explain working of mining algorithm in Proof of Work (PoW).
Solution:
The mining algorithm in Proof of Work (PoW) algorithm consists of the
following steps.
1. The previous block's header is retrieved from the bitcoin
network.
Q5
2. Assemble a set of transactions broadcasted on the network into
CO-2;
a block to be proposed.   [10]
SO-1,2;
3. Compute the double hash of the previous block's header
BL-3
combined with a nonce and the newly proposed block using the
SHA-256 algorithm.
4. Check if the resultant hash is lower than the current difficulty
level (target) then PoW is solved. As a result of successful PoW
the discovered block is broadcasted to the network and miners
fetch the reward.
********** 8 **********
--- page 9 ---
5. If the resultant hash is not less than the current difficulty level
(target), then repeat the process after incrementing the nonce.
This process can be visualized by using the following flowchart:
b.   What are smart contracts? Discuss different ways to deploy smart
contracts on the blockchain network.
Solution:
<Definition 2M, Different ways 8M>
A smart contract is a secure and unstoppable computer program
representing an agreement that   is automatically executable and
enforceable. It is a computer program that is written in a language that a
computer or target machine can understand. It encompasses agreements
between parties in the form of business logic.
<any 4 out of 5 ways>
1. Direct Deployment via Wallets and Blockchain Explorers – Write
CO-2;   compile and deploy directly from crypto wallet
SO-1,2;   2. Development Frameworks and Toolkits – Use Hardhat, Remix, [10]
BL-3   Truffle etc.
3. Cloud & Blockchain Platform Integration- Cloud-hosted endpoints
allow deployment via API or framework scripts without running a full
blockchain node.
4. Programmatic and Scripting Approaches - Write deployment scripts
(JS, Python, etc.) to automate deployments, especially for complex
upgradeable/proxy   patterns, batch deployments, and CI/CD
integration
5. On-Chain/Off-Chain Hybrid and Multi-Chain Deployment - Deploy
the same contract logic across different blockchains, sometimes via
platform tools or by configuring deployment scripts for multi-
network support.
********** 9 **********
--- page 10 ---
a.   Explain different types of blockchains in detail with use-case examples
for each type?
Solution:
Four types with example- 2.5 marks *4=10 marks
Blockchains can be broadly categorized into four main types Public,
Private, Consortium (Federated), and Hybrid blockchains. Each type
differs in its level of decentralization, access control, and use-case
suitability. Below is a detailed summary of each type along with
practical examples.
1. Public Blockchain
A public blockchain is a completely open and decentralized network
where anyone can join, participate in the consensus process, and verify
transactions. It operates on a permissionless model, meaning there is no
restriction on who can read or write to the network. Public blockchains
are secured through consensus mechanisms such as Proof of Work
(PoW) or Proof of Stake (PoS).
Use-case Example:
Bitcoin (BTC): The first and most prominent public blockchain, used
for peer-to-peer digital currency transactions without any intermediary.
Ethereum (ETH): A public blockchain enabling smart contracts and
decentralized applications (DApps) in finance (DeFi), NFTs, and
gaming sectors.
Advantages: Transparency, immutability, and high security.
Limitations: Slower transaction speed and high energy consumption in
Q6   some consensus mechanisms.
CO-1;   2. Private Blockchain
[10]
SO-1,2;   A private blockchain is a permissioned network controlled by a single
BL-3   organization or authority. Only authorized participants can access,
validate, and audit the blockchain. While it lacks the full
decentralization of public blockchains, it provides better privacy,
control, and efficiency.
Use-case Example:
Hyperledger Fabric (by IBM): Used by enterprises for supply chain
management, trade finance, and asset tracking. For instance, Walmart
uses Hyperledger Fabric to trace food products from farm to shelf for
enhanced food safety.
Advantages: High transaction throughput, strong privacy, and
controlled participation.
Limitations: Reduced decentralization and possible single point of
failure.
3. Consortium (Federated) Blockchain
A consortium blockchain (or federated blockchain) is a semi-
decentralized system managed by a group of pre-selected organizations
instead of a single entity. It combines the benefits of both public
transparency and private control. Each member organization operates
one or more nodes, and decisions are made collectively.
Advantages: Improved scalability, better governance, and trust among
known parties.
Limitations: Requires coordination between organizations and limited
public transparency.
********** 10 **********
--- page 11 ---
4. Hybrid Blockchain
A hybrid blockchain combines features of both public and private
blockchains. It allows organizations to keep certain data private while
enabling limited public access to ensure transparency and verifiability.
Hybrid models are ideal where data sensitivity and public accountability
must coexist.
Advantages: Flexible design, customizable transparency, and controlled
data exposure.
Limitations: Complex architecture and partial reliance on centralized
entities.
b.   Explain following elements of Ethereum Blockchain:
•   Ether cryptocurrency/tokens
• Addresses
•   Transactions
• The EVM
Solution: Explanation of each element – 2 marks *5=10 marks
• Cryptocurrency: As an incentive to the miners, Ethereum
rewards its own native currency, called ether (abbreviated as
ETH).
• Keys and addresses: Keys and addresses are used in the
Ethereum blockchain to represent ownership and transfer ether.
The keys used are made up of pairs of private and public parts.
The private key is generated randomly and is kept secret,
whereas the public key is derived from the private key.
CO-2;
Addresses are derived from public keys and are 20-byte codes
SO-1,2;   [10]
used to identify accounts.
BL-3
Address: x71C7656EC7ab88b098defB751B7401B5f6d8976F.
• Transaction in Ethereum is a digitally signed (using a private
key) data packet that contains the instructions that, when
completed, either result in a message call or contract creation.
Transactions are constructed by an actor external to the
Ethereum blockchain or some external software tool.
Smart contracts cannot send a transaction
• EVM is a simple stack-based execution machine that runs
bytecode instructions to transform the system state from one
state to another.
The EVM is a Turing-complete machine but is limited by the
amount of gas that is required to run any instruction.
a.   What do you mean by 51% attack. How does a 51% Attack Work.
Briefly explain the risks and consequences Of A 51% Attack in detail.
Solution:
What do you mean by 51% attack- 2 marks
Q7
How does a 51% Attack Work- 5 marks
CO-3;
Briefly explain the risks and consequences Of A 51% Attack in detail- 3 [10]
SO-1,2;
marks
BL-3
A 51% attack is an attack on a blockchain network where a single entity
gains control of more than half (51%) of its staking or computational
power.
********** 11 **********
--- page 12 ---
This disproportionate control allows them to implement substantial
changes, contravening the decentralization principle fundamental to the
blockchain. In other words, a 51% attack gives the power to rewrite tx
history, prevent tx completion, stop rewards to validators, and double
spend.
It's important to note that a 51% attack is among the most significant
security threats to blockchains, particularly those utilizing Proof-of-
Work and Delegated Proof-of-Stake consensus algorithms. One
alarming outcome of such an attack is a double-spending, where the
same coins are spent more than once, damaging the trust and reliability
of the blockchain.
How Does A 51% Attack Work
Diving deeper into the mechanics of a 51% attack, let's explore the step-
by-step process an attacker follows to gain and exploit control over a
blockchain network. While the exact specifics of an attack can vary
depending on several factors, here’s a simplified, general sequence of
events that typically characterizes such an attack:
Accumulate Power: The first step involves the attacker accumulating
more than half (51%) of the network's computational or hashing power.
This could be accomplished by acquiring substantial hardware resources
or convincing a large number of miners to join a pool under the attacker's
control.
Partitioning: The attacker, now commanding a majority of the network's
hashing power, effectively segregates their group from the main network
while still maintaining internal communication. Despite this separation,
the hacking group proceeds with mining operations but refrains from
sharing their progress with the primary network or receiving updates
from it. Consequently, two parallel versions of the blockchain start
evolving independently.
Fast-Paced Mining: Due to their superior hashing power, the attacker's
group is able to add blocks to their version of the blockchain faster than
the rest of the network. Over time, the difference in length between the
two versions of the chain becomes statistically proportional to the
difference in hashing power between the two groups.
Reintegration and Dominance: Once the hacking group rejoins the
network, the two competing versions of the blockchain propagate through
the entire network. According to the consensus protocol's rules, the nodes
keep the longest blockchain, and the shorter one is discarded.
Potential Threats: Upon successful execution, a 51% attack can open
Pandora's box of threats that can significantly impact a blockchain
network and its participants. These threats range from financial fraud in
the form of double-spending to outright denial of service attacks that
paralyze network functionality.
Risks And Consequences Of A 51% Attack
A successful attack can have significant implications for a blockchain
network and its users. Here's what happens:
Double-Spending: This is the most feared consequence. The attacker
could spend their money twice first, they perform a regular transaction
and then change the blockchain to show they never used the money at all.
Denial-of-Service (DoS) Attack: The hacker takes over and blocks the
addresses of other miners for a while. This stops the good guys - the
honest miners - from getting back control of the network. As a result, the
attacker's false chain of transactions can become permanent.
********** 12 **********
--- page 13 ---
Transaction Reversal: The attacker can block payments between some or
all users. This disrupts the normal operation of the network and can lead
to significant delays in transaction confirmations, undermining
confidence in the network's reliability.
Damage to Reputation: Also, the attack can severely damage a
blockchain's reputation. This can lead to a loss of trust among current and
potential users, resulting in a significant drop in the value of the
associated cryptocurrency and deterring new users or investors from
joining the network.
b.   Discuss in detail the key challenges faced by the education sector and
explain how Blockchain Technology provides effective solutions to
overcome these challenges.
Solution:
The education sector plays a vital role in the development of industries
such as medicine, agriculture, science, and technology. However,
managing educational institutions—from pre-kindergarten to PhD
level—is a complex task. The sector faces several major challenges:
Challenges in the Education Sector:
1. Record Maintenance:
Every year, billions of students enroll in various institutions.
Maintaining their personal and academic records in paper format
is a huge task. Retrieving data of students who graduated 4–5
years ago becomes time-consuming and inefficient.
2. Certificate Security:
Storing student certificates securely is difficult. Paper-based
certificates are prone to damage, loss, and falsification. Ensuring
their authenticity requires manpower and resources.
3. Accounting and Finance Management:
Educational institutions need to manage finances such as staff
CO-3;   salaries, student fees, maintenance, and operational costs. This
SO-1,2;   process is labor-intensive and requires accurate calculations.   [10]
BL-3   4. Scholarship Monitoring:
With a growing number of students and scholarship programs,
tracking and managing scholarships has become increasingly
difficult.
These challenges affect the overall performance and efficiency of the
education system.
Role of Blockchain Technology in Overcoming Challenges:
Blockchain Technology offers innovative solutions to address these
issues:
1. Digital Record Keeping:
Blockchain replaces paper documents with secure digital
records. Student and staff data can be stored in a decentralized
ledger, making it easy to access and verify without the risk of
tampering or loss.
2. Cost and Effort Saving:
By eliminating the need for physical documents, blockchain
reduces costs related to paper, printing, and manpower. It also
saves time spent on manual record maintenance.
3. Transparency and Security:
Blockchain provides a transparent and tamper-proof system for
storing student records. Since it is decentralized, ownership and
********** 13 **********
--- page 14 ---
access are distributed among authorized individuals, ensuring
data integrity.
4. Simplified Financial Processes:
Blockchain simplifies accounting tasks such as calculating staff
salaries and student scholarships. Some institutions even accept
cryptocurrencies like Bitcoin for fee payments, making
transactions faster and more transparent.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 75f93b03629a

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Blockchain Technology/ANS_Blockchain Technology(702IT0E016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION IN
TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (Comp)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Blockchain Technology
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question 1 is compulsory.
5. Attempt any four questions out of remaining questions.
Q1
Answer briefly:   [20]
a.   Differentiate Consensus mechanism: Proof of Work (PoW) and Proof of
Stake (PoS)
Solution:
Any five valid points- 5 marks
Sr. no   Proof of Work   Proof of Stake
1   Miners don’t need to hold any of the Requires validators
blockchain’s assets, and only need   to hold some of the
computing power to validate a   blockchain’s token or
transaction.   cryptocurrency.
2   May use a very significant amount   Doesn’t require
of electricity.   significant computing
power for transaction
CO-1 ;
validation.
SO-1,2 ;
3   Proof of work has a longer proven   It’s a newer approach
BL-3
history of use as a blockchain   than proof of work,
consensus mechanism.   with less adoption as
a consensus
mechanism.
4   Cryptos using proof of work are   Cryptos that use
often excluded from ESG portfolios   proof of stake might
because of the energy demands.   be more attractive for
an ESG portfolio
because 5of the lower
environmental
impact.
5   Used in Bitcoin   Used in Ethereum
b.   Explain the term contractual confidentiality? Identify the solutions to
CO-2 ;
achieve confidentiality.
SO-1,2 ;
Solution:
BL-2
<Definition – 2M, Solutions – 3M>
********** 1 **********
--- page 2 ---
While transparency is beneficial, certain futures contract details must
remain confidential to prevent front-running, strategy leakage, or
commercial espionage. The Challenges are -
1. Blockchain is a public ledger → default state is transparent.
2. Traders may not want asset quantity, strike price, or leverage
exposed.
Solutions –
1. Zero-Knowledge Proofs (zk-SNARKs / zk-STARKs)-Prove that
contract conditions are met without revealing sensitive values.
Example: Verify settlement eligibility without showing
exact strike price.
2. Confidential Transactions-Use cryptographic commitments
(Pedersen commitments) to hide amounts but allow verification.
3. Permissioned Blockchains-Access restricted to authorized
entities (Hyperledger Fabric, Quorum).
4. Off-Chain Storage with On-Chain Hashes-Sensitive contract
terms stored securely off-chain; only the hash is on-chain for
integrity checks.
5. Data Encryption on Chain-Store encrypted fields in the contract;
keys shared only between counterparties.
c.   Differentiate between Bitcoin Scripting and Ethereum Smart Contracts.
Solution: Any five valid points- 5 marks
Bitcoin   Ethereum
Generation 1   blockchain   Generation 1 blockchain(2015)
(2009)
Programming   lang   used: Programming lang used: Solidity
Scripts   is used Ethereum
Consensus alg: PoW   PoS
CO-2 ;
SO-1,2 ;   Scalability: 3-7 transactions   Eht- 30-50 trans per sec
BL-4   per sec
Block size: 1 mb in Bitcoin   0.1 mb in Ethereum
Only   cryptocurrency   Real life solutions are supported
applications are supported in   in Ethereum
Bitcoin
Bitcoin   limiting   the Etherum has more functionality
functionality to increase the
security
d.   Explain the key features of the InterPlanetary File System (IPFS) that
CO-3 ;   differentiate it from traditional HTTP-based systems?
SO-1,2 ;   Solution:
BL-3   • The InterPlanetary File System (IPFS) is a distributed storage
protocol developed by Protocol Labs for uploading, storing, and
********** 2 **********
--- page 3 ---
accessing data, files, websites, and applications in a decentralized
manner.
• Unlike traditional HTTP-based systems, which use location-based
addressing (such as URLs), IPFS uses content-based addressing.
In this system, each file is assigned a unique Content Identifier
(CID) generated through cryptographic hashing. This ensures that
the content can be retrieved from any node that stores it,
regardless of its physical location.
• IPFS operates on a peer-to-peer (P2P) network, where users share
and host portions of data. This decentralized approach enhances
data availability, reduces dependency on centralized servers, and
improves fault tolerance.
• Additionally, IPFS uses IPLD Merkle Directed Acyclic Graphs
(DAGs) to link pieces of content together. This structure ensures
data integrity, supports efficient versioning, and allows for
deduplication of data.
• IPFS offers a more secure, efficient, and resilient alternative to
traditional web protocols by leveraging content addressing and
decentralized storage.
a.   Explain the role of consensus algorithms in blockchain technology and
illustrate the working process of a consensus algorithm with a neat
diagram.
Solution:
Role 3 marks, working process explanation 5 m and diagram 2marks
The role of consensus is an attaining agreement common state or value
among multiple nodes despite the failure of some nodes. A consensus
mechanism is a set of steps that are taken by most or all nodes in a
blockchain to agree on a proposed state or value. Further, various
Q2   requirements must be met to provide the desired results in a consensus
CO-2;   mechanism.   [10]
SO-1,2;   The following describes these requirements:
BL-3   • Agreement: All honest nodes decide on the same value
• Termination: All honest nodes terminate execution of the consensus
process and eventually reach a decision.
• Validity: The value agreed upon by all honest nodes must be the same
as the initial value proposed by at least one honest node
• Fault-tolerant: The consensus algorithm should be able to run in the
presence of faulty or malicious nodes (Byzantine nodes)
• Integrity: This is a requirement that no node can make the decision
more than once in a single consensus cycle
********** 3 **********
--- page 4 ---
Working process
Transaction Verification: Nodes validate digital signatures and confirm
sufficient sender balance.
Miner or Validator Selection: Miners compete solving cryptographic
puzzles using Proof of Work.
Block Verification & Validation: Network nodes verify block hash,
structure, and transaction integrity.
Updating Blockchain: Verified block is appended to distributed ledger
across all nodes.
Incentive Miner or Validator: Successful miner rewarded with new
bitcoins and transaction fees.
b.   Define blockchain. Explain the main features of Blockchain.
Solution
Definition- 2 marks
Blockchain is a peer-to-peer, distributed ledger that is
cryptographically-secure, append-only, immutable (extremely hard to
change), and updateable only via consensus or agreement among peers.
Explain features- 8 marks.
Peer-to-peer- This means that there is no central controller in the
network, and all participants talk to each other directly. This property
allows for cash transactions to be exchanged directly among the peers
without a third-party involvement, such as by a bank.
Distributed ledger- which simply means that a ledger is spread across
CO-1;
the network among all peers in the network, and each peer holds a copy
SO-1,2;   [10]
of the complete ledger.
BL-3
Cryptographically-secure- which means that cryptography has been
used to provide security services which make this ledger secure against
tampering and misuse. These services include non-repudiation, data
integrity, and data origin authentication.
Append-only, which means that data can only be added to the
blockchain in time-ordered sequential order
Updateable only via consensus- This is what gives it the power of
decentralization. In this scenario, no central authority is in control of
updating the ledger. Instead, any update made to the blockchain is
validated against strict criteria defined by the blockchain protocol and
added to the blockchain only after a consensus has been reached among
all participating peers/nodes on the network.
********** 4 **********
--- page 5 ---
a.   Draw and explain block structure in Blockchain.
Solution
Diagram- 4 marks
Q3
CO-1;
[10]
SO-1,2;
BL-3
Explain- 6 marks
attributes of a block: the block header, which is composed of pointer to
previous block, the timestamp, nonce, Merkle root, and the block body
that contains transactions.
A nonce is a number that is generated and used only once. A nonce is
used extensively in many cryptographic operations to provide replay
protection, authentication, and encryption. In blockchain, it's used in
PoW consensus algorithms and for transaction replay protection.
Merkle root is a hash of all of the nodes of a Merkle tree. Merkle trees
are widely used to validate the large data structures securely and
efficiently.
b.   Explain Ethereum accounts and their types in detail.
Solution:
Accounts are one of the main building blocks of the Ethereum
blockchain. The state is created or updated as a result of the interaction
between accounts. Operations performed between and on the accounts
represent state transitions. State transition is achieved using what's
called the Ethereum state transition function, which works as follows:
1. Confirm the transaction validity by checking the syntax, signature
CO-2;
validity, and nonce.
SO-1,2;   [10]
2. Transaction fee is calculated and the sending address is resolved
BL-3
using the signature. Furthermore, sender's account balance is checked
and subtracted accordingly and nonce is incremented. An error is
returned if the account balance is not enough.
3. Provide enough ether (gas price) to cover the cost of the transaction.
This is charged per byte incrementally according to the size of the
transaction.
4. In this step, the actual transfer of value occurs. The flow is from the
sender's account to receiver's account. The account is created
********** 5 **********

[Text in pictures on this page, read by OCR]
POINTER TO PREVIOUS BLOCK’S HASH
NONCE

TIME STAMP
MERKLE ROOT

LIST OF TRANSACTIONS

The generic structure of a block.
--- page 6 ---
automatically if the destination account specified in the transaction does
not exist yet. Moreover, if the destination account is a contract, then the
contract code is executed. This also depends on the amount of gas
available. If enough gas is available, then the contract code will be
executed fully; otherwise, it will run up to the point where it runs out of
gas.
5. In cases of transaction failure due to insufficient account balance or
gas, all state changes are rolled back with the exception of fee payment,
which is paid to the miners.
6. Finally, the remainder (if any) of the fee is sent back to the sender as
change and fee is paid to the miners accordingly. At this point, the
function returns the resulting state.
There are two types of accounts in Ethereum:
Externally owned accounts
Contract accounts
The first is externally owned accounts (EOAs) and the other is contract
accounts. EOAs are similar to accounts that are controlled by a private
key in bitcoin. Contract accounts are the accounts that have code
associated with them along with the private key. An EOA has ether
balance, is able to send transactions, and has no associated code,
whereas a Contract Account (CA) has ether balance, associated code,
and the ability to get triggered and execute code in response to a
transaction or a message. It is worth noting that due to the Turing-
completeness property of the Ethereum blockchain, the code within
contract accounts can be of any level of complexity. The code is
executed by EVM by each mining node on the Ethereum network. In
addition, contract accounts are able to maintain their own permanent
state and can call other contracts. It is envisaged that in the serenity
release, the distinction between externally owned accounts and contract
accounts may be eliminated.
a.   Explain pseudo-anonymity and anonymity in blockchain systems and
differentiate. Illustrate your answer with appropriate examples?
Solution:
Explain with example- 6 marks
Q4   Differentiate- 4 marks
CO-2;   Anonymity means that the identity of a person is unknown and its
[10]
SO-1,2;   actions are not trackable. Pseudonymity, however, is a much weaker
BL-3   form. It means that a person’s identity is unknown, but it is possible to
assign actions to the same person.
The first figure shows a situation where the person’s identity is
unknown. But all the actions the person made can be linked to this
person.
********** 6 **********
--- page 7 ---
The second figure shows a situation where a person’s identity is
unknown and it is impossible to link any transaction to a specific
person.
Blockchains like Bitcoin or Ethereum are pseudonymous instead of
anonymous. The address is a pseudonym for the person holding the
corresponding private key.
Every action done with this address can be traced back to this person,
although its identity might be unknown. And since all transactions are
stored in the blockchain, it is possible for everybody to trace them back,
even though this transaction lies long in the past.
There are so-called privacy coins like Monero or ZCash that allow for
real anonymity through cryptography. Here, transactions cannot be
linked to individual addresses.
b.   Explain the key steps involved in implementing blockchain technology.
Solution:
Implementing blockchain technology involves a series of well-defined
steps to ensure successful deployment and integration. The key steps are:
1. Conduct a Feasibility Study
• Assess whether blockchain is suitable for the business case.
• Analyze technical and economic viability (usually 2–4 weeks).
CO-3;
SO-1,2;   [10]
2. Create a Business Case
BL-3
• Document functional and non-functional requirements.
•   Identify risks, including regulatory compliance.
3. Conceptualize the Blockchain
• Decide on:
o Blockchain type: Public, private, or hybrid.
o Consensus mechanism: Proof of Stake, Proof of
Authority, etc.
********** 7 **********
--- page 8 ---
o Implementation approach: Build from scratch or fork an
existing protocol.
4. Scope the Project
• Define objectives, deliverables, and boundaries.
• Assign roles, estimate budget, timeline, and resources.
• Assess risks and compliance needs.
5. Design the Blockchain Solution
• Prepare feature list and prioritize based on cost-benefit analysis.
• Design UX/UI for user applications (web, mobile, desktop).
•   Include cybersecurity features.
6. Select the Tech Stack
• Choose appropriate tools, frameworks, and platforms.
• Compare options based on scalability and business needs.
7. Develop and Deploy the Solution
• Develop:
o Blockchain network (from scratch or modified protocol).
o Smart contracts for automation.
o Oracles for external data integration.
o User-facing apps and backend APIs.
• Perform QA testing and deploy to production with backup and
recovery setup.
8. Integrate with Existing Systems
• Ensure smooth integration with enterprise systems and enable
interoperability.
9. Provide After-Launch Support
• Monitor performance, fix bugs, and maintain uptime.
• Apply security patches and updates.
• Offer user support and training.
10. Continuously Evolve the Solution
• Update smart contracts, improve scalability, and enhance security.
• Add new features based on user feedback and regulatory changes.
a.   Explain working of mining algorithm in Proof of Work (PoW).
Solution:
The mining algorithm in Proof of Work (PoW) algorithm consists of the
following steps.
1. The previous block's header is retrieved from the bitcoin
network.
Q5
2. Assemble a set of transactions broadcasted on the network into
CO-2;
a block to be proposed.   [10]
SO-1,2;
3. Compute the double hash of the previous block's header
BL-3
combined with a nonce and the newly proposed block using the
SHA-256 algorithm.
4. Check if the resultant hash is lower than the current difficulty
level (target) then PoW is solved. As a result of successful PoW
the discovered block is broadcasted to the network and miners
fetch the reward.
********** 8 **********
--- page 9 ---
5. If the resultant hash is not less than the current difficulty level
(target), then repeat the process after incrementing the nonce.
This process can be visualized by using the following flowchart:
b.   What are smart contracts? Discuss different ways to deploy smart
contracts on the blockchain network.
Solution:
<Definition 2M, Different ways 8M>
A smart contract is a secure and unstoppable computer program
representing an agreement that   is automatically executable and
enforceable. It is a computer program that is written in a language that a
computer or target machine can understand. It encompasses agreements
between parties in the form of business logic.
<any 4 out of 5 ways>
1. Direct Deployment via Wallets and Blockchain Explorers – Write
CO-2;   compile and deploy directly from crypto wallet
SO-1,2;   2. Development Frameworks and Toolkits – Use Hardhat, Remix, [10]
BL-3   Truffle etc.
3. Cloud & Blockchain Platform Integration- Cloud-hosted endpoints
allow deployment via API or framework scripts without running a full
blockchain node.
4. Programmatic and Scripting Approaches - Write deployment scripts
(JS, Python, etc.) to automate deployments, especially for complex
upgradeable/proxy   patterns, batch deployments, and CI/CD
integration
5. On-Chain/Off-Chain Hybrid and Multi-Chain Deployment - Deploy
the same contract logic across different blockchains, sometimes via
platform tools or by configuring deployment scripts for multi-
network support.
********** 9 **********
--- page 10 ---
a.   Explain different types of blockchains in detail with use-case examples
for each type?
Solution:
Four types with example- 2.5 marks *4=10 marks
Blockchains can be broadly categorized into four main types Public,
Private, Consortium (Federated), and Hybrid blockchains. Each type
differs in its level of decentralization, access control, and use-case
suitability. Below is a detailed summary of each type along with
practical examples.
1. Public Blockchain
A public blockchain is a completely open and decentralized network
where anyone can join, participate in the consensus process, and verify
transactions. It operates on a permissionless model, meaning there is no
restriction on who can read or write to the network. Public blockchains
are secured through consensus mechanisms such as Proof of Work
(PoW) or Proof of Stake (PoS).
Use-case Example:
Bitcoin (BTC): The first and most prominent public blockchain, used
for peer-to-peer digital currency transactions without any intermediary.
Ethereum (ETH): A public blockchain enabling smart contracts and
decentralized applications (DApps) in finance (DeFi), NFTs, and
gaming sectors.
Advantages: Transparency, immutability, and high security.
Limitations: Slower transaction speed and high energy consumption in
Q6   some consensus mechanisms.
CO-1;   2. Private Blockchain
[10]
SO-1,2;   A private blockchain is a permissioned network controlled by a single
BL-3   organization or authority. Only authorized participants can access,
validate, and audit the blockchain. While it lacks the full
decentralization of public blockchains, it provides better privacy,
control, and efficiency.
Use-case Example:
Hyperledger Fabric (by IBM): Used by enterprises for supply chain
management, trade finance, and asset tracking. For instance, Walmart
uses Hyperledger Fabric to trace food products from farm to shelf for
enhanced food safety.
Advantages: High transaction throughput, strong privacy, and
controlled participation.
Limitations: Reduced decentralization and possible single point of
failure.
3. Consortium (Federated) Blockchain
A consortium blockchain (or federated blockchain) is a semi-
decentralized system managed by a group of pre-selected organizations
instead of a single entity. It combines the benefits of both public
transparency and private control. Each member organization operates
one or more nodes, and decisions are made collectively.
Advantages: Improved scalability, better governance, and trust among
known parties.
Limitations: Requires coordination between organizations and limited
public transparency.
********** 10 **********
--- page 11 ---
4. Hybrid Blockchain
A hybrid blockchain combines features of both public and private
blockchains. It allows organizations to keep certain data private while
enabling limited public access to ensure transparency and verifiability.
Hybrid models are ideal where data sensitivity and public accountability
must coexist.
Advantages: Flexible design, customizable transparency, and controlled
data exposure.
Limitations: Complex architecture and partial reliance on centralized
entities.
b.   Explain following elements of Ethereum Blockchain:
•   Ether cryptocurrency/tokens
• Addresses
•   Transactions
• The EVM
Solution: Explanation of each element – 2 marks *5=10 marks
• Cryptocurrency: As an incentive to the miners, Ethereum
rewards its own native currency, called ether (abbreviated as
ETH).
• Keys and addresses: Keys and addresses are used in the
Ethereum blockchain to represent ownership and transfer ether.
The keys used are made up of pairs of private and public parts.
The private key is generated randomly and is kept secret,
whereas the public key is derived from the private key.
CO-2;
Addresses are derived from public keys and are 20-byte codes
SO-1,2;   [10]
used to identify accounts.
BL-3
Address: x71C7656EC7ab88b098defB751B7401B5f6d8976F.
• Transaction in Ethereum is a digitally signed (using a private
key) data packet that contains the instructions that, when
completed, either result in a message call or contract creation.
Transactions are constructed by an actor external to the
Ethereum blockchain or some external software tool.
Smart contracts cannot send a transaction
• EVM is a simple stack-based execution machine that runs
bytecode instructions to transform the system state from one
state to another.
The EVM is a Turing-complete machine but is limited by the
amount of gas that is required to run any instruction.
a.   What do you mean by 51% attack. How does a 51% Attack Work.
Briefly explain the risks and consequences Of A 51% Attack in detail.
Solution:
What do you mean by 51% attack- 2 marks
Q7
How does a 51% Attack Work- 5 marks
CO-3;
Briefly explain the risks and consequences Of A 51% Attack in detail- 3 [10]
SO-1,2;
marks
BL-3
A 51% attack is an attack on a blockchain network where a single entity
gains control of more than half (51%) of its staking or computational
power.
********** 11 **********
--- page 12 ---
This disproportionate control allows them to implement substantial
changes, contravening the decentralization principle fundamental to the
blockchain. In other words, a 51% attack gives the power to rewrite tx
history, prevent tx completion, stop rewards to validators, and double
spend.
It's important to note that a 51% attack is among the most significant
security threats to blockchains, particularly those utilizing Proof-of-
Work and Delegated Proof-of-Stake consensus algorithms. One
alarming outcome of such an attack is a double-spending, where the
same coins are spent more than once, damaging the trust and reliability
of the blockchain.
How Does A 51% Attack Work
Diving deeper into the mechanics of a 51% attack, let's explore the step-
by-step process an attacker follows to gain and exploit control over a
blockchain network. While the exact specifics of an attack can vary
depending on several factors, here’s a simplified, general sequence of
events that typically characterizes such an attack:
Accumulate Power: The first step involves the attacker accumulating
more than half (51%) of the network's computational or hashing power.
This could be accomplished by acquiring substantial hardware resources
or convincing a large number of miners to join a pool under the attacker's
control.
Partitioning: The attacker, now commanding a majority of the network's
hashing power, effectively segregates their group from the main network
while still maintaining internal communication. Despite this separation,
the hacking group proceeds with mining operations but refrains from
sharing their progress with the primary network or receiving updates
from it. Consequently, two parallel versions of the blockchain start
evolving independently.
Fast-Paced Mining: Due to their superior hashing power, the attacker's
group is able to add blocks to their version of the blockchain faster than
the rest of the network. Over time, the difference in length between the
two versions of the chain becomes statistically proportional to the
difference in hashing power between the two groups.
Reintegration and Dominance: Once the hacking group rejoins the
network, the two competing versions of the blockchain propagate through
the entire network. According to the consensus protocol's rules, the nodes
keep the longest blockchain, and the shorter one is discarded.
Potential Threats: Upon successful execution, a 51% attack can open
Pandora's box of threats that can significantly impact a blockchain
network and its participants. These threats range from financial fraud in
the form of double-spending to outright denial of service attacks that
paralyze network functionality.
Risks And Consequences Of A 51% Attack
A successful attack can have significant implications for a blockchain
network and its users. Here's what happens:
Double-Spending: This is the most feared consequence. The attacker
could spend their money twice first, they perform a regular transaction
and then change the blockchain to show they never used the money at all.
Denial-of-Service (DoS) Attack: The hacker takes over and blocks the
addresses of other miners for a while. This stops the good guys - the
honest miners - from getting back control of the network. As a result, the
attacker's false chain of transactions can become permanent.
********** 12 **********
--- page 13 ---
Transaction Reversal: The attacker can block payments between some or
all users. This disrupts the normal operation of the network and can lead
to significant delays in transaction confirmations, undermining
confidence in the network's reliability.
Damage to Reputation: Also, the attack can severely damage a
blockchain's reputation. This can lead to a loss of trust among current and
potential users, resulting in a significant drop in the value of the
associated cryptocurrency and deterring new users or investors from
joining the network.
b.   Discuss in detail the key challenges faced by the education sector and
explain how Blockchain Technology provides effective solutions to
overcome these challenges.
Solution:
The education sector plays a vital role in the development of industries
such as medicine, agriculture, science, and technology. However,
managing educational institutions—from pre-kindergarten to PhD
level—is a complex task. The sector faces several major challenges:
Challenges in the Education Sector:
1. Record Maintenance:
Every year, billions of students enroll in various institutions.
Maintaining their personal and academic records in paper format
is a huge task. Retrieving data of students who graduated 4–5
years ago becomes time-consuming and inefficient.
2. Certificate Security:
Storing student certificates securely is difficult. Paper-based
certificates are prone to damage, loss, and falsification. Ensuring
their authenticity requires manpower and resources.
3. Accounting and Finance Management:
Educational institutions need to manage finances such as staff
CO-3;   salaries, student fees, maintenance, and operational costs. This
SO-1,2;   process is labor-intensive and requires accurate calculations.   [10]
BL-3   4. Scholarship Monitoring:
With a growing number of students and scholarship programs,
tracking and managing scholarships has become increasingly
difficult.
These challenges affect the overall performance and efficiency of the
education system.
Role of Blockchain Technology in Overcoming Challenges:
Blockchain Technology offers innovative solutions to address these
issues:
1. Digital Record Keeping:
Blockchain replaces paper documents with secure digital
records. Student and staff data can be stored in a decentralized
ledger, making it easy to access and verify without the risk of
tampering or loss.
2. Cost and Effort Saving:
By eliminating the need for physical documents, blockchain
reduces costs related to paper, printing, and manpower. It also
saves time spent on manual record maintenance.
3. Transparency and Security:
Blockchain provides a transparent and tamper-proof system for
storing student records. Since it is decentralized, ownership and
********** 13 **********
--- page 14 ---
access are distributed among authorized individuals, ensuring
data integrity.
4. Simplified Financial Processes:
Blockchain simplifies accounting tasks such as calculating staff
salaries and student scholarships. Some institutions even accept
cryptocurrencies like Bitcoin for fee payments, making
transactions faster and more transparent.
********** 14 **********
````
