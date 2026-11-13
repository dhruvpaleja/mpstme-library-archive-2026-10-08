# Reinforcement Learning: question papers in full

19 unique papers · 2023-24 to 2025-26 · Data Science, Artificial Intelligence, AI and Machine Learning, Computer Engineering, AI and Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 172c17165ef0

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Reinforcement Learning/QP_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
Q1
Answer briefly:   [20]
CO-1;   a
Explain types of Reinforcement Learning.
SO-1;   [05]
BL-2
CO-3;   b
SO-1;   Define the Bellman Equation for state-value function.   [05]
BL-2
c   Discuss the efficiency of Dynamic Programming methods in solving
CO-2,4;
SO- 1;   MDPs. What are the major challenges and limitations?   [05]
BL-2
CO-5;   d   Write short note on Actor-Critic methods.
SO-1;   [05]
BL-2
Q2   a   Define Reinforcement Learning (RL). Describe the key component
CO-1;
involved in the RL framework with a suitable example and diagram.   [10]
SO-1;
BL-2
b   Consider the following environment with states and rewards as mentioned.
Each arrow indicates the policy the immediate reward received upon
moving to the next state. The goal state is S9 and its state value is 0.
Assume that the actions are deterministic. Apply the Bellman Equation and
CO-3   find:
SO-1;   i.   Evaluate state value for all the states except the terminal   [10]
BL-3,4   state for discount factor γ = 0.9.
ii.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.1.
iii.   State your comment based on evaluation done for both
the discount factors.
********** 1 **********
--- page 2 ---
Apply the Bellman equation 𝑉(𝑠) = 𝑅(𝑠, 𝑎, 𝑠′) + 𝛾𝑉(𝑠′),
Note: Work backwards from terminal state to calculate value.
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states P and Q and a terminal state T.
Assume the discount factor γ = 0.7.
Episode 1: P 4 Q 3 P 2 T
Q3   Episode 2: Q 5 P 1 Q 2 T
CO-2,4;
Estimate the state value using First Visit Monte Carlo.   [10]
SO-1
Estimate the state value using Every Visit Monte Carlo.
BL-4,5
Construct Markov model that best explains the observations.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
CO-2,4   b
Explain how iterative updates are used in Dynamic Programming methods
SO-1
(Value Iteration/Policy Iteration) for solving MDPs. Also mention any two   [05]
BL-2
challenges or limitations of these methods.
CO-2,4   c   Define on-policy and off-policy learning in the context of Monte Carlo
SO-1   methods. Give one real-world example of each. Explain the role of the   [05]
BL-2,3   behavior policy and the target policy in off-policy Monte Carlo learning.
a   Consider a Multi-Armed Bandit problem with the following parameters:
Time step t = 5
Number of bandits (machines) = 4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
Q4
The probability of winning for each machine is:
CO-2
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
SO-1   [10]
BL-3,4
Assume that the random number generated for selection of one machine in
the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
********** 2 **********
--- page 3 ---
b   A student switches between:
Study Mode (S1) and Relax Mode (S2).
Actions: Study or Relax.
From Study: Study → 0.7 stay, 0.3 go to Relax,
CO-3   From Relax: Study → 0.6 go to Study, 0.4 stay Relax → always stay
SO-1   Rewards: +5 for Study and +1 for Relax   [05]
BL-3
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
c   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 3, R₂ = 6, R₃ = -4, R₄ = 2, R₅ = 8
CO-3
SO-1   i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.7   [05]
BL-3,4   ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.4
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
a   [10]
In the given example, the robot must move from the Start state 𝒓 to the
Target state 𝒂 with a reward structure of +80 for reaching the target and -2
for each step taken. Assume the initial Q-value to be zero and discount factor
= 0.8. Apply the Monte-Carlo Exploring Starts Algorithm with T=6 and
initial random state as (𝑔, 𝐿) update the policy for given episode E1 and E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.8, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Q5   Episodes:
CO-2,4
SO-1   E1: (𝒈, 𝑳) →(𝑓, 𝑅) →(𝑔, 𝑅) →(ℎ, 𝑈) →(𝑐, 𝐿) →(𝑏, 𝐿) →(𝑎, 𝑠𝑡𝑜𝑝)
BL-3,4
E2: (𝒊, 𝑫) →(𝑚, 𝑈) →(𝑖, 𝑈) →(𝑒, 𝐿) →(𝑑, 𝑅) →(𝑐, 𝐿) →(𝑏, 𝑅)
Targe
t a   b   c   d   e
f   g   h   i
j   k   m
n   o   p   q   r
********** 3 **********
--- page 4 ---
b   With reference to TD Learning and SARSA, answer the following:
(i) Explain TD (0) and TD (1) approaches in RL.
(ii) Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
CO-2,4   Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
SO-1   Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
[10]
BL-2, 3   Take α = 0.2 and γ = 0.9.
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
steps.
Hint: V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
SARSA Update Rule:
Q (Sₜ, Aₜ) ← Q (Sₜ, Aₜ) + α [ Rₜ₊₁ + γ Q (Sₜ₊₁, Aₜ₊₁) – Q (Sₜ, Aₜ)
a   Consider an n-armed bandit problem where the action values are estimated
using incremental methods. Apply the incremental update rule to compute
Q6
action-value estimates for a given sequence of rewards. Analyze how the
CO-2
choice of step-size parameter affects convergence and stability of
SO-1   [10]
estimates. Evaluate the effectiveness of incremental implementation
BL-3,4,5
compared to sample-average methods in practical scenarios
b   A mining resource vessel is located near a coastal mining region. It must
reach its home base safely and can move only in East and West directions.
Possible routes:
Go to Mineral Site, collect minerals, then go to Home (East → West)
Go to Fuel Station, refuel, then go to Home (West → East)
Go directly to Home
Dangers:
There is a landslide zone to the East of the Mineral Site
There is a storm zone to the West of the Fuel Station
Uncertainty:
Intended direction = 0.6
Opposite direction = 0.4
Assume:
CO-2,4   Initial policy: Move East
SO-1   Initial values = 0   [10]
BL-2, 4
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   Sta Mineral   Fuel   Ho   Landslide   Storm
rt   Site   Station   me   Zone   Zone
Reward   0   +18   +9   +6   −130   −95
Values   0   0   0   0   0   0
Initial   E   E   E   –   –   –
Policy
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
********** 4 **********
--- page 5 ---
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
Q7   a
Explain Policy Gradient Methods in Reinforcement Learning, discuss
CO-5
SO-1   policy approximation, and describe their advantages.   [10]
BL-2,3
b   i.   Describe the concept of eligibility traces in TD(λ).
ii.   Consider an environment with 3 states: S1, S2, S3. The agent
moves sequentially to the next state:
• S1 → S2 gives reward 4
CO-2,4   • S2 → S3 gives reward 5
SO-1   • S3 → Terminal gives reward 3
[10]
BL-3,4   Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3, V(terminal) =0
Using Temporal Difference TD (0), compute the updated values:
V(S1), V(S2), and V(S3).
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 869f47bfa5a0

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Reinforcement Learning/QP_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
Q1
Answer briefly:   [20]
CO-1;   a
Explain types of Reinforcement Learning.
SO-1;   [05]
BL-2
CO-3;   b
SO-1;   Define the Bellman Equation for state-value function.   [05]
BL-2
c   Discuss the efficiency of Dynamic Programming methods in solving
CO-2,4;
SO- 1;   MDPs. What are the major challenges and limitations?   [05]
BL-2
CO-5;   d   Write short note on Actor-Critic methods.
SO-1;   [05]
BL-2
Q2   a   Define Reinforcement Learning (RL). Describe the key component
CO-1;
involved in the RL framework with a suitable example and diagram.   [10]
SO-1;
BL-2
b   Consider the following environment with states and rewards as mentioned.
Each arrow indicates the policy the immediate reward received upon
moving to the next state. The goal state is S9 and its state value is 0.
Assume that the actions are deterministic. Apply the Bellman Equation and
CO-3   find:
SO-1;   i.   Evaluate state value for all the states except the terminal   [10]
BL-3,4   state for discount factor γ = 0.9.
ii.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.1.
iii.   State your comment based on evaluation done for both
the discount factors.
********** 1 **********
--- page 2 ---
Apply the Bellman equation 𝑉(𝑠) = 𝑅(𝑠, 𝑎, 𝑠′) + 𝛾𝑉(𝑠′),
Note: Work backwards from terminal state to calculate value.
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states P and Q and a terminal state T.
Assume the discount factor γ = 0.7.
Episode 1: P 4 Q 3 P 2 T
Q3   Episode 2: Q 5 P 1 Q 2 T
CO-2,4;
Estimate the state value using First Visit Monte Carlo.   [10]
SO-1
Estimate the state value using Every Visit Monte Carlo.
BL-4,5
Construct Markov model that best explains the observations.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
CO-2,4   b
Explain how iterative updates are used in Dynamic Programming methods
SO-1
(Value Iteration/Policy Iteration) for solving MDPs. Also mention any two   [05]
BL-2
challenges or limitations of these methods.
CO-2,4   c   Define on-policy and off-policy learning in the context of Monte Carlo
SO-1   methods. Give one real-world example of each. Explain the role of the   [05]
BL-2,3   behavior policy and the target policy in off-policy Monte Carlo learning.
a   Consider a Multi-Armed Bandit problem with the following parameters:
Time step t = 5
Number of bandits (machines) = 4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
Q4
The probability of winning for each machine is:
CO-2
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
SO-1   [10]
BL-3,4
Assume that the random number generated for selection of one machine in
the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
********** 2 **********
--- page 3 ---
b   A student switches between:
Study Mode (S1) and Relax Mode (S2).
Actions: Study or Relax.
From Study: Study → 0.7 stay, 0.3 go to Relax,
CO-3   From Relax: Study → 0.6 go to Study, 0.4 stay Relax → always stay
SO-1   Rewards: +5 for Study and +1 for Relax   [05]
BL-3
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
c   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 3, R₂ = 6, R₃ = -4, R₄ = 2, R₅ = 8
CO-3
SO-1   i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.7   [05]
BL-3,4   ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.4
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
a   [10]
In the given example, the robot must move from the Start state 𝒓 to the
Target state 𝒂 with a reward structure of +80 for reaching the target and -2
for each step taken. Assume the initial Q-value to be zero and discount factor
= 0.8. Apply the Monte-Carlo Exploring Starts Algorithm with T=6 and
initial random state as (𝑔, 𝐿) update the policy for given episode E1 and E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.8, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Q5   Episodes:
CO-2,4
SO-1   E1: (𝒈, 𝑳) →(𝑓, 𝑅) →(𝑔, 𝑅) →(ℎ, 𝑈) →(𝑐, 𝐿) →(𝑏, 𝐿) →(𝑎, 𝑠𝑡𝑜𝑝)
BL-3,4
E2: (𝒊, 𝑫) →(𝑚, 𝑈) →(𝑖, 𝑈) →(𝑒, 𝐿) →(𝑑, 𝑅) →(𝑐, 𝐿) →(𝑏, 𝑅)
Targe
t a   b   c   d   e
f   g   h   i
j   k   m
n   o   p   q   r
********** 3 **********
--- page 4 ---
b   With reference to TD Learning and SARSA, answer the following:
(i) Explain TD (0) and TD (1) approaches in RL.
(ii) Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
CO-2,4   Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
SO-1   Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
[10]
BL-2, 3   Take α = 0.2 and γ = 0.9.
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
steps.
Hint: V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
SARSA Update Rule:
Q (Sₜ, Aₜ) ← Q (Sₜ, Aₜ) + α [ Rₜ₊₁ + γ Q (Sₜ₊₁, Aₜ₊₁) – Q (Sₜ, Aₜ)
a   Consider an n-armed bandit problem where the action values are estimated
using incremental methods. Apply the incremental update rule to compute
Q6
action-value estimates for a given sequence of rewards. Analyze how the
CO-2
choice of step-size parameter affects convergence and stability of
SO-1   [10]
estimates. Evaluate the effectiveness of incremental implementation
BL-3,4,5
compared to sample-average methods in practical scenarios
b   A mining resource vessel is located near a coastal mining region. It must
reach its home base safely and can move only in East and West directions.
Possible routes:
Go to Mineral Site, collect minerals, then go to Home (East → West)
Go to Fuel Station, refuel, then go to Home (West → East)
Go directly to Home
Dangers:
There is a landslide zone to the East of the Mineral Site
There is a storm zone to the West of the Fuel Station
Uncertainty:
Intended direction = 0.6
Opposite direction = 0.4
Assume:
CO-2,4   Initial policy: Move East
SO-1   Initial values = 0   [10]
BL-2, 4
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   Sta Mineral   Fuel   Ho   Landslide   Storm
rt   Site   Station   me   Zone   Zone
Reward   0   +18   +9   +6   −130   −95
Values   0   0   0   0   0   0
Initial   E   E   E   –   –   –
Policy
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
********** 4 **********
--- page 5 ---
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
Q7   a
Explain Policy Gradient Methods in Reinforcement Learning, discuss
CO-5
SO-1   policy approximation, and describe their advantages.   [10]
BL-2,3
b   i.   Describe the concept of eligibility traces in TD(λ).
ii.   Consider an environment with 3 states: S1, S2, S3. The agent
moves sequentially to the next state:
• S1 → S2 gives reward 4
CO-2,4   • S2 → S3 gives reward 5
SO-1   • S3 → Terminal gives reward 3
[10]
BL-3,4   Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3, V(terminal) =0
Using Temporal Difference TD (0), compute the updated values:
V(S1), V(S2), and V(S3).
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 5122181d59bf

- Departments: AI and Machine Learning, Artificial Intelligence, Data Science
- Programmes: B TECH / DATA SCIENCE, BTech AI 7012, BTech AIML 7053, MBA TECH / Artificial Intelligence, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/Reinforcement Learning/QP_Reinforcement Learning(702DB0E014)_2025-2026.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (8 pages), mean OCR confidence 84.9
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

; Academic Year: 2025-2026
Program/s: B.Tech/MBA Tech

Year: IV Semester: VIL
Stream/s ; DS/AI/AIML

Subject: Reinforcement Learning

Time: 3 hrs (Jos 00an¢o 1:00pm)
Date:__ 2 / 12/2025

No. of Pages: 8
Marks: 100 __

Final Examination(Qqs— 26)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. :

1) Question No. _1l___ is compulsory.

2) Out of remaining questions, attempt any 4
3) In all___5_ questions to be attempted.

4) All questions carry equal marks,

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

questions.

: Ql Answer briefly: [20]
CO-1; a . : : : ‘

SO-1: : With reference to. Reinforcement Learning, . discuss exploration and
BL.2. exploitation trade-off with suitable example.

ae p Define Markov Decision Process (MDP) with reference to rewards,
BL? transition model, discount factor, horizon, goal.

co24. |° In the context of Reinforcement Learning, discuss the key points of
$6.1. : Dynamic Programming approach, highlighting its significance. Compare
BL.2 : Dynamic Programming with Monte Carlo approach in terms of model

requirement, type of value update and convergence. :

CO-S; d Explain policy gradient approach in reinforcement learning. State the
SO-1 ; advantages of using parameterized policy instead of a tabular one.

BL-2 ee :
--- page 2 ---
Q2 ya With the help of suitable examples, define the following concepts in

CO-1; reinforcement learning- [10]
SO-1; Agent, Environment, State, Action, Reward, Policy, Reward, Episode,
BL-2._. Value function, Model. .

b . | Consider the following environment with states and rewards as mentioned.

Each arrow indicates the allowed movement direction and the immediate

reward received upon moving to the next state. Reaching the goal state I
yields a reward of +10. This is the terminal state and its value is 0. Assume
that the actions are deterministic (that means the agent always moves in the

indicated direction). .
Bio vor Deeps og

-1 | iz |
B |. E | H

2 | ic : 10 |

