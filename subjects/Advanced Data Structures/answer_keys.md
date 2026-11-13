# Advanced Data Structures: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper a9a6c4317d54

- Departments: Information Technology
- Programmes: BTech IT 7001, Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/BTech_IT_7001/Advanced Data Structures/ANS_Advanced Data Structures(702IT0E009)_2024-2025.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)
Year: III/Semester IX/Semester V(Exam Year: NA)
Subject: Advanced Data Structures
Date: NA   Time: NA to NA (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 1 pages.
2. Question No. 1 is compulsory.
3. Instruction....Out of the remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:
a. Define splaying and state its need in a splay tree.
 Splay tree is another variant of a binary search tree.
 Is an efficient implementation of a balanced binary search tree that
takes advantage of locality in the keys used in incoming lookup
requests.
 The recently accessed element is placed at the root of the tree.
 All the operations in splay tree are involved with a common
operation called Splaying.
⚫ Is the process of bringing the element under consideration to
the root position by performing suitable rotation operations.
 By splaying elements, we bring more frequently used elements closer
to the root of the tree so that any operation on those elements is
BL1; CO3   performed quickly.   [5]
 For example:
⚫ The insertion operation first inserts the new element using the
binary search tree insertion process, then the newly inserted
element is splayed so that it is placed at the root of the tree.
⚫ The search operation in a splay tree is nothing but searching
the element using binary search process and then splaying
that searched element so that it is placed at the root of the tree.
This makes the recently searched item to be accessible in O(1)
time if accessed again.
 In general, if a small number of elements are being heavily used, they
will tend to be found near the top of the tree and are thus found
quickly.
b. Describe how a Huffman Tree helps in data compression.
 Is a lossless data compression algorithm.
 A variable-length code is assigned to input different characters.
BL2; CO1   [5]
 The code length is related to how frequently characters are used.
 Most frequent characters have the smallest codes and longer codes
for least frequent characters.
********** 1 **********
--- page 2 ---
 Huffman codes are of variable-length and prefix-free (no code is
prefix of any other).
Steps:
1. Take a list of symbols and their probabilities.
2. Select two symbols with the lowest probabilities (if
multiple symbols have the same probability, select two
arbitrarily).
3. Create a binary tree out of these two symbols, labeling
one branch with a "1" and the other with a "0“ (i.e., the
left side should always be 1 and the right side should
always be 0, or the left side should always be 0 and the
right side should always be 1).
4. Add the probabilities of the two symbols to get the
probability of the new subtree.
5. Remove the symbols from the list and add the subtree to
the list.
6. Go back through   the   list and   take   the two
symbols/subtrees with the smallest probabilities and
combine those into a new subtree. Remove the original
symbols/subtrees from the list and add the new subtree to
the list.
7. Repeat until all of the elements are combined.
1 Marks – For an example that shows how reduction happens in terms
of number of bits required to encode the character.
c. Describe how the greedy approach is applied in solving the Activity
Selection Problem.
 Is an approach of selecting non-conflicting tasks based on start and
end time.
 Can be solved in O(N logN) time using a simple greedy approach.
 Problem Statement: “Given a set of n activities with their start and
finish times, we need to select maximum number of non-conflicting
BL2; CO1   [5]
activities that can be performed by a single person, given that the
person can handle only one activity at a time.”
 Applications:
⚫ Scheduling events in a room having multiple competing
events.
⚫ Scheduling and manufacturing multiple products having their
time of production on the same machine.
********** 2 **********
--- page 3 ---
⚫ Scheduling meetings in one room.
Steps:
⚫ Sort activity by finish time (let A1, A2, · · · , An denote sorted
sequence)
⚫ Pick first activity A1
⚫ Remove all activities with start time before finish time of A1
⚫ Recursively solve problem on remaining activities.
Activities 0, 1, 4 and 6 get selected, while others get rejected.
1 Marks – Justifying why Activity selection problem comes under the
basket of Greedy algorithms
d. State the objective and constraint of the 0–1 Knapsack Problem.
Problem Statement: Given the weights and profits of ‘N’ items, we are
asked to put these items in a knapsack that has a capacity ‘C’. The goal
is to get the maximum profit from the items in the knapsack. Each item
can only be selected once.
 Knapsack problem has the following two variants-
