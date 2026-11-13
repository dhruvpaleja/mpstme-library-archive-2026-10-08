# Recommendation Systems: question papers in full

10 unique papers · 2023-24 to 2025-26 · Artificial Intelligence, AI and Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper 4ac3b4accaf2

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Recommendation Systems/QP_Recommendation Systems(702AI0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Recommendation Systems
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1   a.   Explain the various evaluation metrics for online recommender [5]
BL-2   systems.
CO-2   b.   Describe the different possible ways in which ratings can be [5]
BL-2   represented in a recommender system with suitable examples.
CO-2   c.   Differentiate between   content-based recommendation   and [5]
BL-2   collaborative filtering based on data usage and recommendation
approach.
CO-1   d.   Explain how contextual information is obtained in recommender [5]
BL-2   systems. Describe implicit, explicit, and inferred methods with
examples.
Q2   [20]
CO-   a.   Explain the concept of neighborhood formation in collaborative [10]
1,2   filtering. Identify (and justify by calculation) the top-2 nearest
BL-   neighbors for user U1 based on similarity. Analyse the importance
2,3,4   of selecting appropriate neighbors in prediction accuracy.
CO-2   b. A news application aims to recommend articles to users based on [10]
BL-4   the content of articles they have previously read. Analyze how a
content-based recommendation system can be developed for
personalized news delivery, focusing on feature representation,
********** 1 **********

[Text in pictures on this page, read by OCR]
in) 12 I3 15 16 17
ul 0 5 4 4 Oo 5
U2 5 3 4 4 2 2
U3 4 ie} 3 4 ie) ie}
U4 3 2 Oo ie} 3 ie)
US 3 4 3 3 Oo 4
--- page 2 ---
user profiling, similarity computation, and adaptation to changing
user interests.
Q3   [20]
CO-1   a.   Explain the concept of latent factor models in model-based [7]
BL-4   collaborative filtering. How do these models capture hidden
relationships between users and items? Illustrate your answer with
a suitable example.
CO-2   b.   For the given matrix, determine the U, V and ∑ using singular value [8]
BL-4   decomposition:
𝐴 = [0 2
2 0]
CO-   c.   Explain the difference between content-based and knowledge- [5]
1,   based recommender systems.
BL-2
Q4   [20]
CO-3   a.   For an online course recommendation system, the following table [10]
BL-3   shows actual ratings and predicted ratings for user Ravi.
i.   Compute the Mean Squared Error (MSE), Mean Absolute
Error (MAE), Root Mean Squared Error (RMSE) of the
predicted ratings.
ii.   Compute the Normalized MAE and RMSE, assuming all
ratings lie in the range {1 to 5}, and 0 is denoting the unrated
items.
CO-4   b. A smart city transportation system aims to recommend optimal [10]
BL-   travel routes to users based on contextual factors such as traffic
3,4   conditions, weather, time of day, and user preferences (cost vs. time
efficiency). Design a context-aware recommendation framework
by selecting and applying an appropriate paradigm (pre-filtering,
post-filtering, or contextual modeling). Justify your choice and
analyze how contextual factors influence route recommendations,
system scalability, and real-time adaptability.
Q5   [20]
CO-2   a.   For the given user-item matrix, the decomposed P and Q matrix are [7]
BL-   given. Assume that:
3,4
********** 2 **********
--- page 3 ---
i. Predict the missing ratings of R14, and R23.
ii. Compute the RMSE using only the known ratings.
iii. Update 𝑃11and 𝑄12 using one iteration of gradient descent for
rating 𝑅12.
iv. Assume learning rate 𝛼 = 0.01
CO-   b.   Explain how ratings are predicted in user-based collaborative [8]
2,   filtering. Given the following user-item ratings matrix, compute the
BL-   predicted rating for user U1 on item I4 using a neighborhood-based
2,3   approach (consider only similar users with available ratings).
Analyse the factors that influence the reliability of the predicted
rating.
CO-2   c.   Apply preprocessing and feature extraction techniques in a content- [5]
BL-4   based recommender system. Briefly explain how raw text data (e.g.,
product descriptions or movie summaries) is converted into useful
features for recommendation.
Q6   [20]
CO-3   a.   Consider a user Rohan, whose actual ratings for the following [10]
BL-3   mobile apps are: WhatsApp (3), Instagram (5), YouTube (4),
Telegram (2). The values in brackets represent his hidden ratings,
and higher values are better ratings.
The recommender system ranks them as:
Instagram, YouTube, WhatsApp, Telegram
(a) Calculate the Spearman rank correlation coefficient between the
user’s actual ratings and the predicted ranking.
(b) Calculate the Kendall rank correlation coefficient, and interpret
which metric better reflects the ranking quality in this case.
********** 3 **********

[Text in pictures on this page, read by OCR]
R=PxQ

Rating Matrix
Items
Ti Rn 13 14
U1 | 2.0 | 3.0 | 3.5 ?
U2 ? 4.0 ? 2.5
U3 | 3.0 ? ? 1.5
U4 2? 2.5 | 4.0 ?

User Matrix P

1.0 0.8
1.2 0.6
0.9 0.7
1.1 0.5

x

Item Matrix Q

14 10 08 0.6
0.6 1.2 1.1 1.3

