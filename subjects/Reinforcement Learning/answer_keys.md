# Reinforcement Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d9afe6b83943

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Reinforcement Learning/ANS_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (21 pages), mean OCR confidence 66.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
Q1
Answer briefly:   [20]
a   Explain types of Reinforcement Learning.
Answer:
CO-1;   Immediate vs Delayed Reinforcement [3M for each]
SO-1;   [05]
BL-2   Positive Reinforcement Learning or Negative Reinforcement Learning”-
2M or any other valid classification.
b   Define the Bellman Equation for state-value function.
Answer:
The Bellman Equation is a fundamental recursive relationship in RL,
introduced by Richard Bellman (1957), that expresses the value of a state
in terms of the immediate reward and the discounted value of successor
states. (1M)
CO-3;   The State-Value Function Vπ(s) is the expected cumulative return starting
SO-1;   from state s under policy π: (2M)   [05]
BL-2   Vπ(s) = 𝔼π [ Gₜ | Sₜ = s]
Expanding the return recursively (since Gₜ = Rₜ₊₁ + γ Gₜ₊₁), the Bellman
Equation becomes:
Vπ(s) = Σₐ π(a|s) Σₛ' P(s'|s, a) [ R(s, a, s') + γ Vπ(s')]
Where:
π(a|s) = probability of selecting action a in state s
P(s'|s, a) = probability of transitioning to next state s'
R(s, a, s') = immediate reward received
γ = discount factor (0 ≤ γ ≤ 1)
********** 1 **********
--- page 2 ---
Vπ(s') = bootstrapped value of the next state
In simple words:
Value of current state = Expected [ Immediate Reward + γ × Value of Next
State]
Bellman Optimality Equation: (2M)
For the optimal policy π, the optimal value V(s) satisfies:
V(s) = maxₐ Σₛ' P(s'|s, a) [ R(s, a, s') + γ V(s')]
This selects the action that maximizes the sum of immediate reward and
discounted future value.
Bellman Equation for Q-Function:
Qπ(s, a) = Σₛ' P(s'|s, a) [ R(s, a, s') + γ Σₐ' π(a'|s') Qπ(s', a')]
This form is the foundation of SARSA and Q-Learning.
c   Discuss the efficiency of Dynamic Programming methods in solving
MDPs. What are the major challenges and limitations?
Answer:
Dynamic programming refers to a collection of algorithms that can be used
to compute optimal policies given a perfect model of the environment as
an MDP. Dynamic programming for MDP assumes full knowledge of the
transition and reward models of the MDP. (1M)
Efficiency of Dynamic Programming (DP): (2M)
Dynamic Programming methods such as Value Iteration and Policy
Iteration are widely used to solve Markov Decision Processes (MDPs).
They are efficient because they systematically compute optimal value
CO-2,4;   functions and policies using the Bellman equations. DP guarantees
SO-1;   convergence to the optimal solution when the model (transition   [05]
BL-2   probabilities and rewards) is known. It also reuses previously computed
results, reducing redundant calculations.
Challenges and Limitations: (2M)
1. Requirement of Complete Model:
DP requires full knowledge of the transition model and reward
function, which is often unavailable in real-world problems.
2. Curse of Dimensionality:
As the number of states and actions increases, computation and
memory requirements grow exponentially, making DP impractical
for large-scale problems.
3. High Computational Cost:
Iterative updates over all states and actions can be time-consuming,
especially for large MDPs.
4. Scalability Issues:
DP methods do not scale well to continuous or very large state
spaces.
********** 2 **********
--- page 3 ---
5. Not Suitable for Online Learning:
DP is typically an offline method and cannot directly learn from
real-time interaction with the environment.
While Dynamic Programming is theoretically powerful and guarantees
optimal solutions, its practical use is limited by computational complexity
and the need for a complete model of the environment.
d   Write short note on Actor-Critic methods.
Answer:
Actor Critic method is a reinforcement learning approach that combines
elements of both policy-based (actor) and value-based (critic) methods to
improve learning efficiency and stability. In this framework, the actor and
critic work together in a coordinated way to optimize the policy. (1M)
Components
• Actor
CO-5;   •   Critic
SO-1;   Actor: The actor represents the policy, which decides which action to take   [05]
BL-2   given a state. It directly updates the policy parameters in the direction that
maximizes expected cumulative rewards, often using a policy gradient
method. The actor’s goal is to maximize the rewards by making better action
selections over time. (2M)
Critic: The critic estimates the value function (usually the state value V(s)
or action value Q( s,a) function), which represents the expected return from
a given state or state action pair. It provides feedback (called the temporal
difference (TD) error) to the actor about how good the actions taken were,
relative to the expected value. The TD error helps the actor understand
whether it should adjust its policy in a positive or negative direction. (2M)
a   Define Reinforcement Learning (RL). Describe the key component
involved in the RL framework with a suitable example and diagram.
Answer:
(Give all the component relating to any suitable Example)
Define Reinforcement Learning (RL):- 2M
Q2
Framework Diagram: - 2M
CO-1;
[10]
SO-1;   Description about key component: - 6M (With related to the suitable
BL-2
Example)
Reinforcement learning (RL) is a branch of machine learning where the
learning of the Agent occurs via interacting with an Environment.
Environment: The world or system the agent interacts with. It receives
actions from the agent and responds with new states and rewards.
********** 3 **********
--- page 4 ---
State (s): A representation of the current situation or configuration of the
environment. This is the information available to the agent for decision-
making.
Action (a): The choices available to the agent. These are the decisions the
agent can make that affect the environment.
Reward (r): A scalar feedback signal that indicates how good or bad an
action was. The agent's goal is to maximize cumulative rewards over time.
Policy (π): The agent's strategy for selecting actions based on states. It can
be deterministic (always choosing the same action for a given state) or
stochastic (choosing actions probabilistically).
b   Consider the following environment with states and rewards as mentioned.
Each arrow indicates the policy the immediate reward received upon
moving to the next state. The goal state is S9 and its state value is 0.
Assume that the actions are deterministic. Apply the Bellman Equation and
find:
i.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.9.
ii.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.1.
CO-3   iii.   State your comment based on evaluation done for both
SO-1;   the discount factors.   [10]
BL-3,4
********** 4 **********
--- page 5 ---
Apply the Bellman equation 𝑉(𝑠) = 𝑅(𝑠, 𝑎, 𝑠′) + 𝛾𝑉(𝑠′),
Note: Work backwards from terminal state to calculate value can complete
the following table.
Answer: (4M + 4M +2M)
State Reward Next State V(s) for γ = 0.9   V(s) for γ = 0.1
S8   20   S9   20+0.9*0=20   20+0.1*0=20
S7   -2   S8   -2+0.9* 20 = 16   -2+0.1* 20 = 0
S6   20   S9   20+0.9.0=20   20+0.1.0=20
S5   -2   S8   -2+0.9*20=16   -2+0.1*20=0
S4   -4   S5   -4+0.9*16=10.4   -4+0.1*0=-4
S3   -4   S6   -4+0.9*20 =14   -4+0.1*20 = -2
S2   -2   S3   -2+0.9*14=10.6   -2+0.1*(-2)=-2.2
S1   -2   S2   -2+0.9*10.6=7.54 -2+0.1*(-2.2) =-2.22
Comment:
For γ = 0.9, the values of states are higher and mostly positive.
For γ = 0.1, the values are much smaller and many are negative.
The difference becomes more significant for states farther from the
terminal state.
A higher discount factor (γ = 0.9) gives more importance to future rewards,
so states accumulate the benefit of rewards obtained later. This results in
larger state values, even for earlier states like S1 and S2.
A lower discount factor (γ = 0.1) emphasizes immediate rewards, reducing
the influence of future rewards. As a result, penalties dominate, and many
state values become negative or very small.
Therefore, γ controls how far-sighted the agent is:
High γ → long-term planning (future rewards matter more)
Low γ → short-term behaviour (immediate rewards dominate)
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states P and Q and a terminal state T.
Assume the discount factor γ = 0.7.
Episode 1: P 4 Q 3 P 2 T
Q3   Episode 2: Q 5 P 1 Q 2 T
CO-2,4;   Estimate the state value using First Visit Monte Carlo.
[10]
SO-1   Estimate the state value using Every Visit Monte Carlo.
BL-4,5   Construct Markov model that best explains the observations.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (4M+4M+2M)
********** 5 **********
--- page 6 ---
Returns
Episode 1:
P₁ = 4 + 0.7(3) + 0.7²(2)
= 4 + 2.1 + 0.98 = 7.08
Q = 3 + 0.7(2) = 4.4
P₂ = 2
Episode 2:
Q₁ = 5 + 0.7(1) + 0.7²(2)
= 5 + 0.7 + 0.98 = 6.68
P = 1 + 0.7(2) = 2.4
Q₂ = 2
First Visit Monte Carlo
P = (7.08 + 2.4) / 2 = 4.74
Q = (4.4 + 6.68) / 2 = 5.54
Every Visit Monte Carlo
P = (7.08 + 2 + 2.4) / 3 = 3.83
Q = (4.4 + 6.68 + 2) / 3 = 4.36
iii. Construct Markov Model (with Probabilities)
Transition Counts
From P:
P → Q = 2
P → T = 1
Total = 3
From Q:
Q → P = 2
Q → T = 1
Total = 3
Transition Probabilities
P(P → Q) = 2/3 = 0.67
P(P → T) = 1/3 = 0.33
P(Q → P) = 2/3 = 0.67
P(Q → T) = 1/3 = 0.33
Final Markov Model
P → Q, P → T
Q → P, Q → T
********** 6 **********
--- page 7 ---
b   Explain how iterative updates are used in Dynamic Programming methods
(Value Iteration/Policy Iteration) for solving MDPs. Also mention any two
challenges or limitations of these methods.
Answer: (3M+2M)
Dynamic Programming methods such as Value Iteration and Policy
Iteration use iterative updates to compute optimal solutions for Markov
Decision Processes (MDPs).
In Value Iteration, the value of each state is repeatedly updated using the
Bellman optimality equation. At every iteration, the algorithm selects the
action that maximizes the expected return and updates the state value
accordingly. This process continues until the change in values becomes
CO-2,4   very small (convergence).
SO-1
[05]
BL-2   In Policy Iteration, iteration occurs in two steps:
•   Policy Evaluation: Iteratively compute the value function for the
current policy.
•   Policy Improvement: Update the policy by choosing better
actions.
These steps repeat until the policy becomes stable.
Challenges / Limitations:
•   Requires complete knowledge of transition probabilities and
rewards.
• Computationally expensive for large state spaces (curse of
dimensionality).
c   Define on-policy and off-policy learning in the context of Monte Carlo
methods. Give one real-world example of each. Explain the role of the
behavior policy and the target policy in off-policy Monte Carlo learning.
Answer:
On-policy Learning (Monte Carlo): (1.5M)
On-policy learning refers to learning the value of a policy using episodes
CO-2,4   generated by the same policy. In Monte Carlo methods, the agent follows a
SO-1   single policy to generate episodes and updates the value function based on   [05]
BL-2,3   the returns observed from those episodes. The behavior policy and target
policy are the same.
Example:
A robot learning to navigate a maze by following its current policy (e.g., ε-
greedy) and improving it based on the rewards received while following
that same policy.
********** 7 **********
--- page 8 ---
Off-policy Learning (Monte Carlo): (1.5M)
Off-policy learning refers to learning the value of a target policy using
episodes generated from a different policy called the behavior policy. This
allows learning from exploratory or previously collected data.
Example:
A self-driving car learning the optimal driving strategy (target policy)
using data collected from human drivers (behavior policy).
Role of Behaviour Policy and Target Policy in Off-policy Monte Carlo:
(2M)
• Behavior Policy (b): It is the policy used to generate episodes. It is
usually more exploratory to ensure sufficient coverage of state-
action pairs.
•   Target Policy (π): It is the policy whose value function we want to
learn or evaluate. It is typically more optimal or greedy.
Since the data is generated using the behavior policy but evaluated for the
target policy, there is a mismatch. To correct this, importance sampling is
used, which reweights the returns based on the likelihood of actions under
both policies. This ensures that the estimated values accurately reflect the
target policy.
a   Consider a Multi-Armed Bandit problem with the following parameters:
Time step t = 5
Number of bandits (machines) = 4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
The probability of winning for each machine is:
Q4   Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
CO-2
SO-1   Assume that the random number generated for selection of one machine in   [10]
BL-3,4   the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
Answer: (4M + 4M + 2M)
********** 8 **********
--- page 9 ---
b   A student switches between Study Mode (S1) and Relax Mode (S2).
Actions: Study or Relax. From Study: Study → 0.7 stay, 0.3 go to Relax,
From Relax: Study → 0.6 go to Study, 0.4 stay Relax → always stay
Rewards: +5 for Study and +1 for Relax
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
Answer (2.5M + 2.5M)
MDP Representation States: S1: Study, S2: Relax, Actions: Study, Relax
Transition Probabilities
CO-3   From S1: P(S1, +5 | S1, Study) = 0.7, P(S2, +1 | S1, Study) = 0.3, P(S2, +1
SO-1   | S1, Relax) = 1.0   [05]
BL-3   From S2: P(S1, +5 | S2, Study) = 0.6, P(S2, +1 | S2, Study) = 0.4, P(S2, +1
| S2, Relax) = 1.0
Summary Table
Current State   Action Next State   𝑝(𝑠′, 𝑟|𝑠, 𝑎) Reward
S1   Study   S1   0.7   +5
S1   Study   S2   0.3   +1
S1   Relax   S2   1.0   +1
S2   Study   S1   0.6   +5
S2   Study   S2   0.4   +1
S2   Relax   S2   1.0   +1
State Diagram
S1 → S1 (Study, 0.7, +5)
S1 → S2 (Study, 0.3, +1)
********** 9 **********

[Text in pictures on this page, read by OCR]
We know that in 4 chances of

exploration, Random Reward obtained
© Machine M3 got played 3 times out of number i P.=P,

which it won twice generated for | That is P. <=0.6
= Machine M;got played one time and it reward P. Reward=1

won
Therefore, estimated values for each 1 0.33 1
machines are , 2 0.25 1
5 Q.(Mx) = 1,Q.(M2) = 0,Q.(M3) = 5 =

0.67,0.(Ms) = 0 3 0.55 1
From the Q, estimates , machine Myis 4 0.45 1
exploited for the next 6 steps

sin a 5 0.6 1

Probability of winning for
My is Py (M;) = 0.6 6 0.8 (0)

Random number generated to estimate
the rewards for remaining six iterations
are [0.33, 0.25, 0.55,0.45, 0.6, 0.8]
--- page 10 ---
S2 → S1 (Study, 0.6, +5)
S2 → S2 (Study, 0.4, +1)
Self-loops:
S2 → S2 (Relax, 1.0, +1)
c   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 3, R₂ = 6, R₃ = -4, R₄ = 2, R₅ = 8
i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.7
ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.4
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (2M + 2M + 1M)
Returns for γ = 0.7
t   Calculation   Gₜ
5 –   0
4 R₅   8
3 R₄ + 0.7·R₅   2 + 0.7·8 = 7.6
2 R₃ + 0.7·R₄ + 0.49·R₅   -4 + 0.7·2 + 0.49·8 = 1.32
CO-3
1 R₂ + 0.7·R₃ + 0.49·R₄ +   6 + 0.7·(-4) + 0.49·2 + 0.343·8 =
SO-1   [05]
0.343·R₅   6.924
BL-3,4
0 R₁ + 0.7·R₂ + 0.49·R₃ +   3 + 0.7·6 + 0.49·(-4) + 0.343·2 +
0.343·R₄ + 0.2401·R₅   0.2401·8 = 7.8448
Returns for γ = 0.4
t   Calculation   Gₜ
5 –   0
4 R₅   8
3 R₄ + 0.4·R₅   2 + 0.4·8 = 5.2
2 R₃ + 0.4·R₄ + 0.16·R₅   -4 + 0.4·2 + 0.16·8 = -1.92
1 R₂ + 0.4·R₃ + 0.16·R₄ +   6 + 0.4·(-4) + 0.16·2 + 0.064·8 =
0.064·R₅   5.232
0 R₁ + 0.4·R₂ + 0.16·R₃ +   3 + 0.4·6 + 0.16·(-4) + 0.064·2 +
0.064·R₄ + 0.0256·R₅   0.0256·8 = 5.0928
Comparison Table
Return γ = 0.7 γ = 0.4
G5   0   0
G4   8   8
********** 10 **********
--- page 11 ---
G3   7.6   5.2
G2   1.32   -1.92
G1   6.924   5.232
G0   7.8448 5.0928
Observation: Higher γ reduces the effect of negative rewards over time.
a   In the given example, the robot must move from the Start state 𝑟 to the
Target state 𝑎 with a reward structure of +80 for reaching the target and -2
for each step taken. Assume the initial Q-value to be zero and discount factor
= 0.8. Apply the Monte-Carlo Exploring Starts Algorithm with T=6 and
initial random state as (𝑔, 𝐿) update the policy for given episode E1 and E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.8, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Episodes:
E1: (𝑔, 𝐿) →(𝑓, 𝑅) →(𝑔, 𝑅) →(ℎ, 𝑈) →(𝑐, 𝐿) →(𝑏, 𝐿) →(𝑎, 𝑠𝑡𝑜𝑝)
E2: (𝑖, 𝐷) →(𝑚, 𝑈) →(𝑖, 𝑈) →(𝑒, 𝐿) →(𝑑, 𝑅) →(𝑐, 𝐿) →(𝑏, 𝑅)
Target
Q5   a   b   c   d   e
CO-2,4
SO-1   [10]
BL-3, 4   f   g   h   i
j   k   m
n   o   p   q   r
Answer: (5x2M)
•   Target reward = +80
•   Step penalty = −2
• Discount factor γ=0.8
•   Initial Q(s,a)=0
• Episode length T=6
Episode 1
Return Calculation (Episode 1)
********** 11 **********
--- page 12 ---
Using:
Gt=Rt+1+γGt+1
t   (State, Action)   Return Gt
7   (a, stop)   80
6 (b, L)   −2 + 0.8(80) = 62
5   (c, L)   −2 + 0.8(62) = 47.6
4 (h, U)   −2 + 0.8(47.6) = 36.08
3 (g, R)   −2 + 0.8(36.08) = 26.864
2   (f, R)   −2 + 0.8(26.864) = 19.4912
1 (g, L)   −2 + 0.8(19.4912) = 13.5930
Policy Update (Episode 1)
State Action   Q(s,a)
g   L   13.593
f   R   19.491
g   R   26.864
h   U   36.08
c   L   47.6
b   L   62
a   stop   80
For state g, choose best action:
•   Best = R (26.864)
Episode 2:
Return Calculation (Episode 2)
(No terminal reached → all rewards = −2)
t   (State, Action)   Return Gt
7 (b, R)   −2
6   (c, L)   −2 + 0.8(−2) = −3.6
5 (d, R)   −2 + 0.8(−3.6) = −4.88
4   (e, L)   −2 + 0.8(−4.88) = −5.904
3   (i, U)   −2 + 0.8(−5.904) = −6.7232
2 (m, U)   −2 + 0.8(−6.7232) = −7.3786
1   (i, D)   −2 + 0.8(−7.3786) = −7.9029
Policy Update (Episode 2)
State Action   Q(s,a)
i   D   −7.903
********** 12 **********
--- page 13 ---
m   U   −7.379
i   U   −6.723
e   L   −5.904
d   R   −4.88
c   L   avg(47.6, −3.6) = 22.0
b   R   −2
Final Policy
State Best Action Q value
g   R   26.864
f   R   19.491
h   U   36.08
c   L   22.0
b   L   62
a   stop   80
d   R   −4.88
e   L   −5.904
i   U   −6.723
m   U   −7.379
• MC-ES uses full return Gt (no bootstrapping)
• Episode reaching goal → high positive returns
• Non-terminal episode → negative returns
•   Policy updated using maximum Q(s,a)
• Repeated state-action pairs use average returns
b   With reference to TD Learning and SARSA, answer the following:
(i) Explain TD (0) and TD (1) approaches in RL.
(ii) Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
Take α = 0.2 and γ = 0.9.
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
CO-2,4   steps.
SO-1   Hint: V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
[10]
BL-2,3   SARSA Update Rule:
Q (Sₜ, Aₜ) ← Q (Sₜ, Aₜ) + α [ Rₜ₊₁ + γ Q (Sₜ₊₁, Aₜ₊₁) – Q (Sₜ, Aₜ)]
Answer: (4M + 6M)
i. TD (0) and TD (1) in Reinforcement Learning
Temporal Difference (TD) learning is a model-free, online RL method that
learns directly from experience by combining ideas from both Monte Carlo
(MC) and Dynamic Programming (DP). It updates value estimates at every
step using bootstrapping — using a learned estimate to update another
estimate.
********** 13 **********
--- page 14 ---
TD (0) — One-Step TD:
TD (0) updates the value of the current state using only the immediate next
reward and the estimated value of the next state.
Update Rule:
V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
TD Target: Rₜ₊₁ + γ V(Sₜ₊₁)
TD Error (δₜ): Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)
Updates happen at every step (online)
Low variance but slight bias due to bootstrapping
TD (1) — Equivalent to Monte Carlo:
TD (1) is the other extreme where the update is based on the complete
return Gₜ — the sum of all rewards until the end of the episode.
Update Rule:
V(Sₜ) ← V(Sₜ) + α [ Gₜ − V(Sₜ)]
Uses the full actual return with no bootstrapping
Updates only at the end of each episode
Unbiased but high variance
(ii)
Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
Take α = 0.2 and γ = 0.9. (6 marks)
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
steps.
Answer:
Q-Table:
State   A1   A2
S1   5.0   3.0
S2   4.0   7.0
α = 0.2, γ = 0.9
Experience tuple: ⟨S1, A1, 6, S2, A2⟩
Step 1 — Identify the Experience Tuple
The SARSA experience tuple ⟨S, A, R, S', A'⟩ contains five elements:
Symbol   Value   Meaning
S   S1   Current state
A   A1   Action taken in S1
********** 14 **********
--- page 15 ---
R   6   Reward received
S'   S2   Next state transitioned to
A'   A2   Next action selected in S2
Step 2 — Identify Which Q-Value is Updated
In SARSA, the Q-value that gets updated is always Q (S, A) — the Q-
value of the current state-action pair that was just executed.
Q (S1, A1) is the value to be updated
Current value: Q (S1, A1) = 5.0
Step 3 — Write the SARSA Update Rule
Q (S, A) ← Q (S, A) + α × [R + γ × Q (S', A') – Q (S, A)]
Where:
R + γ × Q (S', A') is the TD Target — the estimated true value based on the
actual next action taken
R + γ × Q (S', A') – Q (S, A) is the TD Error (δ) — how wrong the current
estimate was
Step 4 — Substitute All Known Values
Q (S1, A1) ← Q (S1, A1) + α × [R + γ × Q (S2, A2) – Q (S1, A1)]
Substituting:
Q (S1, A1) = 5.0, α = 0.2, R = 6, γ = 0.9
Q (S2, A2) = 7.0
Q (S1, A1) ← 5.0 + 0.2 × [6 + 0.9 × 7.0 − 5.0]
Step 5 — Compute the TD Target
TD Target = R + γ × Q (S2, A2)
TD Target = 6 + 0.9 × 7.0
TD Target = 6 + 6.3
TD Target = 12.3
Step 6 — Compute the TD Error
TD Error (δ) = TD Target – Q (S1, A1)
TD Error (δ) = 12.3 − 5.0
TD Error (δ) = 7.3
********** 15 **********
--- page 16 ---
Step 7 — Compute the Update
Correction = α × TD Error
Correction = 0.2 × 7.3
Correction = 1.46
Step 8 — Compute New Q (S1, A1)
Q (S1, A1) ← 5.0 + 1.46
Q (S1, A1) = 6.46
Updated Q-Table:
State A1   A2
S1   6.46 (updated)   3.0
S2   4.0   7.0
a   Consider an n-armed bandit problem where the action values are estimated
using incremental methods. Apply the incremental update rule to compute
action-value estimates for a given sequence of rewards. Analyze how the
choice of step-size parameter affects convergence and stability of
estimates. Evaluate the effectiveness of incremental implementation
compared to sample-average methods in practical scenarios
Answer: (4M + 3M +3M)
Application of Incremental Update Rule
In an n-armed bandit problem, the action-value estimate can be updated
incrementally without storing all past rewards.
The incremental update rule is:
Q(n+1) = Q(n) + α [R(n) − Q(n)]
Q6
Where:
CO-2
Q(n) = current estimated value
SO-1   [10]
R(n) = reward obtained at step n
BL-3,4,5
α = step-size parameter
For sample-average method, α = 1/n.
Example:
Let rewards for an action be: 10, 8, 6
Step 1:
Q1 = 10
Step 2:
Q2 = 10 + (1/2)(8 − 10) = 10 − 1 = 9
Step 3:
Q3 = 9 + (1/3)(6 − 9) = 9 − 1 = 8
Thus, the action-value is updated step by step using only the previous
estimate and new reward.
Effect of Step-Size Parameter
The step-size parameter α controls how much new information affects the
estimate.
********** 16 **********
--- page 17 ---
If α = 1/n (decreasing step size):
Gives equal weight to all past rewards
Converges slowly but is stable
Suitable for stationary environments
If α is constant (e.g., 0.1):
Gives more weight to recent rewards
Adapts quickly to changes
May cause fluctuations (less stable)
Thus:
Small α → slow learning but stable
Large α → fast learning but less stable
Evaluation of Incremental Implementation (Evaluate)
Advantages over sample-average method:
Does not require storing all past rewards
Computationally efficient
Suitable for online and real-time learning
Works well in non-stationary environments when α is constant
Limitations:
Choice of α is critical
Improper α may lead to slow convergence or instability
Incremental implementation is more practical and efficient than sample-
average methods, especially in dynamic environments, but requires careful
selection of step size.
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
CO-2,4   Intended direction = 0.6
SO-1   Opposite direction = 0.4   [10]
BL-2, 4   Assume:
Initial policy: Move East
Initial values = 0
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   Sta Mineral   Fuel   Ho   Landslide   Storm
rt   Site   Station   me   Zone   Zone
********** 17 **********
--- page 18 ---
Reward   0   +18   +9   +6   −130   −95
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
Answer: (2M+6M+2M)
Iteration 1: Policy Evaluation
V(S1)=0,  V(S2)=18,  V(S3)=9,  V(S4)=6,  V(S5)=−130,  V(S6)=−95
Policy Iteration
S1
East:
V(S1)=0.6(18)+0.4(9)=10.8+3.6=14.4V
West:
V(S1)=0.4(18)+0.6(9)=7.2+5.4=12.6
Best: East
S2
East:
V(S2)=0.6(−130)+0.4(6)=−78+2.4=−75.6
West:
V(S2)=0.4(−130)+0.6(6)=−52+3.6=−48.4
Best: West
S3
East:
V(S3)=0.6(6)+0.4(−95)=3.6−38=−34.4
West:
V(S3)=0.4(6)+0.6(−95)=2.4−57=−54.6
Best: East
Improved Policy
{E,  W,  E}
********** 18 **********
--- page 19 ---
a   Explain Policy Gradient Methods in Reinforcement Learning, discuss
policy approximation, and describe their advantages.
Answer:
Policy Gradient Methods: (3M)
Policy Gradient methods are a class of Reinforcement Learning techniques
that directly optimize the policy (π) instead of estimating value functions.
The policy is parameterized using θ, and the objective is to maximize the
expected cumulative reward.
The policy is represented as:
π(a|s, θ)
The parameters θ are updated using gradient ascent:
θ ← θ + α ∇θ J(θ)
Using the log-derivative trick, the gradient can be written as:
∇θ J(θ) = E[∇θ log π(a|s, θ) · R]
These methods learn by interacting with the environment and adjusting the
policy to increase the probability of actions that yield higher rewards.
Q7
CO-5
Policy Approximation: (3M)
SO-1   [10]
Policy Approximation refers to representing the policy using a
BL-2,3
parameterized function such as a neural network instead of a tabular form.
•   It maps states directly to action probabilities.
• Helps handle large or continuous state and action spaces.
• Enables generalization across similar states.
Advantages of Policy Gradient Methods: (4M)
•   Direct Optimization of Policy:
No need to derive policy from value functions; the policy is learned
directly.
•   Suitable for Continuous Action Spaces:
Works well in problems where actions are continuous (e.g.,
robotics).
•   Better Convergence in Some Cases:
Can converge to optimal stochastic policies.
• Handles High-Dimensional Problems:
Works effectively with function approximation like neural
networks.
•   Flexibility:
Can represent complex policies and adapt to dynamic
environments.
********** 19 **********
--- page 20 ---
Policy Gradient methods, combined with policy approximation, provide a
powerful and flexible approach to solving complex Reinforcement
Learning problems, especially in large-scale and continuous environments.
b   i.   Describe the concept of eligibility traces in TD(λ).
ii.   Consider an environment with 3 states: S1, S2, S3. The agent
moves sequentially to the next state:
• S1 → S2 gives reward 4
• S2 → S3 gives reward 5
• S3 → Terminal gives reward 3
Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3, V(terminal) =0
Using Temporal Difference TD (0), compute the updated values:
V(S1), V(S2), and V(S3).
Answer:
Describe the concept of eligibility traces in TD(λ). - 4M
Eligibility traces are a mechanism in Reinforcement Learning that allow an
agent to assign credit not only to the most recent state, but also to previous
states visited in the episode. In TD (0), only the current state is updated using
the immediate TD error. In TD(λ), eligibility traces keep track of how
recently and how frequently each state has been visited, enabling multiple
past states to be updated simultaneously.
Formula for trace decay
CO-2,4   𝐸(𝑠) = 𝛾𝜆𝐸(𝑠)
SO-1   Where:
BL-3,4   λ (0 ≤ λ ≤ 1) controls how far back credit is assigned   [10]
λ = 0 → behaves like TD (0)
λ = 1 → similar to Monte Carlo learning
Consider an environment with 3 states: S1, S2, S3. The agent moves
sequentially to the next state:
• S1 → S2 gives reward 4
• S2 → S3 gives reward 5
• S3 → Terminal gives reward 3
Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3
Using Temporal Difference TD (0), compute the updated values: V(S1),
V(S2), and V(S3).
𝑉(𝑠) ←𝑉(𝑠) + 𝛼[𝑟+ 𝛾𝑉(𝑠′) −𝑉(𝑠)]
Transition   Mathematical calculation   V(S V(S V(S
1)   2)   3)
Initial   2   1   3
value
S1 → S2   𝑉(𝑆1) ←𝑉(𝑆1) + 0.2[4   2.5   1   3
gives   + 0.9 ∗𝑉(𝑆2) 8
reward   --   −𝑉(𝑆1)]
2M   𝑉(𝑆1) ←2 + 0.2[4 + 0.9 ∗1
−2)]
********** 20 **********
--- page 21 ---
S2 — S3 V(S2)—1+0.2[5+0.9*3]2.5 | 2.3 |3
gives -1)] 8 4
reward 5 =2.34

