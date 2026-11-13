# Computational Thinking for Problem Solving: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper eef13b369edb

- Departments: AI and Data Science, Information Technology
- Programmes: BTech AIDS 7056, BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_AIDS_7056/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 12394ec39239

- Departments: AI and Machine Learning, Artificial Intelligence, Civil, Computer Engineering, Computer Science and Business Systems, Cyber Security, Data Science, Information Technology
- Programmes: BTech AI 7012, BTech AIML 7053, BTech Civil 7005, BTech Computer 7002, BTech CSBS 7036, BTech CSE DS 7057, BTech CyberSecurity 7010, BTech DS 7009, MBATech Computer 7047, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_AIML_7053/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf` (+9 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Copying contents in uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 43ba7a819400

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_CSBS_7036/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026_43ba7a8194.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper cce23a28df84

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_CS_7055/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper e9cfd764d415

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_EXTC_7006/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 207cc97e0f72

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_Mechanical_7003/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 942ff7202138

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/BTech_Mechatronics_7004/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 63e7dd26beb8

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MBATech_AI_7051/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 5b54a7e88915

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MBATech_DS_7052/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: mixed (13 pages), mean OCR confidence 73.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 29 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks - BMI Calculation
#include <stdio.h>
int main() {
float weight, height, bmi;
[5]
printf("Enter weight (kg) and height (m): ");
scanf("%f %f", &weight, &height);
bmi = weight / (height * height);
printf("BMI = %.2f\n", bmi);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include<stdio.h>
main( ){   [5]
int cp, sp;
printf("Enter Cost and Selling Price: \n ");
scanf("%d%d",&cp,&sp);
if(cp<sp)
printf("Profit");
********** 1 **********
--- page 2 ---
else if(cp>sp)
printf("Loss");
else
printf("Neither");
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float convertToFahrenheit(float celsius) {
return (celsius * 9.0 / 5.0) + 32;
}
int main() {   [5]
float celsius, fahrenheit;
printf("Enter temperature in Celsius: ");
scanf("%f", &celsius);
fahrenheit = convertToFahrenheit(celsius);
printf("Temperature: %.2f°C = %.2f°F\n", celsius, fahrenheit);
return 0;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Product {
int code;
char name[50];
int quantity;
float price;
};
int main() {
struct Product p;
[5]
printf("Enter Product Code: ");
scanf("%d", &p.code);
printf("Enter Product Name: ");
scanf("%s", p.name); )
printf("Enter Quantity: ");
scanf("%d", &p.quantity);
printf("Enter Price per Unit: ");
scanf("%f", &p.price);
printf("\n----- Product Details -----\n");
printf("Product Code   : %d\n", p.code);
printf("Product Name   : %s\n", p.name);
printf("Quantity   : %d\n", p.quantity);
printf("Price per Unit : %.2f\n", p.price);
return 0;
********** 2 **********
--- page 3 ---
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks – Bubble sort logic
2 Marks – Printing the sorted array
#include <stdio.h>
int main() {
int n, i, j, temp;
int arr[100]; // Maximum array size set to 100
printf("Enter number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
// Bubble sort   [10]
for(i = 0; i < n-1; i++) {
for(j = 0; j < n-i-1; j++) {
if(arr[j] > arr[j+1]) {
temp = arr[j];
arr[j] = arr[j+1];
arr[j+1] = temp;
}
}
}
printf("Sorted array:\n");
for(i = 0; i < n; i++) {
printf("%d ", arr[i]);
}
printf("\n");
}
B   5 Marks – Decomposition and Abstraction
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Decomposition and Abstraction
Decomposition
-   Its dictionary meaning is breakdown
- The basic paradigm to tackle large problem is clear – we must “divide and rule”
- Problem Decomposition helps in several ways:
o   It makes the problem more tractable by breaking it down into smaller,
more manageable parts.   [10]
o   It allows for a better understanding of the problem and its components.
o   It helps identify the key areas where solutions can be developed.
- Goal in decomposition is to create modules(subprograms/subproblems)
- Work distribution will be possible (people can work independently)
- While integrating or during maintenance, it will be possible to modify some of
the modules without affecting others.
- When decomposing a problem, we factor it into separate subproblems in such a
way that:
o Each subproblem is at the same level of detail.
********** 3 **********
--- page 4 ---
o Each sub-problem can be solved independently
o The solution to the subproblems can be combined to solve the original
problem
-   Example:-
o Merge sort
o Macros and Subroutines
o Compiler working is divided into a series of Phases
Abstraction:
-   Abstraction is the process of simplifying a problem by abstracting away
unnecessary details and focusing on the essential elements.
-   It involves identifying the relevant information and ignoring the irrelevant
details that do not affect the solution.
-   Abstraction is a way to do decomposition productively by changing the level of
detail to be considered.
-   It is nothing but removing unnecessary details from the problem.
-   Example:- High level → Assembly → Machine Level
-   In problem solving, abstraction simplifies the problem.
-   Example:-
o When designing an algorithm, we can ignore implementation details.
- The process of abstraction can be seen as an application of a many-to-one
mapping. [one function can be called any no of times ]
- One can achieve abstraction using a common mechanism, such as the use of
procedures(methods)
o By separating procedures and invocation.
-   Abstraction helps in several ways:
o   It reduces the complexity of the problem by removing irrelevant details.
o   It allows for a better understanding of the essential elements and their
relationships.
o   It facilitates the development of simpler solutions that are more
manageable and efficient.
********** 4 **********
--- page 5 ---
Start

Input temperature

Is temperature >= 40 ‘Yes Print "Very Hot"

No

Is temperature >= 30 Yes: Print "Hot"

No

Is temperature >= 20 ‘Yes: Print "Warm"

No

Is temperature >= 10 Yes: Print "Cool"

No

Is temperature < 10 Yes} Print "cold"

No

Stop J)

FIC DI EH ar
--- page 6 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
int choice, roll, r;
char name[30];
float marks;
printf("1.Append 2.Search : ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("student.txt", "a");
printf("Enter Roll, Name, Marks: ");
scanf("%d %s %f", &roll, name, &marks);
[10]
fprintf(fp, "%d %s %.2f\n", roll, name, marks);
printf("Record added.\n");
}
else if (choice == 2) {
fp = fopen("student.txt", "r");
printf("Enter Roll to search: ");
scanf("%d", &r);
int found = 0;
while (fscanf(fp, "%d %s %f", &roll, name, &marks) != EOF) {
if (roll == r) {
printf("Found: %d %s %.2f\n", roll, name, marks);
found = 1; break;
}
}
if (!found) printf("Record not found.\n");
}
fclose(fp);
return 0;
}
B   2 Marks – Character Array
3 Marks – function description and example
-   In C language, a string is a sequence of characters that ends with a null
character '\0'.   [5]
-   It is usually represented as a character array.
- Example:
o char name[10] = "CTPS";
strupr(str) - Converts all lowercase letters in a string to uppercase.
********** 6 **********
--- page 7 ---
strrev(str) - Reverses the order of characters in a string.
strcat(str1,str2) - Concatenates two strings; appends one string to the end of another.
strlen(str) - Finds the length of a string; returns the number of characters in a string.
Programming Example
main(){
char S[20]="CTPS",R[20]="C lang";
printf("\nLength = %d", strlen(S) );
strupr(S);
printf("\nString in Upper = %s", S);
strcat(S,R);
printf("\nAfter String Concatenation = %s", S);
strrev(S);
printf("\nReverse String is = %s", S);
}
C   1 Mark – list of basic data types (int, char, float, double)
2 Marks – variable declaration and initialisation
2 Marks - Output
#include <stdio.h>
int main() {
int a =5;
float b=5.6f;   [5]
char c = ‘D’;
double d = 6.0;
printf("A = %d \n", a);
printf("B = %f \n", b);
printf("C = %c\n", c);
printf("D = %lf\n", d);
return 0;
}
A
3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Q4   Aspect   Library Function   User-Defined Function
[10]
Definition   Predefined in C libraries   Written by programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Source   <stdio.h>, <math.h> etc.   Defined in source code
Reusability   Limited to provided functionality   Fully customizable
********** 7 **********
--- page 8 ---
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main( ) {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying GCD
Syntax:-
for (initlialization;condition;update_expression ){
//loop body
}
[10]
#include <stdio.h>
int main() {
int num1, num2, i, gcd ;
printf("Enter two numbers: ");
scanf("%d %d", &num1, &num2);
int min = (num1 < num2) ? num1 : num2;
for (i = 1; i <= min; i++) {
if (num1 % i == 0 && num2 % i == 0) {
gcd = i;
}
}
printf("The GCD of %d and %d is %d\n", num1, num2, gcd);
return 0;
}
A   2 Marks – File Opening in read mode
2 Marks – File Opening in write mode
4 Marks – Uppercase logic
2 marks – Closing the file
Q5
[10]
#include <stdio.h>
#include <ctype.h>
int main() {
FILE *S, *T;
char ch;
********** 8 **********
--- page 9 ---
S = fopen("input.txt", "r");
T = fopen("output.txt", "w");
if (S == NULL || T == NULL) {
printf("Error opening files!\n");
return 1;
}
while ((ch = fgetc(S)) != EOF) {
fputc(toupper(ch), T);
}
printf("File converted to uppercase successfully.\n");
fclose(S);
fclose(T);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying cars and its availability
#include <stdio.h>
struct Car {
char model[50];
char company[50];
int year;
float price;
};
int main() {
int n, i;
printf("Enter the number of cars: ");
scanf("%d", &n);
struct Car cars[n];
for(i = 0; i < n; i++) {
[10]
printf("\n--- Enter details of Car %d ---\n", i + 1);
printf("Model Name: ");
scanf("%s", cars[i].model);
printf("Company Name: ");
scanf("%s", cars[i].company);
printf("Year of Manufacture: ");
scanf("%d", &cars[i].year);
printf("Price: ");
scanf("%f", &cars[i].price);
}
printf("\n===== Cars Manufactured in 2025 =====\n");
int found = 0;
for(i = 0; i < n; i++) {
if(cars[i].year == 2025) {
printf("\nCar %d:\n", i + 1);
printf("Model Name : %s\n", cars[i].model);
printf("Company   : %s\n", cars[i].company);
printf("Year   : %d\n", cars[i].year);
printf("Price   : %.2f\n", cars[i].price);
********** 9 **********
--- page 10 ---
found = 1;
}
}
if(!found) {
printf("No cars found manufactured in 2025.\n");
}
return 0;
}
Q6 A   4 Marks – inline function
4 Marks – Recursive function definition and logic
2 Marks – input/output and function call from main( )
Inline Function:
A function defined with the inline keyword that requests the compiler to insert its code
directly at the call site, reducing function call overhead.
Example:
inline int square(int x) { return x * x; }
Benefits:
•   Faster execution (no call overhead).
•   Useful for short, frequently used functions.
Real-world example:
Used in embedded systems and signal processing for quick, repeated computations like   [10]
squaring, addition, or bit masking.
#include <stdio.h>
int reverse(int n, int rev) {
if (n == 0)
return rev;
return reverse(n / 10, rev * 10 + n % 10);
}
int main() {
int num, revNum;
printf("Enter a number: ");
scanf("%d", &num);
revNum = reverse(num, 0); // Call recursive function
if (num == revNum)
printf("%d is a Palindrome number.", num);
else
printf("%d is not a Palindrome number.", num);
return 0;
}
B   5 Marks – Pointers Arithmetic ( 3 explanation + 2 example )
5 Marks – Swapping function (Definition 3, input and call-2)   [10]
Pointer Arithmetic’s:
********** 10 **********
--- page 11 ---
-   Pointer arithmetic refers to performing arithmetic operations such as addition,
subtraction, increment, or comparison on pointer variables.
-   Since pointers store memory addresses, arithmetic operations are performed
based on the size of the data type to which the pointer points.
- When a pointer is incremented or decremented, it moves to the next or
previous memory location of the data type it points to.
-   For example, if p is an int * and each integer occupies 4 bytes, then p + 1
increases the address by 4 bytes, not by 1.
-   Pointer Addition – Moves the pointer forward by given number of
elements.e.g. p = p + 1
-   Pointer Subtraction – Moves the pointer backward. e.g. p= p-1
-   Pointer Increment p++
- Ponter Decrement p- -
#include <stdio.h>
int main() {
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
printf("Initial address: %p\n", p);
p = p+2;
printf("After p+2: %p, value = %d\n", p, *p);
p = p-2;
printf("After p-2: %p, value = %d\n", p, *p);
p++;
printf("After p++: %p, value = %d\n", p, *p);
p--;
printf("After p--: %p, value = %d\n", p, *p);
return 0;
}
//Program to exchange two numbers
#include <stdio.h>
void swap(int *x, int *y);
int main() {
int a, b;
printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nBefore swapping: a = %d, b = %d\n", a, b);
swap(&a, &b);
printf("After swapping: a = %d, b = %d\n", a, b);
return 0;
}
void swap(int *x, int *y) {
int temp;
temp = *x;
*x = *y;
*y = temp;
}
********** 11 **********
--- page 12 ---
A   1 Mark - Declaration of matrix and variables
2 Marks - Input of matrix size and elements
5 Marks- Logic for finding upper triangular elements
2 Marks - Proper printing of the upper triangular matrix
#include <stdio.h>
int main() {
int n, i, j;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d", &n);
printf("Enter the elements of the %dx%d matrix:\n", n, n);
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
printf("\nOriginal matrix:\n");
Q7
for(i = 0; i < n; i++) {   [10]
for(j = 0; j < n; j++) {
printf("%6d ", matrix[i][j]);
}
printf("\n");
}
printf("\nUpper triangular matrix:\n");
for(i = 0; i < n; i++) {
for(j = 0; j < n; j++) {
if(i<=j) {
printf("%6d", matrix[i][j]);
}
else
printf("%6d",0);
}
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Mark – Outer for loop (rows)
2 Mark – Inner for loop (spacing)
2 Mark – Inner for loop (column)
3 Mark – Printing the correct pattern
#include <stdio.h>
[10]
int main( )
{
int i,j,k,n;
printf(“Enter number of lines\n”);
scanf(“%d”,&n);
for(i=1;i<=n;i++){
for(k=1;k<=n-i;k++)
printf(" ");
for(j=1;j<=i;j++){
********** 12 **********
--- page 13 ---
printf("%d ",j%2);
}
printf("\n");
}

return 0;

FIR ICR 7] QI HO
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper a51682fddd30

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_AIDS_7056/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 3498457fdd08

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_AIML_7053/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 602e05a0c5a3

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_AI_7012/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 4a3e0679ac67

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_CSBS_7036/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 84d25697a56e

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_CSE_DS_7057/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 6b4aa5417c0e

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_CS_7055/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 6f503e54ae28

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_Civil_7005/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 8e7a4ce04974

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_Computer_7002/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Mar 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Sem I Spl Exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 13 Mar 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Section-A
Q1
CO-1   A.   Write a program to calculate and print the speed of an object in km/h, using   [05]
BL-2   the following formula. Input the distance in kilometers (km) and time in
hours (h).
speed = 𝐷𝑖𝑠𝑡𝑎𝑛𝑐𝑒
𝑇𝑖𝑚𝑒
1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – Speed Calculation
#include <stdio.h>
int main() {
float distance, time, speed;
printf("Enter distance in kilometers (km): ");
scanf("%f", &distance);
printf("Enter time in hours (h): ");
scanf("%f", &time);
speed = distance / time;
printf("Speed = %.2f km/h\n", speed);
return 0;
}
CO-2   B.   Implement a program that uses a loop to generate and display the   [05]
BL-3   multiplication table for N, where N is entered by the user.
1 Mark - Variables Declaration
1 Mark- User Input
********** 1 **********
--- page 2 ---
3 Marks – Looping statement and correct output
#include <stdio.h>
int main() {
int N, i;
printf("Enter a number: ");
scanf("%d", &N);
printf("\nMultiplication Table of %d:\n", N);
for (i = 1; i <= 10; i++) {
printf("%d x %d = %d\n", N, i, N * i);
}
return 0;
}
CO-3   C.   Develop a program to calculate the cube of a user-entered number using user   [05]
BL-3   defined function. The function should accept the number as an argument and
return the result to the main function.
3 Marks – function definition & correct logic
1 Mark – function call from main( )
1 Mark – Output display
#include <stdio.h>
int cube(int n) {
return n * n * n;
}
int main( ) {
int x;
scanf("%d", &x);
printf("Cube = %d", cube(x));
return 0;
}
CO-4   D.   Define a structure 'Date' with the members day, month, and year. Declare a   [05]
BL-3   variable of type 'Date' in main( ). Write a complete program to input and
display a person's date of birth.
2 Marks – Structure definition
1 Mark – Date variable declaration
2 Marks – Structure member access, input and output
struct Date {
int day;
char month[20];
int year;
};
int main() {
struct Date dob;
printf("Enter day: ");
scanf("%d %s %d",&dob.day,dob.month,&dob.year);
printf("%d-%s-%d", dob.day, dob.month, dob.year);
return 0;
}
********** 2 **********
--- page 3 ---
Section-B
Q2
CO-3 A   Create a program that prompts the user to input a one-dimensional array of   [10]
BL-3   size 'n', identifies the largest and smallest elements in the array, and then
outputs the sum of these two elements.
1 Mark - Declaration of array and variables
2 Marks – Reading array elements from the user
5 Marks finding the largest and smallest elements
2 Marks – sum of the largest and smallest elements
#include <stdio.h>
int main( ) {
int n, i;
int arr[100];
int largest, smallest, sum;
printf("Enter the number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
largest = arr[0];
smallest = arr[0];
for(i = 1; i < n; i++) {
if(arr[i] > largest) {
largest = arr[i];
}
if(arr[i] < smallest) {
smallest = arr[i];
}
}
sum = largest + smallest;
printf("Sum of largest and smallest element: %d\n", sum);
}
CO-1 B   Explain the steps in computational thinking. Draw a flowchart that prompts   [10]
BL-2   the user to enter the three sides of a triangle, checks whether the triangle is
valid, and, if valid, determines whether it is Equilateral, Isosceles, or Scalene.
A triangle is valid if the sum of any two sides is greater than the third side.
Triangles are classified by side lengths as Equilateral (3 equal sides), Isosceles
(at least 2 equal sides), or Scalene (0 equal sides).
5 Marks – Steps in computational thinking
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking
– 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
********** 3 **********
--- page 4 ---
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example:-Temperature Conversion from Celsius to Fahrenheit
1. Decomposition
•   Input the temperature in Celsius.
• Use formula: F = (C × 9/5) + 32.
• Output the temperature in Fahrenheit.
2. Pattern Recognition
•   It’s a direct mathematical formula application.
•   Similar structure can be used for other unit conversions (km to miles,
etc.).
3. Abstraction
• Focus only on the numeric value of Celsius.
• Ignore units or environmental factors.
• Only one formula is needed; user doesn’t need to know the logic
behind it.
4. Algorithmic Thinking
1. Start
2. Input C (Celsius temperature)
3. F = (C * 9.0 / 5.0) + 32
4. Print F (Fahrenheit temperature)
5. End
********** 4 **********
--- page 5 ---
Q3
CO-5 A   Develop a program that can perform operations like appending and searching   [10]
BL-3   in Employee.dat. It should be able to add a new employee's data and search
for a record by the employee's number. The data includes the employee's
number, name, and salary.
2 Marks – Opening the file with the appropriate file opening mode.
4 Marks – Append Operation
4 Marks – Search Operation & display
#include <stdio.h>
#include <stdlib.h>
struct Employee {
int empNo;
char name[50];
float salary;
}emp;
int main() {
********** 5 **********
--- page 6 ---
FILE *fp;
int choice, searchNo, found = 0;
printf("Enter your choice 1 Add and 2 Search: ");
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("Employee.dat", "ab");
if (fp == NULL) {
printf("Error opening file!\n");
return 1;
}
printf("\nEnter Employee Number: ");
scanf("%d", &emp.empNo);
printf("Enter Employee Name: ");
scanf(" %[^\n]", emp.name);
printf("Enter Employee Salary: ");
scanf("%f", &emp.salary);
fwrite(&emp, sizeof(emp), 1, fp);
fclose(fp);
printf("\nEmployee record added successfully!\n");
}
else if (choice == 2) {
fp = fopen("Employee.dat", "rb");
if (fp == NULL) {
printf("File not found!\n");
return 1;
}
printf("\nEnter Employee Number to search: ");
scanf("%d", &searchNo);
while (fread(&emp, sizeof(emp), 1, fp) == 1) {
if (emp.empNo == searchNo) {
printf("\nRecord Found:\n");
printf("Employee Number: %d\n", emp.empNo);
printf("Name: %s\n", emp.name);
printf("Salary: %.2f\n", emp.salary);
found = 1;
break;
}
}
if (found==0) {
printf("\nRecord not found!\n");
}
fclose(fp);
}
else {
printf("\nInvalid choice!\n");
}
********** 6 **********
--- page 7 ---
return 0;
}
CO-3 B   Write a program to count the number of digits in a given string.   [05]
BL-3   1 Mark for character array declaration
1 Mark for reading a character array/string
3 Marks – Logic to count the number and display it
#include <stdio.h>
int main( ) {
char str[200];
int i, digits = 0,;
printf("Enter a string: ");
gets(str);
for (i = 0; str[i] != '\0'; i++) {
// Check for digits
if (str[i] >= '0' && str[i] <= '9')
digits++;
}
printf("Number of digits is %d\n", digits);
}
CO1   C   Describe the basic structure of a C program and provide a relevant example.   [05]
BL-2   3 Marks – Structure of C program,
2 Marks – Programming example
Basic Structure of a C   Programming Example
Program
Documentation Section   /*C program to find area of Circle*/
#include Section/Link   #include<stdio.h>
Section
Definition Section   #define PI 3.147
Global Declaration   float A;
Section
main( ){   int main(){
float rad;
//body
printf("Enter Radius\n");
}   scanf("%f",&rad);
A = PI*rad*rad;
********** 7 **********
--- page 8 ---
Subprogram Section   printf("Area is %f",A);
return 0;
Function1( ){
}
}
:
function( ){
}
Q4
CO-3   Explain the process of parameter passing with examples. Develop a program   [10]
BL-3 A   that counts the number of positive and negative integers in an array by
utilising a user-defined function.
4 Marks – Parameter passing example
3 Marks – Function Definition and Logic of counting +ve and -ve
numbers
2 Marks – passing an array and its size to a function from main( )
1 Mark – displaying output
Parameter passing mechanisms:
Call by value   Call by address
#include <stdio.h>   #include <stdio.h>
int cube(int n) {   int cube(int *n) {
return n * n * n;   return (*n) * (*n) * (*n);
}   }
int main( ) {   int main( ) {
int x;   int x;
scanf("%d", &x);   scanf("%d", &x);
printf("Cube = %d",   printf("Cube=%d",
cube(x));   cube(&x));
return 0;   return 0;
}   }
Normal/Ordinary Variables are   Pointer variables are used as a
used as a parameter   parameter
Formal parameter can’t update   Formal parameter update the value
the value of actual parameter   of actual parameter
#include <stdio.h>
void countNumbers(int arr[ ], int n, int *pos, int *neg) {
*pos = 0;
*neg = 0;
for (int i = 0; i < n; i++) {
if (arr[i] >= 0)
(*pos)++;
else
********** 8 **********
--- page 9 ---
(*neg)++;
}
}
int main( ) {
int n, pos, neg;
printf("Enter number of elements: ");
scanf("%d", &n);
int arr[n];
printf("Enter %d elements: ", n);
for (int i = 0; i < n; i++)
scanf("%d", &arr[i]);
countNumbers(arr, n, &pos, &neg);
printf("Positive Numbers = %d\n", pos);
printf("Negative Numbers = %d\n", neg);
return 0;
}
CO-2 B   How does a while loop differ from a do-while loop? Write a program that uses   [10]
BL-3   a switch-case statement to determine whether an entered character is a vowel
or a consonant. The program should also validate the input (using if-else) to
ensure that only alphabetic characters are processed. If the input is a number
or a special symbol, the program should indicate that the input is not an
alphabetic character.
4 Marks – while and do-while difference (correct 3-4 points)
4 Marks – appropriate use of switch-case
2 Marks – if-else to ensure alphabets
While Loop   Do-While Loop
In the While loop, the condition is   In a do-while loop, the statement
tested before any statement is   is executed at least once, even if
executed.   the condition is false
Syntax:   Syntax:
while(condition){   do{
// statements   //statements
}   }while(expression);
In a while loop, no semicolon is   In a do-while loop, a semicolon is
needed after the end of the   needed after the end of the
condition.   condition
A while loop is an entry-   A do-while loop is an exit-
controlled loop.   controlled loop.
The while loop may or may not be A do-while loop will execute at
executed at all.   least once.
A while loop can lead to errors if A do-while loop helps prevent
the condition is always false.   errors as it runs at least once.
#include <stdio.h>
int main() {
char ch;
********** 9 **********
--- page 10 ---
printf("Enter a character: ");
scanf("%c", &ch);
if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')) {
if (ch >= 'A' && ch <= 'Z') {
ch = ch + 32;
}
switch (ch) {
case 'a':
case 'e':
case 'i':
case 'o':
case 'u':
printf("It is a Vowel.\n");
break;
default:
printf("It is a Consonant.\n");
}
} else {
printf("Input is not an alphabetic character.\n");
}
return 0;
}
Q5
CO-5 A   Write a program that keeps writing words to a file until the user enters ‘y’,   [10]
and stops when the user enters ‘n’. After the writing is complete, read the file
BL-3
and count how many words end with the letter ‘e’.
2 Marks – File Opening and Closing
4 Marks – Writing in the file until the user enters ‘y’
4 Marks – Counting the words ending with the letter ‘e’.
#include <stdio.h>
int main() {
FILE *fp;
char word[100],choice='y';
int count = 0,length;
fp = fopen("data.txt", "w");
if (fp == NULL) {
printf("File cannot be opened!\n");
return 1;
}
printf("Enter words to write into file:\n");
printf("Press 'y' to continue and 'n' to stop\n");
while (choice == 'y') {
printf("Enter a word: ");
scanf("%s", word);
fprintf(fp, "%s ", word);
printf("Continue? (y/n): ");
scanf(" %c", &choice);
}
fclose(fp);
********** 10 **********
--- page 11 ---
fp = fopen("data.txt", "r");
if (fp == NULL) {
printf("File cannot be opened for reading!\n");
return 1;
}
while (fscanf(fp, "%s", word) == 1) {
length = strlen(word);
if (word[length - 1] == 'e' || word[length - 1] == 'E') {
count++;
}
}
fclose(fp);
printf("\nNumber of words ending with letter 'e': %d\n", count);
return 0;
}
Build a program that stores information for N players (player_id, name, runs,
CO-4 B   matches played) using an array of structures and displays all players who have   [10]
played more than 100 matches and scored more than 3000 runs.
BL-3   3 Marks - Declaring a structure and an array of size N
2 Marks - Accepting input
5 Marks - Displaying all players who have played more than 100 matches
and scored over 3000 runs.
#include <stdio.h>
struct Player {
int player_id;
char name[50];
int runs;
int matches;
};
int main() {
int N, i;
printf("Enter number of players: ");
scanf("%d", &N);
struct Player players[N];
for(i = 0; i < N; i++) {
printf("\nEnter details for Player %d\n", i + 1);
printf("Player ID: ");
scanf("%d", &players[i].player_id);
printf("Name: ");
scanf("%s", players[i].name);
printf("Total Runs: ");
scanf("%d", &players[i].runs);
printf("Matches Played: ");
scanf("%d", &players[i].matches);
}
printf("\nPlayers who played more than 100 matches and scored over 3000
runs:\n");
********** 11 **********
--- page 12 ---
for(i = 0; i < N; i++) {
if(players[i].matches > 100 && players[i].runs > 3000) {
printf("\nPlayer ID: %d", players[i].player_id);
printf("\nName: %s", players[i].name);
printf("\nTotal Runs: %d", players[i].runs);
printf("\nMatches Played: %d\n", players[i].matches);
}
}
return 0;
}
Q6
CO-3 A   Distinguish between inline functions and macro functions. Write a program   [10]
BL-3   that uses recursion to count the number of digits.
4 Marks – Difference
4 Marks - Recursive function definition to count the digits in a number
2 Marks - Input/output and function call from main( )
#include <stdio.h>
int countDigits(int n) {
if (n == 0)
return 0;
return 1 + countDigits(n / 10);
}
int main() {
int num;
printf("Enter a number: ");
scanf("%d", &num);
if (num == 0)
printf("Number of digits = 1\n");
********** 12 **********
--- page 13 ---
else
printf("Number of digits = %d\n", countDigits(num));
return 0;
}
CO-4 B   What is a pointer? Which operators are used with pointers? List the possible   [10]
BL-3   arithmetic operations that can be performed on pointers, and give a program
find the multiplication of two numbers using pointers.
5 Marks - Definition(1), Operators(2), List Operations(2)
5 Marks – Program to multiply two numbers using pointers.
Pointer - it’s a variable that stores the address of another variable
Ex
int a=10;
int * p = &a;
Operators
* - value at operator
& - address of operator
List of Operations:
Adding or subtracting an integer constant from a pointer
Ex. int *p=&a;
p = p+2
p = p-2
Incrementing and decrementing a pointer
Ex.
p++
--p
Subtracting two pointers
Ex. int *p1=&a, *p2=&b;
int diff = p1-p2
Pointer Assignment
Ex.
p1=p2
Program:
#include<stdio.h>
int main( ){
int n1=10,n2=20,n3;
int *p1,*p2,*p3;
p1=&n1;
p2=&n2;
p3=&n3;
*p3 = *p1 * *p2;
printf("%d",*p3);
return 0;
}
********** 13 **********
--- page 14 ---
Q7
CO-3 A   Implement a program to calculate the sum of the diagonal elements in a square   [10]
BL-3   matrix. Your program should read the order (m × n) of the matrix and the
elements from the user, display the matrix, and find and display the sum of
the diagonal elements.
1 Mark - Declaration of matrix and variables
3 Marks – Reading Matrix and displaying Matrix elements
5 Marks – Logic for finding the sum of diagonal elements
1 Mark - Proper printing of the upper triangular matrix
#include <stdio.h>
int main( ) {
int m,n, i, j, sum = 0;
int matrix[10][10];
printf("Enter the size of the square matrix: ");
scanf("%d%d",&m, &n);
printf("Enter the elements of the %dx%d matrix:\n", m, n);
for(i = 0; i < m; i++) {
for(j = 0; j < n; j++) {
scanf("%d", &matrix[i][j]);
}
}
if(m==n){
for(i = 0; i < m; i++) {
for(j = 0; j < n; j++) {
if(i == j) {
sum += matrix[i][j];
}
}
}
printf("Sum of diagonal elements: %d\n", sum);
}
else
printf(“Not a square matrix”);
}
CO-2 B   Develop a program to display the following pattern using a nested loop.   [10]
BL-3   5 4 3 2 1 1
4 3 2 1 0
3 2 1 1
2 1 0
1 1
0
1 Mark – Reading the number of lines
2 Mark – Outer for loop with appropriate condition (rows)
2 Mark – Inner for loop with appropriate condition (column)
1 Mark – if condition to print end of the line, either 1 or 0.
4 Mark – Printing the correct pattern
********** 14 **********
--- page 15 ---
#include<stdio.h>
int main( ){
int i,j,n;
scanf("%d",&n);
for(i=n;i>=0;i--){
for(j=i;j>=1;j--){
printf("%d",j);
}
i%2 ? printf("1"): printf("0");
printf("\n");
}
return 0;
}
X------------------------------------------------------------------------------------------------------------------ X
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper b216abe805d8

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_CyberSecurity_7010/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 372d4365f159

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_DS_7009/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper bc54d5ce9a50

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_EXTC_7006/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 266fd1a84e81

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_IT_7001/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA
Tech (Comp)/MBA Tech (DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output
#include <stdio.h>   [5]
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
********** 1 **********
--- page 2 ---
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");
scanf("%f", &pounds);   [5]
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration   [5]
2 Marks – Structure member access, input and output
********** 2 **********
--- page 3 ---
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);   [10]
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
found = 1;
}
}
if(found==0) {
printf("\n Not found");
********** 3 **********
--- page 4 ---
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper b4636b323f62

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_Mechanical_7003/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper ae9a559cfce9

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/BTech_Mechatronics_7004/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 092c97bca7e3

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MBATech_AI_7051/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper d45471ed282c

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MBATech_Computer_7047/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper d38a2ae517c0

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MBATech_DS_7052/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper d3e8139da151

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MBATech_IT_7041/COMPUTATIONAL THINKING FOR PROBLEM SOLVING/ANS_COMPUTATIONAL THINKING FOR PROBLEM SOLVING(702CO0C065)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech
(COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech
(DS)/MBA Tech (IT)
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTATIONAL THINKING FOR PROBLEM SOLVING
Date: 06 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Section A is compulsory.
3. Attempt any 4 questions from Section B.
4. In all 5 questions are to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. The figure on the right-hand side indicates full marks.
8. Assume suitable data if necessary.
Q1   Section A
A   1 Mark - Variable Declaration
2 Marks – Input and Correct Output
2 Marks – GST Amount and Net Price Calculation
#include <stdio.h>
int main() {
float originalCost, gstRate, gstAmount, netPrice;
printf("Enter the original cost of the item\n");
scanf("%f",&originalCost);   [5]
printf("Enter the GST rate\n");
scanf("%f",&gstRate);
gstAmount = (originalCost * gstRate) / 100;
netPrice = originalCost + gstAmount;
printf("\nGST Amount: %.2f", gstAmount);
printf("\nNet Price (Including GST): %.2f\n", netPrice);
return 0;
}
B   1 Marks - Variable Declaration
1 Mark- User Input
3 Marks – Decision Making and correct output   [5]
#include <stdio.h>
********** 1 **********
--- page 2 ---
int main() {
int fdgt;
printf("Enter the leading digit of the train number: ");
scanf("%d", &fdgt);
switch (fdgt) {
case 0:
printf("Train Type: Special Trains\n");
break;
case 1:
case 2:
printf("Train Type: Long-Distance Trains\n");
break;
case 3:
case 4:
case 9:
printf("Train Type: Suburban Railway\n");
break;
case 5:
printf("Train Type: Passenger\n");
break;
case 6:
printf("Train Type: MEMU (Mainline Electric Multiple Unit)\n");
break;
case 7:
printf("Train Type: Diesel Multiple Units and Railcars\n");
break;
case 8:
printf("Train Type: Suvidha Express\n");
break;
default:
printf("Invalid input\n");
}
return 0;
}
C   3 Marks – function definition & correct logic
1 Mark – function call from main()
1 Mark – Output display
#include <stdio.h>
float currencyConverter(float pounds);
int main( ) {
float pounds, rupees;
printf("Enter amount in Pounds:");   [5]
scanf("%f", &pounds);
rupees = currencyConverter(pounds);
printf("\nAmount in Indian Rupees: %.2f\n", rupees);
return 0;
}
float currencyConverter(float pounds) {
float rupees;
rupees = pounds * 100;
return rupees;
********** 2 **********
--- page 3 ---
}
D   2 Marks – Structure definition
1 Mark – Product variable declaration
2 Marks – Structure member access, input and output
#include <stdio.h>
struct Book {
int id;
char name[50];
float price;
};
int main() {
struct Book b;
printf("Enter Book ID: ");
scanf("%d", &b.id);   [5]
printf("Enter Book Name: ");
scanf("%s", b.name);
printf("Enter Book Price: ");
scanf("%f", &b.price);
printf("\n--- Book Details ---\n");
printf("Book ID: %d\n", b.id);
printf("Book Name: %s\n", b.name);
printf("Book Price: ₹%f\n", b.price);
return 0;
}
Q2 A   1 Mark - Declaration of array and variables
2 Marks - Reading array size, elements and key to search from the user
5 Marks - Linear search logic
2 Marks - Printing the correct output position or "Not found"
#include <stdio.h>
int main() {
int n, i, key, found = 0;
int arr[100];
printf("Enter the number of elements: ");
scanf("%d", &n);   [10]
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
printf("Enter the element to search: ");
scanf("%d", &key);
printf("Element %d found at positions: ", key);
for(i = 0; i < n; i++) {
if(arr[i] == key) {
printf("%d ", i );
********** 3 **********
--- page 4 ---
found = 1;
}
}
if(found==0) {
printf("\n Not found");
}
}
B   5 Marks – Steps in problem solving & explaining any two steps
5 Marks - Flowchart – (Terminal, I/O -2 marks and Conditional checking – 03 marks)
Computational Thinking (CT) is a problem-solving process that involves:
1. Decomposition - Breaking down problems
2. Pattern Recognition - Identifying patterns
3. Abstraction - Abstracting important details
4. Algorithm Design - Designing step-by-step solutions
5. Implementation – Use tools or programming to implement
Example: Find the Largest of Two Numbers
1. Decomposition
•   Input two numbers.
• Compare them using conditional logic.
•   Display the larger number.
[10]
2. Pattern Recognition
• Use if-else or conditional (? :) operators.
• Same logic applies to: smallest of two, largest of three, etc.
3. Abstraction
• Focus on comparison operation.
• We just need two numbers and one comparison.
4. Algorithmic Thinking
1. Start
2. Input a,b
3. If a > b, print a ‘is largest’
4. Else, print b ‘is largest’
5. End
********** 4 **********
--- page 5 ---
Q3 A   2 Marks – Opening the file with the appropriate file opening mode.
5 Marks – input the search word and searching in file
3 Marks – displaying the count and closing the file
#include <stdio.h>
#include <string.h>
int main() {
FILE *fp;
char word[50], temp[200];
int count = 0;   [10]
fp = fopen("input.txt", "r");
if (fp == NULL) {
printf("Error: File not found.\n");
return 1;
}
printf("Enter word to search: ");
scanf("%s", word);
while (fscanf(fp, "%s", temp) != EOF) {
if (strcmp(temp, word) == 0)
count++;
********** 5 **********
--- page 6 ---
}
if (count == 0)
printf("Word '%s' not found in file.\n", word);
else
printf("Word '%s' found %d time(s) in file.\n", word, count);
fclose(fp);
return 0;
}
B   2 Marks – Character array declaration and input
3 Marks – Using appropriate functions to check for palindrome
#include<stdio.h>
int main(){
char S[20],R[20];
puts("Enter String");
gets(S);
strupr(S);   [5]
strcpy(R,S);
strrev(R);
if(strcmp(S,R)==0)
printf("Its Palindrome");
else
printf("Its not Palindrome");
}
C   2 Marks – Conditional operator
3 Marsk - Logical operators
Conditional Operator
- The Conditional Operator is the only ternary operator in C.
-   The ternary operator takes three operands (condition, expression1 and
expression2). Hence, the name ternary operator.
- The syntax of the ternary operator is:
testCondition? expression1 : expression 2;
[5]
The testCondition is a boolean expression that results in either true or false. If the
condition is
•   true - expression1 (before the colon) is executed
•   false - expression2 (after the colon) is executed
Example:
(num % 2 == 0) ? printf("The number is Even.\n")
: printf("The number is Odd.\n");
********** 6 **********
--- page 7 ---
Logical Operators
- An expression containing a logical operator returns either 0 or 1 depending
upon whether the expression results in true or false.
-   Logical operators are commonly used in decision-making in C
programming.
Operator   Meaning   Example
Logical AND. True   If c = 5 and d = 2 then,
&&   only if all operands   expression ((c==5) &&
are true   (d>5)) equals to 0.
Logical OR. True   If c = 5 and d = 2 then,
||   only if either one   expression ((c==5) ||
operand is true   (d>5)) equals to 1.
Logical NOT. True
If c = 5 then, expression
!   only if the operand
!(c==5) equals to 0.
is 0
A   3 Marks – Difference (3-4 differences)
4 Marks – Function Definition and Logic
2 Marks – passing arrays and its size to a function from main( )
1 Mark – displaying output
Aspect   Library Function   User-Defined
Function
Definition   Predefined in C   Written by
libraries   programmer
Example   printf(), scanf(), sqrt()   areaCircle(), sum()
Q4   Source   <stdio.h>, <math.h>   Defined in source
etc.   code   [10]
Reusability   Limited to provided   Fully customizable
functionality
#include <stdio.h>
float average(int arr[5], int n) {
int sum = 0;
for (int i = 0; i < n; i++)
sum += arr[i];
return (float)sum / n;
}
int main() {
int a[5] = {10, 20, 30, 40, 50};
printf("Average = %.2f", average(a, 5));
********** 7 **********
--- page 8 ---
return 0;
}
B   2 Marks – Syntax
2 Marks – Flowchart
3 Marks – Input and any loop
3 Marks - Condition for factor and displaying it
Syntax:-
initlialization;
while(condition){
//loop body
update_expression;
}
[10]
#include<stdio.h>
int main(){
int i,n;
printf("Enter a number\n");
scanf("%d",&n);
printf("The factors of %d are:",n);
for(i=1;i<=n;i++)
if(n%i==0)
printf(" %d ",i);
return 0;
}
A   2 Marks – Opening & closing the file
4 Marks – Read Operation
4 Marks – Write operation
#include <stdio.h>
struct Emp {
Q5   int id;
char name[30];   [10]
float sal;
};
int main() {
FILE *fp;
struct Emp e;
int choice, n;
printf("1.Write 2.Read : ");
********** 8 **********
--- page 9 ---
scanf("%d", &choice);
if (choice == 1) {
fp = fopen("employee.dat", "wb");
printf("How many employees? ");
scanf("%d", &n);
for (int i=0; i<n; i++) {
printf("Enter ID, Name, Salary: ");
scanf("%d %s %f", &e.id, e.name, &e.sal);
fwrite(&e, sizeof(e), 1, fp);
}
printf("Records saved.\n");
}
else if (choice == 2) {
fp = fopen("employee.dat", "rb");
printf("Employee Details:\n");
while (fread(&e, sizeof(e), 1, fp))
printf("%d %s %.2f\n", e.id, e.name, e.sal);
}
fclose(fp);
return 0;
}
B   3 Marks - Declaring structure and array
2 Marks - Accepting input
5 Marks - Displaying names
#include <stdio.h>
#define SIZE 10
struct Bank {
int acc_no;
char name[50];
float balance;
};
int main() {
struct Bank customers[SIZE];
int i, count = 0;
[10]
printf("Enter details of %d customers:\n", SIZE);
for(i = 0; i < SIZE; i++) {
printf("\nCustomer %d:\n", i + 1);
printf("Enter Account Number: ");
scanf("%d", &customers[i].acc_no);
printf("Enter Account Holder's Name: ");
scanf("%s", customers[i].name);
printf("Enter Balance: ");
scanf("%f", &customers[i].balance);
}
printf("\nCustomers having balance less than 5000:\n");
for(i = 0; i < SIZE; i++) {
if(customers[i].balance < 5000) {
********** 9 **********
--- page 10 ---
printf("%s\n", customers[i].name);
count++;
}
}
printf("\nTotal number of customers with balance less than 5000: %d\n", count);
return 0;
}
Q6 A   4 Marks - Macro definition & its call
4 Marks – Recursive function
2 Marks - Input and output
#include <stdio.h>
#define DISCOUNT(p) (p - (p * 0.05))
int factorial(int n) {
if(n == 0 || n == 1)
return 1;
else
return n * factorial(n - 1);
}
int main( ) {
float totalAmount, finalAmount;
int items;   [10]
printf("Enter total bill amount: ");
scanf("%f", &totalAmount);
printf("Enter number of items purchased: ");
scanf("%d", &items);
finalAmount = DISCOUNT(totalAmount);
int bonus = factorial(items);
printf("\n--- BILL SUMMARY ---\n");
printf("Original Amount: %.2f\n", totalAmount);
printf("Amount after 5%% discount: %.2f\n", finalAmount);
printf("Bonus reward (factorial of %d): %d\n", items, bonus);
return 0;
}
B   5 Marks – Sum using pointers
5 Marks - find the frequency of a character
I.   Addition Using pointers
#include <stdio.h>
int main() {
int a, b, sum;   [10]
int *p1, *p2;
p1 = &a;
p2 = &b;
printf("Enter first integer: ");
scanf("%d", p1);
********** 10 **********
--- page 11 ---
printf("Enter second integer: ");
scanf("%d", p2);
sum = *p1 + *p2;
printf("\nSum of %d and %d is: %d\n", *p1, *p2, sum);
return 0;
}
II.   Frequency of a Character
#include <stdio.h>
int main( ) {
char str[100], ch;
char *ptr;
int count = 0;
printf("Enter a string: ");
scanf("%s", str);
printf("Enter a character to find its frequency: ");
scanf(" %c", &ch);
ptr = str;
// Traverse string using pointer
while (*ptr != '\0') {
if (*ptr == ch) {
count++;
}
ptr++;
}
printf("\nFrequency of '%c' = %d\n", ch, count);
return 0;
}
A   1 Mark - Declaration of matrix and dimensions
2 Marks - Input of both matrices
5 Marks- Logic for subtraction
2 Marks - Proper printing of the resultant matrix
Q7
#include <stdio.h>   [10]
int main() {
int A[10][10], B[10][10], C[10][10];
int m, n, i, j;
printf("Enter number of rows and columns: ");
scanf("%d %d", &m, &n);
********** 11 **********
--- page 12 ---
printf("Enter elements of first matrix (A):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &A[i][j]);
printf("Enter elements of second matrix (B):\n");
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
scanf("%d", &B[i][j]);
// Subtract B from A
for (i = 0; i < m; i++)
for (j = 0; j < n; j++)
C[i][j] = A[i][j] - B[i][j];
printf("Resultant matrix after subtraction (A - B):\n");
for (i = 0; i < m; i++) {
for (j = 0; j < n; j++)
printf("%5d", C[i][j]);
printf("\n");
}
}
B   1 Mark – Reading the number of lines
2 Marks – Outer for loop (rows)
2 Marks – Inner for loop (spacing)
2 Marks – Inner for loop (column)
3 Marks – Printing the correct pattern
#include<stdio.h>
int main( )
{
int i,j,k,n;   [10]
printf(“Enter number of lines \n”);
scanf(“%d”,&n);
for(i=n;i>=1;i--){
for(k=n;k>=i;k--)
printf(" ");
for(j=i;j>=1;j--){
printf("%4c",'*');
}
printf("\n");
}
return 0;
}
********** 12 **********
````
