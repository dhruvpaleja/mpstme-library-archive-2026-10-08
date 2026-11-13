# Natural Language Processing: question papers in full

52 unique papers · 2018-19 to 2025-26 · Computer Engineering, Artificial Intelligence, Data Science, Information Technology, AI and Data Science, Computer Science, AI and Machine Learning, Electronics and Telecommunication

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 7 · paper f713f0617894

- Departments: AI and Data Science, Artificial Intelligence, Computer Engineering, Data Science, Information Technology
- Programmes: BTech AI 7012, BTech AIDS 7056, BTech Computer 7002, BTech CSE DS 7011, BTech IT 7001, Integrated Computer 7032, MBATech AI 7051, MBATech Computer 7047, MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_07/Final-Exam/BTech_IT_7001/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2024-2025.pdf` (+10 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: text (4 pages)

````text
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
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples
BL-2;
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
CO-4,   c.   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
CO-3;   d.   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;   ii.   Discuss the significance of NER in three different NLP
SO-1;   applications
BL-2,3
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
********** 1 **********
--- page 2 ---
Assume the <s> and </s> for each sentence.
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
iii. Plot the target word vectors by considering only two dimensions:
“wrote” and “notes”.
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
BL-4   Noun   Verb   Noun
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
********** 2 **********
--- page 3 ---
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Q5   a   For the following two sentences:   [10]
CO-2;   • Sentence A: “The student read a science book in the library”
SO-1 ;   • Sentence B: “The teacher read a history book in the classroom”
BL-3;   1. Construct the TF-IDF matrix for these sentences after removing
the stop words {The, a, in}.
2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
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
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate how
it predicts the target word from its surrounding context
********** 3 **********
--- page 4 ---
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Q7   a   Explain the working of text classification in Natural Language Processing [10]
CO-4;   (NLP) and discuss the key steps involved in building a text classification
SO-1 BL-   system in context of real-world applications such as spam detection or
news categorization.
3:
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 1 · paper 294ff29e7562

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Natural Language Processing/QP_Natural Language Processing(703DB0C057)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. Assume Suitable data if necessary
8. Use of calculator (both normal as well as scientific) is allowed
9. Use of python/ excel is allowed, without access to the internet
Q1. Answer briefly.   (20 marks)
a.   What is NLP? List and explain applications of NLP.   (5 marks)
b.   Explain the Naive Bayes classifier for binary text classification in NLP. List its applications.
(5 marks)
c.   Explain how Convolutional Neural Networks (CNN) are used in Natural Language Processing.
Mention their advantages and applications.   (5 marks)
d.   Explain Transfer Learning in Natural Language Processing. Mention its advantages and
applications with examples.   (5 marks)
Q2. Answer the followings:   (20 marks)
a.   Explain Stemming and Lemmatization in Natural Language Processing. Compare both techniques
and discuss their advantages, limitations, and applications with examples.   (10 marks)
b.   Suppose you are given a dataset of customer reviews labeled as positive or negative. Explain how
you would build a text classification system using NLP. Discuss the steps involved, the role of feature
extraction, model selection, and evaluation.   (10 marks)
Q3. Answer the followings:
a.   Explain the concept of TF-IDF in Natural Language Processing, including its purpose and
advantages. Then, given the following three documents, compute the TF, IDF, and TF-IDF values for the
term “data”:
Doc1: "big data is transforming industries"
Doc2: "data science and machine learning are important"
Doc3: "cloud computing enables scalable data storage"
Discuss the significance of the TF-IDF value obtained for the term in these documents.   (10 marks)
b.   Explain the architecture of Convolutional Neural Networks (CNN) for text data in Natural
Language Processing. Describe each layer, its function, and how text is processed through the network.
(10 marks)
********** 1 **********
--- page 2 ---
Q4. Answer the followings:
a.   Explain the concept of Transfer Learning in Natural Language Processing. Describe how BERT
can be fine-tuned for text classification tasks. Explain the architecture, the steps involved in fine-tuning,
and its advantages for classification tasks.   (10 marks)
b.   Explain Sentiment Analysis in Natural Language Processing. Discuss its objectives, methods,
workflow, challenges, and applications with examples.   (10 marks)
Q5. Answer the followings:
a.   Given the sentence below, perform Part-of-Speech (POS) tagging for each word. Explain the POS
tagging process. Sentence: "Researchers develop innovative algorithms to analyze large datasets
efficiently."   (10 marks)
b.   Explain the concepts of Tokenization and Word Embedding in Natural Language Processing.
Discuss their purposes and significance in NLP applications. Also, illustrate with examples how a
sentence is tokenized and converted into embeddings.   (10 marks)
Q6. Answer the followings:
a.   Explain how Hidden Markov Models (HMM) are used in voice recognition systems. Discuss the
architecture and its key components.   (10 marks)
b.   Describe how clustering can be applied to group similar text documents?   (10 marks)
Q7. Answer the followings:
a.   Define the Continuous Bag of Words (CBOW) model in Word2Vec. Explain its working principle,
the role of context words, advantages, limitations, and applications in Natural Language Processing.
(10 marks)
b.   Explain the concept of n-grams in Natural Language Processing. Distinguish between unigram,
bigram, trigram, and higher-order n-grams. Illustrate with an example how a short sentence can be
represented using unigram, bigram, and trigram models.   (10 marks)
********** 2 **********
````

## 2025-26 · Final-Exam · Sem 2 · paper e70ee4f11872

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Natural Language Processing/QP_Natural Language Processing(703DB0C057)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Natural Language Processing
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
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
b.   Explain the process of tokenization in Natural Language Processing. Discuss at least three
challenges faced when tokenizing text from different languages or domains.   (5 marks)
c.   What is Bidirectional Encoder Representations from Transformers (BERT)? Explain the concept
of bidirectional context in BERT and why it is important for understanding language compared to
unidirectional models.   (5 marks)
d.   Explain how Convolutional Neural Networks process text data differently from Recurrent Neural
Networks. What makes Convolutional Neural Networks particularly effective for sentence-level NLP
tasks?   (5 marks)
Q2. Answer the followings:   (20 marks)
a. Explain all the major accuracy metrics used to evaluate text classification models including
precision, recall, F1-score, accuracy, and confusion matrix. Define each metric mathematically
and explain when each is most appropriate. Why is accuracy alone sometimes misleading,
especially for imbalanced datasets? Illustrate with an example.   (10 marks)
b. Explain the complete text processing pipeline including tokenization, stemming, lemmatization,
and Part-of-Speech tagging. For the sentence "The researchers are researching better ways to
research user behaviors," demonstrate the output at each processing stage. Why is the order of
these operations important?   (10 marks)
********** 1 **********
--- page 2 ---
Q3. Answer the followings:   (20 marks)
a. Explain the working of Bidirectional Encoder Representations from Transformers. Describe
Masked Language Modelling and Next Sentence Prediction. Explain how the model is fine-
tuned for classification tasks and discuss its advantages.   (10 marks)
b. Given the sentence below, perform Part-of-Speech tagging for each word. Clearly indicate the
appropriate grammatical category for each term. Explain the tagging process and justify your
assigned tags based on contextual meaning.
Sentence: "Researchers develop innovative algorithms to analyze large datasets efficiently."
(10 marks)
Q4. Answer the followings:   (20 marks)
a. Explain in detail the function of each layer in a CNN model used for NLP. Discuss how each layer
contributes to feature extraction and final classification.   (10 marks)
b. Explain the role of Hidden Markov Models (HMM) in voice recognition systems. Describe how
HMM models sequential data and discuss its application in recognizing speech patterns. (10 marks)
Q5. Answer the followings:   (20 marks)
a. Explain the concept of document clustering in Natural Language Processing (NLP). Discuss the
complete process of clustering text documents, including preprocessing, feature representation
(such as TF-IDF), similarity measures, and clustering algorithms like K-means or hierarchical
clustering. Also highlight the advantages and applications of document clustering.   (10 marks)
b. Although CNNs were originally developed for image processing, they are widely used in NLP
tasks. Explain why CNNs are effective for text classification tasks, highlighting their key
properties.   (10 marks)
Q6. Answer the followings:   (20 marks)
a. Analyze the role of transfer learning in improving NLP model performance. Explain why transfer
learning is particularly effective for text data, and discuss its advantages over training models from
scratch. Illustrate your answer with examples of real-world applications, including domain-
specific models such as FinBERT, and explain how they enhance performance in specialized tasks.
(10 marks)
b. Differentiate between speech recognition and voice recognition. Discuss their working principles,
applications, and key challenges in real-world systems.   (10 marks)
********** 2 **********
--- page 3 ---
Q7. Answer the followings:   (20 marks)
a. Consider a dataset containing noisy text with inconsistent formatting, including extra spaces,
special characters, and mixed case words. Explain how Regular Expressions can be used to clean
and standardize the text. Illustrate your answer with suitable examples and discuss the limitations
of using Regular Expressions for complex Natural Language Processing tasks.   (10 marks)
b. Explain the Continuous Bag of Words model used in word embedding. Describe its architecture
and working mechanism. Illustrate how the model predicts a target word using surrounding context
words with a suitable example.   (10 marks)
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper d98300b43e11

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: text (4 pages)

````text
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
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples
BL-2;
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
CO-4,   c.   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
CO-3;   d.   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;   ii.   Discuss the significance of NER in three different NLP
SO-1;   applications
BL-2,3
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
********** 1 **********
--- page 2 ---
Assume the <s> and </s> for each sentence.
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
iii. Plot the target word vectors by considering only two dimensions:
“wrote” and “notes”.
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
BL-4   Noun   Verb   Noun
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
********** 2 **********
--- page 3 ---
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Q5   a   For the following two sentences:   [10]
CO-2;   • Sentence A: “The student read a science book in the library”
SO-1 ;   • Sentence B: “The teacher read a history book in the classroom”
BL-3;   1. Construct the TF-IDF matrix for these sentences after removing
the stop words {The, a, in}.
2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
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
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate how
it predicts the target word from its surrounding context
********** 3 **********
--- page 4 ---
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Q7   a   Explain the working of text classification in Natural Language Processing [10]
CO-4;   (NLP) and discuss the key steps involved in building a text classification
SO-1 BL-   system in context of real-world applications such as spam detection or
news categorization.
3:
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 52a6f98c6256

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CS_7055/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: text (4 pages)

````text
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
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1   Answer briefly   [20]
CO-1 ;   a.   Differentiate between Natural Language Understanding (NLU) and [5]
SO-1 ;   Natural Language Generation (NLG) in NLP with suitable examples
BL-2;
CO-2,   b.   Explain the concepts of chunking and chinking in Natural Language   [5]
SO-   Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports
BL-2   these processes, and illustrate your explanation with a suitable example.
CO-4,   c.   Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1   can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3   resolve the correct meaning of polysemous words? Provide an example?
CO-3;   d.   Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1 ;   examples.
BL-3
Q2   a   i.   Differentiate between Morpheme and Lexeme with examples   [10]
CO-1,4;   ii.   Discuss the significance of NER in three different NLP
SO-1;   applications
BL-2,3
CO-   b   Consider the following training corpus:   [10]
2;SO-1;   1. artists paint murals in city
BL-3   2. musicians play songs in city
3. painters paint murals on walls
4. signs are near city
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”
********** 1 **********
--- page 2 ---
Assume the <s> and </s> for each sentence.
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
iii. Plot the target word vectors by considering only two dimensions:
“wrote” and “notes”.
Q4   a   Explain any three basic text preprocessing techniques used in Natural [10]
CO-2;   Language Processing (NLP). Discuss the purpose of each technique and
SO-1;   illustrate them with suitable examples.
BL-2
Q4   b   Consider the following POS tagged corpus. Apply Hidden Markov Model [10]
CO-3;   (HMM) approach to
SO-1;
BL-4   Noun   Verb   Noun
1   Cat   chase   mice
Det   Noun   Verb
2   The   dog   runs
********** 2 **********
--- page 3 ---
Det   Noun   Verb   Noun
3   A   cat   eats   cheese
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of sequence of Events
Det   Noun   Verb   Noun
The   cat   eats   mice
Note: Include start and end characters for all the sentences
Q5   a   For the following two sentences:   [10]
CO-2;   • Sentence A: “The student read a science book in the library”
SO-1 ;   • Sentence B: “The teacher read a history book in the classroom”
BL-3;   1. Construct the TF-IDF matrix for these sentences after removing
the stop words {The, a, in}.
2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores.
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
Q6   a   i.   Differentiate between co-reference resolution and pronoun [10]
CO-4;   resolution with suitable examples
SO-1;   ii.   Explain the working principle of the Continuous Bag of Words
BL-3   (CBOW) model and Skipgram model in Word2Vec. Illustrate how
it predicts the target word from its surrounding context
********** 3 **********
--- page 4 ---
CO-3;   b   i.   Explain Hobb's Algorithm. Discuss the steps with help of example [10]
SO-1;   and state its limitation.
BL-4
ii.   Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according to the
algorithm
Q7   a   Explain the working of text classification in Natural Language Processing [10]
CO-4;   (NLP) and discuss the key steps involved in building a text classification
SO-1 BL-   system in context of real-world applications such as spam detection or
news categorization.
3:
CO-2;   b   i.   Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL-   and discuss how each can be applied in various NLP tasks with
3   suitable examples.
ii.   Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaccard is the best choice in that case.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 5 · paper 1934bdce4374

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Information Technology
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / ARTIFICIAL INTELLIGENCE, B TECH / COMPUTER, B TECH / CSE DATA SCIENCE (311), B TECH / IT, B.TECH INTEGRATED / COMPUTER, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing 2025-26 Final.pdf` (+9 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Dec 2025
- Text: ocr (4 pages), mean OCR confidence 89.4

````text
oo

MPSTME

SVKMs NMIMS LIBRARY
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AD/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B=te
(CS)/B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/B. Tech (IT)/MBA

Tech (AI)/MBA Tech (Comp)/MBA Tech (IT) 2
Year: IlL/ IV/ VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)

