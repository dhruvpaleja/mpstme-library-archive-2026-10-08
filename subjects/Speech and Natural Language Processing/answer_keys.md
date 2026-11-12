# Speech and Natural Language Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Re-Exam · Sem 7 · Answer key · paper c8a561b82b8f

- Departments: Data Science
- Programmes: BTech DS 7009, MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_07/Re-Exam/MBATech_DS_7052/Speech and Natural Language Processing/ANS_Speech and Natural Language Processing(702DB0C028)_2024-2025.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (25 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/MBA Tch (DS)
Year: IV/Semester VII (Exam Year: 2025-2026)
Subject: Speech and Natural Language Processing
Date: 03 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)/RE EXAMINATION (2024-2025)
Instructions:
1. This question paper contains 25 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
9. The marks distribution is given for reference, may be changed as per the pattern of the given ans.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   What is tokenization and why is it important in NLP?   [05]
BL-2
ANS:
Tokenization is the process of breaking text into smaller units called tokens,
which can be words, subwords, or characters. For example, the sentence “I   2.5
love NLP” can be tokenized into [“I”, “love”, “NLP”].
Importance in NLP:
Standardizes input: Converts raw text into a structured format that models   2.5
can process.
Enables embedding: Each token can be mapped to a vector representation for
further analysis.
Facilitates text analysis: Helps in tasks like parsing, language modeling, and
information retrieval.
Handles vocabulary efficiently: Subword tokenization reduces the problem
of unknown words.
What is POS Tagging? Mention the applications of POS Tagging.
CO-3; SO-1;   b.   [05]
BL-2   ANS:
Part-of-Speech (POS) Tagging is the process of assigning grammatical
categories (such as noun, verb, adjective, adverb, etc.) to each word in a
sentence based on its definition and context.
********** 1 **********
--- page 2 ---
Example:
Sentence: “The cat sits on the mat.”   03
POS Tags:
• The → Determiner (DET)
•   cat → Noun (NN)
•   sits → Verb (VBZ)
• on → Preposition (IN)
•   the → Determiner (DET)
• mat → Noun (NN)
02
Applications of POS Tagging:
1. Information Retrieval: Helps search engines understand query
intent.
2. Machine Translation: Assists in accurate word alignment and
grammatical translation.
3. Text-to-Speech Systems: Determines correct pronunciation and
intonation.
4. Named Entity Recognition (NER): Helps identify names of people,
places, and organizations.
5. Syntactic Parsing: Used in building parse trees for sentence
structure analysis.
In short: POS Tagging adds grammatical intelligence to text, enabling
better understanding and processing in various NLP applications.
Differentiate between arguments and adjuncts with suitable examples.
CO-4; SO-1;   c.   [05]
BL-3   ANS:
Arguments
Arguments are essential elements that are required by the verb to complete
its meaning. They have a direct semantic relationship with the verb.   2x2.5
• Mandatory for grammatical completeness
• Determined by the verb’s valency
• Limited in number
• Cannot be freely omitted
Examples
1. She gave a book to her friend
• Arguments:
▪ a book (theme)
▪   to her friend (recipient)
2. He kicked the ball.
• Argument: the ball
If the argument is removed, the sentence becomes incomplete or
ungrammatical:
********** 2 **********
--- page 3 ---
• He kicked. (meaning incomplete)
Adjuncts
Adjuncts are optional elements that provide additional information such as
time, place, manner, reason, or condition. They are not required by the verb.
•   Optional
• Can be freely added or removed
• Not selected by the verb
• Can occur in large numbers
Examples
1. He kicked the ball in the park
• Adjunct: in the park (place)
2. She gave a book to her friend yesterday
• Adjunct: yesterday (time)
Removing adjuncts does not affect grammaticality:
• ✔ He kicked the ball.
Aspect   Arguments   Adjuncts
Necessity   Mandatory   Optional
Relation to   Selected by verb   Not selected by verb
Verb
Number   Limited   Unlimited
Removal   Makes sentence   Sentence remains
incomplete   grammatical
Type of Info Core meaning   Extra details (time, place,
manner)
Example Sentence with Both
She wrote a letter to her friend yesterday at home
• Arguments:
• a letter
•   to her friend
•   Adjuncts:
• yesterday
•   at home
CO-5; SO-1;   d.   Give the formula for self-attention and explain each variable.   [05]
BL-3
ANS:
01
********** 3 **********
--- page 4 ---
Explanation of Each Variable
1. Q (Query Matrix)
•   Represents what the current word is looking for
• Derived from the input embeddings
03
• Dimension: n×dk
• Computed as:
Q=XWQ
2. K (Key Matrix)
•   Represents what each word offers
• Used to match with the query
• Dimension: n×dk
• Computed as:
K=XWK
3. V (Value Matrix)
•   Contains the actual information to be aggregated
• Weighted by attention scores
• Dimension: n×dv
• Computed as:
V=XWV
4. QKT (Dot Product)
• Measures similarity between query and keys
• Produces attention scores indicating word relevance
5. sqrt{dk} (Scaling Factor)
•   Prevents dot-product values from becoming too large
• Helps stabilize gradients during training
6. softmax(·)
• Converts scores into probability distribution
• Ensures all attention weights sum to 1
7. Final Multiplication with V
• Produces the weighted sum of values
********** 4 **********
--- page 5 ---
• Output captures contextual representation of each word
Each word in a sentence:
• Compares itself with every other word (Q vs K)
• Assigns importance scores (attention weights)
• Combines information accordingly (V)
Example (Conceptual)   01
In the sentence:
"The animal didn’t cross the street because it was tired."
Self-attention helps “it” focus more on “animal” than “street”, improving
contextual understanding.
Q2   Describe the process of lemmatization. Explain rule-based, dictionary-
CO-1; SO-1;   a.   based, and morphological analysis-based lemmatization approaches with   [10]
BL-3   examples, advantages, disadvantages and their tools of implementation.
ANS:
Lemmatization
01
Lemmatization is the process of reducing a word to its base or dictionary
form (lemma) by considering its part of speech (POS) and morphological
structure. Unlike stemming, lemmatization produces linguistically valid
words.
Examples:
• running → run
•   better → good
•   children → child
Process of Lemmatization
1. Tokenization of text
2. POS tagging to identify grammatical role
3. Morphological analysis of the word
4. Lemma lookup or rule application
5. Output normalized base word
1. Rule-Based Lemmatization
03
Uses hand-crafted linguistic rules to convert words into their base forms by
removing suffixes or applying transformations based on POS.
********** 5 **********
--- page 6 ---
Example Rules
• Remove –ing, –ed → running → run
• Convert –ies → y → studies → study
Examples
Word   POS   Lemma
running   Verb   run
cars   Noun   car
Advantages
• Simple and fast
• No external resources required
• Easy to implement
Disadvantages
• Cannot handle irregular forms
• Language-dependent
• Limited accuracy
Tools
• Custom NLP rules
• spaCy (rule components)
• Snowball (limited lemmatization-like rules)
2. Dictionary-Based Lemmatization
03
Uses a predefined dictionary or lexicon that maps inflected words to their
lemmas.
Examples
Word   Lemma
better   good
children   child
went   go
Advantages
• Accurate for irregular words
• Produces valid dictionary forms
Disadvantages
•   Requires large dictionary storage
•   Fails for out-of-vocabulary words
********** 6 **********
--- page 7 ---
•   Language-specific
Tools
• WordNet Lemmatizer (NLTK)
•   Stanford CoreNLP
• MorphAdorner
3. Morphological Analysis-Based Lemmatization   03
Performs deep linguistic analysis by breaking words into:
• Root
•   Prefix
•   Suffix
• Grammatical features (tense, number, gender)
Example
• unhappiness → un + happy + ness → happy
• running → run + ing → run
Advantages
• High accuracy
• Handles complex word forms
•   Supports rich morphology languages
Disadvantages
• Computationally expensive
• Complex to implement
•   Requires linguistic expertise
Tools
• spaCy (advanced lemmatization)
• TreeTagger
•   Stanza (Stanford NLP)
• HFST (Helsinki Finite-State Tools)
Lemmatization improves text normalization in NLP pipelines and is
preferred over stemming when semantic meaning must be preserved,
especially in tasks like text classification, sentiment analysis, and
machine translation.
Q2   Using a small corpus word_counts and add-one (Laplace) smoothing,
CO-2; SO-1;   b.   calculate the bigram probability of the sentence:   [10]
BL-4
“Natural language processing is fun and exciting”
Where:
********** 7 **********
--- page 8 ---
word_counts = [("Natural", 2), ("language", 3), ("processing", 2), ("is",
4), ("fun", 1), ("and", 3), ("exciting", 1), ("other words…", 10)]
ANS:   02
Step1. Identify the Sentence Bigrams
The sentence has 7 words:
Natural, language, processing, is, fun, and, exciting
Bigrams are:
1. (Natural, language)
2. (language, processing)
3. (processing, is)
4. (is, fun)
5. (fun, and)
6. (and, exciting)
Step 2. Vocabulary Size (V)
word_counts = [
("Natural", 2),
("language", 3),
("processing", 2),
("is", 4),
("fun", 1),
("and", 3),
("exciting", 1),
("other words…", 10)
]
We count unique words:
Natural, language, processing, is, fun, and, exciting, other words
V=8   02
Assume bigram counts in the corpus:
Bigram   Count
(Natural, language)   1
(language, processing)   1
(processing, is)   1
(is, fun)   1
(fun, and)   0
(and, exciting)   0
01
********** 8 **********
--- page 9 ---
Step 4: Calculate Each Bigram Probability (Using Laplace Smoothing)
Formula used:
P(wᵢ | wᵢ₋₁) = ( C(wᵢ₋₁, wᵢ) + 1 ) / ( C(wᵢ₋₁) + V )
Where Vocabulary Size, V = 8
1. P(language | Natural)   03
P(language | Natural)
= (1 + 1) / (2 + 8)
= 2 / 10
2. P(processing | language)
P(processing | language)
= (1 + 1) / (3 + 8)
= 2 / 11
3. P(is | processing)
P(is | processing)
= (1 + 1) / (2 + 8)
= 2 / 10
4. P(fun | is)
P(fun | is)
= (1 + 1) / (4 + 8)
= 2 / 12
= 1 / 6
5. P(and | fun) (Bigram not seen) Assumed
P(and | fun)
= (0 + 1) / (1 + 8)
= 1 / 9
6. P(exciting | and) (Bigram not seen) Assumed
P(exciting | and)
= (0 + 1) / (3 + 8)
= 1 / 11
Step 5: Overall Sentence Probability
The probability of the sentence is the product of all bigram probabilities:
P(sentence)
= (2/10) × (2/11) × (2/10) × (1/6) × (1/9) × (1/11)   02
********** 9 **********
--- page 10 ---
P(sentence)
= 8 / 653400
≈ 0.00001224
Using add-one (Laplace) smoothing and assuming reasonable bigram counts,
the probability of the sentence:
“Natural language processing is fun and exciting”
is:
P ≈ 1.22 × 10⁻⁵
Laplace smoothing ensures that unseen bigrams such as (fun, and) and (and,
exciting) receive non-zero probabilities, preventing zero probability for the
entire sentence.
Q3   Evaluate and explain the joint probability of this sequence:
CO-2; SO-1;   a.   [1,3,2, H, C, H] For this given HMM:   [10]
BL-5
ANS:
Joint probability of the observation–state sequence
(o1,o2,o3)=(1,3,2)with(s1,s2,s3)=(H,C,H)
under the given HMM.
02
02
********** 10 **********
--- page 11 ---
02
02
02
Q3   Analyse how Dependency Parsing represents relationships between words
CO-3; SO-1;   b.   in a sentence, and explain how this structure helps in understanding
BL-4   sentence meaning compared to simple sequential parsing.
ANS:   [10]
Dependency Parsing in NLP
Dependency Parsing is a technique in Natural Language Processing that
represents the syntactic structure of a sentence by identifying binary   03
relationships (dependencies) between words.
• Each word in a sentence is connected to a head word (its governor)
via a labeled dependency (e.g., subject, object, modifier).
• The result is a dependency tree where the root represents the main
verb or central concept of the sentence, and other words branch
out according to their syntactic relationships.
How Dependency Parsing Helps in Understanding Sentence Structure
1. Captures grammatical relationships:
• Shows which words depend on which, e.g., subject → verb, 03
verb → object.
2. Disambiguates meaning:
• In sentences with multiple interpretations, dependencies
clarify relationships, e.g., "I saw the man with a telescope"
can be analyzed to identify who has the telescope.
3. Supports NLP applications:
********** 11 **********
--- page 12 ---
• Used in relation extraction, question answering, machine
translation, and information retrieval because it captures
meaning beyond simple word order.
Comparison with Sequential Parsing
Feature   Sequential   Dependency Parsing
Parsing
Focus   Linear order of   Head-dependent relationships   04
words
Ambigui Harder to   Resolves structural ambiguities via
ty   resolve   dependencies
Applicati Limited   Enables semantic-level understanding
ons   understanding   and NLP tasks
Example (Dependency Tree)
Sentence: "The cat chased the mouse"
chased
/   \
cat   mouse
|   |
The   the
• chased → root verb
•   cat → subject
• mouse → object
• Determiners (The, the) depend on their nouns
Dependency Parsing analyzes syntactic relationships, making it easier to
understand sentence meaning and support downstream NLP tasks.
Sequential view:
The → cat → chased → the → mouse
• Words are processed in order.
•   Relationships like subject and object are not explicitly represented.
• Meaning must be inferred indirectly from position, which becomes
difficult in complex or reordered sentences.
Q4   What are the components of the Encoder-Decoder network of
CO-5; SO-1;   a.   transformers? Explain with diagram.   [10]
BL-2
ANS:
A Transformer has an Encoder-Decoder architecture used for tasks like
translation.
********** 12 **********
--- page 13 ---
Components of Encoder-Decoder Network in Transformers
The Transformer architecture has two main parts:
1. Encoder
2. Decoder
Both are made up of stacked layers, typically 6 layers each (can be more or
fewer).
1. Encoder Components
Each encoder layer consists of the following components:
a) Input Embedding
• Converts input tokens into dense vector representations.
•   Captures semantic meaning of words.
b) Positional Encoding
04
• Adds information about the position of words since transformers do
not process sequences sequentially.
• Uses sine and cosine functions.
c) Multi-Head Self-Attention
• Allows each word to attend to all other words in the sentence.
•   Captures contextual relationships and long-distance dependencies.
•   Multiple attention heads learn different types of relationships.
d) Feed Forward Neural Network (FFN)
•   Applies two linear transformations with a non-linear activation
(ReLU or GELU).
•   Processes each position independently.
e) Add & Normalize
•   Residual connections followed by layer normalization.
• Helps stabilize training and improve gradient flow.
Encoder Input: Token embeddings + positional encodings
Encoder Output: Contextualized representations of the input sequence
Encoder: Takes the input sequence and produces contextual representations.
Each encoder layer has input embeddings with positional encoding, multi-
head self-attention, feed-forward layers, and residual connections with layer
normalization. Multiple encoder layers are stacked.
2. Decoder Components
Each decoder layer has similar components, with additional mechanisms:
********** 13 **********
--- page 14 ---
a) Masked Multi-Head Self-Attention
04
•   Prevents the model from attending to future tokens during training.
• Ensures autoregressive generation.
b) Encoder–Decoder Attention
• Allows the decoder to attend to encoder outputs.
• Helps align input and output sequences (e.g., in translation).
c) Feed Forward Neural Network
• Same as encoder FFN, applied to decoder outputs.
d) Add & Normalize
•   Residual connections and normalization after each sub-layer.
e) Output Layer
• A Linear layer transforms decoder outputs to vocabulary size.
• Softmax converts logits into probability distribution over possible
output tokens.
Advantages of Encoder–Decoder Transformer
• Enables parallel processing, unlike RNNs.
• Handles long-range dependencies efficiently.
•   Provides better performance in NLP tasks like translation,
summarization, and question answering.
Decoder: Generates the output sequence. Each layer has masked self-
02
attention (to prevent seeing future tokens), encoder-decoder attention
(attending to encoder outputs), feed-forward layers, and residual connections
with layer normalization.
********** 14 **********
--- page 15 ---
Final Output: Decoder outputs go through a linear layer and softmax to
produce probabilities over the vocabulary.
Q4   Explain in brief the three main approaches to Word Sense Disambiguation
CO-4; SO-1;   b.   (WSD): supervised, unsupervised, and knowledge-based. Discuss their   [10]
BL-4   advantages and disadvantages. Explain how RNN-based models can be
integrated with WSD for improved contextual disambiguation.
ANS:
Word Sense Disambiguation (WSD) Approaches
WSD is the task of identifying the correct sense of a word in a given context.
The three main approaches are:
1. Supervised WSD
• Method: Uses labelled datasets where words are annotated with their
correct senses. Machine learning models, including RNNs, are
trained to predict the sense of a word based on contextual features.   03
• Advantages:
• High accuracy when sufficient labelled data is available.
• RNNs capture sequential and contextual information,
improving disambiguation.
•   Disadvantages:
• Requires large labelled corpora, which are expensive to
create.
• May not generalize well to unseen words or domains.
• Example: In "I deposited money at the bank", supervised WSD
predicts financial institution for "bank".
********** 15 **********
--- page 16 ---
2. Unsupervised WSD
• Method: Uses unlabelled data to infer word senses, typically by
clustering occurrences based on context similarity (e.g., word   03
embeddings or RNN-based contextual embeddings).
• Advantages:
• No need for labelled data.
• Can discover new or rare senses dynamically.
•   Disadvantages:
• Lower accuracy than supervised methods.
•   Clusters may be ambiguous or hard to interpret.
• Example: Clustering sentences containing "bass" to distinguish fish
vs musical instrument.
3. Knowledge-Based WSD
• Method: Leverages lexical resources like WordNet to assign senses,
e.g., Lesk algorithm (definition overlap) or graph-based methods.   02
• Advantages:
• Does not require labelled corpora.
•   Interpretable results based on dictionary knowledge.
•   Disadvantages:
• Limited by the coverage of the knowledge base.
• May fail for contexts not represented in the resource.
• Example: Using WordNet, "The factory is a large plant" → "plant" =
industrial facility.
Integration of RNNs with WSD
• RNNs (LSTM/GRU) capture contextual dependencies across a
sentence.
•   In supervised or unsupervised WSD, RNNs generate context-aware   02
embeddings for target words, improving sense prediction.
• Example: "I went to the bank to withdraw cash" → RNN considers
surrounding words to correctly assign financial institution to "bank".
Q5   Explain briefly what a Probabilistic Context-Free Grammar (PCFG) is
CO-3; SO-1;   a.   and calculate the probability of the given parsed tree for the sentence:   [10]
BL-3,
"Tom gave Emma a gift today."
S → NP VP   [1.0]
NP → N   [0.6] → ("Tom", "Emma")
NP → Det N   [0.4] → ("a gift")
VP → V NP NP ADV [0.5] → ("gave Emma a gift today")
VP → V NP NP   [0.5] → ("gave Emma a gift")
N → "Tom"   [0.4]
N → "Emma"   [0.3]
N → "gift"   [0.3]
V → "gave"   [1.0]
Det → "a"   [1.0]
********** 16 **********
--- page 17 ---
ADV → "today"   [1.0]
ANS:
Sentence:
"Tom gave Emma a gift today."
Given PCFG Rules:
S → NP VP   [1.0]
NP → N   [0.6] → ("Tom", "Emma")
NP → Det N   [0.4] → ("a gift")
VP → V NP NP ADV   [0.5] → ("gave Emma a gift today")
VP → V NP NP   [0.5] → ("gave Emma a gift")
N → "Tom"   [0.4]
N → "Emma"   [0.3]
N → "gift"   [0.3]
V → "gave"   [1.0]
Det → "a"   [1.0]
ADV → "today"   [1.0]
Step 1: Identify the parse tree
03
We assume the parse tree uses:
• NP → N for “Tom” and “Emma”
• NP → Det N for “a gift”
• VP → V NP NP ADV for “gave Emma a gift today”
S
/   \
NP   VP
|   /   |   |   \
"Tom" V NP NP ADV
|   |   |   |
"gave" "Emma" "a gift" "today"
04
********** 17 **********
--- page 18 ---
03
Step 3: Compute probability of S → NP VP
• NP (subject) = 0.24
• VP = 0.0108
• S → NP VP = 1.0 × 0.24 × 0.0108 = 0.002592
Q5   Explain the concept of Text Clustering and its importance in Natural
CO-4; SO-1;   b.   Language Processing. Discuss the main clustering techniques used for   [10]
BL-4   grouping similar texts (such as K-Means and Hierarchical Clustering), and
illustrate the process with a suitable example.
ANS: (Diagram Required)
Text Clustering is the process of grouping similar documents or text
segments based on their semantic or lexical similarity. It helps in organizing
large collections of unstructured text into meaningful clusters without prior
labelling.
The goal is to automatically identify natural groupings or themes within a
text corpus—such as news topics, product reviews, or research abstracts—
based on content similarity.
Steps in Text Clustering
06
1. Text Preprocessing:
• Tokenization, stopword removal, stemming/lemmatization.
• Converts raw text into a clean, structured format.
2. Feature Extraction:
• Represent each document as a numerical vector using
methods like:
▪ Bag of Words (BoW)
********** 18 **********
--- page 19 ---
▪ TF-IDF (Term Frequency–Inverse Document
Frequency)
▪ Word Embeddings (Word2Vec, GloVe, BERT)
3. Similarity Measurement:
• Compute pairwise similarity between text vectors using
Cosine similarity or Euclidean distance.
4. Clustering Algorithm:
• Apply algorithms such as:
▪ K-Means (partition-based)
▪   Hierarchical Clustering (tree-based)
▪ DBSCAN (density-based)
5. Evaluation:
• Use metrics like Silhouette Score, Purity, or Adjusted Rand
Index to assess cluster quality.
Example (Detail)   04
Consider a set of documents:
1. “The bank approved the loan.”
2. “The river overflowed near the bank.”
3. “Loan interest rates are increasing.”
4. “Floods damaged the river embankment.”
After clustering using TF-IDF + K-Means:
•   Cluster 1: (1, 3) → Financial context
•   Cluster 2: (2, 4) → Geographical/River context
This shows how clustering can disambiguate the word “bank” based on
context.
Applications
• Document organization and topic discovery
•   Information retrieval and recommendation systems
• Text summarization and sentiment analysis pre-processing
Text clustering enables semantic grouping of unlabelled text using
distributional features. With advanced embeddings and clustering
algorithms, it helps uncover hidden structure and meaning within large
corpora efficiently.
Q6
CO-1; SO-1;   a.   Explain how Naive Bayes works for text classification with count   [10]
BL-3,   vectorizer.
ANS:
Naive Bayes for Text Classification with Count Vectorizer
********** 19 **********
--- page 20 ---
1. Overview of Naive Bayes:
• Naive Bayes is a probabilistic classifier based on Bayes’ theorem,
assuming that features are conditionally independent given the
class.
•   It is widely used for text classification, such as spam detection,
sentiment analysis, and topic categorization.
02x5
Where:
• C = class label
• X = feature vector of a document
2. Role of Count Vectorizer: (Example with all the calculations Count
Vectorizer)
• Count Vectorizer converts a text corpus into a document-term
matrix.
• Each document is represented as a vector of word counts.
• This provides the feature representation required for Naive Bayes.
Example:
Corpus:
1. “I love NLP”
2. “NLP is amazing”
Count Vectorizer Output:
Word   Doc1   Doc2
I   1   0
love   1   0
NLP   1   1
is   0   1
amazing   0   1
3. Training Naive Bayes:
1. Compute prior probabilities of each class: P(C)
2. Compute likelihood probabilities of each word given the class:
P(word∣C)
• Use Laplace smoothing to handle zero counts.
3. Store these probabilities as the model parameters.
4. Classification:
• For a new document:
1. Transform it into a count vector.
********** 20 **********
--- page 21 ---
2. Compute the posterior probability for each class:
3. Assign the class with the highest posterior probability.
Example:
Document: “I love NLP”
• Compute P(spam ∣ X) and P(ham | X) using prior and likelihood
• Choose class with max probability
5. Advantages of Naive Bayes for Text Classification:
• Simple and fast to train.
• Works well with high-dimensional sparse data.
• Performs surprisingly well even with the independence
assumption.
Naive Bayes, combined with a count vectorizer, transforms text into
numerical features and computes class probabilities to classify new
documents efficiently. It is an application-oriented approach in basic NLP
pipelines.
Q6   Name all the gates in an LSTM cell and explain their functions. Discuss
CO-4; SO-1;   b. how these gates help in modelling contextual word representations, for   [10]
BL-4   example in Word Sense Disambiguation (WSD) tasks.
ANS:
LSTM Gates and Their Role in WSD
1. LSTM Overview:
A Long Short-Term Memory (LSTM) network is a type of Recurrent
Neural Network (RNN) designed to capture long-range dependencies in
sequences, overcoming the vanishing gradient problem in standard RNNs.   05
In NLP, LSTMs are widely used to model contextual word
representations, which are crucial for tasks like Word Sense
Disambiguation (WSD).
********** 21 **********
--- page 22 ---
02
03
3. Role of Gates in Modelling Contextual Word Representations
• The forget gate removes irrelevant prior context, helping the
model focus on the current word’s semantics.
• The input gate and candidate state incorporate new information,
allowing the model to adapt its understanding of the sentence
dynamically.
• The output gate controls which information flows forward,
preserving meaningful context for downstream tasks.
4. Application to Word Sense Disambiguation (WSD)
• WSD requires understanding a word’s sense based on surrounding
words.
• LSTM gates enable the network to capture dependencies over long
contexts, ensuring that the right sense of a polysemous word is
predicted.
• Example: The word “bank” in:
• “He sat by the river bank.” → LSTM captures surrounding
words like “river” to predict the geographical sense.
• “He went to the bank to deposit money.” → Context words
like “deposit” lead to the financial sense.
• LSTM-based models can also be enhanced using lexical resources
like WordNet, which provide semantic relations between senses
for improved disambiguation.
********** 22 **********
--- page 23 ---
Q7   Explain Low-Rank Adaptation (LoRA) and analyse how it efficiently
CO-5; SO-1;   a.   modifies transformer models compared to full fine-tuning.   [10]
BL-4
Low-Rank Adaptation (LoRA) and Efficient Transformer Fine-Tuning
1. Introduction to LoRA:
• Low-Rank Adaptation (LoRA) is a technique for parameter-efficient
fine-tuning of large pretrained transformer models.   02
•   Traditional fine-tuning updates all model weights, which is resource-
intensive for large models like BERT, GPT, or T5.
• LoRA instead injects trainable low-rank matrices into certain layers
(usually attention or feed-forward layers) while keeping the original
weights frozen.
2. How LoRA Works:   02
3. Efficiency Compared to Full Fine-Tuning:
Aspect   Full Fine-Tuning   LoRA
Parameters   All weights   Only low-rank matrices
Updated   (few %)
Training Cost   High   Low
Memory Usage   High   Low
04
Knowledge   Can overwrite pretrained   Preserves pretrained
Retention   knowledge   knowledge
Deployment   Large checkpoints   Small, easy to share
********** 23 **********
--- page 24 ---
02
4. Advantages of LoRA:
• Computationally efficient: Less GPU memory and faster training.
•   Parameter-efficient: Only a fraction of parameters are trained.
•   Maintains pretrained knowledge: Reduces catastrophic forgetting.
•   Flexible: Can be applied to different transformer architectures and
downstream tasks.
Q7   Explain how Thesauruses like WordNet are used in the retrofitting algorithm
CO-4; SO-1;   b.   to refine word embeddings. Describe the process and illustrate with an   [10]
BL-4   example using the words dog, hound, and cat.
ANS:
Retrofitting Word Embeddings Using Thesauruses like WordNet   02
1. Concept:
Retrofitting is a post-processing technique that improves pre-trained
embeddings (e.g., Word2Vec, GloVe) by incorporating semantic relations
from a thesaurus such as WordNet.
It adjusts word vectors so that related words (e.g., synonyms) become closer
in the embedding space.   02
2. Role of Thesauruses:
Thesauruses like WordNet provide structured lexical relations such as:
• Synonymy (dog ↔ hound)
• Hypernymy (dog → animal)
• Antonymy (hot ↔ cold)
These relations form a graph that guides retrofitting by linking
semantically related words.   03
3. Algorithmic Process:
1. Start with pre-trained embeddings for all words.
2. Build a graph where each word is a node and semantic relations (e.g.,
synonyms) form edges.
3. Update each word vector as the average of:
•   Its original embedding, and
• The embeddings of its related words.
4. Repeat until the vectors stabilize (converge).
Formula:
********** 24 **********
--- page 25 ---
03
4. Example (Simplified 2D Vectors): (Expected to give in detail)
Word Original (x, y) After Retrofitting (x, y)
dog   (0.8, 0.1)   (0.5, 0.15)
hound (0.2, 0.2)   (0.5, 0.15)
cat   (0.7, 0.9)   (0.7, 0.9)
•   Before: dog was closer to cat (similar contexts).
•   After: dog and hound become closer due to synonymy, improving
semantic accuracy.
After Retrofitting
dog and hound vectors move closer together
cat remains related but farther away
Semantic structure becomes clearer
Before:   After:
dog   dog —— hound
\   \
cat   cat
Embeddings reflect true lexical meaning, not just co-occurrence
Enhances performance in Word Sense Disambiguation (WSD), semantic
similarity, and analogy tasks.
Retrofitting with thesauruses like WordNet aligns corpus-based
embeddings with human-defined semantics, producing more accurate
and interpretable word representations.
********** 25 **********
````