i 12 13 14 15 16
Ul 5 4 0 2 3 )
u2 4 5 3 4 3 2
u3 5 4 4 5 4 3
u4 3 3 2 3 3 1
U5 4 5 4 4 4 2
--- page 4 ---
CO-3   b.   Assume two recommender systems: one uses only global average [6]
BL-4   ratings, and the other incorporates user and item biases. Analyze
how the inclusion of biases improves prediction quality.
CO-3   c.   Assume a recommender system is trained on a very sparse user- [4]
BL-2   item matrix. Explain why model-based collaborative filtering
performs better than neighborhood-based methods in this case.
Q7   [20]
CO-2   a. A content-based recommender system uses nearest neighbor   [10]
BL-4   classification to generate recommendations. Analyze how nearest
neighbor classification is applied in such systems to identify and
recommend relevant items, highlighting the role of similarity
measures and decision-making in the recommendation process.
CO-3   b.   Analyze how contextual modeling captures interactions between   [6]
BL-4   user, item, and multiple contextual factors, and explain why it is
considered more accurate yet computationally complex.
CO-3   c.   Analyze the impact of incorrect or noisy contextual data on the   [4]
BL-4   performance of a context-aware recommender system.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper b28c1a529f1e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIDS_7056/Recommendation Systems/QP_Recommendation Systems(702AI0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Recommendation Systems
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1   a.   Describe how recommender systems aim to increase user engagement [5]
BL-2   and retention, and how a recommender systems help users discover
new and relevant items.
CO-2   b. Explain   the   difference between user-based and item-based [5]
BL-2   collaborative filtering. Explain the advantage of combining clustering
with neighborhood-based collaborative filtering.
CO-2   c.   Describe the role of user profiles in content-based filtering.   [5]
BL-2
CO-1   d. Explain how contextual factors can influence recommendation [5]
BL-2   outcomes.
Q2   [20]
CO-   a.   Define sparsity and item bias in the context of recommendation [10]
1,2   systems. How does item bias influence recommendation results?
BL-   Compute the sparsity and item bias for each item using the following
2,3,4   dataset (Assume '0' represents missing values/ratings):
CO-2   b. Analyze the impact of different feature extraction techniques (e.g., [10]
BL-4   BoW vs TF-IDF vs Word Embeddings) on the quality of item
similarity computations.
********** 1 **********

[Text in pictures on this page, read by OCR]
Hh] 12 13 14 15 16
Ul 4 te) 3 5 4 (e)
U2 5 3 4 te) (e) 2
U3 te) 4 3 4 5 3
U4 5 5 te) 3 4 te)
--- page 2 ---
Q3   [20]
CO-1   a.   List and explain advantages and limitations of neighborhood-based [7]
BL-2   collaborative filtering.
CO-2   b. Design a Model-Based Collaborative Filtering System by explaining [8]
BL-4   its key components.
CO-1,   c.   Describe the types of data sources used in recommender systems. [5]
BL-2   Discuss the motivation behind using contextual information in
recommender systems?
Q4   [20]
CO-3   a. A user Shubham has true preference ratings for these songs:   [10]
BL-3   Shape of You (5), Perfect (4), Photograph (3), and Bad Habits (2).
The values in brackets represent his hidden ratings, and higher values
are better ratings.
The recommender system ranks them as follows:
Perfect, Shape of You, Photograph, Bad Habits.
(a) Calculate the Spearman rank correlation coefficient between the
user’s actual ratings and the predicted ranking.
(b) Calculate the Kendall rank correlation coefficient, and interpret
which metric better reflects the ranking quality in this case.
CO-4   b. Consider a Context-Aware E-commerce Recommendation System [10]
BL-   that uses the following contextual factors:
3,4   1. Device type (Mobile/Desktop)
2. User’s location (City/Region)
3. Time of access (Morning/Afternoon/Evening)
Based on the above design, develop an algorithm to integrate
contextual pre-filtering and post-filtering techniques into the
recommendation pipeline. Explain how each stage contributes to
improving personalization.
Q5   [20]
CO-2   a.   Explain what is meant by matrix factorization in the context of [7]
BL-   recommender systems. Using a small user–item matrix, show how
2,3   matrix factorization decomposes ratings into latent features.
CO-2,   b. Explain how clustering techniques help improve the efficiency and [8]
BL-   accuracy of Neighborhood-Based Collaborative Filtering (CF). Using
3,4   the same dataset (from Question 2 (part a)), calculate the cosine
similarity between users U1 and U3.
CO-2   c. Apply preprocessing techniques to prepare a text dataset for content- [5]
BL-3   based recommendation.
Q6   [20]
********** 2 **********
--- page 3 ---
CO-3   a. A recommender system predicts ratings for a user Meera for the [10]
BL-3   following movies. Higher values indicate stronger preferences.
(a) Compute the Mean Squared Error (MSE) of the predicted ratings.
(b) Compute the Normalized MAE and RMSE, assuming all ratings
lie in the range {1 to 5}.
CO-3   b. Compare SVD and SVD++ in terms of their mathematical structure, [6]
BL-4   data requirements, and ability to handle implicit feedback.
CO-3   c.   Describe the advantages of using model-based collaborative filtering [4]
BL-2   over neighborhood-based collaborative filtering.
Q7   [20]
CO-2   a.   Differentiate between supervised and unsupervised feature selection   [10]
BL-4   methods and discuss their implications for system scalability and
adaptability.
CO-3   b. Evaluate how contextual modeling contributes to personalization   [6]
BL-4   compared to non-contextual methods.
CO-3   c. Analyze how contextual information can reduce the cold-start   [4]
BL-4   problem in recommender systems.
********** 3 **********

[Text in pictures on this page, read by OCR]
Movies True Rating | Predicted Rating

Avatar 4.0 3.5
Titanic 5.0 4.6
The Martian 3.0 3.8
Gravity 2.0 2.5

Interstellar 5.0 47
````

