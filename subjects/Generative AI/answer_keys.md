# Generative AI: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper d55d7adf0cae

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AI_7012/GENERATIVE AI/ANS_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: IV/Semester VII (Exam Year: NA)
Subject: GENERATIVE AI
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
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
Ans: 1 mark for each correct point as asked in the question
CO-3; b.   When using Locality Sensitive Hashing (LSH), two policy-related shingle sets   [5]
BL-3   (unique terms) are extracted from different documents:
C1= {policy, compliance, risk, audit, KYC, AML}
C2= {risk, audit, KYC, onboarding, sanctions, AML}
i. Compute the true Jaccard similarity J(C1, C2)
********** 1 **********
--- page 2 ---
ii. Compute the true Jaccard distance D(C1, C2)
iii. In a practical LSH system, how is the similarity checked? Explain briefly.
Solution:
(Jaccard similarity: 2 marks, Jaccard distance: 2 marks, how is the similarity
checked: 1mark)
i.   Intersection: {risk, audit, KYC, AML}
∣C1∩C2∣=4
Union: {policy, compliance, risk, audit, KYC, AML, onboarding, sanctions}
∣C1∪C2∣=8
Jaccard similarity
J(C1, C2)=∣C1∩C2∣∣C1∪C2∣=4/8=0.5
ii.   Jaccard distance
D(C1, C2)=1−J=1−0.5=0.5
iii.   In real systems, we use multiple Hash functions/hash tables, and band MinHash
signatures, to determine similarity.
CO-2; c.   i.   Justify the significance of masked SoftMax   [5]
BL-3   ii.   Given the following logits (scores) for a query-key interaction:
• Logits= [3.0, −2.0,2.0, −1.0]
And a mask vector, where 1 means the position is valid and 0 means the
position should be ignored:
Mask= [1,0,1,0]
Apply a masked SoftMax operation to the logits.
Solution:
(2 marks for significance, 3 marks for numerical)
Masked SoftMax is the mechanism that keeps attention legal, focused, and numerically
sound—a small operation with outsized impact on correctness and quality.
What goes wrong if you don’t mask
• Leakage: next-token training sees answers it shouldn’t (for left to right
generation).
• Spurious correlations: attention over PAD or irrelevant regions which causes
degraded generalization.
•   Mis-normalization: probabilities spread over junk positions which causes weaker
gradients and slower convergence.
Logits = [3.0, −2.0, 2.0, −1.0],
Mask = [1, 0, 1, 0] (only positions 1 and 3 are valid).
Compute SoftMax only over unmasked logits (indices 1 and 3):
•   e3.0=20.0855
•   e2.0=7.3891
• Sum S=20.0855+7.3891=27.4746
Probabilities (masked positions get 0):
• p1=20.0855/27.4746≈0.7311
• p2=0
• p3=7.3891/27.4746≈0.2689
• p4=0
Result: [0.7311, 0, 0.2689, 0]
CO-2; d. d. You are given a reference and a candidate summary (case-insensitive, whitespace   [5]
BL-4   tokenization):
********** 2 **********
--- page 3 ---
• Reference: the committee approved the budget last week
• Predicted: the committee unanimously approved budget last month
Compute the following (show formulas and brief working):
i. ROUGE-1: Compute precision, recall, and F1 using unigram overlap.
ii. ROUGE-2 Compute precision, recall, and F1 using bigram overlap.
iii. ROUGE-L: Given LCS length = 5, compute precision, recall, and F1 for
ROUGE-L using the LCS-based definitions.
Solution:
(ROUGE-1: 1.5, ROUGE-2: 1.5, ROUGE-L: 2 marks)
ROUGE-1 (unigram overlap)
Ref counts: {the×2, committee, approved, budget, last, week}
Cand counts: {the, committee, unanimously, approved, budget, last, month}
Overlap (min counts): the×1, committee×1, approved×1, budget×1, last×1 → 5 matches
•   Precision = 5 / 7 = 0.7143
•   Recall = 5 / 7 = 0.7143
• F1 = 2PR/(P+R) = 0.7143
ROUGE-2 (bigram overlap)
Ref bigrams (6):
the committee, committee approved, approved the, the budget, budget last, last week
Cand bigrams (6):
the committee, committee unanimously, unanimously approved, approved budget, budget
last, last month
Overlap: the committee, budget last → 2 matches
•   Precision = 2 / 6 = 0.3333
•   Recall = 2 / 6 = 0.3333
• F1 = 0.3333
ROUGE-L (from LCS)
Given LCS = 5, candidate length N=7, reference length M=7
•   Precision = LCS / N = 5 / 7 = 0.7143
•   Recall = LCS / M = 5 / 7 = 0.7143
• F1 = 0.7143
Q2
CO-2;   a.   With respect to GPT 1 model, answer the following questions:   [10
BL-   • Explain the unsupervised pre-training used in GPT 1.
]
2,3   • Briefly outline how GPT-1 was fine-tuned for supervised tasks using task
specific transformations. Give examples for at least two tasks.
• Justify the use of masked self-attention used to enforce left-to-right
generation in GPT 1.
Solution:
(Unsupervised pre training: 3 marks, fine tuning: 4 marks, masked self-attention: 3
marks)
•
• Objective: Causal language modelling to maximize next-token likelihood
over raw text (no labels).
********** 3 **********
--- page 4 ---
• Architecture: Decoder-only Transformer with masked (causal) self-attention, so
each token attends only to positions ≤ t (left-to-right).
• Data: Long-form prose (e.g., BooksCorpus) to learn discourse-level dependencies;
no task annotations required.
• Tokenization: BPE subwords to handle rare/compound words efficiently and keep
vocab manageable.
• Context window: ~512 tokens; the model learns to compress long left-context into
useful representations.
• Training signal: Every position in every sequence provides a supervised target
(the next token), learning from the large corpus.
•   Pre-training learns general syntax/semantics/world knowledge which helps for
downstream tasks;
• Fine-tuning adds a small task head and adapts to labeled tasks with relatively few
examples.
•
GPT-1’s fine-tuning with task-specific transformations:
• GPT-1 uses the same Transformer decoder architecture for all tasks.
• The only thing that changes between tasks is how the input text is formatted
(transformed) so that the model can treat every task as predicting the next token in
a sequence.
• Instead of building separate architectures for classification, entailment, or QA,
GPT-1 turns each task into a language modeling problem through special input
arrangements.
• Allows a single pretrained LM to handle multiple NLP tasks without changing its
internals.
• The model doesn’t need task-specific layers; it just gets a different prompt-like
input format.
• Training objective remains next token prediction.
Examples
• Task Specific Input Transformations (any two examples)
• Text Classification
• Example Task: Sentiment analysis.
• Transformation:
•   Input: "Review: The movie was fantastic. Sentiment: “
• The model predicts the next token(s) → "positive“
• The label is simply another token in the sequence.
• Textual Entailment (NLI)
• Example Task: Recognizing Textual Entailment (RTE).
• Transformation:
o Input: "Premise: A man is playing a guitar. Hypothesis: A person is
making music. Answer:
o Output: "entailment“ or "contradiction“ or "neutral"
iii.
• In self-attention, each token at position t computes attention over all keys/values
in the sequence.
• GPT-1 applies a causal (look-ahead) mask so position t can only see positions ≤ t.
Future positions > t are set to –∞ in the attention logits, making their softmax
probabilities exactly 0.
• During training, token t predicts the next token using only the past (and current)
context—no “peeking.”
********** 4 **********
--- page 5 ---
• During inference, generation is naturally left-to-right; the model’s training
condition matches test time (train–inference alignment), reducing exposure bias.
CO-3;   b.   A global research team needs a unified semantic search over a read-only corpus of [10
BL-4   200k research PDFs (updated weekly). Queries are free-text, often cross-lingual
]
(English/Hindi/Spanish) and may include image-caption text extracted from figures.
There are no exact ID lookups, no transactional updates, and only lightweight
metadata filters (year, domain) and results must return top-k passages with source
citations (doc + page).
i.   Suggest a database for this application (traditional database or vector database)
highlighting with three reasons about your choice.
ii. Design a search solution for the research team. Your solution should highlight
the following points:
• the embedding model(s) you’d choose (unimodal/multimodal) and why,
• the index type and two key parameters you’d tune for latency/recall,
• how you’d store and use metadata (year/domain) for filtered ANN queries,
• the retrieval workflow and how you’ll surface citations,
Solution:
(Suggestion of vector database: 4 marks, design: 6 marks)
i.   Vector DB only (fits the research-PDF scenario)
Why vector-only fits better than a traditional DB here (3 concrete reasons):
1. Pure semantic need: Queries are free-text and cross-lingual; vector
search captures meaning across languages where keyword/B-tree
cannot.
2. Unstructured corpus: Research PDFs + captions lack rigid schemas;
vector DBs index embeddings directly without complex relational
modeling.
3. Read-mostly, weekly updates: ANN indexes handle batch re-embedding
easily; no need for transactional features (constraints/joins) of RDBMS,
keeping the stack simpler and faster.
ii.
• Embeddings: Use a strong multilingual text model for titles/abstracts/body
and an image-caption/text model (e.g., CLIP) for figure captions. This
covers cross-lingual queries and caption-like phrasing; store both vectors
(text, caption) per chunk.
•   Index: Build HNSW indexes (one per vector type) with, e.g., M=32–64,
efConstruction=200–400; efSearch=64–128 for recall/latency balance.
• Metadata & filters: Attach {doc_id, page, year, domain, section} to each
chunk as payload; use vector DB filtered ANN (e.g., year >= 2019, domain
in {NLP, CV}) so semantic search respects simple constraints.
•   Retrieval workflow:
Ingest PDFs   sentence/section-aware chunking (≈200–400 tokens, small
overlap)   embed (text + caption fields) ANN search on the appropriate
index (or hybrid within vector DB: combine text and caption scores by
weighted sum/RRF)   (optional) LLM/cross-encoder reranker on top-50 to
refine semantics   return top-k.
********** 5 **********
--- page 6 ---
•   Citations: Each hit returns {doc_id, page, section, snippet} from metadata.
Present answers as passage snippets with (doc/page); for LLM summaries,
require inline citations per claim (carry through the node IDs).
Q3
CO-3;   a.   i. Compare Hierarchial Navigable Small World (HNSW) and Locality Sensitive   [10
Hashing (LSH) algorithms used in indexing in vector databases.
BL-3   ]
ii. You are given a single-layer HNSW graph (only the bottom layer is shown).
Edge cap per node M=2. Use Euclidean distance. Search uses efSearch = 3 and
returns top-k = 2 neighbors. Start from entry node A.
The node coordinates are:
A(0,0), B(1,0), C(0,1), D(1,1), E(2,0), F(2,1)
Undirected edges (respecting M=2)
• A ↔ B, A ↔ C
• B ↔ D, B ↔ E
• C ↔ D
• D ↔ F
• E ↔ F
The Query(q) is (1.6, 0.3).
a. Compute the distances d(q,x) for all nodes x∈{A,B,C,D,E,F.
b. Run the HNSW best-first search on this layer with efSearch=3, starting at A.
• Maintain a candidate (min-heap) and a result set WWW (size up to
efSearch).
• Expand nodes in order of increasing distance; when you pop a node, push
any unvisited neighbors with their distances (avoid revisits).
HNSW (Hierarchical
Aspect   LSH (Locality Sensitive Hashing)
Navigable Small World)
Multi-layer graph; greedy
Multiple hash tables built with LSH
search down the hierarchy,
Core idea   functions so near points collide with
then neighborhood expansion
high probability
on bottom layer
Any metric/semi-metric with Needs LSH family for the target metric
Supported
a comparator (cosine, L2,   (e.g., SimHash for cosine, E2LSH for
distances
inner-product, etc.)   L2)
Higher: construct graph links; Moderate: compute hashes & insert into
Build cost   parameters (M),   (L) tables; parameters (L), #hashes per
(ef_{construction})   table (K), bin width (w)
Very fast and adaptive; tune
Sub-linear on average; probes limited
Query time   with (ef_{search}). Typically
buckets, then re-ranks candidates
high recall at low latency
Good when a proper LSH exists; recall
State-of-the-art recall–latency
Recall/quality   can degrade if metric/data not well
tradeoff for many workloads
matched
Good inserts; deletions
Dynamic   Inserts easy; deletions easy; tables are
trickier (lazy delete/periodic
updates   independent
rebuild)
********** 6 **********
--- page 7 ---
(M) (degree),
(ef_{construction}) (build   (K) (selectivity), (L) (tables/recall), (w)
Parameters
quality), (ef_{search}) (query (bin width), probe count
recall/latency)
• Stop when the nearest candidate in the queue is farther than the worst
item in W.
• Write the visit order and the final contents of W (node, distance).
• Report the top-2 neighbors (node names) returned to the user.
• Predict how the answer might change if efSearch were increased to 10 (no
need to recompute).
Solution:
(Comparison: 4 marks, numerical: 6 marks (1 marks for Euclidean distance, correct
implementation: 2 marks, top 2 neighbour calculation: 2 marks, prediction of
increase in efSearch : 1 mark))
i.   Any 4 correct points
ii.
Distances from q=(1.6, 0.3)
(q,A) =(1.6−0)2+(0.3−0)2=1.628
d(q,B) =(1.6−1)2+(0.3−0)2=0.671
d(q,C) =(1.6−0)2+(0.3−1)2=1.746
d(q,D) =(1.6−1)2+(0.3−1)2=0.922
d(q,E) =(1.6−2)2+(0.3−0)2=0.500
d(q,F) =(1.6−2)2+(0.3−1)2=0.806
(b) HNSW best-first search on the bottom layer (efSearch = 3), start at A
•   Init:
Candidates C={(A,1.628)}; Result set W={(A,1.628)}; Visited={A}.
• Pop A (nearest in C) → expand neighbors B, C
Add B (0.671), C (1.746).
• C={(B,0.671),(C,1.746)};
• W={(A,1.628),(B,0.671),(C,1.746)} (size capped at 3).
• Pop B (0.671) → expand neighbors D, E (A already visited)
• Add D (0.922), E (0.500).
• Keep top ef (=3) in W: farthest drops ⇒ W={(E,0.500),(B,0.671),(D,0.922)}.
•   C={(D,0.922),(C,1.746),(E,0.500)} (as a min-heap it will next pop E).
• Pop E (0.500) → expand neighbors F (B already visited)
• Add F (0.806).
• Update W (still size 3): W={(E,0.500),(B,0.671),(F,0.806)}
• (D is now the 4th and gets dropped).
• Next candidate in C has distance ≥ current worst in W; stopping criterion met.
•   Visit order: A → B → E → F
Final W: E (0.500), B (0.671), F (0.806)
• Top-2 neighbors (k = 2)
• E (0.500), B(0.671)
•   If efSearch were increased substantially, you’d explore more neighbors—
slightly higher latency—with the same top-2 here, since E and B are already
the closest.
********** 7 **********
--- page 8 ---
CO-2;   a. With reference to GPT 3 model, answer the following:   [10
BL-   iii. Define in-context learning in GPT-3. Contrast it with parameter fine-tuning,
]
2,3   and give one situation where ICL is preferable.
iv. Design a few-shot prompt that makes GPT-3 classify short reviews as {Positive,
Neutral, Negative}.
Requirements:
• Include two labeled examples in the prompt (few-shot).
• Add an instruction that the output must be exactly one of the three
labels.
• Provide the final prompt text you would send (≤8 lines total).
iii.   Discuss limitations of GPT-3 like prompt sensitivity, hallucination, bias
when used in zero/few-shot mode.
Solution:
(In context learning: 3 marks, prompt:3 marks, limitations: 4 marks)
i.
In-context learning (ICL) in GPT-3 is when the model learns a task on the fly at
inference time by reading an instruction and a few demonstration examples placed in
the prompt, then continuing the pattern—without updating its weights.
vs. Parameter fine-tuning
• ICL: No gradient updates; knowledge comes from the prompt; task behavior
vanishes when the prompt is removed; fast to set up; cheap data needs (a handful
of examples).
•   Fine-tuning: Trains on labeled data with gradient descent; updates weights;
behavior persists across prompts; better for stable, high-volume tasks; requires
more data, training time, and MLOps.
When ICL is preferable
• Rapid, low-data adaptation. e.g., a support team launches a new, frequently
changing label set (promo names or product variants). You can paste 5–10 fresh
labeled examples into the prompt and get usable classifications immediately,
without waiting for a fine-tune cycle.
ii.
Classify each short review as exactly one of {Positive, Neutral, Negative}. Respond
with only the label.
Review: Loved the battery life and camera. → Positive
Review: It’s okay—does the job, nothing special. → Neutral
Review: The app crashes every time I open it. →
iii.
1) Prompt sensitivity
• What happens: Small changes in wording, ordering of shots, delimiter choice, or
even whitespace can swing accuracy and style (the model imitates surface
patterns).
********** 8 **********
--- page 9 ---
• Why: The model conditions purely on the prompt distribution at inference—no
learned, stable task head—so it overfits to the presented pattern.
• Symptoms: Output drift, flip-flopped labels if examples are reordered, degradation
with slightly longer inputs.
• Knock-on effects: Poor reproducibility and fragile deployment; hard A/B control.
•   (Mitigate briefly): Standardized templates, example ordering (easy→hard),
calibration instructions (“answer with one of {…} only”), and prompt ensembling.
2) Hallucination (unfaithful generation)
• What happens: Fluent but incorrect or unsupported statements, fabricated
facts/citations, or confident reasoning errors.
• Why: Causal next-token prediction optimizes fluency/likelihood, not truth; in
zero/few-shot there’s no retrieval or supervision to ground claims.
• Symptoms: Confidently wrong explanations, invented entities/metrics,
overgeneralization from few shots.
•   Risks: Misleading answers in high-stakes domains; hard to detect without external
checks.
•   (Mitigate briefly): Retrieval-augmented prompts, cite-and-quote requirements,
constrained output schemas, post-generation verification.
3) Bias & toxicity
• What happens: Stereotyped, toxic, or unfair outputs reflecting patterns in
pretraining data; class-conditional bias in sentiment/toxicity tasks.
• Why: Large web corpora encode societal biases; zero/few-shot conditioning may
amplify them (few examples ≈ weak counter-signal).
• Symptoms: Skewed classifications by demographic terms, biased completions,
disparate error rates.
•   Impacts: Ethical/legal concerns; harmed user groups; reputational risk.
•   (Mitigate briefly): Safety filters, bias-balanced exemplars, instruction constraints
(forbidden content), debiasing/reranking, human-in-the-loop for sensitive cases.
Cross-cutting constraints in zero/few-shot
• Length limits: Short context windows cap number/variety of examples.
• Evaluation drift: No persistent training signal → behavior changes with each
prompt revision.
• Lack of task calibration: Probabilities are not well-calibrated; thresholds vary by
prompt.
Bottom line: In zero/few-shot mode, GPT-3 is powerful but fragile—highly sensitive
to prompt form, prone to unfaithful outputs, and capable of biased behavior without
grounding, guardrails, and consistent prompt design.
Q4
CO-3;   a.   i.   Briefly explain Contrastive Language Image Pretraining (CLIP’s)   [10
BL-4   dual-encoder architecture (image encoder + text encoder) and how
]
its contrastive loss is applied over an image–text batch to align
modalities.
ii.   Design a simple image search and retrieval pipeline using CLIP.
iii.   Briefly explain the limitations of CLIP in real deployments.
********** 9 **********
--- page 10 ---
iv.   You use CLIP for zero-shot classification with class prompts.
a. For an image, the cosine similarities to prompts are: “a photo
of a cat” = 0.58, “a photo of a dog” = 0.56, “a photo of a fox” =
0.47. Which label is predicted, and why?
b.   If you change the template to “an image of a {label}” and the
order of labels in the prompt set, explain in 2–3 sentences how
this can alter the scores (prompt sensitivity) and name one
mitigation you would apply.
Solution:
(2.5 marks each)
i.
Dual-encoder:
CLIP has two separate networks—a vision encoder (e.g., ResNet/ViT) that maps an
image to a vector, and a text encoder (e.g., Transformer) that maps its caption/prompt to
a vector. Both outputs are L2-normalized, so their dot product is a cosine similarity in a
shared embedding space.
Contrastive loss over a batch:
Given a batch of BBB matched (image, text) pairs, CLIP computes the B×BB\times
BB×B similarity matrix between all image and all text embeddings. Using a temperature-
scaled softmax, it maximizes the probability of each true pair along its row/column while
treating the other B−1B-1B−1 combinations as in-batch negatives. The loss is applied
symmetrically (image→text and text→image) so matched pairs are pulled together and
mismatches are pushed apart, aligning the two modalities.
ii.
• Semantic Image Search and Retrieval
• CLIP can be employed for semantic image search and retrieval beyond simple
keyword-based searches.
• Users can input natural language queries, and the CLIP AI model will retrieve
images that best match the textual descriptions.
• This approach improves the precision and relevance of search results.
• Makes it a valuable tool in content management systems, digital asset
management, and any use case requiring efficient and accurate image retrieval.
iii.
• Lack of Interpretability
• The lack of interpretability in CLIP’s decision-making process.
• Understanding why the model classifies a specific image in a certain way
can be challenging.
• This can hinder its application in sensitive areas where interpretability is
crucial, such as healthcare diagnostics or legal contexts.
• Lack of Fine-Grained Understanding
• CLIP’s understanding is also limited in terms of fine-grained details.
• While it excels at high-level tasks, it may struggle with intricate nuances and
subtle distinctions within images or texts.
• Thus, limiting its effectiveness in applications requiring granular analysis.
• Limited Understanding of Relationships (Emotions, Abstract Concepts, etc.)
• CLIP’s comprehension of relationships, especially emotions and abstract
concepts, remains constrained.
•   It might misinterpret complex or nuanced visual cues.
• In turn, impacting its performance in tasks requiring a deeper understanding
of human experiences.
• Biases in Pretraining Data
********** 10 **********
--- page 11 ---
• Biases present in the pretraining data can transfer to CLIP, potentially
perpetuating and amplifying societal biases.
• This raises ethical concerns, particularly in AI applications like content
moderation or decision-making systems.
• In those use cases, biased outcomes lead to real-world consequences.
iv.
(a) Cat, because CLIP predicts the class whose text embedding has the highest cosine
similarity to the image embedding (0.58 > 0.56 > 0.47).
(b) Changing the template (e.g., “a photo of” to “an image of”) changes the text
embeddings, which can shift relative cosines and flip the top-1 class (prompt sensitivity).
Mitigation: use prompt ensembling (multiple templates per label with normalized,
averaged scores) and/or a small in-domain adapter/linear probe to stabilize predictions.
CO-3;   b.   i.   Compare LangChain and LlamaIndex.   [10
BL-   ii.   Given a knowledge base of PDFs, outline the flow of steps for a basic RAG flow
]
using LlamaIndex framework.
2,4
iii.   Explain context augmentation with reference to LlamaIndex.
Solution:
(Comparison: 3 marks, flow of steps: 4 marks, context augmentation: 3 marks)
•   Any three points:
ii.
• Context augmentation
•   Indexing stage
•   Storing
• Vector stores
• Embeddings
• Query
•   Retrieval
•   Post processing
iii.
In RAG, you add the right context (snippets, tables, section summaries) to the user’s
prompt before generation so the LLM answers grounded in your PDFs, not its pretraining.
LlamaIndex provides building blocks to retrieve, refine, and pack that context
automatically.
Why it matters: Improves faithfulness, keeps prompts short, and makes outputs auditable
(citations).
• Any three to be mentioned
********** 11 **********

