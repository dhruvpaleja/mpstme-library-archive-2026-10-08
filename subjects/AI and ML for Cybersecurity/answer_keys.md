# AI and ML for Cybersecurity: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 4ba55a5779d4

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CyberSecurity_7010/AI and ML for Cybersecurity/ANS_AI and ML for Cybersecurity(702IT0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: AI and ML for Cybersecurity
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
a   Identify typical data problems in machine learning
 Data quality: To ensure that the data is accurate, complete, and
representative of the problem domain. Low-quality data can result in
inaccurate or biased models (Very crucial in Health domain).
⚫ Ex: Data that has lot of formatting errors, typos, redundancies,
missing entries, irrelevant values etc.
 Data quantity: There may not be enough data available to train an accurate
machine learning model.
⚫ Ex: 1000 samples used to train a deep learning model to detect
cancerous cells
 Bias and fairness: To ensure that the training data is not biased or
unrepresentative. This can lead to unfair outcomes for certain groups of
people, such as minorities or women when the model is trained on them.
 Ex: 70 safe mails and 30 spam mails to train a Spam detection
CO-1; BL-1   model   [5]
 Overfitting: It occurs when a model is too complex and fits the training data
too closely, resulting in poor generalization to new data.
⚫ Ex: A model that picks up noise or random fluctuations in the training
data and learns them as concepts.
⚫ Real time Ex: A student preparing for an exam and has studied all
non-exam topics in books( which have no relevance with the exam).
 Underfitting: It occurs when a model is too simple and does not capture all
the relevant patterns in the data.
⚫ Ex: A model fails to capture patterns in the data set
⚫ Real time Ex: A student preparing for an exam and has left all major
topics in books( which is very important for the exam).
 Privacy and security: Data may sometimes be sensitive information about
individuals or organizations, raising concerns about privacy and security.
Ex: Health related data, personal data etc.
CO-2; BL-2 b Describe the importance of feature engineering in building ML models   [5]
********** 1 **********
--- page 2 ---
 Data are observations of real-world (Ex: Personal biometric data can include
measurements of our minute-by-minute heart rate, blood sugar level, blood
pressure, etc.)
 Each piece of data provides a small window into a limited aspect of reality.
The collection of all these observations gives us a picture of the whole which
maybe messy most of the times as it may have noise and missing pieces.
 A feature is a numeric representation of raw data. In datasets, they appear as
columns. So, by choosing the most relevant pieces of data, we achieve more
accurate predictions for the model.
 The number of features is also important. If there are not enough informative
features, then the model will be unable to perform the ultimate task. If there
are too many features, or if most of them are irrelevant, then the model will
be more expensive and tricky to train.
 Feature Engineering is the process of extracting and organizing the important
features from raw data in such a way that it fits the purpose of the machine
learning model.
 It can be thought of as the art of selecting the important features and
transforming them into refined and meaningful features that suit the needs of
the model.
 Feature Engineering encapsulates various data engineering techniques such
as selecting relevant features, handling missing data, encoding the data, and
normalizing it.
 It has 2 goals:
 Preparing the proper input dataset, compatible with the machine
learning algorithm requirements.
 Improving the performance of machine learning models.
c Recall the key limitations associated with Decision Tree models.
 Sensitivity to hyper parameter tuning: Decision Trees are very
sensitive to hyper parameter tuning (i.e. parameters which are in control
of the programmer) and can be tuned to get better performance out of a
given model but can also vary drastically if the hyper parameters are
inaccurately tuned.
 Overfitting: Decision trees are prone to overfitting (Model learns the data
CO-2; BL-1   too well and hence performs well on training dataset but fails to perform   [5]
on testing dataset). Decision trees are prone to overfitting if the breadth
and depth of the tree is set to very high for a simpler dataset.
 Underfitting: Decision trees are also prone to under fitting (Model is too
simple for it to learn the dataset effectively). Decision tree suffers from
under fitting if the breadth and depth of the model or the number of nodes
are set too low. This does not allow the model to fit the data properly and
hence fails to learn.
d Discuss how different clustering approaches group data.
 Connectivity (Hierarchical) models: These models are based on the
notion that the data points closer in data space exhibit more similarity
to each other than the data points lying farther away (Ex: Hierarchical
Clustering)
 Centroid models: These are iterative clustering algorithms in which
the notion of similarity is derived by the closeness of a data point to the
CO-1; BL-2   [5]
centroid or cluster center of the clusters (Ex: k-Means Clustering)
 Distribution models: Based on the notion of how probable it is that all
data points in the cluster belong to the same distribution (like Normal,
Gaussian) (Ex: Expectation-maximization algorithm ). As the distance
from the distribution’s center increases, the probability that a point
belongs to the distribution decreases. The band colors show a decrease
in probability.
********** 2 **********
--- page 3 ---
 Density models: These models search the data space for areas of the
varied density of data points in the data space. They isolate different
dense regions and assign the data points within these regions to the
same cluster (Ex: DBSCAN and OPTICS).
a Demonstrate the working of a clustering algorithm suitable for large databases.
DBSCAN:
 Is the most common unsupervised density-based clustering algorithm
that works on the principle that for each point of a cluster, the
neighborhood of a given radius has to contain at least a minimum
number of points.
 Every data point is surrounded by a circle with a radius of
epsilon(eps), and DBSCAN identifies them as being either a
⚫ Core point - If the circle that surrounds it has a minimum
number of points specified by minPoints parameter.
⚫ Border Point - if the number of points is lower than the
minimum required.
⚫ Noise Point - if there are no additional data points located
within an epsilon radius of any data point.
 DBSCAN algorithms require only two parameters from the user:
⚫ The radius of the circle to be created around each data point,
also known as `epsilon`
Q2   ⚫ MinPoints which defines the minimum number of data points   [10]
CO-2; BL-3   required inside that circle for that data point to be classified as
a Core point.
Steps of the algorithm:
 Step 1:
⚫ Algorithm start by selecting a point (x) randomly from the data
set and finding all the neighbor points within Eps from it.
⚫ If the number of Eps-neighbours is greater than or equal
to MinPoints, we consider x a core point. Then, with its Eps-
neighbours, x forms the first cluster.
⚫ After creating the first cluster, we examine all its member points
and find their respective Eps -neighbors. If a member has at
least MinPoints Eps-neighbours, we expand the initial cluster
by adding those Eps-neighbours to the cluster. This continues
until there are no more points to add to this cluster.
 Step 2:
⚫ For any other core point not assigned to cluster, create a new
cluster.
 Step 3:
⚫ To the core point cluster, find and assign all points that are
recursively connected to it.
⚫ Step 4: Iterate through all unattended points in the dataset and
assign them to the nearest cluster at Eps distance from
********** 3 **********
--- page 4 ---
themselves. If a point does not fit any available clusters, locate
it as a noise point.
b Analyze the data points and form 2 clusters with the K-Means algorithm,
starting with A and B as initial means.
X   Y
A   3   3
B   5   3
C   7   6
D   8   7
Initial centroids:
•   Cluster 1 centroid = A (3,3)
•   Cluster 2 centroid = B (5,3)
Step 1: Assign points to nearest centroid
Distance formula:
𝑑= √(𝑥2 −𝑥1)2 + (𝑦2 −𝑦1)2
Cluster assignment after Step 1
Cluster Points
1   A
2   B, C, D
Step 2: Recalculate centroids
CO-3; BL-4   Cluster 1 (only A)   [10]
New centroid = (3,3)(no change)
Cluster 2 (B, C, D)
5 + 7 + 8 20
X mean =   =   ≈6.667
3   3
3 + 6 + 7 16
Y mean =   =   ≈5.333
3   3
New centroid for Cluster 2: (6.667, 5.333)
Final Cluster Assignment
Cluster Points
1   A, B
2   C, D
Step 4: Final Centroids
Cluster 1 (A, B):
𝑋= (3 + 5)/2 = 4, 𝑌= (3 + 3)/2 = 3 ⇒(4,3)
Cluster 2 (C, D):
𝑋= (7 + 8)/2 = 7.5, 𝑌= (6 + 7)/2 = 6.5 ⇒(7.5,6.5)
Clusters:
•   Cluster 1: A, B → Centroid (4,3)
•   Cluster 2: C, D → Centroid (7.5,6.5)
a Discuss how AI can be categorized based on its capabilities
Q3
[10]
CO-1; BL-2   Based on how they learn and how far they can apply their knowledge, all AI can
be broken down into three capability types:
********** 4 **********
--- page 5 ---
•   Artificial Narrow Intelligence (ANI) or Weak AI
o   Is goal oriented and is programmed to perform a single task.
o   Is very intelligent in completing the specific task that   it is
programmed to do.
o Are built to serve and excel in one cognitive capability and cannot
independently learn skills beyond its design.
o They use information from a specific dataset and do not perform any
task that is outside of the single task that they are designed to
perform.
o They can fail in unpredictable ways if it goes beyond its limits.
o Ex: Siri, Auto pilot in an airplane, Recommendation Systems –
Netflix, YouTube, and Amazon recommendations, Image and speech
recognition, ChatGPT etc.
•   Artificial General Intelligence (AGI) or Strong AI
o   Is a concept in which machines exhibit human intelligence.
o These machines have the ability to learn, understand and act in a way
that is indistinguishable from a human in a given situation.
o They are machines that can think, strategize and perform multiple
tasks under uncertain conditions.
o They integrate their prior knowledge in decision making to come up
with innovative, creative and unconventional solutions.
o Ex: ChatGPT (to some extent), Fujitsu has built the K computer(is
one of the fastest supercomputers in the world) , Tianhe-2 is a
supercomputer that was developed by the China's National University
of Defense Technology (It holds the record for cps (calculations per
second) at 33.86 petaflops), Creative AI in Art and Music etc.
•   Artificial Super Intelligence (ASI)
o   Is a hypothetical AI where machines will be capable of exhibiting
intelligence that surpasses that of the brightest humans.
o Apart from having multifaceted intelligence of human beings
machines will have greater problem solving and decision-making
capabilities that will be far superior to human beings.
o Some key characteristics include their capability to think, to reason,
solve the puzzle, make judgments, plan, learn, and communicate by
its own. (Ex: Solving complex global issues like climate change,
disease and poverty, Capable of forming its own goals and improving
itself)
o   It’s theorized that once AI has reached the general intelligence level,
it will soon learn at such a fast rate that its knowledge and capabilities
will become stronger than that even of humankind.
b Apply Principal Component Analysis and discuss how it helps in building
efficient ML models
Dimensionality Reduction:
⚫   It is a data preparation technique performed on data prior to modeling.
⚫   It might be performed after data cleaning and data scaling and before training
a ML model.
⚫ Any dimensionality reduction performed on training data must also be
CO-2; BL-3   performed on test dataset, validation dataset, and data when making a   [10]
prediction with the final model.
⚫ The process essentially transforms data from high-dimensional feature space
to a low-dimensional feature space ensuring that meaningful properties
present in the data are not lost during the transformation.
⚫   It is also commonly used in data visualization to understand and interpret the
data.
Benefits:
********** 5 **********
--- page 6 ---
⚫   It helps in data compression by reducing features hence the space required to
store the dataset also gets reduced.
⚫   It makes machine learning algorithms computationally efficient.
⚫ Less computation training time is required for reduced dimensions of
features.
⚫ Reduced dimensions of features of the dataset help in visualizing the data
quickly.
⚫   It removes the redundant features   (if present) by taking care of
multicollinearity.
PCA
⚫ Is a dimensionality reduction technique used to reduce the number of
variables of a data set, while preserving as much information as possible.
⚫   It takes datasets that have several correlated features and projects them onto
a coordinate (axis) system that has fewer correlated features. These new,
uncorrelated features are called principal components.
⚫ The goal is to identify patterns and latent structures within datasets in order
to create new columns and use these columns instead of the original
features.
⚫ With a data matrix of size n x d where n is the number of observations and
d is the number of original features, PCA projects the matrix onto a matrix
of size n x k (where k < d).
⚫ PCA gives rise to new columns that maximize the variance in our data
(refers to identifying which features (or variables) in a dataset contribute the
most to the variability or spread of the data or which aspects of the data
change the most and might be the most important for analysis.)
⚫ Principal components are ordered by variance (ones with higher variance
often are more informative because they contribute more to the overall
spread and diversity of the data) explained so that the first principal
component does the most to explain the variance of the data, while the
second component does the second most to explain the variance of the data.
⚫   Principal components indicates the directions in which the data varies the
most (i.e. they point in the direction where the data points are most spread
out)
⚫ Thus, PCA is a method that brings together:
⚫ A measure of how each variable is associated with one another.
(Covariance matrix.)
⚫ The directions in which our data are dispersed. (Eigenvectors.)
⚫ The amount of variance carried by each principal component.
(Eigenvalues.)
⚫ PCA combines our predictors and allows us to drop the eigenvectors
that are relatively unimportant.
a Clarify the meaning of data imbalance and illustrate why it should be managed
using an example.
 It refers to a problem in classification where the classes are not represented
equally.
 Imbalanced data refers to those types of datasets where the target class has an
uneven distribution of observations, i.e. one class label has a very high
number of observations and the other has a very low number of observations.
Q4
 Ex: In a fraudulent transactions data set, 98% transaction is “No Fraud” in   [10]
CO-2; BL-2
nature and 2% data is of type “Fraud”
 With imbalanced classes, it’s easy to get a high accuracy without actually
making useful predictions. So, accuracy as an evaluation metrics makes sense
only if the class labels are uniformly distributed.
 In case of imbalanced classes confusion-matrix and F1 score are good
techniques to summarize the performance of a classification algorithm.
 Oversampling (or Up sample):
********** 6 **********
--- page 7 ---
 Minority class is oversampled using replacement.
 Simply adding duplicate records of minority class often don’t add any
new information to the model.
 Undersampling (or Down sample): Rows are randomly deleted from majority
class to match with minority class
b Analyze the dataset and classify the tuple (Login_frequency =” Medium”,
Suspicious IP =” Yes” ,Malware Flag=”No” ) as M or H using Naïve Bayes
Login_Frequency Suspicious_IP   Malware_Flag   Risk
Low   No   No   M
High   Yes   Yes   H
Medium   No   Yes   M
High   Yes   No   H
Medium   No   No   M
High   Yes   Yes   H
Low   Yes   No   M
Medium   Yes   No   H
Low   No   Yes   M
Medium   Yes   Yes   H
Step 1: Prior probabilities
5   5
𝑃(𝑀) = = 0.5, 𝑃(𝐻) = = 0.5
10   10
CO-3; BL-4   Step 2: Likelihoods   [10]
• Login_Frequency = Medium
𝑃(𝐿𝑜𝑔𝑖𝑛= 𝑀𝑒𝑑𝑖𝑢𝑚∣𝑀) = 2/5 = 0.4, 𝑃(𝐿𝑜𝑔𝑖𝑛= 𝑀𝑒𝑑𝑖𝑢𝑚∣𝐻) = 2/5 = 0.4
•   Suspicious_IP = Yes
𝑃(𝑆𝑢𝑠𝑝𝑖𝑐𝑖𝑜𝑢𝑠= 𝑌𝑒𝑠∣𝑀) = 2/5 = 0.4, 𝑃(𝑆𝑢𝑠𝑝𝑖𝑐𝑖𝑜𝑢𝑠= 𝑌𝑒𝑠∣𝐻) = 5/5 = 1
• Malware_Flag = No
𝑃(𝑀𝑎𝑙𝑤𝑎𝑟𝑒= 𝑁𝑜∣𝑀) = 3/5 = 0.6, 𝑃(𝑀𝑎𝑙𝑤𝑎𝑟𝑒= 𝑁𝑜∣𝐻) = 2/5 = 0.4
Step 3: Compute posterior probabilities
Class M
𝑃(𝑀∣𝑡𝑢𝑝𝑙𝑒) ∝𝑃(𝑀) ⋅𝑃(𝐿𝑜𝑔𝑖𝑛= 𝑀𝑒𝑑𝑖𝑢𝑚∣𝑀) ⋅𝑃(𝑆𝑢𝑠𝑝𝑖𝑐𝑖𝑜𝑢𝑠= 𝑌𝑒𝑠
∣𝑀) ⋅𝑃(𝑀𝑎𝑙𝑤𝑎𝑟𝑒= 𝑁𝑜∣𝑀)
𝑃(𝑀∣𝑡𝑢𝑝𝑙𝑒) = 0.5 ⋅0.4 ⋅0.4 ⋅0.6 = 0.048
Class H
𝑃(𝐻∣𝑡𝑢𝑝𝑙𝑒) ∝𝑃(𝐻) ⋅𝑃(𝐿𝑜𝑔𝑖𝑛= 𝑀𝑒𝑑𝑖𝑢𝑚∣𝐻) ⋅𝑃(𝑆𝑢𝑠𝑝𝑖𝑐𝑖𝑜𝑢𝑠= 𝑌𝑒𝑠
∣𝐻) ⋅𝑃(𝑀𝑎𝑙𝑤𝑎𝑟𝑒= 𝑁𝑜∣𝐻)
𝑃(𝐻∣𝑡𝑢𝑝𝑙𝑒) = 0.5 ⋅0.4 ⋅1 ⋅0.4 = 0.08
********** 7 **********
--- page 8 ---
Step 4: Compare posteriors
𝑃(𝐻∣𝑡𝑢𝑝𝑙𝑒) > 𝑃(𝑀∣𝑡𝑢𝑝𝑙𝑒)
Classification: H (High Risk)
a   Identify the key distinctions between Linear and Logistic Regression
Linear Regression   Logistic Regression
Is used to predict the continuous   Is used to predict the categorical
dependent variable using a given set   dependent variable using a given set
of independent variables.   of independent variables.
Is used for solving Regression   Is used for solving Classification
problem.   problems.
We find the best fit line, by which we We find the S-curve by which we can
can easily predict the output.   classify the samples.
Least square estimation method is   Maximum likelihood estimation
used for estimation of accuracy.   method is used for estimation of
accuracy.
The output must be a continuous   The output must be a Categorical
Q5   value, such as price, age, etc.   value such as 0 or 1, Yes or No, etc.   [10]
CO2; BL1
It is required that relationship   It is not required to have the linear
between dependent variable and   relationship between the dependent
independent variable must be linear.   and independent variable.
b Describe how Decision Trees can be applied to regression and classification
problems with examples
 Are popular machine learning algorithms that can be used for both regression
(observes features of an object and trains a model in the structure of a tree to
predict data in the future to produce meaningful continuous output) and
CO-2; BL-2   classification tasks.   [10]
 It uses a flowchart like a tree structure to show the predictions that result from
a series of feature-based splits.
 It starts with a root node and ends with a decision made by leaves.
 Are Partitioning based algorithms – that is search space is divided into
rectangular regions.
 Tuple placed into class based on the region within which it falls.
********** 8 **********
--- page 9 ---
 Different decision tree approaches differ in how the tree is built: DT
Induction
 Assumptions made while using the decision tree:
 At the beginning, we consider the whole training set as the root.
 Feature values are preferred to be categorical. If the values are continuous
then they are discretized prior to building the model.
 On the basis of attribute values, records are distributed recursively.
 We use statistical methods for ordering attributes as root or the internal node.
 Algorithms: ID3, C4.5, CART, Random Forest
a   Illustrate the functioning of Support Vector Machines with an example.
 Is a supervised machine learning algorithm that works best on smaller
datasets that are complex.
 It finds a hyperplane that best separates two or more classes.
 It selects the hyperplane that has maximum distances between the classes.
 Types:
⚫ Linear SVM – Used when the data is perfectly linearly separable (i.e.,
the data points can be classified into 2 classes by using a single
straight line).
⚫ Non-Linear SVM - Used when the data is not linearly separable
 Applications:
⚫ They work on a range of different types of data, but are most effective
Q6   on data sets with very high dimensions relative to the observations.
[10]
CO-3; BL-2   ⚫ Ex: Text classification, in which language has many dimensions of
word   vectors, DNA sequencing by labeling chromatograms
correctly, in determining malicious IP addresses and malicious port
address in face detection as there are many features that can be taken
into consideration while classifying.
 Hyperplane: There can be multiple lines/decision boundaries to segregate
the classes in n-dimensional space and the best boundary is known as the
hyperplane of SVM. The dimensions of the hyperplane depend on the features
present in the dataset. (Ex: If there are 2 features then hyperplane is a straight
line, if there are 3 features then hyperplane is a 2-dimensional plane etc.)
 Support Vectors: These are the points that are closest to the hyperplane.
 Margin: Is the distance between the hyperplane and the observations closest
to the hyperplane (support vectors).
********** 9 **********
--- page 10 ---
Working:
 The process starts by finding different hyperplanes which classify the labels
in the best way.
 Out of all the different hyperplanes, the one which is farthest from the data
points or the one which has a maximum margin is selected.
 The best hyperplane is that plane that has the maximum distance from both
the classes, and this is the main aim of SVM. The hyperplane with maximum
margin is called the optimal hyperplane.
b Build a two-hidden-layer neural network with proper activation functions and
illustrate how it processes data.
 Is a small neural network of four layers.
 The input layer is where we feed data from which our neural network has
to learn.
 The output layer is where we get the target value, this represents what the
neural network is trying to predict or learn.
 All layers in between are called hidden layers.
 When we feed the inputs into the first layer, the values of the nodes will be
calculated layer by layer using the matrix multiplications and activation
functions till we get the final values at the output layer.
CO2; BL-3   [10]

Ex: Problem statement: Whether to go surfing or not?
 Factors influencing our decision making are:
 Are the waves good? (Yes: 1, No: 0)
 Is the line-up empty? (Yes: 1, No: 0)
 Has there been a recent shark attack? (Yes: 0, No: 1)
 Assuming the following inputs:
 X1 = 1, since the waves are good
 X2 = 0, since the crowds are out
 X3 = 1, since there hasn’t been a recent shark attack
 Assigning weights to determine importance (Larger weights signify that
particular variables are of greater importance to the decision or outcome)
********** 10 **********
--- page 11 ---
 W1 = 5, since large swells don’t come around often
 W2 = 2, since you’re used to the crowds
 W3 = 4, since you have a fear of sharks
∑wixi + bias = w1x1 + w2x2 + w3x3 + bias
output = f(x) = 1 if ∑w1x1 + b>= 0
= f(x) = 0 if ∑w1x1 + b < 0
Assuming a bias of -3, which is an external factor,
Predicted value = (1*5) + (0*2) + (1*4) – 3 = 6
As 6 > 0, predicted value is “go surfing"
Short notes on:
a. Hierarchical vs. Centroid based models
Hierarchial:
 Is an unsupervised machine-learning clustering strategy.
 It groups the data points together that are close to each other based on
the measure of similarity or distance.
 Tree-like morphologies called Dendograms are used to bunch the
dataset and create the hierarchy of the clusters.
 Individual data points are located at the bottom of the dendrogram,
while the largest clusters, which include all the data points, are located
at the top.
 The Dendrogram is created by iteratively merging or splitting clusters
based on a measure of similarity or distance between data points.
 In order to generate different numbers of clusters, the Dendrogram can
be sliced at various heights.
 Agglomerative
 Initially each item in its own cluster.
 Iteratively clusters are merged together.
 Bottom Up
 Divisive
 Initially all items in one cluster.
Q7
 Large clusters are successively divided.
CO-1; CO-
 Top Down
3; CO-1;   [5*4=20]
Centroid based:
CO-1; BL-2
 It organizes the data into non-hierarchical clusters.
 This technique uses centroids, the center of each cluster, to minimize
the sum of the distances between the data points and their corresponding
cluster centroids.
 The data points are as close as possible to the center of the cluster and
the inter-cluster distance is maximized.
 Is ideal for datasets with easily separable, well-defined clusters and also
suitable when the number of clusters is known or can be easily
estimated.
 Creates clusters in one step as opposed to several steps and further
iterations refines the clusters formed.
 Usually deals with static sets.
 They suffer from a combinatorial explosion due to the number of
possible solutions.
 Real-world applications include image segmentation, Cyber profiling
(an analysis on the digital footprints associated with a person whose
identity may or may not have been known such as personality, motives
etc. ), Insurance Fraud Detection, Malware detection (detect malware
behavior of data based on the features of the malware) etc.
b. Application of AI/ML in domain of cybersecurity
AI is employed in:
********** 11 **********
--- page 12 ---
 Threat detection and response by learning normal network
behavior to identify anomalies.
 Conducting behavioral   analysis   to   detect suspicious
activities.
 Enabling   real-time monitoring   for immediate   threat
identification.
Enhanced Threat Detection:
 AI systems can analyze vast amounts of data quickly to
identify anomalies and potential threats that might be missed
by traditional methods.
 This capability is crucial for identifying sophisticated and
emerging threats in real time.
 Ex: An AI-powered SIEM (Security Information and Event
Management) platform detects an unusual login pattern from
an employee’s account—accessing sensitive files at odd
hours from an unrecognized IP address across multiple
locations.
c. Describe various stages in Machine Learning
 Gathering Data
 Preparing that data
 Choosing a model
 Training
 Evaluation
 Hyperparameter Tuning
 Prediction
d. Explain concept of Cost and loss function
Loss Function:
 The loss function, also known as the error function, measures how
well a single prediction matches the actual value.
 It quantifies the error or deviation of the predicted value from the true
value for a single data point.
 It helps in determining how much the model's prediction deviates
from the actual value for each individual data point.
Cost Function:
 Is basically the calculation of the error between predicted values and
expected values and presents it in the form of a single real number.
 It is the average of error of n-sample in the data.
 Is used during the training process to optimize the model. The goal of
training is to minimize the cost function, which indicates that the
model’s predictions are becoming closer to the actual values on
average.
 Ideal value of the Cost Function is 0 or somewhere closer to 0, that
indicates a better model fit to the data.
********** 12 **********
--- page 13 ---
 In order to get out ideal Cost Function, we can use Gradient technique
(iterative optimization technique used to find the parameters that
minimize the cost function).
********** 13 **********
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper e8d622e6090b

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/BTech_CyberSecurity_7010/AI and ML for Cybersecurity/ANS_AI and ML for Cybersecurity(702IT0E003)_2024-2025.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (14 pages), mean OCR confidence 71.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester V(Exam Year: NA)
Subject: AI and ML for Cybersecurity
Date: NA   Time: NA to NA (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 1 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
a What is reinforcement learning?
•   Is an autonomous, self-teaching system that essentially learns by trial
and error.
•   It works on a feedback-based process, in which it automatically
explores its surrounding by hitting & trail, taking action, learning from
experiences (no labelled data) , and improving its performance.
• Good action gets rewarded and bad action gets punished. Hence the
goal of reinforcement learning agent is to maximize the rewards.
•   It uses algorithms that learn from outcomes and decide which action to
take next. After each action, the algorithm receives feedback that helps
it determine whether the choice it made was correct, neutral or
incorrect.
• They can handle environments that are non-deterministic, meaning that
the outcomes of actions are not always predictable. This is useful in
real-world applications where the environment may change overtime
CO-1; BL-1   [5]
or is uncertain.
• They require huge data and involve complex computations.
•   It is highly dependent on the quality of the reward function. If the
reward function is poorly designed, the agent may not learn the desired
behavior.
•   It can be difficult to debug and interpret as it is not always clear why
the agent is behaving in a certain way, which can make it difficult to
diagnose and fix problems.
Ex:
Stock Market - Observe the rules and patterns of the stock market before it
tests actions and records associated rewards. It dynamically creates a value
function and develops a strategy to maximize profits.
An application may display ads to a user based on some demographic
information. With each ad interaction, the application learns which ads to
display to the user to optimize product sales.
********** 1 **********
--- page 2 ---
b Summarize the key features that differentiate high-quality data from poor-
quality data.
• Completeness: Is a measure of whether all of the required data is present
within the dataset and if it meets the objectives of the project being worked
on. If missing data are present, then it should be clear how these are
handled.
o Ex: Customer age details that are normally left blank in surveys
• Accuracy: Is a measure of how well the data accurately reflects the object
being described, i.e., how well does the data reflect reality?
o Ex: A customer’s recorded phone number is outdated or entered
incorrectly (e.g., typo).
•   Timeliness: Is a measure of the data being available when it is needed for
decision-making. Is the data that is being worked on the latest version that
is available to make appropriate interpretations?
o Ex: Constantly changing phone numbers, home addresses and
CO-2; BL-2   [5]
email addresses.
•   Consistency: Is a measure of how consistent the data is. The same data
should be consistent across different storage locations, software packages
and file formats.
o Ex: A customer's birthdate is 11-31-1990 in one system and 13-
02-1990 in another.
•   Validity: Is a measure of how well the data fits within pre-defined limits,
expectations and standards. This can apply to date formats, telephone
numbers, sensor measurements and more.
o Ex: Valid yet inaccurate value - usage of valid postal code but
used for the wrong suburb and thus ends up failing the data
accuracy rules)
• Uniqueness: Features or objects should only be represented within a
particular dataset once. Duplicate data, not only skews results but can
increase computational processing times and storage space.
c What is meant by the curse of dimensionality?
Following sections expected in the answer:
1. What is cure of dimensionality, example indicating the same
2. Approaches used to handle this with appropriate example.
o Data forms the foundation of any machine learning algorithm.
o The performance of machine learning algorithms can degrade with too
many input variables (are columns that are fed as input to a model, also
called as features)
o A geometric interpretation of a dataset indicates columns as the
dimensions on an n-dimensional feature space and the rows of data as
points in that space.
CO-2; BL-1   o High-dimensionality might mean hundreds, thousands, or even millions   [5]
of input variables and fewer input dimensions often mean
correspondingly fewer parameters or a simpler structure in the machine
learning model
o The higher the number of features, the more difficult it is to model them,
this is known as the curse of dimensionality, hence it is often desirable to
reduce the number of input features.
o Dimensionality Reduction:
o   It is a data preparation technique performed on data prior to modeling.
o   It might be performed after data cleaning and data scaling and before
training a ML model.
o Any dimensionality reduction performed on training data must also be
performed on test dataset, validation dataset, and data when making a
prediction with the final model.
********** 2 **********
--- page 3 ---
o The process essentially transforms data from high-dimensional feature
space to a low-dimensional feature space ensuring that meaningful
properties present in the data are not lost during the transformation.
o   It is also commonly used in data visualization to understand and interpret
the data.
d   Describe how agglomerative clustering builds clusters compared to divisive
clustering.
Following sections expected in the answer:
1. What is hierarchical clustering
2. Characterstics of both agglomerative and divisive
3. How do they actually differ, with an appropriate example.
 Agglomerative
o Initially each item in its own cluster.
o Iteratively clusters are merged together.
o Bottom Up
CO-1; BL-2    Divisive   [5]
o Initially all items in one cluster.
o Large clusters are successively divided.
o Top Down
a   Demonstrate how DBSCAN can be used to detect clusters in a dataset.
Following sections expected in the answer:
1. What is the problem with clustering large data bases.
2. Characterstics of DBSCAN
3. Working of DBSCAN with appropriate example.
 Is the most common unsupervised density-based clustering
algorithm that works on the principle that for each point of a
cluster, the neighborhood of a given radius has to contain at least
a minimum number of points.
 Every data point is surrounded by a circle with a radius of
Q2   epsilon(eps), and DBSCAN identifies them as being either a
CO-2; BL-3   ⚫ Core point - If the circle that surrounds it has a minimum   [10]
number of points specified by minPoints parameter.
⚫ Border Point - if the number of points is lower than the
minimum required.
⚫ Noise Point - if there are no additional data points located
within an epsilon radius of any data point.
********** 3 **********
--- page 4 ---
 DBSCAN algorithms require only two parameters from the
user:
⚫ The radius of the circle to be created around each data
point, also known as `epsilon`
⚫ MinPoints which defines the minimum number of data
points required inside that circle for that data point to be
classified as a Core point.
Steps of the algorithm:
Step 1:
 Algorithm start by selecting a point (x) randomly from the data
set and finding all the neighbor points within Eps from it.
 If the number of Eps-neighbours is greater than or equal
to MinPoints, we consider x a core point. Then, with its Eps-
neighbours, x forms the first cluster.
 After creating the first cluster, we examine all its member points
and find their respective Eps -neighbors. If a member has at
least MinPoints Eps-neighbours, we expand the initial cluster
by adding those Eps-neighbours to the cluster. This continues
until there are no more points to add to this cluster.
Step 2:
⚫ For any other core point not assigned to cluster, create a
new cluster.
Step 3:
⚫ To the core point cluster, find and assign all points that
are recursively connected to it.
Step 4: Iterate through all unattended points in the dataset and assign
them to the nearest cluster at Eps distance from themselves. If a point
does not fit any available clusters, locate it as a noise point.
b A company’s cybersecurity team wants to predict the number of phishing
emails a new employee will correctly identify based on their cybersecurity
awareness test score.
Awareness Test Score   Phishing Detection Score
95   90
85   80
80   70
70   60
60   55
• Determine the linear regression equation that predicts phishing detection
score based on the awareness test score.
CO-3; BL-4   If a new employee scores 75 on the cybersecurity awareness test, predict how   [10]
many phishing emails they are expected to detect correctly.
Step 1: Calculate means
95 + 85 + 80 + 70 + 60 390
𝑋ˉ =   =   = 78
5   5
90 + 80 + 70 + 60 + 55 355
𝑌ˉ =   =   = 71
5   5
Step 2: Calculate slope 𝑏
∑(𝑋𝑖−𝑋ˉ)(𝑌𝑖−𝑌ˉ)
𝑏=
∑(𝑋𝑖−𝑋ˉ)2
********** 4 **********
--- page 5 ---
Compute numerator ∑(𝑋𝑖−𝑋ˉ)(𝑌𝑖−𝑌ˉ):
X Y X - X̄ Y - Ȳ (X-X̄)(Y-Ȳ)
95 90 17   19   323
85 80 7   9   63
80 70 2   -1   -2
70 60 -8   -11   88
60 55 -18   -16   288
Numerator = 323 + 63 −2 + 88 + 288 = 760
Compute denominator ∑(𝑋𝑖−𝑋ˉ)2:
(17)2 + (7)2 + (2)2 + (−8)2 + (−18)2 = 289 + 49 + 4 + 64 + 324 = 730
760
𝑏=   ≈1.041
730
Step 3: Calculate intercept 𝑎
𝑎= 𝑌ˉ −𝑏𝑋ˉ = 71 −(1.041 ⋅78) ≈71 −81.2 ≈−10.2
Step 4: Linear regression equation
𝑌= −10.2 + 1.041𝑋
Step 5: Predict for X = 75
𝑌= −10.2 + 1.041 ⋅75 ≈−10.2 + 78.075 ≈67.875
Prediction: ~68 phishing emails correctly detected.
a   Explain the difference between nominal and ordinal attributes and how each
can be encoded.
Following sections expected in the answer:
1. Characteristics of both, with appropriate example
2. Need Encoding techniques used with their pros and cons.
Categorical/Qualitative data:
⚫ Is non-numerical information that is used to describe
characteristics, qualities, or properties.
⚫ This encompasses data that can be represented through words.
It usually defines groups or categories & is therefore known
as categorical data.
Q3
⚫ Ex: Names of all items in a supermarket, movie ratings (good,   [10]
CO-1; BL-2
average, bad), country of birth of individuals & so on.
⚫ Are of 2 types:
Nominal –
⚫ The data has categories that don’t have any particular order or
ranking associated with them.
⚫ The total number of categories is usually finite in this type of
data as well.
⚫ Ex: Colour of hair (Blonde, red, Brown, Black, etc.), Marital
status (Single, Widowed, Married), Nationality (Indian,
German, American) etc.
Ordinal –
⚫ The data has an inherent ordering present within the
categories.
⚫ There is a fixed, finite number of categories/groups.
********** 5 **********
--- page 6 ---
⚫ These categories/groups needs to be taken into account while
converting this type of data into numbers so that the models
can learn this ranking as well.
⚫ Ex: Letter grades in the exam (A, B, C, D, etc.), Economic
Status (High, Medium, and Low), Education Level (Higher,
Secondary, Primary) etc.
Few algorithms require categorical variables that are non-numeric values to
be encoded into a convenient numeric value so that they can be used to train
the model.
 Label Encoding
⚫   Is simply converting each categorical value in a column to a
number.
⚫ Usually used when categorical data has just two levels, so that
it can be encoded as 0 and 1 (Ex: Gender – M to 0 and F to 1)
⚫ For categorical columns with more than 2 levels, this method
is not suggested as the machine learning model will wrongly
assume that there is some sort of sequential relationship
between the values assigned and it may result in feeding the
model with incorrect information.
 One hot Encoding
⚫ For each category, it designs a new binary feature, often
called a “dummy variable.”
⚫ We assign 1 to the column which is true and 0 to the others.
⚫ The entire set of columns that represent the Categorical
variable shall give us the result without creating any ordinal
relationship.
b   Demonstrate how labeled and unlabeled data are handled differently in
supervised and unsupervised learning.
Following sections expected in the answer:
1. Explanation of labelled and unlabelled data
2. Their importance with supervised and unsupervised techniques
3. Difficulties in labelling data
Supervised Learning (uses labeled data)
•   Definition:
In supervised learning, the algorithm is trained using input data with
known output labels.
The model learns to map inputs (features) to the correct output
(label).
• Example:
CO-2; BL-3   [10]
A dataset of emails where each email is labeled as Spam or Not Spam.
o   Input: Email text, number of links, presence of suspicious
keywords.
o Output (label): Spam / Not Spam.
o The model learns the pattern and later predicts the label for
new, unseen emails.
•   Process:
o Provide labeled training data.
o Model learns patterns between features and labels.
o   Predict labels for new input data.
Unsupervised Learning (uses unlabeled data)
•   Definition:
In unsupervised learning, the algorithm is trained using input data
without labels.
The goal is to find patterns, structures, or clusters in the data.
********** 6 **********
--- page 7 ---
• Example:
Analyzing network traffic data without prior knowledge of which
sessions are malicious.
o   Input: Connection duration, number of packets, data size, IP
frequency.
o No labels (unknown if malicious or normal).
o The model groups similar sessions together — abnormal
clusters may indicate potential attacks.
•   Process:
o Provide unlabeled data.
o Model identifies structure or grouping.
o Analyst interprets clusters (e.g., potential threats).
a   Explain how overfitting affects a model’s generalization ability and usability.
Following sections expected in the answer:
1. What is overfitting
2. How does it affect performance of a model
3. Appropriate example
Overfitting occurs when a machine learning model learns the training data too
well,   including   its   noise,   outliers,   and   random   fluctuations.
As a result, the model performs extremely well on training data but poorly on
unseen (test) data.
Effect on Generalization Ability
• A model’s generalization ability refers to how well it performs on new,
unseen data.
• When a model is overfitted, it fails to generalize patterns; instead, it
Q4   memorizes training examples.
[10]
CO-2; BL-2   •   Consequently, the model cannot correctly predict outcomes for new
inputs, leading to high variance and low predictive accuracy on test
data.
Example:
A cybersecurity model trained to detect malware may memorize specific
malware file names instead of learning underlying patterns. It will then fail to
detect new types of malware.
Effect on Usability
•   Overfitted models are unreliable in real-world deployment because
they cannot adapt to slightly different or changing data.
• They may give misleading predictions, reducing trust and effectiveness
in decision-making systems.
•   In practical terms, this limits the model’s usability, since a model that
only performs well on past data is of little value in dynamic, real
environments.
b Apply the ID3 method to the dataset and explain your reasoning for selecting
the initial attribute for the decision tree.
IP   Device   Time of   Login Malicious
Location   Type   Access
Foreign   Mobile   Night   Yes
CO-3; BL-4   Local   Desktop   Day   No   [10]
Foreign   Desktop   Night   Yes
Local   Mobile   Night   No
Foreign   Mobile   Day   No
Local   Desktop   Night   No
Foreign   Desktop   Day   Yes
********** 7 **********
--- page 8 ---
Step 1: Compute Entropy of Target (Login Malicious?)
Target values: Yes = 3, No = 4
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) = −∑𝑝𝑖log⁡2 𝑝𝑖
𝑝𝑌𝑒𝑠= 3/7, 𝑝𝑁𝑜= 4/7
𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) = −(3/7)log⁡2(3/7) −(4/7)log⁡2(4/7)
≈−0.429 ⋅(−1.222) −0.571 ⋅(−0.807) ≈0.985
Step 2: Compute Information Gain for Each Attribute
Attribute 1: IP Location
•   Foreign → Yes=3, No=1 → Entropy = - (3/4)log2(3/4) -
(1/4)log2(1/4) ≈ 0.811
•   Local → Yes=0, No=3 → Entropy = 0 (pure)
−(4   3
𝐼𝐺(𝐼𝑃𝐿𝑜𝑐𝑎𝑡𝑖𝑜𝑛) = 0.985   ∗0.811 + ∗0) ≈0.985 −0.464 ≈0.521
7   7
Attribute 2: Device Type
• Mobile → Yes=2, No=1 → Entropy ≈ 0.918
• Desktop → Yes=1, No=3 → Entropy ≈ 0.811
−(3   4
𝐼𝐺(𝐷𝑒𝑣𝑖𝑐𝑒) = 0.985   ∗0.918 + ∗0.811) ≈0.985 −0.858 ≈0.127
7   7
Attribute 3: Time of Access
•   Night → Yes=2, No=2 → Entropy = 1
• Day → Yes=1, No=2 → Entropy ≈ 0.918
−(4   3
𝐼𝐺(𝑇𝑖𝑚𝑒) = 0.985   ∗1 + ∗0.918) ≈0.985 −0.966 ≈0.019
7   7
Step 3: Select the First Splitting Attribute
•   IP Location has the highest information gain (0.521).
•   Reasoning: Splitting the tree by IP Location reduces the uncertainty
the most and separates the data into more homogeneous groups
(Foreign vs Local).
a   Recall the basic purpose of feature scaling in model development.
Following sections expected in the answer:
1. What is feature scaling
2. Need for feature scaling with example
3. Techniques used for the same
 Is the process of scaling or converting all the values in our dataset to