## 2025-26 · Re-Exam · Sem 7 · paper d6befa5e4811

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/RECOMMENDATION SYSTEM/B Tech, (AI) Recommendation Systems, Sem VII, Batch 2023 & 2024, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 88.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026 .

Program/s: B.Tech /MBA.Tech Year: 4 Semester: VII

Stream/s : Artificial Intelligence ,

Subject: Recommendation Systems Time: _ 3 _ hrs (to2manto 44 Mp).
Date:_1 /'A/a5- No. of Pages:__ 3.

Marks: 100
—. .
: ReExamination (23-24 /24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
. Answer briefly: [20]

CO- 1; a.
SO-1 ; How do recommendation systems handle the cold-start problem? [5]
BL-2
Co- 1; b. : .
SO-1; Compare content-based recommendation system and a collaborative-based [5]
BL-2 recommendation system?

c. Explain Stochastic gradient descent method. Write the update equations for

Uiq and Vig using stochastic gradient descent method (with regularization)
CO-2 ; including
SO-1 ; , (i) Explicit feedback only [5]
BL-3 . (ii) Incorporating user bias and item bias
(iii) Incorporating implicit feedback.

CO-3 ; d. : . eye . a . 5
SO-1: Explain the different Similarity Function used in recommendation system? [5]

BL-2
--- page 2 ---
Consider a matrix that shows four users Alice, Ul, U2 and U3 rating on
different news apps. The rating range is from 1 to 5 on.the basis of user’s
likability of the news app. The “?” indicates that the user has not rated the app.


@ > .
CO-2; Alice | 5 4 1 4 2 [10]
SO-1; Ul 3 1 2 3 3
BL-3 U2 4 3 _|4 3 5
U3 3 3 1 5 4
Solve for the values of missing rating of Alice on BBC(5) using user based
collaborative filtering algorithm. Use the Pearson correlation coefficient.
A user rates 20 movies as either “liked” or “disliked.” Out of these, 11 movies
are disliked and 9 are liked. Among the 6 movies tagged with the genre
CO-3; ‘| “comedy,” 4 are disliked. :
SO-1; @) Compute the Gini index for the overall dataset. [10]
BL-5 (ii) Compute the Gini index for the subset of movies labelled
“comedy.” . .
(iii) Based on the Gini index values, discuss whether the genre label
“comedy” should be considered a useful feature for classification.
“NextStar has incorporated a recommender system into their application,
Q3 which provides personalized recommendations to users based on their ratings [10]
CO-3; and preferences. As the system becomes more sophisticated, it is critical to
SO-1; ensure that it provides accurate and relevant recommendations to users.” ;
BL-2 Explain how can NextStar test and evaluate their recommender system to
ensure it provides accurate and relevant recommendations to users.
Analyze the concept of matrix factorization and its application in the
CO-2; recommendation systems. Discuss the advantages and limitations of matrix
SO-1: factorization compared to other techniques and provide examples of real-world | [10]
BL-4 applications :
Q4 CO-2; . . 4 0 ; ae
For the given matrix A = [ | , Determine U, V and = using singular
SO-1; 30-5 — [10]
BL-5 vector decomposition.
CO-1; In an online fashion store, users frequently browse and purchase clothing
SO-1; items. Explain how a content-based recommender can use attributes like color, | [10]
BL-2 style, and brand to suggest similar products?
--- page 3 ---
Q5

Explain the optimization objective in unconstrained matrix factorization.

CO-2; a. Interpret the loss function and discuss how it is minimized using gradient [10]

SO-1; descent.

BL-5

CO-3; b. Explain the significance of precision, recall, and F1 score in evaluating

SO-1; recommendation systems. Why might accuracy alone be misleading in [10]

BL-2 imbalanced datasets? ,

Q6 a. A music streaming app wants to recommend songs based on time of day and

So user mood. Discuss how contextual modeling can be used to improve [10]

BL-6 recommendation quality.

CO-2: b. Compare the effectiveness of recommendation models trained on explicit 110]

SO-1; feedback versus those trained on implicit feedback. Which is more scalable

BL-2 and why?

Q7CO-4; ) a. Discuss how stochastic gradient descent (SGD) can be used to optimize a

SO-1; context-aware recommendation model. Illustrate the update rules for user, [10]
item, and context embeddings.

BL-6

CO-1,2; b. ;

SO-1; Explain how matrix factorization uses latent factors to model user-item

BL-2 : [10]

interactions. Discuss its advantages over neighborhood-based methods.
--- page 4 ---

````

## 2024-25 · Final + Re-Exam · Sem 7 · paper 4b870492a285

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/RECOMMENDATION SYSTEM/Recommendation Systems, Sem-VII, Final Exam 2024-25 & Re Exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (5 pages), mean OCR confidence 87.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGI
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025

Program/s: B.Tech / MBA.Tech Year: 4 Semester: VII

Stream/s : Artificial Intelligence

Subject: Recommendation Systeme “ Time: 3 __ hrs (lororamto Ls 00pm)
Date:_2 / 12/2024 No. of Pages: 5”

Marks: 100

Fina] Examination/Re Examination (2023-24)
2024-25 _
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use.

1) Question No. _ 1 is compulsory.