[Text in pictures on this page, read by OCR]
Feature Llamaindex LangChain

Primary Focus [Search and retrieval Flexible LLM-powered application development
Data Indexing Highly efficient Modular and customizable

Retrieval Algorithms Advanced and optimized Integrated with LLMs for context-aware outputs

User Interface Simple and user-friendly [Comprehensive and adaptable

Integration Multiple data sources, seamless platform integration |Supports diverse Al technologies and services
[Customization Limited, focused on indexing and retrieval Extensive, supports complex workflows

[Context Retention Basic /Advanced, crucial for chatbots and long interactions

Use Cases Internal search, knowledge management, enterprise solutions | Customer support, content generation, code documentation
Performance JOptimized for speed and accuracy Efficient in handling complex data structures

Lifecycle Manage Integrates with debugging and ng tools [Comprehensive evaluation suite (LangSmith)
--- page 12 ---
• Query rewriting/expansion: QueryTransform / multi-query retrievers reformulate
the question (synonyms, constraints) to catch missed matches.
•   Contextual compression: A compressor retriever asks a small LLM to trim each
Node down to just the relevant sentences, shrinking tokens while keeping evidence.
• Sentence windowing: Add surrounding sentences (±N) for local coherence
(definitions, scope statements).
• Auto-merging / hierarchy: Start with fine chunks; automatically merge adjacent
Nodes when the query requires broader context (policies often span clauses).
•   Reranking: Use LLMRerank or a cross-encoder to re-order candidates so the top
few are truly on-topic.
• Metadata   filters: Constrain by   fields   like quarter=Q4, region=APAC,
doc=Policy_v3.pdf to cut noise.
•   Citation mode: Response synthesizer inserts Node IDs/page refs inline so
augmented context is visible and auditable.
• Packing for token budget: Context packers choose the max-value set of Nodes that
fit (e.g., 2–5 best snippets instead of a wall of text).
•   Conversational memory: Conversational Query Engine/memory objects carry prior
turns (e.g., “use last quarter only”) and inject that into retrieval.
Q5
CO-3;   a.   i.   Compare Simple Retrieval Augmented Generation (RAG) and advanced RAG. [10
BL-4   ii. A company is building a regulatory-compliance assistant for a multinational
]
bank. The knowledge base contains versioned policy PDFs (hundreds of
pages), FAQ wikis, and incident reports. Queries arrive in English and Hindi,
often vague (“What’s the large-cash deposit limit in Q4 for APAC?”) and
sometimes contradictory (users paste old screenshots). The system must return
grounded answers with section-level citations, prefer the latest effective
version of a policy, and keep p95 latency < 1.2s.
• Suggest an advanced RAG stack for this assistant.
• Highlight the significance of each step in advanced RAG with respect to
this assistant.
Solution:
(Comparison: 4 marks, scenario-based question: 6 marks (advanced RAG stack: 3
marks, significance of each step: 3 marks)
o Comparison of Simple RAG and Advanced RAG (Any 4 correct points)
Dimension   Simple RAG (baseline)   Advanced RAG (production-grade)
Single dense retriever (top-
Retrieval   Hybrid (with metadata filters)
k)
Query rewriting / multi-query (synonyms,
Query handling Raw user query
acronyms, translations)
Sentence/section-aware, token-capped,
Chunking   Fixed-length chunks
overlap tuned
Cross-encoder / LLM reranker to refine
Reranking   None (accept top-k)
top-k → top-m
All retrieved chunks stuffed Contextual compression (keep only salient
Context size
into prompt   sentences)
Required, fine-grained
Citations   Optional, coarse (doc-level)
(DocID/Version/§/Page or span quotes)
Versioning &   Version guards (latest-valid policy),
Not enforced
freshness   freshness filters
********** 12 **********
--- page 13 ---
Abstains/asks clarifying Qs when evidence
Answerability   Always answers
is weak or stale
Lang detect + bilingual
Multilingual   Assumes single language
embeddings/translate-then-search
Policy checks (PII, compliance), template-
Guardrails   Minimal
constrained outputs
Full tracing (retrieved IDs/scores, prompts,
Observability   Little to no tracing
citations, lat/$$)
Lower but noisy (long   Similar or lower via compression; added
Latency & cost
prompts)   rerank cost offset by smaller prompts
Off-topic context,
Typical failure   Reduced hallucinations, better
hallucinated specifics, stale
modes   recall/precision; higher setup complexity
answers
ii.
a) Advanced RAG stack for the compliance assistant
Advanced RAG works as a sequential step-based process as follows:
• Query processing:
Upon the reception of a user query, it is transformed into a high-
dimensional vector by using the embedding model that captures the
semantic meaning of the query.
• Document retrieval:
The encoded query traverses a huge knowledge database that provides
hybrid retrieval by using both dense vector search and sparse retrieval that
is, semantic similarity and keyword-based search.
The results thus introduce semantic keyword matches into the retrieved
documents.
• Reranking retrieved documents:
The retriever gives a final score based on context and in relation to the
query retrieving the documents.
• Contextual fusion for generation:
Because each document is encoded differently, the decoder fuses all
encoded contexts to ensure that the generated responses have coherence
with to the encoded query.
• Response generation:
The generator of advanced RAG, usually an LLM provides the answer
based on the retrieved documents.
• Feedback loop:
********** 13 **********
--- page 14 ---
As advanced RAG uses various techniques like active learning,
reinforcement learning and retriever-generator co-training to continuously
enhance its performance.
During this phase implicit signals occur, such as clicks on retrieved
documents that infer relevance causing explicit feedback that includes
corrections or ratings for further application during generation.
b) Why each step matters for THIS assistant
• Query understanding + multi-query rewriting: Users are often vague or
contradictory. Extracting entities and generating paraphrases (including
translation) boosts retrieval hit-rate without relying on users to be exact.
•   Ingestion & normalization: Policies are versioned and regional. Capturing
effective_date, version, region in metadata is the only way to prefer the latest
valid policy and to filter for APAC.
•   Sentence/section-aware chunking: Regulations have clause-level meaning;
keeping §/page boundaries makes section-level citations precise and reduces
hallucinations.
• Reranking (cross-encoder): In long policies, initial top-k can be near-misses. A
cross-encoder optimizes semantic alignment at sentence level, lifting the truly
relevant clauses.
• Contextual compression: Keeps prompts short while increasing the density of on-
point evidence, which improves faithfulness.
•   Metadata-filtered retrieval: Ensures answers aren’t stale even if the corpus
contains old PDFs or screenshots.
•   Answerability/abstention: Prevents confident wrong answers when evidence is
missing or outdated—protects trust and regulatory posture.
•   Observability & performance tactics: Tracing retrieved IDs/scores and citations
lets you debug false positives/negatives; parallel retrieval + small reranker +
caching keep the latency SLA.
CO-4;   b.   i. Briefly explain the forward diffusion process in Denoising Diffusion   [10
BL-2   Probabilistic Models (DDPM).
]
ii. Compare Hierarchical VAE and DDPMs.
iii. What is the ELBO connection in DDPM training?
Solution:
(forward diffusion process: 4 marks, Comparison: 4 marks, ELBO: 2 marks)
i.
ii.
********** 14 **********

[Text in pictures on this page, read by OCR]
The Diffusion (Encoding) Process

The known forward process Xo — Xs
T

q(x11|x0) = I] q(%t|%t-1) Probability Chain Rule (Markov Chain)
t=1

/

Notation: A Gaussian distribution “for” x,

0<f, < By <- < By < 1, typical value range [0.0001, 0.02], with T = 1000
--- page 15 ---
Any 3 correct points)
Aspect   Hierarchical VAE (HVAE)   Diffusion (DDPM)
Latent   Many (hundreds–thousands) steps; acts
Few learned stochastic layers
structure   like an ultra-deep latent chain
Also an ELBO (under fixed forward
Maximizes ELBO with
Training   process); implemented as noise-
reconstruction + KL per layer;
objective   prediction MSE; avoids posterior
risks posterior collapse
collapse by construction
Typically Gaussian with   Gaussian reverse transitions with
Conditionals
learned means/vars   learned mean (often fixed variance)
Long iterative denoising (many steps)
Short ancestral path (few
Sampling path   → typically slow; can use accelerators
layers) → fast at inference
(DDIM, distillation)
ELBO-based with fixed forward; exact
Likelihood   Tractable ELBO; explicit latent
likelihood uncommon but bound
handling   prior (often standard Normal)
available
Stronger global latent   Strong fidelity/diversity; excels at high-
Inductive
bottlenecks; good for   quality generation and editing
behavior
representation learning   (inpaint/super-res)
Can be tricky (KL annealing,   Generally stable to train; no adversarial
Stability
collapse)   dynamics
Add to encoder/decoder or
Conditioning   Classifier/classifier-free guidance or
prior (cVAE); learned
(labels, text)   cross-attention; strong controllability
alignment
Efficient sampling, modest
Data/compute   Heavier inference cost; superb detail
compute; may underfit fine
trade-off   and mode coverage
details
iii.
DDPMs maximize a variational lower bound (ELBO) on the data log-likelihood by
treating the fixed forward noising q(xt∣xt−1) as the inference model and the learned
reverse pθ(xt−1∣xt) as the decoder. The ELBO decomposes into a sum of per-timestep
KL/reconstruction terms; under common choices (fixed variances, reweighting), this
reduces to the familiar noise-prediction MSE loss
which is equivalent to denoising score matching. So the standard DDPM training
objective is precisely an ELBO surrogate for likelihood maximization.
Q6
********** 15 **********
--- page 16 ---
a.   i. CNNs and LVMs are both used for computer vision applications. Compare their [10
CO-2;   performance for these applications.
]
BL-2   ii. Consider a ViT using 16×16 patches on a 256×256 RGB image.
a. Compute the number of patches N.
b. Compute the flattened patch vector dimension.
c.   If a [CLS] token is prepended, what is the Transformer input sequence
length?
iii. How do the results on ViT compare with that of ResNet?
iv. Briefly describe token-based distillation in DeiT. What extra token is introduced,
what supervision it receives, and why this helps data-efficient training compared
to vanilla ViT.
Solution:
(Each sub question for 2.5 marks)
i.
CNNs(Convolutional Neural
Aspect   LVMs(Large Vision Models)
Networks)
Competitive performance,   Higher accuracy and
Performance
faster inference, task-specific   generalization but slower
Computational   More efficient, can run on   High GPU/TPU requirements,
Cost   mobile/edge devices   costly at scale
Scales well on fixed-size   Highly scalable with vast data
Scalability
tasks, less generalizable   and new tasks
Deployment   Mature tooling, easier   Higher infrastructure cost,
Complexity   optimization, and deployment complex to deploy
Typically faster, suited to   Slower inference needs
Latency
real-time applications   optimization
More interpretable via   Harder to interpret, post-hoc
Interpretability
feature/activation maps   analysis
Generally cheaper in both   Higher deployment and compute
Cost
training and inference   costs
Suitable for specific, well-   Best for multimodal, few-shot,
Use Case Fit
defined image tasks   large-scale tasks
ii.
a) N=256/16×256/16=16×16=256 patches.
b) Flattened patch dim =16×16×3=256×3=768
c) With a prepended [CLS], sequence length =N+1=257.
********** 16 **********
--- page 17 ---
iii.
iv.
DeiT’s token-based distillation (brief):
• Extra token: a learned distillation token ([dist]) is added alongside the usual
[CLS] and patch tokens.
•   Supervision: its output head is trained to match a teacher model’s class
probabilities (e.g., a strong CNN) via a distillation loss (KL / cross-entropy to the
teacher’s soft targets), while the [CLS] head still learns from ground-truth labels.
• Why it helps data efficiency: the [dist] token pulls in the teacher’s inductive
biases and richer soft labels, guiding attention and decision boundaries so ViTs
can reach high accuracy with only ImageNet-1k (no massive pretraining),
outperforming vanilla ViT trained from scratch.
CO-5;   b.   [10
BL-   i. A model assigns probabilities to a 3-token reference [ 0.5,   0.25,   0.125].
]
Compute cross-entropy (bits/token) and perplexity.
2, 3
ii. Given the pros and cons of automated vs. human evaluations, hybrid
approaches seek to get the best of both worlds. In practice, most LLM
evaluation setups are hybrid to some extent.
a. Briefly explain the different hybrid approaches that are used in practice.
b. Give a scenario where this hybrid approach can be used.
Solution:
(Numerical: 3 marks, ii. 7 marks (hybrid approaches: 5 marks, scenario: 2 marks)
It should be entropy and not cross entropy. Allot marks even if only perplexity is
calculated.
i. Cross-entropy (bits/token) H=−1/n∑ 𝑛 𝑖=1 𝑙𝑜𝑔2 pi.
Perplexity =  2H (equivalently =(∏𝑝𝑖 𝑖   −1/𝑛.)
Compute:
log2(0.5)=−1, log2(0.25)=−2, log2(0.125)=−3.
H=−1/3(−1−2−3)=−1/3(−6)=2.000 bits/token.
Perplexity=22=4.0.
Alternate method:
P(w) =0.5*0.25*0.125
P(w) = 0.156
Pnorm = p(w)1/N
********** 17 **********
--- page 18 ---
= (0.156)1/3
=0.25
Perplexity = 1/ Pnorm = 1/0.25 = 4
ii.   Brief explanation of any 5 of them
Human-in-the-loop + Automation: Use automated metrics or LLM judges to pre-screen
or rank outputs, then have humans focus on tricky cases. For example, if you have 1,000
outputs to evaluate, you might use a toxicity classifier to automatically mark any clearly
toxic outputs (and fail the model if any are found), use an LLM judge to score coherence
and flag the lowest 100 outputs, and then have human evaluators carefully review those
100 (plus a random sample of the rest to spot-check). This way, human effort is
concentrated where the model likely has problems, improving efficiency.
Blending qualitative and quantitative: While you might present overall automatic
metric scores to summarize performance, you also include qualitative analysis from
humans. Many research papers do this: "Model X achieved a BLEU of 0.25, close to
Model Y's 0.27. To further understand, we conducted a human study: raters preferred
Model X 55% of the time, citing more factual consistency, even though it had slightly
lower BLEU." The combination gives a fuller picture.
LLM-assisted human eval: Interestingly, LLMs can even help human evaluators. An
example: when humans evaluate long text (like a 5-page story by the model), it's hard to
keep track of everything. An LLM could summarize the story or highlight potential issues
(like "In paragraph 3, the model contradicted something from paragraph 1"). The human
then makes the final judgment using these pointers. The human is still the judge, but the
AI helps speed up the process.
Iterative eval and refinement: Hybrid evaluation can be part of the development cycle.
For instance, a workflow could be:
• Develop a new model version.
• Run automated tests/benchmarks (perplexity, BLEU, etc.) - if it's worse than
before on these, go back (regression).
•   If it passes, run an LLM-judge comparison against the old model on a variety of
prompts - get a quick sense of wins/losses.
•   If the new model seems better or comparable, do a small human eval on key
metrics to confirm quality.
•   If all looks good, deploy to a small user group and monitor real interactions
(perhaps with metrics like user rating, or measuring if the new model answers
questions that the old failed). This real-world data serves as further evaluation.
•   If that is positive, then fully launch the model.
• In this cycle, automated and human evaluations happen at different stages with
different scopes (offline vs online, small-scale vs large-scale).
Continuous feedback loop: In production, combining human and automated evaluation
in a loop can maintain model performance. For example, some customer service bots
allow users to rate answers or say "this was not helpful". Those signals can be aggregated
(automated analysis of human feedback) to find failure patterns. Then, either humans or
an LLM can go through those failure cases to categorize them (e.g., "Many failures are
about technical questions the bot couldn't handle"). This can inform the next training
iteration or prompt adjustment. Here, user (human) feedback is part of evaluation, and
automated analysis of that feedback helps identify where to improve.
Ensembling evaluators: Another hybrid idea is to use multiple evaluation methods on
the same outputs and treat the evaluation result as a combination. For instance, you might
require that a new model should improve on at least one automatic metric without
degrading others, and also be preferred by human judges. This multi-pronged criterion
********** 18 **********
--- page 19 ---
ensures you're not blindly optimizing one metric. If an output passes all automated
checks (no toxicity, high similarity to reference, etc.) but humans still dislike it, that flags
something the metrics missed.
Task-specific hybrid metrics: Sometimes a metric itself can be hybrid. For example,
consider evaluating a dialogue system. You might create a composite score that includes
a semantic similarity part (via BERTScore to a reference answer), a penalty for any rule
violations (via regex or classifier, e.g., if it said something forbidden), and a small bonus
if it uses polite wording (via a list of polite phrases). Such a metric mixes automated
components (embedding similarity, classification) that reflect human priorities (accuracy,
safety, politeness). The final "score" tries to approximate a human's holistic judgment. If
tuned well, such composite metrics can be useful to rank models before a final human
check.
Benchmark + human synergy: Use benchmarks to diagnose weaknesses, then human
creativity to design new tests. For example, if a model aces all standard math problems
but users still find it struggles with tricky word puzzles, evaluators can create new
adversarial examples (perhaps by hand or with an LLM's help) to add to the evaluation
set. Over time, this enriches the automated benchmark to include those human-identified
edge cases.
Task-specific hybrid metrics: Sometimes a metric itself can be hybrid. For example,
consider evaluating a dialogue system. You might create a composite score that includes
a semantic similarity part (via BERTScore to a reference answer), a penalty for any rule
violations (via regex or classifier, e.g., if it said something forbidden), and a small bonus
if it uses polite wording (via a list of polite phrases). Such a metric mixes automated
components (embedding similarity, classification) that reflect human priorities (accuracy,
safety, politeness). The final "score" tries to approximate a human's holistic judgment. If
tuned well, such composite metrics can be useful to rank models before a final human
check.
Benchmark + human synergy: Use benchmarks to diagnose weaknesses, then human
creativity to design new tests. For example, if a model aces all standard math problems
but users still find it struggles with tricky word puzzles, evaluators can create new
adversarial examples (perhaps by hand or with an LLM's help) to add to the evaluation
set. Over time, this enriches the automated benchmark to include those human-identified
edge cases.
iii.
A concrete scenario of hybrid eval: Suppose we built a medical FAQ bot with an LLM.
We might:
• Test it on a set of 100 known Q&A pairs (from a medical dataset) and measure
exact match or F1 (automated).
• Also measure BERTScore or semantic similarity to the reference answers
(automated).
• Have a medical professional review 50 of its answers for correctness (human).
• Use an LLM like GPT-4 to double-check those answers as well (LLM judge).
• Compare the professional's review with GPT-4's review: if they largely agree, we
might trust GPT-4 to screen more questions.
• After deployment, monitor user feedback: any low-rated answers are collected.
Periodically, have a human go through those to see what went wrong (e.g., was
the answer wrong, or was it correct but user didn't understand?).
• Feed those findings back into improving the model and also into our evaluation
set for the next version (closing the loop).
Q7
********** 19 **********
--- page 20 ---
CO-6;   a.   Define Agentic AI in one or two sentences and name two traits that distinguish it   [5]
BL-2   from a plain LLM. Give two examples where a tool call is essential and pure LLM
text generation would fail.
Solution: (Definition: 2 marks, examples: 1.5 marks each)
Agentic AI is an LLM-powered system that doesn’t just generate text—it perceives,
plans, and acts in a loop, using tools and memory to pursue goals autonomously under
constraints.
Two distinguishing traits
• Tool-using action loop: chooses and calls APIs/tools (search, DB, calendar,
payments), verifies results, and retries—beyond pure next-token generation.
•   Persistent state/memory: maintains and updates task state across steps/sessions
(plans, facts, user prefs), enabling multi-step, goal-directed behavior.
• Live flight booking + payment: Selecting specific flights at current prices, holding
seats, and charging a corporate card requires calling airline/GDS and payment APIs; an
LLM can’t transact or see real-time availability, so text-only guesses would be wrong.
• Querying an internal policy/database: Returning the latest effective per-diem (with
clause ID) demands a filtered query to the company’s policy store; an LLM without a
tool can only hallucinate or use stale training data, not verify the exact, current value.
CO-1; b.   A company has a 30-page compliance policy updated quarterly. They need concise,   [5]
BL-4   accurate 200-word summaries for executives.
• Outline a two-stage pipeline (chunking and synthesizing) specifying chunk
size, overlap, and how you’ll handle cross-section references.
• Draft a crisp prompt to get the 200-word summary.
• Suggest an evaluation metric for this.
Solution:
(pipeline: 2 marks, prompt: 2 marks, evaluation metric:1 mark)
Two-stage pipeline (chunk → synthesize)
• Chunking: Split the 30-page policy into ~800-token chunks with 100–150 token
overlap to avoid boundary loss.
• Per-chunk pass: For each chunk, extract meta data
•   Synthesis: Aggregate micro-summaries; de-duplicate by section ID; resolve cross-
references.
Prompt:
“Write a ~200-word executive brief of the policy.
Include: Scope, Key changes since last quarter (each with §ID), and Action items
(who/when).
Use only facts supported by the provided excerpts; quote section IDs like [§2.3].
If a required item is missing, state ‘Not specified.’
Evaluation metric: ROUGE or any similar.
CO-5; c   i.   Describe briefly hit rate.   [5]
BL-3   ii. You have 4 queries with the single correct node per query:
• Gold: Q1→N3, Q2→N7, Q3→N2, Q4→N5
• Retrieved@3:
o Q1: [N8, N3, N1]
o Q2: [N4, N6, N2]
********** 20 **********
--- page 21 ---
o Q3: [N2, N9, N7]
o Q4: [N5, N3, N8]
Compute HitRate@3 over the 4 queries.
iii. What are the challenges with hit rate as a metric?
Solution:
(Describing Hit rate: 2 marks, numerical: 2 marks, challenges: 1 mark)
i. Hit Rate is one of the measures used to assess how well recommendation systems
work. The desired item’s frequency of appearance in the top-N recommendations is
measured. Within the framework of RAG, Hit Rate denotes the frequency with
which pertinent data is successfully included into the output that is produced.
ii.
HitRate@3 = 3/4 = 0.75
Checks:
• Q1: gold N3 ∈ [N8, N3, N1] √
• Q2: gold N7 ∉ [N4, N6, N2] X
• Q3: gold N2 ∈ [N2, N9, N7] √
• Q4: gold N5 ∈ [N5, N3, N8] √
Hits = 3 out of 4 queries → 0.75 (75%).
iii. The major challenge that we face when using Hit Rate as our evaluation metric is
that it does not take into account the position of the retrieved node.
CO-6; d   iv. Contrast “reactive prompting” vs. “deliberate planning” in agents.   [5]
BL-2   v. State two ethical risks unique to autonomous agents vs. chat LLMs.
Solution: (2.5 marks each)
i.
Reactive prompting
• What it is: Single-step (or few-step) response to the current input—no explicit
plan or multi-step control flow.
• When it works: Simple Q&A, lookup-style tasks, or when a single tool call
suffices.
•   Pros: Fast, cheap, low engineering overhead.
• Cons: Brittle for multi-hop tasks; prone to omissions/hallucinations; no recovery
if a step fails.
Deliberate planning
• What it is: Explicit loop: perceive → plan → act (tools) → observe → reflect,
often with intermediate goals and conditional branching.
• When it works: Multi-step workflows (book → pay → confirm), ambiguous specs,
or tasks needing verification and retries.
•   Pros: Higher reliability, better decomposition, supports validation/guardrails and
error handling.
********** 21 **********
--- page 22 ---
• Cons: More latency/cost and orchestration complexity; requires state
management and evaluation beyond final text.
ii.
• Unsupervised real-world actions: Agents can execute tools/APIs (buy, delete,
transfer, post) without immediate human oversight, so mis-specification or bugs can
cause irreversible, real-world harm—far beyond a chat LLM’s text-only mistakes.
• Goal misspecification & reward hacking: Persistent, goal-seeking loops can
optimize the wrong proxy (e.g., “reduce tickets” by auto-closing them), leading to
perverse, deceptive, or unsafe behavior that a non-acting chat model wouldn’t
manifest.
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper eb595cbf5b32

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_AI_7051/GENERATIVE AI/ANS_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
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
1. This question paper contains 21 pages.
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
i.   The dimension of each head
ii.   The total concatenated dimension before final projection
iii.   The shape of the output after the final projection if sequence length is 20
Solution:
(Dimension of each head: 1-mark, total concatenated dimension: 1 mark, shape of
output: 2 marks)
i. Dimension of each head
dhead=dmodel/h=512/8=64
ii. Total concatenated dimension before final projection
Each of the 8 heads produces a vector of dimension 64, so after concatenation:
8×64=512
iii. Shape of the output after the final projection if sequence length is 20
The final linear projection maps the concatenated output back to dmodel=512
So for sequence length 20 the output shape is: 20×512
CO-1;   b.   i. Compare data generation and data classification tasks in AI.   [5]
BL-4   ii. State the key characteristics of Generative AI models.
Solution:
(Comparison: 3 marks, characteristics: 2 marks)
Aspect   Data generation   Data classification
********** 1 **********
--- page 2 ---
Main goal   Create new data samples   Assign an input to a known
class/label
Output   New text, image, audio, video, A category such as spam/not
etc.   spam, cat/dog,
positive/negative
Nature of   Constructive / creative   Predictive / decision-making
task
Example   Generate an image of a sunset   Classify an image as cat or dog
Learning   Learn the underlying data   Learn boundaries between
focus   distribution   classes
Common   GANs, VAEs, diffusion   Logistic regression, SVM,
models   models, autoregressive models CNNs, classifiers
Evaluation   Quality, realism, diversity,   Accuracy, precision, recall, F1-
similarity metrics   score
Key Characteristics:
1. Content Creation: Generates human-like text, realistic images, or other forms of
media.
2. Versatility: Can be applied across industries, including education, entertainment,
healthcare, and more.
3. Interactivity: Adapts to user prompts or contextual inputs to generate meaningful
and personalized outputs.
CO-5;   c. A retriever is tested on 3 queries. The top-5 retrieved relevance labels are:   [5]
BL-3   Q1: [0,1,0,0,1], total relevant docs = 3
Q2: [1,0,0,1,0], total relevant docs = 2
Q3: [0,0,0,1,0], total relevant docs = 4
Compute:
a. Hit Rate across the 3 queries
b. MRR across the 3 queries
c. Precision@5 for each query
d. Recall@5 for each query
e. average Precision@5 and average Recall@5
Solution:
(1 mark for each bit)
1. Hit Rate
A query is a hit if at least one relevant document appears in the top-5.
Q1: [0,1,0,0,1] → hit
Q2: [1,0,0,1,0] → hit
Q3: [0,0,0,1,0] → hit
Hit Rate=3/3=1.0
2. MRR
MRR uses the rank of the first relevant document.
Q1: first relevant at rank 2
RR1=1/2=0.5
********** 2 **********
--- page 3 ---
Q2: first relevant at rank 1
RR2=1/1=1
Q3: first relevant at rank 4
RR3=1/4=0.25
Now average:
MRR=0.5+1+0.253=1.75/3=0.5833
3. Precision@5 for each query
Precision@5=relevant docs in top 5
Q1
Relevant docs in top 5 = 2
P@5=2/5=0.4
Q2
Relevant docs in top 5 = 2
P@5=2/5=0.4
Q3
Relevant docs in top 5 = 1
P@5=15=0.2
4. Recall@5 for each query
Recall@5=relevant docs in top 5
Q1
Relevant retrieved = 2, total relevant = 3
R@5=2/3=0.6667
Q2
Relevant retrieved = 2, total relevant = 2
R@5=22=1.0
Q3
Relevant retrieved = 1, total relevant = 4
R@5=1/4=0.25
5. Average Precision@5
Average Precision@5=0.4+0.4+0.23=1.0/3=0.3333
6. Average Recall@5
Average Recall@5=0.6667+1.0+0.253=1.9167/3=0.6389
CO-3;   d.   Consider Hierarchical Navigable Small World (HNSW) algorithm being implemented   [5]
BL-3   with the two settings as given below:
Setting   M   efConstruction   efSearch
A   32   200   50
B   64   400   200
Determine:
i.   Which case is expected to give higher recall?
ii.   Which case is expected to use more memory?
iii.   Which case is expected to answer faster?
iv.   Which case is more suitable for real-time production?
v.   Which case is better for research or accuracy-critical tasks?
********** 3 **********
--- page 4 ---
Solution:
(1 mark for each bit)
i. Which case is expected to give higher recall?
Case 2, because higher M gives a denser graph and better recall, and higher efSearch
explores more candidates at query time, improving top-k accuracy.
ii. Which case is expected to use more memory?
Case 2, because higher M increases the number of connections stored per node, so
memory usage increases.
iii. Which case is expected to answer faster?
Case 1, because lower efSearch means fewer candidate neighbors are explored, so
latency is lower. Larger efSearch makes search slower because more nodes are visited.
iv. Which case is more suitable for real-time production?
Case 1, because the notes explicitly recommend keeping efSearch smaller for production
(real-time queries) to get faster responses.
v.Which case is better for research or accuracy-critical tasks?
Case 2, because the notes explicitly recommend increasing efSearch for
research/accuracy-critical tasks to improve accuracy.
Q2
CO-2;   a.   i.   Highlight the different steps in building a foundation model.   [10]
BL-   ii. Compare foundation models and large language models.
2,3   iii. Consider a LLM which works on auto regressivity, for a sample x= [1,1,0], the
predicted probabilities are as given below:
p(x1=1) =0.9,
p(x2 =1∣x1 )=0.8,
p(x3 = 0∣x1 ,x2 )=0.4
Compute the joint probability.
Solution:
(Steps in building LLM: 4 marks, Comparison: 4 marks, numerical: 2 marks)
i.   Brief explanation of each step:
ii.
********** 4 **********
--- page 5 ---
iii.
Using autoregressive factorization:
p(x)=p(x1) p(x2∣x1) p(x3∣x1,x2)
Given:
p(x1=1) =0.9,
p(x2 =1∣x1 )=0.8,
p(x3 = 0∣x1 ,x2 )=0.4
So,
p([1,1,0])=0.9×0.8×0.4 =0.288
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
Solution:
(2 marks for each bit)
1) Candidate A: “He was extremely happy last night”
Candidate A unigrams:
[He, was, extremely, happy, last, night]
So,
∣CA∣=6
Exact unigram overlaps with the reference:
********** 5 **********

[Text in pictures on this page, read by OCR]
Aspect Foundational Model Large Language Model

Subset of Foundational Models trained
General-purpose models that are generally

Scope . . exclusively on text data, and sometimes
trained on multimodal data. 5 as
fine-tuned for a specific task.
Training Data Diverse (and generally multimodal) datasets. Primarily text corpora.

Multiple architectures: Transformers,

Architecture Convolutional Neural Networks (CNNs), or Typically Transformer-
hybrid architectures depending on the data based architecture.
type.

Focused on language tasks: translation,
summarization, chatbot, code
generation, etc.

Popular across society nowadays. Find
the most popular open-source models in
our guide.

Use-cases Multimodal general tasks.
--- page 6 ---
[He, was, happy, last, night]
Number of matches:
mA=5
ROUGE-1 for Candidate A
Using unigram precision, recall, and F1 as in the ROUGE-1 examples from the notes,
PA=5/6=0.8333
RA=5/5=1.0
ROUGE-1A=2(PARA)/(PA+RA)= 2(0.8333*1.0)/(0.8333+1.0) ≈0.9091
BLEU-1 for Candidate A
BLEU uses unigram precision, and with one reference and no brevity penalty here
because the candidate is longer than the reference,
BLEU-1A=5/6=0.8333
2) Candidate B: “He was joyful yesterday evening”
Candidate B unigrams:
[He, was, joyful, yesterday, evening]
∣CB∣=5
Exact unigram overlaps with the reference:
[He, was]
Number of matches:
mB=2
ROUGE-1 for Candidate B
PB=2/5=0.4
RB=2/5=0.4
ROUGE-1B= 2(PBRB)/(PB+RB) = 2(0.4*0.4)/(0.4+0.4)=0.4
BLEU-1 for Candidate B
Candidate length = reference length, so brevity penalty is 1.
BLEU-1B=2/5=0.4
BLEU-1 is harsher here, especially for Candidate A, because it is mainly precision-
oriented and penalizes extra words like “extremely.” ROUGE-1, as used here, balances
precision and recall, so Candidate A gets a higher score because it preserves all the
reference words and only adds one extra word.
For Candidate B, both scores are the same because:
•   candidate and reference have the same length
•   exact unigram overlap is only 2 words
So precision and recall both become 0.4. Also, both BLEU and ROUGE are
limited by surface exact matches, so words like joyful and yesterday evening do
not get credit even though they are semantically related to happy and last night.
Q3
********** 6 **********
--- page 7 ---
CO-3;   a.   i.   Show with examples any two types of chunking strategies as used in the   [10]
indexing phase of RAG.
BL-4
ii.   Justify the significance of reranking, filtering, and contextual fusion in
advanced RAG pipelines.
iii.   Analyze why pre-retrieval and post-retrieval processing can improve answer
quality in complex enterprise applications.
Solution:
(Examples: 1.5 marks, significance: 4.5 marks, pre-retrieval and post-retrieval
processing: 4 marks)
i. Any two chunking strategies in the indexing phase of RAG, with examples
In the indexing phase of RAG, documents are broken into smaller chunks before
embeddings are created and stored. The slides show several chunking strategies such as
fixed-size, sentence-based, paragraph-based, sliding window, heading-based, and
semantic/embedding-based chunking.
1. Fixed-size chunking
Here, the document is split into chunks of a fixed number of words or tokens.
Example: if a paragraph has 60 words and we use 20 words per chunk, it becomes:
Chunk 1: words 1–20
Chunk 2: words 21–40
Chunk 3: words 41–60
The slides give a similar example where a paragraph on vector databases is broken into
fixed-size 20-word chunks.
2. Sliding-window chunking
Here, chunks overlap so that information near boundaries is not lost.
Example: with window size = 20 words and overlap = 5 words:
Chunk 1: words 1–20
Chunk 2: words 16–35
Chunk 3: words 31–50
The slides show this as a more advanced indexing strategy because overlapping chunks
preserve continuity better than strict fixed-size splitting.
You could also mention sentence-based chunking, where each sentence becomes a
chunk, or paragraph-based chunking, where the whole paragraph is stored as one chunk.
ii. Significance of reranking, filtering, and contextual fusion in advanced RAG
In advanced RAG, retrieval is not treated as a one-step process. After documents are
retrieved, extra stages such as reranking, filtering, and contextual fusion improve the
quality of the final answer.
Reranking
Reranking reorders the retrieved documents so the most relevant ones appear first. This
is important because the first-stage retriever may return approximate matches, but
reranking refines the ranking using stronger relevance signals.
Filtering
Filtering removes irrelevant, redundant, stale, or low-quality retrieved content. In
enterprise settings, this is useful for excluding documents that do not satisfy metadata,
recency, or relevance constraints.
Contextual fusion
Contextual fusion combines the useful retrieved information into a coherent context
before generation. Since each retrieved document may contain only part of the answer,
fusion helps the generator produce a more complete, grounded, and consistent response.
Justification
• improve retrieval relevance
• reduce noise
• provide the LLM with better evidence
********** 7 **********
--- page 8 ---
• increase answer accuracy and coherence
iii. Why pre-retrieval and post-retrieval processing improve answer quality in complex
enterprise applications
Complex enterprise applications often deal with:
•   large document collections
• multiple sources
• changing policies
•   strict relevance and compliance requirements
So basic retrieval alone is often not enough. Advanced RAG adds:
•   pre-retrieval processing such as query rewriting, summaries, routing, and
confidence judgment
•   post-retrieval processing such as reorder, filter, and content refinement.
Why pre-retrieval helps
Pre-retrieval improves the query before searching. If the user’s request is vague,
incomplete, or ambiguous, rewriting and routing help the system search in the right way
and in the right data source. This increases the chance of retrieving the correct evidence.
Why post-retrieval helps
Post-retrieval improves the retrieved results before generation. Retrieved chunks may be
partially relevant, duplicated, or noisy. Reordering, filtering, and refinement ensure that
only the best evidence is passed to the LLM.
CO-2; b.   i. Compare encoder only models and decoder only models in LLMs.   [10]
BL-   ii. Analyze how in-context learning in GPT-3 differs from the earlier GPT models,
3,4   and evaluate its significance for NLP.
iii. A company wants to use GPT-3 for sentiment classification without fine-tuning.
Explain how in context learning can be used for this task, and give an example
prompt with sample input-output pairs.
Solution:
(Comparison: 3 marks, in-context learning: 3 marks, example for sentiment
classification: 4 marks)
i.
Aspect   Encoder-only models   Decoder-only models
Context used   Bidirectional: can see both   Left-to-right only: sees only
left and right context   previous tokens
Main   Masked Language Modeling   Next-token prediction
objective   + NSP in BERT
Best suited   Understanding tasks such as   Generation tasks such as text
for   classification, NLI, token   completion, dialogue, stories,
labeling   code
Architecture BERT   GPT, GPT-2, GPT-3
example
Strength   Better full-sentence/context   Better fluent autoregressive
understanding   generation
Limitation   Not inherently generative   Lacks bidirectional context, so
weaker for some understanding-
heavy tasks
ii.
Earlier GPT models, especially GPT-1, mainly followed a pretraining + supervised fine-
tuning paradigm. GPT-1 learned a generative language model on unlabeled text, then
adapted to downstream tasks using labeled data and task-specific input transformations.
********** 8 **********
--- page 9 ---
GPT-3 shifts this idea significantly. Its key concept is in-context learning: instead of
updating model parameters for each new task, the model is given a task description and
a few examples inside the prompt, and it infers the pattern from those examples while
generating the answer. The unit explicitly says GPT-3 matches the pattern of the
examples with what it learned during pretraining and then uses that knowledge to
perform the task. It also notes that few-shot, one-shot, and zero-shot performance
improve with model scale.
Significance for NLP
This is important because it reduces the need for:
•   collecting task-specific labeled datasets
•   separate fine-tuning for every new task
• designing many task-specific models
It makes one large model more adaptable, general-purpose, and flexible across
summarization, translation, QA, sentiment analysis, and other tasks. The unit also states
that GPT-3 often performs better in few-shot settings than in one-shot or zero-shot
settings, showing the practical value of in-context learning for NLP.
iii.
A company can use GPT-3 for sentiment classification by giving it:
•   a short instruction describing the task
•   a few labeled examples inside the prompt
•   a new unlabeled review to classify
Here, the model is not fine-tuned. Instead, it uses the examples in the prompt to infer the
pattern and predict the correct sentiment label. This matches the unit’s description of
few-shot learning: the model is given a task description and as many examples as fit in
the context window.
Example prompt
Classify the sentiment of each review as Positive or Negative.
Review: The movie was amazing and very engaging.
Sentiment: Positive
Review: The product stopped working after two days.
Sentiment: Negative
Review: The food was delicious and the service was excellent.
Sentiment: Positive
Review: The laptop battery drains too quickly and performance is poor.
Sentiment:
Expected output
Negative
Q4
CO-3;   a.   Locality Sensitive Hashing (LSH) is used for comparing two document indexes in RAG: [10]
BL-3   • Doc1 = "machine vision"
• Doc2 = "machine revision"
********** 9 **********
--- page 10 ---
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
Solution:
(2 marks for each sub point)
1) Set of 2-shingles
Doc1 = "machine vision"
2-shingles:
S1={ma, ac, ch, hi, in, ne, e_, _v, vi, is, si, io, on}
Doc2 = "machine revision"
2-shingles:
S2={ma, ac, ch, hi, in, ne, e_, _r, re, ev, vi, is, si, io, on
2) Jaccard similarity and distance
Intersection
Common shingles:
S1∩S2={ma, ac, ch, hi, in, ne, e_, vi, is, si, io, on}
So,
∣S1∩S2∣=12 |
Union
All unique shingles:
S1∪S2={ma, ac, ch, hi, in, ne, e_, _v, vi, is, si, io, on, _r, re, ev}
So,
∣S1∪S2∣=16
Jaccard similarity
J(S1,S2)=∣S1∩S2∣/∣S1∪S2∣=12/16=0.75
Jaccard distance
d(S1,S2)=1−J(S1,S2)=1−0.75=0.25
3) Characteristic matrix
Row Shingl   Doc1 Doc2
e
0 ma   1   1
1 ac   1   1
2 ch   1   1
3 hi   1   1
4 in   1   1
5 ne   1   1
6 e_   1   1
7 _v   1   0
8 vi   1   1
9   is   1   1
10   si   1   1
11 io   1   1
********** 10 **********
--- page 11 ---
12 on   1   1
13 _r   0   1
14 re   0   1
15 ev   0   1
4) Signature matrix
Given:
H1(x)=(x+1) mod 19
H2(x)=(3x+1) mod 19
H3(x)=(4x+2) mod 19
Row Shingl (H_1)   (H_2)   (H_3)
e
0 ma   1   1   2
1 ac   2   4   6
2 ch   3   7   10
3 hi   4   10   14
4 in   5   13   18
5 ne   6   16   3
6 e_   7   0   7
7 _v   8   3   11
8 vi   9   6   15
9   is   10   9   0
10   si   11   12   4
11 io   12   15   8
12 on   13   18   12
13 _r   14   2   16
14 re   15   5   1
15 ev   16   8   5
MinHash signature for Doc1
Doc1 has rows 0 to 12.
Minimum under H1 = 1
Minimum under H2 = 0
Minimum under H3 = 0
So,
Sig(D1)=[1, 0, 0]
MinHash signature for Doc2
Doc2 has rows 0,1,2,3,4,5,6,8,9,10,11,12,13,14,15
Minimum under H1 = 1
Minimum under H2 = 0
Minimum under H3 = 0
So,
Sig(D2)=[1, 0, 0]
Signature matrix
MinHash uses matching signature values to estimate Jaccard similarity.
5) Are they likely near-duplicates under LSH banding?
Yes.
********** 11 **********
--- page 12 ---
Because the two signatures are identical:
[1,0,0]=[1,0,0]
they will match in every band under any normal banding scheme, so they will definitely
become a candidate pair under LSH. Since the true Jaccard similarity is also fairly high:
0.75
the documents are likely near-duplicates.
CO-2;   b.   i. Compare the two LLM frameworks LangChain and LlamaIndex, on the basis of their [10]
BL-   primary focus, data indexing, use cases and performance.
2,3   ii. Highlight a typical LlamaIndex workflow.
iii. A hospital wants doctors to query clinical documents and reports efficiently. Briefly
explain how LlamaIndex can help in this use case.
Solution:
(Comparison: 4 marks, LlamaIndex workflow: 4 marks, use case: 2 marks)
i.
Basis   LangChain   LlamaIndex
Primary   Flexible framework for LLM-   Primarily focused on search and
focus   powered application   retrieval over large datasets
development
Data   Supports vector stores and   Highly efficient indexing of
indexing   retrieval, but indexing is not its   structured and unstructured data
main specialization   for querying
Use cases   Chatbots, customer support,   Internal search, document Q&A,
content generation, virtual   knowledge management,
agents, complex workflows   enterprise retrieval, RAG
Performanc   Efficient for handling complex   Optimized for speed and accuracy
e   workflows and data structures   in retrieval and search
ii.
A typical LlamaIndex workflow is:
1. Data Loading
External data such as documents, PDFs, or databases is loaded into the system.
2. Indexing
The data is organized into structured indexes and converted into embeddings so
it becomes searchable. This stage prepares the knowledge base for efficient
retrieval.
3. Storing
The created index can be stored or persisted so that it does not need to be rebuilt
every time.
4. Querying / Retrieval
When the user asks a query, the system searches the index and retrieves the most
relevant chunks using semantic similarity, often via top-kkk retrieval.
5. Postprocessing
Retrieved nodes or chunks may be reranked, filtered, or transformed to improve
relevance.
********** 12 **********
--- page 13 ---
6. Response Synthesis
The query and retrieved information are passed to the LLM, which generates the
final response.
iii.
LlamaIndex can help by turning the hospital’s clinical documents, reports, and records
into searchable indexes so doctors can ask questions in natural language and quickly
retrieve the most relevant information. It is especially suitable here because its main
strength is external knowledge integration, indexing, and efficient retrieval from large
document collections.
In this use case, the workflow would be:
•   load clinical reports and documents into the system
• index them into a searchable structure using embeddings
• when a doctor asks a query, retrieve the most relevant chunks based on semantic
similarity
•   pass those retrieved snippets to the LLM to generate a context-aware answer
This is useful in a hospital because it improves speed, relevance, and retrieval accuracy
when searching through large volumes of medical text, instead of requiring doctors to
manually scan many files.
Q5
CO-1;   a. Compare image understanding and language generation in multimodal systems.   [5]
BL-2
Solution:
(Any 5 correct points)
Aspect   Image understanding   Language generation
Main purpose   Extract meaning from visual input   Produce text based on visual and
textual context
Input focus   Images or video frames   Usually image features plus
optional text prompt/context
Core module   Image encoder such as ViT extracts   Decoder-only language model
visual features from image patches   generates output tokens
autoregressively
What it learns   Objects, scenes, relations, spatial   Descriptions, answers, captions,
patterns, visual semantics   explanations in natural language
Representation Converts image into   Uses shared visual-textual
embeddings/tokens   embeddings to generate text
Output type   Internal visual representation or   Text output such as captions,
prediction like   VQA answers, retrieval text,
classification/detection   explanations
Typical tasks   Classification, detection,   Captioning, visual question
segmentation, identifying objects in   answering, text-based response
an image   generation
Role in VLM   First “understands” the image   Then “expresses” that
pipeline   understanding in language
********** 13 **********
--- page 14 ---
CO-6;   b.   i.   Differentiate between reactive agents and proactive agents.   [10]
BL-   ii. Explain the terms reactive prompting and deliberate planning in agents.
2,4   iii. A company wants to deploy a travel and expense assistant. Analyze how the agent
should behave in each of the four stages: perceive, plan, act, and reflect.
Solution:
(Differentiate: 3 marks, explaining the terms: 3 marks, four stages: 4 marks)
i. Differentiate between reactive agents and proactive agents
Reactive agents simply respond to the environment or a user’s request. They are suitable
for narrow, repetitive, or immediate-response tasks.
Proactive agents go beyond responding. They plan ahead, anticipate needs, and take
initiative to achieve outcomes without requiring constant prompting.
ii. Explain reactive prompting and deliberate planning in agents
Reactive prompting
Reactive prompting means the agent gives a single-step or few-step response to the
current input, without building an explicit plan or using a multi-step control flow. It
works well for simple Q&A, lookup tasks, or cases where one tool call is enough. Its
advantages are speed, lower cost, and simpler engineering, but it is brittle for multi-step
tasks and has poor recovery when a step fails.
Deliberate planning
Deliberate planning means the agent follows an explicit loop such as:
perceive→plan→act→observe→reflect
It is suited for multi-step workflows, ambiguous requests, verification-heavy tasks, and
retry logic. Its advantages are better reliability, validation, decomposition, and error
handling, but it increases latency, cost, and orchestration complexity.
iii. Travel and expense assistant: analyze behavior in perceive, plan, act, and reflect
For a travel and expense assistant, the document gives a concrete T&E example where
the agent has access to flights API, hotels API, company policy database, calendar, and
corporate card tool.
At the perceive stage, the agent should observe and understand the request by
extracting:
•   travel route
•   dates and time constraints
•   hotel location constraints
• expense/per-diem needs
• booking and reimbursement intent
It should also fetch relevant memory/context such as:
• home airport
•   preferred airlines
•   calendar availability
• company travel policy
•   prior user preferences
It must identify ambiguities and ask clarification questions if needed, for example if the
client office address is unclear or if policy-related details are missing. The document
says perceive should parse the goal and context, normalize them into task state, and
clarify ambiguous goals when necessary.
********** 14 **********
--- page 15 ---
At the planning stage, the agent should break the goal into a minimal actionable
workflow. For example:
1. check calendar availability
2. retrieve company travel and expense policy
3. search flights for outbound and return travel
4. search hotels near the client office
5. verify whether options satisfy fare caps, hotel distance, and per-diem policy
6. estimate reimbursement/per-diem
7. book travel and hotel
8. file the request
It should decide which tools to call and define acceptance criteria such as:
•   airfare within policy cap
•   correct travel times
•   hotel within allowed distance
•   valid per-diem rate
•   calendar has no conflict
The document states that planning should decompose the task, choose tools/APIs, define
execution order, and set stop/success criteria.
At the act stage, the agent should execute the plan using the available tools in the correct
sequence:
•   call the calendar tool to check availability
• query the policy database for airfare caps, hotel rules, and per-diem
•   call the flights API for valid travel options
•   call the hotels API for nearby hotels
• use the corporate card tool only after policy validation
• submit the reimbursement/request
While acting, it should:
• handle retries and timeouts
•   validate outputs against policy constraints
•   enforce schema checks and guardrails
• update intermediate state such as shortlisted itinerary, policy hits, and estimated
cost
The document emphasizes that the act stage should call tools with structured inputs,
enforce policy checks, integrate results into state, and branch if results fail validation.
At the reflect stage, the agent should verify and finalize. It should:
•   cross-check the booking against the user’s calendar
•   verify policy compliance for fare class, hotel constraints, and per-diem
• confirm that all details are consistent
•   surface uncertainty if something is conflicting or missing
•   abstain or ask for clarification if required
• produce a concise audited summary with booking IDs, policy clause IDs, and
actions taken.
********** 15 **********
--- page 16 ---
CO-5;   c.   •   State and explain any two human evaluation methods used for LLMs.   [5]
BL-2   •   Highlight the challenges of human evaluation methods.
Solution:
(Two human evaluation methods: 3 marks (1.5 marks each), challenges: 2 marks)
i.
• Common human evaluation approaches include:
•   Preference Tests (Pairwise Comparison):
• Show annotators two model answers for the same prompt; ask which one
they prefer.
•   Output: a win rate (e.g., “Model A preferred 70% over Model B”).
•   Benefits: simple for raters, avoids noisy absolute scores, and gives a
direct head-to-head comparison—great for choosing between variants.
•   Uses: widely used in industry; core to RLHF—humans’ pairwise choices
train a preference model; also used for evaluation to report win rates
between models.
• Why it’s strong: aligns with human judgment, scalable, and correlates
with real user satisfaction better than many automatic metrics.
•   Likert Scale Ratings
• Annotators rate an output on a fixed scale for certain criteria.
• For example, rate from 1 to 5 on quality, or 1 to 7 on how informative or harmful
the response is.
• This allows more fine-grained evaluation on multiple axes. In a chatbot
evaluation, you might have people rate overall satisfaction, accuracy of the
answer, politeness, etc.
• The average ratings (and distribution) indicate where the model stands.
•   Likert scaling provides more detail than a binary win/lose comparison, but it can
be harder to get consistency - one person's "4" might be another's "3".
•   Clear guidelines and training examples for raters help mitigate this.
•   Scalar or Ranked Outputs
• Sometimes outputs are ranked from best to worst if comparing many models at
once, or given a numeric score like 0–10.
• This is similar to Likert but not bounded to labeled categories like "strongly
agree" etc.
• For instance, an evaluator might score a summary on a 0–100 scale for
readability.
•   Typically, though, bounded Likert scales are used to maintain consistency.
• A/B Testing with End Users
•   In live systems, an ultimate test is deploying model A to a fraction of users and
model B to another, then using implicit or explicit feedback to judge which
performs better.
• For example, you might deploy two versions of a search query answering model
- one uses a new LLM, one uses the old - and see which version yields higher
user engagement or satisfaction ratings in a real setting.
********** 16 **********
--- page 17 ---
• This is a form of human evaluation at scale (the "users as judges" approach).
•   It's very powerful because it measures actual real-world success criteria (like
user clicks or task success).
• The downside is that it's post-deployment - you only do this with models you
believe are safe enough to test with real users.
ii.
•   Challenges with human evaluation:
•   It's considered the gold standard, but it's resource-intensive.
•   Obtaining a lot of human judgments is difficult, time-consuming and
expensive.
• This doesn't scale well if you need to evaluate thousands of model outputs
or re-evaluate frequently after every model update.
•   There's also variance - different annotators might disagree, so one must
gather multiple opinions and use statistical analysis (e.g., measuring inter-
annotator agreement, or taking majority votes) for reliable results.
•   Clear instructions and training examples are crucial to guide evaluators.
• Another issue is evaluator bias: human raters might have their own
preferences (one might favor more verbose answers, another prefers
concise ones, etc.), or even biases (e.g., harsh on grammar mistakes).
• Using a diverse pool of evaluators and averaging results can help.
Q6
a.   i.   Explain how a Vision Transformer converts an image into a sequence suitable   [10]
CO-4;   for a Transformer encoder.
BL-   ii.   For a 224×224 RGB image, compute the number of patches and patch vector
2,3   dimension for:
• P=32
• P=16
• P=14
Which choice gives the longest sequence?
iii.   Analyze when a ViT-based solution would be more suitable than a CNN-based
solution.
Solution:
(Vision Transformer converts an image into a sequence: 3 marks, numerical: 4 marks,
ViT-based solution would be more suitable: 3 marks)
i. How a Vision Transformer converts an image into a sequence for a Transformer
encoder
A Vision Transformer (ViT) first splits the image into fixed-size patches. Each patch is
then flattened into a 1D vector and passed through a learnable linear projection to obtain
a patch embedding. A special [CLS] token is prepended to the sequence, and positional
embeddings are added so the model retains spatial order information. The final result is
a sequence of embeddings that can be fed into the Transformer encoder just like a token
sequence in NLP.
So the pipeline is:
•   split image into patches
•   flatten each patch
********** 17 **********
--- page 18 ---
•   linearly project each patch to embedding dimension DDD
• add [CLS] token
• add positional embeddings
feed the sequence to the Transformer encoder.
ii. Patch calculations for a 224×224 RGB image
Given:
image size H=W=224
RGB image, so C=3
Formulas from ViT:
N=H×W/P2×W
patch vector dimension=P2×C
1. For P=32
Number of patches
N=224×224/32×32=50176/1024=49
Patch vector dimension
322×3=1024×3=3072
2. For P=16
Number of patches
N=224×224/16×16=50176/256=196
Patch vector dimension
162×3=256×3=768
3. For P=14P=14P=14
Number of patches
N=224×224/14×14=50176/196=256
Patch vector dimension
142×3=196×3=588
Which choice gives the longest sequence?
The sequence length depends on the number of patches. Comparing:
P=32→49 patches
P=16→196 patches
P=14→256 patches
The longest sequence is for: P=14
If the [CLS] token is included, sequence lengths become:
50 for P=32
197 for P=16
257 for P=14
iii. When a ViT-based solution is more suitable than a CNN-based solution
A ViT-based solution is more suitable when the task benefits from global context, large-
scale data, and strong generalization. Since self-attention allows each patch to attend to
every other patch, ViT captures long-range relationships more directly than CNNs,
which rely mainly on local receptive fields.
ViT is preferable when:
•   large pretraining datasets are available
• high accuracy and generalization are more important than low latency
• the application needs broader scene-level understanding
• the model must scale well to new tasks or large data regimes.
********** 18 **********
--- page 19 ---
CO-4;   b.   i.   Describe how DDPM is trained with a U-Net using the noise-prediction objective.   [10]
BL-2,   ii. Analyze why diffusion models are generally more stable to train than GANs.
4   Solution:
(Training process: 5 marks, DM more stable: 5 marks)
i. How DDPM is trained with a U-Net using the noise-prediction objective
DDPM training uses a U-Net denoiser and teaches it to predict the noise added to an
image at a randomly chosen diffusion step. The training process is:
•   Start with a real image x0 and normalize it.
• Sample a timestep t uniformly from 1 to T.
• Create a noisy image xt from x0 in one shot using the closed-form forward
diffusion equation.
• Feed xt and the timestep embedding into a U-Net. Optional conditioning, such as
class labels or text embeddings, can also be provided.
• The U-Net predicts the noise 𝜀̂(xt,t,c) that was added at step t.
• Train the model using a simple MSE loss between the true noise ϵ and the
predicted noise 𝜀̂.
U-Net is used because its downsampling and upsampling paths with skip connections
help denoise both coarse structure and fine details, while attention blocks help exchange
global information.
ii. Why diffusion models are generally more stable to train than GANs
Diffusion models are generally more stable because they do not rely on adversarial
training. Instead of training a generator and discriminator in competition, DDPM uses a
single denoising model trained with a simple noise-prediction MSE objective. This
makes optimization easier and avoids the unstable dynamics common in GANs.
Compared with GANs:
DDPM: simple MSE / likelihood-based objective, generally stable, low risk of mode
collapse
GAN: adversarial/minimax objective, can be unstable, and mode collapse is a common
failure mode
Diffusion models learn denoising directly
GANs learn through generator–discriminator competition, which is harder to optimize
reliably.
Q7
CO-3;   a.   iii. Describe the concept of a probability skip list and how it enables fast search.   [10]
BL-2,   iv. Discuss the idea of a navigable small world graph in the context of nearest
4   neighbor search.
v. Analyze how HNSW combines skip-list hierarchy and small-world graph
navigation to improve search efficiency in high-dimensional spaces.
Solution:
(Probability skip list: 3 marks, idea of a navigable small world graph: 3 marks, HNSW
combines skip-list hierarchy and small-world graph navigation: 4 marks)
i. Probability skip list and how it enables fast search
A probability skip list is a probabilistic data structure built as multiple layers of linked
lists. The bottom layer contains all elements, while higher layers contain fewer elements
and therefore create longer “skips” across the list. This structure allows the search to
begin at the topmost layer, where large jumps are possible, and then move down
gradually to lower, denser layers for finer search.
It enables fast search because the algorithm does not need to scan every element one by
one. Instead, it first makes coarse jumps at higher layers and then refines the search at
********** 19 **********
--- page 20 ---
lower layers. The notes state that skip lists allow insertion and searching in O(log(n)) on
average.
ii. Navigable small world graph in nearest neighbor search
A navigable small world (NSW) graph is a graph where most connections are local, but
some carefully chosen longer-range connections create short paths between distant
nodes. In nearest neighbor search, vectors are connected so that starting from an entry
point, the search can move greedily through the graph toward nodes that are closer to
the query.
The key idea is that the search does not require global knowledge of the whole graph.
Instead, at each step, it checks the immediate neighbors and moves to the one that
appears closest to the target. This greedy navigation works efficiently when the graph
has the small-world property and the long-range links are well distributed. The notes
mention that in such cases the target can often be reached in a number of steps
proportional to log(n).
iii. How HNSW combines skip-list hierarchy and small-world navigation
HNSW improves search efficiency by combining two ideas:
the layered hierarchy of a probability skip list
the graph navigation of a navigable small world graph.
From the skip-list side, HNSW uses multiple layers:
top layers are sparse and contain long-range links
lower layers are denser and contain short-range links
This means the search first uses the upper layers to quickly move toward the rough
region of the target, and then uses the lower layers to refine the search more accurately.
From the small-world side, HNSW uses greedy graph traversal. Starting from an entry
point, it follows neighbors that reduce the distance to the query. Because the graph is
built with a mix of long-range and short-range connections, the search can “zoom out”
quickly across the space and then “zoom in” near the target.
This combination improves efficiency in high-dimensional spaces because:
•   it avoids exhaustive comparison with all vectors
•   it reduces the number of nodes explored
•   it provides a good trade-off between speed and recall
•   it achieves fast search, often close to logarithmic behavior in practice.
HNSW is efficient because it combines the fast coarse search of skip lists with the
effective greedy search of small-world graphs, making it one of the most powerful ANN
methods for vector databases.
CO-4;   b.   i.   Describe the CLIP training process, including paired data, shared embedding   [10]
BL-   space, and contrastive loss.
2,3,4   ii. Analyze why CLIP enables strong zero-shot transfer without task-specific fine-
tuning.
iii. CLIP is pretrained on 40 lakh image-text pairs. If training uses batches of N=256,
estimate:
a. number of batches required to see 40 lakh pairs once
b. how many pairwise similarity entries are computed per batch
Solution:
(CLIP training process: 3 marks, zero shot transfer: 3 marks, numerical: 4 marks)
i. CLIP training process: paired data, shared embedding space, and contrastive loss
********** 20 **********
--- page 21 ---
CLIP is trained on a very large dataset of paired image–text examples collected from the
internet. In the original setup, it used about 400 million image-text pairs. Each image is
passed through an image encoder and each caption through a text encoder. The resulting
features are then projected into a shared embedding space, so both images and text are
represented as vectors of the same dimension. After projection, the embeddings are L2-
normalized, and CLIP computes similarities between every image and every text in the
batch.
For a batch of N matched pairs, CLIP forms an N×N similarity matrix. The diagonal
entries are the correct image–text matches, while the off-diagonal entries are
mismatched pairs. CLIP uses a symmetric contrastive loss: it trains the model so each
image assigns highest score to its correct caption, and each caption assigns highest score
to its correct image. This pulls matched pairs closer in the shared space and pushes
unrelated pairs apart.
ii. Why CLIP enables strong zero-shot transfer without task-specific fine-tuning
CLIP enables strong zero-shot transfer because it learns from natural language
supervision rather than fixed closed-set labels. During training, it does not just learn
“class IDs”; it learns how visual concepts align with language in a shared embedding
space. As a result, after pretraining, we can classify a new image by writing candidate
prompts such as “a photo of a dog,” “a photo of a cat,” and comparing their text
embeddings with the image embedding. The class whose prompt has the highest
similarity is selected.
This is significant because the model does not need task-specific retraining for every
dataset. Instead, new tasks can often be framed through prompts, which makes CLIP
flexible across domains. Its zero-shot ability comes from the fact that the representation
is already linked to language, so the model can transfer to unseen classes and tasks by
matching images to text descriptions rather than learning new classifier weights each
time.
iii. Numerical part
Given:
total image-text pairs =40,00,000
batch size N=256
a. Number of batches required to see 40,000 pairs once
Number of batches=40,00,000/256 =1,562,5 batches
b. Pairwise similarity entries computed per batch
For CLIP, each batch compares every image with every text, so the similarity matrix has
size:
N×N=256×256 = 65,536
********** 21 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 2bbdd25c5783

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AI_7012/GENERATIVE AI/ANS_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: GENERATIVE AI
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data wherever necessary.
Q1   Answer briefly:
CO-   a.   Compare Natural Language Understanding (NLU) and Natural Language   [5]
1;   Generation (NLG). Considering example applications, explain how they interact
SO-   with real systems.
1;
BL-   Solution: (Comparison 4 marks, examples 1 mark)
4
Aspect   NLU (Understanding)   NLG (Generation)
Derive meaning/structure from Produce fluent, relevant text from
Goal
text   data/intents
Typical
Text
Input   Structured info/prompts/context → text
labels/slots/graphs/embeddings
Output
intent detection, classification,
dialogue/answers, summarization,
Common   NER/slot filling, parsing,
translation, data-to-text, style transfer,
Tasks   coreference, sentiment, QA
code/doc drafting
evidence retrieval
Often encoder-heavy (BERT,
Often decoder-heavy (GPT-style) to expand
Model Bias RoBERTa) to compress
into language
meaning
Used when understanding
Encoder-   Same models can both understand and
feeds generation (e.g., T5
Decoder?   generate when trained seq2seq
“read then write”)
Discriminative or span-level
Training   Generative objectives (next-token, seq2seq
objectives (MLM, contrastive,
Signals   likelihood), RLHF for preference alignment
token classification)
Accuracy/F1, EM/F1 (QA),
BLEU/ROUGE/BERT Score, human eval
Evaluation NMI/ARI (clustering),
(quality, faithfulness), toxicity/harm checks
calibration
********** 1 **********
--- page 2 ---
Shallow cues, poor grounding,
Typical   Hallucination, verbosity, style drift,
entity/negation errors, domain
Failures   factuality and safety issues
shift
Labeled or weakly-labeled task Parallel/paired data or instructions; high-
Data Needs
data; domain coverage   quality references for factual tasks
Product   Robustness, recall for rare   Faithfulness to sources, controllability,
Concerns   entities, latency modest   latency higher (long outputs)
• Task-oriented assistants: NLU parses user intent & slots → NLG realizes a natural
reply.
• RAG pipelines: NLU retrieves/grounds evidence → NLG verbalizes the answer
with citations.
• Analytics → narrative: NLU extracts facts from docs → NLG converts them into
summaries/reports.
CO-   b.   i. Explain in brief the concept of autoregressive models
2;   ii. An autoregressive model which predicts the token from left to right. For the
SO-   sequence S = “A B C ⟨eos⟩”, the model’s predicted conditional probabilities at each
2;   step are:
BL-   p(A|⟨bos⟩)=0.55,
3   p(B|⟨bos⟩ A)=0.60,
p(C|⟨bos⟩ A B)=0.50,
p(⟨eos⟩|⟨bos⟩ A B C)=0.70.
where bos is beginning of sequence and eos is end of sequence. Compute the joint
probability p(S) under the autoregressive factorization.
Solution:
(explanation: 3 marks, numerical : 2marks)
The aim of autoregressive models is to learn a joint distribution over x.
AR models do not make any independence assumption but use the default factorization of
p(x) given by the chain rule
********** 2 **********
--- page 3 ---
p(S)=p(A)p(B∣A)p(C∣AB)p(⟨eos⟩∣ABC)
=0.55×0.60×0.50×0.70=0.1155
CO-   c.   If an Hierarchial Navigable Small Worls (HNSW) index is built with parameters:   [5]
3;   • M (max connections per node) = 8,
SO-   • efConstruction (size of dynamic candidate list during index building) =
2;   100, and
BL-   • efSearch (size of dynamic candidate list during querying) = 50,
3   what will happen if efSearch is increased to 150 while keeping the other parameters
unchanged? Specifically, explain the expected effect on:
i.   Recall,
ii.   Query latency
iii.   Index memory usage
Give a brief justification for each.
Solution:
(1 mark for increase/decrease of each parameter, correct justification: 2 marks)
Recall — increases.
A larger efSearch (50 → 150) expands the candidate set explored during query-time graph
walk, so the search is less myopic and more likely to reach true nearest neighbors (until
gains plateau based on graph quality M, efConstruction).
Query latency — increases.
Higher efSearch means visiting more nodes and doing more distance computations/heap
ops per query, so runtime grows roughly with the explored set size (higher recall ↔ higher
latency trade-off).
Index memory usage — no change.
efSearch is a query-time parameter; it doesn’t alter stored graph connectivity. Memory is
determined mainly by M (neighbors per node) and build settings, not by the search budget.
CO-   d.   You are given one target and one predicted translation:   [5]
5;
SO-   • Target: “the quick brown fox jumps over the lazy dog”
2;   • Predicted Sentence: “the quick brown dog jumps over the lazy dog”
BL-
3   Use case-insensitive matching and assume uniform weights for BLEU-4 and compute
with natural logs. Compute the following:
i. Compute the n gram precisions p1, p2, p3 and p4 for unigrams through 4-grams.
Show counts of matches and totals for each n.
ii. Compute the brevity penalty (BP) given candidate length c and reference length
r.
iii. Compute the final BLEU-4 score.
Solution:
(Precision computation: 2 marks, BP: 1mark, final BLUE score: 2 marks)
Precision computation
• Unigrams (p₁): Matches = {the x 2, quick, brown, dog, jumps, over, lazy} = 8 of 9
⇒p1=8/9=0.8889
********** 3 **********
--- page 4 ---
• Bigrams (p₂):
Ref: [the quick, quick brown, brown fox, fox jumps, jumps over, over the, the lazy,
lazy dog]
Cand: [the quick, quick brown, brown dog, dog jumps, jumps over, over the, the
lazy, lazy dog]
Matches = {the quick, quick brown, jumps over, over the, the lazy, lazy dog} = 6
of 8
⇒p2=6/8=0.75
• Trigrams (p₃):
Matches = {the quick brown, jumps over the, over the lazy, the lazy dog} = 4 of 7
⇒p3=4/7=0.5714
• 4-grams (p₄):
Matches = {jumps over the lazy, over the lazy dog} = 2 of 6
⇒p4=2/6=0.3333
(b) Brevity penalty (BP)
Candidate length c=9, reference length r=9
BP=min (1,c/r)=1.
(c) BLEU-4

