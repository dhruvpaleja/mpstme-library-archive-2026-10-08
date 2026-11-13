# Advanced Social, Text and Media Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper c3a4fb40fc48

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSBS_7036/Advanced Social, Text and Media Analytics/ANS_Advanced Social, Text and Media Analytics(702CO0E020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Advanced Social, Text and Media Analytics
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a.   Analyze the role of Social Media Analysis in improving the performance of a
restaurant business. Examine how customer comments, online reviews, and
social media discussions can influence service quality, menu decisions, and
brand reputation.
2m,2m,
• Improving Service Quality: Analysis of customer comments and reviews
helps restaurants identify issues related to service, staff behavior, or waiting time 1m
and take corrective actions.
• Menu Improvement: Feedback from customers on social media helps identify
popular dishes and dishes that need improvement, assisting restaurants in refining
their menu.
.• Brand Reputation Management: Monitoring online reviews and ratings
helps restaurants maintain a positive brand image and respond quickly to negative
feedback.
b.   Differentiate between Temporal & Statistical visualization.
1m
Aspect   Temporal Visualization   Statistical Visualization   each
Represents data changes   Represents numerical summaries and   differen
Definition
over time.   distributions of data.
ce
Time-based patterns and   Quantitative measures and statistical
Focus
trends.   relationships.
********** 1 **********
--- page 2 ---
Timeline graphs, time-
Representa   Bar charts, histograms, scatter plots, pie
series charts, dynamic
tion   charts.
network evolution.
Showing how social media
Showing the percentage of positive vs
Example   interactions increase
negative sentiments in reviews.
during a festival.
c.   Draw and Explain web analytic process with diagram.
3m
dia,2m
explana
tion
d.   Explain how the efficiency of text clustering algorithms can be evaluated.
1. Purity
Purity measures the extent to which each cluster contains documents belonging
to a single class. Higher purity indicates better clustering quality.
2. Entropy
Entropy measures the distribution of different classes within a cluster. Lower
[5]
entropy indicates that the cluster is more homogeneous and therefore better.
3. Precision and Recall
Precision measures the proportion of correctly grouped documents in a cluster,
while recall measures how many relevant documents are successfully grouped
together.
4. F-Measure
a   Explain document level, sentence level, word/phrase level sentiment analysis
with an example.
Q2   1. Document-Level Sentiment Analysis   2m,2m
This level determines the overall sentiment of an entire document or review as
,1m
positive, negative, or neutral.
Example:
Review: “The mobile phone has excellent performance and battery life.”
Overall sentiment → Positive.
********** 2 **********
--- page 3 ---
2. Sentence-Level Sentiment Analysis
This level analyzes each individual sentence to determine its sentiment.
Example:
Sentence: “The camera quality is good, but the battery drains quickly.”
First part → Positive, Second part → Negative.
3. Word/Phrase-Level Sentiment Analysis
This level focuses on specific words or phrases that express sentiment.
Example:
Words like “excellent”, “amazing” → Positive,
Words like “poor”, “bad” → Negative.
b   Explain concepts of Degree Centrality, Closeness Centrality, Betweenness
Centrality, Eigenvector Centrality with example.
a.   Degree centrality
Degree centrality is a simple count of the total number of connections linked to
a vertex. It can be thought of as a kind of popularity measure, but a crude one
that does not recognize a difference between quantity and quality. Degree
centrality does not differentiate between a link to the president of the United
States and a link to a high school dropout. Degree is the measure of the total
number of edges connected to a particular vertex. For directed networks, there
are two measures of degree.
In-degree is the number of connections that point inward at a vertex.
Out-degree is the number of connections that originate at a vertex and point
outward to other vertices.
b.   Betweenness Centralities: Bridge Scores for Boundary Spanners. The
notion of paths is central to the study of networks. Perhaps one of the most 3m,3m
natural questions to ask about any two people in a network it is “How far apart   , 2m,
are they?” This distance is measured simply: the distance between people who
are not neighbours is measured by the smallest number of neighbour-to- 2m
neighbour hops from one to the other. For instance, people who are not your
neighbours, but are your neighbors’ neighbors, are a distance 2 from you, and
so on. The shortest path between two people is called the “geodesic distance”
and is used in many centrality metrics. For example, betweenness centrality is a
measure of how often a given vertex lies on the shortest path between two other
vertices. This can be thought of as a kind of “bridge” score, a measure of how
much removing a person would disrupt the connections between other people in
the network. The idea of brokering is often captured in the measure of
betweenness centrality.
A structural hole is a missing bridge. Wherever two or more groups fail to
connect, one can argue that there is a structural hole, a missing gap waiting to
be filled. Burt provides compelling evidence that individuals who bridge
structural holes are promoted faster than others.
Social network analysis has many strategic applications when people in an
organization can analyse their position and the position of others. Managers and
leaders can recognize gaps or disconnections within organizations and devote
********** 3 **********
--- page 4 ---
resources to traversing the divide. People may be able to apply social network
analysis to identify locations in which a gap exists and elect to fill them,
recognizing the value they can generate as broker between two otherwise
separate groups.
a.   Closeness Centrality: Distance Scores for Broadly Connected People.
Closeness centrality takes a different perspective from the other network
metrics, capturing the average distance between a vertex and every other vertex
in the network. Assuming that vertices can only pass messages to or influence
their existing connections, a low closeness centrality means that a person is
directly connected or “just a hop away” from most others in the network. In
contrast, vertices in very peripheral locations may have high closeness centrality
scores, indicating the number of hops or connections they need to take to connect
to distant others in the network. Think of closeness, paradoxically, as a
“distance” score. Some people are just a few miles from the big city, others must
drive for hours: similarly, people with high “closeness” centrality scores have
many miles or rather personal connections that they must travel to reach many
other people in the network. Note that in some cases the inverse of the average
distance to others in the network is used as a measure of closeness centrality. In
that case, higher values indicate a more central position.
c.   Eigenvector Centrality: Influence Scores for Strategically Connected
People
Eigenvector centrality is a more sophisticated view of centrality: a person with
few connections could have a very high eigenvector centrality if those few
connections were themselves very well connected. Eigenvector centrality allows
for connections to have a variable value, so that connecting to some vertices has
more benefit than connecting to others. The PageRank algorithm used by
Google’s search engine is a variant of Eigenvector Centrality.
a   Draw and explain architecture of Text mining in detail.
Dia7m
Q3   , 3m
explan
ation
********** 4 **********

[Text in pictures on this page, read by OCR]
{ Document ‘ Preprocessing Processed
| Document | Tasks Document
| Fetching’ .
> | Graming | > | Categorization, | =>} — Collection
Newsand | Techniques Feature/Term (categorized,
jews an i Extraction keyword-labeled,
ms KS __ time-stamped) a
rw “ a non
Compressed and/or | ee
Other Online { Hierarchical | ( Parsing Routines
Resources Representation
JL <r
A, | Text Mining Discovery
a Algorithms
> Pattern Identification,
Refinement Trend Analysis
Techniques JL <p

Suppression, Ordering,

Pruning, Generalization, ‘Browsing Functionality
Clusterit 4
ng a Simple Filters, Query om
oS Interpreter, Search Knowledge

Interpreter, Visualization | -—"°NECGE _]
Tools, GUI, Graphing

:

User

Gu

Figure 1.6. System architecture for an advanced or domain-oriented text mining system.
--- page 5 ---
b   Analyze Audience Analysis, behavior analysis and acquisition analysis,
conversion analysis provided by google analytics tool.
Audience analysis gives you an overview of the audience who visit your site
along with their session history, page views, bounce rate, etc. You can trace
the new as well as the returning users along with their geographical locations.
You can track −
1. The age and gender of your audience under Demographics.
2. The affinity reach and market segmentation under Interests.
3. Language and location under Geo.
4. New and returning visitors, their frequency, and engagement
under Behavior.
5. Browsers, Operating systems, and network of your audience
in Technology.
6. Mobile device info under Mobile.
7. Custom variable report under Custom. This report shows the activity
by custom modules that you created to capture the selections.   3m,3m
8. Benchmarking channels, locations, and devices under Benchmarking.   , 2m,
Benchmarking allows you to compare your metrics with other related   2m
industries. So, you can plot what you need to incur in order to overtake
the market.
9. Flow of user activity under Users flow to see the path they took on your
website.
Acquisition means ‘to acquire.’ Acquisition analysis is carried out to find out
the sources from where your web traffic originates. Using acquisition analysis,
you can −
1. Capture traffic from all channels, particular source/medium, and
referrals.
2. Trace traffic from AdWords (paid search).
3. See traffic from search engines. Here, you can see Queries, triggered
landing pages, and geographical summary.
4. Track social media traffic. It helps you to identify networks where
your users are engaged. You can see referrals from where your traffic
originates. You can also have a view of your hub activity, bookmarking
sites follow-up, etc. In the same tab, you can have a look at your
********** 5 **********
--- page 6 ---
endorsement details. It helps you measure the impact of social media on
your website.
5. See which plug-ins gave you traffic.
6. Have a look at all the campaigns you built throughout your website
with detailed statistics of paid/organic keywords and the cost incurred
on it.
Behaviour analysis monitors users’ activities on a website. You can find
behavioral data under the following four segments −
Site Content − It shows how many pages were viewed. You can see the
detailed interaction of data across all pages or in segments like content drill-
down, landing pages, and exit pages. Content drill-down is breaking up data
into sub-folders. A landing page is a page where the user lands, and an exit
page is where the user exits your site. You can measure the behavioural flow
in terms of content.
Site Speed − Here, you can capture page load time, execution speed, and
performance data. You can see how quickly the browser can parse through the
page. Further, you can measure page timings, and user timings, and get speed
suggestions. It helps you to know where you are lagging.
Site Search − It gives you a full picture of how the users search across your
site, what they normally look for, and how they arrive at a particular landing
page. You can analyze what they search for before landing on your website.
Events − Events are visitors’ actions with content, which can be traced
independently. Example − downloads, sign up, log-in, etc.
a   Explain role of these patterns in text mining with example: Concept   3m,3m
Distribution, Concept Proportion Distribution, Conditional Proportion   ,4m
Distribution.
Q4   Concept Distribution
Commonly, a text mining system needs to analyze the distribution of
concepts that are descendents of a particular node in a concept hierarchy.
For example, a text mining system might need to allow the analysis of the
distribution of concepts denoting finance topics – that is, descendents of the
finance topics node in an example concept hierarchy.
********** 6 **********
--- page 7 ---
To accomplish this, a text mining system could use the expression PK(x) to
refer to such distributions – it will assign to any concept x in K a value
between 0 and 1 – where the values are not required to add up to 1. This type
of proportion can be referred to as a concept distribution.
we are analyzing documents for finance-related topics. Suppose we find:
• PK(Banking) = 0.4
• PK(Loans) = 0.2
• PK(Stock Market) = 0.3
• PK(Credit Cards) = 0.1
These values mean that:
• 40% of the documents mention Banking
• 20% mention Loans
• And so on...
This gives a concept distribution under the "Finance" node.
Concept Proportion Distribution
If D is a collection of documents and K is a set of concepts, FK(D, x) is the
proportion of documents in D labeled with x for any x in K. When D is
clear from context, we will write this as FK(x).
Note the distinction between PK(x) and FK(x). PK(x) refers generically to any
function that is a concept distribution. FK(x) is a specific concept distribution
defined by a particular concept-labeled set of documents.
Thus, for example Ftopics(R, x) would represent the proportions of documents
in W labeled with keywords under the topics node in the concept hierarchy. In
this expression, topics is used as shorthand for referring to a set of concepts –
namely, all those that occur under the topics node – instead of explicitly
enumerating them all.
Also, note that F{k}(D, k) = f (D, k) – that is, FK subsumes the earlier defined
f when it is applied to a single concept. Unlike f, however, FK is restricted to
refer only to the proportion of occurrences of individual concepts (those
occurring in the set K).1 Thus f and F are not comparable.
Conditional Proportion Distribution
If D is a collection of documents and K and K are sets of concepts, FK(D, x
| K) is the proportion of those documents in D labeled with all the concepts
********** 7 **********
--- page 8 ---
in K that are also labeled with concept x (with x in K), that is, FK(D, x | K) =
FK(D/K | K, x).We often write this as FK(x | K) when D is clear from context.
Thus, for example, Ftopics(x | Argentina) would assign any concept x under
topics in the hierarchy with the proportion of documents labeled by x within
the set of all
documents labeled by the concept Argentina, and Ftopics(x | {UK,USA) is the
similar distribution for those documents labeled with both the UK and USA
concepts
b   Explain web crawler architecture with the help of diagram.   5m
dia,
5m
explan
ation
a   Explain Split URL testing, Multivariate testing, and Multipage testing with   3m,3m,
4m
example.
1. Split URL Testing
In Split URL testing, two completely different webpages with different URLs
are created to test which version performs better. Users are randomly directed to
either version, and their behavior is analyzed.
Q5   Example:
An e-commerce website tests two different product pages:
• Version A: www.shop.com/productA
• Version B: www.shop.com/new-productA
The company compares which page results in more purchases or clicks.
2. Multivariate Testing
Multivariate testing tests multiple elements of a webpage simultaneously to
determine which combination performs best.
********** 8 **********

[Text in pictures on this page, read by OCR]
WWW

DNS C__ > YS
Doc obot URL
FP’s filters set
SL — _—
Parse
Fetch Conten URL Dup
seen? filter URL
elim

URL Frontier
--- page 9 ---
Example:
A website tests different combinations of:
• Button color (red, blue)
• Headline text
•   Product image
The goal is to identify the best combination that increases user engagement or
conversions.
3. Multipage Testing
Multipage testing analyzes changes across multiple pages in a sequence to
understand how they affect user behavior throughout a process.
Example:
In a food delivery website, the company tests improvements across:
• Menu page
• Order page
• Checkout page
The test evaluates which version leads to more completed orders.
b   Write a short note on trend graph with example.   8m
explan
A trend graph is a very specialized representation that builds on the temporal
ation,
context graph as informed by the general approaches found in trend analysis. A
2m
trend graph can be obtained by partitioning the entire timespan covered by a
examp
time- or date stamped document collection, or both, into a series of
le
consecutive time intervals.
These intervals can then be used to generate a corresponding sequence of
temporal context graphs. This sequence of temporal context graphs can be
leveraged to create combined or cumulative trend graphs that display the
evolution of concept relationships in a given context by means of visual cues
such as the character and relative weight of edges in the graph. For instance,
several classes of edges may be used to indicate various conditions:
New Edges: edges that did not exist in the previous graph.
Increased Edges: edges that have a relatively higher weight in relation to the
previous interval.
Decreased Edges: edges that have a relatively decreased weight than the
previous interval.
Stable Edges: edges that have about the same weight as the corresponding
edge in the previous interval.
********** 9 **********
--- page 10 ---
a   Explain following web analytic tool along with features in details: Crazy Egg   [10]
Crazy Egg is an online analytics application that provides you eye-tracking
tools. It generates heatmaps based on where people clicked on your website.
Thus, it gives you an idea on where to focus. It lets you filter data on top 15
referrers, search terms, operating systems, etc.
It offers you insights in four different ways −
1. Heatmap − It gives you a defined picture of where visitors clicked on
your page. Where you need to make changes so as to improve
conversions.
Q6   2. Scrollmaps − It gives you insights into to what lengths people scroll
down on your page. With Crazy Egg, you can ensure where people
leave your page and where to hold them exactly and where to add more
to hold them for longer.
3. Overlay Tool − It gives you an overlay report of the number of clicks
occurring on your website. You may be able to get more on it.
4. Confetti − Confetti distinguishes clicks for you segmented by referral
sources, search terms, etc. Now, you know the origin of your clicks, so
you uncover the traffic sources. Put extra efforts there and you will earn
more traffic and revenue.
b   Explain The Hidden Markov Model (HMM) Probabilistic Model for   8m
Information Extraction with example.
explan
The Hidden Markov Model (HMM) is an analytical Model where the system   ation,
being modeled is considered a Markov process with hidden or unobserved
2m
states. Machine learning and pattern recognition applications, like gesture
recognition & speech handwriting, are applications of the Hidden Markov   examp
Model.
le
The main goal of HMM is to learn about a Markov chain by observing its
hidden states.
So let’s consider a day where Rahul called Ashok and told him that he has
cleaned his residence.
In that scenario, Ashok will have a belief that there are more chances of a rainy
day and we can say that belief Ashok has is the start probability of HMM let’s
say which is like the following.
The states and observation are:
states = ('Rainy', 'Sunny')
observations = ('walk', 'shop', 'clean')
And the start probability is:
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
Now the distribution of the probability has the weightage more on the rainy
day stateside so we can say there will be more chances for a day to being rainy
again and the probabilities for next day weather states are as following
transition_probability = {   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6}, }
From the above we can say the changes in the probability for a day is transition
probabilities and according to the transition probability the emitted results for
the probability of work that Rahul will perform is
emission_probability = {   'Rainy' : {'jog': 0.1, 'work': 0.4, 'clean': 0.5},
********** 10 **********
--- page 11 ---
'Sunny' : {'jog': 0.6, 'work: 0.3, 'clean': 0.1}, }
This probability can be considered as the emission probability.
Using the emission probability Ashok can predict the states of the weather or
using the transition probabilities Ashok can predict the work which Rahul is
going to perform the next day.
a   Consider a directed network with five pages P1, P2, P3, P4, P5 with the   2m
following links:   iteratio
P1→P3   n 0,
P2→P3, P4   2m
P3→P2   iteratio
P4→P5   n 1,
P5→P2, P3   3m
Q7   Apply the PageRank algorithm for two iterations and determine the final   iteratio
ranking of pages.   n 2,
3m
Pag Iteration Iteration Iteration   Final   final
e   0   1   2   Rank   rank
P1   1/5   1/5   1/5   5
P2   1/5   7/20   9/20   2
P3   1/5   9/20   1/2   1
P4   1/5   3/10   7/20   3
P5   1/5   1/5   1/4   4
b   Consider an e-commerce website that sells electronics such as mobile phones,   4m,3m
laptops, and accessories.   ,3m
a) Explain how A/B testing can be implemented on this website to improve
user engagement and product purchases.
b) Provide suitable examples of website elements that can be tested (such as
product page layout, “Add to Cart” button design, discount banners, etc.).
c) Discuss the advantages of A/B testing for improving conversion rate and
customer experience.
Implementation of A/B Testing
Create two versions of a webpage or feature (Version A and Version B) on the
e-commerce site.
Divide website visitors into two groups and show each group a different
version.
Track user behavior such as clicks, time spent on page, and product purchases.
********** 11 **********
--- page 12 ---
Compare the performance of both versions using metrics like conversion rate
and engagement.
Select the version that generates higher product purchases and better user
interaction.
This process follows the concept of A/B Testing.
b) Examples of Website Elements that can be Tested
Product page layout (placement of product images, description, and
specifications).
“Add to Cart” button design (color, size, or position).
Discount banners or promotional offers displayed on the homepage.
Product recommendation sections such as “Related Products”.
Checkout page design to make the purchase process easier.
c) Advantages of A/B Testing
Helps identify the most effective website design and features.
Improves conversion rate and product purchases.
Enhances customer experience and usability of the website.
Supports data-driven decision making for website improvements.
Helps businesses increase sales and customer engagement.
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 0f619340818a

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSBS_7036/Advanced Social, Text and Media Analytics/ANS_Advanced Social, Text and Media Analytics(702CO0E020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Advanced Social, Text and Media Analytics
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a.   Consider a scenario of an online food delivery platform like Zomato.
How can A/B testing be applied to test the impact of different menu layouts on
customer order rate? Explain in brief.
[5]
Create Variations (A and B versions)
Analyze Results
Implement the Best-Performing Version
b.   Identify and explain different types of sentiment analysis.
Polarity based Sentiment Analysis
Subjectivity based Sentiment Analysis   [5]
Feature / Aspect based Sentiment Analysis
c.   Dia 3m.
Draw and explain web crawler architecture.   explana
tion 2m
********** 1 **********
--- page 2 ---
d.   Differentiate between structural and semantic-based visualization.
Structural :
-Focuses on Structure
-topology of a graph that represents the actors and relationships in a social
network
1m for
each
differen
ce
semantic-based:
Structural visualizations less effective when the social network
becomes large.
Recent approaches have focused on a different aspect of social
networks semantics
Instead of highlighting the explicit relationships found in the data,
these represent high level attributes and connections of actors
and links either as specified explicitly in the data, or implicitly
inferred from cross referencing external sources
Q2   a   Explain with mathematical function, following common types of patterns   5m
encountered in text mining.   each
********** 2 **********

[Text in pictures on this page, read by OCR]
DNS =>
Doc obot URL

FP’s filters set

WWW

Parse [I
Fetch Conten URL OR
seen? filter .
elim

URL Frontier
--- page 3 ---
a. Concept selection
b. Average Proportion Distribution
Concept Selection
Whether as an initial step, to create a baseline, or to create more meaningful
subdivisions of a single document collection for comparison purposes, text
mining systems generally need to refer to some subcollection of a complete
document collection.
Given some collection of documents D, a text mining system will have a
requirement to refer to some subcollection of D that is labeled by one or more
given concepts.
If D is a collection of documents and K is a set of concepts, D/K is the subset
of documents in D labeled with all of the concepts in K. When it is clear from
the context, given a single concept k, rather than writing
D/{k} we use the notation D/k.
For example, the collection W contains a subset of the World Affairs collection
– namely those documents that are labeled with the concepts iran, nicaragua,
and reagan; W/bush contains the subset of documents that are labeled (at least)
with reagan;
Average Proportion Distribution
One of the baseline distributions text mining systems use to compare
distributions is the average distribution over a set of sibling nodes in the
hierarchy.
For example,
when looking at the proportions of loan within South American countries such
as f (W, loan | Argentina), f (W, loan | Brazil), and f (W, loan | Columbia)), an
end user may be interested in the average of all proportions of this form for all
the South American countries – that is, the average of all proportions of the
form f (W, loan |k), where k ranges over all South American countries.
Given a collection of documents D, a concept k, and an internal node in the
hierarchy n, an average concept proportion, denoted by a(D, k | n), is the
average value of f (D, k| k), where k ranges over all immediate children of n –
that is, a(D, k| n) = Avg{k is a child of n}{ f (D, k| k)}.When D is clear from
context, this will be written a(k|n).
********** 3 **********
--- page 4 ---
b   Describe the following fundamental concepts used in graph theory.
1. Dyad
2. Triad
3. Actors
4. Relational Ties
5. Subgroup
Relational Tie. Actors are linked to one another by social ties. As we will see
in the examples discussed throughout this book, the range and type of ties can
be quite extensive. The defining feature of a tie is that it establishes a linkage
between a pair of actors. Some of the more common examples of ties employed
in network analysis are:
Evaluation of one person by another (for example expressed friendship, liking,
or respect)
Transfers of material resources (for example business transactions, lending or
borrowing things)   2m
Association or affiliation (for example jointly attending "a social event, or each
belonging to the same social club)
Behavioural interaction (talking together, sending messages)
Movement between places or statuses (migration, social or physical mobility)
Physical connection (a road, river, or bridge connecting two points)
Formal relations (for example authority)
Biological. Relationship (kinship or descent)
Dyad. At the most basic level, a linkage or relationship establishes a tie between
two actors.
Triad. Relationships among larger subsets of actors may also be studied. Many
important social network methods and models focus on the triad; a subset of
three actors and the (possible) tie(s) among them.
Subgroup. Dyads are pairs of actors and associated ties; triads are triples of
actors and associated ties. It follows that we can define a subgroup of actors as
any subset of actors, and all ties among them.
a   Explain audience analysis, behavior analysis and acquisition analysis provided
by google analytics.
Audience analysis gives you an overview of the audience who visit your site
Q3   along with their session history, page views, bounce rate, etc. You can trace   3,3,4
the new as well as the returning users along with their geographical locations. m each
You can track −
1. The age and gender of your audience under Demographics.
2. The affinity reach and market segmentation under Interests.
3. Language and location under Geo.
********** 4 **********
--- page 5 ---
4. New and returning visitors, their frequency, and engagement
under Behavior.
5. Browsers, Operating systems, and network of your audience
in Technology.
6. Mobile device info under Mobile.
7. Custom variable report under Custom. This report shows the activity
by custom modules that you created to capture the selections.
8. Benchmarking channels, locations, and devices under Benchmarking.
Benchmarking allows you to compare your metrics with other related
industries. So, you can plot what you need to incur in order to overtake
the market.
9. Flow of user activity under Users flow to see the path they took on your
website.
Acquisition means ‘to acquire.’ Acquisition analysis is carried out to find out
the sources from where your web traffic originates. Using acquisition analysis,
you can −
1. Capture traffic from all channels, particular source/medium, and
referrals.
2. Trace traffic from AdWords (paid search).
3. See traffic from search engines. Here, you can see Queries, triggered
landing pages, and geographical summary.
4. Track social media traffic. It helps you to identify networks where
your users are engaged. You can see referrals from where your traffic
originates. You can also have a view of your hub activity, bookmarking
sites follow-up, etc. In the same tab, you can have a look at your
endorsement details. It helps you measure the impact of social media on
your website.
5. See which plug-ins gave you traffic.
6. Have a look at all the campaigns you built throughout your website
with detailed statistics of paid/organic keywords and the cost incurred
on it.
Behaviour analysis monitors users’ activities on a website. You can find
behavioral data under the following four segments −
Site Content − It shows how many pages were viewed. You can see the
detailed interaction of data across all pages or in segments like content drill-
********** 5 **********
--- page 6 ---
down, landing pages, and exit pages. Content drill-down is breaking up data
into sub-folders. A landing page is a page where the user lands, and an exit
page is where the user exits your site. You can measure the behavioural flow
in terms of content.
Site Speed − Here, you can capture page load time, execution speed, and
performance data. You can see how quickly the browser can parse through the
page. Further, you can measure page timings, and user timings, and get speed
suggestions. It helps you to know where you are lagging.
Site Search − It gives you a full picture of how the users search across your
site, what they normally look for, and how they arrive at a particular landing
page. You can analyze what they search for before landing on your website.
Events − Events are visitors’ actions with content, which can be traced
independently. Example − downloads, sign up, log-in, etc.
b   Draw and explain web traffic model. Differentiate between organic traffic and
paid traffic.
Dia
5m,
explan
ation
5m
a   Dia
Draw and explain system architecture for an advanced text mining system.   7m,
Q4
3m
explan
ation
********** 6 **********

[Text in pictures on this page, read by OCR]
J Web-request time —> } Viewing