a given scale.
 K Nearest Neighbours, Support Vector Machine, and K-Means
Q5   clustering also show a drastic rise in performance on scaling the data.
[10]
CO2; BL1    Two main techniques are:
⚫ Standardization
•   Ensures that each feature has a mean of 0 and a
standard deviation of 1, bringing all features to the
same magnitude.
•   All the data points are subtracted by their mean and
the result divided by the distribution’s variance.
•
 Normalization
⚫ All values are scaled in a specified range between 0 and 1 via
normalization (or min-max normalization).
********** 8 **********
--- page 9 ---
⚫ For each value in a feature, Min-Max normalization subtracts
the minimum value in the feature and then divides by its
range.
⚫ The range is the difference between the original maximum
and the original minimum.
b   Describe the functionality of multi-layered neural networks and how input is
transformed through hidden layers.
Following sections expected in the answer:
1. What are neural networks
2. Characteristics of multi-layer network
3. Appropriate example
A multi-layered neural network (also called a multilayer perceptron, MLP)
is an artificial neural network composed of an input layer, one or more hidden
layers, and an output layer. It is designed to learn complex, non-linear
relationships between input data and output predictions.
1. Input Layer
o Receives raw data features (e.g., numerical values, pixels,
word embeddings).
o Each neuron in this layer represents one input feature.
o No computation occurs here — it just passes the input
values to the next layer.
2. Hidden Layers
o Perform feature transformation and abstraction.
CO-2; BL-2   o Each neuron in a hidden layer computes a weighted sum of   [10]
inputs from the previous layer, adds a bias, and applies a
non-linear activation function.
o This process allows the network to learn complex, non-
linear mappings.
Mathematically, for a hidden layer neuron:
hj=f(∑iwijxi+bj)h_j = f\left(\sum_i w_{ij}x_i + b_j\right)hj
=f(i∑wijxi+bj)
where
o xix_ixi = inputs from the previous layer
o wijw_{ij}wij = weights
o bjb_jbj = bias term
o   f(⋅)f(\cdot)f(⋅) = activation function (e.g., ReLU, sigmoid,
tanh)
3. Output Layer
o Receives the transformed features from the last hidden layer.
o Produces the final output, such as class probabilities or
regression values.
o Uses an activation suitable for the task (e.g., softmax for
classification, linear for regression).
a   Interpret how SVM can be applied to solve a practical problem, such as email
Q6
spam detection or image classification   [10]
CO-3; BL-2
********** 9 **********
--- page 10 ---
Following sections expected in the answer:
1. Characteristic of SVM
2. Application of this to any real time application with proper
justification why this model proves to be better
 Is a supervised machine learning algorithm that works best on smaller