=1⋅exp (1/4(ln (0.8889) + ln(0.75)+ln(0.5714)+ln(0.3333))
=exp (1/4(−0.1173−0.2877−0.5596−1.0986)) = exp (−0.5158) ≈ 0.597
Final BLEU4: 0.597
Q2
CO-   a.   With respect to the Bidirectional Transformer (BERT) model, answer the following:   [10]
2;   i. Explain the advantage of BERT over decoder only models.
SO-   ii. Justify the significance of Masked Language Model (MLM).
2;   iii. Explain the roles of [CLS], [SEP], token embeddings, position embeddings,
BL-   and segment (token-type) embeddings in BERT’s input representation.
2,4   iv. Explain how the fine tuning can be done for sentence pair classification task.
Solution:
(advantage of BERT: 2 marks, MLM significance: 3 marks, roles of embeddings: 4
marks, fine tuning: 1 mark)
i.
• True bidirectional context: BERT sees left + right context at once (MLM), so
it’s usually better for understanding tasks (classification, NER, span QA)
than causal, left-to-right decoders.
•   Parallel, fast inference for encodings: Encoders process all tokens in parallel;
great for low-latency sentence/Document embeddings, retrieval, and batch
classification. (Decoders are sequential at generation time.)
• Token-level precision: Per-token representations from BERT’s encoder suit
NER, POS, span extraction; no exposure bias from autoregression.
• Stronger retriever/backbone: As a bi-encoder or cross-encoder, BERT
variants yield high-quality similarity scores for RAG, search, reranking.
• Parameter/compute efficiency for non-gen tasks: You don’t pay the decoding
cost; fine-tuning a BERT-base often matches or beats larger decoder-only
models on understanding benchmarks.
ii.
********** 4 **********
--- page 5 ---
• MLM Solves the problem of label leakage in bidirectional models.
• In Masked Language Modeling, we randomly mask out some percentage
(typically 15%) of the input tokens.
• The model then predicts these masked words using the surrounding
unmasked context—both left and right.
• This allows the model to learn deep bidirectional context, while preventing
label leakage.
iii.
• [CLS]: A special token at the start; its final hidden state is used as a single
summary vector for sequence-level classification (e.g., sentiment, NLI).
• [SEP]: Separator token; ends a sentence and separates two sentences in pair
tasks, marking boundaries.
• Token embeddings: Learned vectors for WordPiece tokens (e.g., “play”,
“##ing”) capturing lexical identity/morphology.
• Position embeddings: Learned vectors by position index (0,1,2,…) to inject
word order (since attention is order-agnostic).
• Segment (token-type) embeddings: Tags which segment a token belongs to
(A or B) so BERT can model relationships between two sentences.
iv.
CO-   b.   i.   Compare traditional databases and vector databases highlighting the   [10]
3;   strengths and weakness of each of them.
SO-   ii.   An online marketplace wants a unified search for:
2;
BL-   • Exact lookups: ORDER-IDs, SKU, seller usernames.
• Structured filters: price range, brand, availability, delivery region.
4
• Semantic queries: “lightweight waterproof hiking jacket under ₹5k”,
plus multilingual queries (Hindi/English mix).
• Unstructured data: product descriptions & user reviews (text) and
image captions.
• Constraints: inventory updates are frequent (per-minute), p95 latency
< 1.0 s, and results must show verifiable fields (price/stock) and source
snippets from reviews.
Which storage/retrieval approach would you choose—traditional
database, vector database, or a hybrid? Justify with three concrete
reasons tied to
********** 5 **********
--- page 6 ---
i.   exact/structured vs. semantic needs,
ii. update frequency & latency
iii. trust/traceability.
Solution:
(Comparison: 3 marks, choice of DB: 1 mark, reasons: 2 marks each)
Traditional Databases   Vector Databases
Data Type: Store structured data (rows,   Data Type: Store embeddings (high-
columns, tables).   dimensional vectors) from ML/AI
Query Mechanism: Rely on exact match   models.
or relational logic (e.g., SQL).   Query Mechanism: Similarity search
Indexing: B-trees, hash indexes   (cosine similarity, Euclidean distance,
optimized for structured queries.   dot product).
Use Cases: Banking transactions,   Indexing: Approximate Nearest
inventory systems, CRM, ERP.   Neighbor (ANN) techniques (HNSW,
Strengths:   IVF, PQ).
ACID compliance (transactions,   Use Cases: Semantic search,
consistency) Atomicity, Consistency,   recommendation engines, Retrieval-
Isolation, and Durability—that ensure   Augmented Generation (RAG),
database transactions are processed   image/video/audio similarity, anomaly
reliably and result in a valid and   detection.
consistent database state.   Strengths:
Great for well-defined schema   Handles unstructured data effectively
High efficiency for deterministic   Supports semantic and fuzzy queries
queries   (meaning-based)
Limitations:   Scales to billions of embeddings
Cannot handle unstructured data   Limitations:
(images, text, audio) effectively   Not optimized for transactions
No semantic understanding — “apple”   Emerging ecosystem — fewer mature
the fruit ≠ “Apple” the company   tools than traditional DBs
Compute-intensive indexing/search
choose a hybrid (traditional relational DB + vector DB).
1) Exact/structured vs. semantic needs
•   Relational DB:
o Use B-tree indexes for exact IDs (ORDER_ID, SKU, seller username) and numeric
fields (price, stock).
o Use BRIN/B-tree for time/region columns and GIN for keyword search on titles if
needed.
o Perfect for filters & joins (brand, availability, delivery region) with ACID
guarantees.
• Vector DB:
o Use HNSW index over embeddings for semantic and multilingual search across
product descriptions, user reviews, and image captions (e.g., CLIP text).
o Handles queries like “lightweight waterproof hiking jacket under ₹5k” even when
wording differs.
2) Update frequency & latency (p95 < 1.0 s)
•   Relational side: Per-minute inventory/price updates are cheap with indexed writes;
exact lookups/filtered queries return in <100–200 ms.
********** 6 **********
--- page 7 ---
• Vector side: Maintain an async embedding pipeline (CDC/queue) to re-embed only
changed items/reviews; HNSW top-k retrieval is tens of ms.
• Serving plan: Route parts of the query—numeric filters to SQL (pre-filter
candidate SKUs), semantic text to ANN—and run both in parallel. Typical end-to-
end = parallel retrieval + one rerank + render < 1.0 s.
3) Trust & traceability (verifiable + explainable)
•   Authoritative facts from SQL: Price/stock/seller are returned directly from tables
(no hallucination).
• Evidence from vector nodes: Return snippets from reviews/captions with item &
paragraph IDs for citations.
•   Guardrails: Only enrich the SQL-filtered candidate set with semantic matches;
never infer numeric fields from text.
Q3
CO-   a. With respect to GPT 2 model, answer the following:   [10]
i.   Briefly explain the following key changes from GPT-1 to GPT-2 in training
2;
setup/aims
SO-   • zero-shot evaluation
2;   • context window
and why these changes matter for generalization.
BL-   ii.   Explain how GPT-2 performs zero-shot tasks via prompting. Give one
2   example of a task that benefits, and discuss two limitations.
Solution:
(key changes: 5 marks, zero shot prompting examples: 5 marks)
i.
Zero-shot evaluation (GPT-2 vs. GPT-1):
a. Change: GPT-1 mainly reported supervised fine-tuning results; GPT-2
emphasized zero-shot prompting—casting tasks as plain text prompts and
evaluating without task-specific heads.
b. Why it helps generalization: Forces the model to rely on broad, transferable
language knowledge rather than task-specific supervision; reduces
overfitting to small labeled sets and shows capability to adapt to unseen
tasks via instructions alone.
Larger context window (~1024 vs. ~512):
c. Change: GPT-2 roughly doubled the context length, letting the model
condition on longer sequences (more document history, longer prompts).
d. Why it helps generalization: Enables modeling of long-range dependencies
(coreference, discourse, code blocks), supports richer prompts/few-shot
demonstrations, reduces truncation artifacts, and improves coherence—
yielding better transfer across varied, real-world inputs.
ii.
• You format the task as plain text so it looks like natural continuation. GPT-2 (a
left-to-right LM) then generates the next tokens conditioned on that prompt—no
task-specific head or fine-tuning.
********** 7 **********
--- page 8 ---
•   Pattern:
“Instruction / Context / Input → delimiter → expected start of answer”, e.g.
Translate to French: "The sky is clear." Answer: → model continues with the
translation.
• Example task that benefits:
Cloze/QA or simple translation. For translation, explicit cues like “Translate to
French:” plus quotes give GPT-2 enough structure to output a reasonable
sentence without any supervised tuning.
• Two key limitations:
• Prompt sensitivity / brittleness: Small wording or delimiter changes can swing
accuracy a lot; there’s no learned alignment to a fixed task format.
•   Factuality & grounding: Without retrieval or supervision, GPT-2 can
hallucinate or reflect training-set biases; it doesn’t verify facts or cite sources.
CO-   b.   i. Explain the difference between a typical Hash function used in dictionaries in   [10]
3;   python and a Hash function used in Locality Sensitive Hashing (LSH).
SO-   ii. Suppose that Locality sensitive hashing (LSH) algorithm is being implemented
2;   on two short documents Doc1 and Doc2. The documents contain the following
BL-   content:
3   • DocX = “machine learning”
• DocY = “learning machines”
(lowercase; keep spaces and treat them as _ when listing shingles):
Use character bigrams (k = 2). Consider unique bigrams only.
Assign IDs: List all unique bigrams across both docs in lexicographic order
(same as used in dictionaries) and assign integer IDs starting at 0.
Hash functions (mod 19):
• h1(x)=(7x+2) mod 19
• h2(x)=(5x+4) mod 19
• h3(x)=(9x+1) mod 19
• h4(x)=(3x+6) mod 19
Compute the following:
a. Build the characteristic matrix: rows = bigram IDs, columns = {DocX,
DocY}, entries ∈ {0,1}. Show the bigram → ID mapping.
b. Compute the true Jaccard similarity.
c. Compute the MinHash signatures (length 4) for DocX and DocY using
h1..h4. For each hash, take the minimum hash value over the bigram
IDs present in that doc.
d. Compare the signatures.
Solution:
(Difference: 2 marks, numerical: 8 marks (correct shingles: 2 marks, characteristic
matrix: 2 marks, Jaccard similarity: 1 mark, MinHash: 2 marks, comparison:1
mark)
i.
•   Traditional hashing tries to minimize collisions.
• LSH does the opposite: it designs hash functions so that similar items are more
likely to collide (land in the same bucket).
•   This allows fast approximate nearest neighbor (ANN) search.
********** 8 **********
--- page 9 ---
Traditional Hash   LSH Hash
ii.
Unique bigrams (k = 2) and characteristic matrix
Lowercase and keep spaces (shown as _).
• DocX = “machine_learning” → bigrams:
{ma, ac, ch, hi, in, ne, e_, _l, le, ea, ar, rn, ni, ng}
• DocY = “learning_machines” → bigrams:
{le, ea, ar, rn, ni, in, ng, g_, _m, ma, ac, ch, hi, ne, es}
Universe (lexicographic) & IDs (start at 0):
0:_l, 1:_m, 2:ac, 3:ar, 4:ch, 5:e_, 6:ea, 7:es, 8:g_,
9:hi, 10:in, 11:le, 12:ma, 13:ne, 14:ng, 15:ni, 16:rn
Characteristic matrix (rows = shingle IDs; columns = DocX, DocY):
ID Shingle DocX DocY
0 _l   1   0
1 _m   0   1
2 ac   1   1
3 ar   1   1
4 ch   1   1
5 e_   1   0
6 ea   1   1
7 es   0   1
8 g_   0   1
9 hi   1   1
10 in   1   1
11 le   1   1
12 ma   1   1
13 ne   1   1
14 ng   1   1
15 ni   1   1
16 rn   1   1
DocX shingle IDs = {0,2,3,4,5,6,9,10,11,12,13,14,15,16}
DocY shingle IDs = {1,2,3,4,6,7,8,9,10,11,12,13,14,15,16}
The true Jaccard of the bigram sets is ∣X∩Y∣∣X∪Y∣=12/17≈0.706
b) MinHash signatures (mod 19)
Hash functions:
h1(x)=(7x+2) mod 19
h2(x)=(5x+4) mod 19
********** 9 **********
--- page 10 ---
h3(x)=(9x+1) mod 19
h4(x)=(3x+6) mod 19
For each doc, take the minimum hash value over its present shingle IDs.
• DocX:
min h1=0 (e.g., ID 16 → (7⋅16+2) mod 19=0)
min h2=0 (e.g., ID 16 → (5⋅16+4) mod 19=0)
min h3=0 (e.g., ID 14 → (9⋅14+1) mod 19=0)
min h4=1 (e.g., ID 11 → (3⋅11+6) mod 19=1)
Signature_X = (0, 0, 0, 1)
• DocY:
min h1=0 (e.g., ID 14 → 0)
min h2=0 (e.g., ID 11 → 0)
min h3=0 (e.g., ID 12 → 0)
min h4=1 (e.g., ID 11 → 1)
Signature_Y = (0, 0, 0, 1)
Compare the signatures
They match in all 4 components → estimated Jaccard similarity =4/4=1.0.
Q4
CO-   a.   i.   Given a knowledge base of PDFs, outline the flow of steps for a basic RAG flow   [10]
3;
using LangChain framework.
SO-
2;   ii. A query used for RAG retrieves k = 5 chunks (avg 300 tokens each).
BL-
Embedding cost = $0.05 / 1K tokens; LLM generation cost = $0.20 / 1K tokens.
2,3
The prompt to the generator includes:
• user query (50 tokens)
• the five chunks
• instructions (100 tokens).
The model generates 150 tokens.
e. Compute total tokens embedded, prompt tokens, generated tokens.
f. Compute total dollar cost for this query.
iii.   Explain when you would prefer fixed-length chunking vs.
semantic/sentence-aware chunking for policy PDFs.
Solution:
(Flow of steps: 4 marks, numerical: 3 marks, fixed length vs semantic/sentence: 3
marks)
i.
1. User Query
• The process begins when a user submits a query or request.
• For example, a user might ask, “Is today a holiday in India?”
• This query serves as the input to the LangChain pipeline
2. Vector Representation and Similarity Search
********** 10 **********
--- page 11 ---
• Once the query is received, LangChain converts it into a vector
representation using embeddings.
• This vector captures the semantic meaning of the query.
• The vector is then used to perform a similarity search in a vector database.
• The goal is to find the most relevant information or context stored in the
database that matches the user's query.
3. Fetching Relevant Information
• Based on the similarity search, LangChain retrieves the most relevant data or
context from the database.
• This step ensures that the language model has access to accurate and contextually
appropriate information to generate a meaningful response.
4. Generating a Response
• The retrieved information is passed to the language model (e.g., OpenAI's GPT,
Anthropic's Claude or others).
• The LLM processes the input and generates a response or takes an action based on
the provided data.
• For example, if the query is about holiday, the LLM might generate a response
like, “Today is a holiday in India on account of Ganesh Chaturthi.”
• The formatted response is returned to the user as the final output. The user receives
a clear, accurate and contextually relevant answer to their query.
ii.
(i) Tokens
• Embedded: 5×300=1,500
• Prompt (to generator): 50+ (5×300) + 100=1,650
• Generated: 120
(ii) Cost
• Embedding: 1,500/1,000×$0.05=$0.075
• LLM (prompt + output): (1,650+120) = 1,770 tokens → 1.77×$0.20=$0.354
•   Total: $0.075+$0.354=$0.429
iii.
Prefer fixed-length chunking (e.g., 800–1200 chars with 10–15% overlap) when…
• Uniform structure or noisy layout: Scanned PDFs, mixed fonts, headers/footers that
break sentence detection; fixed windows avoid parser brittleness.
• Throughput first: You want predictable chunk sizes for stable embedding/latency
budgets and easier batching.
• Dense retrieval over broad context: Queries often need dispersed cues (definitions
spread across pages); fixed windows ensure coverage even if sentence splitting
fails.
• Downstream reranking present: You plan to use a cross-encoder/reranker that can
re-score coarse chunks—so coarse splitting is acceptable.
Trade-offs: May cut sentences/sections mid-thought → lower semantic cohesion;
can inflate prompt with irrelevant text unless you rerank/filter.
Prefer semantic / sentence-aware chunking (e.g., split by sentences/sections; 3–8
sentences per chunk) when…
•   Precision and readability matter: Policy PDFs have meaningful boundaries
(sections, clauses, bullet points); sentence-aware chunks keep concepts intact →
better match to user queries and cleaner citations.
• You need faithful answers with citations: Cohesive chunks map cleanly to section
IDs/page refs, reducing hallucinations and making audits simpler.
********** 11 **********
--- page 12 ---
• Queries are specific: “Reimbursement cap for travel in Q4” maps to a single
clause; semantic chunks boost exact-match retrieval and reduce prompt bloat.
•   Post-processing uses structure: Easy to render sources as “§4.2, p. 17” and to
enforce source-grounded generation.
Trade-offs: Slightly more preprocessing; variable chunk sizes can complicate
batching and occasionally miss dispersed signals if chunks are too narrow.
CO-   b.   i.   State one scenario where a Large Vision Model (Transformer-based, ViT) is [10]
4;   preferable to a CNN, and one scenario where a CNN is still the better choice.
SO-   Justify each in 1–2 lines focusing on accuracy/scale vs. latency/edge efficiency.
2;   ii.   Explain how positional embeddings are injected in ViT. Mention one limitation of
BL-   absolute position embeddings and name one alternative (or improvement) used in
later variants.
2,3
iii. ViTs lack strong locality/translation inductive bias. Name any two improvements
in training strategies and explain in one line each how they help ViTs match CNNs
on ImageNet-scale data.
iv. A ViT uses patch size P × P=16 × 16, RGB input (C=3), and embedding dimension
D=768. The patch embedding is implemented as a linear projection (equivalently
a conv with kernel 16 ×16, stride 16). Compute the total number of parameters in
the patch projection with bias.
Solution:
(scenario: 3 marks, positional embeddings: 3 marks, improvements: 2 marks,
numerical: 2 marks)
i.
ViT preferable:
• Open-vocabulary / zero-shot classification on diverse, large-scale data (e.g., CLIP-
style product or artwork tagging).
Why: Transformers exploit global context and scale elegantly with pretraining,
yielding higher accuracy and transfer than CNNs at large model/data scales.
CNN preferable:
•   Real-time, on-device inference (e.g., 60 FPS mobile AR object detection on
battery-constrained hardware).
Why: CNNs are lighter and more cache-friendly, delivering lower latency and
power usage for edge deployments with tight compute budgets.
ii.
After splitting the image into patches and projecting each to a D-dim token, ViT adds
a learned absolute positional embedding vector to each patch token (and to the
[CLS] token) elementwise before the Transformer layers.
•   xclass: Special [CLS] token (like in BERT), used for classification.
• 𝑥𝑝 𝑖: Flattened image patch i
•   E: Linear projection (embedding matrix) that maps patches into a D-dimensional
space.
•   Epos: Positional embeddings to preserve patch order
•   Output: z0, the initial sequence of embeddings fed into the Transformer.
• The output of this projection is referred as the patch embeddings.
********** 12 **********
--- page 13 ---
iii.
Improving Vision Transformer performance
•   Regularization
• Weight Decay
1. Adds a penalty to large weights in the loss function.
2. Prevents overfitting by encouraging smaller, more generalizable
weights.
3. Especially important in ViTs since they often have very high capacity
(lots of parameters).
•   Stochastic Depth
1. Randomly drops entire layers during training (like skipping residual
blocks).
2. Makes the network behave like an ensemble of shallower models,
improving robustness.
3. Helps ViTs avoid overfitting and speeds up training.
• Dropout (in FFN layers of Transformer)
1. Randomly sets some neuron outputs to zero during training.
2. In ViTs, dropout is mainly used in the Feed-Forward Network (FFN)
layers, not in self-attention.
3. Reduces co-adaptation and improves generalization.
• Augmentation
• MixUp
• Combines two training images (and their labels) by linear interpolation.
• Example: new image = 0.7 × image A + 0.3 × image B.
•   Prevents overfitting and makes the model smoother in decision
boundaries.
• RandAugment
• Applies a random set of image transformations (e.g., rotation, color shift,
crop, shear).
• Improves data diversity without manually tuning augmentation policies.
• Works well with ViTs, which typically require large datasets to
generalize well.
iv.
Given: P=16, C=3, D=768
Patch vector size =P×P×C=16×16×3=768.
(i) Parameters (no bias): weight matrix maps R768 → R768
⇒768×768=589,824.
(ii) Bias parameters: one per output dimension
⇒768.
(iii) Total with bias: 589,824+768=590,592
Q5
CO-   a.   i. What are the inherent limitations of Large Language Models (LLMs)?   [10]
3;
SO-
2;
********** 13 **********
--- page 14 ---
BL-   ii. Your university pilots a GPT-style assistant for course advising. Below are three real
chat excerpts the team collected during testing (timestamps are from October 2025).
2,4
The model has not been connected to any internal databases.
Excerpt A (Policy answer):
Student: “What are the graduation requirements for the BTech AI program updated this
year?”
Assistant: “You need 180 credits including a Capstone. Two ethics electives are optional.”
Excerpt B (Scholarship info):
Student: “Is there financial aid for students who publish in top AI conferences?”
Assistant: “Yes, the university offers the ‘Scholars Grant’ covering 50% tuition for one
year.”
Excerpt C (Advising style):
Student: “I’m a third-year transfer student from mechanical engineering, targeting
machine perception roles. Which two electives fit best next term?”
Assistant: “Consider taking Programming 101 and Introduction to Data. These are great
starting points for everyone.”
Based on these responses, answer the following questions:
a. For each excerpt (A, B, C), identify the primary failure and explain why it
arises from inherent LLM limitations, not just a bad prompt. Use precise
terminology and tie it to the excerpt.
b. Propose system-level mitigations for each failure that does not rely on
retraining from scratch.
Solution:
(Inherent limitations: 3 marks, identifying the failure for each excerpt: 3 marks, proposed
solution for each: 4 marks)
i.
LLMs are powerful but come with inherent limitations:
Limited knowledge:
Limited to providing generic answers based on their training data.
Cannot provide accurate answers to specific domain related questions.
The training data of these models have a cutoff date, limiting their ability to provide up-
to-date responses.
Hallucinations:
They tend to confidently generate false responses based on imagined facts.
Can provide responses that are off-topic if they don’t have an accurate answer to the
user’s query.
These models sometimes generate plausible-sounding but incorrect information.
Generic responses:
Often provide generic responses that aren’t tailored to specific contexts.
Cannot provide a personalized customer experience.
Without access to external sources, LLMs may provide vague or imprecise answers.
ii.
Diagnose the primary failure in each excerpt (and why it’s inherent)
• A — Policy answer (“180 credits… ethics electives optional”)
Failure: Uses stale/ungrounded policy claims.
********** 14 **********
--- page 15 ---
Why inherent: A GPT-style LM predicts next tokens from pretraining; without live
retrieval it can’t know this year’s requirements. Bidirectional patterning yields
plausible-but-ungrounded numbers/rules.
• B — Scholarship info (“Frontier AI Scholars Grant… 50% tuition”)
Failure: Fabricated entity/details (hallucination).
Why inherent: When asked for specifics absent in its context, an LM pattern-
completes to a grant-sounding name and terms, optimizing fluency—not truth—
because there’s no built-in verification loop.
• C — Advising style (“Programming 101” & “Intro to Data” to a 3rd-year transfer
targeting perception)
Failure: Generic, non-personalized recommendation ignoring the user’s level/goal.
Why inherent: Base LMs lack persistent user models and constraint satisfaction;
they regress to safe, frequent defaults when the prompt requires domain matching
and prerequisite reasoning.
System-level mitigations (no full retraining)
• A (policies): RAG over the authoritative policy repo + prompt that requires
section-level citations and exact copy for numeric thresholds; add a freshness guard
(“answer only if doc date ≥ current AY”).
• B (scholarships): Route through a catalog/aid API tool; response template enforces
source URL + program ID. If lookup fails, return “no verified program found”
(abstain).
• C (advising): Add a profile intake & slot-filling step (year, prereqs, target role) +
catalog retriever filtered by level/tags (vision/perception). LLM only rephrases
top-k catalog matches; no free-form guessing.
CO-   b.   i.   What is the difference between Large language model (LLM) and Vision   [10]
4;   Language Model (VLM)?
SO-   ii.   Briefly explain how CLIP aligns images and text into a shared embedding
2;   space and how this enables zero-shot classification with class name prompts.
BL-   iii.   How is Contrastive Language Image Image Pretraining (CLIP) used in zero-
shot transfer?
2,3
iv.   You are given L2-normalized embeddings (dimension doesn’t matter):
• Image vector is vI
• Text vectors are vlion,vzebra,vgiraffe
• The dot products (cosines) are:
⟨vI,vlion⟩=0.62, ⟨vI,vzebra⟩=0.55, ⟨vI,vgiraffe⟩=0.40.
a. Compute the Softmax probabilities over classes using a temperature
T=0.01(i.e., logits = cosines / T).
b. Report the predicted class.
Solution:
(2.5 marks each)
i.
********** 15 **********
--- page 16 ---
ii.
How CLIP aligns the modalities:
CLIP trains two encoders—an image encoder and a text encoder—in parallel. For each
minibatch of (image, caption) pairs, it L2-normalizes both embeddings and uses a
contrastive (InfoNCE) loss to make the cosine similarity of the matched pair high and all
mismatched pairs low (with a learnable temperature). After training, images and their
correct texts occupy nearby points in one shared embedding space.
Why this gives zero-shot classification:
At test time, you write class name prompts (e.g., “a photo of a {label}”), encode each
prompt with the text encoder, and encode the image once. The class whose text embedding
has the highest cosine similarity to the image embedding is chosen—no task-specific
training needed. (Prompt wording matters; using templates/ensembles often improves
accuracy.)
iii.
• Using clip for zero-shot transfer
• CLIP is pre-trained to predict if an image and a text snippet are paired together in
its dataset.
• For each dataset, we use the names of all the classes in the dataset are used as the
set of potential text pairings and predict the most probable (image, text) pair
according to CLIP.
• Implementation steps:
• Compute the feature embedding of the image and the feature embedding of
the set of possible texts by their respective encoders.
• The cosine similarity of these embeddings is then calculated, scaled by a
temperature parameter t , and normalized into a probability distribution via
a Softmax.
• This prediction layer is a multinomial logistic regression classifier with L2-
normalized inputs, L2-normalized weights, no bias, and temperature
scaling.
********** 16 **********

[Text in pictures on this page, read by OCR]
Feature tn” Large Language Model Vision Language Model (VLM)
Primary Input Text only Images and Text

Knowledge Base Derived from text corpora Grounded in both text and visual
Core Ability Generation. reasoning and Multimodal reasoning across vision
Example Task “Write a poem about the ocean.” “Describe what is happening in this

picture of a beach.”
--- page 17 ---
• When interpreted this way, the image encoder is the computer vision
backbone which computes a feature representation for the image and the
text encoder is a hypernetwork which generates the weights of a linear
classifier based on the text specifying the visual concepts that the classes
represent.
iv.
(i) Softmax with temperature T=0.01
Logits === cosine/T ⇒[62,  55,  40].
Stabilize by subtracting max (62): [0,  −7,  −22].
Exponentials: [e0,  e−7,  e−22]≈[1,  0.0009119,  2.789×10−10].
Sum S≈1.0009119.
Probabilities
• p(lion)=1/S≈0.9991
• p(zebra)=0.0009119/S≈0.0009
•   p(giraffe)≈0.0000
(ii) Predicted class: lion (highest probability).
Q6
a.   With reference to Denoising Diffusion Probabilistic models (DDPM), answer the   [10]
CO-
following:
4;
SO-   i.   What is the similarity between Hierarchical VAE and DDPM?
2;
ii.   Explain how Gaussian noise is added over T steps to obtain xt from x0.
BL-
iii.   What is the advantage of reparameterization technique in forward diffusion
2
process of DDPM? What is the advantage of this technique?
Solution:
(similarity: 4 marks, gaussian noise added: 3 marks, reparameterization technique: 3
marks)
i.
• Both are latent-variable generative models.
DDPM can be viewed as a VAE with a very deep hierarchy of latents
{zT,…,z1}; the forward noising q(zt∣zt−1) plays the role of an inference model,
and the reverse denoiser pθ(zt−1∣zt) is the decoder—just like a hierarchical VAE
with many stochastic layers.
• Both optimize an ELBO-style objective.
DDPM’s standard noise-prediction MSE is equivalent to maximizing a
variational lower bound (under a fixed forward process), mirroring the VAE’s
ELBO training.
• Both use simple Gaussian conditionals at each layer.
Hierarchical VAEs and DDPMs factorize generation into a chain of Gaussian
transitions, making each step easy to train and sample.
• Both perform iterative refinement.
Samples are produced by ancestral sampling through layers/steps (top-down in
VAEs; denoise steps in DDPM), progressively adding detail.
********** 17 **********
--- page 18 ---
• Both support conditional generation naturally.
Conditioning (class/text) can be injected into the decoder/denoiser (akin to
cVAE vs. guided diffusion), steering the same latent chain.
•   Intuition: a DDPM is essentially a very deep hierarchical VAE with a fixed
encoder (the noising process) and a learned decoder (the denoiser), trading one
big jump for many tiny Gaussian steps.
ii.
iii.
The reparameterization trick was first popularized in VAEs, and it allows the gradient to
flow through random sampling.
In DDPM:
• Sampling from a Gaussian normally breaks gradient flow.
• Rewriting it as a deterministic function of a noise sample lets us differentiate
through the sampling process.
A. Enables Efficient and Differentiable Training
• By expressing xt in terms of ϵ, we can backpropagate gradients during training.
• The neural network learns to predict ϵ directly.
B. Simplifies Sampling
• We can compute any noisy image xt directly from x0 without iterating through all
previous steps.
• This makes the forward diffusion process analytically tractable and efficient.
C. Improves Numerical Stability
• Because αˉ and ϵ are explicit, we can control the noise schedule precisely.
********** 18 **********

[Text in pictures on this page, read by OCR]
Forward (noising) process in DDPM
We define a noise schedule {8}4, with 6; € (0,1), and ay = 1 — 8, & = Ia Qi.
1. One-step transition (Markov):
(xe | t1) = N(Var ara, (1—a:)Z),
equivalently
wy = Voy ey) + Vl—ae, EX N (0,1).