Subject: Natural Language Processing
Date: 02 Dec 2025 Time: 10:00 am to 01:00 pm (03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:
1. This question paper contains 4 pages.
2. Question No. | is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Inall 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.

Ql Answer briefly [20]
CO-1 ; a. Differentiate between Natural Language Understanding (NLU) and [5]
SO-1; Natural Language Generation (NLG) in NLP with suitable examples
BL-2;

CO-2, b. Explain the concepts of chunking and chinking in Natural Language. | [5]
So- Processing (NLP). Discuss how Part-of-Speech (POS) tagging supports

BL-2 these processes, and illustrate your explanation with a suitable example.
CO-4, c. Define hyponymy and hypernymy with suitable linguistic examples. How [5]
SO-1 can hypernymy be applied in Word Sense Disambiguation (WSD) to
BL-3 resolve the correct meaning of polysemous words? Provide an example?
CO-3; d. Compare pragmatic and discourse analysis with the help of appropriate [5]
SO-1; examples. ‘

BL-3

Q2 a i. Differentiate between Morpheme and Lexeme with examples _ [10]
CO-1,4; ii. Discuss the significance of NER in three different NLP
SO-1; applications

BL-2,3

Co- b Consider the following training corpus: [10]
2;SO-1; 1. artists paint murals in city

BL-3 2. musicians play songs in city

; 3. painters paint murals on walls
4. signs are near city t

Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence:
“artists paint murals near city”

FR RK 7 RR RRR
--- page 2 ---
Assume the <s> and </s> for each sentence.

Q3
COo- 3,
SO-, BL-

a

i. Explain the various types of ambiguities encountered in Natural. [10]
Language Processing (NLP). Illustrate each type with suitable
examples. ‘ee

ii. Compare top-down and bottom-up parsing and apply bottom-up
syntax parsing approach to the sentence given below and draw a
parse tree using the grammar rules-

“A cat chased the ynouse”

Grammar Lexicon

S — NP VP Det — {A, the}

NP — Pronoun Noun — {cat, mouse}
NP — Proper-Noun Verb > {chased}

NP = Det Nominal
Nominal — Noun
Nominal — Nominal Noun
Nominal — Nominal PP
VP — Verb

VP — Verb NP

VP — VP PP

PP — Prep NP

CO-3;
SO- 1
BL-4:

Consider the given paragraph given below: [10]
The teacher wrote on the board. The students listened to the teacher.

The board was full of notes. The student asked a question. The
teacher answered from the book.

Target words: teacher, student, board, book
Context words: wrote, listened, notes, question

i. Construct a co-occurrence matrix for the target and context words.
Take the window size as one whole sentence.

ii. Evaluate the similarity between the vectors of the target words
“teacher-student” and “teacher-board” using the cosine similarity.

iii. Plot the target word vectors by considering only two dimensions:
“wrote” and “notes”. ‘

>.

Q4
CO-2;
SO-1;
BL-2

Explain any three basic text preprocessing techniques used in Natural | [10]
Language Processing (NLP). Discuss the purpose of each technique and
illustrate them with suitable examples.

Q4

CO-3;
SO-1;
BL-4

*

Consider the following POS tagged corpus. Apply Hidden Markov Model | [10]
(HMM) approach to

Noun Verb Noun

1 Cat chase mice
Det Noun Verb
2 The dog runs

FRR 2 cdo RR
--- page 3 ---
LQ ANI.

Det Noun Verb Noun
3 A cat eats cheese
i. Construct the emission probability matrix.
ii. Construct the transmission probability matrix.
iii. Calculate the probability of sequence of Events

Det “Noun Verb Noun

The cat eats mice
Note: Include start and end characters for all the sentences
Q5 a For the following two sentences: [10]
CO-2; e Sentence A: “The student read a science book in the library”
SO-1 ; ¢ Sentence B: “The teacher read a history book in the classroom”
BL-3; 1. Construct the TF-IDF matrix for these sentences after removing
the stop words {The, a, in}.
2. Identify and comment on the important terms in each sentence
based on their TF-IDF scores. - »
CO-4; b Consider the sentence: “The bat hit the ball hard on the cricket field.” [10]
SO-1BL- Two possible senses of “bat”:
4
¢ Sense 1: Bat (Sports equipment — cricket/baseball)
¢ Sense 2: Bat (Nocturnal flying mammal)
Senence Context Words Sense (Class)
1 ball, cricket, score, Sports (Bat =
stadium equipment)
; A Animal (Bat =
2; night, cave, wings, fly mammal)
B_ __ player, run, match, bat « |Sports |
4 |fnocturnal, vampire, insect [Animal
5 I[team, field, bowl, bat [Sports
le I[dark, flying, cave, night | Animal
a) Using the Naive Bayes algorithm, classify the sense of “bat” in
the given sentence Apply Laplace Smoothing wherever
applicable.
b) Discuss the significance of Laplace Smoothing in Naive Bayes
Classification.
AQ6 a i. Differentiate between co-reference resolution and pronoun | [10]
CO-4; resolution with suitable examples
SO-1; ii. Explain the working principle of the Continuous Bag of Words
BL-3

(CBOW) model and Skipgram model in Word2Vec. Illustrate how
it predicts the target word from its surrounding context

. RK dk RR Re
4 .

J
--- page 4 ---
CO-3; i. Explain Hobb's Algorithm. Discuss the steps with help of example , [10]
SO-1; and state its limitation. i
BL-4 . . <
ii. Sentence: Ravi met Suresh at the station after he arrived from
Delhi.
Using Hobbs’ algorithm, determine the most likely antecedent of
the pronoun "he". Show the steps of traversal according: to the
algorithm
Q7 Explain the working of text classification in Natural Language Processing | [10]
CO-4; (NLP) and discuss the key steps involved in building a text classification
SO-1 BL- system in context of real-world applications such as spam detection or
3: news categorization.
CO-2; i. Differentiate between a flat text corpus and an annotated corpus, [10]
SO-1 BL- and discuss how each can be applied in various NLP tasks with
3 suitable examples.

ii. Explain a real-world scenario where the Jaccard Similarity
measure is more appropriate than Euclidean or Manhattan
distance, and justify why Jaocard is the best choice in that case.

FOR AGG A kk dia deka

om.
````

## 2025-26 · Final-Exam · Sem 1 · paper 6eb9b6dee6a4

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM I/Natural Language Processing/Natural Language Processing 2025-26 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: ocr (2 pages), mean OCR confidence 92.7

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-

Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL

Year: I/Semester [(Exam Year: 2025-2026) «

Subject: Natural Language Processing :

Date: 03 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions: ‘

1. This question paper contains 2 pages. -

2. Answer to each new question to be started on a fresh page.

3. Figure in right hand side indicates full marks

4. Question No. 1 is compulsory

5. Out of remaining questions, attempt any 4 questions

6. In all 5 questions to be attempted

7. Assume Suitable data if necessary

8. Use of calculator (both normal as well as scientific) is allowed

9. Use of python/ excel is allowed, without access to the internet

Ql. Answer briefly. (20 marks)

a. What is NLP? List and explain applications of NLP. (5 marks)
b. Explain the Naive Bayes classifier for binary text classification in NLP. List its applications.

(5 marks)
c Explain how Convolutional Neural Networks (CNN) are used in Natural Language Processing.
Mention their advantages and applications. (5 marks)
d. Explain Transfer Learning in Natural Language Processing. Mention its advantages and
applications with examples. (5 marks)
Q2. Answer the followings: (20 marks)
a. Explain Stemming and Lemmatization in Natural Language Processing. Compare both techniques
and discuss their advantages, limitations, and applications with examples. (10 marks)
b. Suppose you are given a dataset of customer reviews labeled as positive or negative. Explain how
you would build a text classification system using NLP. Discuss the steps involved, the role of feature
extraction, model selection, and evaluation. ; (10 marks)

Q3. Answer the followings:

a. Explain the concept of TF-IDF in Natural Language Processing, including its purpose and
advantages. Then, given the following three documents, compute the TF, IDF, and TF-IDF values for the
term “data”:

Docl: "big data is transforming industries"

Doc2: "data science and machine learning are important"

Doc3: "cloud computing enables scalable data storage"

Discuss the significance of the TF-IDF value obtained for the term in these documents. (10 marks)
tr

b. Explain the architecture of Convolutional Neural Networks (CNN) for text data in Natural
Language Processing. Describe each layer, its function, and how text is processed through the network.
(10 marks)

FER 7 dG kok A kk
--- page 2 ---
Q4. Answer the followings:

a. Explain the concept of Transfer Learning in Natural Language Processing. Describe how BERT
can be fine-tuned for text classification tasks. Explain the architecture, the steps invelved in fine-tuning,
and its advantages for classification tasks. ** (10 marks)
b. Explain Sentiment Analysis in Natural Language Processing. Discuss its objectives, methods,
workflow, challenges, and applications with examples. ; (10 marks)

Q5. Answer the followings: S

a. Given the sentence below, perform Part-of-Speech (POS) tagging for each word. Explain the POS
tagging process. Sentence: "Researchers develop innovative algorithms to analyze large datasets
efficiently." (10 marks)

b. Explain the concepts of Tokenization and Word Embedding in Natural Language Processing.

Discuss their purposes and significance in NLP applications. Also, illustrate with examples how a
"sentence is tokenized and converted into embeddings. . (10 marks)

Q6. Answer the followings:

a. Explain how Hidden Markov Models (HMM) are used in voice recognition systems. Discuss the
architecture and its key components. _° (10 marks)
b. Describe how clustering can be applied to group similar text documents? (10 marks)

Q7. Answer the followings:
a. Define the Continuous Bag of Words (CBOW) model in Word2Vec. Explain its working principle,
the role of context words, advantages, limitations, and applications in Natural Language Processing.

~ (10 marks)
b. Explain the concept of n-grams in Natural Language Processing. Distinguish between unigram,
bigram, trigram, and higher-order n-grams. Illustrate with an example how a short sentence can be
represented using unigram, bigram, and trigram models. (10 marks)

RRR RR RRR DR RK
````

## 2025-26 · Re-Exam · Sem 5 · paper 6f12e9c9ff49

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIML_7053/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
2. dogs bark loudly at night
CO-2;
3. birds sing in the morning
SO-1;   [10]
4. children play games in the park
BL-3
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
Assume <s> and </s> as start and end of the sentence.
********** 1 **********
--- page 2 ---
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Noun   Verb   Noun
Q4
1   Dog   eats   bread
CO-2;
[10]
SO-1,2;   Det   Noun   Verb
BL-4
2   The   cat   sleeps
Det   Noun   Verb   Noun
3   A   dog   eats   fish
********** 2 **********
--- page 3 ---
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 8220cbf6921d

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 681b62c1ae48

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AIDS_7056/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper fe2ab8d3dcff

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper b90e56bbefa5

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7057/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 8479227013cf

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CS_7055/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 90cd34a8d9ac

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 2af6728f742b

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 11 · paper bd5059f62e89

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_11/Re-Exam/Integrated_Computer_7032/Natural Language Processing/QP_Natural Language Processing(702AI0C009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q1
Answer briefly   [20]
CO-1;   a.
Draw block diagram of generic NLP pipeline and explain the task associated
SO-1;   [5]
with each block
BL-2;
b.   i.   Define function words and content words.   [5]
ii.   Which category (function words and content words) belong to
CO-2,   open class and closed class? Justify your answer.
SO-1;   iii.   For the sentence given below, identify the function words and
BL-3   content words –
“The small cat is sleeping under the tree”
CO-3,   c.   Differentiate between word2vec and GloVe in terms of their learning [5]
SO-1,2   strategies. Which type of corpus would be more suitable for each method,
BL-3   and why?
CO-4;   d.   [5]
Differentiate between cataphora and anaphora in terms of direction of
SO-1;
reference. How coreference resolution is different from anaphora reference?
BL-3
a   i. Discuss five different tasks associated with Natural Language
Q2
Processing.
CO-1,3;
ii. Compare and contrast syntactic analysis and semantic analysis in [10]
SO-1;
NLP. Support your explanation with examples.
BL-2,3
b   Consider the following training corpus:
1. cats chase mice in the garden
CO-2;   2. dogs bark loudly at night
SO-1;   3. birds sing in the morning   [10]
BL-3   4. children play games in the park
Using a bigram language model with Laplace smoothing, evaluate the
probability of the test sentence: “cats bark in the park.”
********** 1 **********
--- page 2 ---
Assume <s> and </s> as start and end of the sentence.
a   In the context of natural language processing, explain the concept of top-
down and bottom-up parsing approaches.
Apply top-down syntax parsing approach to the sentence given below and
draw a parse tree using the CFG grammar rules-
Q3
CO-2,   “The tall boy saw a girl in the park.”.
[10]
SO-, BL-
4   CFG Grammar   Lexicon
S → NP VP   Det → {the | a}
NP → Det Adj N | Det N   Adj → {tall}
VP → V NP | VP PP   N → {boy | girl | park}
PP → P NP   V → {saw}
P → {in}
b   Consider the sentence: "The bank can ensure your deposits are safe."
The word “bank” has the following two possible senses (WordNet-style
glosses):
• Bank₁: Sloping land especially beside a body of water.
CO-3;
• Bank₂: A financial institution that accepts deposits and channels the
SO-1,6   [10]
money into lending activities.
BL-4:
i. Apply the LESK algorithm to determine the correct sense of the
word “bank” in the given sentence. Show the steps clearly.
ii. Briefly discuss limitations of the LESK algorithm in handling
ambiguous words in real-world contexts.
a   Consider the following three documents:
• Document A: “The dog chased the cat.”
• Document B: “The cat chased the mouse.”
• Document C: “The dog ran after the cat.”
Q4
Using the Bag of Words (BoW) model, represent each document as a vector
CO-2;
after removing the stop words {The, by, was}.
SO-1,2;   [10]
i. Construct the term-document matrix.
BL-4
ii. Compute the cosine similarity between each pair of documents (A–
B, A–C, and B–C).
iii. Interpret and comment on the results obtained in terms of document
similarity.
b   Consider the following POS tagged corpus. Apply Hidden Markov Model
(HMM) approach to
Q4   Noun   Verb   Noun
CO-2;   1   Dog   eats   bread   [10]
SO-1,2;
BL-4   Det   Noun   Verb
2   The   cat   sleeps
Det   Noun   Verb   Noun
********** 2 **********
--- page 3 ---
3   A   dog   eats   fish
i.   Construct the emission probability matrix.
ii.   Construct the transmission probability matrix.
iii.   Calculate the probability of given sequence of events.
Det   Noun   Verb   Noun
The   dog   eats   bread
Note: Include start and end characters for all the sentences
Q5   a
CO-2 ;   Justify with an appropriate example the importance of TF-IDF technique in
[10]
SO-1 ;   the document representation and information retrieval task.
BL-2;
b   Consider the given paragraph given below:
The farmer planted seeds in the soil. The rain watered the soil. The sun
helped the plants grow. The farmer harvested the plants. The soil became
rich and fertile.
Target words: farmer, soil, sun, plant
CO-3;   Context words: plant, water, grow, harvest
SO-1,2;   i. Construct a co-occurrence matrix for the target and context words. [10]
BL-4:   Take the window size as one whole sentence.
ii. Evaluate the similarity between the vectors of the target words
"farmer-soil", farmer-sun", and "farmer-plant" using the cosine
similarity.
iii. Plot the target word vectors by considering only two dimensions:
"planted" and "harvested".
a   i. Briefly describe any two approaches to pronoun resolution and
Q6
mention one advantage of each.
CO-3,4;
ii. Describe the difference between Homonymy and Synonymy with [10]
SO-1;
suitable examples. Discuss how these two relations differently affect
BL-3
natural language processing applications?
b   i. Explain Hobbs’ Algorithm for pronoun resolution. State its main
steps and limitations.
CO-4;
ii. Apply   Hobbs’   Algorithm   to   the   sentence:
SO-1;   [10]
“When   Ramesh   gave   Shyam   a   book,   he   smiled.”
BL-3
Identify the antecedent of “he” by showing traversal steps.
Q7   a   i. Explain the concept of Information Retrieval, highlighting its role in
CO-4;   Recommender Systems and Search Engines.
[10]
SO-1 BL-   ii. Discuss the various steps involved in the Information Retrieval
3:   process.
b   i. Discuss how the Gutenberg Corpus can be utilized for various text
CO-2;   analysis tasks in Natural Language Processing?
SO-1 BL-   ii. Explain the importance of text normalization in Natural Language [10]
3:   Processing (NLP). Illustrate your answer with a suitable example of
an application where text normalization plays a crucial role.
********** 3 **********
````

## 2024-25 · Final-Exam · Sem 5 · paper 045ac9ee7f98

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / COMPUTER, B TECH / CSE DATA SCIENCE, B TECH / EXTC, B TECH / I T, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/NATURAL LANGUAGE PROCESSING/Natural Language Processing, Sem-V, Final Exam 2024-25.pdf` (+4 identical copies)
- Printed on paper: duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 89.1

````text
/

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B TECH/MBA TECH Year: III/ITV’Semester: V/VII
Stream/s ; IT/COM/EXTC/CSE-DS/CS/AI/AIML/AIDS :

Subject: Natural Language Processing ‘ Time: 3 hrs (_10am__to__lpm_)
Date:_03_ / 12 /2024 No. of Pages:_S_

Marks: __ 100

Final Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No._1____ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all. 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

=>
6) Figures in brackets on the right hand side indicate full marks.
8 re
7) Assume Suitable data if necessary. a

Ql Answer briefly: : [20]

co-12: |* With the help of suitable expressions explain the concept of TF-IDF

SO-1 we vectorization approach. Discuss its application in information retrieval task.

BL-2

CO-2: b. With the help of suitable example, explain the concept of Named Entity

SO- I Recognition (NER). List some approaches to jmplement NER.

BL-2

CO-3: c. Compare Skipgram and CBOW approaches to implement Word2Vec with

SO-1 2 the help of suitable example.

_ | BL-3
cO-3: d. Compare pragmatic analysis with discourse analysis with the help of

SO-1 2 appropriate examples.

BL-3

Q2 a Discuss few commonly used techniques such as Lowercasing, tokenization,

C0-2: stopword removal, stemming, lemmatization and POS tagging in textual

SO-1 ° data preprocessing using a suitable examples [06]
BL-2
ne: CO-2: b Discuss the need for various lexical similarity measures. Explain cosine

SO-1 ° lexical similarity measure with the help of suitable‘example [04]

BL-2

1

i t.l*“
--- page 2 ---
c Consider the following training corpus.

Name Give | Can | Live jn Have | Class
Birth | Fly Water Legs
Human Yes No No Yes Mammals
Python No No No No Non-Mammals
Salmon No No Yes No Non-Mammals
Whale Yes No Yes No Mammals
Frog No No Sometimes | Yes Non-Mammals
Komodo No No No Yes Non-Mammals
Bat Yes Yes | No Yes Mammals
Pigeon No Yes | No Yes Non-Mammals
Cat Yes No No Yes Mammals
Leopard Yes | No Yes No Non-Mammals
CO-3: Shark
SO-1 i Turtle No No Sometimes | Yes Non-Mammals [10]
BL-4 Penguin No No__-| Sometimes _| Yes Non-Mammals
Porcupine Yes No. | No Yes Mammals
Eel No No Yes No Non-Mammals
Salamander_| No No Sometimes | Yes Non-Mammals
Gila No No No Yes Non-Mammals
Monster
Platypus No No No Yes Mammals
Owl No Yes No Yes Non-Mammals
Dolphin Yes No Yes No Mammals
Eagle No Yes | No Yes Non-Mammals
Apply Naive Bayes classifier to determine the class of the following test
instance ,
Give Birth | Can Fly | Live in Water | Have Legs | Class
Yes No Yes No 2
a Based on the concept of reference resolution, answer the following
questions-
Q3 i. Discuss the significance of reference resolution.
CO-3: ii. With reference to Hobb’s Algorithm for pronoun resolution,
SO-1 : explain binding theory, gender agreement, distance property and | [10]

BL-4.5 recency property. ;
> iii. For the given sentence, apply Hobb’s algorithm to determine the
antecedent for the pronoun “she”. Identify and mention the
property at each step.
“The professor advised the student because she was struggling”
--- page 3 ---
Discuss the role of text classification and sentiment analysis in real- world

CO-4;
SO-1; applications? Provide examples from industries where these NLP tasks are | [10]
BL-2, implemented to improve decision-making and customer engagement.
With reference to Syntax Parsing, answer the following-
i. Discuss the need for syntax parsing.
ii. Compare Top-Down and Bottom-Up parsing approach.
iii. Construct the Syntax Tree for the given input sentence using
Q4 Top-Down approach. Refer to the following rules-
CO-2; 1. S— NP VP [10]
SO-1; 2. NP— DetN
BL-3,4 3. VP—VNP
4. Det — the
5. N- cat, dog
6. V— chased , saw
Input Sentence: “ the cat chased the dog”
With reference to acquiring data for NLP tasks, answer the following
CO-2: questions- _
S O-1: i Discuss various approaches of acquiring data for NLP tasks. [10]
BL2 ii. Explain the need for data augmentation technique.
iii. Briefly explain any four data augmentation methods.
With reference to text data, explain the concept of feature engineering. List
the names of some basic vectorization approaches to implement feature
engineering. .
Consider the corpus given below.
Sentence 1: "Natural Language Processing is fascinating”
Q5 Sentence 2: "I love Natural Language processing and like to study
CO-2; Natural Language" [10]
SO-1; Sentence 3: “I like things that are fascinating”
BL-4
i. Create a vocabulary by removing the stop words {is, that, are,
to, and}
ii. Construct Bag of Words (BOW) matrix
iii. Compute Euclidean distance similarity between sentence 1 and
sentence 2
With reference to Word Sense Disambiguation(WSD), answer the
. following-
Pa 7 te i. Discuss the concept of WSD in brief
- 1; c . ; [05]
BL-2 ii. List various approaches to WSD

iii. State some applications of WSD
--- page 4 ---
c Explain the Discourse Analysis in terms of coherence, cohesion, topic
structure, flow of information, and discourse markers in the given

conversation. ,
CO-3: Conversation:
7 + Speaker 1: “I wént to the store to buy some milk.”
SO-1; ” Waa 4 om [05]
BL-3 * Speaker 2: “Was it crowded?
* Speaker 1: “Yes, I had to wait in line for 10 minutes.”
+ Speaker 3: "I was going to attend the meeting, but I got stuck in
traffic.
a Consider the following training corpus.
Training corpus iv

Cand

<s> I am Henry </s>

<s> I like college </s>

<s> Do Henry like college </s>
<s> Henry I am </s>

<s> Do I like Henry </s>

Q6 <s> Do I like college </s>

CO-2; <s> I do like Henry </s> [10]
SO-1; :

BL-4 Evaluate the most probable next word for the following test corpus using

bi-gram language modelling

Test corpus
i <s> Do ------
ii <s> I like ----------------
iii <g> | -----------------------
. b Discuss the contribution of phonology, morphology, syntax, semantics,
ae and pragmatics to language understanding in NLP
SO-1; prag guag g [05]
BL-2
€ Explain how NLU and NLG work together in an NLP system to create
CO-1: meaningful communication between humans and machines
SO-1; [05]
BL-2 »
--- page 5 ---
Q7
CO-2;
SO-1;
BL-2,3,4

a

With reference to Parts of Speech (POS) Tagging answer the following-

i. Define Function words and Content words with suitable examples
ii. Explain Chunking and Chinking with suitable examples
iii. List various applications of POS tagging
iv. For the given training corpus, construct the transition probability
table and emission probability table using Hidden Markov Model
(HMM) approach (Note: Include start and end characters)

Verb Det Noun

4, Book a flight

Verb Det Noun

2 Read the book

Det Noun Modal Verb Noun

3 The book . | is green

e}y

[10]

CO-3;
SO-1;
BL-4,5

b

With reference to vector space model, answer the following
i. Explain the terms target words, context window, context words, co-
occurrence matrix
ii. For the corpus given below construct a co-occurrence matrix for the
target and context words. Take the window size as one whole
sentence.
iii. | Evaluate the similarity between the vectors of the target words "boy-
dog" and "boy-sun" using the simple dot product.
iv. Plot the target word vectors by considering only two dimensions:
"kicked" and "field".
y. Comment on the results obtained in points iii above.

The boy kicked the ball into the field. The dog barked at the boy. The
sun was shining over the field. The boy ran after the dog. The ball rolled
to the tree.

Target words: boy, ball, dog, sun
Context words: kicked, field, tree, ran

[10]
````

## 2024-25 · Final-Exam · Sem 1 · paper ac3e60038324

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM I/Natural Language Processing/Natural Language Processing Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20/12/24
- Text: ocr (2 pages), mean OCR confidence 87.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025

Program/s: M.Tech Year: I Semester: I

Stream/s ; Artificial Intelligence

—

Subject: Natural Language Processing a Time: 3 hrs (2pm to 5pm )
Date: 20/12/24 _ No. of Pages: 2
Marks: 100

Final Examination (2024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) All Question are compulsory

2) Answer to each new question to be started on a fresh page.

3) Figures in brackets on the right hand side indicate full marks.
4) Assume Suitable data if necessary.

5) Open Internet Exam

6) .ipynb Notebook to be submitted

lan Ql
Answer briefly: [20]
cc (S07) a | What is TE-IDE [A]
. _ |b. What are unigrams, bigrams, trigrams, and n-grams in NLP?
CO-; SO-; PTO — | [10]

BL-
--- page 2 ---
Load the date from !kaggle datasets download -d

Q2 kazanova/sentiment140

CO-; SO-; a. LOAD

BL- b. CLEANING [40]

c. Prepare the model

Load the data from
https://www.kaggle.com/datasets/selener/consume
r-complaint-database

Q3 [40]

CO-; $O-; d. LOAD

BL- e. CLEANING ow

f. Prepare the model *= »
````

## 2024-25 · Final-Exam · paper bbec9c8a2475

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/Natural Language Processing/Natural Language Processing Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30/4 /25
- Text: ocr (2 pages), mean OCR confidence 91.4
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-N

Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINES ANALY:
Year: I/Semester [II(Exam Year: NA) 2024 - 25)
Subject: Natural Language Processing fn
Date: 30/4 /25 Time:2:o0pmty Sieph03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)

Instructions: :

1. This question paper contains ‘2 pages.

2. Answer to each new question to be started on a fresh page.

3. Figure in right hand side indicates full marks.

4. Question | is compulsory. Solve any 4 out of the remaining questions.

Question 1
A. Explain how NLP is used in daily use applications? 5
B. Explain the relevance of syntax in language and explain a parse tree? 5
C. Explain the data acquisition phase of a NLP pipeline? 5
D. Explain how class imbalance can lead to a bias in the classifier and ways to 5

eliminate it?

Question 2

With examples, explain the following NLP use cases — text classification,
A. information extraction, conversational agents, question answering and machine 10
translation?

With examples, explain how language modelling can be challenging? Also contrast
B. modelling basis a generalized approach compared to modelling basis a language 10
specific approach?

Question 3

A. Explain the preprocessing steps within a NLP pipeline? 10

Explain how feature engineering is different in a NLP pipeline? Compare and
B. contrast simple heuristics with features extracted within a classical NLP pipeline and 10
a Deep Learning NLP pipeline

Question 4
A Compare and contrast one hot encoding to bag of words encoding? How are both 10
: of these different from TF-IDF?
B Explain the concept of the word2vec model. Also explain the CBOW and 10
: SkipGram methodologies?
Question 5
A. Explain with examples - the tasks carried out within information extraction? 10

--- page 2 ---
Explain the concept of transfer learning. State and explain the difference between

B. Inductive and Transductive transfer learning. Give an example of how you would, 10
use transfer learning within a NLP application
Question 6 Z
& Explain how CNNs are used in NLP and contrast it to a RNN architecture? Which 10
. of the two is frequently used and why?
What is Attention in NLP and how is it different from a general sequence to 10
sequence model?
Question 7
A. Explain the encoder and decoder architecture of a transformer in detail? 10
B. Explain how you would go about a text classification task in detail? 10

ry

BIRR DFO RE
````

## 2024-25 · Final-Exam · Sem 3 · paper defa7e42880f

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM III/Natural Language Processing/Natural Language Processing Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; exam date: 28 /12 / 202
- Text: ocr (2 pages), mean OCR confidence 88.5

````text
SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: Mtech Year:2 Semester: 3
Stream/s ;AI
Subject: Natural Language Processing : Time: 3 _hrs(Z2pmMto Sp™ )

Date: 28 /12 / 202% No. of Pages: 2.

Marks: 100
Final Examination (2024-2025)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions. = *”
3) In all___5_ questions to be attempted.
4) All questions carry equal marks. 7
5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

ey

Answer briefly: [20]
1
Ql Explain TF-IDF in 7-10 lines with an example. Write and explain
CO- ; SO- ; necessary steps :
BL- 5
Q2 Demonstrate Latent Dirichlet Allocation model for topic modelling
C CO-: SO-: In Latent Dirichlet Allocation model for text classification, what does [20]
BL- alpha and beta hyper parameters represent:
Q3 Explain topic modelling to extract top 5 topics. Write and explain
CO-; S0-; necessary steps {20]
BL-
Qa . . . we
How to apply sentiment analysis on a dataset and obtain positive, neutral
CO-; SO-; [20]

BL or negative sentences. Write and explain necessary steps.
--- page 2 ---
5 :
Q Explain how Named Entity Recognition is done. Write and explain **.,
CO-; $O-; “ [20]
necessary steps

BL-
On a sentiment analysis dataset of 3 sentiments, how would you balance
Q the dataset and handle imbalance in data. Write and explain necessary
CO-; SO-; [20]
, steps
BL-

Which are the different word vectorization techniques ? Briefly explain any
2 methods.
Consider the following 3 sentences:

; a
Q - The quick brown fox jumps.over the lazy dog.
CO-; SO-;

BL-

[20]
- The lazy dog sleeps in the’sun.

- The brown cat and black dog are friends.
Perform word vectorization using Bag of Words model for these
sentences. Create a vocabular and represent each sentence as a count of

words frequencies. Provide the BoW representation for each sentence.
````

## 2024-25 · Re-Exam · Sem 5 · paper 76633af3ac45

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / CSE DATA SCIENCE, B TECH / EXTC, B TECH / I T, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing, Sem-V, Batch 2024-25 Re Exam.pdf` (+6 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 4 / 2/2026
- Text: ocr (6 pages), mean OCR confidence 91.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B TECH/MBA TECH Year: III/IV Semester: V/VII
Stream/s ; IT/COM/EXTC/CSE-DS/CS/AI/AIML/AIDS

Subject: Natural Language Processing Time: 3 hrs (_10am__to__Ipm_)
Date 4 / 2/2026 No. of Pages:_5_

Marks: 100

Re Examination(24- 25)
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any _4 _questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

[ Q1

a. | Explain the following feature representation techniques with appropriate example
CO-1,2 :
SO-1 MIs Bag of Words (BOW)

Answer briefly: [20]

BL2 il. One hot Encoding

€0-35 (|b: |=. ; : pees F

SO- 1: Discuss Lesk approach to implement Word Sense Disambiguation (WSD) with the
BL-2 help of suitable example

aa : E Ce Explain the concept of syntax parsing. Compare top-down and bottom-up approaches
BL23 to implement syntax parsing

eek abe Compare Natural Language Understanding and Natural Language Generation
SO-1 ; ay

BL-3 concepts. List some real world NLP applications that use these concepts

a | Consider the corpus given below.

Sentence 1: "The cat sat on the mat."
Sentence 2: "The dog barked at the cat."

Q2 Sentence 3: "I love my dog and my cat."
CO-2; [10]
SO-1; i. Create a vocabulary by removing the stop words {I, the, on, my, at, and}
BL-4,5 ii. Construct TF-IDF matrix

ili. Comment on prominent terms in the respective sentences

iv. Evaluate cosine similarity between sentence 1 and sentence 2
--- page 2 ---
b | Consider the following training corpus where counts and probabilities are given.

The weather data, with counts and probabilities

Outlook Temperature Humidity Windy Play
Yes | No Yes | No Yes | No Yes | No | Yes | No

Sunny 2 3 Hot | 2 2 High 3 4 False | 6 2 9 5

Overcast | 4 0 Mild | 4 2 | Normal | 6 1 True | 3 3
Rainy 3 2H Goole|x3 1

Sunny 2/9 | 3/5 | Hot | 2/9 | 2/5 | High 3/9 | 4/5 | False | 6/9 | 2/5 | 9/14 5/14 [10]
Overcast | 4/9 | 0/5 | Mild | 4/9 | 2/5 | Normal | 6/9 1/5 | True | 3/9 | 3/5
Rainy 3/9 | 2/5 | Cool | 3/9 | 1/5

Apply Naive Bayes classifier to determine the class for the foilowing test instance

A new day v4
Outlook Temperature Humidity Windy Play
Sunny Cool High True ®

Q3 a | Discuss the need for reference resolution. With the help of suitable examples,

} p iP.
CO-3; differentiate between Coreference resolution and Anaphora resolution. [05]
SO-1;
BL-3
co-3: b | With reference to discourse analysis, explain the terms cohesion, coherence and
SO-1; discourse markers with the help of suitable examples [05]
BL-2
co-3: |° With the help of suitable block diagram, explain various blocks in question answer
SO-1 i system. Discuss the role of question answering systems in real-world applications [10]
BL-2

pea. 4 | Define Natural Language Processing (NLP). Discuss a general NLP pipeline to build

ae NLP based system with the help suitable block diagram [05]
BL-2

b | Discuss the significance of linguistic building blocks such as morphology and syntax
CO-1: in developing NLP applications like machine translation or sentiment analysis.
SO-1: Provide examples to illustrate your answer. [05]
BL-2
--- page 3 ---
c | Consider the following training corpus.
Training corpus
<s> | love programming </s>
<s> Programming is fun </s>
<s> | love coding </s>
<s> Coding is great </s>

CO-2;
SO-1; Evaluate the most probable next word for the following test corpus using the bigram [10]
BL-4 language modelling.
Test corpus
i. <s> I love ------------
ii, <s> programming ----------------
iii. <s> coding ----------------
a_| Consider the following textual data.
“Natural Language Processing (NLP) is a field of artificial intelligence that focuses
on the interaction between computers and humans through natural language. The
ultimate objective of NLP is to read, decipher, understand, and make sense of
Qs human languages in a valuable way.”
on 8 Perform the following text preprocessing tasks and discuss their need in NLP [06]
BL-3 applications.

a. . Sentence segmentation

b. Lowercasing

c. Stop word removal. Consider the following stop words: {is, a, of, that, on, I,
the, and, to, in}

d. Tokenization

CO-2: b | With reference to text preprocessing techniques for textual data, explain with
S O-l: suitable examples the concept of stemming and lemmatization. List the names of [04]
BL2. any two stemmers and any two lemmatizers.

c | Based on the concept of reference resolution, answer the following questions-

is Discuss the significance of reference resolution.

: ii. With reference to Hobb’s Algorithm for pronoun resolution, explain
as) i binding theory, gender agreement, distance property and recency property. [10]
BL- 45 iii. For the given sentence, apply Hobb’s algorithm to determine the

: antecedent for the pronoun “he”. Identify and mention the property at each

step.

“John gave a book to Mary after he finished reading it."
--- page 4 ---
a | With reference to text corpora for NLP application answer the following-

Q6 i: Discuss some significant traits of a good corpus

CO-2; ii. Describe with suitable diagram various text corpus structures [10]
SO-1; iii. Explain Guttenberg, Annotated Text, Web and Chat Text and WordList

BL-2 corpora.

b | With reference to Hidden Markov Model (HMM) in the context of Part-of-Speech
(POS) tagging answer the following questions

i. Describe what is meant by transition probabilities in HMM and their role in

modeling.
ii. Clarify the term emission probabilities and their importance in the HMM

framework.
iii. Calculate the total number of combinations available for a given sequence of

states and observations.
CO-2; iv. Identify and discuss the disadvantages of using the HMM method for POS
SO-1; tagging tasks. [10]
Training corpus with POS tagging is given below. Construct transition

BL-3,4 Vv.
probability table and emission probability table using HMM method
Sentence Words Respective POS tag

ID

1 Alice will eat cookies Noun, Modal Verb, Verb, Noun

2} Bob can drink tea Noun, Modal Verb, Verb, Noun

3 They will watch movies __| Pronoun, Modal Verb, Verb, Noun
4 The cat is sleeping Determiner, Noun, Verb, Verb

a | With reference to Parts of Speech (POS) Tagging explain the following concepts
with suitable example

Q7
ied i. | Open words and Closed words [05]
Ea ii. © Chunki d Chinkin
BL-2 ii. unking an inking
b | Explain the concept of Named Entity Recognition (NER).Discuss various
CO-2; approaches to implement NER. State some real word applications where NER
SO-1; concept is applicable. [05]
BL-2
--- page 5 ---
¢ | With reference to vector space model, answer the following

i. Define target words, context window, context words, co-occurrence matrix
ii. - For the corpus given below construct a co-occurrence matrix for the target and
context words. Take the window size as one whole sentence.
iii. _ Evaluate the similarity between the vectors of the target words "boy-dog" and
"boy-sun" using the simple dot product.

CO-3; iv. Plot the target word vectors by considering only two dimensions: "kicked" and
SO-1; "field". [10]
BL-4,5 v. Comment on the results obtained in points iii above

“The bird flew across the sky. The cat watched the bird. The flowers grew in the
| garden. The bird rested on the tree. The cat slept near the tree.”

Target words: bird, cat, garden, flowers
Context words: sky, tree, garden, slept
--- page 6 ---

````

## 2023-24 · Final-Exam · Sem 5 · paper ebd3d53c7c42

- Departments: Artificial Intelligence, Computer Engineering
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing ,Final exam 2023-24.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 89.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE}
SCHOOL OF TECHNOLOGY MANAGEMENT }

Academic Year: 2023-2024 ee
Program/s: BTech/ MBA Tech Stream/s : Al/Computer/AIML Year: III/IV Semester: V/VII
Subject: Natural Language Processing Time: 03 hrs (10.00 to 1.00)
Date:__01 /12 _/ 2023 . No. ofPages:03 -

Marks: 100
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. ,

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
Answer briefly: [20]

c0-1;s0- | * Define Word Sense Disambiguation and Pronoun Resolution. Give an (5)
4 ;BL-2 example of each.
CO-2,3; b.
SO- 1;BL- Define WordNet. Describe the wordnet hierarchy. (5]
LZ

c. Assume that you have to do sentiment analysis on the given text. For'this

purpose, extract 3 features (x, to x3) from the given text. Description of
the three features is given below —
X1 = logy9(word count of the document)

CO-1,2 ; X2 = count(positive lexicon words)
SO- 1;
BL-4

[5]

X3 = count(negative lexicon words)

“I was amazed at how the product quickly it arrived. The customer service
was exceptional. The support team responded promptly and professionally.
I was not sad with my decision. Overall, my experience with them was

outstanding.”
--- page 2 ---
positive lexicon= {amazed, promptly, outstanding, great}

negative lexicon words= {horrible, sad, disgusting}

C0-2:s0- d. Compare the following supervised text classification approaches with
1; example- Binary classification, Multiclass classification, Multilabel | [5]
BL-4 classification .

A. Explain the structure of Text Corpus. What are the various | [10]
Q2 applications of text corpus in NLP?
c0-2,3; B. Differentiate between Lesk and Walker Algorithm for WSD. | [10]
S0-6; Calculate the sense score and disambiguate the sense of word
BL-2,4 “Bank” using Walker algorithm for given context: Money in this

bank fetches an interest of 8% per annum. .

A. Explain Hobb’s Algorithm. Discuss the steps with help of example | [10]
Q3 : and state it’s limitation.
CO-2; SO- B. Discuss need for Stemming. List different types of Stemming and | [10]
— differentiate between Stemming and Lemmatization.

A. Explain Lexical Semantics and Vector Semantics with suitable | [10]

example.
Q4 B. Consider the following corpus
c0-1.2; Sr.No Sentences [10]
SO-1; 1. Inflation increased unemployment <
BL-2 2. Company increased sales
3. Fear increased pulse

Calculate TF-IDF.
--- page 3 ---
A. Elaborate on Word Embeddings. Explain the steps in CROW model | [10]

with suitable diagram.

B. A training corpus with POS tagging is as given below [10]
Noun Modal Verb_ | Verb Noun
1 Rita aan teach Will
Noun Modal Verb | Verb Noun
2 Spot will see | Will
Q5 Noun Noun Verb Noun
CO-1,2; 3 Will Rita spot Geeta
SO-1; Noun Modal Verb | Verb Noun
alee 4 Geeta will pat Spot
With reference to Hidden Markov Model approach for POS tagging,
i. Evaluate transition probabilities table [3 Marks]
ii. Evaluate emission probabilities table [3Marks]
iii. Calculate the probability of the following sequence, given Initial
probability P(Noun)= 0.5, P(Modal Verb)= 0.25, P(Verb)= 0.25
[4 Marks]
Noun Modal Verb Verb Noun
Geeta will spot Rita “
A. Explain text classification pipeline in details with a suitable block [10]
06 diaorem
cou, B. Define the following with respect to Information Retrieval: [10]
50-1; BL- a) Vector Space Model
2,3 b) Term Frequency

c) Inverse Document Frequency
````

