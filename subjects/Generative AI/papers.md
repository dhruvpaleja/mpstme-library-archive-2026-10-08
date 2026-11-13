# Generative AI: question papers in full

10 unique papers · 2025-26 to 2025-26 · Artificial Intelligence

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 7 · paper dd8938073c9c

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `00_Original_Downloads/SYLLABUS/B TECH/12169__4TH YEAR.zip :: ARTIFICIAL INTELLIGENCE/SEM-VII/GENERATIVE AI/Generative_AI__Sem-VII__Year_2025-2026__Final_Exam_M0ZzvJyKof.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: ocr (4 pages), mean OCR confidence 90.0
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS .
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)

Year: IV/Semester VII(Exam Year: 2025-2026) * »

Subject: GENERATIVE AI

Date: 27 Nov 2025
Max. Marks: 100

Instructions:

1. This question paper contains 4 pages.

2. Answer to eac

3. Figure in right hand side indicates full marks

4. Question No.1

5. Out of remaining questions, attempt any 4 questions.

Time: 10:00 am to 01:00 pm (03:00 Hrs.)

FINAL EXAMINATION (Acad. Year:2025-2026)

.

h new question to be started on a fresh page.

is compulsory.

6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data wherever necessary.

vl Answer briefly:
CO-1; | a. Compare GANs, VAEs and Diffusion models with respect to the following aspects: [5]
BL-4 Concept used for generation, Training stability, sample quality, strengths and
disadvantages.
CO-3; |b. F F ae F : : : [5]
When using Locality Sensitive Hashing (LSH), two policy-related shingle sets (unique
BL-3 terms) are extracted from different documents:
Cl1= {policy, compliance, risk, audit, KYC, AML}
C2= {risk, audit, KYC, onboarding, sanctions, AML}
i. Compute the true Jaccard similarity J(C1, C2)
ii. Compute the true Jaccard distance D(C1, C2)
iii. In a practical LSH system, how is the similarity checked? Explain briefly.
CO-2; |c. i. Justify the significance of masked SoftMax [5]
BL-3 ii. Given the following logits (scores) for a query-key interaction:
Logits= [3.0, —2.0,2.0, -1.0]
And a mask vector, where 1 means the position is valid and 0 means the position
should be ignored:
Mask= [1,0,1,0]
Apply a masked SoftMax operation to the logits.
CO-2; |d. You are given a reference and a candidate summary (case-insensitive, whitespace [5]
BL-4 tokenization):

Reference: the committee approved the budget last week
Predicted: the committee unanimously approved budget last month

Compute the following (show formulas and brief working):

i.
il.
iii.

ROUGE-1: Compute precision, recall, and F1 using unigram overlap.
ROUGE-2 Compute precision, recall, and F1 using bigram overlap.
ROUGE-L: Given LCS length = 5, compute precision, recall, and F1 for
ROUGE-L using the LCS-based definitions.

--- page 2 ---
Q2

CO-2; | a. With respect to GPT 1 model, answer the following questions: ; [10]
BL- i. Explain the unsupervised pre-training used in GPT 1. |
2,3 ii. Briefly outline how GPT-1 was fine-tuned for supervised tasks using task

specific transformations. Give examples for at least two tasks. Me
iii. Justify the use of masked self-attention used to enforce left-to-right generation

in GPT 1.
CO-3; | b. A global research team needs a unified semantic search over a read-only corpus of 200k | [10]
BL-4 research PDFs (updated weekly). Queries are free-text, often cross- lingual

(English/Hindi/Spanish) and may include image-caption text extracted from figures.
There are no exact ID lookups, no transactional updates, and only lightweight metadata
filters (year, domain) and results must return top-k passages with source citations (doc +
page).

i. Suggest a database for this application (traditional database or vector database)
highlighting with three reasons about your choice.

ii. Design a search solution for the research team. Your solution should highlight the
following points: ae)

* the embedding model(s) you’d choose (unimodal/multimodal) and why,

¢ the index type and two key parameters you’d tune for latency/recall,

¢ how you'd store and use metadata (year/domain) for filtered ANN queries,
e the retrieval workflow and how you’ll surface citations.

Q3
CO-3; | a. i. Compare Hierarchial Navigable Small World (HNSW) and Locality Sensitive [10]
BL-3 Hashing (LSH) algorithms used in indexing in vector databases.

ii. You are given a single-layer HNSW graph (only the bottom layer is shown).
Edge cap per node M=2. Use Euclidean distance. Search uses etSeash = 3 and
returns top-k = 2 neighbors. Start from entry node A.

The node coordinates are:

A(0,0), B(1,0), C(0,1), D(1,1), E(2,0), F(2,1)
Undirected edges (respecting M=2)
AoB,A@eC
BoD,BoE
CoD ‘

DoF
EoF

e The Query(q) is (1.6, 0.3).

« Compute the distances d(q,x) for all nodes x€ {A,B,C,D,E,F.

¢ Run the HNSW best-first search on this layer with efSearch=3, starting at A.

* Maintain a candidate (min-heap) and a result set WWW (size up to efSearch).

¢ Expand nodes in order of increasing distance; when you pop a node, push any
unvisited neighbors with their distances (avoid revisits).

¢ Stop when the nearest candidate in the queue is farther than the worst item in
W.

¢ Write the visit order and thetfinal contents of W (node, distance).

e Report the top-2 neighbors (node names) returned to the user.

¢ Predict how the answer might change if efSearch were increased to 10 (no need
to recompute).

FOI Rk
--- page 3 ---
>

‘| CO-2; b. | With reference to GPT 3 model, answer the following: [10]

BL- iii. Define in-context learning in GPT-3. Contrast it with parameter fine-tuning, and
2,3 give one situation where ICL is preferable. f
iv. Design a few-shot prompt that makes GPT-3 classify short reviews as {Positive,
Neutral, Negative}. -   e
Requirements: _

e Include two labeled examples in the prompt (few-shot).

e Add an instruction that the output must be exactly one of the three labels.

e Provide the final prompt text you would send (<8 lines total).

e Discuss limitations of GPT-3 like prompt sensitivity, hallucination, bias
when used in zero/few-shot mode. ~

Q4

CO-3; a. i. Briefly explain Contrastive Language Image Pretraining (CLIP’s) dual- [10]
BL-4 encoder architecture (image encoder + text encoder) and how its contrastive
loss is applied over an image-text batch to align modalities.
ii. Design a simple image search and retrieval pipeline using CLIP.
iii. Briefly explain the limitations of CLIP in real deployments.
iv. You use CLIP for zero-shot classification with class prompts.

a. For an image, the cosine similarities to prompts are: “a photo of a cat” = 0.58,
“a photo of a dog” = 0.56, “a photo of a fox” = 0.47. Which label is predicted,
and why?

b. If you change the template to “an image of a {label}” and the order of labels
in the prompt set, explain in 2-3 sentences how this can alter the scores
(prompt sensitivity) and name one mitigation you would apply.

CO-3; b. i. Compare LangChain and Llamalndex. : [10]
BL- ii. | Given a knowledge base of PDFs, outline the flow of steps for a basic RAG flow

24 using Llamalndex framework. ;

iii. | Explain context augmentation with reference to Llamalndex.

Q5

CO-3; a. i. Compare Simple Retrieval Augmented Generation (RAG) and advanced RAG. [10]
4 ii. A company is building a regulatory-compliance assistant for a multinational bank.
The knowledge base contains versioned policy PDFs (hundreds of pages), FAQ
wikis, and incident reports. Queries arrive in English and Hindi, often vague
(“What’s the large-cash deposit limit in Q4 for APAC?”) and sometimes
contradictory (users paste old screenshots). The system must return grounded
answers with section-level citations, prefer the latest effective version of a policy,
and keep p95 latency < 1.2s.
e Suggest an advanced RAG stack for this assistant.
¢ Highlight the significance of each step in advanced RAG with respect to this
— assistant.
‘ CO-4; b. i. Briefly explain the forward diffusion process in Denoising Diffusion Probabilistic | [10]
5 BL-2 Models (DDPM).
. li. Compare Hierarchical VAE and DDPMs.
7 " iii. What is the ELBO connection irr DDPM training?

FICK Fr

i
--- page 4 ---
Q6

a. |i. CNNs and LVMs are both used for computer vision applications. Compare their | [10]
CO-2; performance for these applications.
BL-2 ii. Consider a ViT using 16x16 patches on a 256x256 RGB image. ~~...
a. Compute the number of patches N. ;
b. Compute the flattened patch vector dimension.
c. If a [CLS] token is prepended, what is the Transformer input sequence
length?
iii. How do the results on ViT compare with that of ResNet?
iv. Briefly describe token-based distillation in DeiT. What extra token is imtroduced,
what supervision it receives, and why this helps data-efficient training compared to
vanilla ViT.

CO-5; b. [10]
BL- i. A model assigns probabilities to a 3-token reference [ 0.5, 0.25, 0.125]. Compute
2.3 cross-entropy (bits/token) and perplexity.

, ii. Given the pros and cons of automated vs. human evaluations, hybrid approaches
seek to get the best of both worlds. In practice, most LLM evaluation setups are
hybrid to some extent.

a. Briefly explain the different hybrid approaches that are used in practice.
b. Give a scenario where this hybrid approach can be used.

Q7

CO-6; | a. Define Agentic AI in one or two sentences and name two traits that distinguish it froma | [5]
BL-2 plain LLM. Give two examples where a tool call is essential and pure LLM text
generation would fail.

CO-1; | b. A company has a 30-page compliance policy updated quarterly. They need concise, [5]
BL-4 accurate 200-word summaries for executives. .
e Outline a two-stage pipeline (chunking and synthesizing) specifying chunk size,
overlap, and how you’ll handle cross-section references.
e Draft a crisp prompt to get the 200-word summary.
e Suggest an evaluation metric for this.

or,
CO-S5; | c i. Describe briefly hit rate. [5]
BL-3 ii. You have 4 queries with the single correct node per query:

* Gold: QI--N3, Q2-3N7, Q3-N2, Q4N5
e Retrieved@3:

o QI: [N8, N3, N1]

o Q2: [N4, N6, N2]

o Q3: [N2, N9, N7]

o =Q4: [N5, N3, N8]

Compute HitRate@3 over the 4 queries.

+ iii. What are the challenges with hit rate as a metric?

CO-6; | d iv. Contrast “reactive prompting” vs. “deliberate planning” in agents. [5]
BL-2 v. State two ethical risks unique to autonomous agents vs. chat LLMs.

FIG 7 aC Gk ak kk
````

## 2025-26 · Final-Exam · Sem 7 · paper ab76329a26c5

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AI_7012/GENERATIVE AI/QP_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: GENERATIVE AI
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data wherever necessary.
Q1   Answer briefly:
CO-1;   a.   Compare GANs, VAEs and Diffusion models with respect to the following aspects:   [5]
BL-4   Concept used for generation, Training stability, sample quality, strengths and
disadvantages.
CO-3; b.   When using Locality Sensitive Hashing (LSH), two policy-related shingle sets (unique   [5]
BL-3   terms) are extracted from different documents:
C1= {policy, compliance, risk, audit, KYC, AML}
C2= {risk, audit, KYC, onboarding, sanctions, AML}
i. Compute the true Jaccard similarity J(C1, C2)
ii. Compute the true Jaccard distance D(C1, C2)
iii. In a practical LSH system, how is the similarity checked? Explain briefly.
CO-2; c.   i.   Justify the significance of masked SoftMax   [5]
BL-3   ii.   Given the following logits (scores) for a query-key interaction:
Logits= [3.0, −2.0,2.0, −1.0]
And a mask vector, where 1 means the position is valid and 0 means the position
should be ignored:
Mask= [1,0,1,0]
Apply a masked SoftMax operation to the logits.
CO-2; d.   You are given a reference and a candidate summary (case-insensitive, whitespace   [5]
BL-4   tokenization):
• Reference: the committee approved the budget last week
•   Predicted: the committee unanimously approved budget last month
Compute the following (show formulas and brief working):
i.   ROUGE-1: Compute precision, recall, and F1 using unigram overlap.
ii. ROUGE-2 Compute precision, recall, and F1 using bigram overlap.
iii.   ROUGE-L: Given LCS length = 5, compute precision, recall, and F1 for
ROUGE-L using the LCS-based definitions.
********** 1 **********
--- page 2 ---
Q2
CO-2;   a.   With respect to GPT 1 model, answer the following questions:   [10]
BL-   i.   Explain the unsupervised pre-training used in GPT 1.
2,3   ii. Briefly outline how GPT-1 was fine-tuned for supervised tasks using task
specific transformations. Give examples for at least two tasks.
iii. Justify the use of masked self-attention used to enforce left-to-right generation
in GPT 1.
CO-3;   b.   A global research team needs a unified semantic search over a read-only corpus of 200k [10]
BL-4   research PDFs (updated weekly). Queries are   free-text, often   cross-lingual
(English/Hindi/Spanish) and may include image-caption text extracted from figures.
There are no exact ID lookups, no transactional updates, and only lightweight metadata
filters (year, domain) and results must return top-k passages with source citations (doc +
page).
i.   Suggest a database for this application (traditional database or vector database)
highlighting with three reasons about your choice.
ii. Design a search solution for the research team. Your solution should highlight the
following points:
•   the embedding model(s) you’d choose (unimodal/multimodal) and why,
•   the index type and two key parameters you’d tune for latency/recall,
• how you’d store and use metadata (year/domain) for filtered ANN queries,
•   the retrieval workflow and how you’ll surface citations.
Q3
CO-3;   a.   i. Compare Hierarchial Navigable Small World (HNSW) and Locality Sensitive   [10]
Hashing (LSH) algorithms used in indexing in vector databases.
BL-3
ii. You are given a single-layer HNSW graph (only the bottom layer is shown).
Edge cap per node M=2. Use Euclidean distance. Search uses efSearch = 3 and
returns top-k = 2 neighbors. Start from entry node A.
The node coordinates are:
A(0,0), B(1,0), C(0,1), D(1,1), E(2,0), F(2,1)
Undirected edges (respecting M=2)
A ↔ B, A ↔ C
B ↔ D, B ↔ E
C ↔ D
D ↔ F
E ↔ F
•   The Query(q) is (1.6, 0.3).
•   Compute the distances d(q,x) for all nodes x∈{A,B,C,D,E,F.
• Run the HNSW best-first search on this layer with efSearch=3, starting at A.
•   Maintain a candidate (min-heap) and a result set WWW (size up to efSearch).
•   Expand nodes in order of increasing distance; when you pop a node, push any
unvisited neighbors with their distances (avoid revisits).
•   Stop when the nearest candidate in the queue is farther than the worst item in
W.
•   Write the visit order and the final contents of W (node, distance).
•   Report the top-2 neighbors (node names) returned to the user.
•   Predict how the answer might change if efSearch were increased to 10 (no need
to recompute).
********** 2 **********
--- page 3 ---
CO-2;   b. With reference to GPT 3 model, answer the following:   [10]
BL-   iii. Define in-context learning in GPT-3. Contrast it with parameter fine-tuning, and
2,3   give one situation where ICL is preferable.
iv. Design a few-shot prompt that makes GPT-3 classify short reviews as {Positive,
Neutral, Negative}.
Requirements:
• Include two labeled examples in the prompt (few-shot).
• Add an instruction that the output must be exactly one of the three labels.
• Provide the final prompt text you would send (≤8 lines total).
• Discuss limitations of GPT-3 like prompt sensitivity, hallucination, bias
when used in zero/few-shot mode.
Q4
CO-3;   a.   i.   Briefly explain Contrastive Language Image Pretraining (CLIP’s) dual-   [10]
BL-4   encoder architecture (image encoder + text encoder) and how its contrastive
loss is applied over an image–text batch to align modalities.
ii.   Design a simple image search and retrieval pipeline using CLIP.
iii.   Briefly explain the limitations of CLIP in real deployments.
iv.   You use CLIP for zero-shot classification with class prompts.
a. For an image, the cosine similarities to prompts are: “a photo of a cat” = 0.58,
“a photo of a dog” = 0.56, “a photo of a fox” = 0.47. Which label is predicted,
and why?
b.   If you change the template to “an image of a {label}” and the order of labels
in the prompt set, explain in 2–3 sentences how this can alter the scores
(prompt sensitivity) and name one mitigation you would apply.
CO-3;   b.   i.   Compare LangChain and LlamaIndex.   [10]
BL-   ii.   Given a knowledge base of PDFs, outline the flow of steps for a basic RAG flow
using LlamaIndex framework.
2,4
iii.   Explain context augmentation with reference to LlamaIndex.
Q5
CO-3;   a.   i.   Compare Simple Retrieval Augmented Generation (RAG) and advanced RAG.   [10]
BL-4   ii. A company is building a regulatory-compliance assistant for a multinational bank.
The knowledge base contains versioned policy PDFs (hundreds of pages), FAQ
wikis, and incident reports. Queries arrive in English and Hindi, often vague
(“What’s the large-cash deposit limit in Q4 for APAC?”) and sometimes
contradictory (users paste old screenshots). The system must return grounded
answers with section-level citations, prefer the latest effective version of a policy,
and keep p95 latency < 1.2s.
• Suggest an advanced RAG stack for this assistant.
• Highlight the significance of each step in advanced RAG with respect to this
assistant.
CO-4;   b.   i. Briefly explain the forward diffusion process in Denoising Diffusion Probabilistic   [10]
BL-2   Models (DDPM).
ii. Compare Hierarchical VAE and DDPMs.
iii. What is the ELBO connection in DDPM training?
********** 3 **********
--- page 4 ---
Q6
a.   i. CNNs and LVMs are both used for computer vision applications. Compare their [10]
CO-2;   performance for these applications.
BL-2   ii. Consider a ViT using 16×16 patches on a 256×256 RGB image.
a. Compute the number of patches N.
b. Compute the flattened patch vector dimension.
c.   If a [CLS] token is prepended, what is the Transformer input sequence
length?
iii. How do the results on ViT compare with that of ResNet?
iv. Briefly describe token-based distillation in DeiT. What extra token is introduced,
what supervision it receives, and why this helps data-efficient training compared to
vanilla ViT.
CO-5;   b.   [10]
BL-   i. A model assigns probabilities to a 3-token reference [ 0.5,   0.25,   0.125]. Compute
cross-entropy (bits/token) and perplexity.
2, 3
ii. Given the pros and cons of automated vs. human evaluations, hybrid approaches
seek to get the best of both worlds. In practice, most LLM evaluation setups are
hybrid to some extent.
a. Briefly explain the different hybrid approaches that are used in practice.
b. Give a scenario where this hybrid approach can be used.
Q7
CO-6;   a.   Define Agentic AI in one or two sentences and name two traits that distinguish it from a   [5]
BL-2   plain LLM. Give two examples where a tool call is essential and pure LLM text
generation would fail.
CO-1;   b.   A company has a 30-page compliance policy updated quarterly. They need concise,   [5]
BL-4   accurate 200-word summaries for executives.
• Outline a two-stage pipeline (chunking and synthesizing) specifying chunk size,
overlap, and how you’ll handle cross-section references.
• Draft a crisp prompt to get the 200-word summary.
• Suggest an evaluation metric for this.
CO-5; c   i.   Describe briefly hit rate.   [5]
BL-3   ii. You have 4 queries with the single correct node per query:
• Gold: Q1→N3, Q2→N7, Q3→N2, Q4→N5
• Retrieved@3:
o Q1: [N8, N3, N1]
o Q2: [N4, N6, N2]
o Q3: [N2, N9, N7]
o Q4: [N5, N3, N8]
Compute HitRate@3 over the 4 queries.
iii. What are the challenges with hit rate as a metric?
CO-6; d   iv. Contrast “reactive prompting” vs. “deliberate planning” in agents.   [5]
BL-2   v. State two ethical risks unique to autonomous agents vs. chat LLMs.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 8 · paper 3c3053c4e745

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_AI_7051/GENERATIVE AI/QP_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (ARTIFICIALINTELLIGENCE)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: GENERATIVE AI
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO-2;   a.   Consider the transformer architecture which uses the model embedding dimension:   [5]
BL-3   dmodel = 512, number of heads: h=8
Compute:
i.   The dimension of each head.
ii.   The total concatenated dimension before final projection.
iii.   The shape of the output after the final projection if sequence length is 20.
CO-1;   b.   i. Compare data generation and data classification tasks in AI.   [5]
BL-4   ii. State the key characteristics of Generative AI models.
CO-5;   c. A retriever is tested on 3 queries. The top-5 retrieved relevance labels are:   [5]
BL-3   Q1: [0,1,0,0,1], The total relevant docs for Q1 = 3
Q2: [1,0,0,1,0], The total relevant docs for Q1 = 2
Q3: [0,0,0,1,0], The total relevant docs for Q1 = 4
Compute:
a. Hit Rate across the 3 queries
b. Mean Reciprocal Rank (MRR) across the 3 queries
c. Precision@5 for each query
d. Recall@5 for each query
e. average Precision@5 and average Recall@5
********** 1 **********
--- page 2 ---
CO-3;   d.   Consider Hierarchical Navigable Small World (HNSW) algorithm being implemented   [5]
BL-3   with the two settings as given below:
Setting   M   efConstruction   efSearch
(Max.   (Size of dynamic   (Size of dynamic candidate
connections   candidate list during   list during querying)
per node)   index building)
A   32   200   50
B   64   400   200
Determine:
i.   Which case is expected to give higher recall?
ii.   Which case is expected to use more memory?
iii.   Which case is expected to answer faster?
iv.   Which case is more suitable for real-time production?
v.   Which case is better for research or accuracy-critical tasks?
Q2
CO-2;   a.   i.   Highlight the different steps in building a foundation model.   [10]
BL-   ii. Compare foundation models and large language models.
2,3   iii. Consider a LLM which works on auto regressivity, for a sample x= [1,1,0], the
predicted probabilities are as given below:
p(x1=1) =0.9,
p(x2 =1∣x1)=0.8,
p(x3 = 0∣x1,x2)=0.4
Compute the joint probability.
CO-5;   b.   Consider a reference sentence which is used for benchmarking.   [10]
BL-   Reference: He was happy last night
3,4   Two different LLMs are used and they generate the outputs as given below:
Candidate A: He was extremely happy last night
Candidate B: He was joyful yesterday evening
Using exact matches only:
a. compute ROUGE-1 for Candidate A
b. compute BLEU-1 for Candidate A
c. compute ROUGE-1 for Candidate B
d. compute BLEU-1 for Candidate B
e. Interpret which metric is harsher and why.
Q3
********** 2 **********
--- page 3 ---
CO-3; a.   i.   Show with examples any two types of chunking strategies as used in the   [10]
indexing phase of RAG.
BL-4
ii.   Justify the significance of reranking, filtering, and contextual fusion in
advanced RAG pipelines.
iii.   Analyze why pre-retrieval and post-retrieval processing can improve answer
quality in complex enterprise applications.
CO-2; b.   i. Compare encoder only models and decoder only models in LLMs.   [10]
BL-   ii. Analyze how in-context learning in GPT-3 differs from the earlier GPT models,
3,4   and evaluate its significance for NLP.
iii. A company wants to use GPT-3 for sentiment classification without fine-tuning.
Explain how in context learning can be used for this task, and give an example
prompt with sample input-output pairs.
Q4
CO-3;   a.   Locality Sensitive Hashing (LSH) is used for comparing two document indexes in RAG. [10]
BL-3   • Doc1 = "machine vision"
• Doc2 = "machine revision"
The parameter settings for LSH are:
•   shingle length k=2
• Hash functions:
H1(x)=( x+1) mod 19, H2(x)=(3x+1) mod 19, H3(x)=(4x+2) mod 19
Determine:
1. Set of shingles for both documents
2. Jaccard similarity and distance
3. Characteristic matrix
4. Signature similarity
5. Whether the documents are likely near-duplicates under LSH banding
CO-2;   b.   i. Compare the two LLM frameworks LangChain and LlamaIndex, on the basis of   [10]
BL-   their primary focus, data indexing, use cases and performance.
2,3   ii. Highlight a typical LlamaIndex workflow.
iii. A hospital wants doctors to query clinical documents and reports efficiently.
Briefly explain how LlamaIndex can help in this use case.
Q5
CO-1;   a. Compare image understanding and language generation in multimodal systems.   [5]
BL-2
CO-6;   b.   i.   Differentiate between reactive agents and proactive agents.   [10]
BL-   ii. Explain the terms reactive prompting and deliberate planning in agents.
2,4   iii. A company wants to deploy a travel and expense assistant. Analyze how the
agent should behave in each of the four stages: perceive, plan, act, and reflect.
CO-5;   c.   i.   State and explain any two human evaluation methods used for LLMs.   [5]
BL-2   ii.   Highlight the challenges of human evaluation methods.
Q6
a.   i.   Explain how a Vision Transformer converts an image into a sequence suitable   [10]
for a Transformer encoder.
********** 3 **********
--- page 4 ---
CO-4;   ii.   For a 224×224 RGB image, compute the number of patches and patch vector
BL-   dimension for:
2,3   • P=32
• P=16
• P=14
Which choice gives the longest sequence?
iii.   Analyze when a ViT-based solution would be more suitable than a CNN-based
solution.
CO-4;   b.   i.   Describe how DDPM is trained with a U-Net using the noise-prediction   [10]
BL-2,   objective.
4   ii. Analyze why diffusion models are generally more stable to train than GANs.
Q7
CO-3;   a.   i.   Describe the concept of a probability skip list and how it enables fast search.   [10]
BL-2,   ii. Discuss the idea of a navigable small world graph in the context of nearest
4   neighbor search.
iii. Analyze how HNSW combines skip-list hierarchy and small-world graph
navigation to improve search efficiency in high-dimensional spaces.
CO-4; b.   i.   Describe the CLIP training process, including paired data, shared embedding   [10]
BL-   space, and contrastive loss.
2,3,4   ii. Analyze why CLIP enables strong zero-shot transfer without task-specific fine-
tuning.
iii. CLIP is pretrained on 40 lakh image-text pairs. If training uses batches of
N=256, estimate:
a. number of batches required to see 40 lakh pairs once
b. how many pairwise similarity entries are computed per batch
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 78f4d3fabe5f

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AI_7012/GENERATIVE AI/QP_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: GENERATIVE AI
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data wherever necessary.
Q1   Answer briefly:
CO-1; a.   Compare Natural Language Understanding (NLU) and Natural Language Generation   [5]
BL-4   (NLG). Considering example applications, explain how they interact with real systems.
CO-2; b.   i. Explain in brief the concept of autoregressive models   [5]
BL-3   ii. An autoregressive model which predicts the token from left to right. For the sequence S
= “A B C ⟨eos⟩”, the model’s predicted conditional probabilities at each step are:
p(A|⟨bos⟩)=0.55,
p(B|⟨bos⟩ A)=0.60,
p(C|⟨bos⟩ A B)=0.50,
p(⟨eos⟩|⟨bos⟩ A B C)=0.70.
where bos is beginning of sequence and eos is end of sequence. Compute the joint
probability p(S) under the autoregressive factorization.
CO-3; c.   If an Hierarchial Navigable Small Worls (HNSW) index is built with parameters:   [5]
BL-3   • M (max connections per node) = 8,
• efConstruction (size of dynamic candidate list during index building) = 100,
and
• efSearch (size of dynamic candidate list during querying) = 50,
what will happen if efSearch is increased to 150 while keeping the other parameters
unchanged? Specifically, explain the expected effect on:
i.   Recall,
ii.   Query latency
iii.   Index memory usage
Give a brief justification for each.
CO-5; d.   You are given one target and one predicted translation:   [5]
BL-3
•   Target: “the quick brown fox jumps over the lazy dog”
•   Predicted Sentence: “the quick brown dog jumps over the lazy dog”
Use case-insensitive matching and assume uniform weights for BLEU-4 and compute with
natural logs. Compute the following:
i.   Compute the n gram precisions p1, p2, p3 and p4 for unigrams through 4-grams.
Show counts of matches and totals for each n.
ii.   Compute the brevity penalty (BP) given candidate length c and reference length r.
iii.   Compute the final BLEU-4 score.
********** 1 **********
--- page 2 ---
Q2
CO-2; a.   With respect to the Bidirectional Transformer (BERT) model, answer the following:   [10]
BL-   i.   Explain the advantage of BERT over decoder only models.
2,4   ii. Justify the significance of Masked Language Model (MLM).
iii. Explain the roles of [CLS], [SEP], token embeddings, position embeddings, and
segment (token-type) embeddings in BERT’s input representation.
iv. Explain how the fine tuning can be done for sentence pair classification task.
CO-3; b.   i.   Compare traditional databases and vector databases highlighting the strengths   [10]
BL-4   and weakness of each of them.
ii.   An online marketplace wants a unified search for:
• Exact lookups: ORDER-IDs, SKU, seller usernames.
•   Structured filters: price range, brand, availability, delivery region.
• Semantic queries: “lightweight waterproof hiking jacket under ₹5k”, plus
multilingual queries (Hindi/English mix).
• Unstructured data: product descriptions & user reviews (text) and image
captions.
•   Constraints: inventory updates are frequent (per-minute), p95 latency < 1.0
s, and results must show verifiable fields (price/stock) and source snippets
from reviews.
Which storage/retrieval approach would you choose—traditional database,
vector database, or a hybrid? Justify with three concrete reasons tied to
i.   exact/structured vs. semantic needs,
ii. update frequency & latency
iii. trust/traceability.
Q3
CO-2; a.   With respect to GPT 2 model, answer the following:   [10]
i.   Briefly explain the following key changes from GPT-1 to GPT-2 in training
BL-2
setup/aims
• zero-shot evaluation
• context window
and why these changes matter for generalization.
ii.   Explain how GPT-2 performs zero-shot tasks via prompting. Give one example
of a task that benefits, and discuss two limitations.
CO-3; b.   i.   Explain the difference between a typical Hash function used in dictionaries in python [10]
BL-3   and a Hash function used in Locality Sensitive Hashing (LSH).
ii. Suppose that Locality sensitive hashing (LSH) algorithm is being implemented on
two short documents Doc1 and Doc2. The documents contain the following content:
• DocX = “machine learning”
• DocY = “learning machines”
(lowercase; keep spaces and treat them as _ when listing shingles):
Use character bigrams (k = 2). Consider unique bigrams only.
Assign IDs: List all unique bigrams across both docs in lexicographic order (same as
used in dictionaries) and assign integer IDs starting at 0.
Hash functions (mod 19):
h1(x)=(7x+2) mod 19
h2(x)=(5x+4) mod 19
h3(x)=(9x+1) mod 19
h4(x)=(3x+6) mod 19
********** 2 **********
--- page 3 ---
Compute the following:
a. Build the characteristic matrix: rows = bigram IDs, columns = {DocX,
DocY}, entries ∈ {0,1}. Show the bigram → ID mapping.
b. Compute the true Jaccard similarity.
c. Compute the MinHash signatures (length 4) for DocX and DocY using
h1..h4. For each hash, take the minimum hash value over the bigram IDs
present in that doc.
d. Compare the signatures.
Q4
CO-3; a.   i.   Given a knowledge base of PDFs, outline the flow of steps for a basic RAG flow   [10]
BL-
using LangChain framework.
2,3
ii. A query used for RAG retrieves k = 5 chunks (avg 300 tokens each). Embedding cost
= $0.05 / 1K tokens; LLM generation cost = $0.20 / 1K tokens. The prompt to the
generator includes:
• user query (50 tokens)
• the five chunks
•   instructions (100 tokens).
The model generates 150 tokens.
e. Compute total tokens embedded, prompt tokens, generated tokens.
f. Compute total dollar cost for this query.
ii.   Explain when you would prefer fixed-length chunking vs. semantic/sentence-
aware chunking for policy PDFs.
CO-4; b.   i.   State one scenario where a Large Vision Model (Transformer-based, ViT) is preferable [10]
BL-   to a CNN, and one scenario where a CNN is still the better choice. Justify each in 1–2
2,3   lines focusing on accuracy/scale vs. latency/edge efficiency.
ii.   Explain how positional embeddings are injected in ViT. Mention one limitation of
absolute position embeddings and name one alternative (or improvement) used in later
variants.
iii. ViTs lack strong locality/translation inductive bias. Name any two improvements in
training strategies and explain in one line each how they help ViTs match CNNs on
ImageNet-scale data.
iv. A ViT uses patch size P × P=16 × 16, RGB input (C=3), and embedding dimension
D=768. The patch embedding is implemented as a linear projection (equivalently a conv
with kernel 16 ×16, stride 16). Compute the total number of parameters in the patch
projection with bias.
Q5
CO-3;   a.   i. What are the inherent limitations of Large Language Models (LLMs)?   [10]
BL-   ii. Your university pilots a GPT-style assistant for course advising. Below are three real
chat excerpts the team collected during testing (timestamps are from October 2025).
2,4
The model has not been connected to any internal databases.
********** 3 **********
--- page 4 ---
Excerpt A (Policy answer):
Student: “What are the graduation requirements for the BTech AI program updated this
year?”
Assistant: “You need 180 credits including a Capstone. Two ethics electives are optional.”
Excerpt B (Scholarship info):
Student: “Is there financial aid for students who publish in top AI conferences?”
Assistant: “Yes, the university offers the ‘Scholars Grant’ covering 50% tuition for one
year.”
Excerpt C (Advising style):
Student: “I’m a third-year transfer student from mechanical engineering, targeting machine
perception roles. Which two electives fit best next term?”
Assistant: “Consider taking Programming 101 and Introduction to Data. These are great
starting points for everyone.”
Based on these responses, answer the following questions:
a. For each excerpt (A, B, C), identify the primary failure and explain why it
arises from inherent LLM limitations, not just a bad prompt. Use precise
terminology and tie it to the excerpt.
b. Propose system-level mitigations for each failure that does not rely on
retraining from scratch.
CO-4; b.   i.   What is the difference between Large language model (LLM) and Vision   [10]
BL-   Language Model (VLM)?
2,3   ii.   Briefly explain how CLIP aligns images and text into a shared embedding space
and how this enables zero-shot classification with class name prompts.
iii.   How is Contrastive Language Image Image Pretraining (CLIP) used in zero-shot
transfer?
iv.   You are given L2-normalized embeddings (dimension doesn’t matter):
• Image vector is vI
• Text vectors are vlion,vzebra,vgiraffe
• The dot products (cosines) are:
⟨vI,vlion⟩=0.62, ⟨vI,vzebra⟩=0.55, ⟨vI,vgiraffe⟩=0.40.
a. Compute the Softmax probabilities over classes using a temperature
T=0.01(i.e., logits = cosines / T).
b. Report the predicted class.
Q6
a.   With reference to Denoising Diffusion Probabilistic models (DDPM), answer the   [10]
CO-4;
following:
BL-2
i.   What is the similarity between Hierarchical VAE and DDPM?
ii.   Explain how Gaussian noise is added over T steps to obtain xt from x0.
iii.   What is the advantage of reparameterization technique in forward diffusion process
of DDPM? What is the advantage of this technique?
CO-5; b.   [10]
BL-2,   i. Given two retrievers A and B have identical Recall@10 but A has higher MRR@10,
3   analyze what this implies about ranking quality and user experience.
ii. With reference to LLM evaluation, answer the following:
a. Explain the term LLM as a Judge.
b. How does LLM as a judge work (typical set up)?
c. Highlight the limitations and issues of this approach.
********** 4 **********
--- page 5 ---
Q7
CO-1;   a.   Considering a specific application of Text-to-Image Generation for E-commerce Product   [5]
BL-2   Creatives, answer the following questions:
• highlight the process of generation,
•   Justification of choice of the chosen architecture
• Generation pipeline
CO-6;   b.   Give a practical example explain the Agentic AI four-step process for problem-solving.   [5]
BL-2
CO-5;   c.   You are given a reference and a predicted summary (case-insensitive, whitespace   [5]
BL-3   tokenization):
Reference (R): the child plays in the park
Candidate (C): child plays in the park
Use exact unigram matching only (no stems/synonyms). Assume the matched tokens form
one contiguous chunk in the reference (i.e., ch=1).
Assume α (parameter controls the relative weights of precision and recall) = of 0.9,
𝑐ℎ 3
fragmentation penalty = 0.5x ( 𝑚)
Calculate the following:
d. Find matched tokens m, lengths ∣C∣, ∣R∣, and compute Precision P and Recall R.
e. Compute weighted F-score Fmean.
f. With ch=1, compute the Penalty and the final METEOR.
CO-6;   d.   For an outbound-email agent, list three risks (data exfiltration, persuasive harm, over-   [5]
BL-2   automation) and one mitigation each.
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 8 · paper d83ac7d6acd2

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_AI_7051/GENERATIVE AI/QP_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (ARTIFICIALINTELLIGENCE)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: GENERATIVE AI
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO-2;   a.   Assume that we are using a transformer encoder block in which when using self-   [5]
BL-3   attention output for a 2-token Sequence, the input tokens are:
x1= [1,0], x2= [0,1]
The query, key and value matrices are given by
WQ=[1 0 WK=[1 1 WV=[2 0
0   1],   0   1],   1 1]
Compute the self-attention output for tokens x1 and x2 .
CO-1;   b.   Suggest ways to address the following challenges in Generative AI:   [5]
BL-4   1. Metrics for evaluation
2. Training challenges
3. Ethical considerations
CO-5;   c.   The reference summary and the candidate summary generated by LLM for a   [5]
BL-3   model is as given below:
Reference summary: the system gives correct answers
Candidate summary: the system gives useful correct answers
Compute:
i.   overlapping bigrams
ii.   precision
iii.   recall
iv. ROUGE-2 F1 score
CO-3;   d.   i.   State the two fundamental techniques that contribute to Hierarchical [5]
BL-3   Navigable Small World (HNSW).
ii.   In a simplified HNSW search, the query-to-node distances are:
A=1.513, B=0.539, C=1.700, D=0.943, E=0.539, F=0.
********** 1 **********
--- page 2 ---
If k=2, determine the returned top-2 nodes.
If k=3, determine the returned top-3 nodes.
Q2
CO-2;   a.   With respect to the GPT1 model answer the following questions:   [10]
BL-   i.   State and explain the loss function used in the pretraining and fine-
2,3   tuning stage.
ii.   Justify the significance of Task Specific Input Transformations as
used in GPT1.
iii.   Compare GPT1 and BERT model.
CO-5;   b.   i. The reference sentence and the candidate sentence generated by the LLM is   [10]
BL-   as given below:
3,4   Reference: the child plays in the park
Candidate: child plays in the park
Assume:
• exact unigram matching only
• matched tokens form one contiguous chunk, so c=1
• α=0.9, γ=0.5, β=3
Compute:
a. number of matched tokens m
b. candidate length and reference length
c. precision and recall
d. weighted F-score
e. penalty
f. final METEOR score
ii. Compare METEOR and BLUE score evaluation metrics as used in LLMs.
Q3
CO-3;   a.   i.   Compare Simple RAG and advanced RAG techniques.   [10]
ii.   Explain why chunking is necessary in the indexing phase of a RAG
BL-4
system. Analyze how chunk size and chunking strategy affect retrieval
quality, efficiency, and final answer relevance.
CO-2;   b.   With respect to LangChain, answer the following:   [10]
BL-   i.   Explain the role of Chains in LangChain and differentiate between simple
3,4   chains and multi-step chains.
ii.   State the significance of PromptTemplate in LangChain applications.
iii.   Explain the working of LangChain in a query-answering pipeline, starting
from user query, vector representation, similarity search, retrieval of
relevant information, and final response generation.
Q4
CO-3;   a.   Consider that Locality Sensitive Hashing (LSH) is being applied on two short [10]
BL-3   documents:
• Doc1 = "deep learning"
• Doc2 = "learning deep"
Use the following parameters:
•   shingle length k=2
• Hash functions:
H1(x)=(2x+1) mod 13, H2(x)=(3x+2) mod 13, H3(x)=(4x+1) mod 13
Determine:
i.   True Jaccard similarity and Jaccard distance
ii.   Characteristic matrix
********** 2 **********
--- page 3 ---
iii.   Signature matrix using the hash functions
iv.   Signature similarity
CO-2;   b.   i.   Analyze why GPT-3 is called a few-shot learner rather than just a larger   [10]
BL-   language model.
2,3   ii.   Give one example of few-shot learning for GPT3 for a use case of your
choice.
iii.   Highlight some of the limitations of GPT-3.
Q5
CO-1;   a.   Justify the use of large models help in visual question answering? Briefly state the [5]
BL-2
steps.
CO-6;   b.   i. Compare Generative AI and Agentic AI.   [10]
BL-   ii. How is a multi-agent system different than a single agent system?
2,4   iii. Analyze how memory and tool use together make agentic AI more effective
than simple text generation.
CO-5;   c.   Briefly explain any two hybrid evaluation methods used to evaluate the performance [5]
BL-2
of LLMs.
Q6
a.   i.   Briefly explain how contrastive loss helps align image and text   [10]
CO-4;   representations in CLIP.
BL-   ii. Design and depict a zero-shot image classification pipeline using CLIP.
2,3   iii. A CLIP training batch contains N=40 matched image-text pairs.
Find:
a. the total number of possible image-text pairings in the batch
b. the number of genuine matched pairs
c. the number of mismatched pairs
CO-4;   b.   i.   Explain the multi-step closed-form formulation of the forward diffusion   [10]
BL-2,   process.
4   ii. Explain why the reparameterization trick is useful in DDPM training.
iii. Analyze how reparameterization improves efficiency, differentiability, and
numerical stability during training.
Q7
CO-3;   a.   i.   Explain the basic idea of RAG and fine-tuning as two ways of improving   [10]
BL-2,   LLM performance.
4   ii.   Describe situations where RAG is preferable to fine-tuning.
iii.   Analyze the trade-offs between RAG and fine-tuning in terms of cost,
scalability, freshness of knowledge, and domain adaptation.
********** 3 **********
--- page 4 ---
CO-4;   b.   i.   Explain the roles of patch embeddings, positional embeddings, and the   [10]
BL-   [CLS] token in ViT.
2,3,4   ii.   Analyze why ViT can capture global context better than CNNs but
usually requires larger pretraining datasets.
iii.   A ViT is pretrained on 224×224 RGB images with patch size 16×16
and later fine-tuned on 384×384 images with the same patch size.
Compute:
a. number of patches during pretraining
b. number of patches during fine-tuning
c. change in sequence length after adding the [CLS] token
d. Identify why position embeddings become an issue during
fine tuning.
********** 4 **********
````

## 2025-26 · Re-Exam · paper 30cebaf194a9

- Departments: Artificial Intelligence
- Programmes: MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/Artificial Intelligence/Generative AI/Generative AI, Sem-VIII, Batch 2025-2026, RE Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: ocr (4 pages), mean OCR confidence 89.1

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHS.
MANAGEMENT (ARTIFICIALINTELLIGENCE)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: GENERATIVE AI

Date: 09 Jul 2026 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

RE EXAMINATION (Acad. Year:2025-2026)

Instructions:

I. This question paper contains 4 pages.

2. Question No.1 is compulsory.

3. Out of remaining questions, attempt any 4 questions.

4. In all 5 questions to be attempted.

5. All questions carry equal marks.

6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right hand side indicate full marks.

8. Assume Suitable data if necessary.

LQl Answer briefly:

CO-2; | a. Assume that we are using a transformer encoder block in which when using self- [5]
BL-3 attention output for a 2-token Sequence, the input tokens are:
x1= [1,0], x2= [0,1]
The query, key and value matrices dre given by
_f1 0 fl 1 _[2 0
We-[) ik We-[5 i} We-[f
Compute the self-attention output for tokens x; and x> .
CO-1; | b. Suggest ways to address the following challenges in Generative AT: [5]
BL-4 1. Metrics for evaluation
2. Training challenges
3. Ethical considerations
CO-5; | c. The reference summary and the candidate summary generated by LLM for a [5]
I-RL-3 model is as given below:
Reference summary: the system gives correct answers
Candidate summary: the system gives useful correct answers
Compute:
i. overlapping bigrams
ii, precision
viii, recall
iv. ROUGE-2 F1 score
CO-3;] d. i. State the two fundamentad techniques that contribute to Hierarchical [5]
BL-3 Navigable Small World (HNSW).
il. In a simplified HNSW search, the query-to-node distances are:
é A=1.513, B=0.539, C=1.700, D=0.943, E=0.539, F=0.

FICK 7 Rk
--- page 2 ---
If k=2, determine the returned top-2 nodes.
If k=3, determine the returned top-3 nodes.

Q2 .

CO-2; | a. With respect to the GPT1 model answer the following questions: ~ . [10]
BL- i. State and explain the loss function used in the pretraining and fine-

2,3 tuning stage.

ii. Justify the significance of Task Specific Input Transformations as
used in GPT1.
ii. Compare GPT1 and BERT model.

CO-S; |b. i. The reference sentence and the candidate sentence generated by the LLM is [10]
BL- as given below:
3,4 Reference: the child plays in the park

Candidate: child plays in the park

Assume:

e exact unigram matching only
e matched tokens form one contiguous chunk, so c=1
e a=0.9, y=0.5, B=3
Compute:
a. number of matched tokens m
b. candidate length and reference length
c. precision and recall
d. weighted F-score
e. penalty
f. final METEOR score
ii. Compare METEOR and BLUE score evaluation metrics as used in LLMs.

Q3
CO-3; | a. i. Compare Simple RAG and advanced RAG techniques. : [10]
il. Explain why chunking is necessary in the indexing phase of a RAG
BL-4 . : :
system. Analyze how chunk size and chunking strategy affect retrieval
quality, efficiency, and final answer relevance.
CO-2; | b. With respect to LangChain, answer the following: [10]
BL- i. Explain the role of Chains in LangChain and differentiate between simple
3,4 chains and multi-step chains.
ii. State the significance of PromptTemplate in LangChain applications.
ii. Explain the working of LangChain in a query-answering pipeline, starting
from user query, vector representation, similarity search, retrieval of
relevant information, and final response generation.
Q4

CO-3; a. | Consider that Locality Sensitive Hashing (LSH) is being applied on two short | [10]
BL-3 documents:
f ¢ Docl = "deep learning"
¢ Doc2 = "learning deep"
Use the following parameters:
e shingle length k=2
e Hash functions:
H1(x)=(2x+1) mod 13, H2(x)=(3x+2) mod 13, H3(x)=(4x+1) mod 13

*

» | Determine:

4 : ' . ” :

’ i. True Jaccard similarity and Jaccard distance
ii. Characteristic matrix

FOGG 2 A Gk
--- page 3 ---
iii. Signature matrix using the hash functions
iv. _ Signature similarity

CO-2; b. i. Analyze why GPT-3 is called a few-shot learner rather than just a larger [10]
BL- language model. °
pat ii. Give one example of few-shot learning for GPT3 for a use case 6f your
choice. :
iii. Highlight some of the limitations of GPT-3.
Q5
CO-1; | a. | Justify the use of large models help in visual question answering? Briefly state the | [5]
BL-2
steps.
CO-6; b. |i. Compare Generative AI and Agentic Al. [10]
BL- ii. How is a multi-agent system different than a single agent system?
2,4 iii. Analyze how memory and tool use together make agentic AI more effective
than simple text generation.
CO-5; c. | Briefly explain any two hybrid evaluation methods used to evaluate the performance | [5]
hee of LLMs.
la .
Q6
a. i. Briefly explain how contrastive loss helps align image and text [10]
CO-4; representations in CLIP.
BL- ii. Design and depict a zero-shot image classification pipeline using CLIP.
252 iii. A CLIP training batch contains N=40 matched image-text pairs.
Find:
a. the total number of possible image-text pairings in the batch.
b. the number of genuine matched pairs
c. the number of mismatched pairs
CO-4; b. | i. Explain the multi-step closed-form formulation of the forward diffusion [10]
BL-2, process.
4 ii. Explain why the reparameterization trick is useful in DDPM training.
iii. Analyze how reparameterization improves efficiency, differentiability, and
numerical stability during training.
E27
CO-3; i. Explain the basic idea of RAG and fine-tuning as two ways of improving [10]
BL-2, ‘LLM performance.
4 ii. Describe situations where RAG is preferable to fine-tuning.

iii. Analyze the trade-offs between RAG and fine-tuning in terms of cost,
scalability, freshness of knowledge, and domain adaptation.

FIC TORO IHC II A i a
--- page 4 ---
>i

CO-4;

BL-
2,3,4

b.

il.

ili.

Explain the roles of patch embeddings, positional embeddings, and the
[CLS] token in ViT. *

Analyze why ViT can capture global context better than Cie but
usually requires larger pretraining datasets.

A ViT is pretrained on 224x224 RGB images with patch size 16x16
and later fine-tuned on 384384 images with the same Data size.
Compute:

a. number of patches during pretraining
b. number of patches during fine-tuning
c. change in sequence length after adding the [CLS] token

d. Identify why position embeddings become an issue during
fine tuning.

[10]

FO Ok
````