2. Closed-form from <9 in one shot:

By composing the steps,
q(t | xo) = N( Vat xo, (1 — &e)I),
so you can sample directly as
y= Vai zy + V1 — Ge, e~ N(0,1).

Intuition: Each step shrinks the signal by ,/a and adds Gaussian noise with variance 1 — a. After T' steps,
the signal is heavily attenuated (,/a7 ~ 0) and a7 is close to isotropic Gaussian.
--- page 19 ---
• This ensures smooth transitions between clean and noisy states.
D. Reduces Computational Complexity
•   Instead of performing thousands of noise-addition steps, you can jump directly to
any step.
• Makes the process fast and parallelizable — crucial during training.
CO-   b.   [10]
5;   i. Given two retrievers A and B have identical Recall@10 but A has higher
SO-   MRR@10, analyze what this implies about ranking quality and user experience.
1;   ii. With reference to LLM evaluation, answer the following:
BL-   a. Explain the term LLM as a Judge.
b. How does LLM as a judge work (typical set up)?
2, 3
c. Highlight the limitations and issues of this approach.
Solution:
(i:3 marks, ii: 7 marks (explaining the term: 2 marks, typical set up: 3 marks,
limitations and issues: 2 marks)
i.
• Ranking quality: If Recall@10 is equal, both systems surface a relevant item
somewhere in the top-10 at the same rate. The higher MRR@10 for A means the
first relevant result appears at higher ranks on average (closer to rank-1), so A’s
ordering is superior.
• User experience: Users find a good answer faster with A—fewer scrolls/clicks,
higher top-1/top-3 precision, and better perceived relevance.
• RAG impact: If your generator mainly consumes top-1 (or a small k), A will yield
more accurate, faithful answers because the correct context is earlier in the list.
•   Operational effects: Better MRR often reduces latency to success (fewer follow-up
queries) and support load; same Recall but lower MRR (system B) risks users
missing the relevant item despite it being in top-10.
ii.
a. An intriguing development in LLM evaluation is using Large Language Models
themselves to evaluate the outputs of other LLMs (or even their own outputs). This
approach is often termed LLM-as-a-judge or LLM-based evaluators. It offers a way
to scale evaluations without needing humans for every comparison. For example,
instead of having humans compare Model A vs Model B responses, we might prompt
GPT-4 to choose the better response for each prompt, effectively creating an AI
judge.
b. How LLM-as-a-judge works: Typically, you provide the evaluating LLM with the
original question/prompt and the two answers (or one answer and maybe a reference
solution), and ask it to output which answer is better or to give a score. A carefully
crafted prompt is important - it might include a rubric like "The ideal answer is
factually correct, concise, and polite. Here are two answers, please choose which is
better according to those criteria and explain why." Some setups have the LLM just
output a choice (A or B), others have it output a score 1–10, others have it output a
detailed explanation (which can help in understanding the rationale). Chain-of-
thought prompting (where the LLM is told to reason step-by-step) has been found to
improve the quality of its evaluations.
• LLM judges can approximate human preferences reasonably well in certain
domains, especially if the criteria are well-defined. They are extremely
********** 19 **********
--- page 20 ---
consistent in how they apply the given rubric (no annotator mood swings or
fatigue, unless the prompt itself has randomness).
• They are very fast and cheap once you have the model (especially if using an
open-source LLM as the judge, or an API like GPT-4 which, while not free,
can evaluate thousands of pairs much faster than humans could).
c.
• Inconsistency and prompt sensitivity: LLM evaluators can be inconsistent.
For instance, phrasing the evaluation prompt slightly differently might change
the outcome, indicating they are not entirely robust evaluators . Also, if asked
to score outputs independently, they might not maintain a stable scale (one
day a response is "8/10", another day the same response might get "7/10"
because these models don't have a persistent rubric memory unless enforced
via prompt). Some work suggests that having them do pairwise comparisons
(A vs B) is more stable than absolute scoring.
• Biases and alignment: LLMs carry biases from their training. If asked to judge
outputs, they might have a bias towards more verbose or formal answers, or
they might reflect biases in content (e.g., prefer answers that align with
majority opinions in training data). One study noted that LLM-based
evaluations are prone to similar biases as human ones, since the LLM was
trained on human-written content and human preferences. Moreover, if the
model being evaluated and the model judging have similar weaknesses, the
judge might not catch certain errors. For example, if both have a propensity
to think a subtly false statement is true, the LLM judge won't flag the other
model's false statement as wrong.
• Honesty of explanation: If an LLM judge provides a reasoning, it might
produce a plausible-sounding explanation that isn't actually the true reason it
preferred one output. It could potentially rationalize a choice that was made
due to some spurious pattern. So reading LLM judges'
explanations needs caution - they are not guaranteed to reflect the real
"thought process" (since they don't have one in the human sense, they just
generate likely text). However, these explanations can still be informative and
even out-of-line explanations can signal a problem in the judging process.
• Ranking vs rating: Empirical evidence suggests LLM judges perform better
when choosing between outputs than when giving an absolute score . In a
pairwise setup, models like GPT-4 can identify which answer is more correct
or better written with reasonable accuracy. When asked to just rate a single
answer on a scale, they might exhibit scale drift (e.g., tend to rate things higher
overall than a human would, or compress everything to a narrow band). To
mitigate this, some frameworks use Elo ratings or TrueSkill by doing many
pairwise comparisons and deriving a ranking for models from those.
•   Self-evaluation: If one uses the same model to evaluate itself, that can be
problematic. It might be overly lenient or simply mirror its own confusion. A
model might think an answer it wrote is good because it cannot see the
mistake. Using a stronger or at least different model as the judge is advisable.
For example, using GPT-4 to judge outputs from GPT-3.5 or another model.
Or use an ensemble of judges (GPT-4, plus some rules, plus maybe another
LLM). There's research on "ensembling" LLM evaluators or calibrating them
with some human feedback to improve reliability.
• Tricking LLM judges: There have been cases observed where a poorer answer
can fool the LLM judge by, say, including an authoritative tone or even a fake
reference. For example, if one answer boldly states a (wrong) fact and the
other answer is unsure, the LLM judge might prefer the confident (but wrong)
********** 20 **********
--- page 21 ---
answer if its prompt isn't carefully instructing it to check factuality.
Essentially, an LLM judge might be swayed by the style of the answer. If not
told to prioritize correctness, it might favor a more verbose, polite answer
over a terse but correct one. Crafting the judge prompt to avoid these pitfalls
is an area of ongoing tweaking.
Given these limitations, the consensus is that LLM-as-a-judge is helpful but not yet a
replacement for human eval in all cases. It's great for rapid iteration - for example, you can
have GPT-4 evaluate 1000 pairs of answers from two model versions in minutes and give a
sense of which is better. But before deploying a model, you'd still want to do a human eval to
double-check, especially for critical aspects. Some work has combined them: using LLM
judgements as a filter or first pass, then having humans look at a subset of cases or just
validating the final conclusion.
Q7   a.   Considering a specific application of Text-to-Image Generation for E-commerce   [5]
CO-   Product Creatives, answer the following questions:
1;   • highlight the process of generation,
SO-   • Justification of choice of the chosen architecture
2;   • Generation pipeline
BL-
2   Solution:
(process of generation: 1 mark, choice of architecture: 2 marks, generation pipeline:
2 marks)
Generation process: Prompted, evidence-controlled denoising in latent space with
guardrails yields repeatable, editable outputs ready for production use.
Architecture choice: Diffusion/ CLIP
Diffusion models reliably avoid mode collapse common in GANs, yielding varied
angles/styles.
Generation pipeline:
Data curation: Curate compliant, high-res product shots; label style tags (angle, lighting,
background).
Tokenizer/encoder: Use a robust text encoder (e.g., CLIP). Build a style glossary (brand
lexicon) to stabilize prompts.
Base latent-diffusion model: Training a U net based diffusion model.
Inference (Generation) step:
CO-   b.   Give a practical example explain the Agentic AI four-step process for problem-   [5]
6;   solving.
SO-
2;   Solution:
BL-
2   • Perceive (Observe & Understand)
• Parse the goal + context (user request, constraints, prior state, environment/tool
outputs).
• Normalize into a task state (entities, slots, assumptions).
•   Artifacts: parsed intent, constraints, confidence.
•   Pitfalls: ambiguous goals → add a clarifying question.
Plan (Decompose & Choose Tools)
• Break the goal into actionable steps; pick tools/APIs and an execution order; set
stop criteria.
• May simulate/chain-of-thought privately to evaluate alternatives.
•   Artifacts: step list, chosen tools, arguments, success checks.
********** 21 **********
--- page 22 ---
•   Pitfalls: overlong plans → prune to minimal viable path.
Act (Execute & Retrieve)
•   Call tools with structured inputs; handle retries/timeouts; enforce schemas and
guardrails (e.g., policy checks).
•   Integrate results back into state; branch conditionally if results fail checks.
•   Artifacts: tool traces, evidence (docs/DB rows), intermediate answers.
•   Pitfalls: tool errors, stale data → add backoff, validation, and fallbacks.
Reflect (Verify, Learn, Update Memory)
• Verify against specs/constraints; cross-check with sources; detect uncertainty and
abstain or ask for clarification when needed.
• Summarize what worked, update memory/state, and produce the final answer with
citations/actions taken.
•   Artifacts: verified output, rationale, updated long-/short-term memory.
•   Pitfalls: hallucination → require evidence-backed claims and confidence
thresholds.
Tiny example: expense-policy query
Perceive: read the question + user’s dept/region → Plan: “retrieve latest policy; extract
per-diem; compute total” → Act: vector-search + policy API; compute → Reflect: check
effective date, include section citation; if missing, ask user or abstain.
CO-   c.   You are given a reference and a predicted summary (case-insensitive, whitespace
5;   tokenization):
SO-   Reference (R): the child plays in the park
2;   Candidate (C): child plays in the park
BL-   Use exact unigram matching only (no stems/synonyms). Assume the matched tokens
3   form one contiguous chunk in the reference (i.e., ch=1).
Assume α (parameter controls the relative weights of precision and recall) = of 0.9,
𝒄𝒉 𝟑
fragmentation penalty = 0.5x ( 𝒎)
Calculate the following:
d. Find matched tokens m, lengths ∣C∣, ∣R∣, and compute Precision P and Recall
R.
e. Compute weighted F-score Fmean.
f. With ch=1, compute the Penalty and the final METEOR.
Solution:
(i: 2 marks, weighted F-score: 1 mark, penalty and METEOR: 2 marks)
R: the child plays in the park → ∣R∣=6|R|=6∣R∣=6
C: child plays in the park → ∣C∣=5|C|=5∣C∣=5
Exact matches (contiguous): child, plays, in, the, park ⇒ m = 5
i. Precision & Recall
P=m/∣C∣=5/5=1.000
R=m/∣R∣=5/6≈0.8333
ii. Recall-weighted F-mean
Fmean=10PRR+9P=10⋅1⋅(5/6)(5/6)+9=5059≈0.8475
********** 22 **********
--- page 23 ---
iii. Penalty & METEOR (given one chunk ch=1)
Penalty=0.5(ch/m)3=0.5(1/5)3=0.004
METEOR=Fmean⋅(1−Penalty)≈0.8475×0.996≈0.844
Answer: P=1.000, R=0.8333, Fmean≈0.8475, METEOR≈0.844.
CO-   d.   For an outbound-email agent, list three risks (data exfiltration, persuasive harm,
6;   over-automation) and one mitigation each.
SO-
2;   Solution:
BL-   Data exfiltration (sending sensitive info to the wrong recipient)
2   Mitigation: Enforce DLP + allowlists: classify/redact PII/PHI, block external domains by
default, require human approval for first-time recipients or when sensitive entities are
detected.
Persuasive harm (manipulative or non-compliant messaging at scale)
Mitigation: Policy-grounded templates + toxicity/compliance filters: constrain generation
to approved templates, run safety/compliance classifiers, and require legal/brand-review
for high-risk intents.
Over-automation (sending without adequate human oversight, mistakes multiply fast)
Mitigation: Human-in-the-loop + rate limits + staged rollout: queue emails for
review/approval above confidence or impact thresholds, apply per-recipient/per-hour caps,
and maintain audit logs with instant rollback/cancel.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper d52dadbd7844

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_AI_7051/GENERATIVE AI/ANS_GENERATIVE AI(702AI0C030)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: text (20 pages)

````text
SYNOPTICS
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
1. This question paper contains 20 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
CO-2;   a.   Assume that we are using a transformer encoder block in which when using self-attention   [5]
BL-3   output for a 2-token Sequence, the input tokens are:
x1= [1,0], x2= [0,1]
The query, key and value matrices are given by
WQ=[1 0 WK=[1 1 WV=[2 0
0   1],   0   1],   1 1]
Compute the self-attention output for tokens x1 and x2 .
Solution:
(2.5 marks each for x1 and x2)
For token x1
q1=x1WQ= [1,0] [1 0 1]= [1,0]
0
k1=x1WK= [1,0] [1 1 1]= [1,1]
0
v1=x1WV= [1,0] [2 0 1]= [2,0]
1
For token x2
q2=x2WQ= [0,1] [1 0 1]= [0,1]
0
k2=x2WK= [0,1] [1 1 1]= [0,1]
0
v2=x2WV= [0,1] [2 0 1]= [1,1]
1
attention scores for token x1
q1⋅k1= [1,0]⋅[1,1]=1
********** 1 **********
--- page 2 ---
q1⋅k2= [1,0]⋅[0,1]=0
scaled scores:
[ 1 , 0 ] = [0.707,0]
√2 √2
e0.707≈2.028, e0=1
Attention weights for x1:
α1= 2.2028/3.2028 = 0.670, α2= 1/3.2028 = 0.330
weights= [0.670,0.330]
Output for x1=0.670[2,0] + 0.330[1,1] = [1.340,0] + [0.330,0.330] =[1.670,  0.330]
attention scores for token x2
q2⋅k1= [0,1]. [1,1] = 1
q2⋅k2 = [0,1]. [0,1]= 1
scaled scores:
[ 1 , 1 ] = [0.707, 0.707]
√2 √2
Because both values are equal, the softmax weights are equal: [0.5,0.5]
Output for x2 = 0.5[2,0] + 0.5[1,1] = [1,0] + [0.5,0.5= [1.5,0.5]
CO-1;   b.   Suggest ways to address the following challenges in Generative AI:   [5]
BL-4   1. Metrics for evaluation
2. Training challenges
3. Ethical considerations
Solution:
(metrics:2 marks, training challenges:1.5 marks: ethical considerations: 1.5 marks)
CO-5;   c.   [5]
BL-3   The reference summary and the candidate summary generated by LLM for a model
is as given below:
Reference summary: the system gives correct answers
Candidate summary: the system gives useful correct answers
Compute:
i.   overlapping bigrams
********** 2 **********
--- page 3 ---
ii.   precision
iii.   recall
iv. ROUGE-2 F1 score
Solution:
(1 mark for i, ii and iii each. 2 marks for iv)
i. List the bigrams
Reference bigrams
•   the system
• system gives
•   gives correct
•   correct answers
Total reference bigrams: 4
Candidate bigrams
•   the system
• system gives
•   gives useful
•   useful correct
•   correct answers
Total candidate bigrams: 5
ii. Overlapping bigrams
Common bigrams in both reference and candidate:
•   the system
• system gives
•   correct answers
So, number of overlapping bigrams: 3
iii. Precision
Precision=overlapping bigrams/candidate bigrams= 3/5=0.6
iv. Recall
Recall=overlapping bigrams/reference bigrams=3/4=0.75
5) ROUGE-2 F1 score
ROUGE-2=2PR/(P+R)
ROUGE-2=2(0.6)(0.75)/(0.6+0.75) =0.9/1.35=0.6667
CO-3;   d.   i.   State the two fundamental techniques that contribute to Hierarchical Navigable [5]
BL-3   Small World (HNSW).
ii.   In a simplified HNSW search, the query-to-node distances are:
A=1.513, B=0.539, C=1.700, D=0.943, E=0.539, F=0.
If k=2, determine the returned top-2 nodes.
If k=3, determine the returned top-3 nodes.
Solution:
(stating techniques with very brief explanation: 2 marks, numerical: 3 marks)
i.
• The two fundamental techniques that contribute to HNSW:
********** 3 **********
--- page 4 ---
•   Probability skip list
• Navigable small world graphs
ii.
Sorted from smallest to largest:
F(0), B(0.539), E(0.539), D(0.943), A(1.513), C(1.700)
If k=2
Top-2 nodes are:
F, E or B
If k=3
Top-3 nodes are:
F, B, E
Q2
CO-2;   a.   With respect to the GPT1 model answer the following questions:   [10
BL-   i.   State and explain the loss function used in the pretraining and fine-tuning
]
2,3   stage.
ii.   Justify the significance of Task Specific Input Transformations as used in
GPT1.
iii.   Compare GPT1 and BERT model.
Solution:
(Loss function: 3 marks, significance of Task Specific Input Transformations: 4 marks,
comparison: 3 marks)
i.
• Learning Objectives and Concepts: This semi-supervised learning (unsupervised
pre-training followed by supervised fine-tuning) for NLP tasks has following three
components:
•   a. Unsupervised Language Modelling (Pre-training): For unsupervised learning,
standard language model objective was used.
•
• where T was the set of tokens in unsupervised data {t_1,…,t_n}, k was size of
context window, θ were the parameters of neural network trained using stochastic
gradient descent.
•
• where C was the labeled dataset made up of training examples.
•   Instead of simply maximizing the objective mentioned in equation (ii), the authors
added an auxiliary learning objective for supervised fine-tuning to get better
generalization and faster convergence. The modified training objective was stated
as:
• where L₁(C) was the auxiliary objective of learning language model and λ was the
weight given to this secondary learning objective. λ was set to 0.5.
********** 4 **********
--- page 5 ---
•   Supervised fine-tuning was achieved by adding a linear and a Softmax layer to the
transformer model to get the task labels for downstream tasks.
ii.
•   In order to make minimal changes to the architecture of the model during fine
tuning, inputs to the specific downstream tasks were transformed into ordered
sequences.
The tokens were rearranged in following manner:
Start and end tokens were added to the input sequences.
A delimiter token was added between different parts of example so that input
could be sent as ordered sequence.
For tasks like question answering, multiple choice questions etc. multiple
sequences were sent for each example.
E.g. a training example comprised of sequences for context, question and answer
for question answering task.
• GPT-1 uses the same Transformer decoder architecture for all tasks.
• The only thing that changes between tasks is how the input text is formatted
(transformed) so that the model can treat every task as predicting the next
token in a sequence.
•   Instead of building separate architectures for classification, entailment, or
QA, GPT-1 turns each task into a language modeling problem through
special input arrangements.
• Allows a single pretrained LM to handle multiple NLP tasks without
changing its internals.
• The model doesn’t need task-specific layers; it just gets a different prompt-
like input format.
•   Training objective remains next token prediction.
• Task Specific Input Transformations
• Text Classification
• Example Task: Sentiment analysis.
• Transformation:
•   Input: "Review: The movie was fantastic. Sentiment: “
• The model predicts the next token(s) → "positive“
The label is simply another token in the sequence.
iii.
CO-5;   b.   i. The reference sentence and the candidate sentence generated by the LLM is as given   [10
BL-   below:
]
3,4   Reference: the child plays in the park
Candidate: child plays in the park
Assume:
• exact unigram matching only
• matched tokens form one contiguous chunk, so c=1
• α=0.9, γ=0.5, β=3
Compute:
a. number of matched tokens m
b. candidate length and reference length
********** 5 **********
--- page 6 ---
c. precision and recall
d. weighted F-score
e. penalty
f. final METEOR score
ii. Compare METEOR and BLUE score evaluation metrics as used in LLMs.
Solution:
(i: 7 marks, ii: 3 marks)
i.
(a, b,c,d,e: 1 mark each, f: 2 marks)
Number of matched tokens mmm
Reference tokens:
the, child, plays, in, the, park
Candidate tokens:
child, plays, in, the, park
Matching unigrams:
child, plays, in, the, park
So, m=5
Candidate length and reference length
Candidate length:
∣C∣=5
Reference length:
∣R∣=6
3) Precision and Recall
P=m/∣C∣=5/5=1
R=m/∣R∣=5/6=0.8333
4) Weighted F-score
Fmean=PR/(αP+(1−α)R)
Fmean=(1)(0.8333)/(0.9(1)+0.1(0.8333))≈0.8475
5) Penalty
The slides use chunk penalty:
Penalty=γ(c/m)β
Penalty=0.5(1/5)3 =0.004
6) Final METEOR score
METEOR=(1−Penalty)×Fmean =(1−0.004)×0.8475≈0.8441
ii.
Aspect   BLEU   METEOR
Full form   Bilingual Evaluation   Metric for Evaluation of Translation
Understudy   with Explicit Ordering
Main basis   n-gram precision with   Unigram matching with weighted
brevity penalty   precision-recall and chunk penalty
Matching level Usually 1-gram to 4-gram   Mainly unigram alignment
overlap
Precision /   Primarily precision-   Uses both precision and recall, usually
Recall focus   oriented   giving more weight to recall
********** 6 **********
--- page 7 ---
Penalty used   Brevity penalty for very   Fragmentation / chunk penalty for poor
short outputs   word order
Word order   Limited   Better, because chunk penalty rewards
handling   correct ordering
Flexibility in   Mostly exact word matches Can consider exact forms, stems,
matching   synonyms, and meanings
Sensitivity to   Lower   Higher
paraphrases
Best suited for Quick automatic evaluation More refined evaluation when wording
of translation overlap   may differ but meaning is similar
Limitation   Misses semantic similarity,   Still reference-based; does not directly
recall, and deeper meaning   measure factual correctness or
i.   reasoning
Q3
CO-3; a.   i.   Compare Simple RAG and advanced RAG techniques.   [10
ii.   Explain why chunking is necessary in the indexing phase of a RAG system.
BL-4   ]
Analyze how chunk size and chunking strategy affect retrieval quality,
efficiency, and final answer relevance.
Solution:
(5 marks each)
i.   (Any 5 correct points)
Aspect   Simple RAG   Advanced RAG
Core idea   Basic pipeline: indexing   Extended pipeline with index
→ retrieval → generation   optimization, pre-retrieval, retrieval,
post-retrieval, and generation
Retrieval   Usually basic vector   Can use hybrid retrieval: dense
method   similarity search   semantic search + sparse keyword
search
Query   Query is embedded and   Adds query processing, such as
handling   sent directly for retrieval   rewriting, summaries, routing, and
confidence judgment
Indexing   Standard chunking +   Improves indexing using sliding
embeddings stored in   windows, fine-grained segmentation,
vector DB   and metadata
Post-   Minimal or no extra   Includes reranking, filtering, and
retrieval   processing   reordering of retrieved documents
Context use   Retrieved chunks are   Uses contextual fusion to combine
passed directly to the LLM retrieved evidence more coherently
Feedback   Usually absent   Often includes feedback loops using
loop   clicks, corrections, ratings, or retriever-
generator co-training
Accuracy   Good for straightforward   Higher accuracy, adaptability, and
use cases   performance
Complexity   Easier to build and deploy More complex, with more components
and tuning
ii.
• Chunking is necessary because the indexing phase breaks large documents into
small, searchable units, generates an embedding for each chunk, and stores those
chunk embeddings in the vector database. This makes retrieval manageable and
efficient instead of searching whole documents.
********** 7 **********
--- page 8 ---
•   It is needed because a large document often contains multiple topics. If the full
document is stored as one unit, retrieval may return a lot of irrelevant context
along with the useful part. Chunking keeps each piece more focused on a specific
idea.
• Smaller chunks usually improve retrieval precision because the returned text is
more specific to the query. But if chunks are too small, important context may be
split across chunks, so the LLM may receive incomplete information.
• Larger chunks preserve more context, which can help answer broader questions,
but they may reduce retrieval quality because each chunk mixes relevant and
irrelevant content. This can also make the final answer less focused.
•   Fixed-size chunking is simple and efficient, but it can cut sentences or ideas at
arbitrary places.
• Sentence-based chunking usually improves answer relevance because each chunk
preserves a complete thought.
• Paragraph-based chunking keeps broader context together, but it may be too
coarse for precise retrieval.
• Sliding-window chunking improves retrieval quality by using overlap, so
important information near boundaries is less likely to be lost. However, it
increases storage and indexing redundancy.
• Heading-based chunking works well when document structure is meaningful,
since chunks align with sections.
• Semantic/embedding-based chunking is often better for final answer relevance
because chunks are grouped by meaning rather than only by size, though it is more
complex to build.
Chunking is necessary because it makes document retrieval searchable, efficient, and
query-focused. The choice of chunk size and chunking strategy directly affects:
•   retrieval quality: how well the right chunk is found
•   efficiency: speed and storage cost
•   final answer relevance: whether the LLM gets enough context without too much
noise.
i.
CO-2; b.   With respect to LangChain, answer the following:   [10
BL-
]
3,4   i.   Explain the role of Chains in LangChain and differentiate between simple
chains and multi-step chains.
ii.   State the significance of PromptTemplate in LangChain applications.
iii.   Explain the working of LangChain in a query-answering pipeline, starting
from user query, vector representation, similarity search, retrieval of relevant
information, and final response generation.
Solution:
(Role of chain and multistep chain: 3 marks, PromptTemplate: 3 marks, query answering
pipeline: 4marks)
i. Role of Chains in LangChain; simple vs multi-step chains (3 marks)
• Chains are the basic workflow units in LangChain. They define a sequence of
operations where each step may involve an LLM call, tool use, or data processing.
• A simple chain has a single LLM invocation, where one prompt is passed to one
model and one output is produced.
********** 8 **********
--- page 9 ---
• A multi-step chain combines multiple LLM calls or actions, where the output of
one step becomes the input to the next step. This is useful for more complex tasks
such as extraction followed by summarization.
ii. How PromptTemplate helps in LangChain (3 marks)
• PromptTemplate helps structure prompts in a reusable and organized way instead
of hard-coding them manually.
•   It allows developers to define input variables, instructions, examples, and output
format clearly.
• This makes prompt management easier, supports consistent formatting, and
integrates smoothly with other LangChain features such as chains.
iii. Working of LangChain in a query-answering pipeline (4 marks)
1. User Query
The process starts when the user submits a query, such as asking a question.
2. Vector Representation
LangChain converts the query into an embedding vector that captures its semantic
meaning.
3. Similarity Search
This query vector is compared against vectors stored in a vector database to find
the most relevant context or documents.
4. Retrieval of Relevant Information
The top matching information is retrieved from the database so the model has
accurate and contextually relevant input.
5. Response Generation
The retrieved information is passed to the language model, which generates the
final answer for the user.
So, LangChain supports a complete pipeline of query → embedding → retrieval → LLM
response, making question answering more accurate and context-aware.
Q4
CO-3;   a.   Consider that Locality Sensitive Hashing (LSH) is being applied on two short documents: [10
BL-3   • Doc1 = "deep learning"
]
• Doc2 = "learning deep"
Use the following parameters:
•   shingle length k=2
• Hash functions:
H1(x)=(2x+1) mod 13, H2(x)=(3x+2) mod 13, H3(x)=(4x+1) mod 13
Determine:
1. True Jaccard similarity and Jaccard distance
2. Characteristic matrix
3. Signature matrix using the hash functions
4. Signature similarity
5. If 3 bands of 1 row each are used, determine whether they become a candidate pair
Solution:
(2 marks for each sub point)
True Jaccard similarity and distance
Doc1: "deep learning"
2-shingles:
{de, ee, ep, p_ , _l, le, ea, ar, rn, ni, in, ng}
********** 9 **********
--- page 10 ---
Doc2: "learning deep"
2-shingles:
{le, ea, ar, rn, ni, in, ng, g_, _d, de, ee, ep}
Here _ denotes a blank space.
Intersection
Common shingles:
{de, ee, ep, le, ea, ar, rn, ni, in, ng}
So,
∣S1∩S2∣=10|
Union
All unique shingles:
{de, ee, ep, p_, _l, le, ea, ar, rn, ni, in, ng, g_, _d}
So,
∣S1∪S2∣=14|
Jaccard similarity
J(S1,S2)=∣S1∩S2∣∣S1∪S2∣=10/14=5/7≈0.7143
Jaccard distance
d(S1,S2)=1−J(S1,S2)=1−0.7143=0.2857
Answer
•   Jaccard similarity =0.7143
•   Jaccard distance =0.2857
2) Characteristic matrix
Assign row IDs to the union of shingles:
0:de
1:ee
2:ep
3:p_
4:_l
5:le
6:ea
7:ar
8:rn
9:ni
10:in
11:ng
12:g_
13:_d
Row   Shingle   Doc1 Doc2
0   de   1   1
1   ee   1   1
2   ep   1   1
3   p_   1   0
4   _l   1   0
5   le   1   1
6   ea   1   1
7   ar   1   1
8   rn   1   1
9   ni   1   1
10   in   1   1
11   ng   1   1
12   g_   0   1
13   _d   0   1
********** 10 **********
--- page 11 ---
Sig(D1)=[0, 0, 0]
Sig(D2)=[0, 0, 1]
Signature matrix
4) Compare signatures and find similarity
Compare component-wise:
• Row 1 matches: 0=0
• Row 2 matches: 0=0
• Row 3 does not match: 0≠1
So signature similarity is:
2/3=0.6667
5) Banding: 3 bands of 1 row each
Since there are 3 hash rows, using 3 bands of 1 row each gives:
• Band 1: [0] vs [0]→ match
• Band 2: [0] vs [0] → match
• Band 3: [0] vs [1]→ no match
Since the two signatures match in at least one band, they become a candidate pair.
CO-2;   b.   i.   Analyze why GPT-3 is called a few-shot learner rather than just a larger language   [10
BL-   model.
]
2,3   ii.   Give one example of few-shot learning for GPT3 for a use case of your choice.
iii.   Highlight some of the limitations of GPT-3.
Solution:
(few-shot learner: 4, example: 2 marks, limitations: 4 marks)
i.
•   In-context learning
• Large language models develop pattern recognition and other skills using the text
data they are trained on.
• While learning the primary objective of predicting the next word given context
words, the language models also start recognising patterns in data which help
them minimise the loss for language modelling task.
•   Later, this ability helps the model during zero-shot task transfer.
• When presented with few examples and/or a description of what it needs to do, the
language models matches the pattern of the examples with what it had learnt in
past for similar data and uses that knowledge to perform the tasks.
• This is a powerful capability of large language models which increases with the
increase in the number of parameters of the model.
Few-shot, one-shot and zero-shot setting:
• Few, one and zero-shot settings are specialized cases of zero-shot task transfer.
•   In few-shot setting, the model is provided with task description and as many
examples as fit into the context window of model.
•   In one-shot setting the model is provided exactly one example and in zero-shot
setting no example is provided.
• With increase in capacity of model, few, one and zero-shot capability of model
also improves.
********** 11 **********
--- page 12 ---
ii.
In few-shot learning, GPT-3 is given a task description along with a few labeled
examples inside the prompt, and then it predicts the label for a new input. This uses in-
context learning instead of separate fine-tuning.
Example prompt (any such prompt )
Classify the sentiment of the review as Positive or Negative.
Review: The movie was amazing and full of suspense.
Sentiment: Positive
Review: The service was too slow and the food was cold.
Sentiment: Negative
Review: The product quality is excellent and worth the price.
Sentiment: Positive
Review: The laptop battery dies very quickly and performance is poor.
Sentiment:
iii.
• GPT-3 does not perform very well on tasks like:
•   natural language inference (determining that if a sentence implies other
sentence)
•   fill in the blanks
• some reading comprehension tasks etc.
• Another limitation pointed by the paper is GPT-3’s generic language modelling
objective which weighs each token equally and lacks the notion of task or goal-
oriented prediction of tokens.
• Other limitations of GPT-3 include complex and costly inferencing from model
due to its heavy architecture, less interpretability of the language and results
generated by model and uncertainty around what helps the model achieve its few
shot learning behaviour.
• High Computational Cost
• Running GPT-3 is resource-intensive, requiring significant computational
power and memory.
•   Bias and Ethical Concerns
• Like GPT-2, GPT-3 has been criticized for generating biased or harmful
content based on its training data. Addressing ethical concerns is a key area
of focus.
•   Factual Accuracy
• GPT-3 can sometimes generate incorrect or misleading information, as it
lacks true understanding of the facts it generates.
Q5
CO-1;   a.   Justify the use of large models help in visual question answering? Briefly state the steps.   [5]
BL-2
Solution:
(Justification: 2 marks, steps: 3 marks)
********** 12 **********
--- page 13 ---
Large models are useful in Visual Question Answering (VQA) because the task requires
both:
• understanding the image, and
• understanding the language question,
and then combining both to produce a correct answer. Large models are better at this
because they can learn rich visual features, capture language context, and model the
relationship between image content and question meaning.
Justification
• They can identify objects, scenes, colors, actions, and spatial relationships in the
image.
• They can understand different forms of natural language questions.
• They can connect visual information with textual meaning more effectively.
• Their large-scale training helps them generalize to many different question types.
Brief steps
1. Input image and question are given to the system.
2. A vision model extracts important features from the image.
3. A language model encodes the meaning of the question.
4. The large model combines image and text information.
5. It reasons over both inputs to find the most relevant answer.
The system outputs the final answer in text form.
CO-6;   b.   i. Compare Generative AI and Agentic AI.   [10
BL-   ii. How is a multi-agent system different than a single agent system?
]
2,4   iii. Analyze how memory and tool use together make agentic AI more effective than
simple text generation.
Solution:
(comparison: 4 marks, multi agent : 2 marks, memory and tool use together: 4 marks)
i.
ii.   Single vs Multi-Agent Systems
Single Agent:
One AI does everything, like a chatbot answering questions.
It’s simpler but may struggle with complex tasks.
Multi-Agent:
********** 13 **********
--- page 14 ---
Multiple AIs work together, like a team where one handles logistics and
another customer service.
It’s more robust but harder to coordinate.
iii.   Memory and tool use make agentic AI more effective than simple text generation
because together they let the system remember, verify, and act, instead of only
producing plausible text.
A simple LLM mainly works turn by turn. Its context is mostly limited to the current
prompt, so it may forget earlier constraints, user preferences, or intermediate
results. An agent, however, maintains state and memory across steps or sessions.
This allows it to store facts such as task progress, prior decisions, user preferences,
and retrieved information. Because of this, it can handle multi-step goals more
consistently and avoid repeating work or losing track of the objective.
Tool use adds a second major advantage. A plain LLM can only generate text from
its training and prompt context, so it may hallucinate or give stale information. An
agent can instead call tools such as search, databases, calendars, APIs, or payment
systems to fetch current and exact information, perform transactions, validate
outputs, and retry if needed. This makes the result more reliable and grounded in
real data.
Together, these two features are powerful:
Memory keeps the task coherent over time.
Tools connect the agent to the external world for accurate action and verification.
For example, in a travel assistant, memory stores the user’s preferred airlines, policy
constraints, and trip details, while tool use checks live flight prices, hotel availability, and
company policy limits. So the agent does not just “suggest” an answer — it can plan,
check, book, and confirm correctly.
CO-5;   c.   Briefly explain any two hybrid evaluation methods used to evaluate the performance of [5]
BL-2
LLMs.
Solution:
(2.5 marks each, any two given below)
• Human-in-the-loop + Automation
• Blending qualitative and quantitative
• LLM-assisted human eval
•   Iterative eval and refinement
• Continuous feedback loop
• Ensembling evaluators
•   Task-specific hybrid metrics
• Benchmark + human synergy
Q6
a.   [10
CO-4;   i.   Briefly explain how contrastive loss helps align image and text representations in
]
BL-   CLIP.
2,3   ii. Design and depict a zero-shot image classification pipeline using CLIP.
********** 14 **********
--- page 15 ---
iii. A CLIP training batch contains N=40 matched image-text pairs.
Find:
•   the total number of possible image-text pairings in the batch
•   the number of genuine matched pairs
•   the number of mismatched pairs
Solution:
(contrastive loss: 3 marks, zero-shot classification pipeline: 4 marks, numerical: 3 marks)
i.
CLIP uses two encoders: an image encoder and a text encoder. For a training batch of
NNN matched image–text pairs, it projects both modalities into a shared embedding
space, L2-normalizes them, and computes an N×N similarity matrix using cosine
similarity with temperature scaling. The diagonal entries correspond to the true image–
text matches, while the off-diagonal entries are mismatched pairs.
The contrastive loss then encourages the model to:
• increase similarity for the correct image–text pairs
• decrease similarity for incorrect pairs
CLIP applies this as a symmetric cross-entropy loss in both directions:
• image →text
•   text → image
This pulls semantically related images and captions closer together in the shared space
and pushes unrelated pairs apart, so both encoders learn aligned multimodal
representations.
ii.
Zero-shot image classification pipeline using CLIP
Steps
1. Input image
2. Pass image through the image encoder to get an image embedding.
3. Create text prompts for all candidate classes, such as:
o “a photo of a cat”
o “a photo of a dog”
o “a photo of a fox”
4. Pass all prompts through the text encoder to get text embeddings.
5. Project both into the same shared embedding space and normalize them.
6. Compute cosine similarity between the image embedding and each text
embedding.
7. Apply temperature scaling + softmax.
8. Choose the class with the highest similarity / logit as the prediction.
Image
↓
Image Encoder
↓
Image Embedding
↓
Shared Embedding Space
↑
Class Prompts → Text Encoder → Text Embeddings
↑
“a photo of a cat”
“a photo of a dog”
“a photo of a fox”
Then:
********** 15 **********
--- page 16 ---
Cosine similarity(Image Embedding, each Text Embedding)
↓
Temperature scaling + Softmax
↓
Highest score = Predicted class
iii.
1. Total possible image–text pairings
N2=402=1600
2. Number of genuine matched pairs
N=40
3. Number of mismatched pairs
N2−N=1600−40=1560
CO-4;   b.   i.   Explain the multi-step closed-form formulation of the forward diffusion process.   [10
BL-2,   ii. Explain why the reparameterization trick is useful in DDPM training.
]
4   iii. Analyze how reparameterization improves efficiency, differentiability, and
numerical stability during training.
Solution:
(the multi-step closed-form formulation of the forward diffusion process: 3 marks,
reparameterization trick: 3 marks, Analyze how reparameterization improves: 4 marks)
In DDPM, the forward process conceptually adds a small amount of Gaussian noise at
each timestep. Doing this one step at a time for hundreds or thousands of steps is correct
but inefficient. So the multi-step formulation combines all those small Gaussian additions
into one closed-form expression, which lets us sample a noisy image xt directly from the
original clean image x0 without generating all intermediate states. It expresses xt as a
balance between:
•   the remaining signal from x0, controlled by αˉt
•   fresh Gaussian noise ϵ∼N(0,I)
So, instead of simulating every noising step, we use one formula to jump directly to any
timestep t. The slides describe this as combining all the small Gaussian steps into a single
Gaussian distribution.
ii. Why the reparameterization trick is useful in DDPM training
The reparameterization trick is useful because sampling from a Gaussian normally breaks
gradient flow, which makes backpropagation difficult. DDPM rewrites the noisy sample
as a deterministic function of the clean image and a random noise sample. This allows
gradients to pass through the sampling process during training.
Because of this:
•   the model can be trained with standard gradient-based optimization
•   the network can learn to predict the noise ϵ directly
•   the loss becomes a simple and stable MSE between true noise and predicted noise
iii. How reparameterization improves efficiency, differentiability, and numerical stability
1. Efficiency
Reparameterization makes training efficient because we can compute any noisy sample x t
directly from x0, instead of simulating all previous diffusion steps. This means we do not
need to retain or compute all intermediate noisy images during training. The slides
explicitly say this makes the forward process analytically tractable, efficient, fast, and
parallelizable.
2. Differentiability
********** 16 **********
--- page 17 ---
It improves differentiability because the stochastic sampling step is rewritten so that
gradients can still flow through it. As a result, the model can be trained end-to-end with
backpropagation while learning to predict the added noise.
3. Numerical stability
It improves numerical stability because αˉt and ϵ are explicit in the formulation, so
the noise schedule can be controlled precisely. This ensures smoother transitions
between clean and noisy states and avoids unstable behavior during training.
Q7
CO-3;   a.   i.   Explain the basic idea of RAG and fine-tuning as two ways of improving LLM   [10
BL-2,   performance.
]
4   ii.   Describe situations where RAG is preferable to fine-tuning.
iii.   Analyze the trade-offs between RAG and fine-tuning in terms of cost, scalability,
freshness of knowledge, and domain adaptation.
Solution:
(i: 3 marks, ii: 3 marks, iii: 4 marks)
i. Basic idea of RAG and fine-tuning as two ways of improving LLM performance
RAG (Retrieval-Augmented Generation) improves an LLM by connecting it to an
external knowledge source. The documents are first chunked, converted into embeddings,
and stored in a vector database. When a user asks a question, the query is also embedded,
the most relevant chunks are retrieved, and those chunks are given to the LLM along with
the query so that it can generate a grounded answer. In short, RAG improves performance
by adding external context at inference time.
Fine-tuning improves an LLM by changing the model itself. The pretrained model is
further trained on task-specific or domain-specific data so that its parameters adapt to the
new use case. In short, fine-tuning improves performance by updating the model’s
learned behavior rather than retrieving external documents at runtime. The unit also
highlights fine-tuning as one of the main ways to optimize LLMs.
ii. Situations where RAG is preferable to fine-tuning
RAG is preferable when:
• knowledge changes frequently, because RAG can retrieve updated information
from external sources without retraining the model.
• answers need verification and traceability, since retrieved chunks can act as
supporting evidence.
•   the use case involves specialized domain knowledge that is stored in documents,
manuals, policies, or enterprise data.
•   data privacy preservation is important, because private knowledge can stay in an
external database and need not be baked into the model weights.
•   retraining would be too expensive, since the slides explicitly state that fine-tuning
large models is costly, while RAG can reduce this need by dynamically retrieving
relevant data.
So, RAG is generally better when the main problem is missing, changing, or domain-
specific knowledge rather than the base model’s language ability.
iii. Trade-offs between RAG and fine-tuning
1. Cost
RAG is usually more cost-effective when the goal is to add knowledge, because it avoids
repeated retraining of a large model. The slides note that fine-tuning large models is
expensive, while RAG can reduce cost and computational load by retrieving relevant data
********** 17 **********
--- page 18 ---
dynamically. However, RAG still requires a retrieval pipeline, embeddings, and vector
database infrastructure.
Fine-tuning can be more expensive upfront because it requires training resources, careful
hyperparameter tuning, and repeated experiments. The unit also notes that poor
hyperparameter choices waste compute and affect convergence and generalization.
2. Scalability
RAG is highly scalable across domains because the same base model can be used with
different knowledge bases. You mainly update the external documents, embeddings, and
index. This makes RAG flexible for many enterprise use cases.
Fine-tuning is less scalable when many domains or clients must be supported, because
separate tuning may be needed for each adaptation. That increases maintenance effort.
3. Freshness of knowledge
This is where RAG has a major advantage. It can retrieve up-to-date information in real
time from external sources, while a fine-tuned model may become outdated once the
underlying data changes. The slides explicitly list outdated information as a limitation of
static LLMs and present RAG as a solution.
Fine-tuning is weaker here because updating knowledge usually requires another tuning
cycle.
4. Domain adaptation
Fine-tuning is often stronger when the objective is to adapt the model’s style, behavior,
or task-specific capability, because the model parameters themselves are changed. This
can help the model follow domain conventions more naturally.
RAG is stronger when the main requirement is domain-specific facts and references,
because it injects external knowledge at answer time. But if the base model is weak at the
task itself, retrieval alone may not be enough.
CO-4;   b.   i. Explain the roles of patch embeddings, positional embeddings, and the [CLS] token [10
BL-   in ViT.   ]
2,3,4   ii. Analyze why ViT can capture global context better than CNNs but usually requires
larger pretraining datasets.
iii. A ViT is pretrained on 224×224 RGB images with patch size 16×16 and later fine-
tuned on 384×384 images with the same patch size.
Compute:
• number of patches during pretraining
• number of patches during fine-tuning
• change in sequence length after adding the [CLS] token
•   Identify why position embeddings become an issue during fine tuning.
Solution:
(roles of patch embeddings, positional embeddings, and the [CLS] token: 3 marks, why
ViT can capture global context: 3 marks, numerical: 4 marks)
i. Roles of patch embeddings, positional embeddings, and the [CLS] token in ViT
• Patch embeddings: The image is split into fixed-size patches, each patch is
flattened, and then linearly projected into a DDD-dimensional vector. These
embeddings convert the 2D image into a sequence of tokens that a Transformer
can process.
•   Positional embeddings: Since the Transformer does not inherently know the
spatial order of image patches, positional embeddings are added to patch
embeddings so the model can retain patch location and ordering information.
********** 18 **********
--- page 19 ---
• [CLS] token: A learnable classification token is prepended to the input sequence.
After passing through the Transformer encoder, its final output representation is
used as the overall image representation for classification.
ii. Why ViT captures global context better than CNNs but usually needs larger
pretraining datasets
ViT can capture global context better than CNNs because self-attention allows every
patch token to attend to every other patch token in the image. This makes it easier for
ViT to model long-range dependencies and whole-image relationships directly. CNNs, in
contrast, mainly rely on local receptive fields and inductive biases such as local
connectivity and weight sharing, so they build global understanding more gradually
through many layers.
However, ViT usually needs larger pretraining datasets because it does not have the
strong built-in inductive biases of CNNs. CNNs already encode useful assumptions like
locality and translation invariance, which helps them learn well even with smaller
datasets. ViT is more flexible, but that flexibility means it must learn these patterns from
data itself, so it benefits much more from large-scale pretraining. The slides explicitly
note that ViT scales very well with large data, but its drawback is that it needs very large
datasets for pretraining.
Number of patches in ViT:
N=H×W/P2
1) Number of patches during pretraining
Npre=224×224/16×16=50176/256=196
2) Number of patches during fine-tuning
Nfine=384×384/16×16=147456/256=576
3) Change in sequence length after adding the [CLS] token
Sequence length in ViT:
sequence length=N+1because of one extra [CLS] token.
During pretraining
196+1=197
During fine-tuning
576+1=577
4) Why position embeddings become an issue during fine-tuning
********** 19 **********
--- page 20 ---
Position embeddings become an issue because the pretrained model learned positional
embeddings for a sequence length of 197, but after moving to higher-resolution images
the new sequence length becomes 577. So the old position embeddings no longer match
the new patch grid directly and may no longer be meaningful unless adapted, resized, or
interpolated. The slides explicitly note that when fine-tuning at higher resolution with the
same patch size, the effective sequence length increases and the pretrained position
embeddings may no longer be meaningful.
********** 20 **********
````
