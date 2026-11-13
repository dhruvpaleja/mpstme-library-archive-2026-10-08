# Programming for Problem Solving: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper d2ed9502f63c

- Departments: Computer Engineering, Cyber Security, Data Science, Mechanical
- Programmes: BTech CyberSecurity 7010, Integrated Computer 7032, Integrated DS 7038, Integrated Mechanical 7031
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_CyberSecurity_7010/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Dec 2025
- Text: mixed (18 pages), mean OCR confidence 39.1
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (Mech)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Programming for Problem Solving
Date: 10 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. _1_ is compulsory
3. Out of remaining questions, attempt any _4_ questions.
4. In all _5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1
Draw a flowchart to accept student’s name, roll no and marks of 3 subjects from user
SO-1   a.   [5]
and calculate total, average marks and print it for ‘n’ students.
BL-6
Ans.
********** 1 **********
--- page 2 ---
CO-2   Develop a solution for the following scenario.
SO-7   Despite everyone's advice, Harshad has decided to gamble away his money.
Today he chose a dice game to bet on. Harshad will roll 2 die one after the other, and
b.   Harshad wins if and only if the sum of the 2 dice rolls is exactly x.   [5]
BL-6   The die are standard fair 6-faced, with numbers 1 through 6 written on the sides.
Harshad 's first roll turned up to be the number A. What number does Harshad need on
his second roll to win the game? It can be proven that this number exists and is unique.
#include <iostream>
using namespace std;
int main() {
int A, X;
Ans.
cout << "Enter the first die roll (A): ";
cin >> A;
cout << "Enter the required total sum (X): ";
********** 2 **********

[Text in pictures on this page, read by OCR]
Start
/ Enter number of students n /

Seti=1

Enter Student Name, Roll / (Ena)
No

/ Enter Marks of 3 Subjects ]

Calculate Total = Sub1 +
Sub2 + Sub3

Calculate Average = Total /
3

Display Student Name, Roll
No, Total, Average

NN