La ° as :
2) Out of remaining questions, attempt any __ 4 questions.
3)Inall___5_ questions to be attempted. ww

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh} page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly: [20]
CO-1;SO-1 | a. ;
; Explain the goals of recommender systems. [5]
BL-2 i
CO-1; SO-1 |b,
; Explain the basic components of content-based recommendation system. [5]
BL-2
c. Imagine you are using a restaurant recommendation app that suggests places
to eat based on your location. You are currently at a beachside resort, and its
_~| CO-4 ; SO-
11; noon. The app suggests seafood restaurants nearby. What contextual factors | [5]
BL-1 are influencing these recommendations, and how might the system prioritize
them?
d. Suppose you have an implicit feedback dataset in which the ratings are
CO-2 ; SO- : . A
1: unary. Explain would an ROC curve provide more meaningful results or [5]
BL-2 would the RMSE metric??
--- page 2 ---
Consider the following user-item rating matrix, where each Tow represents a
user, and each column represents an item. The values indicate ratings from 1
to 5. A blank space represents a missing rating.

a users Product 1 Product 2 Product 3 Product 4
: Ul 5 3 4 ?
U2 4 1 2 5
0-2 80 se : : ; i [10]
i; |. U4 ? 2 4 4
BL-6

Using user-user collaborative filtering with k=2, nearest neighbours, predict
the missing rating for User U1 for Item 4 using

(i) Pearson’s Correlation Coefficient Similarity measure

(ii) Adjusted Cosine Similarity Measure

Suggest which one should be preferred for user-user collaborative filtering
and why. aa

“ EduLearn, an online learning platform, offers a wide variety of courses
ranging from programming to design and business skills. Currently, EduLearn
uses a simple popularity-based recommendation system that suggests the most
enrolled courses to users. However, the platform's team has noticed that this
approach doesn't provide personalized recommendations tailored to individual
users’ interests. To address this, EduLearn has decided to implement a content-
based recommendation system that analyzes course metadata, such as course
descriptions, categories, instructor information, and keywords, to suggest
relevant courses to each user. The system will also incorporate users’ past
course enrollments, ratings, and interactions (such as completed modules and
courses they viewed) to recommend similar content that aligns with their
preferences. EduLearn faces several challenges in implementing the content-
0-1: SO- based recommendation system. These include how to effectively represent
1; course content, handle cold-start issues for new users with limited interaction
BL-1 data, and ensure that the recommendations are diverse rather than only

recommending courses highly similar to what users have already taken.”

[10]

Answer the following questions:

(i) How would you represent the course content in the content-based
recommendation system?

(ii) What methods would you use to extract relevant features from
course descriptions, and how would you represent users’
preferences based on their interactions with the platform?

(iii) | Once course content is represented, how would you compute

- similarity between courses and users’ preferences?

(iv) | How would you handle the cold-start problem for new users who
have little or no interaction data?
--- page 3 ---
(v) What strategies would you implement to provide relevant
recommendations to these users? .

Consider a user John whose actual preference ranking for a set of 5 movies is [te]
given by
John’s Actual Preference Ranking
1. Battleship
2. The Adam Project
Q3 3. Black Mirror: Bandersnatch
CO-3; SO- >. Door
1; BL-5 5.- Bird-Box ‘
The recommendation system’s ranked list of same set of movies is given by
a 1. The Adam Project
2. Anon a
3. Battleship a
4. Bird-Box Tey
5. Black Mirror: Bandersnatch
Determine the Kendall Rank Correlation Coefficient to evaluate the
agreement between the system's ranked list and the user's actual preference
ranking and interpret the result in terms of ranking quality.
CO-1; SO- (i) Explain the concept of implicit versus explicit feedback in the [05]
1; context of recommendation systems.
BL-2 (ii) Explain how matrix factorization can be used to predict ‘the
missing ratings in rating matrix. [05]
OF, RO For the given matrix A = [+ ~ 7| , Determine U, V and © using
SO-1; 1 4 [10]
BL-5 singular vector decomposition.
CO-1 ; SO-
4g Discuss the key properties of rating matrices in recommendation systems. [05]
For the given scenarios, identify which recommendation technique is to be
used with explanation.
(i) A user frequently reads science fiction books on an online
= ; So- bookstore. The system starts recommending more science fiction [05]

titles and books with similar themes (space exploration, futuristic
technology). The user then reads a mystery novel, and the system
begins to recommend books that combine elements of both science
fiction and mystery.
--- page 4 ---
(ii) A movie streaming service recommends films to a user based on
what other similar users have watched and rated highly. The user
who enjoys action films starts receiving recommendations for
action-thrillers and adventure movies, even though they haven't
watched or rated those specific genres yet.

Q5
CO-2; SO- a. Explain the unconstrained matrix factorization method with stochastic [10]
: , gradient descent and batch updates with incorporating user and item biases.
L- :
b. . . = ead leebe cverrauae : 7 [05]
(i) Explain the common challenges associated with neighborhood-based
CO-2; SO- collaborative filtering.
th. ad (ii) Why mean centering or mean normalization is mandatory in collaborative [05]
ne filtering? “\
26 a. ; ; — ; ; [05]
0-4-1850) (i) Identify a scenario where contextual pre-filtering would be useful in a
: recommendation system.
BL-3,1 (ii) What types of context can be used in contextual pre-filtering? [05]
b.
For the given user item rating matrix, the decomposed P and Q matrix are
given. «
Rating Matrix R Feature P Feature O
n %
=
CO-2; SO- [10]
1; Matrix
BL-1,6 factorization
, m me m on
Predict the missing ratings and compute the RMSE. Update the value of Ui1
and I1; for one iteration . Observe the changes in RMSE.
7 CO-2; a
sli Discuss the optimization problem in contextual recommendation system [10]
SO-1;BL-6 using stochastic gradient algorithm.
CO-1; SO- b. (i) Discuss the importance of serendipity, novelty and diversity in [05]

1;
BL-6 recommendation systems.
--- page 5 ---
y

CO-2; SO-
i;
BL-1

(ii)

What are the advantages of latent factor models over