⚫ Fractional Knapsack Problem (i.e., items are divisible
here. We can even put the fraction of any item into the
knapsack if taking the complete item is not possible.
BL1; CO1   [5]
Solved by Greedy method)
⚫ 0/1 Knapsack Problem (i.e., items are indivisible. We
have to either take an item completely or leave it
completely)
Ex: Merry wants to carry some fruits in the knapsack to get maximum
profit. The items, weights and profits of the fruits and the capacity of the
knapsack are as shown below,
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
********** 3 **********
--- page 4 ---
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
Solution:
 Different combinations of fruits in the knapsack, such that their
total weight is not more than 5:
⚫ Apple + Orange (total weight 5) => 9 profit
⚫ Apple + Banana (total weight 3) => 7 profit
⚫ Orange + Banana (total weight 4) => 8 profit
⚫ Banana + Melon (total weight 5) => 10 profit
 As combination of Banana + Melon is the one with highest
profit, it’s the best choice.
a Demonstrate quadratic probing to handle a collision in hashing with
appropriate example
Following sections expected in the answer:
1. Disadvantage of linear probing
2. Characteristics of quadratic probing
3. Example illustrating the technique.
4. Pros and Cons
o Quadratic Probing eliminates primary clustering problem of
linear probing.
o Collision function is quadratic.
• The popular choice is f(i) = i2.
o   If the hash function evaluates to h and a search in cell h is
inconclusive, we try cells h + 12, h+22, … h + i2.
Q2   •   i.e., It examines cells 1,4,9 and so on away from the   [10]
BL3 ; CO2   original probe.
o Subsequent probe points are a quadratic number of positions
from the original probe point.
********** 4 **********
--- page 5 ---
o Problem:
• We may not be sure that we will probe all locations in
the table (i.e., there is no guarantee to find an empty cell
if table is more than half full.)
•   If the hash table size is not prime, this problem will be
much severe.
•   Quadratic probing appears to require * and % operations.
o Although quadratic probing eliminates primary clustering,
elements that hash to the same location will probe the same
alternative cells (secondary clustering).
o Double Hashing is one of the technique that eliminate
secondary clustering.
b For the graph shown below, use the shortest path algorithm and find the
nodes reachable from “E” with shortest distance.
BL4; CO1   [10]
********** 5 **********
--- page 6 ---
a Create an AVL Tree by performing the following operations and indicate
all the steps.
Insert: 30, 50, 40, 35, 45, 20
Delete: 35
Insert: 48, 47
Delete: 40
Q3
BL4; CO3   [10]
********** 6 **********
--- page 7 ---
b Apply Dynamic Programming to a problem and analyze how it reduces
redundant computations compared to Divide and Conquer.
Following sections expected in the answer:
1. Description of any problem statement.
2. Solution using Divide and conquer technique
3. Solution using Dynamic programming
4. Comparing their approach and justifying how Dynamic
BL3; CO1   [10]
programming is better
Example: Find the n-th Fibonacci number, where
F(n)=F(n−1)+F(n−2), with F(0)=0, F(1)=1
Divide and conquer:
********** 7 **********
--- page 8 ---
• The same values like fib(3), fib(2) are recomputed many
times.
•   Total recursive calls grow exponentially → O(2ⁿ) time.
Problem: Massive redundancy and recomputation.
Dynamic Programming:
Dynamic Programming improves upon Divide and Conquer by:
• Storing subproblem results (overlapping subproblems are
solved once).
• Exploiting optimal substructure, meaning the optimal solution
of the whole problem can be built from optimal solutions of
smaller ones.
Aspect   Divide & conquer   Dynamic
Programming
Approach   Solves every subproblem   Solves each
repeatedly   subproblem once
Time Complexity   Exponential — O(2ⁿ)   Linear — O(n)
Space Complexity O(n) (stack calls)   O(n) (table)
Redundant   Many (e.g., fib(3)   None — stored and
Computations   recomputed multiple   reused
times)
Technique Type   Top-down recursion   Bottom-up
Q4   a   In the string “PQRSTUVSTUQR”, search for the presence of the
[10]
BL3; CO4   substring “STUVST” and find its index using Boyer Moore Horspool
********** 8 **********
--- page 9 ---
Algorithm.
b Describe using an example why a self-balanced tree is more efficient
for search and insertion than a BST.
Following sections expected in the answer:
1. Problems with search and insert operation in a BST with
appropriate examples
2. For the same example, justification how self-balanced trees are
better
If the input to binary search tree comes in a sorted (ascending or
descending) manner, the tree formed will look like this,
BL2; CO3   [10]
********** 9 **********
--- page 10 ---
Ex: With 3 keys - 30,20,10 we can have 3!=6 different BST’s created
of min/max height.
a   Illustrate the working of the Brute Force Pattern Matching algorithm
with an example and discuss when it is efficient or inefficient.
Following sections expected in the answer:
1. Explanation of Brute force technique.
2. With appropriate example, discuss its pros and cons in relation
with time and space complexity
 These algorithms are also referred to as String Searching