## 2023-24 · Final-Exam · Sem 10 · paper 0fb9e89dffca

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM X/NATURAL LANGUAGE PROCESSING/Natural Language Processing Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 83.2

````text
SVKM’S NMIMS’
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT ie
Academic Year: 2023-2024

Program/s: B. Tech Integrated ; ; Year: V Semester: x
Stream/s ; Computer Engineering
Subject: Natural Language Processing ~
Date:.27 / 04/2024
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper a and on the cover
of the Answer Book, which is provided for their use. ‘

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly: [20]

rani & Why NLP is hard? Explain different terms. [5]
aera bs Discuss the applications and limitations of N-gram model in NLP. [5]
CO- 1; SO- |-c.

1: BL? c Distinguish between CBOW and skip gram model. : [5]
CO-2 ; SO- | d. Explain working of Machine Translation in NLP. - [5]
1; BL-1 :

Q2 a Explain TF-IDF with the help of below sentences. [10]

F noe _ A: You must be the change you wish to see in the world.
; B: To observe change in the world, you must actively be the change.

CO-1; SO-

1; BL-2 ° b. Explain language models in NLP. [10]
Q3 a. Explain corpus-based semantic model with example. [10]
CO-1; SO- :

2; BL-4

Page -|
--- page 2 ---
CO-2; SO- | b. Discuss Long Short Term. Memory Networks in terms of NLP. 7 | [10]
2; BL-2