-2
C F
CO-3 (Goal)
SO-1; - . , [10]
BL-4,5 Apply the Bellman equation V(s) = R(s,a,s') + yV(s‘),~
: i. Evaluate value V(s) for all the states except the terminal state
for discount factor y = 0.9. Show the steps. ;
ii. Evaluate value V(s) for all the states except the terminal state
_ for discount factor y = 0.1. Show the steps.
iii. Comprehend. your observations based on. evaluation done for

; both the discount factors.
Note: Work backwards from terminal state to calculate value and complete
the following table. . :
State S Values V(s) | Values V(s)
y= 0.9 y=01
I V)=0 Vd) =0
--- page 3 ---
la Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states A and B and a terminal state T. Assume that the following
two episodes are observed when Monte-Carlo evaluation is being carried
out. The numbers within the episodes denote the rewards that are collected
during the transition. For example, Episode | the agent starts with state A,
then goes to state A again, then to B, and B again and then terminates. On
: the way, the agent collects the rewards of 2, 6, 1 and 0 respectively.
Assume the discount factor to be y = 0.7. .

ae : a. Episode 1: A2A6B1BO0T
50-1. : Episode 2:B3B6A1 BOT [10]
BL-4,5 F Fi a .
: i. Estimate the state value for both the states A and B using First
Visit Monte Carlo algorithm. :
ii. Estimate the state value for both the states A and B using Every
Visit Monte Carlo algorithm. . 5
iii. Construct Markov model that best explains the above scenario.
Hint:
CO-2,4 b : ; i ee 2 :
SO-1 With reference to Dynamic Programming approach, explain pseudo-code [5].
BL-2 of Value Iteration algorithm. :
CO-2,4 c ; piace ; ;
S0-1 Compare on-policy and off-policy methods. Discuss offpolicy method — [5]
BL-2,3 wath importance sampling technique.
a i. Discuss the pseudo-code for Epsilon greedy Multi Arm Bandit
: Algorithm. ;

ii. A 3-armed bandit problem is initialized with action-value
estimates Q(a)=0 for all actions. Using the Epsilon-greedy
action selection strategy with Epsilon € =0.1, the following

Q4 sequence of actions and rewards is observed: (A,,2), (A>, 3),
Co-2 (Az,1), (Az, 3), (A3,2).Using the incremental update formula,
SO-1 calculate the action-value estimates Q(a) after each step and | [10]
BL-3,4 complete the table below. Assume N(a) = 1 for step 0 for all

the actions.
iii. Identify the greedy action would be selected for step 6
--- page 4 ---
Step | Action | Reward Q(Ax) | Q(Az) | Q(Az) | Reason why

selected | observed the next
action was
. selected
0 0 0 0
1 Ay 2
2 Ay 3
3 Ap 1
4 Az 3
5 A3 2
6

"| Hint: Incremental update is given by

1
Qn+1 (a) = Qn(@) + New Len Fort Qn(a@)]

b A bird lives in a park that has two favorite spots — one near the fountain
and another on a tree branch. At each step, the bird can choose to either fly
or rest. If the bird is near the fountain and decides to fly, there is a 70%
chance that it will reach the tree branch and a 30% chance that it will remain
near the fountain. If the bird is on the tree branch and decides to fly, there is
a 40% chance that it will go to the fountain and a 60% chance that it will
stay on the tree branch. If the bird decides to rest, it always remains in the

Co-3 ~ | same spot with 100% probability. The bird receives a reward of +5 for every
So-l. action that results in staying on the tree branch and a reward of +1 for every | [5]-
BL-3 action that results in staying near the fountain. The objective is to represent

this situation as a Markov Decision Process (MDP).

i. Develop a state diagram showing transitions and rewards for all
state-action pairs for the above mentioned scenario.
ii. Write p(s',r|s, a) for all the possible state action -
combinations.
c For a Markov Decision Process with the number of time steps T = 5,

sequence of rewards observed are as follows-
_ Ry =—1,Rz = 1,R3 = 5,R, = 7,Rs5 = 10

i. Solve for the returns Gp to Gs with discount factor y = 0.8
CO-3 ii. Solve for the returns Go to Gs with discount factor y = 0.1
SO-1 iii. Compare the returns for both the discount factors and [5]
BL-3,5 comprehend your observations.

Hint: Return G; = Resa + YRevo + ¥7Reta toy” Rr
--- page 5 ---
a Consider the given grid with the following parameters
e States are A to L
e Rewards:
o +40 for target
o -1 for each state
e Actions= {West, East, North, South} as
shown . West
e States with X are obstacles and that action
would be avoided by the agent
e Initial random policy for each state is
mentioned.

© Initial Q value is equal to zero for all the
states :

> East

Apply Exploring Start Monte Carlo Algorithm for an Episode with T=6 and

Q5 initial random state-action as (G, West)

CO-2,4 i. .Generate state-action sequence for this episode for the given policy

SO-1- ii. Discounted return given by equation G = yG + R;41. For discount [10]
BL-4,5 factor y = 0.8, compute discounted return list for the given episode

ili. Obtain the average return list and update the Q value .
iv. Update the policy in the grid

B Cc
>. L
D E
L L
G H
> > L
I J
L at
K L Target
: > 3
b Consider the following environment with four states A, B, C, D.

The state transitions and corresponding rewards collected are as given
below. The current values for each state are also given below. Assume

CO-2,4 ‘learning rate a = 0.2 and discount factor y = 0.8. Evaluate values for all
SO-1_ . the states using TD(0) approach for the following episode-

[10]
BL-2,3
Episode: ADB>ADDDC ;
--- page 6 ---
Environment Transition rewards Initial Values

A B Transition | Rewards | V(A) =4
|| ADB 2 V(B)=2
D C BDA 2 V(C)=4
ADD 3: VDI
D>C 0
i. - Using Temporal Difference TD(0) approach, compute V(A),.
V(B), V(C), and V(D)
ii. Explain the term temporal difference in TD(0) expression

. .| Hint: TD(0) expression

V™(S,) — V™(S,) + a[Regs + YV™ Spar) — VSD]

Q6
CO-2
SO-1
BL-3,4,5

a-

Upper Confidence Bound (UCB) equation is given by

log(t)
A; = argmax,|Q;(a) + N,(a)
Where, .
Q(a) is the estimated value of action ‘a’ at time step ‘t’.
N,(a) is the number of times that action ‘a’ has been selected, prior to .
time ‘t’. : :
c’ is a confidence value
i. State the drawback of € —greedy algorithm and explain how it
can be overcome in UCB.
ii. . Explain exploitation and exploration in the context of the
abovementioned equation. ° _ ;
iii. After 12 iterations of UCB algorithm, applied on 4 arm bandit [10]
problem, we have the number of times each machine was played
N(M,) = 4, N(M2) = 4,N(M3) = 3 and N(M,) =1. Also
values for each machine after 12 iterations are-
Q(M,) = 0.55,Q(M2) = 0.63,Q(M3) = 0.45, Q(M,) = 0.61.
Apply UCB algorithm to identify which machine should be
played next. Consider confidence value c = 2.

Note: Take natural log for all calculations
--- page 7 ---
b Consider the following maze where the agent (at initial state $,) has to
reach the goal state S;,. Rewards for every state are given in the state
diagram as (Sq, Reward). With the following parameters given, evaluate
the value and identify the optimal policy for the next one iteration using
Policy iteration algorithm. ; .

e Actions taken by agent= {L, R}. That means, from state A,
action L takes the agent to state S. and action R takes the agent
to state S;,

e Discount factor y = 0.7

e Probability to go in the intended direction =0.8

¢ Probability to go in the direction other than intended= 0.2
© Initial policy and values as given in the adjacent table

State Sa S, S. Sa Se : Sy So Sh

Initial | 0 0 0 0 0 0 0 0

Value

V(s)
Initial | R R R - R R - -
Policy
Hint: Policy iteration expressions

CO-2,4
SO-1 Policy evaluation: 1
BL-2, 4 Hel

V(s) = 1(s) + y Sery P(s,r]s, (3))¥(s")

Policy improvement:

‘n(s) = argmax, y ic rls, a)Vz(s')

sles :
--- page 8 ---
a Answer the following questions-

Q7 i. With the help of a pseudo-code of explain one step actor critic
CO-5 algorithm .

| SO-1 ii. Explain the role of an actor and a critic and describe how they | [10]
BL-2,3 interact during training :

iii. Compare actor-critic method with REINFORCE method

b- Consider an environment with one state X and two actions associated with
this state {b, c}. Let state T be the terminal state. The temporal difference
(TD) algorithm generates the following episode using policy 7 when
interacting with its environment-

Time Reward State Action
0 . x b
1 12 xX Cc
2 8 x b
3. 12 T
CO-2,4
SO-I
BL-3,4 ° The policy zis given by (b|X) = 0.9, m(clX) = 0.1 [10]

e The current values of q are: Q(X,b) = land Q(X,c) = 2.
e The discount factor y = 0.6 4,
e The step size or learning rate a = 0.1

i. Solve for the values of Q(X, b)and Q(X, c) using one step
SARSA. . :

ii. Differentiate between Q-learning and SARSA algorithms with
reference to their expression, learning approach, policy type,
update rule.

Recall the following expression forSARSA
Q(Sp, At) — Qe, Ae) + ef Rear + YO Star Ares) — OSr Ard]
````

## 2025-26 · Final-Exam · Sem 8 · paper 8d79869bad82

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_DS_7052/Reinforcement Learning/QP_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Instruction....
5. This question paper contains 3 pages.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Question No. 1 is compulsory.
9. Out of remaining questions, attempt any 4 questions.
10. In all 5 questions to be attempted.
11. All questions carry equal marks.
12. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
CO-1;   a   Discuss in detail the application of Reinforcement Learning for HealthCare
SO-1;   by cosidering all the components of RL.   [05]
BL-2
CO-3;   b   Define a Markov Chain. Draw a simple state transition diagram with at
SO-1;   least 3 states and label the transition probabilities.   [05]
BL-2
c   With the help of suitable illustration compare Dynamic Programming
CO-2,4;
Reinforcement Learning approach and Monte Carlo Reinforcement
SO- 1;   [05]
Learning
BL-2
CO-5;   d   Compare value function methods and policy function methods in
SO-1;   Reinforcement Learning, highlighting their main differences.   [05]
BL- 2
Q2   a   How do Immediate and Delayed Reinforcement differ in Reinforcement
CO-1;
Learning? Provide a comparative explanation and support your answer   [10]
SO-1;
BL-2,3   with relevant real-life examples
b   Consider a 4×4 Grid World problem where the goal is to reach either the
top-left corner or the bottom-right corner (refer to the figure). The agent
CO-3
can choose from four actions: Up, Down, Left, Right, which
SO-1;   [10]
deterministically cause the corresponding state transitions, except that
BL-3,4
actions leading outside the grid leave the state unchanged. The task is
modelled as an undiscounted episodic problem (γ = 1) with a reward of −1
********** 1 **********
--- page 2 ---
for all transitions, and the agent follows an equiprobable random policy
(π).
Given the partial value function for this grid, apply and analyse the
Bellman Expectation Equation to compute the missing state values in the
second and fourth rows.
𝑉𝜋(𝑠) = 𝑅(𝑠) + 𝛾∑𝑃(𝑠′|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
𝑠′
a   [10]
In the given example, the robot must move from the Start state 𝑆17 to the
Target state 𝑠0 with a reward structure of +110 for reaching the target and -
2 for each step taken. Assume the initial Q-value to be zero and discount
factor = 0.6. Apply the Monte-Carlo Exploring Starts Algorithm with T=6
and initial random state as (𝑆6, 𝐿) update the policy for given episode E1 and
E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.6, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Q3
CO-2,4;   E1: (𝑺𝟖, 𝑫) → (𝑆12, 𝑈) →(𝑆8, 𝑈) →(𝑆4, 𝐿) →(𝑆3, 𝑅) →(𝑆4, 𝐿) →
SO-1   (𝑆3, 𝑅)
BL-4,5
E2: (𝑺𝟔, 𝑳) →(𝑆5, 𝑅) →(𝑆6, 𝑅) →(𝑆7, 𝑈) →(𝑆2, 𝐿) →(𝑆1, 𝐿) →
(𝑠0, 𝑠𝑡𝑜𝑝)
Targe
t S0   S1   S2   S3   S4
S5   S6   S7   S8
S9   S10   S11   S12
S13   S14   S15   S16   S17
********** 2 **********
--- page 3 ---
CO-2,4   b   Explain the Value Iteration algorithm used in Dynamic Programming for
SO-1   solving MDPs. Provide the pseudo-code and describe it’s working.
[05]
BL-2
CO-2,4   c   Differentiate between on-policy and off-policy reinforcement learning methods.
Also, explain how importance sampling is used in off-policy learning with a
SO-1   suitable example.   [05]
BL-2,3
a   Consider a Multi-Armed Bandit problem with the following parameters:
Time step t = 5
Number of bandits (machines) = 4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
Q4
The probability of winning for each machine is:
CO-2
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
SO-1   [10]
BL-3,4
Assume that the random number generated for selection of one machine in
the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
b   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 7, R₂ = -2, R₃ = 5, R₄ = 3, R₅ = 2
CO-3   i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.9
SO-1   [05]
ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.3
BL-3
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
c   A delivery drone operates between Warehouse (S1) and Customer (S2). It
can Deliver or Wait. From Warehouse: Deliver → 0.8 reach Customer, 0.2
stay
From Customer: Deliver → 0.3 return to Warehouse, 0.7 stay Wait →
CO-3   stays in same location
SO-1   Rewards: +6 for Customer and +2 for Warehouse   [05]
BL-3
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
********** 3 **********
--- page 4 ---
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states X and Y and a terminal state T. Assume that the following
two episodes are observed.
Assume the discount factor γ = 0.9.
Episode 1: X 3 X 2 Y 4 T
Q5
Episode 2: Y 2 X 5 Y 1 T
CO-2,4
Estimate the state value for both states X and Y using First Visit Monte
SO-1   [10]
Carlo algorithm.
BL-3,4
Estimate the state value for both states X and Y using Every Visit Monte
Carlo algorithm.
Construct Markov model that best explains the above scenario.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
b   Consider the following environment with four states P, Q, S, R.
The state transitions and corresponding rewards collected are as given
below. The current values for each state are also given below. Assume
learning rate 𝛼= 0.3 and discount factor 𝛾= 0.7. Evaluate values for all
the states using TD (0) approach for the following episode-
Episode: P→Q→R→S→P
Environment   Transition rewards   Initial Values
CO-2,4   P   Q   Transition Rewards V(P) =3
SO-1   P→Q   4   V(Q)=5   [10]
BL-2,3   R   S   Q→R   1   V(R)=2
R→S   -3   V(S)=4
S→P   2
i.   Using Temporal Difference TD (0) approach, compute V(P),
V(Q), V(R), and V(S)
ii.   Explain the term temporal difference in TD (0) expression
Hint: TD (0) expression
𝑉𝜋(𝑆𝑡) ←𝑉𝜋(𝑆𝑡) + 𝛼(𝑅𝑡+1 + 𝛾𝑉𝜋(𝑆𝑡+1) −𝑉𝜋(𝑆𝑡))
a   Describe the Upper Confidence Bound (UCB) method for action selection
Q6
in reinforcement learning. Apply the UCB formula to explain how it
CO-2
balances exploration and exploitation.
SO-1   [10]
Analyse its advantages over ε-greedy strategy and evaluate its
BL-3,4,5
effectiveness in scenarios with limited data and high uncertainty.
b   A food relief vessel is stationed near a disaster-hit region. It must reach its
base safely and can move only in East and West directions.
CO-2,4   The possible routes are—
SO-1   Go to Food Warehouse, collect supplies and then go to Home (East →
[10]
BL-2, 4   West)
Go to Backup Storage, collect food and then go to Home (West → East)
Go directly to home
Dangers:
********** 4 **********
--- page 5 ---
There is a contaminated zone to the East of the Food Warehouse
There is a pirate zone to the West of the Backup Storage
Uncertainty:
Intended direction = 0.7
Opposite direction = 0.3
Assume:
Initial policy: Move East
Initial values = 0
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   Sta Wareho Backup   Ho   Contaminated   Pirate
rt   use   Storage   me   Zone   Zone
Reward   0   +12   +6   +4   −110   −80
Values   0   0   0   0   0   0
Initial   E   E   E   –   –   –
Policy
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
Q7   a   Explain how the Actor and Critic collaborate to improve the policy in
CO-5   Reinforcement Learning, using appropriate pseudocode.
SO-1   ii. Differentiate between the Actor-Critic method and the REINFORCE   [10]
BL-2,3   algorithm, highlighting their differences.
b   i.   With help of a pseudo code, explain SARSA TD control
algorithm.
Consider the following Q [S, A] table:
CO-2,4
SO-1   State 1   State 2   [10]
BL-3,4
Action 1   3.0   5.0
Action 1   7.0   4.0
Assume that 𝛼= 0.3, 𝑎𝑛𝑑 𝛾= 0.6
********** 5 **********
--- page 6 ---
ii.   After the experience < 1,1,8,2,2 > for ⟨S, A, R, S’, A’⟩,
which value of the table gets updated and what is its new
value?
iii.   “SARSA is called an on-policy TD control algorithm” State
true or false and justify the same.
Hint: SARSA learning algorithm is given by the following equation:
𝑄( 𝑆𝑡, 𝐴𝑡) ← 𝑄( 𝑆𝑡, 𝐴𝑡) + 𝛼 [𝑅𝑡+1 + 𝛾𝑄( 𝑆𝑡+1, 𝐴𝑡+1) − 𝑄( 𝑆𝑡, 𝐴𝑡)].
********** 6 **********
````

## 2025-26 · Final-Exam · paper 598bc2ccda42

- Departments: Artificial Intelligence
- Programmes: MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/Artificial Intelligence/Reinforcement Learning/Reinforcement Learning, 2025-26 Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (8 pages), mean OCR confidence 87.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENG
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2025-2026 "Me
Program/s: B.Tech/MBA Tech Year: [V Semester:
Stream/s ; DS/AI/AIML
Subject: Reinforcement Learning . Time: 3 hrs (Jos00anto 4 500Pm)
Date:__2 / 12/2025 No. of Pages: 8 ~
Marks: 100 |

Final Examination(a5~ 26)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

at Answer briefly: - [20]
CO-1; a . r . . ‘
SO-1: With reference to Reinforcement Learning, .discuss exploration and
BL-2. exploitation trade-off with suitable example.
CO-3; b as ;
SO-1: Define Markov Decision Process (MDP) with reference to rewards,
BL2. transition model, discount factor, horizon, goal.
c In the context of Reinforcement Learning, discuss the key points of
© | CO-2,4; : ; enue Rin eos

SO- |: Dynamic Programming approach, highlighting its significance. Compare
BL2 > Dynamic Programming with Monte Carlo approach in terms of model

requirement, type of value update and convergence. ;
CO-S; d Explain policy gradient approach in reinforcement learning. State the
SO-1 ; advantages of using parameterized policy instead of a tabular one.
BL-2

i t
1
,
--- page 2 ---
Q2 a With the help of suitable examples, define the following goncepts in
CO-1; reinforcement learning-

SO-1; Agent, Environment, State, Action, Reward, Policy, Reward, Episode, Le
BL-2 Value function, Model.
b Consider the following environment with states and rewards as mentioned.

Each arrow indicates the allowed movement direction and the immediate

reward received upon moving to the next state. Reaching the goal state I
yields a reward of +10. This is the terminal state and its value is 0. Assume
that the actions are deterministic (that means the agent always moves in the
indicated direction).

A D |“"+| G

-1 | |-4 1

B £ 4

2 | | -2 10 |

-2
C - |
CO-3 (Goal)
SO-1; [10]
BL-4,5 Apply the Bellman equation V(s) = R(s,a,s') + yV(s’),

i. Evaluate value V(s) for all the states except the terminal state
for discount factor y = 0.9. Show the steps.
ii. Evaluate value V(s) for all the states except the terminal state
for discount factor y = 0.1. Show the steps.
iii. Comprehend your observations based on evaluation done for
both the discount factors.
Note: Work backwards from terminal state to calculate value and complete
the following table.
State S Values V(s) | Values V(s)
y= 0.9 y = 0.1
I Vd) =0 VG) =0
--- page 3 ---
om

»

Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states A and B and a terminal state T. Assume that the following
two episodes are observed when Monte-Carlo evaluation is being carried
out. The numbers within the episodes denote the rewards that are collected
during the transition. For example, Episode | the agent starts with state A,
then goes to state A again, then to B, and B again and then terminates: Orr
the way, the agent collects the rewards of 2, 6, 1 and 0 respectively.
Assume the discount factor to be y = 0.7.

OF oa: Episode 1:A2A6B1BOT
SO-1. > Episode 2:B3 B6A1B0T [10]
BL-4,5 . . . .
> i. Estimate the state value for both the states A and B using First
Visit Monte Carlo algorithm.

ii. Estimate the state value for both the states A and B using Every
Visit Monte Carlo algorithm.

iii. Construct Markov model that best explains the above scenario.

Hint:

Return Gp = Rey + YRea2 + ?Reag toy? Rp
CO-2,4
SO-1 With referenae to Dynamic Programming approach, explain pseudo-~ -code [5]
BL2 of Value Iteration algorithm.
CO-2,4 . , ; .
SO-1 Compare on-policy and off-policy methods. Discuss off policy method [5]
BL-2,3 with importance sampling technique.

i. Discuss the pseudo-code for Epsilon greedy Multi Arm Bandit
Algorithm.

ii. A 3-armed bandit problem is initialized with action-value
estimates Q(a)=0 for all. actions. Using the Epsilon-greedy
action selection strategy with Epsilon € =0.1, the following

Q4 sequence of actions and rewards is observed: (Aj, 2), (Az, 3),
CO-2 (Az,1), (Az2,3), (Az, 2).Using the incremental update formula,

SO-1 calculate the action-value estimates Q(a) after each step and | [10]
BL-3,4

complete the table below. Assume N(a) = 1 for step 0 for all
the actions.

iii. Identify the greedy action would be selected for step 6
--- page 4 ---
Step | Action | Reward Q(Ax) | Q(A2) | Q(A3) | Reason why

selected | observed ‘thé next
action was
. selected
0 0 0 0
1 Ay 2
2 Az* | 3
3 Az 1 ;
4 Ag 3
5 A3 2

Hint: Incremental update is given by

Qn+1(a) = Qn (a) +77 a ) [Rn ~ Qn(a)]