Algorithms.
 These algorithms are useful in the case of searching a string
within another string.
 Uses of pattern matching include outputting the locations (if
any) of a pattern within a token sequence, to output some
Q5   component of the matched pattern, and to substitute the
[10]
BL3; CO4   matching pattern with some other token sequence (i.e., search
and replace).
 Ex:
1. Input: txt[] = "THIS IS A TEST TEXT"
pat[] = "TEST"
Output: Pattern found at index 10
2. Input: txt[] = "AABAACAADAABAABA"
pat[] = "AABA"
Output: Pattern found at index 0
Pattern found at index 9
Pattern found at index 12
 Also called as Naive String-Matching Algorithm.
 Slide the pattern over text one by one and check for a match. If
a match is found, then slides by 1 again to check for subsequent
matches.
 Ex:
********** 10 **********
--- page 11 ---
Performance:
 Best case is O(n), it occurs when the first character of the
pattern is not present in text at all.
Ex: txt[] = "AABCCAADDEE";
pat[] = "FAA“
 Worst case O(n*m), occurs when,
⚫ When all characters of the text and pattern are same.
Ex: txt[] = "AAAAAAAAAAAAAAAAAA";
pat[] = "AAAAA";
⚫ When only the last character is different
Ex: txt[] = "AAAAAAAAAAAAAAAAA";
pat[] = "AAAAB";
Pros:
⚫ Doesn’t require pre-processing of the text(Most of the
algorithms for string matching need to build an index of
the text in order to search quickly).
⚫ Doesn’t require additional space
⚫ Can be quite effective for short texts and patterns
Cons:
⚫ Can be ineffective, if we search the text more than once.
⚫ It’s comparatively slower
b What are some instances of graph data structures being used in
different industries?
Following sections expected in the answer:
1. Good elaborate real time examples showcasing the usage of
Graph data structure.
 GPS systems and Google Maps use graphs to find the shortest path
from one destination to another.
⚫ Uber, Ola, Lyft uses a graph to find the shortest and cheapest
BL1; CO3   [10]
path for a car from one city to another.
⚫ Google Maps, Apple Maps, Waze use graphs to treat all cities
and places as nodes and routes between them as edges.
 The Google Search algorithm uses graphs to determine the