| a4 a. What do you understand by similarity in NLP? What are different metrics
CO-1; SO [10]
col to measure it? .
2; BL-2
. : 10
CO-2; SO- b Explain applications and Challenges of Entity Extraction. [10]
2; BL-2 .
Q5 a. Explain Neural Networks for sentiment analysis. ; [10]
CO-2; SO- ; se
2; BL-2
CO-2; SO- ee te |
2: BL? b. - Elaborate the role of NLP in Question Answering system appiication. [5]
CO-2; SO- . ar; .
(es Discuss text normalization steps in-NLP. [5]
2; BL-2
Qé6 a. : .
CO-2; SO-. illustrate how RNN works in NLP in terms of language modeling. [10]
1; BL-2
CO-2: SO- Explain different types of Named Entities in detail. [10]
, b. tat
2; BL-2
Q7 a. Discuss in detail about Information extraction. Why it is required? [10]
CO-2; SO- :
1; BL-2
CO-1; SO- . hs :
4: BL2 b. Explain workflow and applications of Part of Speech (PoS) Tagging. [10]

Passe -=
````

## 2023-24 · Final-Exam · Sem 3 · paper 7de2168c0696

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM III/Natural Language Processing/Natural Language Processing Batch 2023-24 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 89.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

Program:MTech ; Stream ; Artificial Intelligence Year: Il; Semester: III

Subject: Natural Language Processing Time: 03 hrs. (2PM__to_ 5PM)
Date:___ 21/11/2023 No. of Pages: 02

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper.

= 1)Question No. _1____ is compulsory.
2) Out of remaining questions, attempt any _4 questions.
3) In all___5_ questions to be attempted.
4)Internet access is allowed
5)Free to use any ML or DL algorithm

