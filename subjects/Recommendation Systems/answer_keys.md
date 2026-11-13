# Recommendation Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d251bee6949d

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Recommendation Systems/ANS_Recommendation Systems(702AI0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (17 pages)

````text
SYNOPTICS
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
1. This question paper contains 17 pages.
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
Ans:   Evaluation metrics for recommender systems (offline evaluation)
include (1 Marks each):
1. CTR (Click-Through Rate)
Ratio of clicks to number of recommendations shown
2. Conversion Rate
Percentage of users who take desired action (e.g., purchase)
3. CTR per User / per Session
Measures engagement at user/session level
4. Conversion Rate per User / per Visit
Tracks effectiveness across sessions
5. A/B Testing
Compares two recommendation strategies in real-time
CO-2   b.   Describe the different possible ways in which ratings can be [5]
BL-2   represented in a recommender system with suitable examples.
Ans:   Ratings can be represented in different forms:
1. Explicit Ratings
o Direct user input (e.g., 1–5 stars)
o Example: Movie rated 4/5
2. Implicit Ratings
o Derived from user behavior
o Example: clicks, watch time, purchases
********** 1 **********
--- page 2 ---
3. Binary Ratings
o Like/Dislike, 1/0
4. Ordinal Ratings
o Ordered scale (poor → excellent)
5. Continuous Ratings
o Real-valued scores (e.g., 3.7/5)
CO-2   c.   Differentiate between content-based recommendation and [5]
BL-2   collaborative   filtering   based   on   data   usage   and
recommendation approach.
Aspect   Content-Based   Collaborative Filtering
Ans:   Item features (genre,
Data Used   User-item interactions
keywords)
Recommends similar   Recommends based on
Approach
items   similar users/items
Dependency Single user profile   Community data
Problem for new users &
Cold Start Problem for new users
items
Recommend similar
Example   “Users like you also liked”
movies
CO-1   d.   Explain how   contextual   information   is   obtained   in [5]
BL-2   recommender systems. Describe implicit, explicit, and inferred
methods with examples.
Ans:   Methods to Obtain Context:
1. Explicit Context (2 Marks)
o Directly provided by user
o Example: Selecting “Evening” or “Happy mood”
2. Implicit Context (2 Marks)
o Collected from behavior
o Example: browsing time, location from GPS
3. Inferred Context (1 Marks)
o Derived using models/algorithms
o Example: inferring mood from music listening
pattern
Q2   [20]
CO-   a.   Explain the concept of neighborhood formation in collaborative [10]
1,2   filtering. Identify (and justify by calculation) the top-2 nearest
BL-   neighbors for user U1 based on similarity. Analyse the
2,3,4   importance of selecting appropriate neighbors in prediction
accuracy.
********** 2 **********
--- page 3 ---
Ans:
Concept of Neighborhood Formation (2 Marks)
In user-based collaborative filtering, neighborhood formation
involves:
•   Identifying users with similar preferences (neighbors)
• Using a similarity measure (e.g., cosine similarity, Pearson
correlation)
•   Selecting Top-k nearest neighbors
• Using their ratings to predict unknown ratings
Users with similar past behavior will have similar future
preferences.
Similarity Calculation (Using Cosine Similarity) (4 Marks)
U1 vs U2
57
Similarity ≈   ≈0.94
√82 ⋅√45
U1 vs U3
53   53
sim(𝑈1, 𝑈3) =   =   ≈𝟎. 𝟗𝟗𝟑
√57 × 50 √2850
U1 vs U4
25   25
sim(𝑈1, 𝑈4) =   =   ≈𝟎. 𝟗𝟖𝟎
√50 × 13 √650
U1 vs U5
64   64
sim(𝑈1, 𝑈5) =   =   ≈𝟎. 𝟗𝟗𝟗
√82 × 50 √4100
Top-2 Neighbors = U5 and U3 (2 Marks)
Importance of Selecting Appropriate Neighbors (2 Marks)
1. Improves Prediction Accuracy
o Highly similar users give more reliable predictions
2. Reduces Noise
o Poorly matched neighbors introduce errors
3. Better Personalization
o Captures true user preferences
4. Trade-off in k Selection
o Too few neighbors → unstable predictions
o Too many neighbors → less relevant influence
CO-2   b. A news application aims to recommend articles to users based [10]
BL-4   on the content of articles they have previously read. Analyze
how a content-based recommendation system can be developed
********** 3 **********
--- page 4 ---
for personalized news   delivery,   focusing on   feature
representation, user profiling, similarity computation, and
adaptation to changing user interests.
Ans:   A content-based recommender system suggests news articles by
analyzing the content of previously read articles and matching them
with new articles. A content-based system effectively delivers
personalized news by modeling   article content and user
preferences, while continuous adaptation ensures relevance over
time.
(1 Marks)
1. Feature Representation of Articles (2 Marks)
• Convert articles into structured feature vectors
• Common techniques:
o TF-IDF vectors (keywords importance)
o Word embeddings (Word2Vec, BERT)
o Metadata (category, author, publish time)
Example: Politics article → high weights for words like election,
policy
2. User Profiling (2 Marks)
• Build a user profile based on previously read articles
• Methods:
o Aggregate feature vectors of read articles
o Weighted   profiles   (recent   reads given more
importance)
Example: If user reads tech articles → profile emphasizes AI,
gadgets
3. Similarity Computation (2 Marks)
• Compare user profile with candidate articles
• Common similarity measures:
o Cosine similarity (most widely used)
o Euclidean distance
•   Articles with highest similarity are recommended
4. Recommendation Generation (1 Marks)
• Rank articles based on similarity scores
•   Select Top-N articles for recommendation
5. Adaptation to Changing User Interests (2 Marks)
• Time-based weighting → recent behavior prioritized
• Decay functions → older interests gradually reduced
• Session-based updates → capture short-term preferences
• Feedback incorporation → clicks, reading time
Example: If user shifts from sports to finance, system adapts
accordingly
6. Advantages
•   Personalized recommendations
• No need for other users’ data
•   Effective for new/unrated articles
********** 4 **********
--- page 5 ---
7. Limitations
• Limited novelty (over-specialization)
• Cannot recommend diverse topics outside user profile
Q3   [20]
CO-1   a.   Explain the concept of latent factor models in model-based [7]
BL-4   collaborative filtering. How do these models capture hidden
relationships between users and items? Illustrate your answer
with a suitable example.
Ans:   (2 Marks)
Latent factor models are a class of model-based collaborative
filtering techniques that represent users and items in terms of
hidden (latent) features.
•   Instead of using direct ratings, they learn underlying factors
such as:
o Genre preference (e.g., action, romance)
o Quality, popularity, style
Working Principle (2 Marks)
• The user–item rating matrix is factorized into two lower-
dimensional matrices:
o User matrix (user × latent factors)
o Item matrix (item × latent factors)
•   Predicted rating:
𝑟̂𝑢𝑖= 𝑝𝑢 𝑇𝑞𝑖
where:
o 𝑝𝑢: latent vector for user
o   𝑞𝑖: latent vector for item
How Hidden Relationships are Captured (2 Marks)
1. Dimensionality Reduction
o Converts sparse matrix into compact latent space
2. Captures Implicit Patterns
o Learns relationships not explicitly visible
o Example: Users liking sci-fi and action may share a
hidden “high-intensity” factor
3. Generalization
o Predicts unknown ratings using learned patterns
4. Handles Sparsity
o Works even when many ratings are missing
Example (1 Marks)
Consider a movie recommendation system:
•   Latent factors:
o Factor 1 → Action intensity
o Factor 2 → Romance level
User / Movie Action Romance
User A   0.9   0.2
********** 5 **********
--- page 6 ---
Movie X   0.8   0.1
•   Predicted rating:
𝑟̂ = (0.9 × 0.8) + (0.2 × 0.1) = 0.72 + 0.02 = 0.74
High score → Movie X is recommended to User A
Latent factor models effectively capture hidden relationships by
mapping users and items into a shared feature space, enabling
accurate and scalable recommendations.
CO-2   b.   For the given matrix, determine the U, V and ∑ using singular [8]
BL-4   value decomposition:
𝑨 = [𝟎 𝟐
𝟐 𝟎]
Ans:   Compute 𝐴𝑇𝐴 (2 Marks)
𝐴𝑇𝐴= [0 2 [0 2 = [4 0
2 0] 2 0]   0 4]
Eigenvalues of 𝐴𝑇𝐴 (2 Marks)
𝜎1 = √4 = 2, 𝜎2 = √4 = 2
Thus,
Σ = [2 0
0 2]
Compute 𝑉(Eigenvectors of 𝐴𝑇𝐴) (2 Marks)
Since 𝐴𝑇𝐴= 4𝐼, eigenvectors can be standard orthonormal basis:
𝑉= [0 1 or 𝑉= 1 [1   1
1 0]   √2 1 −1]
Compute 𝑈 (1.5 Marks)
1
𝑈= 𝜎𝐴𝑉
Since 𝑉= 𝐼:
1   1 [0 2   [0 1
𝑈= 𝐴=   0] =   0]
2   2 2   1
Construct Σ (1.5 Marks)
Σ = [2 0
0 2]
Final Answer (1 Marks)
𝑈= [0 1   , Σ = [2 0   , 𝑉= [1 0
1 0]   0 2]   0 1]
This is also correct:
𝑈= [ 0 −1 ] , Σ = [2 0   , 𝑉𝑇= [−1 0
−1 0   0 2]   0 −1]
CO-   c.   Explain the difference between content-based and knowledge- [5]
1,   based recommender systems.
BL-2
********** 6 **********
--- page 7 ---
Ans:   Content-Based Recommender System (1 Marks)
• Recommends items based on user’s past preferences
• Uses item features (e.g., genre, keywords)
• Builds a user profile from previously liked items
• Example: Recommending similar news articles based on
reading history
Knowledge-Based Recommender System (1 Marks)
• Recommends items based on explicit knowledge of user
needs and domain rules
• Uses constraints, rules, or utility functions
• Does not rely on past ratings/history
• Example: Recommending a laptop based on budget, RAM,
and purpose
Key Differences (3 Marks)
Aspect   Content-Based   Knowledge-Based
Basis   Past user behavior   Explicit user requirements
Data Needed Historical data   Domain knowledge/rules
Cold Start   Problematic   Less affected
Technique   Similarity matching   Constraint/logic-based
Example   Movie recommendation Product configuration
Q4   [20]
CO-3   a.   For an online course recommendation system, the following [10]
BL-3   table shows actual ratings and predicted ratings for user Ravi.
i.   Compute the Mean Squared Error (MSE), Mean
Absolute Error (MAE), Root Mean Squared Error
(RMSE) of the predicted ratings.
ii.   Compute the Normalized MAE and RMSE, assuming all
ratings lie in the range {1 to 5}, and 0 is denoting the
Ans:   unrated items.
Compute Errors
|   Course   |   Error   (r −   p)   |   |Error|   |   Error²   |
|   Data   Science   |   0.5   |   0.5   |   0.25   |
|   Machine   Learning   |   0.8   |   0.8   |   0.64   |
|   Python   Basics   |   -0.3   |   0.3   |   0.09   |
********** 7 **********
--- page 8 ---
|   Deep   Learning   |   -0.5   |   0.5   |   0.25   |
| Statistics   | -0.8   | 0.8   | 0.64 |
MAE (Mean Absolute Error) (2 Marks)
0.5 + 0.8 + 0.3 + 0.5 + 0.8   2.9
𝑀𝐴𝐸=   =   = 0.58
5   5
MSE (Mean Squared Error) (2 Marks)
0.25 + 0.64 + 0.09 + 0.25 + 0.64   1.87
𝑀𝑆𝐸=   =   = 0.374
5   5
RMSE (Root Mean Squared Error) (2 Marks)
𝑅𝑀𝑆𝐸= √0.374 ≈0.61
Normalized MAE and RMSE
Rating range = 1 to 5 → range = 4
Normalized MAE (2 Marks)
𝑀𝐴𝐸   0.58
𝑁𝑀𝐴𝐸=   =   = 0.145
5 −1   4
Normalized RMSE (2 Marks)
𝑅𝑀𝑆𝐸   0.61
𝑁𝑅𝑀𝑆𝐸=   =   ≈0.1525
4   4
CO-4   b. A smart city transportation system aims to recommend optimal [10]
BL-   travel routes to users based on contextual factors such as traffic
3,4   conditions, weather, time of day, and user preferences (cost vs.
time efficiency). Design a context-aware recommendation
framework by selecting and applying an appropriate paradigm
(pre-filtering, post-filtering, or contextual Modelling). Justify
your choice and analyze how contextual factors influence route
recommendations,   system   scalability,   and   real-time
adaptability.
Ans:   Chosen Paradigm: Contextual Modeling (2 Marks)
In this scenario, contextual modeling is the most suitable approach,
where recommendations are generated using a User × Route ×
Context model.
Justification:
• Context (traffic, weather, time) is highly dynamic and
critical
•   Pre-filtering may discard useful data
•   Post-filtering may give suboptimal results
• Contextual modeling integrates all factors directly → more
accurate and adaptive
Framework Design (3 Marks)
1. Data Collection
• User Data: preferences (fastest route, lowest cost)
• Route Data: distance, tolls, estimated time
• Context Data:
********** 8 **********
--- page 9 ---
o Traffic (real-time congestion)
o Weather (rain, fog)
o Time (peak/off-peak hours)
2. Context Representation
• Multi-dimensional model:
Score = 𝑓(User,Route,Context)
3. Model Implementation
• Use a weighted scoring function:
Score = 𝑤1(time) + 𝑤2(cost) + 𝑤3(traffic) + 𝑤4(weather)
• Weights adjusted based on user preference (e.g., time-
sensitive vs cost-sensitive)
4. Recommendation Generation
• Rank routes based on score
• Recommend Top-N optimal routes
Influence of Contextual Factors (2 Marks)
1. Traffic Conditions
• High congestion → avoid route
• Real-time updates essential
2. Weather
• Bad weather → safer routes preferred
• May increase travel time
3. Time of Day
• Peak hours → alternate routes
• Night → faster but possibly less safe routes
4. User Preferences
•   Cost-sensitive → avoid toll roads
•   Time-sensitive → shortest travel time
System Scalability (1.5 Marks)
Challenges
• High-dimensional data (User × Route × Context)
• Large number of users and routes
Solutions
•   Distributed systems (cloud-based processing)
• Caching frequently used routes
•   Efficient indexing and approximate ranking
Real-Time Adaptability (1.5 Marks)
Requirements
• Continuous updates from traffic and weather APIs
•   Fast re-ranking of routes
Techniques
• Online learning models
• Incremental updates
• Event-driven recommendation updates
********** 9 **********
--- page 10 ---
Q5   [20]
CO-2   a.   For the given user-item matrix, the decomposed P and Q matrix [7]
BL-   are given. Assume that:
3,4
i. Predict the missing ratings of R14, and R23.
ii. Compute the RMSE using only the known ratings.
iii. Update 𝑷𝟏𝟏and 𝑸𝟏𝟐using one iteration of gradient descent
for rating 𝑹𝟏𝟐.
iv. Assume learning rate 𝛼 = 0.01
Ans:
Predict Missing Ratings (2 Marks)
R₁₄ (U1, I4)
[1.0,0.8] ⋅[0.6,1.3] = (1.0 × 0.6) + (0.8 × 1.3) = 0.6 + 1.04
= 1.64
R₂₃ (U2, I3)
[1.2,0.6] ⋅[0.8,1.1] = (1.2 × 0.8) + (0.6 × 1.1) = 0.96 + 0.66
= 1.62
Compute RMSE (Only Known Ratings)
Predicted Values & Errors (1 Marks)
Entry Actual Predicted Error Error²
U1,I1 2.0   1.88   0.12 0.0144
U1,I2 3.0   1.96   1.04 1.0816
U1,I3 3.5   1.68   1.82 3.3124
U2,I2 4.0   1.92   2.08 4.3264
U2,I4 2.5   1.50   1.00 1.0000
U3,I1 3.0   1.68   1.32 1.7424
U3,I4 1.5   1.45   0.05 0.0025
U4,I2 2.5   1.70   0.80 0.6400
U4,I3 4.0   1.43   2.57 6.6049
MSE (2 Marks)
18.7246
𝑀𝑆𝐸=   ≈2.08
9
RMSE (2 Marks)
𝑅𝑀𝑆𝐸= √2.08 ≈1.44
Update 𝑃11and 𝑄12using Gradient Descent (for 𝑅12) (3 Marks)
********** 10 **********
--- page 11 ---
Given
•   𝑟12 = 3
• 𝑃1 = [1.0, 0.8]
• 𝑄2 = [1.0, 1.2]
• Learning rate 𝛼= 0.01
Step 1: Predicted Rating
𝑟̂12 = (1.0 × 1.0) + (0.8 × 1.2) = 1 + 0.96 = 1.96
Step 2: Error
𝑒12 = 𝑟12 −𝑟̂12 = 3 −1.96 = 1.04
Step 3: Update Formula
𝑃𝑢,𝑘←𝑃𝑢,𝑘+ 𝛼⋅(2𝑒𝑢𝑖⋅𝑄𝑘,𝑖)
𝑄𝑘,𝑖←𝑄𝑘,𝑖+ 𝛼⋅(2𝑒𝑢𝑖⋅𝑃𝑢,𝑘)
Step 4: Update 𝑃11
𝑃11 = 1.0 + 0.01 × (2 × 1.04 × 1.0)
𝑃11 = 1.0 + 0.0208 = 1.0208
Step 5: Update 𝑄12
𝑄12 = 1.0 + 0.01 × (2 × 1.04 × 1.0)
𝑄12 = 1.0208
Final Updated Values
•   𝑃11 = 1.0208
• 𝑄12 = 1.0208
CO-   b.   Explain how ratings are predicted in user-based collaborative [8]
2,   filtering. Given the following user-item ratings matrix, compute
BL-   the predicted rating for user U1 on item I4 using a
2,3   neighborhood-based approach (consider only similar users
with available ratings). Analyse the factors that influence the
reliability of the predicted rating.
Ans:   In user-based collaborative filtering:
• Find users similar to the target user (U1)
• Use their ratings to predict missing values
•   Prediction is based on a weighted average of neighbors’
ratings
Prediction formula (standard neighborhood-based approach):
∑   sim(𝑢, 𝑣) ⋅ 𝑟𝑣,𝑖
𝑣∈𝑁(𝑢)
𝑟̂𝑢,𝑖=
∑   ∣sim(𝑢, 𝑣) ∣
𝑣∈𝑁(𝑢)
********** 11 **********
--- page 12 ---
where:
• 𝑁(𝑢)= set of similar users (neighbors) who have already
rated item 𝑖,
•   sim(𝑢, 𝑣) = similarity between users 𝑢and 𝑣(commonly
cosine similarity),
•   𝑟𝑣,𝑖= rating given by neighbor 𝑣to item 𝑖.
Similarity is computed only on items that both users have rated (co-
rated items). Unrated items (0) are ignored during similarity
calculation.
Identify Similar Users to U1
Use cosine similarity on co-rated items (I1, I2, I5):
U1 vector = [5, 4, 3]
Similarity with U2
U2 = [4, 5, 3]
𝑠𝑖𝑚(𝑈1, 𝑈2) ≈0.98
Similarity with U3
U3 = [5, 4, 4]
𝑠𝑖𝑚(𝑈1, 𝑈3) ≈0.99
Similarity with U4
U4 = [3, 3, 3]
𝑠𝑖𝑚(𝑈1, 𝑈4) ≈0.99
Similarity with U5
U5 = [4, 5, 4]
𝑠𝑖𝑚(𝑈1, 𝑈5) ≈0.99
Use Ratings for Item I4
User Rating on I4   Similarity
U2   4   0.98
U3   5   0.99
U4   3   0.99
U5   4   0.99
Predict Rating for U1 on I4
Weighted Sum
= (0.98 × 4) + (0.99 × 5) + (0.99 × 3) + (0.99 × 4)
= 3.92 + 4.95 + 2.97 + 3.96 = 15.80
Sum of Similarities
= 0.98 + 0.99 + 0.99 + 0.99 = 3.95
Final Prediction
15.80
𝑟̂14 =   ≈4.0
3.95
Factors Affecting Reliability
1. Similarity Measure
********** 12 **********
--- page 13 ---
o Better similarity → more accurate prediction
2. Number of Neighbors (k)
o Too few → unstable
o Too many → noisy
3. Data Sparsity
o Less overlap reduces reliability
4. User Rating Behavior
o Bias (strict vs lenient users) affects prediction
5. Quality of Data
o Noisy or inconsistent ratings reduce accuracy
CO-2   c.   Apply preprocessing and feature extraction techniques in a [5]
BL-4   content-based recommender system. Briefly explain how raw
text data (e.g., product descriptions or movie summaries) is
converted into useful features for recommendation.
Ans:   1. Text Preprocessing (2 Marks)
•   Tokenization: Split text into words
• Stop-word Removal: Remove common words (e.g., “the”,
“is”)
• Stemming/Lemmatization: Reduce words to root form (e.g.,
“running” → “run”)
• Lowercasing: Normalize text
Example:
“Action movies are exciting” → [action, movie, excite]
2. Feature Extraction (2 Marks)
• Convert processed text into numerical vectors:
(a) Bag of Words (BoW)
• Represents word frequency
(b) TF-IDF
• Assigns importance to words based on frequency and rarity
(c) Word Embeddings
• Dense   vectors   capturing   semantic meaning   (e.g.,
Word2Vec, BERT)
3. Use in Recommendation (1 Marks)
• Each item is represented as a feature vector
•   Similarity (e.g., cosine similarity) is computed between
items or user profile and items
• Items with highest similarity are recommended
Q6   [20]
CO-3   a.   Consider a user Rohan, whose actual ratings for the following [10]
BL-3   mobile apps are: WhatsApp (3), Instagram (5), YouTube (4),
Telegram (2). The values in brackets represent his hidden
ratings, and higher values are better ratings.
The recommender system ranks them as:
Instagram, YouTube, WhatsApp, Telegram
(a) Calculate the Spearman rank correlation coefficient
between the user’s actual ratings and the predicted ranking.
********** 13 **********
--- page 14 ---
(b) Calculate the Kendall rank correlation coefficient, and
interpret which metric better reflects the ranking quality in this
case.
Spearman Rank Correlation (4 Marks)
Formula:
Ans:   6∑𝑑𝑖 2
𝜌= 1 −
𝑛(𝑛2 −1)
Step: Compute 𝑑𝑖= Actual Rank −Predicted Rank
App   Actual Rank Predicted Rank 𝑑𝑖 𝑑𝑖 2
Instagram 1   1   0 0
YouTube 2   2   0 0
WhatsApp 3   3   0 0
Telegram 4   4   0 0
∑𝑑𝑖 2 = 0
Spearman Coefficient
6 × 0
𝜌= 1 −   = 1
4(16 −1)
Kendall Rank Correlation (4 Marks)
Total pairs
4(4 −1)
= 6
2
Pairwise Comparison
All pairs are in the same order → all concordant
• Concordant pairs = 6
• Discordant pairs = 0
Kendall’s Tau
𝐶−𝐷   6 −0
𝜏=   =   = 1
Total pairs   6
Interpretation (2 Marks)
• Spearman = 1 → Perfect rank agreement
• Kendall = 1 → All pairwise orderings match
Both metrics indicate perfect ranking quality
CO-3   b.   Assume two recommender systems: one uses only global [6]
BL-4   average ratings, and the other incorporates user and item
biases. Analyze how the inclusion of biases improves prediction
quality.
Ans:   In recommender systems, predictions based only on global average
rating (μ) ignore individual tendencies of users and items. Including
biases provides a more realistic baseline, significantly improving
accuracy before applying advanced models. (1 Marks)
Without Bias (Global Average Model) (1.5 Marks)
********** 14 **********
--- page 15 ---
•   Prediction:
𝑟̂𝑢𝑖= 𝜇
• Assumes all users and items behave similarly
• Leads to high error due to oversimplification
With Bias Model (1.5 Marks)
•   Prediction:
𝑟̂𝑢𝑖= 𝜇+ 𝑏𝑢+ 𝑏𝑖
where:
o 𝑏𝑢: user bias (e.g., user gives generally high ratings)
o   𝑏𝑖: item bias (e.g., popular item gets high ratings)
How Bias Improves Prediction (2 Marks)
1. Captures User Behavior
o Some users are lenient/strict raters
2. Captures Item Popularity
o Some items are inherently better or worse
3. Reduces Systematic Error
o Adjusts deviations from global mean
4. Better Personalization
o Predictions closer to actual user preferences
CO-3   c.   Assume a recommender system is trained on a very sparse user- [4]
BL-2   item matrix. Explain why model-based collaborative filtering
performs better than neighborhood-based methods in this case.
Ans:   In sparse user-item matrices, most entries are missing, making
similarity computation unreliable. Model-based collaborative
filtering is more effective in sparse datasets due to its ability to
learn latent structures and generalize beyond observed data.
(1 Marks)
Limitations of Neighborhood-Based Methods (1.5 Marks)
1. Insufficient Overlap
o Few co-rated items → poor similarity estimation
2. Unstable Neighbors
o Neighbors may not be reliable
3. Cold Start Intensified
o Hard to find similar users/items
Why Model-Based Methods Perform Better (1.5 Marks)
1. Latent Factor Learning
o Matrix factorization learns hidden patterns
2. Handles Sparsity
o Uses all available data to generalize
3. Better Generalization
o Predicts missing values effectively
4. Robust to Noise
o Less dependent on direct overlaps
********** 15 **********
--- page 16 ---
Q7   [20]
CO-2   a. A content-based recommender system uses nearest neighbor   [10]
BL-4   classification to generate recommendations. Analyze how
nearest neighbor classification is applied in such systems to
identify and recommend relevant items, highlighting the role
of similarity measures and decision-making in the
recommendation process.
Ans:   (2 Marks)
A content-based recommender system represents each item using
feature vectors (e.g., genre, keywords, TF-IDF). Nearest neighbor
(k-NN) is applied to identify items similar to a user’s preferences.
Working Process (3 Marks):
1. User Profile Construction
o Build profile from items liked by the user
o Example: If user likes action movies → profile
vector emphasizes “action”
2. Item Representation
o Each item is represented as a feature vector
3. Similarity Computation
o Compute similarity between user profile and items
o Common measures:
▪ Cosine similarity
▪ Euclidean distance
▪   Jaccard similarity
4. Nearest Neighbor Selection
o Select top-k most similar items (nearest neighbors)
5. Decision-Making
o Recommend items with highest similarity scores
o Ranking based on similarity
Role of Similarity Measures(2 Marks)
• Determine closeness between user preferences and items
• Higher similarity → higher recommendation priority
• Choice of metric impacts recommendation quality
Decision-Making Mechanism(2 Marks)
• Threshold-based selection or Top-k ranking
• Can include weighting (recent items, frequency)
(1 Marks)
k-NN enables personalized recommendations by selecting items
most similar to user preferences, making it simple yet effective.
CO-3   b.   Analyze how contextual modeling captures interactions   [6]
BL-4   between user, item, and multiple contextual factors, and
explain why it is considered more accurate yet
computationally complex.
Ans:   Contextual modeling extends traditional user-item interactions by
incorporating additional dimensions such as time, location, mood,
and device. (1 Marks)
********** 16 **********
--- page 17 ---
How it Captures Interactions (1 Marks)
• Models interaction as: User × Item × Context
• Example: A user may prefer different items in morning vs
night
Approaches (2 Marks)
1. Pre-filtering
o   Filter data based on context before recommendation
2. Post-filtering
o Generate recommendations first, then adjust using
context
3. Contextual Modeling (Direct)
o Integrate context directly into model (e.g., tensor
factorization)
Why More Accurate (1 Marks)
• Captures dynamic preferences
• Provides personalized and situation-aware
recommendations
Why Computationally Complex (1 Marks)
•   Increased dimensionality (multi-dimensional data)
• Sparse data problem worsens
• Requires advanced models and higher processing power
CO-3   c.   Analyze the impact of incorrect or noisy contextual data on   [4]
BL-4   the performance of a context-aware recommender system.
Ans:   Incorrect or noisy contextual data negatively affects recommender
performance. Accurate context is critical; noise handling and
preprocessing are essential for reliable recommendations.
(1 Marks)
Impacts: (2 Marks)
1. Reduced Recommendation Accuracy
o Wrong context leads to irrelevant suggestions
2. Poor User Experience
o Recommendations may not match user needs
3. Model Mislearning
o System learns incorrect patterns from noisy data
4. Increased Uncertainty
o   Difficult to identify true user preferences
Example (1 Marks)
•   If location data is incorrect, system may recommend
irrelevant nearby services
********** 17 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 3e9b931f795c

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIDS_7056/Recommendation Systems/ANS_Recommendation Systems(702AI0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (14 pages)

````text
SYNOPTICS
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
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1   a. Describe how recommender systems aim to increase user [5]
BL-2   engagement and retention, and how a recommender systems help
users discover new and relevant items.
Answer:
Increase User Engagement:
• Recommender systems show personalized and interesting
items, keeping users active longer.
•   Frequent, relevant suggestions encourage more clicks, views,
and purchases.
• Dynamic updates (based on recent activity) maintain
continuous user interest.
Enhance User Retention:
• By consistently offering valuable recommendations, users
trust and return to the platform.
• Builds a sense of personalization and loyalty over time.
Help Users Discover New & Relevant Items:
• Suggest items users might not find on their own (serendipity).
• Balance between familiar and new content to broaden user
experience.
• Match users with hidden but relevant products, movies, or
content based on patterns.
********** 1 **********
--- page 2 ---
CO-2   b. Explain the difference between user-based and item-based [5]
BL-2   collaborative filtering. Explain the advantage of combining
clustering with neighborhood-based collaborative filtering.
Answer:
1. User-Based Collaborative Filtering (UBCF):
• Finds users similar to the target user based on past ratings.
• Recommends items liked by those similar users.
• Focuses on user–user similarity (e.g., Pearson, cosine).
2. Item-Based Collaborative Filtering (IBCF):
• Finds items similar to the ones the user has already liked.
• Recommends items with high item–item similarity.
• More stable as item preferences change less frequently than
user preferences.
Aspect   User-Based CF   Item-Based CF
Similarity Focus Between users   Between items
Dynamic
Changes often   More stable
Behavior
Harder with many   Easier with fewer
Scalability
users   items
CO-2   c. Describe the role of user profiles in content-based filtering.   [5]
BL-2
Answer:
Definition:
• A user profile represents a user’s interests, preferences, and
behavior in a content-based filtering system.
Role in Recommendation:
•   Stores information about items the user has liked or interacted
with (e.g., movie genres, product features).
• Used to match new items with similar features to those in the
profile.
Profile Construction:
•   Built using explicit ratings or implicit feedback (clicks, views,
purchases).
• Continuously updated as the user interacts with more items.
Function:
• Acts   as   the   personalized   model   for   generating
recommendations.
• Ensures relevance by focusing on items that align with known
user preferences.
********** 2 **********
--- page 3 ---
CO-1   d. Explain how contextual factors can influence recommendation [5]
BL-2   outcomes.
Answer:
Definition:
• Contextual factors are situational conditions such as time,
location, weather, or mood that affect user behavior.
Dynamic Preferences:
• A user’s choices may vary across contexts (e.g., prefers
thrillers at night, comedies in the morning).
Improved Relevance:
•   Incorporating context tailors recommendations to the current
situation, not just past behavior.
Examples:
•   Location: Suggest nearby restaurants.
• Time: Recommend coffee in the morning, movies in the
evening.
• Mood: Suggest upbeat songs when happy.
Outcome:
• Context-aware systems deliver more accurate, personalized,
and situationally appropriate recommendations.
Q2   [20]
CO-   a. Define sparsity and item bias in the context of recommendation [10]
1,2   systems. How does item bias influence recommendation results?
BL-   Compute the sparsity and item bias for each item using the
2,3,4   following dataset (Assume '0' represents missing values/ratings):
Answer:
5 Marks
1. Sparsity:
• Represents the proportion of missing ratings in the user–item
matrix.
• Formula:
−No. of observed ratings
Sparsity = 1
Total possible ratings
2. Item Bias:
• Measures how an item’s ratings differ from the global average.
• Formula:
********** 3 **********
--- page 4 ---
𝑏𝑖= 𝑟𝑖ˉ −𝑟𝑔𝑙𝑜𝑏𝑎𝑙 ˉ
• A positive bias → item generally rated higher than average.
• A negative bias → item rated lower than average.
3. Effect on Recommendations:
• Items with higher bias are more likely to be recommended.
• Helps correct for systematic item-level rating tendencies,
improving fairness and prediction accuracy.
Solution 5 Marks:
Total entries = users × items = 4 × 6 = 24.
Count non-missing ratings (ignore zeros):
• Non-missing per item: I1=3, I2=3, I3=3, I4=3, I5=3, I6=2.
•   Total non-missing = 17.
Sparsity
Sparsity = 1 −17 = 1 −0.70833 = 0.29167  (≈29.17%)
24
Global mean (mean of all observed ratings):
• Sum of all non-missing ratings = 65 → Global mean =
65/17 ≈3.88235.
Item means (only non-missing values):
•   I1: (4 + 5 + 5)/3 = 14/3 = 4.6667
•   I2: (3 + 4 + 5)/3 = 12/3 = 4.0000
•   I3: (3 + 4 + 3)/3 = 10/3 = 3.3333
•   I4: (5 + 4 + 3)/3 = 12/3 = 4.0000
•   I5: (4 + 5 + 4)/3 = 13/3 = 4.3333
•   I6: 2+3 = 5 = 2.5000
2   2
Item bias = (Item mean − Global mean):
•   I1 bias = 4.6667 −3.88235 ≈+0.7843
•   I2 bias = 4.0000 −3.88235 ≈+0.1176
•   I3 bias = 3.3333 −3.88235 ≈−0.5490
•   I4 bias = 4.0000 −3.88235 ≈+0.1176
•   I5 bias = 4.3333 −3.88235 ≈+0.4510
•   I6 bias = 2.5000 −3.88235 ≈−1.3824
Sparsity: 0.2917 (29.17%)
Global mean: 3.8824
Item   Item
Item
Mean   Bias
I1   4.6667 +0.7843
I2   4.0000 +0.1176
I3   3.3333 −0.5490
I4   4.0000 +0.1176
I5   4.3333 +0.4510
I6   2.5000 −1.3824
********** 4 **********
--- page 5 ---
CO-2   b. Analyze the impact of different feature extraction techniques (e.g., [10]
BL-4   BoW vs TF-IDF vs Word Embeddings) on the quality of item
similarity computations.
Answer:
Bag of Words (BoW):
• Represents items by raw word counts.
• Simple and fast, but ignores word importance and meaning.
•   Similarity depends on exact word overlap, leading to lower
semantic accuracy.
TF-IDF (Term Frequency–Inverse Document Frequency):
• Weights rare but important words higher.
• Reduces the influence of common terms (e.g., “movie”,
“good”).
• Produces more accurate similarity than BoW by focusing on
distinctive terms.
Word Embeddings (e.g., Word2Vec, GloVe):
• Represent words in continuous vector space capturing
semantic meaning.
• Compute similarity based on context and relationships
between words.
• Provide high-quality, semantic item similarity, even for
different but related words.
Q3   [20]
CO-1   a.   List and explain advantages and limitations of neighborhood- [7]
BL-2   based collaborative filtering.
Answer:
1. Advantages:
1. Simplicity: Easy to understand and implement (based on
similarity measures).
2. No Training Required: Works directly on the user–item rating
matrix.
3. Personalization:   Provides   highly   personalized
recommendations.
4. Interpretability: Easy to explain (“recommended because
similar users/items liked it”).
5. Domain Independence: Doesn’t need item features or
metadata.
2. Limitations:
1. Data Sparsity: Struggles when few ratings are available.
2. Scalability: Similarity computations become costly for large
datasets.
3. Cold Start Problem: Cannot recommend for new users or items
with no history.
4. Dynamic Updates: Recomputing similarities for new data is
time-consuming.
5. Limited Accuracy: Performance decreases with noisy or biased
ratings.
********** 5 **********
--- page 6 ---
CO-2   b. Design a Model-Based Collaborative Filtering System by [8]
BL-4   explaining its key components.
Answer:
User–Item Rating Matrix:
•   Input data showing user ratings or interactions with items.
• May include explicit (ratings) or implicit (clicks, views)
feedback.
Feature Extraction / Latent Factors:
• The model learns hidden (latent) features representing user
preferences and item characteristics   (e.g., via Matrix
Factorization).
Model Training:
• Algorithms such as SVD, ALS, or Neural Networks learn
patterns and predict missing ratings.
•   Objective: minimize prediction error (e.g., MSE) with
regularization to avoid overfitting.
Prediction Engine:
• Estimates unknown ratings using learned parameters:
𝑟̂𝑢,𝑖= 𝑝𝑢 ⊤𝑞𝑖+ 𝑏𝑢+ 𝑏𝑖
where 𝑝𝑢, 𝑞𝑖are latent vectors.
Recommendation Generator:
• Ranks items by predicted ratings and recommends top-N items
for each user.
CO-1,   c. Describe the types of data sources used in recommender systems. [5]
BL-2   Discuss the motivation behind using contextual information in
recommender systems?
Answer:
1. Types of Data Sources in Recommender Systems:
1. Explicit Data:
o Direct user input such as ratings, likes, or reviews.
o Indicates clear preferences.
2. Implicit Data:
o Indirect behavior data like clicks, purchases, watch
time, or browsing history.
o Easier to collect but noisier.
3. Content Data:
o Information about item   attributes   (e.g., genre,
keywords, price).
4. Demographic Data:
o User profile details such as age, gender, or location.
5. Contextual Data:
o Situational factors like time, device, mood, or location
during interaction.
2. Motivation for Using Contextual Information:
• Improves relevance by adapting recommendations to the user’s
current situation.
********** 6 **********
--- page 7 ---
• Captures dynamic preferences (e.g., different choices at work
vs. home).
• Enhances personalization and satisfaction by delivering
timely, context-aware results.
Q4   [20]
CO-3   a. A user Shubham has true preference ratings for these songs:   [10]
BL-3   Shape of You (5), Perfect (4), Photograph (3), and Bad Habits (2).
The values in brackets represent his hidden ratings, and higher
values are better ratings.
The recommender system ranks them as follows:
Perfect, Shape of You, Photograph, Bad Habits.
(a) Calculate the Spearman rank correlation coefficient between
the user’s actual ratings and the predicted ranking.
Answer:
True   True Rank   System Rank
Song
Rating   (R₁)   (R₂)
Shape of
5   1   2
You
Perfect   4   2   1
Photograph 3   3   3
Bad Habits 2   4   4
di=R1−R2
Song   R₁ R₂ dᵢ dᵢ²
Shape of   -
1 2   1
You   1
Perfect   2 1 1 1
Photograph 3 3 0 0
Bad Habits 4 4 0 0
∑di2=1+1+0+0=2
Apply Spearman’s Rank Correlation Formula
6∑𝑑𝑖 2
𝜌= 1 −
𝑛(𝑛2 −1)
For 𝑛= 4:
6(2)   −12
𝜌= 1 −   = 1   = 1 −0.2 = 0.8
4(16 −1)   60
********** 7 **********
--- page 8 ---
(b) Calculate the Kendall rank correlation coefficient, and
interpret which metric better reflects the ranking quality in this
case.
Answer:
• Concordant pairs (C): 5
• Discordant pairs (D): 1
Apply Kendall’s Tau formula
𝐶−𝐷   5 −1 4
𝜏=   =   = = 0.667
Total Pairs   6   6
CO-4   b. Consider a Context-Aware E-commerce Recommendation System [10]
BL-   that uses the following contextual factors:
3,4   1. Device type (Mobile/Desktop)
2. User’s location (City/Region)
3. Time of access (Morning/Afternoon/Evening)
Based on the above design, develop an algorithm to integrate
contextual pre-filtering and post-filtering techniques into the
recommendation pipeline. Explain how each stage contributes to
improving personalization.
Answer:
Context-Aware Pipeline: Pre-filtering + Post-filtering (brief, point-
wise)
Assumptions:
• Base recommender (CF or CB) is available and returns top-K
candidates.
• Context features: Device ∈ {Mobile, Desktop}, Location ∈
{City/Region}, Time ∈ {Morning, Afternoon, Evening}.
• We have historical interactions tagged with these contexts.
Algorithm (step-wise)
1. Input: user u, current context c = (device, location, time), base
model, K (candidates), N (final recommendations).
2. Pre-filtering   stage:
2.1. Select historical interactions matching context c (exact or
relaxed — e.g., same device & time, or same location only).
2.2. If matched-history size ≥ threshold → use this context-
specific subset to train / query a context-specific base model
or   compute   context-specific   similarities.
2.3. Else → fall back to global data or nearest-context subset
(e.g.,   same   time   OR   same   device).
2.4. Generate top-K candidate items from the (context-filtered)
base model.
3. Feature   extraction   for   candidates:
3.1. For each candidate item i, compute: base score s_base(i)
(from model), and context-compatibility features f_ctx(i,c)
(e.g., mobile-friendly flag, location-availability, typical time-
of-day popularity).
********** 8 **********
--- page 9 ---
4. Post-filtering   /   re-ranking   stage:
4.1. Compute context score s_ctx(i) = g(f_ctx(i,c)) (simple rule
or   learned   function).
4.2. Combine scores: s_final(i) = (1-γ) * s_base(i) + γ *
s_ctx(i) where γ ∈   [0,1]   controls   context   weight.
4.3. Apply hard filters (remove items not available in location,
or   incompatible   with   device).
4.4. Re-rank candidates by s_final and pick top-N.
5. Output: top-N context-aware recommendations.
6. Logging & learning: store (user, item, context, outcome) →
use for updating context models and learning g() or tuning γ.
Q5   [20]
CO-2   a. Explain what is meant by matrix factorization in the context of [7]
BL-   recommender systems. Using a small user–item matrix, show how
2,3   matrix factorization decomposes ratings into latent features.
Answer:
1. Meaning:
• Matrix Factorization (MF) is a model-based collaborative
filtering technique that decomposes the user–item rating
matrix (R) into two lower-dimensional matrices:
𝑅≈𝑃× 𝑄𝑇
where:
o 𝑃= user–feature matrix (user preferences)
o 𝑄= item–feature matrix (item characteristics)
• Each user and item is represented by a small number of latent
features (e.g., taste dimensions).
Example: Given a user–item matrix 𝑹:
User/Item   I1 I2 I3
U1   5 3 0
U2   4 0 2
U3   1 1 0
Factorization:
We approximate 𝑅as:
𝑅= 𝑃× 𝑄𝑇
Let
2   1   2   1
𝑃= [ 1   1 ],𝑄= [ 1   1 ]
0.5 0.5   1 0.5
Then the predicted matrix:
5   3 2
𝑅̂ = 𝑃× 𝑄𝑇= [ 4   2 1.5 ]
1.5 1 0.8
********** 9 **********
--- page 10 ---
4. Interpretation:
• Each latent dimension captures hidden traits (e.g.,
genre preference, quality sensitivity).
•   Predictions for missing ratings come from the dot
product of corresponding user and item vectors.
CO-2,   b. Explain how clustering techniques help improve the efficiency and [8]
BL-   accuracy of Neighborhood-Based Collaborative Filtering (CF).
3,4   Using the same dataset (from Question 2 (part a)), calculate the
cosine similarity between users U1 and U3.
Answer:
Clustering in CF:
• Groups similar users or items into clusters based on rating
patterns or features.
• Reduces the search space for finding neighbors   in
Neighborhood-Based CF.
Improves Efficiency:
•   Instead of comparing a user with all others, similarity is
computed only within the cluster.
• Decreases computational time and memory usage.
Improves Accuracy:
• Neighbors within the same cluster are more relevant and
consistent, reducing noise.
• Enhances   the   quality of   similarity computation and
predictions.
Common Techniques:
• K-Means, Hierarchical Clustering, or DBSCAN for grouping
users/items.
Result:
• Produces faster, more scalable, and contextually accurate
recommendations.
Solution:
Common   rated   items:   I3,   I4,   I5
→ U1 = [3, 5, 4], U3 = [3, 4, 5]
(3 × 3 + 5 × 4 + 4 × 5)
Cosine Similarity =
√(32 + 52 + 42) × √(32 + 42 + 52)
9 + 20 + 20 49
=   = = 0.98
√50 × √50   50
Indicates very high similarity between users U1 and U3 — they have
almost identical rating patterns on common items.
CO-2   c. Apply preprocessing techniques to prepare a text dataset for [5]
BL-3   content-based recommendation.
Answer:
Key Preprocessing Steps:
1. Text Cleaning:
********** 10 **********
--- page 11 ---
o Remove punctuation, numbers, HTML tags, and special
characters.
2. Lowercasing:
o Convert all text to lowercase to ensure uniformity.
3. Tokenization:
o   Split text into individual words or tokens for further
processing.
4. Stopword Removal:
o Remove common words (e.g., the, is, and) that do not
add meaning.
5. Stemming / Lemmatization:
o Reduce words to their base or root form (running →
run).
6. Vectorization:
o Convert processed text into numerical feature vectors
using BoW, TF-IDF, or Word Embeddings.
Q6   [20]
CO-3   a. A recommender system predicts ratings for a user Meera for the [10]
BL-3   following movies. Higher values indicate stronger preferences.
(a) Compute the Mean Squared Error (MSE) of the predicted
ratings.
(b) Compute the Normalized MAE and RMSE, assuming all
ratings lie in the range {1 to 5}.
Answer:
MSE
0.25 + 0.16 + 0.64 + 0.25 + 0.09
𝑀𝑆𝐸=   = 0.278
5
Normalized Metrics
0.5   0.528
𝑁𝑀𝐴𝐸= = 0.125,𝑁𝑅𝑀𝑆𝐸=   = 0.132
4   4
********** 11 **********
--- page 12 ---
CO-3   b. Compare SVD and SVD++ in terms of their mathematical [6]
BL-4   structure, data requirements, and ability to handle implicit
feedback.
Answer:
CO-3   c. Describe the advantages of using model-based collaborative [4]
BL-2   filtering over neighborhood-based collaborative filtering.
Answer:
Advantages of Model-Based Collaborative Filtering (CF) over
Neighborhood-Based CF:
1. Better Accuracy:
o Learns   hidden   (latent)   patterns   in   user–item
interactions, improving prediction quality.
2. Scalability:
o Handles large datasets efficiently once the model is
trained (e.g., using Matrix Factorization, SVD).
3. Handles Sparsity:
o Can make predictions even with few common ratings,
unlike neighborhood-based methods.
4. Faster Predictions:
o Pre-trained models generate recommendations quickly
without repeated similarity computations.
5. Captures Complex Relationships:
o   Identifies deeper user–item dependencies beyond direct
co-ratings.
********** 12 **********
--- page 13 ---
Q7   [20]
CO-2   a.   Differentiate between supervised and unsupervised feature   [10]
BL-4   selection methods and discuss their implications for system
scalability and adaptability.
Answer:
Supervised Feature   Unsupervised Feature
Aspect
Selection   Selection
Works without labels;
Uses labeled data (target
selects features based
Definition   variable) to select features
on data structure or
that best predict the output.
similarity.
Correlation analysis, Mutual
PCA, clustering-based
Information, Chi-square,
Techniques   selection, variance
Recursive Feature
thresholding.
Elimination (RFE).
Preserve intrinsic
Maximize predictive
Goal   structure or diversity of
accuracy.
data.
More scalable —
Less scalable — requires
Scalability   simpler and faster on
label-based computations.
unlabeled data.
Task-specific; needs   More flexible; adapts
Adaptability retraining when labels   easily to new or
change.   unlabeled datasets.
CO-3   b. Evaluate how contextual modeling contributes to personalization   [6]
BL-4   compared to non-contextual methods.
Answer:
Contextual Modeling:
•   Incorporates situational factors (e.g., time, location, mood,
device) directly into the recommendation model.
•   Predicts ratings as a function of user, item, and context →
𝑟𝑢,𝑖,𝑐= 𝑓(𝑢, 𝑖, 𝑐).
Improved Personalization:
• Captures dynamic user preferences that change with context
(e.g., music choice differs morning vs. night).
• Provides more relevant, real-time recommendations tailored to
the current situation.
Compared to Non-Contextual Methods:
• Non-contextual models use only user–item interactions →
static and less adaptive.
• Contextual models offer higher accuracy, adaptability, and
satisfaction.
********** 13 **********
--- page 14 ---
CO-3   c. Analyze how contextual information can reduce the cold-start   [4]
BL-4   problem in recommender systems.
Answer:
Cold-Start Problem:
• Occurs when the system lacks sufficient data for new users or
new items, making it hard to generate recommendations.
Role of Contextual Information:
• Provides additional signals (e.g., location, time, device,
mood) even when historical ratings are missing.
• Helps infer preferences based on situational behavior patterns
— e.g., suggesting trending items in a user’s city or time of
day.
• Enables context-based filtering (recommend what similar
users liked in similar contexts).
Impact:
• Reduces data sparsity for new users/items.
• Improves early-stage personalization and relevance.
********** 14 **********
````