b A bird lives in a park that has two favorite spots — one near the fountain
and another on a tree branch. At each step, the bird can choose to either fly
or rest. If the bird is near the fduntain and decides to fly, there is a 70%
chance that it will reach the tree branch and a 30% chance that it will remain
near the fountain. If the bird is on the tree branch and decides to fly, there is
a 40% chance that it will go to the fountain and a 60% chance that it will
stay on the tree branch. If the bird decides to rest, it always remains in the

CO-3 same spot with 100% probability. The bird receives a reward of +5 for every
SO-1 action that results in staying on the tree branch and a reward of +1 for every | [5]
BL-3 action that results in staying near the fountain. The objective is to represent

this situation as a Markov Decision Process (MDP).

i. Develop a state diagram showing transitions and rewards for all
state-action pairs for the above mentioned scenario.

ii. Write p(s’, r|s, a) for all the possible state action -
combinations.

c For a Markov Decision Process with the number of time steps T = 5,
sequence of rewards observed are as follows-
R, =—1,Rp =1,R3 =5,R, =7,Rs = 10

i. Solve for the returns Gp to Gs with discount factor y = 0.8
CO-3 ii. Solve for the returns Gp to Gs with discount factor y = 0.1
SO-1 iii. Compare the returns for both the discount factors and [5]
BL-3,5 comprehend your observations.

Hint: Return G; = Rear + VRea2 t+ V7 Rag Hoey OTR
--- page 5 ---
a Consider the given grid with the following parameters
e States are A to L
e Rewards:
o +40 for target

o -1 for each state North
e Actions= {West, East, North, South} as
shown’ West East

e States with X are obstacles and that action
would be avoided by the agent

e Initial random policy for each state is
mentioned.

e Initial Q value is equal to zero for all the
states

South

Apply Exploring Start Monte Carlo Algorithm for an Episode with T=6 and

Q5 initial random state-action as (G, West)

CO-2,4 i.. Generate state-action sequence for this episode for the given policy

SO-1- ii. Discounted return given by equation G = yG + Re41. For discount [10]
BL-4,5 factor y = 0.8, compute discounted return list for the given episode

iii. Obtain the average return list and update the Q value
iv. | Update the policy in the grid

A B Cc
> | > L
D E
L L
F G H
> > i
I J
L dt
Kk L Target
~ >
b Consider the following environment with four states A, B, C, D.

The state transitions and corresponding rewards collected are as given
below. The current values for each state are also given below. Assume

CO-2,4 ‘learning rate @ = 0.2 and discount factor y = 0.8. Evaluate values for all
SO-1 the states using TD(0) approach for the following episode-
BL-2, 3 [10]

Episode: ADB>ADDDC
--- page 6 ---
Environment Transition rewards Initial Values
= ¥

A B Transition | Rewards | V(A) =4
ADB 2 V(B)=2
D Cc BOA -2 V(C)=4
ADD 3 Vv(D)1
. DSC 0
i. Using Temporal Difference TD(0) approach, compute V(A),
V(B), V(C), and V(D)
ii. Explain the term temporal difference in TD(0) expression

Hint: TD(0) expression
V™(St) — V™(St) + @[Reaa + YV™ Staa) — V"(Sz)]

a Upper Confidence Bound (UCB)-equation is given by

log(t)
N,(@)

At = argmax,|Q,(a) +c

Where,
Q,(a) is the estimated value of action ‘a’ at time step ‘t’.
N,(a) is the number of times that action ‘a’ has been selected, prior to

time ‘t’.

‘c’ is a confidence value

i. State the drawback of € —greedy algorithm and explain how it

can be overcome in UCB.

Q6 ii. Explain exploitation and exploration in the context of the
Cco-2 abovementioned equation.
SO-1 iii. After 12 iterations of UCB algorithm, applied on 4 arm bandit [10]
BL-3,4,5 problem, we have the number of times each machine was played

N(M,) = 4, N(M2) = 4,N(M3) = 3 and N(M,) = 1. Also
values for each machine after 12 iterations are-
Q(M,) = 0.55,Q(M2) = 0.63,Q(M3) = 0.45, Q(M,) = 0.61.
Apply UCB algorithm to identify which machine should be
played next. Consider confidence value c = 2.

Note: Take natural log for all calculations
--- page 7 ---
sd ro

Consider the following maze where the agent (at initial state Sz) has to
reach the goal state S,. Rewards for every state are given in the state
diagram as (Sg, Reward). With the following parameters given, evaluate
the value and identify the optimal policy for the next one iteration using
Policy iteration algorithm.
° Actions taken by agent= {L, R}. That means, from state A,
action L takes the agent to state S, and action R takes the agent
to state S,
e Discount factor y = 0.7
e Probability to go in the intended direction =0.8
e Probability to go in the direction other than intended= 0.2
e Initial policy and values as given in the adjacent table
State Sq S) S, Sa Se Sy Sy Sp

Initial | 0 0 0 0 0 0 0 0
Value

V(s) .
Initial | R R R - R R - -
Policy

Hint: Policy iteration expressions

Policy evaluation: ;
V(s) = r(s) + VY Ustr P(s',r

s,1(s))V_(s’)

Policy improvement:
m(s) = argmax, y » p(s’, rls, a)V,(s")

s'ES

q

*

[10]

Ps
--- page 8 ---
a Answer the following questions- a;

Q7 is With the help of a pseudo-code of explain one step actor critic

CO-5 algorithm

SO-1 ii. Explain the role of an actor and a critic and describe how they [10]
BL-2,3 interact during training

iii. Compare actor-critic method with REINFORCE method

b Consider an environment with one state X and two actions associated with
this state {b,c}. Let state T be the terminal state. The temporal difference
(TD) algorithm generates the following episode using policy z when
interacting with its environment-

Time Reward State Action

0 Xx b

1 12 Xx c

2 8 X b

3 12 T
CO-2,4
SO-I [10
BL-3,4 e The policy 7 is given by 1(b|X) = 0.9, m(c|X) = 0.1 ]

¢ The current values of q are: Q(X,b) = 1 and Q(X,c) = 2.
e The discount factor y = 0.6
¢ The step size or learning rate a = 0.1

i, Solve for the values of Q(X, b)and Q(X, c) using one step
SARSA.

ii. Differentiate between Q-learning and SARSA algorithms with
reference to their expression, learning approach, policy type,
update rule.

‘

Recall the following expression for SARSA
Q(Se,At) — Q(St,At) + @[Resa +¥QSria Arer) — Q(St,A1)]
````

