# Natural Language Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 03f12a163ddd

- Departments: Computer Engineering, Data Science, Information Technology
- Programmes: BTech CSE DS 7011, BTech IT 7001, Integrated Computer 7032, MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_07/Final-Exam/BTech_IT_7001/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2024-2025.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: mixed (19 pages), mean OCR confidence 36.4
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 02 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.1   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples.
BL-2;   Ans:
Natural Language   Natural Language
Aspect
Understanding (NLU)   Generation (NLG)
NLU is the ability of a NLG is the ability of a
machine to   machine to generate
comprehend and   human-like language (text
Definition
interpret human   or speech) from structured
language in a   data or internal
meaningful way.   representations.
To understand the
To produce coherent and
Purpose   meaning of the input
meaningful text as output.
text.
Structured data, machine-
Human-readable text or
Input   readable content, or
speech.
semantic representation.
Semantic
understanding, intents, Human-readable text,
Output   entities, sentiment, or   sentences, paragraphs, or
meaning   conversational responses.
representation.
********** 1 **********
--- page 2 ---
Named Entity
Template-based generation,
Recognition (NER),
Neural Networks (like GPT
Techniques Used Sentiment Analysis,
models), Rule-based text
Intent Detection,
generation.
Semantic Parsing.
Input: “Book a flight to
Example
New York tomorrow.”
Output: Intent =   Input: Structured data:
BookFlight,   {“City”: “New York”,
Destination = New “Weather”: “Sunny”,
York, Date =   “Temperature”:
Tomorrow.   “25°C”}
Output: “The
weather in New
York is sunny
today with a
temperature of
25°C.”
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
Ans:
Chunking-2M
Chinking 2M
POS Tagging role 1M
Sentence: “The black dog is running in the park.”
• Chunking: Groups words → [The black dog] (NP), [the park]
(NP).
• Chinking: Removes unwanted words → e.g., remove in
(preposition) from the chunk.
POS Tagging: Provides word categories (DT, JJ, NN, etc.), which are
used to apply chunking and chinking rules.
CO-4,   c.5   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
Ans:
(2+2+1) = 5 Marks
Hyponymy and Hypernymy
Hyponymy is a semantic relation in which the meaning of one word is
included in the meaning of another word.
Example: rose, tulip, and lily are hyponyms of flower.
The statement can be expressed as: “A rose is a kind of flower.”
Hypernymy is the opposite relation: it refers to the more general word
whose meaning includes that of more specific words.
********** 2 **********
--- page 3 ---
Example: flower is a hypernym of rose, tulip, and lily.
Similarly, animal is a hypernym of dog, cat, and elephant.
Application of Hypernymy in Word Sense Disambiguation (WSD)
Hypernymy relations are very useful in WSD because they allow a system
to connect ambiguous words to their broader, more general categories. By
checking the surrounding context and mapping it to the correct hypernym,
a system can choose the right sense of a word.
Example: Consider the polysemous word “bank.”
Sense 1: financial institution (hypernym = organization)
Sense 2: river bank (hypernym = geographical feature / landform)
If the sentence is:
“The boy was fishing on the bank.”
Words like fishing and river in the context point towards the hypernym
geographical feature.
Therefore, bank here means river bank.
“She deposited money in the bank.”
Context words like money and deposit map to the hypernym organization.
Therefore, bank here means financial institution.
In WSD, hypernymy helps map ambiguous words to their general category,
and then context determines which sense is correct.
CO-3;   d. 6   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3   Ans: Marks Distribution-3 Marks for Comparison and 2 Marks for
Example of each type
Pragmatics concentrates on speaker intention and context-dependent meaning,
whereas discourse analysis investigates how sentences and utterances are
connected to form coherent texts and conversations. Together, they provide a
comprehensive   understanding   of how language   functions   in   real
communication.
Pragmatics is the branch of linguistics that studies how meaning is shaped by
context of use. It goes beyond the literal semantic meaning of words and
focuses on how speakers use language to achieve communicative goals.
Example “Can you pass the salt?” — pragmatically, this is not a question about
ability but a request.
Discourse analysis studies how sentences and utterances are connected to
form larger units of meaning such as conversations, narratives, or written
texts.   It   is concerned with cohesion (linguistic ties like reference,
substitution, conjunctions) and coherence (logical flow of ideas in context).
Example :“I bought a book yesterday. The book was about artificial
intelligence.”
********** 3 **********
--- page 4 ---
→ The second sentence refers back to “a book” using “the book,” creating
textual cohesion.
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;
SO-1;   ii.   Discuss the significance of NER in three different NLP
BL-2,3   applications.
Ans:
Ans: [Marks 5+5]
i.
Feature   Morpheme   Lexeme
Meaning The smallest grammatical The basic unit of lexical
unit in a language that   meaning — represents a set
carries meaning.   of related word forms.
Function Deals with word structure Deals with word meaning
(morphology).   and usage in the lexicon.
Example   Morpheme   Lexeme
Unhappi   Has three morphemes:   The lexeme is HAPPY,
ness   “un-” (prefix), “happy”   which can appear as happy,
(root), “-ness” (suffix).   happier, happiest.
Running   Has two morphemes:   The lexeme is RUN, which
“run” + “-ing”.   includes run, runs, ran,
running.
ii.
1. Information Extraction (IE)
Automatically extracts structured information (names, dates,
locations, organizations) from unstructured text such as news
articles, reports, or legal documents.
2. Question Answering Systems (QA)
Helps identify entities in questions and documents (e.g., “Who is
the   CEO of Tesla?” → CEO = role, Tesla = organization).
3. Machine Translation
Ensures named entities like “Barack Obama” or “New Delhi”
are   translated correctly or kept unchanged.
4. Healthcare & Biomedical Text Mining
Extracts entities such as patient names, diseases, medications,
genes, or proteins from medical records and research papers.
5. Customer Feedback & Social Media Analysis
Identifies product names, brands, locations, or events in tweets,
reviews, and online discussions for business intelligence.
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
********** 4 **********
--- page 5 ---
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
Assume the <s> and </s> for each sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> artists paint murals in city </s>
<s> musicians play songs in city </s>
<s> painters paint murals on walls </s>
<s> signs are near city </s>
Test sentence-
<s> artists paint murals near city </s>
Distinct tokens are:
<s>, </s>, artists, paint, murals, in, city, musicians, play, songs,
painters, on, walls, signs, are, near
That gives V=16.
Counts:
• Unigram counts:
o C(artists)=1
o C(paint)=2
o C(murals)=2
o C(near)=1
o C(city)=3
o C(<s>)=4
• Bigram counts:
o C(<s>,artists)=1
o C(artists,paint)=1
o C(paint,murals)=2
o C(murals,near)=0
o C(near,city)=1
o C(city,</s>)=3
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(artists∣<s>)=[1+1]/[4+16]=2/20=1/10≈0.1
2. P(paint∣artists)=[1+1]/[1+16]=2/17≈0.117647
3. P(murals∣paint)=[2+1]/[2+16]=3/18=1/6≈0.166667
4. P(near∣murals)=[0+1]/[2+16]=1/18≈0.0555556
5. P(city∣near)=[1+1]/[1+16]=2/17≈0.117647
6. P(</s>∣city)=[3+1]/[3+16]=4/19≈0.210526
Exact fraction:
P+1=1/10*2/17*1/6*1/18*2/17*4/19=16/5930280=2.698E-6
Hence, the probability of the test sentence is =2.698E-6.
********** 5 **********
--- page 6 ---
Q3   a   i.   Explain the various types of ambiguities encountered in Natural [10]
CO- 3,   Language Processing (NLP). Illustrate each type with suitable
SO-, BL-   examples.
ii.   Compare top-down and bottom-up parsing and apply bottom-up
4
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-
“A cat chased the mouse”
Grammar   Lexicon
S → NP VP   Det → {A, the}
NP → Pronoun   Noun → {cat, mouse}
NP → Proper-Noun   Verb → {chased}
NP → Det Nominal
Nominal → Noun
Nominal → Nominal Noun
Nominal → Nominal PP
VP → Verb
VP → Verb NP
VP → VP PP
PP → Prep NP
Ans: Marks-5
1. Lexical Ambiguity:
Meaning:
Occurs when a word has multiple possible meanings.
Example:
He went to the bank.
• “bank” can mean a financial institution or the side of a river.
Explanation:
NLP systems must use context to decide which meaning of “bank”
applies in the sentence.
2. Syntactic Ambiguity (Structural Ambiguity)
Meaning:
Occurs when a sentence can be parsed in more than one way due to
different grammatical structures.
Example:
I saw the man with the telescope.
•   Interpretation 1: I used the telescope to see the man.
•   Interpretation 2: The man had the telescope.
Explanation:
The ambiguity arises because the prepositional phrase (“with the
telescope”) can modify either the verb saw or the noun man.
3. Semantic Ambiguity
Meaning:
Occurs when the meaning of the sentence itself is unclear, even if the
structure is fine.
Example:
Visiting relatives can be boring.
********** 6 **********
--- page 7 ---
•   Interpretation 1: The act of visiting relatives is boring.
•   Interpretation 2: The relatives who visit are boring.
Explanation:
The confusion comes from whether visiting is used as a gerund (verb)
or adjective (modifier).
4. Pragmatic Ambiguity
Meaning:
Arises when the intended meaning depends on context or speaker’s
intention rather than grammar or word meaning.
Example:
Can you pass the salt?
•   Literally, it’s a question about ability.
•   Pragmatically, it’s a request for action.
Explanation:
Understanding pragmatic meaning requires world knowledge and
context.
5. Referential Ambiguity
Meaning:
Occurs when a pronoun or reference word could refer to multiple
entities.
Example:
John told Tom that he was late.
• “he” could refer to John or Tom.
Explanation:
The ambiguity arises in anaphora (reference resolution).
ii.
Comparison (Any two relevant points-2M)
Aspect   Top-Down Parsing   Bottom-Up Parsing
Starts from the root (start   Starts from input tokens
Parsing   symbol) and expands   and reduces toward the
Direction   toward the input.   root.
Expands non-terminals
using grammar rules,   Combines tokens/phrases
Grammar Rule   even before seeing if   only if they appear in the
Application   input matches.   input.
Fails or loops infinitely
Handling Left   if grammar has left   Naturally handles left
Recursion   recursion.   recursion without issues.
May get stuck or need   Can face shift-reduce or
Ambiguity   backtracking when   reduce-reduce conflicts in
Handling   grammar is ambiguous.   ambiguous grammars.
Ease of   Conceptually simple and More complex (needs
Implementation   intuitive to implement.   parsing tables, stacks).
Bottom up parsing with steps-3
********** 7 **********
--- page 8 ---
Godors wp awry ti

‘ vos Hy )
=— : ver
a Nowr vub \ cbt
\ che ome Pet
; nan
_ Norin® wee
\ % *
Oe one ‘i ete atase
kb
zeus avid Mar Rs arte)
Ng NP
aearel worn
aie wee vib DE “
y 2
stop bak rik yin?” “nr 1°
NP
~~
4 J
My ye Nomint
7 ; / degee
ve
al var mone

“ unr Chock 1

Shp © form cunUR tt)

62 NY Ny

Coton we “nt IM Fina

“A Cok chuck ue we
= a

‘Se:

ok che TN Monee