--2M

S3 > V(S3) —3+0.2[3+0.9*0]2.5 | 2.3 | 3
Terminal — 3)] 8 4

gives =3

reward 3

--2M

V(S1) — V(S1) + a[r + yV(s') — V(s)]

FI ICR D7 FAC HOH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 56126022c988

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Reinforcement Learning/ANS_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (21 pages), mean OCR confidence 66.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (AI & ML)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Reinforcement Learning
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
Q1
Answer briefly:   [20]
a   Explain types of Reinforcement Learning.
Answer:
CO-1;   Immediate vs Delayed Reinforcement [3M for each]
SO-1;   [05]
BL-2   Positive Reinforcement Learning or Negative Reinforcement Learning”-
2M or any other valid classification.
b   Define the Bellman Equation for state-value function.
Answer:
The Bellman Equation is a fundamental recursive relationship in RL,
introduced by Richard Bellman (1957), that expresses the value of a state
in terms of the immediate reward and the discounted value of successor
states. (1M)
CO-3;   The State-Value Function Vπ(s) is the expected cumulative return starting
SO-1;   from state s under policy π: (2M)   [05]
BL-2   Vπ(s) = 𝔼π [ Gₜ | Sₜ = s]
Expanding the return recursively (since Gₜ = Rₜ₊₁ + γ Gₜ₊₁), the Bellman
Equation becomes:
Vπ(s) = Σₐ π(a|s) Σₛ' P(s'|s, a) [ R(s, a, s') + γ Vπ(s')]
Where:
π(a|s) = probability of selecting action a in state s
P(s'|s, a) = probability of transitioning to next state s'
R(s, a, s') = immediate reward received
γ = discount factor (0 ≤ γ ≤ 1)
********** 1 **********
--- page 2 ---
Vπ(s') = bootstrapped value of the next state
In simple words:
Value of current state = Expected [ Immediate Reward + γ × Value of Next
State]
Bellman Optimality Equation: (2M)
For the optimal policy π, the optimal value V(s) satisfies:
V(s) = maxₐ Σₛ' P(s'|s, a) [ R(s, a, s') + γ V(s')]
This selects the action that maximizes the sum of immediate reward and
discounted future value.
Bellman Equation for Q-Function:
Qπ(s, a) = Σₛ' P(s'|s, a) [ R(s, a, s') + γ Σₐ' π(a'|s') Qπ(s', a')]
This form is the foundation of SARSA and Q-Learning.
c   Discuss the efficiency of Dynamic Programming methods in solving
MDPs. What are the major challenges and limitations?
Answer:
Dynamic programming refers to a collection of algorithms that can be used
to compute optimal policies given a perfect model of the environment as
an MDP. Dynamic programming for MDP assumes full knowledge of the
transition and reward models of the MDP. (1M)
Efficiency of Dynamic Programming (DP): (2M)
Dynamic Programming methods such as Value Iteration and Policy
Iteration are widely used to solve Markov Decision Processes (MDPs).
They are efficient because they systematically compute optimal value
CO-2,4;   functions and policies using the Bellman equations. DP guarantees
SO-1;   convergence to the optimal solution when the model (transition   [05]
BL-2   probabilities and rewards) is known. It also reuses previously computed
results, reducing redundant calculations.
Challenges and Limitations: (2M)
1. Requirement of Complete Model:
DP requires full knowledge of the transition model and reward
function, which is often unavailable in real-world problems.
2. Curse of Dimensionality:
As the number of states and actions increases, computation and
memory requirements grow exponentially, making DP impractical
for large-scale problems.
3. High Computational Cost:
Iterative updates over all states and actions can be time-consuming,
especially for large MDPs.
4. Scalability Issues:
DP methods do not scale well to continuous or very large state
spaces.
********** 2 **********
--- page 3 ---
5. Not Suitable for Online Learning:
DP is typically an offline method and cannot directly learn from
real-time interaction with the environment.
While Dynamic Programming is theoretically powerful and guarantees
optimal solutions, its practical use is limited by computational complexity
and the need for a complete model of the environment.
d   Write short note on Actor-Critic methods.
Answer:
Actor Critic method is a reinforcement learning approach that combines
elements of both policy-based (actor) and value-based (critic) methods to
improve learning efficiency and stability. In this framework, the actor and
critic work together in a coordinated way to optimize the policy. (1M)
Components
• Actor
CO-5;   •   Critic
SO-1;   Actor: The actor represents the policy, which decides which action to take   [05]
BL-2   given a state. It directly updates the policy parameters in the direction that
maximizes expected cumulative rewards, often using a policy gradient
method. The actor’s goal is to maximize the rewards by making better action
selections over time. (2M)
Critic: The critic estimates the value function (usually the state value V(s)
or action value Q( s,a) function), which represents the expected return from
a given state or state action pair. It provides feedback (called the temporal
difference (TD) error) to the actor about how good the actions taken were,
relative to the expected value. The TD error helps the actor understand
whether it should adjust its policy in a positive or negative direction. (2M)
a   Define Reinforcement Learning (RL). Describe the key component
involved in the RL framework with a suitable example and diagram.
Answer:
(Give all the component relating to any suitable Example)
Define Reinforcement Learning (RL):- 2M
Q2
Framework Diagram: - 2M
CO-1;
[10]
SO-1;   Description about key component: - 6M (With related to the suitable
BL-2
Example)
Reinforcement learning (RL) is a branch of machine learning where the
learning of the Agent occurs via interacting with an Environment.
Environment: The world or system the agent interacts with. It receives
actions from the agent and responds with new states and rewards.
********** 3 **********
--- page 4 ---
State (s): A representation of the current situation or configuration of the
environment. This is the information available to the agent for decision-
making.
Action (a): The choices available to the agent. These are the decisions the
agent can make that affect the environment.
Reward (r): A scalar feedback signal that indicates how good or bad an
action was. The agent's goal is to maximize cumulative rewards over time.
Policy (π): The agent's strategy for selecting actions based on states. It can
be deterministic (always choosing the same action for a given state) or
stochastic (choosing actions probabilistically).
b   Consider the following environment with states and rewards as mentioned.
Each arrow indicates the policy the immediate reward received upon
moving to the next state. The goal state is S9 and its state value is 0.
Assume that the actions are deterministic. Apply the Bellman Equation and
find:
i.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.9.
ii.   Evaluate state value for all the states except the terminal
state for discount factor γ = 0.1.
CO-3   iii.   State your comment based on evaluation done for both
SO-1;   the discount factors.   [10]
BL-3,4
********** 4 **********
--- page 5 ---
Apply the Bellman equation 𝑉(𝑠) = 𝑅(𝑠, 𝑎, 𝑠′) + 𝛾𝑉(𝑠′),
Note: Work backwards from terminal state to calculate value can complete
the following table.
Answer: (4M + 4M +2M)
State Reward Next State V(s) for γ = 0.9   V(s) for γ = 0.1
S8   20   S9   20+0.9*0=20   20+0.1*0=20
S7   -2   S8   -2+0.9* 20 = 16   -2+0.1* 20 = 0
S6   20   S9   20+0.9.0=20   20+0.1.0=20
S5   -2   S8   -2+0.9*20=16   -2+0.1*20=0
S4   -4   S5   -4+0.9*16=10.4   -4+0.1*0=-4
S3   -4   S6   -4+0.9*20 =14   -4+0.1*20 = -2
S2   -2   S3   -2+0.9*14=10.6   -2+0.1*(-2)=-2.2
S1   -2   S2   -2+0.9*10.6=7.54 -2+0.1*(-2.2) =-2.22
Comment:
For γ = 0.9, the values of states are higher and mostly positive.
For γ = 0.1, the values are much smaller and many are negative.
The difference becomes more significant for states farther from the
terminal state.
A higher discount factor (γ = 0.9) gives more importance to future rewards,
so states accumulate the benefit of rewards obtained later. This results in
larger state values, even for earlier states like S1 and S2.
A lower discount factor (γ = 0.1) emphasizes immediate rewards, reducing
the influence of future rewards. As a result, penalties dominate, and many
state values become negative or very small.
Therefore, γ controls how far-sighted the agent is:
High γ → long-term planning (future rewards matter more)
Low γ → short-term behaviour (immediate rewards dominate)
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
terminal states P and Q and a terminal state T.
Assume the discount factor γ = 0.7.
Episode 1: P 4 Q 3 P 2 T
Q3   Episode 2: Q 5 P 1 Q 2 T
CO-2,4;   Estimate the state value using First Visit Monte Carlo.
[10]
SO-1   Estimate the state value using Every Visit Monte Carlo.
BL-4,5   Construct Markov model that best explains the observations.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (4M+4M+2M)
********** 5 **********
--- page 6 ---
Returns
Episode 1:
P₁ = 4 + 0.7(3) + 0.7²(2)
= 4 + 2.1 + 0.98 = 7.08
Q = 3 + 0.7(2) = 4.4
P₂ = 2
Episode 2:
Q₁ = 5 + 0.7(1) + 0.7²(2)
= 5 + 0.7 + 0.98 = 6.68
P = 1 + 0.7(2) = 2.4
Q₂ = 2
First Visit Monte Carlo
P = (7.08 + 2.4) / 2 = 4.74
Q = (4.4 + 6.68) / 2 = 5.54
Every Visit Monte Carlo
P = (7.08 + 2 + 2.4) / 3 = 3.83
Q = (4.4 + 6.68 + 2) / 3 = 4.36
iii. Construct Markov Model (with Probabilities)
Transition Counts
From P:
P → Q = 2
P → T = 1
Total = 3
From Q:
Q → P = 2
Q → T = 1
Total = 3
Transition Probabilities
P(P → Q) = 2/3 = 0.67
P(P → T) = 1/3 = 0.33
P(Q → P) = 2/3 = 0.67
P(Q → T) = 1/3 = 0.33
Final Markov Model
P → Q, P → T
Q → P, Q → T
********** 6 **********
--- page 7 ---
b   Explain how iterative updates are used in Dynamic Programming methods
(Value Iteration/Policy Iteration) for solving MDPs. Also mention any two
challenges or limitations of these methods.
Answer: (3M+2M)
Dynamic Programming methods such as Value Iteration and Policy
Iteration use iterative updates to compute optimal solutions for Markov
Decision Processes (MDPs).
In Value Iteration, the value of each state is repeatedly updated using the
Bellman optimality equation. At every iteration, the algorithm selects the
action that maximizes the expected return and updates the state value
accordingly. This process continues until the change in values becomes
CO-2,4   very small (convergence).
SO-1
[05]
BL-2   In Policy Iteration, iteration occurs in two steps:
•   Policy Evaluation: Iteratively compute the value function for the
current policy.
•   Policy Improvement: Update the policy by choosing better
actions.
These steps repeat until the policy becomes stable.
Challenges / Limitations:
•   Requires complete knowledge of transition probabilities and
rewards.
• Computationally expensive for large state spaces (curse of
dimensionality).
c   Define on-policy and off-policy learning in the context of Monte Carlo
methods. Give one real-world example of each. Explain the role of the
behavior policy and the target policy in off-policy Monte Carlo learning.
Answer:
On-policy Learning (Monte Carlo): (1.5M)
On-policy learning refers to learning the value of a policy using episodes
CO-2,4   generated by the same policy. In Monte Carlo methods, the agent follows a
SO-1   single policy to generate episodes and updates the value function based on   [05]
BL-2,3   the returns observed from those episodes. The behavior policy and target
policy are the same.
Example:
A robot learning to navigate a maze by following its current policy (e.g., ε-
greedy) and improving it based on the rewards received while following
that same policy.
********** 7 **********
--- page 8 ---
Off-policy Learning (Monte Carlo): (1.5M)
Off-policy learning refers to learning the value of a target policy using
episodes generated from a different policy called the behavior policy. This
allows learning from exploratory or previously collected data.
Example:
A self-driving car learning the optimal driving strategy (target policy)
using data collected from human drivers (behavior policy).
Role of Behaviour Policy and Target Policy in Off-policy Monte Carlo:
(2M)
• Behavior Policy (b): It is the policy used to generate episodes. It is
usually more exploratory to ensure sufficient coverage of state-
action pairs.
•   Target Policy (π): It is the policy whose value function we want to
learn or evaluate. It is typically more optimal or greedy.
Since the data is generated using the behavior policy but evaluated for the
target policy, there is a mismatch. To correct this, importance sampling is
used, which reweights the returns based on the likelihood of actions under
both policies. This ensures that the estimated values accurately reflect the
target policy.
a   Consider a Multi-Armed Bandit problem with the following parameters:
Time step t = 5
Number of bandits (machines) = 4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
The probability of winning for each machine is:
Q4   Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
CO-2
SO-1   Assume that the random number generated for selection of one machine in   [10]
BL-3,4   the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
Answer: (4M + 4M + 2M)
********** 8 **********
--- page 9 ---
b   A student switches between Study Mode (S1) and Relax Mode (S2).
Actions: Study or Relax. From Study: Study → 0.7 stay, 0.3 go to Relax,
From Relax: Study → 0.6 go to Study, 0.4 stay Relax → always stay
Rewards: +5 for Study and +1 for Relax
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
Answer (2.5M + 2.5M)
MDP Representation States: S1: Study, S2: Relax, Actions: Study, Relax
Transition Probabilities
CO-3   From S1: P(S1, +5 | S1, Study) = 0.7, P(S2, +1 | S1, Study) = 0.3, P(S2, +1
SO-1   | S1, Relax) = 1.0   [05]
BL-3   From S2: P(S1, +5 | S2, Study) = 0.6, P(S2, +1 | S2, Study) = 0.4, P(S2, +1
| S2, Relax) = 1.0
Summary Table
Current State   Action Next State   𝑝(𝑠′, 𝑟|𝑠, 𝑎) Reward
S1   Study   S1   0.7   +5
S1   Study   S2   0.3   +1
S1   Relax   S2   1.0   +1
S2   Study   S1   0.6   +5
S2   Study   S2   0.4   +1
S2   Relax   S2   1.0   +1
State Diagram
S1 → S1 (Study, 0.7, +5)
S1 → S2 (Study, 0.3, +1)
********** 9 **********

[Text in pictures on this page, read by OCR]
We know that in 4 chances of

exploration, Random Reward obtained
© Machine M3 got played 3 times out of number i P.=P,

which it won twice generated for | That is P. <=0.6
= Machine M;got played one time and it reward P. Reward=1

won
Therefore, estimated values for each 1 0.33 1
machines are , 2 0.25 1
5 Q.(Mx) = 1,Q.(M2) = 0,Q.(M3) = 5 =

0.67,0.(Ms) = 0 3 0.55 1
From the Q, estimates , machine Myis 4 0.45 1
exploited for the next 6 steps

sin a 5 0.6 1

Probability of winning for
My is Py (M;) = 0.6 6 0.8 (0)

Random number generated to estimate
the rewards for remaining six iterations
are [0.33, 0.25, 0.55,0.45, 0.6, 0.8]
--- page 10 ---
S2 → S1 (Study, 0.6, +5)
S2 → S2 (Study, 0.4, +1)
Self-loops:
S2 → S2 (Relax, 1.0, +1)
c   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
Sequence of rewards: R₁ = 3, R₂ = 6, R₃ = -4, R₄ = 2, R₅ = 8
i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.7
ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.4
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (2M + 2M + 1M)
Returns for γ = 0.7
t   Calculation   Gₜ
5 –   0
4 R₅   8
3 R₄ + 0.7·R₅   2 + 0.7·8 = 7.6
2 R₃ + 0.7·R₄ + 0.49·R₅   -4 + 0.7·2 + 0.49·8 = 1.32
CO-3
1 R₂ + 0.7·R₃ + 0.49·R₄ +   6 + 0.7·(-4) + 0.49·2 + 0.343·8 =
SO-1   [05]
0.343·R₅   6.924
BL-3,4
0 R₁ + 0.7·R₂ + 0.49·R₃ +   3 + 0.7·6 + 0.49·(-4) + 0.343·2 +
0.343·R₄ + 0.2401·R₅   0.2401·8 = 7.8448
Returns for γ = 0.4
t   Calculation   Gₜ
5 –   0
4 R₅   8
3 R₄ + 0.4·R₅   2 + 0.4·8 = 5.2
2 R₃ + 0.4·R₄ + 0.16·R₅   -4 + 0.4·2 + 0.16·8 = -1.92
1 R₂ + 0.4·R₃ + 0.16·R₄ +   6 + 0.4·(-4) + 0.16·2 + 0.064·8 =
0.064·R₅   5.232
0 R₁ + 0.4·R₂ + 0.16·R₃ +   3 + 0.4·6 + 0.16·(-4) + 0.064·2 +
0.064·R₄ + 0.0256·R₅   0.0256·8 = 5.0928
Comparison Table
Return γ = 0.7 γ = 0.4
G5   0   0
G4   8   8
********** 10 **********
--- page 11 ---
G3   7.6   5.2
G2   1.32   -1.92
G1   6.924   5.232
G0   7.8448 5.0928
Observation: Higher γ reduces the effect of negative rewards over time.
a   In the given example, the robot must move from the Start state 𝑟 to the
Target state 𝑎 with a reward structure of +80 for reaching the target and -2
for each step taken. Assume the initial Q-value to be zero and discount factor
= 0.8. Apply the Monte-Carlo Exploring Starts Algorithm with T=6 and
initial random state as (𝑔, 𝐿) update the policy for given episode E1 and E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.8, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Episodes:
E1: (𝑔, 𝐿) →(𝑓, 𝑅) →(𝑔, 𝑅) →(ℎ, 𝑈) →(𝑐, 𝐿) →(𝑏, 𝐿) →(𝑎, 𝑠𝑡𝑜𝑝)
E2: (𝑖, 𝐷) →(𝑚, 𝑈) →(𝑖, 𝑈) →(𝑒, 𝐿) →(𝑑, 𝑅) →(𝑐, 𝐿) →(𝑏, 𝑅)
Target
Q5   a   b   c   d   e
CO-2,4
SO-1   [10]
BL-3, 4   f   g   h   i
j   k   m
n   o   p   q   r
Answer: (5x2M)
•   Target reward = +80
•   Step penalty = −2
• Discount factor γ=0.8
•   Initial Q(s,a)=0
• Episode length T=6
Episode 1
Return Calculation (Episode 1)
********** 11 **********
--- page 12 ---
Using:
Gt=Rt+1+γGt+1
t   (State, Action)   Return Gt
7   (a, stop)   80
6 (b, L)   −2 + 0.8(80) = 62
5   (c, L)   −2 + 0.8(62) = 47.6
4 (h, U)   −2 + 0.8(47.6) = 36.08
3 (g, R)   −2 + 0.8(36.08) = 26.864
2   (f, R)   −2 + 0.8(26.864) = 19.4912
1 (g, L)   −2 + 0.8(19.4912) = 13.5930
Policy Update (Episode 1)
State Action   Q(s,a)
g   L   13.593
f   R   19.491
g   R   26.864
h   U   36.08
c   L   47.6
b   L   62
a   stop   80
For state g, choose best action:
•   Best = R (26.864)
Episode 2:
Return Calculation (Episode 2)
(No terminal reached → all rewards = −2)
t   (State, Action)   Return Gt
7 (b, R)   −2
6   (c, L)   −2 + 0.8(−2) = −3.6
5 (d, R)   −2 + 0.8(−3.6) = −4.88
4   (e, L)   −2 + 0.8(−4.88) = −5.904
3   (i, U)   −2 + 0.8(−5.904) = −6.7232
2 (m, U)   −2 + 0.8(−6.7232) = −7.3786
1   (i, D)   −2 + 0.8(−7.3786) = −7.9029
Policy Update (Episode 2)
State Action   Q(s,a)
i   D   −7.903
********** 12 **********
--- page 13 ---
m   U   −7.379
i   U   −6.723
e   L   −5.904
d   R   −4.88
c   L   avg(47.6, −3.6) = 22.0
b   R   −2
Final Policy
State Best Action Q value
g   R   26.864
f   R   19.491
h   U   36.08
c   L   22.0
b   L   62
a   stop   80
d   R   −4.88
e   L   −5.904
i   U   −6.723
m   U   −7.379
• MC-ES uses full return Gt (no bootstrapping)
• Episode reaching goal → high positive returns
• Non-terminal episode → negative returns
•   Policy updated using maximum Q(s,a)
• Repeated state-action pairs use average returns
b   With reference to TD Learning and SARSA, answer the following:
(i) Explain TD (0) and TD (1) approaches in RL.
(ii) Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
Take α = 0.2 and γ = 0.9.
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
CO-2,4   steps.
SO-1   Hint: V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
[10]
BL-2,3   SARSA Update Rule:
Q (Sₜ, Aₜ) ← Q (Sₜ, Aₜ) + α [ Rₜ₊₁ + γ Q (Sₜ₊₁, Aₜ₊₁) – Q (Sₜ, Aₜ)]
Answer: (4M + 6M)
i. TD (0) and TD (1) in Reinforcement Learning
Temporal Difference (TD) learning is a model-free, online RL method that
learns directly from experience by combining ideas from both Monte Carlo
(MC) and Dynamic Programming (DP). It updates value estimates at every
step using bootstrapping — using a learned estimate to update another
estimate.
********** 13 **********
--- page 14 ---
TD (0) — One-Step TD:
TD (0) updates the value of the current state using only the immediate next
reward and the estimated value of the next state.
Update Rule:
V(Sₜ) ← V(Sₜ) + α [ Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)]
TD Target: Rₜ₊₁ + γ V(Sₜ₊₁)
TD Error (δₜ): Rₜ₊₁ + γ V(Sₜ₊₁) − V(Sₜ)
Updates happen at every step (online)
Low variance but slight bias due to bootstrapping
TD (1) — Equivalent to Monte Carlo:
TD (1) is the other extreme where the update is based on the complete
return Gₜ — the sum of all rewards until the end of the episode.
Update Rule:
V(Sₜ) ← V(Sₜ) + α [ Gₜ − V(Sₜ)]
Uses the full actual return with no bootstrapping
Updates only at the end of each episode
Unbiased but high variance
(ii)
Consider the following Q [S, A] table with states {S1, S2} and actions
{A1, A2}:
Q (S1, A1) = 5.0; Q (S1, A2) = 3.0
Q (S2, A1) = 4.0; Q (S2, A2) = 7.0
Take α = 0.2 and γ = 0.9. (6 marks)
Apply the SARSA update for experience ⟨S1, A1, 6, S2, A2⟩:
Identify which Q value is updated and compute its new value. Show all
steps.
Answer:
Q-Table:
State   A1   A2
S1   5.0   3.0
S2   4.0   7.0
α = 0.2, γ = 0.9
Experience tuple: ⟨S1, A1, 6, S2, A2⟩
Step 1 — Identify the Experience Tuple
The SARSA experience tuple ⟨S, A, R, S', A'⟩ contains five elements:
Symbol   Value   Meaning
S   S1   Current state
A   A1   Action taken in S1
********** 14 **********
--- page 15 ---
R   6   Reward received
S'   S2   Next state transitioned to
A'   A2   Next action selected in S2
Step 2 — Identify Which Q-Value is Updated
In SARSA, the Q-value that gets updated is always Q (S, A) — the Q-
value of the current state-action pair that was just executed.
Q (S1, A1) is the value to be updated
Current value: Q (S1, A1) = 5.0
Step 3 — Write the SARSA Update Rule
Q (S, A) ← Q (S, A) + α × [R + γ × Q (S', A') – Q (S, A)]
Where:
R + γ × Q (S', A') is the TD Target — the estimated true value based on the
actual next action taken
R + γ × Q (S', A') – Q (S, A) is the TD Error (δ) — how wrong the current
estimate was
Step 4 — Substitute All Known Values
Q (S1, A1) ← Q (S1, A1) + α × [R + γ × Q (S2, A2) – Q (S1, A1)]
Substituting:
Q (S1, A1) = 5.0, α = 0.2, R = 6, γ = 0.9
Q (S2, A2) = 7.0
Q (S1, A1) ← 5.0 + 0.2 × [6 + 0.9 × 7.0 − 5.0]
Step 5 — Compute the TD Target
TD Target = R + γ × Q (S2, A2)
TD Target = 6 + 0.9 × 7.0
TD Target = 6 + 6.3
TD Target = 12.3
Step 6 — Compute the TD Error
TD Error (δ) = TD Target – Q (S1, A1)
TD Error (δ) = 12.3 − 5.0
TD Error (δ) = 7.3
********** 15 **********
--- page 16 ---
Step 7 — Compute the Update
Correction = α × TD Error
Correction = 0.2 × 7.3
Correction = 1.46
Step 8 — Compute New Q (S1, A1)
Q (S1, A1) ← 5.0 + 1.46
Q (S1, A1) = 6.46
Updated Q-Table:
State A1   A2
S1   6.46 (updated)   3.0
S2   4.0   7.0
a   Consider an n-armed bandit problem where the action values are estimated
using incremental methods. Apply the incremental update rule to compute
action-value estimates for a given sequence of rewards. Analyze how the
choice of step-size parameter affects convergence and stability of
estimates. Evaluate the effectiveness of incremental implementation
compared to sample-average methods in practical scenarios
Answer: (4M + 3M +3M)
Application of Incremental Update Rule
In an n-armed bandit problem, the action-value estimate can be updated
incrementally without storing all past rewards.
The incremental update rule is:
Q(n+1) = Q(n) + α [R(n) − Q(n)]
Q6
Where:
CO-2
Q(n) = current estimated value
SO-1   [10]
R(n) = reward obtained at step n
BL-3,4,5
α = step-size parameter
For sample-average method, α = 1/n.
Example:
Let rewards for an action be: 10, 8, 6
Step 1:
Q1 = 10
Step 2:
Q2 = 10 + (1/2)(8 − 10) = 10 − 1 = 9
Step 3:
Q3 = 9 + (1/3)(6 − 9) = 9 − 1 = 8
Thus, the action-value is updated step by step using only the previous
estimate and new reward.
Effect of Step-Size Parameter
The step-size parameter α controls how much new information affects the
estimate.
********** 16 **********
--- page 17 ---
If α = 1/n (decreasing step size):
Gives equal weight to all past rewards
Converges slowly but is stable
Suitable for stationary environments
If α is constant (e.g., 0.1):
Gives more weight to recent rewards
Adapts quickly to changes
May cause fluctuations (less stable)
Thus:
Small α → slow learning but stable
Large α → fast learning but less stable
Evaluation of Incremental Implementation (Evaluate)
Advantages over sample-average method:
Does not require storing all past rewards
Computationally efficient
Suitable for online and real-time learning
Works well in non-stationary environments when α is constant
Limitations:
Choice of α is critical
Improper α may lead to slow convergence or instability
Incremental implementation is more practical and efficient than sample-
average methods, especially in dynamic environments, but requires careful
selection of step size.
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
CO-2,4   Intended direction = 0.6
SO-1   Opposite direction = 0.4   [10]
BL-2, 4   Assume:
Initial policy: Move East
Initial values = 0
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   Sta Mineral   Fuel   Ho   Landslide   Storm
rt   Site   Station   me   Zone   Zone
********** 17 **********
--- page 18 ---
Reward   0   +18   +9   +6   −130   −95
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
Answer: (2M+6M+2M)
Iteration 1: Policy Evaluation
V(S1)=0,  V(S2)=18,  V(S3)=9,  V(S4)=6,  V(S5)=−130,  V(S6)=−95
Policy Iteration
S1
East:
V(S1)=0.6(18)+0.4(9)=10.8+3.6=14.4V
West:
V(S1)=0.4(18)+0.6(9)=7.2+5.4=12.6
Best: East
S2
East:
V(S2)=0.6(−130)+0.4(6)=−78+2.4=−75.6
West:
V(S2)=0.4(−130)+0.6(6)=−52+3.6=−48.4
Best: West
S3
East:
V(S3)=0.6(6)+0.4(−95)=3.6−38=−34.4
West:
V(S3)=0.4(6)+0.6(−95)=2.4−57=−54.6
Best: East
Improved Policy
{E,  W,  E}
********** 18 **********
--- page 19 ---
a   Explain Policy Gradient Methods in Reinforcement Learning, discuss
policy approximation, and describe their advantages.
Answer:
Policy Gradient Methods: (3M)
Policy Gradient methods are a class of Reinforcement Learning techniques
that directly optimize the policy (π) instead of estimating value functions.
The policy is parameterized using θ, and the objective is to maximize the
expected cumulative reward.
The policy is represented as:
π(a|s, θ)
The parameters θ are updated using gradient ascent:
θ ← θ + α ∇θ J(θ)
Using the log-derivative trick, the gradient can be written as:
∇θ J(θ) = E[∇θ log π(a|s, θ) · R]
These methods learn by interacting with the environment and adjusting the
policy to increase the probability of actions that yield higher rewards.
Q7
CO-5
Policy Approximation: (3M)
SO-1   [10]
Policy Approximation refers to representing the policy using a
BL-2,3
parameterized function such as a neural network instead of a tabular form.
•   It maps states directly to action probabilities.
• Helps handle large or continuous state and action spaces.
• Enables generalization across similar states.
Advantages of Policy Gradient Methods: (4M)
•   Direct Optimization of Policy:
No need to derive policy from value functions; the policy is learned
directly.
•   Suitable for Continuous Action Spaces:
Works well in problems where actions are continuous (e.g.,
robotics).
•   Better Convergence in Some Cases:
Can converge to optimal stochastic policies.
• Handles High-Dimensional Problems:
Works effectively with function approximation like neural
networks.
•   Flexibility:
Can represent complex policies and adapt to dynamic
environments.
********** 19 **********
--- page 20 ---
Policy Gradient methods, combined with policy approximation, provide a
powerful and flexible approach to solving complex Reinforcement
Learning problems, especially in large-scale and continuous environments.
b   i.   Describe the concept of eligibility traces in TD(λ).
ii.   Consider an environment with 3 states: S1, S2, S3. The agent
moves sequentially to the next state:
• S1 → S2 gives reward 4
• S2 → S3 gives reward 5
• S3 → Terminal gives reward 3
Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3, V(terminal) =0
Using Temporal Difference TD (0), compute the updated values:
V(S1), V(S2), and V(S3).
Answer:
Describe the concept of eligibility traces in TD(λ). - 4M
Eligibility traces are a mechanism in Reinforcement Learning that allow an
agent to assign credit not only to the most recent state, but also to previous
states visited in the episode. In TD (0), only the current state is updated using
the immediate TD error. In TD(λ), eligibility traces keep track of how
recently and how frequently each state has been visited, enabling multiple
past states to be updated simultaneously.
Formula for trace decay
CO-2,4   𝐸(𝑠) = 𝛾𝜆𝐸(𝑠)
SO-1   Where:
BL-3,4   λ (0 ≤ λ ≤ 1) controls how far back credit is assigned   [10]
λ = 0 → behaves like TD (0)
λ = 1 → similar to Monte Carlo learning
Consider an environment with 3 states: S1, S2, S3. The agent moves
sequentially to the next state:
• S1 → S2 gives reward 4
• S2 → S3 gives reward 5
• S3 → Terminal gives reward 3
Assume: Discount factor γ = 0.9, Learning rate α = 0.2 and
Initial state values: V(S1) = 2, V(S2) = 1, V(S3) = 3
Using Temporal Difference TD (0), compute the updated values: V(S1),
V(S2), and V(S3).
𝑉(𝑠) ←𝑉(𝑠) + 𝛼[𝑟+ 𝛾𝑉(𝑠′) −𝑉(𝑠)]
Transition   Mathematical calculation   V(S V(S V(S
1)   2)   3)
Initial   2   1   3
value
S1 → S2   𝑉(𝑆1) ←𝑉(𝑆1) + 0.2[4   2.5   1   3
gives   + 0.9 ∗𝑉(𝑆2) 8
reward   --   −𝑉(𝑆1)]
2M   𝑉(𝑆1) ←2 + 0.2[4 + 0.9 ∗1
−2)]
********** 20 **********
--- page 21 ---
S2 — S3 V(S2)—1+0.2[5+0.9*3]2.5 | 2.3 |3
gives -1)] 8 4
reward 5 =2.34

