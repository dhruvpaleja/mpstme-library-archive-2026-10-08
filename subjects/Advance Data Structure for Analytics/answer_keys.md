# Advance Data Structure for Analytics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper f3dc045840b1

- Departments: Data Science
- Programmes: BACHELOR OF TECHNOLOGY (DATA SCIENCE)SIX YEARS INTEGRATED PROGRAM - 7038
- Source: `00_Original_Downloads/2025/76555__Semester X.zip :: Final-Exam/BACHELOR OF TECHNOLOGY (DATA SCIENCE)SIX YEARS INTEGRATED PROGRAM - 7038/Advance Data Structure for Analytics/ANS_Final-Exam_Advance Data Structure for Analytics(702DB0C026)_Semester X_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: mixed (20 pages), mean OCR confidence 78.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
Implement the single linked list with the following functionalities:
CO-1,2;   i. Insertion and Deletion
SO- 1;   a.   ii. Display   [5]
BL- 3   (Practical)
Note: Can be implemented in C++/Java/Python language.
********** 1 **********
--- page 2 ---
Explain what a KD-tree is and how it differs from a standard BST, highlighting its
advantages in multidimensional data.
A KD-tree (K-Dimensional Tree) is a space-partitioning data structure used
to organize points in a k-dimensional space. It is a type of binary tree in
which each node represents a point in k-dimensional space, and the tree
recursively partitions the space into smaller regions. Unlike a simple Binary
Search Tree, which stores one-dimensional data, a KD-tree stores
multidimensional data such as points in 2D, 3D, or higher dimensions.
Differences Between KD-Tree and BST
CO-1,5;
b.   Differences Between KD-Tree and BST: The KD-tree and BST are both   [5]
SO-1;
binary tree structures, they are designed for different purposes and handle
BL-2   data differently.
Feature   KD-Tree   Binary Search Tree (BST)
Data Type Multidimensional data (points in k-   One-dimensional data
dimensions)
Splitting   Splits data based on different   Splits based on single key comparison
Criteria   dimensions alternately
Structure   Each level uses a different   All levels use the same key comparison
dimension
********** 2 **********
--- page 3 ---
Example Data   (x, y), (x, y, z) coordinates   Numbers or strings
Application Spatial searching, nearest neighbor Sorting, dictionary operations
s   queries
Range   Efficient in multi-dimensional range   Efficient only for one-dimensional range
Queries   queries   queries
Search   Divides geometric space into   Divides ordered key values
Space   regions
Differentiate between best-case, average-case, and worst-case time complexity.
Best-case Time Complexity:
Minimum time an algorithm takes to complete.
Example: Quick Sort on a perfectly balanced array.
Notation: O(n)
(2 marks)
CO-1;   Average-case Time Complexity:
SO-1,2;   c.   [5]
BL-4   Expected time over all possible inputs of a given size.
Example: Quick Sort on a random array → O(n log n)
(2 marks)
Worst-case Time Complexity:
Maximum time an algorithm takes on any input of size n.
Example: Quick Sort on a sorted array with last element as pivot → O(n²)
(1 marks)
Given two arrays:
A: random order
B: already sorted
Explain how Quick Sort behaves on both when the last element is always
chosen as pivot.
CO-4;
SO-1;   d.   [5]
BL-2
********** 3 **********
--- page 4 ---
In the Dynamic Connectivity problem using Disjoint Sets, discuss the
Quick-Find and Quick-Union approaches for managing relationships
between elements. State their limitations in terms of worst-case time
complexity.
Dynamic connectivity is a problem where we need to determine whether two
elements are in the same connected component and efficiently merge
components when a new connection is added. Two fundamental approaches
to solving this problem are Quick Find and Quick Union.
Quick Find Approach: Quick Find is an approach in which each element in
the data structure maintains an array index as its identifier. When performing
the union operation, all elements in the set of one element are updated to
match the identifier of the other set.
Algorithm:
1. Initialize an array id[] of size N, where id[i] = i.
Q2 a   2. find(p): Returns id[p].
CO-1,5;   [10]
SO-1,2;   3. union(p, q): Change id[i] to id[q] for all i where id[i] = id[p].
BL-2,4
Time Complexity: The time complexity is mentioned below.
-   find(p): O(1) (constant time lookup).
-   union(p, q): O(N) (modifies all elements in the set).
Quick Union Approach: Quick Union is a lazy approach where elements
maintain a pointer to their parent. The root of a tree represents the set.
Algorithm:
Initialize an array id[], where each element is its own parent
1. find(p): Follow parent pointers until reaching the root.
2. union(p, q): Attach the root of one tree to the root of another.
Time Complexity: The time complexity is mentioned below.
-   find(p): O(N) in the worst case.
-   union(p, q): O(N) in the worst case.
Comparison of Quick Find and Quick Union approaches
********** 4 **********
--- page 5 ---
Quick Find is preferable when we need fast find operations and are willing
to pay a higher cost for union. Quick Union is preferable when union
operations are frequent, but it should be used with optimizations like
Weighted Quick Union and Path Compression to achieve near-constant
time complexity.
Marks Distribution: Quick Find and Quick Union 6 Marks + Time Complexity
Analysis 4 Marks
Define a Red-Black Tree and list all five essential properties that maintain
its balance. Construct an initially empty Red Black Tree by inserting keys
15,13,12,16,19,23,5,8 and show the result of step-by-step insertion. Clearly
label node colors and indicate where rotations or recoloring occurred.
A Red-Black Tree (RBT) is a self-balancing Binary Search Tree where each
Q2 b   node has an extra bit for color (Red or Black), ensuring the tree remains
CO-5;   approximately balanced after insertions and deletions.   [10]
SO-1;
BL-6   Five Essential Properties
1. Every node is either Red or Black
2. The root is always Black
3. No two consecutive Red nodes (no Red parent with Red child)
4. Every path from a node to its NULL descendants has the same
number of Black nodes
5. All NULL leaves are Black
********** 5 **********
--- page 6 ---
3. Step-by-Step Insertion

Insert 15

= First mode — becomes root + colored Black

1s(8)

Insert 13

. Insert as left child of 15
7 Parent is Back + no violation

15(8)
f
1a(R)

Insert 12

= Insert as Jett child of 13 — Red-Red violation
« Case: Left-Left — Right Rotation at 15 + recoloring

1308)
# \
12(R) 15(R)

Insert 16

. Insert as night child of 15
= Parent (15) is Red. Uncle (12) is Rad —- Recoloring

13(8)
f ‘
12(8) 15(B)

1e(R)

Insert 19

= Insert as. right child of 16 — Red-Red violation
« Case: Right-Right — Left Rotation at 15 + recoloring

13(8)
i “
12(8) 26(B)
!
1s(R} 1S(R)

%

FIC 6 I HF
--- page 7 ---
Implement a static queue using an array and a dynamic queue using a linked
list. Perform enqueue and dequeue operations, display the queue after each
operation. (practical)
Can be implemented in C++/Java/Python language
1. Static Queue (Array-Based)
Q3 a   Class StaticQueue:
CO-2,4;   Define:   [10]
SO-1;
BL-3   - `capacity`: Maximum queue size
- `front`, `rear`: Pointers for queue operations
- `size`: Tracks current number of elements
- `array`: Stores queue elements
Function ENQUEUE(value):
- If queue is full, print "Queue is full".
********** 7 **********
--- page 8 ---
- Increment `rear` circularly.
- Insert `value` at `rear` position.
- Increase `size`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next element.
- Decrease `size`.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
2. Dynamic Queue (Linked List-Based)
Class Node:
- `data`: Holds value
- `next`: Pointer to next node
Class DynamicQueue:
Define:
- `front`, `rear`: Pointers to track queue
Function ENQUEUE(value):
- Create a new node with `value`.
- If queue is empty, set both `front` and `rear` to new node.
- Else, attach new node to `rear.next` and update `rear`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next node.
- If `front` becomes null, update `rear` to null.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
Marks Distribution: Static Queue 5 Marks + Dynamic Queue 5 Marks
Q3 b
Insert the keys H, C, R, A, E, S, X into a Binary Search Tree (BST) in the given
CO-3;   [10]
SO-1;   order and draw the tree. Determine the minimum and maximum keys. Perform
BL-2
********** 8 **********
--- page 9 ---
deleteMin() and deleteMax() operations and draw the final tree after both deletions.
Also, write pseudocode for deleteMin() and deleteMax() in a BST.
Q4 a   Implement a hash table using separate chaining. Demonstrate how to
[10]
CO-5;   perform insertion, search, and deletion operations with a sample dataset.
SO-1;
********** 9 **********
--- page 10 ---
BL-4
A hash table is a data structure that stores key-value pairs. It uses a hash
function to compute an index for storing values efficiently. When multiple
keys hash to the same index, we use separate chaining, where each bucket
contains a linked list of entries. Separate chaining is a collision resolution
technique used in hash tables. When two or more keys map to the same
index (collision), a linked list (or another data structure like a balanced tree)
is maintained at that index to store all colliding elements. Each bucket of
the hash table stores a reference to the head of a linked list containing all
elements that hash to that index. Collisions are unavoidable in hash tables
due to a limited number of slots and potentially unlimited input keys.
Separate chaining helps in handling these collisions efficiently while
maintaining fast insert, delete, and search operations. A simple hash
function can be designed as
Hash Index=Key mod Table Size
For example, if the table size is 10, and the key is 25:25 mod 10=5. So,
the key 25 will be stored in bucket index 5.
1. Implementation of Insertion(2 Marks): The insertion steps are
mentioned as below.
- Compute the hash index using the hash function.
-   If the index is empty, insert the key.
-   If a collision occurs, insert the key at the end of the linked list at
that index.
Example: Inserting 15, 25, 35 in a hash table of size 10:
- 15 mod 10=5, stored at index 5.
- 25 mod 10=5, stored at index 5 (collision, linked list used).
- 35 mod 10=5, stored at index 5.
2. Implementation of Search (2 Marks): Searching steps are
mentioned below.
- Compute the hash index.
-   Traverse the linked list at that index.
-   If the key is found, return success; otherwise, return failure.
Example: Searching for 25, then Compute
- 25 mod 10=5.
-   Traverse the linked list at index 5. Found 25 in the list.
3. Implementation of Deletion (2 Marks): The steps are listed below.
- Compute the hash index.
-   Locate the key in the linked list.
-   Delete the key by adjusting the links.
Example: Deleting 25, then compute as
- 25 mod 10=5.
-   Traverse the linked list at index 5. Remove 25 and adjust links.
Compare the time complexity of search, insertion, and deletion operations
in Red-Black trees and B-trees.
Q4 b   Illustrate the structure and properties of a B-Tree. Demonstrate how
CO-5;   insertion and node splitting maintain balance and ensure efficient disk [10]
SO-1;
BL-3   access.
********** 10 **********
--- page 11 ---
Consider a weighted undirected graph with vertices {A, B, C, D, E, F} and
edges :(A–B, 3), (A–C, 1), (B–C, 2), (B–D, 4), (C–D, 5), (C–E, 6), (D–E,
Q5 a
7), (D–F, 8), (E–F, 9).
CO-1,5;   [10]
SO-1;   Using Kruskal’s Algorithm and Union–Find, construct the Minimum
BL-5
Spanning Tree. Show the edges selected at each step and compute the total
weight of the MST.
********** 11 **********
--- page 12 ---
Solution with Union-Find (10 Marks)

1. Sort Edges by Weight (2 Marks)

Exige Weight
AC 1
ac 2
4-8 a
8D 4
co 5
ct &
DHE 7
DF a

2, Initialize Union—Find (MakeSet) (1 Mark)

Each vertex is its own parent:

Parent: A BC DE F
AB COEF

3. Kruskal with Union—Find Operations (5 Marks)

Step 1: A-C (1)
= FindA)=A, Find(C)}=C — different
» UnioniA.d

Parent: A BA DE F

w Selected

Step 2: BC (2)
= Find(B)=B, Find(Q)=A — different
«   Union(B,A)

Parent: A A A DE F

wf Selected

FRR ICR] DA KH
--- page 13 ---
What is a collision in hashing? Explain two common methods to handle
Q5 b
collisions. Compare separate chaining and open addressing. When would
CO-5;   [10]
SO-1;   you use one over the other?
BL-2
********** 13 **********
--- page 14 ---
Role of Hash Table in Symbol Table Applications:
A hash table provides efficient storage and retrieval of key-value pairs.
In symbol tables, it is used to store identifiers (like variable names) along
with associated information (type, value, memory location).
Hash tables allow average-case O(1) search, insert, and delete, making them
ideal for applications that require fast lookup.
Comparison: Sets vs Dictionaries:
Aspect   Sets   Dictionaries
Purpose   Store unique elements   Store key-value pairs
Key Use   Only the element itself   Key maps to a value
Collision Handling Same as hash table (e.g., chaining, linear probing)
Same as hash table
Advantages   Fast membership checking, prevents duplicates   Fast
retrieval of associated values, flexible storage
Limitations   Cannot store associated data Slightly higher memory usage
due to storing values along with keys
Given a set of 1000 words, design a hash table for efficient lookup
operations. Justify your choice of hash function and collision resolution
strategy.
Given the recurrence
T(n)=T(n/2)+T(n/4)+cn
Q6 a
Using the recursion tree method:
CO-1;   [5+5]
SO-1,2;   • Draw the recursion tree
BL-2
• Show the cost at each level and derive a general expression
• Determine the total cost and overall time complexity
********** 14 **********
--- page 15 ---
Q6 b   Explain the role of sift-up and sift-down operations in maintaining the heap
[10]
CO-2;   property in a binary heap. Also write the algorithm for both operations.
SO-1;
********** 15 **********
--- page 16 ---
BL-2,3 1. Role of Sift-Up and Sift-Down (5 Marks)

A binary heap is 2 complete binary tree that satisfies the heap property:

© Max-Heap: Parent > Children
© Min-Heap: Parent < Children

Sift-Up (Heapify-Up)

Role:

e Used after insertion

© Restores heap property by moving the element upward
Working:

* Compare node with its parent

¢ If heap property is violated — swap with parent
© Repeat until property is satisfied or root is reached

Sift-Down (Heapify-Down)

Role:

* Used after deletion (removing root)

© Restores heap property by moving the element downward
Working:

* Compare node with its children

© Swap with larger child (max-heap) or smaller child (min-heap)
© Continue until heap property is restored

FRR ICR 7 6 AC OH
--- page 17 ---
Explain the Merge Sort algorithm. Apply Merge Sort to the array
[38, 27, 43, 3, 9, 82, 10] and show the intermediate steps during the division
and merging process.
Step 1: Division Phase (5 marks)
Q7 a   Given array:
CO-4;   [38, 27, 43, 3, 9, 82, 10]   [10]
SO-1;
BL-2
Divide recursively:
[38, 27, 43, 3, 9, 82, 10]
→[38,27,43][3,9,82,10]
→[38][27,43][3,9][82,10]
→[38][27][43][3][9][82][10]
********** 17 **********
--- page 18 ---
All subarrays reduced to single elements
Step 2: Merging Phase (5 marks)
Merge step-by-step:
• Merge [27] and [43] →
[27, 43]
• Merge [38] and [27,43] →
[27, 38, 43]
• Merge [3] and [9] →
[3, 9]
• Merge [82] and [10] →
[10, 82]
• Merge [3,9] and [10,82] →
[3, 9, 10, 82]
•   Final merge:
[27,38,43]  &  [3,9,10,82]
⇒[3,9,10,27,38,43,82]
Final Sorted Array:
[3, 9, 10, 27, 38, 43, 82]
(i) Explain floor and ceiling operations in a BST. State the cases for
Q7 b   computing floor(key) and write the recursive logic.
CO-2,3,5;   (ii) Discuss how sparse vectors can be efficiently represented using   [5+5]
SO-1;
BL-3,2   hash tables and explain their significance.
(i)   5 marks
********** 18 **********
--- page 19 ---
(i) Floor and Ceiling in a BST

Definition

« Floor(key): Largest value = key
* Ceiling(key): Smallest value = key

Cases for Floor(key)
Ata node with value x:
1. lf x == key - floor = x
2. If x > key — search in left subtree
3. lf x < key —
* x can bea candidate

* search in right subtree for a closer value

Recursive Logic (Floor)

floor(root, key):
if root == NULL:
return NULL

if root.data == key:
return root.data

if root.data > key:
return floor(root.left, key)

val = floor(root.right, key)
if val != NULL:
return val

else:
return root.data

(ii) 5 marks

FRR ICR 7 QI OR
--- page 20 ---
(ii) Sparse Vectors using Hash Tables

Representation

* Store only non-zero elements
* Use index as key and value as data in a hash table

Example:
Vector [@, @, 5, @, @, 3] + {2:5, 5:3}

Advantages / Significance

® Space efficient - avoids storing zeros
* Faster operations — direct access using index
* Efficient for:
* Dot product computation
* Machine learning / data science applications

FRI ICR DO) A RH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper aafc557da9aa

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: mixed (20 pages), mean OCR confidence 78.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
Implement the single linked list with the following functionalities:
CO-1,2;   i. Insertion and Deletion
SO- 1;   a.   ii. Display   [5]
BL- 3   (Practical)
Note: Can be implemented in C++/Java/Python language.
********** 1 **********
--- page 2 ---
Explain what a KD-tree is and how it differs from a standard BST, highlighting its
advantages in multidimensional data.
A KD-tree (K-Dimensional Tree) is a space-partitioning data structure used
to organize points in a k-dimensional space. It is a type of binary tree in
which each node represents a point in k-dimensional space, and the tree
recursively partitions the space into smaller regions. Unlike a simple Binary
Search Tree, which stores one-dimensional data, a KD-tree stores
multidimensional data such as points in 2D, 3D, or higher dimensions.
Differences Between KD-Tree and BST
CO-1,5;
b.   Differences Between KD-Tree and BST: The KD-tree and BST are both   [5]
SO-1;
binary tree structures, they are designed for different purposes and handle
BL-2   data differently.
Feature   KD-Tree   Binary Search Tree (BST)
Data Type Multidimensional data (points in k-   One-dimensional data
dimensions)
Splitting   Splits data based on different   Splits based on single key comparison
Criteria   dimensions alternately
Structure   Each level uses a different   All levels use the same key comparison
dimension
********** 2 **********
--- page 3 ---
Example Data   (x, y), (x, y, z) coordinates   Numbers or strings
Application Spatial searching, nearest neighbor Sorting, dictionary operations
s   queries
Range   Efficient in multi-dimensional range   Efficient only for one-dimensional range
Queries   queries   queries
Search   Divides geometric space into   Divides ordered key values
Space   regions
Differentiate between best-case, average-case, and worst-case time complexity.
Best-case Time Complexity:
Minimum time an algorithm takes to complete.
Example: Quick Sort on a perfectly balanced array.
Notation: O(n)
(2 marks)
CO-1;   Average-case Time Complexity:
SO-1,2;   c.   [5]
BL-4   Expected time over all possible inputs of a given size.
Example: Quick Sort on a random array → O(n log n)
(2 marks)
Worst-case Time Complexity:
Maximum time an algorithm takes on any input of size n.
Example: Quick Sort on a sorted array with last element as pivot → O(n²)
(1 marks)
Given two arrays:
A: random order
B: already sorted
Explain how Quick Sort behaves on both when the last element is always
chosen as pivot.
CO-4;
SO-1;   d.   [5]
BL-2
********** 3 **********
--- page 4 ---
In the Dynamic Connectivity problem using Disjoint Sets, discuss the
Quick-Find and Quick-Union approaches for managing relationships
between elements. State their limitations in terms of worst-case time
complexity.
Dynamic connectivity is a problem where we need to determine whether two
elements are in the same connected component and efficiently merge
components when a new connection is added. Two fundamental approaches
to solving this problem are Quick Find and Quick Union.
Quick Find Approach: Quick Find is an approach in which each element in
the data structure maintains an array index as its identifier. When performing
the union operation, all elements in the set of one element are updated to
match the identifier of the other set.
Algorithm:
1. Initialize an array id[] of size N, where id[i] = i.
Q2 a   2. find(p): Returns id[p].
CO-1,5;   [10]
SO-1,2;   3. union(p, q): Change id[i] to id[q] for all i where id[i] = id[p].
BL-2,4
Time Complexity: The time complexity is mentioned below.
-   find(p): O(1) (constant time lookup).
-   union(p, q): O(N) (modifies all elements in the set).
Quick Union Approach: Quick Union is a lazy approach where elements
maintain a pointer to their parent. The root of a tree represents the set.
Algorithm:
Initialize an array id[], where each element is its own parent
1. find(p): Follow parent pointers until reaching the root.
2. union(p, q): Attach the root of one tree to the root of another.
Time Complexity: The time complexity is mentioned below.
-   find(p): O(N) in the worst case.
-   union(p, q): O(N) in the worst case.
Comparison of Quick Find and Quick Union approaches
********** 4 **********
--- page 5 ---
Quick Find is preferable when we need fast find operations and are willing
to pay a higher cost for union. Quick Union is preferable when union
operations are frequent, but it should be used with optimizations like
Weighted Quick Union and Path Compression to achieve near-constant
time complexity.
Marks Distribution: Quick Find and Quick Union 6 Marks + Time Complexity
Analysis 4 Marks
Define a Red-Black Tree and list all five essential properties that maintain
its balance. Construct an initially empty Red Black Tree by inserting keys
15,13,12,16,19,23,5,8 and show the result of step-by-step insertion. Clearly
label node colors and indicate where rotations or recoloring occurred.
A Red-Black Tree (RBT) is a self-balancing Binary Search Tree where each
Q2 b   node has an extra bit for color (Red or Black), ensuring the tree remains
CO-5;   approximately balanced after insertions and deletions.   [10]
SO-1;
BL-6   Five Essential Properties
1. Every node is either Red or Black
2. The root is always Black
3. No two consecutive Red nodes (no Red parent with Red child)
4. Every path from a node to its NULL descendants has the same
number of Black nodes
5. All NULL leaves are Black
********** 5 **********
--- page 6 ---
3. Step-by-Step Insertion

Insert 15

= First mode — becomes root + colored Black

1s(8)

Insert 13

. Insert as left child of 15
7 Parent is Back + no violation

15(8)
f
1a(R)

Insert 12

= Insert as Jett child of 13 — Red-Red violation
« Case: Left-Left — Right Rotation at 15 + recoloring

1308)
# \
12(R) 15(R)

Insert 16

. Insert as night child of 15
= Parent (15) is Red. Uncle (12) is Rad —- Recoloring

13(8)
f ‘
12(8) 15(B)

1e(R)

Insert 19

= Insert as. right child of 16 — Red-Red violation
« Case: Right-Right — Left Rotation at 15 + recoloring

13(8)
i “
12(8) 26(B)
!
1s(R} 1S(R)

%

FIC 6 I HF
--- page 7 ---
Implement a static queue using an array and a dynamic queue using a linked
list. Perform enqueue and dequeue operations, display the queue after each
operation. (practical)
Can be implemented in C++/Java/Python language
1. Static Queue (Array-Based)
Q3 a   Class StaticQueue:
CO-2,4;   Define:   [10]
SO-1;
BL-3   - `capacity`: Maximum queue size
- `front`, `rear`: Pointers for queue operations
- `size`: Tracks current number of elements
- `array`: Stores queue elements
Function ENQUEUE(value):
- If queue is full, print "Queue is full".
********** 7 **********
--- page 8 ---
- Increment `rear` circularly.
- Insert `value` at `rear` position.
- Increase `size`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next element.
- Decrease `size`.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
2. Dynamic Queue (Linked List-Based)
Class Node:
- `data`: Holds value
- `next`: Pointer to next node
Class DynamicQueue:
Define:
- `front`, `rear`: Pointers to track queue
Function ENQUEUE(value):
- Create a new node with `value`.
- If queue is empty, set both `front` and `rear` to new node.
- Else, attach new node to `rear.next` and update `rear`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next node.
- If `front` becomes null, update `rear` to null.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
Marks Distribution: Static Queue 5 Marks + Dynamic Queue 5 Marks
Q3 b
Insert the keys H, C, R, A, E, S, X into a Binary Search Tree (BST) in the given
CO-3;   [10]
SO-1;   order and draw the tree. Determine the minimum and maximum keys. Perform
BL-2
********** 8 **********
--- page 9 ---
deleteMin() and deleteMax() operations and draw the final tree after both deletions.
Also, write pseudocode for deleteMin() and deleteMax() in a BST.
Q4 a   Implement a hash table using separate chaining. Demonstrate how to
[10]
CO-5;   perform insertion, search, and deletion operations with a sample dataset.
SO-1;
********** 9 **********
--- page 10 ---
BL-4
A hash table is a data structure that stores key-value pairs. It uses a hash
function to compute an index for storing values efficiently. When multiple
keys hash to the same index, we use separate chaining, where each bucket
contains a linked list of entries. Separate chaining is a collision resolution
technique used in hash tables. When two or more keys map to the same
index (collision), a linked list (or another data structure like a balanced tree)
is maintained at that index to store all colliding elements. Each bucket of
the hash table stores a reference to the head of a linked list containing all
elements that hash to that index. Collisions are unavoidable in hash tables
due to a limited number of slots and potentially unlimited input keys.
Separate chaining helps in handling these collisions efficiently while
maintaining fast insert, delete, and search operations. A simple hash
function can be designed as
Hash Index=Key mod Table Size
For example, if the table size is 10, and the key is 25:25 mod 10=5. So,
the key 25 will be stored in bucket index 5.
1. Implementation of Insertion(2 Marks): The insertion steps are
mentioned as below.
- Compute the hash index using the hash function.
-   If the index is empty, insert the key.
-   If a collision occurs, insert the key at the end of the linked list at
that index.
Example: Inserting 15, 25, 35 in a hash table of size 10:
- 15 mod 10=5, stored at index 5.
- 25 mod 10=5, stored at index 5 (collision, linked list used).
- 35 mod 10=5, stored at index 5.
2. Implementation of Search (2 Marks): Searching steps are
mentioned below.
- Compute the hash index.
-   Traverse the linked list at that index.
-   If the key is found, return success; otherwise, return failure.
Example: Searching for 25, then Compute
- 25 mod 10=5.
-   Traverse the linked list at index 5. Found 25 in the list.
3. Implementation of Deletion (2 Marks): The steps are listed below.
- Compute the hash index.
-   Locate the key in the linked list.
-   Delete the key by adjusting the links.
Example: Deleting 25, then compute as
- 25 mod 10=5.
-   Traverse the linked list at index 5. Remove 25 and adjust links.
Compare the time complexity of search, insertion, and deletion operations
in Red-Black trees and B-trees.
Q4 b   Illustrate the structure and properties of a B-Tree. Demonstrate how
CO-5;   insertion and node splitting maintain balance and ensure efficient disk [10]
SO-1;
BL-3   access.
********** 10 **********
--- page 11 ---
Consider a weighted undirected graph with vertices {A, B, C, D, E, F} and
edges :(A–B, 3), (A–C, 1), (B–C, 2), (B–D, 4), (C–D, 5), (C–E, 6), (D–E,
Q5 a
7), (D–F, 8), (E–F, 9).
CO-1,5;   [10]
SO-1;   Using Kruskal’s Algorithm and Union–Find, construct the Minimum
BL-5
Spanning Tree. Show the edges selected at each step and compute the total
weight of the MST.
********** 11 **********
--- page 12 ---
Solution with Union-Find (10 Marks)

1. Sort Edges by Weight (2 Marks)

Exige Weight
AC 1
ac 2
4-8 a
8D 4
co 5
ct &
DHE 7
DF a

2, Initialize Union—Find (MakeSet) (1 Mark)

Each vertex is its own parent:

Parent: A BC DE F
AB COEF

3. Kruskal with Union—Find Operations (5 Marks)

Step 1: A-C (1)
= FindA)=A, Find(C)}=C — different
» UnioniA.d

Parent: A BA DE F

w Selected

Step 2: BC (2)
= Find(B)=B, Find(Q)=A — different
«   Union(B,A)

Parent: A A A DE F

wf Selected

FRR ICR] DA KH
--- page 13 ---
What is a collision in hashing? Explain two common methods to handle
Q5 b
collisions. Compare separate chaining and open addressing. When would
CO-5;   [10]
SO-1;   you use one over the other?
BL-2
********** 13 **********
--- page 14 ---
Role of Hash Table in Symbol Table Applications:
A hash table provides efficient storage and retrieval of key-value pairs.
In symbol tables, it is used to store identifiers (like variable names) along
with associated information (type, value, memory location).
Hash tables allow average-case O(1) search, insert, and delete, making them
ideal for applications that require fast lookup.
Comparison: Sets vs Dictionaries:
Aspect   Sets   Dictionaries
Purpose   Store unique elements   Store key-value pairs
Key Use   Only the element itself   Key maps to a value
Collision Handling Same as hash table (e.g., chaining, linear probing)
Same as hash table
Advantages   Fast membership checking, prevents duplicates   Fast
retrieval of associated values, flexible storage
Limitations   Cannot store associated data Slightly higher memory usage
due to storing values along with keys
Given a set of 1000 words, design a hash table for efficient lookup
operations. Justify your choice of hash function and collision resolution
strategy.
Given the recurrence
T(n)=T(n/2)+T(n/4)+cn
Q6 a
Using the recursion tree method:
CO-1;   [5+5]
SO-1,2;   • Draw the recursion tree
BL-2
• Show the cost at each level and derive a general expression
• Determine the total cost and overall time complexity
********** 14 **********
--- page 15 ---
Q6 b   Explain the role of sift-up and sift-down operations in maintaining the heap
[10]
CO-2;   property in a binary heap. Also write the algorithm for both operations.
SO-1;
********** 15 **********
--- page 16 ---
BL-2,3 1. Role of Sift-Up and Sift-Down (5 Marks)

A binary heap is 2 complete binary tree that satisfies the heap property:

© Max-Heap: Parent > Children
© Min-Heap: Parent < Children

Sift-Up (Heapify-Up)

Role:

e Used after insertion

© Restores heap property by moving the element upward
Working:

* Compare node with its parent

¢ If heap property is violated — swap with parent
© Repeat until property is satisfied or root is reached

Sift-Down (Heapify-Down)

Role:

* Used after deletion (removing root)

© Restores heap property by moving the element downward
Working:

* Compare node with its children

© Swap with larger child (max-heap) or smaller child (min-heap)
© Continue until heap property is restored

FRR ICR 7 6 AC OH
--- page 17 ---
Explain the Merge Sort algorithm. Apply Merge Sort to the array
[38, 27, 43, 3, 9, 82, 10] and show the intermediate steps during the division
and merging process.
Step 1: Division Phase (5 marks)
Q7 a   Given array:
CO-4;   [38, 27, 43, 3, 9, 82, 10]   [10]
SO-1;
BL-2
Divide recursively:
[38, 27, 43, 3, 9, 82, 10]
→[38,27,43][3,9,82,10]
→[38][27,43][3,9][82,10]
→[38][27][43][3][9][82][10]
********** 17 **********
--- page 18 ---
All subarrays reduced to single elements
Step 2: Merging Phase (5 marks)
Merge step-by-step:
• Merge [27] and [43] →
[27, 43]
• Merge [38] and [27,43] →
[27, 38, 43]
• Merge [3] and [9] →
[3, 9]
• Merge [82] and [10] →
[10, 82]
• Merge [3,9] and [10,82] →
[3, 9, 10, 82]
•   Final merge:
[27,38,43]  &  [3,9,10,82]
⇒[3,9,10,27,38,43,82]
Final Sorted Array:
[3, 9, 10, 27, 38, 43, 82]
(i) Explain floor and ceiling operations in a BST. State the cases for
Q7 b   computing floor(key) and write the recursive logic.
CO-2,3,5;   (ii) Discuss how sparse vectors can be efficiently represented using   [5+5]
SO-1;
BL-3,2   hash tables and explain their significance.
(i)   5 marks
********** 18 **********
--- page 19 ---
(i) Floor and Ceiling in a BST

Definition

« Floor(key): Largest value = key
* Ceiling(key): Smallest value = key

Cases for Floor(key)
Ata node with value x:
1. lf x == key - floor = x
2. If x > key — search in left subtree
3. lf x < key —
* x can bea candidate

* search in right subtree for a closer value

Recursive Logic (Floor)

floor(root, key):
if root == NULL:
return NULL

if root.data == key:
return root.data

if root.data > key:
return floor(root.left, key)

val = floor(root.right, key)
if val != NULL:
return val

else:
return root.data

(ii) 5 marks

FRR ICR 7 QI OR
--- page 20 ---
(ii) Sparse Vectors using Hash Tables

Representation

* Store only non-zero elements
* Use index as key and value as data in a hash table

Example:
Vector [@, @, 5, @, @, 3] + {2:5, 5:3}

Advantages / Significance

® Space efficient - avoids storing zeros
* Faster operations — direct access using index
* Efficient for:
* Dot product computation
* Machine learning / data science applications

FRI ICR DO) A RH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a65f28b0e3b0

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: mixed (20 pages), mean OCR confidence 78.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
Implement the single linked list with the following functionalities:
CO-1,2;   i. Insertion and Deletion
SO- 1;   a.   ii. Display   [5]
BL- 3   (Practical)
Note: Can be implemented in C++/Java/Python language.
********** 1 **********
--- page 2 ---
Explain what a KD-tree is and how it differs from a standard BST, highlighting its
advantages in multidimensional data.
A KD-tree (K-Dimensional Tree) is a space-partitioning data structure used
to organize points in a k-dimensional space. It is a type of binary tree in
which each node represents a point in k-dimensional space, and the tree
recursively partitions the space into smaller regions. Unlike a simple Binary
Search Tree, which stores one-dimensional data, a KD-tree stores
multidimensional data such as points in 2D, 3D, or higher dimensions.
Differences Between KD-Tree and BST
CO-1,5;
b.   Differences Between KD-Tree and BST: The KD-tree and BST are both   [5]
SO-1;
binary tree structures, they are designed for different purposes and handle
BL-2   data differently.
Feature   KD-Tree   Binary Search Tree (BST)
Data Type Multidimensional data (points in k-   One-dimensional data
dimensions)
Splitting   Splits data based on different   Splits based on single key comparison
Criteria   dimensions alternately
Structure   Each level uses a different   All levels use the same key comparison
dimension
********** 2 **********
--- page 3 ---
Example Data   (x, y), (x, y, z) coordinates   Numbers or strings
Application Spatial searching, nearest neighbor Sorting, dictionary operations
s   queries
Range   Efficient in multi-dimensional range   Efficient only for one-dimensional range
Queries   queries   queries
Search   Divides geometric space into   Divides ordered key values
Space   regions
Differentiate between best-case, average-case, and worst-case time complexity.
Best-case Time Complexity:
Minimum time an algorithm takes to complete.
Example: Quick Sort on a perfectly balanced array.
Notation: O(n)
(2 marks)
CO-1;   Average-case Time Complexity:
SO-1,2;   c.   [5]
BL-4   Expected time over all possible inputs of a given size.
Example: Quick Sort on a random array → O(n log n)
(2 marks)
Worst-case Time Complexity:
Maximum time an algorithm takes on any input of size n.
Example: Quick Sort on a sorted array with last element as pivot → O(n²)
(1 marks)
Given two arrays:
A: random order
B: already sorted
Explain how Quick Sort behaves on both when the last element is always
chosen as pivot.
CO-4;
SO-1;   d.   [5]
BL-2
********** 3 **********
--- page 4 ---
In the Dynamic Connectivity problem using Disjoint Sets, discuss the
Quick-Find and Quick-Union approaches for managing relationships
between elements. State their limitations in terms of worst-case time
complexity.
Dynamic connectivity is a problem where we need to determine whether two
elements are in the same connected component and efficiently merge
components when a new connection is added. Two fundamental approaches
to solving this problem are Quick Find and Quick Union.
Quick Find Approach: Quick Find is an approach in which each element in
the data structure maintains an array index as its identifier. When performing
the union operation, all elements in the set of one element are updated to
match the identifier of the other set.
Algorithm:
1. Initialize an array id[] of size N, where id[i] = i.
Q2 a   2. find(p): Returns id[p].
CO-1,5;   [10]
SO-1,2;   3. union(p, q): Change id[i] to id[q] for all i where id[i] = id[p].
BL-2,4
Time Complexity: The time complexity is mentioned below.
-   find(p): O(1) (constant time lookup).
-   union(p, q): O(N) (modifies all elements in the set).
Quick Union Approach: Quick Union is a lazy approach where elements
maintain a pointer to their parent. The root of a tree represents the set.
Algorithm:
Initialize an array id[], where each element is its own parent
1. find(p): Follow parent pointers until reaching the root.
2. union(p, q): Attach the root of one tree to the root of another.
Time Complexity: The time complexity is mentioned below.
-   find(p): O(N) in the worst case.
-   union(p, q): O(N) in the worst case.
Comparison of Quick Find and Quick Union approaches
********** 4 **********
--- page 5 ---
Quick Find is preferable when we need fast find operations and are willing
to pay a higher cost for union. Quick Union is preferable when union
operations are frequent, but it should be used with optimizations like
Weighted Quick Union and Path Compression to achieve near-constant
time complexity.
Marks Distribution: Quick Find and Quick Union 6 Marks + Time Complexity
Analysis 4 Marks
Define a Red-Black Tree and list all five essential properties that maintain
its balance. Construct an initially empty Red Black Tree by inserting keys
15,13,12,16,19,23,5,8 and show the result of step-by-step insertion. Clearly
label node colors and indicate where rotations or recoloring occurred.
A Red-Black Tree (RBT) is a self-balancing Binary Search Tree where each
Q2 b   node has an extra bit for color (Red or Black), ensuring the tree remains
CO-5;   approximately balanced after insertions and deletions.   [10]
SO-1;
BL-6   Five Essential Properties
1. Every node is either Red or Black
2. The root is always Black
3. No two consecutive Red nodes (no Red parent with Red child)
4. Every path from a node to its NULL descendants has the same
number of Black nodes
5. All NULL leaves are Black
********** 5 **********
--- page 6 ---
3. Step-by-Step Insertion

Insert 15

= First mode — becomes root + colored Black

1s(8)

Insert 13

. Insert as left child of 15
7 Parent is Back + no violation

15(8)
f
1a(R)

Insert 12

= Insert as Jett child of 13 — Red-Red violation
« Case: Left-Left — Right Rotation at 15 + recoloring

1308)
# \
12(R) 15(R)

Insert 16

. Insert as night child of 15
= Parent (15) is Red. Uncle (12) is Rad —- Recoloring

13(8)
f ‘
12(8) 15(B)

1e(R)

Insert 19

= Insert as. right child of 16 — Red-Red violation
« Case: Right-Right — Left Rotation at 15 + recoloring

13(8)
i “
12(8) 26(B)
!
1s(R} 1S(R)

%

FIC 6 I HF
--- page 7 ---
Implement a static queue using an array and a dynamic queue using a linked
list. Perform enqueue and dequeue operations, display the queue after each
operation. (practical)
Can be implemented in C++/Java/Python language
1. Static Queue (Array-Based)
Q3 a   Class StaticQueue:
CO-2,4;   Define:   [10]
SO-1;
BL-3   - `capacity`: Maximum queue size
- `front`, `rear`: Pointers for queue operations
- `size`: Tracks current number of elements
- `array`: Stores queue elements
Function ENQUEUE(value):
- If queue is full, print "Queue is full".
********** 7 **********
--- page 8 ---
- Increment `rear` circularly.
- Insert `value` at `rear` position.
- Increase `size`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next element.
- Decrease `size`.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
2. Dynamic Queue (Linked List-Based)
Class Node:
- `data`: Holds value
- `next`: Pointer to next node
Class DynamicQueue:
Define:
- `front`, `rear`: Pointers to track queue
Function ENQUEUE(value):
- Create a new node with `value`.
- If queue is empty, set both `front` and `rear` to new node.
- Else, attach new node to `rear.next` and update `rear`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next node.
- If `front` becomes null, update `rear` to null.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
Marks Distribution: Static Queue 5 Marks + Dynamic Queue 5 Marks
Q3 b
Insert the keys H, C, R, A, E, S, X into a Binary Search Tree (BST) in the given
CO-3;   [10]
SO-1;   order and draw the tree. Determine the minimum and maximum keys. Perform
BL-2
********** 8 **********
--- page 9 ---
deleteMin() and deleteMax() operations and draw the final tree after both deletions.
Also, write pseudocode for deleteMin() and deleteMax() in a BST.
Q4 a   Implement a hash table using separate chaining. Demonstrate how to
[10]
CO-5;   perform insertion, search, and deletion operations with a sample dataset.
SO-1;
********** 9 **********
--- page 10 ---
BL-4
A hash table is a data structure that stores key-value pairs. It uses a hash
function to compute an index for storing values efficiently. When multiple
keys hash to the same index, we use separate chaining, where each bucket
contains a linked list of entries. Separate chaining is a collision resolution
technique used in hash tables. When two or more keys map to the same
index (collision), a linked list (or another data structure like a balanced tree)
is maintained at that index to store all colliding elements. Each bucket of
the hash table stores a reference to the head of a linked list containing all
elements that hash to that index. Collisions are unavoidable in hash tables
due to a limited number of slots and potentially unlimited input keys.
Separate chaining helps in handling these collisions efficiently while
maintaining fast insert, delete, and search operations. A simple hash
function can be designed as
Hash Index=Key mod Table Size
For example, if the table size is 10, and the key is 25:25 mod 10=5. So,
the key 25 will be stored in bucket index 5.
1. Implementation of Insertion(2 Marks): The insertion steps are
mentioned as below.
- Compute the hash index using the hash function.
-   If the index is empty, insert the key.
-   If a collision occurs, insert the key at the end of the linked list at
that index.
Example: Inserting 15, 25, 35 in a hash table of size 10:
- 15 mod 10=5, stored at index 5.
- 25 mod 10=5, stored at index 5 (collision, linked list used).
- 35 mod 10=5, stored at index 5.
2. Implementation of Search (2 Marks): Searching steps are
mentioned below.
- Compute the hash index.
-   Traverse the linked list at that index.
-   If the key is found, return success; otherwise, return failure.
Example: Searching for 25, then Compute
- 25 mod 10=5.
-   Traverse the linked list at index 5. Found 25 in the list.
3. Implementation of Deletion (2 Marks): The steps are listed below.
- Compute the hash index.
-   Locate the key in the linked list.
-   Delete the key by adjusting the links.
Example: Deleting 25, then compute as
- 25 mod 10=5.
-   Traverse the linked list at index 5. Remove 25 and adjust links.
Compare the time complexity of search, insertion, and deletion operations
in Red-Black trees and B-trees.
Q4 b   Illustrate the structure and properties of a B-Tree. Demonstrate how
CO-5;   insertion and node splitting maintain balance and ensure efficient disk [10]
SO-1;
BL-3   access.
********** 10 **********
--- page 11 ---
Consider a weighted undirected graph with vertices {A, B, C, D, E, F} and
edges :(A–B, 3), (A–C, 1), (B–C, 2), (B–D, 4), (C–D, 5), (C–E, 6), (D–E,
Q5 a
7), (D–F, 8), (E–F, 9).
CO-1,5;   [10]
SO-1;   Using Kruskal’s Algorithm and Union–Find, construct the Minimum
BL-5
Spanning Tree. Show the edges selected at each step and compute the total
weight of the MST.
********** 11 **********
--- page 12 ---
Solution with Union-Find (10 Marks)

1. Sort Edges by Weight (2 Marks)

Exige Weight
AC 1
ac 2
4-8 a
8D 4
co 5
ct &
DHE 7
DF a

2, Initialize Union—Find (MakeSet) (1 Mark)

Each vertex is its own parent:

Parent: A BC DE F
AB COEF

3. Kruskal with Union—Find Operations (5 Marks)

Step 1: A-C (1)
= FindA)=A, Find(C)}=C — different
» UnioniA.d

Parent: A BA DE F

w Selected

Step 2: BC (2)
= Find(B)=B, Find(Q)=A — different
«   Union(B,A)

Parent: A A A DE F

wf Selected

FRR ICR] DA KH
--- page 13 ---
What is a collision in hashing? Explain two common methods to handle
Q5 b
collisions. Compare separate chaining and open addressing. When would
CO-5;   [10]
SO-1;   you use one over the other?
BL-2
********** 13 **********
--- page 14 ---
Role of Hash Table in Symbol Table Applications:
A hash table provides efficient storage and retrieval of key-value pairs.
In symbol tables, it is used to store identifiers (like variable names) along
with associated information (type, value, memory location).
Hash tables allow average-case O(1) search, insert, and delete, making them
ideal for applications that require fast lookup.
Comparison: Sets vs Dictionaries:
Aspect   Sets   Dictionaries
Purpose   Store unique elements   Store key-value pairs
Key Use   Only the element itself   Key maps to a value
Collision Handling Same as hash table (e.g., chaining, linear probing)
Same as hash table
Advantages   Fast membership checking, prevents duplicates   Fast
retrieval of associated values, flexible storage
Limitations   Cannot store associated data Slightly higher memory usage
due to storing values along with keys
Given a set of 1000 words, design a hash table for efficient lookup
operations. Justify your choice of hash function and collision resolution
strategy.
Given the recurrence
T(n)=T(n/2)+T(n/4)+cn
Q6 a
Using the recursion tree method:
CO-1;   [5+5]
SO-1,2;   • Draw the recursion tree
BL-2
• Show the cost at each level and derive a general expression
• Determine the total cost and overall time complexity
********** 14 **********
--- page 15 ---
Q6 b   Explain the role of sift-up and sift-down operations in maintaining the heap
[10]
CO-2;   property in a binary heap. Also write the algorithm for both operations.
SO-1;
********** 15 **********
--- page 16 ---
BL-2,3 1. Role of Sift-Up and Sift-Down (5 Marks)

A binary heap is 2 complete binary tree that satisfies the heap property:

© Max-Heap: Parent > Children
© Min-Heap: Parent < Children

Sift-Up (Heapify-Up)

Role:

e Used after insertion

© Restores heap property by moving the element upward
Working:

* Compare node with its parent

¢ If heap property is violated — swap with parent
© Repeat until property is satisfied or root is reached

Sift-Down (Heapify-Down)

Role:

* Used after deletion (removing root)

© Restores heap property by moving the element downward
Working:

* Compare node with its children

© Swap with larger child (max-heap) or smaller child (min-heap)
© Continue until heap property is restored

FRR ICR 7 6 AC OH
--- page 17 ---
Explain the Merge Sort algorithm. Apply Merge Sort to the array
[38, 27, 43, 3, 9, 82, 10] and show the intermediate steps during the division
and merging process.
Step 1: Division Phase (5 marks)
Q7 a   Given array:
CO-4;   [38, 27, 43, 3, 9, 82, 10]   [10]
SO-1;
BL-2
Divide recursively:
[38, 27, 43, 3, 9, 82, 10]
→[38,27,43][3,9,82,10]
→[38][27,43][3,9][82,10]
→[38][27][43][3][9][82][10]
********** 17 **********
--- page 18 ---
All subarrays reduced to single elements
Step 2: Merging Phase (5 marks)
Merge step-by-step:
• Merge [27] and [43] →
[27, 43]
• Merge [38] and [27,43] →
[27, 38, 43]
• Merge [3] and [9] →
[3, 9]
• Merge [82] and [10] →
[10, 82]
• Merge [3,9] and [10,82] →
[3, 9, 10, 82]
•   Final merge:
[27,38,43]  &  [3,9,10,82]
⇒[3,9,10,27,38,43,82]
Final Sorted Array:
[3, 9, 10, 27, 38, 43, 82]
(i) Explain floor and ceiling operations in a BST. State the cases for
Q7 b   computing floor(key) and write the recursive logic.
CO-2,3,5;   (ii) Discuss how sparse vectors can be efficiently represented using   [5+5]
SO-1;
BL-3,2   hash tables and explain their significance.
(i)   5 marks
********** 18 **********
--- page 19 ---
(i) Floor and Ceiling in a BST

Definition

« Floor(key): Largest value = key
* Ceiling(key): Smallest value = key

Cases for Floor(key)
Ata node with value x:
1. lf x == key - floor = x
2. If x > key — search in left subtree
3. lf x < key —
* x can bea candidate

* search in right subtree for a closer value

Recursive Logic (Floor)

floor(root, key):
if root == NULL:
return NULL

if root.data == key:
return root.data

if root.data > key:
return floor(root.left, key)

val = floor(root.right, key)
if val != NULL:
return val

else:
return root.data

(ii) 5 marks

FRR ICR 7 QI OR
--- page 20 ---
(ii) Sparse Vectors using Hash Tables

Representation

* Store only non-zero elements
* Use index as key and value as data in a hash table

Example:
Vector [@, @, 5, @, @, 3] + {2:5, 5:3}

Advantages / Significance

® Space efficient - avoids storing zeros
* Faster operations — direct access using index
* Efficient for:
* Dot product computation
* Machine learning / data science applications

FRI ICR DO) A RH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3fb12c2aac72

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_DS_7052/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: mixed (20 pages), mean OCR confidence 78.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
Implement the single linked list with the following functionalities:
CO-1,2;   i. Insertion and Deletion
SO- 1;   a.   ii. Display   [5]
BL- 3   (Practical)
Note: Can be implemented in C++/Java/Python language.
********** 1 **********
--- page 2 ---
Explain what a KD-tree is and how it differs from a standard BST, highlighting its
advantages in multidimensional data.
A KD-tree (K-Dimensional Tree) is a space-partitioning data structure used
to organize points in a k-dimensional space. It is a type of binary tree in
which each node represents a point in k-dimensional space, and the tree
recursively partitions the space into smaller regions. Unlike a simple Binary
Search Tree, which stores one-dimensional data, a KD-tree stores
multidimensional data such as points in 2D, 3D, or higher dimensions.
Differences Between KD-Tree and BST
CO-1,5;
b.   Differences Between KD-Tree and BST: The KD-tree and BST are both   [5]
SO-1;
binary tree structures, they are designed for different purposes and handle
BL-2   data differently.
Feature   KD-Tree   Binary Search Tree (BST)
Data Type Multidimensional data (points in k-   One-dimensional data
dimensions)
Splitting   Splits data based on different   Splits based on single key comparison
Criteria   dimensions alternately
Structure   Each level uses a different   All levels use the same key comparison
dimension
********** 2 **********
--- page 3 ---
Example Data   (x, y), (x, y, z) coordinates   Numbers or strings
Application Spatial searching, nearest neighbor Sorting, dictionary operations
s   queries
Range   Efficient in multi-dimensional range   Efficient only for one-dimensional range
Queries   queries   queries
Search   Divides geometric space into   Divides ordered key values
Space   regions
Differentiate between best-case, average-case, and worst-case time complexity.
Best-case Time Complexity:
Minimum time an algorithm takes to complete.
Example: Quick Sort on a perfectly balanced array.
Notation: O(n)
(2 marks)
CO-1;   Average-case Time Complexity:
SO-1,2;   c.   [5]
BL-4   Expected time over all possible inputs of a given size.
Example: Quick Sort on a random array → O(n log n)
(2 marks)
Worst-case Time Complexity:
Maximum time an algorithm takes on any input of size n.
Example: Quick Sort on a sorted array with last element as pivot → O(n²)
(1 marks)
Given two arrays:
A: random order
B: already sorted
Explain how Quick Sort behaves on both when the last element is always
chosen as pivot.
CO-4;
SO-1;   d.   [5]
BL-2
********** 3 **********
--- page 4 ---
In the Dynamic Connectivity problem using Disjoint Sets, discuss the
Quick-Find and Quick-Union approaches for managing relationships
between elements. State their limitations in terms of worst-case time
complexity.
Dynamic connectivity is a problem where we need to determine whether two
elements are in the same connected component and efficiently merge
components when a new connection is added. Two fundamental approaches
to solving this problem are Quick Find and Quick Union.
Quick Find Approach: Quick Find is an approach in which each element in
the data structure maintains an array index as its identifier. When performing
the union operation, all elements in the set of one element are updated to
match the identifier of the other set.
Algorithm:
1. Initialize an array id[] of size N, where id[i] = i.
Q2 a   2. find(p): Returns id[p].
CO-1,5;   [10]
SO-1,2;   3. union(p, q): Change id[i] to id[q] for all i where id[i] = id[p].
BL-2,4
Time Complexity: The time complexity is mentioned below.
-   find(p): O(1) (constant time lookup).
-   union(p, q): O(N) (modifies all elements in the set).
Quick Union Approach: Quick Union is a lazy approach where elements
maintain a pointer to their parent. The root of a tree represents the set.
Algorithm:
Initialize an array id[], where each element is its own parent
1. find(p): Follow parent pointers until reaching the root.
2. union(p, q): Attach the root of one tree to the root of another.
Time Complexity: The time complexity is mentioned below.
-   find(p): O(N) in the worst case.
-   union(p, q): O(N) in the worst case.
Comparison of Quick Find and Quick Union approaches
********** 4 **********
--- page 5 ---
Quick Find is preferable when we need fast find operations and are willing
to pay a higher cost for union. Quick Union is preferable when union
operations are frequent, but it should be used with optimizations like
Weighted Quick Union and Path Compression to achieve near-constant
time complexity.
Marks Distribution: Quick Find and Quick Union 6 Marks + Time Complexity
Analysis 4 Marks
Define a Red-Black Tree and list all five essential properties that maintain
its balance. Construct an initially empty Red Black Tree by inserting keys
15,13,12,16,19,23,5,8 and show the result of step-by-step insertion. Clearly
label node colors and indicate where rotations or recoloring occurred.
A Red-Black Tree (RBT) is a self-balancing Binary Search Tree where each
Q2 b   node has an extra bit for color (Red or Black), ensuring the tree remains
CO-5;   approximately balanced after insertions and deletions.   [10]
SO-1;
BL-6   Five Essential Properties
1. Every node is either Red or Black
2. The root is always Black
3. No two consecutive Red nodes (no Red parent with Red child)
4. Every path from a node to its NULL descendants has the same
number of Black nodes
5. All NULL leaves are Black
********** 5 **********
--- page 6 ---
3. Step-by-Step Insertion

Insert 15

= First mode — becomes root + colored Black

1s(8)

Insert 13

. Insert as left child of 15
7 Parent is Back + no violation

15(8)
f
1a(R)

Insert 12

= Insert as Jett child of 13 — Red-Red violation
« Case: Left-Left — Right Rotation at 15 + recoloring

1308)
# \
12(R) 15(R)

Insert 16

. Insert as night child of 15
= Parent (15) is Red. Uncle (12) is Rad —- Recoloring

13(8)
f ‘
12(8) 15(B)

1e(R)

Insert 19

= Insert as. right child of 16 — Red-Red violation
« Case: Right-Right — Left Rotation at 15 + recoloring

13(8)
i “
12(8) 26(B)
!
1s(R} 1S(R)

%

FIC 6 I HF
--- page 7 ---
Implement a static queue using an array and a dynamic queue using a linked
list. Perform enqueue and dequeue operations, display the queue after each
operation. (practical)
Can be implemented in C++/Java/Python language
1. Static Queue (Array-Based)
Q3 a   Class StaticQueue:
CO-2,4;   Define:   [10]
SO-1;
BL-3   - `capacity`: Maximum queue size
- `front`, `rear`: Pointers for queue operations
- `size`: Tracks current number of elements
- `array`: Stores queue elements
Function ENQUEUE(value):
- If queue is full, print "Queue is full".
********** 7 **********
--- page 8 ---
- Increment `rear` circularly.
- Insert `value` at `rear` position.
- Increase `size`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next element.
- Decrease `size`.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
2. Dynamic Queue (Linked List-Based)
Class Node:
- `data`: Holds value
- `next`: Pointer to next node
Class DynamicQueue:
Define:
- `front`, `rear`: Pointers to track queue
Function ENQUEUE(value):
- Create a new node with `value`.
- If queue is empty, set both `front` and `rear` to new node.
- Else, attach new node to `rear.next` and update `rear`.
Function DEQUEUE():
- If queue is empty, print "Queue is empty".
- Move `front` pointer to next node.
- If `front` becomes null, update `rear` to null.
Function DISPLAY():
- Traverse from `front` to `rear` and print elements.
Time Complexity:
- Enqueue: O(1) (Direct insertion at `rear`)
- Dequeue: O(1) (Direct removal at `front`)
Marks Distribution: Static Queue 5 Marks + Dynamic Queue 5 Marks
Q3 b
Insert the keys H, C, R, A, E, S, X into a Binary Search Tree (BST) in the given
CO-3;   [10]
SO-1;   order and draw the tree. Determine the minimum and maximum keys. Perform
BL-2
********** 8 **********
--- page 9 ---
deleteMin() and deleteMax() operations and draw the final tree after both deletions.
Also, write pseudocode for deleteMin() and deleteMax() in a BST.
Q4 a   Implement a hash table using separate chaining. Demonstrate how to
[10]
CO-5;   perform insertion, search, and deletion operations with a sample dataset.
SO-1;
********** 9 **********
--- page 10 ---
BL-4
A hash table is a data structure that stores key-value pairs. It uses a hash
function to compute an index for storing values efficiently. When multiple
keys hash to the same index, we use separate chaining, where each bucket
contains a linked list of entries. Separate chaining is a collision resolution
technique used in hash tables. When two or more keys map to the same
index (collision), a linked list (or another data structure like a balanced tree)
is maintained at that index to store all colliding elements. Each bucket of
the hash table stores a reference to the head of a linked list containing all
elements that hash to that index. Collisions are unavoidable in hash tables
due to a limited number of slots and potentially unlimited input keys.
Separate chaining helps in handling these collisions efficiently while
maintaining fast insert, delete, and search operations. A simple hash
function can be designed as
Hash Index=Key mod Table Size
For example, if the table size is 10, and the key is 25:25 mod 10=5. So,
the key 25 will be stored in bucket index 5.
1. Implementation of Insertion(2 Marks): The insertion steps are
mentioned as below.
- Compute the hash index using the hash function.
-   If the index is empty, insert the key.
-   If a collision occurs, insert the key at the end of the linked list at
that index.
Example: Inserting 15, 25, 35 in a hash table of size 10:
- 15 mod 10=5, stored at index 5.
- 25 mod 10=5, stored at index 5 (collision, linked list used).
- 35 mod 10=5, stored at index 5.
2. Implementation of Search (2 Marks): Searching steps are
mentioned below.
- Compute the hash index.
-   Traverse the linked list at that index.
-   If the key is found, return success; otherwise, return failure.
Example: Searching for 25, then Compute
- 25 mod 10=5.
-   Traverse the linked list at index 5. Found 25 in the list.
3. Implementation of Deletion (2 Marks): The steps are listed below.
- Compute the hash index.
-   Locate the key in the linked list.
-   Delete the key by adjusting the links.
Example: Deleting 25, then compute as
- 25 mod 10=5.
-   Traverse the linked list at index 5. Remove 25 and adjust links.
Compare the time complexity of search, insertion, and deletion operations
in Red-Black trees and B-trees.
Q4 b   Illustrate the structure and properties of a B-Tree. Demonstrate how
CO-5;   insertion and node splitting maintain balance and ensure efficient disk [10]
SO-1;
BL-3   access.
********** 10 **********
--- page 11 ---
Consider a weighted undirected graph with vertices {A, B, C, D, E, F} and
edges :(A–B, 3), (A–C, 1), (B–C, 2), (B–D, 4), (C–D, 5), (C–E, 6), (D–E,
Q5 a
7), (D–F, 8), (E–F, 9).
CO-1,5;   [10]
SO-1;   Using Kruskal’s Algorithm and Union–Find, construct the Minimum
BL-5
Spanning Tree. Show the edges selected at each step and compute the total
weight of the MST.
********** 11 **********
--- page 12 ---
Solution with Union-Find (10 Marks)

1. Sort Edges by Weight (2 Marks)

Exige Weight
AC 1
ac 2
4-8 a
8D 4
co 5
ct &
DHE 7
DF a

2, Initialize Union—Find (MakeSet) (1 Mark)

Each vertex is its own parent:

Parent: A BC DE F
AB COEF

3. Kruskal with Union—Find Operations (5 Marks)

Step 1: A-C (1)
= FindA)=A, Find(C)}=C — different
» UnioniA.d

Parent: A BA DE F

w Selected

Step 2: BC (2)
= Find(B)=B, Find(Q)=A — different
«   Union(B,A)

Parent: A A A DE F

wf Selected

FRR ICR] DA KH
--- page 13 ---
What is a collision in hashing? Explain two common methods to handle
Q5 b
collisions. Compare separate chaining and open addressing. When would
CO-5;   [10]
SO-1;   you use one over the other?
BL-2
********** 13 **********
--- page 14 ---
Role of Hash Table in Symbol Table Applications:
A hash table provides efficient storage and retrieval of key-value pairs.
In symbol tables, it is used to store identifiers (like variable names) along
with associated information (type, value, memory location).
Hash tables allow average-case O(1) search, insert, and delete, making them
ideal for applications that require fast lookup.
Comparison: Sets vs Dictionaries:
Aspect   Sets   Dictionaries
Purpose   Store unique elements   Store key-value pairs
Key Use   Only the element itself   Key maps to a value
Collision Handling Same as hash table (e.g., chaining, linear probing)
Same as hash table
Advantages   Fast membership checking, prevents duplicates   Fast
retrieval of associated values, flexible storage
Limitations   Cannot store associated data Slightly higher memory usage
due to storing values along with keys
Given a set of 1000 words, design a hash table for efficient lookup
operations. Justify your choice of hash function and collision resolution
strategy.
Given the recurrence
T(n)=T(n/2)+T(n/4)+cn
Q6 a
Using the recursion tree method:
CO-1;   [5+5]
SO-1,2;   • Draw the recursion tree
BL-2
• Show the cost at each level and derive a general expression
• Determine the total cost and overall time complexity
********** 14 **********
--- page 15 ---
Q6 b   Explain the role of sift-up and sift-down operations in maintaining the heap
[10]
CO-2;   property in a binary heap. Also write the algorithm for both operations.
SO-1;
********** 15 **********
--- page 16 ---
BL-2,3 1. Role of Sift-Up and Sift-Down (5 Marks)

A binary heap is 2 complete binary tree that satisfies the heap property:

© Max-Heap: Parent > Children
© Min-Heap: Parent < Children

Sift-Up (Heapify-Up)

Role:

e Used after insertion

© Restores heap property by moving the element upward
Working:

* Compare node with its parent

¢ If heap property is violated — swap with parent
© Repeat until property is satisfied or root is reached

Sift-Down (Heapify-Down)

Role:

* Used after deletion (removing root)

© Restores heap property by moving the element downward
Working:

* Compare node with its children

© Swap with larger child (max-heap) or smaller child (min-heap)
© Continue until heap property is restored

FRR ICR 7 6 AC OH
--- page 17 ---
Explain the Merge Sort algorithm. Apply Merge Sort to the array
[38, 27, 43, 3, 9, 82, 10] and show the intermediate steps during the division
and merging process.
Step 1: Division Phase (5 marks)
Q7 a   Given array:
CO-4;   [38, 27, 43, 3, 9, 82, 10]   [10]
SO-1;
BL-2
Divide recursively:
[38, 27, 43, 3, 9, 82, 10]
→[38,27,43][3,9,82,10]
→[38][27,43][3,9][82,10]
→[38][27][43][3][9][82][10]
********** 17 **********
--- page 18 ---
All subarrays reduced to single elements
Step 2: Merging Phase (5 marks)
Merge step-by-step:
• Merge [27] and [43] →
[27, 43]
• Merge [38] and [27,43] →
[27, 38, 43]
• Merge [3] and [9] →
[3, 9]
• Merge [82] and [10] →
[10, 82]
• Merge [3,9] and [10,82] →
[3, 9, 10, 82]
•   Final merge:
[27,38,43]  &  [3,9,10,82]
⇒[3,9,10,27,38,43,82]
Final Sorted Array:
[3, 9, 10, 27, 38, 43, 82]
(i) Explain floor and ceiling operations in a BST. State the cases for
Q7 b   computing floor(key) and write the recursive logic.
CO-2,3,5;   (ii) Discuss how sparse vectors can be efficiently represented using   [5+5]
SO-1;
BL-3,2   hash tables and explain their significance.
(i)   5 marks
********** 18 **********
--- page 19 ---
(i) Floor and Ceiling in a BST

Definition

« Floor(key): Largest value = key
* Ceiling(key): Smallest value = key

Cases for Floor(key)
Ata node with value x:
1. lf x == key - floor = x
2. If x > key — search in left subtree
3. lf x < key —
* x can bea candidate

* search in right subtree for a closer value

Recursive Logic (Floor)

floor(root, key):
if root == NULL:
return NULL

if root.data == key:
return root.data

if root.data > key:
return floor(root.left, key)

val = floor(root.right, key)
if val != NULL:
return val

else:
return root.data

(ii) 5 marks

FRR ICR 7 QI OR
--- page 20 ---
(ii) Sparse Vectors using Hash Tables

Representation

* Store only non-zero elements
* Use index as key and value as data in a hash table

Example:
Vector [@, @, 5, @, @, 3] + {2:5, 5:3}

Advantages / Significance

® Space efficient - avoids storing zeros
* Faster operations — direct access using index
* Efficient for:
* Dot product computation
* Machine learning / data science applications

FRI ICR DO) A RH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper e4c50e23d625

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7057/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: mixed (10 pages), mean OCR confidence 85.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:
Design and implement a Stack using an array. The program should support
the following operations:
CO-1,2;   i. Push , Pop
SO- 1;   a.   [5]
ii. Display
BL- 3
(Practical)
Can be done in any language
CO-1,5;   Describe how Interval Trees are used to identify overlapping intervals.
SO-1;   b.   [5]
Explain the working principle and analyze the time complexity.
BL-2
********** 1 **********
--- page 2 ---
Compare the Master Theorem and the recursion tree method for solving
recurrence relations. When is each method preferred?
CO-1;
SO-1,2;   c.   [5]
BL-4
Explain why Heap Sort is considered an unstable sorting algorithm. Support
your answer with reasoning.
Heap Sort is considered unstable because it does not preserve the relative
order of equal elements during sorting.
CO-4;   Reasoning:
SO-1;   d.   [5]
Heap Sort repeatedly swaps the root (maximum element) with the last
BL-2
element in the heap.
During heapify (sift-down), elements may move across different levels of
the tree.
These operations do not track or preserve the original order of equal keys.
Q2 a   Explain Kruskal’s Algorithm for constructing a Minimum Spanning Tree in
CO-1,5;   a weighted graph. Analyze the role of the Union–Find in detecting cycles [10]
SO-1,2;
during the execution of the algorithm.
BL-2,4
********** 2 **********
--- page 3 ---
Construct a Red-Black Tree for the keys [10, 20, 30, 15, 25, 5, 1].
Demonstrate all rotations and color adjustments during insertion, and justify
how each step satisfies the five properties of a Red-Black Tree and maintains
balance after updates.
Q2 b
CO-5;   [10]
SO-1;
BL-6
Five Properties (Justification)
1. Every node is either RED or BLACK ✔
2. Root is BLACK → 20(B) ✔
3. No two consecutive RED nodes ✔
********** 3 **********
--- page 4 ---
4. Every path has same number of BLACK nodes ✔
5. All NULL leaves are BLACK ✔
Role of Rotations
•   Left rotation (at 10) balanced the tree when inserting 30
•   Rotations help:
o Maintain BST structure
o Reduce tree height
o Fix RED–RED violations
Implement a queue using both an array and a linked list. Demonstrate
Q3 a   enqueue and dequeue operations for both representations and show the state
CO-2,4;   of the queue after each operation.   [10]
SO-1;
(practical)
BL-3
Can be done in any language
Construct a Binary Search Tree (BST) using the keys 45, 25, 65, 15, 35, 55,
75 in the given order and draw the resulting tree. Find its height and perform
a search for the key 35 by tracing the path. Also, state the effect on the BST
structure and search complexity if the keys are inserted in sorted order.
Q3 b
CO-3;   [10]
SO-1;
BL-2
Q4 a
A sparse vector of size 15 is given as:
CO-5;   V = [0, 0, 5, 0, 0, 9, 0, 0, 0, 12, 0, 0, 3, 0, 0]   [10]
SO-1;
BL-4
********** 4 **********
--- page 5 ---
Design a hash table representation for this sparse vector using the hash
function h(i) = i mod 7, where i is the index.
•   Insert all non-zero elements into the hash table (store index, value
pairs).
• Show the final hash table.
• Demonstrate how to retrieve the value at index 9 and 4.
Insert keys 3, 7, 1, 5, 9, 2, 8 one by one into an empty 2-3 tree.
• Draw the tree after every insertion and show all splits and
Q4 b
promotions clearly.
CO-5;   [10]
SO-1;   • On the final 2-3 tree from above, perform an in-order traversal and
BL-3
compute: floor (4), ceiling (6), rank (7), and select (4).
(5 Marks) Construction of 2-3 Tree
********** 5 **********
--- page 6 ---
(1 Marks) In-order Traversal
1, 2, 3, 5, 7, 8, 9
(4 Marks) Computations
•   floor(4) → 3
•   ceiling(6) → 7
•   rank(7) → 4 (elements < 7)
•   select(4) → 5 (4th smallest)
Discuss Quick-Find and Quick-Union algorithms for Disjoint Set
operations.Analyze and compare their time complexities for large datasets.
Explain why Quick-Find becomes inefficient compared to Quick-Union.
(3 Marks) Concepts
• Quick-Find:
Maintains an array where each element stores its set id.
o Find: Direct lookup (fast)
o Union: Update all entries with same id
• Quick-Union:
Represents sets as trees.
o Find: Follow parent pointers to root
o Union: Connect roots
Q5 a
CO-1,5;   [10]
SO-1;
BL-5
********** 6 **********
--- page 7 ---
Explain how collisions are resolved using linear probing and quadratic
probing in open addressing. Analyze the issue of primary clustering in linear
probing and discuss how quadratic probing reduces its impact on
performance.
Q5 b
CO-5;   [10]
SO-1;
BL-2
Describe asymptotic notations and their role in analysing algorithm
efficiency.
Also Determine the order of growth of the function:
f(n) = 6n⁴ + 3n³ log n + 8n² + 12n + 5
Asymptotic Notations describe how an algorithm’s running time grows
Q6 a
with input size nnn.
CO-1;   [10]
SO-1,2;   • Big-O (O): Upper bound (worst-case growth)
BL-2   • Omega (Ω): Lower bound (best-case growth)
• Theta (Θ): Tight bound (exact growth rate)
Role:
• Helps compare algorithms independent of hardware
• Focuses on dominant terms for large inputs
•   Predicts scalability and performance
********** 7 **********
--- page 8 ---
Outline the applications of priority queues in real-world problems such as
scheduling and shortest path algorithms. Apply heap-based implementations
to illustrate how they improve the efficiency of priority queue operations
compared to simple array-based implementations, with suitable reasoning.
(3 Marks) Applications of Priority Queue
Priority queues are used where elements are processed based on priority
rather than arrival order.
Q6 b
•   Scheduling: CPU/process scheduling, printer job management
CO-2;   •   Shortest Path Algorithms: Dijkstra’s Algorithm uses it to select the   [10]
SO-1;   minimum-distance node
BL-2,3   •   Event-driven simulation and network routing
(3 Marks) Heap-Based Implementation
A Binary Heap is commonly used.
•   Insert → place at end + sift-up
•   Delete highest priority → remove root + sift-down
• Peek → root element
This maintains the heap property.
4 marks (example)
Analyze the Quick Sort algorithm. Derive its best, average, and worst-case
time complexities based on pivot selection.
Q7 a
CO-4;   [10]
SO-1;
BL-2
********** 8 **********
--- page 9 ---
i. Why does the time complexity of BST operations become O(n) in
the worst case? Explain with reason.
(2 Marks) Concept of Binary Search Tree
In a BST, operations like search, insert, and delete depend on the height of
the tree (h).
• Time complexity = O(h)
(2 Marks) Reason for Worst Case O(n)
• When elements are inserted in sorted order, the BST becomes skewed
•   Structure degenerates into a linear chain (like a linked list)
Q7 b
Example:
CO-2,3,5;   [5+5]
SO-1;   1
BL-3,2   \
2
\
3
\
4
•   Height becomes n instead of log n
•   Every operation may traverse all nodes
👉 Time Complexity = O(n)
(1 Mark) Conclusion
BST becomes inefficient in the worst case due to loss of balance, which
increases height and degrades performance from O(log n) to O(n).
********** 9 **********
--- page 10 ---
ii. | Compare and contrast the separate chaining and linear probing.

Feature Separate Chaining Linear Probing

Storage Linked list at each index Stores all elements in array

Collision handling Add to chain (list) Search next empty slot
Memory Extra memory required No extra memory
Qlustering No primary clustering Suffers from primary clustering

FRR ICR 7 OI HOH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 922bb1ff1e34

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_DS_7009/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: mixed (10 pages), mean OCR confidence 85.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:
Design and implement a Stack using an array. The program should support
the following operations:
CO-1,2;   i. Push , Pop
SO- 1;   a.   [5]
ii. Display
BL- 3
(Practical)
Can be done in any language
CO-1,5;   Describe how Interval Trees are used to identify overlapping intervals.
SO-1;   b.   [5]
Explain the working principle and analyze the time complexity.
BL-2
********** 1 **********
--- page 2 ---
Compare the Master Theorem and the recursion tree method for solving
recurrence relations. When is each method preferred?
CO-1;
SO-1,2;   c.   [5]
BL-4
Explain why Heap Sort is considered an unstable sorting algorithm. Support
your answer with reasoning.
Heap Sort is considered unstable because it does not preserve the relative
order of equal elements during sorting.
CO-4;   Reasoning:
SO-1;   d.   [5]
Heap Sort repeatedly swaps the root (maximum element) with the last
BL-2
element in the heap.
During heapify (sift-down), elements may move across different levels of
the tree.
These operations do not track or preserve the original order of equal keys.
Q2 a   Explain Kruskal’s Algorithm for constructing a Minimum Spanning Tree in
CO-1,5;   a weighted graph. Analyze the role of the Union–Find in detecting cycles [10]
SO-1,2;
during the execution of the algorithm.
BL-2,4
********** 2 **********
--- page 3 ---
Construct a Red-Black Tree for the keys [10, 20, 30, 15, 25, 5, 1].
Demonstrate all rotations and color adjustments during insertion, and justify
how each step satisfies the five properties of a Red-Black Tree and maintains
balance after updates.
Q2 b
CO-5;   [10]
SO-1;
BL-6
Five Properties (Justification)
1. Every node is either RED or BLACK ✔
2. Root is BLACK → 20(B) ✔
3. No two consecutive RED nodes ✔
********** 3 **********
--- page 4 ---
4. Every path has same number of BLACK nodes ✔
5. All NULL leaves are BLACK ✔
Role of Rotations
•   Left rotation (at 10) balanced the tree when inserting 30
•   Rotations help:
o Maintain BST structure
o Reduce tree height
o Fix RED–RED violations
Implement a queue using both an array and a linked list. Demonstrate
Q3 a   enqueue and dequeue operations for both representations and show the state
CO-2,4;   of the queue after each operation.   [10]
SO-1;
(practical)
BL-3
Can be done in any language
Construct a Binary Search Tree (BST) using the keys 45, 25, 65, 15, 35, 55,
75 in the given order and draw the resulting tree. Find its height and perform
a search for the key 35 by tracing the path. Also, state the effect on the BST
structure and search complexity if the keys are inserted in sorted order.
Q3 b
CO-3;   [10]
SO-1;
BL-2
Q4 a
A sparse vector of size 15 is given as:
CO-5;   V = [0, 0, 5, 0, 0, 9, 0, 0, 0, 12, 0, 0, 3, 0, 0]   [10]
SO-1;
BL-4
********** 4 **********
--- page 5 ---
Design a hash table representation for this sparse vector using the hash
function h(i) = i mod 7, where i is the index.
•   Insert all non-zero elements into the hash table (store index, value
pairs).
• Show the final hash table.
• Demonstrate how to retrieve the value at index 9 and 4.
Insert keys 3, 7, 1, 5, 9, 2, 8 one by one into an empty 2-3 tree.
• Draw the tree after every insertion and show all splits and
Q4 b
promotions clearly.
CO-5;   [10]
SO-1;   • On the final 2-3 tree from above, perform an in-order traversal and
BL-3
compute: floor (4), ceiling (6), rank (7), and select (4).
(5 Marks) Construction of 2-3 Tree
********** 5 **********
--- page 6 ---
(1 Marks) In-order Traversal
1, 2, 3, 5, 7, 8, 9
(4 Marks) Computations
•   floor(4) → 3
•   ceiling(6) → 7
•   rank(7) → 4 (elements < 7)
•   select(4) → 5 (4th smallest)
Discuss Quick-Find and Quick-Union algorithms for Disjoint Set
operations.Analyze and compare their time complexities for large datasets.
Explain why Quick-Find becomes inefficient compared to Quick-Union.
(3 Marks) Concepts
• Quick-Find:
Maintains an array where each element stores its set id.
o Find: Direct lookup (fast)
o Union: Update all entries with same id
• Quick-Union:
Represents sets as trees.
o Find: Follow parent pointers to root
o Union: Connect roots
Q5 a
CO-1,5;   [10]
SO-1;
BL-5
********** 6 **********
--- page 7 ---
Explain how collisions are resolved using linear probing and quadratic
probing in open addressing. Analyze the issue of primary clustering in linear
probing and discuss how quadratic probing reduces its impact on
performance.
Q5 b
CO-5;   [10]
SO-1;
BL-2
Describe asymptotic notations and their role in analysing algorithm
efficiency.
Also Determine the order of growth of the function:
f(n) = 6n⁴ + 3n³ log n + 8n² + 12n + 5
Asymptotic Notations describe how an algorithm’s running time grows
Q6 a
with input size nnn.
CO-1;   [10]
SO-1,2;   • Big-O (O): Upper bound (worst-case growth)
BL-2   • Omega (Ω): Lower bound (best-case growth)
• Theta (Θ): Tight bound (exact growth rate)
Role:
• Helps compare algorithms independent of hardware
• Focuses on dominant terms for large inputs
•   Predicts scalability and performance
********** 7 **********
--- page 8 ---
Outline the applications of priority queues in real-world problems such as
scheduling and shortest path algorithms. Apply heap-based implementations
to illustrate how they improve the efficiency of priority queue operations
compared to simple array-based implementations, with suitable reasoning.
(3 Marks) Applications of Priority Queue
Priority queues are used where elements are processed based on priority
rather than arrival order.
Q6 b
•   Scheduling: CPU/process scheduling, printer job management
CO-2;   •   Shortest Path Algorithms: Dijkstra’s Algorithm uses it to select the   [10]
SO-1;   minimum-distance node
BL-2,3   •   Event-driven simulation and network routing
(3 Marks) Heap-Based Implementation
A Binary Heap is commonly used.
•   Insert → place at end + sift-up
•   Delete highest priority → remove root + sift-down
• Peek → root element
This maintains the heap property.
4 marks (example)
Analyze the Quick Sort algorithm. Derive its best, average, and worst-case
time complexities based on pivot selection.
Q7 a
CO-4;   [10]
SO-1;
BL-2
********** 8 **********
--- page 9 ---
i. Why does the time complexity of BST operations become O(n) in
the worst case? Explain with reason.
(2 Marks) Concept of Binary Search Tree
In a BST, operations like search, insert, and delete depend on the height of
the tree (h).
• Time complexity = O(h)
(2 Marks) Reason for Worst Case O(n)
• When elements are inserted in sorted order, the BST becomes skewed
•   Structure degenerates into a linear chain (like a linked list)
Q7 b
Example:
CO-2,3,5;   [5+5]
SO-1;   1
BL-3,2   \
2
\
3
\
4
•   Height becomes n instead of log n
•   Every operation may traverse all nodes
👉 Time Complexity = O(n)
(1 Mark) Conclusion
BST becomes inefficient in the worst case due to loss of balance, which
increases height and degrades performance from O(log n) to O(n).
********** 9 **********
--- page 10 ---
ii. | Compare and contrast the separate chaining and linear probing.

Feature Separate Chaining Linear Probing

Storage Linked list at each index Stores all elements in array

Collision handling Add to chain (list) Search next empty slot
Memory Extra memory required No extra memory
Qlustering No primary clustering Suffers from primary clustering

FRR ICR 7 OI HOH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 477c7f32ac60

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_DS_7052/Advance Data Structure for Analytics/ANS_Advance Data Structure for Analytics(702DB0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: mixed (10 pages), mean OCR confidence 85.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Advance Data Structure for Analytics
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks.
6. Q1(a) and Q3(a) are lab based questions which are to be done on computer and write code in answer
sheets.Implemention can be done in C++/Java/Python language
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1
Answer briefly:
Design and implement a Stack using an array. The program should support
the following operations:
CO-1,2;   i. Push , Pop
SO- 1;   a.   [5]
ii. Display
BL- 3
(Practical)
Can be done in any language
CO-1,5;   Describe how Interval Trees are used to identify overlapping intervals.
SO-1;   b.   [5]
Explain the working principle and analyze the time complexity.
BL-2
********** 1 **********
--- page 2 ---
Compare the Master Theorem and the recursion tree method for solving
recurrence relations. When is each method preferred?
CO-1;
SO-1,2;   c.   [5]
BL-4
Explain why Heap Sort is considered an unstable sorting algorithm. Support
your answer with reasoning.
Heap Sort is considered unstable because it does not preserve the relative
order of equal elements during sorting.
CO-4;   Reasoning:
SO-1;   d.   [5]
Heap Sort repeatedly swaps the root (maximum element) with the last
BL-2
element in the heap.
During heapify (sift-down), elements may move across different levels of
the tree.
These operations do not track or preserve the original order of equal keys.
Q2 a   Explain Kruskal’s Algorithm for constructing a Minimum Spanning Tree in
CO-1,5;   a weighted graph. Analyze the role of the Union–Find in detecting cycles [10]
SO-1,2;
during the execution of the algorithm.
BL-2,4
********** 2 **********
--- page 3 ---
Construct a Red-Black Tree for the keys [10, 20, 30, 15, 25, 5, 1].
Demonstrate all rotations and color adjustments during insertion, and justify
how each step satisfies the five properties of a Red-Black Tree and maintains
balance after updates.
Q2 b
CO-5;   [10]
SO-1;
BL-6
Five Properties (Justification)
1. Every node is either RED or BLACK ✔
2. Root is BLACK → 20(B) ✔
3. No two consecutive RED nodes ✔
********** 3 **********
--- page 4 ---
4. Every path has same number of BLACK nodes ✔
5. All NULL leaves are BLACK ✔
Role of Rotations
•   Left rotation (at 10) balanced the tree when inserting 30
•   Rotations help:
o Maintain BST structure
o Reduce tree height
o Fix RED–RED violations
Implement a queue using both an array and a linked list. Demonstrate
Q3 a   enqueue and dequeue operations for both representations and show the state
CO-2,4;   of the queue after each operation.   [10]
SO-1;
(practical)
BL-3
Can be done in any language
Construct a Binary Search Tree (BST) using the keys 45, 25, 65, 15, 35, 55,
75 in the given order and draw the resulting tree. Find its height and perform
a search for the key 35 by tracing the path. Also, state the effect on the BST
structure and search complexity if the keys are inserted in sorted order.
Q3 b
CO-3;   [10]
SO-1;
BL-2
Q4 a
A sparse vector of size 15 is given as:
CO-5;   V = [0, 0, 5, 0, 0, 9, 0, 0, 0, 12, 0, 0, 3, 0, 0]   [10]
SO-1;
BL-4
********** 4 **********
--- page 5 ---
Design a hash table representation for this sparse vector using the hash
function h(i) = i mod 7, where i is the index.
•   Insert all non-zero elements into the hash table (store index, value
pairs).
• Show the final hash table.
• Demonstrate how to retrieve the value at index 9 and 4.
Insert keys 3, 7, 1, 5, 9, 2, 8 one by one into an empty 2-3 tree.
• Draw the tree after every insertion and show all splits and
Q4 b
promotions clearly.
CO-5;   [10]
SO-1;   • On the final 2-3 tree from above, perform an in-order traversal and
BL-3
compute: floor (4), ceiling (6), rank (7), and select (4).
(5 Marks) Construction of 2-3 Tree
********** 5 **********
--- page 6 ---
(1 Marks) In-order Traversal
1, 2, 3, 5, 7, 8, 9
(4 Marks) Computations
•   floor(4) → 3
•   ceiling(6) → 7
•   rank(7) → 4 (elements < 7)
•   select(4) → 5 (4th smallest)
Discuss Quick-Find and Quick-Union algorithms for Disjoint Set
operations.Analyze and compare their time complexities for large datasets.
Explain why Quick-Find becomes inefficient compared to Quick-Union.
(3 Marks) Concepts
• Quick-Find:
Maintains an array where each element stores its set id.
o Find: Direct lookup (fast)
o Union: Update all entries with same id
• Quick-Union:
Represents sets as trees.
o Find: Follow parent pointers to root
o Union: Connect roots
Q5 a
CO-1,5;   [10]
SO-1;
BL-5
********** 6 **********
--- page 7 ---
Explain how collisions are resolved using linear probing and quadratic
probing in open addressing. Analyze the issue of primary clustering in linear
probing and discuss how quadratic probing reduces its impact on
performance.
Q5 b
CO-5;   [10]
SO-1;
BL-2
Describe asymptotic notations and their role in analysing algorithm
efficiency.
Also Determine the order of growth of the function:
f(n) = 6n⁴ + 3n³ log n + 8n² + 12n + 5
Asymptotic Notations describe how an algorithm’s running time grows
Q6 a
with input size nnn.
CO-1;   [10]
SO-1,2;   • Big-O (O): Upper bound (worst-case growth)
BL-2   • Omega (Ω): Lower bound (best-case growth)
• Theta (Θ): Tight bound (exact growth rate)
Role:
• Helps compare algorithms independent of hardware
• Focuses on dominant terms for large inputs
•   Predicts scalability and performance
********** 7 **********
--- page 8 ---
Outline the applications of priority queues in real-world problems such as
scheduling and shortest path algorithms. Apply heap-based implementations
to illustrate how they improve the efficiency of priority queue operations
compared to simple array-based implementations, with suitable reasoning.
(3 Marks) Applications of Priority Queue
Priority queues are used where elements are processed based on priority
rather than arrival order.
Q6 b
•   Scheduling: CPU/process scheduling, printer job management
CO-2;   •   Shortest Path Algorithms: Dijkstra’s Algorithm uses it to select the   [10]
SO-1;   minimum-distance node
BL-2,3   •   Event-driven simulation and network routing
(3 Marks) Heap-Based Implementation
A Binary Heap is commonly used.
•   Insert → place at end + sift-up
•   Delete highest priority → remove root + sift-down
• Peek → root element
This maintains the heap property.
4 marks (example)
Analyze the Quick Sort algorithm. Derive its best, average, and worst-case
time complexities based on pivot selection.
Q7 a
CO-4;   [10]
SO-1;
BL-2
********** 8 **********
--- page 9 ---
i. Why does the time complexity of BST operations become O(n) in
the worst case? Explain with reason.
(2 Marks) Concept of Binary Search Tree
In a BST, operations like search, insert, and delete depend on the height of
the tree (h).
• Time complexity = O(h)
(2 Marks) Reason for Worst Case O(n)
• When elements are inserted in sorted order, the BST becomes skewed
•   Structure degenerates into a linear chain (like a linked list)
Q7 b
Example:
CO-2,3,5;   [5+5]
SO-1;   1
BL-3,2   \
2
\
3
\
4
•   Height becomes n instead of log n
•   Every operation may traverse all nodes
👉 Time Complexity = O(n)
(1 Mark) Conclusion
BST becomes inefficient in the worst case due to loss of balance, which
increases height and degrades performance from O(log n) to O(n).
********** 9 **********
--- page 10 ---
ii. | Compare and contrast the separate chaining and linear probing.

Feature Separate Chaining Linear Probing

Storage Linked list at each index Stores all elements in array

Collision handling Add to chain (list) Search next empty slot
Memory Extra memory required No extra memory
Qlustering No primary clustering Suffers from primary clustering

FRR ICR 7 OI HOH
````