FIC QF EH 1
--- page 9 ---
CO-3;   b   Consider the given paragraph given below:   [10]
SO- 1   The teacher wrote on the board. The students listened to the teacher.
BL-4:   The board was full of notes. The student asked a question. The
teacher answered from the book.
Target words: teacher, student, board, book
Context words: wrote, listened, notes, question
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.
Plot the target word vectors by considering only two dimensions: “wrote”
and “notes”.
Ans: [Marks 5+5]
Co-occurrence matrix:
target \ context   wrote   listened   notes
teacher   1   1   0
student   0   1   0
board   1   0   1
book   0   0   0
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2   Ans:[Marks-5+5]
It is an essential step in natural language processing (NLP) that involves
cleaning and transforming unstructured text data to prepare it for analysis.
Text data contains noise in various forms like emoticons, punctuations, text in
a different cases, HTML tags etc.
********** 9 **********
--- page 10 ---
Inadequate or low-quality data can lead to lower accuracy and effectiveness of
the model.
The pre-processing steps for a problem depend mainly on the domain and the
problem itself, hence, we don’t need to apply all steps to every problem and
also the order of applying these steps may also vary.
Various text preprocessing steps are widely used for dimensionality reduction.
Some of the commonly used preprocessing steps are:
o Removing punctuations like . , ! $( ) * % @, URLs, Stop
words
o Lower casing
o Normalization (some common ones)
▪   Tokenization
▪ Stemming
▪ Lemmatization
Stop word removal:
• Stop words are a set of commonly used words in a language like “a”,
“the”, “is”, “are” etc. in English.
• These words do not carry important meaning and are removed from
texts in many data science tasks.
• The intuition behind this approach is that, by removing low
information words from text, we can focus on the important words
instead.
• One of the advantages of removing stop words is that it can reduce the
size of the dataset, which in turn reduces the training time required for
building natural language processing models.
• Stop word removal is commonly applied in search systems, text
classification applications, topic modeling, topic extraction and others.
• Stop word lists can come from pre-established sets or you can create a
custom one for your domain. This creation may be tricky as few words
that may not be useful in some problem statement may be important in
others.
Lower casing:
•   Usually, this is the first step that is performed while pre-processing.
•   Is a text preprocessing step where all letters in the text are converted
to lowercase.
•   This step is implemented so that the algorithm does not treat the same
words differently in different situations.
o Ex: Book and book mean the same but when not converted to
the lower case those two are represented as two different
words in the vector space model (resulting in more
dimensions).
• However, it is important to remember that some words, like “US” and
“us”, can change meanings when reduced to the lower case. Also,
there can be cases where the capitalization is important and has to be
preserved. So we should avoid performing this step in such cases
Normalization:
• As raw text data is random, each word has a lot of variations in the form of
tenses, superlatives, and many more.
********** 10 **********
--- page 11 ---
• These variations increase the complexity of the data and are difficult for the
machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data into a
predefined standard, hence improving the efficiency of the model.
• Ex: Many forms of the base word collect - "collection", "collective", and
"collectively".
•   If we reduce the variations of a word in the raw text, there will be fewer
input variables for our machine-learning model to deal with, thus increasing
efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for structures
like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Few common ones used are:
• Removal of duplicate whitespaces and punctuation.
• Accent removal (if your data includes diacritical marks from ‘foreign’
languages).
•   Substitution of contractions (Ex: ‘I’m ’→‘I am’ and don’t to do not).
• Transform word numerals into numbers (Ex: ‘twenty three’→‘23’).
•   Substitution of values for their type (Ex: ‘$50’→‘MONEY’).
• Acronym normalization (Ex: ‘US ’→‘United States’/‘U.S.A’) and
abbreviation normalization (Ex: ‘btw’ → ‘by the way’).
• Normalize date formats, social security numbers or other data that have a
standard format.
•   Spell correction (one could say that a word can be misspelled infinite
ways, so spell corrections reduce the vocabulary variation by “correcting”)
•   Substitution of rare words for more common synonyms.
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
Noun   Verb   Noun
BL-4
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Ans:
********** 11 **********
--- page 12 ---
Q5   a   For the following two sentences:   [10]
• Sentence A: “The student read a science book in the library”
• Sentence B: “The teacher read a history book in the classroom”
********** 12 **********
--- page 13 ---
CO-2;   1. Construct the TF-IDF matrix for these sentences after removing
SO-1 ;   the stop words {The, a, in}.
BL-3;   2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
Ans:[Marks 5+5]
Term   Sentence   Sentence
A   B
student   0.693   0
read   0   0
science   0.693   0
book   0   0
library   0.693   0
teacher   0   0.693
history   0   0.693
classroo   0   0.693
m
Analysis:
For Sentence A, the unique theme is student, science, library.
For Sentence B, the unique theme is teacher, history, classroom.
So, it indicates that TF–IDF clearly shows that shared words don’t matter for
separation, while unique words carry more importance.
CO-4;   b   Consider the sentence: “The bat hit the ball hard on the cricket field.”   [10]
SO-1BL-   Two possible senses of “bat”:
4
• Sense 1: Bat (Sports equipment – cricket/baseball)
• Sense 2: Bat (Nocturnal flying mammal)
Sentence
Context Words   Sense (Class)
ID
ball, cricket, score,   Sports (Bat =
1
stadium   equipment)
Animal (Bat =
2   night, cave, wings, fly
mammal)
3   player, run, match, bat   Sports
4   nocturnal, vampire, insect Animal
5   team, field, bowl, bat   Sports
6   dark, flying, cave, night   Animal
a) Using the Naïve Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naïve Bayes
Classification.
Ans:
********** 13 **********
--- page 14 ---
P(Sports)=0.5
1 mk
P(Animal)=0.5
Unique words across both classes: (words: ball, cricket, score, stadium,
player, run, match, bat, team, field, bowl, night, cave, wings, fly,
nocturnal, vampire, insect, dark, flying) Total 20
1
mk
Calculations:
For Sports:
2 mks
• P(hit∣S)=(0+1)/32=1/32=0.03125
• P(ball∣S)=(1+1)/32=2/32=0.0625
• P(cricket∣S)=2/32=0.0625
• P(field∣S)=2/32=0.0625
• P(hard∣S)=1/32=0.03125
For Animal:
P(w∣A)=1/31≈0.03225806
Likelihood for sports:
2 mks
0.5 * 0.03125*0.0625*0.0625*0.0625*0.03125 =1.19209290×10-7
Likelihood for animal :
1.74647163×10-8
Classified sense: Sports equipment
1 mk
Laplace Smoothing:
3 mks
Handles problem of zero probabilities, improves robustness of
classifier.
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate
how it predicts the target word from its surrounding context
Ans:
********** 14 **********
--- page 15 ---
iii.   Marks Distribution-3 Marks for approach explanation and 2
Marks for advantage of each type
Co-reference resolution: task of finding all expressions in text that refer to
the same entity. (1.5 marks)
Example: Mary said Mary is tired. She went home. → "Mary" and "She" co-
refer.
Pronoun resolution: a subtask focusing only on resolving pronouns to their
antecedents. (1.5 marks)
Example: John met Peter when he was leaving. → "he" could refer to John or
Peter.
Difference: co-reference is broader (includes noun phrases, names, definite
descriptions), while pronoun resolution is narrower.
In Word2Vec, two main architectures are used to learn word
embeddings:
Continuous Bag of Words (CBOW) and
Skip-Gram.
Both are neural network-based models that learn to represent words as
dense vectors based on their context in a text corpus.
1. Continuous Bag of Words (CBOW) Model
Working Principle:
The CBOW model predicts the target word from its surrounding
context words.
It takes context words as input and tries to predict the central
(target) word.
The model averages (or sums) the vectors of the context words and
passes them through a neural network to predict the target word.
Example:-Sentence
“The cat sat on the mat”
If the window size = 2, and the target word is “sat”, then the context
words are:
["The", "cat", "on", "the"]
The CBOW model learns:
P(sat | The, cat, on, the)
Intuition:
It focuses on understanding the meaning of a word based on its
surrounding words.
2. Skip-Gram Model
Working Principle:
• The Skip-Gram model does the reverse of CBOW.
•   It predicts the context words given a target word.
• The target word is input, and the model learns to predict
surrounding context words.
Example:-Sentence:
“The cat sat on the mat”
If the target word is “sat” and window size = 2, then the context
words are:
["The", "cat", "on", "the"]
********** 15 **********
--- page 16 ---
The Skip-Gram model learns:
P(The | sat), P(cat | sat), P(on | sat), P(the | sat)
Intuition:
It focuses on how a single word relates to its neighboring words.
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Ans: Marks Distribution-5 Marks for approach explanation and 5 Marks
for resolution
i
Hobbs’ Algorithm is a syntactic algorithm for pronoun resolution in NLP.
It identifies possible antecedents for a pronoun by traversing a syntactic parse
tree in a systematic manner.
Example:
Sentence: “When Mary saw Alice, she waved.”
• Pronoun = she
• Step 1: Start at NP dominating “she.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs = “Mary,” “Alice.”
• Step 4: First candidate = Mary, chosen as antecedent.
Limitations :
Struggles with ambiguous cases (gender/number mismatch ignored).
Not efficient for long, complex sentences.
ii Sentence: “Ravi met Suresh at the station after he arrived from
Delhi.”
Pronoun: he
Steps of traversal:
1. Start at NP for “he.”
2. Move up to nearest S node.
3. Traverse left branches → encounter NPs: Ravi, Suresh.
4. Candidate 1 = Ravi, Candidate 2 = Suresh.
5. According to Hobbs’ order: Ravi is encountered first.
Hobbs’ algorithm chooses Ravi as antecedent of “he.”
But semantically, “Suresh” may also make sense depending on context
→ shows limitation of Hobbs.
Q7   a   Explain the working of text classification in Natural Language Processing [10]
(NLP) and discuss the key steps involved in building a text classification
********** 16 **********
--- page 17 ---
CO-4;   system in context of real-world applications such as spam detection or
SO-1 BL-   news categorization.
3:   Ans:
Text classification is the process of automatically assigning categories or
labels to text data based on its content.
Examples include:
Spam filtering – Classifying emails as “spam” or “not spam.”
News categorization – Grouping news articles into topics like sports,
politics, or entertainment.
Sentiment analysis – Identifying whether a review or comment is
positive, negative, or neutral.
Steps Involved in Text Classification
1. Data Collection
Gather a dataset containing text documents and their corresponding labels.
• Example: A set of emails labeled as “spam” or “ham” (not spam).
2. Data Preprocessing
Prepare the text for analysis by cleaning and normalizing it. Common steps
include:
• Lowercasing – Convert all text to lowercase.
• Removing noise – Punctuation, special characters, HTML tags, etc.
•   Tokenization – Splitting text into individual words or tokens.
•   Stop word removal – Removing common words like “the,” “is,”
“and.”
• Stemming/Lemmatization – Reducing words to their base or root form
(e.g., “running” → “run”).
3. Feature Extraction / Text Representation
Convert the cleaned text into a numerical format that a machine learning
model can understand. Common methods:
• Bag of Words (BoW) – Counts the occurrence of each word in the
document.
• TF-IDF (Term Frequency–Inverse Document Frequency) – Weighs
words based on their importance.
• Word Embeddings (e.g., Word2Vec, GloVe) – Captures semantic
meaning of words in vector form.
•   Transformer-based embeddings (e.g., BERT) – Context-aware
representations of text.
4. Model Training
Train a classification algorithm using the numerical features and their labels.
Examples of models:
•   Traditional ML: Naive Bayes, Logistic Regression, SVM.
• Deep Learning: RNNs, CNNs for text, Transformers (e.g., BERT).
5. Model Evaluation
Evaluate the trained model using metrics such as:
• Accuracy – Overall correctness.
•   Precision & Recall – Useful for imbalanced datasets (e.g., spam
detection).
•   F1-score – Balance between precision and recall.
6. Prediction / Deployment
********** 17 **********
--- page 18 ---
Use the trained model to classify new, unseen text data.
Example: A new email arrives → model predicts “spam” or “not spam” →
automatically sorted into the correct folder.
7. Monitoring and Updating
Over time, new words and patterns emerge. The model should be regularly
retrained with updated data to maintain accuracy.
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
Ans: [Marks 5+5]
i. Different corpus structures are applied to different NLP tasks
depending on the information they provide:
Flat Text Corpus (e.g., plain .txt files):
This type contains only raw text without labels. It can be applied to tasks
like word frequency analysis, calculating readability scores, or
comparing the styles of different writers. For example, one can apply it
to study the most common words in political speeches.
Annotated Corpus (e.g., POS-tagged or parsed text):
This type contains extra linguistic information such as part-of-speech
tags, named entities, or syntactic structures. It can be applied in
supervised learning tasks such as training a Part-of-Speech tagger,
Named Entity Recognition, or parsing models. For instance, a POS-
tagged corpus can be used to train a model that automatically identifies
nouns and verbs in new texts.
ii. Jaccard similarity takes into account only the set of unique words
for each text document. This makes it the likely candidate for
assessing the similarity of documents when repetition is not an issue.
Both Euclidean and cosine similarity metrics drop if an additional
word is added to the list.
Jaccard similarity is limited to assessing the lexical similarity of text,
i.e., how similar documents are on a word level.
The differentiating factor between Euclidean and Cosine measure is
that cosine similarity is not affected by the magnitude/length of the
feature vectors. It only considers the angle between them, making it
ideal for comparing vectors of different lengths. (Ex: If a word
‘senate’ occurs more frequently in doc 1 than it does in doc 2, we
could assume that doc 1 is more related to the topic of Politics.
However, it could also be the case that we are working with news
articles of different lengths and word ‘senate’ probably occurred more
in doc 1 simply because it was way longer)
Ex:
********** 18 **********
--- page 19 ---
Doc 1: “I love data science and machine learning”
Doc 2: “I love machine learning”
Step 1: Preprocess the documents - Remove stopwords like “I”, “and”,
etc., and lowercase everything.
Doc 1 → ['love', 'data', 'science', 'machine', 'learning’]
Doc 2 → ['love', 'machine', 'learning’]
Vocabulary :['love', 'data', 'science', 'machine', 'learning']
Jaccard
Intersection: ['love', 'machine', 'learning'] → 3 words
Union: ['love', 'data', 'science', 'machine', 'learning'] → 5 words
Jaccard=3/5=0.6
Cosine
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Dot product = 1∗1+1∗0+1∗0+1∗1+1∗1=31∗1+1∗0+1∗0+1∗1+1∗1=3
|A| = √(1²+1²+1²+1²+1²) = √5 ≈ 2.236
|B| = √(1²+0²+0²+1²+1²) = √3 ≈ 1.732
cos(θ)= 3/(2.236×1.7323) ≈ 3/3.8723 ≈0.775
Euclidean:
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Distance=Sqrt((1−1)2+(1−0)2+(1−0)2+(1−1)2+(1−1)2 )
Distance= ≈1.414
Measure   Value   Meaning
Jaccard   0.6   60% of the words overlap
Cosine   0.775   High similarity in word pattern
Euclidean   1.414   Some difference in word presence
In short, flat corpora are applied to simpler, surface-level analysis, while
annotated corpora are applied to more advanced supervised NLP tasks.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper e7ba1d026b1d

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Natural Language Processing/ANS_Natural Language Processing(703DB0C057)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. Assume Suitable data if necessary
8. Use of calculator (both normal as well as scientific) is allowed
9. Use of python/ excel is allowed, without access to the internet
Q1. Answer briefly.   (20 marks)
a. What is NLP? List and explain applications of NLP.   (5 marks)
Answer: Natural Language Processing (NLP) is a field of Artificial Intelligence that focuses on enabling
computers to understand, interpret, and generate human language in a meaningful way.
It combines concepts from linguistics, computer science, and machine learning to process and analyze
large amounts of natural language data such as text and speech.
Applications of NLP:
Machine Translation:
Converting text or speech from one language to another automatically, for example, Google Translate.
Sentiment Analysis:
Identifying emotions or opinions in text, used in social media monitoring, customer feedback, and
marketing analysis.
Chatbots and Virtual Assistants:
Systems like Siri, Alexa, or customer service bots use NLP to understand and respond to user queries
naturally.
Text Summarization:
Automatically generating a concise summary of a large document while preserving key information.
Information Retrieval and Search Engines:
********** 1 **********
--- page 2 ---
NLP helps search engines understand user queries and retrieve the most relevant results.
b. Explain the Naive Bayes classifier for binary text classification in NLP. List its applications.
(5 marks)
Answer: The Naive Bayes classifier is a probabilistic model used in NLP to classify text into two
categories, such as spam or non-spam. It calculates the probability of a document belonging to each class
using Bayes’ Theorem and assigns it to the class with the highest probability.
Applications:
Spam detection – Identifying spam emails.
Sentiment analysis – Detecting positive or negative opinions in text.
Text categorization – Classifying news articles or documents into topics
c. Explain how Convolutional Neural Networks (CNN) are used in Natural Language Processing. Mention
their advantages and applications.   (5 marks)
Answer: Convolutional Neural Networks (CNNs), originally developed for image processing, are also
used in NLP to capture local patterns in text, such as key phrases or n-grams. In NLP, the text is usually
represented as a word embedding matrix, and convolutional filters slide over sequences of words to detect
important features.
CNNs are particularly useful because they can automatically extract features without manual engineering
and are computationally efficient. They are good at capturing local dependencies in text but do not model
long-term dependencies as effectively as RNNs.
Applications in NLP:
Text classification – Sentiment analysis, topic categorization.
Sentence modeling – Detecting important phrases in questions or commands.
Named Entity Recognition – Extracting entities like names or locations in text.
Question Answering – Representing sentences to find relevant answers.
d. Explain Transfer Learning in Natural Language Processing. Mention its advantages and applications
with examples.   (5 marks)
Answer: Transfer Learning in NLP is a technique where a pretrained language model is used as a starting
point and then adapted to a specific NLP task. Instead of training a model from scratch, the knowledge
learned from a large dataset is transferred to tasks like text classification, sentiment analysis, or question
answering.
Advantages:
Reduces the need for large labeled datasets.
********** 2 **********
--- page 3 ---
Speeds up training and improves model performance.
Allows leveraging knowledge from general language patterns for specific tasks.
Applications:
Text classification – Using BERT for classifying news articles or reviews.
Sentiment analysis – Fine tuning GPT or RoBERTa to detect positive or negative opinions.
Question answering and chatbots – Adapting pretrained models to understand and respond to user queries.
Q2. Answer the followings:   (20 marks)
a. Explain Stemming and Lemmatization in Natural Language Processing. Compare both techniques
and discuss their advantages, limitations, and applications with examples.   (10 marks)
Answer: In Natural Language Processing (NLP), text data often contains multiple forms of the same word.
For example, run, runs, running, ran represent the same concept. To process text efficiently and reduce
vocabulary size, Stemming and Lemmatization are widely used preprocessing techniques. They help NLP
models generalize better and improve performance in tasks like text classification, search, and information
retrieval.
Explain Stemming and Lemmatization in Natural Language Processing. Compare both techniques and
discuss their advantages, limitations, and applications with examples.
Answer: In Natural Language Processing (NLP), text data often contains multiple forms of the same word.
For example, run, runs, running, ran represent the same concept. To process text efficiently and reduce
vocabulary size, Stemming and Lemmatization are widely used preprocessing techniques. They help NLP
models generalize better and improve performance in tasks like text classification, search, and information
retrieval.
1. Stemming
Definition: Stemming is the process of reducing words to their root form or stem using simple rules.
Method: Typically, algorithms like the Porter Stemmer or Snowball Stemmer are used.
Example:
running, runs, runner → run
better → bett (may not be a real word)
Advantages:
Fast and easy to implement.
********** 3 **********
--- page 4 ---
Reduces vocabulary size for large text datasets.
Limitations:
Can produce non-dictionary words.
May reduce accuracy for tasks requiring precise word meaning.
2. Lemmatization
Definition: Lemmatization reduces a word to its dictionary or canonical form (lemma) using linguistic
knowledge such as part-of-speech tags.
Method: Requires morphological analysis and POS tagging.
Example:
running, ran → run
better → good
Advantages:
Produces meaningful and valid words.
More accurate for NLP applications needing precise semantics.
Limitations:
Computationally more expensive than stemming.
Requires external linguistic resources like WordNet.
b. Suppose you are given a dataset of customer reviews labeled as positive or negative. Explain how
you would build a text classification system using NLP. Discuss the steps involved, the role of
feature extraction, model selection, and evaluation.   (10 marks)
Answer: Introduction:
Text classification is an NLP task where text documents are automatically assigned to one or more
predefined categories. In this example, the categories are positive and negative reviews, making it a binary
classification problem.
1. Data Preprocessing:
Cleaning text: Remove punctuation, special characters, and HTML tags.
Tokenization: Split sentences into words or tokens.
********** 4 **********
--- page 5 ---
Lowercasing: Standardize all words.
Stop word removal: Remove common words like "the", "is" which do not contribute to meaning.
Stemming/Lemmatization: Reduce words to root or lemma to handle variations.
2. Feature Extraction:
Convert text into numerical representation so that models can process it.
Bag of Words (BoW): Counts occurrence of each word.
TF-IDF: Measures importance of words relative to the dataset.
Word Embeddings: Capture semantic meaning (e.g., Word2Vec, GloVe, or contextual embeddings like
BERT).
3. Model Selection:
Traditional ML models: Naive Bayes, Logistic Regression, SVM – suitable for small datasets.
Deep Learning models: CNNs, LSTMs, or Transformers – better for large datasets and capturing context.
Transfer learning: Fine-tuning pretrained models like BERT for better accuracy with less labeled data.
4. Model Training and Evaluation:
Split dataset into training, validation, and test sets.
Train the model on the training set and tune hyperparameters on the validation set.
Evaluate performance using metrics like accuracy, precision, recall, F1-score, and confusion matrix.
Q3. Answer the followings:
a. Explain the concept of TF-IDF in Natural Language Processing, including its purpose and
advantages. Then, given the following three documents, compute the TF, IDF, and TF-IDF values
for the term “data”:
Doc1: "big data is transforming industries"
Doc2: "data science and machine learning are important"
Doc3: "cloud computing enables scalable data storage"
Discuss the significance of the TF-IDF value obtained for the term in these documents.   (10 marks)
Answer: TF-IDF (Term Frequency – Inverse Document Frequency) is a statistical measure used to
evaluate the importance of a word in a document relative to a corpus. Term Frequency (TF): Measures
how frequently a term appears in a document. Inverse Document Frequency (IDF): Measures how rare a
term is across all documents. TF-IDF: Combines both measures to give higher weight to words that are
frequent in a document but rare across the corpus. Purpose:
********** 5 **********
--- page 6 ---
Identifies important and distinctive words in a document.
Reduces the impact of common words like “the”, “is”.
Advantages:
Simple and effective for text representation.
Widely used in text classification, information retrieval, search engines, and recommendation systems.
The TF-IDF value for the term “data” is zero in all documents because it appears in all documents, making
it not distinctive in this corpus.
TF-IDF gives high weight to terms that are frequent in a document but rare across documents, helping
identify keywords that differentiate documents.
In this example, other terms like “transforming”, “cloud”, “machine” would have non-zero TF-IDF and
be more important for distinguishing documents.
b. Explain the architecture of Convolutional Neural Networks (CNN) for text data in Natural
Language Processing. Describe each layer, its function, and how text is processed through the
network.   (10 marks)
Answer: 1. Introduction
Convolutional Neural Networks (CNNs) are widely used in NLP to capture local patterns in text, such as
key phrases or n-grams. Unlike images, text is represented as a sequence of word embeddings, which
forms the input to the CNN.
2. Architecture Layers
Input Layer:
Converts text into numerical vectors using word embeddings such as Word2Vec, GloVe, or contextual
embeddings like BERT.
Each word is represented as a dense vector; the sentence or document becomes a matrix of word vectors.
Convolutional Layer:
Applies filters (kernels) of different sizes over sequences of words to detect local features such as n-grams.
Each filter slides over the embedding matrix to produce a feature map.
Activation Layer:
********** 6 **********
--- page 7 ---
Introduces non-linearity using functions like ReLU to capture complex patterns in the text.
Pooling Layer:
Often uses max pooling to extract the most important features from each feature map.
Explain the architecture of Convolutional Neural Networks (CNN) for text data in Natural Language
Processing. Describe each layer, its function, and how text is processed through the network.
Answer: 1. Introduction
Convolutional Neural Networks (CNNs) are widely used in NLP to capture local patterns in text, such as
key phrases or n-grams. Unlike images, text is represented as a sequence of word embeddings, which
forms the input to the CNN.
2. Architecture Layers
Input Layer:
Converts text into numerical vectors using word embeddings such as Word2Vec, GloVe, or contextual
embeddings like BERT.
Each word is represented as a dense vector; the sentence or document becomes a matrix of word vectors.
Convolutional Layer:
Applies filters (kernels) of different sizes over sequences of words to detect local features such as n-grams.
Each filter slides over the embedding matrix to produce a feature map.
Activation Layer:
Introduces non-linearity using functions like ReLU to capture complex patterns in the text.
Pooling Layer:
Often uses max pooling to extract the most important features from each feature map.
Reduces dimensionality and highlights the most salient features.
Fully Connected Layer:
Combines features extracted by convolution and pooling layers.
Prepares the data for the final classification task.
Output Layer:
********** 7 **********
--- page 8 ---
Generates the final prediction using activation functions like softmax for multi-class or sigmoid for binary
classification.
3. Flow of Text Through CNN
Text → Tokenization → Word embeddings → Input matrix.
Convolution filters slide over embeddings → Feature maps.
Activation function applied → Non-linear features.
Pooling layer → Reduced feature maps.
Fully connected layer → Integrated features.
Output layer → Predicted class.
Q4. Answer the followings:
a. Explain the concept of Transfer Learning in Natural Language Processing. Describe how BERT
can be fine-tuned for text classification tasks. Explain the architecture, the steps involved in fine-
tuning, and its advantages for classification tasks.   (10 marks)
Answer: Transfer learning in NLP is the technique of leveraging a pretrained language model trained on
a large corpus and adapting it to a specific downstream NLP task with less labeled data.
BERT Architecture for Classification:
Input Layer: Tokenized text with [CLS] and [SEP] tokens.
Embedding Layer: Combines token, segment, and position embeddings.
Transformer Encoder Layers: Capture bidirectional contextual representations of words.
[CLS] Token Output: Embedding represents the entire sentence.
Classification Layer: Fully connected layer on top of [CLS] with softmax/sigmoid for class probabilities.
Steps to Fine-Tune:
Preprocess text (tokenization, attention masks).
Load pretrained BERT and attach a classification head.
Train on task-specific dataset with a small learning rate.
Evaluate with metrics like accuracy, precision, recall, F1-score.
Predict new instances using the fine-tuned model.
********** 8 **********
--- page 9 ---
Advantages:
Captures contextual meaning of words.
Achieves state-of-the-art performance with small datasets.
Can be adapted for binary or multi-class classification.
Applications:
Sentiment analysis of reviews.
Spam detection.
Topic classification of news or documents.
b. Explain Sentiment Analysis in Natural Language Processing. Discuss its objectives, methods,
workflow, challenges, and applications with examples.   (10 marks)
Answer: 1. Introduction
Sentiment Analysis is the task of identifying and extracting opinions, emotions, or attitudes expressed in
text. It determines whether the sentiment in a piece of text (e.g., review, tweet, comment) is positive,
negative, or neutral.
Objective: Understand public opinion.
Monitor customer feedback.
Support decision-making in business, politics, and social media.
2. Methods of Sentiment Analysis
Lexicon-Based Approach:
Uses a predefined dictionary of words with sentiment scores.
Example: “good” → positive, “bad” → negative.
Pros: Simple, interpretable.
Cons: Cannot handle context, sarcasm, or new words.
Machine Learning-Based Approach:
Treats sentiment classification as a text classification problem.
********** 9 **********
--- page 10 ---
Common algorithms: Naive Bayes, SVM, Logistic Regression.
Requires labeled datasets for training.
Deep Learning-Based Approach:
Uses models like CNN, LSTM, or Transformers (e.g., BERT) to capture context and semantic meaning.
Can handle complex sentences, negations, and context better.
3. Workflow / Steps
Data Collection: Reviews, tweets, or social media posts.
Preprocessing: Tokenization, stop word removal, stemming/lemmatization, lowercasing.
Feature Extraction: Bag of Words, TF-IDF, or Word Embeddings (Word2Vec, GloVe, BERT).
Model Training: Train ML or DL models for classification.
Q5. Answer the followings:
a. Given the sentence below, perform Part-of-Speech (POS) tagging for each word. Explain the POS
tagging process. Sentence: "Researchers develop innovative algorithms to analyze large datasets
efficiently."   (10 marks)
Answer: Part-of-Speech (POS) Tagging is a fundamental task in Natural Language Processing (NLP) that
involves assigning a grammatical category or part of speech—such as noun, verb, adjective, or adverb—
to each word in a sentence. The objective of POS tagging is to determine the syntactic role of each word
based on both its meaning and context within a sentence. For instance, the word “book” can act as a noun
(“I read a book”) or a verb (“Please book a ticket”), and POS tagging helps resolve such ambiguities using
linguistic rules or statistical models.
The POS tagging process typically consists of three stages. First, tokenization is performed to split the
sentence into individual words or tokens. Next, a lexicon lookup or pre-trained model identifies possible
tags for each token. Finally, contextual disambiguation occurs — this step uses grammar rules or
probabilistic models (like Hidden Markov Models or Neural Taggers) to select the most appropriate tag
based on surrounding words. Modern NLP systems often employ machine learning approaches, such as
the Conditional Random Field (CRF) or deep learning models, to improve tagging accuracy.
Now, applying POS tagging to the given sentence:
“Researchers develop innovative algorithms to analyze large datasets efficiently.”
| Word   | POS Tag   | Description   |
| ----------- | -------------- | ----------------------------------------- |
| Researchers | Noun (NNS)   | Plural noun; subject of the sentence   |
| develop   | Verb (VBP)   | Present tense verb; denotes action   |
********** 10 **********
--- page 11 ---
| innovative   | Adjective (JJ) | Describes the noun “algorithms”   |
| algorithms   | Noun (NNS)   | Plural noun; object of the verb   |
| to   | Particle (TO)   | Used with infinitive verb form   |
| analyze   | Verb (VB)   | Infinitive verb; complements “to”   |
| large   | Adjective (JJ) | Describes the noun “datasets”   |
| datasets   | Noun (NNS)   | Plural noun; object of the verb “analyze” |
| efficiently | Adverb (RB)   | Modifies the verb “analyze”   |
Thus, the POS tagging process helps in identifying the syntactic structure of the sentence, which is
essential for higher-level NLP tasks such as parsing, sentiment analysis, machine translation, and
information extraction. By correctly tagging each word, we enable algorithms to better understand the
grammatical and contextual meaning of text.
b. Explain the concepts of Tokenization and Word Embedding in Natural Language Processing.
Discuss their purposes and significance in NLP applications. Also, illustrate with examples how a
sentence is tokenized and converted into embeddings.   (10 marks)
Answer: 1. Tokenization and Word Embedding are foundational steps in NLP for converting unstructured
text into a format suitable for machine learning and deep learning models.
Tokenization: Process of splitting text into smaller units called tokens, such as words, subwords, or
characters.
Word Embedding: Representation of tokens as dense numerical vectors that capture semantic meaning
and relationships between words.
2. Tokenization
Purpose:
Converts raw text into analyzable units.
Helps models understand the structure and meaning of text.
Applications: Preprocessing for text classification, sentiment analysis, and machine translation.
Input preparation for models like BERT, GPT, or RNNs.
3. Word Embedding
Purpose:
Converts tokens into numerical vectors for computational models.
Captures semantic similarity between words.
Example:
********** 11 **********
--- page 12 ---
Sentence: “NLP is fascinating”
Tokenization → ["NLP", "is", "fascinating"]
Embedding →
"NLP" → [0.12, -0.34, 0.56, ...]
"is" → [0.01, 0.05, -0.02, ...]
"fascinating" → [0.33, -0.11, 0.47, ...]
Significance:
Dense embeddings capture meaning better than sparse vectors like BoW.
Enable downstream tasks like sentiment analysis, text classification, machine translation, and question
answering.
Q6. Answer the followings:
a. Explain how Hidden Markov Models (HMM) are used in voice recognition systems. Discuss the
architecture and its key components.   (10 marks)
Answer: 1. Introduction
Hidden Markov Models (HMMs) are widely used in voice recognition systems to model temporal
sequences of speech sounds. In HMMs, the hidden states represent phonemes or words, which are not
directly observable, while the observations are audio features extracted from the speech signal.
2. Key Components of HMM in Voice Recognition
Hidden States:
Represent phonemes, words, or sub-word units.
Example: The word “cat” can have hidden states /k/, /æ/, /t/.
Observations:
Audio features derived from the speech signal, such as MFCCs (Mel-Frequency Cepstral Coefficients).
Transition Probabilities (A):
Probability of moving from one hidden state to another.
Example: Probability of /k/ being followed by /æ/.
********** 12 **********
--- page 13 ---
Emission Probabilities (B):
Probability of observing a specific feature vector given a hidden state.
Example: Likelihood that a feature vector corresponds to /æ/.
Initial State Probabilities (π):
Probability distribution of starting in a particular hidden state.
b. Describe how clustering can be applied to group similar text documents?   (10 marks)
Answer: 1. Introduction
Clustering is an unsupervised learning technique used to group similar objects together. In NLP, clustering
is used to organize text documents based on their content similarity, without using any predefined labels.
It is useful for tasks like topic discovery, document organization, and information retrieval.
2. Steps to Apply Clustering on Text Documents
Text Preprocessing:
Clean the text by removing punctuation, numbers, and stop words.
Tokenize the text into words.
Apply stemming or lemmatization to reduce words to their base forms.
Feature Extraction / Representation:
Convert text documents into numerical vectors that capture their meaning.
Common methods:
Bag-of-Words (BoW) or TF-IDF for simple frequency-based features.
Word embeddings (Word2Vec, GloVe, or BERT embeddings) for semantic similarity.
Choosing a Clustering Algorithm:
K-Means: Groups documents into K clusters based on vector similarity.
Hierarchical Clustering: Builds a tree-like structure (dendrogram) of document clusters.
DBSCAN: Groups dense clusters and identifies outliers.
Applying the Algorithm:
********** 13 **********
--- page 14 ---
Use the chosen algorithm to assign each document to a cluster based on similarity.
Evaluation & Visualization:
Evaluate clusters using metrics like silhouette score or Davies-Bouldin index.
Optional: Reduce dimensions using PCA or t-SNE to visualize clusters.
Q7. Answer the followings:
a. Define the Continuous Bag of Words (CBOW) model in Word2Vec. Explain its working principle,
the role of context words, advantages, limitations, and applications in Natural Language
Processing.   (10 marks)
Answer: 1. Definition
The Continuous Bag of Words (CBOW) model is a predictive word embedding technique in the
Word2Vec framework. It is designed to learn dense vector representations of words by predicting a target
word from its surrounding context words in a sentence. These embeddings capture both semantic and
syntactic relationships between words.
2. Working Principle
Input: Context words surrounding a target word within a specified window.
Output: Predicted target word.
Mechanism:
Each context word is converted into a numerical vector (one-hot or embedding).
The vectors are aggregated (typically averaged) to form a single context vector.
The context vector is passed through a neural network, which outputs a probability distribution over the
vocabulary.
The word with the highest probability is selected as the predicted target word.
3. Example
Sentence: “I would like to check my account balance today.”
Target word: “check”
Context window size: 2
Context words: Words before and after the target within the window: ["I", "would", "to", "my"]
Process:
Convert context words to embeddings.
********** 14 **********
--- page 15 ---
Aggregate embeddings to form a context vector.
Predict the target word “check” from the aggregated context vector.
This illustrates how CBOW uses surrounding words to infer the central word.
4. Advantages
Efficient and faster to train compared to Skip-gram on large datasets.
Captures semantic similarity between frequent words.
Produces dense embeddings suitable for downstream NLP tasks.
5. Limitations
Performs poorly on rare words due to lack of sufficient context.
Bag-of-words assumption ignores the order of context words.
Cannot capture long-range dependencies effectively.
6. Applications in NLP
Text Classification: Sentiment analysis, spam detection.
Named Entity Recognition (NER): Identifying entities such as names and locations.
Machine Translation: Embeddings improve cross-lingual mapping.
Information Retrieval: Finding semantically similar documents or queries.
Chatbots and Virtual Assistants: Understand context and generate meaningful responses.
b. Explain the concept of n-grams in Natural Language Processing. Distinguish between unigram,
bigram, trigram, and higher-order n-grams. Illustrate with an example how a short sentence can be
represented using unigram, bigram, and trigram models.   (10 marks)
Answer: In Natural Language Processing (NLP), an n-gram is a contiguous sequence of n items, usually
words or characters, extracted from text. N-grams are widely used in applications such as language
modeling, text prediction, and information retrieval, as they capture local context and word co-occurrence
patterns. A unigram (1-gram) represents a single word and treats each word independently, while a bigram
(2-gram) is a sequence of two consecutive words that captures pairwise relationships between words. A
trigram (3-gram) consists of three consecutive words and captures slightly longer contextual information.
Higher-order n-grams (n>3) capture more extended context but may result in data sparsity and increased
computational requirements.
********** 15 **********
--- page 16 ---
The working principle of n-grams involves first tokenizing the text into words or characters and then
creating sequences of length n by sliding a window over the tokens. The frequency of each n-gram can be
counted to form a probabilistic language model or used as features in machine learning tasks. For example,
given the sentence “I love natural language processing”, the unigrams are ["I", "love", "natural",
"language", "processing"], the bigrams are ["I love", "love natural", "natural language", "language
processing"], and the trigrams are ["I love natural", "love natural language", "natural language
processing"]. This illustrates how n-grams capture progressively larger contexts in the sentence.
N-grams have several advantages, including the ability to capture local word dependencies effectively,
simplicity of implementation, and usefulness in applications such as text classification, speech recognition,
and predictive typing. However, they also have limitations: large n values lead to sparsity due to many
rare sequences, increased memory and computation costs, and an inability to capture long-range
dependencies or semantic similarities between words, such as synonyms. Despite these limitations, n-
grams are widely used in NLP tasks such as language modeling (predicting the next word in a sequence),
text classification (using n-gram features as input for models), spell correction and autocomplete, and
information retrieval (matching query phrases using bigrams or trigrams).
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper cc6119f9af9d

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Natural Language Processing/ANS_Natural Language Processing(703DB0C057)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. Assume Suitable data if necessary
8. Use of calculator (both normal as well as scientific) is allowed
9. Use of python/ excel is allowed, without access to the internet
Q1. Answer briefly.   (20 marks)
a.   Explain how Logistic Regression works for text classification. Describe the sigmoid function and
its role in converting continuous values to probabilities.   (5 marks)
Answer: Logistic Regression is a supervised learning algorithm commonly used for text classification
tasks such as spam detection or sentiment analysis. In this approach, text data is first converted into
numerical features using techniques like bag-of-words or TF-IDF, where each document is represented as
a vector of word frequencies or importance scores. Logistic Regression then computes a weighted sum of
these features, where each word contributes to the final score based on its learned weight. This linear
combination produces a continuous value that represents how strongly the input text belongs to a
particular class.
The sigmoid function is used to transform this continuous output into a probability value between 0 and
1. It is defined as a mathematical function that takes any real number as input and maps it into a bounded
range from 0 to 1. When the output of the linear model is passed through the sigmoid function, it produces
a probability that the input belongs to the positive class. If this probability is greater than a chosen
threshold, typically 0.5, the text is classified into that class; otherwise, it is assigned to the other class.
The role of the sigmoid function is crucial because it enables Logistic Regression to model classification
problems by converting raw scores into interpretable probabilities. This allows the model not only to make
predictions but also to express the confidence of those predictions, making it especially useful in text
classification tasks where uncertainty matters.
********** 1 **********
--- page 2 ---
b.   Explain the process of tokenization in Natural Language Processing. Discuss at least three
challenges faced when tokenizing text from different languages or domains.   (5 marks)
Answer: Tokenization is the process of breaking down a piece of text into smaller units called tokens,
which can be words, subwords, or characters. It is one of the first steps in Natural Language Processing,
as raw text cannot be directly processed by machine learning models. For example, a sentence like “I love
NLP” can be tokenized into individual words such as “I”, “love”, and “NLP”. Depending on the method
used, tokenization can be word-level, subword-level (like byte pair encoding), or character-level. The
goal is to convert text into a structured form that can be further analyzed or used as input for models.
One major challenge in tokenization is handling languages that do not use clear word boundaries, such as
Chinese or Japanese. In such languages, words are not separated by spaces, making it difficult to
determine where one word ends and another begins. Specialized algorithms are required to correctly
segment the text.
Another challenge arises from ambiguity and variations in language, such as contractions, punctuation,
and compound words. For example, words like “don’t” can be split into “do” and “not” or treated as a
single token depending on the context. Similarly, hyphenated words or domain-specific terms may not be
consistently tokenized.
A third challenge is dealing with domain-specific vocabulary and out-of-vocabulary words. In technical,
medical, or legal texts, many specialized terms or abbreviations may not be recognized by standard
tokenizers. This can lead to incorrect splitting or loss of meaning, which affects downstream tasks like
classification or sentiment analysis.
Overall, while tokenization is a fundamental step in NLP, it requires careful handling of linguistic and
contextual differences across languages and domains.
c.   What is Bidirectional Encoder Representations from Transformers (BERT)? Explain the concept
of bidirectional context in BERT and why it is important for understanding language compared to
unidirectional models.   (5 marks)
Answer: BERT, which stands for Bidirectional Encoder Representations from Transformers, is a deep
learning model developed for Natural Language Processing tasks such as text classification, question
answering, and language understanding. It is based on the transformer architecture and is designed to
learn rich representations of text by analyzing the context of words in a sentence. Unlike traditional
models, BERT is pre-trained on large corpora using tasks like masked language modeling and next
sentence prediction, and can then be fine-tuned for specific applications.
The key feature of BERT is its bidirectional context. This means that BERT reads and understands a word
by considering both the words that come before it and the words that come after it in a sentence. For
********** 2 **********
--- page 3 ---
example, in the sentence “He went to the bank to deposit money,” the meaning of the word “bank” depends
on the surrounding words. BERT uses information from both sides simultaneously to correctly interpret
such words.
This is different from unidirectional models, which process text either from left to right or right to left.
Such models can only use past context (or future context, but not both at the same time), which limits
their understanding of language. As a result, they may misinterpret words whose meaning depends on
future context.
The importance of bidirectional context lies in its ability to capture deeper and more accurate linguistic
relationships. By considering the full context of a word, BERT can better understand nuances, resolve
ambiguities, and improve performance on a wide range of NLP tasks. This makes it significantly more
powerful than earlier unidirectional models for language understanding.
d.   Explain how Convolutional Neural Networks process text data differently from Recurrent Neural
Networks. What makes Convolutional Neural Networks particularly effective for sentence-level NLP
tasks?   (5 marks)
Answer: Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) process text
data in fundamentally different ways. In CNNs, text is first converted into word embeddings, forming a
matrix where each row represents a word vector. Convolutional filters are then applied over this matrix
to capture local patterns such as phrases or n-grams. These filters slide across the text and detect important
features regardless of their position. After convolution, pooling operations (such as max pooling) are used
to extract the most significant features, resulting in a fixed-size representation of the sentence.
In contrast, RNNs process text sequentially, one word at a time, maintaining a hidden state that captures
information from previous words. This allows RNNs to model temporal dependencies and word order
explicitly. However, they can suffer from issues like vanishing gradients and are slower to train due to
their sequential nature.
CNNs are particularly effective for sentence-level NLP tasks because they efficiently capture local
patterns such as key phrases or combinations of words that are strong indicators of meaning, such as
sentiment-bearing phrases. Their ability to perform parallel computation makes them faster and more
scalable than RNNs. Additionally, pooling layers help in selecting the most important features, making
CNNs robust to variations in sentence structure. This combination of efficiency, ability to detect salient
features, and position invariance makes CNNs well-suited for tasks like text classification and sentiment
analysis.
Q2. Answer the followings:   (20 marks)
********** 3 **********
--- page 4 ---
a. Explain all the major accuracy metrics used to evaluate text classification models including
precision, recall, F1-score, accuracy, and confusion matrix. Define each metric mathematically
and explain when each is most appropriate. Why is accuracy alone sometimes misleading,
especially for imbalanced datasets? Illustrate with an example.   (10 marks)
Answer: In text classification, different evaluation metrics are used to understand how well a
model performs, since relying on a single measure may not give the complete picture.
A confusion matrix is the foundation of most evaluation metrics. It shows how many predictions
were correct and incorrect by comparing actual labels with predicted labels. It breaks results into
four categories: correctly predicted positives, correctly predicted negatives, incorrectly predicted
positives, and incorrectly predicted negatives. This helps in understanding the types of errors the
model is making.
Accuracy measures the overall proportion of correct predictions out of all predictions made. It is
simple and useful when the dataset is balanced and all types of errors are equally important.
However, it does not distinguish between different kinds of mistakes.
Precision focuses on the quality of positive predictions. It tells us, out of all instances predicted as
positive, how many were actually correct. Precision is most appropriate in situations where false
alarms are costly, such as spam filtering or fraud detection.
Recall measures how well the model identifies actual positive cases. It tells us, out of all real
positive instances, how many were correctly captured by the model. Recall is important in cases
where missing a positive instance is critical, such as medical diagnosis or risk detection.
The F1-score combines both precision and recall into a single measure by taking their balance. It
is useful when there is a need to consider both false positives and false negatives, especially in
cases where the dataset is imbalanced.
Accuracy can be misleading in imbalanced datasets because a model may achieve high accuracy
simply by predicting the majority class most of the time. For example, if 95% of emails are non-
spam and only 5% are spam, a model that predicts every email as non-spam will achieve 95%
accuracy. However, it completely fails to identify any spam emails, making it ineffective. In such
cases, precision, recall, and F1-score provide a more meaningful evaluation of model performance.
b. Explain the complete text processing pipeline including tokenization, stemming, lemmatization,
and Part-of-Speech tagging. For the sentence "The researchers are researching better ways to
research user behaviors," demonstrate the output at each processing stage. Why is the order of
these operations important?   (10 marks)
Answer: The text processing pipeline in Natural Language Processing involves a sequence of steps
that transform raw text into a structured form suitable for analysis. Key steps include tokenization,
stemming, lemmatization, and Part-of-Speech (POS) tagging.
********** 4 **********
--- page 5 ---
Tokenization is the first step, where the sentence is broken into individual words or tokens.
For the sentence:
“The researchers are researching better ways to research user behaviors”
Tokenization output:
[The, researchers, are, researching, better, ways, to, research, user, behaviors]
Stemming reduces words to their root form by removing suffixes, often in a crude way without
considering grammar.
Stemming output:
[the, research, are, research, better, way, to, research, user, behavior]
(Here, words like “researchers,” “researching,” and “behaviors” are reduced to simpler roots.)
Lemmatization converts words to their base or dictionary form while considering context and
grammar.
Lemmatization output:
[the, researcher, be, research, good, way, to, research, user, behavior]
(For example, “are” becomes “be,” and “better” becomes “good.”)
Part-of-Speech (POS) Tagging assigns grammatical labels to each word based on its role in the
sentence.
POS tagging output:
[The (Determiner), researchers (Noun), are (Verb), researching (Verb), better (Adjective), ways
(Noun), to (Preposition), research (Verb), user (Noun), behaviors (Noun)]
Importance of Order
The order of these operations is important because each step builds on the previous one.
Tokenization must come first, as it defines the basic units of analysis. POS tagging is often
performed before lemmatization because accurate lemmatization depends on knowing the
grammatical role of each word. Stemming or lemmatization should be applied after tokenization,
as they operate on individual words. If the order is incorrect, such as performing stemming before
identifying parts of speech, it may lead to loss of meaning or incorrect transformations, ultimately
affecting the performance of downstream tasks.
Q3. Answer the followings:   (20 marks)
********** 5 **********
--- page 6 ---
a. Explain the working of Bidirectional Encoder Representations from Transformers. Describe
Masked Language Modelling and Next Sentence Prediction. Explain how the model is fine-
tuned for classification tasks and discuss its advantages.   (10 marks)
Answer: Bidirectional Encoder Representations from Transformers is a deep learning model
based on the transformer architecture that is designed to understand the context of words in a
sentence by looking at both the left and right surroundings simultaneously. It uses multiple
layers of self-attention mechanisms, where each word attends to every other word in the
sentence to capture relationships and contextual meaning. This bidirectional nature allows the
model to develop rich representations of language, making it highly effective for various
natural language processing tasks.
The model is pre-trained using two key tasks. The first is Masked Language Modelling, where
a small percentage of words in a sentence are randomly masked, and the model is trained to
predict those missing words based on the surrounding context. For example, in a sentence, one
word may be hidden, and the model learns to infer it by understanding both the preceding and
following words. This helps the model learn deep contextual relationships.
The second task is Next Sentence Prediction, where the model is given pairs of sentences and
learns to determine whether the second sentence logically follows the first. Some sentence
pairs are actual consecutive sentences from the text, while others are randomly paired. This
helps the model understand relationships between sentences, which is useful for tasks like
question answering and text inference.
After pre-training, the model is fine-tuned for specific classification tasks such as sentiment
analysis or spam detection. Fine-tuning involves adding a simple classification layer on top of
the pre-trained model and training it on a labeled dataset. The parameters of the entire model
are slightly adjusted during this process so that it adapts to the specific task while retaining the
general language understanding learned during pre-training.
The advantages of this model include its ability to capture bidirectional context, which
improves understanding of word meanings in different situations. It achieves high accuracy
across a wide range of tasks due to its deep contextual representations. It also reduces the need
for task-specific architectures, as the same pre-trained model can be fine-tuned for multiple
applications. Overall, it represents a significant advancement in natural language processing
by improving both performance and flexibility.
b. Given the sentence below, perform Part-of-Speech tagging for each word. Clearly indicate the
appropriate grammatical category for each term. Explain the tagging process and justify your
assigned tags based on contextual meaning.
********** 6 **********
--- page 7 ---
Sentence: "Researchers develop innovative algorithms to analyze large datasets efficiently."
(10 marks)
Answer: In the sentence “Researchers develop innovative algorithms to analyze large datasets
efficiently,” each word is assigned a grammatical category based on its role in context.
“Researchers” is a plural noun as it represents the subject performing the action. “Develop” is
a verb because it expresses the main action carried out by the subject. “Innovative” is an
adjective as it describes the noun “algorithms,” which itself is a plural noun acting as the object
of the verb. The word “to” functions as an infinitive marker introducing the verb “analyze,”
which expresses purpose. “Large” is an adjective describing “datasets,” which is another plural
noun representing what is being analyzed. Finally, “efficiently” is an adverb as it modifies the
verb “analyze” by indicating how the action is performed. The tagging process relies on
understanding both the meaning of each word and its relationship with surrounding words,
ensuring that each term is correctly classified according to its contextual usage.
Q4. Answer the followings:   (20 marks)
a. Explain in detail the function of each layer in a CNN model used for NLP. Discuss how each layer
contributes to feature extraction and final classification.   (10 marks)
Answer: In a Convolutional Neural Network (CNN) for NLP, text data is processed through a
series of layers, each contributing to feature extraction and final classification.
The first layer is the embedding layer, which converts words into dense numerical vectors. Instead
of treating words as discrete symbols, this layer represents them in a continuous vector space where
similar words have similar representations. This transformation allows the model to capture
semantic meaning and relationships between words.
Next is the convolutional layer, which applies multiple filters over the input embeddings. Each
filter slides over the sequence of word vectors and captures local patterns such as phrases or n-
grams. For example, a filter may learn to detect patterns like “very good” or “not bad.” This layer
is crucial for extracting meaningful features from text by identifying important word combinations.
After convolution, an activation function (commonly ReLU) is applied. This introduces non-
linearity into the model, allowing it to learn complex patterns beyond simple linear relationships.
It also helps in making the model more expressive and capable of capturing subtle linguistic
features.
The next layer is the pooling layer, often max pooling, which reduces the dimensionality of the
feature maps generated by the convolutional layer. It selects the most important features by taking
the maximum value from each feature map. This helps in retaining the most significant information
while reducing computational complexity and making the model robust to small variations in text.
********** 7 **********
--- page 8 ---
Following pooling, the features are passed to a fully connected (dense) layer, where all extracted
features are combined. This layer learns higher-level interactions between features and prepares
the representation for classification. It essentially acts as a decision-making layer.
Finally, the output layer produces the final prediction. For classification tasks, this is usually a
softmax layer (for multi-class classification) or a sigmoid layer (for binary classification), which
converts the outputs into probabilities for each class.
Overall, each layer in a CNN contributes progressively: the embedding layer captures word
meaning, convolution extracts local features, activation adds non-linearity, pooling selects
important features, and fully connected layers combine them to produce the final classification.
b. Explain the role of Hidden Markov Models (HMM) in voice recognition systems. Describe how
HMM models sequential data and discuss its application in recognizing speech patterns. (10 marks)
Answer: Hidden Markov Models (HMMs) play a fundamental role in voice recognition systems
by modeling speech as a sequence of observable signals generated from hidden states. In speech
recognition, the actual spoken words or phonemes are considered hidden states, while the audio
signal features (such as frequency or spectral characteristics) are the observed data. The goal of
the HMM is to determine the most likely sequence of hidden states (words or phonemes) that could
have produced the observed speech signal.
HMM models sequential data by assuming that the system moves through a series of states over
time, where each state depends only on the previous state (Markov property). Each state has a
probability of transitioning to another state, known as transition probabilities. Additionally, each
state is associated with a probability distribution over possible observations, called emission
probabilities. In voice recognition, this means that each phoneme has a certain likelihood of
producing specific acoustic signals. By combining these probabilities, the HMM can evaluate
different possible sequences of states and choose the most probable one.
The model processes speech as a time series, where audio input is divided into small frames, and
features are extracted from each frame. Using algorithms such as the Forward-Backward algorithm
or the Viterbi algorithm, the HMM computes the likelihood of different state sequences and
identifies the most probable sequence corresponding to spoken words. This allows the system to
handle variations in speech, such as differences in speed, accent, and pronunciation.
In practical applications, HMMs are used to recognize speech patterns by mapping sequences of
acoustic signals to words or sentences. They are particularly effective in modeling temporal
dependencies and sequential structure in speech data. Although modern systems often combine
HMMs with deep learning models, HMMs remain important for understanding the probabilistic
framework behind speech recognition and for modeling time-dependent patterns in sequential data.
Q5. Answer the followings:   (20 marks)
********** 8 **********
--- page 9 ---
a. Explain the concept of document clustering in Natural Language Processing (NLP). Discuss the
complete process of clustering text documents, including preprocessing, feature representation
(such as TF-IDF), similarity measures, and clustering algorithms like K-means or hierarchical
clustering. Also highlight the advantages and applications of document clustering.   (10 marks)
Answer: Document clustering in Natural Language Processing refers to the task of grouping a
collection of text documents into clusters such that documents within the same cluster are more
similar to each other than to those in other clusters. It is an unsupervised learning technique,
meaning that no labeled data is required. The goal is to discover hidden patterns or structures in
large text datasets, such as grouping news articles by topic or organizing research papers into
thematic categories.
The process of document clustering begins with preprocessing. Raw text is cleaned by removing
punctuation, special characters, and stopwords (common words like “the” and “is” that carry little
meaning). The text is then tokenized into words, and techniques such as stemming or
lemmatization are applied to reduce words to their base forms. This step ensures that the text is in
a consistent and analyzable format.
Next, the text is converted into a numerical representation using feature extraction techniques such
as Term Frequency–Inverse Document Frequency (TF-IDF). TF-IDF assigns weights to words
based on their importance in a document relative to the entire collection. Words that appear
frequently in a document but are rare across the corpus receive higher weights, helping to capture
meaningful distinctions between documents.
Once documents are represented as vectors, similarity measures are used to determine how close
or similar two documents are. Common measures include cosine similarity, which calculates the
angle between two document vectors, and Euclidean distance, which measures the straight-line
distance between them. These measures help quantify the degree of similarity between documents.
After computing similarities, clustering algorithms are applied. K-means clustering partitions
documents into a predefined number of clusters by assigning each document to the nearest cluster
centroid and iteratively updating the centroids. Hierarchical clustering, on the other hand, builds a
tree-like structure of clusters either by merging smaller clusters (agglomerative) or splitting larger
ones (divisive). These methods group documents based on their similarity in the feature space.
Document clustering offers several advantages. It helps in organizing large volumes of
unstructured text, improves information retrieval, and enables better data exploration without
requiring labeled data. It is widely used in applications such as topic detection, news aggregation,
recommendation systems, customer feedback analysis, and search engine optimization.
********** 9 **********
--- page 10 ---
Overall, document clustering is a powerful technique for uncovering structure in textual data by
combining preprocessing, feature representation, similarity measurement, and clustering
algorithms.
b. Although CNNs were originally developed for image processing, they are widely used in NLP
tasks. Explain why CNNs are effective for text classification tasks, highlighting their key
properties.   (10 marks)
Answer: Although Convolutional Neural Networks were originally designed for image processing,
they have proven to be highly effective for text classification tasks due to their ability to capture
local patterns and important features in text data.
One key property of CNNs is their ability to detect local features using convolutional filters. When
applied to text, these filters slide over sequences of word embeddings and capture meaningful
patterns such as phrases or n-grams like “very good” or “not satisfied.” These local patterns are
often strong indicators of the overall meaning or sentiment of a sentence, making CNNs well-
suited for classification tasks.
Another important property is parameter sharing. The same filter is applied across the entire text,
which allows the model to detect the same pattern regardless of its position in the sentence. This
property, known as position invariance, ensures that important features are recognized no matter
where they appear, improving the robustness of the model.
CNNs also use pooling operations, such as max pooling, to reduce the dimensionality of the feature
maps while retaining the most important information. Pooling helps in selecting the most relevant
features and makes the model less sensitive to small variations in text, such as slight changes in
word order.
Additionally, CNNs are computationally efficient because they allow parallel processing of data,
unlike sequential models such as Recurrent Neural Networks. This makes them faster to train and
scalable for large datasets.
CNNs are also effective because they require fewer parameters compared to some other deep
learning models, reducing the risk of overfitting while still capturing essential patterns in the data.
Overall, the ability of CNNs to capture local dependencies, recognize patterns regardless of
position, reduce dimensionality through pooling, and process data efficiently makes them highly
effective for text classification tasks such as sentiment analysis, spam detection, and topic
categorization.
Q6. Answer the followings:   (20 marks)
a. Analyze the role of transfer learning in improving NLP model performance. Explain why transfer
learning is particularly effective for text data, and discuss its advantages over training models from
********** 10 **********
--- page 11 ---
scratch. Illustrate your answer with examples of real-world applications, including domain-
specific models such as FinBERT, and explain how they enhance performance in specialized tasks.
(10 marks)
Answer: Transfer learning in NLP refers to the process of taking a model that has been pre-trained
on a large corpus of text and adapting it to a specific task or domain. Instead of training a model
from scratch, which requires large amounts of labeled data and computational resources, transfer
learning leverages knowledge already learned during pre-training and fine-tunes it for a target task
such as sentiment analysis, classification, or question answering.
The key role of transfer learning is to improve model performance by utilizing general language
understanding learned from massive datasets. During pre-training, models learn grammar, syntax,
semantics, and contextual relationships between words. When fine-tuned on a smaller, task-
specific dataset, the model can quickly adapt and achieve high accuracy because it already
understands the structure of language. This significantly reduces the need for large labeled datasets
in the target task.
Transfer learning is particularly effective for text data because language has underlying patterns
and structures that are common across domains. Words, phrases, and grammatical rules are reused
in different contexts, allowing pre-trained models to generalize well. Additionally, labeled text
data is often scarce and expensive to obtain, so transfer learning helps overcome data limitations
by reusing knowledge from large unlabeled corpora.
Compared to training models from scratch, transfer learning offers several advantages. It reduces
training time and computational cost, as the model starts from a well-informed state rather than
random initialization. It improves performance, especially when the available labeled data is
limited. It also enhances generalization, making models more robust to variations in text.
Furthermore, it simplifies model development since pre-trained architectures can be reused for
multiple tasks.
A strong example of transfer learning in practice is domain-specific models such as FinBERT.
FinBERT is a version of BERT that has been further trained on financial texts such as earnings
reports, news articles, and analyst reports. While a general model understands everyday language,
FinBERT captures domain-specific terminology and nuances like “bullish,” “liquidity,” or
“earnings surprise.” This leads to improved performance in tasks such as financial sentiment
analysis, risk assessment, and market prediction.
Other real-world applications include healthcare NLP models trained on medical literature for
clinical text analysis, legal NLP models for contract analysis, and customer support chatbots that
adapt to company-specific language. In each case, transfer learning allows the model to retain
general language understanding while specializing in a particular domain.
********** 11 **********
--- page 12 ---
Overall, transfer learning plays a crucial role in modern NLP by enabling efficient, accurate, and
scalable model development. By combining general knowledge with domain-specific adaptation,
it significantly enhances performance across a wide range of real-world applications.
b. Differentiate between speech recognition and voice recognition. Discuss their working principles,
applications, and key challenges in real-world systems.   (10 marks)
Answer: Speech recognition and voice recognition are related but distinct technologies used in
audio processing systems.
Speech recognition refers to the process of converting spoken language into text. It focuses on
understanding *what is being said*, regardless of who is speaking. The system analyzes audio
signals, extracts features such as frequency and phonemes, and maps them to words using acoustic
and language models. Modern systems often use deep learning models along with probabilistic
approaches to improve accuracy. Speech recognition is widely used in applications such as virtual
assistants, transcription services, automated customer support, and dictation software.
Voice recognition, on the other hand, is concerned with identifying or verifying *who is speaking*.
It analyzes unique characteristics of a person’s voice, such as pitch, tone, and speaking style, to
match it with stored voice profiles. It is commonly used for authentication and security purposes,
such as unlocking devices, banking verification systems, and access control.
The working principles of the two also differ. Speech recognition systems process audio signals
by breaking them into smaller units, extracting features, and using models to convert them into
text based on language patterns. In contrast, voice recognition systems focus on biometric analysis,
where voice features are compared against known samples to identify or verify an individual.
In terms of applications, speech recognition is used in areas like real-time translation, voice typing,
and chatbot interaction, while voice recognition is used in security systems, personalized user
experiences, and fraud detection.
Both systems face several challenges in real-world environments. For speech recognition,
challenges include background noise, accents, dialects, homophones, and variations in speaking
speed. For voice recognition, challenges include changes in a person’s voice due to illness or aging,
background interference, and the risk of spoofing or imitation. Additionally, both systems must
handle privacy concerns and ensure secure processing of audio data.
In summary, speech recognition focuses on understanding spoken content, while voice recognition
focuses on identifying the speaker, and both play important roles in modern intelligent systems
despite facing practical challenges.
Q7. Answer the followings:   (20 marks)
********** 12 **********
--- page 13 ---
a. Consider a dataset containing noisy text with inconsistent formatting, including extra spaces,
special characters, and mixed case words. Explain how Regular Expressions can be used to clean
and standardize the text. Illustrate your answer with suitable examples and discuss the limitations
of using Regular Expressions for complex Natural Language Processing tasks.   (10 marks)
Answer: Regular Expressions (regex) are powerful pattern-matching tools used to clean and
standardize noisy text by identifying and transforming specific patterns in strings. In datasets with
inconsistent formatting—such as extra spaces, special characters, or mixed case—regex helps
automate preprocessing and prepare text for further NLP tasks.
One common use is removing extra spaces. For example, a sentence like “This is messy text”
can be cleaned by using a pattern that matches multiple spaces and replaces them with a single
space, resulting in “This is messy text.” Regex can also remove leading and trailing spaces to
standardize formatting.
Another use is handling special characters. For instance, text like “Hello!!! @user #NLP$$$” can
be cleaned by removing unwanted symbols using a pattern that retains only alphabets and numbers.
The result becomes “Hello user NLP.” This helps in eliminating noise that does not contribute to
meaning.
Regex is also useful for case normalization. Although case conversion is often done using built-in
functions, regex can help identify patterns before applying transformations. For example,
converting “TeXT DaTa” into “text data” ensures consistency across the dataset.
Additionally, regex can standardize patterns such as numbers, emails, or dates. For example, email
addresses like “[test123@gmail.com](mailto:test123@gmail.com)” can be detected and replaced
with a placeholder like “EMAIL,” and dates in different formats can be normalized to a consistent
structure. This is especially useful in anonymization and structured data extraction.
Regex can also be used for token cleaning, such as removing repeated characters in words like
“soooo good” to “soo good” or filtering out unwanted tokens.
However, regex has several limitations in complex NLP tasks. It is rule-based and lacks
understanding of context or semantics, so it cannot handle ambiguity in language. For example, it
cannot distinguish between different meanings of the same word based on context. It also becomes
difficult to maintain and scale when dealing with large and complex text patterns. Regex is not
suitable for tasks like sentiment analysis, entity recognition, or language understanding, where
deeper linguistic and contextual knowledge is required. Additionally, overly complex regex
patterns can become hard to read and error-prone.
In summary, regular expressions are highly effective for basic text cleaning and standardization
tasks, but they are limited when it comes to handling complex language structures and deeper NLP
problems.
********** 13 **********
--- page 14 ---
b. Explain the Continuous Bag of Words model used in word embedding. Describe its architecture
and working mechanism. Illustrate how the model predicts a target word using surrounding context
words with a suitable example.   (10 marks)
Answer: The Continuous Bag of Words (CBOW) model is a neural network–based approach used
in word embedding techniques to learn vector representations of words. It is part of the Word2Vec
framework and is designed to predict a target word based on its surrounding context words. The
main idea is that words appearing in similar contexts tend to have similar meanings, and CBOW
captures this by learning embeddings that reflect these relationships.
The architecture of the CBOW model consists of three main layers: an input layer, a hidden layer,
and an output layer. The input layer takes multiple context words surrounding a target word. These
words are usually represented as one-hot encoded vectors. In the hidden layer, these input vectors
are projected into a lower-dimensional continuous space using a shared weight matrix, which acts
as the embedding matrix. The embeddings of the context words are then averaged (or summed) to
form a single context vector. The output layer uses this context vector to predict the probability
distribution over all words in the vocabulary, typically using a softmax function.
The working mechanism of CBOW involves sliding a fixed-size window over the text. For each
position in the text, the model takes the surrounding words within the window as input and tries to
predict the center word. During training, the model adjusts its weights to maximize the probability
of correctly predicting the target word given its context. Over time, the embedding matrix learns
meaningful representations of words.
For example, consider the sentence: “The cat sits on the mat.” If the context window size is 2, and
the target word is “sits,” the context words would be “The,” “cat,” “on,” and “the.” These context
words are fed into the model, their embeddings are averaged, and the model predicts the word
“sits.” By repeatedly training on such examples, the model learns that words appearing in similar
contexts (like “sits,” “rests,” “lies”) will have similar vector representations.
The CBOW model is efficient and works well for learning word embeddings from large datasets.
It captures semantic relationships between words and is particularly effective when the dataset is
large and context information is rich.
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 56b6ae3fde98

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AI_7012/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: mixed (20 pages), mean OCR confidence 36.4
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 02 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.1   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples.
BL-2;   Ans:
Natural Language   Natural Language
Aspect
Understanding (NLU)   Generation (NLG)
NLU is the ability of a NLG is the ability of a
machine to   machine to generate
comprehend and   human-like language (text
Definition
interpret human   or speech) from structured
language in a   data or internal
meaningful way.   representations.
To understand the
To produce coherent and
Purpose   meaning of the input
meaningful text as output.
text.
Structured data, machine-
Human-readable text or
Input   readable content, or
speech.
semantic representation.
Semantic
understanding, intents, Human-readable text,
Output   entities, sentiment, or   sentences, paragraphs, or
meaning   conversational responses.
representation.
********** 1 **********
--- page 2 ---
Named Entity
Template-based generation,
Recognition (NER),
Neural Networks (like GPT
Techniques Used Sentiment Analysis,
models), Rule-based text
Intent Detection,
generation.
Semantic Parsing.
Input: “Book a flight to
Example
New York tomorrow.”
Output: Intent =   Input: Structured data:
BookFlight,   {“City”: “New York”,
Destination = New “Weather”: “Sunny”,
York, Date =   “Temperature”:
Tomorrow.   “25°C”}
Output: “The
weather in New
York is sunny
today with a
temperature of
25°C.”
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
Ans:
Chunking-2M
Chinking 2M
POS Tagging role 1M
Sentence: “The black dog is running in the park.”
• Chunking: Groups words → [The black dog] (NP), [the park]
(NP).
• Chinking: Removes unwanted words → e.g., remove in
(preposition) from the chunk.
POS Tagging: Provides word categories (DT, JJ, NN, etc.), which are
used to apply chunking and chinking rules.
CO-4,   c.5   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
Ans:
(2+2+1) = 5 Marks
Hyponymy and Hypernymy
Hyponymy is a semantic relation in which the meaning of one word is
included in the meaning of another word.
Example: rose, tulip, and lily are hyponyms of flower.
The statement can be expressed as: “A rose is a kind of flower.”
Hypernymy is the opposite relation: it refers to the more general word
whose meaning includes that of more specific words.
********** 2 **********
--- page 3 ---
Example: flower is a hypernym of rose, tulip, and lily.
Similarly, animal is a hypernym of dog, cat, and elephant.
Application of Hypernymy in Word Sense Disambiguation (WSD)
Hypernymy relations are very useful in WSD because they allow a system
to connect ambiguous words to their broader, more general categories. By
checking the surrounding context and mapping it to the correct hypernym,
a system can choose the right sense of a word.
Example: Consider the polysemous word “bank.”
Sense 1: financial institution (hypernym = organization)
Sense 2: river bank (hypernym = geographical feature / landform)
If the sentence is:
“The boy was fishing on the bank.”
Words like fishing and river in the context point towards the hypernym
geographical feature.
Therefore, bank here means river bank.
“She deposited money in the bank.”
Context words like money and deposit map to the hypernym organization.
Therefore, bank here means financial institution.
In WSD, hypernymy helps map ambiguous words to their general category,
and then context determines which sense is correct.
CO-3;   d. 6   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3   Ans: Marks Distribution-3 Marks for Comparison and 2 Marks for
Example of each type
Pragmatics concentrates on speaker intention and context-dependent meaning,
whereas discourse analysis investigates how sentences and utterances are
connected to form coherent texts and conversations. Together, they provide a
comprehensive   understanding   of how language   functions   in   real
communication.
Pragmatics is the branch of linguistics that studies how meaning is shaped by
context of use. It goes beyond the literal semantic meaning of words and
focuses on how speakers use language to achieve communicative goals.
Example “Can you pass the salt?” — pragmatically, this is not a question about
ability but a request.
Discourse analysis studies how sentences and utterances are connected to
form larger units of meaning such as conversations, narratives, or written
texts.   It   is concerned with cohesion (linguistic ties like reference,
substitution, conjunctions) and coherence (logical flow of ideas in context).
Example :“I bought a book yesterday. The book was about artificial
intelligence.”
********** 3 **********
--- page 4 ---
→ The second sentence refers back to “a book” using “the book,” creating
textual cohesion.
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;
SO-1;   ii.   Discuss the significance of NER in three different NLP
BL-2,3   applications.
Ans:
Ans: [Marks 5+5]
i.
Feature   Morpheme   Lexeme
Meaning The smallest grammatical The basic unit of lexical
unit in a language that   meaning — represents a set
carries meaning.   of related word forms.
Function Deals with word structure Deals with word meaning
(morphology).   and usage in the lexicon.
Example   Morpheme   Lexeme
Unhappi   Has three morphemes:   The lexeme is HAPPY,
ness   “un-” (prefix), “happy”   which can appear as happy,
(root), “-ness” (suffix).   happier, happiest.
Running   Has two morphemes:   The lexeme is RUN, which
“run” + “-ing”.   includes run, runs, ran,
running.
ii.
1. Information Extraction (IE)
Automatically extracts structured information (names, dates,
locations, organizations) from unstructured text such as news
articles, reports, or legal documents.
2. Question Answering Systems (QA)
Helps identify entities in questions and documents (e.g., “Who is
the   CEO of Tesla?” → CEO = role, Tesla = organization).
3. Machine Translation
Ensures named entities like “Barack Obama” or “New Delhi”
are   translated correctly or kept unchanged.
4. Healthcare & Biomedical Text Mining
Extracts entities such as patient names, diseases, medications,
genes, or proteins from medical records and research papers.
5. Customer Feedback & Social Media Analysis
Identifies product names, brands, locations, or events in tweets,
reviews, and online discussions for business intelligence.
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
********** 4 **********
--- page 5 ---
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
Assume the <s> and </s> for each sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> artists paint murals in city </s>
<s> musicians play songs in city </s>
<s> painters paint murals on walls </s>
<s> signs are near city </s>
Test sentence-
<s> artists paint murals near city </s>
Distinct tokens are:
<s>, </s>, artists, paint, murals, in, city, musicians, play, songs,
painters, on, walls, signs, are, near
That gives V=16.
Counts:
• Unigram counts:
o C(artists)=1
o C(paint)=2
o C(murals)=2
o C(near)=1
o C(city)=3
o C(<s>)=4
• Bigram counts:
o C(<s>,artists)=1
o C(artists,paint)=1
o C(paint,murals)=2
o C(murals,near)=0
o C(near,city)=1
o C(city,</s>)=3
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(artists∣<s>)=[1+1]/[4+16]=2/20=1/10≈0.1
2. P(paint∣artists)=[1+1]/[1+16]=2/17≈0.117647
3. P(murals∣paint)=[2+1]/[2+16]=3/18=1/6≈0.166667
4. P(near∣murals)=[0+1]/[2+16]=1/18≈0.0555556
5. P(city∣near)=[1+1]/[1+16]=2/17≈0.117647
6. P(</s>∣city)=[3+1]/[3+16]=4/19≈0.210526
Exact fraction:
P+1=1/10*2/17*1/6*1/18*2/17*4/19=16/5930280=2.698E-6
Hence, the probability of the test sentence is =2.698E-6.
********** 5 **********
--- page 6 ---
Q3   a   i.   Explain the various types of ambiguities encountered in Natural [10]
CO- 3,   Language Processing (NLP). Illustrate each type with suitable
SO-, BL-   examples.
ii.   Compare top-down and bottom-up parsing and apply bottom-up
4
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-
“A cat chased the mouse”
Grammar   Lexicon
S → NP VP   Det → {A, the}
NP → Pronoun   Noun → {cat, mouse}
NP → Proper-Noun   Verb → {chased}
NP → Det Nominal
Nominal → Noun
Nominal → Nominal Noun
Nominal → Nominal PP
VP → Verb
VP → Verb NP
VP → VP PP
PP → Prep NP
Ans: Marks-5
1. Lexical Ambiguity:
Meaning:
Occurs when a word has multiple possible meanings.
Example:
He went to the bank.
• “bank” can mean a financial institution or the side of a river.
Explanation:
NLP systems must use context to decide which meaning of “bank”
applies in the sentence.
2. Syntactic Ambiguity (Structural Ambiguity)
Meaning:
Occurs when a sentence can be parsed in more than one way due to
different grammatical structures.
Example:
I saw the man with the telescope.
•   Interpretation 1: I used the telescope to see the man.
•   Interpretation 2: The man had the telescope.
Explanation:
The ambiguity arises because the prepositional phrase (“with the
telescope”) can modify either the verb saw or the noun man.
3. Semantic Ambiguity
Meaning:
Occurs when the meaning of the sentence itself is unclear, even if the
structure is fine.
Example:
Visiting relatives can be boring.
********** 6 **********
--- page 7 ---
•   Interpretation 1: The act of visiting relatives is boring.
•   Interpretation 2: The relatives who visit are boring.
Explanation:
The confusion comes from whether visiting is used as a gerund (verb)
or adjective (modifier).
4. Pragmatic Ambiguity
Meaning:
Arises when the intended meaning depends on context or speaker’s
intention rather than grammar or word meaning.
Example:
Can you pass the salt?
•   Literally, it’s a question about ability.
•   Pragmatically, it’s a request for action.
Explanation:
Understanding pragmatic meaning requires world knowledge and
context.
5. Referential Ambiguity
Meaning:
Occurs when a pronoun or reference word could refer to multiple
entities.
Example:
John told Tom that he was late.
• “he” could refer to John or Tom.
Explanation:
The ambiguity arises in anaphora (reference resolution).
ii.
Comparison (Any two relevant points-2M)
Aspect   Top-Down Parsing   Bottom-Up Parsing
Starts from the root (start   Starts from input tokens
Parsing   symbol) and expands   and reduces toward the
Direction   toward the input.   root.
Expands non-terminals
using grammar rules,   Combines tokens/phrases
Grammar Rule   even before seeing if   only if they appear in the
Application   input matches.   input.
Fails or loops infinitely
Handling Left   if grammar has left   Naturally handles left
Recursion   recursion.   recursion without issues.
May get stuck or need   Can face shift-reduce or
Ambiguity   backtracking when   reduce-reduce conflicts in
Handling   grammar is ambiguous.   ambiguous grammars.
Ease of   Conceptually simple and More complex (needs
Implementation   intuitive to implement.   parsing tables, stacks).
Bottom up parsing with steps-3
********** 7 **********
--- page 8 ---
Godors wp awry ti

‘ vos Hy )
=— : ver
a Nowr vub \ cbt
\ che ome Pet
; nan
_ Norin® wee
\ % *
Oe one ‘i ete atase
kb
zeus avid Mar Rs arte)
Ng NP
aearel worn
aie wee vib DE “
y 2
stop bak rik yin?” “nr 1°
NP
~~
4 J
My ye Nomint
7 ; / degee
ve
al var mone