--2M

S3 > V(S3) —3+0.2[3+0.9*0]2.5 | 2.3 | 3
Terminal — 3)] 8 4

gives =3

reward 3

--2M

V(S1) — V(S1) + a[r + yV(s') — V(s)]

FI ICR D7 FAC HOH
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper c0ecbd09e388

- Departments: AI and Machine Learning, Artificial Intelligence
- Programmes: BTech AI 7012, BTech AIML 7053, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/Reinforcement Learning/ANS_Reinforcement Learning(702DB0E014)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (26 pages), mean OCR confidence 69.1
- 15 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program/s: B.Tech/MBA Tech ; ce Year: IV Semester: VII
Stream/s ; DS/AI/AIML

Subject: Reinforcement Learning Time: 3 hrs(_____to )
Date: /_ 12025 : No. of Pages: 26

Marks: 100. .

Synoptic - Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. :

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 __ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: : : . [20]

a With reference to Reinforcement Learning, discuss exploration and
exploitation trade-off with suitable example.

Concept of exploration with example (2.5M)
Concept of exploitation with example (2.5M)

a Challenges in RL
CO-1;
SO-1 : O Trade-off between Exploration and Exploitation
BL-2 f a To obtain a lot of reward, a RL agent must prefer actions
: that it has tried in the past and found to be effective in
producing reward- Exploit
0 But to discover such actions, it has.to try actions that it has
not selected before- Explore
a Note: Neither exploration nor exploitation can be pursue
exclusively without failing at the task
--- page 2 ---
O Restaurant
a Exploitation: Go to your favorite restaurant
g Exploration: Try a new restaurant

0 Oil Drilling ,
O Exploitation: Drill at the best_known location
Exploration: Drill at a new location

a Game Playing ;
oO Exploitation: Play the move you believe is best
O Exploration: Play an experimental move

b Define Markov Decision Process (MDP) with reference to rewards,
transition model, discount factor, horizon, goal.

(1M for each concept)

Oo A sequential decision problem for a fully observable, stochastic environment
with a Markovian transition model and additive rewards is called a Markov
decision process, or MDP ©

a If consists of
Oa set of states (with an initial state )
O a set ACTIONS(s) of actions in each state
O a transition model
a reward function

CO-3 ;

SO-1 ; Modelling MDP _

BL-2

oO “We have states and actions in n each state
oO Reward R, = R(S;, Ar)

O Transition model P(S;|5p_4,At—1)

a. Discount factor y

a Horizon (episode or time steps)

a Goal is to map state to action to maximize the reward (Optimal Policy)

(Ss, A, PS, (Sey At-1), R(S:, At), Y)

4

c In the context of Reinforcement Learning, discuss the key points of
Dynamic Programming approach, highlighting its significance. Compare
Dynamic Programming with Monte Carlo approach in terms of model

CO-2.4: requirement, type of value update and convergence.
SO- 1;
BL-2 Significance (2M)

e DP provides the mathematical framework e. g., Bellman equations)
for evaluating and improving policies. It forms the basis for
understanding how agents can estimate value functions and
iteratively refine their behavior
--- page 3 ---
© When the environment model (transition probabilities and rewards)
is known, DP can compute the exact optimal value function and
policy; demonstrating how an ideal agent should behave. -

e DP illustrates how value functions can be updated using estimates
of other values (bootstrapping). This concept is directly applied in
RL algorithms where the model may be unknown but values are -
updated incrementally through experience. :

Comparison (3M)

DP MC

Model : Model based Model free

Type of update Uses bootstrapping — | Uses sampling —
updates value updates values based
estimates using other | on actual returns
estimated values (via_| observed from full
Bellman equations). episodes.

Convergence Converges quickly if | Converges with

the model is accurate. | enough samples, but
‘| variance can be high

d Explain policy gradient approach in reinforcement learning. State the
advantages of using parameterized policy instead of a tabular one. [3M +2M

Limitation of Tabular Approach in RL

Cco-5; o Tabular representation for Value function or Q values
SO-1; . ; OH It is in form of vector, matrix or array
BL-2 ;

o In many problems state space and action space are
very large : :
Hi Here sometimes learning of each and.every. Q value for
each state becomes very slow

B All possible state value or Q values may not fit the memory
--- page 4 ---
Policy Gradient Method

ps

a Goal in RL is to find the optimal policy for the agent to
get maximum rewards

o Policy Gradient Family directly optimizes the policy
instead of state action or value action

a Here, we model the policy with parameterized function

o Se actions are selected without calculating value
functions

v So, the objective function is to maximize the expected return:

a With the help of suitable examples, define the following concepts in
reinforcement learning (RL)-
Agent, Environment, State, Action, Reward, Policy, Reward, Episode,
Value function, Model.

Each concept with example (1M)

Concept Definition Example
~ |} Agent ‘ Learner/decision- . Self-driving car
Q2 . maker :
CO-1; . : ptt [10]
SO-1; | - Environment World interacting - Road, traffic,
BL-2 . | with agent weather
State (s) Current situation Car speed,
position, traffic
light
Action (a) Decision affecting Accélerate,
environment , brake, turn
Reward (r) Feedback for action | +10 for safe
: arrival, -10 for
‘| collision
--- page 5 ---
Policy (1) Strategy mapping Stop at red

states > actions light, go at
green
Episode Sequence from start | Trip from home
> terminal >work
Value function Expected future Empty road
rewards state = +50
Model Predicts next Next speed and
state/reward : position after

acceleration

b Consider the following environment with states and rewards as mentioned.
Each arrow indicates the allowed movement direction .and the immediate
reward received upon moving to the next state. Reaching the goal state /
yields a reward of +10. This is the terminal state and its value is 0. Assume
that the actions are deterministic (that means the agent always moves in the
indicated direction). ;

A |p “4G
| : J-1 -1]
| Bo] E el
o oe