datasets that are complex.
 It finds a hyperplane that best separates two or more classes.
 It selects the hyperplane that has maximum distances between the classes.
 Types:
⚫ Linear SVM – Used when the data is perfectly linearly separable
(i.e., the data points can be classified into 2 classes by using a
single straight line).
⚫ Non-Linear SVM - Used when the data is not linearly separable
 Applications:
⚫ They work on a range of different types of data, but are most
effective on data sets with very high dimensions relative to the
observations.
⚫ Ex: Text classification, in which language has many dimensions of
word   vectors, DNA sequencing by labeling chromatograms
correctly, in determining malicious IP addresses and malicious port
address in face detection as there are many features that can be
taken into consideration while classifying.
Spam/Not Spam:
 Feature Extraction:
⚫ Convert emails into numerical features such as word
frequencies, presence of certain keywords (like “free”,
“offer”), or the number of links.
 Training:
⚫ Feed the labeled data (spam/not spam) to the SVM model.
⚫ The algorithm learns to separate spam from non-spam
messages using a hyperplane.
 Prediction:
⚫ When a new email arrives, the SVM classifies it based on
which side of the hyperplane it falls on.
Interpretation:
SVM helps filter spam efficiently because it can handle high-
dimensional text data and find clear boundaries between spam and
legitimate emails.
b   Demonstrate, with an example, the impact of high bias and high variance on
predictions.
Following sections expected in the answer:
1. What is bias and variance
2. Their effects on model building
3. Relationship between the two
CO2; BL-3   [10]
4. Appropriate example
Bias:
o It refers to the error introduced by approximating a real-world problem,
which may be complex, by a simplified model.
o These are the simplifying assumptions made by a model to make the target
function easier to learn.
********** 10 **********
--- page 11 ---
o A high bias (more assumptions made about the target function form)
indicates that the model is too simple to capture the underlying patterns
in the data, resulting in under-fitting.
o Ex: A voice assistant system that is built by training the model with the
voices of people from a particular region. This model cannot perform
very well if we use it in a different region due to changes in voice tone,
dialect, culture, etc.
o Types of Bias:
o   Prejudicial Bias (beliefs – Ex: Favouring male candidates for a
typical role)
o Sampling Bias (Intentionally or unintentionally, we may
oversample from a population group)
o Algorithm Bias (wrong choice of algorithm)
o Confirmation Bias (tend to retain information that affirms our
preconceived notions – Ex: Most brute-force attacks come from
foreign IP addresses, The ransomware attack must be from the
same group that was faced last year.)
Variance:
 It refers to the error introduced by the model’s sensitivity to