Questions marks

1. Which are the different word vectorization techniques? Briefly explain any two
methods.

Consider the following three sentences:
C01; $02: nls quick brown fox jumps over the lazy dog."
BL3 The lazy dog sleeps in the sun." 20
"The brown fox and the lazy dog are friends."
Perform word vectorization using the Bag of Words model for these sentences.
Create a vocabulary and represent each sentence as a numerical vector using
word frequencies. Provide the BoW representation for each sentence.

Ze You are working on a Sentiment analysis dataset having 3 classes of sentiments,
CO1; $02; positive, negative and neutral. There is class imbalance amongst the classes, how 20
BL3 would you deal with this scenario? Which library would you use to generate the *
Sentiment scores for raw text and elaborate on the merits of that library?
ze
Explain how a typical Named Entity Recognition system works? Take an
CO1; SO2; ; . ‘ ee
BL3 example and run it through Spacy’s NER system to identify the named entities in | 20
the sentence.
03; 3) 4. er .
oF Soni | How does LSTM help overcome the vanishing gradient problem of RNN’s? 20
2: Why are Keyword Extraction Algorithms Unsupervised in nature ? In the context
CO1; SO2; a A i
BL3 of e-commerce product descriptions, how can keyword extraction techniques, 20

such as RAKE or TF-IDF, be applied to improve search engine optimization

page|
--- page 2 ---
(SEO) and product discoverability on an online retail website? Provide spepific
examples of how this can benefit both the retailer and the customers.

6. Use topic model to extract top 10 topics from the below dataset —
CO1; SO2; kaggle.com/prakharprasad/mobile-reviews-topic-modeling/data 20
BL3 Write necessary code lines with parameters and write the top 10 topics, words
and their probabilities. '
Te Use evaluation metrics for judging the results of the topic models — perplexity
CO1; SO2; . es
BL3 score and coherence score. Compare the results with one other competitive 20

models — LSA or NMF.

Pay o-
````

## 2023-24 · Re-Exam · Sem 5 · paper 73570ed54f7e

- Departments: Artificial Intelligence, Computer Engineering
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing , Re-exam 2023-24.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 89.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING?
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

a

Program/s: BTech/ MBA Tech _ Stream/s : Al/Computer/AIML Year: III/IV Semester: V/VII
Subject: Natural Language Processing ; Time: 03 hrs (10:00 to oh
Date:__ 12 / 02 /2024 No. of Pages:04

Marks: 100 :

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql .
Answer briefly: [20]

CO-1 ; SO- | a. Compare between Anaphoric and Cataphoric reference with example. [5]
4 ;BL-3
CO-2,3; b. i
SO- 1;BL- Define corpora. Discuss any 5-corpus used in NLP. [5]
Lz
CO-1,2 ; c. Define the term "linguistic foundation" and explain its importancé in

O |s0-1; ; [5]
BL-12 Natural Language Processing

d. With reference to regular expression used for detecting a word pattern, write

the behavior of the following the following regular expression operators

i. “abe
CO-2 ; SO-
1; ii. abc$ [5]
BL-1 iii. [A-Z0-9]

iv. edjing|s

v. [abc]
Q2 A. Explain Lexical Resource? How wordlist corpus can be used to solve | [10]
CO-2,3; given Word Puzzle problem:
SO-6;
--- page 2 ---
BL-2,4 EIGII 7
Vv V
O;N|L

How many words of four letters or more can you make from given
puzzle? Each word must satisfy following conditions:

a. Each letter may be used once per word.
b. Each word must contain center letter.
c. There must be at least one 9-letter word.

B. List various applications of NLP and explain the limitations of NLP. [10]

A. Draw parse tree using top-down approach for the following sentence

“A restaurant serves dosas” [10]

Grammar Det: A
S—> NPVP Noun: restaurant, dosas

S—> Aux NP VP Verb: serves
S-— VP ._
NP -> Pronoun
NP — Proper-Noun

Q3 NP — Det Nominal
Nominal — Noun

CO-2; SO- Nominal — Nominal Noun
Nominal —- Nominal PP

2; BL-2,4 VP — Verb
VP > Verb NP
VP > VPPP
PP > Prep NP

B. With a suitable pipeline structure state and explain basic 110]