neighborhood based collaborative filtering.

[05]

a
````

## 2024-25 · Final + Re-Exam · paper 66190d6317b1

- Departments: Artificial Intelligence
- Programmes: MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/Artificial Intelligence/Recommendation System/Recommendation Systems , Final exam 2024-25, Re-exam 2023-24.pdf`
- Text: ocr (6 pages), mean OCR confidence 73.9
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B.Tech / MBA.Tech Year: 4 ~~ Semester: VII

Stream/s : Artificial Intelligence

Subject: Recommendation Systems Time: 73 __ hrs (lorovamto1.260pm)
Date:_2 / 12/2024 No. of Pages: 5

Marks: _ 100

ee Ee omit Examination (2023-24)
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4___ questions.

3) Inall__5__ questions to be attempted.

4) All questions carry equal marks. '

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

1

. Answer briefly: [20]
CO-1; SO-1 | a,
z Explain the goals of recommender systems. [5]
BL-2
CO-1; SO-1 | b. :
; Explain the basic components of content-based recommendation system. [5]
BL-2 3

Cs Imagine you are using a restaurant recommendation app that suggests places
esate to-eat based on your location. You are currently at a beachside resort, and its
fale. a noon. The app suggests seafood restaurants nearby. What contextual factors | [5]
BL-1 are influencing these recommendations, and how might the system prioritize

them?

d. Suppose you have an implicit feedback dataset in which the ratings are

‘eae 100: unary. Explain would an ROC curve provide more meaningful results or [5]

BL2 would the RMSE metric??
--- page 2 ---
Consider the following user-item rating matrix, where each row represents a
user, and each column represents an item. The values indicate ratings from 1

to 5. A blank space represents a missing rating.

a users Product 1 Product 2 Product 3 Product 4
: Ul 5 3 4 2
U2 4 1 2 5
= U3 5 ? a 4
CO-2; SO- U4 2 2 4 4 [10]

BL-6 F
Using user-user collaborative filtering with k=2, nearest neighbours, predict

the missing rating for User U1 for Item 4 using
(i) Pearson’s Correlation Coefficient Similarity measure

(ii) Adjusted Cosine Similarity Measure

Suggest which one should be preferred for user-user collaborative filtering
and why.

b. “ EduLearn, an online learning platform, offers a wide variety of courses

ranging from programming to design and business skills. Currently, EduLearn

uses a simple popularity-based recommendation system that suggests the most

enrolled courses to users. However, the platform's team has noticed that this

approach doesn't provide personalized recommendations tailored to individual

users' interests. To address this, EduLearn has decided to implement a content-

based recommendation system that analyzes course metadata, such as course

descriptions, categories, instructor information, and keywords, to suggest

relevant courses to each user. The system will also incorporate users’ past

course enrollments, ratings, and interactions (such as completed modules and

courses they viewed) to recommend similar content that aligns with their

preferences. EduLearn faces several challenges in implementing the content-

C0-1: SO- based recommendation system. These include how to effectively represent
1; ; ; course content, handle cold-start issues for new users with limited interaction [10]

BL-1 data, and ensure that the recommendations are diverse rather than only
recommending courses highly similar to what users have already taken.”

Answer the following questions:

(i) How would you represent the course content in the content-based
recommendation system?

(ii) What methods would you use to extract relevant features from
course descriptions, and how would you represent users!
preferences based on their interactions with the platform?

(iii) | Once course content is represented, how would you compute
similarity between courses and users’ preferences?

(iv) | How would you handle the cold-start problem for new users who
have little or no interaction data?
--- page 3 ---
(v) What strategies would you implement to ‘provide relevant
recommendations to these users?

a: Consider a user John whose actual preference ranking for a set of 5 movies is [10]
given by
John’s Actual Preference Ranking
1. Battleship
2. The Adam Project
Q3 3. Black Mirror: Bandersnatch
CO-3; SO- Anceetion
1: BL-5 5.. Bird-Box s
The recommendation system’s ranked list of same set of movies is given by
1. The Adam Project
2. Anon
3. Battleship
4.. Bird-Box
5. Black Mirror: Bandersnatch
Determine the Kendall Rank Correlation Coefficient to evaluate the
agreement between the system's ranked list and the user's actual preference
ranking and interpret the result in terms of ranking quality.
CO-1;'S0- b (i) Explain the concept of implicit versus explicit feedback in the - [05]
1; ; context of recommendation systems.
BL-2 _ (ii) Explain how matrix factorization can be used to predict the
missing ratings in rating matrix. ; [05]
hb Coes Gp For.the given matrix A = [* E | , Determine U, V and = using
$O-1; laa [10]
BL-5 singular vector decomposition.
CO-1 ; SO- b.
ay P Discuss the key properties of rating matrices in recommendation systems. [05]
c. For the given. scenarios, identify which recommendation technique is to be
used with explanation.
(i) A user frequently reads science fiction books on an online
CO-1 ; so- bookstore. The system starts recommending more science fiction [05]
1; BL-

titles and books with similar themes (space exploration, futuristic
technology). The user then reads a mystery novel, and the system
begins to recommend books that combine elements of both science
fiction and mystery.
--- page 4 ---
(ii) A movie streaming service recommends films to a user based on
what other similar users have watched and rated highly. The user
who enjoys action films starts receiving recommendations for
action-thrillers and adventure movies, even though they haven't
watched or rated those specific genres yet.

Q5
CO-2; SO- a. Explain the unconstrained matrix factorization method with stochastic [10]
1; gradient descent and batch updates with incorporating user and item biases.
BL-2 :

(i) Explain the common challenges associated with neighborhood-based
CO-2; SO- collaborative filtering.
ee 4 (ii) Why mean centering or mean normalization is mandatory in collaborative [05]

= filtering?
Q6 a ; : : F ; [05]
—, (i) Identify a scenario where contextual pre-filtering would be useful in a
mo recommendation system.
BL-3,1 (ii) What types of context can be used in contextual pre-filtering? [05]
b.
For the given user item rating matrix, the decomposed P and Q matrix are
given.
Rating Matrix R Feature P Feature O
a b
(acne
CO-2; SO- em 10
1; Matrix fe Te 8 [ ]
BL-1,6 factorization 17 06: 44 0.4:
ie! ue_~+_--—_Y
n
Predict the missing ratings and compute the RMSE. Update the value of U11
and I11 for one iteration . Observe the changes in RMSE.
bbe a.

Tee: Discuss the optimization problem in contextual recommendation system [10]
SO-1;BL-6 using stochastic gradient algorithm.
CO-1; SO- b. 0) Discuss the importance of serendipity, novelty and diversity in [05]

1;
BL-6 recommendation systems.
--- page 5 ---
CO-2; SO- (ii) What are the advantages of latent factor models over [05]
1;
BL-1 neighborhood based collaborative filtering.
--- page 6 ---
~
````

## 2024-25 · Re-Exam · Sem 7 · paper 7a23d117f7b6

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/RECOMMENDATION SYSTEM/Recommendation Systems, Sem-VII, Batch 2023-24 & 2024-25, Re Exam.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 87.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B.Tech+MBA.Tech Year: 4" —- Semester: VII

Stream/s : Artificial Intelligence

Subject: Recommendation Systems ; : Time: 3 _ hrs (to:0oamto 4:00pm _)
Date:_20 / 2 / 2024 No. of Pages: 4

Marks: 100

Re Examination (2023-24)/24 2s

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions-carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

a Answer briefly: [20]
CO-1; SO-1 | a.
; Compare collaborative filtering and content based recommendation system. | [5]
BL-2
Con soola Ty, Explain the roles ofuser profiles and item profiles in a recommendation [5]
*BL-2 system?

c. A customer is browsing an e-commerce platform for clothing on a cold winter
aad ; SO- morning. The system recommends winter jackets, scarves, and boots. What [5]
BL-l contextual data might the recommendation system be utilizing, and how does

it improve the shopping experience?

co-1;so- | 4. Explain the concept of implicit versus explicit feedback in the context
1; of recommendation systems. [5]

BL-2
--- page 2 ---
Consider the following user-item rating matrix, where each row represents a
user, and each column represents an item. The values indicate ratings from 1 |
to 5. A blank space represents a missing rating. |

- users Product 1 Product 2 Product 3 Product 4
/ Ul 5 3 ? 4
Q2 U2 4 2) 1 ?
CO-2; SO- U3 2 5 4 3 [10]
1B U4 3 4 2 5
BL-6 Using user-user collaborative filtering with k=2, nearest neighbours, predict
the missing rating for User U1 for Item 3 using
(i) User-User similarity
(ii) Item-Item Similarity
Use Pearson’s correlation coefficient for user-user and adjusted cosine for
item-item similarity.
b: (i) What strategies can be used to mitigate the cold start problem for new users
CO-1; SO- and new items in neighbourhood-based collaborative filtering? [05]
1;
BL-1 (ii) How does cosine similarity differ from Pearson correlation in the context
of neighbourhood-based collaborative filtering? When would you prefer one [05]
over the other?
a. A movie streaming platform recommends movies to its users based on their
viewing history. The following table shows the predicted ratings and actual
ratings given by 5 users for 5 different movies: [10]
User Predicted Rating by system | Actual Rating by user
U1 4.2 5
U2 3.7 4
U3 2.8 3
Q3 ua 45 2
CO-3 ; SO- US - 1.9 2)
1; BL-5

The ratings are on a scale from | to 5. Based on the predicted and actual
ratings, determine the following error metrics to evaluate the performance of
the recommendation system:

1. Mean Squared Error (MSE)

2. Root Mean Squared Error (RMSE)

3. Mean Absolute Error (MAE)

4. Normalized Mean Absolute Error (NMAE)

5. Normalized Root Mean Squared Error (NRMSE)
--- page 3 ---
CO-2: So- b (i) What is the objective function used in matrix factorization for [05]

1; latent factor models, and how is it minimized?
BL-1
(ii) What role does regularization play in latent factor models? [05]
4. CO-2; 4 9 : .
2 ae For the given matrix A = iE °] , Determine U, V and = using
SO-1; 30-5 [10]
BL-5 singular vector decomposition.
CO-1; SO- b. . : Dow saree p
1; Discuss the main challenges in building a recommendation system. [05]
BL-6
@ Explain the various evaluation metrics for evaluation of recommendation
CO-3 ; SO- [05]
1; BL-2 systems,
Q5
CO-2; SO- a. Derive the equation for the loss function and the update equations for [10]
1, unconstrained matrix factorization method with batch gradient descent.
BL-6
b. : =e
COIS. (i) Explain the basic components of content-based recommendation system. | [05]
1,
BL-2 (ii) Explain the different preprocessing and feature selection techniques for
content based recommendation system. [05]
Q6 a.
CO-4; SO- Discuss the paradigms of context based recommendation system with [10]
1; example.
BL-3,1
b.
For the given user item rating matrix, the decomposed P and Q matrix are
given.
Item
CO-2; SO- [10]
1;
BL-1,6

Aa eee 25
abe 14°13 9 12
8 4 2 8

Item
--- page 4 ---
Predict the missing ratings and compute the RMSE. Update the value of Ui
and I11 for one iteration . Observe the changes in RMSE.

QTCO-2; Expiain the latent factor model for context-based recommendation system [10]
SO-1 ;BL-6 with all required equations with all assumptions.
b. Assume we have the following ratings matrix, with users u and items ig
users Item 1 Item 2 Item 3
Ul B) 3 ?
U2 4 ? 2
U3 1 1 iv
Incorporate the following user and item biases and randomly initialized latent
factors,
e User biases bur= 0.1, bu2= 0.2, bus= —0.1
® litem biases bi1= 0.1, biz= 0.05, bis= —0.05
CO-2; SO- e Latent factors pu and qi:
1; pu=[0.1, 0.2], pw=[0.0, 0.1] pus=[0.1, —0.1] F
BL-6 qi=[0.1, 0.1],   qi=[-0.1, 0.05] qa=(0.0, 0.2] | [0

e Learning rate = 0.01
e Regularization parameter = 0.02

Determine
(i) The predicted rating
(ii) The error
(iii) | Update the biases
(iv) Update latent factors
(vy) RMSE
````

## 2023-24 · Final-Exam · Sem 7 · paper 8755f70494ac

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/RECOMMENDATION SYSTEM/Recommendation System, Sem-VII, Final Exam, A Y 2023-24.pdf`
- Printed on paper: duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 87.2

