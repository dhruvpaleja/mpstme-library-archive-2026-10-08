# Basic Data Structures: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 37346ec86e59

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/Integrated_Computer_7032/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2025-2026.docx`
- Text: docx (1 page)

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF   TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
|
Program/s:   B Tech INTG
Stream/s :   Computer Engineering/Data Science
| Year: III   Semester: V
|
Subject:   Basic Data Structures
| Time: __3___ hrs.   (______to_______)
|
Date:   /   / 2025
| No. of Pages: 46
|
Marks: __100_______
|
|
Final Examination
|
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1

|
| Answer briefly:
| Marks
|

| a.
| Differentiate between a stack and a queue data structure.
Ans:
Stack
| Queue
|
Stack is a linear data structure where data is added and removed from the top.
| Queue is a linear data structure where data is ended at the rear end and removed from the front.
|
Stack is based on LIFO(Last In First Out) principle
| Queue is based on FIFO(First In First Out) principle
|
Insertion operation in Stack is known as push.
| Insertion operation in Queue is known as eneque.
|
Delete operation in Stack is known as pop.
| Delete operation in Queue is known as dequeue.
|
Only one pointer is available for both addition and deletion: top()
| Two pointers are available for addition and deletion: front() and rear()
|
Used in solving recursive problems
| Used in solving sequential processing problems
|

| 5
|

| b.
| What will be the output of the following program?
#include <iostream>
using namespace std;
int main()
{
int num[5];
int* p;
p = num;
*p = 10;
p++;
*p = 20;
p = &num[2];
*p = 30;
p = num + 3;
*p = 40;
p = num;
*(p + 4) = 50;
for (int i = 0; i < 5; i++)
cout << num[i] << ", ";
return 0;
}
Ans: 10, 20, 30, 40, 50,
| 5
|
CO-3 ; SO-2 ;
BL-2
| c.
| Explain the algorithmic steps for performing different operations on a Circular Queue.
(Each 1 marks)
IsEmpty
Purpose: To check whether the queue is empty.
Condition:
If front == -1, then queue is empty.
IsFull
Purpose: To check whether the queue is full.
Condition:
If (front == (rear + 1) % MAX), then queue is full.
Enqueue (Insertion)
Purpose: To insert an element at the rear of the queue.
Steps:
Check for overflow:
If (front == 0 && rear == MAX - 1) OR (rear + 1) % MAX == front,
the queue is full.
If the queue is empty (front == -1):
Set front = 0 and rear = 0.
Otherwise:
Move rear circularly → rear = (rear + 1) % MAX.
Insert the new element at queue[rear].
Dequeue (Deletion)
Purpose: To remove an element from the front of the queue.
Steps:
Check for underflow:
If front == -1, queue is empty.
Retrieve the element at queue[front].
If front == rear, it means only one element was present:
Set both front = -1 and rear = -1 (queue becomes empty).
Otherwise:
Move front circularly → front = (front + 1) % MAX.
Display
Purpose: To display all elements in the circular queue.
Steps:
If front == -1, the queue is empty.
Else, start from front and move to rear using modular arithmetic:

| 5
|
CO4, SO1,BL2
| d.
| An e-commerce platform sorts items by price and updates the list frequently, would Insertion Sort be efficient here? Explain.

Ans: Yes, Insertion Sort is efficient for an e-commerce price list that is updated frequently because it performs very well on nearly sorted data, allowing fast insertion of new prices without re-sorting the entire list.
| 5
|
Q2
| A
| Boxes are stacked vertically in a warehouse. Only the topmost box can be removed at a time.
Question:
Write a program to simulate warehouse management where:
Each box has an ID number.
Add a new box (PUSH).
Remove the top box (POP).
Display current stack of boxes.
Ans : Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks

#include <iostream>
using namespace std;

// Structure to represent a box (node)
struct Box {
int boxID;
Box* next;   // pointer to the box below it
};

// Pointer to the top of the stack
Box* topBox = nullptr;

// Function to add a new box (PUSH)
void pushBox(int id) {
Box* newBox = new Box();
newBox->boxID = id;
newBox->next = topBox;   // new box goes on top of current stack
topBox = newBox;
cout << "Box with ID " << id << " added to the stack.\n";
}

// Function to remove the topmost box (POP)
void popBox() {
if (topBox == nullptr) {
cout << "No boxes to remove! Stack is empty.\n";
return;
}

Box* temp = topBox;
cout << "Box with ID " << topBox->boxID << " removed from the stack.\n";
topBox = topBox->next;   // move to next box
delete temp;   // free memory
}

// Function to display all boxes in the stack
void displayBoxes() {
if (topBox == nullptr) {
cout << "No boxes in the warehouse.\n";
return;
}

cout << "Current stack of boxes (top to bottom):\n";
Box* temp = topBox;
while (temp != nullptr) {
cout << "Box ID: " << temp->boxID << endl;
temp = temp->next;
}
}

// Main function
int main() {
int choice, id;

cout << "===== Warehouse Box Management using Stack =====\n";

while (true) {
cout << "\n1. Add a new box (PUSH)";
cout << "\n2. Remove top box (POP)";
cout << "\n3. Display all boxes";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;

switch (choice) {
case 1:
cout << "Enter Box ID to add: ";
cin >> id;
pushBox(id);
break;

case 2:
popBox();
break;

case 3:
displayBoxes();
break;

case 4:
cout << "Exiting Program. Thank You!\n";
return 0;

default:
cout << "Invalid choice! Please try again.\n";
}
}

return 0;
}
| [10]
|

| B
| Write a program to store details of bank customers: Account Number, Name, and Balance. The program should display customers having a balance less than ₹1000.
Ans: Structure declaration(2)+input(3)+computing per(3)+display(2)

#include <iostream>
#include <string>
using namespace std;

// Structure definition
struct Customer {
int accountNumber;
string name;
float balance;
};

int main() {
int n;
cout << "Enter number of customers: ";
cin >> n;

// Array of structures
Customer customers[n];

// Input details
for (int i = 0; i < n; i++) {
cout << "\nEnter details for customer " << i + 1 << ":\n";
cout << "Account Number: ";
cin >> customers[i].accountNumber;
cin.ignore(); // To handle newline after integer input
cout << "Name: ";
getline(cin, customers[i].name);
cout << "Balance: ";
cin >> customers[i].balance;
}

// Display customers with balance < 1000
cout << "\n--- Customers having balance less than 1000 ---\n";
bool found = false;
for (int i = 0; i < n; i++) {
if (customers[i].balance < 1000) {
cout << "Account No: " << customers[i].accountNumber << "\n";
cout << "Name: " << customers[i].name << "\n";
cout << "Balance: " << customers[i].balance << "\n\n";
found = true;
}
}

if (!found) {
cout << "No customers with balance less than 1000.\n";
}

return 0;
}

| [10]

|
Q3
| A
| Explain different applications of stack data structure. Convert the given infix expression into postfix using stack.
(A + B) * C + D / (B + A * C) + D
Ans:
Applications of Stack: (4 marks)
Expression Conversion and Evaluation
Used to convert infix expressions (e.g., A + B) into postfix (AB+) or prefix (+AB) form.
Also used to evaluate postfix or prefix expressions efficiently.
Function Call Management
Stack is used to store return addresses, parameters, and local variables when functions are called.
The function call stack ensures that after a function finishes, control returns to the correct place.
Undo/Redo Operations
Applications like text editors, graphics software, and IDEs use stacks to store the previous states of actions.
Undo pops the last action, and redo pushes it back.
Backtracking Algorithms
Used in maze solving, puzzles (like Sudoku), and recursion — to remember previous steps and backtrack when necessary.
Parentheses Matching / Syntax Checking
Used in compilers or expression validation to check balanced parentheses ((), {}, []).
Memory Management
Stack memory is used during program execution for temporary storage (function calls, local variables, etc.).
Conversion: 6 marks
Ans: AB+C*DBAC*+/+D+

| [10]
|

| B
| At a ticket counter, people stand in a line to buy tickets. Implement a linear queue to simulate the process where people arrive and are served in the order they came. Track the total number of people served.
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks

#include <iostream>
using namespace std;

#define MAX 100   // maximum queue size

class TicketQueue {
private:
int queue[MAX];
int front, rear;
int servedCount;   // to track total people served

public:
// Constructor
TicketQueue() {
front = -1;
rear = -1;
servedCount = 0;
}
// Function to check if queue is full
bool isFull() {
return (rear == MAX - 1);
}
// Function to check if queue is empty
bool isEmpty() {
return (front == -1 || front > rear);
}
// Function to add person to queue
void enqueue(int personID) {
if (isFull()) {
cout << "Queue is full! Cannot add more people.\n";
return;
}
if (front == -1) front = 0;
queue[++rear] = personID;
cout << "Person " << personID << " joined the queue.\n";
}
// Function to serve person (dequeue)
void dequeue() {
if (isEmpty()) {
cout << "Queue is empty! No one to serve.\n";
return;
}
cout << "Person " << queue[front] << " has been served.\n";
front++;
servedCount++;
}

// Function to display current queue
void displayQueue() {
if (isEmpty()) {
cout << "Queue is empty.\n";
return;
}
cout << "Current queue: ";
for (int i = front; i <= rear; i++) {
cout << queue[i] << " ";
}
cout << endl;
}
// Function to show total served people
void showServedCount() {
cout << "Total number of people served: " << servedCount << endl;
}
};
// -------------------- Main Function --------------------
int main() {
TicketQueue tq;
int choice, id = 1;

cout << "=== Ticket Counter Simulation Using Linear Queue ===\n";
do {
cout << "\nMenu:\n";
cout << "1. Add Person to Queue\n";
cout << "2. Serve Person\n";
cout << "3. Display Queue\n";
cout << "4. Show Total People Served\n";
cout << "5. Exit\n";
cout << "Enter your choice: ";
cin >> choice;

switch (choice) {
case 1:
tq.enqueue(id++);
break;
case 2:
tq.dequeue();
break;
case 3:
tq.displayQueue();
break;
case 4:
tq.showServedCount();
break;
case 5:
cout << "Exiting... Thank you!\n";
break;
default:
cout << "Invalid choice! Try again.\n";
}
} while (choice != 5);

return 0;
}
cin >> choice;

switch (choice) {
case 1:
tq.enqueue(id++);
break;
case 2:
tq.dequeue();
break;
case 3:
tq.displayQueue();
break;
case 4:
tq.showServedCount();
break;
case 5:
cout << "Exiting... Thank you!\n";
break;
default:
cout << "Invalid choice! Try again.\n";
}
} while (choice != 5);

return 0;
}

| [10]
|
Q4
CO3, SO2, BL3
| A
| Imagine a train where each coach is represented as a node in a linked list. Write a Program to :
Represent this train structure using a linked list.
To add a new coach at the front of the train.
To delete a coach from a given position in the linked list.
Display the current coaches.
Ans:
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks

#include <iostream>
using namespace std;

// Structure to represent each coach (node) in the train
struct Coach {
int coachNumber;   // Data part: Coach ID/Number
Coach* next;   // Pointer to the next coach
};

// Function to add a new coach at the front
void addCoachFront(Coach*& head, int number) {
Coach* newCoach = new Coach();   // Create new node
newCoach->coachNumber = number;
newCoach->next = head;   // Point new node to current head
head = newCoach;   // Move head to new node
cout << "Coach " << number << " added at the front of the train.\n";
}

// Function to delete a coach from a given position
void deleteCoachAtPosition(Coach*& head, int position) {
if (head == nullptr) {
cout << "Train is empty. No coach to delete.\n";
return;
}

Coach* temp = head;

// Case 1: Delete first coach
if (position == 1) {
head = head->next;
cout << "Coach " << temp->coachNumber << " removed from position 1.\n";
delete temp;
return;
}

// Traverse to the (position - 1)th coach
for (int i = 1; temp != nullptr && i < position - 1; i++) {
temp = temp->next;
}

// If position is invalid
if (temp == nullptr || temp->next == nullptr) {
cout << "Invalid position. No coach deleted.\n";
return;
}

// Node to be deleted
Coach* nodeToDelete = temp->next;
temp->next = nodeToDelete->next;

cout << "Coach " << nodeToDelete->coachNumber << " removed from position " << position << ".\n";
delete nodeToDelete;
}

// Function to display all coaches in the train
void displayTrain(Coach* head) {
if (head == nullptr) {
cout << "No coaches in the train.\n";
return;
}

cout << "Current Train Coaches: ";
while (head != nullptr) {
cout << "[Coach " << head->coachNumber << "] -> ";
head = head->next;
}
cout << "NULL\n";
}

// Main function
int main() {
Coach* head = nullptr;   // Initially, no coaches in the train
int choice, number, pos;

cout << "====== Train Coaches Management System ======\n";

while (true) {
cout << "\n1. Add a New Coach at Front";
cout << "\n2. Delete a Coach from a Given Position";
cout << "\n3. Display Train Coaches";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;

switch (choice) {
case 1:
cout << "Enter Coach Number to Add: ";
cin >> number;
addCoachFront(head, number);
break;

case 2:
cout << "Enter Position to Delete Coach: ";
cin >> pos;
deleteCoachAtPosition(head, pos);
break;

case 3:
displayTrain(head);
break;

case 4:
cout << "Exiting Program. Thank You!\n";
return 0;

default:
cout << "Invalid choice! Please try again.\n";
}
}

return 0;
}

| [10]
|
CO4, SO3,BL4
| B
| Write a C++ program to perform Selection Sort on a list of numbers entered by the user. Apply the Selection Sort algorithm to arrange the following numbers in ascending order and show the array after each pass : 25, 16, 5, 81, 27, 63, 8

Ans: Marks:
Program: 5 marks
Solution : 5 marks
#include <iostream>
using namespace std;

int main() {
int n = 7;
int arr[] = {25, 16, 5, 81, 27, 63, 8};

cout << "Original Array: ";
for (int i = 0; i < n; i++)
cout << arr[i] << " ";
cout << "\n\n--- Selection Sort Process ---\n";

// Selection Sort Algorithm
for (int i = 0; i < n - 1; i++) {
int minIndex = i;

// Find index of minimum element in unsorted part
for (int j = i + 1; j < n; j++) {
if (arr[j] < arr[minIndex])
minIndex = j;
}

// Swap smallest found with first unsorted element
int temp = arr[i];
arr[i] = arr[minIndex];
arr[minIndex] = temp;

// Display array after each pass
cout << "Pass " << i + 1 << ": ";
for (int k = 0; k < n; k++)
cout << arr[k] << " ";
cout << endl;
}

cout << "\nSorted Array (Ascending Order): ";
for (int i = 0; i < n; i++)
cout << arr[i] << " ";
cout << endl;

return 0;
}
| [10]
|
Q5
CO3, SO2,BL5
| A
| Write a program in C++ to implement a Queue using a Linked List that supports the following operations:
Enqueue: Add an element to the rear of the queue
Dequeue: Remove an element from the front of the queue
Display: Show all the elements of the queue
Ans:
Marks: Structure/class declaration: 2 marks
Functions : 6 marks
Main: 2 marks

#include <iostream>
using namespace std;

// Structure to represent a node in the queue
struct Node {
int data;
Node* next;
};

// Front and Rear pointers for the queue
Node* front = nullptr;
Node* rear = nullptr;

// Function to add an element to the rear of the queue
void enqueue(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->next = nullptr;

if (rear == nullptr) {   // Queue is empty
front = rear = newNode;
cout << "Enqueued: " << value << endl;
return;
}

// Add new node at the end and update rear
rear->next = newNode;
rear = newNode;
cout << "Enqueued: " << value << endl;
}

// Function to remove an element from the front of the queue
void dequeue() {
if (front == nullptr) {
cout << "Queue is empty! Cannot dequeue.\n";
return;
}

Node* temp = front;
cout << "Dequeued: " << front->data << endl;

front = front->next;

// If queue becomes empty after dequeue
if (front == nullptr)
rear = nullptr;

delete temp; // Free memory
}

// Function to display all elements in the queue
void display() {
if (front == nullptr) {
cout << "Queue is empty.\n";
return;
}

Node* temp = front;
cout << "Queue Elements: ";
while (temp != nullptr) {
cout << temp->data << " ";
temp = temp->next;
}
cout << endl;
}

// Main function
int main() {
int choice, value;

cout << "====== Queue Implementation using Linked List (Structure) ======\n";

while (true) {
cout << "\n1. Enqueue (Add Element)";
cout << "\n2. Dequeue (Remove Element)";
cout << "\n3. Display Queue";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;

switch (choice) {
case 1:
cout << "Enter value to enqueue: ";
cin >> value;
enqueue(value);
break;

case 2:
dequeue();
break;

case 3:
display();
break;

case 4:
cout << "Exiting Program. Thank You!\n";
return 0;

default:
cout << "Invalid choice! Please try again.\n";
}
}

return 0;
}

| [10]
|

| B
| What is dynamic memory allocation? Explain with example. Write a C/C++ program to print Fibonacci series using recursive function.
Ans:
Explanation 4 marks
Program 6 marks
#include <iostream>
using namespace std;
// Recursive function to find nth Fibonacci term
int fibonacci(int n) {
if (n == 0)
return 0;
else if (n == 1)
return 1;
else
return fibonacci(n - 1) + fibonacci(n - 2);
}
int main() {
int n;
cout << "Enter number of terms: ";
cin >> n;
cout << "Fibonacci Series: ";
for (int i = 0; i < n; i++) {
cout << fibonacci(i) << " ";
}
cout << endl;
return 0;
}
| [10]
|

Q6

| A
| An array AR [-4…6,-2…12] stores elements in Row Major Wise, with the address AR[2][3] as 4142. If each element requires 2 bytes of storage, find the Base address.
Ans:
4142=Base+((2+4)×15+(3+2))×2
4142=𝐵𝑎𝑠𝑒+((6×15)+5)×2
4142=𝐵𝑎𝑠𝑒+(90+5)×2
4142=𝐵𝑎𝑠𝑒+(95×2)
4142=Base+190
Base=4142−190=3952

Write a program in   to compute the sum of all elements in an array using pointers.
Ans: #include <stdio.h>

int main() {
// Declaring variables
int arr1[10];
int i, n, sum = 0;
int *pt;
// Displaying the purpose of the program
printf("\n\n Pointer : Sum of all elements in an array :\n");

// Inputting the number of elements for the array (maximum 10)
printf(" Input the number of elements to store in the array (max 10) : ");
scanf("%d", &n);

// Inputting elements into the array
printf(" Input %d number of elements in the array : \n", n);
for (i = 0; i < n; i++) {
printf(" element - %d : ", i + 1);
scanf("%d", &arr1[i]);
}

pt = arr1; // pt stores the base address of array arr1

// Calculating the sum of array elements using pointer
for (i = 0; i < n; i++) {
sum = sum + *pt; // Adding the value pointed by pt to the sum
pt++; // Moving the pointer to the next element of the array
}

// Displaying the sum of the array elements
printf(" The sum of array is : %d\n\n", sum);
}
| [10]
|
CO3, SO2,BL4
| B
| Explain how forward and backward traversal is possible in a doubly linked list.
Write a program to implement a Doubly Linked List supporting the following operations:
Insert at Beginning – Add a new node at the start of the list.
Delete a Node – Delete a node with a given value.
Display Forward and Backward – Traverse and display the list from both directions.
Ans : (Explanation : 2 marks+ Program -8 marks)

Each node has two links: prev (to the previous node) and next (to the next node).
Forward traversal: start from head, repeatedly do ptr = ptr->next until nullptr.
Backward traversal: first reach the tail by moving next until nullptr, then move back with ptr = ptr->prev until nullptr.
#include <iostream>
using namespace std;

struct Node {
int data;
Node* prev;
Node* next;
};

Node* head = nullptr;   // start of the list

// 1) Insert at Beginning
void insertAtBeginning(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->prev = nullptr;
newNode->next = head;

if (head != nullptr) head->prev = newNode;
head = newNode;
cout << "Inserted " << value << " at beginning.\n";
}

// 2) Delete first node with given value
void deleteByValue(int value) {
if (!head) { cout << "List is empty.\n"; return; }

Node* cur = head;
while (cur && cur->data != value) cur = cur->next;

if (!cur) { cout << "Value " << value << " not found.\n"; return; }

// If cur is head
if (cur == head) {
head = cur->next;
if (head) head->prev = nullptr;
cout << "Deleted " << cur->data << ".\n";
delete cur;
return;
}

// Middle or tail
if (cur->prev) cur->prev->next = cur->next;
if (cur->next) cur->next->prev = cur->prev;

cout << "Deleted " << cur->data << ".\n";
delete cur;
}

// 3a) Display forward
void displayForward() {
if (!head) { cout << "List is empty.\n"; return; }
cout << "Forward : ";
for (Node* p = head; p != nullptr; p = p->next)
cout << p->data << (p->next ? " <-> " : " -> NULL\n");
}

// 3b) Display backward
void displayBackward() {
if (!head) { cout << "List is empty.\n"; return; }
// Go to tail
Node* tail = head;
while (tail->next) tail = tail->next;

cout << "Backward: ";
for (Node* p = tail; p != nullptr; p = p->prev)
cout << p->data << (p->prev ? " <-> " : " -> NULL\n");
}

int main() {
int choice, val;

cout << "===== Doubly Linked List =====\n";
while (true) {
cout << "\n1. Insert at Beginning"
<< "\n2. Delete a Node (by value)"
<< "\n3. Display Forward"
<< "\n4. Display Backward"
<< "\n5. Exit"
<< "\nEnter your choice: ";
if (!(cin >> choice)) return 0;

switch (choice) {
case 1:
cout << "Enter value: ";
cin >> val;
insertAtBeginning(val);
break;
case 2:
cout << "Enter value to delete: ";
cin >> val;
deleteByValue(val);
break;
case 3:
displayForward();
break;
case 4:
displayBackward();
break;
case 5:
cout << "Exiting...\n";
return 0;
default:
cout << "Invalid choice. Try again.\n";
}
}
}

| [10]
|
Q7

| A
| In a restaurant, customers place orders that are processed in the order they are received. Write a Program to design a restaurant order management system using a circular queue. Orders are processed on a first-come, first-served basis.
Ans:
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks

#include <iostream>
#include <string>
using namespace std;

// Structure to represent each order
struct Order {
int orderID;
string customerName;
};

// Structure for Circular Queue
struct CircularQueue {
Order orders[50];   // Maximum 50 orders
int front;
int rear;
int size;
};

// Function to initialize the queue
void initializeQueue(CircularQueue &q, int n) {
q.size = n;
q.front = -1;
q.rear = -1;
}

// Function to check if queue is full
bool isFull(CircularQueue q) {
return ((q.front == 0 && q.rear == q.size - 1) || (q.front == q.rear + 1));
}

// Function to check if queue is empty
bool isEmpty(CircularQueue q) {
return (q.front == -1);
}

// Function to place a new order (Enqueue)
void placeOrder(CircularQueue &q, int id, string name) {
if (isFull(q)) {
cout << "⚠️ Cannot place new order. Queue is full!\n";
return;
}

// First order
if (q.front == -1)
q.front = 0;

// Circular increment
q.rear = (q.rear + 1) % q.size;
q.orders[q.rear].orderID = id;
q.orders[q.rear].customerName = name;

cout << "Order placed successfully! [Order ID: "
<< id << ", Customer: " << name << "]\n";
}

// Function to serve an order (Dequeue)
void serveOrder(CircularQueue &q) {
if (isEmpty(q)) {
cout << "No pending orders to serve.\n";
return;
}

cout << "Serving Order ID: " << q.orders[q.front].orderID
<< " | Customer: " << q.orders[q.front].customerName << endl;

// Only one order left
if (q.front == q.rear) {
q.front = q.rear = -1;
} else {
q.front = (q.front + 1) % q.size;
}
}

// Function to display all pending orders
void displayOrders(CircularQueue q) {
if (isEmpty(q)) {
cout << "No pending orders.\n";
return;
}

cout << "\n Current Pending Orders (Front → Rear):\n";
int i = q.front;
while (true) {
cout << "Order ID: " << q.orders[i].orderID
<< " | Customer: " << q.orders[i].customerName << endl;

if (i == q.rear) break;
i = (i + 1) % q.size;
}
}

// Main function
int main() {
CircularQueue q;
int maxOrders;
cout << "Enter maximum number of orders the restaurant can handle: ";
cin >> maxOrders;
initializeQueue(q, maxOrders);

int choice, id;
string name;

cout << "\n====== Restaurant Order Management System (Circular Queue) ======\n";

while (true) {
cout << "\n1. Place New Order (Enqueue)"
<< "\n2. Serve Order (Dequeue)"
<< "\n3. Display Pending Orders"
<< "\n4. Exit"
<< "\nEnter your choice: ";
cin >> choice;

switch (choice) {
case 1:
cout << "Enter Order ID: ";
cin >> id;
cout << "Enter Customer Name: ";
cin.ignore();
getline(cin, name);
placeOrder(q, id, name);
break;

case 2:
serveOrder(q);
break;

case 3:
displayOrders(q);
break;

case 4:
cout << "Exiting system... Thank you!\n";
return 0;

default:
cout << "Invalid choice! Please try again.\n";
}
}

return 0;
}

| [10]
|
CO4, SO2,BL4
| B
| Explain the working principle of Binary Search algorithm.
You are developing a student record system where data (roll numbers) must be first sorted before performing a quick search.
Write a program that performs the following tasks using arrays:
Accept n roll numbers from the user.
Sort them in ascending order using Bubble Sort.
Perform a Binary Search to find a given roll number.
Display suitable messages for “Record Found” or “Record Not Found.”
Ans: working of Binary search (4 marks)

Program ( 6 marks )

#include <iostream>
using namespace std;

// Function to perform Bubble Sort
void bubbleSort(int arr[], int n) {
for (int i = 0; i < n - 1; i++) {
bool swapped = false;
for (int j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
int temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
swapped = true;
}
}
if (!swapped) break;   // Optimization for already sorted data
}
}

// Function to perform Binary Search
int binarySearch(int arr[], int n, int key) {
int low = 0, high = n - 1;

while (low <= high) {
int mid = (low + high) / 2;

if (arr[mid] == key)
return mid;   // Record found
else if (arr[mid] < key)
low = mid + 1;   // Search right half
else
high = mid - 1; // Search left half
}

return -1; // Record not found
}

int main() {
int n;

cout << "Enter number of students: ";
cin >> n;

int roll[n];
cout << "Enter " << n << " roll numbers:\n";
for (int i = 0; i < n; i++)
cin >> roll[i];

// Step 1: Sort roll numbers using Bubble Sort
bubbleSort(roll, n);

cout << "\nRoll numbers after sorting: ";
for (int i = 0; i < n; i++)
cout << roll[i] << " ";
cout << endl;

// Step 2: Search for a roll number using Binary Search
int key;
cout << "\nEnter roll number to search: ";
cin >> key;

int result = binarySearch(roll, n, key);

// Step 3: Display result
if (result != -1)
cout << " Record Found at position: " << result + 1 << endl;
else
cout << "Record Not Found.\n";

return 0;
}
| [10]
|
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper d6e370f47452

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/Integrated_Computer_7032/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (40 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Basic Data Structures
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 40 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions are to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Assume suitable data if necessary
Q1
Answer briefly:   Marks
a.   Differentiate between a stack and a queue data
structure.
Ans:
Stack   Queue
Stack is a linear data
Queue is a linear data stru
structure where data is
where data is ended at th
added and removed from the
and removed from the fro
top.
Stack is based on LIFO(Last Queue is based on FIFO(F
In First Out) principle   First Out) principle   5
Insertion operation in Stack is Insertion operation in Qu
known as push.   known as eneque.
Delete operation in Stack is   Delete operation in Queu
known as pop.   known as dequeue.
Only one pointer is available Two pointers are available
for both addition and   addition and deletion: fro
deletion: top()   rear()
Used in solving recursive   Used in solving sequentia
problems   processing problems
b. What will be the output of the following program?
#include <iostream>   5
using namespace std;
********** 1 **********
--- page 2 ---
int main()
{
int num[5];
int* p;
p = num;
*p = 10;
p++;
*p = 20;
p = &num[2];
*p = 30;
p = num + 3;
*p = 40;
p = num;
*(p + 4) = 50;
for (int i = 0; i < 5; i++)
cout << num[i] << ", ";
return 0;
}
Ans: 10, 20, 30, 40, 50,
CO-3 ;   c.   Explain the algorithmic steps for performing
SO-2 ;
BL-2   different operations on a Circular Queue.
(Each 1 marks)
1. IsEmpty
Purpose: To check whether the queue is empty.   5
Condition:
If front == -1, then queue is empty.
2. IsFull
Purpose: To check whether the queue is full.
Condition:
If (front == (rear + 1) % MAX), then queue is full.
********** 2 **********
--- page 3 ---
3. Enqueue (Insertion)
Purpose: To insert an element at the rear of the queue.
Steps:
1. Check for overflow:
o   If (front == 0 && rear == MAX - 1)
OR (rear + 1) % MAX == front,
the queue is full.
2. If the queue is empty (front == -1):
o Set front = 0 and rear = 0.
3. Otherwise:
o Move rear circularly → rear = (rear
+ 1) % MAX.
4. Insert the new element at queue[rear].
4. Dequeue (Deletion)
Purpose: To remove an element from the front of the
queue.
Steps:
1. Check for underflow:
o   If front == -1, queue is empty.
2. Retrieve the element at queue[front].
3. If front == rear, it means only one element
was present:
o Set both front = -1 and rear = -1
(queue becomes empty).
4. Otherwise:
o Move front circularly → front =
(front + 1) % MAX.
5. Display
Purpose: To display all elements in the circular queue.
Steps:
1. If front == -1, the queue is empty.
2. Else, start from front and move to rear using
modular arithmetic:
CO4,   d. An e-commerce platform sorts items by price and
SO1,BL
updates the list frequently, would Insertion Sort be
2   5
efficient here? Explain.
********** 3 **********
--- page 4 ---
Ans: Yes, Insertion Sort is efficient for an e-
commerce price list that is updated frequently
because it performs very well on nearly sorted data,
allowing fast insertion of new prices without re-
sorting the entire list.
A   Boxes are stacked vertically in a warehouse. Only the
topmost box can be removed at a time.
Question:
Write a program to simulate warehouse management
where:
i. Each box has an ID number.
ii. Add a new box (PUSH).
iii. Remove the top box (POP).
iv. Display current stack of boxes.
Ans : Ans: Marks: Structure/class declaration: 2
marks
Function : 6 marks
Main: 2 marks
Q2   [10]
#include <iostream>
using namespace std;
// Structure to represent a box (node)
struct Box {
int boxID;
Box* next; // pointer to the box below it
};
// Pointer to the top of the stack
********** 4 **********
--- page 5 ---
Box* topBox = nullptr;
// Function to add a new box (PUSH)
void pushBox(int id) {
Box* newBox = new Box();
newBox->boxID = id;
newBox->next = topBox; // new box goes on
top of current stack
topBox = newBox;
cout << "Box with ID " << id << " added to the
stack.\n";
}
// Function to remove the topmost box (POP)
void popBox() {
if (topBox == nullptr) {
cout << "No boxes to remove! Stack is
empty.\n";
return;
}
Box* temp = topBox;
cout << "Box with ID " << topBox->boxID <<
" removed from the stack.\n";
topBox = topBox->next; // move to next box
delete temp;   // free memory
********** 5 **********
--- page 6 ---
}
// Function to display all boxes in the stack
void displayBoxes() {
if (topBox == nullptr) {
cout << "No boxes in the warehouse.\n";
return;
}
cout << "Current stack of boxes (top to
bottom):\n";
Box* temp = topBox;
while (temp != nullptr) {
cout << "Box ID: " << temp->boxID <<
endl;
temp = temp->next;
}
}
// Main function
int main() {
int choice, id;
cout << "===== Warehouse Box Management
using Stack =====\n";
********** 6 **********
--- page 7 ---
while (true) {
cout << "\n1. Add a new box (PUSH)";
cout << "\n2. Remove top box (POP)";
cout << "\n3. Display all boxes";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter Box ID to add: ";
cin >> id;
pushBox(id);
break;
case 2:
popBox();
break;
case 3:
displayBoxes();
break;
case 4:
********** 7 **********
--- page 8 ---
cout << "Exiting Program. Thank You!\n";
return 0;
default:
cout << "Invalid choice! Please try
again.\n";
}
}
return 0;
}
B   Write a program to store details of bank
customers: Account Number, Name, and Balance.
The program should display customers having a
balance less than ₹1000.
Ans: Structure declaration(2)+input(3)+computing
per(3)+display(2)
#include <iostream>
#include <string>   [10]
using namespace std;
// Structure definition
struct Customer {
int accountNumber;
string name;
float balance;
};
********** 8 **********
--- page 9 ---
int main() {
int n;
cout << "Enter number of customers: ";
cin >> n;
// Array of structures
Customer customers[n];
// Input details
for (int i = 0; i < n; i++) {
cout << "\nEnter details for customer " << i +
1 << ":\n";
cout << "Account Number: ";
cin >> customers[i].accountNumber;
cin.ignore(); // To handle newline after
integer input
cout << "Name: ";
getline(cin, customers[i].name);
cout << "Balance: ";
cin >> customers[i].balance;
}
// Display customers with balance < 1000
cout << "\n--- Customers having balance less
than 1000 ---\n";
bool found = false;
for (int i = 0; i < n; i++) {
if (customers[i].balance < 1000) {
cout << "Account No: " <<
customers[i].accountNumber << "\n";
********** 9 **********
--- page 10 ---
cout << "Name: " << customers[i].name
<< "\n";
cout << "Balance: " <<
customers[i].balance << "\n\n";
found = true;
}
}
if (!found) {
cout << "No customers with balance less
than 1000.\n";
}
return 0;
}
A   Explain different applications of stack data [10]
structure. Convert the given infix expression into
postfix using stack.
(A + B) * C + D / (B + A * C) + D
Ans:
Applications of Stack: (4 marks)
1. Expression Conversion and Evaluation
Q3   o Used to convert infix expressions (e.g., A +
B) into postfix (AB+) or prefix (+AB) form.
o Also used to evaluate postfix or prefix
expressions efficiently.
2. Function Call Management
o Stack is used to store return addresses,
parameters, and local variables when
functions are called.
o The function call stack ensures that after a
function finishes, control returns to the
correct place.
3. Undo/Redo Operations
********** 10 **********
--- page 11 ---
o Applications like text editors, graphics
software, and IDEs use stacks to store the
previous states of actions.
o Undo pops the last action, and redo pushes
it back.
4. Backtracking Algorithms
o Used in maze solving, puzzles (like
Sudoku), and recursion — to remember
previous steps and backtrack when
necessary.
5. Parentheses Matching / Syntax Checking
o Used in compilers or expression validation
to check balanced parentheses ((), {},
[]).
6. Memory Management
o Stack memory is used during program
execution for temporary storage (function
calls, local variables, etc.).
Conversion: 6 marks
Ans: AB+C*DBA*+/+D+
B   At a ticket counter, people stand in a line to buy tickets. [10]
Implement a linear queue to simulate the process where
people arrive and are served in the order they came. Track
the total number of people served.
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks
#include <iostream>
using namespace std;
#define MAX 100 // maximum queue size
class TicketQueue {
private:
int queue[MAX];
int front, rear;
int servedCount; // to track total people served
********** 11 **********
--- page 12 ---
public:
// Constructor
TicketQueue() {
front = -1;
rear = -1;
servedCount = 0;
}
// Function to check if queue is full
bool isFull() {
return (rear == MAX - 1);
}
// Function to check if queue is empty
bool isEmpty() {
return (front == -1 || front > rear);
}
// Function to add person to queue
void enqueue(int personID) {
if (isFull()) {
cout << "Queue is full! Cannot add more
people.\n";
return;
}
if (front == -1) front = 0;
queue[++rear] = personID;
cout << "Person " << personID << " joined the
queue.\n";
}
// Function to serve person (dequeue)
void dequeue() {
if (isEmpty()) {
cout << "Queue is empty! No one to serve.\n";
return;
}
cout << "Person " << queue[front] << " has been
served.\n";
********** 12 **********
--- page 13 ---
front++;
servedCount++;
}
// Function to display current queue
void displayQueue() {
if (isEmpty()) {
cout << "Queue is empty.\n";
return;
}
cout << "Current queue: ";
for (int i = front; i <= rear; i++) {
cout << queue[i] << " ";
}
cout << endl;
}
// Function to show total served people
void showServedCount() {
cout << "Total number of people served: " <<
servedCount << endl;
}
};
// -------------------- Main Function --------------------
int main() {
TicketQueue tq;
int choice, id = 1;
cout << "=== Ticket Counter Simulation Using Linear
Queue ===\n";
do {
cout << "\nMenu:\n";
cout << "1. Add Person to Queue\n";
cout << "2. Serve Person\n";
cout << "3. Display Queue\n";
cout << "4. Show Total People Served\n";
********** 13 **********
--- page 14 ---
cout << "5. Exit\n";
cout << "Enter your choice: ";
cin >> choice;
switch (choice) {
case 1:
tq.enqueue(id++);
break;
case 2:
tq.dequeue();
break;
case 3:
tq.displayQueue();
break;
case 4:
tq.showServedCount();
break;
case 5:
cout << "Exiting... Thank you!\n";
break;
default:
cout << "Invalid choice! Try again.\n";
}
} while (choice != 5);
return 0;
}
cin >> choice;
switch (choice) {
case 1:
tq.enqueue(id++);
break;
case 2:
tq.dequeue();
********** 14 **********
--- page 15 ---
break;
case 3:
tq.displayQueue();
break;
case 4:
tq.showServedCount();
break;
case 5:
cout << "Exiting... Thank you!\n";
break;
default:
cout << "Invalid choice! Try again.\n";
}
} while (choice != 5);
return 0;
}
A   Imagine a train where each coach is represented as [10]
a node in a linked list. Write a Program to :
i. Represent this train structure using a linked
list.
ii. To add a new coach at the front of the
train.
iii. To delete a coach from a given position in
the linked list.
Q4   iv. Display the current coaches.
CO3,
SO2,   Ans:
BL3
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks
#include <iostream>
********** 15 **********
--- page 16 ---
using namespace std;
// Structure to represent each coach (node) in the
train
struct Coach {
int coachNumber;   // Data part: Coach
ID/Number
Coach* next;   // Pointer to the next coach
};
// Function to add a new coach at the front
void addCoachFront(Coach*& head, int number) {
Coach* newCoach = new Coach(); // Create new
node
newCoach->coachNumber = number;
newCoach->next = head;   // Point new node
to current head
head = newCoach;   // Move head to new
node
cout << "Coach " << number << " added at the
front of the train.\n";
}
// Function to delete a coach from a given position
void deleteCoachAtPosition(Coach*& head, int
position) {
if (head == nullptr) {
cout << "Train is empty. No coach to
delete.\n";
return;
********** 16 **********
--- page 17 ---
}
Coach* temp = head;
// Case 1: Delete first coach
if (position == 1) {
head = head->next;
cout << "Coach " << temp->coachNumber <<
" removed from position 1.\n";
delete temp;
return;
}
// Traverse to the (position - 1)th coach
for (int i = 1; temp != nullptr && i < position -
1; i++) {
temp = temp->next;
}
// If position is invalid
if (temp == nullptr || temp->next == nullptr) {
cout <<   "Invalid   position. No coach
deleted.\n";
return;
}
// Node to be deleted
Coach* nodeToDelete = temp->next;
temp->next = nodeToDelete->next;
********** 17 **********
--- page 18 ---
cout <<   "Coach   " <<   nodeToDelete-
>coachNumber << " removed from position " <<
position << ".\n";
delete nodeToDelete;
}
// Function to display all coaches in the train
void displayTrain(Coach* head) {
if (head == nullptr) {
cout << "No coaches in the train.\n";
return;
}
cout << "Current Train Coaches: ";
while (head != nullptr) {
cout << "[Coach " << head->coachNumber <<
"] -> ";
head = head->next;
}
cout << "NULL\n";
}
// Main function
int main() {
Coach* head = nullptr;   // Initially, no coaches
in the train
int choice, number, pos;
cout << "====== Train Coaches Management
System ======\n";
********** 18 **********
--- page 19 ---
while (true) {
cout << "\n1. Add a New Coach at Front";
cout << "\n2. Delete a Coach from a Given
Position";
cout << "\n3. Display Train Coaches";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter Coach Number to Add: ";
cin >> number;
addCoachFront(head, number);
break;
case 2:
cout << "Enter Position to Delete Coach: ";
cin >> pos;
deleteCoachAtPosition(head, pos);
break;
case 3:
displayTrain(head);
break;
case 4:
cout << "Exiting Program. Thank You!\n";
return 0;
********** 19 **********
--- page 20 ---
default:
cout << "Invalid choice! Please   try
again.\n";
}
}
return 0;
}
B   Write a C++ program to perform Selection Sort on [10]
a list of numbers entered by the user. Apply the
Selection Sort algorithm to arrange the following
numbers in ascending order and show the array
after each pass : 25, 16, 5, 81, 27, 63, 8
Ans: Marks:
Program: 5 marks
CO4,
Solution : 5 marks
SO3,BL
#include <iostream>
4
using namespace std;
int main() {
int n = 7;
int arr[] = {25, 16, 5, 81, 27, 63, 8};
cout << "Original Array: ";
for (int i = 0; i < n; i++)
cout << arr[i] << " ";
********** 20 **********
--- page 21 ---
cout << "\n\n--- Selection Sort Process ---\n";
// Selection Sort Algorithm
for (int i = 0; i < n - 1; i++) {
int minIndex = i;
// Find index of minimum element in unsorted
part
for (int j = i + 1; j < n; j++) {
if (arr[j] < arr[minIndex])
minIndex = j;
}
// Swap smallest found with first unsorted
element
int temp = arr[i];
arr[i] = arr[minIndex];
arr[minIndex] = temp;
// Display array after each pass
cout << "Pass " << i + 1 << ": ";
for (int k = 0; k < n; k++)
cout << arr[k] << " ";
cout << endl;
}
cout << "\nSorted Array (Ascending Order): ";
for (int i = 0; i < n; i++)
cout << arr[i] << " ";
cout << endl;
********** 21 **********
--- page 22 ---
return 0;
}
A   Write a program in C++ to implement a Queue   [10]
using a Linked List that supports the following
operations:
i. Enqueue: Add an element to the rear of the
queue
ii. Dequeue: Remove an element from the front
of the queue
iii. Display: Show all the elements of the queue
Ans:
Marks: Structure/class declaration: 2 marks
Functions : 6 marks
Main: 2 marks
Q5
#include <iostream>
CO3,
SO2,BL   using namespace std;
5
// Structure to represent a node in the queue
struct Node {
int data;
Node* next;
};
// Front and Rear pointers for the queue
Node* front = nullptr;
Node* rear = nullptr;
********** 22 **********
--- page 23 ---
// Function to add an element to the rear of the
queue
void enqueue(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->next = nullptr;
if (rear == nullptr) { // Queue is empty
front = rear = newNode;
cout << "Enqueued: " << value << endl;
return;
}
// Add new node at the end and update rear
rear->next = newNode;
rear = newNode;
cout << "Enqueued: " << value << endl;
}
// Function to remove an element from the front of
the queue
void dequeue() {
if (front == nullptr) {
cout << "Queue is empty! Cannot
dequeue.\n";
********** 23 **********
--- page 24 ---
return;
}
Node* temp = front;
cout << "Dequeued: " << front->data << endl;
front = front->next;
// If queue becomes empty after dequeue
if (front == nullptr)
rear = nullptr;
delete temp; // Free memory
}
// Function to display all elements in the queue
void display() {
if (front == nullptr) {
cout << "Queue is empty.\n";
return;
}
Node* temp = front;
cout << "Queue Elements: ";
********** 24 **********
--- page 25 ---
while (temp != nullptr) {
cout << temp->data << " ";
temp = temp->next;
}
cout << endl;
}
// Main function
int main() {
int choice, value;
cout << "====== Queue Implementation using
Linked List (Structure) ======\n";
while (true) {
cout << "\n1. Enqueue (Add Element)";
cout << "\n2. Dequeue (Remove Element)";
cout << "\n3. Display Queue";
cout << "\n4. Exit";
cout << "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter value to enqueue: ";
********** 25 **********
--- page 26 ---
cin >> value;
enqueue(value);
break;
case 2:
dequeue();
break;
case 3:
display();
break;
case 4:
cout << "Exiting Program. Thank You!\n";
return 0;
default:
cout << "Invalid choice! Please try
again.\n";
}
}
return 0;
}
********** 26 **********
--- page 27 ---
B What is dynamic memory allocation? Explain with [10]
example. Write a C/C++ program to print
Fibonacci series using recursive function.
Ans:
Explanation 4 marks
Program 6 marks
#include <iostream>
using namespace std;
// Recursive function to find nth Fibonacci term
int fibonacci(int n) {
if (n == 0)
return 0;
else if (n == 1)
return 1;
else
return fibonacci(n - 1) + fibonacci(n - 2);
}
int main() {
int n;
cout << "Enter number of terms: ";
cin >> n;
cout << "Fibonacci Series: ";
for (int i = 0; i < n; i++) {
cout << fibonacci(i) << " ";
}
cout << endl;
return 0;
}
A   i)   An array AR [-4…6,-2…12] stores   [10]
elements in Row Major Wise, with the
Q6   address AR[2][3] as 4142. If each element
requires 2 bytes of storage, find the Base
address.
********** 27 **********
--- page 28 ---
Ans:
4142=Base+((2+4)×15+(3+2))×2
4142=𝐵𝑎𝑠𝑒+((6×15)+5)×2
4142=𝐵𝑎𝑠𝑒+(90+5)×2
4142=𝐵𝑎𝑠𝑒+(95×2)
4142=Base+190
Base=4142−190=3952
ii)   Write a program in to compute the sum
of all elements in an array using pointers.
Ans: #include <stdio.h>
int main() {
// Declaring variables
int arr1[10];
int i, n, sum = 0;
int *pt;
// Displaying the purpose of the
program
printf("\n\n Pointer : Sum of all
elements in an array :\n");
// Inputting the number of elements for
the array (maximum 10)
printf(" Input the number of elements
to store in the array (max 10) : ");
scanf("%d", &n);
// Inputting elements into the array
printf(" Input %d number of elements
in the array : \n", n);
********** 28 **********
--- page 29 ---
for (i = 0; i < n; i++) {
printf(" element - %d : ", i + 1);
scanf("%d", &arr1[i]);
}
pt = arr1; // pt stores the base address
of array arr1
// Calculating the sum of array
elements using pointer
for (i = 0; i < n; i++) {
sum = sum + *pt; // Adding the
value pointed by pt to the sum
pt++; // Moving the pointer to the
next element of the array
}
// Displaying the sum of the array
elements
printf(" The sum of array is : %d\n\n",
sum);
}
B   Explain how forward and backward traversal is [10]
possible in a doubly linked list.
CO3,
Write a program to implement a Doubly Linked
SO2,BL   List supporting the following operations:
4
i. Insert at Beginning – Add a new node at the
start of the list.
ii. Delete a Node – Delete a node with a given
value.
********** 29 **********
--- page 30 ---
iii. Display Forward and Backward – Traverse
and display the list from both directions.
Ans : (Explanation : 2 marks+ Program -8 marks)
Each node has two links: prev (to the previous
node) and next (to the next node).
Forward traversal: start from head, repeatedly do
ptr = ptr->next until nullptr.
Backward traversal: first reach the tail by moving
next until nullptr, then move back with ptr = ptr-
>prev until nullptr.
#include <iostream>
using namespace std;
struct Node {
int data;
Node* prev;
Node* next;
};
Node* head = nullptr; // start of the list
// 1) Insert at Beginning
void insertAtBeginning(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->prev = nullptr;
newNode->next = head;
if (head != nullptr) head->prev = newNode;
********** 30 **********
--- page 31 ---
head = newNode;
cout << "Inserted " << value << " at
beginning.\n";
}
// 2) Delete first node with given value
void deleteByValue(int value) {
if (!head) { cout << "List is empty.\n"; return; }
Node* cur = head;
while (cur && cur->data != value) cur = cur-
>next;
if (!cur) { cout << "Value " << value << " not
found.\n"; return; }
// If cur is head
if (cur == head) {
head = cur->next;
if (head) head->prev = nullptr;
cout << "Deleted " << cur->data << ".\n";
delete cur;
return;
}
// Middle or tail
if (cur->prev) cur->prev->next = cur->next;
if (cur->next) cur->next->prev = cur->prev;
cout << "Deleted " << cur->data << ".\n";
********** 31 **********
--- page 32 ---
delete cur;
}
// 3a) Display forward
void displayForward() {
if (!head) { cout << "List is empty.\n"; return; }
cout << "Forward : ";
for (Node* p = head; p != nullptr; p = p->next)
cout << p->data << (p->next ? " <-> " : " ->
NULL\n");
}
// 3b) Display backward
void displayBackward() {
if (!head) { cout << "List is empty.\n"; return; }
// Go to tail
Node* tail = head;
while (tail->next) tail = tail->next;
cout << "Backward: ";
for (Node* p = tail; p != nullptr; p = p->prev)
cout << p->data << (p->prev ? " <-> " : " ->
NULL\n");
}
int main() {
int choice, val;
cout << "===== Doubly Linked List =====\n";
while (true) {
********** 32 **********
--- page 33 ---
cout << "\n1. Insert at Beginning"
<< "\n2. Delete a Node (by value)"
<< "\n3. Display Forward"
<< "\n4. Display Backward"
<< "\n5. Exit"
<< "\nEnter your choice: ";
if (!(cin >> choice)) return 0;
switch (choice) {
case 1:
cout << "Enter value: ";
cin >> val;
insertAtBeginning(val);
break;
case 2:
cout << "Enter value to delete: ";
cin >> val;
deleteByValue(val);
break;
case 3:
displayForward();
break;
case 4:
displayBackward();
break;
case 5:
cout << "Exiting...\n";
return 0;
default:
cout << "Invalid choice. Try again.\n";
********** 33 **********
--- page 34 ---
}
}
}
A   In a restaurant, customers place orders that are
processed in the order they are received. Write a
Program to design a restaurant order management
system using a circular queue. Orders are
processed on a first-come, first-served basis.
Ans:
Ans: Marks: Structure/class declaration: 2 marks
Function : 6 marks
Main: 2 marks
#include <iostream>
#include <string>
using namespace std;
// Structure to represent each order
Q7   struct Order {
[10]
int orderID;
string customerName;
};
// Structure for Circular Queue
struct CircularQueue {
Order orders[50];   // Maximum 50 orders
int front;
int rear;
int size;
};
// Function to initialize the queue
void initializeQueue(CircularQueue &q, int n) {
q.size = n;
q.front = -1;
q.rear = -1;
}
// Function to check if queue is full
********** 34 **********
--- page 35 ---
bool isFull(CircularQueue q) {
return ((q.front == 0 && q.rear == q.size - 1) ||
(q.front == q.rear + 1));
}
// Function to check if queue is empty
bool isEmpty(CircularQueue q) {
return (q.front == -1);
}
// Function to place a new order (Enqueue)
void placeOrder(CircularQueue &q, int id, string
name) {
if (isFull(q)) {
cout << "   Cannot place new order. Queue
is full!\n";
return;
}
// First order
if (q.front == -1)
q.front = 0;
// Circular increment
q.rear = (q.rear + 1) % q.size;
q.orders[q.rear].orderID = id;
q.orders[q.rear].customerName = name;
cout << "Order placed successfully! [Order ID:
"
<< id << ", Customer: " << name << "]\n";
}
// Function to serve an order (Dequeue)
void serveOrder(CircularQueue &q) {
if (isEmpty(q)) {
cout << "No pending orders to serve.\n";
return;
}
cout << "Serving Order ID: " <<
q.orders[q.front].orderID
<< " | Customer: " <<
q.orders[q.front].customerName << endl;
********** 35 **********
--- page 36 ---
// Only one order left
if (q.front == q.rear) {
q.front = q.rear = -1;
} else {
q.front = (q.front + 1) % q.size;
}
}
// Function to display all pending orders
void displayOrders(CircularQueue q) {
if (isEmpty(q)) {
cout << "No pending orders.\n";
return;
}
cout << "\n Current Pending Orders (Front →
Rear):\n";
int i = q.front;
while (true) {
cout << "Order ID: " << q.orders[i].orderID
<< " | Customer: " <<
q.orders[i].customerName << endl;
if (i == q.rear) break;
i = (i + 1) % q.size;
}
}
// Main function
int main() {
CircularQueue q;
int maxOrders;
cout << "Enter maximum number of orders the
restaurant can handle: ";
cin >> maxOrders;
initializeQueue(q, maxOrders);
int choice, id;
string name;
cout << "\n====== Restaurant Order
Management System (Circular Queue)
======\n";
while (true) {
cout << "\n1. Place New Order (Enqueue)"
********** 36 **********
--- page 37 ---
<< "\n2. Serve Order (Dequeue)"
<< "\n3. Display Pending Orders"
<< "\n4. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter Order ID: ";
cin >> id;
cout << "Enter Customer Name: ";
cin.ignore();
getline(cin, name);
placeOrder(q, id, name);
break;
case 2:
serveOrder(q);
break;
case 3:
displayOrders(q);
break;
case 4:
cout << "Exiting system... Thank you!\n";
return 0;
default:
cout << "Invalid choice! Please try
again.\n";
}
}
return 0;
}
B   Explain the working principle of Binary Search
algorithm.
CO4,   You are developing a student record system where
data (roll numbers) must be first sorted before
SO2,BL   performing a quick search.   [10]
4   Write a program that performs the following tasks
using arrays:
i. Accept n roll numbers from the user.
********** 37 **********
--- page 38 ---
ii. Sort them in ascending order using Bubble
Sort.
iii. Perform a Binary Search to find a given roll
number.
iv. Display suitable messages for “Record
Found” or “Record Not Found.”
Ans: working of Binary search (4 marks)
Program ( 6 marks )
#include <iostream>
using namespace std;
// Function to perform Bubble Sort
void bubbleSort(int arr[], int n) {
for (int i = 0; i < n - 1; i++) {
bool swapped = false;
for (int j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
int temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
swapped = true;
}
}
if (!swapped) break; // Optimization for
already sorted data
}
}
// Function to perform Binary Search
int binarySearch(int arr[], int n, int key) {
********** 38 **********
--- page 39 ---
int low = 0, high = n - 1;
while (low <= high) {
int mid = (low + high) / 2;
if (arr[mid] == key)
return mid; // Record found
else if (arr[mid] < key)
low = mid + 1; // Search right half
else
high = mid - 1; // Search left half
}
return -1; // Record not found
}
int main() {
int n;
cout << "Enter number of students: ";
cin >> n;
int roll[n];
cout << "Enter " << n << " roll numbers:\n";
for (int i = 0; i < n; i++)
cin >> roll[i];
// Step 1: Sort roll numbers using Bubble Sort
bubbleSort(roll, n);
********** 39 **********
--- page 40 ---
cout << "\nRoll numbers after sorting: ";
for (int i = 0; i < n; i++)
cout << roll[i] << " ";
cout << endl;
// Step 2: Search for a roll number using Binary
Search
int key;
cout << "\nEnter roll number to search: ";
cin >> key;
int result = binarySearch(roll, n, key);
// Step 3: Display result
if (result != -1)
cout << " Record Found at position: " <<
result + 1 << endl;
else
cout << "Record Not Found.\n";
return 0;
}
********** 40 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 9b129d6ae54b

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/Integrated_Computer_7032/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (29 pages), mean OCR confidence 54.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Basic Data Structures
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 29 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions are to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Assume suitable data if necessary
Q1
Answer briefly:   Marks
a.   Define ADT with an example
Ans: An Abstract Data Type (ADT) is a conceptual model
for a data type defined by its behavior in terms of the
operations that can be performed on it and the rules for
those operations, without specifying how these operations
will be implemented or how data is organized in memory.
ADTs focus on what operations are to be performed rather
CO-1 ;   than how they are executed, providing abstraction and
SO-1 ;   encapsulation.   5
BL-1
For example, a Stack ADT is a collection of elements with
two primary operations: push (to add an element) and pop
(to remove the last added element), following a Last-In-
First-Out (LIFO) principle. How the stack is implemented
internally such as using an array or a linked list is not
described by the ADT itself; only the operations and their
behavior matter.
CO-2 ;   b.   What will be the output of the following program?
SO- 1;
#include <iostream>
BL-3
using namespace std;
int main()
5
{
int arr[] = { 4, 5, 6, 7 };
int* p = (arr + 1);
cout << *arr + 10;
********** 1 **********
--- page 2 ---
return 0;
}
Answer:14
CO-3 ;   c.   Explain algorithmic steps of different operations on a
SO-2 ;
Linear Queue.
BL-2
(Each 1 marks)
IsEmpty
Purpose: To check if the queue is empty.
Condition:
front == -1 or front > rear
IsFull
Purpose: To check if the queue is full.
Condition:
rear == MAX - 1
Enqueue (Insertion)
Purpose: To insert an element at the rear of the queue.
Steps:
1. Check for Overflow (Queue Full):
If rear == MAX - 1, insertion is not possible.
2. If Queue is Empty:
5
Set front = 0 and rear = 0.
3. Else:
Increment rear = rear + 1.
4. Insert Element:
queue[rear] = item.
Dequeue (Deletion)
Purpose: To remove an element from the front of the
queue.
Steps:
1. Check for Underflow (Queue Empty):
If front == -1 or front > rear, the queue is
empty.
2. Access Element:
item = queue[front].
3. If Only One Element Left:
Reset front = -1 and rear = -1.
4. Else:
Increment front = front + 1.
Display
Purpose: To print all the elements in the queue.
Steps:
********** 2 **********
--- page 3 ---
1. If front == -1, queue is empty.
2. Else, loop from front to rear and print each
element.
CO4,   d.   After the first pass of Bubble Sort on [9, 3, 7, 1, 5], what
SO1,BL2
will be the array? Calculate.
5
Ans: [3, 7, 1, 5, 9]
Students have to show the steps .
A   A) A palindrome is a string that reads the same forward and
backward. You want to check if a given string is a
palindrome by using a stack. Write a program that uses a
stack to check whether a given string is a palindrome. Push
all characters of the string onto a stack, and then pop them
off to compare with the original string to see if it reads the
same backward.
#include <iostream>
#include <stack>
#include <string>
using namespace std;
bool isPalindrome(const string& str) {
stack<char> s;
Q2
CO-3;   // Push all characters of the string onto the stack   [10]
SO-2; BL-
for (char ch : str) {
3
s.push(ch);
}
// Compare characters while popping from stack
for (char ch : str) {
if (ch != s.top()) {
return false; // Not a palindrome
}
s.pop();
}
return true; // Palindrome
********** 3 **********
--- page 4 ---
}
int main() {
string input;
cout << "Enter a string to check if it is a palindrome: ";
getline(cin, input);
if (isPalindrome(input))
cout << "The string is a palindrome." << endl;
else
cout << "The string is NOT a palindrome." << endl;
return 0;
}
Output:
Madam
The string is a palindrome.
B   Create an array of structures for N students with fields: Roll
No, Name, and Marks in 5 subjects. Calculate the total and
percentage of each student and display the student who
scored the highest percentage.
Ans:
#include <iostream>
#include <string>
using namespace std;
// Structure definition
CO-2 ;
struct Student {
SO-2;   [10]
BL-3   int rollNo;
string name;
float marks[5];
float total;
float percentage;
};
int main() {
int n;
********** 4 **********
--- page 5 ---
cout << "Enter number of students: ";
cin >> n;
Student s[n];
// Input details for each student
for (int i = 0; i < n; i++) {
cout << "\nEnter details for student " << i + 1 <<
":\n";
cout << "Roll No: ";
cin >> s[i].rollNo;
cin.ignore(); // to ignore newline
cout << "Name: ";
getline(cin, s[i].name);
s[i].total = 0;
cout << "Enter marks in 5 subjects:\n";
for (int j = 0; j < 5; j++) {
cout << "Subject " << j + 1 << ": ";
cin >> s[i].marks[j];
s[i].total += s[i].marks[j];
}
s[i].percentage = s[i].total / 5.0;
}
// Find student with highest percentage
int topIndex = 0;
for (int i = 1; i < n; i++) {
if (s[i].percentage > s[topIndex].percentage)
topIndex = i;
}
// Display all students' results
cout << "\n--- Student Results ---\n";
********** 5 **********
--- page 6 ---
for (int i = 0; i < n; i++) {
cout << "\nRoll No: " << s[i].rollNo;
cout << "\nName: " << s[i].name;
cout << "\nTotal Marks: " << s[i].total;
cout << "\nPercentage: " << s[i].percentage <<
"%\n";
}
// Display topper
cout << "\n--- Topper ---\n";
cout << "Roll No: " << s[topIndex].rollNo << endl;
cout << "Name: " << s[topIndex].name << endl;
cout << "Percentage: " << s[topIndex].percentage <<
"%\n";
return 0;
}
Structure   declaration(2)+input(3)+computing
per(3)+display(2)
A   Explain advantages and disadvantages of stack data [10]
structure. Convert the given infix expression into postfix
using stack.
(A + B – C * D / (E + F / G) * (I + J))
Ans: Advantages of Stack (4 marks)
1. Efficient Memory Management:
o Operates on a fixed memory area (LIFO),
Q3   reducing overhead of dynamic allocation.
o Memory for function calls and local
CO-3;   variables is efficiently managed using stack.
SO-1; BL-   2. Reversing and Backtracking Made Easy:
5   o Stack allows simple reversal of data
sequences.
o Used in algorithms that need to go “back” to
a previous state (like maze-solving,
recursion).
3. Simplifies Expression Handling:
o Used to convert infix to postfix/prefix
expressions and to evaluate them efficiently.
4. Supports Recursion:
o Each recursive call stores its state (local
variables, return address) in the stack.
5. Undo/Redo Functionality:
********** 6 **********
--- page 7 ---
o Commonly used in applications (e.g., text
editors) to revert or repeat actions
Disadvantages of Stack
1. Limited Size (Overflow Possibility):
o Stack has a fixed size; if it exceeds capacity,
stack overflow occurs.
2. Difficult Random Access:
o Only the top element is directly accessible;
you can’t access elements in the middle
easily.
3. Underflow Condition:
o Trying to pop an element from an empty
stack causes stack underflow.
4. Limited Data Management:
o Not suitable when data must be accessed in
other orders (like FIFO).
Conversion: 6 marks
Ans: AB+CD*EFG/+/IJ+*-
B   A) Explain advantages and disadvantages of stack data   [10]
structure. Convert the given infix expression into
postfix using stack.
(A + B – C * D / (E + F / G) * (I + J))
Advantages of Stack (4 marks)
6. Efficient Memory Management:
o Operates on a fixed memory area (LIFO),
reducing overhead of dynamic allocation.
o Memory for function calls and local
CO-3;   variables is efficiently managed using stack.
7. Reversing and Backtracking Made Easy:
SO-2; BL-   o Stack allows simple reversal of data
4   sequences.
o Used in algorithms that need to go “back” to
a previous state (like maze-solving,
recursion).
8. Simplifies Expression Handling:
o Used to convert infix to postfix/prefix
expressions and to evaluate them efficiently.
9. Supports Recursion:
o Each recursive call stores its state (local
variables, return address) in the stack.
10. Undo/Redo Functionality:
o Commonly used in applications (e.g., text
editors) to revert or repeat actions
********** 7 **********
--- page 8 ---
Disadvantages of Stack
5. Limited Size (Overflow Possibility):
o Stack has a fixed size; if it exceeds capacity,
stack overflow occurs.
6. Difficult Random Access:
o Only the top element is directly accessible;
you can’t access elements in the middle
easily.
7. Underflow Condition:
o Trying to pop an element from an empty
stack causes stack underflow.
8. Limited Data Management:
o Not suitable when data must be accessed in
other orders (like FIFO).
Conversion: 6 marks
********** 8 **********
--- page 9 ---
B) At a bank, customers arrive to be served by a teller.
Use a linear queue to manage customers. Serve each
customer in the order they arrived, and display the
queue after each service.
#include <iostream>
using namespace std;
#define MAX 100   // maximum queue size
class BankQueue {
private:
int queue[MAX];
int front, rear;
int servedCount;
public:
// Constructor
BankQueue() {
front = -1;
rear = -1;
servedCount = 0;
}
********** 9 **********
--- page 10 ---
// Check if queue is full
bool isFull() {
return (rear == MAX - 1);
}
// Check if queue is empty
bool isEmpty() {
return (front == -1 || front > rear);
}
// Add a customer to queue (enqueue)
void addCustomer(int customerID) {
if (isFull()) {
cout << "Queue is full! Cannot add more
customers.\n";
return;
}
if (front == -1)
front = 0;
queue[++rear] = customerID;
cout << "Customer " << customerID << " joined the
queue.\n";
}
// Serve a customer (dequeue)
void serveCustomer() {
if (isEmpty()) {
cout << "No customers in queue to serve.\n";
return;
}
cout << "Customer " << queue[front] << " is being
served by the teller.\n";
front++;
servedCount++;
displayQueue();
}
// Display current queue
void displayQueue() {
********** 10 **********
--- page 11 ---
if (isEmpty()) {
cout << "Queue is empty now.\n";
return;
}
cout << "Current queue: ";
for (int i = front; i <= rear; i++) {
cout << queue[i] << " ";
}
cout << endl;
}
// Display total served
void showTotalServed() {
cout << "Total customers served so far: " <<
servedCount << endl;
}
};
// -------------------- Main Function --------------------
int main() {
BankQueue bq;
int choice;
int id = 1;
cout << "=== Bank Teller Simulation Using Linear
Queue ===\n";
do {
cout << "\nMenu:\n";
cout << "1. Customer Arrives (Add to Queue)\n";
cout << "2. Serve Next Customer\n";
cout << "3. Display Current Queue\n";
cout << "4. Show Total Customers Served\n";
cout << "5. Exit\n";
cout << "Enter your choice: ";
********** 11 **********
--- page 12 ---
cin >> choice;
switch (choice) {
case 1:
bq.addCustomer(id++);
break;
case 2:
bq.serveCustomer();
break;
case 3:
bq.displayQueue();
break;
case 4:
bq.showTotalServed();
break;
case 5:
cout << "Exiting... Thank you for visiting the
bank!\n";
break;
default:
cout << "Invalid choice! Please try again.\n";
}
} while (choice != 5);
return 0;
}
A   Write a program for performing the following operations in [10]
Stack using Linked List representation
i.   Create
Q4   ii.   Push
CO-3,   iii.   Pop
SO-2, BL-
iv.   Stack top
3
Ans: #include <iostream>
using namespace std;
********** 12 **********
--- page 13 ---
// Structure for each node in the stack
struct Node {
int data;
Node* next;
};
Node* top = nullptr; // Top of the stack (initially
empty)
// i. CREATE (Initialize an empty stack)
void createStack() {
top = nullptr;
cout << "Stack created successfully.\n";
}
// ii. PUSH (Insert element at the top)
void push(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->next = top;
top = newNode;
cout << "Pushed " << value << " onto the
stack.\n";
}
// iii. POP (Remove top element)
void pop() {
if (top == nullptr) {
cout << "Stack Underflow! No element to
pop.\n";
return;
}
Node* temp = top;
********** 13 **********
--- page 14 ---
cout << "Popped element: " << temp->data <<
endl;
top = top->next;
delete temp;
}
// iv. STACK TOP (Display top element)
void stackTop() {
if (top == nullptr) {
cout << "Stack is empty.\n";
return;
}
cout << "Top element is: " << top->data <<
endl;
}
// Display entire stack
void displayStack() {
if (top == nullptr) {
cout << "Stack is empty.\n";
return;
}
cout << "\nCurrent Stack (Top → Bottom): ";
Node* temp = top;
while (temp != nullptr) {
cout << temp->data << " ";
temp = temp->next;
}
cout << endl;
}
// Main function
int main() {
int choice, value;
********** 14 **********
--- page 15 ---
cout << "====== Stack Operations using
Linked List ======\n";
while (true) {
cout << "\n1. Create Stack"
<< "\n2. Push Element"
<< "\n3. Pop Element"
<< "\n4. Display Top Element"
<< "\n5. Display Entire Stack"
<< "\n6. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
createStack();
break;
case 2:
cout << "Enter value to push: ";
cin >> value;
push(value);
break;
case 3:
pop();
break;
case 4:
stackTop();
break;
case 5:
displayStack();
break;
case 6:
cout << "Exiting program... Thank
you!\n";
return 0;
********** 15 **********
--- page 16 ---
default:
cout << "Invalid choice! Try again.\n";
}
}
}
B   What is Searching? Compare Linear and Binary search. [10]
Write a Program for recursive Binary search
Ans: #include <iostream>
using namespace std;
// Function for recursive binary search
int binarySearch(int arr[], int low, int high, int key) {
if (low > high)
return -1; // Element not found
int mid = (low + high) / 2;
if (arr[mid] == key)
return mid; // Element found
CO-4,
else if (key < arr[mid])
SO-3,BL-
return binarySearch(arr, low, mid - 1, key); // Search
4
left half
else
return binarySearch(arr, mid + 1, high, key); // Search
right half
}
int main() {
int n, key;
cout << "Enter number of elements: ";
cin >> n;
int arr[n];
cout << "Enter " << n << " sorted elements:\n";
********** 16 **********
--- page 17 ---
for (int i = 0; i < n; i++)
cin >> arr[i];
cout << "Enter element to search: ";
cin >> key;
int result = binarySearch(arr, 0, n - 1, key);
if (result == -1)
cout << "Element not found in the array.\n";
else
cout << "Element found at position: " << result + 1 <<
endl;
return 0;
}.
A   Explain the following operations performed on doubly   [10]
linked list with the help of pseudocode:
i.   Inserting an element in the beginning of the list
ii.   Deleting an element from the end of the list
iii.   Display all the elements in the list
Ans: i. Inserting an Element at the Beginning
Logic:
1. Create a new node and assign the data.
2. Set the new node’s next pointer to the current
Q5   head.
3. Set the new node’s prev pointer to NULL.
CO-3,   4. If the list is not empty, change the previous pointer
SO-2,BL-   of the existing head to point to the new node.
5   5. Make the new node the head of the list.
Pseudocode:
Function insertAtBeginning(data):
newNode = createNode(data)
newNode.prev = NULL
newNode.next = head
if head != NULL:
head.prev = newNode
head = newNode
Result:
The new node becomes the first element in the list, and
the links are adjusted accordingly.
********** 17 **********
--- page 18 ---
ii. Deleting an Element from the End
Logic:
1. Traverse the list until the last node is reached
(where next == NULL).
2. If the list has only one node, set head = NULL.
3. Otherwise:
o Set the next of the second-last node to
NULL.
o Delete (free) the last node.
Pseudocode:
Function deleteFromEnd():
if head == NULL:
print "List is empty"
return
temp = head
while temp.next != NULL:
temp = temp.next
if temp.prev == NULL:
head = NULL
else:
temp.prev.next = NULL
delete temp
Result:
The last node is removed, and the list shrinks by one
element from the end.
iii. Displaying All Elements in the List
Logic:
1. Start from the head node.
2. Traverse using the next pointer until the end of
the list.
3. Print each node’s data.
Pseudocode:
Function displayList():
if head == NULL:
print "List is empty"
return
temp = head
while temp != NULL:
print temp.data
temp = temp.next
Result:
All elements are displayed sequentially from first to last.
********** 18 **********
--- page 19 ---
B   Explain Recursion and Iteration. Write a C/C++ program   [10]
to calculate GCD of two numbers using recursive function.
Explanation =5 marks
Program = 5 marks
Ans: #include <iostream>
using namespace std;
// Recursive function to find GCD
int gcd(int a, int b) {
if (b == 0)
return a;
else
CO-3;   return gcd(b, a % b);
SO-2;
BL-3   }
int main() {
int num1, num2;
cout << "Enter two numbers: ";
cin >> num1 >> num2;
cout << "GCD of " << num1 << " and " << num2 << "
is: " << gcd(num1, num2) << endl;
return 0;
}
A   i.   Each element of an array ARR [15][20] requires [10]
‘W’   bytes   of   storage.
If the address of ARR [6][8] is 4580 and the
Base Address   of ARR[1][1]   is   4000,
find the width ‘W’ (size of each element in
Q6
bytes) when the array is stored in Column
CO-2 ;
SO- 2;   Major Order.
BL-3   Ans:
4580=4000+W×[(6−1)+(8−1)×15]
(6−1)+(8−1)×15=5+7×15=5+105=110
4580=4000+110W
********** 19 **********
--- page 20 ---
4580−4000=110W
580=110W580 = 110W
580=110W
W=580/110=5.2727
Approx. = 5 bytes per element
ii.   Explain call by Value and Call by Reference
using example
Ans: Explanation 5 marks
B   An institute maintains alumni records using a linked list.   [10]
Each node stores the alumnus’s name, batch, and email
ID. New alumni are added every year.
Write a Program to:
i. To insert a new alumni record at the end.
ii. To search for an alumnus by email ID.
iii.   To release memory when alumni data is
deleted.
Ans: #include <iostream>
#include <string>
using namespace std;
CO-3,
SO-2,BL-
// Structure to represent each alumni record
4
struct Alumni {
string name;
string batch;
string email;
Alumni* next;
};
// Head pointer for the linked list
Alumni* head = nullptr;
// i. Insert new alumni record at the end
********** 20 **********
--- page 21 ---
void insertAlumni(string name, string batch,
string email) {
Alumni* newAlumni = new Alumni();
newAlumni->name = name;
newAlumni->batch = batch;
newAlumni->email = email;
newAlumni->next = nullptr;
if (head == nullptr) {
head = newAlumni;
} else {
Alumni* temp = head;
while (temp->next != nullptr)
temp = temp->next;
temp->next = newAlumni;
}
cout << "Alumni record added
successfully.\n";
}
// ii. Search for an alumnus by email ID
void searchByEmail(string email) {
if (head == nullptr) {
cout << "No alumni records found.\n";
return;
}
Alumni* temp = head;
bool found = false;
while (temp != nullptr) {
if (temp->email == email) {
cout << "\nAlumnus Found:\n";
********** 21 **********
--- page 22 ---
cout << "Name: " << temp->name <<
endl;
cout << "Batch: " << temp->batch <<
endl;
cout << "Email: " << temp->email <<
endl;
found = true;
break;
}
temp = temp->next;
}
if (!found)
cout << "Alumnus with email '" << email
<< "' not found.\n";
}
// iii. Delete all alumni records (release
memory)
void deleteAllRecords() {
Alumni* temp;
while (head != nullptr) {
temp = head;
head = head->next;
delete temp;
}
cout << "All alumni records have been
deleted and memory released.\n";
}
// Function to display all alumni
void displayAll() {
if (head == nullptr) {
cout << "No alumni records to display.\n";
return;
********** 22 **********
--- page 23 ---
}
Alumni* temp = head;
cout << "\nList of Alumni:\n";
while (temp != nullptr) {
cout << "Name: " << temp->name
<< " | Batch: " << temp->batch
<< " | Email: " << temp->email <<
endl;
temp = temp->next;
}
}
// Main function
int main() {
int choice;
string name, batch, email;
cout << "====== Alumni Record
Management System ======\n";
while (true) {
cout << "\n1. Add New Alumni Record"
<< "\n2. Search Alumni by Email ID"
<< "\n3. Display All Alumni"
<< "\n4. Delete All Records (Release
Memory)"
<< "\n5. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cin.ignore();
cout << "Enter Name: ";
********** 23 **********
--- page 24 ---
getline(cin, name);
cout << "Enter Batch: ";
getline(cin, batch);
cout << "Enter Email ID: ";
getline(cin, email);
insertAlumni(name, batch, email);
break;
case 2:
cin.ignore();
cout << "Enter Email ID to Search: ";
getline(cin, email);
searchByEmail(email);
break;
case 3:
displayAll();
break;
case 4:
deleteAllRecords();
break;
case 5:
cout << "Exiting system... Thank
you!\n";
deleteAllRecords(); // Ensure memory is
freed
return 0;
default:
cout << "Invalid choice! Please try
again.\n";
}
}
********** 24 **********
--- page 25 ---
return 0;
}
A A printer stores print jobs in memory before printing them.
Once a job is printed, that memory is reused for the next
print job.
Explain how a Circular Queue can be used to manage print
jobs efficiently.
Implement enqueue (add new print job) and dequeue
(remove completed job) operations.
Ans: Explanation 3 marks
Program 7 marks
#include <iostream>
#include <string>
using namespace std;
// Structure for each print job
struct PrintJob {
int jobID;
string documentName;
};
// Structure for Circular Queue
Q7   struct CircularQueue {
CO-3;   PrintJob jobs[5]; // Maximum 5 jobs in memory
SO-2;   int front;
BL-5   int rear;   [10]
int size;
};
// Initialize the queue
void initializeQueue(CircularQueue &q, int n) {
q.size = n;
q.front = -1;
q.rear = -1;
}
// Check if queue is full
bool isFull(CircularQueue q) {
return ((q.front == 0 && q.rear == q.size - 1) || (q.front
== q.rear + 1));
}
// Check if queue is empty
bool isEmpty(CircularQueue q) {
return (q.front == -1);
}
// Enqueue (Add new print job)
void enqueue(CircularQueue &q, int id, string doc) {
if (isFull(q)) {
********** 25 **********
--- page 26 ---
cout << "Printer memory full! Cannot add new job.\n";
return;
}
if (q.front == -1) // first job
q.front = 0;
q.rear = (q.rear + 1) % q.size;
q.jobs[q.rear].jobID = id;
q.jobs[q.rear].documentName = doc;
cout << "Print job added: [Job ID: " << id
<< ", Document: " << doc << "]\n";
}
// Dequeue (Remove completed print job)
void dequeue(CircularQueue &q) {
if (isEmpty(q)) {
cout << "No pending print jobs.\n";
return;
}
cout << "Completed Print Job -> [Job ID: "
<< q.jobs[q.front].jobID
<< ", Document: " << q.jobs[q.front].documentName
<< "]\n";
if (q.front == q.rear) {
q.front = q.rear = -1; // queue becomes empty
} else {
q.front = (q.front + 1) % q.size; // circular move
}
}
// Display all pending print jobs
void displayQueue(CircularQueue q) {
if (isEmpty(q)) {
cout << "No pending print jobs.\n";
return;
}
cout << "\nPending Print Jobs (Front → Rear):\n";
int i = q.front;
while (true) {
cout << "[Job ID: " << q.jobs[i].jobID
<< ", Document: " << q.jobs[i].documentName <<
"]\n";
if (i == q.rear)
break;
i = (i + 1) % q.size;
}
}
********** 26 **********
--- page 27 ---
// Main function
int main() {
CircularQueue printerQueue;
initializeQueue(printerQueue, 5);
int choice, id;
string doc;
cout << "===== Printer Job Management using Circular
Queue =====\n";
while (true) {
cout << "\n1. Add Print Job (Enqueue)"
<< "\n2. Complete Print Job (Dequeue)"
<< "\n3. Display Pending Jobs"
<< "\n4. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter Job ID: ";
cin >> id;
cout << "Enter Document Name: ";
cin.ignore();
getline(cin, doc);
enqueue(printerQueue, id, doc);
break;
case 2:
dequeue(printerQueue);
break;
case 3:
displayQueue(printerQueue);
break;
case 4:
cout << "Exiting Printer Job Manager...\n";
return 0;
default:
cout << "Invalid choice. Try again.\n";
}
}
}
B   Explain the working principle of Selection Sort with
CO-4,   reasoning and an example. Why is it not suitable for large
SO-2,   datasets? Write a C++ program to implement Selection   [10]
Sort in descending order.
BL-4   Ans: Explanation – 4 marks
Program – 6 marks
********** 27 **********
--- page 28 ---
Why Selection Sort is not suitable for large datasets:
1. Fixed comparisons: It always performs
n(n−1)2\frac{n(n-1)}{2}2n(n−1) comparisons →
O(n²) time complexity, even if the data is nearly
sorted.
2. Non-adaptive: It doesn’t become faster for
partially sorted lists.
3. Full scans per pass: Each pass scans the
remaining array completely → poor scalability
compared to O(n log n) algorithms like Merge Sort
or Quick Sort.
4. Not stable: Equal elements can lose their original
order unless additional logic is added.
#include <iostream>
#include <vector>
using namespace std;
void selectionSortDescending(vector<int>& a) {
int n = static_cast<int>(a.size());
for (int i = 0; i < n - 1; ++i) {
int maxIndex = i; // assume a[i] is the largest in the
unsorted part
for (int j = i + 1; j < n; ++j) {
if (a[j] > a[maxIndex]) {
maxIndex = j;
}
}
if (maxIndex != i) {
int tmp = a[i];
a[i] = a[maxIndex];
a[maxIndex] = tmp;
}
}
}
int main() {
int n;
cout << "Enter number of elements: ";
if (!(cin >> n) || n <= 0) return 0;
vector<int> arr(n);
cout << "Enter " << n << " elements: ";
for (int i = 0; i < n; ++i) cin >> arr[i];
selectionSortDescending(arr);
cout << "Sorted (Descending): ";
for (int x : arr) cout << x << " ";
cout << "\n";
********** 28 **********
--- page 29 ---
return 0;

FAR ICR QA HH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper d55703d0ea7e

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/Integrated_DS_7038/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (29 pages), mean OCR confidence 54.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Basic Data Structures
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 29 pages.
2. Question No. 1 is compulsory
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions are to be attempted
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Assume suitable data if necessary
Q1
Answer briefly:   Marks
a.   Define ADT with an example
Ans: An Abstract Data Type (ADT) is a conceptual model
for a data type defined by its behavior in terms of the
operations that can be performed on it and the rules for
those operations, without specifying how these operations
will be implemented or how data is organized in memory.
ADTs focus on what operations are to be performed rather
CO-1 ;   than how they are executed, providing abstraction and
SO-1 ;   encapsulation.   5
BL-1
For example, a Stack ADT is a collection of elements with
two primary operations: push (to add an element) and pop
(to remove the last added element), following a Last-In-
First-Out (LIFO) principle. How the stack is implemented
internally such as using an array or a linked list is not
described by the ADT itself; only the operations and their
behavior matter.
CO-2 ;   b.   What will be the output of the following program?
SO- 1;
#include <iostream>
BL-3
using namespace std;
int main()
5
{
int arr[] = { 4, 5, 6, 7 };
int* p = (arr + 1);
cout << *arr + 10;
********** 1 **********
--- page 2 ---
return 0;
}
Answer:14
CO-3 ;   c.   Explain algorithmic steps of different operations on a
SO-2 ;
Linear Queue.
BL-2
(Each 1 marks)
IsEmpty
Purpose: To check if the queue is empty.
Condition:
front == -1 or front > rear
IsFull
Purpose: To check if the queue is full.
Condition:
rear == MAX - 1
Enqueue (Insertion)
Purpose: To insert an element at the rear of the queue.
Steps:
1. Check for Overflow (Queue Full):
If rear == MAX - 1, insertion is not possible.
2. If Queue is Empty:
5
Set front = 0 and rear = 0.
3. Else:
Increment rear = rear + 1.
4. Insert Element:
queue[rear] = item.
Dequeue (Deletion)
Purpose: To remove an element from the front of the
queue.
Steps:
1. Check for Underflow (Queue Empty):
If front == -1 or front > rear, the queue is
empty.
2. Access Element:
item = queue[front].
3. If Only One Element Left:
Reset front = -1 and rear = -1.
4. Else:
Increment front = front + 1.
Display
Purpose: To print all the elements in the queue.
Steps:
********** 2 **********
--- page 3 ---
1. If front == -1, queue is empty.
2. Else, loop from front to rear and print each
element.
CO4,   d.   After the first pass of Bubble Sort on [9, 3, 7, 1, 5], what
SO1,BL2
will be the array? Calculate.
5
Ans: [3, 7, 1, 5, 9]
Students have to show the steps .
A   A) A palindrome is a string that reads the same forward and
backward. You want to check if a given string is a
palindrome by using a stack. Write a program that uses a
stack to check whether a given string is a palindrome. Push
all characters of the string onto a stack, and then pop them
off to compare with the original string to see if it reads the
same backward.
#include <iostream>
#include <stack>
#include <string>
using namespace std;
bool isPalindrome(const string& str) {
stack<char> s;
Q2
CO-3;   // Push all characters of the string onto the stack   [10]
SO-2; BL-
for (char ch : str) {
3
s.push(ch);
}
// Compare characters while popping from stack
for (char ch : str) {
if (ch != s.top()) {
return false; // Not a palindrome
}
s.pop();
}
return true; // Palindrome
********** 3 **********
--- page 4 ---
}
int main() {
string input;
cout << "Enter a string to check if it is a palindrome: ";
getline(cin, input);
if (isPalindrome(input))
cout << "The string is a palindrome." << endl;
else
cout << "The string is NOT a palindrome." << endl;
return 0;
}
Output:
Madam
The string is a palindrome.
B   Create an array of structures for N students with fields: Roll
No, Name, and Marks in 5 subjects. Calculate the total and
percentage of each student and display the student who
scored the highest percentage.
Ans:
#include <iostream>
#include <string>
using namespace std;
// Structure definition
CO-2 ;
struct Student {
SO-2;   [10]
BL-3   int rollNo;
string name;
float marks[5];
float total;
float percentage;
};
int main() {
int n;
********** 4 **********
--- page 5 ---
cout << "Enter number of students: ";
cin >> n;
Student s[n];
// Input details for each student
for (int i = 0; i < n; i++) {
cout << "\nEnter details for student " << i + 1 <<
":\n";
cout << "Roll No: ";
cin >> s[i].rollNo;
cin.ignore(); // to ignore newline
cout << "Name: ";
getline(cin, s[i].name);
s[i].total = 0;
cout << "Enter marks in 5 subjects:\n";
for (int j = 0; j < 5; j++) {
cout << "Subject " << j + 1 << ": ";
cin >> s[i].marks[j];
s[i].total += s[i].marks[j];
}
s[i].percentage = s[i].total / 5.0;
}
// Find student with highest percentage
int topIndex = 0;
for (int i = 1; i < n; i++) {
if (s[i].percentage > s[topIndex].percentage)
topIndex = i;
}
// Display all students' results
cout << "\n--- Student Results ---\n";
********** 5 **********
--- page 6 ---
for (int i = 0; i < n; i++) {
cout << "\nRoll No: " << s[i].rollNo;
cout << "\nName: " << s[i].name;
cout << "\nTotal Marks: " << s[i].total;
cout << "\nPercentage: " << s[i].percentage <<
"%\n";
}
// Display topper
cout << "\n--- Topper ---\n";
cout << "Roll No: " << s[topIndex].rollNo << endl;
cout << "Name: " << s[topIndex].name << endl;
cout << "Percentage: " << s[topIndex].percentage <<
"%\n";
return 0;
}
Structure   declaration(2)+input(3)+computing
per(3)+display(2)
A   Explain advantages and disadvantages of stack data [10]
structure. Convert the given infix expression into postfix
using stack.
(A + B – C * D / (E + F / G) * (I + J))
Ans: Advantages of Stack (4 marks)
1. Efficient Memory Management:
o Operates on a fixed memory area (LIFO),
Q3   reducing overhead of dynamic allocation.
o Memory for function calls and local
CO-3;   variables is efficiently managed using stack.
SO-1; BL-   2. Reversing and Backtracking Made Easy:
5   o Stack allows simple reversal of data
sequences.
o Used in algorithms that need to go “back” to
a previous state (like maze-solving,
recursion).
3. Simplifies Expression Handling:
o Used to convert infix to postfix/prefix
expressions and to evaluate them efficiently.
4. Supports Recursion:
o Each recursive call stores its state (local
variables, return address) in the stack.
5. Undo/Redo Functionality:
********** 6 **********
--- page 7 ---
o Commonly used in applications (e.g., text
editors) to revert or repeat actions
Disadvantages of Stack
1. Limited Size (Overflow Possibility):
o Stack has a fixed size; if it exceeds capacity,
stack overflow occurs.
2. Difficult Random Access:
o Only the top element is directly accessible;
you can’t access elements in the middle
easily.
3. Underflow Condition:
o Trying to pop an element from an empty
stack causes stack underflow.
4. Limited Data Management:
o Not suitable when data must be accessed in
other orders (like FIFO).
Conversion: 6 marks
Ans: AB+CD*EFG/+/IJ+*-
B   A) Explain advantages and disadvantages of stack data   [10]
structure. Convert the given infix expression into
postfix using stack.
(A + B – C * D / (E + F / G) * (I + J))
Advantages of Stack (4 marks)
6. Efficient Memory Management:
o Operates on a fixed memory area (LIFO),
reducing overhead of dynamic allocation.
o Memory for function calls and local
CO-3;   variables is efficiently managed using stack.
7. Reversing and Backtracking Made Easy:
SO-2; BL-   o Stack allows simple reversal of data
4   sequences.
o Used in algorithms that need to go “back” to
a previous state (like maze-solving,
recursion).
8. Simplifies Expression Handling:
o Used to convert infix to postfix/prefix
expressions and to evaluate them efficiently.
9. Supports Recursion:
o Each recursive call stores its state (local
variables, return address) in the stack.
10. Undo/Redo Functionality:
o Commonly used in applications (e.g., text
editors) to revert or repeat actions
********** 7 **********
--- page 8 ---
Disadvantages of Stack
5. Limited Size (Overflow Possibility):
o Stack has a fixed size; if it exceeds capacity,
stack overflow occurs.
6. Difficult Random Access:
o Only the top element is directly accessible;
you can’t access elements in the middle
easily.
7. Underflow Condition:
o Trying to pop an element from an empty
stack causes stack underflow.
8. Limited Data Management:
o Not suitable when data must be accessed in
other orders (like FIFO).
Conversion: 6 marks
********** 8 **********
--- page 9 ---
B) At a bank, customers arrive to be served by a teller.
Use a linear queue to manage customers. Serve each
customer in the order they arrived, and display the
queue after each service.
#include <iostream>
using namespace std;
#define MAX 100   // maximum queue size
class BankQueue {
private:
int queue[MAX];
int front, rear;
int servedCount;
public:
// Constructor
BankQueue() {
front = -1;
rear = -1;
servedCount = 0;
}
********** 9 **********
--- page 10 ---
// Check if queue is full
bool isFull() {
return (rear == MAX - 1);
}
// Check if queue is empty
bool isEmpty() {
return (front == -1 || front > rear);
}
// Add a customer to queue (enqueue)
void addCustomer(int customerID) {
if (isFull()) {
cout << "Queue is full! Cannot add more
customers.\n";
return;
}
if (front == -1)
front = 0;
queue[++rear] = customerID;
cout << "Customer " << customerID << " joined the
queue.\n";
}
// Serve a customer (dequeue)
void serveCustomer() {
if (isEmpty()) {
cout << "No customers in queue to serve.\n";
return;
}
cout << "Customer " << queue[front] << " is being
served by the teller.\n";
front++;
servedCount++;
displayQueue();
}
// Display current queue
void displayQueue() {
********** 10 **********
--- page 11 ---
if (isEmpty()) {
cout << "Queue is empty now.\n";
return;
}
cout << "Current queue: ";
for (int i = front; i <= rear; i++) {
cout << queue[i] << " ";
}
cout << endl;
}
// Display total served
void showTotalServed() {
cout << "Total customers served so far: " <<
servedCount << endl;
}
};
// -------------------- Main Function --------------------
int main() {
BankQueue bq;
int choice;
int id = 1;
cout << "=== Bank Teller Simulation Using Linear
Queue ===\n";
do {
cout << "\nMenu:\n";
cout << "1. Customer Arrives (Add to Queue)\n";
cout << "2. Serve Next Customer\n";
cout << "3. Display Current Queue\n";
cout << "4. Show Total Customers Served\n";
cout << "5. Exit\n";
cout << "Enter your choice: ";
********** 11 **********
--- page 12 ---
cin >> choice;
switch (choice) {
case 1:
bq.addCustomer(id++);
break;
case 2:
bq.serveCustomer();
break;
case 3:
bq.displayQueue();
break;
case 4:
bq.showTotalServed();
break;
case 5:
cout << "Exiting... Thank you for visiting the
bank!\n";
break;
default:
cout << "Invalid choice! Please try again.\n";
}
} while (choice != 5);
return 0;
}
A   Write a program for performing the following operations in [10]
Stack using Linked List representation
i.   Create
Q4   ii.   Push
CO-3,   iii.   Pop
SO-2, BL-
iv.   Stack top
3
Ans: #include <iostream>
using namespace std;
********** 12 **********
--- page 13 ---
// Structure for each node in the stack
struct Node {
int data;
Node* next;
};
Node* top = nullptr; // Top of the stack (initially
empty)
// i. CREATE (Initialize an empty stack)
void createStack() {
top = nullptr;
cout << "Stack created successfully.\n";
}
// ii. PUSH (Insert element at the top)
void push(int value) {
Node* newNode = new Node();
newNode->data = value;
newNode->next = top;
top = newNode;
cout << "Pushed " << value << " onto the
stack.\n";
}
// iii. POP (Remove top element)
void pop() {
if (top == nullptr) {
cout << "Stack Underflow! No element to
pop.\n";
return;
}
Node* temp = top;
********** 13 **********
--- page 14 ---
cout << "Popped element: " << temp->data <<
endl;
top = top->next;
delete temp;
}
// iv. STACK TOP (Display top element)
void stackTop() {
if (top == nullptr) {
cout << "Stack is empty.\n";
return;
}
cout << "Top element is: " << top->data <<
endl;
}
// Display entire stack
void displayStack() {
if (top == nullptr) {
cout << "Stack is empty.\n";
return;
}
cout << "\nCurrent Stack (Top → Bottom): ";
Node* temp = top;
while (temp != nullptr) {
cout << temp->data << " ";
temp = temp->next;
}
cout << endl;
}
// Main function
int main() {
int choice, value;
********** 14 **********
--- page 15 ---
cout << "====== Stack Operations using
Linked List ======\n";
while (true) {
cout << "\n1. Create Stack"
<< "\n2. Push Element"
<< "\n3. Pop Element"
<< "\n4. Display Top Element"
<< "\n5. Display Entire Stack"
<< "\n6. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
createStack();
break;
case 2:
cout << "Enter value to push: ";
cin >> value;
push(value);
break;
case 3:
pop();
break;
case 4:
stackTop();
break;
case 5:
displayStack();
break;
case 6:
cout << "Exiting program... Thank
you!\n";
return 0;
********** 15 **********
--- page 16 ---
default:
cout << "Invalid choice! Try again.\n";
}
}
}
B   What is Searching? Compare Linear and Binary search. [10]
Write a Program for recursive Binary search
Ans: #include <iostream>
using namespace std;
// Function for recursive binary search
int binarySearch(int arr[], int low, int high, int key) {
if (low > high)
return -1; // Element not found
int mid = (low + high) / 2;
if (arr[mid] == key)
return mid; // Element found
CO-4,
else if (key < arr[mid])
SO-3,BL-
return binarySearch(arr, low, mid - 1, key); // Search
4
left half
else
return binarySearch(arr, mid + 1, high, key); // Search
right half
}
int main() {
int n, key;
cout << "Enter number of elements: ";
cin >> n;
int arr[n];
cout << "Enter " << n << " sorted elements:\n";
********** 16 **********
--- page 17 ---
for (int i = 0; i < n; i++)
cin >> arr[i];
cout << "Enter element to search: ";
cin >> key;
int result = binarySearch(arr, 0, n - 1, key);
if (result == -1)
cout << "Element not found in the array.\n";
else
cout << "Element found at position: " << result + 1 <<
endl;
return 0;
}.
A   Explain the following operations performed on doubly   [10]
linked list with the help of pseudocode:
i.   Inserting an element in the beginning of the list
ii.   Deleting an element from the end of the list
iii.   Display all the elements in the list
Ans: i. Inserting an Element at the Beginning
Logic:
1. Create a new node and assign the data.
2. Set the new node’s next pointer to the current
Q5   head.
3. Set the new node’s prev pointer to NULL.
CO-3,   4. If the list is not empty, change the previous pointer
SO-2,BL-   of the existing head to point to the new node.
5   5. Make the new node the head of the list.
Pseudocode:
Function insertAtBeginning(data):
newNode = createNode(data)
newNode.prev = NULL
newNode.next = head
if head != NULL:
head.prev = newNode
head = newNode
Result:
The new node becomes the first element in the list, and
the links are adjusted accordingly.
********** 17 **********
--- page 18 ---
ii. Deleting an Element from the End
Logic:
1. Traverse the list until the last node is reached
(where next == NULL).
2. If the list has only one node, set head = NULL.
3. Otherwise:
o Set the next of the second-last node to
NULL.
o Delete (free) the last node.
Pseudocode:
Function deleteFromEnd():
if head == NULL:
print "List is empty"
return
temp = head
while temp.next != NULL:
temp = temp.next
if temp.prev == NULL:
head = NULL
else:
temp.prev.next = NULL
delete temp
Result:
The last node is removed, and the list shrinks by one
element from the end.
iii. Displaying All Elements in the List
Logic:
1. Start from the head node.
2. Traverse using the next pointer until the end of
the list.
3. Print each node’s data.
Pseudocode:
Function displayList():
if head == NULL:
print "List is empty"
return
temp = head
while temp != NULL:
print temp.data
temp = temp.next
Result:
All elements are displayed sequentially from first to last.
********** 18 **********
--- page 19 ---
B   Explain Recursion and Iteration. Write a C/C++ program   [10]
to calculate GCD of two numbers using recursive function.
Explanation =5 marks
Program = 5 marks
Ans: #include <iostream>
using namespace std;
// Recursive function to find GCD
int gcd(int a, int b) {
if (b == 0)
return a;
else
CO-3;   return gcd(b, a % b);
SO-2;
BL-3   }
int main() {
int num1, num2;
cout << "Enter two numbers: ";
cin >> num1 >> num2;
cout << "GCD of " << num1 << " and " << num2 << "
is: " << gcd(num1, num2) << endl;
return 0;
}
A   i.   Each element of an array ARR [15][20] requires [10]
‘W’   bytes   of   storage.
If the address of ARR [6][8] is 4580 and the
Base Address   of ARR[1][1]   is   4000,
find the width ‘W’ (size of each element in
Q6
bytes) when the array is stored in Column
CO-2 ;
SO- 2;   Major Order.
BL-3   Ans:
4580=4000+W×[(6−1)+(8−1)×15]
(6−1)+(8−1)×15=5+7×15=5+105=110
4580=4000+110W
********** 19 **********
--- page 20 ---
4580−4000=110W
580=110W580 = 110W
580=110W
W=580/110=5.2727
Approx. = 5 bytes per element
ii.   Explain call by Value and Call by Reference
using example
Ans: Explanation 5 marks
B   An institute maintains alumni records using a linked list.   [10]
Each node stores the alumnus’s name, batch, and email
ID. New alumni are added every year.
Write a Program to:
i. To insert a new alumni record at the end.
ii. To search for an alumnus by email ID.
iii.   To release memory when alumni data is
deleted.
Ans: #include <iostream>
#include <string>
using namespace std;
CO-3,
SO-2,BL-
// Structure to represent each alumni record
4
struct Alumni {
string name;
string batch;
string email;
Alumni* next;
};
// Head pointer for the linked list
Alumni* head = nullptr;
// i. Insert new alumni record at the end
********** 20 **********
--- page 21 ---
void insertAlumni(string name, string batch,
string email) {
Alumni* newAlumni = new Alumni();
newAlumni->name = name;
newAlumni->batch = batch;
newAlumni->email = email;
newAlumni->next = nullptr;
if (head == nullptr) {
head = newAlumni;
} else {
Alumni* temp = head;
while (temp->next != nullptr)
temp = temp->next;
temp->next = newAlumni;
}
cout << "Alumni record added
successfully.\n";
}
// ii. Search for an alumnus by email ID
void searchByEmail(string email) {
if (head == nullptr) {
cout << "No alumni records found.\n";
return;
}
Alumni* temp = head;
bool found = false;
while (temp != nullptr) {
if (temp->email == email) {
cout << "\nAlumnus Found:\n";
********** 21 **********
--- page 22 ---
cout << "Name: " << temp->name <<
endl;
cout << "Batch: " << temp->batch <<
endl;
cout << "Email: " << temp->email <<
endl;
found = true;
break;
}
temp = temp->next;
}
if (!found)
cout << "Alumnus with email '" << email
<< "' not found.\n";
}
// iii. Delete all alumni records (release
memory)
void deleteAllRecords() {
Alumni* temp;
while (head != nullptr) {
temp = head;
head = head->next;
delete temp;
}
cout << "All alumni records have been
deleted and memory released.\n";
}
// Function to display all alumni
void displayAll() {
if (head == nullptr) {
cout << "No alumni records to display.\n";
return;
********** 22 **********
--- page 23 ---
}
Alumni* temp = head;
cout << "\nList of Alumni:\n";
while (temp != nullptr) {
cout << "Name: " << temp->name
<< " | Batch: " << temp->batch
<< " | Email: " << temp->email <<
endl;
temp = temp->next;
}
}
// Main function
int main() {
int choice;
string name, batch, email;
cout << "====== Alumni Record
Management System ======\n";
while (true) {
cout << "\n1. Add New Alumni Record"
<< "\n2. Search Alumni by Email ID"
<< "\n3. Display All Alumni"
<< "\n4. Delete All Records (Release
Memory)"
<< "\n5. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cin.ignore();
cout << "Enter Name: ";
********** 23 **********
--- page 24 ---
getline(cin, name);
cout << "Enter Batch: ";
getline(cin, batch);
cout << "Enter Email ID: ";
getline(cin, email);
insertAlumni(name, batch, email);
break;
case 2:
cin.ignore();
cout << "Enter Email ID to Search: ";
getline(cin, email);
searchByEmail(email);
break;
case 3:
displayAll();
break;
case 4:
deleteAllRecords();
break;
case 5:
cout << "Exiting system... Thank
you!\n";
deleteAllRecords(); // Ensure memory is
freed
return 0;
default:
cout << "Invalid choice! Please try
again.\n";
}
}
********** 24 **********
--- page 25 ---
return 0;
}
A A printer stores print jobs in memory before printing them.
Once a job is printed, that memory is reused for the next
print job.
Explain how a Circular Queue can be used to manage print
jobs efficiently.
Implement enqueue (add new print job) and dequeue
(remove completed job) operations.
Ans: Explanation 3 marks
Program 7 marks
#include <iostream>
#include <string>
using namespace std;
// Structure for each print job
struct PrintJob {
int jobID;
string documentName;
};
// Structure for Circular Queue
Q7   struct CircularQueue {
CO-3;   PrintJob jobs[5]; // Maximum 5 jobs in memory
SO-2;   int front;
BL-5   int rear;   [10]
int size;
};
// Initialize the queue
void initializeQueue(CircularQueue &q, int n) {
q.size = n;
q.front = -1;
q.rear = -1;
}
// Check if queue is full
bool isFull(CircularQueue q) {
return ((q.front == 0 && q.rear == q.size - 1) || (q.front
== q.rear + 1));
}
// Check if queue is empty
bool isEmpty(CircularQueue q) {
return (q.front == -1);
}
// Enqueue (Add new print job)
void enqueue(CircularQueue &q, int id, string doc) {
if (isFull(q)) {
********** 25 **********
--- page 26 ---
cout << "Printer memory full! Cannot add new job.\n";
return;
}
if (q.front == -1) // first job
q.front = 0;
q.rear = (q.rear + 1) % q.size;
q.jobs[q.rear].jobID = id;
q.jobs[q.rear].documentName = doc;
cout << "Print job added: [Job ID: " << id
<< ", Document: " << doc << "]\n";
}
// Dequeue (Remove completed print job)
void dequeue(CircularQueue &q) {
if (isEmpty(q)) {
cout << "No pending print jobs.\n";
return;
}
cout << "Completed Print Job -> [Job ID: "
<< q.jobs[q.front].jobID
<< ", Document: " << q.jobs[q.front].documentName
<< "]\n";
if (q.front == q.rear) {
q.front = q.rear = -1; // queue becomes empty
} else {
q.front = (q.front + 1) % q.size; // circular move
}
}
// Display all pending print jobs
void displayQueue(CircularQueue q) {
if (isEmpty(q)) {
cout << "No pending print jobs.\n";
return;
}
cout << "\nPending Print Jobs (Front → Rear):\n";
int i = q.front;
while (true) {
cout << "[Job ID: " << q.jobs[i].jobID
<< ", Document: " << q.jobs[i].documentName <<
"]\n";
if (i == q.rear)
break;
i = (i + 1) % q.size;
}
}
********** 26 **********
--- page 27 ---
// Main function
int main() {
CircularQueue printerQueue;
initializeQueue(printerQueue, 5);
int choice, id;
string doc;
cout << "===== Printer Job Management using Circular
Queue =====\n";
while (true) {
cout << "\n1. Add Print Job (Enqueue)"
<< "\n2. Complete Print Job (Dequeue)"
<< "\n3. Display Pending Jobs"
<< "\n4. Exit"
<< "\nEnter your choice: ";
cin >> choice;
switch (choice) {
case 1:
cout << "Enter Job ID: ";
cin >> id;
cout << "Enter Document Name: ";
cin.ignore();
getline(cin, doc);
enqueue(printerQueue, id, doc);
break;
case 2:
dequeue(printerQueue);
break;
case 3:
displayQueue(printerQueue);
break;
case 4:
cout << "Exiting Printer Job Manager...\n";
return 0;
default:
cout << "Invalid choice. Try again.\n";
}
}
}
B   Explain the working principle of Selection Sort with
CO-4,   reasoning and an example. Why is it not suitable for large
SO-2,   datasets? Write a C++ program to implement Selection   [10]
Sort in descending order.
BL-4   Ans: Explanation – 4 marks
Program – 6 marks
********** 27 **********
--- page 28 ---
Why Selection Sort is not suitable for large datasets:
1. Fixed comparisons: It always performs
n(n−1)2\frac{n(n-1)}{2}2n(n−1) comparisons →
O(n²) time complexity, even if the data is nearly
sorted.
2. Non-adaptive: It doesn’t become faster for
partially sorted lists.
3. Full scans per pass: Each pass scans the
remaining array completely → poor scalability
compared to O(n log n) algorithms like Merge Sort
or Quick Sort.
4. Not stable: Equal elements can lose their original
order unless additional logic is added.
#include <iostream>
#include <vector>
using namespace std;
void selectionSortDescending(vector<int>& a) {
int n = static_cast<int>(a.size());
for (int i = 0; i < n - 1; ++i) {
int maxIndex = i; // assume a[i] is the largest in the
unsorted part
for (int j = i + 1; j < n; ++j) {
if (a[j] > a[maxIndex]) {
maxIndex = j;
}
}
if (maxIndex != i) {
int tmp = a[i];
a[i] = a[maxIndex];
a[maxIndex] = tmp;
}
}
}
int main() {
int n;
cout << "Enter number of elements: ";
if (!(cin >> n) || n <= 0) return 0;
vector<int> arr(n);
cout << "Enter " << n << " elements: ";
for (int i = 0; i < n; ++i) cin >> arr[i];
selectionSortDescending(arr);
cout << "Sorted (Descending): ";
for (int x : arr) cout << x << " ";
cout << "\n";
********** 28 **********
--- page 29 ---
return 0;

FAR ICR QA HH
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper de4835fc783a

- Departments: Data Science
- Programmes: BACHELOR OF TECHNOLOGY (DATA SCIENCE)SIX YEARS INTEGRATED PROGRAM - 7038
- Source: `00_Original_Downloads/2024/65247__Semester V__context_fixed.zip :: Final-Exam/BACHELOR OF TECHNOLOGY (DATA SCIENCE)SIX YEARS INTEGRATED PROGRAM - 7038/Basic Data Structures/ANS_Final-Exam_Basic Data Structures(701CO0C013)_Semester V_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2024
- Text: mixed (23 pages), mean OCR confidence 33.9
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester V(Exam Year: 2024-2025)
Subject: Basic Data Structures
Date: 28 Nov 2024   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Instruction Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary.
9. Figures in brackets on the right hand side indicate full marks
Q1
Answer briefly:   [20]
a.   Define data structures. Draw a diagram of classification of data structures and explain
each type.
. Data structure is a representation of the logical relationship existing between
individual elements of data.
[5]
A data structure is said to be Linear, if its elements are connected in linear
fashion by means of logically or in sequence memory locations.
•   There are two ways to represent a linear data structure in memory,
o   Static memory allocation – Fixed memory size
o Dynamic memory allocation – Memory allocation at runtime
Array
An array is a collection of similar data elements. These data elements have the
same data type. The elements are stored in consecutive/contiguous memory
locations and are referenced by an index.
data type variable_name[size];
•   Arrays are of fixed size.
********** 1 **********
--- page 2 ---
•   Insertion and deletion of elements can be problematic because of
shifting elements from their positions.
Linked list:
A linked list is a very flexible, dynamic data structure in which elements form a
sequential list.
•   Each node is allocated space as it is added to the list. Every node in the
list points to the next node in the list. Therefore, in a linked list, every
node contains the following two types of data:
• The value of the node
• A Pointer or link to the next node
Stack:
Stack is called a last-in, first-out (LIFO) structure because the last element which
is added to the stack is the first element which is deleted from the stack.
•   Insertion and deletion operations are done only from one end.
•   In the computer’s memory, stack can be implemented using arrays or
linked list.
• PUSH
• POP
• PEEp
Queue:
A queue is a first-in, first-out (FIFO) data structure in which the elements that
is inserted first is the first one to be taken out.
• The elements in a queue are added at one end called the rear and
removed from the other end called the front.
•   Operations performed on queue are:
• Enqueue
• Dequeue
Nonlinear data structures are those data structure in which data items are not
arranged in a sequence.
•   In a non-linear data structure, we can’t traverse all the elements in a
single run only.
•   Examples of Non-linear Data Structure are Tree and Graph.
b.
[5]
•
c.   Write a Program for Fibonacci series up to n terms using recursion .   [5]
********** 2 **********
--- page 3 ---
#include <stdio.h>
// Recursive function to return Fibonacci number at position 'n'
int fibonacci(int n) {
if (n == 0) {
return 0;   // Base case: 0th Fibonacci number is 0
} else if (n == 1) {
return 1;   // Base case: 1st Fibonacci number is 1
} else {
return fibonacci(n - 1) + fibonacci(n - 2); // Recursive case
}
}
int main() {
int n, i;
// Ask the user for the number of terms
printf("Enter the number of terms: ");
scanf("%d", &n);
// Print Fibonacci series up to n terms
printf("Fibonacci Series up to %d terms: ", n);
for (i = 0; i < n; i++) {
printf("%d ", fibonacci(i));
}
printf("\n");
return 0;
}
d.   An array ARR[-5…15, 10…20] stores elements in Row Major Wise with each element
requiring 2 bytes of storage. Find the address of ARR[10][15] when the base address is
2500.
[5]
Address of ARR[10][15]=2500+[(10−(−5))×11+(15−10)]×2
=2840
a.   Write a program for Bubble sort .Sort the elements 77, 49, 25, 12, 9, 33, 56, 81 using
Bubble sort.
#include <stdio.h>
Q2   [10]
b.
[10]
// Function to perform Bubble Sort
void bubbleSort(int arr[], int n) {
int i, j, temp;
********** 3 **********
--- page 4 ---
// Outer loop for each pass
for (i = 0; i < n - 1; i++) {
// Inner loop for comparing adjacent elements
for (j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
// Swap if the element found is greater than the next element
temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
}
}
}
}
// Function to print the array
void printArray(int arr[], int size) {
int i;
for (i = 0; i < size; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
int main() {
int arr[] = {77, 49, 25, 12, 9, 33, 56, 81}; // Given array
int n = sizeof(arr) / sizeof(arr[0]); // Calculate size of the array
// Display the original array
printf("Original array: ");
printArray(arr, n);
// Perform Bubble Sort
bubbleSort(arr, n);
// Display the sorted array
printf("Sorted array: ");
printArray(arr, n);
return 0;
}
********** 4 **********
--- page 5 ---
Write a program to define a structure for a restaurant that has the following
members—name, location, rating and average meal cost. Write a function to: (i) Print
the names of restaurants in a particular location.
(ii) Print the names of restaurants that have an average meal cost less than a specified
value.
#include <stdio.h>
#include <string.h>
#define MAX 100
// Defining structure for Restaurant
struct Restaurant {
char name[50];
char location[50];
float rating;
float avgMealCost;
};
// Function to print restaurant names in a particular location
void printRestaurantsByLocation(struct Restaurant restaurants[], int n, char location[])
{
printf("Restaurants in %s:\n", location);
for (int i = 0; i < n; i++) {
if (strcmp(restaurants[i].location, location) == 0) {
printf("- %s\n", restaurants[i].name);
}
}
}
// Function to print restaurant names with meal cost less than a specified value
void printRestaurantsByMealCost(struct Restaurant restaurants[], int n, float maxCost)
{
printf("Restaurants with an average meal cost less than %.2f:\n", maxCost);
for (int i = 0; i < n; i++) {
if (restaurants[i].avgMealCost < maxCost) {
printf("- %s\n", restaurants[i].name);
}
}
}
int main() {
int n;
********** 5 **********
--- page 6 ---
// Input number of restaurants
printf("Enter the number of restaurants: ");
scanf("%d", &n);
// Array of Restaurant structures
struct Restaurant restaurants[MAX];
// Input details for each restaurant
for (int i = 0; i < n; i++) {
printf("\nEnter details for restaurant %d:\n", i + 1);
printf("Name: ");
scanf(" %[^\n]", restaurants[i].name); // Reading string with spaces
printf("Location: ");
scanf(" %[^\n]", restaurants[i].location); // Reading string with spaces
printf("Rating: ");
scanf("%f", &restaurants[i].rating);
printf("Average Meal Cost: ");
scanf("%f", &restaurants[i].avgMealCost);
}
// Search by location
char searchLocation[50];
printf("\nEnter location to search restaurants: ");
scanf(" %[^\n]", searchLocation);
printRestaurantsByLocation(restaurants, n, searchLocation);
// Search by average meal cost
float maxCost;
printf("\nEnter maximum average meal cost to search restaurants: ");
scanf("%f", &maxCost);
printRestaurantsByMealCost(restaurants, n, maxCost);
return 0;
}
Q3   a.   Convert the following infix expression into postfix using a stack. At each step of the
conversion, display the contents of the stack and explain how each operator and operand   [10]
CO-1; SO-   is processed.
2; BL-2   b.
CO-2; SO-   Infix Expression:   [10]
1;   ((A + B) * (C - D) / (E + F * G) - H) + ((I * J) / (K - L) + M * N)
BL-2
********** 6 **********
--- page 7 ---
Ans: A B + C D - * E F G * + / H - I J * K L - / M N * + +
Write a program to delete the first element of a doubly linked list.
#include <stdio.h>
#include <stdlib.h>
// Defining the structure of a doubly linked list node
struct Node {
int data;
struct Node* prev;
struct Node* next;
};
// Function to create a new node
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->prev = NULL;
newNode->next = NULL;
return newNode;
}
// Function to delete the first node of the doubly linked list
void deleteFirst(struct Node** head) {
if (*head == NULL) {
printf("The list is already empty.\n");
return;
}
struct Node* temp = *head;
// If the list has more than one node
if (temp->next != NULL) {
*head = temp->next;
(*head)->prev = NULL;
} else {
// If there's only one node
*head = NULL;
}
[10]
Q4
a.   Write a C/C++ program to delete duplicates from 1-D array.
********** 7 **********
--- page 8 ---
CO-2; SO-   sample i/p: [ 1 2 1 4 3 2 1 3 2 1 4 5 7 6 9 9]
2;
BL-3   o/p: [ 1 2 4 3 5 7 6 9]   [10]
CO-1; SO-   b.   #include <iostream>
1;   using namespace std;
BL-1   int main ()
{
int A[10], B[10], n, i, j, k = 0;
cout << "Enter size of array : ";
cin >> n;
cout << "Enter elements of array : ";
for (i = 0; i < n; i++)
cin >> A[i];
for (i = 0; i < n; i++)
{
for (j = 0; j < k; j++)
{
if (A[i] == B[j])
break;
}
if (j == k)
{
B[k] = A[i];
k++;
}
}
cout << "after deletion elements of array : ";
for (i = 0; i < k; i++)
cout << B[i] << " ";
return 0;
}
Write a program to Create a linked list which stores names of the employees and their
salary. Delete the employee record with highest salary.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Structure to define a node in the linked list
struct Employee {
char name[50];
float salary;
struct Employee* next;
};
// Function to create a new node (employee)
struct Employee* createEmployee(char name[], float salary) {
struct Employee* newEmployee = (struct Employee*)malloc(sizeof(struct
Employee));
********** 8 **********
--- page 9 ---
strcpy(newEmployee->name, name);
newEmployee->salary = salary;
newEmployee->next = NULL;
return newEmployee;
}
// Function to insert an employee at the end of the linked list
void insertEmployee(struct Employee** head, char name[], float salary) {
struct Employee* newEmployee = createEmployee(name, salary);
if (*head == NULL) {
*head = newEmployee;
} else {
struct Employee* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newEmployee;
}
}
// Function to print the list of employees
void printEmployees(struct Employee* head) {
if (head == NULL) {
printf("No employees to display.\n");
return;
}
struct Employee* temp = head;
printf("Employee List:\n");
while (temp != NULL) {
printf("Name: %s, Salary: %.2f\n", temp->name, temp->salary);
temp = temp->next;
}
}
// Function to delete the employee with the highest salary
void deleteHighestSalary(struct Employee** head) {
if (*head == NULL) {
printf("The list is empty.\n");
return;
}
struct Employee *temp = *head, *maxPrev = NULL, *prev = NULL, *maxNode =
*head;
********** 9 **********
--- page 10 ---
// Find the employee with the highest salary
while (temp != NULL) {
if (temp->salary > maxNode->salary) {
maxPrev = prev;
maxNode = temp;
}
prev = temp;
temp = temp->next;
}
// If the highest salary node is the head
if (maxPrev == NULL) {
*head = maxNode->next;
} else {
maxPrev->next = maxNode->next;
}
printf("\nDeleted employee with highest salary: %s, Salary: %.2f\n", maxNode-
>name, maxNode->salary);
free(maxNode);
}
int main() {
struct Employee* head = NULL;
int n;
char name[50];
float salary;
// Input number of employees
printf("Enter the number of employees: ");
scanf("%d", &n);
// Input employee details and create the list
for (int i = 0; i < n; i++) {
printf("\nEnter details for employee %d:\n", i + 1);
printf("Name: ");
scanf(" %[^\n]", name); // Reading string with spaces
printf("Salary: ");
scanf("%f", &salary);
insertEmployee(&head, name, salary);
}
********** 10 **********
--- page 11 ---
// Print the initial list of employees
printf("\nBefore deletion:\n");
printEmployees(head);
// Delete the employee with the highest salary
deleteHighestSalary(&head);
// Print the list after deletion
printf("\nAfter deletion:\n");
printEmployees(head);
return 0;
}
a.   Explain the concept of a circular queue? How is it better than a linear queue?WAP in
C/C++ to implement Enque and Dqueue for circular queue.
oncept of a Circular Queue:
b.
A circular queue is a data structure that overcomes the limitations of a
linear queue by connecting the end of the queue back to the front. It
allows the queue to use the empty space left behind by dequeued
elements. In a linear queue, once an element is dequeued, the space is
left unused, which can lead to inefficiency when the queue has fixed
capacity.
In a circular queue:
Q5   • The front and rear pointers are used to track the start and end of
the queue.
CO-2; SO-   • When the rear reaches the end of the queue, it wraps around to   [10]
2;
BL-2   the front if there’s space (hence "circular").
• The condition rear + 1 == front (or modulo-based equivalent)
CO-1; SO-
1;   indicates the queue is full.   [10]
BL-2   • The condition front == rear indicates the queue is empty.
Why Circular Queue is Better than Linear Queue:
•   Efficient Memory Utilization: In a circular queue, after
dequeueing elements, the empty space at the front can be reused
for new elements, avoiding wastage of memory.
• No Shifting of Elements: Unlike a linear queue, where elements
need to be shifted when dequeuing, a circular queue does not
require any shifting.
• Better for Fixed-Size Queues: Circular queues are useful when
the maximum size of the queue is known, making it easier to
manage with limited resources like arrays.
#include <stdio.h>
********** 11 **********
--- page 12 ---
#include <stdlib.h>
#define MAX 5 // Define the maximum size of the circular queue
// Structure to represent the circular queue
struct CircularQueue {
int items[MAX];
int front, rear;
};
// Function to initialize the queue
void initializeQueue(struct CircularQueue* q) {
q->front = -1;
q->rear = -1;
}
// Function to check if the queue is full
int isFull(struct CircularQueue* q) {
if ((q->rear + 1) % MAX == q->front)
return 1;
return 0;
}
// Function to check if the queue is empty
int isEmpty(struct CircularQueue* q) {
if (q->front == -1)
return 1;
return 0;
}
// Function to insert (enqueue) an element in the queue
void enqueue(struct CircularQueue* q, int value) {
if (isFull(q)) {
printf("Queue is full! Cannot enqueue %d\n", value);
return;
}
if (isEmpty(q)) {
q->front = 0;
}
q->rear = (q->rear + 1) % MAX;
q->items[q->rear] = value;
printf("Enqueued %d\n", value);
********** 12 **********
--- page 13 ---
}
// Function to remove (dequeue) an element from the queue
int dequeue(struct CircularQueue* q) {
int value;
if (isEmpty(q)) {
printf("Queue is empty! Cannot dequeue.\n");
return -1;
}
value = q->items[q->front];
if (q->front == q->rear) {
// If there's only one element in the queue
q->front = q->rear = -1;
} else {
q->front = (q->front + 1) % MAX;
}
printf("Dequeued %d\n", value);
return value;
}
// Function to display the circular queue
void displayQueue(struct CircularQueue* q) {
if (isEmpty(q)) {
printf("Queue is empty.\n");
return;
}
printf("Queue elements: ");
int i = q->front;
while (1) {
printf("%d ", q->items[i]);
if (i == q->rear) break;
i = (i + 1) % MAX;
}
printf("\n");
}
int main() {
struct CircularQueue q;
initializeQueue(&q);
// Enqueue some elements
********** 13 **********
--- page 14 ---
enqueue(&q, 10);
enqueue(&q, 20);
enqueue(&q, 30);
enqueue(&q, 40);
enqueue(&q, 50); // Queue is full after this
// Display the queue
displayQueue(&q);
// Try enqueueing another element
enqueue(&q, 60); // Should show "Queue is full"
// Dequeue some elements
dequeue(&q);
dequeue(&q);
// Display the queue after dequeuing
displayQueue(&q);
// Enqueue more elements
enqueue(&q, 60);
enqueue(&q, 70);
// Display the queue
displayQueue(&q);
return 0;
}
Write a program to print the total number of occurrences of a given item in the linked
list.
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a node
struct Node {
int data;
struct Node* next;
};
// Function to create a new node
struct Node* createNode(int value) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = value;
********** 14 **********
--- page 15 ---
newNode->next = NULL;
return newNode;
}
// Function to insert a node at the end of the linked list
void insertNode(struct Node** head, int value) {
struct Node* newNode = createNode(value);
if (*head == NULL) {
*head = newNode;
} else {
struct Node* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newNode;
}
}
// Function to count the occurrences of a given item in the linked list
int countOccurrences(struct Node* head, int item) {
int count = 0;
struct Node* temp = head;
while (temp != NULL) {
if (temp->data == item) {
count++;
}
temp = temp->next;
}
return count;
}
// Function to display the linked list
void displayList(struct Node* head) {
struct Node* temp = head;
printf("Linked List: ");
while (temp != NULL) {
printf("%d -> ", temp->data);
temp = temp->next;
}
printf("NULL\n");
}
********** 15 **********
--- page 16 ---
int main() {
struct Node* head = NULL;
int n, value, item;
// Insert elements into the linked list
printf("Enter the number of elements to insert: ");
scanf("%d", &n);
for (int i = 0; i < n; i++) {
printf("Enter element %d: ", i + 1);
scanf("%d", &value);
insertNode(&head, value);
}
// Display the linked list
displayList(head);
// Input the item to find its occurrences
printf("Enter the item to find its occurrences: ");
scanf("%d", &item);
// Count and display the occurrences of the item
int occurrences = countOccurrences(head, item);
printf("Total occurrences of %d in the linked list: %d\n", item, occurrences);
return 0;
}
Write a program to manage a simple inventory system for a store. Each inventory item
should have a name, quantity, and price. Implement this inventory system using a
singly linked list. Write a program that allows users to add new items to the inventory,
a.   update the quantity of existing items, display the current inventory, and remove items
from the inventory.
b.
#include <stdio.h>
Q6
#include <stdlib.h>
CO-1;   #include <string.h>
SO-;2   [10]
BL-2   // Define the structure for an inventory item
struct InventoryItem {
CO-3; SO-
1;   char name[50];   [10]
int quantity;
BL-2
float price;
struct InventoryItem* next;
};
// Function to create a new inventory item
struct InventoryItem* createItem(const char* name, int quantity, float price) {
struct InventoryItem* newItem = (struct InventoryItem*)malloc(sizeof(struct
InventoryItem));
********** 16 **********
--- page 17 ---
strcpy(newItem->name, name);
newItem->quantity = quantity;
newItem->price = price;
newItem->next = NULL;
return newItem;
}
// Function to add an item to the inventory
void addItem(struct InventoryItem** head, const char* name, int quantity, float price)
{
struct InventoryItem* newItem = createItem(name, quantity, price);
newItem->next = *head;
*head = newItem;
printf("Item '%s' added to the inventory.\n", name);
}
// Function to update the quantity of an existing item
void updateItem(struct InventoryItem* head, const char* name, int quantity) {
struct InventoryItem* temp = head;
while (temp != NULL) {
if (strcmp(temp->name, name) == 0) {
temp->quantity += quantity;
printf("Updated quantity of '%s' to %d.\n", name, temp->quantity);
return;
}
temp = temp->next;
}
printf("Item '%s' not found in the inventory.\n", name);
}
// Function to display the current inventory
void displayInventory(struct InventoryItem* head) {
if (head == NULL) {
printf("Inventory is empty.\n");
return;
}
printf("\nCurrent Inventory:\n");
printf("%-20s %-10s %-10s\n", "Item Name", "Quantity", "Price");
struct InventoryItem* temp = head;
while (temp != NULL) {
printf("%-20s %-10d $%-10.2f\n", temp->name, temp->quantity, temp->price);
temp = temp->next;
}
}
// Function to remove an item from the inventory
void removeItem(struct InventoryItem** head, const char* name) {
struct InventoryItem* temp = *head;
struct InventoryItem* prev = NULL;
// If the item to be removed is the head
if (temp != NULL && strcmp(temp->name, name) == 0) {
*head = temp->next; // Change head
free(temp); // Free old head
printf("Item '%s' removed from the inventory.\n", name);
return;
}
// Search for the item to be removed
while (temp != NULL && strcmp(temp->name, name) != 0) {
prev = temp;
temp = temp->next;
}
********** 17 **********
--- page 18 ---
// If the item was not found
if (temp == NULL) {
printf("Item '%s' not found in the inventory.\n", name);
return;
}
// Unlink the node from the linked list
prev->next = temp->next;
free(temp); // Free memory
printf("Item '%s' removed from the inventory.\n", name);
}
int main() {
struct InventoryItem* inventory = NULL;
int choice;
char name[50];
int quantity;
float price;
do {
printf("\nInventory Management System\n");
printf("1. Add Item\n");
printf("2. Update Item Quantity\n");
printf("3. Display Inventory\n");
printf("4. Remove Item\n");
printf("5. Exit\n");
printf("Enter your choice: ");
scanf("%d", &choice);
switch (choice) {
case 1:
printf("Enter item name: ");
scanf("%s", name);
printf("Enter quantity: ");
scanf("%d", &quantity);
printf("Enter price: ");
scanf("%f", &price);
addItem(&inventory, name, quantity, price);
break;
case 2:
printf("Enter item name to update: ");
scanf("%s", name);
printf("Enter quantity to add: ");
scanf("%d", &quantity);
updateItem(inventory, name, quantity);
break;
case 3:
displayInventory(inventory);
break;
case 4:
printf("Enter item name to remove: ");
scanf("%s", name);
removeItem(&inventory, name);
break;
case 5:
printf("Exiting the program.\n");
break;
default:
printf("Invalid choice! Please try again.\n");
}
} while (choice != 5);
// Free the allocated memory
struct InventoryItem* temp;
********** 18 **********
--- page 19 ---
while (inventory != NULL) {
temp = inventory;
inventory = inventory->next;
free(temp);
}
return 0;
}
Compare and contrast selection and insertion sort. Write the algorithm for selection
sort.
#include <stdio.h>
void selectionSort(int arr[], int n) {
int i, j, min_index, temp;
for (i = 0; i < n - 1; i++) {
min_index = i; // Assume the minimum is the first element in the unsorted part
// Find the minimum element in the unsorted array
for (j = i + 1; j < n; j++) {
if (arr[j] < arr[min_index]) {
min_index = j; // Update the index of the minimum element
}
}
// Swap the found minimum element with the first element of the unsorted part
temp = arr[min_index];
arr[min_index] = arr[i];
arr[i] = temp;
}
}
int main() {
int arr[] = {64, 25, 12, 22, 11};
int n = sizeof(arr) / sizeof(arr[0]);
printf("Original array: \n");
for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
selectionSort(arr, n);
printf("Sorted array: \n");
********** 19 **********
--- page 20 ---
for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
return 0;
}
Compare and contrast a queue with a stack. Implement stack ADT operation using link
list.
a.
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a stack node
struct StackNode {
int data;
struct StackNode* next;
};
// Define the structure for the stack
struct Stack {
struct StackNode* top;
};
// Function to create a new stack node
struct StackNode* newNode(int data) {
b.   struct StackNode* stackNode = (struct StackNode*)malloc(sizeof(struct
StackNode));
stackNode->data = data;
stackNode->next = NULL;
Q7
return stackNode;
CO-2; SO-   }
1   [10]
BL-2   // Function to create an empty stack
struct Stack* createStack() {   [10]
CO-3; SO-
struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
1;
stack->top = NULL;
BL-2
return stack;
}
// Function to check if the stack is empty
int isEmpty(struct Stack* stack) {
return stack->top == NULL;
}
// Function to add an item to the stack
void push(struct Stack* stack, int data) {
struct StackNode* stackNode = newNode(data);
stackNode->next = stack->top;
stack->top = stackNode;
printf("%d pushed to stack\n", data);
}
// Function to remove an item from the stack
int pop(struct Stack* stack) {
if (isEmpty(stack)) {
printf("Stack underflow\n");
return -1; // Return an invalid value for underflow
}
struct StackNode* temp = stack->top;
stack->top = stack->top->next;
********** 20 **********
--- page 21 ---
int popped = temp->data;
free(temp);
return popped;
}
// Function to display the stack
void display(struct Stack* stack) {
struct StackNode* current = stack->top;
printf("Stack elements: ");
while (current != NULL) {
printf("%d ", current->data);
current = current->next;
}
printf("\n");
}
// Main function to demonstrate stack operations
int main() {
struct Stack* stack = createStack();
push(stack, 10);
push(stack, 20);
push(stack, 30);
display(stack);
printf("%d popped from stack\n", pop(stack));
display(stack);
return 0;
}
Write a program in C to print a string in reverse using a pointer.
#include <stdio.h>
// Function to print a string in reverse using pointers
void printReverse(char *str) {
// Move the pointer to the end of the string
char *end = str;
while (*end != '\0') {
end++;
}
end--; // Move back to the last character (excluding the null terminator)
// Print the string in reverse
while (end >= str) {
printf("%c", *end);
end--;
}
printf("\n"); // Print a newline at the end
}
int main() {
char str[100];
// Get user input
printf("Enter a string: ");
fgets(str, sizeof(str), stdin); // Using fgets to include spaces and avoid overflow
// Remove the newline character from the input if present
char *newline = str;
while (*newline != '\0') {
if (*newline == '\n') {
********** 21 **********
--- page 22 ---
*newline = '\0';
break;
}
newline++;
}
// Print the string in reverse
printf("Reversed string: ");
printReverse(str);
return 0;
}
********** 22 **********
--- page 23 ---
FIR ICR 2 I OH
````

## 2024-25 · Final-Exam · Sem 4 · Answer key · paper b5d42fba8e97

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_04/Final-Exam/Integrated_IT_7037/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2025
- Text: text (2 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: II/Semester IV(Exam Year: 2024-2025)
Subject: Basic Data Structures
Date: 02 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Detailed Answer with Marks Distribution
Answer briefly:   [20]
a.   Definition: (2M) - A data structure is a
way of organizing and storing data to
CO-1;   enable efficient access and modification.
Define data structures and explain their
BL-   Importance in Programming: (3M) -   [5 M]
importance in programming.
1,2   Enhances code efficiency, optimizes
memory usage, and improves
performance in problem-solving.
b. A hospital management system needs to   Usage of Structures: (2M) - Stores
store   and   update   patient   records   multiple attributes per patient (Name,
CO-
dynamically. How can structures and   Age, Diagnosis). Pointers in Dynamic
2,BL-   [5 M]
pointers be used to efficiently manage   Storage: (3M) - Enable dynamic memory
3,4
patient details?   allocation, allowing efficient addition and
removal of patient records.
c.   Push Operation: (2M) - Inserts an element
CO-3;   at the top of the stack. Pop Operation:
Explain the push and pop operations in a
BL-   (2M) - Removes the top element from the   [5 M]
stack with an example.
3,4   stack. Example: (1M) - Stack used in
undo operations.
d. A university admission system needs to Efficient Algorithm: (2M) - Merge Sort or
CO-4;   sort thousands of applications based on   Quick Sort. Reasoning: (3M) - Merge
[5 M]
BL-4   student scores. Which sorting algorithm   Sort for stability and large data, Quick
would be most efficient, and why?   Sort for faster average-case performance.
Q2   [20]
a.   Discuss the advantages and disadvantages   Advantages: (5M) - Efficient memory
CO-1;
of dynamic memory allocation in data   usage, flexibility. Disadvantages: (5M) -
BL-   [10 M]
structure and its impact on performance.   Risk of memory leaks, slower access
1,2
time.
CO-2;   b.   Differentiate between arrays and linked   Arrays: (5M) - Fixed size, fast indexing
BL-   lists. Compare   their advantages and   but costly insertions/deletions. Linked   [10 M]
1,4   limitations with examples.
********** 1 **********
--- page 2 ---
Lists: (5M) - Dynamic size, efficient
insertions/deletions but slower access.
Q3   [20]
a.   Explain the concept of stack in data   Stack Concept: (3M) - Uses LIFO (Last
CO-3;
structures. Discuss its LIFO property with   In, First Out) approach. Real-World
BL-   [10 M]
real-world applications.   Examples: (7M) - Function call stack,
1,4
undo feature in software.
b.   Define abstract data types (ADT) and   Definition: (3M) - ADT defines data
CO-2;   explain their significance in data structure   structures independently of
BL-   design.   implementation. Significance: (7M) -   [10 M]
2,3   Provides abstraction and reusability in
programming.
Q4   [20]
a.   Write a C++ code to declare a structure,   Structure Definition: (5M) - Declare
CO-2;   store student details, and access   its   student struct with Name, Age, Marks.
[10 M]
BL-3   elements.   Access & Print Elements: (5M) - Create
object, assign values, print data.
b.   Write a C++ function to find the largest   Code Implementation: (5M) - Loop
CO-3;   element in an array. How do arrays and   through array, store max value. Memory
BL-   pointers differ in memory management?   Management: (5M) - Arrays use static   [10 M]
3,6   memory, pointers allow dynamic
allocation.
Q5   [20]
a.   Write a C++ program to implement a stack   Program Explanation: (4M) - Stack class
CO-3;
using an array with push, pop, and display   with array, top variable. Code
BL-   [10 M]
operations.   Implementation: (6M) - Implement push,
1,3
pop, and display functions.
b.   Program Explanation: (4M) - Circular
WAP to implement a C++ program for a
CO-3;   queue avoids memory wastage. Code
Circular Queue with enqueue and dequeue   [10 M]
BL-4   Implementation: (6M) - Implement
operation.
enqueue, dequeue, and display.
Q6   [20]
a.   Discuss two real-world applications of   Applications: (4M) - CPU scheduling,
CO-3;
queues. Write a pseudo-code for enqueue   printer jobs. Pseudo-code: (6M) - Show   [10 M]
BL-5
and dequeue operations in a simple queue.   enqueue and dequeue implementation.
b.   Describe the process of inserting a node at   Insertion at Beginning: (5M) - Create new
CO-3;   the beginning and end of a singly linked   node, point to head, update head.
[10 M]
BL-3   list.   Insertion at End: (5M) - Traverse list,
update last node's next pointer.
Q7   [20]
a. What is the advantage of recursive binary   Recursive vs Iterative: (4M) - Recursive
CO-4;   search over   iterative binary search?   is elegant, but may have stack overhead.
BL-   Provide a scenario where recursive binary   Scenarios: (6M) - Recursive useful for   [10 M]
2,4   search is preferred and another where   large sorted datasets, iterative preferred
iterative binary search is more suitable   for memory constraints.
b.   Definition: (3M) - A linked list where the
CO-3;
What is a circular linked list? Explain its   last node points back to the first.
BL-   [10 M]
advantages over a singly linked list.   Advantages: (7M) - Efficient in real-time
2,4
systems, avoids null terminations.
********** 2 **********
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper bff0c72d7794

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/Integrated_Computer_7032/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2024
- Text: mixed (23 pages), mean OCR confidence 33.9
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester V(Exam Year: 2024-2025)
Subject: Basic Data Structures
Date: 28 Nov 2024   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Instruction Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary.
9. Figures in brackets on the right hand side indicate full marks
Q1
Answer briefly:   [20]
a.   Define data structures. Draw a diagram of classification of data structures and explain
each type.
. Data structure is a representation of the logical relationship existing between
individual elements of data.
[5]
A data structure is said to be Linear, if its elements are connected in linear
fashion by means of logically or in sequence memory locations.
•   There are two ways to represent a linear data structure in memory,
o   Static memory allocation – Fixed memory size
o Dynamic memory allocation – Memory allocation at runtime
Array
An array is a collection of similar data elements. These data elements have the
same data type. The elements are stored in consecutive/contiguous memory
locations and are referenced by an index.
data type variable_name[size];
•   Arrays are of fixed size.
********** 1 **********
--- page 2 ---
•   Insertion and deletion of elements can be problematic because of
shifting elements from their positions.
Linked list:
A linked list is a very flexible, dynamic data structure in which elements form a
sequential list.
•   Each node is allocated space as it is added to the list. Every node in the
list points to the next node in the list. Therefore, in a linked list, every
node contains the following two types of data:
• The value of the node
• A Pointer or link to the next node
Stack:
Stack is called a last-in, first-out (LIFO) structure because the last element which
is added to the stack is the first element which is deleted from the stack.
•   Insertion and deletion operations are done only from one end.
•   In the computer’s memory, stack can be implemented using arrays or
linked list.
• PUSH
• POP
• PEEp
Queue:
A queue is a first-in, first-out (FIFO) data structure in which the elements that
is inserted first is the first one to be taken out.
• The elements in a queue are added at one end called the rear and
removed from the other end called the front.
•   Operations performed on queue are:
• Enqueue
• Dequeue
Nonlinear data structures are those data structure in which data items are not
arranged in a sequence.
•   In a non-linear data structure, we can’t traverse all the elements in a
single run only.
•   Examples of Non-linear Data Structure are Tree and Graph.
b.
[5]
•
c.   Write a Program for Fibonacci series up to n terms using recursion .   [5]
********** 2 **********
--- page 3 ---
#include <stdio.h>
// Recursive function to return Fibonacci number at position 'n'
int fibonacci(int n) {
if (n == 0) {
return 0;   // Base case: 0th Fibonacci number is 0
} else if (n == 1) {
return 1;   // Base case: 1st Fibonacci number is 1
} else {
return fibonacci(n - 1) + fibonacci(n - 2); // Recursive case
}
}
int main() {
int n, i;
// Ask the user for the number of terms
printf("Enter the number of terms: ");
scanf("%d", &n);
// Print Fibonacci series up to n terms
printf("Fibonacci Series up to %d terms: ", n);
for (i = 0; i < n; i++) {
printf("%d ", fibonacci(i));
}
printf("\n");
return 0;
}
d.   An array ARR[-5…15, 10…20] stores elements in Row Major Wise with each element
requiring 2 bytes of storage. Find the address of ARR[10][15] when the base address is
2500.
[5]
Address of ARR[10][15]=2500+[(10−(−5))×11+(15−10)]×2
=2840
a.   Write a program for Bubble sort .Sort the elements 77, 49, 25, 12, 9, 33, 56, 81 using
Bubble sort.
#include <stdio.h>
Q2   [10]
b.
[10]
// Function to perform Bubble Sort
void bubbleSort(int arr[], int n) {
int i, j, temp;
********** 3 **********
--- page 4 ---
// Outer loop for each pass
for (i = 0; i < n - 1; i++) {
// Inner loop for comparing adjacent elements
for (j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
// Swap if the element found is greater than the next element
temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
}
}
}
}
// Function to print the array
void printArray(int arr[], int size) {
int i;
for (i = 0; i < size; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
int main() {
int arr[] = {77, 49, 25, 12, 9, 33, 56, 81}; // Given array
int n = sizeof(arr) / sizeof(arr[0]); // Calculate size of the array
// Display the original array
printf("Original array: ");
printArray(arr, n);
// Perform Bubble Sort
bubbleSort(arr, n);
// Display the sorted array
printf("Sorted array: ");
printArray(arr, n);
return 0;
}
********** 4 **********
--- page 5 ---
Write a program to define a structure for a restaurant that has the following
members—name, location, rating and average meal cost. Write a function to: (i) Print
the names of restaurants in a particular location.
(ii) Print the names of restaurants that have an average meal cost less than a specified
value.
#include <stdio.h>
#include <string.h>
#define MAX 100
// Defining structure for Restaurant
struct Restaurant {
char name[50];
char location[50];
float rating;
float avgMealCost;
};
// Function to print restaurant names in a particular location
void printRestaurantsByLocation(struct Restaurant restaurants[], int n, char location[])
{
printf("Restaurants in %s:\n", location);
for (int i = 0; i < n; i++) {
if (strcmp(restaurants[i].location, location) == 0) {
printf("- %s\n", restaurants[i].name);
}
}
}
// Function to print restaurant names with meal cost less than a specified value
void printRestaurantsByMealCost(struct Restaurant restaurants[], int n, float maxCost)
{
printf("Restaurants with an average meal cost less than %.2f:\n", maxCost);
for (int i = 0; i < n; i++) {
if (restaurants[i].avgMealCost < maxCost) {
printf("- %s\n", restaurants[i].name);
}
}
}
int main() {
int n;
********** 5 **********
--- page 6 ---
// Input number of restaurants
printf("Enter the number of restaurants: ");
scanf("%d", &n);
// Array of Restaurant structures
struct Restaurant restaurants[MAX];
// Input details for each restaurant
for (int i = 0; i < n; i++) {
printf("\nEnter details for restaurant %d:\n", i + 1);
printf("Name: ");
scanf(" %[^\n]", restaurants[i].name); // Reading string with spaces
printf("Location: ");
scanf(" %[^\n]", restaurants[i].location); // Reading string with spaces
printf("Rating: ");
scanf("%f", &restaurants[i].rating);
printf("Average Meal Cost: ");
scanf("%f", &restaurants[i].avgMealCost);
}
// Search by location
char searchLocation[50];
printf("\nEnter location to search restaurants: ");
scanf(" %[^\n]", searchLocation);
printRestaurantsByLocation(restaurants, n, searchLocation);
// Search by average meal cost
float maxCost;
printf("\nEnter maximum average meal cost to search restaurants: ");
scanf("%f", &maxCost);
printRestaurantsByMealCost(restaurants, n, maxCost);
return 0;
}
Q3   a.   Convert the following infix expression into postfix using a stack. At each step of the
conversion, display the contents of the stack and explain how each operator and operand   [10]
CO-1; SO-   is processed.
2; BL-2   b.
CO-2; SO-   Infix Expression:   [10]
1;   ((A + B) * (C - D) / (E + F * G) - H) + ((I * J) / (K - L) + M * N)
BL-2
********** 6 **********
--- page 7 ---
Ans: A B + C D - * E F G * + / H - I J * K L - / M N * + +
Write a program to delete the first element of a doubly linked list.
#include <stdio.h>
#include <stdlib.h>
// Defining the structure of a doubly linked list node
struct Node {
int data;
struct Node* prev;
struct Node* next;
};
// Function to create a new node
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->prev = NULL;
newNode->next = NULL;
return newNode;
}
// Function to delete the first node of the doubly linked list
void deleteFirst(struct Node** head) {
if (*head == NULL) {
printf("The list is already empty.\n");
return;
}
struct Node* temp = *head;
// If the list has more than one node
if (temp->next != NULL) {
*head = temp->next;
(*head)->prev = NULL;
} else {
// If there's only one node
*head = NULL;
}
[10]
Q4
a.   Write a C/C++ program to delete duplicates from 1-D array.
********** 7 **********
--- page 8 ---
CO-2; SO-   sample i/p: [ 1 2 1 4 3 2 1 3 2 1 4 5 7 6 9 9]
2;
BL-3   o/p: [ 1 2 4 3 5 7 6 9]   [10]
CO-1; SO-   b.   #include <iostream>
1;   using namespace std;
BL-1   int main ()
{
int A[10], B[10], n, i, j, k = 0;
cout << "Enter size of array : ";
cin >> n;
cout << "Enter elements of array : ";
for (i = 0; i < n; i++)
cin >> A[i];
for (i = 0; i < n; i++)
{
for (j = 0; j < k; j++)
{
if (A[i] == B[j])
break;
}
if (j == k)
{
B[k] = A[i];
k++;
}
}
cout << "after deletion elements of array : ";
for (i = 0; i < k; i++)
cout << B[i] << " ";
return 0;
}
Write a program to Create a linked list which stores names of the employees and their
salary. Delete the employee record with highest salary.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Structure to define a node in the linked list
struct Employee {
char name[50];
float salary;
struct Employee* next;
};
// Function to create a new node (employee)
struct Employee* createEmployee(char name[], float salary) {
struct Employee* newEmployee = (struct Employee*)malloc(sizeof(struct
Employee));
********** 8 **********
--- page 9 ---
strcpy(newEmployee->name, name);
newEmployee->salary = salary;
newEmployee->next = NULL;
return newEmployee;
}
// Function to insert an employee at the end of the linked list
void insertEmployee(struct Employee** head, char name[], float salary) {
struct Employee* newEmployee = createEmployee(name, salary);
if (*head == NULL) {
*head = newEmployee;
} else {
struct Employee* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newEmployee;
}
}
// Function to print the list of employees
void printEmployees(struct Employee* head) {
if (head == NULL) {
printf("No employees to display.\n");
return;
}
struct Employee* temp = head;
printf("Employee List:\n");
while (temp != NULL) {
printf("Name: %s, Salary: %.2f\n", temp->name, temp->salary);
temp = temp->next;
}
}
// Function to delete the employee with the highest salary
void deleteHighestSalary(struct Employee** head) {
if (*head == NULL) {
printf("The list is empty.\n");
return;
}
struct Employee *temp = *head, *maxPrev = NULL, *prev = NULL, *maxNode =
*head;
********** 9 **********
--- page 10 ---
// Find the employee with the highest salary
while (temp != NULL) {
if (temp->salary > maxNode->salary) {
maxPrev = prev;
maxNode = temp;
}
prev = temp;
temp = temp->next;
}
// If the highest salary node is the head
if (maxPrev == NULL) {
*head = maxNode->next;
} else {
maxPrev->next = maxNode->next;
}
printf("\nDeleted employee with highest salary: %s, Salary: %.2f\n", maxNode-
>name, maxNode->salary);
free(maxNode);
}
int main() {
struct Employee* head = NULL;
int n;
char name[50];
float salary;
// Input number of employees
printf("Enter the number of employees: ");
scanf("%d", &n);
// Input employee details and create the list
for (int i = 0; i < n; i++) {
printf("\nEnter details for employee %d:\n", i + 1);
printf("Name: ");
scanf(" %[^\n]", name); // Reading string with spaces
printf("Salary: ");
scanf("%f", &salary);
insertEmployee(&head, name, salary);
}
********** 10 **********
--- page 11 ---
// Print the initial list of employees
printf("\nBefore deletion:\n");
printEmployees(head);
// Delete the employee with the highest salary
deleteHighestSalary(&head);
// Print the list after deletion
printf("\nAfter deletion:\n");
printEmployees(head);
return 0;
}
a.   Explain the concept of a circular queue? How is it better than a linear queue?WAP in
C/C++ to implement Enque and Dqueue for circular queue.
oncept of a Circular Queue:
b.
A circular queue is a data structure that overcomes the limitations of a
linear queue by connecting the end of the queue back to the front. It
allows the queue to use the empty space left behind by dequeued
elements. In a linear queue, once an element is dequeued, the space is
left unused, which can lead to inefficiency when the queue has fixed
capacity.
In a circular queue:
Q5   • The front and rear pointers are used to track the start and end of
the queue.
CO-2; SO-   • When the rear reaches the end of the queue, it wraps around to   [10]
2;
BL-2   the front if there’s space (hence "circular").
• The condition rear + 1 == front (or modulo-based equivalent)
CO-1; SO-
1;   indicates the queue is full.   [10]
BL-2   • The condition front == rear indicates the queue is empty.
Why Circular Queue is Better than Linear Queue:
•   Efficient Memory Utilization: In a circular queue, after
dequeueing elements, the empty space at the front can be reused
for new elements, avoiding wastage of memory.
• No Shifting of Elements: Unlike a linear queue, where elements
need to be shifted when dequeuing, a circular queue does not
require any shifting.
• Better for Fixed-Size Queues: Circular queues are useful when
the maximum size of the queue is known, making it easier to
manage with limited resources like arrays.
#include <stdio.h>
********** 11 **********
--- page 12 ---
#include <stdlib.h>
#define MAX 5 // Define the maximum size of the circular queue
// Structure to represent the circular queue
struct CircularQueue {
int items[MAX];
int front, rear;
};
// Function to initialize the queue
void initializeQueue(struct CircularQueue* q) {
q->front = -1;
q->rear = -1;
}
// Function to check if the queue is full
int isFull(struct CircularQueue* q) {
if ((q->rear + 1) % MAX == q->front)
return 1;
return 0;
}
// Function to check if the queue is empty
int isEmpty(struct CircularQueue* q) {
if (q->front == -1)
return 1;
return 0;
}
// Function to insert (enqueue) an element in the queue
void enqueue(struct CircularQueue* q, int value) {
if (isFull(q)) {
printf("Queue is full! Cannot enqueue %d\n", value);
return;
}
if (isEmpty(q)) {
q->front = 0;
}
q->rear = (q->rear + 1) % MAX;
q->items[q->rear] = value;
printf("Enqueued %d\n", value);
********** 12 **********
--- page 13 ---
}
// Function to remove (dequeue) an element from the queue
int dequeue(struct CircularQueue* q) {
int value;
if (isEmpty(q)) {
printf("Queue is empty! Cannot dequeue.\n");
return -1;
}
value = q->items[q->front];
if (q->front == q->rear) {
// If there's only one element in the queue
q->front = q->rear = -1;
} else {
q->front = (q->front + 1) % MAX;
}
printf("Dequeued %d\n", value);
return value;
}
// Function to display the circular queue
void displayQueue(struct CircularQueue* q) {
if (isEmpty(q)) {
printf("Queue is empty.\n");
return;
}
printf("Queue elements: ");
int i = q->front;
while (1) {
printf("%d ", q->items[i]);
if (i == q->rear) break;
i = (i + 1) % MAX;
}
printf("\n");
}
int main() {
struct CircularQueue q;
initializeQueue(&q);
// Enqueue some elements
********** 13 **********
--- page 14 ---
enqueue(&q, 10);
enqueue(&q, 20);
enqueue(&q, 30);
enqueue(&q, 40);
enqueue(&q, 50); // Queue is full after this
// Display the queue
displayQueue(&q);
// Try enqueueing another element
enqueue(&q, 60); // Should show "Queue is full"
// Dequeue some elements
dequeue(&q);
dequeue(&q);
// Display the queue after dequeuing
displayQueue(&q);
// Enqueue more elements
enqueue(&q, 60);
enqueue(&q, 70);
// Display the queue
displayQueue(&q);
return 0;
}
Write a program to print the total number of occurrences of a given item in the linked
list.
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a node
struct Node {
int data;
struct Node* next;
};
// Function to create a new node
struct Node* createNode(int value) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = value;
********** 14 **********
--- page 15 ---
newNode->next = NULL;
return newNode;
}
// Function to insert a node at the end of the linked list
void insertNode(struct Node** head, int value) {
struct Node* newNode = createNode(value);
if (*head == NULL) {
*head = newNode;
} else {
struct Node* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newNode;
}
}
// Function to count the occurrences of a given item in the linked list
int countOccurrences(struct Node* head, int item) {
int count = 0;
struct Node* temp = head;
while (temp != NULL) {
if (temp->data == item) {
count++;
}
temp = temp->next;
}
return count;
}
// Function to display the linked list
void displayList(struct Node* head) {
struct Node* temp = head;
printf("Linked List: ");
while (temp != NULL) {
printf("%d -> ", temp->data);
temp = temp->next;
}
printf("NULL\n");
}
********** 15 **********
--- page 16 ---
int main() {
struct Node* head = NULL;
int n, value, item;
// Insert elements into the linked list
printf("Enter the number of elements to insert: ");
scanf("%d", &n);
for (int i = 0; i < n; i++) {
printf("Enter element %d: ", i + 1);
scanf("%d", &value);
insertNode(&head, value);
}
// Display the linked list
displayList(head);
// Input the item to find its occurrences
printf("Enter the item to find its occurrences: ");
scanf("%d", &item);
// Count and display the occurrences of the item
int occurrences = countOccurrences(head, item);
printf("Total occurrences of %d in the linked list: %d\n", item, occurrences);
return 0;
}
Write a program to manage a simple inventory system for a store. Each inventory item
should have a name, quantity, and price. Implement this inventory system using a
singly linked list. Write a program that allows users to add new items to the inventory,
a.   update the quantity of existing items, display the current inventory, and remove items
from the inventory.
b.
#include <stdio.h>
Q6
#include <stdlib.h>
CO-1;   #include <string.h>
SO-;2   [10]
BL-2   // Define the structure for an inventory item
struct InventoryItem {
CO-3; SO-
1;   char name[50];   [10]
int quantity;
BL-2
float price;
struct InventoryItem* next;
};
// Function to create a new inventory item
struct InventoryItem* createItem(const char* name, int quantity, float price) {
struct InventoryItem* newItem = (struct InventoryItem*)malloc(sizeof(struct
InventoryItem));
********** 16 **********
--- page 17 ---
strcpy(newItem->name, name);
newItem->quantity = quantity;
newItem->price = price;
newItem->next = NULL;
return newItem;
}
// Function to add an item to the inventory
void addItem(struct InventoryItem** head, const char* name, int quantity, float price)
{
struct InventoryItem* newItem = createItem(name, quantity, price);
newItem->next = *head;
*head = newItem;
printf("Item '%s' added to the inventory.\n", name);
}
// Function to update the quantity of an existing item
void updateItem(struct InventoryItem* head, const char* name, int quantity) {
struct InventoryItem* temp = head;
while (temp != NULL) {
if (strcmp(temp->name, name) == 0) {
temp->quantity += quantity;
printf("Updated quantity of '%s' to %d.\n", name, temp->quantity);
return;
}
temp = temp->next;
}
printf("Item '%s' not found in the inventory.\n", name);
}
// Function to display the current inventory
void displayInventory(struct InventoryItem* head) {
if (head == NULL) {
printf("Inventory is empty.\n");
return;
}
printf("\nCurrent Inventory:\n");
printf("%-20s %-10s %-10s\n", "Item Name", "Quantity", "Price");
struct InventoryItem* temp = head;
while (temp != NULL) {
printf("%-20s %-10d $%-10.2f\n", temp->name, temp->quantity, temp->price);
temp = temp->next;
}
}
// Function to remove an item from the inventory
void removeItem(struct InventoryItem** head, const char* name) {
struct InventoryItem* temp = *head;
struct InventoryItem* prev = NULL;
// If the item to be removed is the head
if (temp != NULL && strcmp(temp->name, name) == 0) {
*head = temp->next; // Change head
free(temp); // Free old head
printf("Item '%s' removed from the inventory.\n", name);
return;
}
// Search for the item to be removed
while (temp != NULL && strcmp(temp->name, name) != 0) {
prev = temp;
temp = temp->next;
}
********** 17 **********
--- page 18 ---
// If the item was not found
if (temp == NULL) {
printf("Item '%s' not found in the inventory.\n", name);
return;
}
// Unlink the node from the linked list
prev->next = temp->next;
free(temp); // Free memory
printf("Item '%s' removed from the inventory.\n", name);
}
int main() {
struct InventoryItem* inventory = NULL;
int choice;
char name[50];
int quantity;
float price;
do {
printf("\nInventory Management System\n");
printf("1. Add Item\n");
printf("2. Update Item Quantity\n");
printf("3. Display Inventory\n");
printf("4. Remove Item\n");
printf("5. Exit\n");
printf("Enter your choice: ");
scanf("%d", &choice);
switch (choice) {
case 1:
printf("Enter item name: ");
scanf("%s", name);
printf("Enter quantity: ");
scanf("%d", &quantity);
printf("Enter price: ");
scanf("%f", &price);
addItem(&inventory, name, quantity, price);
break;
case 2:
printf("Enter item name to update: ");
scanf("%s", name);
printf("Enter quantity to add: ");
scanf("%d", &quantity);
updateItem(inventory, name, quantity);
break;
case 3:
displayInventory(inventory);
break;
case 4:
printf("Enter item name to remove: ");
scanf("%s", name);
removeItem(&inventory, name);
break;
case 5:
printf("Exiting the program.\n");
break;
default:
printf("Invalid choice! Please try again.\n");
}
} while (choice != 5);
// Free the allocated memory
struct InventoryItem* temp;
********** 18 **********
--- page 19 ---
while (inventory != NULL) {
temp = inventory;
inventory = inventory->next;
free(temp);
}
return 0;
}
Compare and contrast selection and insertion sort. Write the algorithm for selection
sort.
#include <stdio.h>
void selectionSort(int arr[], int n) {
int i, j, min_index, temp;
for (i = 0; i < n - 1; i++) {
min_index = i; // Assume the minimum is the first element in the unsorted part
// Find the minimum element in the unsorted array
for (j = i + 1; j < n; j++) {
if (arr[j] < arr[min_index]) {
min_index = j; // Update the index of the minimum element
}
}
// Swap the found minimum element with the first element of the unsorted part
temp = arr[min_index];
arr[min_index] = arr[i];
arr[i] = temp;
}
}
int main() {
int arr[] = {64, 25, 12, 22, 11};
int n = sizeof(arr) / sizeof(arr[0]);
printf("Original array: \n");
for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
selectionSort(arr, n);
printf("Sorted array: \n");
********** 19 **********
--- page 20 ---
for (int i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
return 0;
}
Compare and contrast a queue with a stack. Implement stack ADT operation using link
list.
a.
#include <stdio.h>
#include <stdlib.h>
// Define the structure for a stack node
struct StackNode {
int data;
struct StackNode* next;
};
// Define the structure for the stack
struct Stack {
struct StackNode* top;
};
// Function to create a new stack node
struct StackNode* newNode(int data) {
b.   struct StackNode* stackNode = (struct StackNode*)malloc(sizeof(struct
StackNode));
stackNode->data = data;
stackNode->next = NULL;
Q7
return stackNode;
CO-2; SO-   }
1   [10]
BL-2   // Function to create an empty stack
struct Stack* createStack() {   [10]
CO-3; SO-
struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
1;
stack->top = NULL;
BL-2
return stack;
}
// Function to check if the stack is empty
int isEmpty(struct Stack* stack) {
return stack->top == NULL;
}
// Function to add an item to the stack
void push(struct Stack* stack, int data) {
struct StackNode* stackNode = newNode(data);
stackNode->next = stack->top;
stack->top = stackNode;
printf("%d pushed to stack\n", data);
}
// Function to remove an item from the stack
int pop(struct Stack* stack) {
if (isEmpty(stack)) {
printf("Stack underflow\n");
return -1; // Return an invalid value for underflow
}
struct StackNode* temp = stack->top;
stack->top = stack->top->next;
********** 20 **********
--- page 21 ---
int popped = temp->data;
free(temp);
return popped;
}
// Function to display the stack
void display(struct Stack* stack) {
struct StackNode* current = stack->top;
printf("Stack elements: ");
while (current != NULL) {
printf("%d ", current->data);
current = current->next;
}
printf("\n");
}
// Main function to demonstrate stack operations
int main() {
struct Stack* stack = createStack();
push(stack, 10);
push(stack, 20);
push(stack, 30);
display(stack);
printf("%d popped from stack\n", pop(stack));
display(stack);
return 0;
}
Write a program in C to print a string in reverse using a pointer.
#include <stdio.h>
// Function to print a string in reverse using pointers
void printReverse(char *str) {
// Move the pointer to the end of the string
char *end = str;
while (*end != '\0') {
end++;
}
end--; // Move back to the last character (excluding the null terminator)
// Print the string in reverse
while (end >= str) {
printf("%c", *end);
end--;
}
printf("\n"); // Print a newline at the end
}
int main() {
char str[100];
// Get user input
printf("Enter a string: ");
fgets(str, sizeof(str), stdin); // Using fgets to include spaces and avoid overflow
// Remove the newline character from the input if present
char *newline = str;
while (*newline != '\0') {
if (*newline == '\n') {
********** 21 **********
--- page 22 ---
*newline = '\0';
break;
}
newline++;
}
// Print the string in reverse
printf("Reversed string: ");
printReverse(str);
return 0;
}
********** 22 **********
--- page 23 ---
FIR ICR 2 I OH
````

## 2024-25 · Re-Exam · Sem 4 · Answer key · paper 4b3d191cb5d4

- Departments: Information Technology
- Programmes: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX YEARS INTEGRATED PROGRAM - 7037
- Source: `00_Original_Downloads/2024/67804__Semester IV__context_fixed.zip :: Re-Exam/BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX YEARS INTEGRATED PROGRAM - 7037/Basic Data Structures/ANS_Re-Exam_Basic Data Structures(701CO0C013)_Semester IV_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2025
- Text: text (2 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: II/Sem 4 Re-exam(Exam Year: 2024-2025)
Subject: Basic Data Structures
Date: 04 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Detailed Answer with Marks Distribution
Answer briefly:   [20]
a.   Classification: (2M) - Linear: Arrays, Linked
Lists, Stacks, Queues. - Non-Linear: Trees,
Explain the   classification of data
Graphs, Hash Tables. Primitive vs. Non-
CO-1;   structures and differentiate between
Primitive: (3M) - Primitive: Directly   [5 M]
BL-1,2   primitive   and   non-primitive   data
managed by the system (int, float, char). -
structures.
Non-Primitive: Derived from primitive types
(array, structures).
b. An online   ticket booking system   Choice: Structure (2M) because it allows
requires storing booked and available   multiple attributes per seat (seat number,
CO-   seats efficiently. Would you recommend   booking status). Explanation: (3M) - An
2,BL-   using an array or a structure to store seat   array can only store one type of data, making   [5 M]
3,4   information? Explain your choice.   it inefficient. - A structure allows grouping of
multiple seat properties, improving
management.
c. A printer in a shared office environment   Queue’s Role: (2M) - Uses FIFO (First-In-
CO-3;   receives multiple print requests. How   First-Out) principle. - Ensures fair execution
[5 M]
BL-3,4   does a queue help in managing these   of jobs. Efficiency: (3M) - Prevents priority
print requests fairly and efficiently?   inversion. - Avoids starvation of requests.
d. Explain why merge sort is preferred   Merge Sort Preference: (2M) - Stable sort
over quick sort in certain applications   (maintains order of equal elements). - Works
CO-4;   well on linked lists. Quick Sort Drawbacks:
[5 M]
BL-4   (3M) - Worst-case time complexity O(n²) if
poorly partitioned. - Inefficient for large
datasets when recursion depth is high.
Q2   [20]
a. What are the differences between static   Static vs. Dynamic: (5M) - Static: Fixed
and dynamic memory   allocation? memory allocation (array). - Dynamic: Uses
CO-1;
Explain the significance of pointers in   malloc() and free() to   [10 M]
BL-1,2
implementing dynamic data structure?   allocate/deallocate memory. Significance of
Pointers: (5M) - Enable dynamic memory
********** 1 **********
--- page 2 ---
management in linked lists. - Improve
memory efficiency.
b. Explain the different types of arrays and   Types: (4M) - 1D Arrays: Simple storage of
compare   their   advantages   and elements. - 2D Arrays: Matrix representation.
CO-2;   limitations.   - Jagged Arrays: Efficient memory usage.
[10 M]
BL-1,4   Advantages & Limitations: (6M) - Fast
access, but fixed size. - Inefficient
insertions/deletions.
Q3   [20]
a. Compare and contrast stacks and queues   Comparison: (5M) - Stack (LIFO) used in
in data structures with their advantages   recursion, undo features. - Queue (FIFO)
CO-3;   and applications.   used in scheduling, buffering. Applications:
[10 M]
BL-1,4   (5M) - Stack: Function calls, expression
evaluation. - Queue: Job scheduling,
networking.
b. Write a C++ program to implement   Algorithm Explanation: (4M) - Iterating
CO-2;   matrix multiplication using a 2D array .   through rows/columns. Code
[10 M]
BL-2,3   Implementation: (6M) - Nested loop logic in
C++.
Q4   [20]
a.   Code Explanation: (4M) - Structure
CO-2;   WAP to Implement a C++ program to   declaration. - Array implementation.
[10 M]
BL-3   demonstrate an array of structures.   Implementation: (6M) - User input and
output.
b. Convert the following infix expressions   Conversion Process: (6M) - Operator
to postfix and prefix notation and   precedence. - Stack-based approach.
CO-3;
explain the process:   Explanation with Steps: (4M) - Step-by-step   [10 M]
BL-6
(A + B) * C - D / E   conversion.
X / (Y + Z) * W
Q5   [20]
a. What are the applications of stacks in   Applications: (5M) - Undo operation,
CO-3;   real-world scenarios? Write a C++   backtracking, function calls. Code
[10 M]
BL-1,3   function to check if a stack is empty or   Explanation: (5M) - Stack condition
full.   checking.
b.   Queue Types: (5M) - Simple (FIFO). -
CO-3;   Differentiate between a simple queue,   Circular (Reuses memory). - Priority (Based
[10 M]
BL-4   circular queue, priority queue.   on priority). Comparison: (5M) - Efficiency
differences.
Q6   [20]
a. Discuss the role of queues in process Role of Queues: (5M) - CPU scheduling, task
CO-3;   scheduling. Provide an example of a   handling. Example: (5M) - Round Robin
[10 M]
BL-5   queue-based scheduling algorithm.   scheduling.
b. Differentiate between singly linked lists   Difference: (5M) - Singly: One pointer per
CO-3;
and doubly linked lists with an example.   node. - Doubly: Two pointers per node.   [10 M]
BL-3
Example Code: (5M)
Q7   [20]
a. Explain the difference between linear   Linear Search: (5M) - O(n), sequential
CO-4;
search and binary search with an   checking. Binary Search: (5M) - O(log n),   [10 M]
BL-2,4
example.   requires sorted data.
b. Explain the advantages of using a linked Memory Allocation: (5M) - Linked lists are
CO-3;
list over an array in terms of memory   dynamic. Insertion: (5M) - Easier in linked   [10 M]
BL-2,4
allocation and insertion operations.   lists.
********** 2 **********
````

## 2024-25 · Re-Exam · Sem 5 · Answer key · paper 5851bf50d311

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_05/Re-Exam/Integrated_Computer_7032/Basic Data Structures/ANS_Basic Data Structures(701CO0C013)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 17 Feb 2025
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 5 Re-exam(Exam Year: 2024-2025)
Subject: Basic Data Structures
Date: 17 Feb 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Instruction Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary.
9. Figures in brackets on the right hand side indicate full marks
Q1
Answer briefly:   [20]
a.   Define an abstract data type (ADT) with its different types and explain its importance
in data structure design.
Built-in data types like int, float, and double support basic operations (addition,
subtraction, etc.). For user-defined data types, we define specific operations as needed.
To simplify problem-solving, we create data structures with their own operations. These
non built-in data structures are called Abstract Data Types (ADTs).
An Abstract Data Type (ADT) defines a type by its values and operations without
[5]
specifying how they are implemented. It focuses on what operations are performed, not
how they are executed, providing an implementation-independent view.
A user does not need to know how a data type is implemented to use it. For example, we
use primitive types like int, float, and char without knowing their internal workings.
Similarly, ADTs are like black boxes that hide their inner structure and design. Users
only need to know what a data type can do, not how it is implemented. Examples of
ADTs include List ADT, Stack ADT, and Queue ADT.
b.   Which linear data structure would be suitable for below given scenarios:
A.   You are implementing a browser feature that allows users to navigate back to
previously visited web pages in reverse order. When the user clicks “Back,” the most
recently visited page is shown.
B.   You are tasked with creating a calculator that evaluates mathematical
expressions. The calculator needs to process operators and operands, respecting the
order of operations (parentheses, exponents, multiplication, division, addition,   [5]
subtraction).
C.   You are building a feature for a browser where a user can switch between
open tabs, moving left or right in a circular manner. After the last tab, the user goes
back to the first one.
D.   You are developing a music player that allows users to manage a playlist. The
users can add, remove, or rearrange songs frequently, without needing a fixed order or
continuous memory allocation.
********** 1 **********
--- page 2 ---
E.   You are designing a text editor that allows users to undo and redo changes.
Each edit is recorded, and users can undo recent changes or redo them later.
:   A. Stack
B. Stack
C. Circular Queue
D. Singly Linked list
E. Doubly Linked list
c.   Describe the process of recursion and give an example of a recursive function.
is a process in which a function calls itself directly or indirectly in order to solve a
problem. Recursive functions break down a problem into smaller, simpler sub-problems
of the same type, and this process continues until the problem becomes simple enough
to be solved directly, usually when a base case is met.
#include <stdio.h>
// Recursive function to calculate factorial
int factorial(int n) {
[5]
// Base case
if (n == 0) {
return 1;
}
// Recursive case
else {
return n * factorial(n - 1);
}
}
d.   Compare and contrast and contrast linked list and an array.   [5]
********** 2 **********
--- page 3 ---
a.   Write a program for Insertion sort.Sort the elements 77, 49, 25, 12, 9, 33, 56, 81 using
insertion sort.
#include <stdio.h>
b.
// Function to perform insertion sort
void insertionSort(int arr[], int n) {
int i, key, j;
for (i = 1; i < n; i++) {
key = arr[i];
j = i - 1;
Q2   [10]
// Move elements of arr[0..i-1] that are greater than key
[10]
// to one position ahead of their current position
while (j >= 0 && arr[j] > key) {
arr[j + 1] = arr[j];
j = j - 1;
}
arr[j + 1] = key;
}
}
// Function to print the array
void printArray(int arr[], int size) {
********** 3 **********
--- page 4 ---
for (int i = 0; i < size; i++)
printf("%d ", arr[i]);
printf("\n");
}
int main() {
int arr[] = {77, 49, 25, 12, 9, 33, 56, 81};
int n = sizeof(arr) / sizeof(arr[0]);
printf("Original array: ");
printArray(arr, n);
insertionSort(arr, n);
printf("Sorted array: ");
printArray(arr, n);
return 0;
}
Create a structure called Movie with attributes for Title, Director, Release
Year, and IMDB Rating. Implement an array of this structure to hold the
details of various movies. Develop a program that outputs the details of
movies that have a rating less than 5.
#include <stdio.h>
#include <string.h>
// Structure to store movie details
struct Movie {
char title[50];
char director[50];
int releaseYear;
float imdbRating;
};
// Function to print movies with IMDB rating less than 5
void printLowRatingMovies(struct Movie movies[], int size) {
printf("\nMovies with IMDB rating less than 5:\n");
int found = 0;
for (int i = 0; i < size; i++) {
if (movies[i].imdbRating < 5.0) {
printf("Title: %s\n", movies[i].title);
printf("Director: %s\n", movies[i].director);
********** 4 **********
--- page 5 ---
printf("Release Year: %d\n", movies[i].releaseYear);
printf("IMDB Rating: %.1f\n\n", movies[i].imdbRating);
found = 1;
}
}
if (!found) {
printf("No movies found with an IMDB rating less than 5.\n");
}
}
int main() {
int n;
// Asking for the number of movies
printf("Enter the number of movies: ");
scanf("%d", &n);
// Array of movie structures
struct Movie movies[n];
// Input movie details from the user
for (int i = 0; i < n; i++) {
printf("\nEnter details for Movie %d\n", i + 1);
printf("Enter Title: ");
getchar(); // To consume newline character left by previous scanf
fgets(movies[i].title, sizeof(movies[i].title), stdin);
movies[i].title[strcspn(movies[i].title, "\n")] = 0; // Remove trailing newline
printf("Enter Director: ");
fgets(movies[i].director, sizeof(movies[i].director), stdin);
movies[i].director[strcspn(movies[i].director, "\n")] = 0; // Remove trailing
newline
printf("Enter Release Year: ");
scanf("%d", &movies[i].releaseYear);
printf("Enter IMDB Rating: ");
scanf("%f", &movies[i].imdbRating);
}
// Call the function to print movies with IMDB rating < 5
printLowRatingMovies(movies, n);
********** 5 **********
--- page 6 ---
return 0;
}
a.   Write an algorithm that evaluates the postfix expression using a stack. Evaluate
following post fix expression using stack: 5 6 2 + * 9 3 - + 4 /. Show how the stack
b.   changes with each operation and explain how the result is obtained.
This algorithm finds the VALUE of an arithmetic expression P written in postfix
notation:
1. Add a right parenthesis “)” at the end of P. [This acts as a guard]
2.   Scan P from left to right and repeat steps 3 and 4 for each element of P until
the “)” is encountered.
a.   If an operand is encountered, put it on STACK.
b.   If an operator @ is encountered, then:
•   Remove the two top elements of STACK, where A is the top
element and B is the next top element.
•   Evaluate B @ A.
•   Place the result of (b) back on STACK
[End of If structure]
[End of Step 2 loop]
1. Set VALUE equal to the top element on STACK.
Exit.
Step   Action Stack   Explanation   [10]
Q3   1   Push 5 [5]   Operand 5 pushed to stack
2   Push 6 [5, 6]   Operand 6 pushed to stack   [10]
3   Push 2 [5, 6, 2] Operand 2 pushed to stack
4   + (add) [5, 8] Pop 6 and 2, compute 6 + 2 = 8, push 8
5   * (multiply)   [40]   Pop 5 and 8, compute 5 * 8 = 40, push 40
6   Push 9 [40, 9] Operand 9 pushed to stack
7   Push 3 [40, 9, 3]   Operand 3 pushed to stack
8   - (subtract)   [40, 6] Pop 9 and 3, compute 9 - 3 = 6, push 6
9   + (add) [46]   Pop 40 and 6, compute 40 + 6 = 46, push 46
10   Push 4 [46, 4] Operand 4 pushed to stack
11   / (divide)   [11.5] Pop 46 and 4, compute 46 / 4 = 11.5, push 11.5
Write a program in C/C++ to insert in after a specified element in a doubly link
list
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->prev = NULL;
newNode->next = NULL;
return newNode;
********** 6 **********
--- page 7 ---
}
// Function to insert a new node after a specified element
void insertAfter(struct Node** head, int key, int newData) {
struct Node* current = *head;
// Traverse the list to find the node with the given key
while (current != NULL && current->data != key) {
current = current->next;
}
// If the key is found, insert the new node
if (current != NULL) {
struct Node* newNode = createNode(newData);
newNode->next = current->next;
newNode->prev = current;
if (current->next != NULL) {
current->next->prev = newNode;
}
current->next = newNode;
printf("Inserted %d after %d.\n", newData, key);
} else {
printf("Element %d not found in the list.\n", key);
}
}
Write a C/C++ Program to swap two characters in function using pointer.
a.
#include <iostream>
#include <string.h>
b.
using namespace std;   [10]
Q4
void reverseString(char *str)
{   [10]
int l, i;
char *begin_ptr, *end_ptr, ch;
l = strlen(str);
********** 7 **********
--- page 8 ---
begin_ptr = str;
end_ptr = str + l - 1;
for (i = 0; i < l / 2; i++)
{
ch = *end_ptr;
*end_ptr = *begin_ptr;
*begin_ptr = ch;
begin_ptr++;
end_ptr--;
}
}
int main()
{
char str[100] = "NMIMSMumbai";
reverseString(str);
cout << "Reverse of the string:" << str;
return 0;
}
You are tasked with building a music playlist manager where each song
contains a title, artist, and duration (in minutes). Implement the playlist using
a singly linked list. Write a program that enables users to add new songs,
display the entire playlist, and calculate the total duration of all the songs in
the playlist.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Structure to define a node in the singly linked list (song)
struct Song {
char title[50];
char artist[50];
float duration;
struct Song* next;
};
********** 8 **********
--- page 9 ---
// Function to create a new song node
struct Song* createSong(char title[], char artist[], float duration) {
struct Song* newSong = (struct Song*)malloc(sizeof(struct Song));
strcpy(newSong->title, title);
strcpy(newSong->artist, artist);
newSong->duration = duration;
newSong->next = NULL;
return newSong;
}
// Function to add a song to the end of the playlist
void addSong(struct Song** head, char title[], char artist[], float duration) {
struct Song* newSong = createSong(title, artist, duration);
if (*head == NULL) {
*head = newSong;
} else {
struct Song* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newSong;
}
}
// Function to display the playlist
void displayPlaylist(struct Song* head) {
if (head == NULL) {
printf("The playlist is empty.\n");
return;
}
struct Song* temp = head;
printf("Playlist:\n");
while (temp != NULL) {
printf("Title: %s, Artist: %s, Duration: %.2f mins\n", temp->title, temp->artist,
temp->duration);
temp = temp->next;
}
}
// Function to calculate the total duration of the playlist
float calculateTotalDuration(struct Song* head) {
float totalDuration = 0;
********** 9 **********
--- page 10 ---
struct Song* temp = head;
while (temp != NULL) {
totalDuration += temp->duration;
temp = temp->next;
}
return totalDuration;
}
int main() {
struct Song* playlist = NULL;
int choice;
char title[50], artist[50];
float duration;
while (1) {
printf("\n1. Add a song\n");
printf("2. Display playlist\n");
printf("3. Calculate total duration\n");
printf("4. Exit\n");
printf("Enter your choice: ");
scanf("%d", &choice);
switch (choice) {
case 1:
printf("Enter song title: ");
scanf(" %[^\n]", title); // Read string with spaces
printf("Enter artist name: ");
scanf(" %[^\n]", artist); // Read string with spaces
printf("Enter song duration (in minutes): ");
scanf("%f", &duration);
addSong(&playlist, title, artist, duration);
printf("Song added to the playlist!\n");
break;
case 2:
displayPlaylist(playlist);
break;
case 3:
printf("Total duration of the playlist: %.2f minutes\n",
calculateTotalDuration(playlist));
break;
********** 10 **********
--- page 11 ---
case 4:
printf("Exiting the program...\n");
exit(0);
default:
printf("Invalid choice! Please try again.\n");
}
}
return 0;
}
a.   Conceptually compare a circular queue with a priority queue. In what situations would
you prefer using one over the other? In an amusement park, visitors wait in line for
rides. The system should ensure that visitors are allowed onto the ride in the order they
entered the line. Explain how you would design this system using a queue data
b.   structure, and discuss its benefits in this scenario.
#include <iostream>
#include <string>
using namespace std;
#define MAX 5 // Define the maximum size of the queue
// Define a structure for a visitor
struct Visitor {   [10]
Q5   string name; // Name of the visitor
};
// Define a structure for a linear queue   [10]
struct LinearQueue {
Visitor queue[MAX]; // Array to hold visitors
int front;   // Index of the front of the queue
int rear;   // Index of the rear of the queue
// Constructor to initialize the queue
LinearQueue() {
front = -1; // Initialize front to -1 (empty queue)
rear = -1; // Initialize rear to -1 (empty queue)
}
// Check if the queue is empty
bool isEmpty() {
return front == -1; // Queue is empty if front is -1
}
********** 11 **********
--- page 12 ---
// Check if the queue is full
bool isFull() {
return rear == MAX - 1; // Queue is full if rear is at the last
position
}
// Add a visitor to the queue
void enqueue(const string& visitorName) {
if (isFull()) {
cout << "The queue is full. Cannot add more visitors." <<
endl;
return;
}
// If the queue is empty, initialize front and rear
if (isEmpty()) {
front = 0; // Set front to 0 for the first visitor
}
rear++; // Move rear to the next position
queue[rear].name = visitorName; // Add the visitor to the
queue
cout << visitorName << " has entered the queue." << endl;
}
// Remove a visitor from the queue
void dequeue() {
if (isEmpty()) {
cout << "No visitors in the queue." << endl;
return;
}
cout << queue[front].name << " has exited the queue." <<
endl;
// If there is only one visitor, reset the queue
if (front == rear) {
front = -1;
rear = -1; // Reset the queue
} else {
front++; // Move front to the next position
}
}
// View the visitor at the front of the queue
void viewFrontVisitor() {
if (isEmpty()) {
cout << "No visitors in the queue." << endl;
return;
}
cout << "Visitor at the front: " << queue[front].name <<
endl;
}
********** 12 **********
--- page 13 ---
// Display all visitors in the queue
void displayQueue() {
if (isEmpty()) {
cout << "No visitors in the queue." << endl;
return;
}
cout << "Visitors in the queue: ";
for (int i = front; i <= rear; i++) {
cout << queue[i].name << " ";
}
cout << endl;
}
};
int main() {
LinearQueue queue; // Create a LinearQueue object
char choice;
string visitorName;
do {
int action;
cout << "Choose an action:\n"
<< "1. Add a visitor to the queue\n"
<< "2. Remove a visitor from the queue\n"
<< "3. View the visitor at the front of the queue\n"
<< "4. Display all visitors in the queue\n"
<< "Enter your choice: ";
cin >> action;
switch (action) {
case 1: // Add a visitor to the queue
cout << "Enter visitor name: ";
cin.ignore(); // To clear the input buffer
getline(cin, visitorName);
queue.enqueue(visitorName);
break;
case 2: // Remove a visitor from the queue
queue.dequeue();
break;
case 3: // View the visitor at the front of the queue
queue.viewFrontVisitor();
break;
case 4: // Display all visitors in the queue
queue.displayQueue();
break;
default:
cout << "Invalid choice! Please try again." << endl;
}
cout << "Do you want to continue? (Y/N): ";
********** 13 **********
--- page 14 ---
cin >> choice;
} while (choice == 'Y' || choice == 'y');
return 0;
}
Write a program to print the number of non-zero elements in the link list and also
multiply every non zero element of the linked list with 10 and print .
#include <stdio.h>
#include <stdlib.h>
// Structure to define a node in the linked list
struct Node {
int data;
struct Node* next;
};
// Function to create a new node
struct Node* createNode(int data) {
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
newNode->data = data;
newNode->next = NULL;
return newNode;
}
// Function to add a node at the end of the linked list
void addNode(struct Node** head, int data) {
struct Node* newNode = createNode(data);
if (*head == NULL) {
*head = newNode;
} else {
struct Node* temp = *head;
while (temp->next != NULL) {
temp = temp->next;
}
temp->next = newNode;
}
}
// Function to count the non-zero elements in the linked list
int countNonZero(struct Node* head) {
int count = 0;
struct Node* temp = head;
********** 14 **********
--- page 15 ---
while (temp != NULL) {
if (temp->data != 0) {
count++;
}
temp = temp->next;
}
return count;
}
// Function to multiply each non-zero element by 10
void multiplyNonZeroByTen(struct Node* head) {
struct Node* temp = head;
while (temp != NULL) {
if (temp->data != 0) {
temp->data *= 10;
}
temp = temp->next;
}
}
// Function to print the linked list
void printList(struct Node* head) {
if (head == NULL) {
printf("The list is empty.\n");
return;
}
struct Node* temp = head;
while (temp != NULL) {
printf("%d -> ", temp->data);
temp = temp->next;
}
printf("NULL\n");
}
int main() {
struct Node* head = NULL;
int n, data;
// Input number of elements in the linked list
printf("Enter the number of elements in the linked list: ");
scanf("%d", &n);
********** 15 **********
--- page 16 ---
// Input the elements and add them to the linked list
for (int i = 0; i < n; i++) {
printf("Enter element %d: ", i + 1);
scanf("%d", &data);
addNode(&head, data);
}
// Print the original list
printf("\nOriginal list:\n");
printList(head);
// Count the non-zero elements
int nonZeroCount = countNonZero(head);
printf("\nNumber of non-zero elements: %d\n", nonZeroCount);
// Multiply non-zero elements by 10 and print the updated list
multiplyNonZeroByTen(head);
printf("\nList after multiplying non-zero elements by 10:\n");
printList(head);
return 0;
}
Write the recursive algorithm for Binary Search. Compare and contrast
iterative and recursive method.
int binarySearch(int[] A, int low, int high, int x)
a.
{
b.   if (low > high) {
return -1;
}
int mid = (low + high) / 2;
if (x == A[mid]) {
return mid;   [10]
Q6   }
else if (x < A[mid]) {
return binarySearch(A, low, mid - 1, x);   [10]
}
else {
return binarySearch(A, mid + 1, high, x);
}
}
Convert the given expression into post fix using Stack:
A^ B ^ C – D + E + F / G-H*I
Ans: A B C ^ D - E + F G / + H I * -
Q7   In a task management application, users can create, complete, or delete tasks. The
a.   app allows users to prioritize tasks and view the most recent task at the top. Each   [10]
action (create, complete, delete) is stored in a stack for viewing and retrieval. Write a
********** 16 **********
--- page 17 ---
b.   program that uses a stack to manage task actions. The program should allow the user   [10]
to:
Create a new task (push onto the stack)
Complete a task (pop from the stack and mark it as completed)
View the most recent task (peek at the top of the stack)
Ans: #include <iostream>
#include <string>
using namespace std;
#define MAX 100 // Define the maximum size of the stack
// Define the structure for a task
struct Task {
string description; // Description of the task
};
// Define the stack structure for tasks
struct TaskStack {
Task stack[MAX]; // Array to hold tasks
int top;   // Index for the top of the stack
// Constructor to initialize the stack
TaskStack() {
top = -1; // Initialize top to -1 (empty stack)
}
// Check if the stack is empty
bool isEmpty() {
return top == -1;
}
// Check if the stack is full
bool isFull() {
return top == MAX - 1;
}
********** 17 **********
--- page 18 ---
// Push a new task onto the stack
void createTask(const string& description) {
if (isFull()) {
cout << "Task stack is full. Cannot create a new task." <<
endl;
return;
}
top++;
stack[top].description = description;
cout << "Task created: " << description << endl;
}
// Pop the most recent task from the stack and mark it as
completed
void completeTask() {
if (isEmpty()) {
cout << "No tasks to complete." << endl;
return;
}
cout << "Task completed: " << stack[top].description <<
endl;
top--; // Remove the completed task from the stack
}
// Peek at the most recent task
void viewMostRecentTask() {
if (isEmpty()) {
cout << "No tasks available." << endl;
return;
}
********** 18 **********
--- page 19 ---
cout << "Most recent task: " << stack[top].description <<
endl;
}
};
int main() {
TaskStack taskStack; // Create a TaskStack object
char choice;
string taskDescription;
do {
int action;
cout << "Choose an action:\n"
<< "1. Create a new task\n"
<< "2. Complete a task\n"
<< "3. View the most recent task\n"
<< "Enter your choice: ";
cin >> action;
switch (action) {
case 1: // Create a new task
cout << "Enter task description: ";
cin.ignore(); // To clear the input buffer
getline(cin, taskDescription);
taskStack.createTask(taskDescription);
break;
case 2: // Complete a task
taskStack.completeTask();
break;
********** 19 **********
--- page 20 ---
case 3: // View the most recent task
taskStack.viewMostRecentTask();
break;
default:
cout << "Invalid choice! Please try again." << endl;
}
cout << "Do you want to continue? (Y/N): ";
cin >> choice;
} while (choice == 'Y' || choice == 'y');
return 0;
}
Write a C/C++ program to print character array in reverse order in function using
pointer.
#include <iostream>
using namespace std;
// Function to print character array in reverse order
void printReverse(char* arr, int length) {
// Use a pointer to traverse the array in reverse
for (int i = length - 1; i >= 0; i--) {
cout << *(arr + i); // Dereference the pointer to get the character
}
cout << endl; // Print a newline at the end
}
int main() {
char str[100]; // Declare a character array
// Input character array
cout << "Enter a string: ";
cin.getline(str, sizeof(str)); // Use getline to read a string with spaces
********** 20 **********
--- page 21 ---
// Calculate the length of the string
int length = 0;
while (str[length] != '\0') {
length++;
}
// Call the function to print the string in reverse order
cout << "Reversed string: ";
printReverse(str, length);
return 0;
}
********** 21 **********
````