## 2025-26 · Re-Exam · Sem 8 · paper e88d3b1525a0

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_DS_7052/Reinforcement Learning/QP_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Instruction....
5. This question paper contains 3 pages.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Question No. 1 is compulsory.
9. Out of remaining questions, attempt any 4 questions.
10. In all 5 questions to be attempted.
11. All questions carry equal marks.
12. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a
CO-1;   Discuss in detail the application of Reinforcement Learning for Trading
SO-1 ;   and Finances by cosidering all the components of RL.   [05]
BL-2
CO-3;   b   Define Markov Decision Process (MDP) with reference to rewards,
SO-1;   transition model, discount factor, horizon, goal.   [05]
BL-2
c
CO-2,4;   With reference to Dynamic Programming and Monte Carlo approaches,
SO- 1;   explain the concepts of model-based and model-free reinforcement   [05]
BL-2   learning.
d   Write the pseudocode for the Naive REINFORCE algorithm. State the
CO-5;   weight update rule used in REINFORCE and explain the role of each term
SO-1;   in the expression.   [05]
BL-2
a   Explain the concepts of Immediate Reinforcement and Delayed
Q2
Reinforcement in Reinforcement Learning (RL). Compare the two
CO-1;
SO-1;   approaches and illustrate their importance using suitable real-world   [10]
BL-2   examples.
b   Consider a 4×4 Grid World problem where the goal is to reach either the
CO-3
top-left corner or the bottom-right corner (refer to the figure). The agent
SO-1;   [10]
can choose from four actions: Up, Down, Left, Right, which
BL-3,4
deterministically cause the corresponding state transitions, except that
********** 1 **********
--- page 2 ---
actions leading outside the grid leave the state unchanged. The task is
modelled as an undiscounted episodic problem (γ = 1) with a reward of −1
for all transitions, and the agent follows an equiprobable random policy
(π).
Given the partial value function for this grid, apply and analyse the
Bellman Expectation Equation to compute the missing state values in the
first and third rows, Hint: 𝑉𝜋(𝑠) = 𝑅(𝑠) + 𝛾∑ 𝑠′ 𝑃(𝑠′|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states C and D and a terminal state T. Assume that the following
two episodes are observed when Monte-Carlo evaluation is being carried
out. The numbers within the episodes denote the rewards collected during
transitions.
Assume the discount factor γ = 0.6.
Q3
Episode 1: C 2 D 4 C 3 D 1 T
CO-2,4;
Episode 2: D 5 C 2 D 2 C 0 T   [10]
SO-1
BL-4,5
1. Estimate the state value for both states C and D using First Visit
Monte Carlo algorithm.
2. Estimate the state value for both states C and D using Every Visit
Monte Carlo algorithm.
3. Construct Markov model that best explains the above scenario.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
CO-2,4   b
Describe the Policy Iteration algorithm in the context of Dynamic
SO-1
Programming. Illustrate your answer with appropriate pseudo-code.   [05]
BL-2
c   Define on-policy and off-policy learning in the context of Monte Carlo
CO-2,4
methods. Give one real-world example of each. Explain the role of the
SO-1   [05]
behavior policy and the target policy in off-policy Monte Carlo learning.
BL-2,3
Q4   a   Consider a Multi-Armed Bandit problem with the following parameters:
CO-2
SO-1   Time step t = 5   [10]
BL-3,4   Number of bandits (machines) = 4
********** 2 **********
--- page 3 ---
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
The probability of winning for each machine is:
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
Assume that the random numbers generated for selection of machines for
five iterations are:
[0.68, 0.55, 0.23, 0.95, 0.80]
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for each of the five iterations:
[0.60, 0.20, 0.30, 0.40, 0.90]
b   A robot operates in a house with two areas: Living Room (S1) and Kitchen
(S2). At each step, the robot can either Clean or Stay Idle.
From Living Room: Clean → 0.6 chance to move to Kitchen, 0.4 stay in
Living Room
From Kitchen: Clean → 0.5 chance to move to Living Room, 0.5 stay in
Kitchen
CO-3   Stay Idle → remains in same state
SO-1   Rewards: +4 for ending in Kitchen and +2 for ending in Living Room   [05]
BL-3
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
c   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 5, R₂ = 4, R₃ = 3, R₄ = 2, R₅ = 1
i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.8
CO-3
ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.2
SO-1   [05]
iii.   Compare the returns for both the discount factors and
BL-3,4
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
a   In the given example, the robot must move from the Start state 𝑆17 to the [10]
Target state 𝑠0 with a reward structure of +90 for reaching the target and
-1 for each step taken. Assume the initial Q-value Q(s,a) to be zero and
Q5   discount factor = 0.6. Apply the Monte-Carlo Exploring Starts Algorithm
CO-2,4   with T=6 and initial random state as (𝑆6, 𝐿) update the policy for given
SO-1   episode E1 and E2.
BL-3, 4
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.6, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
********** 3 **********
--- page 4 ---
Episode E1:
(S₉,U) → (S₅,R) → (S₆,U) → (S₂,L) → (S₁,R) → (S₂,L) → (S₁,R)
Episode E2:
(S₆,D) → (S₁₀,U) → (S₆,R) → (S₇,U) → (S₂,L) → (S₁,L) → (S₀,stop)
Targ
et S0   S1   S2   S3   S4
S5   S6   S7   S8
S9   S10   S11   S12
S13   S14   S15   S16   S17
b   Consider an environment with three states: X, Y, and Z.
There is only one action available, which deterministically moves the agent
to the next state.
Rewards:
Transition from X → Y gives a reward of 2
Transition from Y → Z gives a reward of 5
Transition from Z → Terminal gives a reward of 3
Given:
CO-2,4   Discount factor γ=0.9, Learning rate α=0.2, Initial values:
SO-1   V(X)=V(Y)=V(Z)=0
[10]
BL-2, 3
Tasks:
i.   Compare TD (0) and TD (1) approaches.
ii.   Apply Temporal Difference TD (1) to compute: V(X), V(Y),
V(Z)
(show return calculation for each state)
Hint: Value expression for TD (1) approach is –
𝑉(𝑆𝑡) = 𝑉(𝑆𝑡) + 𝛼(𝐺𝑡−𝑉(𝑆𝑡))
where,
𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
a   Describe the Upper Confidence Bound (UCB) method for action selection
Q6   in reinforcement learning. Apply the UCB formula to explain how it
CO-2   balances exploration and exploitation.
SO-1   Analyse its advantages over ε-greedy strategy and evaluate its   [10]
BL-3,4,5   effectiveness in scenarios with limited data and high uncertainty.
********** 4 **********
--- page 5 ---
b   A chemical supply vessel is anchored near an industrial zone. It has to
reach its home base safely and it can only take two directions, namely, East
and West.
The possible routes the vessel can take are:
Go to Chemical Depot, collect chemicals and then go to Home (Move
East, then West)
Go to Gas Storage Terminal, collect gas and then go to Home (Move West,
then East)
Go to home directly
There are two dangers in the first two routes:
There is a toxic leak zone to the East of the Chemical Depot
There is a military restricted zone to the West of the Gas Terminal
There is uncertainty in directions:
Probability of intended direction = 0.7
Probability of opposite direction = 0.3
Assume:
CO-2,4
SO-1   Initial policy: Move East
BL-2, 4   Initial values = 0   [10]
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   St   Chemical   Gas   Ho   Toxic   Restricted
art Depot   Terminal me   Zone   Zone
Reward   0   +15   +8   +5   −120   −90
Values   0   0   0   0   0   0
Initial   E   E   E   –   –   –
Policy
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
********** 5 **********
--- page 6 ---
a   Attempt the following:
Q7   i.   Explain the one-step Actor-Critic algorithm.
CO-5   ii.   Describe the roles of the Actor and the Critic, and explain
SO-1   how they work together during the training process.   [10]
BL-2,3   iii.   Compare the Actor-Critic method with the REINFORCE
algorithm, highlighting key differences.
b   i.   With help of a pseudo code, explain SARSA TD control
algorithm.
Consider the following Q[S, A] table:
State 1   State 2
Action 1   2.5   6.0
Action 1   4.5   3.5
CO-2,4
Assume that 𝛼= 0.4, 𝑎𝑛𝑑 𝛾= 0.5
SO-1
[10]
BL-3,4
ii.   After the experience < 2,1,5,1,2 > for ⟨S, A, R, S’, A’⟩, which
value of the table gets updated and what is its new value?
iii.   “SARSA is called an on-policy TD control algorithm” State
true or false and justify the same.
Hint: SARSA learning algorithm is given by the following equation:
𝑄( 𝑆𝑡, 𝐴𝑡) ← 𝑄( 𝑆𝑡, 𝐴𝑡) + 𝛼 [𝑅𝑡+1 + 𝛾𝑄( 𝑆𝑡+1, 𝐴𝑡+1) − 𝑄( 𝑆𝑡, 𝐴𝑡)]
********** 6 **********
````

## 2025-26 · Re-Exam · paper 4bd8bd69cf36

- Departments: Data Science
- Programmes: MBA TECH / Data Science
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/Data Science/Reinforcement Learning/Reinforcement Learning, Sem-VIII, Batch 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: ocr (6 pages), mean OCR confidence 86.1

````text
">

Programme: MASTER OF BUSINESS ADMINISTRATION IN TE

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-If

MANAGEMENT (DATA SCIENCE)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)

Subject: Reinforcement Learning

Date: 09 Jul 2026
Max. Marks: 100

Instructions:

Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

RE EXAMINATION (Acad. Year:2025-2026)

1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks

4. Instruction...

5. This question paper contains 3 pages.

6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks

8. Question No. 1 is compulsory.

9. Out of remaining questions, attempt any 4 questions.

10. In all 5 questions to be attempted.

11. All questions carry equal marks.

12. Assume Suitable data if necessary.

Ql

Answer briefly: [20]

CO-1; a Discuss in detail the application of Reinforcement Learning for Trading
SO-1 ; and Finances by cosidering all the components of RL. : [05]
BL-2
CO-3; b Define Markov Decision Process (MDP) with reference to rewards,
BO-1g transition model, discount factor, horizon, goal. [05]
BL-2

c
CO-2,4; With reference to Dynamic Programming and Monte Carlo approaches,
SO- 1; explain the concepts of model-based and model-free reinforcement ° [05]
BL-2 learning.

d Write the pseudocode for the Naive REINFORCE algorithm. State the
CO-5; weight update rule used in REINFORCE and explain the role of each term
ee in the expression. [05]
Q2 a Explain the concepts of Immediate Reinforcement and Delayed
CO-L: Reinforcement in Reinforcement Learning (RL). Compare the. two
SO-1 : approaches and illustrate their importance using suitable real-world [10]
BL-2 examples.
cO03 b Consider a 4x4 Grid World problem where the goal is to reach either the
S0-1: top-left corner or the bottom-right corner (refer to the figure). The agent [10]
BL3 > af can choose from four actions: Up, Down, Left, Right, which

deterministically cause the corresponding state transitions, except that

FOI ICI aOR a a kk
--- page 2 ---
actions leading outside the grid leave the state unchanged. The task is

modelled as an undiscounted episodic problem (y = 1) with a reward of —1

for all transitions, and the agent follows an equiprobable random policy

(a). e : °

Given the partial value function for this grid, apply and analyse the ~
Bellman Expectation Equation to compute the missing state values in the
first and third rows, Hint: V"(s) = R(s) +y Yer P(s' ls, m(s))V™(s")

Table 1: 4 x 4 Grid-world
10 | 2 | -20| -22

-14 | -18 | -20
? | -20 | -18 | -14
-22 | -20

a Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states C and D and a terminal state T. Assume that the following
two episodes are observed when Monte-Carlo evaluation is being carried
out. The numbers within the episodes denote the rewards collected during ny
transitions. :

Assume the discount factor y = 0.6.

Ca Episode 1:C2D4C3D1T
SO-1 , Episode 2: D5C2D2C0T [10]
BL-4,5 . . , -

1. Estimate the state value for both states C and D using First Visit

Monte Carlo algorithm.
2. Estimate the state value for both states C and D using Every Visit
Monte Carlo algorithm.
3. Construct Markov model that best explains the above scenario.
Hint:
Return G = Rrey + VRea2 +? Rigg toy Ry
soa” 5 Describe the Policy Iteration algorithm in the context of Dynamic
BL-2 Programming. Illustrate your answer with appropriate pseudo-code. [05]
CO-2.4 c Define on-policy and off-policy learning in the context of Monte Carlo
° methods. Give one real-world example of each. Explain the role of the

ee behavior policy and the target policy in off-policy Monte Carlo learni [05]
BL-2,3 policy get policy policy earning.
Q4 a Consider a Multi-Armed Bandit problem with the following parameters:
CO-2 .
SO-1 Time step t= 5 [10]
BL-3,4 Number of bandits (machines) = 4

FRAG Ae
--- page 3 ---
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1

The probability of winning for each machine is:
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9

Assume that the random numbers generated for selection of machines for
five iterations are:
[0.68, 0.55, 0.23, 0.95, 0.80]

Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for each of the five iterations:
[0.60, 0.20, 0.30, 0.40, 0.90]

b A robot operates in a house with two areas: Living Room (S1) and Kitchen
(S2). At each step, the robot can either Clean or Stay Idle.
From Living Room: Clean — 0.6 chance to move to Kitchen, 0.4 stay in
Living Room
From Kitchen: Clean — 0.5 chance to move to Living Room, 0.5 stay in
Kitchen

(>) CO-3 Stay Idle — remains in same state ,
a Rewards: +4 for ending in Kitchen and +2 for ending in Living Room [05]
i. Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
il. Write p(s’,r|s, a) for all the possible state action combinations.
c For a Markov Decision Process with the number of time steps T = 5,
sequence of rewards observed are as follows:
Sequence of rewards: Ri = 5, Ro = 4, Rs =3, Ra =2, Rs =1
i. Solve for the returns Gy to Gs with discount factor y = 0.8
Sod il. Solve for the returns Gy to Gs with discount factor y = 0.2
SO-1 “ ‘ [05]
BL-3.4 iil. Compare the returns for both the discount factors and
° comprehend your observations.
a Hint: Return G, = Ris, + VReg2 FY? Reg toy? OI Re
a In the given example, the robot must move from the Start state S,7 to the | [10]
Target state sg with a reward structure of +90 for reaching the target and
¥ -1 for each step taken. Assume the initial Q-value Q(s,a) to be zero and
Q5 discount factor = 0.6. Apply the Monte-Carlo Exploring Starts Algorithm
CO-2,4 with T=6 and initial random state as (S¢,L) update the policy for given
SO-1 episode El and E2. .
BL-3, 4

i.. Discounted return given by equationG = yG + R,,,. For discount
factor y = 0.6, compute discounted return list for the given episode
ii. Obtain the average return list and update the Q value
iii. _ Update the policy in the grid

FOR doi a a ao ok
--- page 4 ---
Episode E1:

(So,U) — (Ss,R) — (S6,U) — (S2,L) > (Si,R) > (S2,L) > (Si,R)
Episode E2: .
(Ss,D) — (S10,U) > (Ss,R) — (S2,U) — (S2,L) — (Si,L) — (So,stop)

Targ | om | Gon | > | Gomm

et So Si So S83 S4

=> ad ts 7

Ss

11

Sio oe S2
t= 39> —

Si3 Sia Sis Sie Si

b Consider an environment with three states: X, Y, and Z.
There is only one action available, which deterministically moves the agent
to the next state.
» a

Rewards:

Transition from X — Y gives a reward of 2
Transition from Y — Z gives a reward of 5
Transition from Z — Terminal gives a reward of 3

Given:
CO-2,4 Discount factor y=0.9, Learning rate a=0.2, Initial values:
SO-1 V(X)=V(Y)=V(Z)-0 110)
BL-2, 3 —
Tasks:
1. Compare TD (0) and TD (1) approaches.
ii. Apply Temporal Difference TD (1) to compute: V(X), V(Y),
V(Z)
(show return calculation for each state)
Hint; Value expression for TD (1) approach is — .
V(S_) = V(S,) + a(G; — V(S,))
where,

Gp = Rear + VRea2 FY? Reag toy IR

a Describe the Upper Confidence Bound (UCB) method for action selection
Q6 in reinforcement learning. Apply the UCB formula to explain how it
CO-2 balances exploration and exploitation.
SO-1 Analyse its advantages over €-greedy strategy and evaluate its [10]
BL-3,4,5 effectiveness in scenarios with limited data and high uncertainty.

FOO OAK
--- page 5 ---
a

CO-2,4
SO-1
BL-2, 4

A chemical supply vessel is anchored near an industrial zone. It has to
reach its home base safely and it can only take two directions, namely, East
and West.

The possible routes the vessel can take are: °

Go to Chemical Depot, collect chemicals and then go to Home (Move
East, then West)

Go to Gas Storage Terminal, collect gas and then go to Home (Move West,
then East)

Go to home directly

There are two dangers in the first two routes:

There is a toxic leak zone to the East of the Chemical Depot
There is a military restricted zone to the West of the Gas Terminal
There is uncertainty in directions:

Probability of intended direction = 0.7
Probability of opposite direction = 0.3

Assume: 7
Initial policy: Move East
Initial values = 0

State Table .
States Sl | 82 S3 S4 | S5 S6
Meaning | St’ | Chemical Gas Ho | Toxic Restricted

art | Depot Terminal | me | Zone Zone

Reward | 0 | +15 +8 +5 | -120 —90
Values 0 |0 0 0 0 0
Initial E |E E - - _
Policy

Hint: Policy iteration expressions

Policy evaluation:
Ve = 1(s) + vYstx PCs’ r|s, w(s))VY(s")

Policy improvement:
m(s) = argmax, »y p(s',r|s,a)V,(s')
s'eS
State Diagram:

[10]

FOR RR ar
--- page 6 ---
. -

$4,
+5

a Attempt the following:
Q7 is Explain the one-step Actor-Critic algorithm.
CO-5 il. Describe the roles of the Actor and the Critic, and explain
SO-1 how they work together during the training process. [10]
BL-2,3 iii. Compare the Actor-Critic method with the REINFORCE

algorithm, highlighting key differences.

b i. With help of a pseudo code, explain SARSA TD control
algorithm.

Consider the following Q[S, A] table:

State 1 State 2
Action 1 2.5 6.0
Action | 4.5 3.5
CO-2,4 _ _
SO-1 Assume that a = 0.4,andy = 0.5

BL-3,4 [10]
il. After the experience < 2,1,5,1,2 > for (S, A, R, S’, A’), which
value of the table gets updated and what is its new value?
iil. “SARSA is called an on-policy TD control algorithm” State
true or false and justify the same.

Hint: SARSA learning algorithm is given by the following equation:

QOS Ad) — QCSp A) + @ Re + YQ Star, Ats1) — QS, Ad]

FOG 6 OE
````

## 2024-25 · Final-Exam · Sem 6 · paper 33dd805ed8f5