fluctuations in the training data (i.e. it measures how much a model’s
predictions change if you train it on different training datasets from
the same distribution.)
 High variance often leads to overfitting, where the model learns the
noise in the training data instead of the underlying pattern.
 Ex: A decision tree perfectly fits the training data, but on a slightly
different dataset, it learns a completely different set of splits.
 As the model complexity grows, the bias reduces while the variance
increases, and vice versa.
 Models with high bias will have low variance (it will reduce the risk
of inaccurate predictions, the model will not properly match the data
set) and models with high variance will have a low bias (model will fit
with the data set while increasing the chances of inaccurate
predictions).
 A model should, in theory, have minimal variance and bias. However,
having both is nearly impossible (Increasing the bias will decrease the
variance and increasing the variance will decrease the bias)
 A trade-off must be made in order to build a strong model that
performs well on both train and unseen data.
EX:
For building a model to classify network connections as normal or
attack, we have a large dataset of network connections collected over
time i.e. mixed traffic (port scans, SQL injections, DDoS, etc.), but
we only use random samples of it to train.
High variance model (overfitting):
⚫ Train on sample 1 → predicts port scans correctly but fails on
SQL injections.
⚫ Train on sample 2 → predicts SQL injections correctly but
fails on DDoS.
⚫ Train on sample 3 → predicts DDoS well but misses port
scans.
 The model overfits to training subsets, causing high variance in