relevance of search results.
⚫ Web graph describes a directed graph between pages of the
WWW. Each page is a vertex, and the hyperlinks are edges.
The Google Page Ranking Algorithm makes use of this
structure.
 Social Networks use graphs to represent connections between
users.
********** 11 **********
--- page 12 ---
⚫ Social media like Facebook, LinkedIn uses graphs that store
users, groups, check-ins, likes and more as nodes.
 Airline Network use graph theory to manage flight networks as
they want to connect countless cities in the most efficient way,
moving the most passengers with the fewest possible trips (used in
the similar way to connect communication traffic)
a Simulate topological sort technique on the following graph using BFS.
P → Q & R (Indicating, Node P connected with node Q and R)
Q → S & T
R → S & T
Q6   S → U
BL3; CO1   T → U   [10]
Following sections expected in the answer:
1. One paragraph explanation of the technique.
2. Step by step indication of queue and list content as per BFS
implementation of Topological sorting.
********** 12 **********
--- page 13 ---
b A hash table of size 11 uses double hashing. The first hash function is
h1(k)=k mod 11, and the second hash function is h2(k)=2+(k mod 7).
Insert the following keys into the hash table: 20, 50, 53, 75, 100 Show
the hash table after all insertions.
Step 1: Insert 20
• h1(20)=20 mod 11=9h_1(20) = 20 \bmod 11 = 9h1
(20)=20mod11=9
• h2(20)=2+(20 mod 7)=2+6=8h_2(20) = 2 + (20 \bmod 7) = 2 + 6
BL4; CO2   [10]
= 8h2(20)=2+(20mod7)=2+6=8
•   Position 9 is empty → place 20 there.
Slot 9 ← 20
Step 2: Insert 50
• h1(50)=50 mod 11=6h_1(50) = 50 \bmod 11 = 6h1
(50)=50mod11=6
• h2(50)=2+(50 mod 7)=2+1=3h_2(50) = 2 + (50 \bmod 7) = 2 + 1
= 3h2(50)=2+(50mod7)=2+1=3
•   Position 6 is empty → place 50 there.
********** 13 **********
--- page 14 ---
Slot 6 ← 50
Step 3: Insert 53
• h1(53)=53 mod 11=9h_1(53) = 53 \bmod 11 = 9h1
(53)=53mod11=9
• h2(53)=2+(53 mod 7)=2+4=6h_2(53) = 2 + (53 \bmod 7) = 2 + 4
= 6h2(53)=2+(53mod7)=2+4=6
•   Position 9 occupied (20) → collision.
Use double hashing:
i   Calculation   Index   Result
0 (9 + 0×6) mod 11 9   occupied
1 (9 + 1×6) mod 11 4   empty
Slot 4 ← 53
Step 4: Insert 75
• h1(75)=75 mod 11=9h_1(75) = 75 \bmod 11 = 9h1
(75)=75mod11=9
• h2(75)=2+(75 mod 7)=2+5=7h_2(75) = 2 + (75 \bmod 7) = 2 + 5
= 7h2(75)=2+(75mod7)=2+5=7
•   Position 9 occupied → probe further:
i   Calculation   Index   Result
0 (9 + 0×7) mod 11 9   occupied
1 (9 + 1×7) mod 11 5   empty
Slot 5 ← 75
Step 5: Insert 100
• h1(100)=100 mod 11=1h_1(100) = 100 \bmod 11 = 1h1
(100)=100mod11=1
• h2(100)=2+(100 mod 7)=2+2=4h_2(100) = 2 + (100 \bmod 7) =
2 + 2 = 4h2(100)=2+(100mod7)=2+2=4
•   Position 1 is empty → Slot 1 ← 100
Final Table:
Index Key
0   —
1   100
2   —
3   —
4   53
5   75
6   50
7   —
8   —
9   20
10 —
Short Notes on:
Q7   [5*4=20]
a. Minimum Spanning trees
********** 14 **********
--- page 15 ---
BL1; CO1,
CO2, CO4,   Following sections expected in the answer:
CO1   1. What is MST
2. Ways of implementing it
3. Applications
• In a weighted graph, a minimum spanning tree is a spanning
tree that has minimum weight than all other spanning trees of
the same graph.
• In real-world situations, this weight can be measured as
distance, congestion, traffic load or any arbitrary value denoted
to the edges.
• Two popular MST algorithms (in category of Greedy
Algorithms),
o Prim’s
o Kruskal’s
Applications:
 Networking:
⚫ To design efficient network topologies, ensuring all
nodes (computers, routers, etc.) are connected without
creating loops, which could cause broadcast storms.
⚫ To design cost-effective telephone or fiber-optic
networks, connecting all nodes (e.g., cities or exchanges)
with minimal cable length or cost.
 Transportation and Logistics:
⚫ To design road or railway systems that connect multiple
locations (e.g., cities, warehouses) with minimal
construction costs or travel distance.
⚫ To optimize delivery routes for vehicles, ensuring all
destinations are covered with minimal total distance.
 Power Distribution Networks:
⚫ To design efficient power grids, ensuring all substations
or consumers are connected with minimal infrastructure
costs.
b. Desirable properties of hash function
Following sections expected in the answer:
1. Desirable properties of hash function
2. Example of 2 or 3 hash functions justifying the previous points
The hash function:
 If it takes too long for a hash function to compute hash values,
the procedure is not much use. So, they must be simple and quick
to compute.
 Must distribute the keys evenly among the cells.
 Less collisions : Collisions occur when pairs of elements are
mapped to the same hash value. These should be avoided
 One-way: Once a hash value has been generated, it must
be impossible to convert it back into the original data.
 The hash function is a perfect hash function when it uses all the
input data.
********** 15 **********
--- page 16 ---
c. Suffix Tries
Following sections expected in the answer:
1. What are suffix trees
2. Their characteristics with example
3. How are they built
4. Their applications.
 Is a compressed trie for all the suffixes of a text.
 Are are a space-efficient data structure to store a string that
allows many kinds of queries to be answered quickly
 For a text X of size n from an alphabet of size d , it stores all the
n(n-1)/2 suffixes of X in O(n) space.
 Supports arbitrary pattern matching and prefix matching queries
in O(dm) time, where m is the length of the pattern.
 Can be constructed in O(dn) time.
 SufTrie(s) = suffix trie representing string s.
 Edges of the suffix trie are labeled with letters from the
alphabet ∑ (say {A,C,G,T}).
 Every path from the root to a solid node represents a suffix of s.
 Every suffix of s is represented by some path from the root to a
solid node.
d. Dictionary as a data structure
Following sections expected in the answer:
1. What is a dictionary
2. Its characteristics with example
3. Its applications
 A dictionary is a general-purpose data structure for storing a
group of objects extremely useful and widely used in the
programming.
 A dictionary has a set of keys, and each key has a single
associated value.
 When presented with a key the dictionary will   return the
associated value.
********** 16 **********
--- page 17 ---
 A dictionary is also called a hash, a map, a hashmap in different
programming languages.
 The elements of the dictionary are represented by pairs (key,
value), where the key is used for searching.
 The idea of the dictionaries is to provide us with more
flexibility regarding the set of the keys.
 The set of keys usually is a randomly chosen set of values like
real numbers or strings with the only restriction that we can
distinguish one key from the other.
e. Ex: A token (key) given by the security personnel in a shopping
mall, when you want to keep your bags (value) with him. The
bag is returned back when you give the token back to him on
your return.
f. Keys in a dictionary must be unique an attempt to create a
duplicate key will typically overwrite the existing value for that
key.
g. The keys in a dictionary must be simple types (such as integers
or strings) while the values can be of any type.
h. Dictionary represents a mapping from keys to values.
********** 17 **********
````