- Departments: Artificial Intelligence, Computer Engineering, Data Science
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/REINFORCEMENT LEARNING/Reinforcement Learning, Sem VI, Final Exam 2024-25.pdf` (+2 identical copies)
- Printed on paper: duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 89.9
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: MBA Tech/ B Tech (Intgs) Stream/s : AIDS/DS/COMP Year: IIVIV/VI Semester: VI/VILI/XII
Subject: Reinforcement Learning Time: 3hrs(lot00am to Leeopr)
Date:_08/05 / 2025 No. of Pages:05

Marks: __100

Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4__ questions.

3) In all __5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
CO-: a. | Explain the Upper-Confidence-Bound (UCB) algorithm in Multi-
SO-1; Armed Bandits. How it balances exploration and exploitation better
BL-2 than e-greedy methods.
b. | Consider an agent starting in a state A where it can take two possible
actions: move forward (action “F”) or wait (action “W”’). If it selects
“F”, the agent moves to state B, which is a terminal state (no further
CO.2; actions can be taken). If “W” action is selected in state A, the agent
SO- 1; will stay in A with a probability of 0.7, or the agent will go to state B
BL-3 with a probability of 0.3. We assume that the reward for reaching
state B is R(B) = +1.5 and the reward for staying in state A is R(A)
= —0.05. Draw the state diagram for the given Markov Decision
Process (MDP).
c. | List key components of Reinforcement Learning involved in skill
i : ‘ improvement for the following scenario: Consider a student learning
BL-i

to solve mathematical problems. Apply the concepts of
--- page 2 ---
Reinforcement Learning (RL) to explain how trial and error, rewards
(positive reinforcement), penalties (negative reinforcement),
learning, and optimization play a role in improving their problem-

solving skills.

CO-3; | d. | Explain how Value Iteration and Policy Iteration work in Dynamic
St Programming. Describe the main steps involved in each method.
a_ | Using Python
Evaluate how different discount factors (y = 0.1, 0.5, 0.9, 1.0) affect 110)
an RL agent’s decision-making in a reward-based environment with
rewards = [10, 20, 36, 40].
Q2 b | Using python
CO-1,4; Compute the value function for a given policy in a simple 3-state
om 5 MDP? with known transition probabilities and rewards.
Given: P = £0: {0: [(1, 1, 5)], 1: (1, 2, -D]}, [10]
1: {0: [(1, 0, 2)}, 1: [C., 2, 3)]},
2: {0: [(1, 1, 4), 1: (1, 2, 0)]}}
gamma = 0.9
a | Justify the need of policy approximation is needed in reinforcement | [10]
learning.
b | Suppose you have a 10-armed bandit problem where the rewards for
each of the 10 arms is deterministic and in the range (0, 10). Which
Q3 among the following methods will allow you to accumulate
CO-2,4; maximum reward in the long term and why?
SO-1; Justify each option. [10]
BL-4,5 a) e-greedy with e= 0.1.
b) e-greedy with e= 0.01.
c) greedy with initial reward estimates set to 0.
d) greedy with initial reward estimates set to 10.
a Consider a finite, episodic, and undiscounted Markov Decision
Process (MDP) with states P and Q, apart from the terminal state.
Q4
Assume the following two episodes are observed when a Monte-
a Carlo (MC) evaluation is being carried out. Assume the discount [10}
BL-2,3 factor y= 1.
Episode 1:

P44) Q,-2) 043) QS)
--- page 3 ---
| Episode 2:
Q-3)P,+2)+(Q,-4))
For example, a sample such as (Q, -3) — (P, +2) — (Q, -4) means
that the episode starts at Q, moves to P, then transitions back to Qa,
and terminates. The agent receives rewards of -3, +2, -4,
respectively.
« Estimate the state value of both P and Q using First Visit
Monte-Carlo evaluation.
+ Estimate the state value of both P and Q using Every Visit
Monte-Carlo evaluation.

In the game of Blackjack, a player aims to get cards with a total value
as close as possible to 2] without exceeding it. The dealer follows a

fixed policy (e.g., hits until reaching 17 or more). The state of the

game can be defined by:
The player’s current sum
| The dealer’s visible card
Whether the player has a usable ace (an ace counted as 11 without
busting)
a) Define the state space, action space, and reward function for
modeling Blackjack as a reinforcement learning problem.
b) (6) Describe how the Monte Carlo method can be used to
estimate the optimal policy for the player.

A robot is required to traverse a 4x4 grid environment to reach ie |

| goal states (State 1 or State 16), The grid has 16 states, with 2

| terminal states (1 and 16) and 14 non-terminal states (2 to 15).
The robot follows a random policy, meaning that in every state, it
selects one of the four possible actions (Up, Down, Left, Right)

| with an equal probability of 0.25. Each step incurs a reward of -1.

The grid structure is as follows:

| find stale Vo Me
a eS
115 6 7 8

If9 10 rp 12 |

|
Die siinni

|) ae OSS 5S 6

[10]

|
|

| [10]

a | Enat ) | |
--- page 4 ---
b | With reference to Reinforcement Learning, answer the following
briefly
a) Concept of exploration and exploitation
b) Difference-between model free and model based
Reinforcement Learning [103
c) Concept of Immediate Reinforcement Learning and Full
Reinforcement Learning

d) On-Policy learning and Off-Policy Learning

a i. With help of a pseudo code, explain SARSA on-policy
TD control algorithm.
Consider the following Q[S,A] table:

State 1 State 2
Action | 2.0 3.0
Action 1 5.0 4.0
Assume that a = 0.2,and y = 0.7
[10]
ii. After the experience < 1,2,4,2,2 > for (S, A, R, S’, A’),
which value of the table gets updated and what is its new
Q6 value?
iii. Justify why SARSA is called an on-policy TD control
CO-2, 3; algorithm in 1-2 sentences.
SO-1;
BL- 2,4 Hint: SARSA learing algorithm is given by the following equation:
b | In the context of Reinforcement Learning, soft policies are used to
ensure sufficient exploration during learning.
a) What is a soft policy in Monte Carlo control? How does it
differ from a deterministic (greedy) policy? [10]

b) Describe how the e-greedy policy helps in achieving a soft
policy. Illustrate with an example where ¢ = 0.1 and there

are 3 available actions from a given state.
--- page 5 ---
c) In the Monte Carlo Control algorithm with e-soft policies,
explain how policy improvement is performed after
updating the action-value function Q(s, a).

d) Why is using a soft policy necessary in Monte Carlo Control

methods for policy improvement and convergence?

Q7 a | Explain the method that integrate policy-based techniques with 110]
CO-3,4; value-based approaches.
SO-1; 5

BL-2, 4 Compare the difference between Q-learning and SARSA. [10]
````

## 2024-25 · Final-Exam · Sem 7 · paper 0412993ddfd8

- Departments: Artificial Intelligence, Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/DATA SCIENCE/SEM-VII/REINFORCEMENT LEARNING/Reinforcement Learning, Sem-VII, Final Exam 2024-25.pdf` (+1 identical copies)
- Printed on paper: duration hours: 3
- Text: ocr (9 pages), mean OCR confidence 85.7
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
q

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B TECH/MBA TECH Year: IV_ Semester: VIL
Stream/s ; DS/AI/AIML/AIDS

Subject: __ Reinforcement Learning ; Time: __3hrs_ hrs (jotopamto 1: oopm )
Date:_05 /12 /2024 No. of Pages:_9_

Marks: __100.

Final Examination (2024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

> 1) Question No._1___ is compulsory.
2) Out of remaining questions, attempt any 4 quéstions.
3)Inall__5_ questions to be attempted. re
4) All questions carry equal marks. ;
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ot Answer briefly: [20]
CO-L: a. Explain in not more than 5 sentences reinforcement learning framework

So- 1: with the help of suitable diagram using its core components such as Agent,

BL2 ° Environment, Reward, Action, and State. .

b. Consider an MDP with two states {JN, END}. When in IN state, the agent

can choose from a set of actions A = {STAY, QUIT}. If QUIT is selected,

© | co-2: then the game will go to END state and agent receives a reward of 5 points.
“3 If STAY is selected, the agent will stay in IN state and obtain a reward of 2

— > points with probability 34 or the agent will go to END state with probability
of Y% and obtain a reward of 4 points. Draw the state diagram for the given
problem

CO-3: c. Compare Monte Carlo approach and Temporal Difference approach in

SO-1 2 Reinforcement Learning (provide 3 comparison points between the two

BL23. approaches)

CO- 4; d. ee ae . ;

0-1: Compare Value iteration and Policy iteration dynamic programming

BL-3 approaches in terms of computational steps, complexity and convergence.
--- page 2 ---
Q2
CO-2,3;
SO-1;
BL-4,5

a.

Upper Confidence Bound.(U CB) equation is given by

as inc ee
Ay = argmax,|Q;(a) +¢ ae
where:

Q,(a) is the éstimated value’of action ‘a’ at time step-‘t’.

N,(a) is the number of times that action ‘a’ has been selected, prior to
time ‘t’.

Assume confidence value.c = 1

hs Compute the estimated Q value using UCB for the following
scenario. Let there be three machines with the following Q

values after a total of 100 steps.

Q (My) =1.73, Q(Mz) =1.83, Q(M3) =1.89, Q(M,) =1.55

The number of times each machine is played out of 100 is also
given. Ni=25, N2=20, N3=30, Ng=25

ii. Identify the machine that will be selected according to UCB for
the next iteration. Justify your answer

iii. Justify the following statement in 1-2 lines “ UCB balances
exploration and exploitation”

[10]

CO-2,3;
SO-1;
BL-4,5

i. With help of a pseudo code, explain SARSA on-policy TD control
algorithm. ;

Consider the following Q[S, A] table:

State 1 | State 2 7
Action 1 1.5 255
Action 2 4 3

Assume that 0=0.1, and y=0.5.
ii. After the experience (1,1,5,2,1) for <S, A, R, 8’, A’>, which value

of the table gets updated and what is its new value?
iii. - Justify why SARSA is called an on-policy TD control algorithm in

1-2 sentences.

Hint: SARSA learning algorithm is given by the following equation:


[10]
--- page 3 ---
a. Consider a finite, episodic and undiscounted Markov Decision Process
——-——|-——]-(MDP) with states A and B apart from the terminal state. Assume the

following two episodes are observed when a Monte-Carlo (MC) evaluation
is being carried out. Assume discount factor y = 1.
Episodel: (A,+3) > (A,+2) > (B,-4) > (A,+4) > (B,-3)
Episode2: (B,-2) > (A,+3) > (8-3)
For example, a sample such as, (B, —2) > (A,+3) > (B,—3), means that
the episode starts at B then goes to A, then goes to B again and then

oan 2: terminates. On the way, the agent gets rewards of —2, +3 and —3,
SO-: respectively. [10}
BL-4,5 : ; ; : . a
i. Estimate the state value of both’A and B using First Visit
Monte-Carlo evaluation.
~y ii. Estimate the state value of both A and B using Every Visit
Monte-Carlo evaluation
iii. Construct a Markov médel that best explains the observations
given in the question. ,
Hint: Return is given by
Gz = Reay ty Regn +" at yr tt Ry
b. Suppose an agent wants to help Sam make an informed decision about
whether to party or relax over the weekend. Sam prefers to party, but is
worried about getting sick. Such a problem can be modeled as an MDP
with two states, healthy and sick, and two actions, relax, and party. Thus,
S = {healthy(he), sick(se)}
A = {relax(re), party(pa)}
The agent does not know the model (i:e. the transition probabilities from
one state to another). It learns from the S, A, R, S’ experiences, that are
provided in the table ‘below. Assume discount factor, y = 0.8 and learning
CO-2,3; : rate, a = 0.3. Starting with all Q-values to be zero, compute the Q-values
SO-1; for the set of transitions mentioned in the table below: [10]
BL-4 N) A R Ss’ Q-values
he re 7 he
he re 7 he
he | pa 10 | he
he pa 10 si
si pa 2 si
— si re 0 si
; si re 0 he
™ Hint: Q-learning algorithm equation:
Q(St, At) — Q(St, At) + a Resa + ymax Q(St4154) —- QS; Ay)| : |

3
--- page 4 ---
re

Q4
CO-2,3;
SO-1;
BL-4

For an action ‘a’, the n™ estimate for the action-value, ‘Qn’, is given by
the sum of all previous rewards obtained for that action, divided bythe |
number of times that action has been selected (i.e. it’s just the average

value) as follows a
n-1
_ Ry + Ro + Rg to Rava _ 1 by
Qn = n-1 “a-1d*
i=

Mention in 2-3 sentences the limitations of above expression.
ii. State the incremental implementation expression, where the
new value Q,,41is expressed in terms of the previous estimate

Qn, and reward Ry.

Consider a 2-armed bandit problem, where one has to choose one of two
actions. -

we
Assume action a, yields a reward of r = 2 with probability p = 0.4 and 0

otherwise.

If you take action az, you will receive areward ofr = 0.8 with probability

p = 0.8 and 0 otherwise.

The 2-armed bandit game is played four times and Q-values are updated [10]
using the update rule Q¢41(@) = Qe(@) + n(r — Q,(a)). Taken = 0.2.
Assume the initial values of Q as zeros. :

In trial 1, you choose a, and obtain a reward of r = 2.

In trial 2, you choose aj and obtain a reward ofr = 0.8.
In trial 3, Greedy action is exploited and the reward r = 0 is obtained
In trial 4, az is exploréd and the reward r = 0.8 is obtained.

iii. Complete the table given below

Trial t Action r Q(a1) Q(az) Next
selected action
(a,0r a2) selected
0 0 0 ay
1 ay 2 0 + 0.2(2 — 0) - ap
=04 .
2 a2 0.8 0.4 0 +.0.2(0.8 — 0)
; = 0.16
3
4 _|
--- page 5 ---
CO-2,3;
SO-1;
BL-4,5

b

Pirate Ship is anchored in an Island. It has to reach its home safely and it
can only take two directions, namely, North and South. The Possible

routes the ship can take are-

Go to Gold Island, collect gold and then go to Home (Move North,-then-}

South)
eGo to Silver Island, collect silver and then go to Home (Move South and
North)

eGo to home
There are two dangers in the first two routes -

(a) There is a Bermuda Triangle to the North of Gold Island.
(b) There is a Prison to the south of Silver Island.

There is uncertainty in directions which means, there are probabilities
involved whenever a direction is decided. Probability of moving in the
intended direction is 0.8. Example: When the ship wants to move towards
North, the probability of the ship moving towards North is 0.8 and there is
a probability of 0.2 for South. So how does the Ship reach home with
maximum possible benefits? .

Assume randomly initialize the policy as moving in the north direction for
all states. Assume initial values for all state to be zero.

Apply Dynamic Programming based Policy Iteration Algorithm for one
iterations to obtain policy evaluation and policy improvement table. Identify
the change policy after the one iteration.

The state diagram for this scenario is shown below. Also the table for the
initial value, random policy and the reward for each state is given below.

States S1 $2 S3 S4 S5 S6é
Reward 0 1 2 2s 1 -0.5
Values 0 0 0 0 0 0
Initial N N N - - -
Random *

Policy

[10]
--- page 6 ---
Hint: Policy iteration expressions expression

Policy evaluation

Vas) = r(s) +7 > PUGS". 7G, m(S))) VOS')

Policy improvement

n(s) = argmaxg y, p(s’, rls, a) Vas")

s'€S
Q5 Consider discount factor y = 0.8 and rewards R; = 3,R, = =—1,
CO-1,3; R3 = 2, Ry = 4and Rs =5withT=5. Compute Go, Gy, Gz , G3, G4, Gs if [05]
SO-1; return is given by Gy = Rtai + yG;41. State with reason whether the agent
BL-3,4 is myopic or farsighted im
Consider the grid world shown below:
2:0 | 4.4 | 1.1 | 0.5
3.0 | 2.3 | 1.9 | 1.6
0.4 | 0.7. | 1.1 [3.2
4.9 | 2.9 | 2.0 | 1.7
All four actions (right, left, up and down) have'probabilities (0.2, 0.4,0.3
CO-2,3; and 0.1) respectively. In the figure above, the value function, V™ at each
SO-1; state in the grid is provided, for the case where discount factor y = 0.85. [05]
BL-4 Show numerically that the Bellman equation given below applies for the
state of the 24 row and 2"4 column valued at 2.3, with respect to its four
neighboring states. Assume that R(s) at all states is zero.
Hint: Bellman Equation
V™(s) = R(s) + vr), P(s'|s,x(s))V™(s')
st
Consider the given grid with the following parameters
. e Rewards:
CO-2,35, o +50 for target
eae o -1 foreach state [10]
BL-4

