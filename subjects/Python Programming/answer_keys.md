# Python Programming: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 74ec18848df7

- Departments: Science (B.Sc)
- Programmes: Bachelor of Science(Computer Science) - 40721
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/Bachelor of Commerce(Economics & Analytics) - 45617/Principles Of Macroeconomics/Re-Exam/Bachelor of Science(Computer Science) - 40721/Python Programming/ANS_Re-Exam_Python Programming(MSDS101)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 23 Jan 2026
- Text: text (12 pages)

````text
Synoptic
SVKM
Mithibai College (Arts, Sci & Comm)
Programme: B.Sc./B.Sc. (CS)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Python Programming
Date: 23 Jan 2026   Time: 11:00 am - 01:00 pm (02:00 Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 12 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
1.   Attempt any 4(Attempt Any 4 Questions)   20
A. Logical Operators in Python   5
Logical operators are used to combine conditional statements. In Python, there are three logical
operators:
and: Returns True if both conditions are true.
or: Returns True if at least one condition is true.
not: Reverses the logical state. If a condition is True, it becomes False, and vice versa.
Examples of Logical Operators:
1. and Operator:
python
x = 5
y = 10
z = 15
print(x < y and y < z) # Output: True (since 5 < 10 and 10 < 15)
Page 1 of 12
--- page 2 ---
2. or Operator:
python
x = 5
y = 10
print(x > y or x == 5) # Output: True (since x == 5 is True even though x > y is False)
3. not Operator:
python
x = 10
print(not x == 10) # Output: False (since x == 10 is True, not operator makes it False)
2. Identity Operators in Python
Identity operators are used to compare the memory locations of two objects. In Python, there
are two identity operators:
is: Returns True if two variables point to the same object in memory.
is not: Returns True if two variables point to different objects in memory.
Examples of Identity Operators:
1. is Operator:
python
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z) # Output: True (x and z refer to the same object in memory)
print(x is y) # Output: False (x and y refer to different objects even though they have the same
content)
2. is not Operator:
python
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y) # Output: True (x and y refer to different objects)
Page 2 of 12
--- page 3 ---
Differences Between == and is
== compares the values of two objects.
is compares whether two references point to the same object in memory.
Example:
python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # Output: True (values are the same)
print(x is y) # Output: False (they are different objects in memory)
Example: Combining Logical and Identity Operators
python
x = [10, 20, 30]
y = x
z = [10, 20, 30]
if x is y and x == z:
print("x and y are the same object, and x equals z.")
else:
print("x and y are different objects, or x does not equal z.")
Output:
csharp
x and y are the same object, and x equals z.
B. #### 1. upper():   5
Converts all characters in the string to uppercase.
```python
my_str = "hello"
print(my_str.upper()) # Output: "HELLO"
```
#### 2. lower():
Converts all characters in the string to lowercase.
```python
my_str = "HELLO"
Page 3 of 12
--- page 4 ---
print(my_str.lower()) # Output: "hello"
```
#### 3. find():
Searches for a substring in the string and returns the index of the first occurrence. Returns
`-1` if the substring is not found.
```python
my_str = "Hello World"
print(my_str.find("World")) # Output: 6
```
#### 4. replace():
Replaces all occurrences of a substring with another substring.
```python
my_str = "Hello World"
print(my_str.replace("World", "Python")) # Output: "Hello Python"
```
#### 5. count():
Counts the number of occurrences of a substring in the string.
```python
my_str = "Hello World World"
print(my_str.count("World")) # Output: 2
```
C. For Loop in Python   5
A for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range)
and execute a block of code for each item in the sequence. The for loop simplifies the process
of iterating through items without the need to manually manage a counter or index, as you
might in some other programming languages.
Syntax of the For Loop:
python
for variable in sequence:
# Code block to execute for each element
·   variable: This is the loop control variable that takes the value of each element in the
sequence, one at a time.
Page 4 of 12
--- page 5 ---
·   sequence: This can be a list, tuple, string, or any iterable (like a range).
·   The code inside the loop is executed once for each element in the sequence.
How the For Loop Works:
1.   Python retrieves the first item from the sequence and assigns it to the variable.
2. The code block inside the for loop is executed.
3.   Python retrieves the next item, assigns it to the variable, and repeats the process until all
items in the sequence have been processed.
Example 1: Iterating Over a List
python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)
Output:
apple
banana
cherry
In this example:
·   The for loop iterates over each element in the list fruits.
·   For each iteration, the variable fruit takes on the value of the current element in the list,
and the print() function outputs that value.
D. # Taking the Fahrenheit temperature as input from the user   5
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# Converting Fahrenheit to Celsius using the formula C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * (5/9)
# Displaying the result with two decimal places
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
Explanation:
Input:
The program prompts the user to enter the temperature in Fahrenheit. The input is cast to a
float to allow for decimal numbers.
Page 5 of 12
--- page 6 ---
Formula:
The formula C=(F−32)×(59)C = (F - 32) \times \left(\frac{5}{9}\right)This program accurately
converts a temperature from Fahrenheit to Celsius, ensuring the input is a floating-point
number and that the result is displayed with proper formatting.
E. # Multiplication table up to 10 x 10   5
for i in range(1, 11):   # Outer loop for rows
for j in range(1, 11):   # Inner loop for columns
print(i * j, end="\t") # Print product
print()   # Move to next line
The outer loop runs from 1 to 10 → 10 iterations .
For each iteration of the outer loop, the inner loop runs 10 times.
So total steps for printing values = 10 × 10 = 100 steps .
Additionally, there are 10 steps for printing new lines (one after each row).
Total = 110 print operations .
In short, the program takes 100 steps to compute products + 10 steps for formatting = 110
steps .
2.   Attempt any 4(Attempt Any 4 Questions)   20
A. How lists are created/initialized; mutability & indexing   5
Creating/initializing
Literal: nums = [1, 2, 3], mixed = [1, "a", 3.5]
Empty list: empty = []
From iterable: list("abc") # ['a','b','c']
Comprehension: [x*x for x in range(4)] # [0,1,4,9]
Repetition: [0] * 5 # [0,0,0,0,0] (note: inner lists get shared if you repeat lists)
Nested: grid = [[0, 1], [2, 3]]
Mutability
Lists are mutable: you can change elements, grow/shrink.
Page 6 of 12
--- page 7 ---
a = [10, 20, 30]
a[1] = 99   # [10, 99, 30]
a.append(40)   # [10, 99, 30, 40]
Indexing & slicing
Zero-based: a[0] first element; negative: a[-1] last element.
Slicing (non-inclusive end): a[1:3], a[:2], a[::2].
Out-of-range indexing raises IndexError; out-of-range slices are safe and just trim.
B. Both pop()   5
o It removes the last inserted key-value pair (LIFO order in Python 3.7+).
o It returns the removed key-value pair as a tuple.
·   When to use it: When you want to remove any item from the dictionary, typically when
the order doesn't matter, or you want to process items in LIFO order.
Example:
Python
student = {"name": "Alice", "age": 25, "major": "Computer Science"}
item = student.popitem() # Removes and returns ('major', 'Computer Science')
print(item) # Output: ('major', 'Computer Science')
print(student) # Output: {'name': 'Alice', 'age': 25}
Key Differences and Use Cases
Feature   pop(key)   popitem()
Key Required   Yes   No
Item
Specific key-value pair   Arbitrary (last inserted)
Removed
Value of the removed   Tuple (key, value) of the removed
Return Value
item   item
Removing any item, LIFO
Use Cases   Removing a known item
processing
Page 7 of 12
--- page 8 ---
Choose the method that best suits your needs based on whether you need to remove a specific
item or any arbitrary item.
C. Functions are essential building blocks in Python (and programming in general). They provide   5
a way to organize your code, making it more efficient, readable, and maintainable. Here are the
key advantages:
1. Code Reusability
·   Avoid Repetition: Instead of writing the same code multiple times, you can encapsulate it
within a function and call that function whenever needed. This eliminates redundancy and
saves you time and effort.
·   Example: Imagine you need to calculate the area of a circle at different points in your
program. Instead of writing the area calculation code each time, you can create a function
calculate_area(radius) and call it with different radius values.
2. Modularity
·   Breaking Down Complexity: Functions allow you to decompose a complex problem
into smaller, more manageable subproblems. Each function focuses on a specific task, making
your code easier to understand and reason about.
·   Example: If you're building a game, you might have separate functions for handling user
input, updating game state, rendering graphics, and playing sounds.
3. Improved Readability
·   Clearer Structure: Functions give your code a logical structure, making it easier to
follow the flow of execution. Well-named functions act like self-documenting code, improving
readability.
·   Example: A function named validate_email(email) clearly indicates its purpose, making
your code more understandable.
4. Maintainability
·   Easier Debugging and Updates: If you need to fix a bug or make a change, you only
need to modify the code within the relevant function. This reduces the risk of introducing
errors in other parts of your program.
·   Example: If you need to change the way you calculate the area of a circle, you only need
to update the calculate_area() function.
5. Abstraction
·   Hiding Complexity: Functions hide the implementation details, allowing you to use them
without needing to know exactly how they work internally.
·   Example: You can use the built-in print() function without understanding the low-level
details of how it sends output to your console.
How Functions Promote Reusability and Modularity
Page 8 of 12
--- page 9 ---
·   Reusability: By encapsulating a block of code, functions allow you to reuse that code
throughout your program or even in other projects. This is like having a pre-built tool you can
use whenever you need it.
·   Modularity: Functions break down your program into independent modules (functions),
each responsible for a specific task. This modular design makes it easier to develop, test, and
maintain your code, as you can work on each function separately.
In essence, functions are key to writing clean, efficient, and well-organized Python code.
D. # Creating a list of integers   5
my_list = [1, 2, 3, 4, 5]
# Appending a new integer to the list
my_list.append(6)
print("After appending:", my_list)
# Extending the list with another list of integers
my_list.extend([7, 8, 9])
print("After extending:", my_list)
E. # Creating an empty dictionary   5
my_dict = {}
# Adding key-value pairs using the assignment operator
my_dict['name'] = 'Alice'
my_dict['age'] = 25
my_dict['city'] = 'New York'
# Retrieving all keys using the keys() method
keys = my_dict.keys()
print("Keys:", keys)
# Retrieving all values using the values() method
values = my_dict.values()
print("Values:", values)
3.   (Attempt Any 4 Questions)   20
A. The else block completes successfully, without any exceptions.   5
Page 9 of 12
--- page 10 ---
·   Avoiding Unintended Catching: Prevents the except block from accidentally catching
exceptions that might be raised by the code in the else block.
By incorporating the else clause into your exception handling, you can create more robust and
precise error-handling logic in your Python programs.
B. These are all shorthand character classes in regular expressions, providing convenient ways to   5
match common types of characters:
·   \d
o Matches: Any digit (0-9).
o Example: \d\d\d-\d\d\d\d would match basic email address patterns like "[email address
removed]".
·   \s
o Matches: Any whitespace character. This includes:
§ Space
§ Tab (\t)
§ Newline (\n)
§ Carriage return (\r)
§ Form feed (\f)
§ Vertical tab (\v)
o Example: Hello\s+worldThese shorthand character classes are fundamental building blocks
in regular expressions, allowing you to create more concise and readable patterns for various
text-processing tasks.
C. Steps to Connect Python to MySQL Database   5
1.   Install the MySQL Connector: First, you need to install the mysql-connector-python
package. You can install it using pip:
bash
pip install mysql-connector-python
4.   Execute SQL Queries: You can execute SQL queries like SELECT, INSERT, UPDATE,
and DELETE using the cursor object.
for in rows: nbsp print row Step 5: and cursor connection close br Explanation of the Example:
b h3 p style="margin-top:12.0pt; margin-bottom:12.0pt;margin-left:36.0pt;text-indent:-18.0pt"
span new="" serif mso-fareast-font-family: times="" roman mso-ansi-language:en-us>1.
Establish the Connection:
a.   The cursor() method creates a cursor object, which is used to execute SQL queries.
Page 10 of 12
--- page 11 ---
4.   Fetch the Data:
a.   Always close the cursor and connection when done to free up resources.
D. Handling Exceptions During Database Connectivity in Python   5
When connecting to a database in Python, various errors (like connection failures, query issues,
or invalid data) can occur. Exception handling ensures that the program can gracefully deal
with these errors rather than crashing unexpectedly.
How to Handle Exceptions:
In Python, exceptions can be handled using try-except blocks. Here's a general approach for
handling exceptions during database connectivity:
b.   If any error occurs, it is caught by the except3. Always Close Resources in finally
Block
style="font-size:12.0pt;line-height:107%;font-family:Consolas" nbsp host='localhost'
user='username' password='password' database='database_name' span>
)
# Creating a cursor and executing a query
cursor = connection.cursor()
cursor.execute("SELECT * FROM table_name")
results = cursor.fetchall()
print(results)
except Error as e:
print(f"Error occurred: {e}")
finally:
# Ensuring resources are closed
if cursor:
cursor.close()
if connection:
connection.close()
Importance of Exception Handling:
1.   Prevents Program Crashes: Without handling exceptions, the program may crash
unexpectedly when an error occurs.
2.   Graceful Error Reporting: It allows you to report errors meaningfully, helping in
debugging or informing the user about the issue.
3.   Resource Management: Ensures that resources like database connections are properly
closed, avoiding potential memory leaks or locks in the database.
Page 11 of 12
--- page 12 ---
4. Improves Robustness: Exception handling makes the application more reliable and
capable of handling unexpected scenarios gracefully.
E. import re   5
# Function to check if the string contains only digits
def check_only_digits(string):
if re.fullmatch(r"\d+", string):
print("The string contains only digits.")
else:
print("The string contains non-digit characters.")
# Taking user input and calling the function
input_string = input("Enter a string: ")
check_only_digits(input_string)
Page 12 of 12
````