In-line Object 1

Main Object

In-line Object 2

In-line Object 3

« HTTP ON m« HTTP OFF >!

Figure 1: Overview of the basic model
--- page 7 ---
b   Explain the use of the Optimizely web analytics tool, along with the steps to   Use
use Optimizely to set up and generate reports.   3m,
steps
7m
Optimizely provides you with administrative and management functionality to
let you create accounts, organize projects, and experiment. This facility helps
you in tracking clicks, conversions, sign-ups, etc.
You are allowed to run tests and use custom integrations with the Optimizely
interface. All you need is −
1. Set up an account on Optimizely and add a generated script.
2. Once you are done with it, select your test pages. It implies the factors
you want to run the test on.
3. Set Goals. To set goals, click on the flag icon at the top right of the
page and follow up on the instructions. Check the metrics you are
looking for. Click Save.
4. You can create variations with the usual editor like changing text and
images.
5. Next step is monitoring your tests. You need to test which landing
pages are performing well. What is attracting the visitors? What is the
********** 7 **********

[Text in pictures on this page, read by OCR]
a

WWW & FTP
Resources S pa -
a ‘ Preprocessing Processed
| Document j Tasks Document c
I Fetching/ I -
a> | Crawling > Categorization, q Collection
Ne d | Techniques Feature/Term (categorized,
wear | Extraction keyword-labeled, Sources
mal ene . 7 time-stamped) oo
ca ‘ iL Lan
Compressed and/or / Oe
Other Online i Hierarchical i (Parsing Routines)
Resources Representation
JL t
| Text Mit ing Discovery
a Algorithms
o> Pattern Identification,
Refinement \ Trend Analysis
Techniques JIL
Suppression, Ordering, ‘ W
Pruning, G lization, eee
ae Gustering ” Browsing Functionality
a Simple Filters, Query eo und
, Interpreter, Search Knowledge
5 , Interpreter, Visualization \ -—
Tools, GUI, Graphing
bt.

