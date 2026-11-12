# Advanced Data Analysis and Programming: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper bef6387750b4

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Advanced Data Analysis and Programming/ANS_Advanced Data Analysis and Programming(703DB0C055)_2025-2026.docx`
- Text: docx (1 page)

````text
Q1

|
| Answer briefly:
| [20]
|

CO-1; SO-1;
BL-2
| a.
|
Write a brief explanation of Simple API, REST API, and HTTP API. Mention one key feature or use case of each.

ANS:
1. Simple API
A Simple API provides basic communication between software components, usually without following strict architectural rules. It allows one application to access data or functions of another using simple request–response mechanisms.
Use Case:
Easy to implement for small-scale or internal applications where complex features (like authentication or statelessness) are not required.
2. REST API (Representational State Transfer API)
A REST API is a web-based API that follows the REST architecture, using standard HTTP methods (GET, POST, PUT, DELETE) for communication. It is stateless, meaning each request is independent and self-contained.
Use Case:
Ideal for web and mobile applications — for example, fetching data from a database using a GET request or updating records with PUT.
3. HTTP API
An HTTP API uses the HTTP protocol as its communication standard, allowing data to be exchanged between clients and servers using URLs and methods like GET, POST, and DELETE.
Use Case:
Commonly used in cloud services and web applications to connect systems over the internet (e.g., APIs for payment gateways or social media integrations).

| [05]

02

1.5

1.5
|

CO-2; SO-1; BL-2,3
| b.
| For the given DataFrame:

df = pd.DataFrame({ 'Employee': ['E1', 'E2', 'E3'], 'Score': [88, 92, 85]})

Convert Score to float type using astype().
Rank the scores in ascending order and add a new column Rank.
ANS:

Output:

| [05]

2.5

2.5
|

CO-3; SO-1;
BL-3
| c.
| Explain the difference between a List and a Map in Scala. Write a small example showing each and highlight one key difference.

ANS:
Difference Between List and Map in Scala:
Feature
| List
| Map
|
Structure
| Ordered collection of elements
| Collection of key-value pairs
|
Element Access
| Accessed by index
| Accessed by key
|
Duplicates
| Allows duplicate elements
| Keys must be unique
|
Immutability
| Default List is immutable
| Default Map is immutable
|

Scala Example:
object ListMapDemo extends App {

// List example
val fruits = List("Apple", "Banana", "Apple")
println(s"List: $fruits")
println(s"First element: ${fruits(0)}") // Access by index

// Map example
val fruitPrices = Map("Apple" -> 100, "Banana" -> 50)
println(s"Map: $fruitPrices")
println(s"Price of Apple: ${fruitPrices("Apple")}") // Access by key

// Key difference highlighted
println("List allows duplicates, Map keys are unique.")
}
Output:
List: List(Apple, Banana, Apple)
First element: Apple
Map: Map(Apple -> 100, Banana -> 50)
Price of Apple: 100
List allows duplicates, Map keys are unique.
Difference:
List is an ordered collection accessed by index and allows duplicates.
Map is a collection of key-value pairs, accessed by key, and keys must be unique.
| [05]

02

03
|

CO-4; SO-1;
BL-2

| d.
|
Explain the concept of RDD (Resilient Distributed Dataset) in Apache Spark. Write its important features and advantages over traditional data structures.

ANS:
Concept of RDD (Resilient Distributed Dataset):
An RDD is the fundamental data structure in Apache Spark.
It is a distributed collection of elements that can be processed in parallel across a cluster.
RDDs are immutable, fault-tolerant, and support lazy transformations.
Important Features of RDDs:
Immutable: Once created, the data cannot be changed.
Distributed: Data is split across multiple nodes in a cluster.
Fault-tolerant: Can recover lost data using lineage information.
Lazy evaluation: Transformations are only computed when an action is called.
Parallel processing: Supports distributed computations for big data.
Advantages over Traditional Data Structures:
Scalability: Can handle large datasets across clusters, unlike local arrays or lists.
Performance: In-memory computation reduces disk I/O compared to traditional storage.
Fault Tolerance: Automatically recovers from node failures.
Support for Big Data Operations: Enables transformations and actions on large datasets efficiently.

| [05]

02

1.5

1.5
|

|
Q2
CO-1; SO-1;
BL-2
| a.
| Write a Python program to demonstrate data structures - List and Dictionary.
Create each with sample elements. Perform at least five operations on each. Print their outputs.

ANS:

Explanation:
List: Ordered, mutable collection supporting indexing, insertion, removal, and sorting.
Dictionary: Unordered, mutable key-value structure allowing dynamic data manipulation.
Python Program: Demonstrating List and Dictionary Operations
#   List Operations
print(" List Operations ")
# Creating a list
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# 1. Access an element
print("First fruit:", fruits[0])

# 2. Add an element
fruits.append("Orange")

# 3. Insert at a specific position
fruits.insert(2, "Grapes")

# 4. Remove an element
fruits.remove("Banana")

# 5. Sort the list
fruits.sort()

print("Updated List:", fruits)

#   Dictionary Operations
print("\n Dictionary Operations ")
# Creating a dictionary
student = {"Name": "Amit", "Age": 20, "Course": "Python"}

# 1. Access a value
print("Student Name:", student["Name"])

# 2. Add a new key-value pair
student["Grade"] = "A"

# 3. Update an existing key
student["Age"] = 21

# 4. Delete a key-value pair
student.pop("Course")

# 5. Display all items
print("All Items:", student.items())

print("Updated Dictionary:", student)

Output:
List Operations
First fruit: Apple
Updated List: ['Apple', 'Cherry', 'Grapes', 'Mango', 'Orange']

Dictionary Operations
Student Name: Amit
All Items: dict_items([('Name', 'Amit'), ('Age', 21), ('Grade', 'A')])
Updated Dictionary: {'Name': 'Amit', 'Age': 21, 'Grade': 'A'}

| [10]

05x2

|
Q2
CO-2; SO-1;
BL-3

| b.
| Write a Python program to demonstrate the difference between the apply() and map() functions in Pandas. For the given snippet, show how each function works, and display the outputs for comparison.

ANS:

import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3, 4, 5])

# Using map()
result_map = s.map(lambda x: x * 10)
print("Output using map():")
print(result_map)

# Using apply()
result_apply = s.apply(lambda x: x + 5)
print("\nOutput using apply():")
print(result_apply)

map():   element-wise transformation on a Series.
apply():   can be used on Series or DataFrame, can apply row/column functions.
1. map() Function
map() is used only with Pandas Series
It applies a function element-wise
It is commonly used for simple transformations or value mapping
In this example:
s.map(lambda x: x * 10)
Each element of the Series is multiplied by 10.
Result:
[1, 2, 3, 4, 5] → [10, 20, 30, 40, 50]

2. apply() Function
apply() can be used on both Series and DataFrames
It is more flexible than map()
It can apply complex functions row-wise or column-wise (for DataFrames)
In this example:
s.apply(lambda x: x + 5)
Each element of the Series is increased by 5.
Result:
[1, 2, 3, 4, 5] → [6, 7, 8, 9, 10]
Differences Between map() and apply()
Feature
| map()
| apply()
|
Works on
| Series only
| Series & DataFrame
|
Use case
| Simple element-wise mapping
| Complex transformations
|
Flexibility
| Less
| More
|
Performance
| Faster for simple tasks
| Slightly slower
|
OR

| [10]

02

2x03

02
|

|
Q3
CO-2; SO-1;
BL-3
| a.
| Create a DataFrame with the given data and perform:
Department
| Employee
| Salary
| Experience
|
HR
| E1
| 40000
| 2
|
HR
| E2
| 45000
| 3
|
IT
| E3
| 60000
| 5
|
IT
| E4
| 65000
| 6
|
Finance
| E5
| 70000
| 7
|
Finance
| E6
| 72000
| 8
|
IT
| E7
| 68000
| 4
|

Group by Department and calculate:

Total Salary and Average Experience
Create a bar plot of total Salary per department using Matplotlib or Seaborn.
Highlight departments with total Salary > 130000 in a different color.

ANS:

Answer:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create DataFrame
data = {
'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'IT'],
'Employee': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
'Salary': [40000, 45000, 60000, 65000, 70000, 72000, 68000],
'Experience': [2, 3, 5, 6, 7, 8, 4]
}

df = pd.DataFrame(data)

# i. Group by Department and calculate Total Salary and Average Experience
grouped = df.groupby('Department').agg({'Salary': 'sum', 'Experience': 'mean'}).reset_index()
grouped.rename(columns={'Salary': 'Total_Salary', 'Experience': 'Avg_Experience'}, inplace=True)

print("Grouped Data:")
print(grouped)

# ii. Create a bar plot of total Salary per department
plt.figure(figsize=(8, 5))

# Highlight departments with Total_Salary > 130000
colors = ['orange' if x > 130000 else 'skyblue' for x in grouped['Total_Salary']]

sns.barplot(x='Department', y='Total_Salary', data=grouped, palette=colors)

# Add labels and title
plt.title('Total Salary per Department')
plt.xlabel('Department')
plt.ylabel('Total Salary')

# Show the bar values
for index, value in enumerate(grouped['Total_Salary']):
plt.text(index, value + 2000, str(value), ha='center')

plt.show()

Explanation:
Grouping:
groupby('Department').agg({'Salary':'sum','Experience':'mean'})
→ Aggregates total salary and average experience per department.
Bar Plot:
Uses Seaborn’s barplot to visualize total salary per department.
Highlighting:
The colors list assigns 'orange' to departments where total salary > 130000, and 'skyblue' otherwise.
Output Summary:
Department
| Total_Salary
| Avg_Experience
|
Finance
| 142000
| 7.5
|
HR
| 85000
| 2.5
|
IT
| 193000
| 5.0
|
Finance and IT bars appear orange (since total salary > 130000).
HR bar remains sky blue.

| [10]

02

02

04

02

|
Q3
CO-1; SO-1; BL-5
| b.
| Design and implement a Python GUI using Tkinter with the following features:
Use Checkbuttons to allow users to select their preferred hobbies (e.g., Reading, Painting, Music).
Use Radiobuttons to allow users to select their favorite travel mode (Car, Train, Flight).
Display the user’s selections dynamically within the GUI.
Explain the working of your GUI code in detail and justify the choice of using Checkbuttons for multiple selections and Radiobuttons for single selection.

ANS:

Python GUI Implementation using Tkinter
import tkinter as tk

def show_selection():
selected_hobbies = []
for hobby, var in hobbies_vars.items():
if var.get():
selected_hobbies.append(hobby)
selected_travel_mode = travel_var.get()

result_label.config(text=f"Hobbies: {', '.join(selected_hobbies)}\nTravel Mode: {selected_travel_mode}")

# Create main window
root = tk.Tk()
root.title("User Preferences")

# Hobbies using Checkbuttons
hobbies_vars = {
"Reading": tk.BooleanVar(),
"Painting": tk.BooleanVar(),
"Music": tk.BooleanVar()
}

tk.Label(root, text="Select your hobbies:").pack()
for hobby, var in hobbies_vars.items():
tk.Checkbutton(root, text=hobby, variable=var, command=show_selection).pack(anchor='w')

# Output Figure

# Travel mode using Radiobuttons
tk.Label(root, text="Select your favorite travel mode:").pack()
travel_var = tk.StringVar(value="Car")   # Default selection

for mode in ["Car", "Train", "Flight"]:
tk.Radiobutton(root, text=mode, variable=travel_var, value=mode, command=show_selection).pack(anchor='w')

# Label to display selections dynamically
result_label = tk.Label(root, text="Hobbies: \nTravel Mode: ")
result_label.pack(pady=10)

root.mainloop()

# Output Figure

Any MODE will work

Working Explanation
Checkbuttons for Hobbies
Each hobby has a BooleanVar() associated with it.
Users can select multiple hobbies simultaneously.
The command=show_selection updates the displayed selection dynamically.
Radiobuttons for Travel Mode
Only one option can be selected at a time, enforced by sharing a single StringVar().
Dynamic update occurs on selection, showing the chosen travel mode.
Dynamic Display
The show_selection() function collects all selected hobbies and the chosen travel mode, updating the Label widget in real-time.
Justification of Widget Choices
Checkbuttons: Ideal for multiple selections because each option can be independently checked or unchecked.
Radiobuttons: Ideal for single selection because all buttons share the same variable, ensuring only one option is active at a time.
|
[10]

04

04

02
|

|
Q4
CO-3; SO-1;
BL-5

| a.
| Write a Scala program with an abstract class Shape having a method area. Create subclasses Circle and Rectangle that override this method. Demonstrate field overriding and print areas for multiple objects.

ANS:
Scala Program: Abstract Class and Field Overriding
// Abstract class Shape
abstract class Shape {
def area: Double   // Abstract method
}

// Subclass Circle
class Circle(val radius: Double) extends Shape {
override def area: Double = Math.PI * radius * radius
}

// Subclass Rectangle
class Rectangle(val length: Double, val width: Double) extends Shape {
override def area: Double = length * width
}

// Demonstration
object ShapeDemo extends App {
val shapes: List[Shape] = List(
new Circle(5),
new Rectangle(4, 6),
new Circle(3),
new Rectangle(2, 8)
)

shapes.foreach {
case c: Circle   => println(s"Circle area (radius=${c.radius}): ${c.area}")
case r: Rectangle => println(s"Rectangle area (length=${r.length}, width=${r.width}): ${r.area}")
}
}

Output:   As per your choice of values and expalanation.
Explanation
1. Abstract Class Shape
Declared using abstract class
Contains:
An abstract method area()
A field name
Cannot be instantiated directly
2. Method Overriding
Both Circle and Rectangle override the area() method
override keyword ensures compile-time safety
3. Field Overriding
The name field in the parent class is overridden in subclasses
Demonstrates field overriding
4. Polymorphism
A List[Shape] holds objects of different subclasses
At runtime, the correct area() method is called based on the object type
OOP Concepts Demonstrated
Concept
| Explanation
|
Abstraction
| Shape defines common behavior
|
Inheritance
| Circle, Rectangle extend Shape
|
Method Overriding
| area() redefined in subclasses
|
Field Overriding
| name field overridden
|
Polymorphism
| Same reference type, different behavior
|

| [10]

07

03
|
Q4
CO-4; SO-1;
BL-3
| b.
| Describe the Apache Spark architecture with its main components. Draw a diagram showing how the Driver, Cluster Manager, Executors, and Tasks interact during the execution of a Spark job.

ANS:
Apache Spark Architecture Components:
1. Driver Program
The Driver is the central coordinator of a Spark application.
Responsibilities:
Converts user code into a Directed Acyclic Graph (DAG).
Splits the DAG into stages and tasks.
Schedules tasks on executors.
Collects results from executors.
Runs the SparkContext, which is the entry point of Spark.
2. Cluster Manager
Manages and allocates cluster resources.
Responsible for assigning CPU and memory to Spark applications.
Common cluster managers:
Standalone
YARN
Mesos
Kubernetes
3. Executors
Executors are worker processes launched on cluster nodes.
Responsibilities:
Execute tasks assigned by the Driver.
Cache data in memory or disk.
Return results back to the Driver.
Each Spark application has its own executors.
4. Tasks
A task is the smallest unit of execution in Spark.
Each task processes a partition of data.
Multiple tasks run in parallel on executors.
Spark Application
A Spark application consists of:
One Driver program
One or more Executors
Tasks executed on the data
Execution Flow of a Spark Job
User submits a Spark application.
The Driver requests resources from the Cluster Manager.
The Cluster Manager launches Executors on worker nodes.
The Driver creates a DAG and divides it into stages and tasks.
Tasks are sent to Executors for execution.
Executors process data and send results back to the Driver.
Final output is produced.
Apache Spark Architecture Diagram:

With Proper description in the Diagram.
| [10]

05

05

|

|
Q5
CO-4; SO-1;
BL-5
| a.
| Write a Spark Scala program that:
Creates an RDD of integers.
Applies a transformation (like map(x => x*2)).
Persists the transformed RDD in memory or on disk.
ANS:
Spark Scala Program to Persist an RDD
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.storage.StorageLevel

object RDDPersistenceBL5 {
def main(args: Array[String]): Unit = {

// Step 1: Spark configuration and context
val conf = new SparkConf().setAppName("RDD Persistence Example").setMaster("local[*]")
val sc = new SparkContext(conf)

// Step 2: Create an RDD of integers
val rdd = sc.parallelize(List(1, 2, 3, 4, 5))

// Step 3: Apply a transformation (map)
val transformedRDD = rdd.map(x => x * 2)

// Step 4: Persist the RDD in memory
transformedRDD.persist(StorageLevel.MEMORY_AND_DISK)

// Step 5: Perform multiple actions on the persisted RDD
println("Collect: " + transformedRDD.collect().mkString(", "))
println("Count: " + transformedRDD.count())
println("Take(3): " + transformedRDD.take(3).mkString(", "))

// Stop SparkContext
sc.stop()
}
}

# Different way of expiation is also correct.
Explanation & Analysis
RDD Persistence:
Stores the RDD in memory or disk to avoid recomputation when used multiple times.
Reduces execution time for iterative operations like machine learning algorithms.
Types of Persistence:
MEMORY_ONLY – Fast, stores in memory; recomputes lost partitions if memory is insufficient.
MEMORY_AND_DISK – Stores in memory, spills to disk if memory is full.
DISK_ONLY – Stores only on disk; slower but saves memory.
Serialized options (*_SER) – Save memory by storing compressed objects.
Why Useful:
Iterative Algorithms: Multiple actions (e.g., collect, count, take) don’t recompute the RDD each time.
Fault Tolerance: Spark can recover lost partitions from lineage or persisted disk copies.
Performance Optimization: Choice of storage level balances speed vs memory usage.
BL5 Analysis Aspect:
Choosing MEMORY_AND_DISK ensures faster in-memory access while avoiding recomputation if memory is insufficient.
Demonstrates understanding of performance trade-offs and efficient resource utilization in large-scale Spark applications.

| [10]

06

04
|
Q5
CO-1; SO-1;
BL-3
| b.
| Design a class structure for different types of vehicles (Car, Bike, Truck) using Polymorphism in Python.
Show how method overriding and method overloading (simulated) can be applied.
Write proper code.
ANS:

Python Code: Vehicle Class Structure with Polymorphism
# Base class
class Vehicle:
def __init__(self, brand, model):
self.brand = brand
self.model = model

def vehicle_info(self):
print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

# Simulated method overloading using default arguments
def start(self, speed=None):
if speed is not None:
print(f"{self.brand} {self.model} started at speed {speed} km/h")
else:
print(f"{self.brand} {self.model} started")

# Derived class Car
class Car(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Car Brand: {self.brand}, Model: {self.model}")

# Derived class Bike
class Bike(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Bike Brand: {self.brand}, Model: {self.model}")

# Derived class Truck
class Truck(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Truck Brand: {self.brand}, Model: {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
bike1 = Bike("Yamaha", "R15")
truck1 = Truck("Volvo", "FH16")

# Demonstrating method overriding
car1.vehicle_info()   # Car specific info
bike1.vehicle_info()   # Bike specific info
truck1.vehicle_info()   # Truck specific info

# Demonstrating simulated method overloading
car1.start()   # Default start
bike1.start(60)   # Start with speed
truck1.start(80)   # Start with speed

Explanation of method overriding and method overloading (simulated) can be applied.

| [10]

02

04

04

|

|
Q6
CO-3; SO-1;
BL-2,
| a.
| Write a Scala program to:
Create a Tuple with mixed data types.
Create a Set with unique elements.
Perform basic operations on each collection: add, remove, and access elements.
Display the final Tuple and Set
ANS:
Scala Program: Tuple and Set Operations
object TupleSetDemo extends App {

// i. Create a Tuple with mixed data types
val tup = ("Scala", 2025, true)
println(s"Initial Tuple: $tup")

// Access Tuple elements
println(s"First element: ${tup._1}")
println(s"Second element: ${tup._2}")
println(s"Third element: ${tup._3}")

// ii. Create a Set with unique elements
var set = Set(1, 2, 3, 4)
println(s"Initial Set: $set")

// iii. Basic operations
// Set operations (add and remove)
set += 5   // Add element
set -= 2   // Remove element

// Access element
println(s"Contains 3? ${set.contains(3)}")

// iv. Display final collections
println(s"Final Tuple (immutable): $tup")
println(s"Final Set: $set")
}
Explanation
1. Tuple Creation
A Tuple allows storing multiple values of different data types.
myTuple contains an Integer, String, Double, and Boolean.
Tuple elements are accessed using _1, _2, _3, _4.
2. Set Creation
A Set stores unique elements only.
Duplicate values are automatically removed.

3. Set Operations
Add element: +
Remove element: -
Access element: contains()
4. Display Output
The program prints the accessed elements, final tuple, and updated set.
Output:
Initial Tuple: (Scala,2025,true)
First element: Scala
Second element: 2025
Third element: true
Initial Set: Set(1, 2, 3, 4)
Contains 3? true
Final Tuple (immutable): (Scala,2025,true)
Final Set: Set(1, 3, 4, 5)

| [10]

06

04
|
Q6
CO-5; SO-1;
BL-4
| b.
| Discuss the impact of development convenience, debugging tools, and IDE support on improving a programmer’s productivity and ensuring long-term maintainability of code.

ANS: (Give the Example in detail)
Development convenience, debugging tools, and IDE support significantly enhance a programmer’s productivity and the maintainability of code over time.
Development Convenience:
Programming languages and frameworks with simple syntax, readable code structures, and built-in libraries allow developers to write code faster and with fewer errors.
Example: Python’s clear syntax and extensive libraries (e.g., NumPy, Pandas) enable rapid development and reduce boilerplate code.
Debugging Tools:
Debuggers, linters, and static analysers help identify errors early, reducing runtime bugs and improving code quality.
Example: IDEs like PyCharm or Visual Studio Code highlight syntax errors, potential logic issues, and runtime warnings instantly, saving time in testing and troubleshooting.
IDE Support:
Integrated Development Environments provide code completion, refactoring, version control, testing frameworks, and project management tools in one place.
This improves efficiency by reducing context switching and helps maintain consistent coding standards.
Example: Eclipse or IntelliJ IDEA supports large-scale projects with advanced debugging and collaboration features.
When development is convenient, debugging is efficient, and IDE support is robust, programmers can write high-quality code faster. This not only increases productivity but also ensures long-term maintainability, as the code is easier to understand, modify, and extend.
| [10]

03x3

01

|

|
Q7
CO-5; SO-1;
BL-4
| a.
| Explain how security considerations can influence the choice of a programming language and the design of an application. Give one example of a programming language that provides strong security features and explain why it is considered secure.

ANS: (Example of any Language will be considered)
Security considerations are critical when selecting a programming language and designing an application. Applications that handle sensitive data or operate in untrusted environments must minimize vulnerabilities, prevent exploits, and ensure reliability. The choice of language affects the types of security risks and how easily they can be mitigated.
1) Influence on Language Choice and Design
Memory Safety: Languages like Rust or Java prevent buffer overflows and dangling pointers.
Type Safety: Strong typing helps catch errors at compile time, reducing logical flaws.
Concurrency Safety: Safe concurrency prevents data races and related security issues.
Sandboxing & Runtime Checks: VM-based execution limits the impact of malicious code.
Library Ecosystem: Vetted libraries reduce risks from third-party code.
Design Impact:
Unsafe languages require extra measures such as sandboxing, input validation, and strict testing. Safe languages allow simpler and more secure architecture.
Example Scenario:
A web application processing uploaded files:
C/C++: Must sandbox core modules and perform extensive validation to avoid memory exploits.
Rust: Memory safety is enforced at compile time, reducing risk and simplifying design.
2) Example of a Secure Language: Rust
Key Features:
Ownership & Borrowing: Prevents dangling pointers and data races.
Immutable by Default: Reduces unintended state changes.
Safe Concurrency: Compiler prevents unsafe shared mutable access.
Option Types: Eliminates null pointer dereferencing.
Example:
fn main() {
let mut v = vec![1,2,3];
let r = &v[0];
// v.push(4);   // compile-time error
println!("{}", r);
}
Rust prevents modification while a reference exists, avoiding memory corruption and race conditions.
Benefit:
Many critical vulnerabilities are eliminated at compile time, making systems safer than relying solely on runtime checks.
Security requirements guide both language choice and application design. Rust, with its compile-time memory and concurrency safety, is an example of a language that helps prevent vulnerabilities and enables secure system development.
| [10]

05

05
|
Q7
CO-3; SO-1;
BL-3
| b.
|
Write a Scala program to demonstrate the following functional combinators on a list of integers: find, drop and dropWhile, foldRight and foldLeft, flatten
Explain the output of each operation with comments in the code.

ANS:

object FunctionalCombinatorsDemo {
def main(args: Array[String]): Unit = {
val nums = List(1, 2, 3, 4, 5, 6)
// 1. find: Returns the first element that satisfies the condition
val found = nums.find(_ > 3)
println(s"find(_ > 3): $found")
// Output Explanation: It returns Some(4) because 4 is the first element greater than 3.
// 2. drop: Skips first 'n' elements and returns the rest
val dropped = nums.drop(3)
println(s"drop(3): $dropped")
// Output Explanation: First 3 elements (1,2,3) are removed. Remaining list: List(4, 5, 6)
// 3. dropWhile: Drops elements from the start as long as the condition is true
val dropWhileResult = nums.dropWhile(_ < 4)
println(s"dropWhile(_ < 4): $dropWhileResult")
// Output Explanation: Drops 1,2,3 because they are <4. Stops at 4. Result: List(4,5,6)
// 4. foldLeft: Aggregates from the left (start) to the right
val sumLeft = nums.foldLeft(0)(_ + _)
println(s"foldLeft(0)(_ + _): $sumLeft")
// Output Explanation: ((((((0 + 1) + 2) + 3) + 4) + 5) + 6) = 21
// 5. foldRight: Aggregates from the right (end) to the left
val sumRight = nums.foldRight(0)(_ + _)
println(s"foldRight(0)(_ + _): $sumRight")
// Output Explanation: (1 + (2 + (3 + (4 + (5 + (6 + 0)))))) = 21
// Note: foldLeft and foldRight give same value here because addition is associative.
// For non-associative operations (like string concatenation), results differ.
// 6. flatten: Flattens a list of lists into a single list
val nestedList = List(List(1, 2), List(3, 4), List(5))
val flattened = nestedList.flatten
println(s"flatten: $flattened")
// Output Explanation: Combines inner lists → List(1,2,3,4,5)
}
}
Output:
find(_ > 3): Some(4)
drop(3): List(4, 5, 6)
dropWhile(_ < 4): List(4, 5, 6)
foldLeft(0)(_ + _): 21
foldRight(0)(_ + _): 21
flatten: List(1, 2, 3, 4, 5)

| [10]

02x5

|
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 2a94e9b474eb

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Advanced Data Analysis and Programming/ANS_Advanced Data Analysis and Programming(703DB0C055)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (21 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Advance Data Analysis and Programming
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026) SYNOPTIC
Instructions:
1. This question paper contains 21 pages.
2. This question paper contains 03 pages.
3. Answer to each new question to be started on a fresh page.
4. Figure in right hand side indicates full marks
5. Question No. 1 is compulsory.
6. Out of remaining questions, attempt any 4 questions.
7. In all 5 questions to be attempted.
8. All questions carry equal marks.
9. Assume Suitable data if necessary.
10. The marks distribution is given for reference, may be changed as per the pattern of the given ans.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a. Write a brief explanation of Simple API, REST API, and HTTP API.   [05]
BL-2   Mention one key feature or use case of each.
ANS:
1. Simple API
A Simple API provides basic communication between software   02
components, usually without following strict architectural rules. It allows
one application to access data or functions of another using simple
request–response mechanisms.
• Use Case:
Easy to implement for small-scale or internal applications where
complex features (like authentication or statelessness) are not
required.
1.5
2. REST API (Representational State Transfer API)
A REST API is a web-based API that follows the REST architecture, using
standard HTTP methods (GET, POST, PUT, DELETE) for
communication. It is stateless, meaning each request is independent and
self-contained.
• Use Case:
Ideal for web and mobile applications — for example, fetching
data from a database using a GET request or updating records with
PUT.
1.5
********** 1 **********
--- page 2 ---
3. HTTP API
An HTTP API uses the HTTP protocol as its communication standard,
allowing data to be exchanged between clients and servers using URLs
and methods like GET, POST, and DELETE.
• Use Case:
Commonly used in cloud services and web applications to connect
systems over the internet (e.g., APIs for payment gateways or
social media integrations).
For the given DataFrame:
CO-2; SO-1;   b.   [05]
BL-2,3   df = pd.DataFrame({ 'Employee': ['E1', 'E2', 'E3'], 'Score': [88, 92, 85]})
i.   Convert Score to float type using astype().
ii.   Rank the scores in ascending order and add a new column
Rank.
ANS:
2.5
2.5
Output:
Explain the difference between a List and a Map in Scala. Write a small
CO-3; SO-1;   c. example showing each and highlight one key difference.   [05]
BL-3
ANS:
Difference Between List and Map in Scala:
Feature   List   Map
Structure   Ordered collection of   Collection of key-value   02
elements   pairs
Element   Accessed by index   Accessed by key
Access
Duplicates   Allows duplicate elements   Keys must be unique
Immutability   Default List is immutable   Default Map is immutable
********** 2 **********
--- page 3 ---
Scala Example:
object ListMapDemo extends App {
// List example
val fruits = List("Apple", "Banana", "Apple")   03
println(s"List: $fruits")
println(s"First element: ${fruits(0)}") // Access by index
// Map example
val fruitPrices = Map("Apple" -> 100, "Banana" -> 50)
println(s"Map: $fruitPrices")
println(s"Price of Apple: ${fruitPrices("Apple")}") //
Access by key
// Key difference highlighted
println("List allows duplicates, Map keys are unique.")
}
Output:
List: List(Apple, Banana, Apple)
First element: Apple
Map: Map(Apple -> 100, Banana -> 50)
Price of Apple: 100
List allows duplicates, Map keys are unique.
Difference:
•   List is an ordered collection accessed by index and allows
duplicates.
• Map is a collection of key-value pairs, accessed by key, and keys
must be unique.
CO-4; SO-1;   d. Explain the concept of RDD (Resilient Distributed Dataset) in Apache   [05]
BL-2   Spark. Write its important features and advantages over traditional data
structures.
ANS:
Concept of RDD (Resilient Distributed Dataset):
02
• An RDD is the fundamental data structure in Apache Spark.
•   It is a distributed collection of elements that can be processed in
parallel across a cluster.
• RDDs are immutable, fault-tolerant, and support lazy
transformations.
Important Features of RDDs:   1.5
1. Immutable: Once created, the data cannot be changed.
2. Distributed: Data is split across multiple nodes in a cluster.
3. Fault-tolerant: Can recover lost data using lineage information.
4. Lazy evaluation: Transformations are only computed when an
action is called.
********** 3 **********
--- page 4 ---
5. Parallel processing: Supports distributed computations for big data.
1.5
Advantages over Traditional Data Structures:
•   Scalability: Can handle large datasets across clusters, unlike local
arrays or lists.
• Performance: In-memory computation reduces disk I/O compared
to traditional storage.
•   Fault Tolerance: Automatically recovers from node failures.
• Support for Big Data Operations: Enables transformations and
actions on large datasets efficiently.
Q2   Write a Python program to demonstrate data structures - List and
CO-1; SO-1;   a. Dictionary.   [10]
BL-2   Create each with sample elements. Perform at least five operations on
each. Print their outputs.
ANS:
Explanation:
•   List: Ordered, mutable collection supporting indexing, insertion,
removal, and sorting.   05x2
•   Dictionary: Unordered, mutable key-value structure allowing
dynamic data manipulation.
Python Program: Demonstrating List and Dictionary Operations
# List Operations
print(" List Operations ")
# Creating a list
fruits = ["Apple", "Banana", "Cherry", "Mango"]
# 1. Access an element
print("First fruit:", fruits[0])
# 2. Add an element
fruits.append("Orange")
# 3. Insert at a specific position
fruits.insert(2, "Grapes")
# 4. Remove an element
fruits.remove("Banana")
# 5. Sort the list
fruits.sort()
print("Updated List:", fruits)
# Dictionary Operations
********** 4 **********
--- page 5 ---
print("\n Dictionary Operations ")
# Creating a dictionary
student = {"Name": "Amit", "Age": 20, "Course":
"Python"}
# 1. Access a value
print("Student Name:", student["Name"])
# 2. Add a new key-value pair
student["Grade"] = "A"
# 3. Update an existing key
student["Age"] = 21
# 4. Delete a key-value pair
student.pop("Course")
# 5. Display all items
print("All Items:", student.items())
print("Updated Dictionary:", student)
Output:
List Operations
First fruit: Apple
Updated List: ['Apple', 'Cherry', 'Grapes',
'Mango', 'Orange']
Dictionary Operations
Student Name: Amit
All Items: dict_items([('Name', 'Amit'), ('Age',
21), ('Grade', 'A')])
Updated Dictionary: {'Name': 'Amit', 'Age': 21,
'Grade': 'A'}
Q2   Write a Python program to demonstrate the difference between the
CO-2; SO-1;   b. apply() and map() functions in Pandas. For the given snippet, show how   [10]
BL-3   each function works, and display the outputs for comparison.
ANS:
********** 5 **********
--- page 6 ---
import pandas as pd
# Create a Pandas Series
s = pd.Series([1, 2, 3, 4, 5])
02
# Using map()
result_map = s.map(lambda x: x * 10)
print("Output using map():")
print(result_map)
# Using apply()
result_apply = s.apply(lambda x: x + 5)
print("\nOutput using apply():")
print(result_apply)
1. map(): element-wise transformation on a Series.
2. apply(): can be used on Series or DataFrame, can apply
row/column functions.
1. map() Function   2x03
• map() is used only with Pandas Series
•   It applies a function element-wise
•   It is commonly used for simple transformations or value mapping
•   In this example:
• s.map(lambda x: x * 10)
Each element of the Series is multiplied by 10.
Result:
[1, 2, 3, 4, 5] → [10, 20, 30, 40, 50]
2. apply() Function
• apply() can be used on both Series and DataFrames
•   It is more flexible than map()
********** 6 **********
--- page 7 ---
•   It can apply complex functions row-wise or column-wise (for
DataFrames)
•   In this example:
• s.apply(lambda x: x + 5)
Each element of the Series is increased by 5.
Result:
[1, 2, 3, 4, 5] → [6, 7, 8, 9, 10]
Differences Between map() and apply()
Feature   map()   apply()
Works on   Series only   Series & DataFrame
Use case   Simple element-wise   Complex
mapping   transformations
Flexibility Less   More
Performan   Faster for simple tasks   Slightly slower
ce
OR
02
Q3   Create a DataFrame with the given data and perform:
CO-2; SO-1;   a.   [10]
BL-3   Department Employee Salary   Experience
HR   E1   40000   2
HR   E2   45000   3
IT   E3   60000   5
IT   E4   65000   6
Finance   E5   70000   7
Finance   E6   72000   8
IT   E7   68000   4
Group by Department and calculate:
Total Salary and Average Experience
Create a bar plot of total Salary per department using Matplotlib or
Seaborn.
Highlight departments with total Salary > 130000 in a different color.
ANS:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create DataFrame
********** 7 **********
--- page 8 ---
data = {
'Department': ['HR', 'HR', 'IT', 'IT', 'Finance',
'Finance', 'IT'],
'Employee': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
'Salary': [40000, 45000, 60000, 65000, 70000, 72000,
68000],
'Experience': [2, 3, 5, 6, 7, 8, 4]
}   02
df = pd.DataFrame(data)
# i. Group by Department and calculate Total Salary and
Average Experience
grouped = df.groupby('Department').agg({'Salary': 'sum',
'Experience': 'mean'}).reset_index()
grouped.rename(columns={'Salary': 'Total_Salary',
'Experience': 'Avg_Experience'}, inplace=True)
print("Grouped Data:")
02
print(grouped)
# ii. Create a bar plot of total Salary per department
plt.figure(figsize=(8, 5))
# Highlight departments with Total_Salary > 130000
colors = ['orange' if x > 130000 else 'skyblue' for x in
grouped['Total_Salary']]
sns.barplot(x='Department', y='Total_Salary', data=grouped,
palette=colors)
# Add labels and title
plt.title('Total Salary per Department')
plt.xlabel('Department')   04
plt.ylabel('Total Salary')
# Show the bar values
for index, value in enumerate(grouped['Total_Salary']):
plt.text(index, value + 2000, str(value), ha='center')
plt.show()
Explanation:
1. Grouping:
groupby('Department').agg({'Salary':'sum','Experience'
:'mean'})
→ Aggregates total salary and average experience per department.
2. Bar Plot:
Uses Seaborn’s barplot to visualize total salary per department.
3. Highlighting:
The colors list assigns 'orange' to departments where total
salary > 130000, and 'skyblue' otherwise.
02
Output Summary:
Department Total_Salary Avg_Experience
Finance   142000   7.5
HR   85000   2.5
IT   193000   5.0
********** 8 **********
--- page 9 ---
• Finance and IT bars appear orange (since total salary > 130000).
• HR bar remains sky blue.
Q3   Design and implement a Python GUI using Tkinter with the following
CO-1; SO-1;   b. features:
BL-5
i. Use Checkbuttons to allow users to select their preferred hobbies   [10]
(e.g., Reading, Painting, Music).
ii. Use Radiobuttons to allow users to select their favorite travel
mode (Car, Train, Flight).
iii. Display the user’s selections dynamically within the GUI.
Explain the working of your GUI code in detail and justify the choice of
using Checkbuttons for multiple selections and Radiobuttons for single
selection.
ANS:
Python GUI Implementation using Tkinter
import tkinter as tk
04
def show_selection():
selected_hobbies = []
for hobby, var in hobbies_vars.items():
if var.get():
selected_hobbies.append(hobby)
selected_travel_mode = travel_var.get()
result_label.config(text=f"Hobbies: {',
'.join(selected_hobbies)}\nTravel Mode:
{selected_travel_mode}")
# Create main window
root = tk.Tk()
root.title("User Preferences")
# Hobbies using Checkbuttons
hobbies_vars = {
"Reading": tk.BooleanVar(),
"Painting": tk.BooleanVar(),
"Music": tk.BooleanVar()
}
tk.Label(root, text="Select your hobbies:").pack()
for hobby, var in hobbies_vars.items():
tk.Checkbutton(root, text=hobby, variable=var,
command=show_selection).pack(anchor='w')
# Output Figure
********** 9 **********
--- page 10 ---
# Travel mode using Radiobuttons
tk.Label(root, text="Select your favorite travel
mode:").pack()   04
travel_var = tk.StringVar(value="Car") # Default
selection
for mode in ["Car", "Train", "Flight"]:
tk.Radiobutton(root, text=mode,
variable=travel_var, value=mode,
command=show_selection).pack(anchor='w')
# Label to display selections dynamically
result_label = tk.Label(root, text="Hobbies:
\nTravel Mode: ")
result_label.pack(pady=10)
root.mainloop()
# Output Figure
Any MODE will work
Working Explanation
02
1. Checkbuttons for Hobbies
• Each hobby has a BooleanVar() associated with it.
• Users can select multiple hobbies simultaneously.
• The command=show_selection updates the displayed
selection dynamically.
2. Radiobuttons for Travel Mode
• Only one option can be selected at a time, enforced by
sharing a single StringVar().
• Dynamic update occurs on selection, showing the chosen
travel mode.
3. Dynamic Display
********** 10 **********
--- page 11 ---
• The show_selection() function collects all selected
hobbies and the chosen travel mode, updating the Label
widget in real-time.
Justification of Widget Choices
•   Checkbuttons: Ideal for multiple selections because each option
can be independently checked or unchecked.
•   Radiobuttons: Ideal for single selection because all buttons share
the same variable, ensuring only one option is active at a time.
Q4   Write a Scala program with an abstract class Shape having a method
CO-3; SO-1;   a. area. Create subclasses Circle and Rectangle that override this   [10]
BL-5   method. Demonstrate field overriding and print areas for multiple
objects.
ANS:
Scala Program: Abstract Class and Field Overriding
07
// Abstract class Shape
abstract class Shape {
def area: Double   // Abstract method
}
// Subclass Circle
class Circle(val radius: Double) extends Shape {
override def area: Double = Math.PI * radius *
radius
}
// Subclass Rectangle
class Rectangle(val length: Double, val width:
Double) extends Shape {
override def area: Double = length * width
}
// Demonstration
object ShapeDemo extends App {
val shapes: List[Shape] = List(
new Circle(5),
new Rectangle(4, 6),
new Circle(3),
new Rectangle(2, 8)
)
shapes.foreach {
case c: Circle   => println(s"Circle area
(radius=${c.radius}): ${c.area}")
********** 11 **********
--- page 12 ---
case r: Rectangle => println(s"Rectangle
area (length=${r.length}, width=${r.width}):
${r.area}")
}
}
Output: As per your choice of values and expalanation.
Explanation   03
1. Abstract Class Shape
• Declared using abstract class
•   Contains:
• An abstract method area()
• A field name
• Cannot be instantiated directly
2. Method Overriding
• Both Circle and Rectangle override the area() method
• override keyword ensures compile-time safety
3. Field Overriding
• The name field in the parent class is overridden in subclasses
• Demonstrates field overriding
4. Polymorphism
• A List[Shape] holds objects of different subclasses
• At runtime, the correct area() method is called based on the
object type
OOP Concepts Demonstrated
Concept   Explanation
Abstraction   Shape defines common behavior
Inheritance   Circle, Rectangle extend
Shape
Method   area() redefined in subclasses
Overriding
Field Overriding name field overridden
Polymorphism   Same reference type, different
behavior
Q4   Describe the Apache Spark architecture with its main components.
CO-4; SO-1;   b. Draw a diagram showing how the Driver, Cluster Manager, Executors,   [10]
BL-3   and Tasks interact during the execution of a Spark job.
ANS:
********** 12 **********
--- page 13 ---
Apache Spark Architecture Components:
1. Driver Program   05
• The Driver is the central coordinator of a Spark application.
•   Responsibilities:
• Converts user code into a Directed Acyclic Graph (DAG).
•   Splits the DAG into stages and tasks.
• Schedules tasks on executors.
•   Collects results from executors.
• Runs the SparkContext, which is the entry point of Spark.
2. Cluster Manager
• Manages and allocates cluster resources.
•   Responsible for assigning CPU and memory to Spark applications.
• Common cluster managers:
• Standalone
• YARN
• Mesos
• Kubernetes
3. Executors
•   Executors are worker processes launched on cluster nodes.
•   Responsibilities:
• Execute tasks assigned by the Driver.
• Cache data in memory or disk.
• Return results back to the Driver.
• Each Spark application has its own executors.
4. Tasks
• A task is the smallest unit of execution in Spark.
• Each task processes a partition of data.
•   Multiple tasks run in parallel on executors.
Spark Application
• A Spark application consists of:
• One Driver program
• One or more Executors
• Tasks executed on the data
Execution Flow of a Spark Job
1. User submits a Spark application.   05
2. The Driver requests resources from the Cluster Manager.
3. The Cluster Manager launches Executors on worker nodes.
4. The Driver creates a DAG and divides it into stages and tasks.
5. Tasks are sent to Executors for execution.
********** 13 **********
--- page 14 ---
6. Executors process data and send results back to the Driver.
7. Final output is produced.
Apache Spark Architecture Diagram:
With Proper description in the Diagram.
Q5   Write a Spark Scala program that:
CO-4; SO-1;   a.   [10]
BL-5   i.   Creates an RDD of integers.
ii.   Applies a transformation (like map(x => x*2)).
iii.   Persists the transformed RDD in memory or on disk.
ANS:
Spark Scala Program to Persist an RDD
import org.apache.spark.{SparkConf, SparkContext}   06
import org.apache.spark.storage.StorageLevel
object RDDPersistenceBL5 {
def main(args: Array[String]): Unit = {
// Step 1: Spark configuration and context
val conf = new SparkConf().setAppName("RDD Persistence
Example").setMaster("local[*]")
val sc = new SparkContext(conf)
// Step 2: Create an RDD of integers
val rdd = sc.parallelize(List(1, 2, 3, 4, 5))
// Step 3: Apply a transformation (map)
val transformedRDD = rdd.map(x => x * 2)
// Step 4: Persist the RDD in memory
transformedRDD.persist(StorageLevel.MEMORY_AND_DISK)
// Step 5: Perform multiple actions on the persisted
RDD
********** 14 **********
--- page 15 ---
println("Collect: " +
transformedRDD.collect().mkString(", "))
println("Count: " + transformedRDD.count())
println("Take(3): " +
transformedRDD.take(3).mkString(", "))
// Stop SparkContext
sc.stop()
}
}
04
# Different way of expiation is also correct.
Explanation & Analysis
1. RDD Persistence:
•   Stores the RDD in memory or disk to avoid recomputation
when used multiple times.
• Reduces execution time for iterative operations like machine
learning algorithms.
2. Types of Persistence:
• MEMORY_ONLY – Fast, stores in memory; recomputes lost
partitions if memory is insufficient.
• MEMORY_AND_DISK – Stores in memory, spills to disk if
memory is full.
• DISK_ONLY – Stores only on disk; slower but saves memory.
•   Serialized options (*_SER) – Save memory by storing
compressed objects.
3. Why Useful:
•   Iterative Algorithms: Multiple actions (e.g., collect,
count, take) don’t recompute the RDD each time.
•   Fault Tolerance: Spark can recover lost partitions from lineage
or persisted disk copies.
• Performance Optimization: Choice of storage level balances
speed vs memory usage.
4. BL5 Analysis Aspect:
• Choosing MEMORY_AND_DISK ensures faster in-memory
access while avoiding recomputation if memory is
insufficient.
• Demonstrates understanding of performance trade-offs and
efficient resource utilization in large-scale Spark applications.
Q5   Design a class structure for different types of vehicles (Car, Bike,
CO-1; SO-1;   b. Truck) using Polymorphism in Python.   [10]
BL-3   Show how method overriding and method overloading (simulated) can
be applied.
Write proper code.
ANS:
Python Code: Vehicle Class Structure with Polymorphism
# Base class   02
class Vehicle:
def __init__(self, brand, model):
self.brand = brand
********** 15 **********
--- page 16 ---
self.model = model
def vehicle_info(self):
print(f"Vehicle Brand: {self.brand},
Model: {self.model}")
# Simulated method overloading using default
arguments
def start(self, speed=None):
if speed is not None:
print(f"{self.brand} {self.model}
04
started at speed {speed} km/h")
else:
print(f"{self.brand} {self.model}
started")
# Derived class Car
class Car(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Car Brand: {self.brand}, Model:
{self.model}")
# Derived class Bike
class Bike(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Bike Brand: {self.brand}, Model:
{self.model}")
# Derived class Truck
class Truck(Vehicle):
# Method overriding
def vehicle_info(self):
print(f"Truck Brand: {self.brand}, Model:
{self.model}")
# Creating objects
car1 = Car("Toyota", "Corolla")
bike1 = Bike("Yamaha", "R15")
truck1 = Truck("Volvo", "FH16")
# Demonstrating method overriding
car1.vehicle_info()   # Car specific info
bike1.vehicle_info()   # Bike specific info
truck1.vehicle_info()   # Truck specific info
# Demonstrating simulated method overloading   04
car1.start()   # Default start
bike1.start(60)   # Start with speed
truck1.start(80)   # Start with speed
********** 16 **********
--- page 17 ---
Explanation of method overriding and method overloading (simulated)
can be applied.
Q6   Write a Scala program to:
CO-3; SO-1;   a.   [10]
BL-2,   i.   Create a Tuple with mixed data types.
ii.   Create a Set with unique elements.
iii.   Perform basic operations on each collection: add, remove, and
access elements.
iv.   Display the final Tuple and Set
ANS:
Scala Program: Tuple and Set Operations
object TupleSetDemo extends App {
06
// i. Create a Tuple with mixed data types
val tup = ("Scala", 2025, true)
println(s"Initial Tuple: $tup")
// Access Tuple elements
println(s"First element: ${tup._1}")
println(s"Second element: ${tup._2}")
println(s"Third element: ${tup._3}")
// ii. Create a Set with unique elements
var set = Set(1, 2, 3, 4)
println(s"Initial Set: $set")
// iii. Basic operations
// Set operations (add and remove)
set += 5   // Add element
set -= 2   // Remove element
// Access element
println(s"Contains 3? ${set.contains(3)}")
// iv. Display final collections
println(s"Final Tuple (immutable): $tup")
println(s"Final Set: $set")   04
}
Explanation
1. Tuple Creation
• A Tuple allows storing multiple values of different data types.
• myTuple contains an Integer, String, Double, and Boolean.
********** 17 **********
--- page 18 ---
• Tuple elements are accessed using _1, _2, _3, _4.
2. Set Creation
• A Set stores unique elements only.
•   Duplicate values are automatically removed.
3. Set Operations
• Add element: +
• Remove element: -
• Access element: contains()
4. Display Output
• The program prints the accessed elements, final tuple, and updated
set.
Output:
Initial Tuple: (Scala,2025,true)
First element: Scala
Second element: 2025
Third element: true
Initial Set: Set(1, 2, 3, 4)
Contains 3? true
Final Tuple (immutable): (Scala,2025,true)
Final Set: Set(1, 3, 4, 5)
Q6   Discuss the impact of development convenience, debugging tools, and
CO-5; SO-1;   b. IDE support on improving a programmer’s productivity and ensuring   [10]
BL-4   long-term maintainability of code.
ANS: (Give the Example in detail)
Development convenience, debugging tools, and IDE support significantly
enhance a programmer’s productivity and the maintainability of code over
time.   03x3
1. Development Convenience:
• Programming languages and frameworks with simple
syntax, readable code structures, and built-in libraries allow
developers to write code faster and with fewer errors.
• Example: Python’s clear syntax and extensive libraries
(e.g., NumPy, Pandas) enable rapid development and
reduce boilerplate code.
2. Debugging Tools:
• Debuggers, linters, and static analysers help identify errors
early, reducing runtime bugs and improving code quality.
• Example: IDEs like PyCharm or Visual Studio Code
highlight syntax errors, potential logic issues, and runtime
********** 18 **********
--- page 19 ---
warnings instantly, saving time in testing and
troubleshooting.
3. IDE Support:
•   Integrated Development Environments provide code
completion, refactoring, version control, testing
frameworks, and project management tools in one place.
• This improves efficiency by reducing context switching and
helps maintain consistent coding standards.
• Example: Eclipse or IntelliJ IDEA supports large-scale
projects with advanced debugging and collaboration
features.   01
When development is convenient, debugging is efficient, and IDE support
is robust, programmers can write high-quality code faster. This not only
increases productivity but also ensures long-term maintainability, as the
code is easier to understand, modify, and extend.
Q7   Explain how security considerations can influence the choice of a
CO-5; SO-1;   a. programming language and the design of an application. Give one   [10]
BL-4   example of a programming language that provides strong security
features and explain why it is considered secure.
ANS: (Example of any Language will be considered)
Security considerations are critical when selecting a programming
language and designing an application. Applications that handle sensitive   05
data or operate in untrusted environments must minimize vulnerabilities,
prevent exploits, and ensure reliability. The choice of language affects the
types of security risks and how easily they can be mitigated.
1) Influence on Language Choice and Design
• Memory Safety: Languages like Rust or Java prevent buffer
overflows and dangling pointers.
• Type Safety: Strong typing helps catch errors at compile time,
reducing logical flaws.
• Concurrency Safety: Safe concurrency prevents data races and
related security issues.
• Sandboxing & Runtime Checks: VM-based execution limits the
impact of malicious code.
•   Library Ecosystem: Vetted libraries reduce risks from third-party
code.
Design Impact:
Unsafe languages require extra measures such as sandboxing, input
validation, and strict testing. Safe languages allow simpler and more
secure architecture.
Example Scenario:
A web application processing uploaded files:
********** 19 **********
--- page 20 ---
• C/C++: Must sandbox core modules and perform extensive
validation to avoid memory exploits.
•   Rust: Memory safety is enforced at compile time, reducing risk and
simplifying design.
2) Example of a Secure Language: Rust
Key Features:
05
• Ownership & Borrowing: Prevents dangling pointers and data
races.
• Immutable by Default: Reduces unintended state changes.
•   Safe Concurrency: Compiler prevents unsafe shared mutable
access.
• Option Types: Eliminates null pointer dereferencing.
Example:
fn main() {
let mut v = vec![1,2,3];
let r = &v[0];
// v.push(4);   // compile-time error
println!("{}", r);
}
Rust prevents modification while a reference exists, avoiding memory
corruption and race conditions.
Benefit:
Many critical vulnerabilities are eliminated at compile time, making
systems safer than relying solely on runtime checks.
Security requirements guide both language choice and application design.
Rust, with its compile-time memory and concurrency safety, is an example
of a language that helps prevent vulnerabilities and enables secure system
development.
Q7
CO-3; SO-1;   b. Write a Scala program to demonstrate the following functional   [10]
BL-3   combinators on a list of integers: find, drop and dropWhile,
foldRight and foldLeft, flatten
Explain the output of each operation with comments in the code.
ANS:
object FunctionalCombinatorsDemo {
def main(args: Array[String]): Unit = {   02x5
val nums = List(1, 2, 3, 4, 5, 6)
// 1. find: Returns the first element that satisfies the condition
val found = nums.find(_ > 3)
println(s"find(_ > 3): $found")
// Output Explanation: It returns Some(4) because 4 is the first element
greater than 3.
********** 20 **********
--- page 21 ---
// 2. drop: Skips first 'n' elements and returns the rest
val dropped = nums.drop(3)
println(s"drop(3): $dropped")
// Output Explanation: First 3 elements (1,2,3) are removed. Remaining
list: List(4, 5, 6)
// 3. dropWhile: Drops elements from the start as long as the condition is
true
val dropWhileResult = nums.dropWhile(_ < 4)
println(s"dropWhile(_ < 4): $dropWhileResult")
// Output Explanation: Drops 1,2,3 because they are <4. Stops at 4. Result:
List(4,5,6)
// 4. foldLeft: Aggregates from the left (start) to the right
val sumLeft = nums.foldLeft(0)(_ + _)
println(s"foldLeft(0)(_ + _): $sumLeft")
// Output Explanation: ((((((0 + 1) + 2) + 3) + 4) + 5) + 6) = 21
// 5. foldRight: Aggregates from the right (end) to the left
val sumRight = nums.foldRight(0)(_ + _)
println(s"foldRight(0)(_ + _): $sumRight")
// Output Explanation: (1 + (2 + (3 + (4 + (5 + (6 + 0)))))) = 21
// Note: foldLeft and foldRight give same value here because addition is
associative.
// For non-associative operations (like string concatenation), results differ.
// 6. flatten: Flattens a list of lists into a single list
val nestedList = List(List(1, 2), List(3, 4), List(5))
val flattened = nestedList.flatten
println(s"flatten: $flattened")
// Output Explanation: Combines inner lists → List(1,2,3,4,5)
}
}
Output:
find(_ > 3): Some(4)
drop(3): List(4, 5, 6)
dropWhile(_ < 4): List(4, 5, 6)
foldLeft(0)(_ + _): 21
foldRight(0)(_ + _): 21
flatten: List(1, 2, 3, 4, 5)
********** 21 **********
````