C F |

(Goal)

Apply the Bellman equation V(s) = R(s,a,s') + yV(s‘),
i. Evaluate value V(s) for all the states except the terminal state
for discount factor y = 0.9. Show the steps. (4M)

ii. Evaluate value V(s) for all the states except the terminal state
: for discount factor y = 0.1. Show the steps. (4M)
ili. Comprehend your observations based on evaluation done for

both the discount factors. (2M)

Note: Work backwards from terminal state to calculate value can complete
the following table.
--- page 6 ---
State Ss Values V(s) | Values V(s)

y= 09 y=01

I V() =0 VU) =0

H 10 10

G 8 0

F 6.2 -1

E 4.58 -1.1

D 2.12 -2.11

C ~ -0.09 -2.21

Bess -2.08 -2.22
2 A 2 BY 1.22

&> 4 Vive RUS a) 8) + VES) :

Br e0y gk V2

V(t) = 0 VD =
V(H)= 10+ 04 Co] = v0 ves = to I = M9
VCO) = -\ 4 gq (\0) = oe yore ci ro Ci] = O
Vipd= -1 4 9 (wes) = ee Nio d= -1 +0108] =-)

= 1 404 (ieee) = he] VEE = VE aT)

VCO el vel era ev Er ceo

=. ap? E

Vp) = -2 + -4/ é WN - ess VCs} -
NOS) = sy

2 “> 4 04G221) =5.9)1:
“\ 4 0:4 ( abet) = ag 2° 22-

a — VCnJ= “V4 04 [-2r2Je = hoo

Consider a finite, episodic Markov Decision Process (MDP) with two-non-
terminal states A and B and a terminal state T. Assume that the following ~
two episodes are observed when Monte-Carlo evaluation is being carried
out. The numbers within the episodes denote the rewards that are collected

Q3 : during the transition. For example, Episode | the agent starts with state A,

eo) -2,45 then goes to state A again, then to B, and B again and then terminates. On [10]
So-1 ; the way, the agents collects the reward of 2, 6, 1 and 0 respectively. —

BL-4,5 Assume the discount factor to be y = 0.7.

Episode 1:A2A6B1B0T
Episode 2:B3 B6A 1 BOT

i. Estimate the state value for both the states A and B using First
Visit Monte Carlo algorithm.(4M)

6
--- page 7 ---
ii. Estimate the state value for both the states A and B using Every
Visit Monte Carlo algorithm. .4M) ‘

iii. Construct Markov model that best explains the above scenario.
QM)

Hint:
Return Gy = Resi + VReva + v7 Rtas toy? OR

\\2 o1F

wat © ( aren
aie dius
Are war a6
Gor sit A
ee 4 :
. ane y 97 xKO = 6 64
epicales ¢ =. 29 bUxGe Ox + 07°*
epicotta GS It gana = |
ee 4
VOAJ = 6643) = 3 8uUS
. 2 “
for erm 8
ee $ - \
eproder Goeiel oe ge oer 18)
Sa ec 3 eas b+ 0 : —
Eicon
Jone aeeie Gan
& 2
ae
ee fect & ate
fe Ge ee He
‘ J s Be :
iets Lak 62 o-aai~ = 64
a
wr 2! xoaxo = \

eyed fst ey

VA) = 6-604 6 2 gems =4.8

2
--- page 8 ---
Every Visit for state B
Episode1:   Episode 2:
First Visit G=1   First Visit G= 7.69   V(B) = (1+0+7.69+6.7+0)/5= 3.07
Second Visit G=0   Second Visit G= 6.7
Third Visit G=0
--- page 9 ---
Off policy methods using importance
sampling

a Importance sampling is a general technique for
estimating expected values under one distribution given
samples from another

a We apply importance sampling to off-policy learning
by weighting returns according to the relative
probability of their trajectories occurring under the
target and behavior policies, called the importance-
sampling ratio

oO Relative probability of the trajectory under the
target and behavior policies (the importance
sampling ratio) is


* pur =

Although the trajectory probabilities depend on the MDP’s transition probabilities, which are
generally unknown, they appear identically in both the numerator and denominator, and thus
‘cancel.

The importance sampling ratio ends up depending only on the two policies and the sequence,
not on the MDP.

ae i. Discuss the pseudo-code for Epsilon greedy Multi Arm Bandit
Algorithm. (4M)
ite A 3-armed bandit problem is initialized with action-value

estimates Q(a)=0 for all actions. Using the Epsilon-greedy
action selection strategy with Epsilon e=0.1, the following
sequence of actions and rewards is observed: (Aj, 2), (Az, 3),
(Az,1), (Az,3), (Az, 2). Assume N(a) = 1 for step 0 for all the
actions.

o 2 Bf Using the incremental update formula, calculate the action-
sO 5 value estimates Q(a) after each step and complete the table I 10]
BL3 4 below. (S5M- one mark for each step calculation)

iii. Identify the greedy action would be selected for step 6- 1M

Step | Action | Reward Q(A1) | Q(Az) | Q(A3) | Reason why

selected | observed the next
action was’
-| selected
0 0 0 0
1 Ay 2
2: | Ad 3
--- page 10 ---
3 A, {1

4 A, [3
5 Az [2
6

Hint: Incremental update is given by
Onia(@) = On(@) 475 ! [Rn = Qn(@)]

A simple bandit algorithm

Initialize, for a = 1 to k:
Qa) +0
N(a) +0
Loop forever:
Ae £ Emax, Q(a) with probability 1—é (breaking ties randomly)
a random action with probability ¢
R ¢ bandit(A)
N(A) — N(A) +1 ce
Q(A) © QA) + xt [R- aay]

wy |
runk alrig~
vik fel oa

“TV Rnndlars Gh um A 3
|v edockh for 40 >
Gr athye
ne B, fs fal 7

Aperudsjachin Ae |

10.
--- page 11 ---
dts) Fo Cee

rate 0) dni CA = NA)
\ 2 ow 2b fe € ole '
goo ox Lf a8
dele =0, Bile ys o>
eo, Mhuw ie che

pid.) :
ae i Caecdl > tS

ey +
85 (hed = 2
Oy ( hy) = 0 ‘i 1
aces te NTS
ary)
one Nos \ eee al 3
-B2 (pr) = : 2
Woe Oe
b A bird lives in a park that has two favorite spots — one near the fountain

and another on a tree branch. At each time step, the bird can choose to either
fly or rest. If the bird is near the fountain and decides to fly, there is a 70%
chance that it will reach the tree branch and a 30% chance that it will remain
near the fountain. If the bird is on the tree branch and decides to fly, there is
a 40% chance that it will go to the fountain and a 60% chance that it will
stay on the tree branch. If the bird decides to rest, it always remains in the

o : same spot with 100% probability. The bird receives a reward of +5 for every [5]
B L3 action that results in staying on the tree branch and a reward of +1 for every

| action that results in staying near the fountain. The objective is to represent
this situation as a Markov Decision Process (MDP).

i. Develop a state diagram showing transitions and rewards for all
state-action pairs for the above mentioned scenario. (2.5M)
ii. Write p(s’, r|s,a) for all the possible state action

combinations. (2.5M)

11
--- page 12 ---
0:3)! 0

tsteis

\O01, et +5

e(su% \> a)

5 0

0:3
4 \

1 ree

1 0's

No5
ic Diode |
c For a Markov Decision Process with the number of time steps T = 5,

sequence of rewards observed are as follows-
Ry =—1,R, =1,R3 =5,R,=7,Rs5 = 10

i. Solve for the returns Gp to G; with discount factor y = = 0.8
Co-3 (2M)
SO-1 | oii Solve for the returns Gp to Gs with discount factor y = 0.1 [5]
BL-3,4 (2M)
Git. Compare the returns for both the discount factors and

comprehend your observations. (1M)
| Hint: Return G; = Rega + YRea2 + V7 Rag tee” oR

- 12
--- page 13 ---
——

Que 426 a, . q-t-1
= ee bos ARE 40s hoes VN er,
Riz-\ ) Pre Vy Bae Eu Me NO
2 0-8 : eae

Shee Rear a DG :

6s2 O
Guz wr o-(od= 10
_ q+o1) = 8

gee Rus ples 2°

&u= 104 0°80) = .

€
a4 0:90) = Ae ‘ ee

d= ie or 6x olla -
Gee 5% 0-8 4) 98s) © 5a-ee
ec ee |
ere tr 0-8l yee: is
‘ ies So SED =
go's -aye.ec tt) = et ay
be
| Q5 a. | Consider the given grid with the following parameters
re e States are A to L
ae e Rewards:
BL-4,5

o +40 for target
o -1 for each state
e Actions= {West, East, North, South} as

North

shown West East
e States with X are obstacles and those

action would be avoided by the agent south
e Initial random policy for each state is

mentioned.
e Initial Q value is equal'to zero 4] [10]

Apply Exploring Start Monte Carlo Algorithm for an Episode with T=6 and
initial random state-action as (G, West)
i. Generate state-action sequence for this episode for the given policy
(2M)
ii. Discounted return given by equation G = yG + R¢41. For discount
factor y = 0.8, compute discounted return list for the given episode
(4M)
iii. | Obtain the average return list and update the Q value @M)
iv. . Update the policy in the grid (2M)

13
--- page 14 ---
=

. a) ricoh. $F 1=6

> JL

D E

J L

G H

> XY |

t J

te 4

K JL Target
= >
we er qe seer) . |

sa Nein
= tee \: 0-3 y tb a
ees stale - ether Host = , wast) |

Sowk

ee (6,5) a(n, cow)

(& , wut SAE wut
> @, cone) > WA
on de Oe 29-8 SI.