User

Figure 1.6. System architecture for an advanced or domain-oriented text mining system.
--- page 8 ---
bounce rate? Understand the statistics, filter the non-performing areas,
and conclude the test.
6. You can run multipage tests using javascript editors.
7. Optimizely gives you a better understanding of conversion rate
optimization and running tests.
a   Identify and explain SEO strategies.   10m
1) Get Your Site Fully Indexed
2) Get Your Pages Visible
3) Build Links & PageRank
4) Leverage Your PageRank
Q5
5) Encourage Clickthrough
6) Track the Right Metrics
7) Avoid Worst Practices
b   Identify and explain steps involved in text clustering and brief levels of text   5m
clustering.
steps,
5m
steps:
levels
• Text pre-processing: Text can be noisy, hiding information between
stop words, inflexions and sparse representations. Pre-processing makes
the dataset easier to work with.
• Feature Extraction: One of the commonly used technique to extract
the features from textual data is calculating the frequency of
words/tokens in the document/corpus.
•   Clustering: We can then cluster different text documents based on the
features we have generated.
Text clustering can be document level, sentence level or word level.
a   Explain The Hidden Markov Model Model with example.   Explan
ation
The Hidden Markov Model (HMM) is an analytical Model where the system
being modeled is considered a Markov process with hidden or unobserved   7m,
states. Machine learning and pattern recognition applications, like gesture
examp
recognition & speech handwriting, are applications of the Hidden Markov
Model.   le 3m
The main goal of HMM is to learn about a Markov chain by observing its
hidden states.
Q6   So let’s consider a day where Rahul called Ashok and told him that he has
cleaned his residence.
In that scenario, Ashok will have a belief that there are more chances of a rainy
day and we can say that belief Ashok has is the start probability of HMM let’s
say which is like the following.
The states and observation are:
states = ('Rainy', 'Sunny')
observations = ('walk', 'shop', 'clean')
And the start probability is:
********** 8 **********
--- page 9 ---
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
Now the distribution of the probability has the weightage more on the rainy
day stateside so we can say there will be more chances for a day to being rainy
again and the probabilities for next day weather states are as following
transition_probability = {   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6}, }
From the above we can say the changes in the probability for a day is transition
probabilities and according to the transition probability the emitted results for
the probability of work that Rahul will perform is
emission_probability = {   'Rainy' : {'jog': 0.1, 'work': 0.4, 'clean': 0.5},
'Sunny' : {'jog': 0.6, 'work: 0.3, 'clean': 0.1}, }
This probability can be considered as the emission probability.
Using the emission probability Ashok can predict the states of the weather or
using the transition probabilities Ashok can predict the work which Rahul is
going to perform the next day.
b   Identify and explain Pre-Processing Techniques – General Purpose NLP Task.   [10]
1. Tokenization
The approach most frequently found in text mining systems involves breaking
the text into sentences and words, which is called tokenization. The main
challenge in identifying sentence boundaries in the English language is
distinguishing between a period that signals the end of a sentence and a period
that is part of a previous token like Mr., Dr., and so on. It is common for the
tokenizer also to extract token features capitalization, the inclusion of digits,
punctuation, special characters, and so on
2. Part of Speech Tagging
POS tagging is the annotation of words with the appropriate POS tags based on
the context in which they appear. POS tags divide words into categories
based on the role they play in the sentence in which they appear. POS tags
provide information about the semantic content of a word. Nouns usually
denote “tangible and intangible things,” whereas prepositions express
relationships between “things.”
Most POS tag sets make use of the same basic categories. The most common
set of tags contains seven different tags (Article, Noun, Verb, Adjective,
Preposition, Number, and Proper Noun). Some systems contain a much more
elaborate set of tags. For example, the complete Brown Corpus tag set has no
less than 87 basic tags.
3 Syntactical Parsing
Syntactical parsing components perform a full syntactical analysis of sentences
according to a certain grammar theory. The basic division is between the
constituency and dependency grammar.
4 Shallow Parsing
Instead of providing a complete analysis (a parse) of a whole sentence, shallow
parsers produce only parts that are easy and unambiguous. Typically, small
and simple noun and verb phrases are generated, whereas more complex
clauses are not formed. Similarly, most prominent dependencies might be
formed, but unclear and ambiguous ones are left unresolved.
a   Consider a small web graph of pages (1,2,3,4).   2m
Q7
Page 1 links to 2,   ite.0,
2 links to 5,   3m
********** 9 **********
--- page 10 ---
5 links to 4,   iter1,3
4 links to 5, 3,   m iter
3 links to 1,2,4,5   3, rank
If PageRank is applied, which page will have the lowest rank after iteration 2. 2m
b   Write a short note on context graph with example.   Explan
ation
Context relationships are often represented by a context graph, which is a   8m ,
graphic representation of the relationship between a set of concepts (e.g.,
examp
countries) as reflected in a corpus with respect to a given context (e.g.,
crude oil).   le 2m
A context graph consists of a set of vertices (also sometimes referred to as
nodes) and edges. The vertices (or nodes) of the graph represent concepts.
Weighted “edges” denote the affinity between the concepts.
Each vertex in the context graph signifies a single concept, and two
concepts are connected by an edge if their similarity, with respect to a
predefined similarity function, is larger than a given threshold (similarity
functions in graphing are discussed in greater detail in Chapter X). A context
graph is defined with respect to a given context, which determines the
context in which the similarity of concepts is of interest.
********** 10 **********

[Text in pictures on this page, read by OCR]
Iteration 0 Iteration 1 Iteration 2 Final
Rank

1/5 1/20 1/40 5
1/5 5/20 3/40 4
1/5 1/10 5/40 5
1/5 5/20 15/40 2

1/5 7/20 16/40 1
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 466c03422cd0

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSBS_7036/Advanced Social, Text and Media Analytics/ANS_Advanced Social, Text and Media Analytics(702CO0E020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Social, Text and Media Analytics
Date: 02 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a.   Analyze how Social Media Analysis can support the operations of an e-
commerce business. Examine how analyzing customer reviews, ratings, and
online discussions can help in understanding consumer behavior, improving
products, and enhancing marketing strategies.
Understanding Consumer Behavior: By analyzing reviews, ratings, and 2m,2m,
comments, businesses can identify customer preferences, needs, and buying 1m
patterns.   each
Product Improvement: Feedback from customers helps companies identify
product strengths and weaknesses and improve product quality.
Marketing Strategy Enhancement: Analysis of online discussions helps
businesses design targeted promotions and personalized marketing campaigns.
b.   Differentiate between Structural & Semantic visualization.
1m
each
differen
ce
********** 1 **********
--- page 2 ---
Aspect   Structural Visualization   Semantic Visualization
Focuses on the structure of the Focuses on the meaning or
Definition network, showing how nodes   attributes of the data
and edges are connected.   represented in the network.
To analyze relationships and   To understand context, topics,
Main
connectivity patterns between   or information associated
Purpose
nodes.   with nodes and links.
Uses labels, colors, or
Representa Graph structures such as node–
annotations to represent
tion   link diagrams, network graphs.
content or meaning.
Displaying connections   Showing the topics discussed
Example   between users in a social   by users or the type of
network.   relationship between them.
c.   Draw and explain web crawler architecture.
3m
dia.,
2m
explana
tion
d.   Explain how domain ontology use classes and relationship between these
classes.
A domain ontology is a collection of:
•   Classes or concepts (like Disease, Patient, Symptom in medicine)
•   Relationships between those concepts (like Patient has Symptom)
[5]
It’s basically a structured knowledge base that represents the key facts and
relationships for a specific domain.
It acts as background knowledge that machines can use to make better sense of
text.It’s like a vocabulary where all the terms and their meanings are clearly
defined, not just for humans but also in a way that machines can understand.
********** 2 **********

[Text in pictures on this page, read by OCR]
WWW

DNS —=_> —_—
Doc obot URL
FP’s filters set
—_E_ MSE”
Parse
Fetch Conten URL Dup
seen?| |filter| | URL
elim

URL Frontier
--- page 3 ---
Text mining systems exploit (i.e., use) domain ontologies to:
• Understand what terms mean
• Connect related concepts
•   Infer additional information
• Ensure consistency when analyzing documents from the same field
For example:
•   If a document mentions hypertension, the system can use the ontology to
recognize it's a type of disease, possibly linked to heart conditions.
a   Explain following tool in brief. Ling Pipe, OpenNLP, Stanford Parser and Part-
of-Speech (POS) Tagger, NLTK, OpinionFinde.
 Ling Pipe
   linguistic processing of text including entity extraction,
clustering and classification, etc.
 http://alias-i.com/lingpipe/
 OpenNLP
 the most common NLP tasks, such as POS tagging, named entity
extraction, chunking and coreference resolution.
 http://opennlp.apache.org/
Q2    Stanford Parser and Part-of-Speech (POS) Tagger   2m
 http://nlp.stanford.edu/software/tagger.shtm/   each
 NLTK
 Toolkit for teaching and researching classification, clustering
and parsing
 http://www.nltk.org/
 OpinionFinder
 subjective sentences , source (holder) of the subjectivity and
words that are included in phrases expressing positive or
negative sentiments.
 Basic sentiment tokenizer plus some tools, by Christopher Potts
 Twitter NLP and Part-of-speech tagging
b   Explain concepts of FULL, Partial and Egocentric network along with example.
4m,4m
1.   FULL, Partial and Egocentric networks   ,3m
********** 3 **********
--- page 4 ---
Network analysts call the individual that is the focus of attention “ego” and the
people he or she is connected to “alters.”
Some networks, called egocentric networks, only include individuals who are
connected to a specified ego. For example, a network of your personal Facebook
friends would be an egocentric network because you are, by definition,
connected to all other vertices.
An ego-centred network consists of a focal actor, termed ego, as set of alters
who have ties to ego, and measurements on the ties among these alters. For
example, when studying people, one samples respondents, and each respondent
reports on a set of alters to whom they are tied, and on the ties among these
alters. Such data are often referred to as personal network data.
More generally, egocentric networks can extend out any number of “degrees”
from ego. The basic “1-degree” ego network consists of the ego and their alters.
The “1.5-degree” ego network extends the 1-degree network by including
connections between all of the alters.
The “2-degree” ego network extends the 1.5-degree network by including all of
the alters’ own alters (i.e., friends of friends), some of whom may not be
connected to ego.
Higher-degree networks (e.g., 2.5, 3) are feasible to create but not used as often
in practice because they can quickly become intractable.
A full or complete network contains all the people or entities of interest and the
connections among them. All egos are treated equally. A full network is often
created and available when a single system, such as social media platform, acts
as a hub among a group of connected people or groups.
a   Dia.
6m,
Q3
Explain Text mining architecture in detail.   explan
ation
4m
********** 4 **********
--- page 5 ---
b   Analyze the use of the Crazy Egg tool in web analytics. Explain four different
ways in which Crazy Egg provides insights into user behavior.
Crazy Egg is an online analytics application that provides you eye-tracking
tools. It generates heatmaps based on where people clicked on your website.
Thus, it gives you an idea on where to focus. It lets you filter data on top 15
referrers, search terms, operating systems, etc.
It offers you insights in four different ways −   1m
1. Heatmap − It gives you a defined picture of where visitors clicked on
use,
your page. Where you need to make changes so as to improve
conversions.   2m
2. Scrollmaps − It gives you insights into to what lengths people scroll
each
down on your page. With Crazy Egg, you can ensure where people
leave your page and where to hold them exactly and where to add more way
to hold them for longer.
3. Overlay Tool − It gives you an overlay report of the number of clicks
occurring on your website. You may be able to get more on it.
4. Confetti − Confetti distinguishes clicks for you segmented by referral
sources, search terms, etc. Now, you know the origin of your clicks, so
you uncover the traffic sources. Put extra efforts there and you will earn
more traffic and revenue.
a   Explain role of below mentioned patterns in text mining with example:   3m,3m
Q4   Concept Selection, Concept Proportion, Conditional Concept Proportion.   ,4m
Concept Selection
********** 5 **********

[Text in pictures on this page, read by OCR]
a

WWW & FTP
Resources S pa -
a ‘ Preprocessing Processed
| Document j Tasks Document c
I Fetching/ I -
a> | Crawling > Categorization, q Collection
Ne d | Techniques Feature/Term (categorized,
wear | Extraction keyword-labeled, Sources
mal ene . 7 time-stamped) oo
ca ‘ iL Lan
Compressed and/or / Oe
Other Online i Hierarchical i (Parsing Routines)
Resources Representation
JL t
| Text Mit ing Discovery
a Algorithms
o> Pattern Identification,
Refinement \ Trend Analysis
Techniques JIL
Suppression, Ordering, ‘ W
Pruning, G lization, eee
ae Gustering ” Browsing Functionality
a Simple Filters, Query eo und
, Interpreter, Search Knowledge
5 , Interpreter, Visualization \ -—
Tools, GUI, Graphing
bt.

User

Figure 1.6. System architecture for an advanced or domain-oriented text mining system.
--- page 6 ---
Whether as an initial step, to create a baseline, or to create more meaningful
subdivisions of a single document collection for comparison purposes, text
mining systems generally need to refer to some subcollection of a complete
document collection.
Given some collection of documents D, a text mining system will have a
requirement to refer to some subcollection of D that is labeled by one or more
given concepts.
If D is a collection of documents and K is a set of concepts, D/K is the subset
of documents in D labeled with all of the concepts in K. When it is clear from
the context, given a single concept k, rather than writing
D/{k} we use the notation D/k.
For example, the collection W contains a subset of the World Affairs collection
– namely those documents that are labeled with the concepts iran, nicaragua,
and reagan; W/bush contains the subset of documents that are labeled (at least)
with reagan;
Concept Proportion
Text mining systems often need to identify or examine the proportion of a set
of documents labeled with a particular concept. This analytic is commonly
referred to as concept proportion.
If D is a collection of documents and K is a set of concepts, f (D, K) is the
fraction of documents in D labeled with all of the concepts in K, that is, f (D,
K) = |D/ k|
|D| . Given one concept k, rather than writing f (D, {k}), we use the notation f
(D, k). When D is clear from context, we drop it and write f (k).
Thus, for example, f(W, {iran, nicaragua, reagan} is the fraction of
documents in
the World Affairs collection labeled with iran, nicaragua, and reagan; f
(reagan) is
the proportion of the collection labeled with the concept reagan; and f (G8) is
the proportion labeled with any (G8) country.
Conditional Concept Proportion
By employing definitions of selection and proportion, text mining systems can
already begin identifying some useful quantities for analyzing a set of
documents.
For example, a text mining system might want to identify the proportion of
those documents labeled with K2 that are also labeled by K1, which could be
designated by expression f(D/K2, K1).
This type of proportion occurs regularly enough that it has received an explicit
name and notation: conditional concept proportion.
********** 6 **********
--- page 7 ---
If D is a collection of documents and K1 and K2 are sets of concepts, f (D, K1 |
K2) is the proportion of all those documents in D labeled with K2 that are also
labeled with K1, that is, f (D, K1 | K2) = f (D/K2, K1). When D is clear from
context, we will write this as f (K1 | K2).
Applying this definition, we find that f (reagan | iran) would represent the
proportion of all documents labeled by the concept iran that are also
labeled by the concept reagan.
Suppose you have 100 documents:
• 40 are labeled with "Iran"
Out of these 40, 25 are also labeled with "Reagan"
b   Explain any five strategies for website which are recommended for SEO.   2m
1) Get Your Site Fully Indexed   each
2) Get Your Pages Visible
3) Build Links & PageRank
4) Leverage Your PageRank
5) Encourage Clickthrough
a   Explain working of search engine with diagram.   Explan
ation
Crawling: Automated programs, called crawlers or "spiders," systematically
7m, 3m
browse the web by following links from one page to another. They find new   dia.
and updated pages, collecting their content and URLs.
Indexing: The information collected during the crawling process is analyzed,
Q5   organized, and stored in a massive database called an index. The index stores
crucial details about each page, such as keywords, content type, and freshness,
making it searchable.
Ranking (and Retrieval): When a user enters a search query, the search engine
processes the request, retrieves relevant pages from its index, and uses
complex algorithms to rank them by relevance.
********** 7 **********
--- page 8 ---
b   Write a short note on context graph with example.   Explan
ation
Context relationships are often represented by a context graph, which is a
graphic representation of the relationship between a set of concepts (e.g.,   8m ,
countries) as reflected in a corpus with respect to a given context (e.g.,
examp
crude oil).
A context graph consists of a set of vertices (also sometimes referred to as   le 2m
nodes) and edges. The vertices (or nodes) of the graph represent concepts.
Weighted “edges” denote the affinity between the concepts.
Each vertex in the context graph signifies a single concept, and two
concepts are connected by an edge if their similarity, with respect to a
predefined similarity function, is larger than a given threshold (similarity
functions in graphing are discussed in greater detail in Chapter X). A context
graph is defined with respect to a given context, which determines the
context in which the similarity of concepts is of interest.
a   Draw and explain web traffic model. Mention advantages of organic traffic and 4m
paid traffic.
dia,4m
exlana
tion,2
m
advant
Q6
ages
A typical Web page consists of a Hypertext document with links to other
objects that make up the whole page. An object is an entity stored on a server
********** 8 **********