````text
. SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024 pe
Program/s: B.Tech Year: 4" Semester: VII
Stream/s ; Artificial Intelligence
Subject: Recommendation System * esis Time: _03 hrs (19; 20 to [: 00 )
Date:_O) / 12/2023 No. of Pages:_24_

Marks: _ 100.

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
CO-1 ; a. . . .. re
SO-1; What is the difference between explicit and implicit feedback? [5]
BL-1
C02; b. _. a
SO-1; What are the advantages of matrix factorization for rating prediction? [5]
BL-1 .
O C03; 6 oo _
SO-1; Explain diversity and serendipity. [5]
BL-1
CO- 4; d. Explain matrix factorization technique for context aware recommendation
SO-1 ; system. [5]
BL-2
For the given rating matrix,
Batman Alice in Dumb and Equilibrium

Q2 ; Begins wonderland | Dumber

. User A 4 ? 3 5
CO-2; User B 2 5 4 2 [10]
80-1, ® User C 5 4 2 2
BL-5 User D 2 4 ? 3

User E 3 4 5 ?

Determine User C’s prediction for equilibrium using

1
--- page 2 ---
(i) user-user similarity. Use Pearson correlation as similarity function

and take K=2 ¥
(ii) item -item similarity. Use Adjusted cosine similarity and take
K=2.
b. Suppose we have a recommender system that suggests movie ratings to users.