predictions.
Low variance model (simpler, more stable):
 No matter which sample we train on, the model consistently learns
broad rules (Ex: “very high packet rate over short time = suspicious” ,
“a host scans many different ports in a short time = port scan”,
“thousands of requests per second from the same IP - DDoS attack”).
 Predictions don’t change much across samples.
********** 11 **********
--- page 12 ---
Short notes on:
a. Intrusion Detection System using AI/ML model
Following sections expected in the answer:
1. Explanation of IDS system
2. Probable solution using AI/ML
An Intrusion Detection System (IDS) is a cybersecurity tool that monitors
network or system activities to identify suspicious behavior or potential
attacks. When integrated with Artificial Intelligence (AI) or Machine
Learning (ML) models, IDS becomes more adaptive and efficient.
•   Data Collection:
Collect network traffic data — IP addresses, port numbers,
connection duration, number of packets, etc.
Each record is labeled as normal or malicious (for supervised
learning).
•   Feature Extraction:
Select relevant attributes (like packet size, protocol type, byte count).
• Model Training:
Train an ML model such as:
•   Decision Tree
• Random Forest
•   Support Vector Machine (SVM)
•   Neural Network
Detection Phase:
The trained model monitors live traffic and classifies activity as normal
Q7   or intrusive.
CO-3; CO-1;
[5*4
CO-1; CO-1; BL-   b. Effect of types and number of splits in Decision tree algorithms   =20]
2
Following sections expected in the answer:
1. Brief explanation of decision trees
2. What are splits
3. Examples demonstrating the types and their effects in decision trees
algorithms.
 Sensitivity to hyper parameter tuning: Decision Trees are very
