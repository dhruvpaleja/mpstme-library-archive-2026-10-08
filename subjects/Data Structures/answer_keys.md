# Data Structures: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper c0c1681c3d38

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/DATA STRUCTURES/ANS_DATA STRUCTURES(701CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: DATA STRUCTURES
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions.
6. Write algorithms in the proper format, including input, output, and step-by-step instructions wherever
applicable.
7. Provide clear and concise pseudocode wherever applicable.
8. Include diagrams wherever applicable to illustrate data structures or processes clearly.
Q1   Answer briefly:   [20]
Question
Provide a detailed explanation of what an algorithm is, and thoroughly
discuss its main characteristics and key features.
Synoptic:
Definition:
An algorithm is a finite sequence of well-defined steps or instructions
used to solve a computational problem.
Purpose:
Provides a logical and systematic approach to process data and obtain
results efficiently.
a.   [5]
Key Characteristics / Features:
•   Input: Receives zero or more inputs.
• Output: Produces at least one output.
•   Definiteness: Each step must be clearly and unambiguously
defined.
•   Finiteness: Must terminate after a finite number of steps.
•   Effectiveness:Each operation must be simple enough to be
executed within finite time.
********** 1 **********
--- page 2 ---
Importance:
• Foundation of computational logic and data processing.
•   Ensures correctness, efficiency, and predictability in problem-
solving.
• Used in data structure operations (searching, sorting,
traversal, etc.).
[5]
Question
Explain the difference between linear and non-linear data structures.
Provide examples of each.
Synoptics
Linear Data Structures
• Data elements are arranged sequentially, one after another.
• Each element is connected to its previous and next element.
• Data is accessed in order — from start to end or end to start.
• Memory allocation may be contiguous (as in arrays) or linked
(as in linked lists).
b.   •   Suitable for simple, ordered data storage and processing.
• Examples: Array, Linked List, Stack, Queue.
Non-Linear Data Structures
• Data elements are not arranged in sequence.
• They form hierarchical or network relationships.
• A single element may be connected to multiple elements.
• Accessing elements often requires traversal algorithms like
DFS (Depth First Search) or BFS (Breadth First Search).
• Used to represent complex relationships such as hierarchies,
networks, or graphs.
• Examples: Tree, Graph.
Question   [5]
Write the linear search algorithm in detail and explain its best, worst,
and average case scenarios
Synoptic
•   Linear Search is the simplest searching algorithm that
c.   sequentially checks each element of a list or array until the
desired element (key) is found or the end of the list is
reached.
• Step-by-Step Algorithm
o Set i = 0
o Repeat steps 3–5 while i < n
o   If arr[i] == key, then
▪ → Print “Element found at position i”
********** 2 **********
--- page 3 ---
▪ → Exit
o Otherwise, increment i = i + 1
o   If end of array is reached (i == n), print “Element not
found”
• C Code Example (Optional)
int linearSearch(int arr[], int n, int key) {
for (int i = 0; i < n; i++) {
if (arr[i] == key)
return i;   // Element found, return index
}
return -1; // Element not found
}
• Time Complexity Analysis
o Best Case: Key is at the first position, O(1)
o Average Case: Key is somewhere in the middle,
O(n)
o Worst Case: Key is at the end or not present, O(n)
Question   [5]
Differentiate between a linear queue and a circular queue.
Synoptic
•   In a Linear Queue, elements are arranged in a straight line.
In a Circular Queue, the last position is connected back to
the first position.
•   Linear Queue follows the FIFO rule but wastes space when
elements are deleted.
Circular Queue also follows FIFO but reuses the freed space
efficiently.
•   In a Linear Queue, overflow occurs when rear == size - 1.
d.
In a Circular Queue, overflow occurs when (rear + 1) % size
== front.
•   Linear Queue does not reuse deleted spaces.
Circular Queue reuses deleted spaces.
•   Linear Queue may require shifting of elements after deletion.
Circular Queue never requires shifting.
•   Linear Queue is less efficient in memory utilization.
Circular Queue is more efficient in memory utilization.
•   In Linear Queue, front and rear move only in one direction.
********** 3 **********
--- page 4 ---
In Circular Queue, front and rear move circularly using
modulo operation.
•   Linear Queue is easier to implement but less space-efficient.
Circular Queue is slightly complex but makes better use of
space.
•   Linear Queue is used in simple data handling (like waiting
lines).
Circular Queue is used in CPU scheduling, printer queues,
and buffering.
•   In Linear Queue, after several deletions, even if space is
available, new elements cannot be added without resetting.
In Circular Queue, new elements can be added as freed
spaces are reused.
Q2   [20]
Question
Explain the concept of a stack and the role of the 'top' pointer.
Describe the conditions of stack underflow and overflow, and
illustrate with a real-life example
Synoptic:
•   Stack:
o A linear data structure that follows the LIFO (Last
In, First Out) principle.
o The last inserted element is the first one to be
removed.
• Role of ‘TOP’ Pointer   [10]
o Points to the position of the last inserted element in
the stack.
o Used to manage insertion (push) and deletion (pop)
operations.
o Updated after every operation.
• Stack Overflow
o Occurs when trying to push an element into a full
stack (TOP == MAX - 1).
o The program exceeds available memory space for the
stack.
• Stack Underflow
o Occurs when trying to pop an element from an empty
stack (TOP == -1).
o No element exists to remove.
•   Real-life Examples
********** 4 **********
--- page 5 ---
o Stack of plates: Last plate placed is the first to be
removed.
o Undo/Redo in text editors.
o Browser Back Button navigation history.
Question
Write the algorithm and corresponding C code for performing push
and pop operations on a stack
Synoptic:
• Push Operation: To insert a new element at the top of the
stack.
o Algorithm:
▪   If TOP == MAX - 1 → Overflow → display
message.
▪   Else increment TOP.
▪   Insert the new element into stack[TOP].
o Key Points:
▪   Insertion allowed only at one end (TOP).
▪ Must check overflow before inserting.
o C Code:
void push(int val) {
if (top == MAX - 1)
printf("Stack Overflow\n");
else {
top++;   [10]
stack[top] = val;
printf("%d pushed\n", val);
}
}
• Pop Operation: To remove and return the top element of the
stack.
o Algorithm:
▪   If TOP == -1 → Underflow → display
message.
▪   Else, store stack[TOP] in a variable.
▪ Decrement TOP.
▪ Return the removed element.
o Key Points:
▪   Deletion allowed only from the TOP.
▪ Must check underflow before popping.
o C Code:
void pop() {
if (top == -1)
printf("Stack Underflow\n");
else {
********** 5 **********
--- page 6 ---
printf("Popped element = %d\n",
stack[top]);
top--;
}
}
Q3   [20]
Question
Explain the concept of a queue, its characteristics, and the different
types of queues
Synoptics
• Queue: A queue is a linear data structure that stores
elements in a sequential order, where:
o   Insertion happens at the rear (enqueue).
o Deletion happens at the front (dequeue).
o   It follows the FIFO (First In, First Out) principle.
• Example (Real Life):A line of people waiting at a ticket
counter — the first person in line is the first to be served.
•   Characteristics
o Linear structure with sequential data organization.
o Two pointers:
▪   Front → points to the first element (for
deletion).
▪ Rear → points to the last element (for
insertion).
o Can be bounded (fixed-size array) or dynamic
(linked list).
o Queue becomes:
▪ Empty when all elements are removed.
▪   Full when it reaches maximum capacity.
• Types of Queues
o Linear Queue: Insertion at rear, deletion at front
(FIFO).
o Circular Queue: Last position connects back to
first, enabling reuse of freed space.
o Double-Ended Queue (Deque): Insertion and
deletion allowed at both ends.
o Priority Queue: Each element has a priority; higher
priority dequeued first.
Question
Write the algorithm and corresponding C code for performing
enqueue and dequeue operations in a linear queue.
[10]
Synoptics
• Enqueue Algorithm (Insert at Rear)
********** 6 **********
--- page 7 ---
o Check if queue is full → if (rear == size - 1) →
Overflow.
o   If empty → set front = 0.
o Increment rear++.
o   Insert element at queue[rear].
• Dequeue Algorithm (Delete from Front)
o Check if empty → if (front == -1 || front > rear) →
Underflow.
o Remove element at queue[front].
o Increment front++.
o   If front > rear, reset both to -1.
• Code
#define SIZE 5
int Q[SIZE];
int front = -1, rear = -1;
void enqueue(int item) {
if (rear == SIZE - 1)
printf("Queue Overflow\n");
else {
if (front == -1)
front = 0;
rear++;
Q[rear] = item;
printf("%d inserted into queue\n", item);
}
}
void dequeue() {
if (front == -1 || front > rear)
printf("Queue Underflow\n");
else {
printf("%d deleted from queue\n", Q[front]);
front++;
if (front > rear)
front = rear = -1;
}
}
Q4   [20]
Question
Explain what a sorting algorithm is, why sorting is needed, and the
key factors used in evaluating a sorting algorithm.   [10]
Synoptics
********** 7 **********
--- page 8 ---
• A sorting algorithm is a method used to arrange data
elements (numbers, strings, etc.) in a specific order —
usually ascending or descending.
• Why Sorting is Needed
o Faster Searching: Algorithms like Binary Search
require sorted data.
o Better Organization: Easier to read, analyze, and
interpret data.
o Efficiency in Algorithms: Many algorithms depend
on pre-sorted input for optimal performance.
• Key Factors for Evaluating Sorting Algorithms
o Time Complexity
▪ Measures execution time growth with input
size (n).
▪   Best Case: Ideal condition (e.g., already
sorted).
▪ Average Case: Expected performance on
random data.
▪ Worst Case: Completely unsorted or reverse
order data.
o Space Complexity
▪ Measures extra memory used besides input
data.
▪   In-place Algorithms: Use little or no extra
memory.
▪ Non–In-place Algorithms: Require extra
storage space.
Question
Write the step-by-step algorithm for Bubble Sort and explain its time
complexity with an example
Synoptics
• Bubble Sort repeatedly compares adjacent elements and
swaps them if they are in the wrong order. The largest
elements "bubble up" to the end after each pass.
• Algorithm (Step-by-Step)
o Repeat (n – 1) times:
o For each pair of adjacent elements (arr[j], arr[j+1]):   [10]
▪   If arr[j] > arr[j+1], swap them.
o After each pass, the largest element moves to its
correct position.
• Example: Array: {5, 1, 4, 2, 8}
o Pass 1: {1, 4, 2, 5, 8}
o Pass 2: {1, 2, 4, 5, 8}
o Pass 3: No swaps → Array sorted.
o ✅ Final Sorted Array: {1, 2, 4, 5, 8}
• Time Complexity
o Best: Already sorted, O(n)
********** 8 **********
--- page 9 ---
o Average: Random order, O(n²)
o Worst: Reverse order ,O(n²)
Q5   [20]
Question
Explain the functions malloc() and calloc() in C, highlighting their
differences and usage with examples.
Synoptics
•   malloc() Function
o malloc stands for Memory Allocation.
o   It allocates a single continuous block of memory of a
given size.
o Syntax: ptr = (type*) malloc(size_in_bytes);
o Explanation:
▪   size_in_bytes: total number of bytes to
allocate.
▪   Returns a void pointer (void*), so typecasting
is required.
▪ Memory is uninitialized — contains garbage
values.
[10]
•   calloc() Function
o calloc stands for Contiguous Allocation.
o   It allocates memory for multiple elements, each of the
same size.
o Syntax: ptr = (type*) calloc(num, size);
o Explanation:
▪ num: number of elements.
▪   size: size of each element in bytes.
▪   Allocates num * size bytes in total.
▪   Initializes all bytes to 0.
• Key Differences
o malloc() leaves memory uninitialized (contains
garbage values).
o   calloc() initializes all allocated bytes to zero (0x00)
o Both return a void pointer that must be typecast to the
desired pointer type.
o   If allocation fails, both functions return NULL.
Question
Explain, with proper steps and examples, how to delete a node in a
linked list at the beginning, at the end, and at a specific position
[10]
Synoptics
• Types of Deletion:
o From Beginning:
▪   Store head in temp.
********** 9 **********
--- page 10 ---
▪ Update head = head->next.
▪   Free(temp).
o From End:
▪   Traverse to second-last node.
▪   Free last node.
▪   Set secondLast->next = NULL.
o From Specific Position:
▪   Traverse to (position - 1) node.
▪   Store pointer to node to delete.
▪ Update links: prev->next = temp->next.
▪   Free(temp).
Q6   [20]
Question
Explain the concept of a 2D array, including its declaration, example
and the various operations performed on it, in detail
Synoptics
• A 2D array is like a table (matrix) with rows and columns.
• Each element is identified by two indices: [i][j]
• Example: marks[0][1] → 1st row, 2nd column
[10]
•   Declaration: data_type array_name[rows][columns];
• Example: int studentMarks[10][3];
•   Initialization: int marks[2][3] = { {85, 90, 78}, {92, 88,
76} };
• Common Operations
o Traversal: Access each element using nested loops.
o   Insertion / Update: Assign a value to a specific [i][j].
o Deletion: Not possible directly; overwrite with a new
value.
Question
Explain how a one-dimensional array is stored in memory and derive
the formula for calculating the address of an element with an
example.
Synoptics
• 1D arrays are stored in contiguous memory locations.
• The array name itself is a pointer to the first element.
[10]
• Example: int arr[5] = {10, 20, 30, 40, 50};
•   If int = 4 bytes → memory addresses differ by 4.
• Address Calculation Formula
o Address(arr[i]) = Base_Address + (i ×
size_of_each_element)
•   If base address (BA) = 1000 and sizeof(int) = 4 →
Address of arr[2] = 1000 + (2 × 4) = 1008
********** 10 **********
--- page 11 ---
Q7   [20]
Case Study Analysis
Question
•   Explain the application of arrays in modern software development,
providing suitable real-world examples. Discuss any two cases
where arrays are preferred
•   Explain the application of linked lists in modern software
development, providing suitable real-world examples. Discuss any
two cases where linked lists are preferred
Synoptics
•   Applications of Arrays
o Arrays are widely used in modern applications for:
o Image processing and graphics
o Audio/video data handling
o Machine learning and AI (tensors)
o Database indexing and search operations
o   Scientific computing and simulations
o Example 1 – Image Processing & Graphics
▪ Every image is represented as a 2D array (matrix) of
pixel values.
▪ Each element corresponds to a pixel’s intensity or
color (e.g., RGB).
▪ Used In: Photoshop, Instagram filters, medical
imaging software.
▪ Why Array?
• Contiguous storage allows fast access and
updates to pixels.
•   Supports matrix operations like rotation,
scaling, and filtering.
o Example 2 – Machine Learning and AI
▪   Arrays form the base for tensors in frameworks like
NumPy, TensorFlow, and PyTorch.
▪ Used to store datasets, parameters, and activations in
neural networks.
▪ Used In: ChatGPT, face recognition, self-driving car
systems.
▪ Why Array?
•   Enables parallel computations on GPUs.
•   Applications of Linked Lists
o Linked lists are commonly used in:
o Music/video playlist navigation
o Navigation and mapping systems
o Memory management in operating systems
o Blockchain and distributed ledger systems
o Undo/redo operations in editors
o Example 1 – Music or Video Playlists
▪ Each song or video is a node connected to the next
via pointers.
********** 11 **********
--- page 12 ---
▪ “Next” and “Previous” buttons move through the list
dynamically.
▪ Used In: Spotify, YouTube, VLC Media Player.
▪ Why Linked List?
• Allows easy insertion, deletion, or
rearranging of songs.
•   Enables continuous playback and dynamic
playlist updates.
• Example 2 – Navigation and Maps
o Each location or stop is a node connected to the next in a
route.
o Used In: Google Maps, Uber route planning.
o Why Linked List?
▪ Routes can be modified dynamically (add/remove
waypoints).
▪   Efficient for sequential traversal of path data.
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper f76bd549effb

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/DATA STRUCTURES/ANS_DATA STRUCTURES(701CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: DATA STRUCTURES
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions.
6. Write algorithms in the proper format, including input, output, and step-by-step instructions wherever
applicable.
7. Provide clear and concise pseudocode wherever applicable.
8. Include diagrams wherever applicable to illustrate data structures or processes clearly.
Q1   Answer briefly:   [20]
Question
Provide a detailed explanation of what an algorithm is, and thoroughly
discuss its main characteristics and key features.
Synoptic:
Definition:
An algorithm is a finite sequence of well-defined steps or instructions
used to solve a computational problem.
Purpose:
Provides a logical and systematic approach to process data and obtain
results efficiently.
a.   [5]
Key Characteristics / Features:
•   Input: Receives zero or more inputs.
• Output: Produces at least one output.
•   Definiteness: Each step must be clearly and unambiguously
defined.
•   Finiteness: Must terminate after a finite number of steps.
•   Effectiveness:Each operation must be simple enough to be
executed within finite time.
********** 1 **********
--- page 2 ---
Importance:
• Foundation of computational logic and data processing.
•   Ensures correctness, efficiency, and predictability in problem-
solving.
• Used in data structure operations (searching, sorting,
traversal, etc.).
[5]
Question
Explain the difference between linear and non-linear data structures.
Provide examples of each.
Synoptics
Linear Data Structures
• Data elements are arranged sequentially, one after another.
• Each element is connected to its previous and next element.
• Data is accessed in order — from start to end or end to start.
• Memory allocation may be contiguous (as in arrays) or linked
(as in linked lists).
b.   •   Suitable for simple, ordered data storage and processing.
• Examples: Array, Linked List, Stack, Queue.
Non-Linear Data Structures
• Data elements are not arranged in sequence.
• They form hierarchical or network relationships.
• A single element may be connected to multiple elements.
• Accessing elements often requires traversal algorithms like
DFS (Depth First Search) or BFS (Breadth First Search).
• Used to represent complex relationships such as hierarchies,
networks, or graphs.
• Examples: Tree, Graph.
Question   [5]
Write the linear search algorithm in detail and explain its best, worst,
and average case scenarios
Synoptic
•   Linear Search is the simplest searching algorithm that
c.   sequentially checks each element of a list or array until the
desired element (key) is found or the end of the list is
reached.
• Step-by-Step Algorithm
o Set i = 0
o Repeat steps 3–5 while i < n
o   If arr[i] == key, then
▪ → Print “Element found at position i”
********** 2 **********
--- page 3 ---
▪ → Exit
o Otherwise, increment i = i + 1
o   If end of array is reached (i == n), print “Element not
found”
• C Code Example (Optional)
int linearSearch(int arr[], int n, int key) {
for (int i = 0; i < n; i++) {
if (arr[i] == key)
return i;   // Element found, return index
}
return -1; // Element not found
}
• Time Complexity Analysis
o Best Case: Key is at the first position, O(1)
o Average Case: Key is somewhere in the middle,
O(n)
o Worst Case: Key is at the end or not present, O(n)
Question   [5]
Differentiate between a linear queue and a circular queue.
Synoptic
•   In a Linear Queue, elements are arranged in a straight line.
In a Circular Queue, the last position is connected back to
the first position.
•   Linear Queue follows the FIFO rule but wastes space when
elements are deleted.
Circular Queue also follows FIFO but reuses the freed space
efficiently.
•   In a Linear Queue, overflow occurs when rear == size - 1.
d.
In a Circular Queue, overflow occurs when (rear + 1) % size
== front.
•   Linear Queue does not reuse deleted spaces.
Circular Queue reuses deleted spaces.
•   Linear Queue may require shifting of elements after deletion.
Circular Queue never requires shifting.
•   Linear Queue is less efficient in memory utilization.
Circular Queue is more efficient in memory utilization.
•   In Linear Queue, front and rear move only in one direction.
********** 3 **********
--- page 4 ---
In Circular Queue, front and rear move circularly using
modulo operation.
•   Linear Queue is easier to implement but less space-efficient.
Circular Queue is slightly complex but makes better use of
space.
•   Linear Queue is used in simple data handling (like waiting
lines).
Circular Queue is used in CPU scheduling, printer queues,
and buffering.
•   In Linear Queue, after several deletions, even if space is
available, new elements cannot be added without resetting.
In Circular Queue, new elements can be added as freed
spaces are reused.
Q2   [20]
Question
Explain the concept of a stack and the role of the 'top' pointer.
Describe the conditions of stack underflow and overflow, and
illustrate with a real-life example
Synoptic:
•   Stack:
o A linear data structure that follows the LIFO (Last
In, First Out) principle.
o The last inserted element is the first one to be
removed.
• Role of ‘TOP’ Pointer   [10]
o Points to the position of the last inserted element in
the stack.
o Used to manage insertion (push) and deletion (pop)
operations.
o Updated after every operation.
• Stack Overflow
o Occurs when trying to push an element into a full
stack (TOP == MAX - 1).
o The program exceeds available memory space for the
stack.
• Stack Underflow
o Occurs when trying to pop an element from an empty
stack (TOP == -1).
o No element exists to remove.
•   Real-life Examples
********** 4 **********
--- page 5 ---
o Stack of plates: Last plate placed is the first to be
removed.
o Undo/Redo in text editors.
o Browser Back Button navigation history.
Question
Write the algorithm and corresponding C code for performing push
and pop operations on a stack
Synoptic:
• Push Operation: To insert a new element at the top of the
stack.
o Algorithm:
▪   If TOP == MAX - 1 → Overflow → display
message.
▪   Else increment TOP.
▪   Insert the new element into stack[TOP].
o Key Points:
▪   Insertion allowed only at one end (TOP).
▪ Must check overflow before inserting.
o C Code:
void push(int val) {
if (top == MAX - 1)
printf("Stack Overflow\n");
else {
top++;   [10]
stack[top] = val;
printf("%d pushed\n", val);
}
}
• Pop Operation: To remove and return the top element of the
stack.
o Algorithm:
▪   If TOP == -1 → Underflow → display
message.
▪   Else, store stack[TOP] in a variable.
▪ Decrement TOP.
▪ Return the removed element.
o Key Points:
▪   Deletion allowed only from the TOP.
▪ Must check underflow before popping.
o C Code:
void pop() {
if (top == -1)
printf("Stack Underflow\n");
else {
********** 5 **********
--- page 6 ---
printf("Popped element = %d\n",
stack[top]);
top--;
}
}
Q3   [20]
Question
Explain the concept of a queue, its characteristics, and the different
types of queues
Synoptics
• Queue: A queue is a linear data structure that stores
elements in a sequential order, where:
o   Insertion happens at the rear (enqueue).
o Deletion happens at the front (dequeue).
o   It follows the FIFO (First In, First Out) principle.
• Example (Real Life):A line of people waiting at a ticket
counter — the first person in line is the first to be served.
•   Characteristics
o Linear structure with sequential data organization.
o Two pointers:
▪   Front → points to the first element (for
deletion).
▪ Rear → points to the last element (for
insertion).
o Can be bounded (fixed-size array) or dynamic
(linked list).
o Queue becomes:
▪ Empty when all elements are removed.
▪   Full when it reaches maximum capacity.
• Types of Queues
o Linear Queue: Insertion at rear, deletion at front
(FIFO).
o Circular Queue: Last position connects back to
first, enabling reuse of freed space.
o Double-Ended Queue (Deque): Insertion and
deletion allowed at both ends.
o Priority Queue: Each element has a priority; higher
priority dequeued first.
Question
Write the algorithm and corresponding C code for performing
enqueue and dequeue operations in a linear queue.
[10]
Synoptics
• Enqueue Algorithm (Insert at Rear)
********** 6 **********
--- page 7 ---
o Check if queue is full → if (rear == size - 1) →
Overflow.
o   If empty → set front = 0.
o Increment rear++.
o   Insert element at queue[rear].
• Dequeue Algorithm (Delete from Front)
o Check if empty → if (front == -1 || front > rear) →
Underflow.
o Remove element at queue[front].
o Increment front++.
o   If front > rear, reset both to -1.
• Code
#define SIZE 5
int Q[SIZE];
int front = -1, rear = -1;
void enqueue(int item) {
if (rear == SIZE - 1)
printf("Queue Overflow\n");
else {
if (front == -1)
front = 0;
rear++;
Q[rear] = item;
printf("%d inserted into queue\n", item);
}
}
void dequeue() {
if (front == -1 || front > rear)
printf("Queue Underflow\n");
else {
printf("%d deleted from queue\n", Q[front]);
front++;
if (front > rear)
front = rear = -1;
}
}
Q4   [20]
Question
Explain what a sorting algorithm is, why sorting is needed, and the
key factors used in evaluating a sorting algorithm.   [10]
Synoptics
********** 7 **********
--- page 8 ---
• A sorting algorithm is a method used to arrange data
elements (numbers, strings, etc.) in a specific order —
usually ascending or descending.
• Why Sorting is Needed
o Faster Searching: Algorithms like Binary Search
require sorted data.
o Better Organization: Easier to read, analyze, and
interpret data.
o Efficiency in Algorithms: Many algorithms depend
on pre-sorted input for optimal performance.
• Key Factors for Evaluating Sorting Algorithms
o Time Complexity
▪ Measures execution time growth with input
size (n).
▪   Best Case: Ideal condition (e.g., already
sorted).
▪ Average Case: Expected performance on
random data.
▪ Worst Case: Completely unsorted or reverse
order data.
o Space Complexity
▪ Measures extra memory used besides input
data.
▪   In-place Algorithms: Use little or no extra
memory.
▪ Non–In-place Algorithms: Require extra
storage space.
Question
Write the step-by-step algorithm for Bubble Sort and explain its time
complexity with an example
Synoptics
• Bubble Sort repeatedly compares adjacent elements and
swaps them if they are in the wrong order. The largest
elements "bubble up" to the end after each pass.
• Algorithm (Step-by-Step)
o Repeat (n – 1) times:
o For each pair of adjacent elements (arr[j], arr[j+1]):   [10]
▪   If arr[j] > arr[j+1], swap them.
o After each pass, the largest element moves to its
correct position.
• Example: Array: {5, 1, 4, 2, 8}
o Pass 1: {1, 4, 2, 5, 8}
o Pass 2: {1, 2, 4, 5, 8}
o Pass 3: No swaps → Array sorted.
o ✅ Final Sorted Array: {1, 2, 4, 5, 8}
• Time Complexity
o Best: Already sorted, O(n)
********** 8 **********
--- page 9 ---
o Average: Random order, O(n²)
o Worst: Reverse order ,O(n²)
Q5   [20]
Question
Explain the functions malloc() and calloc() in C, highlighting their
differences and usage with examples.
Synoptics
•   malloc() Function
o malloc stands for Memory Allocation.
o   It allocates a single continuous block of memory of a
given size.
o Syntax: ptr = (type*) malloc(size_in_bytes);
o Explanation:
▪   size_in_bytes: total number of bytes to
allocate.
▪   Returns a void pointer (void*), so typecasting
is required.
▪ Memory is uninitialized — contains garbage
values.
[10]
•   calloc() Function
o calloc stands for Contiguous Allocation.
o   It allocates memory for multiple elements, each of the
same size.
o Syntax: ptr = (type*) calloc(num, size);
o Explanation:
▪ num: number of elements.
▪   size: size of each element in bytes.
▪   Allocates num * size bytes in total.
▪   Initializes all bytes to 0.
• Key Differences
o malloc() leaves memory uninitialized (contains
garbage values).
o   calloc() initializes all allocated bytes to zero (0x00)
o Both return a void pointer that must be typecast to the
desired pointer type.
o   If allocation fails, both functions return NULL.
Question
Explain, with proper steps and examples, how to delete a node in a
linked list at the beginning, at the end, and at a specific position
[10]
Synoptics
• Types of Deletion:
o From Beginning:
▪   Store head in temp.
********** 9 **********
--- page 10 ---
▪ Update head = head->next.
▪   Free(temp).
o From End:
▪   Traverse to second-last node.
▪   Free last node.
▪   Set secondLast->next = NULL.
o From Specific Position:
▪   Traverse to (position - 1) node.
▪   Store pointer to node to delete.
▪ Update links: prev->next = temp->next.
▪   Free(temp).
Q6   [20]
Question
Explain the concept of a 2D array, including its declaration, example
and the various operations performed on it, in detail
Synoptics
• A 2D array is like a table (matrix) with rows and columns.
• Each element is identified by two indices: [i][j]
• Example: marks[0][1] → 1st row, 2nd column
[10]
•   Declaration: data_type array_name[rows][columns];
• Example: int studentMarks[10][3];
•   Initialization: int marks[2][3] = { {85, 90, 78}, {92, 88,
76} };
• Common Operations
o Traversal: Access each element using nested loops.
o   Insertion / Update: Assign a value to a specific [i][j].
o Deletion: Not possible directly; overwrite with a new
value.
Question
Explain how a one-dimensional array is stored in memory and derive
the formula for calculating the address of an element with an
example.
Synoptics
• 1D arrays are stored in contiguous memory locations.
• The array name itself is a pointer to the first element.
[10]
• Example: int arr[5] = {10, 20, 30, 40, 50};
•   If int = 4 bytes → memory addresses differ by 4.
• Address Calculation Formula
o Address(arr[i]) = Base_Address + (i ×
size_of_each_element)
•   If base address (BA) = 1000 and sizeof(int) = 4 →
Address of arr[2] = 1000 + (2 × 4) = 1008
********** 10 **********
--- page 11 ---
Q7   [20]
Case Study Analysis
Question
•   Explain the application of arrays in modern software development,
providing suitable real-world examples. Discuss any two cases
where arrays are preferred
•   Explain the application of linked lists in modern software
development, providing suitable real-world examples. Discuss any
two cases where linked lists are preferred
Synoptics
•   Applications of Arrays
o Arrays are widely used in modern applications for:
o Image processing and graphics
o Audio/video data handling
o Machine learning and AI (tensors)
o Database indexing and search operations
o   Scientific computing and simulations
o Example 1 – Image Processing & Graphics
▪ Every image is represented as a 2D array (matrix) of
pixel values.
▪ Each element corresponds to a pixel’s intensity or
color (e.g., RGB).
▪ Used In: Photoshop, Instagram filters, medical
imaging software.
▪ Why Array?
• Contiguous storage allows fast access and
updates to pixels.
•   Supports matrix operations like rotation,
scaling, and filtering.
o Example 2 – Machine Learning and AI
▪   Arrays form the base for tensors in frameworks like
NumPy, TensorFlow, and PyTorch.
▪ Used to store datasets, parameters, and activations in
neural networks.
▪ Used In: ChatGPT, face recognition, self-driving car
systems.
▪ Why Array?
•   Enables parallel computations on GPUs.
•   Applications of Linked Lists
o Linked lists are commonly used in:
o Music/video playlist navigation
o Navigation and mapping systems
o Memory management in operating systems
o Blockchain and distributed ledger systems
o Undo/redo operations in editors
o Example 1 – Music or Video Playlists
▪ Each song or video is a node connected to the next
via pointers.
********** 11 **********
--- page 12 ---
▪ “Next” and “Previous” buttons move through the list
dynamically.
▪ Used In: Spotify, YouTube, VLC Media Player.
▪ Why Linked List?
• Allows easy insertion, deletion, or
rearranging of songs.
•   Enables continuous playback and dynamic
playlist updates.
• Example 2 – Navigation and Maps
o Each location or stop is a node connected to the next in a
route.
o Used In: Google Maps, Uber route planning.
o Why Linked List?
▪ Routes can be modified dynamically (add/remove
waypoints).
▪   Efficient for sequential traversal of path data.
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 687166e8cbc9

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/DATA STRUCTURES/ANS_DATA STRUCTURES(701CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: DATA STRUCTURES
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions.
6. Write algorithms in the proper format, including input, output, and step-by-step instructions wherever
applicable.
7. Provide clear and concise pseudocode wherever applicable.
8. Include diagrams wherever applicable to illustrate data structures or processes clearly.
Q1   Answer briefly:   [20]
Question
Provide a detailed explanation of what an algorithm is, and thoroughly
discuss its main characteristics and key features.
Synoptic:
Definition:
An algorithm is a finite sequence of well-defined steps or instructions
used to solve a computational problem.
Purpose:
Provides a logical and systematic approach to process data and obtain
results efficiently.
a.   [5]
Key Characteristics / Features:
•   Input: Receives zero or more inputs.
• Output: Produces at least one output.
•   Definiteness: Each step must be clearly and unambiguously
defined.
•   Finiteness: Must terminate after a finite number of steps.
•   Effectiveness:Each operation must be simple enough to be
executed within finite time.
********** 1 **********
--- page 2 ---
Importance:
• Foundation of computational logic and data processing.
•   Ensures correctness, efficiency, and predictability in problem-
solving.
• Used in data structure operations (searching, sorting,
traversal, etc.).
[5]
Question
Explain the difference between linear and non-linear data structures.
Provide examples of each.
Synoptics
Linear Data Structures
• Data elements are arranged sequentially, one after another.
• Each element is connected to its previous and next element.
• Data is accessed in order — from start to end or end to start.
• Memory allocation may be contiguous (as in arrays) or linked
(as in linked lists).
b.   •   Suitable for simple, ordered data storage and processing.
• Examples: Array, Linked List, Stack, Queue.
Non-Linear Data Structures
• Data elements are not arranged in sequence.
• They form hierarchical or network relationships.
• A single element may be connected to multiple elements.
• Accessing elements often requires traversal algorithms like
DFS (Depth First Search) or BFS (Breadth First Search).
• Used to represent complex relationships such as hierarchies,
networks, or graphs.
• Examples: Tree, Graph.
Question   [5]
Write the linear search algorithm in detail and explain its best, worst,
and average case scenarios
Synoptic
•   Linear Search is the simplest searching algorithm that
c.   sequentially checks each element of a list or array until the
desired element (key) is found or the end of the list is
reached.
• Step-by-Step Algorithm
o Set i = 0
o Repeat steps 3–5 while i < n
o   If arr[i] == key, then
▪ → Print “Element found at position i”
********** 2 **********
--- page 3 ---
▪ → Exit
o Otherwise, increment i = i + 1
o   If end of array is reached (i == n), print “Element not
found”
• C Code Example (Optional)
int linearSearch(int arr[], int n, int key) {
for (int i = 0; i < n; i++) {
if (arr[i] == key)
return i;   // Element found, return index
}
return -1; // Element not found
}
• Time Complexity Analysis
o Best Case: Key is at the first position, O(1)
o Average Case: Key is somewhere in the middle,
O(n)
o Worst Case: Key is at the end or not present, O(n)
Question   [5]
Differentiate between a linear queue and a circular queue.
Synoptic
•   In a Linear Queue, elements are arranged in a straight line.
In a Circular Queue, the last position is connected back to
the first position.
•   Linear Queue follows the FIFO rule but wastes space when
elements are deleted.
Circular Queue also follows FIFO but reuses the freed space
efficiently.
•   In a Linear Queue, overflow occurs when rear == size - 1.
d.
In a Circular Queue, overflow occurs when (rear + 1) % size
== front.
•   Linear Queue does not reuse deleted spaces.
Circular Queue reuses deleted spaces.
•   Linear Queue may require shifting of elements after deletion.
Circular Queue never requires shifting.
•   Linear Queue is less efficient in memory utilization.
Circular Queue is more efficient in memory utilization.
•   In Linear Queue, front and rear move only in one direction.
********** 3 **********
--- page 4 ---
In Circular Queue, front and rear move circularly using
modulo operation.
•   Linear Queue is easier to implement but less space-efficient.
Circular Queue is slightly complex but makes better use of
space.
•   Linear Queue is used in simple data handling (like waiting
lines).
Circular Queue is used in CPU scheduling, printer queues,
and buffering.
•   In Linear Queue, after several deletions, even if space is
available, new elements cannot be added without resetting.
In Circular Queue, new elements can be added as freed
spaces are reused.
Q2   [20]
Question
Explain the concept of a stack and the role of the 'top' pointer.
Describe the conditions of stack underflow and overflow, and
illustrate with a real-life example
Synoptic:
•   Stack:
o A linear data structure that follows the LIFO (Last
In, First Out) principle.
o The last inserted element is the first one to be
removed.
• Role of ‘TOP’ Pointer   [10]
o Points to the position of the last inserted element in
the stack.
o Used to manage insertion (push) and deletion (pop)
operations.
o Updated after every operation.
• Stack Overflow
o Occurs when trying to push an element into a full
stack (TOP == MAX - 1).
o The program exceeds available memory space for the
stack.
• Stack Underflow
o Occurs when trying to pop an element from an empty
stack (TOP == -1).
o No element exists to remove.
•   Real-life Examples
********** 4 **********
--- page 5 ---
o Stack of plates: Last plate placed is the first to be
removed.
o Undo/Redo in text editors.
o Browser Back Button navigation history.
Question
Write the algorithm and corresponding C code for performing push
and pop operations on a stack
Synoptic:
• Push Operation: To insert a new element at the top of the
stack.
o Algorithm:
▪   If TOP == MAX - 1 → Overflow → display
message.
▪   Else increment TOP.
▪   Insert the new element into stack[TOP].
o Key Points:
▪   Insertion allowed only at one end (TOP).
▪ Must check overflow before inserting.
o C Code:
void push(int val) {
if (top == MAX - 1)
printf("Stack Overflow\n");
else {
top++;   [10]
stack[top] = val;
printf("%d pushed\n", val);
}
}
• Pop Operation: To remove and return the top element of the
stack.
o Algorithm:
▪   If TOP == -1 → Underflow → display
message.
▪   Else, store stack[TOP] in a variable.
▪ Decrement TOP.
▪ Return the removed element.
o Key Points:
▪   Deletion allowed only from the TOP.
▪ Must check underflow before popping.
o C Code:
void pop() {
if (top == -1)
printf("Stack Underflow\n");
else {
********** 5 **********
--- page 6 ---
printf("Popped element = %d\n",
stack[top]);
top--;
}
}
Q3   [20]
Question
Explain the concept of a queue, its characteristics, and the different
types of queues
Synoptics
• Queue: A queue is a linear data structure that stores
elements in a sequential order, where:
o   Insertion happens at the rear (enqueue).
o Deletion happens at the front (dequeue).
o   It follows the FIFO (First In, First Out) principle.
• Example (Real Life):A line of people waiting at a ticket
counter — the first person in line is the first to be served.
•   Characteristics
o Linear structure with sequential data organization.
o Two pointers:
▪   Front → points to the first element (for
deletion).
▪ Rear → points to the last element (for
insertion).
o Can be bounded (fixed-size array) or dynamic
(linked list).
o Queue becomes:
▪ Empty when all elements are removed.
▪   Full when it reaches maximum capacity.
• Types of Queues
o Linear Queue: Insertion at rear, deletion at front
(FIFO).
o Circular Queue: Last position connects back to
first, enabling reuse of freed space.
o Double-Ended Queue (Deque): Insertion and
deletion allowed at both ends.
o Priority Queue: Each element has a priority; higher
priority dequeued first.
Question
Write the algorithm and corresponding C code for performing
enqueue and dequeue operations in a linear queue.
[10]
Synoptics
• Enqueue Algorithm (Insert at Rear)
********** 6 **********
--- page 7 ---
o Check if queue is full → if (rear == size - 1) →
Overflow.
o   If empty → set front = 0.
o Increment rear++.
o   Insert element at queue[rear].
• Dequeue Algorithm (Delete from Front)
o Check if empty → if (front == -1 || front > rear) →
Underflow.
o Remove element at queue[front].
o Increment front++.
o   If front > rear, reset both to -1.
• Code
#define SIZE 5
int Q[SIZE];
int front = -1, rear = -1;
void enqueue(int item) {
if (rear == SIZE - 1)
printf("Queue Overflow\n");
else {
if (front == -1)
front = 0;
rear++;
Q[rear] = item;
printf("%d inserted into queue\n", item);
}
}
void dequeue() {
if (front == -1 || front > rear)
printf("Queue Underflow\n");
else {
printf("%d deleted from queue\n", Q[front]);
front++;
if (front > rear)
front = rear = -1;
}
}
Q4   [20]
Question
Explain what a sorting algorithm is, why sorting is needed, and the
key factors used in evaluating a sorting algorithm.   [10]
Synoptics
********** 7 **********
--- page 8 ---
• A sorting algorithm is a method used to arrange data
elements (numbers, strings, etc.) in a specific order —
usually ascending or descending.
• Why Sorting is Needed
o Faster Searching: Algorithms like Binary Search
require sorted data.
o Better Organization: Easier to read, analyze, and
interpret data.
o Efficiency in Algorithms: Many algorithms depend
on pre-sorted input for optimal performance.
• Key Factors for Evaluating Sorting Algorithms
o Time Complexity
▪ Measures execution time growth with input
size (n).
▪   Best Case: Ideal condition (e.g., already
sorted).
▪ Average Case: Expected performance on
random data.
▪ Worst Case: Completely unsorted or reverse
order data.
o Space Complexity
▪ Measures extra memory used besides input
data.
▪   In-place Algorithms: Use little or no extra
memory.
▪ Non–In-place Algorithms: Require extra
storage space.
Question
Write the step-by-step algorithm for Bubble Sort and explain its time
complexity with an example
Synoptics
• Bubble Sort repeatedly compares adjacent elements and
swaps them if they are in the wrong order. The largest
elements "bubble up" to the end after each pass.
• Algorithm (Step-by-Step)
o Repeat (n – 1) times:
o For each pair of adjacent elements (arr[j], arr[j+1]):   [10]
▪   If arr[j] > arr[j+1], swap them.
o After each pass, the largest element moves to its
correct position.
• Example: Array: {5, 1, 4, 2, 8}
o Pass 1: {1, 4, 2, 5, 8}
o Pass 2: {1, 2, 4, 5, 8}
o Pass 3: No swaps → Array sorted.
o ✅ Final Sorted Array: {1, 2, 4, 5, 8}
• Time Complexity
o Best: Already sorted, O(n)
********** 8 **********
--- page 9 ---
o Average: Random order, O(n²)
o Worst: Reverse order ,O(n²)
Q5   [20]
Question
Explain the functions malloc() and calloc() in C, highlighting their
differences and usage with examples.
Synoptics
•   malloc() Function
o malloc stands for Memory Allocation.
o   It allocates a single continuous block of memory of a
given size.
o Syntax: ptr = (type*) malloc(size_in_bytes);
o Explanation:
▪   size_in_bytes: total number of bytes to
allocate.
▪   Returns a void pointer (void*), so typecasting
is required.
▪ Memory is uninitialized — contains garbage
values.
[10]
•   calloc() Function
o calloc stands for Contiguous Allocation.
o   It allocates memory for multiple elements, each of the
same size.
o Syntax: ptr = (type*) calloc(num, size);
o Explanation:
▪ num: number of elements.
▪   size: size of each element in bytes.
▪   Allocates num * size bytes in total.
▪   Initializes all bytes to 0.
• Key Differences
o malloc() leaves memory uninitialized (contains
garbage values).
o   calloc() initializes all allocated bytes to zero (0x00)
o Both return a void pointer that must be typecast to the
desired pointer type.
o   If allocation fails, both functions return NULL.
Question
Explain, with proper steps and examples, how to delete a node in a
linked list at the beginning, at the end, and at a specific position
[10]
Synoptics
• Types of Deletion:
o From Beginning:
▪   Store head in temp.
********** 9 **********
--- page 10 ---
▪ Update head = head->next.
▪   Free(temp).
o From End:
▪   Traverse to second-last node.
▪   Free last node.
▪   Set secondLast->next = NULL.
o From Specific Position:
▪   Traverse to (position - 1) node.
▪   Store pointer to node to delete.
▪ Update links: prev->next = temp->next.
▪   Free(temp).
Q6   [20]
Question
Explain the concept of a 2D array, including its declaration, example
and the various operations performed on it, in detail
Synoptics
• A 2D array is like a table (matrix) with rows and columns.
• Each element is identified by two indices: [i][j]
• Example: marks[0][1] → 1st row, 2nd column
[10]
•   Declaration: data_type array_name[rows][columns];
• Example: int studentMarks[10][3];
•   Initialization: int marks[2][3] = { {85, 90, 78}, {92, 88,
76} };
• Common Operations
o Traversal: Access each element using nested loops.
o   Insertion / Update: Assign a value to a specific [i][j].
o Deletion: Not possible directly; overwrite with a new
value.
Question
Explain how a one-dimensional array is stored in memory and derive
the formula for calculating the address of an element with an
example.
Synoptics
• 1D arrays are stored in contiguous memory locations.
• The array name itself is a pointer to the first element.
[10]
• Example: int arr[5] = {10, 20, 30, 40, 50};
•   If int = 4 bytes → memory addresses differ by 4.
• Address Calculation Formula
o Address(arr[i]) = Base_Address + (i ×
size_of_each_element)
•   If base address (BA) = 1000 and sizeof(int) = 4 →
Address of arr[2] = 1000 + (2 × 4) = 1008
********** 10 **********
--- page 11 ---
Q7   [20]
Case Study Analysis
Question
•   Explain the application of arrays in modern software development,
providing suitable real-world examples. Discuss any two cases
where arrays are preferred
•   Explain the application of linked lists in modern software
development, providing suitable real-world examples. Discuss any
two cases where linked lists are preferred
Synoptics
•   Applications of Arrays
o Arrays are widely used in modern applications for:
o Image processing and graphics
o Audio/video data handling
o Machine learning and AI (tensors)
o Database indexing and search operations
o   Scientific computing and simulations
o Example 1 – Image Processing & Graphics
▪ Every image is represented as a 2D array (matrix) of
pixel values.
▪ Each element corresponds to a pixel’s intensity or
color (e.g., RGB).
▪ Used In: Photoshop, Instagram filters, medical
imaging software.
▪ Why Array?
• Contiguous storage allows fast access and
updates to pixels.
•   Supports matrix operations like rotation,
scaling, and filtering.
o Example 2 – Machine Learning and AI
▪   Arrays form the base for tensors in frameworks like
NumPy, TensorFlow, and PyTorch.
▪ Used to store datasets, parameters, and activations in
neural networks.
▪ Used In: ChatGPT, face recognition, self-driving car
systems.
▪ Why Array?
•   Enables parallel computations on GPUs.
•   Applications of Linked Lists
o Linked lists are commonly used in:
o Music/video playlist navigation
o Navigation and mapping systems
o Memory management in operating systems
o Blockchain and distributed ledger systems
o Undo/redo operations in editors
o Example 1 – Music or Video Playlists
▪ Each song or video is a node connected to the next
via pointers.
********** 11 **********
--- page 12 ---
▪ “Next” and “Previous” buttons move through the list
dynamically.
▪ Used In: Spotify, YouTube, VLC Media Player.
▪ Why Linked List?
• Allows easy insertion, deletion, or
rearranging of songs.
•   Enables continuous playback and dynamic
playlist updates.
• Example 2 – Navigation and Maps
o Each location or stop is a node connected to the next in a
route.
o Used In: Google Maps, Uber route planning.
o Why Linked List?
▪ Routes can be modified dynamically (add/remove
waypoints).
▪   Efficient for sequential traversal of path data.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 922bdd43d59f

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/DATA STRUCTURES/ANS_DATA STRUCTURES(701CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: DATA STRUCTURES
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions.
6. Write algorithms in the proper format, including input, output, and step-by-step instructions wherever
applicable.
7. Provide clear and concise pseudocode wherever applicable.
8. Include diagrams wherever applicable to illustrate data structures or processes clearly.
Q1   Answer briefly:   [20]
Question
Explain the concept of an Abstract Data Type (ADT) and its
importance in data structure design.
Synoptic:
Definition:
An Abstract Data Type (ADT) is a user-defined data type that
specifies what operations can be performed on the data, but not
how these operations are implemented.
It hides the internal structure and exposes only the interface
a.   [5]
(operations).
Key Concepts:
• Abstraction: Hides the internal implementation details;
shows only necessary operations (e.g., push(), pop()).
• Encapsulation: Combines data and its operations in a
single unit; restricts direct access to internal data.
• Modularity: Each ADT is an independent module —
easier maintenance and debugging.
• Reusability: Once defined, an ADT can be reused
across programs, ensuring consistency.
********** 1 **********
--- page 2 ---
•   Flexibility: Implementation can change without
affecting how users interact with it.
Importance in Data Structure Design:
• Promotes clean separation between interface and
implementation.
• Enhances software maintainability and scalability.
• Encourages modular and reusable code.
Example: Stack ADT allows using push() and pop() without
knowing whether it’s implemented via array or linked list.
Question   [5]
Describe the classification of data structures into primitive and
non-primitive types. Give examples of each
Synoptic:
Classification of Data Structures: Data structures are
classified into Primitive and Non-Primitive types based on their
structure and how data is organized.
1. Primitive Data Structures
• Definition: Basic data types directly supported by the
programming language and manipulated by the CPU.
Data is stored one after another in memory (contiguous
memory allocation).
b.   • Characteristics
o Simple and machine-level data types.
o Operated directly by CPU instructions.
o Used for performing basic computations.
• Examples:
o Integer: Whole numbers (e.g., -10, 0, 42).
o Float: Real numbers with decimals (e.g., 3.14, -
0.001).
o Character (Char): Single symbols (e.g., 'A', 'z').
o Boolean: Logical values (true/false).
2. Non-Primitive Data Structures
a. Definition: Derived from primitive types; cannot
be directly manipulated by the CPU.Focuses on
organizing multiple data elements (homogeneous
or heterogeneous).
b. Types:
********** 2 **********
--- page 3 ---
i. Linear Data Structures: Data is arranged in
a sequence (e.g., Array, Linked List,
Stack, Queue).
ii. Non-Linear   Data   Structures:   Data
elements form hierarchical or networked
relationships (e.g., Tree, Graph).
c. Examples:
i. Linear: Array, Linked List, Stack, Queue.
ii. Non-Linear: Tree, Graph.
Question   [5]
Write an algorithm to calculate the factorial of a number using
a stack, and illustrate it with a proper example
Synotics
A stack can be used to simulate the recursive computation of
factorial by pushing each number and then multiplying them in
reverse order as they are popped.
Algorithm Steps:
•   Initialize an empty stack.
• Push all integers from n down to 1 onto the stack.
•   Initialize result = 1.
• While stack is not empty:
o Pop the top element.
o Multiply it with result.
c.
• Return result as factorial of n
Example:
• Let n = 5
• Operation: Push 5,4,3,2,1
Stack Content: [5,4,3,2,1]
Result: 1
• Operation: Pop 1
Stack Content: [5,4,3,2]
Result: 1*1=1
• Operation: Pop 2
Stack Content: [5,4,3]
Result: 1*2=2
********** 3 **********
--- page 4 ---
• Operation: Pop 3
Stack Content: [5,4]
Result: 2*3=6
• Operation: Pop 4
Stack Content: [5]
Result: 6*4=24
• Operation: Pop 5
Stack Content: []
Result: 25*5=120
Explain pointers in C, their operators, and their usage with [5]
d.   appropriate examples.
Q2   [20]
Question:
Write the algorithm and corresponding C code to implement
stack traversal and peek operation.
Synoptic:
• Peek Operation: To view the top element of the stack
without removing it.
o Algorithm:
▪ Check if top == -1 → Stack is empty →
display message.
▪   Else, return stack[top].
o Key Points:   [10]
▪ Non-destructive operation.
▪ Runs in O(1) constant time.
▪ Must check for empty stack before
accessing top.
o C Code:
void peek() {
if (top == -1)
printf("Stack is Empty\n");
else
printf("Top element = %d\n",
stack[top]);
}
********** 4 **********
--- page 5 ---
• Traverse Operation: To display all elements of the
stack from top to bottom.
o Algorithm:
▪ Check if top == -1 → print “Stack is
Empty”.
▪   Else, for i = top down to 0, print stack[i].
o Key Points:
▪ Traversal is top to bottom (LIFO order).
▪ Non-destructive; does not modify the
stack.
▪ Read-only operation.
o C Code:
void traverse() {
if (top == -1)
printf("Stack is Empty\n");
else {
for (int i = top; i >= 0; i--)
printf("%d\n", stack[i]);
}
}
Question
Explain infix, prefix, and postfix expressions in detail, with
suitable examples for each.
Synoptics
• Infix Expression
o Definition: Operator is written between
operands (usual arithmetic form).
o Example: (A + B) * (C - D)
o Evaluation: Needs operator precedence and
parentheses to define order
• Prefix Expression   [10]
o Definition: Operator is written before operands.
o No parentheses are required — order is
inherently defined.
o Examples:
▪ A + B → + A B
▪ (A + B) * (C - D) → * + A B - C D
o Evaluation: Scanned from right to left using a
stack.
• Postfix Expression
o Definition: Operator is written after operands.
o No parentheses required.
o Examples:
********** 5 **********
--- page 6 ---
▪ A + B → A B +
▪ (A + B) * (C - D) → A B + C D - *
o Evaluation: Scanned from left to right using a
stack.
▪ Push operands to stack.
▪ When operator appears, pop two
operands, apply operator, push result
back.
Q3   [20]
Question
Explain how a linear queue can be implemented using an array,
and state the limitations of a linear queue.
Synoptics
Implementation Using Array
• Represent the queue as an array Q[SIZE].
• Maintain two indices
o front → index of first element.
o rear → index of last element   [10]
• Enqueue adds element at rear
• Dequeue removes element at front.
Limitation
• Wastage of Space: Freed front spaces cannot be reused
after dequeuing.
• Fixed Size: Array size is static; cannot grow
dynamically.
•   Inefficient Shifting: Requires shifting elements to
reuse front space, making time complexity O(n).
Question
Write the algorithm and corresponding C code for performing
enqueue and dequeue operations in a circular queue.
Synoptics   [10]
• Enqueue Algorithm
o Check if queue is full → (rear + 1) % size == front
→ Overflow.
o   If empty → set front = 0
********** 6 **********
--- page 7 ---
o rear = (rear + 1) % size
o Insert element at queue[rear]
• Dequeue Algorithm
o Check if queue is empty → front == -1 →
Underflow
o Remove element at queue[front].
o   If front == rear → reset both to -1.
o Else → front = (front + 1) % size
• Code
#define SIZE 5
int CQ[SIZE];
int front = -1, rear = -1;
void enqueue(int item) {
if ((rear + 1) % SIZE == front)
printf("Queue Overflow\n");
else {
if (front == -1)
front = 0;
rear = (rear + 1) % SIZE;
CQ[rear] = item;
printf("%d inserted into circular queue\n",
item);
}
}
void dequeue() {
if (front == -1)
printf("Queue Underflow\n");
else {
printf("%d deleted from circular queue\n",
CQ[front]);
if (front == rear)
front = rear = -1;
else
front = (front + 1) % SIZE;
}
}
Q4   [20]
Question
[10]
Explain the binary search algorithm in detail, including its
********** 7 **********
--- page 8 ---
working principle with an example. Also, describe the best,
worst, and average case scenarios.
Synoptics
• Binary Search efficiently locates a target element in a
sorted array by repeatedly dividing the search range in
half.
• Algorithm Steps
o Initialize low = 0, high = n - 1.
o While low <= high:
▪ Compute mid = (low + high) / 2.
▪   If arr[mid] == key → found.
▪   If arr[mid] > key → search left half (high
= mid - 1).
▪   If arr[mid] < key → search right half
(low = mid + 1).
o   If range becomes empty → key not found.
• Example
o Array: {10, 20, 30, 40, 50}, Key = 30
o Step 1: low=0, high=4 → mid=2, arr[2]=30 →
✅ Found at index 2
• .Time Complexity
o Best Case: Element found at mid, O(1)
o Average Case: Key found after few divisions,
O(log n)
o Worst Case: Element not present, O(log n)
Question
Explain the differences between binary search and linear
search.
Synoptics
• Linear Search works on both sorted and unsorted
data.Binary Search works only on sorted data.
• Linear Search checks each element sequentially from   [10]
start to end. Binary Search repeatedly divides the array
into halves to find the element.
• Linear Search is simple to implement. Binary Search is
slightly complex because it involves middle element
calculations.
• Linear Search takes more time for large datasets.Binary
Search is much faster, especially for large datasets.
********** 8 **********
--- page 9 ---
• Linear Search does not require sorted data.Binary
Search requires sorted data before searching.
• Linear Search has a time complexity of O(n).Binary
Search has a time complexity of O(log n).
• In Linear Search, every element is compared until the
key is found or the list ends.In Binary Search, only a
subset of elements is compared each time.
• Linear Search can be applied to arrays and linked lists.
Binary Search is typically used on arrays (due to index-
based access).
• Linear Search is less efficient for large data. Binary
Search is highly efficient for large, sorted data.
• Linear Search best case occurs when the key is the first
element → O(1). Binary Search best case occurs when
the key is the middle element → O(1).
Q5   [20]
Question
Explain the concept of a linked list and its advantages, with the
help of an example.
Synoptics
• Definition: A linked list is a linear data structure
consisting of nodes.
• Each node has two parts:
o Data: stores the element’s value.
o Pointer (next): stores the address of the next   [10]
node.
• Example: 10 → 20 → 30 → NULL (each arrow
represents a pointer).
• Advantages:
o Dynamic size: grows or shrinks during runtime.
o Efficient insertion/deletion: no shifting needed
as in arrays.
o Better memory use: uses non-contiguous
memory
Question
Explain, with proper steps and examples, how to insert a node
in a linked list at the beginning, at the end, and at a specific   [10]
position.
Synoptics
********** 9 **********
--- page 10 ---
• Types of Insertion:
o At Beginning:
▪ Allocate memory for new node.
▪ Set newNode->next = head.
▪ Update head = newNode.
o At End:
▪ Allocate new node.
▪ Traverse to last node.
▪ Set last->next = newNode.
• Set newNode->next = NULL.
• At Specific Position:
o Allocate new node.
o Traverse to (position - 1) node.
o Set newNode->next = temp->next.
o Set temp->next = newNode.
Q6   [20]
Question
Explain how a two-dimensional array is stored in memory.
Derive the formula for calculating the address of an element in
row-major order and column-major order with an example.
Synoptics
• A 2D array is stored as a contiguous block in memory.
• Two methods of storage:
o Row-Major Order: Stores elements row by
row.(Used in C/C++)
o Column-Major Order: Stores elements column
by column. (Used in Fortran, MATLAB)   [10]
• Example: int A[2][3] = { {1,2,3}, {4,5,6} };
• Row-Major: 1,2,3,4,5,6
• Column-Major: 1,4,2,5,3,6
• Address Calculation Formula
o BA = Base address
o W = Size of each element (in bytes)
o m = rows, n = columns
o   i = row index, j = column index
• Row-Major Order
o Address(A[i][j]) = BA + ((i × n) + j) × W
o A[3][4] → m = 3, n = 4, BA = 1000, W = 4
********** 10 **********
--- page 11 ---
Find A[2][1] → = 1000 + ((2×4) + 1) × 4 = 1036
• Column-Major Order
o Address(A[i][j]) = BA + ((j × m) + i) × W
o Example= 1000 + ((1×3) + 2) × 4 = 1020
Question
Explain the concept of a 1D array, including its declaration,
example, and the various operations that can be performed on
it, in detail.
Synoptics
• A 1D array stores a fixed-size sequential collection of
same-type elements.
• Allows indexed access (fast retrieval).
• Stored in contiguous memory.
• Declaration: data_type array_name[array_size];   [10]
• Example: int marks[5]; float temperatures[10];
• Operations on 1D Array
o Traversal: visit all elements
o Insertion: add element (requires shifting)
o Deletion: remove element (requires shifting)
o Searching: find element by value
o Sorting: rearrange elements (e.g., bubble sort,
selection sort)
Q7   [20]
Case Study Analysis:
• Question
o Explain the use of binary search in real-time search engines with
appropriate examples.
o Describe the application of stacks in expression evaluation and web
browser history, providing suitable examples.
• Synoptics
o Applications in Real-Time Search Engines
▪ Autocomplete Feature (Type-ahead Suggestions)
• Search engine stores a sorted list of words.
• When user types a prefix (e.g., “prog”):
• Binary Search finds first word starting with “prog” →
“program”.
• Then finds the last word with same prefix.
********** 11 **********
--- page 12 ---
• All words in between = suggestions → ["program",
"programmer", "programming"].
• Time Complexity: O(log n)
▪ Keyword Index Lookup
• Search engines maintain an inverted index:
• keyword → [list of document IDs]
• Example: "search" → [Doc4, Doc6, Doc10]
• Keywords are sorted alphabetically.
• Binary Search is used to quickly locate the keyword
among millions of entries.
▪ Ranked Retrieval
• After fetching matching results, they are ranked by
relevance score.
• When inserting new results, Binary Search finds the
correct position.
• Example: Page score 8.5 is placed between 8.9 and
8.1.
• Keeps the sorted ranking list efficient for quick
retrieval.
▪ Industry Use
• Google Search: Autocomplete suggestions
• Amazon: Product search and ranking
•   Netflix: Movie title search
o Expression Evaluation
▪ Used in compilers and interpreters to evaluate arithmetic
expressions.
▪ Example:
•   Infix: (A + B) * C
•   Postfix: AB + C *
▪ How It Works
• Two stacks are used:
o Operand Stack: Stores numbers or variables.
o Operator Stack: Stores operators and
parentheses.
• Operators are pushed to stack.
• When precedence rules apply, they are popped and
applied to operands.
▪ Example
• Expression: 3 + 4 * 2
• Stack ensures multiplication is done before addition
→ (4 * 2) then + 3.
▪ Real-World Uses
• Programming Languages (C, Java, Python):
Expression parsing
********** 12 **********
--- page 13 ---
• Calculator Apps: Operator precedence and
computation
o Web Browser History Management
▪ Browsers use two stacks to handle Back and Forward
navigation.
▪ How It Works
• When visiting a new page → push it onto the Back
Stack.
• When user clicks Back →
o Current page is popped from Back Stack
o Pushed onto Forward Stack.
• Clicking Forward → reverses the process.
o Industry Applications
▪ Web Browsers: Chrome, Firefox navigation history
▪ Text Editors: Undo/Redo functionality
▪ Programming: Function call management via call stack
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper f2d4e7d4fa71

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/DATA STRUCTURES/ANS_DATA STRUCTURES(701CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: DATA STRUCTURES
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions.
6. Write algorithms in the proper format, including input, output, and step-by-step instructions wherever
applicable.
7. Provide clear and concise pseudocode wherever applicable.
8. Include diagrams wherever applicable to illustrate data structures or processes clearly.
Q1   Answer briefly:   [20]
Question
Explain the concept of an Abstract Data Type (ADT) and its
importance in data structure design.
Synoptic:
Definition:
An Abstract Data Type (ADT) is a user-defined data type that
specifies what operations can be performed on the data, but not
how these operations are implemented.
It hides the internal structure and exposes only the interface
a.   [5]
(operations).
Key Concepts:
• Abstraction: Hides the internal implementation details;
shows only necessary operations (e.g., push(), pop()).
• Encapsulation: Combines data and its operations in a
single unit; restricts direct access to internal data.
• Modularity: Each ADT is an independent module —
easier maintenance and debugging.
• Reusability: Once defined, an ADT can be reused
across programs, ensuring consistency.
********** 1 **********
--- page 2 ---
•   Flexibility: Implementation can change without
affecting how users interact with it.
Importance in Data Structure Design:
• Promotes clean separation between interface and
implementation.
• Enhances software maintainability and scalability.
• Encourages modular and reusable code.
Example: Stack ADT allows using push() and pop() without
knowing whether it’s implemented via array or linked list.
Question   [5]
Describe the classification of data structures into primitive and
non-primitive types. Give examples of each
Synoptic:
Classification of Data Structures: Data structures are
classified into Primitive and Non-Primitive types based on their
structure and how data is organized.
1. Primitive Data Structures
• Definition: Basic data types directly supported by the
programming language and manipulated by the CPU.
Data is stored one after another in memory (contiguous
memory allocation).
b.   • Characteristics
o Simple and machine-level data types.
o Operated directly by CPU instructions.
o Used for performing basic computations.
• Examples:
o Integer: Whole numbers (e.g., -10, 0, 42).
o Float: Real numbers with decimals (e.g., 3.14, -
0.001).
o Character (Char): Single symbols (e.g., 'A', 'z').
o Boolean: Logical values (true/false).
2. Non-Primitive Data Structures
a. Definition: Derived from primitive types; cannot
be directly manipulated by the CPU.Focuses on
organizing multiple data elements (homogeneous
or heterogeneous).
b. Types:
********** 2 **********
--- page 3 ---
i. Linear Data Structures: Data is arranged in
a sequence (e.g., Array, Linked List,
Stack, Queue).
ii. Non-Linear   Data   Structures:   Data
elements form hierarchical or networked
relationships (e.g., Tree, Graph).
c. Examples:
i. Linear: Array, Linked List, Stack, Queue.
ii. Non-Linear: Tree, Graph.
Question   [5]
Write an algorithm to calculate the factorial of a number using
a stack, and illustrate it with a proper example
Synotics
A stack can be used to simulate the recursive computation of
factorial by pushing each number and then multiplying them in
reverse order as they are popped.
Algorithm Steps:
•   Initialize an empty stack.
• Push all integers from n down to 1 onto the stack.
•   Initialize result = 1.
• While stack is not empty:
o Pop the top element.
o Multiply it with result.
c.
• Return result as factorial of n
Example:
• Let n = 5
• Operation: Push 5,4,3,2,1
Stack Content: [5,4,3,2,1]
Result: 1
• Operation: Pop 1
Stack Content: [5,4,3,2]
Result: 1*1=1
• Operation: Pop 2
Stack Content: [5,4,3]
Result: 1*2=2
********** 3 **********
--- page 4 ---
• Operation: Pop 3
Stack Content: [5,4]
Result: 2*3=6
• Operation: Pop 4
Stack Content: [5]
Result: 6*4=24
• Operation: Pop 5
Stack Content: []
Result: 25*5=120
Explain pointers in C, their operators, and their usage with [5]
d.   appropriate examples.
Q2   [20]
Question:
Write the algorithm and corresponding C code to implement
stack traversal and peek operation.
Synoptic:
• Peek Operation: To view the top element of the stack
without removing it.
o Algorithm:
▪ Check if top == -1 → Stack is empty →
display message.
▪   Else, return stack[top].
o Key Points:   [10]
▪ Non-destructive operation.
▪ Runs in O(1) constant time.
▪ Must check for empty stack before
accessing top.
o C Code:
void peek() {
if (top == -1)
printf("Stack is Empty\n");
else
printf("Top element = %d\n",
stack[top]);
}
********** 4 **********
--- page 5 ---
• Traverse Operation: To display all elements of the
stack from top to bottom.
o Algorithm:
▪ Check if top == -1 → print “Stack is
Empty”.
▪   Else, for i = top down to 0, print stack[i].
o Key Points:
▪ Traversal is top to bottom (LIFO order).
▪ Non-destructive; does not modify the
stack.
▪ Read-only operation.
o C Code:
void traverse() {
if (top == -1)
printf("Stack is Empty\n");
else {
for (int i = top; i >= 0; i--)
printf("%d\n", stack[i]);
}
}
Question
Explain infix, prefix, and postfix expressions in detail, with
suitable examples for each.
Synoptics
• Infix Expression
o Definition: Operator is written between
operands (usual arithmetic form).
o Example: (A + B) * (C - D)
o Evaluation: Needs operator precedence and
parentheses to define order
• Prefix Expression   [10]
o Definition: Operator is written before operands.
o No parentheses are required — order is
inherently defined.
o Examples:
▪ A + B → + A B
▪ (A + B) * (C - D) → * + A B - C D
o Evaluation: Scanned from right to left using a
stack.
• Postfix Expression
o Definition: Operator is written after operands.
o No parentheses required.
o Examples:
********** 5 **********
--- page 6 ---
▪ A + B → A B +
▪ (A + B) * (C - D) → A B + C D - *
o Evaluation: Scanned from left to right using a
stack.
▪ Push operands to stack.
▪ When operator appears, pop two
operands, apply operator, push result
back.
Q3   [20]
Question
Explain how a linear queue can be implemented using an array,
and state the limitations of a linear queue.
Synoptics
Implementation Using Array
• Represent the queue as an array Q[SIZE].
• Maintain two indices
o front → index of first element.
o rear → index of last element   [10]
• Enqueue adds element at rear
• Dequeue removes element at front.
Limitation
• Wastage of Space: Freed front spaces cannot be reused
after dequeuing.
• Fixed Size: Array size is static; cannot grow
dynamically.
•   Inefficient Shifting: Requires shifting elements to
reuse front space, making time complexity O(n).
Question
Write the algorithm and corresponding C code for performing
enqueue and dequeue operations in a circular queue.
Synoptics   [10]
• Enqueue Algorithm
o Check if queue is full → (rear + 1) % size == front
→ Overflow.
o   If empty → set front = 0
********** 6 **********
--- page 7 ---
o rear = (rear + 1) % size
o Insert element at queue[rear]
• Dequeue Algorithm
o Check if queue is empty → front == -1 →
Underflow
o Remove element at queue[front].
o   If front == rear → reset both to -1.
o Else → front = (front + 1) % size
• Code
#define SIZE 5
int CQ[SIZE];
int front = -1, rear = -1;
void enqueue(int item) {
if ((rear + 1) % SIZE == front)
printf("Queue Overflow\n");
else {
if (front == -1)
front = 0;
rear = (rear + 1) % SIZE;
CQ[rear] = item;
printf("%d inserted into circular queue\n",
item);
}
}
void dequeue() {
if (front == -1)
printf("Queue Underflow\n");
else {
printf("%d deleted from circular queue\n",
CQ[front]);
if (front == rear)
front = rear = -1;
else
front = (front + 1) % SIZE;
}
}
Q4   [20]
Question
[10]
Explain the binary search algorithm in detail, including its
********** 7 **********
--- page 8 ---
working principle with an example. Also, describe the best,
worst, and average case scenarios.
Synoptics
• Binary Search efficiently locates a target element in a
sorted array by repeatedly dividing the search range in
half.
• Algorithm Steps
o Initialize low = 0, high = n - 1.
o While low <= high:
▪ Compute mid = (low + high) / 2.
▪   If arr[mid] == key → found.
▪   If arr[mid] > key → search left half (high
= mid - 1).
▪   If arr[mid] < key → search right half
(low = mid + 1).
o   If range becomes empty → key not found.
• Example
o Array: {10, 20, 30, 40, 50}, Key = 30
o Step 1: low=0, high=4 → mid=2, arr[2]=30 →
✅ Found at index 2
• .Time Complexity
o Best Case: Element found at mid, O(1)
o Average Case: Key found after few divisions,
O(log n)
o Worst Case: Element not present, O(log n)
Question
Explain the differences between binary search and linear
search.
Synoptics
• Linear Search works on both sorted and unsorted
data.Binary Search works only on sorted data.
• Linear Search checks each element sequentially from   [10]
start to end. Binary Search repeatedly divides the array
into halves to find the element.
• Linear Search is simple to implement. Binary Search is
slightly complex because it involves middle element
calculations.
• Linear Search takes more time for large datasets.Binary
Search is much faster, especially for large datasets.
********** 8 **********
--- page 9 ---
• Linear Search does not require sorted data.Binary
Search requires sorted data before searching.
• Linear Search has a time complexity of O(n).Binary
Search has a time complexity of O(log n).
• In Linear Search, every element is compared until the
key is found or the list ends.In Binary Search, only a
subset of elements is compared each time.
• Linear Search can be applied to arrays and linked lists.
Binary Search is typically used on arrays (due to index-
based access).
• Linear Search is less efficient for large data. Binary
Search is highly efficient for large, sorted data.
• Linear Search best case occurs when the key is the first
element → O(1). Binary Search best case occurs when
the key is the middle element → O(1).
Q5   [20]
Question
Explain the concept of a linked list and its advantages, with the
help of an example.
Synoptics
• Definition: A linked list is a linear data structure
consisting of nodes.
• Each node has two parts:
o Data: stores the element’s value.
o Pointer (next): stores the address of the next   [10]
node.
• Example: 10 → 20 → 30 → NULL (each arrow
represents a pointer).
• Advantages:
o Dynamic size: grows or shrinks during runtime.
o Efficient insertion/deletion: no shifting needed
as in arrays.
o Better memory use: uses non-contiguous
memory
Question
Explain, with proper steps and examples, how to insert a node
in a linked list at the beginning, at the end, and at a specific   [10]
position.
Synoptics
********** 9 **********
--- page 10 ---
• Types of Insertion:
o At Beginning:
▪ Allocate memory for new node.
▪ Set newNode->next = head.
▪ Update head = newNode.
o At End:
▪ Allocate new node.
▪ Traverse to last node.
▪ Set last->next = newNode.
• Set newNode->next = NULL.
• At Specific Position:
o Allocate new node.
o Traverse to (position - 1) node.
o Set newNode->next = temp->next.
o Set temp->next = newNode.
Q6   [20]
Question
Explain how a two-dimensional array is stored in memory.
Derive the formula for calculating the address of an element in
row-major order and column-major order with an example.
Synoptics
• A 2D array is stored as a contiguous block in memory.
• Two methods of storage:
o Row-Major Order: Stores elements row by
row.(Used in C/C++)
o Column-Major Order: Stores elements column
by column. (Used in Fortran, MATLAB)   [10]
• Example: int A[2][3] = { {1,2,3}, {4,5,6} };
• Row-Major: 1,2,3,4,5,6
• Column-Major: 1,4,2,5,3,6
• Address Calculation Formula
o BA = Base address
o W = Size of each element (in bytes)
o m = rows, n = columns
o   i = row index, j = column index
• Row-Major Order
o Address(A[i][j]) = BA + ((i × n) + j) × W
o A[3][4] → m = 3, n = 4, BA = 1000, W = 4
********** 10 **********
--- page 11 ---
Find A[2][1] → = 1000 + ((2×4) + 1) × 4 = 1036
• Column-Major Order
o Address(A[i][j]) = BA + ((j × m) + i) × W
o Example= 1000 + ((1×3) + 2) × 4 = 1020
Question
Explain the concept of a 1D array, including its declaration,
example, and the various operations that can be performed on
it, in detail.
Synoptics
• A 1D array stores a fixed-size sequential collection of
same-type elements.
• Allows indexed access (fast retrieval).
• Stored in contiguous memory.
• Declaration: data_type array_name[array_size];   [10]
• Example: int marks[5]; float temperatures[10];
• Operations on 1D Array
o Traversal: visit all elements
o Insertion: add element (requires shifting)
o Deletion: remove element (requires shifting)
o Searching: find element by value
o Sorting: rearrange elements (e.g., bubble sort,
selection sort)
Q7   [20]
Case Study Analysis:
• Question
o Explain the use of binary search in real-time search engines with
appropriate examples.
o Describe the application of stacks in expression evaluation and web
browser history, providing suitable examples.
• Synoptics
o Applications in Real-Time Search Engines
▪ Autocomplete Feature (Type-ahead Suggestions)
• Search engine stores a sorted list of words.
• When user types a prefix (e.g., “prog”):
• Binary Search finds first word starting with “prog” →
“program”.
• Then finds the last word with same prefix.
********** 11 **********
--- page 12 ---
• All words in between = suggestions → ["program",
"programmer", "programming"].
• Time Complexity: O(log n)
▪ Keyword Index Lookup
• Search engines maintain an inverted index:
• keyword → [list of document IDs]
• Example: "search" → [Doc4, Doc6, Doc10]
• Keywords are sorted alphabetically.
• Binary Search is used to quickly locate the keyword
among millions of entries.
▪ Ranked Retrieval
• After fetching matching results, they are ranked by
relevance score.
• When inserting new results, Binary Search finds the
correct position.
• Example: Page score 8.5 is placed between 8.9 and
8.1.
• Keeps the sorted ranking list efficient for quick
retrieval.
▪ Industry Use
• Google Search: Autocomplete suggestions
• Amazon: Product search and ranking
•   Netflix: Movie title search
o Expression Evaluation
▪ Used in compilers and interpreters to evaluate arithmetic
expressions.
▪ Example:
•   Infix: (A + B) * C
•   Postfix: AB + C *
▪ How It Works
• Two stacks are used:
o Operand Stack: Stores numbers or variables.
o Operator Stack: Stores operators and
parentheses.
• Operators are pushed to stack.
• When precedence rules apply, they are popped and
applied to operands.
▪ Example
• Expression: 3 + 4 * 2
• Stack ensures multiplication is done before addition
→ (4 * 2) then + 3.
▪ Real-World Uses
• Programming Languages (C, Java, Python):
Expression parsing
********** 12 **********
--- page 13 ---
• Calculator Apps: Operator precedence and
computation
o Web Browser History Management
▪ Browsers use two stacks to handle Back and Forward
navigation.
▪ How It Works
• When visiting a new page → push it onto the Back
Stack.
• When user clicks Back →
o Current page is popped from Back Stack
o Pushed onto Forward Stack.
• Clicking Forward → reverses the process.
o Industry Applications
▪ Web Browsers: Chrome, Firefox navigation history
▪ Text Editors: Undo/Redo functionality
▪ Programming: Function call management via call stack
********** 13 **********
````