We want to evaluate the system's performance based on the actual ratings
given by users and the predicted ratings generated by the recommender
system

(i) User 1 rates Movie A: 4.5
(ii) | User 2 rates Movie B: 3.0
* (ili) ~~ User 3 rates Movie C: 2.5
CO-2; (iv) User 4 rates Movie D: 5.0 ;
SO-3; [10]

BL-5 The recommender system predicts the following ratings:

(i) User 1, Movie A: 4.0
(ii) User 2, Movie B: 3.5
(iii) | User 3, Movie C: 2.0
(iv) User 4, Movie D: 4.5

Determine MSE, RMSE, MAE, NRMSE and NMAE. For the given scenario,
which is the best evaluation metric and why?

a.
For the given user item rating matrix, the decomposed P and Q matrix are
given. Predict the missing ratings and compute the RMSE. Update the value
of Ui and Ii; using two iterations. What changes you have observed in the
RMSE value after two iterations.

e
: Item [12]
Q3 w xX Y Z w xX Y Z
A A

Co-2; 4.5 | 2.0 1.2/0.8 1.5) 12| 10] 08

SO-1; LB | 40 3.5 Bl r4lo9 17| 06| 1.4] 04

BL-6,2 8 = xX

; ac 5.0 2.0 Cl 1si1.0
D | 3.5 | 4.0] 1.0 D| .2lo8

. ; User Item

Rating Matrix Matrix Matrix

Matrix Factorization of Movie Ratings Data
--- page 3 ---
son 4; b. (i) Explain the role of long tail problem in recommendation systems. [04]

BL-5 (ii) Compare contextual pre-filtering and post-filtering. a [04]

Q4 a. 2 3
For the give! trix A = i Vv = usi i