Sal meer AC \ =uor O=0
—e : ne -
C1,s0wr>
Hod &= -1 + 0-8C4o =3)
CH) cowh) gy
GOK: oF H\+ o-8thay = 23-8
6 ,Gopr>
£96 . ee -\ + 0.8 (23-5 = i@:0y
Cc Bott .
GF: Geez -\ + 0-0 Li8ouy = 2-43
Co) WAT )

14
--- page 15 ---
ES te phle (ey)
2. Comet = BH?
pe UB, oa = ON
gr (6) ae = =
ON Ct > four a3)
yd

te UD My

wadond A vole Uce : me

lace, Wat Ss 3: aa =
GCF, eri = Wey song ;
GC 6) Gl) = 248)

Qn, came) = 2)

aC Al cowh y= yo

b Consider the following environment with four states A, B, C, D.

The state transitions and corresponding rewards collected are as given
below. The current values for each state are also given below. Assume
learning rate a = 0.2.and discount factor y = 0.8. Evaluate values for all
the states using TD(0) approach for the following episode-

Episode: ADB>ADDIC

eae Environment Transition rewards Initial Values
0- [10
Bie MB Transition | Rewards | V(A) =4
a ADB 2 V(B)=2
D C BDA -2 V(C)=4
A>D 3 V(D)=1
D>C 0
i, Using Temporal Difference TD(0) approach, compute V(A),
V(B), V(C), and V(D)~—«[2M each]
ii, Explain the term temporal difference in TD(0) expression [2M]

45
--- page 16 ---
Hint: TD(0) expression
V™(S_)— V™(S_) + @(Rear + YV" Sea) — V"(St))

awh ©
VN

WCAX= YU
VOR =>,
v@? =u
YOp)= \

, . oN)
yore oo ' \ 4 9V8Csen) V0] ig
row — Wet a (een

N Am
ee
28 vunye 4 prfer orl) ee
o 5 Sey over
aio)
poe MU = et o> a 0G
—= : ray NG
si = 3.96
og (3 VI =3
hop >= 20> + 0-2 [3+
Dp = ‘
ae . -yjr row
ype ve ort pen
p70 . 5
06 a Upper Confidence Bound (UCB) equation is given by
Co-2 e log(t)
S0-1 . . A; = argmax, |Q;(a) +¢ Na) [10]
BL-3,4,5

Where, .
Q,(a) is the estimated value of action ‘a’ at time’step ‘t’.

_ 16
--- page 17 ---
N,(a) is the number of times that action ‘a’ has been selected, prior to

time ‘t’. :

‘cis a confidence value

i. State the drawback of € —greedy algorithm and explain how it
can be overcome in UCB.- (2M)

ii. Explain exploitation and exploration in the context of the
abovementioned equation. (2M)

iii. After 12 iterations of UCB algorithm, applied on 4 arm bandit
problem, we have the number of times each machine was played
N(M,) = 4, N(M,) = 4,N(M3) = 3 and N(M,) =1. Also
values for each machine after 12 iterations are Q(M,) =
0.55, Q(Mz) = 0.63,Q(M3) = 0.45,Q(M,) = 0.61. Apply
UCB algorithm to identify which machine should be played next.
Consider confidence value c = 2. (6M Here we givel.5M for
each calculation)

Note: Take natural log for all calculations

i. Drawback of Epsilon-Greedy

o ’Exploration is needed because there is always uncertainty about the accuracy of the action-
value estimates

0 Greedy actions are those that look best at present, but some of the other actions may actually,
be better

0. €-greedy action selection forces the non-greedy actions to be tried, but indiscriminately, with
no preference for those that are nearly greedy or particularly uncertain

a It would be better to select among the non-greedy actions according to their potential for
gstually.being optimal, taking into.ascount both
B_ how close their estimates are to being maximal and
Othe uncertainties in those estimates

0° One effective way of doing this is to select actions according to

Ar 4 angus [ave te wo 7

ii. Exploration and exploitation part

: log(t.
A, = argmax,|Q,(a) +c ae

Q;(a)- This term is exploitation part as this term focuses on highest value
so far from the past experience
flog(e)
N(a)
of the arm that has been selected fewer times as compared to the other
arms

- This term is the exploration part which encourages the selection

17
--- page 18 ---
7?

at Ave Arama [aie ae [ae |
; a

(Ay

Neto vinvs . 2 ae
AX 4 ; | (: cso + a ; )
G 43 42 wt )

(ows Af)
(oo)

2.20 4.23 ,3-% |

a aie anges [a0
awd be pny oe

Muy

ie 7

pathin

C0:2,4
S0-1
BL-2,4

Consider the following maze where the agent (at initial state S,) has to
reach the goal state S,. Rewards for every state are given in the state
diagram as (S,, Reward). With the following parameters given, evaluate
the value and identify the optimal policy for the next one iteration using
Policy iteration algorithm. .
e - Actions taken by agent= {L, R}. For example, if the agent takes
action ‘L’ in state S,, the agent will go to state S, with a
probability of 0.8.
e Discount factory = 0.7 -
e Probability to go in the intended direction =0.8
e Probability to go in the direction other than intended= 0.2
e Initial policy and values as given in the adjacent table
State | S, Sp |. Se Sa |, Se Ss | Sq Sh

Initial | 0 0 0 0 0 0 0 0:
Value ,

V(s)
Initial | R R R - R R - -
Policy _

[10]

18
--- page 19 ---
Hint: Policy iteration expressions

Policy evaluation:

Vii=r(s)+ vistr P(s',r|s, m(s))Vi(s’)
Policy improvement:

m(s) = argmax, by p(s, rls, a)Y(s’)

sles

19
--- page 20 ---
wnt 4 ae
_ = w

Snir

VG)

pouiuy |
urdinte

© Sunes? Ya)

|

rove
ee
; : State value|3M
Le We , aN” Policy update 2M
Policy evaluation 5M
rym 5 ae on ee ’ i=)
pou" AD .
Uchinnk ve .
Va eno + JS?
oF oF [08CO* ortor J = 0.

(shr\s MD» Vals! )

N@> =
ve Yd)
= 3
: s tery 4 Teng hr > Al=n9nr
. _ ;
vee) = 3» VHD =O gy VChy = 0
m= TqNr TEA We wig
Na =0-
Te righ

20
--- page 21 ---
POW cw ge ay
SEC

for ona

TCS) = ora oe toe x B+ 02x V4] 9 Winn

oa (02d) +024) ) > Ye

= myn [ee oe
0:48 Beas

NGS) > Vesa) uae pe

ee vo ap” (E )
forsinit Sb : ;
TE Ar ;
VG 5 14 [ pOheeet els
Taw
WP Zz: VUb> => opm gtk (LL)
Tentqgne Tbe ae
Vls). = 03 [oe >t gece =
Tengu : =e
Te ur : ae
N| (Sc \ 7? VGser =). ee Ce 5
Tenght fee ee

21
--- page 22 ---
fr Hor $e
Or SE

| 2 -\s

Ve) = oa [oat * or( tJ 4
TW = GAT ;
\l (Se) = o-aCo-e CF? + oacmuy \ a 2774.
Tale

NOS) we Y Cse> E—>) oprion pow ay

Merge Nee iw Wye (LD
For crake SE

powy KWL

a Answer the following questions-
i. “With the help of a pseudo-code of explain one step actor critic
algorithm (4M) .
ii. Explain the role of an actor and a critic and describe how they

interact during training (4M) -
iii. Compare actor-critic method with REINFORCE method (2M )
(Any two relevant points) -

Q7
CO:5 Actor Critic Method

SO-1
BL-2,3

o Actor-Critic mieihodii isa enikorcement isuraing appeseich [10]
that combines elements of both policy-based (actor) and
value-based (critic) methods to improve learning efficiency
and stability

a In this framework, the actor and critic work together in a

' coordinated way to optimize the policy

0 Components ;
g Actor

O Critic

22
--- page 23 ---
Actor Critic Method

O Actor:

O The actor represents the policy, which decides which action
to take given a state :

G It directly updates the policy parameters in the direction
that maximizes expected cumulative rewards, often using a
policy gradient method

G The actor’s goal is to maximize the rewards by making
better action selections over time

Actor Critic Method

oO Critic:

The critic estimates the value function (usually the state-
value V(s) or action-value Q(s,q)function), which represents
the expected return from a given state or state-action pair.

G It provides feedback (called the temporal difference (TD)
error) to the actor about how good the actions taken were,
relative to the expected value.

The TD error helps the actor understand whether it should
adjust its policy in a positive or negative direction.

Actor Critic Method

O Policy Update:
The actor updates its policy using the feedback from
the critic, making incremental adjustments to maximize
future rewards. :

O This update helps the agent learn both efficient action
selection (from the policy update) and the ability to
estimate future rewards accurately (from the value
update).

23
--- page 24 ---
One-step Actor—Critic (episodic), for estimating 79 ~ 7,

Input: a differentiable policy parameterization 7(a|s, 0)
Input: a differentiable Statevaluc function parameterization o(s, w)
Parameters: step sizes.a? > 0, a” > 0
Initialize policy parameter 6 € R* and state-value weights w € R? (e.g., to 0)
Loop forever ‘(for each episode):

Initialize S (first state of episode)

Tel

Loop while S is not terminal (for each time step):
A~x(-|S, 0)
Take action A, observe 5’, R

6 R+70(S',w) — o(S,w) (if S’ is terminal, then 6(S’,w) = 0)
we wt+avrdVil(S,w) z
6 -—64+0°IS5V Ina(AlS, 4)

leo
Ses’
REINFORCE (Monte Carlo ie
Aspect Policy Gradient) Actor—Critic
: eee Hybrid: Policy-based
Type Pure Policy Gradient (no (actor) + Value-based
value function) aes ;
(critic)
Learning — ||Uses total return (G,) as Uses TD error Gacvantege)
Signal feedback las feedback
Update __. Updates after an entire Updates after each step
Frequency |jepisode (Monte Carlo) (online / semi-online)
i sien unica Lower variance, because
Vari High variance, since returns ||"... i ;
ariance critic provides smoother

can fluctuate heavily ee ee

: Unbiased, since full returns Biased, due to 8 isis
Bias bootstrapping from critic’s

are used value estimate
Convergen S1éwer Faster (more stable
ice Speed gradients)
Data Low (each episode used Higher (TD learning reuses
Efficiency |lonce) partial information)

Train a critic to estimate
value function (V(s)) or
(Q(s,a)) and use it to guide
policy updates
A2C-(Advantage Actor—
Critic), A3C, DDPG, PPO
(actor—critic variants)

Directly optimize policy
Key Idea __|lparameters 6 to maximize
expected reward

Example |[REINFORCE, Monte Carlo
[Algorithms ||Policy Gradient

24
--- page 25 ---
oe

CO-2,4

‘| so-1

BL-3,4

Consider an environment with one state X and two actions associated with
this state {b, c}. Let state T be the terminal state. The temporal difference
(TD) algorithm generates the following episode using policy 2 when
interacting with its environment-

Time Reward State Action
0 eee b-
i 12 x c

2 8 Tee eS
3 2 T

e The policy z is given by 2(b|X) = 0.9, m(c|X) =0.1

e The current values of q are: Q(X,b) = land Q(X,c) = 2.
e The discount factor y = 0.6

e The step size or learning rate a = 0.1

i. Solve for the values of Q(X, b)and Q(X, c) using one step
: SARSA. .

ii. Differentiate between Q-learning and SARSA algorithms with
reference to their Se learning approach, policy type,
update rule. . 4M]

Recall the following expression for SARSA

QS Ar) — QS, Ar) + al Rear + VQ Serr Acer) — Q(Si, At) ].

r c\x)=-0')
queen, TO

‘ Q cS
Bexpes fe GLSOT®
=o0'\
A= ob ie e

[10]

25
--- page 26 ---
Zpeth aku

- (%
O(se) 6) = ac — 6 (sey 0o)

, = |
Abd =

. = 2-22.
(2 + Oba > — m)

es wen 2 a Cem 0 EALED HE
TE Bea = Sb? = 2933

5 24 ON (e+ pr6x ER yrs

26
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 8fd3ee33f948

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_DS_7052/Reinforcement Learning/ANS_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
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
1. This question paper contains 21 pages.
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
a   Discuss in detail the application of Reinforcement Learning for HealthCare
by cosidering all the components of RL.
Answer:
Reinforcement Learning (RL) is increasingly used in healthcare to support
decision-making processes such as treatment planning, personalized
medicine, and resource allocation, with the goal of improving patient
outcomes over time. (01)
Components of RL in Healthcare: (03)
CO-1;   1. Agent:
SO-1;   The agent is the decision-making system (e.g., an AI model) that   [05]
BL-2   recommends actions such as selecting treatments, adjusting drug
dosages, or scheduling interventions.
2. Environment:
The environment represents the patient and the healthcare system,
including medical conditions, physiological responses, hospital
settings, and external factors affecting patient health.
3. State:
The state includes the current health condition of the patient, such
as vital signs, medical history, lab results, symptoms, and ongoing
treatments.
4. Actions:
Actions refer to possible medical decisions, such as prescribing
********** 1 **********
--- page 2 ---
medication, choosing a treatment plan, adjusting dosage, or
deciding on further diagnostic tests.
5. Reward:
The reward is based on patient outcomes. Positive rewards are
given for improvements in health, recovery, or stabilization, while
negative rewards may correspond to side effects, complications, or
deterioration.
6. Policy:
The policy defines how the agent selects actions based on the
patient’s current state, aiming to maximize long-term health
benefits and minimize risks.
Working: (01)
The RL agent observes the patient’s state, takes an action (treatment
decision), and receives feedback in terms of patient response. Over time, it
learns an optimal treatment strategy by continuously interacting with
patient data and outcomes.
RL in healthcare enables personalized and adaptive treatment strategies,
improves clinical decision-making, and optimizes long-term patient care.
However, challenges such as data privacy, ethical concerns, and the need
for high reliability must be carefully addressed.
b   Define a Markov Chain. Draw a simple state transition diagram with at
least 3 states and label the transition probabilities.
Answer:
A Markov Chain is a stochastic (random) process that moves through a set
of states, where the probability of transitioning to the next state depends
solely on the current state, satisfying the Markov Property. It consists of:
A state space S — the set of all possible states
Transition probabilities P(s' | s) — the probability of moving from state s to
state s'
The transition probabilities from any state must sum to 1. (3M)
CO-3;
SO-1;   [05]
BL-2
(1M)
From / To   Sunny   Cloudy   Rainy
Sunny   0.6   0.3   0.1
Cloudy   0.4   0.1   0.5
Rainy   0.3   0.3   0.4
********** 2 **********
--- page 3 ---
(1M)
c   With the help of suitable illustration compare Dynamic Programming
Reinforcement Learning approach and Monte Carlo Reinforcement
Learning
Answer: (2.5M + 2.5M)
CO-2,4;
SO-1;   [05]
BL-2
DP   MC   TD
Model based   Model Free   Model Free
Need not wait for the   Waits till end of   Need not wait for the
entire episode to get   episode to estimate   entire episode
over   the value   To get over
Can work for infinite   Works only for   Can work for infinite
horizon   episodic environment   horizon
Learning need not   Learning happens   Learning happens
only be through   only through   only through
experience   experience   experience
d   Compare value function methods and policy function methods in
Reinforcement Learning, highlighting their main differences.
Answer:
In Reinforcement Learning, two main approaches are used to find optimal
behavior: value function methods and policy function methods.
Value Function Methods: (1M)
These methods focus on estimating the value of states or state-action pairs
CO-5;
SO-1;   [05]
(e.g., V(s) or Q(s, a))
BL- 2
The optimal policy is derived indirectly by selecting actions that maximize
these values.
Example: Q-Learning, Value Iteration, Approach: First learn value → then
derive policy
Policy Function Methods: (1M)
These methods directly learn a policy that maps states to actions without
********** 3 **********
--- page 4 ---
explicitly computing value functions. The policy is usually parameterized
and optimized using gradient-based methods.
Example: REINFORCE, Policy Gradient, Approach: Directly learn policy
(3M)
Aspect   Value Function   Policy Function Methods
Methods
Learning Focus Value of states/actions   Direct policy
Policy   Indirect (via values)   Direct
Derivation
Suitable For   Discrete action spaces   Continuous/large action
spaces
Stability   More stable   Can have high variance
a   How do Immediate and Delayed Reinforcement differ in Reinforcement
Learning? Provide a comparative explanation and support your answer
with relevant real-life examples.
Answer:
In Reinforcement Learning (RL), reinforcement refers to the feedback
(reward or penalty) received by an agent after taking an action. Based on
the timing of this feedback, reinforcement can be classified as Immediate
or Delayed.
Immediate Reinforcement: (3M)
Immediate reinforcement occurs when the agent receives feedback
instantly after performing an action. This helps the agent quickly
understand whether the action was correct or not.
Example:
Q2
CO-1;   In an online recommendation system, if a user clicks on a recommended   [10]
SO-1;   product immediately, the system gets instant positive feedback and
BL-2   learns to improve similar recommendations.
Delayed Reinforcement: (3M)
Delayed reinforcement occurs when feedback is received after a
sequence of actions rather than immediately. The agent must determine
which actions contributed to the final outcome.
Example:
In autonomous driving, a sequence of correct decisions (speed control,
lane changes) leads to reaching the destination safely. The reward is
associated with the final outcome, not each individual action.
Comparative Explanation: (2M)
Aspect   Immediate   Delayed Reinforcement
Reinforcement
Timing of   Given instantly after   Given after a delay or
Reward   action   sequence
********** 4 **********
--- page 5 ---
Complexity   Simple to learn   More complex to learn
Credit   Easy   Difficult (credit assignment
Assignment   problem)
Focus   Short-term results   Long-term outcomes
Real-life Importance: (2M)
Immediate reinforcement is useful in systems where quick feedback is
available and decisions are simple. Delayed reinforcement is crucial in
complex real-world problems like healthcare, finance, and robotics, where
actions have long-term consequences.
Immediate and delayed reinforcement differ mainly in the timing of
feedback and learning complexity. While immediate reinforcement enables
faster learning, delayed reinforcement is essential for developing strategies
that maximize long-term rewards in real-world applications.
b   Consider a 4×4 Grid World problem where the goal is to reach either the
top-left corner or the bottom-right corner (refer to the figure). The agent
can choose from four actions: Up, Down, Left, Right, which
deterministically cause the corresponding state transitions, except that
actions leading outside the grid leave the state unchanged. The task is
modelled as an undiscounted episodic problem (γ = 1) with a reward of −1
for all transitions, and the agent follows an equiprobable random policy
(π).
Given the partial value function for this grid, apply and analyse the
Bellman Expectation Equation to compute the missing state values in the
second and fourth rows.
𝑉𝜋(𝑠) = 𝑅(𝑠) + 𝛾∑𝑃(𝑠′|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
𝑠′
CO-3
SO-1;   [10]
BL-3,4
Answer: (5M+ 5M)
Bellman Expectation Equation Calculations
For v₁ (Second Row, Fourth Column)
v₁ = 0.25 × [(-1 - 14) + (-1 - 14) + (-1 - 18) + (-1 + v₁)]
= 0.25 × [-15 - 15 - 19 + (v₁ - 1)]
= 0.25 × [-50 + v₁]
⇒ v₁ = -12.5 + 0.25 v₁
⇒ 0.75 v₁ = -12.5
⇒ v₁ = -16.67
********** 5 **********
--- page 6 ---
For v₂ (Fourth Row, Third Column)
v₂ = 0.25 × [(-1 - 18) + (-1 - 18) + (-1 - 20) + (-1 + 0)]
= 0.25 × [-19 - 19 - 21 - 1]
= 0.25 × [-60]
⇒ v₂ = -15
Final Answers
v₁ = -16.67
v₂ = -15
a   In the given example, the robot must move from the Start state 𝑆17 to the
Target state 𝑠0 with a reward structure of +110 for reaching the target and -
2 for each step taken. Assume the initial Q-value to be zero and discount
factor = 0.6. Apply the Monte-Carlo Exploring Starts Algorithm with T=6
and initial random state as (𝑆6, 𝐿) update the policy for given episode E1 and
E2.
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
factor 𝛾= 0.6, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
E1: (𝑺𝟖, 𝑫) → (𝑆12, 𝑈) →(𝑆8, 𝑈) →(𝑆4, 𝐿) →(𝑆3, 𝑅) →(𝑆4, 𝐿) →
(𝑆3, 𝑅)
E2: (𝑺𝟔, 𝑳) →(𝑆5, 𝑅) →(𝑆6, 𝑅) →(𝑆7, 𝑈) →(𝑆2, 𝐿) →(𝑆1, 𝐿) →
(𝑠0, 𝑠𝑡𝑜𝑝)
Q3
CO-2,4;   Targe   [10]
SO-1   t S0   S1   S2   S3   S4
BL-4,5
S5   S6   S7   S8
S9   S10   S11   S12
S13   S14   S15   S16   S17
Answer: (5x2M)
Episode 1
(All rewards = −2)
t   (State, Action)   Return Gt
6 (S1, R)   −2
5 (S2, L)   −2 + 0.6(−2) = −3.2
4 (S1, R)   −2 + 0.6(−3.2) = −3.92
3 (S2, L)   −2 + 0.6(−3.92) = −4.352
********** 6 **********
--- page 7 ---
2 (S6, U)   −2 + 0.6(−4.352) = −4.6112
1 (S5, R)   −2 + 0.6(−4.6112) = −4.7667
Policy Update after Episode 1
State Action   Q(s,a)
S9   U   −4.7667
S5   R   −4.7667
S6   U   −4.6112
S2   L   avg(−4.352, −3.2) = −3.776
S1   R   avg(−3.92, −2) = −2.96
Episode 2: Return Calculation
(Target reached → final reward = +110)
t   (State, Action)   Return Gt
7 (S0, stop)   110
6 (S1, L)   −2 + 0.6(110) = 64
5 (S2, L)   −2 + 0.6(64) = 36.4
4 (S7, U)   −2 + 0.6(36.4) = 19.84
3 (S6, R)   −2 + 0.6(19.84) = 9.904
2 (S10, U)   −2 + 0.6(9.904) = 3.9424
1 (S6, D)   −2 + 0.6(3.9424) = 0.3654
Policy Update after Episode 2
State Best Action Q value
S6   R   9.904
S10 U   3.9424
S7   U   19.84
S2   L   36.4
S1   L   64
S0   stop   110
Final Policy
State Best Action Q value
S6   R   9.904
S10 U   3.942
S7   U   19.84
S2   L   36.4
S1   L   64
S0   stop   110
S5   R   −4.7667
S9   U   −4.7667
********** 7 **********
--- page 8 ---
• Monte Carlo uses full return Gt
• Negative rewards indicate non-optimal paths
•   Positive values indicate path toward goal
•   Policy improves by selecting maximum Q(s,a)
b   Explain the Value Iteration algorithm used in Dynamic Programming for
solving MDPs. Provide the pseudo-code and describe it’s working.
Answer: (1M+3M+1M)
Value Iteration Algorithm
Value Iteration is a Dynamic Programming technique used to compute the
optimal value function and optimal policy for a Markov Decision Process
(MDP). It is based on the Bellman Optimality Equation and iteratively
updates state values until convergence.
Pseudo-code for Value Iteration:
CO-2,4
SO-1   [05]
BL-2
Working Explanation
• The algorithm starts with arbitrary state values.
•   It repeatedly updates values using the Bellman optimality equation.
• At each step, it selects the best action that maximizes expected
return.
•   Iteration continues until the change in values becomes very small.
•   Finally, the optimal policy is extracted from the computed values.
c   Differentiate between on-policy and off-policy reinforcement learning methods.
Also, explain how importance sampling is used in off-policy learning with a
CO-2,4   suitable example.
SO-1
Answer:   [05]
BL-2,3
Difference between On-policy and Off-policy Methods: (2M)
On-policy methods learn the value of the same policy that is used to make
decisions. Here, the behavior policy (used to generate actions) and the target
********** 8 **********

[Text in pictures on this page, read by OCR]
Algorithm parameter: a small threshold 6 > 0 determining accuracy of estimation
Initialize V(s), for all s € §*, arbitrarily except that V(terminal) = 0

Loop:

| A«O

| Loop for each s € 8:

| v — V(s)

| V(s) + max, }>,, p(s’.
| A © max(A, |v — V(s)})
until A < @

sa) [r + 7V(s‘)]

Output a deterministic policy, 7 ~ 7,, such that
m(s) = argmax, >>, p(s’, r|s,a)[r + yV(s')}
--- page 9 ---
policy (being evaluated/improved) are identical. These methods continuously
update the policy based on actions actually taken. An example is SARSA.
Off-policy methods, in contrast, learn the value of a target policy while following
a different behavior policy. This allows the agent to learn optimal behavior even
when exploring or using previously collected data. The behavior policy may be
more exploratory, while the target policy is usually greedy or optimal. An
example is Q-learning.
Importance Sampling in Off-policy Learning: (3M)
In off-policy methods, since the data is generated using a behavior policy but
evaluated for a target policy, there is a distribution mismatch. Importance
sampling is used to correct this by reweighting the returns so that they reflect the
target policy.
For multi-step episodes, the overall ratio is the product of such ratios across all
steps.
Example:
Suppose the behavior
policy selects an action with probability 0.5, while the target policy selects the
same action with probability 1.
Thus, importance sampling increases the weight of trajectories that are more
likely under the target policy and reduces the influence of those less likely,
enabling accurate evaluation and learning in off-policy methods.
a   Consider a Multi-Armed Bandit problem with the following parameters:
Q4
Time step t = 5
CO-2
Number of bandits (machines) = 4
SO-1   [10]
BL-3,4
The probability of selecting each machine is given as:
Ps(M1) = 0.3, Ps(M2) = 0.4, Ps(M3) = 0.2, Ps(M4) = 0.1
********** 9 **********

[Text in pictures on this page, read by OCR]
The importance sampling ratio is:

_ was)
~ bas)

where:

*« nla 8) = probability of action under target policy
. bla 8) = probability of action under behavior policy
--- page 10 ---
The probability of winning for each machine is:
Pw(M1) = 0.6, Pw(M2) = 0.4, Pw(M3) = 0.7, Pw(M4) = 0.9
Assume that the random number generated for selection of one machine in
the first iteration is 0.65.
Once the machine is selected in the first iteration, the same machine will
be exploited for the remaining 2nd, 3rd, 4th and 5th iterations.
Obtain the estimate of reward generated if the following random numbers
were generated for the selected machine for all five iterations:
[0.6, 0.2, 0.3, 0.5, 0.9]
Answer: (2M + 6M + 2M)
b   For a Markov Decision Process with the number of time steps 𝑇= 5,
sequence of rewards observed are as follows:
CO-3
SO-1   Sequence of rewards: R₁ = 7, R₂ = -2, R₃ = 5, R₄ = 3, R₅ = 2   [05]
BL-3
i.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.9
ii.   Solve for the returns 𝐺0 𝑡𝑜 𝐺5 with discount factor 𝛾= 0.3
********** 10 **********