preprocessing steps on a blob of text with a suitable example

A. Elaborate on concept of Word Embeddings? Explain the steps in (10]

Skip-gram model with suitable diagram.
Q4 B. Define the following concepts of NLP with suitable examples (10]

CO-1.2; a. Part of Speech Tagging
SO-1;

BL-1,2 b. Entity Recognition

c. Chunking
d. Type Token Ratio
--- page 3 ---
A. Explain Lexical Semantics and Vector Semantics with suitable [10]

& example.

CO-1,2; B. Discuss the difference between the following supervised text | [10]
SO-1;

BL-2 classification approaches with example- Binary classification,

Multiclass classification, Multilabel classification

A. How does TF-IDF (Term Frequency-Inverse Document Frequency) | [10]

play a role in document representation and information retrieval?

Explain with help of Example.

B. A training corpus with POS tagging is as given below [10]

Noun Modal Verb | Verb Noun
1 Rita can teach Will
Noun Modal Verb | Verb Noun
2 Spot will =~ see Will
Q6 Noun Noun Verb Noun
CO-1,2; 3 Will Rita spot Geeta
SO-1;
BL-2,4,5 Noun Modal Verb | Verb Noun
4 Geeta will pat Spot

With reference to Hidden Markov Model approach for POS tagging,
i. Evaluate transition probabilities table [3Marks]
ii. Evaluate emission probabilities table [3Marks]
iii. Calculate the probability of the following sequence, given
Intitial probability P(Noun)= 0.5, P(Modal Verb)= 0.25,
P(Verb)= 0.25
Noun Modal Verb Verb Noun

Geeta will spot Rita
--- page 4 ---
A. State and explain various NLP use cases in Healthcare and Fitlance. [10]

B. Predict the sentiment of sentence 7 by implementing Naive Bayes

algorithm on the dataset given below.

SrNo | Text ; Sentiment
Q7 1 amaze, wonderful, great, positive
CO-2,3; 2 happy, happy, great positive
a 45 3 amaze, great, happy, disgust positive —
4 great, happy, wonderful positive
5 disgust, sad, terrible, great * | negative [10]
6 sad, terrible, sad, happy negative
7 great, happy, disgust, great ?
````

## 2023-24 · Re-Exam · Sem 10 · paper 2194dc901f93

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM X/NATURAL LANGUAGE PROCESSING/Natural Language Processing Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 87.9

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERIN

SCHOOL OF TECHNOLOGY MANAGEMENT nae

Academic Year: 2023-2024
Program/s: B. Tech Integrated Year: V Semester: X
Stream/s ; Computer Engineering

Subject: Natural Language Processing Time: 3 hrs ( 2.00 PM to 5.00 PM)

Date:_3/ 07/2024 No. of Pages:2

Marks: 100

ReExamination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of

the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
Answer briefly: [20]
CO-1 ; SO- | a. Define Natural Language Processing. Explain applications of NLP. [5]
1; BL-2
CO-1; SO- | b. What do you mean by N-gram model in NLP. (5]
o>) |4;BL-2
CO- 4; SO- | c. Explain Distributional Semantics in detail. [5]
1; BL-2
CO-2 ; SO- | d. Explain role of Chatbot in NLP. [5]
1; BL-1
Q2 a. Discuss Text Pre-processing steps in Natural Language Processing. [10]
CO-1; SO- :
1; BL-2
b. Explain Text Classification with Naive Bayes theorem with below example:
CO-1; SO- Sr no. Text Class [10]
1; BL-4 1 | absolutely loved this movie Positive
2 The acting was terrible Negative
3 The acting was awful Negative
4 The movie was not terrible Positive
5 | wouldn’t recommend it to anyone Negative

Page- |
--- page 2 ---
re

Classify movie reviews as either positive or negative based on the words”

‘awful’ and ‘terrible’.

Q3 a. . [10]

CO-1; SO- Explain word vectorization with any one technique.

2; BL-4

CO-2;SO- | b. Explain RNN for language modeling.

2; BL-2 [0]

a4 a. Explain word embedding with any one of its technique. [10]

CO-1; SO-

2; BL-2

c0-2:S0- | b. Explain Challenges of Entity Identification in Indian languages with 0)

2; BL-2 example.

Q5 a. Discuss applications of text classification and generation using RNN. [10]

CO-2; SO-

2; BL-2

CO-2; SO- . og

2: BL-2 b. Explain Text Summarization. [5]

CO-2; SO- ' 7 3 .

2: BL-2 G Explain TF-IDF in detail. [5]

Q6 a. Illustrate the basic concepts of Sentiment analysis using Long Short Term__| [10]

CO-2; SO-

1; BL-2 Memory Network.

CO-2; SO- i : ;

>: BL-2 b. Explain different approaches of Named Entity Resolution. [10]
7 a. Discuss in detail about relation extraction. Why it is required? [10]

CO-2; SO- :

1; BL-2

CO-1; SO- . : < . ,

1: BL.2 b. Explain any two Part of Speech (PoS) Tagging techniques in detail. [10]

Pase- 2
````

## 2022-23 · Final-Exam · Sem 5 · paper bf0fe88ad060

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing, 3rd Year, Sem-V, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 November 2022
- Text: ocr (4 pages), mean OCR confidence 85.7
- 1 page scanned sideways or upside down, turned upright before OCR

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
Academic Year: 2022-23

Programme: B. Tech (Artificial Intelligence) Year: III Semester: V

Subject: Natural Language Processing _

Marks: 100 -
Date: 22 November 2022 - Time: 10.00 am - 1.00 pm-
Durations: 3 (Hrs) -

No. of Pages: 3#1 2 O04
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:

CO-1;SO- | a. | What is the need of NLP system? Why it is difficult to process the natural
63 ,

BL-I languages?
CO-1;SO- | b. :
5; Explain different levels in language analysis with examples. [5]
BL-2
CO-3 ; SO- | c. . :
1; Discuss Chabot application for medical applications in brief. [5]
BL-1
CO-2;SO- | d. .
2; Discuss Sentiment analysis using logistic regression with example. [5]
BL-1
Q2 CO-2; a | Explain CBOW and Skip gram word embedding model architecture with r10]
SO-2; BL-2 neat diagram.

b What do you mean by Regular expressions and where it is used? Write
Q2
CO-3: SO- regular expression for the following cases. [10]
3 1*the set of all alphabetic strings.
BL-1,2

2. the set of all lower case alphabetic strings ending in a b.

In,
--- page 2 ---
3. the set of all strings from the alphabet a,b such that each a is immediately
preceded by and immediately followed by a b.

4. the set of all strings with two consecutive repeated words (e.g., “Humbert
Humbert” and “the the” but not “the bug” or “the big bug”).

5. all strings that start at the beginning of the line with an integer and that
end at the end of the line with a word.

6. all strings that have both the word grotto and the word raven in them (but
not, e.g., words like grottos that merely contain the word grotto).

7. write a pattern that places the first word of an English sentence in a

register. Deal with punctuation.

Q3 a Explain various text preprocessing applications with examples of each in [10]
CO-1; SO- brief.
5; BL-2
b
Use the Penn Treebank tag set to tag each word in the following sentences
from Damon Runyon’s short stories. You may ignore punctuation.
1. It is a nice night.
CO-1; SO-; 2. This crap game is over a garage in Fifty-second Street. . .
BL3 3..... Nobody ever takes the newspapers she sells . . . [10]
4..... I am sitting in Mindy’s restaurant putting on the gefillte fish, which
isa
dish I am very fond of, ...
5. What flights do you have from Milwaukee to Tampa?
Q4 a
sok _ Explain mention pair model with a working example in detail. [10]
BL-2
Q4CO-2; |b
SO-3; . a ee . 10
Discuss the text classification pipeline with a neat block diagram. [10]
BL-2
Q5 a What do you mean by text corpus? Discuss different types of text corpuses
CO-2; SO- with their characteristics and structure. [10]
3; * *
BL-1
Q5 b (i) Discuss Naive Bayes classifier for text classification. [10]

?/%
--- page 3 ---
CO-2; SO- (ii) By applying Naive Bayes Classifier in given below text data,
3:

BL+1,3 classify the test instance in relevant class?
docID _ words in document in c = China?
training set 1 Chinese Beijing Chinese yes
2 Chinese Chinese Shanghai yes
K Chinese Macao yes
4 Tokyo Japan Chinese no
test set 5 Chinese Chinese Chinese Tokyo Japan?
Q6 a
wo SO- Discuss word embeddings with global vectors. [10]
BL-2

b_ | Evaluate the Bag of words (Bow) vector representations and Term
Frequency-Inverse Document Frequency (TF-IDF) vector representation for
the given three movie reviews.

CO-1; SO- ;
6; e Review |: This movie is very scary and long [10]
BL-5 e Review 2: This movie is not scary and is slow
e Review 3: This movie is spooky and good
Q7 a
CO-3: SO. (i) Discuss Information Extraction Architecture with neat diagram.
-3; SO- “ : ; : : we ; [10]
l: (ii) Explain chunking and name entity recognition with proper
BL-2 example.
b (i) “You shall know a word by the company it keeps”. True or False.
Justify your answer with proper explanation and example.
(ii) | Suppose you have the following 4-dimensional word vectors for
CO-2; SO- ; the two words wl and w2 respectively:
15 [10]
BL-3

W1= [0.2,0.1,0.3,0.4] and w2=[0.3,0,0.2,0.5]

Calculate the cosine similarity between wl and w2? Are the words wl and
w2 similar or dissimilar?
--- page 4 ---
Tag _ Description Example Tag Description Example Tag Description Example
es ee ee

CC coordinating and, but, or PDT _ predeterminer all, both “BP verb non-3sg eat
conjunction present

CD cardinal number one, two POS possessive ending 's VBZ verb3sgpres eats

DT determiner a, the PRP personal pronoun J, you, he WDT wh-determ. which, that

EX existential ‘there’ there PRP$ possess. pronoun your, one’s WP   wh-pronoun _ what, who

FW foreign word meaculpa RB adverb quickly WP$ wh-possess. whose

IN preposition/ of, in, by |RBR_ comparative faster WRB wh-adverb how, where
subordin-conj adverb

JJ adjective yellow RBS - superlatv. adverb fastest $ dollarsign $

JIR comparative adj bigger RP particle up, off # poundsign #

JIS superlative adj wildest SYM symbol +,%, & left quote “or “

LS list item marker 1,2,One TO — “to” to a right quote or”:

MD modal can, should UH interjection ah, oops ( left paren Gd <

NN sing or mass noun llama VB sverbbaseform _— eat ) right paren Leh >

NNS _ noun, plural llamas VBD verb past tense ate 2 comma i

NNP propernoun, sing. JBM VBG verb gerund éating : sent-end punc . ! ?

NNPS proper noun, plu. Carolinas VBN_ verb past part. eaten : sent-mid punc :;...—-
````