“ unr Chock 1

Shp © form cunUR tt)

62 NY Ny

Coton we “nt IM Fina

“A Cok chuck ue we
= a

‘Se:

ok che TN Monee

FIC QF EH 1
--- page 9 ---
CO-3;   b   Consider the given paragraph given below:   [10]
SO- 1   The teacher wrote on the board. The students listened to the teacher.
BL-4:   The board was full of notes. The student asked a question. The
teacher answered from the book.
Target words: teacher, student, board, book
Context words: wrote, listened, notes, question
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.
Plot the target word vectors by considering only two dimensions: “wrote”
and “notes”.
Ans: [Marks 5+5]
Co-occurrence matrix:
target \ context   wrote   listened   notes
teacher   1   1   0
student   0   1   0
board   1   0   1
book   0   0   0
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2   Ans:[Marks-5+5]
It is an essential step in natural language processing (NLP) that involves
cleaning and transforming unstructured text data to prepare it for analysis.
Text data contains noise in various forms like emoticons, punctuations, text in
a different cases, HTML tags etc.
********** 9 **********
--- page 10 ---
Inadequate or low-quality data can lead to lower accuracy and effectiveness of
the model.
The pre-processing steps for a problem depend mainly on the domain and the
problem itself, hence, we don’t need to apply all steps to every problem and
also the order of applying these steps may also vary.
Various text preprocessing steps are widely used for dimensionality reduction.
Some of the commonly used preprocessing steps are:
o Removing punctuations like . , ! $( ) * % @, URLs, Stop
words
o Lower casing
o Normalization (some common ones)
▪   Tokenization
▪ Stemming
▪ Lemmatization
Stop word removal:
• Stop words are a set of commonly used words in a language like “a”,
“the”, “is”, “are” etc. in English.
• These words do not carry important meaning and are removed from
texts in many data science tasks.
• The intuition behind this approach is that, by removing low
information words from text, we can focus on the important words
instead.
• One of the advantages of removing stop words is that it can reduce the
size of the dataset, which in turn reduces the training time required for
building natural language processing models.
• Stop word removal is commonly applied in search systems, text
classification applications, topic modeling, topic extraction and others.
• Stop word lists can come from pre-established sets or you can create a
custom one for your domain. This creation may be tricky as few words
that may not be useful in some problem statement may be important in
others.
Lower casing:
•   Usually, this is the first step that is performed while pre-processing.
•   Is a text preprocessing step where all letters in the text are converted
to lowercase.
•   This step is implemented so that the algorithm does not treat the same
words differently in different situations.
o Ex: Book and book mean the same but when not converted to
the lower case those two are represented as two different
words in the vector space model (resulting in more
dimensions).
• However, it is important to remember that some words, like “US” and
“us”, can change meanings when reduced to the lower case. Also,
there can be cases where the capitalization is important and has to be
preserved. So we should avoid performing this step in such cases
Normalization:
• As raw text data is random, each word has a lot of variations in the form of
tenses, superlatives, and many more.
********** 10 **********
--- page 11 ---
• These variations increase the complexity of the data and are difficult for the
machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data into a
predefined standard, hence improving the efficiency of the model.
• Ex: Many forms of the base word collect - "collection", "collective", and
"collectively".
•   If we reduce the variations of a word in the raw text, there will be fewer
input variables for our machine-learning model to deal with, thus increasing
efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for structures
like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Few common ones used are:
• Removal of duplicate whitespaces and punctuation.
• Accent removal (if your data includes diacritical marks from ‘foreign’
languages).
•   Substitution of contractions (Ex: ‘I’m ’→‘I am’ and don’t to do not).
• Transform word numerals into numbers (Ex: ‘twenty three’→‘23’).
•   Substitution of values for their type (Ex: ‘$50’→‘MONEY’).
• Acronym normalization (Ex: ‘US ’→‘United States’/‘U.S.A’) and
abbreviation normalization (Ex: ‘btw’ → ‘by the way’).
• Normalize date formats, social security numbers or other data that have a
standard format.
•   Spell correction (one could say that a word can be misspelled infinite
ways, so spell corrections reduce the vocabulary variation by “correcting”)
•   Substitution of rare words for more common synonyms.
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
Noun   Verb   Noun
BL-4
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Ans:
********** 11 **********
--- page 12 ---
Q5   a   For the following two sentences:   [10]
• Sentence A: “The student read a science book in the library”
• Sentence B: “The teacher read a history book in the classroom”
********** 12 **********
--- page 13 ---
CO-2;   1. Construct the TF-IDF matrix for these sentences after removing
SO-1 ;   the stop words {The, a, in}.
BL-3;   2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
Ans:[Marks 5+5]
Term   Sentence   Sentence
A   B
student   0.693   0
read   0   0
science   0.693   0
book   0   0
library   0.693   0
teacher   0   0.693
history   0   0.693
classroo   0   0.693
m
Analysis:
For Sentence A, the unique theme is student, science, library.
For Sentence B, the unique theme is teacher, history, classroom.
So, it indicates that TF–IDF clearly shows that shared words don’t matter for
separation, while unique words carry more importance.
CO-4;   b   Consider the sentence: “The bat hit the ball hard on the cricket field.”   [10]
SO-1BL-   Two possible senses of “bat”:
4
• Sense 1: Bat (Sports equipment – cricket/baseball)
• Sense 2: Bat (Nocturnal flying mammal)
Sentence
Context Words   Sense (Class)
ID
ball, cricket, score,   Sports (Bat =
1
stadium   equipment)
Animal (Bat =
2   night, cave, wings, fly
mammal)
3   player, run, match, bat   Sports
4   nocturnal, vampire, insect Animal
5   team, field, bowl, bat   Sports
6   dark, flying, cave, night   Animal
a) Using the Naïve Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naïve Bayes
Classification.
Ans:
********** 13 **********
--- page 14 ---
P(Sports)=0.5
1 mk
P(Animal)=0.5
Unique words across both classes: (words: ball, cricket, score, stadium,
player, run, match, bat, team, field, bowl, night, cave, wings, fly,
nocturnal, vampire, insect, dark, flying) Total 20
1
mk
Calculations:
For Sports:
2 mks
• P(hit∣S)=(0+1)/32=1/32=0.03125
• P(ball∣S)=(1+1)/32=2/32=0.0625
• P(cricket∣S)=2/32=0.0625
• P(field∣S)=2/32=0.0625
• P(hard∣S)=1/32=0.03125
For Animal:
P(w∣A)=1/31≈0.03225806
Likelihood for sports:
2 mks
0.5 * 0.03125*0.0625*0.0625*0.0625*0.03125 =1.19209290×10-7
Likelihood for animal :
1.74647163×10-8
Classified sense: Sports equipment
1 mk
Laplace Smoothing:
3 mks
Handles problem of zero probabilities, improves robustness of
classifier.
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate
how it predicts the target word from its surrounding context
Ans:
********** 14 **********
--- page 15 ---
iii.   Marks Distribution-3 Marks for approach explanation and 2
Marks for advantage of each type
Co-reference resolution: task of finding all expressions in text that refer to
the same entity. (1.5 marks)
Example: Mary said Mary is tired. She went home. → "Mary" and "She" co-
refer.
Pronoun resolution: a subtask focusing only on resolving pronouns to their
antecedents. (1.5 marks)
Example: John met Peter when he was leaving. → "he" could refer to John or
Peter.
Difference: co-reference is broader (includes noun phrases, names, definite
descriptions), while pronoun resolution is narrower.
In Word2Vec, two main architectures are used to learn word
embeddings:
Continuous Bag of Words (CBOW) and
Skip-Gram.
Both are neural network-based models that learn to represent words as
dense vectors based on their context in a text corpus.
1. Continuous Bag of Words (CBOW) Model
Working Principle:
The CBOW model predicts the target word from its surrounding
context words.
It takes context words as input and tries to predict the central
(target) word.
The model averages (or sums) the vectors of the context words and
passes them through a neural network to predict the target word.
Example:-Sentence
“The cat sat on the mat”
If the window size = 2, and the target word is “sat”, then the context
words are:
["The", "cat", "on", "the"]
The CBOW model learns:
P(sat | The, cat, on, the)
Intuition:
It focuses on understanding the meaning of a word based on its
surrounding words.
2. Skip-Gram Model
Working Principle:
• The Skip-Gram model does the reverse of CBOW.
•   It predicts the context words given a target word.
• The target word is input, and the model learns to predict
surrounding context words.
Example:-Sentence:
“The cat sat on the mat”
If the target word is “sat” and window size = 2, then the context
words are:
["The", "cat", "on", "the"]
********** 15 **********
--- page 16 ---
The Skip-Gram model learns:
P(The | sat), P(cat | sat), P(on | sat), P(the | sat)
Intuition:
It focuses on how a single word relates to its neighboring words.
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Ans: Marks Distribution-5 Marks for approach explanation and 5 Marks
for resolution
i
Hobbs’ Algorithm is a syntactic algorithm for pronoun resolution in NLP.
It identifies possible antecedents for a pronoun by traversing a syntactic parse
tree in a systematic manner.
Example:
Sentence: “When Mary saw Alice, she waved.”
• Pronoun = she
• Step 1: Start at NP dominating “she.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs = “Mary,” “Alice.”
• Step 4: First candidate = Mary, chosen as antecedent.
Limitations :
Struggles with ambiguous cases (gender/number mismatch ignored).
Not efficient for long, complex sentences.
ii Sentence: “Ravi met Suresh at the station after he arrived from
Delhi.”
Pronoun: he
Steps of traversal:
1. Start at NP for “he.”
2. Move up to nearest S node.
3. Traverse left branches → encounter NPs: Ravi, Suresh.
4. Candidate 1 = Ravi, Candidate 2 = Suresh.
5. According to Hobbs’ order: Ravi is encountered first.
Hobbs’ algorithm chooses Ravi as antecedent of “he.”
But semantically, “Suresh” may also make sense depending on context
→ shows limitation of Hobbs.
Q7   a   Explain the working of text classification in Natural Language Processing [10]
(NLP) and discuss the key steps involved in building a text classification
********** 16 **********
--- page 17 ---
CO-4;   system in context of real-world applications such as spam detection or
SO-1 BL-   news categorization.
3:   Ans:
Text classification is the process of automatically assigning categories or
labels to text data based on its content.
Examples include:
Spam filtering – Classifying emails as “spam” or “not spam.”
News categorization – Grouping news articles into topics like sports,
politics, or entertainment.
Sentiment analysis – Identifying whether a review or comment is
positive, negative, or neutral.
Steps Involved in Text Classification
1. Data Collection
Gather a dataset containing text documents and their corresponding labels.
• Example: A set of emails labeled as “spam” or “ham” (not spam).
2. Data Preprocessing
Prepare the text for analysis by cleaning and normalizing it. Common steps
include:
• Lowercasing – Convert all text to lowercase.
• Removing noise – Punctuation, special characters, HTML tags, etc.
•   Tokenization – Splitting text into individual words or tokens.
•   Stop word removal – Removing common words like “the,” “is,”
“and.”
• Stemming/Lemmatization – Reducing words to their base or root form
(e.g., “running” → “run”).
3. Feature Extraction / Text Representation
Convert the cleaned text into a numerical format that a machine learning
model can understand. Common methods:
• Bag of Words (BoW) – Counts the occurrence of each word in the
document.
• TF-IDF (Term Frequency–Inverse Document Frequency) – Weighs
words based on their importance.
• Word Embeddings (e.g., Word2Vec, GloVe) – Captures semantic
meaning of words in vector form.
•   Transformer-based embeddings (e.g., BERT) – Context-aware
representations of text.
4. Model Training
Train a classification algorithm using the numerical features and their labels.
Examples of models:
•   Traditional ML: Naive Bayes, Logistic Regression, SVM.
• Deep Learning: RNNs, CNNs for text, Transformers (e.g., BERT).
5. Model Evaluation
Evaluate the trained model using metrics such as:
• Accuracy – Overall correctness.
•   Precision & Recall – Useful for imbalanced datasets (e.g., spam
detection).
•   F1-score – Balance between precision and recall.
6. Prediction / Deployment
********** 17 **********
--- page 18 ---
Use the trained model to classify new, unseen text data.
Example: A new email arrives → model predicts “spam” or “not spam” →
automatically sorted into the correct folder.
7. Monitoring and Updating
Over time, new words and patterns emerge. The model should be regularly
retrained with updated data to maintain accuracy.
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
Ans: [Marks 5+5]
i. Different corpus structures are applied to different NLP tasks
depending on the information they provide:
Flat Text Corpus (e.g., plain .txt files):
This type contains only raw text without labels. It can be applied to tasks
like word frequency analysis, calculating readability scores, or
comparing the styles of different writers. For example, one can apply it
to study the most common words in political speeches.
Annotated Corpus (e.g., POS-tagged or parsed text):
This type contains extra linguistic information such as part-of-speech
tags, named entities, or syntactic structures. It can be applied in
supervised learning tasks such as training a Part-of-Speech tagger,
Named Entity Recognition, or parsing models. For instance, a POS-
tagged corpus can be used to train a model that automatically identifies
nouns and verbs in new texts.
ii. Jaccard similarity takes into account only the set of unique words
for each text document. This makes it the likely candidate for
assessing the similarity of documents when repetition is not an issue.
Both Euclidean and cosine similarity metrics drop if an additional
word is added to the list.
Jaccard similarity is limited to assessing the lexical similarity of text,
i.e., how similar documents are on a word level.
The differentiating factor between Euclidean and Cosine measure is
that cosine similarity is not affected by the magnitude/length of the
feature vectors. It only considers the angle between them, making it
ideal for comparing vectors of different lengths. (Ex: If a word
‘senate’ occurs more frequently in doc 1 than it does in doc 2, we
could assume that doc 1 is more related to the topic of Politics.
However, it could also be the case that we are working with news
articles of different lengths and word ‘senate’ probably occurred more
in doc 1 simply because it was way longer)
Ex:
********** 18 **********
--- page 19 ---
Doc 1: “I love data science and machine learning”
Doc 2: “I love machine learning”
Step 1: Preprocess the documents - Remove stopwords like “I”, “and”,
etc., and lowercase everything.
Doc 1 → ['love', 'data', 'science', 'machine', 'learning’]
Doc 2 → ['love', 'machine', 'learning’]
Vocabulary :['love', 'data', 'science', 'machine', 'learning']
Jaccard
Intersection: ['love', 'machine', 'learning'] → 3 words
Union: ['love', 'data', 'science', 'machine', 'learning'] → 5 words
Jaccard=3/5=0.6
Cosine
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Dot product = 1∗1+1∗0+1∗0+1∗1+1∗1=31∗1+1∗0+1∗0+1∗1+1∗1=3
|A| = √(1²+1²+1²+1²+1²) = √5 ≈ 2.236
|B| = √(1²+0²+0²+1²+1²) = √3 ≈ 1.732
cos(θ)= 3/(2.236×1.7323) ≈ 3/3.8723 ≈0.775
Euclidean:
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Distance=Sqrt((1−1)2+(1−0)2+(1−0)2+(1−1)2+(1−1)2 )
Distance= ≈1.414
Measure   Value   Meaning
Jaccard   0.6   60% of the words overlap
Cosine   0.775   High similarity in word pattern
Euclidean   1.414   Some difference in word presence
In short, flat corpora are applied to simpler, surface-level analysis, while
annotated corpora are applied to more advanced supervised NLP tasks.
********** 19 **********
--- page 20 ---
Synoptic Answer for Q 3 b iii.
There are two correct ways of plotting the answer.
Regarding marks distribution:
part (i): 4 M
part (ii): 3 M
part (iii): 3 M
Total (10 M)
Q5 a) Formula to calculate TF and IDF
Here doc A refer Sentence A and doc B refer Sentence B
Alternate solution for Q5b
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 5811d7382fb9

- Departments: AI and Data Science, Artificial Intelligence, Computer Engineering, Information Technology
- Programmes: BTech AIDS 7056, BTech Computer 7002, BTech IT 7001, MBATech AI 7051, MBATech Computer 7047, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/MBATech_AI_7051/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf` (+5 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: mixed (20 pages), mean OCR confidence 36.4
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 02 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.1   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples.
BL-2;   Ans:
Natural Language   Natural Language
Aspect
Understanding (NLU)   Generation (NLG)
NLU is the ability of a NLG is the ability of a
machine to   machine to generate
comprehend and   human-like language (text
Definition
interpret human   or speech) from structured
language in a   data or internal
meaningful way.   representations.
To understand the
To produce coherent and
Purpose   meaning of the input
meaningful text as output.
text.
Structured data, machine-
Human-readable text or
Input   readable content, or
speech.
semantic representation.
Semantic
understanding, intents, Human-readable text,
Output   entities, sentiment, or   sentences, paragraphs, or
meaning   conversational responses.
representation.
********** 1 **********
--- page 2 ---
Named Entity
Template-based generation,
Recognition (NER),
Neural Networks (like GPT
Techniques Used Sentiment Analysis,
models), Rule-based text
Intent Detection,
generation.
Semantic Parsing.
Input: “Book a flight to
Example
New York tomorrow.”
Output: Intent =   Input: Structured data:
BookFlight,   {“City”: “New York”,
Destination = New “Weather”: “Sunny”,
York, Date =   “Temperature”:
Tomorrow.   “25°C”}
Output: “The
weather in New
York is sunny
today with a
temperature of
25°C.”
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
Ans:
Chunking-2M
Chinking 2M
POS Tagging role 1M
Sentence: “The black dog is running in the park.”
• Chunking: Groups words → [The black dog] (NP), [the park]
(NP).
• Chinking: Removes unwanted words → e.g., remove in
(preposition) from the chunk.
POS Tagging: Provides word categories (DT, JJ, NN, etc.), which are
used to apply chunking and chinking rules.
CO-4,   c.5   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
Ans:
(2+2+1) = 5 Marks
Hyponymy and Hypernymy
Hyponymy is a semantic relation in which the meaning of one word is
included in the meaning of another word.
Example: rose, tulip, and lily are hyponyms of flower.
The statement can be expressed as: “A rose is a kind of flower.”
Hypernymy is the opposite relation: it refers to the more general word
whose meaning includes that of more specific words.
********** 2 **********
--- page 3 ---
Example: flower is a hypernym of rose, tulip, and lily.
Similarly, animal is a hypernym of dog, cat, and elephant.
Application of Hypernymy in Word Sense Disambiguation (WSD)
Hypernymy relations are very useful in WSD because they allow a system
to connect ambiguous words to their broader, more general categories. By
checking the surrounding context and mapping it to the correct hypernym,
a system can choose the right sense of a word.
Example: Consider the polysemous word “bank.”
Sense 1: financial institution (hypernym = organization)
Sense 2: river bank (hypernym = geographical feature / landform)
If the sentence is:
“The boy was fishing on the bank.”
Words like fishing and river in the context point towards the hypernym
geographical feature.
Therefore, bank here means river bank.
“She deposited money in the bank.”
Context words like money and deposit map to the hypernym organization.
Therefore, bank here means financial institution.
In WSD, hypernymy helps map ambiguous words to their general category,
and then context determines which sense is correct.
CO-3;   d. 6   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3   Ans: Marks Distribution-3 Marks for Comparison and 2 Marks for
Example of each type
Pragmatics concentrates on speaker intention and context-dependent meaning,
whereas discourse analysis investigates how sentences and utterances are
connected to form coherent texts and conversations. Together, they provide a
comprehensive   understanding   of how language   functions   in   real
communication.
Pragmatics is the branch of linguistics that studies how meaning is shaped by
context of use. It goes beyond the literal semantic meaning of words and
focuses on how speakers use language to achieve communicative goals.
Example “Can you pass the salt?” — pragmatically, this is not a question about
ability but a request.
Discourse analysis studies how sentences and utterances are connected to
form larger units of meaning such as conversations, narratives, or written
texts.   It   is concerned with cohesion (linguistic ties like reference,
substitution, conjunctions) and coherence (logical flow of ideas in context).
Example :“I bought a book yesterday. The book was about artificial
intelligence.”
********** 3 **********
--- page 4 ---
→ The second sentence refers back to “a book” using “the book,” creating
textual cohesion.
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;
SO-1;   ii.   Discuss the significance of NER in three different NLP
BL-2,3   applications.
Ans:
Ans: [Marks 5+5]
i.
Feature   Morpheme   Lexeme
Meaning The smallest grammatical The basic unit of lexical
unit in a language that   meaning — represents a set
carries meaning.   of related word forms.
Function Deals with word structure Deals with word meaning
(morphology).   and usage in the lexicon.
Example   Morpheme   Lexeme
Unhappi   Has three morphemes:   The lexeme is HAPPY,
ness   “un-” (prefix), “happy”   which can appear as happy,
(root), “-ness” (suffix).   happier, happiest.
Running   Has two morphemes:   The lexeme is RUN, which
“run” + “-ing”.   includes run, runs, ran,
running.
ii.
1. Information Extraction (IE)
Automatically extracts structured information (names, dates,
locations, organizations) from unstructured text such as news
articles, reports, or legal documents.
2. Question Answering Systems (QA)
Helps identify entities in questions and documents (e.g., “Who is
the   CEO of Tesla?” → CEO = role, Tesla = organization).
3. Machine Translation
Ensures named entities like “Barack Obama” or “New Delhi”
are   translated correctly or kept unchanged.
4. Healthcare & Biomedical Text Mining
Extracts entities such as patient names, diseases, medications,
genes, or proteins from medical records and research papers.
5. Customer Feedback & Social Media Analysis
Identifies product names, brands, locations, or events in tweets,
reviews, and online discussions for business intelligence.
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
********** 4 **********
--- page 5 ---
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
Assume the <s> and </s> for each sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> artists paint murals in city </s>
<s> musicians play songs in city </s>
<s> painters paint murals on walls </s>
<s> signs are near city </s>
Test sentence-
<s> artists paint murals near city </s>
Distinct tokens are:
<s>, </s>, artists, paint, murals, in, city, musicians, play, songs,
painters, on, walls, signs, are, near
That gives V=16.
Counts:
• Unigram counts:
o C(artists)=1
o C(paint)=2
o C(murals)=2
o C(near)=1
o C(city)=3
o C(<s>)=4
• Bigram counts:
o C(<s>,artists)=1
o C(artists,paint)=1
o C(paint,murals)=2
o C(murals,near)=0
o C(near,city)=1
o C(city,</s>)=3
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(artists∣<s>)=[1+1]/[4+16]=2/20=1/10≈0.1
2. P(paint∣artists)=[1+1]/[1+16]=2/17≈0.117647
3. P(murals∣paint)=[2+1]/[2+16]=3/18=1/6≈0.166667
4. P(near∣murals)=[0+1]/[2+16]=1/18≈0.0555556
5. P(city∣near)=[1+1]/[1+16]=2/17≈0.117647
6. P(</s>∣city)=[3+1]/[3+16]=4/19≈0.210526
Exact fraction:
P+1=1/10*2/17*1/6*1/18*2/17*4/19=16/5930280=2.698E-6
Hence, the probability of the test sentence is =2.698E-6.
********** 5 **********
--- page 6 ---
Q3   a   i.   Explain the various types of ambiguities encountered in Natural [10]
CO- 3,   Language Processing (NLP). Illustrate each type with suitable
SO-, BL-   examples.
ii.   Compare top-down and bottom-up parsing and apply bottom-up
4
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-
“A cat chased the mouse”
Grammar   Lexicon
S → NP VP   Det → {A, the}
NP → Pronoun   Noun → {cat, mouse}
NP → Proper-Noun   Verb → {chased}
NP → Det Nominal
Nominal → Noun
Nominal → Nominal Noun
Nominal → Nominal PP
VP → Verb
VP → Verb NP
VP → VP PP
PP → Prep NP
Ans: Marks-5
1. Lexical Ambiguity:
Meaning:
Occurs when a word has multiple possible meanings.
Example:
He went to the bank.
• “bank” can mean a financial institution or the side of a river.
Explanation:
NLP systems must use context to decide which meaning of “bank”
applies in the sentence.
2. Syntactic Ambiguity (Structural Ambiguity)
Meaning:
Occurs when a sentence can be parsed in more than one way due to
different grammatical structures.
Example:
I saw the man with the telescope.
•   Interpretation 1: I used the telescope to see the man.
•   Interpretation 2: The man had the telescope.
Explanation:
The ambiguity arises because the prepositional phrase (“with the
telescope”) can modify either the verb saw or the noun man.
3. Semantic Ambiguity
Meaning:
Occurs when the meaning of the sentence itself is unclear, even if the
structure is fine.
Example:
Visiting relatives can be boring.
********** 6 **********
--- page 7 ---
•   Interpretation 1: The act of visiting relatives is boring.
•   Interpretation 2: The relatives who visit are boring.
Explanation:
The confusion comes from whether visiting is used as a gerund (verb)
or adjective (modifier).
4. Pragmatic Ambiguity
Meaning:
Arises when the intended meaning depends on context or speaker’s
intention rather than grammar or word meaning.
Example:
Can you pass the salt?
•   Literally, it’s a question about ability.
•   Pragmatically, it’s a request for action.
Explanation:
Understanding pragmatic meaning requires world knowledge and
context.
5. Referential Ambiguity
Meaning:
Occurs when a pronoun or reference word could refer to multiple
entities.
Example:
John told Tom that he was late.
• “he” could refer to John or Tom.
Explanation:
The ambiguity arises in anaphora (reference resolution).
ii.
Comparison (Any two relevant points-2M)
Aspect   Top-Down Parsing   Bottom-Up Parsing
Starts from the root (start   Starts from input tokens
Parsing   symbol) and expands   and reduces toward the
Direction   toward the input.   root.
Expands non-terminals
using grammar rules,   Combines tokens/phrases
Grammar Rule   even before seeing if   only if they appear in the
Application   input matches.   input.
Fails or loops infinitely
Handling Left   if grammar has left   Naturally handles left
Recursion   recursion.   recursion without issues.
May get stuck or need   Can face shift-reduce or
Ambiguity   backtracking when   reduce-reduce conflicts in
Handling   grammar is ambiguous.   ambiguous grammars.
Ease of   Conceptually simple and More complex (needs
Implementation   intuitive to implement.   parsing tables, stacks).
Bottom up parsing with steps-3
********** 7 **********
--- page 8 ---
Godors wp awry ti

‘ vos Hy )
=— : ver
a Nowr vub \ cbt
\ che ome Pet
; nan
_ Norin® wee
\ % *
Oe one ‘i ete atase
kb
zeus avid Mar Rs arte)
Ng NP
aearel worn
aie wee vib DE “
y 2
stop bak rik yin?” “nr 1°
NP
~~
4 J
My ye Nomint
7 ; / degee
ve
al var mone

“ unr Chock 1

Shp © form cunUR tt)

62 NY Ny

Coton we “nt IM Fina

“A Cok chuck ue we
= a

‘Se:

ok che TN Monee

FIC QF EH 1
--- page 9 ---
CO-3;   b   Consider the given paragraph given below:   [10]
SO- 1   The teacher wrote on the board. The students listened to the teacher.
BL-4:   The board was full of notes. The student asked a question. The
teacher answered from the book.
Target words: teacher, student, board, book
Context words: wrote, listened, notes, question
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.
Plot the target word vectors by considering only two dimensions: “wrote”
and “notes”.
Ans: [Marks 5+5]
Co-occurrence matrix:
target \ context   wrote   listened   notes
teacher   1   1   0
student   0   1   0
board   1   0   1
book   0   0   0
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2   Ans:[Marks-5+5]
It is an essential step in natural language processing (NLP) that involves
cleaning and transforming unstructured text data to prepare it for analysis.
Text data contains noise in various forms like emoticons, punctuations, text in
a different cases, HTML tags etc.
********** 9 **********
--- page 10 ---
Inadequate or low-quality data can lead to lower accuracy and effectiveness of
the model.
The pre-processing steps for a problem depend mainly on the domain and the
problem itself, hence, we don’t need to apply all steps to every problem and
also the order of applying these steps may also vary.
Various text preprocessing steps are widely used for dimensionality reduction.
Some of the commonly used preprocessing steps are:
o Removing punctuations like . , ! $( ) * % @, URLs, Stop
words
o Lower casing
o Normalization (some common ones)
▪   Tokenization
▪ Stemming
▪ Lemmatization
Stop word removal:
• Stop words are a set of commonly used words in a language like “a”,
“the”, “is”, “are” etc. in English.
• These words do not carry important meaning and are removed from
texts in many data science tasks.
• The intuition behind this approach is that, by removing low
information words from text, we can focus on the important words
instead.
• One of the advantages of removing stop words is that it can reduce the
size of the dataset, which in turn reduces the training time required for
building natural language processing models.
• Stop word removal is commonly applied in search systems, text
classification applications, topic modeling, topic extraction and others.
• Stop word lists can come from pre-established sets or you can create a
custom one for your domain. This creation may be tricky as few words
that may not be useful in some problem statement may be important in
others.
Lower casing:
•   Usually, this is the first step that is performed while pre-processing.
•   Is a text preprocessing step where all letters in the text are converted
to lowercase.
•   This step is implemented so that the algorithm does not treat the same
words differently in different situations.
o Ex: Book and book mean the same but when not converted to
the lower case those two are represented as two different
words in the vector space model (resulting in more
dimensions).
• However, it is important to remember that some words, like “US” and
“us”, can change meanings when reduced to the lower case. Also,
there can be cases where the capitalization is important and has to be
preserved. So we should avoid performing this step in such cases
Normalization:
• As raw text data is random, each word has a lot of variations in the form of
tenses, superlatives, and many more.
********** 10 **********
--- page 11 ---
• These variations increase the complexity of the data and are difficult for the
machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data into a
predefined standard, hence improving the efficiency of the model.
• Ex: Many forms of the base word collect - "collection", "collective", and
"collectively".
•   If we reduce the variations of a word in the raw text, there will be fewer
input variables for our machine-learning model to deal with, thus increasing
efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for structures
like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Few common ones used are:
• Removal of duplicate whitespaces and punctuation.
• Accent removal (if your data includes diacritical marks from ‘foreign’
languages).
•   Substitution of contractions (Ex: ‘I’m ’→‘I am’ and don’t to do not).
• Transform word numerals into numbers (Ex: ‘twenty three’→‘23’).
•   Substitution of values for their type (Ex: ‘$50’→‘MONEY’).
• Acronym normalization (Ex: ‘US ’→‘United States’/‘U.S.A’) and
abbreviation normalization (Ex: ‘btw’ → ‘by the way’).
• Normalize date formats, social security numbers or other data that have a
standard format.
•   Spell correction (one could say that a word can be misspelled infinite
ways, so spell corrections reduce the vocabulary variation by “correcting”)
•   Substitution of rare words for more common synonyms.
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
Noun   Verb   Noun
BL-4
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Ans:
********** 11 **********
--- page 12 ---
Q5   a   For the following two sentences:   [10]
• Sentence A: “The student read a science book in the library”
• Sentence B: “The teacher read a history book in the classroom”
********** 12 **********
--- page 13 ---
CO-2;   1. Construct the TF-IDF matrix for these sentences after removing
SO-1 ;   the stop words {The, a, in}.
BL-3;   2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
Ans:[Marks 5+5]
Term   Sentence   Sentence
A   B
student   0.693   0
read   0   0
science   0.693   0
book   0   0
library   0.693   0
teacher   0   0.693
history   0   0.693
classroo   0   0.693
m
Analysis:
For Sentence A, the unique theme is student, science, library.
For Sentence B, the unique theme is teacher, history, classroom.
So, it indicates that TF–IDF clearly shows that shared words don’t matter for
separation, while unique words carry more importance.
CO-4;   b   Consider the sentence: “The bat hit the ball hard on the cricket field.”   [10]
SO-1BL-   Two possible senses of “bat”:
4
• Sense 1: Bat (Sports equipment – cricket/baseball)
• Sense 2: Bat (Nocturnal flying mammal)
Sentence
Context Words   Sense (Class)
ID
ball, cricket, score,   Sports (Bat =
1
stadium   equipment)
Animal (Bat =
2   night, cave, wings, fly
mammal)
3   player, run, match, bat   Sports
4   nocturnal, vampire, insect Animal
5   team, field, bowl, bat   Sports
6   dark, flying, cave, night   Animal
a) Using the Naïve Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naïve Bayes
Classification.
Ans:
********** 13 **********
--- page 14 ---
P(Sports)=0.5
1 mk
P(Animal)=0.5
Unique words across both classes: (words: ball, cricket, score, stadium,
player, run, match, bat, team, field, bowl, night, cave, wings, fly,
nocturnal, vampire, insect, dark, flying) Total 20
1
mk
Calculations:
For Sports:
2 mks
• P(hit∣S)=(0+1)/32=1/32=0.03125
• P(ball∣S)=(1+1)/32=2/32=0.0625
• P(cricket∣S)=2/32=0.0625
• P(field∣S)=2/32=0.0625
• P(hard∣S)=1/32=0.03125
For Animal:
P(w∣A)=1/31≈0.03225806
Likelihood for sports:
2 mks
0.5 * 0.03125*0.0625*0.0625*0.0625*0.03125 =1.19209290×10-7
Likelihood for animal :
1.74647163×10-8
Classified sense: Sports equipment
1 mk
Laplace Smoothing:
3 mks
Handles problem of zero probabilities, improves robustness of
classifier.
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate
how it predicts the target word from its surrounding context
Ans:
********** 14 **********
--- page 15 ---
iii.   Marks Distribution-3 Marks for approach explanation and 2
Marks for advantage of each type
Co-reference resolution: task of finding all expressions in text that refer to
the same entity. (1.5 marks)
Example: Mary said Mary is tired. She went home. → "Mary" and "She" co-
refer.
Pronoun resolution: a subtask focusing only on resolving pronouns to their
antecedents. (1.5 marks)
Example: John met Peter when he was leaving. → "he" could refer to John or
Peter.
Difference: co-reference is broader (includes noun phrases, names, definite
descriptions), while pronoun resolution is narrower.
In Word2Vec, two main architectures are used to learn word
embeddings:
Continuous Bag of Words (CBOW) and
Skip-Gram.
Both are neural network-based models that learn to represent words as
dense vectors based on their context in a text corpus.
1. Continuous Bag of Words (CBOW) Model
Working Principle:
The CBOW model predicts the target word from its surrounding
context words.
It takes context words as input and tries to predict the central
(target) word.
The model averages (or sums) the vectors of the context words and
passes them through a neural network to predict the target word.
Example:-Sentence
“The cat sat on the mat”
If the window size = 2, and the target word is “sat”, then the context
words are:
["The", "cat", "on", "the"]
The CBOW model learns:
P(sat | The, cat, on, the)
Intuition:
It focuses on understanding the meaning of a word based on its
surrounding words.
2. Skip-Gram Model
Working Principle:
• The Skip-Gram model does the reverse of CBOW.
•   It predicts the context words given a target word.
• The target word is input, and the model learns to predict
surrounding context words.
Example:-Sentence:
“The cat sat on the mat”
If the target word is “sat” and window size = 2, then the context
words are:
["The", "cat", "on", "the"]
********** 15 **********
--- page 16 ---
The Skip-Gram model learns:
P(The | sat), P(cat | sat), P(on | sat), P(the | sat)
Intuition:
It focuses on how a single word relates to its neighboring words.
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Ans: Marks Distribution-5 Marks for approach explanation and 5 Marks
for resolution
i
Hobbs’ Algorithm is a syntactic algorithm for pronoun resolution in NLP.
It identifies possible antecedents for a pronoun by traversing a syntactic parse
tree in a systematic manner.
Example:
Sentence: “When Mary saw Alice, she waved.”
• Pronoun = she
• Step 1: Start at NP dominating “she.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs = “Mary,” “Alice.”
• Step 4: First candidate = Mary, chosen as antecedent.
Limitations :
Struggles with ambiguous cases (gender/number mismatch ignored).
Not efficient for long, complex sentences.
ii Sentence: “Ravi met Suresh at the station after he arrived from
Delhi.”
Pronoun: he
Steps of traversal:
1. Start at NP for “he.”
2. Move up to nearest S node.
3. Traverse left branches → encounter NPs: Ravi, Suresh.
4. Candidate 1 = Ravi, Candidate 2 = Suresh.
5. According to Hobbs’ order: Ravi is encountered first.
Hobbs’ algorithm chooses Ravi as antecedent of “he.”
But semantically, “Suresh” may also make sense depending on context
→ shows limitation of Hobbs.
Q7   a   Explain the working of text classification in Natural Language Processing [10]
(NLP) and discuss the key steps involved in building a text classification
********** 16 **********
--- page 17 ---
CO-4;   system in context of real-world applications such as spam detection or
SO-1 BL-   news categorization.
3:   Ans:
Text classification is the process of automatically assigning categories or
labels to text data based on its content.
Examples include:
Spam filtering – Classifying emails as “spam” or “not spam.”
News categorization – Grouping news articles into topics like sports,
politics, or entertainment.
Sentiment analysis – Identifying whether a review or comment is
positive, negative, or neutral.
Steps Involved in Text Classification
1. Data Collection
Gather a dataset containing text documents and their corresponding labels.
• Example: A set of emails labeled as “spam” or “ham” (not spam).
2. Data Preprocessing
Prepare the text for analysis by cleaning and normalizing it. Common steps
include:
• Lowercasing – Convert all text to lowercase.
• Removing noise – Punctuation, special characters, HTML tags, etc.
•   Tokenization – Splitting text into individual words or tokens.
•   Stop word removal – Removing common words like “the,” “is,”
“and.”
• Stemming/Lemmatization – Reducing words to their base or root form
(e.g., “running” → “run”).
3. Feature Extraction / Text Representation
Convert the cleaned text into a numerical format that a machine learning
model can understand. Common methods:
• Bag of Words (BoW) – Counts the occurrence of each word in the
document.
• TF-IDF (Term Frequency–Inverse Document Frequency) – Weighs
words based on their importance.
• Word Embeddings (e.g., Word2Vec, GloVe) – Captures semantic
meaning of words in vector form.
•   Transformer-based embeddings (e.g., BERT) – Context-aware
representations of text.
4. Model Training
Train a classification algorithm using the numerical features and their labels.
Examples of models:
•   Traditional ML: Naive Bayes, Logistic Regression, SVM.
• Deep Learning: RNNs, CNNs for text, Transformers (e.g., BERT).
5. Model Evaluation
Evaluate the trained model using metrics such as:
• Accuracy – Overall correctness.
•   Precision & Recall – Useful for imbalanced datasets (e.g., spam
detection).
•   F1-score – Balance between precision and recall.
6. Prediction / Deployment
********** 17 **********
--- page 18 ---
Use the trained model to classify new, unseen text data.
Example: A new email arrives → model predicts “spam” or “not spam” →
automatically sorted into the correct folder.
7. Monitoring and Updating
Over time, new words and patterns emerge. The model should be regularly
retrained with updated data to maintain accuracy.
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
Ans: [Marks 5+5]
i. Different corpus structures are applied to different NLP tasks
depending on the information they provide:
Flat Text Corpus (e.g., plain .txt files):
This type contains only raw text without labels. It can be applied to tasks
like word frequency analysis, calculating readability scores, or
comparing the styles of different writers. For example, one can apply it
to study the most common words in political speeches.
Annotated Corpus (e.g., POS-tagged or parsed text):
This type contains extra linguistic information such as part-of-speech
tags, named entities, or syntactic structures. It can be applied in
supervised learning tasks such as training a Part-of-Speech tagger,
Named Entity Recognition, or parsing models. For instance, a POS-
tagged corpus can be used to train a model that automatically identifies
nouns and verbs in new texts.
ii. Jaccard similarity takes into account only the set of unique words
for each text document. This makes it the likely candidate for
assessing the similarity of documents when repetition is not an issue.
Both Euclidean and cosine similarity metrics drop if an additional
word is added to the list.
Jaccard similarity is limited to assessing the lexical similarity of text,
i.e., how similar documents are on a word level.
The differentiating factor between Euclidean and Cosine measure is
that cosine similarity is not affected by the magnitude/length of the
feature vectors. It only considers the angle between them, making it
ideal for comparing vectors of different lengths. (Ex: If a word
‘senate’ occurs more frequently in doc 1 than it does in doc 2, we
could assume that doc 1 is more related to the topic of Politics.
However, it could also be the case that we are working with news
articles of different lengths and word ‘senate’ probably occurred more
in doc 1 simply because it was way longer)
Ex:
********** 18 **********
--- page 19 ---
Doc 1: “I love data science and machine learning”
Doc 2: “I love machine learning”
Step 1: Preprocess the documents - Remove stopwords like “I”, “and”,
etc., and lowercase everything.
Doc 1 → ['love', 'data', 'science', 'machine', 'learning’]
Doc 2 → ['love', 'machine', 'learning’]
Vocabulary :['love', 'data', 'science', 'machine', 'learning']
Jaccard
Intersection: ['love', 'machine', 'learning'] → 3 words
Union: ['love', 'data', 'science', 'machine', 'learning'] → 5 words
Jaccard=3/5=0.6
Cosine
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Dot product = 1∗1+1∗0+1∗0+1∗1+1∗1=31∗1+1∗0+1∗0+1∗1+1∗1=3
|A| = √(1²+1²+1²+1²+1²) = √5 ≈ 2.236
|B| = √(1²+0²+0²+1²+1²) = √3 ≈ 1.732
cos(θ)= 3/(2.236×1.7323) ≈ 3/3.8723 ≈0.775
Euclidean:
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Distance=Sqrt((1−1)2+(1−0)2+(1−0)2+(1−1)2+(1−1)2 )
Distance= ≈1.414
Measure   Value   Meaning
Jaccard   0.6   60% of the words overlap
Cosine   0.775   High similarity in word pattern
Euclidean   1.414   Some difference in word presence
In short, flat corpora are applied to simpler, surface-level analysis, while
annotated corpora are applied to more advanced supervised NLP tasks.
********** 19 **********
--- page 20 ---
Synoptic Answer for Q 3 b iii.
There are two correct ways of plotting the answer.
Regarding marks distribution:
part (i): 4 M
part (ii): 3 M
part (iii): 3 M
Total (10 M)
Q5 a) Formula to calculate TF and IDF
Here doc A refer Sentence A and doc B refer Sentence B
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 117d60339db1

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: mixed (19 pages), mean OCR confidence 36.4
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 02 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.1   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples.
BL-2;   Ans:
Natural Language   Natural Language
Aspect
Understanding (NLU)   Generation (NLG)
NLU is the ability of a NLG is the ability of a
machine to   machine to generate
comprehend and   human-like language (text
Definition
interpret human   or speech) from structured
language in a   data or internal
meaningful way.   representations.
To understand the
To produce coherent and
Purpose   meaning of the input
meaningful text as output.
text.
Structured data, machine-
Human-readable text or
Input   readable content, or
speech.
semantic representation.
Semantic
understanding, intents, Human-readable text,
Output   entities, sentiment, or   sentences, paragraphs, or
meaning   conversational responses.
representation.
********** 1 **********
--- page 2 ---
Named Entity
Template-based generation,
Recognition (NER),
Neural Networks (like GPT
Techniques Used Sentiment Analysis,
models), Rule-based text
Intent Detection,
generation.
Semantic Parsing.
Input: “Book a flight to
Example
New York tomorrow.”
Output: Intent =   Input: Structured data:
BookFlight,   {“City”: “New York”,
Destination = New “Weather”: “Sunny”,
York, Date =   “Temperature”:
Tomorrow.   “25°C”}
Output: “The
weather in New
York is sunny
today with a
temperature of
25°C.”
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
Ans:
Chunking-2M
Chinking 2M
POS Tagging role 1M
Sentence: “The black dog is running in the park.”
• Chunking: Groups words → [The black dog] (NP), [the park]
(NP).
• Chinking: Removes unwanted words → e.g., remove in
(preposition) from the chunk.
POS Tagging: Provides word categories (DT, JJ, NN, etc.), which are
used to apply chunking and chinking rules.
CO-4,   c.5   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
Ans:
(2+2+1) = 5 Marks
Hyponymy and Hypernymy
Hyponymy is a semantic relation in which the meaning of one word is
included in the meaning of another word.
Example: rose, tulip, and lily are hyponyms of flower.
The statement can be expressed as: “A rose is a kind of flower.”
Hypernymy is the opposite relation: it refers to the more general word
whose meaning includes that of more specific words.
********** 2 **********
--- page 3 ---
Example: flower is a hypernym of rose, tulip, and lily.
Similarly, animal is a hypernym of dog, cat, and elephant.
Application of Hypernymy in Word Sense Disambiguation (WSD)
Hypernymy relations are very useful in WSD because they allow a system
to connect ambiguous words to their broader, more general categories. By
checking the surrounding context and mapping it to the correct hypernym,
a system can choose the right sense of a word.
Example: Consider the polysemous word “bank.”
Sense 1: financial institution (hypernym = organization)
Sense 2: river bank (hypernym = geographical feature / landform)
If the sentence is:
“The boy was fishing on the bank.”
Words like fishing and river in the context point towards the hypernym
geographical feature.
Therefore, bank here means river bank.
“She deposited money in the bank.”
Context words like money and deposit map to the hypernym organization.
Therefore, bank here means financial institution.
In WSD, hypernymy helps map ambiguous words to their general category,
and then context determines which sense is correct.
CO-3;   d. 6   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3   Ans: Marks Distribution-3 Marks for Comparison and 2 Marks for
Example of each type
Pragmatics concentrates on speaker intention and context-dependent meaning,
whereas discourse analysis investigates how sentences and utterances are
connected to form coherent texts and conversations. Together, they provide a
comprehensive   understanding   of how language   functions   in   real
communication.
Pragmatics is the branch of linguistics that studies how meaning is shaped by
context of use. It goes beyond the literal semantic meaning of words and
focuses on how speakers use language to achieve communicative goals.
Example “Can you pass the salt?” — pragmatically, this is not a question about
ability but a request.
Discourse analysis studies how sentences and utterances are connected to
form larger units of meaning such as conversations, narratives, or written
texts.   It   is concerned with cohesion (linguistic ties like reference,
substitution, conjunctions) and coherence (logical flow of ideas in context).
Example :“I bought a book yesterday. The book was about artificial
intelligence.”
********** 3 **********
--- page 4 ---
→ The second sentence refers back to “a book” using “the book,” creating
textual cohesion.
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;
SO-1;   ii.   Discuss the significance of NER in three different NLP
BL-2,3   applications.
Ans:
Ans: [Marks 5+5]
i.
Feature   Morpheme   Lexeme
Meaning The smallest grammatical The basic unit of lexical
unit in a language that   meaning — represents a set
carries meaning.   of related word forms.
Function Deals with word structure Deals with word meaning
(morphology).   and usage in the lexicon.
Example   Morpheme   Lexeme
Unhappi   Has three morphemes:   The lexeme is HAPPY,
ness   “un-” (prefix), “happy”   which can appear as happy,
(root), “-ness” (suffix).   happier, happiest.
Running   Has two morphemes:   The lexeme is RUN, which
“run” + “-ing”.   includes run, runs, ran,
running.
ii.
1. Information Extraction (IE)
Automatically extracts structured information (names, dates,
locations, organizations) from unstructured text such as news
articles, reports, or legal documents.
2. Question Answering Systems (QA)
Helps identify entities in questions and documents (e.g., “Who is
the   CEO of Tesla?” → CEO = role, Tesla = organization).
3. Machine Translation
Ensures named entities like “Barack Obama” or “New Delhi”
are   translated correctly or kept unchanged.
4. Healthcare & Biomedical Text Mining
Extracts entities such as patient names, diseases, medications,
genes, or proteins from medical records and research papers.
5. Customer Feedback & Social Media Analysis
Identifies product names, brands, locations, or events in tweets,
reviews, and online discussions for business intelligence.
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
********** 4 **********
--- page 5 ---
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
Assume the <s> and </s> for each sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> artists paint murals in city </s>
<s> musicians play songs in city </s>
<s> painters paint murals on walls </s>
<s> signs are near city </s>
Test sentence-
<s> artists paint murals near city </s>
Distinct tokens are:
<s>, </s>, artists, paint, murals, in, city, musicians, play, songs,
painters, on, walls, signs, are, near
That gives V=16.
Counts:
• Unigram counts:
o C(artists)=1
o C(paint)=2
o C(murals)=2
o C(near)=1
o C(city)=3
o C(<s>)=4
• Bigram counts:
o C(<s>,artists)=1
o C(artists,paint)=1
o C(paint,murals)=2
o C(murals,near)=0
o C(near,city)=1
o C(city,</s>)=3
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(artists∣<s>)=[1+1]/[4+16]=2/20=1/10≈0.1
2. P(paint∣artists)=[1+1]/[1+16]=2/17≈0.117647
3. P(murals∣paint)=[2+1]/[2+16]=3/18=1/6≈0.166667
4. P(near∣murals)=[0+1]/[2+16]=1/18≈0.0555556
5. P(city∣near)=[1+1]/[1+16]=2/17≈0.117647
6. P(</s>∣city)=[3+1]/[3+16]=4/19≈0.210526
Exact fraction:
P+1=1/10*2/17*1/6*1/18*2/17*4/19=16/5930280=2.698E-6
Hence, the probability of the test sentence is =2.698E-6.
********** 5 **********
--- page 6 ---
Q3   a   i.   Explain the various types of ambiguities encountered in Natural [10]
CO- 3,   Language Processing (NLP). Illustrate each type with suitable
SO-, BL-   examples.
ii.   Compare top-down and bottom-up parsing and apply bottom-up
4
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-
“A cat chased the mouse”
Grammar   Lexicon
S → NP VP   Det → {A, the}
NP → Pronoun   Noun → {cat, mouse}
NP → Proper-Noun   Verb → {chased}
NP → Det Nominal
Nominal → Noun
Nominal → Nominal Noun
Nominal → Nominal PP
VP → Verb
VP → Verb NP
VP → VP PP
PP → Prep NP
Ans: Marks-5
1. Lexical Ambiguity:
Meaning:
Occurs when a word has multiple possible meanings.
Example:
He went to the bank.
• “bank” can mean a financial institution or the side of a river.
Explanation:
NLP systems must use context to decide which meaning of “bank”
applies in the sentence.
2. Syntactic Ambiguity (Structural Ambiguity)
Meaning:
Occurs when a sentence can be parsed in more than one way due to
different grammatical structures.
Example:
I saw the man with the telescope.
•   Interpretation 1: I used the telescope to see the man.
•   Interpretation 2: The man had the telescope.
Explanation:
The ambiguity arises because the prepositional phrase (“with the
telescope”) can modify either the verb saw or the noun man.
3. Semantic Ambiguity
Meaning:
Occurs when the meaning of the sentence itself is unclear, even if the
structure is fine.
Example:
Visiting relatives can be boring.
********** 6 **********
--- page 7 ---
•   Interpretation 1: The act of visiting relatives is boring.
•   Interpretation 2: The relatives who visit are boring.
Explanation:
The confusion comes from whether visiting is used as a gerund (verb)
or adjective (modifier).
4. Pragmatic Ambiguity
Meaning:
Arises when the intended meaning depends on context or speaker’s
intention rather than grammar or word meaning.
Example:
Can you pass the salt?
•   Literally, it’s a question about ability.
•   Pragmatically, it’s a request for action.
Explanation:
Understanding pragmatic meaning requires world knowledge and
context.
5. Referential Ambiguity
Meaning:
Occurs when a pronoun or reference word could refer to multiple
entities.
Example:
John told Tom that he was late.
• “he” could refer to John or Tom.
Explanation:
The ambiguity arises in anaphora (reference resolution).
ii.
Comparison (Any two relevant points-2M)
Aspect   Top-Down Parsing   Bottom-Up Parsing
Starts from the root (start   Starts from input tokens
Parsing   symbol) and expands   and reduces toward the
Direction   toward the input.   root.
Expands non-terminals
using grammar rules,   Combines tokens/phrases
Grammar Rule   even before seeing if   only if they appear in the
Application   input matches.   input.
Fails or loops infinitely
Handling Left   if grammar has left   Naturally handles left
Recursion   recursion.   recursion without issues.
May get stuck or need   Can face shift-reduce or
Ambiguity   backtracking when   reduce-reduce conflicts in
Handling   grammar is ambiguous.   ambiguous grammars.
Ease of   Conceptually simple and More complex (needs
Implementation   intuitive to implement.   parsing tables, stacks).
Bottom up parsing with steps-3
********** 7 **********
--- page 8 ---
Godors wp awry ti

‘ vos Hy )
=— : ver
a Nowr vub \ cbt
\ che ome Pet
; nan
_ Norin® wee
\ % *
Oe one ‘i ete atase
kb
zeus avid Mar Rs arte)
Ng NP
aearel worn
aie wee vib DE “
y 2
stop bak rik yin?” “nr 1°
NP
~~
4 J
My ye Nomint
7 ; / degee
ve
al var mone

“ unr Chock 1

Shp © form cunUR tt)

62 NY Ny

Coton we “nt IM Fina

“A Cok chuck ue we
= a

‘Se:

ok che TN Monee

FIC QF EH 1
--- page 9 ---
CO-3;   b   Consider the given paragraph given below:   [10]
SO- 1   The teacher wrote on the board. The students listened to the teacher.
BL-4:   The board was full of notes. The student asked a question. The
teacher answered from the book.
Target words: teacher, student, board, book
Context words: wrote, listened, notes, question
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.
Plot the target word vectors by considering only two dimensions: “wrote”
and “notes”.
Ans: [Marks 5+5]
Co-occurrence matrix:
target \ context   wrote   listened   notes
teacher   1   1   0
student   0   1   0
board   1   0   1
book   0   0   0
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2   Ans:[Marks-5+5]
It is an essential step in natural language processing (NLP) that involves
cleaning and transforming unstructured text data to prepare it for analysis.
Text data contains noise in various forms like emoticons, punctuations, text in
a different cases, HTML tags etc.
********** 9 **********
--- page 10 ---
Inadequate or low-quality data can lead to lower accuracy and effectiveness of
the model.
The pre-processing steps for a problem depend mainly on the domain and the
problem itself, hence, we don’t need to apply all steps to every problem and
also the order of applying these steps may also vary.
Various text preprocessing steps are widely used for dimensionality reduction.
Some of the commonly used preprocessing steps are:
o Removing punctuations like . , ! $( ) * % @, URLs, Stop
words
o Lower casing
o Normalization (some common ones)
▪   Tokenization
▪ Stemming
▪ Lemmatization
Stop word removal:
• Stop words are a set of commonly used words in a language like “a”,
“the”, “is”, “are” etc. in English.
• These words do not carry important meaning and are removed from
texts in many data science tasks.
• The intuition behind this approach is that, by removing low
information words from text, we can focus on the important words
instead.
• One of the advantages of removing stop words is that it can reduce the
size of the dataset, which in turn reduces the training time required for
building natural language processing models.
• Stop word removal is commonly applied in search systems, text
classification applications, topic modeling, topic extraction and others.
• Stop word lists can come from pre-established sets or you can create a
custom one for your domain. This creation may be tricky as few words
that may not be useful in some problem statement may be important in
others.
Lower casing:
•   Usually, this is the first step that is performed while pre-processing.
•   Is a text preprocessing step where all letters in the text are converted
to lowercase.
•   This step is implemented so that the algorithm does not treat the same
words differently in different situations.
o Ex: Book and book mean the same but when not converted to
the lower case those two are represented as two different
words in the vector space model (resulting in more
dimensions).
• However, it is important to remember that some words, like “US” and
“us”, can change meanings when reduced to the lower case. Also,
there can be cases where the capitalization is important and has to be
preserved. So we should avoid performing this step in such cases
Normalization:
• As raw text data is random, each word has a lot of variations in the form of
tenses, superlatives, and many more.
********** 10 **********
--- page 11 ---
• These variations increase the complexity of the data and are difficult for the
machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data into a
predefined standard, hence improving the efficiency of the model.
• Ex: Many forms of the base word collect - "collection", "collective", and
"collectively".
•   If we reduce the variations of a word in the raw text, there will be fewer
input variables for our machine-learning model to deal with, thus increasing
efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for structures
like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Few common ones used are:
• Removal of duplicate whitespaces and punctuation.
• Accent removal (if your data includes diacritical marks from ‘foreign’
languages).
•   Substitution of contractions (Ex: ‘I’m ’→‘I am’ and don’t to do not).
• Transform word numerals into numbers (Ex: ‘twenty three’→‘23’).
•   Substitution of values for their type (Ex: ‘$50’→‘MONEY’).
• Acronym normalization (Ex: ‘US ’→‘United States’/‘U.S.A’) and
abbreviation normalization (Ex: ‘btw’ → ‘by the way’).
• Normalize date formats, social security numbers or other data that have a
standard format.
•   Spell correction (one could say that a word can be misspelled infinite
ways, so spell corrections reduce the vocabulary variation by “correcting”)
•   Substitution of rare words for more common synonyms.
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
Noun   Verb   Noun
BL-4
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Ans:
********** 11 **********
--- page 12 ---
Q5   a   For the following two sentences:   [10]
• Sentence A: “The student read a science book in the library”
• Sentence B: “The teacher read a history book in the classroom”
********** 12 **********
--- page 13 ---
CO-2;   1. Construct the TF-IDF matrix for these sentences after removing
SO-1 ;   the stop words {The, a, in}.
BL-3;   2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
Ans:[Marks 5+5]
Term   Sentence   Sentence
A   B
student   0.693   0
read   0   0
science   0.693   0
book   0   0
library   0.693   0
teacher   0   0.693
history   0   0.693
classroo   0   0.693
m
Analysis:
For Sentence A, the unique theme is student, science, library.
For Sentence B, the unique theme is teacher, history, classroom.
So, it indicates that TF–IDF clearly shows that shared words don’t matter for
separation, while unique words carry more importance.
CO-4;   b   Consider the sentence: “The bat hit the ball hard on the cricket field.”   [10]
SO-1BL-   Two possible senses of “bat”:
4
• Sense 1: Bat (Sports equipment – cricket/baseball)
• Sense 2: Bat (Nocturnal flying mammal)
Sentence
Context Words   Sense (Class)
ID
ball, cricket, score,   Sports (Bat =
1
stadium   equipment)
Animal (Bat =
2   night, cave, wings, fly
mammal)
3   player, run, match, bat   Sports
4   nocturnal, vampire, insect Animal
5   team, field, bowl, bat   Sports
6   dark, flying, cave, night   Animal
a) Using the Naïve Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naïve Bayes
Classification.
Ans:
********** 13 **********
--- page 14 ---
P(Sports)=0.5
1 mk
P(Animal)=0.5
Unique words across both classes: (words: ball, cricket, score, stadium,
player, run, match, bat, team, field, bowl, night, cave, wings, fly,
nocturnal, vampire, insect, dark, flying) Total 20
1
mk
Calculations:
For Sports:
2 mks
• P(hit∣S)=(0+1)/32=1/32=0.03125
• P(ball∣S)=(1+1)/32=2/32=0.0625
• P(cricket∣S)=2/32=0.0625
• P(field∣S)=2/32=0.0625
• P(hard∣S)=1/32=0.03125
For Animal:
P(w∣A)=1/31≈0.03225806
Likelihood for sports:
2 mks
0.5 * 0.03125*0.0625*0.0625*0.0625*0.03125 =1.19209290×10-7
Likelihood for animal :
1.74647163×10-8
Classified sense: Sports equipment
1 mk
Laplace Smoothing:
3 mks
Handles problem of zero probabilities, improves robustness of
classifier.
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate
how it predicts the target word from its surrounding context
Ans:
********** 14 **********
--- page 15 ---
iii.   Marks Distribution-3 Marks for approach explanation and 2
Marks for advantage of each type
Co-reference resolution: task of finding all expressions in text that refer to
the same entity. (1.5 marks)
Example: Mary said Mary is tired. She went home. → "Mary" and "She" co-
refer.
Pronoun resolution: a subtask focusing only on resolving pronouns to their
antecedents. (1.5 marks)
Example: John met Peter when he was leaving. → "he" could refer to John or
Peter.
Difference: co-reference is broader (includes noun phrases, names, definite
descriptions), while pronoun resolution is narrower.
In Word2Vec, two main architectures are used to learn word
embeddings:
Continuous Bag of Words (CBOW) and
Skip-Gram.
Both are neural network-based models that learn to represent words as
dense vectors based on their context in a text corpus.
1. Continuous Bag of Words (CBOW) Model
Working Principle:
The CBOW model predicts the target word from its surrounding
context words.
It takes context words as input and tries to predict the central
(target) word.
The model averages (or sums) the vectors of the context words and
passes them through a neural network to predict the target word.
Example:-Sentence
“The cat sat on the mat”
If the window size = 2, and the target word is “sat”, then the context
words are:
["The", "cat", "on", "the"]
The CBOW model learns:
P(sat | The, cat, on, the)
Intuition:
It focuses on understanding the meaning of a word based on its
surrounding words.
2. Skip-Gram Model
Working Principle:
• The Skip-Gram model does the reverse of CBOW.
•   It predicts the context words given a target word.
• The target word is input, and the model learns to predict
surrounding context words.
Example:-Sentence:
“The cat sat on the mat”
If the target word is “sat” and window size = 2, then the context
words are:
["The", "cat", "on", "the"]
********** 15 **********
--- page 16 ---
The Skip-Gram model learns:
P(The | sat), P(cat | sat), P(on | sat), P(the | sat)
Intuition:
It focuses on how a single word relates to its neighboring words.
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Ans: Marks Distribution-5 Marks for approach explanation and 5 Marks
for resolution
i
Hobbs’ Algorithm is a syntactic algorithm for pronoun resolution in NLP.
It identifies possible antecedents for a pronoun by traversing a syntactic parse
tree in a systematic manner.
Example:
Sentence: “When Mary saw Alice, she waved.”
• Pronoun = she
• Step 1: Start at NP dominating “she.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs = “Mary,” “Alice.”
• Step 4: First candidate = Mary, chosen as antecedent.
Limitations :
Struggles with ambiguous cases (gender/number mismatch ignored).
Not efficient for long, complex sentences.
ii Sentence: “Ravi met Suresh at the station after he arrived from
Delhi.”
Pronoun: he
Steps of traversal:
1. Start at NP for “he.”
2. Move up to nearest S node.
3. Traverse left branches → encounter NPs: Ravi, Suresh.
4. Candidate 1 = Ravi, Candidate 2 = Suresh.
5. According to Hobbs’ order: Ravi is encountered first.
Hobbs’ algorithm chooses Ravi as antecedent of “he.”
But semantically, “Suresh” may also make sense depending on context
→ shows limitation of Hobbs.
Q7   a   Explain the working of text classification in Natural Language Processing [10]
(NLP) and discuss the key steps involved in building a text classification
********** 16 **********
--- page 17 ---
CO-4;   system in context of real-world applications such as spam detection or
SO-1 BL-   news categorization.
3:   Ans:
Text classification is the process of automatically assigning categories or
labels to text data based on its content.
Examples include:
Spam filtering – Classifying emails as “spam” or “not spam.”
News categorization – Grouping news articles into topics like sports,
politics, or entertainment.
Sentiment analysis – Identifying whether a review or comment is
positive, negative, or neutral.
Steps Involved in Text Classification
1. Data Collection
Gather a dataset containing text documents and their corresponding labels.
• Example: A set of emails labeled as “spam” or “ham” (not spam).
2. Data Preprocessing
Prepare the text for analysis by cleaning and normalizing it. Common steps
include:
• Lowercasing – Convert all text to lowercase.
• Removing noise – Punctuation, special characters, HTML tags, etc.
•   Tokenization – Splitting text into individual words or tokens.
•   Stop word removal – Removing common words like “the,” “is,”
“and.”
• Stemming/Lemmatization – Reducing words to their base or root form
(e.g., “running” → “run”).
3. Feature Extraction / Text Representation
Convert the cleaned text into a numerical format that a machine learning
model can understand. Common methods:
• Bag of Words (BoW) – Counts the occurrence of each word in the
document.
• TF-IDF (Term Frequency–Inverse Document Frequency) – Weighs
words based on their importance.
• Word Embeddings (e.g., Word2Vec, GloVe) – Captures semantic
meaning of words in vector form.
•   Transformer-based embeddings (e.g., BERT) – Context-aware
representations of text.
4. Model Training
Train a classification algorithm using the numerical features and their labels.
Examples of models:
•   Traditional ML: Naive Bayes, Logistic Regression, SVM.
• Deep Learning: RNNs, CNNs for text, Transformers (e.g., BERT).
5. Model Evaluation
Evaluate the trained model using metrics such as:
• Accuracy – Overall correctness.
•   Precision & Recall – Useful for imbalanced datasets (e.g., spam
detection).
•   F1-score – Balance between precision and recall.
6. Prediction / Deployment
********** 17 **********
--- page 18 ---
Use the trained model to classify new, unseen text data.
Example: A new email arrives → model predicts “spam” or “not spam” →
automatically sorted into the correct folder.
7. Monitoring and Updating
Over time, new words and patterns emerge. The model should be regularly
retrained with updated data to maintain accuracy.
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
Ans: [Marks 5+5]
i. Different corpus structures are applied to different NLP tasks
depending on the information they provide:
Flat Text Corpus (e.g., plain .txt files):
This type contains only raw text without labels. It can be applied to tasks
like word frequency analysis, calculating readability scores, or
comparing the styles of different writers. For example, one can apply it
to study the most common words in political speeches.
Annotated Corpus (e.g., POS-tagged or parsed text):
This type contains extra linguistic information such as part-of-speech
tags, named entities, or syntactic structures. It can be applied in
supervised learning tasks such as training a Part-of-Speech tagger,
Named Entity Recognition, or parsing models. For instance, a POS-
tagged corpus can be used to train a model that automatically identifies
nouns and verbs in new texts.
ii. Jaccard similarity takes into account only the set of unique words
for each text document. This makes it the likely candidate for
assessing the similarity of documents when repetition is not an issue.
Both Euclidean and cosine similarity metrics drop if an additional
word is added to the list.
Jaccard similarity is limited to assessing the lexical similarity of text,
i.e., how similar documents are on a word level.
The differentiating factor between Euclidean and Cosine measure is
that cosine similarity is not affected by the magnitude/length of the
feature vectors. It only considers the angle between them, making it
ideal for comparing vectors of different lengths. (Ex: If a word
‘senate’ occurs more frequently in doc 1 than it does in doc 2, we
could assume that doc 1 is more related to the topic of Politics.
However, it could also be the case that we are working with news
articles of different lengths and word ‘senate’ probably occurred more
in doc 1 simply because it was way longer)
Ex:
********** 18 **********
--- page 19 ---
Doc 1: “I love data science and machine learning”
Doc 2: “I love machine learning”
Step 1: Preprocess the documents - Remove stopwords like “I”, “and”,
etc., and lowercase everything.
Doc 1 → ['love', 'data', 'science', 'machine', 'learning’]
Doc 2 → ['love', 'machine', 'learning’]
Vocabulary :['love', 'data', 'science', 'machine', 'learning']
Jaccard
Intersection: ['love', 'machine', 'learning'] → 3 words
Union: ['love', 'data', 'science', 'machine', 'learning'] → 5 words
Jaccard=3/5=0.6
Cosine
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Dot product = 1∗1+1∗0+1∗0+1∗1+1∗1=31∗1+1∗0+1∗0+1∗1+1∗1=3
|A| = √(1²+1²+1²+1²+1²) = √5 ≈ 2.236
|B| = √(1²+0²+0²+1²+1²) = √3 ≈ 1.732
cos(θ)= 3/(2.236×1.7323) ≈ 3/3.8723 ≈0.775
Euclidean:
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Distance=Sqrt((1−1)2+(1−0)2+(1−0)2+(1−1)2+(1−1)2 )
Distance= ≈1.414
Measure   Value   Meaning
Jaccard   0.6   60% of the words overlap
Cosine   0.775   High similarity in word pattern
Euclidean   1.414   Some difference in word presence
In short, flat corpora are applied to simpler, surface-level analysis, while
annotated corpora are applied to more advanced supervised NLP tasks.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 80835e1bcef4

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CS_7055/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: mixed (19 pages), mean OCR confidence 36.4
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 02 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.1   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples.
BL-2;   Ans:
Natural Language   Natural Language
Aspect
Understanding (NLU)   Generation (NLG)
NLU is the ability of a NLG is the ability of a
machine to   machine to generate
comprehend and   human-like language (text
Definition
interpret human   or speech) from structured
language in a   data or internal
meaningful way.   representations.
To understand the
To produce coherent and
Purpose   meaning of the input
meaningful text as output.
text.
Structured data, machine-
Human-readable text or
Input   readable content, or
speech.
semantic representation.
Semantic
understanding, intents, Human-readable text,
Output   entities, sentiment, or   sentences, paragraphs, or
meaning   conversational responses.
representation.
********** 1 **********
--- page 2 ---
Named Entity
Template-based generation,
Recognition (NER),
Neural Networks (like GPT
Techniques Used Sentiment Analysis,
models), Rule-based text
Intent Detection,
generation.
Semantic Parsing.
Input: “Book a flight to
Example
New York tomorrow.”
Output: Intent =   Input: Structured data:
BookFlight,   {“City”: “New York”,
Destination = New “Weather”: “Sunny”,
York, Date =   “Temperature”:
Tomorrow.   “25°C”}
Output: “The
weather in New
York is sunny
today with a
temperature of
25°C.”
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
Ans:
Chunking-2M
Chinking 2M
POS Tagging role 1M
Sentence: “The black dog is running in the park.”
• Chunking: Groups words → [The black dog] (NP), [the park]
(NP).
• Chinking: Removes unwanted words → e.g., remove in
(preposition) from the chunk.
POS Tagging: Provides word categories (DT, JJ, NN, etc.), which are
used to apply chunking and chinking rules.
CO-4,   c.5   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
Ans:
(2+2+1) = 5 Marks
Hyponymy and Hypernymy
Hyponymy is a semantic relation in which the meaning of one word is
included in the meaning of another word.
Example: rose, tulip, and lily are hyponyms of flower.
The statement can be expressed as: “A rose is a kind of flower.”
Hypernymy is the opposite relation: it refers to the more general word
whose meaning includes that of more specific words.
********** 2 **********
--- page 3 ---
Example: flower is a hypernym of rose, tulip, and lily.
Similarly, animal is a hypernym of dog, cat, and elephant.
Application of Hypernymy in Word Sense Disambiguation (WSD)
Hypernymy relations are very useful in WSD because they allow a system
to connect ambiguous words to their broader, more general categories. By
checking the surrounding context and mapping it to the correct hypernym,
a system can choose the right sense of a word.
Example: Consider the polysemous word “bank.”
Sense 1: financial institution (hypernym = organization)
Sense 2: river bank (hypernym = geographical feature / landform)
If the sentence is:
“The boy was fishing on the bank.”
Words like fishing and river in the context point towards the hypernym
geographical feature.
Therefore, bank here means river bank.
“She deposited money in the bank.”
Context words like money and deposit map to the hypernym organization.
Therefore, bank here means financial institution.
In WSD, hypernymy helps map ambiguous words to their general category,
and then context determines which sense is correct.
CO-3;   d. 6   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3   Ans: Marks Distribution-3 Marks for Comparison and 2 Marks for
Example of each type
Pragmatics concentrates on speaker intention and context-dependent meaning,
whereas discourse analysis investigates how sentences and utterances are
connected to form coherent texts and conversations. Together, they provide a
comprehensive   understanding   of how language   functions   in   real
communication.
Pragmatics is the branch of linguistics that studies how meaning is shaped by
context of use. It goes beyond the literal semantic meaning of words and
focuses on how speakers use language to achieve communicative goals.
Example “Can you pass the salt?” — pragmatically, this is not a question about
ability but a request.
Discourse analysis studies how sentences and utterances are connected to
form larger units of meaning such as conversations, narratives, or written
texts.   It   is concerned with cohesion (linguistic ties like reference,
substitution, conjunctions) and coherence (logical flow of ideas in context).
Example :“I bought a book yesterday. The book was about artificial
intelligence.”
********** 3 **********
--- page 4 ---
→ The second sentence refers back to “a book” using “the book,” creating
textual cohesion.
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;
SO-1;   ii.   Discuss the significance of NER in three different NLP
BL-2,3   applications.
Ans:
Ans: [Marks 5+5]
i.
Feature   Morpheme   Lexeme
Meaning The smallest grammatical The basic unit of lexical
unit in a language that   meaning — represents a set
carries meaning.   of related word forms.
Function Deals with word structure Deals with word meaning
(morphology).   and usage in the lexicon.
Example   Morpheme   Lexeme
Unhappi   Has three morphemes:   The lexeme is HAPPY,
ness   “un-” (prefix), “happy”   which can appear as happy,
(root), “-ness” (suffix).   happier, happiest.
Running   Has two morphemes:   The lexeme is RUN, which
“run” + “-ing”.   includes run, runs, ran,
running.
ii.
1. Information Extraction (IE)
Automatically extracts structured information (names, dates,
locations, organizations) from unstructured text such as news
articles, reports, or legal documents.
2. Question Answering Systems (QA)
Helps identify entities in questions and documents (e.g., “Who is
the   CEO of Tesla?” → CEO = role, Tesla = organization).
3. Machine Translation
Ensures named entities like “Barack Obama” or “New Delhi”
are   translated correctly or kept unchanged.
4. Healthcare & Biomedical Text Mining
Extracts entities such as patient names, diseases, medications,
genes, or proteins from medical records and research papers.
5. Customer Feedback & Social Media Analysis
Identifies product names, brands, locations, or events in tweets,
reviews, and online discussions for business intelligence.
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
********** 4 **********
--- page 5 ---
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
Assume the <s> and </s> for each sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> artists paint murals in city </s>
<s> musicians play songs in city </s>
<s> painters paint murals on walls </s>
<s> signs are near city </s>
Test sentence-
<s> artists paint murals near city </s>
Distinct tokens are:
<s>, </s>, artists, paint, murals, in, city, musicians, play, songs,
painters, on, walls, signs, are, near
That gives V=16.
Counts:
• Unigram counts:
o C(artists)=1
o C(paint)=2
o C(murals)=2
o C(near)=1
o C(city)=3
o C(<s>)=4
• Bigram counts:
o C(<s>,artists)=1
o C(artists,paint)=1
o C(paint,murals)=2
o C(murals,near)=0
o C(near,city)=1
o C(city,</s>)=3
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(artists∣<s>)=[1+1]/[4+16]=2/20=1/10≈0.1
2. P(paint∣artists)=[1+1]/[1+16]=2/17≈0.117647
3. P(murals∣paint)=[2+1]/[2+16]=3/18=1/6≈0.166667
4. P(near∣murals)=[0+1]/[2+16]=1/18≈0.0555556
5. P(city∣near)=[1+1]/[1+16]=2/17≈0.117647
6. P(</s>∣city)=[3+1]/[3+16]=4/19≈0.210526
Exact fraction:
P+1=1/10*2/17*1/6*1/18*2/17*4/19=16/5930280=2.698E-6
Hence, the probability of the test sentence is =2.698E-6.
********** 5 **********
--- page 6 ---
Q3   a   i.   Explain the various types of ambiguities encountered in Natural [10]
CO- 3,   Language Processing (NLP). Illustrate each type with suitable
SO-, BL-   examples.
ii.   Compare top-down and bottom-up parsing and apply bottom-up
4
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-
“A cat chased the mouse”
Grammar   Lexicon
S → NP VP   Det → {A, the}
NP → Pronoun   Noun → {cat, mouse}
NP → Proper-Noun   Verb → {chased}
NP → Det Nominal
Nominal → Noun
Nominal → Nominal Noun
Nominal → Nominal PP
VP → Verb
VP → Verb NP
VP → VP PP
PP → Prep NP
Ans: Marks-5
1. Lexical Ambiguity:
Meaning:
Occurs when a word has multiple possible meanings.
Example:
He went to the bank.
• “bank” can mean a financial institution or the side of a river.
Explanation:
NLP systems must use context to decide which meaning of “bank”
applies in the sentence.
2. Syntactic Ambiguity (Structural Ambiguity)
Meaning:
Occurs when a sentence can be parsed in more than one way due to
different grammatical structures.
Example:
I saw the man with the telescope.
•   Interpretation 1: I used the telescope to see the man.
•   Interpretation 2: The man had the telescope.
Explanation:
The ambiguity arises because the prepositional phrase (“with the
telescope”) can modify either the verb saw or the noun man.
3. Semantic Ambiguity
Meaning:
Occurs when the meaning of the sentence itself is unclear, even if the
structure is fine.
Example:
Visiting relatives can be boring.
********** 6 **********
--- page 7 ---
•   Interpretation 1: The act of visiting relatives is boring.
•   Interpretation 2: The relatives who visit are boring.
Explanation:
The confusion comes from whether visiting is used as a gerund (verb)
or adjective (modifier).
4. Pragmatic Ambiguity
Meaning:
Arises when the intended meaning depends on context or speaker’s
intention rather than grammar or word meaning.
Example:
Can you pass the salt?
•   Literally, it’s a question about ability.
•   Pragmatically, it’s a request for action.
Explanation:
Understanding pragmatic meaning requires world knowledge and
context.
5. Referential Ambiguity
Meaning:
Occurs when a pronoun or reference word could refer to multiple
entities.
Example:
John told Tom that he was late.
• “he” could refer to John or Tom.
Explanation:
The ambiguity arises in anaphora (reference resolution).
ii.
Comparison (Any two relevant points-2M)
Aspect   Top-Down Parsing   Bottom-Up Parsing
Starts from the root (start   Starts from input tokens
Parsing   symbol) and expands   and reduces toward the
Direction   toward the input.   root.
Expands non-terminals
using grammar rules,   Combines tokens/phrases
Grammar Rule   even before seeing if   only if they appear in the
Application   input matches.   input.
Fails or loops infinitely
Handling Left   if grammar has left   Naturally handles left
Recursion   recursion.   recursion without issues.
May get stuck or need   Can face shift-reduce or
Ambiguity   backtracking when   reduce-reduce conflicts in
Handling   grammar is ambiguous.   ambiguous grammars.
Ease of   Conceptually simple and More complex (needs
Implementation   intuitive to implement.   parsing tables, stacks).
Bottom up parsing with steps-3
********** 7 **********
--- page 8 ---
Godors wp awry ti

‘ vos Hy )
=— : ver
a Nowr vub \ cbt
\ che ome Pet
; nan
_ Norin® wee
\ % *
Oe one ‘i ete atase
kb
zeus avid Mar Rs arte)
Ng NP
aearel worn
aie wee vib DE “
y 2
stop bak rik yin?” “nr 1°
NP
~~
4 J
My ye Nomint
7 ; / degee
ve
al var mone

“ unr Chock 1

Shp © form cunUR tt)

62 NY Ny

Coton we “nt IM Fina

“A Cok chuck ue we
= a

‘Se:

ok che TN Monee

FIC QF EH 1
--- page 9 ---
CO-3;   b   Consider the given paragraph given below:   [10]
SO- 1   The teacher wrote on the board. The students listened to the teacher.
BL-4:   The board was full of notes. The student asked a question. The
teacher answered from the book.
Target words: teacher, student, board, book
Context words: wrote, listened, notes, question
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.
Plot the target word vectors by considering only two dimensions: “wrote”
and “notes”.
Ans: [Marks 5+5]
Co-occurrence matrix:
target \ context   wrote   listened   notes
teacher   1   1   0
student   0   1   0
board   1   0   1
book   0   0   0
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2   Ans:[Marks-5+5]
It is an essential step in natural language processing (NLP) that involves
cleaning and transforming unstructured text data to prepare it for analysis.
Text data contains noise in various forms like emoticons, punctuations, text in
a different cases, HTML tags etc.
********** 9 **********
--- page 10 ---
Inadequate or low-quality data can lead to lower accuracy and effectiveness of
the model.
The pre-processing steps for a problem depend mainly on the domain and the
problem itself, hence, we don’t need to apply all steps to every problem and
also the order of applying these steps may also vary.
Various text preprocessing steps are widely used for dimensionality reduction.
Some of the commonly used preprocessing steps are:
o Removing punctuations like . , ! $( ) * % @, URLs, Stop
words
o Lower casing
o Normalization (some common ones)
▪   Tokenization
▪ Stemming
▪ Lemmatization
Stop word removal:
• Stop words are a set of commonly used words in a language like “a”,
“the”, “is”, “are” etc. in English.
• These words do not carry important meaning and are removed from
texts in many data science tasks.
• The intuition behind this approach is that, by removing low
information words from text, we can focus on the important words
instead.
• One of the advantages of removing stop words is that it can reduce the
size of the dataset, which in turn reduces the training time required for
building natural language processing models.
• Stop word removal is commonly applied in search systems, text
classification applications, topic modeling, topic extraction and others.
• Stop word lists can come from pre-established sets or you can create a
custom one for your domain. This creation may be tricky as few words
that may not be useful in some problem statement may be important in
others.
Lower casing:
•   Usually, this is the first step that is performed while pre-processing.
•   Is a text preprocessing step where all letters in the text are converted
to lowercase.
•   This step is implemented so that the algorithm does not treat the same
words differently in different situations.
o Ex: Book and book mean the same but when not converted to
the lower case those two are represented as two different
words in the vector space model (resulting in more
dimensions).
• However, it is important to remember that some words, like “US” and
“us”, can change meanings when reduced to the lower case. Also,
there can be cases where the capitalization is important and has to be
preserved. So we should avoid performing this step in such cases
Normalization:
• As raw text data is random, each word has a lot of variations in the form of
tenses, superlatives, and many more.
********** 10 **********
--- page 11 ---
• These variations increase the complexity of the data and are difficult for the
machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data into a
predefined standard, hence improving the efficiency of the model.
• Ex: Many forms of the base word collect - "collection", "collective", and
"collectively".
•   If we reduce the variations of a word in the raw text, there will be fewer
input variables for our machine-learning model to deal with, thus increasing
efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for structures
like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Few common ones used are:
• Removal of duplicate whitespaces and punctuation.
• Accent removal (if your data includes diacritical marks from ‘foreign’
languages).
•   Substitution of contractions (Ex: ‘I’m ’→‘I am’ and don’t to do not).
• Transform word numerals into numbers (Ex: ‘twenty three’→‘23’).
•   Substitution of values for their type (Ex: ‘$50’→‘MONEY’).
• Acronym normalization (Ex: ‘US ’→‘United States’/‘U.S.A’) and
abbreviation normalization (Ex: ‘btw’ → ‘by the way’).
• Normalize date formats, social security numbers or other data that have a
standard format.
•   Spell correction (one could say that a word can be misspelled infinite
ways, so spell corrections reduce the vocabulary variation by “correcting”)
•   Substitution of rare words for more common synonyms.
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
Noun   Verb   Noun
BL-4
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Ans:
********** 11 **********
--- page 12 ---
Q5   a   For the following two sentences:   [10]
• Sentence A: “The student read a science book in the library”
• Sentence B: “The teacher read a history book in the classroom”
********** 12 **********
--- page 13 ---
CO-2;   1. Construct the TF-IDF matrix for these sentences after removing
SO-1 ;   the stop words {The, a, in}.
BL-3;   2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
Ans:[Marks 5+5]
Term   Sentence   Sentence
A   B
student   0.693   0
read   0   0
science   0.693   0
book   0   0
library   0.693   0
teacher   0   0.693
history   0   0.693
classroo   0   0.693
m
Analysis:
For Sentence A, the unique theme is student, science, library.
For Sentence B, the unique theme is teacher, history, classroom.
So, it indicates that TF–IDF clearly shows that shared words don’t matter for
separation, while unique words carry more importance.
CO-4;   b   Consider the sentence: “The bat hit the ball hard on the cricket field.”   [10]
SO-1BL-   Two possible senses of “bat”:
4
• Sense 1: Bat (Sports equipment – cricket/baseball)
• Sense 2: Bat (Nocturnal flying mammal)
Sentence
Context Words   Sense (Class)
ID
ball, cricket, score,   Sports (Bat =
1
stadium   equipment)
Animal (Bat =
2   night, cave, wings, fly
mammal)
3   player, run, match, bat   Sports
4   nocturnal, vampire, insect Animal
5   team, field, bowl, bat   Sports
6   dark, flying, cave, night   Animal
a) Using the Naïve Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naïve Bayes
Classification.
Ans:
********** 13 **********
--- page 14 ---
P(Sports)=0.5
1 mk
P(Animal)=0.5
Unique words across both classes: (words: ball, cricket, score, stadium,
player, run, match, bat, team, field, bowl, night, cave, wings, fly,
nocturnal, vampire, insect, dark, flying) Total 20
1
mk
Calculations:
For Sports:
2 mks
• P(hit∣S)=(0+1)/32=1/32=0.03125
• P(ball∣S)=(1+1)/32=2/32=0.0625
• P(cricket∣S)=2/32=0.0625
• P(field∣S)=2/32=0.0625
• P(hard∣S)=1/32=0.03125
For Animal:
P(w∣A)=1/31≈0.03225806
Likelihood for sports:
2 mks
0.5 * 0.03125*0.0625*0.0625*0.0625*0.03125 =1.19209290×10-7
Likelihood for animal :
1.74647163×10-8
Classified sense: Sports equipment
1 mk
Laplace Smoothing:
3 mks
Handles problem of zero probabilities, improves robustness of
classifier.
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate
how it predicts the target word from its surrounding context
Ans:
********** 14 **********
--- page 15 ---
iii.   Marks Distribution-3 Marks for approach explanation and 2
Marks for advantage of each type
Co-reference resolution: task of finding all expressions in text that refer to
the same entity. (1.5 marks)
Example: Mary said Mary is tired. She went home. → "Mary" and "She" co-
refer.
Pronoun resolution: a subtask focusing only on resolving pronouns to their
antecedents. (1.5 marks)
Example: John met Peter when he was leaving. → "he" could refer to John or
Peter.
Difference: co-reference is broader (includes noun phrases, names, definite
descriptions), while pronoun resolution is narrower.
In Word2Vec, two main architectures are used to learn word
embeddings:
Continuous Bag of Words (CBOW) and
Skip-Gram.
Both are neural network-based models that learn to represent words as
dense vectors based on their context in a text corpus.
1. Continuous Bag of Words (CBOW) Model
Working Principle:
The CBOW model predicts the target word from its surrounding
context words.
It takes context words as input and tries to predict the central
(target) word.
The model averages (or sums) the vectors of the context words and
passes them through a neural network to predict the target word.
Example:-Sentence
“The cat sat on the mat”
If the window size = 2, and the target word is “sat”, then the context
words are:
["The", "cat", "on", "the"]
The CBOW model learns:
P(sat | The, cat, on, the)
Intuition:
It focuses on understanding the meaning of a word based on its
surrounding words.
2. Skip-Gram Model
Working Principle:
• The Skip-Gram model does the reverse of CBOW.
•   It predicts the context words given a target word.
• The target word is input, and the model learns to predict
surrounding context words.
Example:-Sentence:
“The cat sat on the mat”
If the target word is “sat” and window size = 2, then the context
words are:
["The", "cat", "on", "the"]
********** 15 **********
--- page 16 ---
The Skip-Gram model learns:
P(The | sat), P(cat | sat), P(on | sat), P(the | sat)
Intuition:
It focuses on how a single word relates to its neighboring words.
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Ans: Marks Distribution-5 Marks for approach explanation and 5 Marks
for resolution
i
Hobbs’ Algorithm is a syntactic algorithm for pronoun resolution in NLP.
It identifies possible antecedents for a pronoun by traversing a syntactic parse
tree in a systematic manner.
Example:
Sentence: “When Mary saw Alice, she waved.”
• Pronoun = she
• Step 1: Start at NP dominating “she.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs = “Mary,” “Alice.”
• Step 4: First candidate = Mary, chosen as antecedent.
Limitations :
Struggles with ambiguous cases (gender/number mismatch ignored).
Not efficient for long, complex sentences.
ii Sentence: “Ravi met Suresh at the station after he arrived from
Delhi.”
Pronoun: he
Steps of traversal:
1. Start at NP for “he.”
2. Move up to nearest S node.
3. Traverse left branches → encounter NPs: Ravi, Suresh.
4. Candidate 1 = Ravi, Candidate 2 = Suresh.
5. According to Hobbs’ order: Ravi is encountered first.
Hobbs’ algorithm chooses Ravi as antecedent of “he.”
But semantically, “Suresh” may also make sense depending on context
→ shows limitation of Hobbs.
Q7   a   Explain the working of text classification in Natural Language Processing [10]
(NLP) and discuss the key steps involved in building a text classification
********** 16 **********
--- page 17 ---
CO-4;   system in context of real-world applications such as spam detection or
SO-1 BL-   news categorization.
3:   Ans:
Text classification is the process of automatically assigning categories or
labels to text data based on its content.
Examples include:
Spam filtering – Classifying emails as “spam” or “not spam.”
News categorization – Grouping news articles into topics like sports,
politics, or entertainment.
Sentiment analysis – Identifying whether a review or comment is
positive, negative, or neutral.
Steps Involved in Text Classification
1. Data Collection
Gather a dataset containing text documents and their corresponding labels.
• Example: A set of emails labeled as “spam” or “ham” (not spam).
2. Data Preprocessing
Prepare the text for analysis by cleaning and normalizing it. Common steps
include:
• Lowercasing – Convert all text to lowercase.
• Removing noise – Punctuation, special characters, HTML tags, etc.
•   Tokenization – Splitting text into individual words or tokens.
•   Stop word removal – Removing common words like “the,” “is,”
“and.”
• Stemming/Lemmatization – Reducing words to their base or root form
(e.g., “running” → “run”).
3. Feature Extraction / Text Representation
Convert the cleaned text into a numerical format that a machine learning
model can understand. Common methods:
• Bag of Words (BoW) – Counts the occurrence of each word in the
document.
• TF-IDF (Term Frequency–Inverse Document Frequency) – Weighs
words based on their importance.
• Word Embeddings (e.g., Word2Vec, GloVe) – Captures semantic
meaning of words in vector form.
•   Transformer-based embeddings (e.g., BERT) – Context-aware
representations of text.
4. Model Training
Train a classification algorithm using the numerical features and their labels.
Examples of models:
•   Traditional ML: Naive Bayes, Logistic Regression, SVM.
• Deep Learning: RNNs, CNNs for text, Transformers (e.g., BERT).
5. Model Evaluation
Evaluate the trained model using metrics such as:
• Accuracy – Overall correctness.
•   Precision & Recall – Useful for imbalanced datasets (e.g., spam
detection).
•   F1-score – Balance between precision and recall.
6. Prediction / Deployment
********** 17 **********
--- page 18 ---
Use the trained model to classify new, unseen text data.
Example: A new email arrives → model predicts “spam” or “not spam” →
automatically sorted into the correct folder.
7. Monitoring and Updating
Over time, new words and patterns emerge. The model should be regularly
retrained with updated data to maintain accuracy.
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
Ans: [Marks 5+5]
i. Different corpus structures are applied to different NLP tasks
depending on the information they provide:
Flat Text Corpus (e.g., plain .txt files):
This type contains only raw text without labels. It can be applied to tasks
like word frequency analysis, calculating readability scores, or
comparing the styles of different writers. For example, one can apply it
to study the most common words in political speeches.
Annotated Corpus (e.g., POS-tagged or parsed text):
This type contains extra linguistic information such as part-of-speech
tags, named entities, or syntactic structures. It can be applied in
supervised learning tasks such as training a Part-of-Speech tagger,
Named Entity Recognition, or parsing models. For instance, a POS-
tagged corpus can be used to train a model that automatically identifies
nouns and verbs in new texts.
ii. Jaccard similarity takes into account only the set of unique words
for each text document. This makes it the likely candidate for
assessing the similarity of documents when repetition is not an issue.
Both Euclidean and cosine similarity metrics drop if an additional
word is added to the list.
Jaccard similarity is limited to assessing the lexical similarity of text,
i.e., how similar documents are on a word level.
The differentiating factor between Euclidean and Cosine measure is
that cosine similarity is not affected by the magnitude/length of the
feature vectors. It only considers the angle between them, making it
ideal for comparing vectors of different lengths. (Ex: If a word
‘senate’ occurs more frequently in doc 1 than it does in doc 2, we
could assume that doc 1 is more related to the topic of Politics.
However, it could also be the case that we are working with news
articles of different lengths and word ‘senate’ probably occurred more
in doc 1 simply because it was way longer)
Ex:
********** 18 **********
--- page 19 ---
Doc 1: “I love data science and machine learning”
Doc 2: “I love machine learning”
Step 1: Preprocess the documents - Remove stopwords like “I”, “and”,
etc., and lowercase everything.
Doc 1 → ['love', 'data', 'science', 'machine', 'learning’]
Doc 2 → ['love', 'machine', 'learning’]
Vocabulary :['love', 'data', 'science', 'machine', 'learning']
Jaccard
Intersection: ['love', 'machine', 'learning'] → 3 words
Union: ['love', 'data', 'science', 'machine', 'learning'] → 5 words
Jaccard=3/5=0.6
Cosine
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Dot product = 1∗1+1∗0+1∗0+1∗1+1∗1=31∗1+1∗0+1∗0+1∗1+1∗1=3
|A| = √(1²+1²+1²+1²+1²) = √5 ≈ 2.236
|B| = √(1²+0²+0²+1²+1²) = √3 ≈ 1.732
cos(θ)= 3/(2.236×1.7323) ≈ 3/3.8723 ≈0.775
Euclidean:
Vectors: Doc1 = [1, 1, 1, 1, 1] Doc2 = [1, 0, 0, 1, 1]
Distance=Sqrt((1−1)2+(1−0)2+(1−0)2+(1−1)2+(1−1)2 )
Distance= ≈1.414
Measure   Value   Meaning
Jaccard   0.6   60% of the words overlap
Cosine   0.775   High similarity in word pattern
Euclidean   1.414   Some difference in word presence
In short, flat corpora are applied to simpler, surface-level analysis, while
annotated corpora are applied to more advanced supervised NLP tasks.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 3dadb3d14255

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIML_7053/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA
Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
• Remove HTML tags, URLs, or non-ASCII characters.
********** 1 **********
--- page 2 ---
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
********** 2 **********
--- page 3 ---
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
********** 3 **********
--- page 4 ---
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
grammar of a sentence. It   sentence. It interprets the
Definitio
determines how words are   intent and context beyond
n
arranged and related   just the grammatical
grammatically.   structure.
********** 4 **********
--- page 5 ---
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
o C(in)=3
o C(the)=3
o C(park)=1
********** 5 **********
--- page 6 ---
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
********** 6 **********
--- page 7 ---
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 239009df9fbb

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper f26c97ae3882

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AIDS_7056/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 3c107a24b377

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 437ea4f3bf65

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7057/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 820068e9ce76

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CS_7055/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 07b2258ae7c6

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 870c905daf22

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 11 · Answer key · paper 10399dc9a736

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_11/Re-Exam/Integrated_Computer_7032/Natural Language Processing/ANS_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER
OF BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Draw block diagram of generic NLP pipeline and explain the task [5]
SO-1 ;   associated with each block
BL-2;   Ans: Marks (2+3)
1. Data Acquisition
Purpose:   Collect raw   textual   data   from   various   sources.
Tasks:
• Handle different formats: JSON, CSV, PDF, XML, or plain text.
• Ensure data is relevant and representative for the NLP task.
2. Text Cleaning
Purpose: Remove noise and irrelevant information from raw text.
Tasks:
• Remove   special   characters,   punctuation,   numbers   (if
unnecessary).
********** 1 **********
--- page 2 ---
• Remove HTML tags, URLs, or non-ASCII characters.
•   Correct encoding issues and remove duplicate entries.
3. Text Preprocessing
Purpose: Transform text into a structured format suitable for analysis or
modeling.
Tasks:Tokenization,   Lowercasing,   Stop-word   removal,
Stemming/Lemmatization, POS Tagging etc.
4. Feature Engineering
Purpose: Convert preprocessed text into numerical representations for
machine learning models.
Tasks:Bag-of-Words (BoW), TF-IDF vectors.,Word embeddings:
Word2Vec, GloVe, BERT embeddings.
5. Modeling
Purpose: Train an NLP model to learn patterns and make predictions.
Tasks: Choose a model type: Traditional ML (SVM, Naive Bayes) or
Deep Learning (RNN, Transformers).Split data into training, validation,
and test sets.Train the model on labeled or unlabeled data.
6. Evaluation
Purpose: Assess the performance of the trained NLP model.
Tasks:
• Use metrics like Accuracy, Precision, Recall, F1-Score (for
classification).Use BLEU, ROUGE (for text generation or
summarization).Confusion matrix or error analysis to understand
model weaknesses.
7. Deployment
Purpose: Make   the model   available   for   real-world   usage.
Tasks:Deploy as an API or integrate into applications (web, mobile,
chatbot).Ensure scalability and handle concurrent requests.
8. Monitoring
Purpose:   Track   model   performance   in   production.
Tasks:Monitor metrics like latency, throughput, and prediction accuracy.
9. Model Update
Purpose: Improve or retrain the model to maintain accuracy.
Tasks:Incorporate new labeled data for retraining.Fine-tune pre-trained
models.
CO-2,   b.   i.   Define function words and content words.   [5]
SO-1   ii.   Which category (function words and content words) belong to
BL-3   open class and closed class? Justify your answer.
iii.   For the sentence given below, identify the function words and
content words –
“The small cat is sleeping under the tree”
Ans: Marks 2+1+2
********** 2 **********
--- page 3 ---
• Function words are words that have little lexical meaning on their
own but serve a grammatical purpose in a sentence. They help link
content words together and indicate relationships (e.g., is, the, under).
• Content words are words that carry lexical meaning and provide the
main information in a sentence. They include nouns, verbs,
adjectives, and adverbs (e.g., cat, sleeping, small
• Content words → Open class
o Because new words are constantly being added (e.g., selfie,
blog, emoji).
o Includes nouns, main verbs, adjectives, adverbs.
• Function words → Closed class
o Because the set of function words is relatively fixed and rarely
changes.
o Includes articles, prepositions, pronouns, auxiliary verbs,
conjunctions, determiners.
For the sentence: “The small cat is sleeping under the tree”
Function words: The, is, under, the
Content words: small, cat, sleeping, tree
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
Ans: (3+2) = 5 Marks
Word2vec vs. GloVe: Learning Strategies
Word2vec
1. Learning strategy: Predictive model.
2. Learns embeddings by predicting a target word from its context
(CBOW) or predicting context words from a target word (Skip-
gram).
3. Relies on local context windows and stochastic gradient descent.
4. Captures syntactic and semantic relationships effectively from
the way words appear near each other.
5. Example: Learns from “The boy kicked the ball” by predicting
ball from {the, boy, kicked, the}.
GloVe (Global Vectors for Word Representation)
1. Learning strategy: Count-based model.
2. Constructs a global word–word co-occurrence matrix from the
entire corpus, then factorizes it to produce word embeddings.
3. Focuses on capturing global statistical information across the
whole corpus, not just local context windows.
4. Example: Learns that ice co-occurs more with cold and water,
while steam co-occurs with hot and boil.
Choice of Corpus
Word2vec is more suitable for large, dynamic, and streaming
corpora (e.g., social media posts, news feeds).
Reason: It learns well from local sequential contexts and does not
require full co-occurrence statistics upfront.
GloVe is more suitable for large, static corpora (e.g., Wikipedia,
Common Crawl, academic text collections).
Reason: It leverages the entire co-occurrence matrix of the corpus,
so it works best when global statistics can be fully computed.
********** 3 **********
--- page 4 ---
CO-4;   d.   Differentiate between cataphora and anaphora in terms of direction of [5]
SO-1 ;   reference. How coreference resolution is different from anaphora
BL-3   reference?
Ans: Marks-3+2
Anaphora → Reference moves backward in the text.
A pronoun or expression refers to something mentioned earlier.
Example: “Ravi was late because he missed the train.” (he → Ravi).
Cataphora → Reference moves forward in the text.
A pronoun or expression refers to something mentioned later.
Example: “When she arrived, Priya looked nervous.” (she → Priya).
Anaphora = backward looking reference.
Cataphora = forward looking reference.
Relationship Between coreference and Anaphora
• Every   anaphora   is   a   coreference,
but not every coreference is an anaphora.
Example (non-anaphoric coreference):
When he arrived, Dr. Verma smiled.
Here, “he” comes before “Dr. Verma” — this is cataphora, a type of
coreference but not anaphora.
Concept   Direction   Example   Type
Anaphor Backward   “Ravi lost his wallet.   Subset of
a   reference   He was upset.”   Coreference
Corefere Any direction   “When he arrived,   Broader
nce   (backward/forward Dr. Verma smiled.”   concept
)
Q2   a   i. Discuss five different tasks associated with Natural Language [10]
CO-4;   Processing.
SO-1;   Ans:[5+5]
BL-2,3   • Machine Translation – Automatically translating text from one
language to another (e.g., Google Translate).
• Sentiment Analysis – Identifying emotions or opinions in text
(positive, negative, neutral).
• Information Extraction – Extracting structured data like names,
dates, or relations from unstructured text.
• Text Summarization – Producing a concise summary of a long
document.
• Question Answering / Chatbots – Understanding user queries
and generating relevant answers (e.g., Siri, Alexa).
ii. Compare and contrast syntactic analysis and semantic analysis in
NLP. Support your explanation with examples.
Ans:
Aspect   Syntactic Analysis   Semantic Analysis
Focuses on the structure and Focuses on the meaning of a
Definitio
grammar of a sentence. It   sentence. It interprets the
n
determines how words are   intent and context beyond
********** 4 **********
--- page 5 ---
arranged and related   just the grammatical
grammatically.   structure.
To understand semantic
To identify syntactic
relationships like roles of
relationships such as subject,
Goal   entities, meanings, and
object, phrases, and parse
relationships between
trees.
concepts.
Word sense disambiguation,
Parsing (Dependency parsing,
Techniq   Named Entity Recognition,
Constituency parsing), POS
ues Used   Semantic Role Labeling,
tagging, Grammar rules.
Ontologies.
A sentence or text with
A well-formed sentence or
Input   syntactic and contextual
text.
cues.
Meaning representation,
Parse tree, grammatical
Output   intent, entity relationships,
structure, phrase hierarchy.
or logic representation.
Example Sentence: “The cat chased the Sentence: “I saw the man
1   mouse.”   with a telescope.”
CO-   b   Consider the following training corpus:   [10]
2;SO-   1. cats chase mice in the garden
1;BL-3   2. dogs bark loudly at night
3. birds sing in the morning
4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
Ans:
[ 1 mark for vocabulary + 1.5 marks each for unigram and bigram
counts + 5 marks for Laplace smoothed probability + 1 mark for
probability of the sentence]
Adding start and end tokens for each sentence-
Training corpus-
<s> cats chase mice in the garden </s>
<s> dogs bark loudly at night </s>
<s> birds sing in the morning </s>
<s> children play games in the park </s>
Test sentence-
<s> cats bark in the park </s>
Distinct tokens are:
<s>, </s>, at, bark, birds, cats, chase, children, dogs, games, garden, in,
loudly, mice, morning, night, park, play, sing, the
That gives V=20
Counts:
• Unigram counts:
o C(<s>)=4
o C(cats)=1
o C(bark)=1
********** 5 **********
--- page 6 ---
o C(in)=3
o C(the)=3
o C(park)=1
• Bigram counts:
o C(<s>,cats)=1
o C(cats,bark)=0
o C(bark,in)=0
o C(in,the)=3
o C(the,park)=1
o C(park,</s>)=1
Laplace (add-one) smoothing-
Formula:
P+1(wi∣wi−1)=[C(wi−1,wi)+1]/[C(wi−1)+V]
Bigram Probabilities:
1. P(cats∣<s>)=[1+1]/[4+20]=2/24=1/12≈0.08333
2. P(bark∣cats)=[0+1]/[1+20]=1/21≈0.04762
3. P(in∣bark)=[0+1]/[1+20]=1/21≈0.04762
4. P(the∣in)=[3+1]/[3+20]=4/23≈0.17391
5. P(park∣the)=[1+1]/[3+20]=2/23≈0.08696
6. P(</s>∣park)=[1+1]/[1+20]=2/21≈0.09524
Exact fraction:
P+1=1/12*1/21*1/21*4/23*2/23*2/21=16/58788828=2.72E-7
Hence, the probability of the test sentence is =2.72E-7.
Q3   a   In the context of natural language processing, explain the concept of top- [10]
CO-3 ,   down and bottom-up parsing approaches.
SO-, BL-
Apply top-down syntax parsing approach to the sentence given below and
4
draw a parse tree using the CFG grammar rules-
The tall boy saw a girl in the park.”.
CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
Ans: Top down brief explanation 2M
Bottom up brief explanation 2M
Top down parsing steps of the given example -4M
Final Tree- 2M
Top-Down Parsing Approach:
•   Starts from the highest level (root) of the parse tree, i.e., the
start symbol (S).
********** 6 **********
--- page 7 ---
•   Tries to expand the grammar rules to reach the input string
(sentence).
•   It predicts what could come next based on the grammar.
• Example: For grammar rule S → NP VP, it first assumes the
sentence starts with S and then tries to find a matching NP and VP
in the input.
Pros: Simple and intuitive.
Cons: May lead to backtracking and inefficiency.
Bottom-Up Parsing Approach:
•   Starts from the input words (tokens) and tries to build up to
the start symbol (S).
•   It identifies small phrases (like NP or VP) and combines them
into larger structures.
• Example: It first finds nouns and verbs, forms phrases, and
finally combines them into a full sentence.
Pros: Efficient and handles ambiguity better.
Cons: Harder to implement and interpret manually.
********** 7 **********
--- page 8 ---
CO-4;   b   Consider the sentence: "The bank can ensure your deposits are safe."   [10]
SO-1   The word “bank” has the following two possible senses (WordNet-style
BL-4:   glosses):
• Bank₁: Sloping land especially beside a body of water.
• Bank₂: A financial institution that accepts deposits and channels
the money into lending activities.
i. Apply the LESK algorithm to determine the correct sense of
the word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
Ans:
********** 8 **********
--- page 9 ---
a) Context words → {bank, ensure, deposits, safe}. (1 mk)
Glossary for sense word:
Gloss1→ {sloping, land, beside, body, water, especially}
Gloss2 → {financial, institution, accepts, deposits, channels, money,
lending, activities}
(1 mk)
Computing Overlaps:
1 marks for each overlap with senses. (2mks)
Final sense : 1mk
b) Limitations:
Dependence on glossary length, vocabulary mismatch, scalability
issues, Domain dependence etc. (5 mks)
Q4   a   Consider the following three documents:   [10]
CO-2;   • Document A: “The dog chased the cat.”
SO-1;   • Document B: “The cat chased the mouse.”
BL-4   • Document C: “The dog ran after the cat.”
Using the Bag of Words (BoW) model, represent each document as a
vector after removing the stop words {The, by, was}.
i. Construct the term-document matrix.
ii. Compute the cosine similarity between each pair of documents
(A–B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of
document similarity.
Ans:
Words in A: dog, chased, cat
Words in B: cat, chased, mouse
Words in C: dog, ran, after , cat
Vocabulary list: ["after", "cat", "chased", "dog", "mouse", "ran"]
A → [0, 1, 1, 1, 0, 0]
B → [0, 1, 1, 0, 1, 0]
C → [1, 1, 0, 1, 0, 1]
Cosine similarity Matrix:
A   B   C
A 1.00   0.66   0.57
0   7   7
B 0.66   1.00   0.28
7   0   8
********** 9 **********
--- page 10 ---
C 0.57   0.28   1.00
7   8   0
Analysis:
• A vs B (0.667): Same structure and 2 common words: cat, chased
• A vs C (0.577): Similar idea, shares dog and cat, but different verbs
(chased vs ran after)
• B vs C (0.288): Only one shared word (cat), different verbs and objects
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO1-;
BL-4   Noun   Verb   Noun
1   Dog   eats   bread
Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Ans:
********** 10 **********
--- page 11 ---
Q5   a   Justify with an appropriate example the importance of TF-IDF technique [10]
in the document representation and information retrieval task.
********** 11 **********
--- page 12 ---
CO-2 ;   Ans:
SO-1 ;   • Used to overcome the drawback of BOW technique that treats all
BL-3;   words equally.
•   It gives importance to words in a document by considering both
frequency and their uniqueness (i.e. words that get repeated too
often don’t overpower less frequent and more important words).
•   It works on a statistical measure of finding word relevance in the
text that can be in the form of a single document or various
documents that are referred to as corpus.
•   It consists of two components:
o Term Frequency (TF)
▪   It denotes the frequency of a word in a document.
▪ For a specified word, it is defined as the ratio of the
number of times a word appears in a document to the
total number of words in the document.
• Inverse Document Frequency (IDF)
o   It measures the importance of the word in the corpus.
o   It measures how common a particular word is across all the
documents in the corpus.
o   It is the logarithmic ratio of no. of total documents to no. of a
document with a particular word.
•
• The TF-IDF score for a term t in a document d is given by
multiplying the TF and IDF values
o
• The higher the TF-IDF score for a term in a document, the more
important that term is to that document within the context of the
entire corpus.
CO-3;   b   Consider the given paragraph given below:   [10]
SO-1 BL-   The farmer planted seeds in the soil. The rain watered the soil. The sun
4:   helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
********** 12 **********
--- page 13 ---
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Mark (4+3+3)
Target words: farmer, soil, sun, plant
Context words: plant, water, grow, harvest
i.   Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
Ans: Co-occurrence matrix:
Target /
plant   water   grow   harvest
Context
farmer   2   0   0   1
soil   1   1   0   0
sun   1   0   1   0
plant   2   0   1   1
Q6   a   Marks (5+5)   [10]
CO-4;   i. Briefly describe any two approaches to pronoun resolution and
SO-1;   mention one advantage of each.
Ans:
BL-3
Rule-based approach: uses syntactic/linguistic rules like gender/number
agreement, recency, and binding theory. (1.5 marks)
Advantage: interpretable and linguistically motivated. (1 mark)
********** 13 **********
--- page 14 ---
Neural/deep learning approach: uses contextual embeddings (e.g., BERT)
and end-to-end models to learn pronoun resolution from data. (1.5 marks)
Advantage: captures semantic and discourse-level context better. (1
mark)
ii. Describe the difference between Homonymy and Synonymy with
suitable examples. Discuss how these two relations differently
affect natural language processing applications?
Ans:
(3+2) = 5 Marks
Homonymy vs. Synonymy
Homonymy
Homonymy occurs when two or more words share the same
spelling or sound but have unrelated meanings.
Example 1: bank (financial institution) vs. bank (side of a river)
Example 2: bat (flying mammal) vs. bat (sports equipment)
Synonymy
Synonymy refers to different words that have the same or nearly the
same meaning.
Example 1: big and large
Example 2: car and automobile
Impact on NLP Applications
Homonymy
Challenge: Homonyms create ambiguity in text because the same
word can represent unrelated meanings.
Example: In Information Retrieval, if a user searches for bank, the
system must decide whether to return documents about finance or
rivers.
NLP Task Affected: Word Sense Disambiguation (WSD) is
necessary to resolve such ambiguity.
Synonymy
Challenge: Synonyms create redundancy in language because
different words can express the same concept.
Example: In a search engine, if the user searches for car, relevant
documents containing automobile should also be retrieved.
NLP Task Affected: Synonym handling improves tasks like
Information Retrieval, Question Answering, and Text
Summarization by recognizing meaning equivalence.
CO-4;   b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main [10]
SO-1;   steps and limitations.
BL-3   ii. Apply Hobbs’ Algorithm to the sentence:
“When Ramesh gave Shyam a book, he smiled.”
Identify the antecedent of “he” by showing traversal steps.
Ans: (Marks 5+5)
Hobbs’ Algorithm
Hobbs’ Algorithm is a syntactic method for resolving pronouns to their
antecedents using parse tree traversal.
Steps
********** 14 **********
--- page 15 ---
1. Start at the NP node immediately dominating the pronoun.
2. Move up to the nearest NP or S node. Call it X.
3. Traverse all branches of X to the left of the path to pronoun,
breadth-first, collecting NPs as candidate antecedents.
4. If no antecedent found, move further up to the next NP or S node
and repeat.
5. If still unresolved, search earlier sentences.
Limitation: Purely syntactic, ignores semantics/world knowledge, may
choose wrong antecedent in ambiguous cases.
Sentence: “When Ramesh gave Shyam a book, he smiled.”
• Pronoun: he
• Step 1: Start at NP “he.”
• Step 2: Move up to nearest S node.
• Step 3: Traverse left branches → NPs encountered: Ramesh,
Shyam.
• Step 4: First candidate = Ramesh.
Hobbs’ Algorithm selects Ramesh as antecedent.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role [10]
CO-4;   in Recommender Systems and Search Engines.
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
process.
3:
Ans: [Marks 5+5]
i. Information Retrieval (IR) is the process of finding relevant
information or documents from a large collection (e.g., the web, a
database, or a library) in response to a user’s query.
• The goal is not just to match keywords, but to understand the
user’s intent and retrieve the most relevant information efficiently.
• Example: When you search “best mobile phones 2025” on
Google, the IR system finds and ranks web pages that best match your
query.
Applications of Information Retrieval
a. Search Engines
• Google, Bing, Yahoo, etc., use IR to crawl, index, and rank
billions of web pages.
• When you enter a search query, the engine retrieves and ranks
pages based on relevance.
b. Recommender Systems
• IR techniques are used to match user preferences with relevant
items (e.g., movies, books, products).
• Example: Netflix uses IR principles to find movies similar to
those you’ve watched and recommend them.
c. Digital Libraries & Archives
• IR is used to search academic papers, legal documents, or
historical records.
d. Question Answering Systems / Chatbots
• These systems retrieve relevant passages or documents to
generate accurate answers.
ii. Steps Involved in the IR Process
********** 15 **********
--- page 16 ---
Step 1: Document Collection
Gather and store the documents to be searched.
• Example: Web crawling for search engines, collecting articles for
digital libraries.
Step 2: Document Preprocessing
Prepare documents for indexing:
•   Tokenization (splitting text)
• Stop-word removal (e.g., “the,” “and”)
• Stemming or lemmatization (e.g., “running” → “run”)
• Removing punctuation and formatting
Step 3: Indexing
Build an index structure (similar to a book’s index) for fast retrieval.
•   Inverted Index is commonly used: it maps each word to a list of
documents where it appears.
• Example:
•   "apple" → [Doc1, Doc3, Doc10]
• "banana" → [Doc2, Doc5]
Step 4: Query Processing
Process the user’s query using similar preprocessing steps
(tokenization, stop-word removal, etc.).
• This ensures consistency between the query and the document
collection.
Step 5: Retrieval & Ranking
Retrieve documents that match the query and rank them based on
relevance scores.
• Common ranking methods:
o TF-IDF (Term Frequency–Inverse Document Frequency)
o Vector Space Model (measuring cosine similarity)
o Probabilistic models (e.g., BM25)
o Neural models / BERT-based ranking
Step 6: Evaluation
Assess how well the system retrieves relevant documents. Common
metrics:
•   Precision – % of retrieved documents that are relevant.
•   Recall – % of relevant documents that are retrieved.
•   F1-score, MAP (Mean Average Precision), nDCG.
Step 7: Feedback & Refinement
Use user feedback or relevance feedback to improve future retrieval
results.
• Example: If users keep clicking a certain type of result, the system
learns to rank those higher.
CO-2;   b   i. Discuss how the Gutenberg Corpus can be utilized for various text [10]
SO-1 BL-   analysis tasks in Natural Language Processing?
3:   Ans:
ii. Explain the importance of text normalization in Natural Language
Processing (NLP). Illustrate your answer with a suitable example
of an application where text normalization plays a crucial role.
Ans: [Marks 5+5]
i.
********** 16 **********
--- page 17 ---
• As raw text data is random, each word has a lot of variations in the
form of tenses, superlatives, and many more.
• These variations increase the complexity of the data and are difficult
for the machine learning model to train them.
• Text normalization reduces this complexity by reducing the text data
into a predefined standard, hence improving the efficiency of the
model.
• Ex: Many forms of the base word collect - "collection", "collective",
and "collectively".
•   If we reduce the variations of a word in the raw text, there will be
fewer input variables for our machine-learning model to deal with,
thus increasing efficiency and avoiding false negatives.
• Text normalization reduces the dimensionality of the input for
structures like bag-of-words and Tf-Idf.
• There is no correct set or list of normalization tasks that work for all
situations.
Ex: If we are building a sentiment classifier for customer reviews.
ii.
Raw text:
Review 1: “The product is AWESOME!!!”
Review 2: “This product is awesome.”
Review 3: “awesomeness of this product is great.”
Without normalization:
Features → {awesome, AWESOME, awesomeness} are treated as different
words.
Model sees them as unrelated → splits sentiment signal.
After normalization:
Lowercasing → awesome, awesome, awesomeness
Lemmatization → awesome, awesome, awesome
Now, all reviews highlight the same positive feature (awesome) → classifier
learns stronger positive signal.
********** 17 **********
````