e Actions= {U,D,L,R} as shown
e States with X are obstacles and those action
would be avoided by the agent
--- page 7 ---
e Initial random policy for each state is
mentioned.
e Initial Q value is equal to zero

Apply Exploring Start Monte Carlo Algorithm for an Episode with T=5 and

initial random state-action as (s10,R)
i. Generate state-action sequence for this episode for the given policy

ii. Discounted return given by equation G = yG + Re41.-For discount
factor y = 0.8, compute discounted return list for the given episode

iii. | Obtain the average return list and update the Q value

iv. Update the policy in the grid

Target < sil - 82 - s3 [< s4

T 85 T s6 T   s7 T s8

T 89 T   s10 «sil T $12
. T s13 T sl4 <= sI5 T sl6

<- siI7 <— 818 T s19 <— s20 StartT 21

a. Consider the Markov Decision Process (MDP) depicted in the figure,

where the agent begins in state So .
There are two actions available at Sp : moving left and moving right.

Q6 : The rewards associated with these actions are deterministic, as shown in the

ced figure. [05]
“a Let there be two deterministic policies:

BL-4 i. Tere: Always move left.

ii, Trignt: Always move right.
--- page 8 ---
Calculate the total expected reward for both policies across the
horizon of time step two, considering the discount factors y =0
and 0.9.

b. Show the calculations for both Tere and right

c. Identify which policy is optimal in each scenario.

Expected Return G; = Res1 + YRe+2 + y7 Regt
co-3: b. Explain the concept of Markov Decision Process (MDP) and describe its
S O-l: key components in not more than’5 sentences. State the significance or [05]
BL2 discount factor y to estimate returns in long term decision making
C.. With reference to policy gradient algorithm, answer the following
questions- *
i. “Policy is modeled with a parameterized function and the actions
are selected without calculating the value function”. Justify this
statement.
ii. Explain the following statement in a maximum of 2-3 sentences:
CO-3; Value function based methods are oriented towards finding
SO-1; deterministic policies whereas policy search methods are geared [10]
BL-2 towards finding stochastic. policies.
iii, | Why are value-based approaches computationally expensive in
continuous spaces? How does Policy-based approach overcome
this issue?
iv. In general, why does the Actor-Critic method improve the
convergence to a solution compared to Monte Carlo REINFORCE
method?
a Sitting at your hall on a rainy evening, you hear an episode of experience as
Q7 follows: At the first step you saw a lightning. At the second step you hear a
CO-3; thunder with a drizzle of rain. At the third step you saw only a drizzle of [10]
SO-1; rain. Then you had a powercut, worth —1 reward, and the episode terminates
BL-4 on the fourth step. All other rewards were zero. The experiment is

undiscounted (i.e., y= 1).
--- page 9 ---
We may represent the state s that you witnessed by a vector of three binary
features, light(s) € {0,1}, thunder(s) € {0,1} and drizzle(s) € {0, \. So, the
sequence of feature vectors corresponding to the four steps of this episode

~| can be expressed as, [1,0,0]", [01,1], [0,0,1]7 and [0,0,0]7.

i. Approximate the state-value function by a linear combination of
these features with two parameters:
g(s) = [l x light(s) + t x thunder(s) + d x drizzle(s)]
Iflight 1 = —3, thunder t = —2and drizzled = 1, then write
down the sequence of approximate values corresponding to this
episode. ;

ii. | Write down the sequence ‘of A-returns G# (1 <t <3) corresponding
to this episode, for 1 =0.5 and 1 = —3,t = —2,d = 1. Clearly
show the detailed evaluations.

oa

Hint:
The n-step return and A-return Ge are given as,
GE = Rea tyRaat VP Raste $7 Rn $7'V (Sr4n)
a = (1a) pana?
n=l
where, of) = RaityRr2 +PRy3 te +77 IRr, as multiplication factor being ar

CO-1;
SO-1;
BL-2

With reference to Reinforcement Learning, answer the following briefly in
not more than 2-3 sentences each

i. Concept of exploration and exploitation

ii. Difference between model free and model based Reinforcement
Learning

ili. Concept of Immediate Reinforcement Learning and Full

Reinforcement Learning
iv. On-Policy learning and Off-Policy Learning

[10]
````

## 2024-25 · Final-Exam · Sem 12 · paper a3a69b2a89e4

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/COMPUTER/Sem_12/Reinforcement Learning/Reinforcement Learning Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 89.5

````text
SVKM’S NMIMS Wen
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/ os Ly
SCHOOL OF TECHNOLOGY MANAGEMENT . es :
Academic Year: 2024-2025

BTedk
Program/s: MBA Tech/ B Tech (Intgs),Stream/s : AIDS/DS/COMP Year: III/IV/VI Semester: VI/VIII/XII

Subject: Reinforcement Learning Time: 3hrs(lof0oam to 1z00pr)
Date:_08/05 / 2025 No. of Pages:05
Marks: 100

Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
COA: a. | Explain the Upper-Confidence-Bound (UCB) algorithm in Multi-
SO-1; Armed Bandits. How it balances exploration and exploitation better
BL-2 than e-greedy methods.
b. | Consider an agent starting in a state A where it can take two possible
- _ _ | actions: move forward (action “F”) or wait (action “W’”). If it selects
“F”, the agent moves to state B, which is a terminal state (no further
; actions can be taken). If ““W” action is selected in state A, the agent
so ‘ will stay in A with a probability of 0.7, or the agent will go to state B
BL-3 with a probability of 0.3. We assume that the reward for reaching
state B is R(B) = +1.5 and the reward for staying in state A is R(A)
= —0.05. Draw the state diagram for the given Markov Decision
Process (MDP). :
c. | List key components of Reinforcement Learning involved in skill
So \ : improvement for the following scenario: Consider a student learning
BL-1 to solve mathematical problems. Apply the concepts of
--- page 2 ---
Reinforcement Learning (RL) to explain how trial and error, rewards
(positive reinforcement), penalties (negative reinforcement),
learning, and optimization play a role in improving their problem-

solving skills.

CO-3 ; d. | Explain how Value Iteration and Policy Iteration work in Dynamic
pe Programming. Describe the main steps involved in each method.

a | Using Python
Evaluate how different discount factors (y = 0.1, 0.5, 0.9, 1.0) affect no]
an RL agent’s decision-making in a reward-based environment with

rewards = [10, 20, 30, 40}.

Q2 b_ | Using python
CO-1,4; Compute the value function for a given policy in a simple 3-state
Piel 5 MDP with known transition probabilities and rewards.
Given: P = {0: {0: [(1, 1, 5)], 1: [(, 2, -1)]}, [10]

1: {0: [C1 0, 2)], 1: [C, 2, 3)]}},
2: {0: [(1, 1, 4)], 1: [C, 2, 0)]}}

gamma = 0.9

a | Justify the need of policy approximation is needed in reinforcement [10]
learning.

b__| Suppose you have a 10-armed bandit problem where the rewards for
each of the 10 arms is deterministic and in the range (0, 10). Which

Q3 among the following methods will allow you to accumulate
CO-2,4; maximum reward in the long term and why?
SO-1, Justify each option. [10]
BL-4,5 a) e-greedy with ¢= 0.1.
b) e-greedy with ¢ = 0.01.
c) greedy with initial reward estimates set to 0.
d) greedy with initial reward estimates set to 10.
a_ | Consider a finite, episodic, and undiscounted Markov Decision
Q4 Process (MDP) with states P and Q, apart from the terminal state.
Assume the following two episodes are observed when a Monte-
So. 35 Carlo (MC) evaluation is being carried out. Assume the discount _ | [10]
BL2,3 factor y = 1. ‘
Episode 1:

(P,+4)>(Q,-2) (P43) -(Q,-5)
--- page 3 ---
Episode 2: »
Q.-3)>(P,+2)(Q,-4)) ;
For example, a sample such as (Q, -3) — (P, +2) — (Q, -4) means
that the episode starts at Q, moves to P, then transitions back to Q,
and terminates. The agent receives rewards of -3, +2, -4,
respectively. ;
e Estimate the state value of both P and Q using First Visit
Monte-Carlo evaluation.
e Estimate the state value of both P and Q using Every Visit
Monte-Carlo evaluation.

b__| In the game of Blackjack, a player aims to get cards with a total value

as close as possible to 21 without exceeding it. The dealer follows a
fixed policy (e.g., hits until reaching 17 or more). The state of the
game can be defined by: a
The player’s current sum
The dealer’s visible card [10]
Whether the player has a usable ace (an ace counted as 11 without
busting)

a) Define the state space, action space, and reward function for

modeling Blackjack as a reinforcement learning problem.
b) (b) Describe how the Monte Carlo method can be used to

estimate the optimal policy for the player.

a__| A robot is required to traverse a 4x4 grid environment to reach its
goal states (State 1 or State 16). The grid has 16 states, with 2
terminal states (1 and 16) and 14 non-terminal states (2 to 15).
The robot follows a random policy, meaning that in every state, it
selects one of the four possible actions (Up, Down, Left, Right)
Q5 with an equal probability of 0.25. Each step incurs a reward of -1.

CO-1,3;

SO-1;
BL-1, 3

The grid structure is as follows: [10]

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
--- page 4 ---
b

With reference to Reinforcement Learning, answer the following .,

briefly
a) Concept of exploration and exploitation
b) Difference:-between model free and model based
Reinforcement Learning
c) Concept of Immediate Reinforcement Learning and Full
Reinforcement Learning

d) On-Policy learning and Off-Policy Learning

[10]

Q6
CO-2, 3;
SO-1;
BL- 2,4

a

i. With help of a pseudo code, explain SARSA on-policy
TD control algorithm.
Consider the following Q[S,A] table:
Statel _ , State 2
Action | 2.0 3.0

Action 1 5.0 4.0

Assume that a = 0.2,and y = 0.7

ii. After the experience < 1,2,4,2,2 > for (S, A, R, S’, A’),
which value of the table gets updated and what is its new
value? .

iii. Justify why SARSA is called an on-policy TD control
algorithm in 1-2 sentences.

Hint: SARSA learing algorithm is given by the following equation:
QC Sp, At) — QC SAL)”
+ @ [Resa + ¥QC Star Aces) — QC St, Ae)]-

[10]

In the context of Reinforcement Learning, soft policies are used to
ensure sufficient exploration during learning.
a) What is a soft policy in Monte Carlo control? How does it
differ from a deterministic (greedy) policy?
b) Describe how the e-greedy policy helps in achieving a soft
policy. Illustrate with an example where ¢ = 0.1 and there

are 3 available actions from a given state.

[10]
--- page 5 ---
c) In the Monte Carlo Control algorithm with ¢-soft policies, _,
explain how policy improvement is performed after -
updating the action-value function Q(s, a).

d) Why is using a soft policy necessary in Monte Carlo Control

methods for policy improvement and convergence?

Q7 a | Explain the method that integrate policy-based techniques with 110]
CO-3,4; value-based approaches.
SO-1;

BL-2, 4 b Compare the difference between Q-learning and SARSA. [10]

rand
````

## 2024-25 · Re-Exam · Sem 7 · paper e4b7d04a4d14

- Departments: Artificial Intelligence, Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/DATA SCIENCE/SEM-VII/REINFORCEMENT LEARNING/Reinforcement Learning, Sem-VII, Batch 2024-25 Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (10 pages), mean OCR confidence 80.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025
Program/s: B TECH/MBA TECH

Stream/s ; DS/AI/AIML/AIDS

Year: IV__ Semester: VII

Subject: Reinforcement Learning Time: __3hrs___ (4o.am_ to 1+ pm )
Date:_24 /o9. /2026 No. of Pages:_9_
Marks: 100 }

_ ReExamination @024- 25)

Instructions: Candidates should read carefully the instructions. printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No._1___is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]
CO- I: a. Discuss the key characteristics that distinguish "Reinforcement Learning"
SO- lL from other machine learning paradigms such as "Supervised Learning" and
BL2. “Unsupervised Learning"? Answer in not‘more than 4 sentences.
b. Consider an agent starting in a room A in which it can take two possible
actions: to leave the room (action “L”) or to stay (action “S”). If it leaves A,
the agent moves to room B, which is a terminal state (no more actions can
cO0.2: be taken). If “L” action is selected in state A, the agent will move to room
so- ie Balt “s” action is selected in state A, agent will stay in room A with a
BL-3 probability of % or the agent will go to state B with probability of % .We

assume that the reward in entering state B is R(B) = +1 and the reward for
being in state A is R(A) =—0.1. Draw the state diagram for the given Markov

Decision Process (MDP).
co-23: |% Define Multi-Arm Bandit problem and state its goal. Compare Greedy
S 0. L a action selection method with Fixed Exploration +Greedy action selection
BL2. method. Answer in not more than 5 sentences.
CO-4 ; d. Compare Monte Carlo, Temporal Difference and Dynamic Programming
SO- 1;

approaches in Reinforcement Learning (provide 3 comparison points among
BL-3 approaches)
--- page 2 ---
a

Given the discount factor y=0.8 and rewards Ri = 3 Ro=—1 R3=2 Ra= 4

and Rs=S.

ik Establish a relationship between Gt and Gt+1.

ii. Compute the values of GO, G1, G2, G3 and G4,

[05]

Q2
CO-2; iii, State your comments for y = 0 andy = 1 in not more
SO-1, than two lines.
BL-3
Hint: Return is defined as
Ge = Rear tReet + yr tt Rr
| In the 2-armed bandit problem, one has to choose one of 2 actions. ;
Assume action a, yields a reward ofr = 2 with probability p = 0.75 and
0 otherwise.
If you take action a2, you will receive a reward of r = 1 with probability
p = 0.25 and 0 otherwise.
The 2-armed bandit game is played five times and Q-values are updated
using the update rule, Qrar(a) = Q,(a) + n(r — Q,(a)). Take n = 0.3.
Assume the initial values of Q as zeros.
In trial 1, you choose a, and obtain a reward of r = 2.
In trial 2, you choose a2 and obtain a reward ofr = 1.
In trial 3, Greedy action is exploited and the reward r = 0 is obtained
In trial 4, az is explored and the reward r = 1 is obtained.
In trial 5, Greedy action is exploited to obtain a non-zero reward
CO-2,3; Complete the table below.
SO-1;
BL-3,4 Trial | Action r Q(a1) Q(az) Next
° t selected action
(a,or az) selected
0 0 i) ay
1 a, 2 0+.0.3(2—0) = 0.6 | - a
2 az 1 | 0.6 | 0+0.3(1-0)
= 0.3
3
4

[05]

IE

4
--- page 3 ---
c Consider a problem where the agent has to reach from state s1 to s8. The
state diagram is as shown below. Table below shows the values and policy
after one iteration. With the following parameters given, estimate the value
and the policy in the next iteration using Policy iteration algorithm.

e Actions taken by agent= {Left (L), Right(R)}
e Discount factor y = 0.9
-e Probability to go in the intended direction =0.7
e Probability to go in the direction other than intended= 0.3
e Rewards for each state is written within the state.
e Initial policy and values as given in the adjacent table

States | sl. — *\’s2e7- = |és3 s4 s5 s6 s7 s8
Values | 0 0 0 0 0 0 0 0
Policy | L R | mot R L/R - -

CO-4;
SO-1;
BL-4,5

[10]

Hint: Policy iteration expressions expression

Policy evaluation

Me) =) +7) PCS! AIG, mS) Vs")

Policy improvement

m(s) = argmax, » p(s’, r|s, a) Vs’)

s'es
--- page 4 ---
a Consider the following Q[S, A] table:

State 1 | State 2 |
Action 1 1.5 25
| Action 2 4 3

Assume that o=0.1, and y=0.5.

Q3 i. After the experience (1,1,5,2) for <S, A, R, 8’>, which value of the