[Text in pictures on this page, read by OCR]
Construct a CDF table based on the following machine selection probability
5 P(M;) = 0.3, P|(Mz) = 0.4, Ps|(M3) = 0.2, Ps(M4) = 0.1

M1 0.3 0.3

M2 0.4 0.7
M3 0.2 0.9
M4 0.1 1.0

Random number generated for selection of one machine out of five in the first iteration is 0.65
Hence from CDF column we infer that Machine M3, is selected for all the iterations 1,2,3,4,and 5

Now based on the machines selected and the random number generated for selection of machine,
Machine Mp, is selected for all the iterations 1,2,3,4,and 5

Probability of winning in each machine is for Mois R,(M2) = 0.4
Random number generated for the reward were as follows
5 (0.6, 0.2, 0.3, 0.5, 0.9]

Random number generated for Reward obtained
reward P.

That is P. <=0.4
Rewa

2 02 1
3 03 1
4 05 0
--- page 11 ---
iii.   Compare the returns for both the discount factors and
comprehend your observations.
Hint: Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (2M + 2M + 1M)
Returns for γ = 0.9
t   Calculation   Gₜ
5 –   0
4 R₅   2
3 R₄ + 0.9·R₅   3 + 0.9·2 = 4.8
2 R₃ + 0.9·R₄ + 0.81·R₅   5 + 0.9·3 + 0.81·2 = 9.32
1 R₂ + 0.9·R₃ + 0.81·R₄ +   -2 + 0.9·5 + 0.81·3 + 0.729·2 =
0.729·R₅   6.388
0 R₁ + 0.9·R₂ + 0.81·R₃ +   7 + 0.9·(-2) + 0.81·5 + 0.729·3 +
0.729·R₄ + 0.6561·R₅   0.6561·2 = 12.7492
Returns for γ = 0.3
t   Calculation   Gₜ
5 –   0
4 R₅   2
3 R₄ + 0.3·R₅   3 + 0.3·2 = 3.6
2 R₃ + 0.3·R₄ + 0.09·R₅   5 + 0.3·3 + 0.09·2 = 6.08
1 R₂ + 0.3·R₃ + 0.09·R₄ +   -2 + 0.3·5 + 0.09·3 + 0.027·2 = -
0.027·R₅   0.176
0 R₁ + 0.3·R₂ + 0.09·R₃ +   7 + 0.3·(-2) + 0.09·5 + 0.027·3 +
0.027·R₄ + 0.0081·R₅   0.0081·2 = 6.9462
Comparison Table
Return   γ = 0.9   γ = 0.3
G5   0   0
G4   2   2
G3   4.8   3.6
G2   9.32   6.08
G1   6.388   -0.176
G0   12.7492 6.9462
Observation: Lower γ emphasizes immediate rewards, making negative
rewards more impactful.
CO-3   c   A delivery drone operates between Warehouse (S1) and Customer (S2). It
SO-1   can Deliver or Wait. From Warehouse: Deliver → 0.8 reach Customer, 0.2   [05]
BL-3,4   stay
********** 11 **********
--- page 12 ---
From Customer: Deliver → 0.3 return to Warehouse, 0.7 stay Wait →
stays in same location
Rewards: +6 for Customer and +2 for Warehouse
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
Answer: (2.5M + 2.5M)
MDP Representation
States: S1: Warehouse, S2: Customer, Actions: Deliver, Wait
Transition Probabilities
From S1: P(S2, +6 | S1, Deliver) = 0.8, P(S1, +2 | S1, Deliver) = 0.2,P(S1,
+2 | S1, Wait) = 1.0
From S2: P(S1, +2 | S2, Deliver) = 0.3, P(S2, +6 | S2, Deliver) = 0.7, P(S2,
+6 | S2, Wait) = 1.0
Summary Table
Current State   Action Next State   𝑝(𝑠′, 𝑟|𝑠, 𝑎) Reward
S1   Deliver S2   0.8   +6
S1   Deliver S1   0.2   +2
S1   Wait   S1   1.0   +2
S2   Deliver S1   0.3   +2
S2   Deliver S2   0.7   +6
S2   Wait   S2   1.0   +6
State Diagram
S1 → S2 (Deliver, 0.8, +6)
S1 → S1 (Deliver, 0.2, +2)
S2 → S1 (Deliver, 0.3, +2)
S2 → S2 (Deliver, 0.7, +6)
Self-loops:
S1 → S1 (Wait, 1.0, +2)
S2 → S2 (Wait, 1.0, +6)
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
********** 12 **********
--- page 13 ---
Answer: (4M+4M+2M)
Returns
Episode 1:
X₁ = 3 + 0.9(2) + 0.9²(4)
= 3 + 1.8 + 3.24 = 8.04
X₂ = 2 + 0.9(4) = 5.6
Y = 4
Episode 2:
Y₁ = 2 + 0.9(5) + 0.9²(1)
= 2 + 4.5 + 0.81 = 7.31
X = 5 + 0.9(1) = 5.9
Y₂ = 1
First Visit Monte Carlo
X = (8.04 + 5.9) / 2 = 6.97
Y = (4 + 7.31) / 2 = 5.655
Every Visit Monte Carlo
X = (8.04 + 5.6 + 5.9) / 3 = 6.51
Y = (4 + 7.31 + 1) / 3 = 4.10
iii. Construct Markov Model (with Probabilities)
Transition Counts
From X:
X → X = 1
X → Y = 2
Total = 3
From Y:
Y → X = 1
Y → T = 2
Total = 3
Transition Probabilities
P(X → X) = 1/3 = 0.33
P(X → Y) = 2/3 = 0.67
P(Y → X) = 1/3 = 0.33
P(Y → T) = 2/3 = 0.67
Final Markov Model
X → X, X → Y
Y → X, Y → T
********** 13 **********
--- page 14 ---
b   Consider the following environment with four states P, Q, S, R.
The state transitions and corresponding rewards collected are as given
below. The current values for each state are also given below. Assume
learning rate 𝛼= 0.3 and discount factor 𝛾= 0.7. Evaluate values for all
the states using TD (0) approach for the following episode-
Episode: P→Q→R→S→P
Environment   Transition rewards   Initial Values
P   Q   Transition Rewards V(P) =3
P→Q   4   V(Q)=5
R   S   Q→R   1   V(R)=2
R→S   -3   V(S)=4
S→P   2
i.   Using Temporal Difference TD (0) approach, compute V(P),
V(Q), V(R), and V(S)
ii.   Explain the term temporal difference in TD (0) expression
CO-2,4
SO-1   Hint: TD (0) expression   [10]
BL-2,3   𝑉𝜋(𝑆𝑡) ←𝑉𝜋(𝑆𝑡) + 𝛼(𝑅𝑡+1 + 𝛾𝑉𝜋(𝑆𝑡+1) −𝑉𝜋(𝑆𝑡))
Answer: (6M +4M)
TD (0) Formula:
V(St)←V(St)+α[R +γ V(St+1)−V(St)]
Step-by-Step Updates
Step 1: P → Q
• V(P)=3, Reward = 4, V(Q)=5
•
V(P)=3+0.3[4+0.7(5) −3] =3+0.3[4+3.5−3] =3+0.3(4.5) =3+1.35=4.35
********** 14 **********
--- page 15 ---
Step 2: Q → R
• V(Q)=5, Reward = 1, V(R)=2
V(Q)=5+0.3[1+0.7(2) −5] =5+0.3[1+1.4−5] =5+0.3(−2.6) =5−0.78=4.22
Step 3: R → S
• V(R)=2, Reward = -3, V(S)=4
V(R)=2+0.3[−3+0.7(4) −2] =2+0.3[−3+2.8−2] =2+0.3(−2.2)
=2−0.66=1.34
Step 4: S → P
• V(S)=4, Reward = 2, V(P)=4.35 (updated value)
V(S)=4+0.3[2+0.7(4.35) −4] =4+0.3[2+3.045−4] =4+0.3(1.045)
=4+0.3135=4.3135
Final Updated Values:
• V(P)=4.35
• V(Q)=4.22
• V(R)=1.34
• V(S)=4.3135
Concept Explanation: Temporal Difference Error
The temporal difference (TD) error is:
δ=R +γ V(St+1) −V(St)
Meaning:
•   It represents the difference between predicted value and improved
estimate.
•   It measures how much the current estimate is wrong based on new
experience.
• TD learning updates values incrementally without waiting for the
final outcome.
Q6   a
Describe the Upper Confidence Bound (UCB) method for action selection
CO-2
in reinforcement learning. Apply the UCB formula to explain how it   [10]
SO-1
balances exploration and exploitation.
BL-3,4,5
********** 15 **********
--- page 16 ---
Analyse its advantages over ε-greedy strategy and evaluate its
effectiveness in scenarios with limited data and high uncertainty.
Answer: (2M + 2M + 4M + 2M)
Description of UCB Method
The Upper Confidence Bound (UCB) method is an action selection
strategy used in reinforcement learning to balance exploration and
exploitation in the n-armed bandit problem.
The action is selected using the formula:
UCB(a) = Q(a) + c * √(ln t / N(a))
Where:
Q(a) = estimated value of action a
N(a) = number of times action a has been selected
t = total number of time steps
c = exploration parameter (controls degree of exploration)
The first term represents exploitation (choosing actions with high
estimated reward), while the second term represents exploration (favouring
less tried actions).
Application and Working
Initially, all actions are selected at least once.
Actions with fewer selections (small N(a)) get a larger exploration bonus.
As an action is selected more often, N(a) increases and the exploration
term decreases.
Thus:
Less explored actions → higher bonus → more likely to be selected
Well-explored actions → lower bonus → selected based on actual
performance
This ensures a systematic balance between exploration and exploitation
without randomness.
Advantages over ε-greedy
Targeted exploration: UCB explores actions based on uncertainty, not
randomly.
Efficient learning: Reduces unnecessary exploration compared to ε-greedy.
Better dec
ision-making: Focuses on actions that may still be promising.
Automatic adjustment: Exploration decreases over time as more data is
collected.
In contrast, ε-greedy explores randomly, even when it is not beneficial.
Evaluation in Limited Data and High Uncertainty
UCB performs well when data is limited because it prioritizes uncertain
actions.
It ensures that all actions are explored sufficiently before exploitation.
Suitable for problems where early decisions are critical.
Limitations:
Slightly more complex than ε-greedy
Requires maintaining counts and logarithmic computation
May not perform well in highly non-stationary environments
********** 16 **********
--- page 17 ---
UCB is a powerful and efficient
b   A food relief vessel is stationed near a disaster-hit region. It must reach its
base safely and can move only in East and West directions.
The possible routes are—
Go to Food Warehouse, collect supplies and then go to Home (East →
West)
Go to Backup Storage, collect food and then go to Home (West → East)
Go directly to home
Dangers:
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
Meaning Sta Wareho Backup   Ho   Contaminated   Pirate
rt   use   Storage   me   Zone   Zone
Reward   0   +12   +6   +4   −110   −80
CO-2,4   Values   0   0   0   0   0   0
SO-1   Initial   E   E   E   –   –   –
BL-2,4   Policy   [10]
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
Answer: (2M+6M+2M)
********** 17 **********
--- page 18 ---
Iteration 1: Policy Evaluation
V(S1)=0,  V(S2)=12,  V(S3)=6,  V(S4)=4,  V(S5)=−110,  V(S6)=−80
Policy Iteration
S1
East:
V(S1)=0.7(12)+0.3(6)=8.4+1.8=10.2
West:
V(S1)=0.3(12)+0.7(6)=3.6+4.2=7.8
Best: East
S2
East:
V(S2)=0.7(−110)+0.3(4)=−77+1.2=−75.8
West:
V(S2)=0.3(−110)+0.7(4)=−33+2.8=−30.2
Best: West
S3
East:
V(S3)=0.7(4)+0.3(−80)=2.8−24=−21.2
West:
V(S3)=0.3(4)+0.7(−80)=1.2−56=−54.8
Best: East
Improved Policy
{E,  W,  E}
a   Explain how the Actor and Critic collaborate to improve the policy in
Reinforcement Learning, using appropriate pseudocode.
ii. Differentiate between the Actor-Critic method and the REINFORCE
algorithm, highlighting their differences.
Answer:
Working of Actor-Critic with Pseudocode: (1M)
In the Actor-Critic method, the actor selects actions based on a policy, while the
Q7   critic evaluates those actions using a value function. The critic provides feedback
CO-5   in the form of a Temporal Difference (TD) error, which helps the actor improve
SO-1   its policy.   [10]
BL-2,3
Pseudocode (One-Step Actor-Critic): (3M)
1. Initialize actor parameters θ and critic parameters w
2. Initialize state s
3. Repeat until termination:
a. Select action a ~ π(a|s, θ)
b. Execute action a, observe reward r and next state s′
c. Compute TD error: δ = r + γV(s′, w) − V(s, w)
d. Update critic: w ← w + αc · δ · ∇w V(s, w)
e. Update actor: θ ← θ + αa · δ · ∇θ log π(a|s, θ)
f. Set s ← s′
********** 18 **********
--- page 19 ---
This process continues, allowing the actor to improve its policy based on
feedback from the critic.
(3M)
Comparison: Actor-Critic vs REINFORCE (3M)
Aspect   Actor-Critic Method   REINFORCE Method
Approac   Combines value and policy   Pure policy gradient
h   methods   method
Learning   Uses TD error (bootstrapping)   Uses full return after
episode
Variance   Lower variance   High variance
Bias   Slight bias due to approximation   Unbiased
********** 19 **********