CO-2: or the given matrix [‘ ial , Determine U,V and using singular [10]

te vector decomposition.

b. (i) Compare user-user and item item similarity techniques in collaborative

CO-2; filtering. . {05}

SO-1; . .

BL-5 (ii) Explain cold start problem in recommendation system. What
recommendation technique will be helpful in avoiding cold start problem and [05]
how?

Q5

CO-2; a. Discuss the various preprocessing and feature selection techniques for [10]

SO-1; content based recommendation systems.

BL-6

b. (i) Explain the gradient descent slgorithm for optimizing the RMSE for [05]

So matrix factorization of rating matrix.

BL-2 (ii) Explain the use of regularization in optimizing RMSE value. How the [05]
regularization parameter can be selected?

a. Netflix has incorporated a recommender system into their application, which
06 provides personalized recommendations to users based on theif ratings and
CO-3: preferences. As the system becomes more sophisticated, it is critical to ensure [10]
SO-1; that it is providing accurate and relevant recommendations to users. How
BL-2 5 : y ; ‘
Netflix test and evaluate their recommendation system to ensure it provides
accurate and relevant recommendations to users?
CO-2; b. ‘ . . eA F
SO-l; Discuss Singular value decomposition for matrix factorization. Explain how [10]
BL-5,6 SVD can be used to predict the missing ratings in rating matrix.
--- page 4 ---
a. (i) Compare traditional recommendation system and

Q7 multidimensional recommendation system. 3 [05]
— (ii) Mention the optimization problem for matrix factorization in
BL-5 context modelling along with the update equations using batch [05]
gradient algorithm.
b.
Explain Briefly:
CO-2,3; (i) Online and Offline evaluation of recommendation systems [05]
pet (ii) Nearest neighborhood classification for content based
recommendation system.
[05]
````

## 2023-24 · Re-Exam · Sem 7 · paper 8cc04a3e60ba

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/RECOMMENDATION SYSTEM/Recommendation System, Sem-VII, Year 2023-24, Re Exam.pdf`
- Printed on paper: duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 88.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024
Program/s: B.Tech Year: 4° Semester: VII

Stream/s : Artificial Intelligence

Subject: Recommendation System Time: 3 hrs ( 10; 00 toliov pony

¥

Date: J2.-/02/2.024 - No. of Pages:_ 3
Marks: _100
Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. .

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary. :

Ql .
Answer briefly: [20]
aaae a. Explain why unary ratings are significantly different from other types of [5]
BL2. ratings in the design of recommender systems. ‘
oO CO- 1; b.
SO-1 ; Compare collaborative filtering and content based filtering. [5]
BL-2 :
CO-2 ; c ee ws , :
SO-1; What do you mean by “context” in context aware recommendation system? [5]
BL-1
. d. A system recommends 12 items, among which only 4 are relevant. In total,
CO-3 ; ‘ A : ‘ ;
SO-1 : there exist 8 relevant items. Determine the F1 measure of this system? [5]
BL-5. Consider the following ratings table between the five users and six items.
--- page 2 ---
Id >
1 P) 6 7 | 3 ?
4 2 4 2 3 4 =) 4
3 ? 3 4 1 1 ?
Q2 4 7 4 3 6 " 4
, 5 i ? 3 2 {2 5
CO-2; (i) Predict the values of missing ratings of user 2 using user based [12]
80-1 collaborative filtering algorithms. Use the pearson correlation
Blob coefficient with mean centering. ;
(ii) Predict the values of missing ratings of user 2 using item based
collaborative filtering al gorithms. Use the adjusted cosine
similarity.
Assume that a peer group of size at most 2 is used in each case, and negative
correlations are filtered out.
b. Consider a scenario in which a user provides like/dislike ratings of a set of 20
items, in which she rates 9 items as a “like” and the remaining as a “dislike.”
CO-2; Suppose that 7 item descriptions contain the word “thriller,” and the user
SO-1; dislikes 5 of these items. Determine the Gini index with respect to the original [08]
BL-5 data distribution, and with respect to the subset of items containing the word
“thriller.” Should feature selection algorithms retain this word in the item
descriptions?
a. “Amazon.com, founded in 1994, started as an online bookstore and has since
Q3 evolved into a vast e-commerce platform offering an extensive range of
products, from books and electronics to clothing and groceries. The company [10]
CO-4; recognized early on the importance of helping customers discover products in
SO-1; a convenient and personalized manner”. Discuss the use of coldaborative
BL-6 filtering and content based filtering for amazon.com recommender system to
enhance user engagement and to increase sales and revenue by encouraging
customers to explore and purchase products.
CO-2; b. In a user-based collaborative filtering system, what are the trade-offs between 10
SO-1; using various similarity metrics, such as cosine similarity, Pearson correlation, [10]
BL-I or Jaccard index? How do you choose the most appropriate metric for your
application?
Q4 CO-2; a. ; 3°41 . a
For the given matrix A = [ | , Determine U, V and = using singular
SO-1; -1 3 1 [10]
BL-5 vector decomposition.
aaa: im Explain the basic components of content based recommendation system. [10]
--- page 3 ---
BL-2

¥

Qs Discuss the optimization problem in unconstrained matrix factorization using
stochastic gradient algorithm using
CO-2; a (i) Explicit Feedback [10]
SO-1; (ii) Incorporating Implicit feedback
BL-6 (iii) incorporating user and item bias.
(iv)
b. Suppose we have a recommendation system for e-commerce, and we want to

evaluate its performance for recommending a specific product ("Product X")
to users. The system makes predictions, and we have a:ground truth dataset
that indicates whether users actually purehassd "Product X" (1 for purchased,
0 for not purchased),

0-3: Here's a small sample of the data:
SO-l ‘ e Total users = 20 [10]
BL-5 e Users who purchased "Product X" = 10

e Users who received a recommendation for "Product X" = 12
e Users who both received a recommendation and purchased
"Product X" = 6
Determine the evaluation metrices accuracy, precision, recall and F1 score.
What will you interpret from these evaluation metrices?

Q6 a.
con Discuss the paradigms for incorporating context in recommendation systems. [10]
BL-6
iain b. (i) What is the role of implicit feedback in recommendation systems? [05]
BL-1,6 (ii) Discuss SVD++ algorithm of matrix factorization. ‘ [05]

_
Q7 CO-4; a.
SO-1:BL- Discuss the optimization problem in contextual recommendation system [10]
g using stochastic gradient algorithm.

hs SO- : i xplain the goals of recommendation system.
_ b (i) Explain the goals of d y: 105)
BL-1 (ii) What do you mean by latent factors? Explain what is the effect of
CO-2; SO- increasing or decreasing the number of latent factors on the [05]
1;
"| BL-1 performance of recommendation systems?
````