CO-2,3; ; table gets updated and what is its new value?
SO-1; ii. What is one potential problem with a Q-learning agent that always
BL-3;4 chooses the action which maximizes the Q-value?
iii. Describe two ways to force a Q-learning agent to explore.
iv. Justify whether Q learning algorithm is an Off Policy or an On Policy
TD control method in not more than 2-3 sentences.

[10]

Hint: Q-learning algorithm equation:

Q(SrrAe) & QS As) + a[ Raga + max Q(Si41,4) — Q(51,A0)]-

b Upper Confidence Bound (UCB) equation is given by

In(t)
A, = argmax (a) +c
t g a|Q ) N,(a)
where

Q:(a) is the estimated value of action ‘a’ at time step ‘t’.
N,(a) is the number of times that action ‘a’ has been selected, prior to
time ‘t’.
Assume confidence value c = 1. :
€O-2,3; i. Compute the estimated Q value using UCB for the following
SO-1; scenario. Let there be four machines with the followingQ - [10]
BL-3,4 values after a total of 12 steps.
i Q(M,) = 0.55, Q(M2) = 0.63, Q(M3) = 0.61, Q(M,) = 0.40
The number of times each machine is played out of 12 is also

given.

N,(M,) = 3, N, (M2) = 4, N, (Mz) = 3, N,(M4) = 2
ii. Which machine will be selected according to UCB for the next

iteration. Justify your answer .
iii. Compare UCB with €- Greedy on the basis of Exploration and

Exploitation Mechanism. Answer in not more than 2-3
sentences. :
--- page 5 ---
a Consider the following scenario _

‘| A pigeon is involved in an experiment. It experiences one episode. At the
first step it hears a whistle. At the second step it sees a flag. At the third
step it both hears a whistle and sees a bell. It then receives some seed,
worth +1 reward, and the episode terminates on the fourth step. All other
rewards were zero. The experiment is undiscounted (i.e.,-y = 1).

We may represent the pigeon’s state ‘s’ by a vector of two binary features,
whistle(s) € {0,1} and flag(s) € {0,1}. So, the sequence of feature
vectors corresponding to the four steps of this episode can be expressed as,
[1, OJ, [0, 1]" , [1, 1]7 and [0, Oo]? .

Q4 : i. Approximate the state-value function by a linear combination
CO-3; of these features with two parameters: [10]
SO-1; [b x whistle(s) + | x flag(s)].
BL-4 Ifb = 2andl = —2, then write down the sequence of
approximate values corresponding to this episode.
ii. Write down the sequence of A-returns G2(1 < t < 3)

corresponding to this episode, for A= 0.5 andb = 2, 1 =
—2. Clearly show the detailed evaluations
Hint

The n-step return and A-return Ge are given as,
GY) = Rat WesatP Rag te $7 Regn +7 (Sean)
Ge = (1-4) Parle

n=t

where, GO) = Rint +7Ra2tPR43t---+7 Re, with multiplication factor being AT‘!
9 Gf 41+ Ye: +: ey ip

b Describe the key components of Markov Decision Process namely state,
actions, transition model and rewards in not more than one line each.
Consider the MDP given below-

CO-2,3;
SO-1;
BL-4

[10]

Here policy 2(a|s) = 5 for a = STAY or QUIT ands = IN.
Assume y = 1 and V(END) = 0

Compute value of state IN, V(UIN)

Hint: Bellman Equation for state value function is given by-

--- page 6 ---
a In the table below, the numbers are the Q values for each state-action pair.

State | Action 1 | Action 2
sl 8 8)
s2 5 3

The agent just took Action 2 from State s1 to State s2, and got a Reward
of 1 (the episode is not terminated yet). According to the behavior policy,
the agent will take Action 2 in s2 for the next step. The discount factor (vy)

Q5 is set to I and the learning rate (@) to 0.5.

CO-3; i. What.will the value for (s1, action 2) be, if you are using SARSA for | [10]
SO-1; updating?

BL-3,4 ii. What is the impact of the choice of value for learning rate?

iii. “SARSA is an on-policy algorithm.” Justify this statement in not more
than 2-3 sentences. : E

Hint: :
SARSA learning algorithm expression:

Q(St, At) — Q(St, At) + a[Rea +97Q(St41, Atya) — QS: Ay).

b Consider the following environment in which states so, S1, $2, $3, $4 and ss
are shown in the grid below (see Figure (a) below). so is the terminal state.
Agent can take one of four possible actions at each state, other than the
terminal state: {L,R, U, D} as shown in Figure (c). Also, assume that the
reward at each state is given as indicated in the Figure (b) below. Also

assume the discount factor y = 1.

so | st s So $1 82
CO-2,3; ; 7 ie ee 100 | 3 5
SO-1; $3 $4 5 [10]
BL-4 S83 S4 $5 2 oii 5
1 imac ane,
Figure (a): Environment with a Figure (b): Rewards
policy

Figure (c): Actions
--- page 7 ---
Consider the following Episodes E1, E2, E3
E1: (84, U) > (s1, R) > (2, L) > (s1, stop)
E2: (s3, U) > (so, stop)

E3: (ss, L) > (sa, U), > (1, R) > (52, stop)

i. Evaluate values for all the states for the given three episodes
using First Visit Monte Carlo Algorithm. Draw the value
table.

ii. Evaluate the values for all the states for given three episodes
using Every Visit Monte Carlo Algorithm. Draw the value
table

iii. Compare First Visit and Every Visit Monte Carlo Algorithms.
Answer in not more than 2-3 sentences.

Hint: Return is defined as-

Gy = Rey ty Reg te tye “R

Q6
CO-1;
SO-1;
BL-2,3

With reference to Reinforcement Learning(RL), answer the following in
not more.than 2-3 sentences each-
i. Discuss the trade-off between exploration and exploitation citing
an appropriate example
ii. For the chess game, identify the following RL components —
Environment, State, Action, Agent, Reward
iii. List some real world applications of RL
iv. Difference between model free and model based RL
v. Define the concept of policy in RL

[10]

CO-4;
SO-1;
BL-4

Consider the following Markov Decision Process (MDP) with two states:
sand s» ,and two possible actions a, and az. The transition probabilities
and rewards are provided in the table below. The discount factor y=0.9.
Assume the initial values of both states V(S,) and V(Sz) are zero.

Table: MDP with two states and two possible action
s| as’ |p(s' | s,a) |r(s, a, 8’)
$)] ay] 4 0.8 4
$, | Gy | So 0.2 4

8, | Q9/s 0.5 6
1 1

$1 | dy | & 0.5 6
1 | @g | 5g

Sy}, | Sy 0.7 it)

So] Cy | So 0.3 =f

$Q| a9] 8 0.4 —3

Sy | Ao | Sg 0.6 _

[10]
--- page 8 ---
es: Current state
e a: Action taken from the current state

es’: Next state
e p(s’ |s, a): Probability of transitioning from state s to s’ given

action a
e r(s,a,s’) : Reward received for taking action a in state s and

transitioning to state s’
Using the value iteration algorithm, compute the value functions V(S;)

and V(S2) after two iterations.

Hint: Value iteration expression
V(s) = r(s) + ymax(), POs rI(,a)) VO)

a With reference to Policy Gradient methods, answer the following in not
more than 2-3 sentences each-
i. Justify the following statement-“ Policy is modeled with a
Q7 parameterized function and the actions are selected without
CO-3; calculating value function”, :
SO-1; ii. | Compare value function methods with policy gradient methods
BL-3 i iii. Explain the working of actor critic method with respect to its
components namely actor and critic
iv. State advantages of actor-critic method

[10]

b Consider the given grid with the following parameters
e Rewards: ;
o +20 for target
o -1-for each state
e Actions= {U,D,L,R} as shown
e States with X are’ obstacles and ‘those action
would be avoided by the agent
e Initial random policy for each state is mentioned.
CO-2,3; e Initial Q value is equal to zero
SO-1; [10]
BL-3,4 ' | Apply Exploring Start Monte Carlo Algorithm for an Episode with T=6
and initial random state-action as (s13,D)
i. Generate state-action sequence for this episode for the given policy
ij. Discounted return given by equation G = yG + Rey1- For discount
factor y = 0.9, compute discounted return list for the given episode
iii. Obtain the average return list and update the Q value
iv. Update the policy in the grid
--- page 9 ---
Target <- sl
Tees5 T s6

if 1s9 T = s10
T 2

T s17 < si18

<< o s2 |e s3 |< — s4
feisT less

— sil ft +s12;

T sl4 <- s15 T 16

T s19 <= 820 StartT sO
--- page 10 ---

````

## 2023-24 · Final-Exam · Sem 7 · paper 15eebc73cdc0

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/DATA SCIENCE/SEM-VII/REINFORCEMENT LEARNING/Reinforcement Learning, Sem-VII, Final Exam, A Y 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30/Nov/2023
- Text: ocr (9 pages), mean OCR confidence 88.4
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
MPSTME
LIBRARY

SVKM’S NMIMS :
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING?
SCHOOL OF TECHNOLOGY MANAGEMENT :
Academic Year: 2023-2024

rr

Program/s: B.Tech. Year: IV Semester: VII
Stream/s: Data Science / CSE DS

Subject: Reinforcement Learning Time: 3 hrs (10 am to | pm)
Date: 30/Nov/2023 No. of Pages: 9

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data, if necessary.
Ql
Answer briefly: Covering multiple topics [20]
A. Explain the difference between “Exploration” and “Exploitation”, with an
example in each of the following contexts. (Please do not write long essays
Qi in response to this question. Maximum of | sentence to explain
exploration, and | sentence to explain exploitation is all that is expected)
CO-1: a) Restaurant Selection ‘ [5]
© |B > b) Online advertisements
c) Oil Drilling
d) Game Playing
B. State at least two characteristics that make “Reinforcement Learning”
Ql different from other machine learning paradigms like “Supervised
CO-1: Learning” and “Unsupervised Learning”? (Please respond in a maximum [5]
BL-1 ; of 1-2 sentences)
--- page 2 ---
c. For an action ‘a’, the n't estimate for the action-value, ‘Q,’, is given by the
sum of all previous rewards obtained for that action, divided by the
number of times that action has been selected (i.e. it’s just the average

value):
Ly
Ql Qn = R;
CO-4; n-1 [5]
BL-2 Starting with the above equation, derive the formula for estimating the

Sample Average, where the new Q value is expressed in terms of the

previous estimate, i.e. derive an equation that expresses Qn+i in terms of
Qn and Rn.

D. In the context of Value Function Approximation by stochastic gradient
descent method, the update to the parameter “w” is given by:

Aw = a(v,(5) — 0(S,w))Vw0(S,w)

If the value function is represented by a linear combination of features

a : using an equation such as the following, then derive the simplified form of [5]
fe the above equation.

0(S,w) =x(S)'w= s x;(S)wy
j=l
--- page 3 ---
BF NAV

Fores a.

——

Q2

re

Multi-armed bandit

[20]

Q2

CO-4;
BL-4

We have two slot machines (single arm bandits) Machine A & Machine B
with actual win rates of 25% and 75% respectively. The actual win rates
are unknown to the model. Optimistic-greedy algorithm is used to select
the optimal bandit. Assume ‘that we start with an optimistic initial estimate
of 200% win rate for each of the machines, even though the highest win
rate that is ever possible is 100%. Fill up the table below with M1n, M2n
values and reason why M1 or M2 was chosen at each iteration:
Time | Machine Win Machine Win Reason
Step | 1(M1) from 2 (M2) from -| why M1 or
No. Machine Viachine M2 was
(n) 1 2 chosen?
0 Mlo= - M20 = -
200% 200%
1 Mli=? No M2: =? - - 2
2 Ml2=? - M22 =? Yes ?
3 M13 =? - M23 =? No 2
4 Ml4=? No M24 =? - 2
5: Mls =? = M2s =? No 2?
What do you expect will happen after Iteration 5 in the context of this
problem?

[12]

Q2

CO-4;
BL-3

With Upper Confidence Bound algorithm for solving multi-armed bandit
problems, ‘A,’, the action chosen at time step ‘t’, is given by:

logt
N,(a)

A; = argmax|Q,(a) +¢

where

* Q,(a) is the estimated value of action ‘a’ at time step ‘t’.
+ N,(a) is the number of times that action ‘a’ has been selected, prior to
time ‘t’.

+ ‘c’ is a confidence value that controls the level of exploration

In the above equation, explain the intuition behind the following
statements: (Your response should be restricted to a maximum of 5

sentences)
- The first part of the RHS, i.e. Q:(a), represents the “exploitation” part

of the algorithm.
- The second part of the RHS, represents the “exploration” part of the

algorithm.

[8]
--- page 4 ---
Markov Decision Processes oe [20]
A Consider a MDP where the following sequence of rewards is received: Ri
=-1, Ro = 2, R3 = 6, Ra =3 and Rs = 2. Assume that the return Gs = 0 (at
Q3 the terminal state T = 5). Assume that the discount factor y = 0.5,
CO-1; Hint: Return is defined as Gi= Rui + y Rua + Rusty Rust... [5]
BL-3 Use the above to derive a relationship between G, and Gu.
What are the values of Go, Gi, G2, G3 and G4?
B Imagine that you design a robot to navi gate a maze. You decide to give it a
Q3 reward of zero for ail steps within the maze. The reward for the step to
CO-1; escape from the maze is +1. By formulating this problem as a MDP, after [5]
BL-2 several iterations, you find that the bot is not showing any improvement in
escaping from the maze. What is possibly going wrong?
Cc Consider the grid world shown below:
3.3) 8.8] 4.4) 5.3/1.5
1.5} 3.0} 2.3) 1.9] 0.5
0.1) 0.7] 0.7} 0.4|-0.4
Q3 -1.0| -0.4)-0.4 -0.6/-1.2
CO-3; . 5
Blot Actions Pa

-1.9/-1.3}-1.2}-1.4]-2.0

All four actions (right, left, up and down) are equiprobable. In the figure
above, the value function, V7 at each state in the grid is provided, for the
case where discount factor g = 0.9. Show numerically that the Bellman
equation given below applies for the center state valued at 0.7, with respect

to its four neighboring states, 2.3, 0.4, -0.4 and 0.7. Assume that R(s) at all
States is zero.

V"™(s) = R(s) + ay P(s'|s, m(s))V™(s')
--- page 5 ---
fa

Q3
CO-3;
BL-4

Consider a 4x4 Grid-world problem where the goal is to reach either the
top-left corner or the bottom-right corner (refer to Figure below), The
agent can choose from four actions up, down, left, right, which
deterministically cause the corresponding state transitions, except that
actions that would take the agent off the grid leave the state unchanged.
We model this as an undiscounted, episodic task, where the reward is —1
for all transitions. Suppose that the agent follows the equiprobable random

policy, 7.
Table 1: 4 x 4 Grid-world
: -20 | -22
-14 | -18 | -20
-20 | -18 | -14
-22 | -20 :

Given above is the partial value function for this problem. Calculate
respectively, the missing values in the first and second row?

V™(s) = RG) + >. P(s'|s,m(s))V™")

[5]
--- page 6 ---
Q4 Dynamic Programming: Value Iteration and Policy Iteration. [20]
Consider an MDP, M(S, A, P, R, y) with 2 states S = {S1, S2}. From each
state there are 2 available actions A = {stay, go}. Choosing “stay” from
any state leaves you in the same state and gives reward -1. Choosing “go”
from state S1 takes you to state S2 deterministically giving reward -2,
CO-3; while choosing “go” from state S2 ends the episode giving reward 3. 6
BL-4 Given the Bellman equation: [6]
Vy (s) = r(s)+y max, ves? r|s,a)Vz(s’)
Draw the Markov diagram for the above transitions.
CO-3; Apply the value iteration algorithm and compute the state values of S1 and
BL-4 S2 at the end of the Ist iteration. [7]
CO-3; Apply the value iteration algorithm and compute the state values of S1 and
BL-4 S2 at the end of the 2nd iteration. [7]
--- page 7 ---
a

Q5

Model-free methods: Monte Carlo, TD *