## 2022-23 · Final-Exam · Sem 8 · paper 730b2a58f8d0

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/COMPUTER/Sem_08/NATURAL LANGUAGE PROCESSING/Natural Language Processing, Sem-VIII, Year 2022-23, Final Exam.pdf` (+1 identical copies)
- Printed on paper: duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 89.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS EN
Academic Year: 2022-2023
Program/s: __B.Tech/MBA Tech

Stream/s ; Computer_

Subject: ___ Natural Language Processing _ Time: __ 3 hrs (_10am to_1pm)
Date:_2_/05 / 2023 No. of Pages: 2
Marks: _100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks. i
5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Qi ‘
Answer briefly: [20]
pag SO-2; | a. Is NLP Science or Engineering? Justify your answer with examples. [5]
CO-1;SO-1 | b. What is a Language Model in NLP? [5]
BL-1
in. i SO-1; | ¢. Define Manhattan distance with appropriate example. [5]
es SO-2 | d. Differentiate between Stemming and Lemmatization. [5]
Q2
CO-1;SO-1; | a. What Is Text Classification? Discuss one technique of text classification. [10]
. ete a b. What is Tokenizing? Why do we need tokenization? Explain NLTK package [10]
BL
Q3 7 Discuss the role of Computational semantics and Distributional Semantics along with Advantages
CO-1; SO-2; wa . [10]
BL-2 of distributional semantics. 110]
CO-2; SO-1; i Explain the working of a Gated Recurrent Unit
BL-1
Q4
a SO-2; | a. Illustrate different approaches to NER. [10]
b. Describe word2vec in vector space model [10]
CO-1; SO-1;
BL-1
Qs a Discuss various Applications of LSTM and its limitations? [10]
CO-2; SO-2; | b.

BL-2 Explain Bleu Score with an example. [10]
--- page 2 ---
CO-1; SO-1;
BL-1

Q6

CO-1;SO-;2 | a.
BL-2 Discuss part of speech tagging with the help of one technique. [10]

CO-3; SO-1; Explain application Natural language processing in text summarization. [5]
BL-2 Describe the limitation of RNN [5]

CO-2; SO-1;
BL-2

Q7 a.

CO-2; SO-1 b. Elucidate the types of named entity recognition? [5]
BL-2

CO-3; SO-1;
BL-2

CO-1; SO-1;
BL-1

c. Describe the application Natural language processing in text extraction [10]

Write a short note on beam search [5]
````

## 2022-23 · Final-Exam · Sem 10 · paper 41af7ac49753

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM X/NATURAL LANGUAGE PROCESSING/Natural language Processing Batch 2022-23 Final0001.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 87.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023
Program/s: B.Tech Integrated .
Stream/s :Computer Engineering
Subject: Natural Language Processing _
Date:_26 /04 / 2023
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.

1) Question No. __1____ is compulsory.
2) Out of remaining questions, attempt any 4 _ questions.
3) Inall___5_ questions to be attempted.

_ r
¢ 4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
1
° Answer briefly: [20]
CO-1 ;SO-2 | a. . oe
: Discuss the Application of NLP. (5]
BL-2
come 1 b. List the Applications of the N-gram Model in NLP? [5]
CO-1;S0-1 fe ; ; _
: Explain computational semantics in NLP. {5]
BL-2
CO-2;S0-2 | d. . : —_
; Discuss the role of NLP in the application of Chatbot?. {5]
BL-1
Q2 a
E C0-1; $0-2; | b. Explain Tokenizing in detail with example [10]
coh $0.2: Illustrate how classification is done by using Bayes classifier [10]
BL-2
Q3 a What do you understand by similarity in NLP? what are different metrics to measure it.?
CO-1; SO-2; Compute the similarity between two sets A = {0, 1, 2, 5, 6} and B = {0, 2, 3, 5, 7, 9}. [10]
BL-2
b What are the main difficulties when training RNNs?Explain with example. How can you | [10]
CO-2; SO-2; .
BL2 handle them?
Q4 a.
oe 80-2; | b. Define word embedding and clearly explain one of its technique? [10]
CO-2: $0-2: Describe the Challenges of NER in Indian languages with examples. [10]
BL-2
Q5 a Outline the role of NLP in question Answering system and its applications. [10]

CO-2; SO-2; b 5 5 woe
BL-2: Discuss the Advantages, Disadvantages and limitations of RNN. {10}
--- page 2 ---
CO-2; SO-2;

BL-2

Q6

sr S0-2, Illustrate the basic concept of Recurrent Neural Network with the help of neat diagram [10]
CO-2; SO-2; Elucidate the working of NER. [10]
BL-2

Q7 Explain how Neural network can play a role in sentiment analysis of human beings?

Le sorh Define its various approaches. {10}
CO-1; SO-2; What is Part of Speech (POS) tagging? What are is techniques.? explain any one. {10}
BL-2
````

## 2022-23 · Final-Exam · Sem 3 · paper 8a6d989c8354

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM III/Natural Language Processing/Natural Language Processing Batch 2022 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 17 November 2022
- Text: ocr (1 page), mean OCR confidence 91.2

````text
SVKM’s NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINE! N
Academic Year: 2022-23

Programme: M. Tech (Artificial Intelligence) Year: II Semester: III
Subject: Natural Language Processing .

Marks: 100 -
Date: 17 November 2022. Time: 2.00 pm - 5.00 pm ~

Durations: 3 (Hrs)

No. of Pages: O4
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper.

1) Question 1 is compulsory. Attempt any two out of the three questions mentioned below.
2) Internet access is allowed

3) Free to use any ML or DL algorithm
4) Evaluation metrics and conclusion is to be mentioned with every problem statement

Questions marks

1. Apply the sentiment analysis approach to the following dataset -
Dataset Link -https://www.kaggle.com/code/ebenhoch/twitter-sentiment-word-
vector-animation/data
CO1; SO2; i) Divide the data into train and test set.
BL3 ii) Try 3 different models for sentiment analysis 50
iii) Subset the data if data is taking too much time to train.
iv) EDA and preprocessing to be performed with respect to the requirement

2. Apply text classification models for the following dataset-
Dataset Link - https://www.kaggle.com/datasets/amananandrai/clickbait-dataset
: . i) Divide the data into train and test set.
C03; S01; ii) Try 3 different models for text classification 50
BL3 iii) Subset the data if data is taking too much time to train.
iv) EDA and preprocessing to be performed with respect to the requirement

3. Apply topic modelling for the following dataset.
Dataset Link - kaggle.com/prakharprasad/mobile-reviews-topic-modeling/data

i) Perform topic modelling to extract 10 categories of mobile reviews for
CO1; SO2; se :
BL3 predicting the filters for reviews , 50

ii) Use evaluation metries to justify your topies - coherence score, perplexity
score

Iv)Use PyLdavis for visualization and perform EDA.

°

yy
````

## 2022-23 · Re-Exam · Sem 5 · paper f9a8b3480cd7

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/NATURAL LANGUAGE PROCESSING/Natural Language Processing, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 January 2023
- Text: ocr (5 pages), mean OCR confidence 88.5

````text
/ . SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Program: B. Tech (Artificial Intelligence) : Year: Il Semester : V
AcademicY ear: 2022-2023

Subject: Natural Language Processing Marks: 100

Date : 30 January 2023 Time: 10.00 am - 1.00 pm
Durations: 3 (Hrs)

No. of Pages:_ 4 +4 =5

Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4 _ questions.
-~> 3)Inall___5_ questions to be attémpted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: > [14/20]
CO-1; a. “The vocabulary of a corpus remains the same before and after text 15]
are normalization”. True or False. Justify your answer with an example.
CO-1 ; b. Explain the good traits for a textual corpora required for solving an NLP [5]
S05; had
CO-2 ; &
SO- 1; Differentiate between word2vec model and doc2vec model. [5]
BL-2
—~ | CO-2; d. “Natural language is full of ambiguities”. Explain what are the different
SO-2 ; we ; [5]
BL-2 types of ambiguities in natural language with example of each. 3
(a) Normalize the given text using sentence segmentation, tokenization,
stopword removal, lowercasing, and stemming. Observe the vocabulary
Q2 CO-2; before and after the normalization:
SO-2; “Tanisha and Simran are best friends. They play together with other friends. | [10]
BL-1 Tanisha likes to play badminton but Simran prefers to play online games.

Tanisha wants to be a badminton player. Simran wants to become an online

gamer.”
--- page 2 ---
(b) What do you mean by word embeddings? Explain the following feature

Q2 representation techniques with their advantages and disadvantages.
cO-3: (i) One hot encoding 110]
SO-5; (ii) Bag of words
Biel (iii) Bag of n-grams
(iv) TF-IDF
(a) (i) Differentiate between semantics and pragmatics.
Q3 (ii) For each sentence, identify whether the different meanings arise from
CO-1; _ | structural ambiguity, semantic ambiguity or pragmatic ambiguity? [10]
SO-5; L. Time flies lik
BL-1.2 . Time flies like an arrow
2. He crushed the key to my heart
COT |)
Describe Text classification using Naive Baye’s classifier with example.
SO-; BL- [10]
2
(a) Explain the following document similarity measures.
1. Jacquard similarity
Q4 2. Cosine similarity
3. Euclidean distance
CO-1; ; . [10]
SO-2; For the given corpus, calculate the above mentioned distance measures.
BL-2,3 co,
Assume no preprocessing is to be done. ;
D1: “Data is the new oil of the digital economy”
D2: “Data is a new oil”
Q4 CO-2; | (b)

63 Explain CBOW and Skip gram word embedding model architecture with 110]
; neat diagram.

BL-2
(a) When you create a password on a website often there are constraints on the
Q5 nature of the password. Suppose the constraints on the password are:
CO-2; 1) Password should be at least 8 characters long but not more than 15 | [10]
ae : characters.

2) Ie must have at least one special character from !%@*.

2/4
--- page 3 ---
7

3) It must have some letters and some digits - that is at least one letter and
one digit.

4) At least one of the letters should be a capital letter.

5) It should not have characters not listed above.

Assume you had a function called match (regexp,str) that returns True or
False depending on whether the regular expression regexp matches the

string str or not. Write regular expressions for each clause given in the

constraints
CO-2; (b)
SO-3; Discuss any two applications of NLP in brief. [10]
BL-2
Q6 (a)
CO-2; . . . . . . .
SO-1: Explain mention pair model with a working example in detail. [10]
BL-2
(b) Explain the following text classification evaluation parameters.
(i) Accuracy
CO-1; (ii) Precision
SO-6; [10]
BL-2 (iii) Recall
(iv) Fl score
(v) ROC-AUC curve
(a) Some defining characteristics of organization and facility as per the ACE
guidelines are as follows:
« An Organization entity must have some formally established association.
Q7 Typical examples are businesses, government units, sports teams, and
CO-3; formally organized music groups. Industrial sectors and industries are also 110]
SO-1; treated as Organization entities. (ACE Entity Guidelines v6.6, page 7)
BL-1

* A facility is a functional, primarily man-made structure. These include
buildings and similar facilities designed for human habitation, such as
houses, factories, stadiums, office buildings, gymnasiums, prisons,

museums, and space stations; objects of similar size designed for storage,

3/y
--- page 4 ---
such as barns, parking garages and airplane hangars; elements of
transportation infrastructure, including streets, highways, airports, ports,
train stations, bridges, and tunnels. Roughly speaking, facilities are artifacts
falling under the domains of architecture and civil engineering. (ACE Entity

Guidelines v6.6, page 22).

In the following text from the May 3, 2012 New York Times (A House Tour:
Yes, That House) mark the organizations by underlining them and writing
an ORG immediately above them; mark the facilities by underlining them
and writing FAC immediately above. If a particular piece of text is difficult

to mark only ORG or only FAC, mark it ORG/FAC.

“After the 9/11 attacks, the system changed radically. Now, anyone who
wants to tour the White House must apply through the office of his or her
representative in Congress, which forwards the names to the White House
for clearance... Once they get the green light, visitors show up at the
appointed time on 15th Street between E and F Streets and join the line to
enter through the southeast gate. Anyone who has flown on an airline in
recent years will recognize the familiar territory of identity checks and
electronic scans, although here you do get to keep your shoes on. At the
head of the line, rangers from the National Park Service check photo IDs

against a list of names.”

(b) (i) Discuss Part of speech tagging in brief.

CO-2: (ii) Assign Penn parts of speech tags to all the words in the following two Eto}
SO-1; sentences using the notation word/POS and sketch the parse tree:
Bia 1. John and Mary bought a refrigerator with three doors .

2. It was purchased from a very small store near their house .

NL
ZN

Yly
--- page 5 ---
Tag Description Example Tag Description Example Tag Description Example

cc coordinating and, but, or PDT   predeterminer all, both VBP verb non-3sg eat
conjunction present
CD cardinal number one, two POS   possessiveending ‘s _ VBZ_ verb3sgpres eats
DT determiner a, the PRP personal pronoun J, you, he WDT wh-determ. which, that
EX existential ‘there’ there PRP$ possess. pronoun your, one’s WP — wh-pronoun what, who
FW foreign word meaculpa RB adverb quickly WP$ wh-possess. whose
IN preposition/ of, in, by RBR_ comparative faster WRB wh-adverb how, where
subordin-conj adverb
JJ adjective yellow RBS © superlatv. adverb fastest $ dollar sign $
JIR   comparativeadj bigger RP particle up, off # pound sign #
JIS superlative adj wildest SYM symbol +,%, & “ left quote ‘or “
LS list item marker 1,2,One TO “to” to * right quote -or”
MD modal can, should UH interjection ah,oops   ( left paren LGi.<
NN sing or mass noun llama VB sverb base form eat ) right paren 1), } >
NNS _ noun, plural Hamas VBD verb past tense ate 5 comma ;
NNP   propernoun, sing. JBM VBG verb gerund eating . sent-end punc .!?
NNPS proper noun, plu. Carolinas VBN verb past part. eaten : sent-mid punc ‘3... —-
x

t/4
````

## 2022-23 · Re-Exam · Sem 8 · paper 7cd33bcf77b7

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/COMPUTER/Sem_08/NATURAL LANGUAGE PROCESSING/Natural Language Processing, Sem-VIII, Year 2022-23, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 85.5

````text
SVKM’S NMIMS V+)

aa

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023 ae?

Program/s: _B,Tech /MBA Tech Year: 4th Semester: VIII
Stream/s ;Computer Engineering
Subject: Natural Language Processing Time: 3 hrs (10 a.m to 1p.m)
Date:__03 /07_/ 2023 No. of Pages:_2
Marks: 100

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any _4__ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

ai
Answer briefly: [14/20]
CO-1;SO-1; | a. Define Normalization with example. [5]
BL-1
co-1; b. Why N grams are required? (5]
$O2;BL-2
CO-1;S0-2; | ¢ Explain Cosine similarities with example [5]
BL-2
“> CO-2;S0-1; | d. Write a short note on RNN (S]
BL-1
+ Q2 a
CO-1;SO-2; | b. Explain TF-IDF for Machine Learning [10]
BL-2 Explain text classifier using Naive baye’s method [10]
CO-1; SO-2;
BL-2
Q3 a. : . : . . '
What is Euclidean Distance? Find the distance between two points P(0, 4) and Q(6, 2).
CO-1; SO-1; [10]
BL-1 b. _ : a . [10]
CO-2; SO-2; . What are sequence models and explain its need in NLP and application with examples?
BL-2
a4 a. Explain entity named recognition.
ne SO-2; b. Explain Jacard distance. Calculate the Jacard similarities and Jacard distance between the following | [10]
L-2
two sets [10]
CO-2; SO-2;

BL-4 A=(0,1, 2,5, 6,8, 9]
--- page 2 ---
B=[0, 2, 3, 4,5, 7,9]

Qs

€0-2-;$0-2; Discuss the architecture of LSTM with neat diagram. [10]

BL-2

CO-2; SO-2; How Does Attention Work in Encoder-Decoder Recurrent Neural Networks? [10]

BL-3

Q6

ot S0-2; What are the challenges of NER in Indian Languages, explain with example? [10]

CO-2; SO-2;

BL-2 Explain application Natural language processing in question answering. [5]
a _— : lati

0-2; $0-2; Explain different methods to calculate performance evaluation in machine translation [5]

BL-2

Q7

CO-1; SO-2; Elucidate different steps in NLP. . i10]

BL-2 Define POS tagging . Why POS tagging required? why is tagging hard. How would you build a dictionary for the 110)

CO-1; SO-2; most frequent POS tagging algorithm?

BL-2

~
````

## 2022-23 · Re-Exam · Sem 10 · paper 978ca9953d50

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM X/NATURAL LANGUAGE PROCESSING/Natural Language Processing Batch 2022-23 Re Exam0001.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 86.0

````text
SVKM’S NMIMS .
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program/s: B.Tech Integrated Year: 5" Semester: X
Stream/s ;_ Computer Engineering '
Subject: _Natural Language Processing _
Date:_28 /06/ 2023
Marks: 100

cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
me 3$0-2; | a List and Explain the challenges of NLP [5]
CO-1; SO-2; | b. Discuss the limitations of N gram model. [5]
BL-1
ot 3SO-1; | c. What does distributional semantic mean in natural language processing? [5]
CO- 1; SO-1; | d. Explain Text Summarization. [5]
BL-2
Qe a Outline and discuss different approaches to NLP?
CO-1; SO-1; [10]
BL-2 " [10]
CO-1; SO-1; . What is Language Model? Explain with example. Why is it required.
BL-1
Q@ a Define word vectors. Explain any one technique with example.
CO-1; SO-2; [10]
BL-1 b [10]
CO-2; SO-2; ° Describe and explain clearly time back propagation (BPTT).
BL-2
Q4 ge .
a. Explain different NE types with examples
CO-2; SO-2;
BL-2 b. Distinguish between CBOW and Skipgram [10]
-2: SO-2: c. Find the Euclidean distance between points P(3, 2) and Q(4, 1). [5]
CO-2; SO-2;
BL-4 [5]
CO-1; SO-2;
BL-3
a. What are different types of Recurrent neural network?. Explain with diagram and example [10]
Q5
CO-2; $0-1; BI
BL-1 b. Discuss chatbot with reference to NLP.

CO-3; SO-2;
--- page 2 ---
BL-2

CO-1; SO-2:
BL-1

3

Explain TF-IDF.

[5]

06
CO-2; SO-2;
BL-2
CO-2; $O-2;
BL-2

Illustrate the working of LSTM Network .

Discuss different approaches to NER ?

[10]
[10]

Q
CO-2; SO-:2
BL-2
CO-1; SO-2
BL-2

Elucidate the concept of Relation extraction in text. Why is it needed?.

Write the Steps Involved in the POS tagging and what are the applications of Part of speech tagging.

{10]\
[10]
````

## 2021-22 · Final-Exam · Sem 6 · paper fc4c1de0aa2f

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/NATURAL LANGUAGE PROCESSING/B Tech, Data Science, Natural Language Processing, 3rd Year, Sem-VI, Final Exam, _94f5f2b6.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 19 April 2022
- Text: ocr (1 page), mean OCR confidence 92.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENG}
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING2S yy 5 1 S

Academic Year: 2021-22
Programme: B.Tech (Data Science) Year: III Semester: VI

Subject: Natural Language Processing
: Marks: 100
Date: 19 April 2022 Time: 10.00 am to 1.00 pm
Durations: 3 (hrs)
No. of Pages:
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper.
1) Attempt any two out of the three questions mentioned below - (Each Question is of 50 marks)

2) Internet access is allowed

3) Free to use any ML or DL algorithm

4) Evaluation metrics and conclusion is to be mentioned with every problem statement

Questions marks

4, Apply the sentiment analysis approach to the following dataset - .
Dataset Link - https://www.kaggle.com/yasserh/imdb-movie-ratings-sentiment-
analysis

C01; S02; i) Divide the data into train and test set. 50
BL3 ii) Try 3 different models for sentiment analysis
iii) Subset the data if data is taking too much time to train.
iv) EDA and preprocessing to be performed with respect to the requirement

2. Apply text classification models for the following dataset-
Dataset Link -
http://kdd.ics.uci.edu/databases/reuters2 1578/reuters2157 8.html?ref=hackernoon.
com
CO3; SO1; 50
BL3 i) Divide the data into train and test set.

ii) Try 3 different models for sentiment analysis
iii) Subset the data if data is taking too much time to train.
iv) EDA and preprocessing to be performed with respect to the requirement

3. Apply topic modelling for the following dataset.
Dataset Link - kaggle.com/prakharprasad/mobile-reviews-topic-modeling/data
C02; S01; i) Perform topic modelling to extract 10 emerging topics 50
BL3 ii) Use evaluation metrics to justify your topics - coherence score, perplexity
score

Iv)Use PyLdavis for visualization and iv) perform EDA.

VL
````

## 2021-22 · Final-Exam · Sem 8 · paper 56d113622f6f

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/COMPUTER/Sem_08/NATURAL LANGUAGE PROCESSING/Natural Language processing, Sem8,Final,2021-22.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 April 2022
- Text: ocr (3 pages), mean OCR confidence 89.4

````text
>

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN!

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERIN

Academic Year: 2021-22

Programme: B. Tech / MBA Tech (Computer) Year: IV Semester: VIII
Subject: Natural Language Processing

. P Marks: 100
Date: 16 April 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)

No. of Pages: _3
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:

os ;S$O-6; | a. | Define recurrent neural network in natural language processing. [5]
CO-1; 0-5; b. | Discuss five key steps involved in processing natural language with suitable [5]
BL-2 example.

as ;SO-1; | c. | Compare Word2Vec and Glove vector semantics. [5]
ol ;SO-2; | d. | Define named entity recognition (NER) in NLP [5]

a | Discuss the following terms with reference to text pre-processing with the help of
suitable example.

i. Tokenization

Q2 CO-1; SO- ii. Stemming [10]
2; BL-2 iii. Lemmatization

iv. Case folding

v. Stop word removal
ee = Define n-gram and illustrate with the help of suitable example. [10]

Cla)
--- page 2 ---
a | Suppose we are building a classifier that says whether a text is about sports
or not. Our training data has 5 sentences:
Text Tag
"A great game" Sports
Q3 "The election was over" Not sports
. _ [10]
eis SO-5; "Very clean match" Sports
"A clean but forgettable game" Sports
"It was a close election" Not sports
Evaluate which tag does the sentence “A very close game” belong to, using
Naive Baye’s Classifier?
CO-2;SO-; |b ;
—_ Describe markov assumption and hidden markov model with suitable example. [10]
a | For the given text A and B, where
A = "Al has transformed the way the world works"
Q4
CO-2; $O-2; B = "AJ has taken the world by storm [10]
BL-4 ;
Evaluate jaccard similarity and cosine similarity for the given text (Label the
solution with appropriate comments)
b
Q4 Correlate the concept of information extraction as the application of natural
CO-3; SO-3; . [10]
BL4 language processing.
Q5 2 | Describe Long Short Term Memory (LSTM) along with its applications in natural
Cites SOS: 1 rocessin ie
BLl anguage p. g.
= b Describe the ‘Question Answering’ as an application of natural language
CO-3; SO-3; . [10]
BL-l processing.
a 2 | Describe encoder and decoder for machine translation and illustrate with the help
CO-3; SO-1; ; . [10]
BL3 of suitable diagram.

(ola)
--- page 3 ---
Define Term Frequency-Inverse Document Frequency (TF-IDF). Evaluate the

Q6 measure of TF-IDF score for the given documents.
CO-1; SO-6; Document 1: It is going to rain today. [10]

BL-4 *
Document 2: Today I am not going outside.

Document 3: I am going to watch the season premiere.

(als)
````

## 2018-19 · Exam not stated · Sem 2 · paper 885f3ab9a6e0

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/NATURAL LANGUAGE PROCESSING/Natural Laguage Procesing 2018-2019.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 April 2019
- Text: ocr (3 pages), mean OCR confidence 87.3

````text
MUKESH PATEL SCHOOL OF TECHN EYAENT ENGINEERING

/ Program M Tech (Artificial Intelligence) Feat: I Semester: II

Academic Year: 2018-2019
Subject: Natural Language Processing Marks: 100
Date : 22 April 2019 Time2.00 pm to 5.00 pm
. Duration: 3 (hrs)
No. of Pages: 3

Final Examination (2018-19)

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _6_ is compulsory.

2) Out of remaining 5 questions, attempt any 3 _ questions.
3)Inall___ 4 questions to be attempted.

4) Question 6 carries 70 marks

5) All others carry 10 each

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Question 1: : 10 marks

Which of the following models can be used for the purpose of document similarity?

A) Training a word 2 vector model on the corpus that learns context present in the
document
B) Training a bag of words model that learns occurrence of words in the document

C) Creating a document-term matrix and using cosine si imitarity for each document
D) All of the above
--- page 2 ---
Question 2: : 10 marks
What is the right order for a text classification model componenis

1. Text cleaning

2. Text annotation
3. Gradient descent
4. Model tuning

5. Text to predictors

A) 12345
B) 13425
C) 12534
D) 13452
Question 3: 10 marks
Term Document
ai d2 d3 d4 d5 d6 a7
tl 2 1 0 0 0 0 0
f i 2 0 0 0 0 1
13 3 1 0 0 ] 1 0
t4 0 0 i 2° 1 1 1
ts 0 0 1 1 1 i 1
t6 0 a] 1 ot 0. 0 0

Question 3): Which of the following documents contains the same number of terms
and the number of terms in the one of the document is not equal to least number of
terms in any document in the entire corpus. 10 marks

A) d{ and d4
B) d6 and d7

C) d2 and d4
D) d5 and dé
--- page 3 ---
Question 4): Which are the most common and the rarest term of the corpus?

10 marks

A) 14, 16
B) 13, t8
C) #5, t1
D) #5, t6

Question 5) What is the term frequency of a term which is used a maximum number
of times in that document? 40 marks

A) t6 - 2/5
B) 13 - 3/6

C) t4- 2/6
D) ti - 2/6

Question 6:

Categorize complaints into categories: Data: and get the PyIDA Visualization

70 marks

https://drive.google.com/open?id=1C86ehVHUZUGqVwr4iOWlw6e8vwviY OME
````