sensitive to hyper parameter tuning (i.e. parameters which are in
control of the programmer) and can be tuned to get better performance
out of a given model but can also vary drastically if the hyper
parameters are inaccurately tuned.
 Overfitting: Decision trees are prone to overfitting (Model learns the
data too well and hence performs well on training dataset but fails to
perform on testing dataset). Decision trees are prone to overfitting if
the breadth and depth of the tree is set to very high for a simpler dataset.
 Underfitting: Decision trees are also prone to under fitting (Model is
too simple for it to learn the dataset effectively). Decision tree suffers
from under fitting if the breadth and depth of the model or the number
of nodes are set too low. This does not allow the model to fit the data
properly and hence fails to learn.
c. MAE vs. MSE
Following sections expected in the answer:
1. Why these metrics are used in evaluating models.
2. Characteristics of both
********** 12 **********
--- page 13 ---
3. Which is better than the other in what scenario, with appropriate
example
MAE:
a. MAE is robust to outliers because it uses absolute errors, which
do not amplify large deviations.
b. Each error contributes linearly to the total error, so a single large
error does not disproportionately affect the MAE.
MSE:
c. MSE is sensitive to outliers because it squares the errors.
d. Large errors result in disproportionately larger contributions to
the MSE, which can significantly increase its value.
e. This means that MSE can be heavily influenced by a few large
errors.
d. Interpret the effect of data imputation on model performance and
analysis.
Following sections expected in the answer:
1. What is data imputation?
2. How does it effect performance with an example
3. Techniques to handle this
Imputation:
a. Is the process of managing missing values, which is one of the
most common problems when it comes to preparing data for
machine learning.
b. Human errors, data flow interruptions, privacy concerns, and
other factors could all contribute to missing values.
c. Missing values have an impact on the performance of machine
learning models for whatever cause.
Techniques to handle Imputation
 Variable Deletion (both numeric & categorical)
o Variable deletion involves dropping variables (columns) with
missing values on a case-by-case basis.
o This method makes sense when there are a lot of missing values
in a variable (60% and above) and if the variable is of relatively
less importance.
 Mean or Median Imputation (only numeric)
o Another common technique is to use the mean or median of the
non-missing observations.
o This strategy can be applied to a feature that has numeric data.
 Mode Imputation (Most Common Value) (both numeric & categorical)
o This method is replacing the missing values with the maximum
occurred value in a column/feature. This is a good option for
handling categorical columns/features.
 Assigning new category (only categorical)
o Replace the missing values with a new category. For example, we
may assign ‘U’ to the missing genders where ‘U’ stands for
Unknown.
 Predict the Missing Values (both numeric & categorical)
 It takes into account the correlation between the missing value
column and other columns to predict the missing values, it yields
much better results than the previous methods.
 Considering column having missing values as the dependent
variable ( or the y column). The rest of the columns can be the
independent variable ( or the x column), a simple Linear regression
********** 13 **********
--- page 14 ---
model or a classification model can be used to predict the missing
values.

FE AACR CIC 7] AAR oR oR ok
````
