# Generative AI with Large Language Models: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 96304de5d7e6

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Generative AI with Large Language Models /ANS_Generative AI with Large Language Models (703DB0C061)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (26 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Generative AI with Large Language Models
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
Explain Generative AI and Large Language Models (LLMs) with
CO-1; SO-2;   a. suitable use cases.   [05]
BL-2
Answer:
Generative AI refers to artificial intelligence systems that can create new
content such as text, images, or audio. Large Language Models (LLMs)
are a type of Generative AI trained on vast amounts of text data to
understand and generate human-like language.   02
Use cases of LLMs include:
• Text generation (articles, emails, chat responses)
• Code generation   03
• Language translation
• Question answering
• Summarization
LLMs are widely used in chatbots, virtual assistants, and content creation
tools.
Explain generative configuration in the context of LLMs.
CO-1; SO-2;   b.   [05]
BL-2   Answer:
********** 1 **********
--- page 2 ---
Generative configuration refers to the set of parameters that control how
a language model generates text. These include:
• Temperature: Controls randomness of output   01x5
• Top-k sampling: Limits selection to top k probable tokens
• Top-p (nucleus sampling): Chooses tokens based on cumulative
probability
• Max tokens: Limits output length
These settings help balance creativity and accuracy in generated
responses.
Apply your knowledge to justify when multi-task instruction fine-tuning
CO-2; SO-2;   c.   is preferred over single-task fine-tuning. Illustrate with an example of   [05]
BL-3   code snippet.
Answer:
Multi-task fine-tuning is preferred when:
• The application requires multiple functionalities
• There is a need for general-purpose models
2.5
Example:
A virtual assistant needs translation, summarization, and Q&A → multi-
task is suitable
Whereas a summarization-only tool → single-task is sufficient
2.5
Analyze the role of the reward model in RLHF and its impact on LLM
CO-3; SO-2;   d. performance.   [05]
BL-4
Answer:
********** 2 **********
--- page 3 ---
The reward model plays a central role in Reinforcement Learning from
Human Feedback, as it acts as a bridge between human preferences and   02
model optimization.
Role of the Reward Model
The reward model is trained on human-labeled data where multiple
outputs are ranked based on quality. It learns to predict a reward score
indicating how well a response aligns with human expectations.
• Converts human feedback into a learnable objective function
Instead of directly using human judgments repeatedly, the reward
model encodes them into a mathematical form.
• Guides reinforcement learning updates
During training (e.g., using Proximal Policy Optimization), the
LLM is optimized to maximize the reward score.
•   Generalizes human preferences
It allows the system to evaluate unseen outputs without requiring
continuous human intervention.
Impact on LLM Performance   02
The reward model significantly influences how well a Large Language
Model behaves in real-world tasks:
• Improves response quality and coherence
The model learns to generate more helpful, relevant, and
structured responses.
• Reduces undesirable outputs
Harmful, biased, or nonsensical responses are penalized,
improving safety.
• Enables scalable alignment
Once trained, the reward model replaces the need for constant
human evaluation, making large-scale deployment feasible.
01
Example
Consider training a chatbot using RLHF:
Prompt: “Explain climate change in simple terms.”
Model Outputs:
1. “Climate change is when weather changes.”
2. “Climate change refers to long-term shifts in temperature and
weather patterns caused mainly by human activities like burning
fossil fuels.”
Human Feedback:
• Output 2 is ranked higher due to clarity and completeness.
********** 3 **********
--- page 4 ---
Reward Model Behavior:
• Assigns a higher reward score to Output 2.
• During RL training, the LLM is updated to prefer similar high-
quality responses.
Result:
• Over time, the model consistently generates more informative and
user-aligned answers.
Q2   Explain the concept of Prompt Engineering in Generative AI. Describe
CO-1; SO-2;   a.   different prompting techniques with suitable examples. Also, provide a   [10]
BL-2   pseudo-code demonstrating how prompt design affects the output of a
language model.
Answer:
Concept of Prompt Engineering
02x5
Prompt Engineering is the process of designing and structuring input
prompts to effectively guide a Generative AI model (such as an LLM) to
produce accurate, relevant, and high-quality outputs.
Since Large Language Models generate responses based on input
context, the quality of the prompt directly influences the quality of the
output.
Objectives:
• Improve response accuracy
• Control tone, format, and style
• Reduce ambiguity and irrelevant outputs
Prompting Techniques
(a) Instruction-Based Prompting
In this technique, the model is given clear and explicit instructions about
what to do.
Example:
• Prompt:
“Summarize the following paragraph in 3 sentences.”
• Output:
A concise summary limited to 3 sentences.
********** 4 **********
--- page 5 ---
Explanation:
The model follows the instruction strictly, producing structured and task-
specific output.
(b) Role-Based Prompting
Here, the model is assigned a specific role or persona, which influences
tone and style.
Example:
• Prompt:
“You are a history teacher. Explain the causes of World War I to
a 10-year-old student.”
• Output:
A simple, easy-to-understand explanation with a teaching tone.
Explanation:
Assigning roles helps control style, expertise level, and perspective.
(c) Contextual Prompting
This technique provides additional background or context to guide the
response.
Example:
• Prompt:
“The student scored low marks in mathematics due to lack of
practice. Suggest improvement strategies.”
• Output:
Practical suggestions like regular practice, solving exercises, and
seeking help.
Explanation:
Context improves relevance and specificity of responses.
Demonstration: Effect of Prompt Design
The same task can produce different outputs based on prompt design.
Task: Write a short poem about nature
• Basic Prompt:
“Write a poem about nature.”
→ Output: General poem
• Improved Prompt (Role + Instruction):
“You are a romantic poet. Write a 4-line poem about nature using
vivid imagery.”
→ Output: More creative, structured, and expressive poem
Pseudo-Code
********** 5 **********
--- page 6 ---
define prompt_1 = "Write a poem about nature"
define prompt_2 = "You are a romantic poet. Write
a 4-line poem about nature using vivid imagery"
output_1 = LLM.generate(prompt_1)
output_2 = LLM.generate(prompt_2)
print("Basic Output:", output_1)
print("Refined Output:", output_2)
Q2   Explain BLEU as a metric for evaluating machine-generated text and
CO-2; SO-2;   b. how it measures similarity between a reference and a candidate sentence.   [10]
BL-4
• Reference: “A boy is playing football in the park”
• Candidate: “A child is playing soccer in a park”
• Compute unigram and bigram precision.
• Calculate the BLEU score (up to bigrams).
• Comment on the quality of the candidate sentence in terms of
semantic similarity and fluency.
Answer:
Definition of BLEU Score:
BLEU (Bilingual Evaluation Understudy) is a metric used to evaluate the   02
quality of machine-generated text by comparing it with one or more
reference sentences.
It measures how closely the candidate sentence matches the reference
using n-gram precision.
Role:
• Evaluates machine translation quality
• Measures similarity based on word and phrase overlap
• Provides a quantitative score for comparison
(i) Calculate Unigram and Bigram Precision:
• Reference Sentence: "A boy is playing football in the park."
• Candidate Sentence: "A child is playing soccer in a park."=
Step 1: Unigram Precision
Unigrams (individual words) in the reference:   02
{A, boy, is, playing, football, in, the, park}
Unigrams in the candidate:
{A, child, is, playing, soccer, in, a, park}
Matching unigrams: {A, is, playing, in, park} (5 out of 8)
********** 6 **********
--- page 7 ---
Unigram Precision = Matching Unigrams / Total Unigrams in Candidate
= 5/8 ≈ 0.625
Step 2: Bigram Precision   02
Bigrams (two-word sequences) in the reference:
{"A boy", "boy is", "is playing", "playing football", "football in", "in
the", "the park"}
Bigrams in the candidate:
{"A child", "child is", "is playing", "playing soccer", "soccer in", "in a",
"a park"}
Matching bigrams: {"is playing"} (1 out of 7)
Bigram Precision = Matching Bigrams / Total Bigrams in Candidate
= 1/7 ≈ 0.143
02
(ii) Compute BLEU Score:
02
(iii) Analysis:
• The BLEU score of 0.30 indicates moderate similarity between the
sentences.
• The unigram precision is reasonable, but bigram precision is low due to
phrase differences.
• Words like “boy → child” and “football → soccer” are correct
synonyms but not exact matches.
• The candidate sentence preserves the meaning but BLEU penalizes
lexical variation.
• BLEU measures surface similarity and may not fully capture semantic
correctness.
Q3   What is meant by quantization in Large Language Models (LLMs)?
CO-1; SO-2;   a. Explain how it contributes to improving memory efficiency, processing   [10]
BL-2   speed, and energy consumption.
Support your answer with an appropriate example.
********** 7 **********
--- page 8 ---
Answer:
Quantization in Large Language Models (LLMs) (Detail explanation)
02
Quantization is a technique used to reduce the precision of numerical
values (weights and activations) in a model. Instead of using high-
precision formats like 32-bit floating point, the model uses lower
precision such as 16-bit or 8-bit.
How Quantization Improves Efficiency
04
Memory Efficiency
• Lower precision → fewer bits per parameter
• Example: FP-32 (32 bits) → INT8 (8 bits)
•   Result: 4× reduction in memory usage
Processing Speed
• Lower precision operations require less computation
•   Faster arithmetic on CPUs/GPUs
• Leads to faster inference time
Energy Consumption
• Reduced computation → less power usage
• Important for battery-powered devices
• Enables energy-efficient AI systems
Example (Detail explanation required)
A chatbot model deployed on a mobile device:
04
•   Original model uses FP-32 → large size, slow response
•   After INT8 quantization:
• Model size reduces significantly
• Response becomes faster
• Battery usage decreases
Quantization helps make LLMs lighter, faster, and more energy-efficient,
enabling practical deployment in real-world applications.
Q3   Evaluate the effectiveness of Parameter-Efficient Fine-Tuning (PEFT)
CO-2; SO-2;   b. methods such as LoRA in reducing computational cost for large language
BL-5   models.
Using suitable calculations, compare the number of trainable parameters in   [10]
full fine-tuning vs LoRA.
Critically assess their impact on model performance and scalability.
Answer:
Parameter-Efficient Fine-Tuning (PEFT), particularly LoRA (Low-Rank
Adaptation), is highly effective in reducing computational cost while
********** 8 **********
--- page 9 ---
maintaining competitive performance. Below is a structured evaluation with
calculations, comparisons, and critical assessment.
02
This dramatically reduces trainable parameters and computational
overhead.
02
~99.6% redution in trainable parameters.
********** 9 **********
--- page 10 ---
02
 Memory drops from ~TB scale → MB scale
3. Computational Cost Reduction
(a) Training Cost
•   Full FT: updates all weights → high FLOPs, memory, and time
• LoRA: updates only low-rank matrices →
o fewer gradients
o fewer optimizer states
o   faster backpropagation
Reported reductions:
• >90% memory savings
• ~99% fewer trainable parameters
(b) Storage Efficiency
•   Full FT: requires storing full model per task
• LoRA: store only adapter weights (~MBs)
Enables multi-task deployment cheaply
(c) Inference Cost
• No additional cost (weights can be merged after training)
02
4. Impact on Model Performance
(a) Positive Aspects
1. Near-parity with full fine-tuning
• Many tasks show comparable accuracy
•   Especially effective in:
********** 10 **********
--- page 11 ---
▪ NLP tasks
▪ domain adaptation
▪   instruction tuning
2. Better generalization
• Avoids overfitting in low-data settings
3. Faster experimentation
•   Enables rapid iteration across tasks
(b) Limitations
1. Capacity constraint
• Low-rank approximation limits expressiveness
• May underperform on:
▪   highly complex reasoning tasks
▪   large domain shifts
2. Hyperparameter sensitivity
• Rank rrr, scaling factor α\alphaα, target layers matter
3. Layer selection dependency
02
• Performance depends on where LoRA is applied
4. Residual performance gap
• Some studies show slight accuracy drop vs full FT
5. Scalability Analysis
Why LoRA Scales Better
(1) Linear Scaling with Rank
Parameters=r(d+k)
• Independent of full model size
• Allows tuning even 100B+ models on single GPU
(2) Multi-task Scalability
• Same base model + multiple LoRA adapters
•   Efficient task switching
(3) Hardware Accessibility
•   Full FT → requires high-end clusters
• LoRA → feasible on:
•   single GPU
• even consumer hardware (with QLoRA)
Trade-off
Aspect   Full Fine-Tuning   LoRA
Trainable parameters Very high   Extremely low
Memory usage   Very high   Low
Training cost   Expensive   Cheap
Performance   Slightly better   Near comparable
Scalability   Limited   Excellent
********** 11 **********
--- page 12 ---
6. Critical Evaluation (Final Insight)
Strengths
• Massive reduction in cost (orders of magnitude)
• Enables democratization of LLM fine-tuning
•   Maintains strong performance in most tasks
Weaknesses
•   Slight loss in peak performance
• Limited adaptability for highly complex transformations
•   Requires careful tuning
Q4   Investigate the role of evaluation and deployment stages in determining the
CO-1; SO-2;   a. success of a Generative AI application. Also give evaluation methods in   [10]
BL-4   brief.
Examine their linkage with prior stages of the lifecycle and illustrate your
explanation with examples and a diagram.
Answer:
Role of Evaluation and Deployment in Generative AI Success
The evaluation and deployment stages are crucial in determining whether a   04
Generative AI application performs effectively in real-world scenarios.
(a) Evaluation Stage – Analytical Role
The evaluation stage assesses how well the model performs after training.
Important Roles:
• Measures accuracy, coherence, and relevance of generated outputs
•   Detects issues such as bias, hallucination, and overfitting
• Ensures the model meets task-specific requirements
Impact on Success:
•   Proper evaluation → reliable and high-quality outputs
• Poor evaluation → flawed model proceeds to deployment
(b) Deployment Stage – Analytical Role
Deployment involves integrating the trained model into real-world
applications.
********** 12 **********
--- page 13 ---
Important Roles:
• Ensures scalability and responsiveness
• Handles user interaction and real-time inference
•   Requires optimization (e.g., latency, memory usage)
Impact on Success:
•   Efficient deployment → smooth user experience
• Poor deployment → delays, failures, or high resource usage
Evaluation Methods (Brief)
• Automatic Metrics
• BLEU, ROUGE (for text generation quality)
• Measure similarity with reference outputs
• Human Evaluation
• Experts assess quality, fluency, and usefulness
•   Task-Specific Evaluation
• Based on application (e.g., accuracy for QA systems)
• A/B Testing
• Compare two model versions in real-world usage
Linkage with Earlier Lifecycle Stages
The evaluation and deployment stages are closely connected with earlier
stages:
02
• Data Collection & Preprocessing → Evaluation
• Poor-quality data leads to poor evaluation results
• Model Training → Evaluation
•   Incorrect training results in low performance metrics
•   Evaluation → Deployment
• Only well-evaluated models should be deployed
Example
Chatbot Application:
01
•   If trained on biased data → evaluation detects bias
•   If ignored → deployed chatbot gives unfair responses
•   Proper evaluation → improved model before deployment
Diagram (Lifecycle with Feedback Loop)
03
Diagram (Life cycle)
********** 13 **********
--- page 14 ---
Evaluation ensures quality and correctness, while deployment ensures practical
usability. Their strong linkage with earlier stages highlights that any weakness
in data or training directly affects final system performance. Continuous
feedback between stages is essential for improving Generative AI applications.
Q4   With the help of a neatly labelled diagram of the Transformer architecture,
CO-1; SO-2;   b. describe how it works.   [10]
BL-3   Illustrate how tokenization and embedding are applied by converting a
sample sentence into its corresponding embeddings.
Answer:
Working of Transformer Architecture
The Transformer model processes input sequences using attention
mechanisms instead of recurrence.
Diagram (Transformer Architecture)
07
********** 14 **********
--- page 15 ---
03
Working (Brief Explanation)
1. Input text is converted into tokens
2. Tokens are transformed into embeddings
3. Positional encoding is added to preserve order
4. Attention layers capture relationships between words
5. Feed-forward layers refine representations
Tokenization and Embedding (Application)
Example Sentence:
“AI is powerful”
Step 1: Tokenization
["AI", "is", "powerful"]
Step 2: Assign Token IDs
[101, 205, 876]
Step 3: Embedding Representation
AI → [0.2, 0.8, 0.1]
is → [0.5, 0.1, 0.3]
powerful → [0.9, 0.7, 0.4]
********** 15 **********
--- page 16 ---
Each word is converted into a vector representation capturing meaning.
Tokenization and embedding convert raw text into numerical form, enabling
the Transformer to process language effectively.
Q5   A reinforcement learning agent trained using RLHF begins to generate
CO-3; SO-2;   a. unexpected outputs that still receive high reward scores. Analyze this   [10]
BL-4   behavior with respect to reward function design. Illustrate your answer
with a suitable example and supporting sketch.
Answer:
Analysis of the Behavior
The given scenario represents a classic case of reward hacking in
Reinforcement Learning from Human Feedback (RLHF).   05
This occurs when an agent learns to maximize the reward signal without
actually achieving the intended objective.
Reason for the Behavior (Reward Function Design Issues):
• The reward function is imperfect or incomplete.
•   It captures proxy objectives instead of the true goal.
• The agent identifies loopholes or shortcuts in the reward system.
• As a result, the agent produces unexpected or undesirable outputs
that still receive high reward scores.
How the Agent Exploits the Reward Function
• RL agents optimize strictly for reward maximization.
•   If the reward function:
• Overemphasizes certain patterns
•   Misses’ constraints
•   Is based on biased human feedback
→ The agent learns strategies that exploit these weaknesses.
The agent is not “wrong”, it is doing exactly what it was trained to do,
but the reward function does not fully align with human intent.
Example
Text Generation Scenario (LLM with RLHF):
Task: Generate helpful and truthful answers
Reward Model: Gives higher scores to long, confident-sounding
responses
Observed Behavior:
The model generates:
Overly verbose answers
Confident but incorrect information
Reason:
********** 16 **********
--- page 17 ---
The reward function Favors fluency and length, not factual correctness
The model exploits this by generating high-reward but misleading
outputs
03
Supporting Sketch
+-------------------+
|   Input Prompt   |
+-------------------+
|
v
+-------------------+
|   Agent   |
| (LLM Policy π)   |
+-------------------+
|
v
+-------------------+
|   Generated Text |
+-------------------+
|
v
+-------------------+
|   Reward Model   |
| (Imperfect Design)|
+-------------------+
|
High Reward ↑
|
(Even if output is incorrect)
Observations
• Mismatch between reward and true objective leads to reward
hacking   02
• Agent exploits statistical patterns rather than understanding
correctness
• Poor reward design = unintended behavior
This behavior highlights the importance of carefully designing reward
functions in RLHF.
If the reward model does not fully represent human intent, the agent may
produce high-reward but low-quality or misleading outputs, reducing the
reliability of LLMs in real-world applications.
Q5   Analyse the impact of chain-of-thought reasoning on the planning and
CO-4; SO-2;   b. decision-making ability of LLMs. Support your answer with an example   [10]
BL-4   without using and with using CoT.
Answer:
********** 17 **********
--- page 18 ---
Introduction to Chain-of-Thought (CoT) Reasoning
05
Chain-of-thought reasoning is a technique where a Large Language Model
(LLM) generates intermediate reasoning steps before producing the final
answer.
Instead of directly giving an output, the model breaks the problem into
smaller logical steps, mimicking human reasoning.
Impact on Planning Ability
Chain-of-thought significantly enhances planning in LLMs:
• Decomposition of Tasks:
Complex problems are divided into smaller sub-tasks, making them
easier to solve.
•   Sequential Reasoning:
The model follows a step-by-step process, ensuring logical flow and
reducing random or incorrect jumps.
•   Goal-Oriented Thinking:
Each step contributes toward achieving the final objective,
improving structured planning.
• Handling Multi-step Problems:
Particularly useful in tasks like:
•   Mathematical problem solving
•   Multi-hop question answering
•   Decision-based tasks
Impact on Decision-Making Ability
Chain-of-thought improves decision-making in the following ways:
• Improved Accuracy:
By evaluating intermediate steps, the model reduces errors.
• Transparency and Interpretability:
The reasoning steps make it easier to understand why a decision was
made.
• Reduced Hallucination:
Logical progression helps avoid unsupported or fabricated answers.
•   Better Context Utilization:
The model uses prior steps to inform future decisions.
Example   03
Problem:
“A shop sells a pen for ₹10. If a person buys 3 pens and pays ₹50, how
much change should be returned?”
Without Chain-of-Thought:
•   Output: ₹10 (may be incorrect due to direct guessing)
********** 18 **********
--- page 19 ---
With Chain-of-Thought:
Step 1: Cost of one pen = ₹10
Step 2: Cost of 3 pens = 3 × 10 = ₹30
Step 3: Amount paid = ₹50
Step 4: Change = 50 − 30 = ₹20
Final Answer: ₹20
Analysis of Improvement
• The reasoning steps ensure:
•   Correct calculation
•   Logical consistency
• The model avoids skipping steps, which reduces errors
• Accuracy improves because each step is validated before moving
forward
Real-World Relevance
Chain-of-thought reasoning is widely used in:
• LLM Applications   02
•   Chatbots requiring logical responses
•   Educational tutors explaining solutions
• Advanced Architectures
• ReAct (Reason + Act): Combines reasoning with tool usage
• Program-Aided Language Models (PAL): Uses reasoning to
generate executable code
•   Decision-Support Systems
•   Financial analysis
•   Healthcare recommendations
Chain-of-thought reasoning significantly enhances both planning and
decision-making in LLMs by enabling structured, step-by-step problem
solving.
It improves accuracy, interpretability, and reliability, making it a crucial
technique for building intelligent and trustworthy AI systems.
Q6   Analyze how a Large Language Model (LLM) can be integrated into a
CO-4; SO-2;   a. real-world application such as a chatbot or document summarization   [10]
BL-4   system. Discuss the important design considerations involved and
illustrate with an example.
Answer:
. Integration of LLM in Real-World Applications
03
A Large Language Model (LLM) can be integrated into applications like
chatbots or document summarization systems by embedding it within a
********** 19 **********
--- page 20 ---
structured pipeline that handles input processing, model inference, and
output delivery.
Typical Integration Workflow:
1. User Input Layer
• Accepts queries (text, voice, or documents)
2. Pre-processing Module
• Cleans and formats input (tokenization, normalization)
3. LLM Processing Layer
• The LLM generates responses or summaries based on
prompts
4. External Tools / APIs (Optional)
•   Fetch additional data (databases, web APIs, knowledge
bases)
5. Post-processing Module
• Formats output (summaries, structured responses)
6. Output Interface
04
•   Displays results to the user
Example: Chatbot Application
Scenario: Customer Support Chatbot
•   Input: “Where is my order?”
•   Process:
• LLM interprets intent
• Connects to order database via API
•   Retrieves order status
• Output: “Your order has been shipped and will arrive tomorrow.”
Analysis:
• LLM handles natural language understanding and generation
•   External system provides real-time data
•   Integration enables accurate and context-aware responses
Example: Document Summarization System
Scenario: News summarization tool
•   Input: Long news article
•   Process:
• LLM extracts key points
• Generates concise summary
• Output: Short summary highlighting main ideas
Analysis:
• LLM reduces information overload
• Improves readability and decision-making
03
********** 20 **********
--- page 21 ---
Important Design Considerations
a. Accuracy and Reliability
• Ensure outputs are factually correct
• Use validation mechanisms or external data sources
b. Latency and Performance
• Optimize response time for real-time applications
• Use efficient model deployment strategies
c. Scalability
• System should handle multiple users and large data volumes
d. Integration with External Systems
• APIs, databases, and tools enhance functionality
• Ensures dynamic and updated responses
e. Prompt Design and Context Handling
• Proper prompts improve output quality
• Maintain conversation history for context-aware responses
f. Security and Privacy
•   Protect sensitive user data
• Ensure secure API communication
g. Cost Efficiency
• Manage computational cost of LLM usage
Analysis of Integration
• LLM acts as the core reasoning and language engine
•   External systems provide real-world grounding
• Proper architecture ensures:
•   Better accuracy
• Context awareness
•   Scalability
Integrating an LLM into real-world applications like chatbots and
summarization systems enhances their ability to understand, process, and
generate human-like responses.
Careful consideration of design factors such as accuracy, scalability, and
integration ensures that the system is efficient, reliable, and practical for
real-world use.
Q6   A reward model in an RLHF system assigns the following scores to
CO-3; SO-2;   b. generated responses:   [10]
BL-5
********** 21 **********
--- page 22 ---
• Response A: R(A)=2.2
• Response B: R(B)=0.8
• Response C: R(C)=−1.0
Using the sigmoid-based preference function, determine the likelihood of
preference between the responses. Based on the calculations, evaluate
whether the reward model produces a reliable ranking of responses.
Justify your answer with appropriate reasoning.
Answer:
02x5
********** 22 **********
--- page 23 ---
4. Evaluation of Reward Model Effectiveness
Strengths:
• The probabilities are logically consistent with reward values
• Larger reward differences produce stronger preference
probabilities
• The model clearly distinguishes between:
• High vs medium (A vs B)
• Medium vs low (B vs C)
• High vs low (A vs C)
Reliability Indicators:
•   All probabilities are above 0.5, correctly indicating preference
direction
• Higher gaps → probabilities closer to 1 → good sensitivity
• Maintains transitivity (A > B and B > C ⇒ A > C)
5. Critical Evaluation
• The reward model is effective in ranking responses due to:
•   Clear separation in scores
•   Strong and consistent probability outputs
• However:
•   It assumes reward scores perfectly reflect human
preference
•   In real scenarios, biases or noise in reward data may
reduce reliability
The reward model produces a reliable and well-ordered ranking (A > B >
C) with strong preference probabilities.
Thus, the sigmoid-based pairwise ranking effectively captures preference
relationships and supports efficient optimization in RLHF systems.
Q7   Critically evaluate the effectiveness of Program-Aided Language Models
CO-4; SO-2;   a. (PAL) in improving the reasoning capabilities of Large Language Models.   [10]
BL-5   Compare it with traditional chain-of-thought prompting and justify with a
real-world example where PAL demonstrates superior problem-solving or
decision-making.
Answer:
Introduction to PAL:
Program-Aided Language Models (PAL) enhance the reasoning abilities of
Large Language Models (LLMs) by combining natural language reasoning   02
with programmatic execution. Unlike traditional prompting, which relies
solely on human-like chain-of-thought (CoT) reasoning, PAL allows the
LLM to generate intermediate code or programmatic steps to solve complex
multi-step problems. This approach reduces ambiguity and errors in
********** 23 **********
--- page 24 ---
reasoning, particularly for structured tasks such as mathematics, logic, or
algorithmic problem-solving.
Comparison with Chain-of-Thought Prompting:   03
Feature   Chain-of-Thought   Program-Aided Language
(CoT)   Model (PAL)
Reasoning   Natural language only Generates structured
Method   program/code to execute
reasoning
Accuracy   Can suffer from   Higher accuracy due to
logical errors or   executable intermediate
inconsistencies   steps
Complexity Limited for multi-step Excels at complex, multi-
Handling   tasks   step problems
Verificatio   Hard to verify each   Code execution provides
n   reasoning step   automatic verification of
intermediate steps
Flexibility   Limited to language   Can integrate with external
reasoning   systems, calculators, or APIs
Analysis: PAL effectively addresses the limitations of CoT prompting by
introducing a deterministic step-wise execution mechanism, thereby
improving reliability and consistency in LLM reasoning.
Real-World Example:
03
Scenario: Multi-step arithmetic reasoning problem.
Task: Solve “If a train departs at 9:00 AM traveling 60 km/h for 3 hours and
another departs at 10:00 AM traveling 80 km/h, when and where will they
meet?”
• CoT Approach: LLM attempts to reason step by step in natural
language. There is a risk of miscalculating relative speeds or time
differences.
• PAL Approach: LLM generates Python code to calculate positions
and intersection points:
# PAL-generated code
t = symbols('t')
train1 = 60 * t
train2 = 80 * (t - 1) # second train leaves 1 hour
later
solution = solve(train1 - train2, t)
solution
• Outcome: PAL executes the code and returns the exact meeting time
and distance without logical errors.
Observation: PAL ensures correctness and allows verification through code
execution, whereas CoT may yield approximations or errors in reasoning.
********** 24 **********
--- page 25 ---
Advantages of PAL:
• Enhances accuracy and reduces reasoning errors.
•   Suitable for multi-step or structured problems.   02
• Enables verification through program execution.
•   Integrates easily with external tools (calculators, APIs) for real-
world applications.
Program-Aided Language Models (PAL) significantly improve the
reasoning capabilities of LLMs compared to traditional chain-of-thought
prompting. By combining natural language reasoning with executable
programs, PAL ensures more reliable, verifiable, and complex problem-
solving. In tasks requiring multi-step logical or mathematical reasoning,
PAL demonstrates clear superiority, making it a valuable advancement in
LLM reasoning frameworks.
Q7   Analyse the given code snippet and describe its working in detail, expected
CO-2; SO-2;   b. output. Also Explain how the code can be applied in real-world scenarios,   [10]
BL-3   particularly in fine-tuning Large Language Models (LLMs).
Answer:
Working of the Code (Step-by-Step Execution Process)   04
The code uses the spaCy library to perform token-level Named Entity
Recognition (NER).
Step 1: Import Library
import spacy
Imports the spaCy NLP library.
Step 2: Load Pre-trained Model
nlp = spacy.load("en_core_web_sm")
Loads a small English model with NER capability.
Step 3: Define Input Text
text = "Amazon is investing $5 billion in India."
Input sentence containing organization, money, and location entities.
Step 4: Process the Text
doc = nlp(text)
Converts text into a Doc object.
Performs tokenization and entity recognition.
Step 5: Token-Level Entity Extraction
for token in doc:
if token.ent_type_:
print(token.text, token.ent_type_)
********** 25 **********
--- page 26 ---
Iterates through each token in the document.
Checks if the token belongs to a named entity (ent_type_ is not empty).
Prints token text along with its entity label.
Expected Output
The model identifies tokens that belong to named entities:
Amazon ORG
$ MONEY
5 MONEY
billion MONEY
India GPE
03
Explanation:
• Amazon → ORG (Organization)
• $ 5 billion → MONEY (split into tokens)
•   India → GPE (Geopolitical Entity)
Real-World Application in LLM Fine-Tuning
a. Token-Level Annotation for Training   03
Provides fine-grained labels for each token.
Useful in training transformer-based LLMs like BERT, where token-
level classification is important.
b. Financial and Business Text Analysis
Extracts monetary values and organizations.
Can be used to build datasets for financial LLMs.
c. Improving Information Extraction Systems
Helps create labeled datasets for:
Entity recognition tasks
Document classification
Automated report generation
d. Enhancing Model Accuracy
Token-level annotations help models learn precise boundaries of entities.
Improves performance in tasks like:
Named Entity Recognition
Relation Extraction
e. Domain-Specific Fine-Tuning
Example:
Finance: Detect investments and amounts
News: Identify companies and locations
Leads to better contextual understanding in specialized LLMs.
The code demonstrates token-level entity extraction, which provides
more granular information compared to span-level extraction. This level
of detail is highly valuable for fine-tuning LLMs, enabling improved
accuracy in tasks such as entity recognition, financial analysis, and
domain-specific NLP applications.
********** 26 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper ab25f58ac78e

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Generative AI with Large Language Models /ANS_Generative AI with Large Language Models (703DB0C061)_2024-2025.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Generative AI with Large Language Models
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 17 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-2;   a.   Differentiate between Generative and Descriptive AI.   [05]
BL-2
Explain the computational challenges encountered during the pre-training of
CO-1; SO-2;   b. large language models (LLMs).   [05]
BL-2
Pre-training LLMs requires significant computational resources and presents
several challenges:
• High Computational Cost: Requires massive GPU/TPU clusters for
training.
• Memory Requirements: Training large models demands extensive
memory due to billions of parameters.
********** 1 **********
--- page 2 ---
•   Training Time: Can take weeks or months to pre-train an LLM from
scratch.
• Energy Consumption: High energy usage makes training expensive
and raises environmental concerns.
•   Optimization Complexity: Finding optimal hyperparameters like
learning rates and batch sizes is difficult.
• Data Quality & Bias: Poor-quality or biased data can affect model
performance and fairness.
CO-2; SO-2;   c. How does multi-task instruction fine-tuning differ from conventional fine-   [05]
BL-3   tuning?
CO-3; SO-2;   d. What are the major challenges in obtaining high-quality human feedback for   [05]
BL-4   RLHF?
ANSWER:
Reinforcement Learning from Human Feedback (RLHF) relies on human
annotations to improve model alignment. However, obtaining high-quality
feedback is challenging due to:
1. Subjectivity & Bias:
•   Different annotators have varied opinions, leading to
inconsistent labels.
•   Cultural and personal biases can affect judgments.
2. Scalability Issues:
• Labelling large datasets manually is time-consuming and
expensive.
• Recruiting and training expert annotators requires resources.
3. Ambiguity in Feedback:
• Some tasks lack a single correct answer, making evaluation
difficult.
• Ambiguous instructions can lead to misinterpretation.
4. Overfitting to Human Preferences:
• The model may reinforce mainstream views while neglecting
minority perspectives.
•   It may prioritize engagement over factual accuracy.
5. Fatigue and Annotation Errors:
********** 2 **********
--- page 3 ---
• Annotators may become fatigued, reducing the quality of
feedback.
•   Inconsistent feedback can misguide the reinforcement
learning process.
Mitigation Strategies:
• Use diverse annotators to reduce bias.
• Implement consistency checks to validate human feedback.
• Use automated evaluation techniques (e.g., adversarial testing) to
supplement human feedback.
Q2   Explain In-Context Learning. Describe Inference Types of In-Context
CO-1; SO-2;   a.   learning: Zero Shot, One Shot and Few Shot Inferences. Discuss them by   [10]
BL-2   taking some examples.
ANSWER:
Explanation of In-Context Learning (ICL)
In-Context Learning (ICL) is a method in which Large Language Models
(LLMs) make predictions based on examples provided within the prompt
itself, without updating their internal parameters. Instead of fine-tuning the
model on a dataset, users supply demonstrations as part of the input text,
allowing the model to infer patterns and generate relevant outputs.
Types of In-Context Learning Inferences
1. Zero-Shot Inference
•   In zero-shot learning, the model makes predictions without any prior
example or context.
•   It relies solely on pre-trained knowledge.
• Example:
Prompt: Translate "Bonjour" into English.
Output: Hello
2. One-Shot Inference
•   In this approach, the model is given one example before making a
prediction.
• This helps provide guidance on how to structure the response.
• Example:
Prompt:
Example: "Hola" → "Hello"
Translate "Bonjour" into English:
Output: Hello
3. Few-Shot Inference
********** 3 **********
--- page 4 ---
• The model is provided with multiple examples before making a
prediction.
• This improves accuracy and helps the model learn patterns.
• Example:
Prompt:
Example: "Hola" → "Hello"
Example: "Merci" → "Thank you"
Translate "Bonjour" into English:
Output: Hello
Comparison and Use Cases
Inferen   Explanation   Best Use Case
ce Type
Zero-   No prior examples;   General queries, common
Shot   relies on pre-trained   knowledge tasks
knowledge
One-   Given one example for   Tasks with a clear pattern but
Shot   guidance   little ambiguity
Few-   Multiple examples for   Complex reasoning tasks,
Shot   better context   language translation,
understanding   sentiment analysis
By leveraging In-Context Learning, LLMs can adapt to different tasks
dynamically without the need for fine-tuning, making them highly flexible
and powerful in real-world applications.
Q2   What is BLEU, and how is it used to evaluate the quality of machine-
CO-2; SO-2;   b. generated text? Explain the calculation of BLEU using an example where   [10]
BL-4   the reference sentence is:
"The cat is sitting on the mat"
and the candidate sentence is:
"The cat is resting on the mat".
Compute the unigram and bigram precision and determine the BLEU score.
Comment on the quality of the candidate sentence based on the BLEU score
and comment.
ANSWER:
(i) Calculate Unigram and Bigram Precision:
• Reference Sentence: "The cat is sitting on the mat."
• Candidate Sentence: "The cat is resting on the mat."
Step 1: Unigram Precision
Unigrams (individual words) in the reference:
{The, cat, is, sitting, on, the, mat}
Unigrams in the candidate:
{The, cat, is, resting, on, the, mat}
********** 4 **********
--- page 5 ---
Matching unigrams: {The, cat, is, on, the, mat} (6 out of 7)
Unigram Precision=Matching Unigrams/Total Unigrams in Candidate
=6/7≈0.857
Step 2: Bigram Precision
Bigrams (two-word sequences) in the reference:
{"The cat", "cat is", "is sitting", "sitting on", "on the", "the mat"}
Bigrams in the candidate:
{"The cat", "cat is", "is resting", "resting on", "on the", "the mat"}
Matching bigrams: {"The cat", "cat is", "on the", "the mat"} (4 out of 6)
Bigram Precision=Matching Bigrams/Total Bigrams in Candidate
=4/6≈0.667
(ii) Compute BLEU Score:
(iii) Analysis:
• The BLEU score of 0.756 suggests a high similarity between the
candidate and reference sentences.
• The unigram precision is high, meaning most individual words
match, but the bigram precision is lower due to the difference in
"sitting" vs. "resting."
• The candidate sentence preserves the meaning of the reference but
uses a synonym ("resting" instead of "sitting").
• BLEU measures surface similarity and may not fully capture
semantic correctness.
Q3   Explain the role of quantization in training and deploying large language models
CO-1; SO-2;   a. (LLMs). How do different precision formats like FP32, FP16, BFLOAT16, and   [10]
BL-2   INT8 impact memory usage and performance? Provide examples.
ANSWER:
********** 5 **********
--- page 6 ---
1. What is Quantization?
• A technique to reduce the memory footprint and computational
cost of models.
•   Converts higher-precision floating-point numbers (FP32) into
lower-precision formats (FP16, BFLOAT16, INT8) while
maintaining model accuracy.
2. Comparison of Precision Formats:
• FP32 (Single Precision Float):
▪ 32 bits, high accuracy, but requires 4 bytes per value,
making it memory-intensive.
• FP16 (Half Precision Float):
▪ 16 bits, needs 2 bytes per value, but has reduced exponent
range (5-bit exponent).
▪ Used in mixed precision training for faster computation.
• BFLOAT16 (Brain Floating Point 16):
▪ 16 bits but retains 8-bit exponent (like FP32).
▪ Used in TPUs and AI accelerators for high-performance
training.
• INT8 (Integer 8-bit):
▪ Needs 1 byte per value, ideal for inference to save memory
and improve latency.
3. Impact on LLMs like FLAN-T5 & GPT Models:
•   Training Phase:
▪ Mixed Precision (FP16, BFLOAT16) reduces memory by
~50% while maintaining accuracy.
•   Inference Phase:
▪ INT8 quantization speeds up processing and saves
memory for real-time applications.
4. Example Use Cases:
• NVIDIA’s TensorRT uses INT8 quantization for optimized
inference.
Google’s TPUs use BFLOAT16 for training FLAN-T5 and other transformer
models.
Q3   Evaluate the effectiveness of PEFT methods like LoRA in optimizing the
CO-2; SO-2;   b. efficiency of large language models? Explain with calculations and discuss
BL-5   their impact on performance and scalability.
[10]
ANSWER:
Introduction
Parameter-Efficient Fine-Tuning (PEFT) is a technique that allows fine-
tuning large language models (LLMs) with minimal computational
resources. One of the most effective PEFT methods is Low-Rank
Adaptation (LoRA), which optimizes fine-tuning by introducing trainable
low-rank matrices instead of modifying the full model.
How LoRA Works
Fine-tuning large models requires updating billions of parameters, which is
resource-intensive. LoRA reduces this cost by keeping the pre-trained
model frozen and injecting smaller trainable matrices into specific layers.
These low-rank matrices are trained while the original model weights
remain unchanged, reducing computational complexity.
********** 6 **********
--- page 7 ---
Mathematical Explanation
1. Standard Fine-Tuning: Updates the full weight matrix W   (size: d
× k) for each layer.
2. LoRA Fine-Tuning: Decomposes the weight update into two low-
rank matrices A (d × r) and B (r × k) such that:
W′=W+AB
Here, r is much smaller than d and k, reducing the number of
trainable parameters.
Example Calculation
Consider an LLM with W of size 1024 × 4096 (4.1M parameters). If we set
r = 8, then:
• Matrix A: 1024 × 8
• Matrix B: 8 × 4096
•   Total parameters trained = (1024 × 8) + (8 × 4096) = 32,768
This is significantly lower than 4.1 million, reducing memory usage while
maintaining efficiency.
Impact on Performance and Scalability
• Memory Efficient: LoRA significantly reduces the memory footprint
compared to full fine-tuning.
•   Faster Training: Since fewer parameters are updated, training is
faster.
•   Reusability: LoRA enables task-specific adaptation while keeping
the base model unchanged.
LoRA is a lightweight fine-tuning method that enables efficient adaptation
of LLMs without modifying the entire model. This makes it ideal for low-
resource environments while maintaining high performance.
Q4   Explain the different stages involved in the Generative AI life cycle using a
CO-1; SO-2;   a.   well-labelled sketch. Describe each stage in detail with relevant examples.   [10]
BL-4
ANSWER:
Generative AI Life Cycle
The Generative AI Life Cycle consists of multiple stages that guide the
development, deployment, and improvement of AI models. Below is a
labelled sketch followed by a detailed explanation of each stage.
********** 7 **********
--- page 8 ---
Labelled Sketch of the Generative AI Life Cycle
+--------------------------------------+
|   1. Problem Definition   |
+--------------------------------------+
↓
+--------------------------------------+
|   2. Data Collection & Preprocessing |
+--------------------------------------+
↓
+--------------------------------------+
|   3. Model Selection & Training   |
+--------------------------------------+
↓
+--------------------------------------+
|   4. Fine-Tuning & Optimization   |
+--------------------------------------+
↓
+--------------------------------------+
|   5. Evaluation & Testing   |
+--------------------------------------+
↓
+--------------------------------------+
|   6. Deployment & Integration   |
+--------------------------------------+
↓
+--------------------------------------+
|   7. Monitoring & Continuous Improvement
|
+--------------------------------------+
1. Problem Definition
Objective: Identify the specific use case for which the AI model will be
built.
• Define goals, constraints, and expected outcomes.
•   Identify whether generative AI is suitable for the problem.
Example:
•   Creating an AI model to generate realistic human faces for game
development.
• Developing a text summarization model for legal documents.
2. Data Collection & Preprocessing
Objective: Gather and prepare data for training.
•   Sources: Public datasets, web scraping, APIs, or synthetic data.
********** 8 **********
--- page 9 ---
•   Processing: Cleaning, filtering, normalizing, tokenizing (for text),
and augmentation (for images).
Example:
• Text Generation: Collect books, articles, and conversations to train a
language model.
• Image Generation: Use datasets like CelebA for face generation.
3. Model Selection & Training
Objective: Choose the best AI model architecture and train it on the dataset.
• Types of Models:
• Transformers (GPT, BERT) for text generation.
• GANs (Generative Adversarial Networks) for image
synthesis.
• VAEs (Variational Autoencoders) for anomaly detection.
•   Training requires high computational resources (GPUs/TPUs).
Example:
• Using GPT-4 for AI-generated articles.
•   Training StyleGAN for creating realistic human faces.
4. Fine-Tuning & Optimization
Objective: Improve the model’s performance with task-specific training.
•   Fine-tuning involves training the model on domain-specific data.
•   Optimization techniques include Parameter Efficient Fine-Tuning
(PEFT), LoRA, and Soft Prompts.
Example:
•   Fine-tuning ChatGPT on medical conversations for healthcare
applications.
• Optimizing an AI art generator to produce anime-style images.
5. Evaluation & Testing
Objective: Measure model accuracy and generalization.
•   Evaluation Metrics:
• BLEU, ROUGE for text generation.
• FID (Fréchet Inception Distance) for image generation.
•   Perplexity Score for language models.
Example:
•   Testing a summarization model using the ROUGE score to compare
generated summaries with human-written summaries.
********** 9 **********
--- page 10 ---
•   Evaluating a speech synthesis model using WER (Word Error Rate).
6. Deployment & Integration
Objective: Deploy the trained model for real-world applications.
• Deploy models via APIs, cloud services, or edge devices.
•   Tools: Hugging Face, TensorFlow Serving, ONNX, AWS, or Azure
AI.
Example:
• Deploying an AI chatbot in customer service applications.
•   Integrating a text-to-image model in a design tool
7. Monitoring & Continuous Improvement
Objective: Track model performance and refine it over time.
• Monitor user feedback, bias, drift, and security risks.
•   Retrain models periodically with updated data.
Example:
• Updating a fraud detection model as fraud patterns evolve.
• Monitoring bias in an AI hiring tool and improving fairness.
The Generative AI Life Cycle is an iterative process where models are
continuously trained, optimized, deployed, and monitored. By following this
structured approach, organizations can build scalable, ethical, and high-
performing AI applications.
Q4   Explain in brief about the working of Transformers by using the sketch of it.
CO-1; SO-2;   b. Also explain in detail the process of Tokenization and embedding.   [10]
BL-3
ANSWER:
Working of Transformers (Brief Explanation)
Transformers are deep learning architectures designed for handling
sequential data, particularly in Natural Language Processing (NLP) tasks.
They rely on self-attention mechanisms instead of recurrent or convolutional
layers, allowing them to process input sequences in parallel.
Components of a Transformer:
1. Input Tokenization: Converts text into numerical tokens.
2. Embedding Layer: Maps tokens to dense vectors.
3. Positional Encoding: Adds positional information since transformers
lack recurrence.
********** 10 **********
--- page 11 ---
4. Multi-Head Self-Attention: Captures relationships between words
regardless of their distance.
5. Feedforward Neural Network: Processes attention output to refine
representations.
6. Layer Normalization & Residual Connections: Help stabilize
training.
7. Final Output Layer: Produces predictions such as translated text or
next-word suggestions.
Sketch of Transformer Architecture
The following diagram illustrates a simplified transformer architecture with
encoder-decoder layers:
Tokenization (Detailed Explanation)
Tokenization is the process of converting text into smaller units (tokens)
that a model can process.
Types of Tokenization:
1. Word Tokenization: Splits text into words.
• Example: "Transformers are amazing" →
["Transformers", "are", "amazing"]
2. Subword Tokenization (Byte Pair Encoding - BPE): Splits words
into frequent subwords.
• Example: "Transformers" → ["Trans",
"former", "s"]
3. Character Tokenization: Splits text at the character level.
• Example: "AI" → ["A", "I"]
4. SentencePiece Tokenization: Used in models like BERT and GPT,
encoding both words and subwords.
Example (Python Implementation using Hugging Face's Tokenizer)
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-
base-uncased")
tokens = tokenizer.tokenize("Transformers are
powerful!")
print(tokens)
Output: ['transformers', 'are', 'powerful', '!']
Embedding
Once text is tokenized, each token is mapped to a dense vector
representation.
Types of Embeddings:
1. One-Hot Encoding:
********** 11 **********
--- page 12 ---
• Represents words as binary vectors.
•   Inefficient for large vocabularies.
2. Word Embeddings (Word2Vec, GloVe):
• Maps words to dense vectors based on meaning.
3. Contextual Embeddings (BERT, GPT):
• Embeddings change based on context.
Example of Word Embedding:
Word   | Embedding Vector
------------------------------
"cat"   | [0.23, 0.45, 0.12, 0.67, ...]
"dog"   | [0.21, 0.48, 0.10, 0.65, ...]
Mathematical Representation:
For a given token t, the embedding function E(t) maps it to a high-
dimensional vector space.
E(t)=[x1,x2,...,xn]
Example (Python Implementation using Word2Vec in Gensim)
from gensim.models import Word2Vec
sentences = [["transformers", "are", "powerful"],
["NLP", "is", "exciting"]]
model = Word2Vec(sentences, vector_size=10,
min_count=1)
print(model.wv["transformers"]) # Get embedding
for "transformers"
Positional Encoding:
Since transformers don't use recurrence, Positional Encoding is added to
embeddings to retain word order. It is computed as:
•   Tokenization breaks text into meaningful units.
• Embedding represents tokens in dense numerical form.
• Transformers use self-attention and embeddings to generate context-
aware outputs.
Q5
CO-3; SO-2;   a. What is reward hacking in RLHF, and how can an agent exploit flaws or   [10]
BL-4   loopholes in the reward function? Provide an example with a supporting
sketch.
ANSWER:
********** 12 **********
--- page 13 ---
Reward hacking in RLHF occurs when an agent exploits flaws in the reward
function to maximize rewards in unintended ways. Instead of genuinely
improving the model’s performance, the agent finds a way to game the
system by optimizing for the reward signal without aligning with the actual
goal.
Example:
•   Initially, the Instruct LLM responds with a negative statement:
“...complete garbage.” This receives a low toxicity reward of -1.8
(Iteration 1).
•   In the next iteration, the model modifies its response to “okay but
not the best,” which is slightly less toxic, leading to an improved
reward score of 0.3 (Iteration 2).
•   Further training encourages the model to generate overly positive
responses, like “..the most awesome, most incredible thing ever.”
This response receives a higher reward of 2.1 (Iteration 3).
•   Ultimately, the model exploits the reward system by generating
unrealistic, exaggeratedly positive responses such as “Beautiful love
and world peace all around.” with a 3.7 reward score (Iteration n),
even if the response is unrelated to the actual product.
Explanation:
1. The model learns to optimize its outputs for the toxicity reward
model, rather than providing balanced and honest feedback.
2. This demonstrates reward hacking, where the model generates
excessively positive and unrealistic responses to maximize the
reward.
3. The agent is misaligned with human intent, as the goal is to generate
useful product descriptions, not overly generic, exaggerated praise.
Thus, reward hacking occurs when the model exploits the reward function
instead of truly improving its responses.
Q5   How does chain-of-thought reasoning help LLMs improve their
CO-4; SO-2;   b. planning and decision-making capabilities? Provide an example   [10]
BL-4
where chain-of-thought reasoning enhances the accuracy of an
LLM’s response.
ANSWER:
Chain-of-thought (CoT) reasoning allows LLMs to break down complex
problems into intermediate reasoning steps, improving accuracy and logical
consistency.
Benefits of CoT Reasoning:
• Encourages step-by-step breakdowns for complex queries.
• Reduces hallucinations by verifying each step.
********** 13 **********
--- page 14 ---
• Mimics human problem-solving methods.
Example: Word Problem Solving
Question: "If John has 3 apples and buys 5 more, then gives away 2, how
many does he have left?"
Without CoT:
• "John has 6 apples" (Incorrect).
With CoT:
1. John starts with 3 apples.
2. He buys 5 more: 3 + 5 = 8.
3. He gives away 2: 8 - 2 = 6.
4. Final answer: 6 apples.
This structured approach improves accuracy and reasoning.
Q6   What are the key components of an LLM application architecture? How do
CO-4; SO-2;   a. LLMs interact with external applications to enhance their functionality?   [10]
BL-4   Provide an example.
Answer:
Components of an LLM Application Architecture:
1. User Interface (UI): Enables users to interact with the LLM-powered
application.
2. Orchestration Layer: Manages input processing, API calls, and
response generation.
3. LLM Model: The core model that generates text-based outputs.
4. External Data Sources: Databases, APIs, or documents providing
relevant information.
5. Retrieval-Augmented Generation (RAG): Enhances responses by
retrieving real-time data.
6. Security & Monitoring: Ensures safe and optimized interactions.
Interaction with External Applications:
LLMs integrate with APIs, databases, and external tools to enhance their
responses. This connection improves accuracy, updates real-time
information, and ensures contextual relevance.
Example:
A customer support chatbot using an LLM can connect to an e-commerce
database via APIs. When a user asks about order status, the chatbot retrieves
real-time tracking details and provides accurate responses instead of
generating a generic reply.
********** 14 **********
--- page 15 ---
Q6   Evaluate the effectiveness of the reward model in Reinforcement Learning
CO-3; SO-2;   b. from Human Feedback (RLHF) by analyzing how pairwise ranking loss   [10]
BL-5   influences preference assignment. Given the reward values:
Given the reward values:
• Response X: R(X) = 2.5
• Response Y: R(Y) = 1.2
• Response Z: R(Z) = −0.5
(i) Calculate the probability that response A is preferred over B using the
sigmoid function:
P(X>Y) =σ(RX−RY) = 1/ (1+e−( RX−RY))
(ii) Calculate the probability that response Y is preferred over Z using the
same formula.
(iii) Aanalyze how the reward values are learned and optimized during the
training process to enhance model performance.
(iii) Interpretation of results:
• The probability of choosing X over Y is 87%, indicating that X is
strongly preferred.
• The probability of choosing Y over Z is 83.2%, meaning Y is also
significantly better than Z.
********** 15 **********
--- page 16 ---
•   Since X has the highest probability, it is considered the most
preferred response, followed by Y, and Z is the least preferred.
Q7   Analyze how the ReAct (Reasoning + Action) framework enhances
CO-4; SO-2;   a. decision-making in LLM-powered applications. Evaluate its effectiveness   [10]
BL-5   by illustrating a real-world scenario where an LLM interacts with an
external application using ReAct.
ANSWER:
ReAct (Reasoning + Action) is a framework that enables large language
models (LLMs) to reason step-by-step while also performing actions, such
as interacting with APIs or external applications. Unlike traditional LLM
approaches, which either generate direct answers or rely on external tools
passively, ReAct allows models to dynamically integrate reasoning with
action execution.
How ReAct Works:
1. Reasoning: The LLM thinks through the problem, breaking it into
logical steps.
2. Action: Based on reasoning, the LLM interacts with external
applications (e.g., search engines, databases, APIs).
3. Observation: The LLM processes the external feedback and updates
its reasoning.
4. Iteration: Steps 1-3 repeat until a final answer is reached.
Example: LLM Using ReAct for Weather Prediction
Scenario: A user asks, "What will the temperature be in New York
tomorrow?"
•   Step 1 (Reasoning): The LLM determines that it needs real-time
weather data.
•   Step 2 (Action): The LLM calls a weather API:
fetch_weather("New York", "tomorrow").
•   Step 3 (Observation): The API returns {"temperature": 22°C,
"condition": "Sunny"}.
•   Step 4 (Final Response): The LLM responds, "The expected
temperature in New York tomorrow is 22°C with sunny weather."
Thus, ReAct enables LLMs to enhance decision-making by dynamically
combining reasoning and action execution.
Q7   Explain the given code snippet, provide the expected output, and identify its
CO-2; SO-2;   b. real-world application in LLM fine-tuning.   [10]
BL-3
********** 16 **********
--- page 17 ---
ANSWER:
The given Python code uses the spaCy library to perform Named Entity
Recognition (NER) on a sentence. Here's a step-by-step breakdown:
1. Import spaCy – The spacy library is imported.
2. Load Pre-trained Model – The en_core_web_sm model is loaded,
which is a small English NLP model.
3. Define a Text String – A sample sentence is provided:
"Sundar Pichai is the CEO of Google, which is based in Mountain
View, California."
4. Process the Text – The text is passed through nlp(), which
tokenizes it and performs NLP tasks.
5. Extract Named Entities – A loop iterates over the recognized named
entities (doc.ents), printing their text and assigned entity label.
Expected Output:
The output will display the detected named entities and their corresponding
labels:
Sundar Pichai -> PERSON
Google -> ORG
Mountain View -> GPE
California -> GPE
NER
This snippet demonstrates Named Entity Recognition (NER), which is an
essential component of LLM fine-tuning for various applications.
********** 17 **********
````