[Text in pictures on this page, read by OCR]
Display The
. Results From

Stores The
Information Into
DataBase

Search = TYosecmssene
Engines =. =
—s , Information

jin Web Sites

E.
Web Crawlers or Crawls The
Web Spiders (Je) Web Sites

J Web-request time —> } Viewing

In-line Object 1

Main Object

In-line Object 2

In-line Object 3

« HTTP ON m« HTTP OFF >!

Figure 1: Overview of the basic model
--- page 9 ---
as a file. There are two kinds of objects, a main object and an in-line object.
The file containing an HTML document is referred to as a main object and the
objects linked from the Hypertext document are referred to as in-line objects
The basic model of Web traffic is shown in Figure 1. A new Web-request is
immediately generated after expiration of the viewing period.
Organic traffic includes all visitors that come to your website through search
results you did not pay for. This kind of traffic is important for every website
and is directly influenced by the quality of your content and SEO measures.
Paid traffic, on the other hand, refers to visits that you paid for. If you place
ads on social media or Google and somebody accesses your website by
clicking on one of these ads, this is referred to as paid traffic.
b   Explain trend analysis and Ephemeral association and use of these methods in 5m
analyzing Document Collection Over Time.
each
Trend analysis is a technique used to identify patterns or changes in data over a
period of time. In text mining and data analytics, it helps analyze how certain
topics, keywords, or events become more or less popular over time. By
examining historical data, organizations can detect emerging topics, predict
future developments, and understand user behavior. For example, analyzing
social media posts may reveal increasing discussions about a new technology
or product. Trend analysis is widely used in marketing, finance, social media
monitoring, and decision-making systems to understand long-term patterns and
support strategic planning.
Ephemeral Association
Ephemeral association refers to temporary relationships or patterns that appear
in data for a short period of time and disappear quickly. Unlike long-term
associations, these patterns are short-lived and often occur due to specific
events or sudden changes in user interests. For instance, during a major sports
event or a festival, certain keywords or products may suddenly appear together
frequently in search queries or online discussions, but the association may
vanish once the event ends. Detecting ephemeral associations is useful for
identifying short-term trends, event-based marketing opportunities, and real-
time analysis of dynamic data sources such as social media streams.
a   Consider a directed network with five pages P1,P2,P3,P4,P5 with the   10
following links:
P1→P2
Q7   P2→P3, P4
P3→P5
P4→P3
P5→P3, P4
Initially all pages have equal rank.
********** 9 **********
--- page 10 ---
Apply the PageRank algorithm for two iterations and determine the final
ranking of pages.
Pag Iteration Iteration Iteration   Final
e   0   1   2   Rank
P1   1/5   1/5   1/5   5
P2   1/5   2/5   1/4   4
P3   1/5   3/5   7/10   1
P4   1/5   7/20   9/20   2
P5   1/5   3/10   7/20   3
b   Consider an online travel website that provides tour packages, flight booking,   4m,4m
and hotel booking services.   ,3m
a) Explain how A/B testing can be implemented on this website to improve
user engagement and conversion rates.
b) Provide suitable examples of elements that can be tested (such as booking
buttons, page layout, offers, etc.).
c) Discuss the advantages of A/B testing for improving business performance.
a) Implementation of A/B Testing
Create two versions of a webpage (Version A and Version B) with slight
variations.
Randomly divide website visitors into two groups.
Each group is shown a different version of the webpage.
Measure performance using metrics such as click-through rate, bookings, or
user engagement.
Select the version that produces higher conversions or better user interaction.
b) Elements that can be Tested
Booking buttons (color, size, position).
Page layout or design of tour package or hotel pages.
Special offers and discounts displayed on the homepage.
Images or descriptions of travel destinations.
Call-to-action messages such as “Book Now” or “Get Best Deal”.
c) Advantages of A/B Testing
Helps identify the most effective website design and features.
Improves user engagement and customer experience.
********** 10 **********
--- page 11 ---
Increases conversion rates and bookings.
Enables data-driven decision making.
Helps businesses optimize marketing and promotional strategies.
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 03829c28ed98

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSBS_7036/Advanced Social, Text and Media Analytics/ANS_Advanced Social, Text and Media Analytics(702CO0E020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Social, Text and Media Analytics
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:
a.   Consider a travel booking website like MakeMyTrip.   [5]
How can A/B testing be applied to compare two versions of the homepage to
improve flight booking conversions? Explain in brief.
Create Variations (A and B versions)
Analyze Results
Implement the Best-Performing Version
b.   Identify advantages and disadvantages of social media analytics.   2.5
Advantages of Social Media Analytics   adv,2.5
Improved Customer Insights:   disadv.
Enhanced Marketing Strategies:
Brand Monitoring & Reputation Management:
Disadvantages of Social Media Analytics
Data Privacy and Ethical Concerns:
High Volume and Noise in Data:
Sentiment Misinterpretation:
********** 1 **********
--- page 2 ---
c.   Draw and explain web analytic process with diagram.   3m dia,
2m
explana
tion
d.   Differentiate between temporal and statistical based visualization.   1m
each
Temporal A special type of semantic information that has captured the differen
attention of social network visualization researchers is time.   ce
Since social interaction is a time dependent phenomenon, it is only natural to
represent the temporal dimension using visual means.
A semantic approach seems more appropriate.
However, time as a dimension deserves a treatment different from other data
specific node attributes One of the difficulties to represent time is a shortage
of
dimensions to depict a dynamic network in a 2 D display.
Statistical
Often correspond to network statistics that represent the structure of the
network, such as degree, centrality and the clustering coefficient.
While the first two describe the importance across the network, the latter metric
indicates how clusterable are the nodes in a network.
A way to understand these distributions is via visual summaries, such as
histograms.
a   Explain with mathematical function, following common types of patterns
encountered in text mining.
Q2   5m
a. Concept Proportion
each
b. Average Concept Distribution
********** 2 **********
--- page 3 ---
Concept Proportion
Text mining systems often need to identify or examine the proportion of a set
of documents labeled with a particular concept. This analytic is commonly
referred to as concept proportion.
If D is a collection of documents and K is a set of concepts, f (D, K) is the
fraction of documents in D labeled with all of the concepts in K, that is, f (D,
K) = |D/ k|
|D| . Given one concept k, rather than writing f (D, {k}), we use the notation f
(D, k). When D is clear from context, we drop it and write f (k).
Thus, for example, f(W, {iran, nicaragua, reagan} is the fraction of
documents in
the World Affairs collection labeled with iran, nicaragua, and reagan; f
(reagan) is
the proportion of the collection labeled with the concept reagan; and f (G8) is
the proportion labeled with any (G8) country.
Average Concept Distribution
Given a collection of documents D and two internal nodes in the hierarchy n
and n, an average concept distribution, denoted by An(Dx | n), is the
distribution that, for any x that is a child of n, averages x’s proportions over
all children of n – that is, An(D, x | n) = Avg{k is a child of n}{Fn(D, x | k)}.
When clear from context, this will be written An(x | n).
For example Atopics(x|South America), which can be read as “the average
distribution of topics within South American countries,” gives the average
proportion within all South American countries for any topic x.
A very basic operation for text mining systems using concept-distributions is
the display of conditional concept-proportion distributions. For example, a
user may be interested in seeing the proportion of documents labeled with
each child of topics for all those documents labeled by the concept Argentina,
that is, the proportion of Argentina documents that are labeled with each
topic keyword.
b   Explain following terms with example.   2.5m
i.   Betweenness Centrality
each
ii.   Eigenvector Centrality
iii.   Degree Centrality
iv.   Closeness Centrality
Betweenness Centralities: Bridge Scores for Boundary Spanners. The notion
of paths is central to the study of networks. Perhaps one of the most natural
questions to ask about any two people in a network it is “How far apart are
they?” This distance is measured simply: the distance between people who are
********** 3 **********
--- page 4 ---
not neighbours is measured by the smallest number of neighbour-to-neighbour
hops from one to the other. For instance, people who are not your neighbours,
but are your neighbors’ neighbors, are a distance 2 from you, and so on. The
shortest path between two people is called the “geodesic distance” and is used
in many centrality metrics. For example, betweenness centrality is a measure
of how often a given vertex lies on the shortest path between two other vertices.
Eigenvector Centrality: Influence Scores for Strategically Connected People
Eigenvector centrality is a more sophisticated view of centrality: a person
with few connections could have a very high eigenvector centrality if those
few connections were themselves very well connected. Eigenvector centrality
allows for connections to have a variable value, so that connecting to some
vertices has more benefit than connecting to others. The PageRank algorithm
used by Google’s search engine is a variant of Eigenvector Centrality.
Degree centrality
Degree centrality is a simple count of the total number of connections linked
to a vertex. It can be thought of as a kind of popularity measure, but a crude
one that does not recognize a difference between quantity and quality. Degree
centrality does not differentiate between a link to the president of the United
States and a link to a high school dropout.
Closeness Centrality: Distance Scores for Broadly Connected People.
Closeness centrality takes a different perspective from the other network
metrics, capturing the average distance between a vertex and every other vertex
in the network. Assuming that vertices can only pass messages to or influence
their existing connections, a low closeness centrality means that a person is
directly connected or “just a hop away” from most others in the network. In
contrast, vertices in very peripheral locations may have high closeness
centrality scores, indicating the number of hops or connections they need to
take to connect to distant others in the network.
a   Identify use of Crazy Egg and explain in brief four different ways Crazy Egg   Use
offers to provide insights wrt to input.   2m ,
4ways
Crazy Egg is an online analytics application that provides you eye-tracking   :2m
tools. It generates heatmaps based on where people clicked on your website.
each
Thus, it gives you an idea on where to focus. It lets you filter data on top 15
referrers, search terms, operating systems, etc.
Q3
It offers you insights in four different ways −
1. Heatmap − It gives you a defined picture of where visitors clicked on
your page. Where you need to make changes so as to improve
conversions.
2. Scrollmaps − It gives you insights into to what lengths people scroll
down on your page. With Crazy Egg, you can ensure where people
leave your page and where to hold them exactly and where to add
more to hold them for longer.
3. Overlay Tool − It gives you an overlay report of the number of clicks
occurring on your website. You may be able to get more on it.
********** 4 **********
--- page 5 ---
4. Confetti − Confetti distinguishes clicks for you segmented by referral
sources, search terms, etc. Now, you know the origin of your clicks,
so you uncover the traffic sources. Put extra efforts there and you will
earn more traffic and revenue.
b   Draw and explain web traffic model. Differentiate between organic traffic   Dia5m
and paid traffic.   ,
explan
ation
5m
A typical Web page consists of a Hypertext document with links to other
objects that make up the whole page. An object is an entity stored on a server
as a file. There are two kinds of objects, a main object and an in-line
object. The file containing an HTML document is referred to as a main
object and the objects linked from the Hypertext document are referred to as
in-line objects The basic model of Web traffic is shown in Figure 1. A new
Web-request is immediately generated after expiration of the viewing period.
Organic traffic includes all visitors that come to your website through search
results you did not pay for. This kind of traffic is important for every website
and is directly influenced by the quality of your content and SEO measures.
Paid traffic, on the other hand, refers to visits that you paid for. If you place
ads on social media or Google and somebody accesses your website by
clicking on one of these ads, this is referred to as paid traffic.
a   Dia
7m,
Draw and explain architecture of information extraction system.
Q4   3m
explan
ation
********** 5 **********

[Text in pictures on this page, read by OCR]
J Web-request time —> } Viewing

In-line Object 1

Main Object

In-line Object 2

In-line Object 3

« HTTP ON » HTTP OFF >!

Figure 1: Overview of the basic model
--- page 6 ---
b   Explain following terms:   2m
working of indexing in SEO, crawler operation, use of robots.txt, URL   each
frontier, URL normalization.
use of robots.txt
Protocol for giving spiders (“robots”) limited access to a website
URL frontier
URLs that have been discovered, but are yet to be crawled
URL normalization
When a fetched document is parsed, some of the extracted links are relative
URLs
E.g., http://en.wikipedia.org/wiki/Main_Page has a relative link to
/wiki/Wikipedia:General_disclaimer which is the same as the absolute URL
http://en.wikipedia.org/wiki/Wikipedia:General_disclaimer
During parsing, must normalize (expand) such relative URLs
a   Explain page ranking algorithm.   [10]
• Algorithm
The PageRank algorithm outputs a probability distribution used to
represent the likelihood that a person randomly clicking on links will
arrive at any particular page.
Q5
• PageRank can be calculated for collections of documents of any size.
It is assumed in several research papers that the distribution is evenly
divided among all documents in the collection at the beginning of the
computational process. The PageRank computations require several
passes, called “iterations”, through the collection to adjust
approximate PageRank values to more closely reflect the theoretical
true value.
********** 6 **********

[Text in pictures on this page, read by OCR]
ay es
EY Asvisavie
[EERE Nice to have
[J can pass

Tokenization

Morphological and
Lexical Analysis

Syntactic Analysis

Domain Analysis

Figure VI.5. Architecture of a typical information extraction system.
--- page 7 ---
b   5m
Identify and explain (with example) applications of text categorizations ‘Text
each
indexing’ and ‘Document Sorting and Text Filtering’
The task of assigning keywords from a controlled vocabulary to text
documents is called text indexing. If the keywords are viewed as categories,
then text indexing is an instance of the general TC problem and can be
addressed by the automatic techniques described in this chapter.
Another common problem related but distinct from document indexing is
sorting the given collection of documents into several “bins.”
For instance, in a newspaper, the classified ads may need to be categorized
into “Personal,” “Car Sale,” “Real Estate,” and so on. Another example is e-
mail coming into an organization, which may need to be sorted into
categories such as “Complaints,” “Deals,” “Job applications,” and others.
a   Explain Linear regression and kNN for text categorization.   5m
each
1. Linear Regression
The most extensively used modelling technique is linear regression, which
assumes a linear connection between a dependent variable (Y) and an
independent variable (X).
It employs a regression line, also known as a best-fit line. The linear
connection is defined as Y = c+m*X + e, where ‘c’ denotes the intercept, ‘m’
denotes the slope of the line, and ‘e’ is the error term.
The linear regression model can be simple (with only one dependent and one
independent variable) or complex (with numerous dependent and independent
variables) (with one dependent variable and more than one independent
variable).
Q6
The most prominent example of an example-based classifier is kNN (k-
nearest neighbor). To decide whether a document d belongs to the category
c, kNN checks whether the k training documents most similar to d belong to
c. If the answer is positive for a sufficiently large proportion of them, a
positive decision is made; otherwise, the decision is negative. The distance-
weighted version of kNN is a variation that weighs the contribution of each
neighbor by its similarity to the test document.
********** 7 **********
--- page 8 ---
The kNNis one of the best-performing text classifiers to this day. It is robust
in the sense of not requiring the categories to be linearly separated. Its only
drawback is the relatively high computational cost of classification – that is,
for each test document, its similarity to all of the training documents must be
computed.
supervised learning classifier, which uses proximity to make classifications
or predictions about the grouping of an individual data point
b   Identify and explain Pre-Processing Techniques.   [10]
1. Tokenization
The approach most frequently found in text mining systems involves
breaking the text into sentences and words, which is called tokenization. The
main challenge in identifying sentence boundaries in the English language is
distinguishing between a period that signals the end of a sentence and a
period that is part of a previous token like Mr., Dr., and so on. It is common
for the tokenizer also to extract token features capitalization, the inclusion of
digits, punctuation, special characters, and so on
2. Part of Speech Tagging
POS tagging is the annotation of words with the appropriate POS tags based
on the context in which they appear. POS tags divide words into categories
based on the role they play in the sentence in which they appear. POS tags
provide information about the semantic content of a word. Nouns usually
denote “tangible and intangible things,” whereas prepositions express
relationships between “things.”
Most POS tag sets make use of the same basic categories. The most common
set of tags contains seven different tags (Article, Noun, Verb, Adjective,
Preposition, Number, and Proper Noun). Some systems contain a much more
elaborate set of tags. For example, the complete Brown Corpus tag set has no
less than 87 basic tags.
3 Syntactical Parsing
Syntactical parsing components perform a full syntactical analysis of
sentences
according to a certain grammar theory. The basic division is between the
constituency and dependency grammar.
4 Shallow Parsing
Instead of providing a complete analysis (a parse) of a whole sentence,
shallow parsers produce only parts that are easy and unambiguous. Typically,
small and simple noun and verb phrases are generated, whereas more
complex clauses are not formed. Similarly, most prominent dependencies
might be formed, but unclear and ambiguous ones are left unresolved.
a   Consider a small web graph of four pages (A, B, C, D).   2m
Page A links to B, C   ite.0,
B links to D   3m
Q7
C links to A, B, D   iter.1,
D links to C   3m
If PageRank is applied, which page will have the lowest rank after iteration 2.   iter.2,
********** 8 **********
--- page 9 ---
2m
rank
b   Write a short note on Trend Graph with example.   8m
explan
A trend graph is a very specialized representation that builds on the temporal   ation,
context graph as informed by the general approaches found in trend analysis. 2m
A trend graph can be obtained by partitioning the entire timespan covered by   examp
a time- or date stamped document collection, or both, into a series of   le.
consecutive time intervals.
These intervals can then be used to generate a corresponding sequence of
temporal context graphs. This sequence of temporal context graphs can be
leveraged to create combined or cumulative trend graphs that display the
evolution of concept relationships in a given context by means of visual cues
such as the character and relative weight of edges in the graph. For instance,
several classes of edges may be used to indicate various conditions:
New Edges: edges that did not exist in the previous graph.
Increased Edges: edges that have a relatively higher weight in relation to the
previous interval.
Decreased Edges: edges that have a relatively decreased weight than the
previous interval.
Stable Edges: edges that have about the same weight as the corresponding
edge in the previous interval.
********** 9 **********

[Text in pictures on this page, read by OCR]
Iteration 0 | Iteration 1 | Iteration 2 | PageRank

A 1/4 1/12 1.5/12
B 1/4 2.5/12 AV
Cc} 1/4 4.5/12 | 4.5/12

D 1/4 4/12 4/12
````