[20]

CO-2;
BL-4

Consider the following environment in which states so, $i, $2, $3, S4 and ss
are shown in the grid below (see Figure (a) below). so is the terminal state.
Agent can take one of four possible actions at each state, other than the
terminal state: i.e. Left, Right, Up or Down. Also, assume that the reward
at each state is given as indicated in the Figure (b) below.

Si S2
=> —

S83 S4 S5
a Tt =

Figure (a): Environment with a policy

50 -1 3
-1 -2 -4
Figure (b): Rewards

Estimate the state values of each state using the First-Visit Monte Carlo
evaluation given the following sample episodes:

Ei: (sa, U, r4) > (si, R, r1) > (s2, L, r2) > (si, stop, r1)

Ex: (s3, U, r3) > (So, stop, ro)

Es: (ss, L, rs) > (sa, U, ra), > (si, R, 11) > (s2, stop, r2)

Hint: Monte Carlo method relies on the following equations:
Increment total return S(s) «+ S(s) + G;

Value is estimated by mean return V(s) = S(s)/N(s)

[10]

CO-2;
BL-4

Estimate the state value of each state using the Every-Visit Monte Carlo
evaluation given the following sample episodes: *

Ei: (Sa, U, r4) > (si, R, 11) > (82, L, r2) > (si, R, r1) > (s2, stop, r2)

Ea: (83, U, 13) > (So, stop, ro)

E3: (Ss, L, rs) > (sa, U, ra), > (Si, R, 11) > (s2, L, r2) > (s1, stop, ri)

[10]
--- page 8 ---
Q6 Model-free methods: SARSA [20]

A You are given an environment with one state, X, and two actions, b and c.
T is the terminal state. Your Temporal Difference (TD) algorithm

generates the following episode using the policy m when interacting with
its environment:

1este

este

¥

2 12 x .b
3 16 T
e The policy x is given by: m (b[X) = 0.9, 2 (c|[X) = 0.1.
CO-2; e The current values of q are: q(X, b) = 1 and q(X, c) =2.

BL-4 ¢ The discount factor, y = 0.5.
; e The step size, a = 0.1.

[10] s

Show the values of q(X, b) and q(X, c) after their first update using the 1-
step SARSA.

Recall the following formulae about SARSA:

Define the n-step Q-return


n-step Sarsa updates Q(s, a) towards the n-step Q-return

Q(Se. Ar) = QS Ar )+a(ah (0) _ Q(S:,Ar))

CO-2; B Show the values of q(X, b) and q(X, c) after their first update using the 2-
BL-4 step SARSA [10]
--- page 9 ---
Q7

Value Function Approximation & Policy Gradients

¥

[20]

CO-3;
BL-4

A rat is involved in an experiment. It experiences one episode. At the first
step it hears a bell. At the second step it sees a light. At the third step it
both hears a bell and sees a light. It then receives some food, worth +1
reward, and the episode terminates on the fourth step. All other rewards
were zero. The experiment is undiscounted (i.¢., y = 1).

We may represent the rat’s state ‘s’ by a vector of two binary features,
bell(s) € {0, 1} and light(s) €{0, 1}. So, the sequence of feature vectors

corresponding to the four steps of this episode can be expressed as, [1, 0]’,
[0, 1]", [1, 1]" and [0, oJ". ;

Approximate the state-value function by a linear combination of these
features with two parameters: [b x bell(s) + | x light(s)]. If b = 3 and 1=
—3, then write down the sequence of approximate values corresponding to
this episode. ,

[6]

CO-3;
BL-4

Write down the sequence of A-returns G;* (1 <t <3) corresponding to this
episode, for A = 0.5, and b = 3, | =—3. Clearly show the detailed
evaluations.

Hint:

The n-step return and A-return G? are given as,

of = Reg t+ 7Reyat PRs to +7 Ren + 1°V (stan)

7
@ = (-d)axrhel”
n=1

where, Go) = RiyritryReyet VY Ri3 +++-+97- Rp, with multiplication factor being yt

[6]

CO-2;
BL-3

Using linear value function approximation, write down the sequence of
TD(A) accumulating eligibility trace e corresponding to the bell, using o
=0.5,y=1.

The equation for eligibility trace is given as: e: = yaer1 + bell(st)

[4]

CO-2;
BL-3

Using the backward-view TD(A) algorithm and your linear function
approximator, what are the sequence of updates to weight b? (Use offline
updates, i.e., do not actually change your weights, just accumulate your
updates). What is the total update to weight b? Use 4 = 0.5, y= 1, a = 0.5,
and start with b = 3, 1=~-3.

Ot = Resi + yV(St41) _ V(S:)
V(s) + V(s) + a6;E;(s)

[4]
````

## 2023-24 · Final-Exam · Sem 12 · paper a04d44b6eaff

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/COMPUTER/Sem_12/Reinforcement Learning/Reinforcement Learning Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 85.5

````text
SVKM’S NMIMS-
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024 e
Program/s: B Tech Integrated Year: VI Semester: XII

Stream/s ; Computer Engg

Subject: Reinforcement Learning Time: 3 hrs (2:eopeto 5” —

Date:_2 / & /2024 No. of Pages:_4 _
Marks: 100

¥

Final aaeaitieen ( nl sia!
the cover of the Answer Book, which is provided for their use.

1) Question No. _1____is compulsory.

2) Out of remaining 4 ions, attemptany 4 questions.
3)Inall__5_ questions to be attempted. ,

‘4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly: [20]
i .
CO- 1; a. | oo. . . .
80-5; | For application of Reinforcement learning example of Bipedal Walker, [05]
BL-4 define objective, state, action reward and termination.
CO- 2; b. i What are the key components of the Bellman equation, and how is it used
SO- 2; in dynamic programming? [05]
BL-2 |
me CO- 3; 6. . Pe : .
; 0-5: Contrast TD(0) with TD(1) learning, highlighting the differences in the [05]
> update equations and their implications.
BL-2
CO- 2; d. Write and describe al gorithm for Sarsa (on-policy TD control) for
| SO- 3; estimating Q = q* [05]
‘BL- 3
Q2 a
CO- 1; Difference between Reinforcement learning and Supervised learning and [10]
SO- 3; elaborate the role of discount factor in reinforcement learning
BL-3
CO-3; b
S0-1: Explain the difference between Monte Carlo prediction and Monte Carlo - [10] -
BL-1 , contro] in reinforcement learning
--- page 2 ---
a Describe the concept of, first-visit and every-visit Monte Carlo methods in
reinforcement learning ; 2
Consider a finite, episodic and undiscounted Markov Decision Process
(MDP) with states A and B apart from the terminal state. Let the following
two samples are observed when a Monte-Carlo (MC) evaluation is being

carried out.
3 Episode 1 Episode 2
a (A, #3) 8,2)
Sor (A, #2) (A,3) [10]
BLA 4) | 6-3)
(A, +4)
* (B, 3)
Estimate the state value of both A and B using every-visit Monte-Carlo
evaluation. ;
Ans
CO-3; b . - .
SO-1: How do k-step TD estimators generalize TD(0) and TD(1)? Discuss their
BL3 application in reinforcement learning
a Consider the following environment in which states s0, s1, s2, s3, s4 and
s5 are shown in the grid below (see Figure (a) below). s0 is the terminal
state. Agent can take one of four possible actions at each state, other than
the terminal state: i.e. Left, Right, Up or Down. Also, assume that the
reward at each state is given as indicated in the Figure (b) below.
. So, Terminal, +50 | S1, Right, -1 { S2, Left, -2
| Q4
9 . S3, Up, -1 S4, Up, -2 S5, Left, -3
CO-4; . 10]
SO-3; Episodes [
BL-4 El: (S4,U,-2) to (S1,R,-1) to(S2,L,-2) to(S1,stop,-1)
E2: (S3,U,-1) to {S0,stop, +50):
E3: (S5,L,-3) to (S4,U,-2) to (S1,R,-1) to (S2,stop,-2)
Estimate the state values of each state using the First-Visit Monte Carlo
evaluation given the following sample episodes
CO-4; * |b . . ee ‘ .
50-3: Describe the concept of function approximation in reinforcement learning [10]

BL2 and its role in handling large state spaces
--- page 3 ---
Q5

| CO-3;
SO-1;
BL-5

Consider the following Markov Decision Process (MDP) with discount
factor y =.0.9. Upper case letters A, B, C represent states; arcs represent
state transitions; lower case letters ab, ba, be, ca, cb represent actions;
signed integers represent onsale; and fractions represent transition
probabilities

I. Define the state-value function Vz(s) for a discounted MDP (1
mark)

I. Write down the Bellman expectation equation for state-value
functions. (2 mark)

II. Consider the uniform random policy 7:(s,a) that takes all actions
from state s with equal probability. Starting with an initial value
function of Vi(A) =Vi(B) =Vi(C) = 3, apply one synchronous _
iteration of iterative policy evaluation (i.e. one backup for eacli
state) to compute a new value function V2(s) (3 marks)

1V. Apply one iteration of greedy policy improvement to compute a
new, deterministic policy 72(s) (2 marks)

VY.   Consider-a deterministic policy x(s). Prove that ifa new policy T°
is greedy with respect to V" then it must be better than or equal to
m, i.e. V™ (s) > V*(s) for all s; and that if. V* (s) = V*(s) for all s
then x’ must be an optimal policy. (5 marks)

VI. Define the optimal state-value function V*(s) for an MDP (1
marks)

VIL Write down the Bellman optimality equation for state-value
functions (2 marks)

VIII. Starting with an initial value function of Vi(A) = Vi(B) = Vi(C) =
2, apply one synchronous iteration of value iteration (i.e. one

[20]
--- page 4 ---
backup for each_state) to compute a new value function Va(5).8

marks)
IX. _ Is your new value function V2(s) optimal? Justify your answer (1

mark)
Q6 a : ; ;
CO-2; » Describe the difference between iterative policy evaluation and full policy [10]
SO-4; evaluation in dynamic programming.
BL-2 ; . : _
CO-3; b Explain the concept of bootstrapping in dynamic programming and its
SO- 5; significance in reinforcement learning ~ | [10]
BL-2
Q7 a . . “s . . ;
C03; ; Hylan how the Retnions algorithm can be modified to incorporate
SO-7: baselines and how it affects the variance of gradient estimates. [10]
BL-3
CO-3: b Describe the architecture and training procedure of an Actor-Critic
s 0-7. network and how it combines value estimation (Critic) with policy [10]

BL-4 improvement (Actor).
````

## 2023-24 · Re-Exam · Sem 12 · paper be71cd33b6b9

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/COMPUTER/Sem_12/Reinforcement Learning/Reinforcement Learning Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 88.0

````text
SVKM’S.NMIMS

SCHOOL.OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program/s: B Tech Integrated Year: VI ee XII
Stream/s ; Computer Engg

Subject: Reinforcement Learning Time: 3 hrs ( 2:00pm to 5:00 pw)
Date:_4_/ 7 /2024 No. of Pages:04 —

Marks: 100

Re Examination (2023 — 24)
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
_~ 2) Out of remaining questions, attempt any 4 _ questions.

3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.
a Answer briefly: [20]
CO- 1; a. or . .
50-5 : For application of Reinforcement learning example of cart Pole, define [05]
BL- 4 objective, state, action reward and termination.
CO- 2; b. . . 4 6 ; i
50-2: Explain the concept of policy evaluation in dynamic programming for [05]
BL- 5 reinforcement learning.

m™ | CO-3; c. . ; : '

50-5: Explain the TD(0) algorithm and how it updates value estimates based on [05]
BL- > immediate rewards and estimates of future rewards.
CO- 2; d.
SO- 3; Write and describe algorithm for Tabular TD(0) for estimating vx [05]
BL- 3
Q2 a
CO- 1; Differentiate partial MDP with MDP and elaborate the role of discount [10]
SO- 3; factor in reinforcement learning
BL-3
CO-3; b

50-1: What is the fundamental idea behind Monte Carlo methods in [10]
BL. i reinforcement learning?
--- page 2 ---
a Describe the concept of first-visit and every-visit Monte Carlo methods in
reinforcement learning - . 3
Consider a finite, episodic and undiscounted Markov Decision Process
(MDP) with states A and B apart from the terminal state. Let the following
two samples are observed when a Monte-Carlo (MC) evaluation is being

carried out.

Q3 Episode 1 Episode 2
CO-4; (A, +3) (B, —2) [10]
SO-3; (A, +2) (A, +3)
BL-7 (B, —4) (B,=3)
(A, +4) terminate
(B, -3)
terminate

Estimate the state value of both A and B using first-visit Monte-Carlo

evaluation.
CO-3; b . F .
SO-1: Describe the advantages and disadvantages of TD(A) learning compared to
ors TD(0) and TD(1).
a Consider the following environment in which states sO, sl, s2, s3, s4 and
s5 are shown in the grid below (see Figure (a) below). sO is the terminal
state. Agent can take one of four possible actions at each state, other than
the terminal state: i.e. Left, Right, Up or Down. Also, assume that the
reward at each state is given.as indicated in the Figure (b) below.
So, Terminal, +50 } S1, Right, -1 | S2, Left, -3
Co $3, Up, -1 S4, Up, -2 S5, Left, -4
SO-3; Episodes [19]
BL-4 E1: (S4,U,-2) to (S1,R,-1) to(S2,L,-3) to(S1,stop,-1)
E2: (S3,U,-1) to (S0,stop,+50)
E3: (S5,L,-4) to (S4,U,-2) to (S1,R,-1) to (S2,stop,-2)
Estimate the state values of each state using the First-Visit and Every
Monte Carlo evaluation given the following sample episodes
CO-4; b Discuss the exploration-exploitation trade-off in TD control methods like
SO-3; ° SARSA and Q-Learning. How do they balance exploration and [10]
BL-2 exploitation?
Q5 Consider the following Markov Decision Process (MDP) with discount [20]

CO-3; factor y = 0.5. Upper case letters A, B, C represent states; arcs represent
--- page 3 ---
SO-1; state transitions; lower case letters ab, ba, bc, ca, cb represent actions;
BL-5 signed integers represent rewards; and fractions represent transition
probabilities

3/4

I. Define the state-value function Vx(s) for a discounted MDP (1
mark)
II. | Write down the Bellman expectation equation for state-value
functions. (2 mark)

Ill. | Consider the uniform random policy 7)(s,a) that takes all actions
from state s with equal probability. Starting with an initial value
function of Vi(A) =Vi(B) =Vi(C) = 2, apply one synchronous
iteration of iterative policy evaluation (i.e. one backup for each
state) to compute a new value function V2(s) (3 marks)

IV. Apply one iteration of greedy policy improvement to compute a
new, deterministic policy 72(s) (2 marks)

V. Consider a deterministic policy z(s). Prove that if a new policy 7’
is greedy with respect to V* then it must be better than or equal to
t, i.e. V* (s) > V* (s) for all s; and that if. V” (s) = V"(s) for all s
then x’ must be an optimal policy. (5 marks)

VI. Define the optimal state-value function V*(s) for an MDP (1
marks) 2

VII. | Write down the Bellman optimality equation for state-value
functions (2 marks)

VIII. Starting with an initial value function of Vi(A) = Vi(B) = Vi(C) =
2, apply one synchronous iteration of value iteration (i.e. one
backup for each state) to compute a new value function V2(s). (3
marks)
--- page 4 ---
IX. _ Is your new value function V2(s) optimal? Justify your answer d

aa

mark) ~

Q6
CO-2; Discuss the advantages of policy approximation methods compared to

: ; ; [10]
SO-4; value-based methods in handling large action spaces
BL-2 «
CO-3; ' i .
50-5: Compare and contrast different bandit algorithms such as e-greedy, UCB, [10]
BL > and Thompson Sampling, highlighting their strengths and weaknesses
Q7
CO-3; What is the role of baselines in reducing the variance of policy gradient [10]
SO- 7; estimates?
BL-3
CO-3; an , P .
SO-7: Compare and contrast Actor-Critic methods with pure policy gradient [10]
BL 4 methods like Reinforce.
````