[Text in pictures on this page, read by OCR]
Actor Critic Method
a
co Actor:

G The actor represents the policy, which decides which action
to take given a state

It directly updates the policy parameters in the direction
that maximizes expected cumulative rewards, often using a
policy gradient method

G The actor’s goal is to maximize the rewards by making
better action selections over time

Actor Critic Method

a
O Critic:

O The critic estimates the value function (usually the state-
value V(s) or action-value Q(s,a)function), which represents
the expected return from a given state or state-action pair.

G It provides feedback (called the temporal difference (TD)
error) to the actor about how good the actions taken were,
relative to the expected value.

G The TD error helps the actor understand whether it should
adjust its policy in a positive or negative direction.

Actor Critic Method

=
c Policy Update:

O The actor updates its policy using the feedback from
the critic, making incremental adjustments to maximize
future rewards.

O This update helps the agent learn both efficient action
selection (from the policy update) and the ability to
estimate future rewards accurately (from the value
update).
--- page 20 ---
Update   Step-by-step (online)   End of episode (offline)
Efficienc   Faster and more stable   Slower convergence
y
b   With help of a pseudo code, explain SARSA TD control algorithm.
Consider the following Q [S, A] table:
State 1   State 2
Action 1   3.0   5.0
Action 1   7.0   4.0
Assume that 𝛼= 0.3, 𝑎𝑛𝑑 𝛾= 0.6
After the experience < 1,1,8,2,2 > for ⟨S, A, R, S’, A’⟩, which value of
the table gets updated and what is its new value?
“SARSA is called an on-policy TD control algorithm” State true or false
and justify the same.
Hint: SARSA learning algorithm is given by the following equation:
𝑄( 𝑆𝑡, 𝐴𝑡) ← 𝑄( 𝑆𝑡, 𝐴𝑡) + 𝛼 [𝑅𝑡+1 + 𝛾𝑄( 𝑆𝑡+1, 𝐴𝑡+1) − 𝑄( 𝑆𝑡, 𝐴𝑡)].
Answer: (4M+4M+2M)
CO-2,4
SO-1
[10]
BL-3,4
Step 1: Identify values
Current state S=1, action A=1 → Q (1,1) =3.0
Reward R=8
Next state S′=2, next action A′=2 → Q (2,2) =4.0
Step 2: Apply SARSA formula
Q(s,a)←Q(s,a)+α[R+γQ(s′,a′) −Q(s,a)]
Step 3: Substitute values
Q (1,1) =3+0.3[8+0.6(4) −3]
Q (1,1) =3+0.3[8+2.4−3] =3+0.3(7.4) =3+2.22=5.22
Updated Value:
Updated entry = Q (1,1)
New value = 5.22
Concept Statement:
“SARSA is called an on-policy TD control algorithm.”
Answer: TRUE
Justification:
SARSA updates Q-values using the actual action taken (A') under the
current policy.
It follows the same policy for both behavior and learning.
********** 20 **********

[Text in pictures on this page, read by OCR]
Sarsa (on-policy TD control) for estimating Q ~

Algorithm parameters: step size a € (0, 1], small ¢ > 0
Initialize Q(s, a), for all s € S*,a € A(s), arbitrarily except that Q(terminal, -) = 0

Loop for each episode:
Initialize S
Choose A from S using policy derived from Q (e.g., ¢-greedy)
Loop for each step of episode:
Take action A, observe R, S’
Choose A’ from S’ using policy derived from Q (e.g., e-greedy)
Q(S, A) — Q(S, A) + a[R + 7Q(S’, A.) — Q(S, A)]
SS, ACA’;
until S is terminal
--- page 21 ---
Hence, it is an on-policy algorithm.
SARSA is called an on-policy algorithm because it learns the value of the
policy that it actually follows during interaction with the environment. The
action-value updates use the current policy’s action (the next action taken)
hence the name State–Action–Reward–State–Action (SARSA) — making
learning dependent on the same policy used for exploration and execution.
********** 21 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 46ee8e2628fb

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_DS_7052/Reinforcement Learning/ANS_Reinforcement Learning(702DB0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (21 pages)

````text
SYNOPTICS
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
1. This question paper contains 21 pages.
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
Answer briefly:
a   Discuss in detail the application of Reinforcement Learning for Trading
and Finances by cosidering all the components of RL.
Answer:
Reinforcement Learning (RL) is widely used in trading and finance to
develop intelligent systems that can make sequential decisions, such as
buying, selling, or holding financial assets, with the objective of
maximizing profit over time. (01)
Components of RL in Trading: (03)
CO-1;
SO-1;   1. Agent:   [05]
BL-2   The agent is the trading algorithm or model that makes decisions in
the market (e.g., whether to buy, sell, or hold a stock).
2. Environment:
The environment represents the financial market, including stock
prices, market trends, economic indicators, and other external
factors that influence trading.
3. State:
The state is the current representation of the market at a given time,
such as current stock prices, historical data, technical indicators,
portfolio value, etc.
4. Actions:
The possible actions include buying, selling, or holding assets. In
********** 1 **********
--- page 2 ---
some cases, actions may also include deciding the quantity of assets
to trade.
5. Reward:
The reward is the profit or loss obtained after taking an action. For
example, a positive reward is given for profitable trades, while
losses result in negative rewards.
6. Policy:
The policy defines the strategy followed by the agent to choose
actions based on the current state, aiming to maximize cumulative
rewards (long-term profit).
Working: (01)
The agent observes the current market state, takes an action
(buy/sell/hold), and receives a reward based on the outcome. Over time, it
learns an optimal policy by interacting with the environment repeatedly
and improving its decisions.
RL helps in automating trading strategies, adapting to changing market
conditions, and optimizing long-term returns. However, challenges such as
market volatility, risk management, and data uncertainty must be carefully
handled.
b   Define Markov Decision Process (MDP) with reference to rewards,
transition model, discount factor, horizon, goal.
Answer:
A Markov Decision Process (MDP) is a mathematical framework used in
Reinforcement Learning to model decision-making in situations where
outcomes are partly random and partly under the control of an agent. It
satisfies the Markov property, meaning the next state depends only on the
current state and action. (1M)
An MDP is defined by the following components: (4M)
CO-3;   1. States (S):
SO-1;   A set of all possible situations in which the agent can exist.   [05]
BL-2   2. Actions (A):
A set of actions available to the agent in each state.
3. Transition Model (P):
Defines the probability of moving from one state to another after
taking an action, i.e.,
P(s′ | s, a) represents the probability of reaching state s′ from state s
after action a.
4. Reward (R):
A numerical value received after transitioning from one state to
another. It indicates the immediate benefit of an action.
5. Discount Factor (γ):
A value between 0 and 1 that determines the importance of future
rewards. A higher γ gives more importance to long-term rewards,
while a lower γ focuses on immediate rewards.
********** 2 **********
--- page 3 ---
6. Horizon:
It refers to the length of time the agent considers for decision-
making. It can be finite (limited steps) or infinite (ongoing
process).
7. Goal:
The objective of the agent is to find an optimal policy that
maximizes the cumulative (discounted) reward over time.
Thus, an MDP provides a structured way to model and solve sequential
decision-making problems in uncertain environments.
c   With reference to Dynamic Programming and Monte Carlo approaches,
explain the concepts of model-based and model-free reinforcement
learning.
Answer:
In Reinforcement Learning, approaches can be classified as model-based
and model-free depending on whether the agent has knowledge of the
environment’s model (transition probabilities and rewards). (1M)
Model-Based Reinforcement Learning (Dynamic Programming): (2M)
Model-based methods assume that the agent has complete knowledge of
the environment, including the transition model and reward function.
Dynamic Programming (DP) is a model-based approach because it uses
this known model to compute value functions and optimal policies using
Bellman equations.
CO-2,4;
SO-1;   The agent does not need to interact with the environment extensively, as it   [05]
BL-2   can plan using the model.
Model-Free Reinforcement Learning (Monte Carlo): (2M)
Model-free methods do not require knowledge of the environment’s
model. The agent learns directly from experience by interacting with the
environment.
Monte Carlo (MC) methods are model-free because they learn value
functions based on sampled episodes and actual rewards received.
The agent improves its policy through trial-and-error learning.
Dynamic Programming represents model-based RL with full knowledge of
the environment, while Monte Carlo represents model-free RL where
learning occurs through experience without a predefined model.
d   Write the pseudocode for the Naive REINFORCE algorithm. State the
CO-5;
weight update rule used in REINFORCE and explain the role of each term
SO-1;   [05]
in the expression.
BL- 2
********** 3 **********
--- page 4 ---
Answer:
REINFORCE is a policy gradient algorithm: a class of model-free RL
methods that directly learns a parameterized policy π_θ(a|s) without using
a value function. It uses Monte Carlo sampling to estimate the policy
gradient from complete episode trajectories. (1M)
(2M)
Term   Name   Role
Policy   The weights of the policy network being
θ
Parameters   optimized
Controls the step size of each update — too
Learning
α   large causes instability, too small causes slow
Rate
convergence
The actual total reward obtained from time
Discounted   step t to the end of the episode; acts as a
G_t
Return   scaling factor — actions that led to high
returns are reinforced more strongly
∇_θ   Score   The gradient of the log probability of the
log   Function /   action taken; points in the direction that
π_θ(A_ Policy   increases the probability of action A_t under
t | S_t)   Gradient   policy π_θ
(2M)
a   Explain the concepts of Immediate Reinforcement and Delayed
Reinforcement in Reinforcement Learning (RL). Compare the two
Q2   approaches and illustrate their importance using suitable real-world
CO-1;   examples.
SO-1;   [10]
BL-2   Answer:
Immediate Reinforcement: (02 M)
Immediate reinforcement refers to situations where the agent receives
********** 4 **********

[Text in pictures on this page, read by OCR]
REINFORCE: Monte-Carlo Policy-Gradient Control (episodic) for 7.

Input: a differentiable policy parameterization 7(a|s, 0)
Algorithm parameter: step size a > 0
Initialize policy parameter 8 € R® (e.g., to 0)

Loop forever (for each episode):
Generate an episode So, Ao, Ri Sr-1, Ar-1, a following z(-|-, 0)
Loop for each step of the episode t = 0,1,..., T-
Ge Vit HR (Gi)
0<-0+a7'GV Inz(A;|S¢, 4)
--- page 5 ---
feedback (reward or penalty) instantly after taking an action. The
consequence of the action is known right away, making it easier for the
agent to learn the correct behaviour.
Example:
In a simple game, if an agent earns points immediately after making a
correct move, it can quickly learn which actions are beneficial.
Delayed Reinforcement: (02 M)
Delayed reinforcement occurs when the reward is not given immediately
after an action but after a sequence of actions. The agent must learn which
earlier actions contributed to the final outcome, making learning more
complex.
Example:
In chess, the agent may make several moves before winning or losing the
game. The reward (win/loss) is received only at the end, so it is difficult to
determine which moves were responsible for the outcome.
Comparison: (02 M)
Aspect   Immediate   Delayed Reinforcement
Reinforcement
Feedback   Instant   After a delay
Timing
Learning   Easier   More complex
Difficulty
Credit   Simple   Difficult (credit assignment
Assignment   problem)
Decision   Short-term focus   Long-term strategy
Making
Importance in Real-World Applications: (02 M)
Immediate RL Applications:
Used in scenarios where quick feedback is available, such as
recommendation systems or simple control systems.
Delayed RL Applications:
Important in complex tasks like autonomous driving, robotics, and
financial trading, where decisions have long-term consequences.
Both immediate and delayed reinforcement are essential in RL. While
immediate reinforcement simplifies learning, delayed reinforcement
enables the agent to optimize long-term rewards, making it more suitable
for real-world complex problems.
b   Consider a 4×4 Grid World problem where the goal is to reach either the
CO-3
top-left corner or the bottom-right corner (refer to the figure). The agent
SO-1;   [10]
can choose from four actions: Up, Down, Left, Right, which
BL-3,4
deterministically cause the corresponding state transitions, except that
********** 5 **********
--- page 6 ---
actions leading outside the grid leave the state unchanged. The task is
modelled as an undiscounted episodic problem (γ = 1) with a reward of −1
for all transitions, and the agent follows an equiprobable random policy
(π).
Given the partial value function for this grid, apply and analyse the
Bellman Expectation Equation to compute the missing state values in the
first and third rows,
𝑉𝜋(𝑠) = 𝑅(𝑠) + 𝛾∑𝑃(𝑠′|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
𝑠′
Answer: (5M+ 5M)
Bellman Expectation Equation Calculations
For v1 (First Row, Second Column)
v1 = 0.25 × [(-1 - 18) + (-1 - 20) + (-1 + 0) + (-1 + v1)]
= 0.25 × [-19 - 21 - 1 + (v1 - 1)]
= 0.25 × [-42 + v1]
⇒ v1 = -10.5 + 0.25 v1
⇒ 0.75 v1 = -10.5
⇒ v1 = -14
For v2 (Third Row, First Column)
v2 = 0.25 × [(-1 - 22) + (-1 - 22) + (-1 - 20) + (-1 + v2)]
= 0.25 × [-23 - 23 - 21 + (v2 - 1)]
= 0.25 × [-68 + v2]
⇒ v2 = -17 + 0.25 v2
⇒ 0.75 v2 = -17
⇒ v2 = -22.67
Final Answers
v1 = -14
v2 = -22.67
a   Consider a finite, episodic Markov Decision Process (MDP) with two non-
Q3   terminal states C and D and a terminal state T. Assume that the following
CO-2,4;   two episodes are observed when Monte-Carlo evaluation is being carried
[10]
SO-1   out. The numbers within the episodes denote the rewards collected during
BL-4,5   transitions.
********** 6 **********
--- page 7 ---
Assume the discount factor γ = 0.6.
Episode 1: C 2 D 4 C 3 D 1 T
Episode 2: D 5 C 2 D 2 C 0 T
1. Estimate the state value for both states C and D using First Visit
Monte Carlo algorithm.
2. Estimate the state value for both states C and D using Every Visit
Monte Carlo algorithm.
3. Construct Markov model that best explains the above scenario.
Hint:
Return 𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer: (4M+4M+2M)
Returns
Episode 1:
C₁ = 2 + 0.6(4) + 0.6²(3) + 0.6³(1)
= 2 + 2.4 + 1.08 + 0.216 = 5.696
D₁ = 4 + 0.6(3) + 0.6²(1)
= 4 + 1.8 + 0.36 = 6.16
C₂ = 3 + 0.6(1) = 3.6
D₂ = 1
Episode 2:
D₁ = 5 + 0.6(2) + 0.6²(2)
= 5 + 1.2 + 0.72 = 6.92
C₁ = 2 + 0.6(2) + 0.6²(0)
= 2 + 1.2 = 3.2
D₂ = 2
C₂ = 0
First Visit Monte Carlo
C = (5.696 + 3.2) / 2 = 4.448
D = (6.16 + 6.92) / 2 = 6.54
Every Visit Monte Carlo
C = (5.696 + 3.6 + 3.2 + 0) / 4 = 3.624
D = (6.16 + 1 + 6.92 + 2) / 4 = 4.02
iii. Construct Markov Model (with Probabilities)
Step 1: Transition Counts
From C:
C → D = 3 times
C → T = 1 time
Total transitions from C = 4
From D:
D → C = 3 times
D → T = 1 time
Total transitions from D = 4
********** 7 **********
--- page 8 ---
Step 2: Transition Probabilities
P(C → D) = 3/4 = 0.75
P(C → T) = 1/4 = 0.25
P(D → C) = 3/4 = 0.75
P(D → T) = 1/4 = 0.25
Final Markov Model
C → D, C → T
D → C, D → T
b   Describe the Policy Iteration algorithm in the context of Dynamic
Programming. Illustrate your answer with appropriate pseudo-code.
Answer: (1M+3M+1M)
Policy Iteration Algorithm
Policy Iteration is another Dynamic Programming method that alternates
between evaluating a policy and improving it until an optimal policy is
obtained.
Pseudo-code for Policy Iteration
CO-2,4
SO-1
[05]
BL-2
Working Explanation
•   Start with an initial policy.
********** 8 **********

[Text in pictures on this page, read by OCR]
1. Initialization
V(s) € B and x(s) € A(s) arbitrarily for all s € 8; V(terminal) = 0

2. Policy Evaluation
Loop:
A+o0
Loop for each s € 8:
v<¢ V(s)
Vis) — Ly. p(s’,7|s,2(s)) [r + 7V/(s')]
A + max(A, |v — V(s)|)
until A < @ (a small positive number determining the accuracy of estimation)

3. Policy Improvement
policy-stable < true
For each s € 8:
old-action — m(s)
n(s) ¢ argmax, ),, ,.p(s’,r|s,a)[r + 7V(s’)]
If old-action 4 x(s), then policy-stable — false
If policy-stable, then stop and return V = v, and 7 ~ 7,; else go to 2
--- page 9 ---
•   Policy Evaluation: Compute value function for that policy.
•   Policy Improvement: Update policy by choosing better actions.
• Repeat until the policy no longer changes.
The final policy is guaranteed to be optimal
c   Define on-policy and off-policy learning in the context of Monte Carlo methods.
Give one real-world example of each. Explain the role of the behavior policy and
the target policy in off-policy Monte Carlo learning.
Answer:
On-policy Learning (Monte Carlo): (1.5M)
On-policy learning refers to learning the value of a policy using episodes
generated by the same policy. In Monte Carlo methods, the agent follows a single
policy to generate episodes and updates the value function based on the returns
observed from those episodes. The behavior policy and target policy are the same.
Example:
A robot learning to navigate a maze by following its current policy (e.g., ε-
greedy) and improving it based on the rewards received while following that same
policy.
Off-policy Learning (Monte Carlo): (1.5M)
Off-policy learning refers to learning the value of a target policy using episodes
generated from a different policy called the behavior policy. This allows learning
CO-2,4   from exploratory or previously collected data.
SO-1   [05]
BL-2,3   Example:
A self-driving car learning the optimal driving strategy (target policy) using data
collected from human drivers (behavior policy).
Role of Behaviour Policy and Target Policy in Off-policy Monte Carlo: (2M)
•   Behavior Policy (b): It is the policy used to generate episodes. It is
usually more exploratory to ensure sufficient coverage of state-action
pairs.
•   Target Policy (π): It is the policy whose value function we want to learn
or evaluate. It is typically more optimal or greedy.
Since the data is generated using the behavior policy but evaluated for the target
policy, there is a mismatch. To correct this, importance sampling is used, which
reweights the returns based on the likelihood of actions under both policies. This
ensures that the estimated values accurately reflect the target policy.
Q4   a   Consider a Multi-Armed Bandit problem with the following parameters:
CO-2
SO-1   Time step t = 5   [10]
BL-3,4   Number of bandits (machines) = 4
********** 9 **********
--- page 10 ---
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
Answer: (2M + 6M + 2M)
********** 10 **********

[Text in pictures on this page, read by OCR]
Construct a CDF table based on the following machine selection probability
5 P;(M;) = 0.3, Ps(Mz) = 0.4, Ps(M3) = 0.2, Ps(Mg) = 0.1

M1 0.3 0.3

M2 0.4 0.7
M3 0.2 0.9
M4 0.1 1.0

Random number generated for selection of machines for five iterations is [0.68, 0.55, 0.23, 0.95,
0.8]

Hence from CDF column we infer that Machines M2, M2, M,, Mgand M3 are selected for iterations
1,2,3,4,and 5 respectively

Now based on the machines selected and the random number generated for each iteration, we
will decide whether the machine fetched a reward of 1 or 0

Probability of winning in each machine is P,,(M,) = 0.6, P,,(M>) = 0.4, PR, (M3) = 0.7,R,(M4) = 0.9
Random number generated were as follows
5 [0.6, 0.2, 0.3, 0.4, 0.9]

Random number

Probability of Random number

winning of each | generated for

generated for

machine selection

machine P,, reward P.

1 0.68 M;
2 0.55 Mz 0.4 02 1
3 0.23 M, 06 03 1
4 0.95 My 09 04 1

5 08 M3 07 09 t)

Total reward obtained = 3

Maximum reward that was possible if the best
machin e is selected(M, with probability of winning P,,(M4) =
0.9) is

00.9*5= 4.5

Regret= 4.5-3=1.5
--- page 11 ---
b   A robot operates in a house with two areas: Living Room (S1) and Kitchen
(S2). At each step, the robot can either Clean or Stay Idle.
From Living Room: Clean → 0.6 chance to move to Kitchen, 0.4 stay in
Living Room
From Kitchen: Clean → 0.5 chance to move to Living Room, 0.5 stay in
Kitchen
Stay Idle → remains in same state
Rewards: +4 for ending in Kitchen and +2 for ending in Living Room
i.   Develop a state diagram showing transitions and rewards for all
state-action pairs for the above-mentioned scenario.
ii.   Write 𝑝(𝑠′, 𝑟|𝑠, 𝑎) for all the possible state action combinations.
Answer: (2.5M + 2.5M)
MDP Representation
States: S1: Living Room S2: Kitchen, Actions: Clean, Idle
Transition Probabilities   P(s′,r∣s,a)
From S1: P(S2, +4 | S1, Clean) = 0.6, P(S1, +2 | S1, Clean) = 0.4, P(S1, +2
CO-3
| S1, Idle) = 1.0
SO-1   [05]
From S2: P(S1, +2 | S2, Clean) = 0.5, P(S2, +4 | S2, Clean) = 0.5, P(S2, +4
BL-3
| S2, Idle) = 1.0
Summary Table
Current State   Action Next State   P(s′,r∣s,a) Reward
S1   Clean   S2   0.6   +4
S1   Clean   S1   0.4   +2
S1   Idle   S1   1.0   +2
S2   Clean   S1   0.5   +2
S2   Clean   S2   0.5   +4
S2   Idle   S2   1.0   +4
State Diagram (Text Form)
S1 → S2 (Clean, 0.6, +4)
S1 → S1 (Clean, 0.4, +2)
S2 → S1 (Clean, 0.5, +2)
S2 → S2 (Clean, 0.5, +4)
Self-loops:
S1 → S1 (Idle, 1.0, +2)
S2 → S2 (Idle, 1.0, +4)
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
********** 11 **********
--- page 12 ---
Answer: (2M + 2M + 1M)
Returns for γ = 0.8
t   Calculation   Gₜ
5 –   0
4 R₅   1
3 R₄ + 0.8·R₅   2.8
2 R₃ + 0.8·R₄ + 0.64·R₅   5.24
1 R₂ + 0.8·R₃ + 0.64·R₄ + 0.512·R₅   8.192
0 R₁ + 0.8·R₂ + 0.64·R₃ + 0.512·R₄ + 0.4096·R₅ 11.5536
Returns for γ = 0.2
t   Calculation   Gₜ
5 –   0
4 R₅   1
3 R₄ + 0.2·R₅   2.2
2 R₃ + 0.2·R₄ + 0.04·R₅   3.44
1 R₂ + 0.2·R₃ + 0.04·R₄ + 0.008·R₅   4.688
0 R₁ + 0.2·R₂ + 0.04·R₃ + 0.008·R₄ + 0.0016·R₅ 5.9376
Comparison Table
Return   γ = 0.8   γ = 0.2
G5   0   0
G4   1   1
G3   2.8   2.2
G2   5.24   3.44
G1   8.192   4.688
G0   11.5536 5.9376
Observation: Higher γ gives more importance to future rewards, resulting
in larger return values.
a   In the given example, the robot must move from the Start state 𝑆17 to the
Target state 𝑠0 with a reward structure of +90 for reaching the target and -1
for each step taken. Assume the initial Q-value Q(s,a) to be zero and discount
factor = 0.6. Apply the Monte-Carlo Exploring Starts Algorithm with T=6
and initial random state as (𝑆6, 𝐿) update the policy for given episode E1 and
Q5
E2.
CO-2,4
SO-1   [10]
i.   Discounted return given by equation 𝐺= 𝛾𝐺+ 𝑅𝑡+1. For discount
BL-3, 4
factor 𝛾= 0.6, compute discounted return list for the given episode
ii.   Obtain the average return list and update the Q value
iii.   Update the policy in the grid
Episode E1:
********** 12 **********
--- page 13 ---
(S₉,U) → (S₅,R) → (S₆,U) → (S₂,L) → (S₁,R) → (S₂,L) → (S₁,R)
Episode E2:
(S₆,D) → (S₁₀,U) → (S₆,R) → (S₇,U) → (S₂,L) → (S₁,L) → (S₀,stop)
Target
S0   S1   S2   S3   S4
S5   S6   S7   S8
S9   S10   S11   S12
S13   S14   S15   S16   S17
Answer: (5x2M)
Episode 1: Return Calculation
Formula:
Gₜ = Rₜ₊₁ + γGₜ₊₁
(All rewards = −1)
t   (State, Action)   Return (Gₜ)
6 (S₁,R)   −1
5 (S₂,L)   −1 + 0.6(−1) = −1.6
4 (S₁,R)   −1 + 0.6(−1.6) = −1.96
3 (S₂,L)   −1 + 0.6(−1.96) = −2.176
2 (S₆,U)   −1 + 0.6(−2.176) = −2.3056
1 (S₅,R)   −1 + 0.6(−2.3056) = −2.3834
Policy Update (Episode 1)
State Action Q(s,a)
S₉   U   −2.3834
S₅   R   −2.3834
S₆   U   −2.3056
S₂   L   avg(−2.176, −1.6) = −1.888
S₁   R   avg(−1.96, −1) = −1.48
Episode 2: Return Calculation
(Target reached → final reward = +90)
t   (State, Action) Return (Gₜ)
7 (S₀,stop)   90
********** 13 **********
--- page 14 ---
6 (S₁,L)   −1 + 0.6(90) = 53
5 (S₂,L)   −1 + 0.6(53) = 30.8
4 (S₇,U)   −1 + 0.6(30.8) = 17.48
3 (S₆,R)   −1 + 0.6(17.48) = 9.488
2 (S₁₀,U)   −1 + 0.6(9.488) = 4.6928
1 (S₆,D)   −1 + 0.6(4.6928) = 1.8157
Policy Update (Episode 2)
State Best Action Q value
S₆   R   9.488
S₁₀ U   4.6928
S₇   U   17.48
S₂   L   30.8
S₁   L   53
S₀   stop   90
Final Policy
State Best Action Q value
S₆   R   9.488
S₁₀ U   4.693
S₇   U   17.48
S₂   L   30.8
S₁   L   53
S₀   stop   90
S₅   R   −2.383
S₉   U   −2.383
Outcomes:
• Monte Carlo method uses complete episode returns
•   States closer to goal have higher Q-values
•   Policy improves by choosing maximum Q(s,a)
•   Step penalty affects how quickly optimal policy is learned
b   Consider an environment with three states: X, Y, and Z.
There is only one action available, which deterministically moves the agent to the
next state.
Rewards:
Transition from X → Y gives a reward of 2
CO-2,4   Transition from Y → Z gives a reward of 5
SO-1   Transition from Z → Terminal gives a reward of 3
[10]
BL-2,3   Given:
Discount factor γ=0.9, Learning rate α=0.2, Initial values: V(X)=V(Y)=V(Z)=0
Tasks:
i.   Compare TD (0) and TD (1) approaches.
ii.   Apply Temporal Difference TD (1) to compute: V(X), V(Y), V(Z)
(show return calculation for each state)
********** 14 **********
--- page 15 ---
Hint: Value expression for TD (1) approach is –
𝑉(𝑆𝑡) = 𝑉(𝑆𝑡) + 𝛼(𝐺𝑡−𝑉(𝑆𝑡))
where,
𝐺𝑡= 𝑅𝑡+1 + 𝛾𝑅𝑡+2 + 𝛾2𝑅𝑡+3 + ⋯𝛾𝑇−𝑡−1𝑅𝑇
Answer:
i.   Comparison: TD(0) vs TD(1) (4M)
Feature   TD (0)   TD (1)
Update basis   One-step lookahead Full return (like Monte Carlo)
Target   R +γ V(S′)   Gt (complete future reward)
Bias   Higher bias   Lower bias
Variance   Low variance   Higher variance
Learning style Incremental   Episode-based
Speed   Faster updates   Slower but more accurate
ii.   TD (1) Calculations (6M)
Episode:
X→Y→Z→Terminal
Step 1: Compute Returns
For state X:
G(X)=2+0.9(5)+0.92(3) =2+4.5+0.81×3=2+4.5+2.43=8.93
For state Y:
G(Y)=5+0.9(3) =5+2.7=7.7
For state Z:
G(Z)=3
Step 2: Update Values using TD (1)
Update V(X):
V(X)=0+0.2(8.93−0)=1.786
Update V(Y):
********** 15 **********
--- page 16 ---
V(Y)=0+0.2(7.7−0)=1.54
Update V(Z):
V(Z)=0+0.2(3−0)=0.6
Final Values:
• V(X)=1.786
• V(Y)=1.54
• V(Z)=0.6
a   Describe the Upper Confidence Bound (UCB) method for action selection
in reinforcement learning. Apply the UCB formula to explain how it
balances exploration and exploitation.
Analyse its advantages over ε-greedy strategy and evaluate its
effectiveness in scenarios with limited data and high uncertainty.
Answer: (2M + 2M + 4M + 2M)
Description of UCB Method
The Upper Confidence Bound (UCB) method is an action selection
strategy used in reinforcement learning to balance exploration and
exploitation in the n-armed bandit problem.
The action is selected using the formula:
UCB(a) = Q(a) + c * √(ln t / N(a))
Where:
Q6   Q(a) = estimated value of action a
CO-2   N(a) = number of times action a has been selected
SO-1   t = total number of time steps   [10]
BL-3,4,5   c = exploration parameter (controls degree of exploration)
The first term represents exploitation (choosing actions with high
estimated reward), while the second term represents exploration (favouring
less tried actions).
Application and Working
Initially, all actions are selected at least once.
Actions with fewer selections (small N(a)) get a larger exploration bonus.
As an action is selected more often, N(a) increases and the exploration
term decreases.
Thus:
Less explored actions → higher bonus → more likely to be selected
Well-explored actions → lower bonus → selected based on actual
performance
This ensures a systematic balance between exploration and exploitation
without randomness.
Advantages over ε-greedy
********** 16 **********
--- page 17 ---
Targeted exploration: UCB explores actions based on uncertainty, not
randomly.
Efficient learning: Reduces unnecessary exploration compared to ε-greedy.
Better decision-making: Focuses on actions that may still be promising.
Automatic adjustment: Exploration decreases over time as more data is
collected.
In contrast, ε-greedy explores randomly, even when it is not beneficial.
Evaluation in Limited Data and High Uncertainty
UCB performs well when data is limited because it prioritizes uncertain
actions.
It ensures that all actions are explored sufficiently before exploitation.
Suitable for problems where early decisions are critical.
Limitations:
Slightly more complex than ε-greedy
Requires maintaining counts and logarithmic computation
May not perform well in highly non-stationary environments
UCB is a powerful and efficient method for action selection, providing a
better balance between exploration and exploitation than ε-greedy,
especially in environments with limited data and high uncertainty.
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
CO-2,4   There is a military restricted zone to the West of the Gas Terminal
SO-1   There is uncertainty in directions:
[10]
BL-2, 4   Probability of intended direction = 0.7
Probability of opposite direction = 0.3
Assume:
Initial policy: Move East
Initial values = 0
State Table
States   S1 S2   S3   S4   S5   S6
Meaning   St   Chemical   Gas   Ho   Toxic   Restricted
art Depot   Terminal me   Zone   Zone
Reward   0   +15   +8   +5   −120   −90
Values   0   0   0   0   0   0
********** 17 **********
--- page 18 ---
Initial   E   E   E   –   –   –
Policy
Hint: Policy iteration expressions
Policy evaluation:
𝑉𝜋= 𝑟(𝑠) + 𝛾∑ 𝑠′,𝑟 𝑃(𝑠′, 𝑟|𝑠, 𝜋(𝑠))𝑉𝜋(𝑠′)
Policy improvement:
𝜋(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥𝑎∑𝑝(𝑠′, 𝑟|𝑠, 𝑎)𝑉𝜋(𝑠′)
𝑠′∈𝑆
State Diagram:
Answer:   (2M+6M+2M)
Iteration 1: Policy Evaluation
V(S1) =0,  V(S2)=15,  V(S3)=8,  V(S4)=5,  V(S5)=−120,  V(S6)=−90
Policy Iteration
S1
East:
V(S1)=0.7(15)+0.3(8)=10.5+2.4=12.9
West:
V(S1)=0.3(15)+0.7(8)=4.5+5.6=10.1
Best: East
S2
East:
V(S2)=0.7(−120)+0.3(5)=−84+1.5=−82.5
West:
V(S2)=0.3(−120)+0.7(5)=−36+3.5=−32.5
Best: West
S3
East:
V(S3)=0.7(5)+0.3(−90)=3.5−27=−23.5
West:
V(S3)=0.3(5)+0.7(−90)=1.5−63=−61.5
Best: East
Improved Policy
********** 18 **********
--- page 19 ---
{E,  W,  E}
a   Attempt the following:
i.   Explain the one-step Actor-Critic algorithm.
ii.   Describe the roles of the Actor and the Critic, and explain
how they work together during the training process.
iii.   Compare the Actor-Critic method with the REINFORCE
algorithm, highlighting key differences.
Answer:
One-Step Actor-Critic Algorithm: (4M)
The one-step Actor-Critic algorithm combines value-based and policy-based
approaches. The actor updates the policy, while the critic evaluates the action
using a value function.
Steps:
i.   Initialize policy parameters (actor) and value function parameters (critic).
ii.   Observe current state s.
iii.   Select action a using the current policy π(a|s).
iv.   Execute action and observe reward r and next state s′.
v.   Compute Temporal Difference (TD) error:
Q7   δ = r + γV(s′) − V(s)
vi.   Update critic using TD error.
CO-5
vii.   Update actor policy in the direction suggested by TD error.
SO-1   [10]
viii.   Move to next state and repeat until termination.
BL-2,3
Roles of Actor and Critic & Their Interaction: (3M)
•   Actor:
The actor is responsible for selecting actions based on the policy. It
decides what action to take in a given state.
•   Critic:
The critic evaluates the action taken by the actor by estimating the value
function. It computes the TD error to measure how good the action was.
•   Interaction:
The actor selects an action → the critic evaluates it → the TD error is
used as feedback → the actor updates its policy to improve future actions.
Thus, the critic guides the actor’s learning process.
Comparison: Actor-Critic vs REINFORCE (3M)
Aspect   Actor-Critic Method   REINFORCE Method
Type   Combines value + policy   Pure policy gradient
methods   method
Learning   Updates policy using TD   Updates policy using full
error   return
Variance   Lower variance   High variance
Bias   Introduces some bias   Unbiased
Update   Step-by-step (online)   After complete episode
Frequency
********** 19 **********
--- page 20 ---
Efficiency   More efficient and faster   Slower learning
The Actor-Critic method improves over REINFORCE by reducing variance and
enabling faster, more stable learning through continuous feedback from the critic.
b   i.   With help of a pseudo code, explain SARSA TD control
algorithm.
Consider the following Q[S,A] table:
State 1   State 2
Action 1   2.5   6.0
Action 1   4.5   3.5
Assume that 𝛼= 0.4, 𝑎𝑛𝑑 𝛾= 0.5
ii.   After the experience < 2,1,5,1,2 > for ⟨S, A, R, S’, A’⟩, which
value of the table gets updated and what is its new value?
iii.   “SARSA is called an on-policy TD control algorithm” State
true or false and justify the same.
Hint: SARSA learning algorithm is given by the following equation:
𝑄( 𝑆𝑡, 𝐴𝑡) ← 𝑄( 𝑆𝑡, 𝐴𝑡) + 𝛼 [𝑅𝑡+1 + 𝛾𝑄( 𝑆𝑡+1, 𝐴𝑡+1) − 𝑄( 𝑆𝑡, 𝐴𝑡)].
CO-2,4
Answer: (4M+4M+2M)
SO-1
[10]
BL-3,4
Step 1: Identify values
•   Current state S=2,
•   action A=1 → Q (2,1) =6.0
• Reward R=5
• Next state S′=1, next action A′=2 → Q (1,2) =4.5
********** 20 **********

[Text in pictures on this page, read by OCR]
Sarsa (on-policy TD control) for estimating Q ~ q.

Algorithm parameters: step size a € (0, 1], small ¢ > 0
Initialize Q(s, a), for all s € 8*,a € A(s), arbitrarily except that Q(terminal, -) = 0

Loop for each episode:
Initialize S
Choose A from S using policy derived from Q (e.g., e-greedy)
Loop for each step of episode:
Take action A, observe R, S’
Choose A’ from S’ using policy derived from Q (e.g., e-greedy)
Q(S, A) + Q(S, A) + a{R + 7Q(S’, A’) — Q(S, A)]
SSeS; ACA,
until S is terminal
--- page 21 ---
Step 2: Apply SARSA formula
Q(s,a)←Q(s,a)+α[R+γQ(s′,a′)−Q(s,a)]
Step 3: Substitute values
Q (2,1) =6+0.4[5+0.5(4.5) −6] =6+0.4[5+2.25−6] =6+0.4(1.25)
=6+0.5=6.5
Updated Value:
• Updated entry: Q (2,1)
• New value: 6.5
Concept Statement:
“SARSA is an on-policy learning algorithm.”
Answer: TRUE
Justification:
• SARSA updates values using the action actually taken (A') by the
current policy.
• The same policy is used for both action selection and learning
updates.
• Hence, it is classified as an on-policy TD control algorithm.
SARSA is called an on-policy algorithm because it learns the value of the
policy that it actually follows during interaction with the environment. The
action-value updates use the current policy’s action (the next action taken)
hence the name State–Action–Reward–State–Action (SARSA) — making
learning dependent on the same policy used for exploration and execution
********** 21 **********
````