Increment i=i+1
--- page 3 ---
cin >> X;
// Calculate the second die value
int second_die = X - A;
cout << "Harshad needs to roll a " << second_die << " on the second die to win."
<< endl;
return 0;
}
CO-3
SO-6   c.   List and explain any four inbuild C-style string functions from <cstring>.   [5]
BL-2
C-style String Functions (from <cstring>):
These functions operate on C-style strings (character arrays terminated by a null
character \0).
•   strlen(const char* str): Calculates the length of a C-style string.
•   strcpy(char* dest, const char* src): Copies a source string to a destination.
•   strncpy(char* dest, const char* src, size_t n): Copies a specified number of
characters.
Ans.   •   strcat(char* dest, const char* src): Concatenates two C-style strings.
•   strncat(char* dest, const char* src, size_t n): Concatenates a specified number
of characters.
•   strcmp(const char* str1, const char* str2): Compares two C-style strings.
•   strncmp(const char* str1, const char* str2, size_t n): Compares a specified
number of characters.
•   strstr(const char* haystack, const char* needle): Finds the first occurrence of a
substring.
CO-4
SO-2   d.   Explain the concept of function overloading using an example program in C++.   [5]
BL-2
Function overloading is a C++ feature that allows you to define multiple functions with
the same name in the same scope, but with different parameters. The compiler
distinguishes between these functions based on the number, type, or order of their
parameters. This is a form of compile-time polymorphism, enabling you to use a single,
intuitive function name for a variety of tasks.
#include <iostream>
// Overloaded function 1: Adds two integers
int add(int a, int b) {
std::cout << "Using integer version." << std::endl;
return a + b;
Ans. }
// Overloaded function 2: Adds two doubles
double add(double a, double b) {
std::cout << "Using double version." << std::endl;
return a + b;
}
// Overloaded function 3: Adds an integer and a double
double add(int a, double b) {
std::cout << "Using integer and double version." << std::endl;
return a + b;
********** 3 **********
--- page 4 ---
}
int main() {
// Calling the integer version
int sum1 = add(5, 10);
std::cout << "Sum of integers: " << sum1 << std::endl;
// Calling the double version
double sum2 = add(5.5, 10.2);
std::cout << "Sum of doubles: " << sum2 << std::endl;
// Calling the integer and double version
double sum3 = add(5, 10.2);
std::cout << "Sum of integer and double: " << sum3 << std::endl;
return 0;
}
Q2   [20]
CO-2
Explain recursive function and write a program to checks if a string is a palindrome
SO-7   a.   [10]
using recursive function. Avoid using loops or inbuilt functions.
BL-2
A recursive function is a function that calls itself to solve a smaller version of the
same problem. This technique is based on the mathematical principle of recursion.
The core components of any recursive solution are:
1. Base Case: The condition that stops the recursion. Without a base case, the
function would call itself infinitely, leading to a stack overflow error. The base
case represents the simplest instance of the problem that can be solved
directly.
2. Recursive Step: The part of the function where the problem is broken down
into a smaller, simpler version of itself, and the function calls itself with this
smaller input.
#include <iostream>
int recursive_strlen(const char* str) {
if (*str == '\0') {
return 0; // Base Case: End of string reached
}
// Recursive Step: Add 1 to the length of the rest of the string
Ans.   return 1 + recursive_strlen(str + 1);
}
bool is_palindrome_recursive(const char* str, int start, int end) {
// 1. Base Case: If the substring is empty or has 1 character, it's a palindrome.
if (start >= end) {
return true;
}
// 2. Check current characters: If first and last characters don't match, return false.
if (str[start] != str[end]) {
return false;
}
// 3. Recursive Step: Check the inner substring.
// Move start one step right and end one step left.
return is_palindrome_recursive(str, start + 1, end - 1);
}
********** 4 **********
--- page 5 ---
int main() {
// Note: Using C-style char array for basic string representation
char str1[] = "madam";
char str2[] = "level";
char str3[] = "hello";
// Test 1: madam
int len1 = recursive_strlen(str1);
bool result1 = is_palindrome_recursive(str1, 0, len1 - 1);
std::cout << str1 << " is a palindrome: " << (result1 ? "True" : "False") << std::endl;
// Test 2: level
int len2 = recursive_strlen(str2);
bool result2 = is_palindrome_recursive(str2, 0, len2 - 1);
std::cout << str2 << " is a palindrome: " << (result2 ? "True" : "False") << std::endl;
// Test 3: hello
int len3 = recursive_strlen(str3);
bool result3 = is_palindrome_recursive(str3, 0, len3 - 1);
std::cout << str3 << " is a palindrome: " << (result3 ? "True" : "False") << std::endl;
return 0;
}
CO-3   Design a C++ program that checks if a password entered by a user is Strong or Weak.
SO-6   A password is considered Strong if it:
• Has at least 8 characters
b.   [10]
•   Contains at least one uppercase letter, one lowercase letter, one digit, and one
BL-6   special character.
If any condition fails, display the reason (example: “Missing digit”).
#include <iostream>
#include <string>
#include <cctype> // For isupper, islower, isdigit
int main() {
std::string password;
bool has_uppercase = false;
bool has_lowercase = false;
bool has_digit = false;
bool has_special = false;
std::cout << "Enter a password to check its strength:" << std::endl;
std::getline(std::cin, password);
Ans.
// Check length
if (password.length() < 8) {
std::cout << "Weak password: Must be at least 8 characters long." << std::endl;
return 0;
}
// Iterate through password to check for character types
for (char c : password) {
if (std::isupper(c)) {
has_uppercase = true;
} else if (std::islower(c)) {
has_lowercase = true;
} else if (std::isdigit(c)) {
has_digit = true;
********** 5 **********
--- page 6 ---
} else {
// Check for special characters by excluding letters and digits
has_special = true;
}
}
// Check all criteria and provide specific feedback
if (has_uppercase && has_lowercase && has_digit && has_special) {
std::cout << "Strong password." << std::endl;
} else {
std::cout << "Weak password. Missing requirements:" << std::endl;
if (!has_uppercase) {
std::cout << "- At least one uppercase letter" << std::endl;
}
if (!has_lowercase) {
std::cout << "- At least one lowercase letter" << std::endl;
}
if (!has_digit) {
std::cout << "- At least one digit" << std::endl;
}
if (!has_special) {
std::cout << "- At least one special character" << std::endl;
}
}
return 0;
}
Q3   [20]
CO-4
List and explain the different types of inheritance. Also, write a program to demonstrate
SO-2   a.   [10]
Multiple inheritance.
BL-6
1. What is Inheritance?
Definition:
Inheritance is an Object-Oriented Programming (OOP) feature in C++ that allows a
derived class to reuse and extend the properties (data members) and behaviors
(member functions) of a base class.
It promotes code reusability, modularity, and hierarchical relationships between
classes.
2. Types of Inheritance in C++
Diagram
Ans.   Type   Description
Represen
1. Single Inheritance A single derived class inherits from one base class. A → B
2. Multiple   A single derived class inherits from two or more
A →B →
Inheritance   base classes.
3. Multilevel
A class is derived from another derived class.   A → B →
Inheritance
4. Hierarchical
Multiple classes inherit from the same base class.   A → B an
Inheritance
Combination of more than one type of inheritance
5. Hybrid Inheritance   Mixed for
(e.g., multiple + multilevel).
********** 6 **********
--- page 7 ---
3. Example: Multiple Inheritance
Concept:
In multiple inheritance, a single class inherits from two or more base classes.
This allows it to combine the features of multiple parent classes into one derived class.
C++ Program: Demonstrating Multiple Inheritance
#include <iostream>
using namespace std;
// Base class 1
class Engine {
public:
void engineType() {
cout << "Engine: Petrol Engine" << endl;
}
};
// Base class 2
class Body {
public:
void bodyType() {
cout << "Body: Sedan Type" << endl;
}
};
// Derived class inherits from both Engine and Body
class Car : public Engine, public Body {
public:
void displayCar() {
cout << "This is a Car combining Engine and Body features." << endl;
}
};
int main() {
Car myCar;
// Accessing members from both base classes
myCar.engineType();
myCar.bodyType();
myCar.displayCar();
return 0;
}
Output:
Engine: Petrol Engine
Body: Sedan Type
This is a Car combining Engine and Body features.
4. Explanation
• Engine and Body are two independent base classes.
• Car inherits publicly from both of them, combining their properties.
•   This demonstrates multiple inheritance, where the derived class (Car) can use
methods from both parent classes.
5. Advantages of Multiple Inheritance
• Combines features of multiple classes into one.
********** 7 **********
--- page 8 ---
• Promotes code reusability.
•   Useful in modeling objects that share traits from different sources (e.g., a Car
“has-a” Engine and Body).
6. Ambiguity in Multiple Inheritance
If both base classes have a function with the same name, ambiguity arises.
Example:
A::show();
B::show();
You must use the scope resolution operator (::) to specify which base class function
to call.
Summary Table
Feature   Single Inheritance   Multiple Inheritance
One class inherits from one base   One class inherits from two or more
Definition
class.   classes.
Complexity Simple   Higher (can lead to ambiguity)
Reusability Moderate   High
Example   Student → Person   Car → Engine, Body
CO-3   Write a program that counts the number of seats available, reserves a seat at a
SO-2   b.   specified row and column, and shows the updated seating (0 = available, 1 = booked).   [10]
BL-6   Show a message if it's already booked.
#include <iostream>
using namespace std;
int main() {
const int rows = 3;
const int cols = 4;
int seats[rows][cols] =
{
{0, 0, 1, 0},
{1, 0, 0, 0},
{0, 1, 0, 0}
};
int available = 0;
for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
if (seats[i][j] == 0)
Ans.
available++;
}
}
cout << "Number of available seats: " << available << endl;
cout << "\nCurrent seating (0 = available, 1 = booked):\n";
for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
cout << seats[i][j] << " ";
}
cout << endl;
}
int r, c;
cout << "\nEnter row (0-" << rows - 1 << "): ";
cin >> r;
cout << "Enter column (0-" << cols - 1 << "): ";
********** 8 **********
--- page 9 ---
cin >> c;
if (r < 0 || r >= rows || c < 0 || c >= cols) {
cout << "Invalid seat position!" << endl;
return 0;
}
if (seats[r][c] == 0) {
seats[r][c] = 1;
cout << "\nSeat reserved successfully!\n";
} else {
cout << "\nSeat already booked!\n";
}
cout << "\nUpdated seating arrangement:\n";
for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
cout << seats[i][j] << " ";
}
cout << endl;
}
return 0;
}
Q4   [20]
CO-3
Write a C++ program to read integer values from user and store them in an array of
SO-6   a.   [10]
size ‘n’. Also, find the average of elements of the arrays using pointer.
BL-6
#include <iostream>
double calculate_average_ptr(const int* arr_ptr, int n) {
if (n <= 0) {
return 0.0; // Avoid division by zero
}
long long sum = 0; // Use long long to prevent potential overflow for the sum
for (int i = 0; i < n; ++i) {
sum += *(arr_ptr + i);
}
Ans.
return static_cast<double>(sum) / n;
}
int main() {
int n;
// Get the size of the array
std::cout << "Enter the size of the array (n): ";
if (!(std::cin >> n) || n <= 0) {
std::cerr << "Invalid array size. Exiting." << std::endl;
return 1;
}
********** 9 **********
--- page 10 ---
int* numbers = new int[n];
if (numbers == nullptr) {
std::cerr << "Memory allocation failed. Exiting." << std::endl;
return 1;
}
std::cout << "Enter " << n << " integer elements:" << std::endl;
for (int i = 0; i < n; ++i) {
std::cout << "Element " << i + 1 << ": ";
if (!(std::cin >> numbers[i])) {
std::cerr << "Invalid input. Exiting." << std::endl;
delete[] numbers;
return 1;
}
}
double average = calculate_average_ptr(numbers, n);
std::cout << "\n--- Calculation Result ---" << std::endl;
std::cout << "Array size: " << n << std::endl;
std::cout << "Average of the elements: " << average << std::endl;
std::cout << "--------------------------" << std::endl;
// Free the dynamically allocated memory
delete[] numbers;
return 0;
}
CO-4
What is friend function? List the properties of friend function and write a program to
SO-2   b.   [10]
illustrate the use of friend function in C++ programming language.
BL-4
A friend function in C++ is a function that, while not a member of a class, is granted
access to its private and protected members. It's a way to break encapsulation when
necessary, allowing an external function to interact with a class's internal data. A class
declares a function as a friend using the friend keyword within its definition.
Properties of a Friend Function
• Not a Member Function: A friend function is not a member of the class it's
befriended to. It's declared outside the class's scope and is not called with the
dot operator (.) or arrow operator (->) on an object of that class.
•   Access Rights: It has special access rights to the private and protected
members of the class. This is its primary purpose.
•   Declaration Location: A friend declaration can be placed anywhere in the
Ans.   class definition (public, private, or protected section), as its access rights are
not affected by its location.
•   Overloading: A friend function can be overloaded. Each overloaded version
must be separately declared as a friend.
•   Inheritance: Friendship is not inherited. If a base class has a friend function,
that function is not automatically a friend of the derived classes.
#include <iostream>
class FriendFunctionExample {
private:
int private_number;
********** 10 **********
--- page 11 ---
public:
// Constructor to initialize the private member
FriendFunctionExample(int num) : private_number(num) {}
// Declare a global function as a friend
friend void displayPrivateData(const FriendFunctionExample& obj);
};
// Definition of the friend function
// It can access obj.private_number directly
void displayPrivateData(const FriendFunctionExample& obj) {
std::cout << "The private number is: " << obj.private_number << std::endl;
}
int main() {
// Create an object of the class
FriendFunctionExample myObject(123);
// Call the friend function, passing the object as an argument
displayPrivateData(myObject);
// Note: The following line would cause a compilation error
// because main() cannot access the private member.
// std::cout << myObject.private_number;
return 0;
}
Q5   [20]
CO-2   Compare for and do while loops. Write a program for the following scenario.
SO-7   A particular month has 31 days, numbered from 1 to 31.
Day 1 is a Monday, and the usual 7-day week is followed (so day 2 is Tuesday, day 3 is
a.   Wednesday, and so on). Every Saturday and Sunday is a holiday. There are 𝑁 festival   [10]
BL-4   days, which are also holidays. Note that it is possible for a festival day to occur on a
Saturday or Sunday. You are given the dates of the festivals. Determine and print the
total number of holidays in this month.
Ans.
#include <iostream>
// Define constants for the week days (0=Mon, 6=Sun)
********** 11 **********

[Text in pictures on this page, read by OCR]
Feature for Loop do-while Loop

Primary Used when the number of iterations is Used when the loop must execute at

Use known (definite loop), such as iterating over least once (indefinite loop), regardless
an array or a fixed range. of the condition.

Condition Entry-controlled. The condition is checked Exit-controlled. The condition is

Check before the loop body executes. If the checked after the loop body executes.
condition is false initially, the body never runs. The loop body is guaranteed to run at

least once.

Structure All control parts (initialization, condition, Control parts (initialization and update)
update) are placed together at the top, are often separate from the condition
making it clean and readable for counted check at the bottom.
loops.

Syntax for (initialization; condition; do { // body; update; } while

update) { // body } (condition);
--- page 12 ---
const int SATURDAY = 5;
const int SUNDAY = 6;
const int MAX_DAYS = 31; // Maximum days in a month for static array
int main() {
int days_in_month;
int num_festivals;
std::cout << "Enter the total number of days in the month (D): ";
if (!(std::cin >> days_in_month) || days_in_month <= 0 || days_in_month >
MAX_DAYS) {
std::cerr << "Invalid day count. Please enter a value between 1 and " <<
MAX_DAYS << "." << std::endl;
return 1;
}
std::cout << "Enter the number of festival days (K): ";
if (!(std::cin >> num_festivals) || num_festivals < 0) {
std::cerr << "Invalid festival count. Exiting." << std::endl;
return 1;
}
// Use a boolean array to track if a day is a holiday.
// We use a fixed size to avoid dynamic allocation, which is a common
// practice when vector is not allowed and the maximum size is known.
bool is_holiday[MAX_DAYS + 1] = {false};
int total_holidays = 0;
// Mark Festival Days
if (num_festivals > 0) {
std::cout << "Enter the " << num_festivals << " festival dates:" << std::endl;
for (int i = 0; i < num_festivals; ++i) {
int date;
std::cout << "Festival date " << i + 1 << ": ";
if (!(std::cin >> date) || date < 1 || date > days_in_month) {
std::cerr << "Invalid date. Exiting." << std::endl;
return 1;
}
if (!is_holiday[date]) {
is_holiday[date] = true;
total_holidays++;
}
}
}
// Mark Weekend Days
for (int date = 1; date <= days_in_month; ++date) {
// Day 1 is Monday (index 0), so we use (date - 1) % 7 to get the day of the week.
int day_index = (date - 1) % 7;
if (day_index == SATURDAY || day_index == SUNDAY) {
if (!is_holiday[date]) {
is_holiday[date] = true;
total_holidays++;
}
}
}
********** 12 **********
--- page 13 ---
std::cout << "\n----------------------------------------------------" << std::endl;
std::cout << "Total number of holidays in the month: " << total_holidays <<
std::endl;
std::cout << "----------------------------------------------------" << std::endl;
return 0;
}
CO-4   Define Constructor and Write a program for following scenario: A bank account has
SO-2   accountNumber, accountHolder, and balance.
b.   • Write a class BankAccount with default and parameterized constructors.   [10]
BL-6   •   Initialize accounts and display account details.
• Perform a deposit and withdrawal operation.
#include <iostream>
#include <string>
using namespace std;
class BankAccount {
private:
int accountNumber;
string accountHolder;
double balance;
public:
// Default Constructor
BankAccount() {
accountNumber = 0;
accountHolder = "Unknown";
balance = 0.0;
}
// Parameterized Constructor
BankAccount(int accNo, string holder, double bal) {
accountNumber = accNo;
accountHolder = holder;
Ans.   balance = bal;
}
// Function to display account details
void display() {
cout << "\nAccount Number: " << accountNumber;
cout << "\nAccount Holder: " << accountHolder;
cout << "\nBalance: Rs. " << balance << endl;
}
// Function to deposit money
void deposit(double amount) {
if (amount > 0) {
balance += amount;
cout << "Deposited Rs. " << amount << " successfully." << endl;
} else {
cout << "Invalid deposit amount!" << endl;
}
}
// Function to withdraw money
void withdraw(double amount) {
if (amount > 0 && amount <= balance) {
********** 13 **********
--- page 14 ---
balance -= amount;
cout << "Withdrawn Rs. " << amount << " successfully." << endl;
} else {
cout << "Invalid withdrawal amount or insufficient balance!" << endl;
}
}
};
int main() {
// Using default constructor
cout << "Creating Default Account:" << endl;
BankAccount acc1;
acc1.display();
// Using parameterized constructor
cout << "\nCreating Parameterized Account:" << endl;
BankAccount acc2(1001, "Rahul Sharma", 5000.0);
acc2.display();
// Performing deposit and withdrawal
cout << "\nPerforming transactions on Rahul's account..." << endl;
acc2.deposit(1500.0);
acc2.withdraw(2000.0);
// Display final details
cout << "\nFinal Account Details:";
acc2.display();
return 0;
}
Q6   [20]
CO-2   Write a program for following scenario.
SO-7   Finally a monsoon has come. According to the Meteorological Department, there will
be rain in the upcoming 𝑁 days in the city. Initially, the water level of the city is zero
millimetres. The amount of rain on the 𝑖-th day can be described by an integer 𝐴𝑖 as
follows:
•   If 𝐴𝑖> 0, the water level of the city increases by 𝐴𝑖 millimetres on the 𝑖-th
a.   [10]
day.
BL-6   •   If 𝐴𝑖= 0, there is no rain on the 𝑖-th day. The water level of the city decreases
by 𝐷 millimetres on such a day. However, if the water level is less
than 𝐷 millimetres before the 𝑖-th day, then it becomes zero instead.
There will be a red alert in the city if the water level becomes strictly greater
than 𝐻 millimetres on at least one of the 𝑁 days. Determine if there will be a red alert.
#include <iostream>
using namespace std;
int main() {
int N, D, H;
Ans.   cout << "\nEnter N (days), D (decrease), and H (alert level): ";
cin >> N >> D >> H;
int A[N];
cout << "Enter rainfall for " << N << " days: ";
for (int i = 0; i < N; i++) {
cin >> A[i];
********** 14 **********
--- page 15 ---
}
int waterLevel = 0;
bool alert = false;
for (int i = 0; i < N; i++) {
if (A[i] > 0) {
waterLevel += A[i]; // rain increases level
} else {
// no rain, decrease level safely
waterLevel = max(0, waterLevel - D);
}
// check for red alert condition
if (waterLevel > H) {
alert = true;
break;
}
}
if (alert)
cout << "YES - Red Alert!" << endl;
else
cout << "NO - Safe Water Level" << endl;
return 0;
}
CO-3   Write a function that verifies a username by removing spaces, making sure it is
SO-6   b.   between 5 and 15 characters long, beginning with a letter, and consisting only of   [10]
BL-6   letters, numbers, or underscores.
#include <iostream>
#include <cctype>
#include <string>
using namespace std;
bool verifyUsername(string username) {
string clean = "";
for (char c : username) {
if (c != ' ')
clean += c;
}
if (clean.length() < 5 || clean.length() > 15) {
Ans.   cout << "Invalid: Username must be between 5 and 15 characters long.\n";
return false;
}
if (!isalpha(clean[0])) {
cout << "Invalid: Username must begin with a letter.\n";
return false;
}
for (char c : clean) {
if (!isalnum(c) && c != '_') {
cout << "Invalid: Username can contain only letters, numbers, or
underscores.\n";
return false;
********** 15 **********
--- page 16 ---
}
}
cout << "Valid username: " << clean << endl;
return true;
}
int main() {
string username;
cout << "Enter a username: ";
getline(cin, username);
verifyUsername(username);
return 0;
}
Q7   [20]
CO-3   Define 2D array and write a program on following scenario: A class has 5 students and
SO-6   3 subjects.
a.   •   Store the marks in a 2D array (rows = students, columns = subjects).   [10]
BL-6   •   Calculate total and average marks of each student.
•   Display results in tabular form.
#include <iostream>
#include <iomanip> // for setw
using namespace std;
int main() {
const int students = 5;
const int subjects = 3;
int marks[students][subjects];
int total;
double average;
// Input marks
for(int i = 0; i < students; i++) {
cout << "Enter marks for student " << i+1 << ":\n";
for(int j = 0; j < subjects; j++) {
cout << "Subject " << j+1 << ": ";
cin >> marks[i][j];
}
Ans.
}
// Display table header
cout << "\nStudent\tSub1\tSub2\tSub3\tTotal\tAverage\n";
cout << "-----------------------------------------------\n";
// Calculate total and average
for(int i = 0; i < students; i++) {
total = 0;
cout << " " << i+1 << "\t";
for(int j = 0; j < subjects; j++) {
cout << marks[i][j] << "\t";
total += marks[i][j];
}
average = total / (double)subjects;
cout << total << "\t" << fixed << setprecision(2) << average << endl;
}
********** 16 **********
--- page 17 ---
return 0;
}
CO-3   Write a program for the following scenario.
SO-6   Sam wants to buy a new phone, but he is not willing to spend a lot of money. Instead,
he checks the price of his chosen model everyday and waits for the price to drop to an
acceptable value. So far, he has observed the price for 𝑁 days (numbere 1 through 𝑁);
for each valid 𝑖, the price on the 𝑖-th day was 𝑃𝑖 rupees.
On each day, Sam considers the price of the phone to be good if it is strictly smaller
than all the prices he has observed during the previous five days. If there is no record
of the price on some of the previous five days (because Sam has not started checking
the price on that day yet), then Sam simply ignores that previous day ― we could say
that he considers the price on that day to be infinite.
Now, Sam is wondering ― on how many days has he considered the price to be good?
b.   [10]
Find the number of these days.
BL-6   Example
Input:
7
375 750 723 662 647 656 619
Output:
2
Hint: Sam considers the price to be good on day 1, because he has not observed any
prices on the previous days. The prices on days 2,3,4,5,6 are not considered good
because they are greater than the price on day 1. Finally, the price on day 7 is
considered good because it is smaller than all of the prices on days 2,3,4,5,6.
#include <iostream>
using namespace std;
int main() {
int N;
cout << "Enter number of days: ";
cin >> N;
int P[1000]; // assuming max 1000 days
cout << "Enter prices for " << N << " days: ";
for (int i = 0; i < N; i++) {
cin >> P[i];
}
int goodDays = 0;
for (int i = 0; i < N; i++) {
Ans.
bool isGood = true;
// Compare with up to 5 previous days
for (int j = (i - 5 > 0 ? i - 5 : 0); j < i; j++) {
if (P[i] >= P[j]) {
isGood = false;
break;
}
}
if (isGood)
goodDays++;
}
cout << "\nNumber of good days: " << goodDays << endl;
return 0;
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 5cb3ee6e9963

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_AIDS_7056/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 2bb1456fd31c

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_AIML_7053/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 76a723d4cc37

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_AI_7012/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 4e0906feaaea

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_CSBS_7036/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper dba3e1d279b0

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_CSE_DS_7057/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 54ecee055bfa

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_CS_7055/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper adbb8cc08900

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_Civil_7005/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper c6546a04c519

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_Computer_7002/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 32391a84592e

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_CyberSecurity_7010/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 9018a6ca4cb7

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_DS_7009/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 10ad44120bfc

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_EXTC_7006/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper c34f195c1b7d

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_IT_7001/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 5a7f39746537

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_Mechanical_7003/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper e7d6501779bc

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/BTech_Mechatronics_7004/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 50bf4055eb1b

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MBATech_AI_7051/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 93cdebb9637e

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MBATech_Computer_7047/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 700c889d95fe

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MBATech_DS_7052/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 71805d40187e

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MBATech_IT_7041/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper 9d122edfbf20

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_03/Final-Exam/Integrated_IT_7037/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: II/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper 31ec36465c6a

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/Integrated_Computer_7032/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: III/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper 0bbd61736252

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/Integrated_DS_7038/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: III/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper c0d3c4463c1a

- Departments: Mechanical
- Programmes: Integrated Mechanical 7031
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/Integrated_Mechanical_7031/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Nov 2024
- Text: text (15 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B.
Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech
(MECH)/B. Tech (MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: III/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 30 Nov 2024   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
FINAL EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 15 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
b. -It is a group of logically related data stored in contiguous memory blocks under a common name.   5
-An Array is a homogeneous or similar data type under a common name.
Page 1 of 15

[Text in pictures on this page, read by OCR]
#include <iostream>
using namespace std;
int main()

It

char ch;
cout<<"Enter any Alpabet\n";
cin>>ch;

vowel letters
case ‘a':
cout<<ch<<" is a vowel";
break;
case 'e':
cout<<ch<<" is a vowel";
break;
case 'i':
cout<<ch<<" is a vowel";
break;
case ‘o':
cout<<ch<<" is a vowel";
break;
case ‘u':
cout<<ch<<" is a vowel";
break;
default:
cout<<ch<<" is a consonant";
break;

: }
return 0;
}
--- page 2 ---
- Reading & Displaying –
- There are multiple elements, and each element can be accessed using its index.
- Typically, element reading and displaying statements is written in a loop
- Program to read and display 1D array.
int main() {
int a[5],i;
cout<<"Enter Array elements:";
for(i=0; i<5; i++)
cin>>a[i];
cout<<"Array is"<<endl;
for(i=0;i<5;i++){
cout<<a[i]<<" ";
}
return 0;
}
c. #include<iostream>   5
using namespace std;
class area
{
public:
void final_area(float r)
{
cout<<"area is "<<3.14*r*r<<endl;
}
void final_area(float l, float b)
{
cout<<"area is "<<l*b<<endl;
}
};
int main()
{
area a;
a.final_area(20.45f);
a.final_area(30.45f,1.00f);
}
d.   5
Page 2 of 15
--- page 3 ---
.   Section B(Attempt Any 4 Questions)   80
1.   20
a. if (condition1) {   10
// Block of code to execute if condition1 is true
if (condition2) {
// Block of code to execute if condition2 is true
} else {
// Block of code to execute if condition2 is false
}
} else {
// Block of code to execute if condition1 is false
#include <iostream>
using namespace std;
int main() {
float temperature;
// Input the temperature
cout << "Enter the temperature in degrees Celsius: ";
cin >> temperature;
// Provide advice based on temperature
if (temperature < 0) {
cout << "It's freezing. Wear a heavy coat." << endl;
} else if (temperature >= 0 && temperature <= 20) {
if (temperature < 10) {
cout << "Wear a warm jacket." << endl;
} else {
cout << "A light jacket is fine." << endl;
}
} else { // temperature > 20
cout << "No jacket needed." << endl;
}
Page 3 of 15
--- page 4 ---
return 0;
}
b. Use of correct formula/Logic – 05 marks (&&,||,!)   5
#include <iostream>
using namespace std;
int main()
{
cout<<"Logical AND "<< ('a'>'A') && ('a'!='A');
cout<<"Logical OR "<< ('a'>'A') || ('a'!='A');
cout<<"Logical NOT "<< !(('a'>'A') || ('a'!='A'));
return 0;
}
c.
Outputs:   Marking Scheme   5
First   1,2,3,4,5,   Output: (1 Mark)
Output:
Second   0,5,10,15,20, Output: (1 Mark)
Output:
Explanation: (1 Mark)
Pointer Arithmetic: The expression p + i moves the pointer
th
p to point to the i   element of the array. Since p is pointing
to the array, incrementing it moves it to the next element in
memory.
Dereferencing: *(p + i) accesses the value stored at the
memory address to which the pointer p + i points.
p is a pointer that is set to point to the first element of
myArray.
th
p + i gives the address of the i element of myArray
*(p + i) dereferences that address, and modifies the value
stored at that location.
For i = 0: *(p + 0) = 5 * 0 = 0
For i = 1: *(p + 1) = 5 * 1 = 5
For i = 2: *(p + 2) = 5 * 2 = 10
For i = 3: *(p + 3) = 5 * 3 = 15
For i = 4: *(p + 4) = 5 * 4 = 20
Third   0,2,4,6,8,   Output: (1 Marks)
Output:
Explanation: (1 Mark)
In the main() function, fillArray(myArray, 5) is called. Here,
myArray (the array) is passed to the function as a pointer, and
5 is passed as the size of the array.
The function takes two parameters:
int *arr: A pointer to the first element of the array
(myArray in this case).
int size: The size of the array, which is 5.
Then fillArray function modifies the array by setting each
element to i * 2, where i is the index of the element. After
modifying, it prints the array elements, which results in the
output: 0,2,4,6,8,
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int n;
Page 4 of 15
--- page 5 ---
// Input the size of the square matrix
cout << "Enter the size of the square matrix: ";
cin >> n;
int matrix[n][n];
int sum = 0;
// Reading the matrix
cout << "Enter elements of the matrix:\n";
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
cin >> matrix[i][j];
// Calculating the sum of upper triangular elements
for (int i = 0; i < n; i++)
for (int j = i; j < n; j++) // j starts from i to only consider upper triangular
sum += matrix[i][j]*matrix[i][j];
// Displaying the result
cout << "sum of squares at upper triangular matrix: " << sum << endl;
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Salesman {
5.   private:
6.   int id;
7.   string name;
8.   float totalSales;
9.   public:
10.   void getData() {
11.   cout << "Enter Salesman ID: ";
12.   cin >> id;
13.   cout << "Enter Salesman Name: ";
14.   cin >> name;
15.   cout << "Enter Total Sales: ";
16.   cin >> totalSales;
17.   }
18.   void displayData() {
Page 5 of 15
--- page 6 ---
19.   cout << "ID: " << id << ", Name: " << name << ", Total Sales: $" << totalSales << endl;
20.   }
21. };
22. int main() {
23.
24.   Salesman salesmen;
25.   cout << "\nEnter details for salesman "<< ":\n";
26.   salesmen.getData();
27.   cout << "\nSalesmen details :\n";
28.   salesmen.displayData();
29.   return 0;
30. }
c. Value of a - 2 marks,   5
Value of b and c 1,1 marks each
explanation of ++ & -- - 1 mark
Output:-
a=58 b=8 c=41
3.   20
10
a.
Program:
#include <iostream>
using namespace std;
int main() {
int number, reversedNumber = 0;
cout << "Enter an integer: ";
cin >> number;
int originalNumber = number;
while (number != 0) {
Page 6 of 15
--- page 7 ---
int digit = number % 10;
reversedNumber = reversedNumber * 10 + digit;
number /= 10;
}
cout << "The reverse of " << originalNumber << " is: " << reversedNumber << endl;
return 0;
}
b. Data Abstraction: - Explanation+Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Data Abstraction focuses on exposing only the necessary information of an object to the outside world while hiding the
internal implementation details. Essentially, abstraction allows you to interact with objects through a well-defined interface
without needing to know the inner workings of the object.
It simplifies complex systems by breaking them into manageable parts. This not only makes code easier to understand and
use but also allows for flexible and maintainable programs. With abstraction, the user does not need to understand how the
object is implemented, only how to interact with it.
Key Points of Data Abstraction:
1. Hides Implementation Details: Internal workings are hidden from the user; only necessary functionality is exposed.
2. Focus on What an Object Does, Not How: Users are concerned with what the object can do, not how it does it.
3. Improves Code Modularity: By separating the interface from the implementation, you can change internal
implementations without affecting external code.
Example of Data Abstraction in C++: (Example may vary)
#include<iostream>
using namespace std;
// Class definition implementing data abstraction
class Add {
// Private data members (hidden from the outside world)
private:
int a, b;
// Public interface (exposed to the outside world)
public:
// Method to set numbers
void setNumbers(int x, int y) {
a = x;
b = y;
}
// Method to add numbers (internal details hidden)
int add() {
return a + b;
}
};
int main() {
Calculator calc;
// Setting the numbers through public interface
calc.setNumbers(10, 20);
// Using the public methods to perform operations
cout << "Sum: " << calc.add() << endl;
return 0;
Page 7 of 15
--- page 8 ---
}
Program:
#include <iostream>
using namespace std;
class Developer {
public:
int dev_id, dev_experience;
};
int main() {
Developer d1;
cout<<"Enter the Developer id: ";
cin>>d1.dev_id;
cout<<"Enter the Developer experience: ";
cin>>d1.dev_experience;
if(d1.dev_experience>5)
cout<<"Senior Developer";
else
cout<<"Junior Developer";
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2 marks   10
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. struct Pizza
5. {
6. string name;
7. float preparation_time;
8. int number_of_workers;
9. float labour_cost_per_hour;
10. float total_labour_cost;
11. };
12. int main()
13. {
14. Pizza pizzas[5];
15. string highest_cost_pizza_name;
Page 8 of 15
--- page 9 ---
16. float highest_cost = 0.0;
17. for (int i = 0; i < 5; i++)
18. {
19. cout << "Enter details for pizza " << i + 1 << endl;
20. cout << "Name of pizza: ";
21. cin >> pizzas[i].name;
22. cout << "Preparation time (in hours): ";
23. cin >> pizzas[i].preparation_time;
24. cout << "Number of workers: ";
25. cin >> pizzas[i].number_of_workers;
26. cout << "Labour cost per hour: ";
27. cin >> pizzas[i].labour_cost_per_hour;
28. pizzas[i].total_labour_cost = pizzas[i].preparation_time * pizzas[i].number_of_workers * pizzas[i].labour_cost_per_hour;
29. }
30.
31.
32. for (int i = 0; i < 5; i++)
33. {
34. if (pizzas[i].total_labour_cost > highest_cost)
35. {
36. highest_cost = pizzas[i].total_labour_cost;
37. highest_cost_pizza_name = pizzas[i].name;
38. }
39. }
40. cout << "The pizza with the highest total labour cost is: " << highest_cost_pizza_name << endl;
41. return 0;
42. }
10
b. 1. Syntax of Function - Declaration, definition, calling - 3Mark.
Page 9 of 15
--- page 10 ---
2. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Function Definition (3 Marks)
Logic/Operation (2 Marks)
A function in C++ consists of three main parts:
1. Function Declaration (Prototype):
The function declaration tells the compiler about the function's name, return type, and parameters. It is written before
main() or inside header files.
Syntax- return_type function_name(parameter_type parameter_name, ...);
Example - int add(int a, int b); // Function prototype
2. Function Definition:
The function definition contains the actual body of the function. It includes the logic of what the function should do.
Syntax- return_type function_name(parameter_type parameter_name, ...) {
// Function body
}
3. Function Call:
A function is called by specifying its name and passing arguments (if any).
Syntax - function_name(argument1, argument2, ...);
int sum = add(5, 10); // Function call
C++ Program to Declare, Define, and Call a power() Function
#include <iostream>
using namespace std;
// Function declaration (prototype)
int power(int base, int exponent);
// Function definition
int power(int base, int exponent) {
int result = 1;
// Loop to multiply base exponent times
for (int i = 1; i <= exponent; i++) {
result *= base;
}
return result; // Return the result of base^exponent
}
int main() {
int base, exponent;
// Input base and exponent from user
cout << "Enter base: ";
cin >> base;
cout << "Enter exponent: ";
cin >> exponent;
// Function call to calculate power
int result = power(base, exponent);
// Display the result
cout << base << "^" << exponent << " = " << result << endl;
return 0;
}
Sample Output
Page 10 of 15
--- page 11 ---
Enter base: 2
Enter exponent: 3
2^3 = 8
5.   20
a.   10
#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
string name;
int age;
public:
void getDetails() {
cout << "Enter Name: ";
getline(cin, name);
cout << "Enter Age: ";
cin >> age;
cin.ignore();
}
void displayDetails() {
cout << "Name: " << name << endl;
cout << "Age: " << age << endl;
}
};
class Student : public Person {
private:
int grade;
public:
void getStudentDetails() {
getDetails();
cout << "Enter Grade: ";
Page 11 of 15
--- page 12 ---
cin >> grade;
}
void displayStudentDetails() {
displayDetails();
cout << "Grade: " << grade << endl;
}
};
int main() {
Student student;
student.getStudentDetails();
student.displayStudentDetails();
return 0;
}
10
Page 12 of 15
--- page 13 ---
b. #include <iostream>
using namespace std;
void min_max(int arr[], int size) {
int min = arr[0];
int max = arr[0];
for (int i = 1; i < size; i++) {
if (arr[i] < min) {
min = arr[i];
}
if (arr[i] > max) {
max = arr[i];
}
}
cout << "Smallest element: " << min << endl;
cout << "Largest element: " << max << endl;
}
int main() {
int size;
cout << "Enter the number of elements in the array: ";
cin >> size;
int arr[size];
cout << "Enter " << size << " elements:" << endl;
for (int i = 0; i < size; i++) {
cin >> arr[i];
}
min_max(arr, size);
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper sequence of letters + 3 marks for   10
printing the appropriate number of spaces before the sequence of letters
Page 13 of 15
--- page 14 ---
#include<iostream>
using namespace std;
int main()
{
int n,i,j;
char ch='a';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<=n-i;j++)
{
cout<<" ";
}
if(i%2==0)
{
for(j=1;j<=i;j++)
{
cout<<char(ch-32)<<" ";
ch++;
}
}
else
{
for(j=1;j<=i;j++)
{
cout<<ch<<" ";
ch++;
}
}
cout<<endl;
}
return 0;
}
Page 14 of 15
--- page 15 ---
b. #include <iostream>   5
using namespace std;
int main() {
const int SIZE = 5;
int original[SIZE];
int copied[SIZE];
cout << "Enter " << SIZE << " elements for the original array:" << endl;
for (int i = 0; i < SIZE; i++) {
cin >> original[i];
}
for (int i = 0; i < SIZE; i++) {
copied[i] = original[i];
}
cout << "Copied array elements are:" << endl;
for (int i = 0; i < SIZE; i++) {
cout << copied[i] << " ";
}
cout << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 15 of 15
````

## 2024-25 · Re-Exam · Sem 3 · Answer key · paper f47d8c44e55b

- Departments: Information Technology
- Programmes: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX YEARS INTEGRATED PROGRAM - 7037
- Source: `00_Original_Downloads/2024/65008__Semester III.zip :: Re-Exam/BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX YEARS INTEGRATED PROGRAM - 7037/Programming for Problem Solving/ANS_Re-Exam_Programming for Problem Solving(701CO0C018)_Semester III_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: II/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 98000a05e06e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_AIDS_7056/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper f2d47883b4e6

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_AI_7012/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper ee8fc507d285

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_CSBS_7036/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 9c26ccc6b5c3

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_CSE_DS_7057/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 96235098fbaf

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_Civil_7005/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper ca3d2ae5a285

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_Computer_7002/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper c955858aff3a

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_DS_7009/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper fb1658ea53cd

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_EXTC_7006/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 24eed4f37e73

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_IT_7001/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 8d91a6b8a1a2

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_Mechanical_7003/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 0eabde703261

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/BTech_Mechatronics_7004/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 0b441920c479

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MBATech_AI_7051/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper 674a6ad3ca9e

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MBATech_Computer_7047/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper d1bf0ee952c5

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MBATech_DS_7052/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper e91fc2bb81bb

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MBATech_IT_7041/Programming for Problem Solving/ANS_Programming for Problem Solving(702CO0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: I/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 5 · Answer key · paper b7ca37c30f47

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_05/Re-Exam/Integrated_Computer_7032/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: III/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````

## 2024-25 · Re-Exam · Sem 5 · Answer key · paper 89a3b917e11a

- Departments: Mechanical
- Programmes: Integrated Mechanical 7031
- Source: `02_Question_Papers/2024/Sem_05/Re-Exam/Integrated_Mechanical_7031/Programming for Problem Solving/ANS_Programming for Problem Solving(701CO0C018)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 Feb 2025
- Text: mixed (18 pages), mean OCR confidence 72.0

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CE)/B. Tech (CIVIL)/B. Tech
(CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech - (CSEDS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg.
(CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA. Tech (AI)/MBA Tech (Comp)/MBA. Tech (DS)/MBA. Tech (IT)
Year: III/Semester I/Semester III/Semester V (Exam Year: 2024-2025)
Subject: Programming for Problem Solving
Date: 20 Feb 2025   Time: 02:00 pm - 05:00 pm (03:00 Hrs.)
Max Marks: 100
RE EXAMINATION(2024-2025)
Instructions:
1. This Synoptic paper contains 18 pages
2. Section A is compulsory.
3. Attempt any 4 questions from Section B
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
.   Section A   20
a.
5
Page 1 of 18
--- page 2 ---
b.   5
- String is an array of characters
- Strings terminated with ‘\0’
Declaration of String…
Syntax:-
char string_name[size];
example:-
char month[15];
char studentname[20];
char s1[10],s2[10];
Initialization of String…
Syntax:-
char string_name[size] = {characters in single inverted comma, separated with comma};
or
char string_name[size] = “string”;
Example:-
char subject[10] = {‘c’,‘p’,‘p’, ‘\0’ };
char name[10] = “cpp”;
char name[ ] = “cpp”;
c. #include<iostream>   5
using namespace std;
class multiplication
{
public:
Page 2 of 18

[Text in pictures on this page, read by OCR]
<iostream>
1a ace std;

int mainQ)
{

int num = 96:

if (um > 0)

cout << "The number is positive"
else if (num <0)
cout << "The number is negative"

cout << "Zero":

return 0;
--- page 3 ---
void mul(int x, int y)
{
cout<<"Multiplication is "<<x+y<<endl;
}
void mul(float a, float b)
{
cout<<"Multiplication is "<<a+b<<endl;
}
};
int main()
{
multiplication m;
m.mul(10,20);
m.mul(10.0f,4.5f);
}
d.
5
Page 3 of 18
--- page 4 ---
Read n

i=2,. sum=0

N
——
¥

sum =sum+j
j=i+2

+ ——_

Section B(Attempt Any 4 Questions)

Page 4 of 18

[1M]

_2M]

_PMy

80

20

10
--- page 5 ---
a. #include <iostream>
using namespace std;
int main() {
int lateDays;
float lateFee = 0.0;
// Input number of days past the return deadline
cout << "Enter the number of days past the return deadline: ";
cin >> lateDays;
// Determine the late return fee based on days
if (lateDays <= 5) {
lateFee = lateDays * 50; // Rs. 50 per day for ≤ 5 days
} else if (lateDays > 5 && lateDays <= 10) {
lateFee = lateDays * 100; // Rs. 100 per day for > 5 and ≤ 10 days
} else { // lateDays > 10
lateFee = lateDays * 200; // Rs. 200 per day for > 10 days
}
// Display the late return fee
cout << "The late return fee is: Rs. " << lateFee << endl;
return 0;
}
b. Variable declaration – 01 Mark   5
Reading input and displaying output – 01 Mark
Use of correct formula/Logic – 03 marks
Page 5 of 18

[Text in pictures on this page, read by OCR]
If.else if.. Ladder flow chart

(expression1)
Statement(s)1

(expression2

Statement(s)2

Statement(s)3

Statement(s)4

Rest of the code
--- page 6 ---
#include <iostream>
using namespace std;
int main()
{
int n,d1,d2,d3,s;
cout<<"Enter the number: ";
cin>>n;
d1 = n % 10;
n = n /10;
d2 = n % 10;
n = n / 10;
d3 = n % 10;
s = d1*d1*d1 + d2*d2*d2 + d3*d3*d3;
cout<<s;
return 0;
}
c. First output:   5
p:3. Here, the pointer *p points to the address of the first index element of the array arr,
thus
int *p = arr implies *p = arr[0] and thus *p = 3. // 2 marks
Second output:
6 12 18. In the loop above the output of the array, each element of the array is being
multiplied by 2, accessing each element by using pointers. // 3 marks
Expected solution   marks
1 mark for value of p & 1 mark for explanation   2 marks
1.5 mark for value of array & 1.5 mark for
3 marks
explanation
2.   20
a. #include <iostream>   10
using namespace std;
int main() {
int r1,c1;
Page 6 of 18
--- page 7 ---
cout << "Enter rows and columns for first matrix: ";
cin >> r1 >> c1;
int matrix1[r1][c1], matrix2[r1][c1], result[r1][c1];
// Reading first matrix
cout << "Enter elements of first"<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix1[i][j];
// Reading second matrix
cout << "Enter elements of second "<<r1<<" X "<<c1<<" matrix:\n";
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
cin >> matrix2[i][j];
// Adding the matrices
for (int i = 0; i < r1; i++)
for (int j = 0; j < c1; j++)
result[i][j] = matrix1[i][j] + matrix2[i][j];
// Displaying the result
cout << "Resultant Matrix after Addition:\n";
for (int i = 0; i < r1; i++) {
for (int j = 0; j < c1; j++)
cout << result[i][j] << " ";
cout << endl;
}
return 0;
}
b.   5
1. #include <iostream>
2. #include <string>
3. using namespace std;
4. class Person {
5.   private:
6.   string name;
Page 7 of 18
--- page 8 ---
7.   int age;
8.   public:
9.   Person(string pName, int pAge) {
10.   name = pName;
11.   age = pAge;
12.   }
13.
14.   void display(){
15.   cout << "Name: " << name << ", Age: " << age << endl;
16.   }
17. };
18. int main() {
19.   Person p("Ram Mishra", 30);
20.   p.display();
21.   return 0;
22. }
c. //Output:-   5
a: 1 // 2 marks
b: 4 // 2 marks
Explanation - 1 mark
3.   20
a. Syntax:   10
initialization ;
do {
Page 8 of 18
--- page 9 ---
// Code to be executed repeatedly
increment/decrement;
} while (condition);
Program:
#include <iostream>
using namespace std;
int main() {
int sum = 0;
for (int i = 1; i < 1000; i++) {
if (i % 3 == 0 || i % 5 == 0) {
sum += i;
}
}
cout << "The sum of all multiples of 3 or 5 below 1000 is: " << sum << endl;
return 0;
}
b. Encapsulation – Explanation + Example (3+2 Marks)   10
Class (0.5), Data Members (1), Object (0.5) - 02 marks
Accessing Data member in main and operations – 03 marks
Page 9 of 18
--- page 10 ---
Encapsulation in C++ is defined as the wrapping up of data and information in a
single unit. In Object Oriented Programming, Encapsulation is defined as binding
together the data and the functions that manipulate them.
For example, (Example may vary)
class Rectangle {
public:
int length;
int breadth;
int getArea() {
return length * breadth;
}
};
In the above program, the function getArea() calculates the area of a rectangle. To
calculate the area, it needs length and breadth. Hence, the data members (length and
breadth) and the function getArea() are kept together in the Rectangle class.
Features of Encapsulation
• We can not access any function from the class directly. We need an object to access
that function that is using the member variables of that class.
• The function which we are making inside the class must use only member variables,
only then it is called encapsulation.
• If we don’t make a function inside the class which is using the member variable of the
class then we don’t call it encapsulation.
• Encapsulation improves readability, maintainability, and security by grouping data
and methods together.
• It helps to control the modification of our data members.
Page 10 of 18
--- page 11 ---
Program:
#include<iostream>
using namespace std;
class Resort
{
public:
int room_no,no_of_days;
float charges;
};
int main()
{
Resort r;
float bill;
cout<<"\nEnter room number:";
cin>>r.room_no;
cout<<"\nEnter number of days:";
cin>>r.no_of_days;
cout<<"\nEnter room charges:";
cin>>r.charges;
bill=r.charges*r.no_of_days;
cout<<"\nResort details are:";
cout<<"\nRoom number is:"<<r.room_no;
cout<<"\nNumber of days are:"<<r.no_of_days;
cout<<"\nRoom charges are:"<<r.charges;
cout<<"\nTotal bill is:"<<bill;
}
4.   20
a. Marking Scheme : Structure Definition and declaration of structure – 2 + 2   10
marks
Reading, processing (logic) and displaying output – 2 + 2 + 2 marks
#include <iostream>
#include <string>
using namespace std;
// Define structure for Patient
struct Patient {
Page 11 of 18
--- page 12 ---
int id;
string name;
string illness;
string doctor;
};
int main()
{
// Array to store 10 patients
Patient patients[10];
// Input patient details
for (int i = 0; i < 10; i++) {
cout << "Enter details for patient " << i + 1 << ":"<<endl;
cout << "ID: ";
cin >> patients[i].id;
cin.ignore(); // To consume the newline character left by cin
cout << "Name: ";
cin>>patients[i].name;
cout << "Illness: ";
cin>>patients[i].illness;
cout << "Doctor assigned: ";
cin>>patients[i].doctor;
cout << endl;
}
// Get the doctor's name to search for patients
string searchDoctor;
cout << "Enter the name of the doctor to see their patients: ";
cin>>searchDoctor;
// Display details of patients under the same doctor
cout << "\nPatients treated by Dr. " << searchDoctor << ":"<<endl;
bool found = false;
for (int i = 0; i < 10; i++) {
if (patients[i].doctor == searchDoctor) {
cout << "Patient ID: " << patients[i].id << "\n";
cout << "Patient Name: " << patients[i].name << "\n";
cout << "Illness: " << patients[i].illness << "\n";
cout << "------------------------\n";
Page 12 of 18
--- page 13 ---
found = true;
}
}
if (!found) {
cout << "No patients are assigned to Dr. " << searchDoctor << ".\n";
}
return 0;
}
10
b. 1. Function definition - 1 Mark.
2. Function usage - 2 Marks
3. Program -
Function Declaration (1 Mark)
Function Call (1 Mark)
Program Function Definition (3 Marks)
Logic/Operation (2 Marks)
What is a function in C++?
A function in C++ is a block of code that performs a specific task. It is used to break
the program into smaller, manageable parts, making the code more modular and
reusable. Functions can take input (arguments), perform a task, and optionally return a
result.
Why are functions used in programming?
Code reuse: Functions allow you to write a block of code once and reuse it multiple
times.
Modularity: Breaking code into functions makes it easier to organize and maintain.
Abstraction: Functions hide the complexity and provide a clear interface for the task
they perform.
C++ Program: Swapping Two Numbers Using Pass-by-Reference
#include <iostream>
using namespace std;
Page 13 of 18
--- page 14 ---
// Function to swap two numbers using pass-by-reference
void swap(int &a, int &b) {
int temp = a;
a = b;
b = temp;
}
int main() {
int num1 = 10, num2 = 20;
cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
// Call the swap function
swap(num1, num2);
cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
return 0;
}
OUTPUT:
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10
5.   20
a. #include <iostream>   10
#include <string>
using namespace std;
class Employee {
protected:
string name;
int employeeID;
public:
void inputEmployeeDetails() {
cout << "Enter Employee Name: ";
getline(cin, name);
cout << "Enter Employee ID: ";
cin >> employeeID;
cin.ignore();
}
void displayEmployeeDetails() {
Page 14 of 18
--- page 15 ---
cout << "Employee Name: " << name << endl;
cout << "Employee ID: " << employeeID << endl;
}
void displayRole() {
cout << "Role: General Employee" << endl;
}
};
class Manager : public Employee {
private:
string department;
public:
void inputManagerDetails() {
inputEmployeeDetails();
cout << "Enter Department: ";
getline(cin, department);
}
void displayManagerDetails() {
displayEmployeeDetails();
cout << "Department: " << department << endl;
}
void displayRole() {
cout << "Role: Manager" << endl;
}
};
int main() {
Manager manager;
manager.inputManagerDetails();
manager.displayManagerDetails();
manager.displayRole();
return 0;
}
b. Finding Factorial using recursion - 04 marks   10
Finding summation using recursion - 04 marks
Displaying result - 02 marks
Page 15 of 18
--- page 16 ---
#include<iostream>
using namespace std;
int fact(int n) {
if(n == 1)
return 1;
return n * fact(n - 1);
}
int sum(int n) {
if(n == 1)
return 1;
return fact(n) + sum(n - 1);
}
int main() {
int n,s;
cout << "Enter a positive integer: ";
cin >> n;
s= sum(n);
cout <<"Sum is"<<s;
return 0;
}
6.   20
a. Step marking- 3 marks for correct looping + 4 marks for printing the proper   10
sequence of letters + 3 marks for printing the appropriate number of spaces
before the sequence of letters
#include<iostream>
Page 16 of 18
--- page 17 ---
using namespace std;
int main()
{
int n,i,j;
char ch='A';
cout<<"Enter number of rows to be printed";
cin>>n;
for(i=1;i<=n;i++)
{
for(j=1;j<i;j++)
{
cout<<" ";
}
for(j=1;j<=n-i+1;j++)
{
cout<<ch<<" ";
}
ch++;
cout<<endl;
}
return 0;
}
b. #include <iostream>   5
using namespace std;
Page 17 of 18
--- page 18 ---
int main() {
char str[50];
int vowelCount = 0;
cout << "Enter a string (up to 100 characters): ";
cin.getline(str, 50);
for (int i = 0; str[i] != '\0'; i++)
{
char ch = str[i];
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
vowelCount++;
}
}
cout << "Number of vowels: " << vowelCount << endl;
return 0;
}
c. Correct conversion – 2 Marks   5
Correct Program with I/O – 3 Marks
Page 18 of 18
````
