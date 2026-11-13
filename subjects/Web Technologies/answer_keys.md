# Web Technologies: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 7dda6f372271

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Web Technologies/ANS_Final-Exam_Web Technologies(NHWEB153)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 23 Mar 2026
- Text: text (13 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)/B.Sc. (IT)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Web Technologies
Date: 23 Mar 2026   Time: 08:00 am - 10:00 am (02:00 Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 13 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. All questions are compulsory.
1.   Answer the following questions.(Attempt Any 4 Questions)   20
a. •   Telnet is a program that allows you to log into computers on the Internet and use online   5
databases, library catalogs, chat services, and more.
•   There are no graphics in Telnet sessions, just text.
•   To Telnet to a computer, you must know its address.
•   This can consist of words (locis.loc.gov) or numbers (140.147.254.3).
•   Some services require you to connect to a specific port on the remote computer.
•   In this case, type the port number after the Internet address. Example: telnet
nri.reston.va.us 185.
• A link to a Telnet resource may look like any other link, but it will launch a Telnet session
to make the connection.
• A Telnet program must be installed on your local computer and configured to your Web
browser in order to work.
[1 mark any 5 point]
b. An absolute URL is a complete web address that includes the protocol (https://) and domain   5
name. It is mainly used to link external websites.
Example
<a href="https://www.google.com">Google</a>
Page 1 of 13
--- page 2 ---
A relative URL specifies the path to a file within the same website and does not include the
domain name. It is used for internal navigation.
<a href="about.html">About Page</a>
Difference:
Absolute URLs link to external websites.
Relative URLs link to pages within the same website and are easier to maintain.
[1 mark each point]
c. <!DOCTYPE html>   5
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Inline CSS Example</title>
</head>
<body style="background-color:#b0c4de;">
<p style="color:red; border:2px solid black; padding:10px;">
This paragraph demonstrates inline CSS styling.
</p>
</body>
</html>
5
d.   <header> introduces the page
<nav> contains navigation links
<section> groups related content
<article> holds independent content
<footer> contains copyright information
<!DOCTYPE html>
<html>
<body>
<header>
<h1>College Website</h1>
</header>
Page 2 of 13
--- page 3 ---
<nav>
<a href="#">Home</a> |
<a href="#">Courses</a>
</nav>
<section>
<article>
<h2>About Us</h2>
<p>This section contains college information.</p>
</article>
</section>
<footer>
<p>2025 College Name</p>
</footer>
</body>
</html>
[5 marks]
or any other working example
e. !DOCTYPE html>   5
<html>
<head>
<title>Styled List</title>
<style>
ul {
list-style-type: none;
color: darkblue;
font-size: 17px;
}
</style>
</head>
<body>
<ul>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
</ul>
Page 3 of 13
--- page 4 ---
</body>
</html>
[5 marks]
Or any other working code
f. <!DOCTYPE html>   5
<html>
<head>
<title>Bus Timetable</title>
</head>
<body>
<table border="1" cellspacing="8">
<caption><b>City Bus Timetable</b></caption>
<tr>
<th>Bus No</th>
<th>Starting Point</th>
<th>Destination</th>
<th>Departure Time</th>
</tr>
<tr>
<td>12A</td>
<td>Railway Station</td>
<td>City Center</td>
<td>8:00 AM</td>
</tr>
<tr>
<td>25B</td>
<td>College Road</td>
<td>Airport</td>
<td>10:30 AM</td>
</tr>
<tr>
<td>44C</td>
<td>Market</td>
<td>Hospital</td>
<td>1:15 PM</td>
</tr>
</table>
</body>
</html>
Page 4 of 13
--- page 5 ---
[5 marks]
2.   Answer the following questions.(Attempt Any 4 Questions)   20
a. Differentiate between local and global variables in JavaScript and demonstrate their usage with   5
an example.
Solution:
A JavaScript variable is the simple name of the storage location where data is stored. There are
two types of variables in JavaScript which are listed below:
·   Local variables: Declare a variable inside of a block or function.
·   Global variables: Declare a variable outside function or with a window object.
[2 marks]
<!DOCTYPE html>
<head>
<title>Global and local variables</title>
</head>
<body>
<script>
let fruitName = "Apple";
MyFunction();
function MyFunction() {
let vegName = "Palak";
document.write("The name of vegetable is:"+vegName+" The name
of fruit is:"+fruitName);
}   </script>
</html>
[3 marks]
Note: or any other working code
b. Explain the conditional control statements in JavaScript. Write a JavaScript program to   5
determine whether a student has passed or failed based on marks entered by the user.
Solution:
In JavaScript, conditional statements are used to make decisions based on conditions. The
different types of conditional statements are:
1.   if Statement - Executes a block of code if the condition is true.
2.   if-else Statement - Executes one block of code if the condition is true, otherwise executes
another block.
3.   if-else if-else Statement - Checks multiple conditions and executes the first block that is
true.
Page 5 of 13
--- page 6 ---
4.   switch Statement - Compares a value against multiple cases and executes the matching
case.
[2 marks]
<!DOCTYPE html>
<html>
<body>
<script>
let marks = prompt("Enter your marks:");
marks = Number(marks);   // Convert input to number
if (marks >= 40) {
document.write("You have Passed.");
} else {
document.write("You have Failed.");
}
</script>
</body>
</html>
[3 marks]
Note: or any other working code
c. It is used to produce a Boolean object that either has a true or false value.   5
let bool = new Boolean(val);
[1 mark]
<!DOCTYPE html>
<html>
<head>
<title>Boolean Object Example</title>
</head>
<body>
<script>
// Input number
let num = 14;
Page 6 of 13
--- page 7 ---
// Check condition using Boolean object
let result = new Boolean(num % 7 === 0);
// Use switch case
switch(result.valueOf()) {
case true:
console.log("True");
break;
case false:
console.log("False");
break;
}
</script>
</body>
</html>
[4 marks]
Note: or any other working code
d. <!DOCTYPE html>   5
<html>
<head>
<title>Salary Calculator</title>
</head>
<body>
<script>
// Store values in variables
let hoursWorked = 40;   // Number of hours worked
let hourlyWage = 500;   // Wage per hour
// Calculate total salary
let totalSalary = hoursWorked * hourlyWage;
// Display results
console.log("Hours Worked: " + hoursWorked);
console.log("Hourly Wage: ₹" + hourlyWage);
console.log("Total Salary: ₹" + totalSalary);
</script>
</body>
</html>
Page 7 of 13
--- page 8 ---
[5 marks]
e. Output:   5
[5, 10]
[5, 10, 15]
Explanation:
1. Initially, both a and b refer to the same array.
2. concat() does NOT modify the original array.
3. It creates a new array and returns it.
4. b now points to a new array.
5. a remains unchanged.
[1 mark each point]
f. <!DOCTYPE html>   5
<html>
<head>
<title>Text Color Change</title>
</head>
<body>
<p id="text"
onmouseover="changeColor()"
onmouseout="resetColor()">
Move mouse over this text
</p>
<script>
function changeColor() {
document.getElementById("text").style.color = "green";
}
function resetColor() {
document.getElementById("text").style.color = "black";
}
</script>
Page 8 of 13
--- page 9 ---
</body>
</html>
[5 makrs]
3.   Answer the following questions.(Attempt Any 4 Questions)   20
a.   5
A string in PHP is a sequence of characters used to store and manipulate text. Strings can be
defined using single quotes (' ') or double quotes (" ").
echo "Hello";
echo 'Hello’;
•   Double quoted string literals perform operations for special characters:
$x = "John";
echo "Hello $x";
•   Single quoted string literals returns the string as it is:
$x = "John";
echo 'Hello $x';
[3 marks]
<?php
$name = "ABC";
$greeting = "Hello, $name!";
$message = 'Welcome';
// String concatenation
$finalMessage = $greeting . " " . $message;
echo $finalMessage; //?>
[2 marks]
Note: or any other working code
b. The global Keyword   5
•   The global keyword is used to access a global variable from within a function.
$x = 5;
$y = 10;
function myTest() {
global $x, $y;
$y = $x + $y;
}
myTest();
echo $y;
Page 9 of 13
--- page 10 ---
[2.5 marks]
The static Keyword
•   When a function is completed/executed, all of its variables are deleted.
•   Sometimes we want a local variable NOT to be deleted. We need it for a further job.
•   To do this, use the static keyword when you first declare the variable.
•   function myTest() {
static $x = 0;
echo $x;
$x++;
}
myTest();
[2.5 marks]
Note: or any other working code
c. 1. strlen() – String Length Function   5
Used to find the length of a string.
Returns the number of characters in the string.
<?php
echo strlen("Hello PHP");
?>
2. strtoupper() – Convert to Uppercase
Converts all characters of a string to uppercase.
<?php
echo strtoupper("hello");
?>
3. count() – Count Array Elements
Used to count the number of elements in an array.
<?php
$colors = array("Red", "Blue", "Green");
echo count($colors);
?>
4. sqrt() – Square Root Function
Returns the square root of a number.
<?php
echo sqrt(49);
Page 10 of 13
--- page 11 ---
?>
5. date() – Date Function
Used to format and display the current date and time.
<?php
echo date("d-m-Y");
?>
[1 mark each point]
Or any other valid in-built functions
d. <!DOCTYPE html>   5
<html>
<head>
<title>Mobile Number Validation</title>
</head>
<body>
<h2>Mobile Number Validation</h2>
<form method="post">
Enter Mobile Number:
<input type="text" name="mobile" required>
<input type="submit" value="Validate">
</form>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$mobile = $_POST["mobile"];
// Regular expression: exactly 10 digits
$pattern = "/^[0-9]{10}$/";
if (preg_match($pattern, $mobile)) {
echo "<p style='color:green;'>Valid Mobile Number</p>";
} else {
echo "<p style='color:red;'>Invalid Mobile Number. Please enter exactly 10 digits.</p>";
}
}
Page 11 of 13
--- page 12 ---
?>
[5 marks]
Note: or any other working code
e. <!DOCTYPE html>   5
<html>
<head>
<title>Circumference of Square</title>
</head>
<body>
<h2>Circumference of Square</h2>
<?php
// Function to calculate circumference of square
function circumferenceOfSquare($side)
{
$circumference = 4 * $side;
return $circumference;
}
// Given side
$side = 6;
// Function call
$result = circumferenceOfSquare($side);
// Display result
echo "Side of square = $side <br>";
echo "Circumference of Square = " . $result;
?>
</body>
</html>
[5 marks]
Note: or any other working code
f. <?php   5
$number = 153;
$original = $number;
$sum = 0;
Page 12 of 13
--- page 13 ---
while ($number > 0) {
$digit = $number % 10;
$sum = $sum + ($digit * $digit * $digit);
$number = (int)($number / 10);
}
if ($original == $sum) {
echo "$original is an Armstrong Number";
} else {
echo "$original is not an Armstrong Number";
}
?>
[5 marks]
Note: or any other working code
Page 13 of 13
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 71091d86f602

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Web Technologies/ANS_Re-Exam_Web Technologies(NHWEB153)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 16 Jun 2026
- Text: text (13 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: B.Sc. (IT)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Web Technologies
Date: 16 Jun 2026   Time: 10:30 am - 12:30 pm (02:00 Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 13 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. All questions are compulsory.
1.   Answer the following questions.(Attempt Any 4 Questions)   20
a. •   Electronic mail often abbreviated to e-mail, email, or simply mail, is a store-and-forward   5
method of writing, sending, receiving and saving messages over electronic communication
systems.
•   The term "e-mail" (as a noun or verb) applies to the Internet e-mail system based on the
Simple Mail Transfer Protocol
•   To network systems based on other protocols and to various mainframe, minicomputer or
intranet systems
•   It allows users within one organization to send messages to each other in support of
workgroup collaboration.
•   E-mail is often used to deliver bulk unsolicited messages, or "spam", but filter programs
exist which can automatically block, quarantine or delete some or most of these, depending on
the situation.
[1 mark each point]
b. An image can be used as a clickable hyperlink in HTML by placing the <img> tag inside the   5
<a> (anchor) tag. When the user clicks on the image, the browser redirects to the linked
webpage instead of displaying text.
Page 1 of 13
--- page 2 ---
The href attribute of the <a> tag specifies the destination website. To open the linked website
in a new browser tab, the target="_blank" attribute is used. The alt attribute of the <img> tag
provides alternative text, which is helpful for accessibility and is displayed if the image fails to
load.
[2 marks]
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Image as Hyperlink</title>
</head>
<body>
<h2>Image as a Hyperlink Example</h2>
<a href="https://www.wikipedia.org" target="_blank">
<img src="wikipedia.png" alt="Wikipedia Website" width="200">
</a>
<p>Click on the image above to visit Wikipedia.</p>
</body>
</html>
[3 marks]
Or any other working example
c. Cascading Style Sheets (CSS) is a style sheet language used to describe the presentation of   5
HTML documents. CSS controls the layout, colors, fonts, and overall appearance of web
pages.
Advantages of CSS (any four):
1. Saves time by reusing styles across multiple pages
2. Faster page loading due to reduced HTML code
3. Easy maintenance and global updates
4. Better design control compared to HTML attributes
Page 2 of 13
--- page 3 ---
5. Supports multiple device compatibility
[1 mark each point]
d. The <embed> and <object> tags are used to include external content such as multimedia files,   5
PDFs, and web applications in HTML pages.
The <embed> tag is simple and easy to use for embedding media like videos or audio.
The <object> tag supports a wider range of external resources and file types.
<object> allows fallback content if the embedded resource is not supported.
<embed> provides limited control and customization compared to <object>.
<object> is more flexible and suitable for complex embedding requirements.
[1 mark each point}
e. <!DOCTYPE html>   5
<html>
<head>
<title>Internal CSS Page</title>
<style>
body {
background-color: #fff8dc;
}
h1 {
color: brown;
}
p {
color: #333;
font-size: 16px;
}
</style>
</head>
<body>
<h1>Internal Style Sheet Example</h1>
<p>This paragraph is styled using internal CSS.</p>
</body>
Page 3 of 13
--- page 4 ---
</html>
[5 marks]
or any other working example
f. <!DOCTYPE html>   5
<html>
<head>
<title>Workout Plan</title>
</head>
<body>
<table border="1">
<tr>
<th>Day</th>
<th>Workout Type</th>
<th>Time</th>
</tr>
<tr>
<td>Monday</td>
<td>Cardio</td>
<td>6:00 AM</td>
</tr>
<tr>
<td>Wednesday</td>
<td>Strength Training</td>
<td>7:00 AM</td>
</tr>
<tr>
<td>Friday</td>
<td>Yoga</td>
<td>6:30 AM</td>
</tr>
</table>
</body>
</html>
[5 marks]
Or any other working code
2.   Answer the following questions.(Attempt Any 4 Questions)   20
a. •   JavaScript is a single-threaded language which means it executes one task at a time.   5
•   It is an Interpreted language which means it executes the code line by line.
Page 4 of 13
--- page 5 ---
•   The data type of the variable is decided at run-time in JavaScript that’s why it is called
dynamically typed.
[2 marks]
<!DOCTYPE html>
<html>
<head>
<title>String Addition</title>
</head>
<body>
<script>
let str1 = prompt("Enter first string:");
let str2 = prompt("Enter second string:");
let result = str1 + str2;
document.write("Concatenated String: " + result);
</script>
</body>
</html>
[3 marks]
Note: or any other working code
b. Explain how certain statements can either terminate a loop completely or skip the current   5
iteration. Illustrate your answer with suitable examples.
Solution:
There are two special statements that can be used inside loops: break and continue. JavaScript
break and continue Statements.
Break
The break command will break the loop and continue executing the code that follows after the
loop (if any).
Example
<html>
<body>
<script type="text/javascript">
var i=0;
for (i=0;i<=10;i++)
{ if (i==3) { break; }
Page 5 of 13
--- page 6 ---
document.write("The number is " + i);
document.write("<br />"); }
</script>
</body>
</html>
[2.5 marks]
Continue
The continue command will break the current loop and continue with the next value.
<html>
<body>
<script type="text/javascript">
var i=0
for (i=0;i<=10;i++)
{ if (i==3) { continue; }
document.write("The number is " + i);
document.write("<br />"); }
</script>
</body>
</html>
[2.5 marks]
Note: or any other working code
c. <!DOCTYPE html>   5
<html>
<head>
<title>Alphabet Validation</title>
</head>
<body>
<h2>Check String Contains Only Alphabets</h2>
<script>
let str = prompt("Enter a string:");
// Regular expression for only alphabets
let pattern = /^[A-Za-z]+$/;
if (pattern.test(str)) {
document.write("The string contains only alphabets.");
Page 6 of 13
--- page 7 ---
} else {
document.write("The string does not contain only alphabets.");
}
</script>
</body>
</html>
[5 marks]
Note: or any other working code
d. <!DOCTYPE html>   5
<html>
<head>
<title>Purchase Discount Calculator</title>
</head>
<body>
script>
// Store total purchase amount
let purchaseAmount = 2500;
let discountRate;
let discountAmount;
let finalAmount;
// Apply discount condition
if (purchaseAmount > 2000) {
discountRate = 15;
} else {
discountRate = 5;
}
// Calculate discount and final amount
discountAmount = (purchaseAmount * discountRate) / 100;
finalAmount = purchaseAmount - discountAmount;
// Display results
console.log("Original Amount: ₹" + purchaseAmount);
console.log("Discount Applied: " + discountRate + "%");
console.log("Discount Amount: ₹" + discountAmount);
console.log("Final Payable Amount: ₹" + finalAmount);
</script>
</body>
</html>
Page 7 of 13
--- page 8 ---
[5 marks]
e. Execution Steps:   5
Start: i = 1
1st iteration: 1 < 5 → prints → i = 2
2nd iteration: 2 < 5 → prints → i = 4
3rd iteration: 4 < 5 → prints → i = 8
Next check: 8 < 5 → false → loop stops
Total Executions:
The loop runs 3 times.
The loop doubles the value each time, so it exits quickly when the condition becomes false
[1 mark each point]
f. DOCTYPE html>   5
<html>
<head>
<title>Show Date</title>
</head>
<body>
<button onclick="showDate()">Show Date</button>
<p id="date"></p>
<script>
function showDate() {
let today = new Date();
document.getElementById("date").innerHTML =
"Current Date: " + today.toDateString();
}
</script>
</body>
</html>
[5 marks]
Page 8 of 13
--- page 9 ---
3.   Answer the following questions.(Attempt Any 4 Questions)   20
a. A Boolean in PHP represents true (1) or false (0) values. It is commonly used in conditional   5
statements and logical operations.
A Boolean variable can have only two values: true or false.
Booleans are often used in if-else statements for decision-making.
true is treated as 1, and false is treated as an empty value when displayed.
[2 marks]
<!DOCTYPE html>
<html>
<head>
<title>PHP Boolean Example</title>
</head>
<body>
<?php
$is_logged_in = true; // Boolean variable
echo "<h2>Boolean Data Type Example</h2>";
if ($is_logged_in) {
echo "<p>Welcome, User! You are logged in.</p>";
} else {
echo "<p>Access Denied. Please log in.</p>";
}
?>
</body>
</html>
[3 marks]
Note: or any other working code
b. Explain the main features of PHP. Write a simple PHP program demonstrating PHP syntax.   5
Solution:
•   PHP is a widely-used, open-source scripting language
•   PHP scripts are executed on the server
•   PHP is free to download and use
• A PHP script can be placed anywhere in the document.
• A PHP script starts with <?php and ends with ?>:
[3 marks]
<?php
// PHP code goes here
?>
Page 9 of 13
--- page 10 ---
<!DOCTYPE html>
<html>
<body>
<h1>My first PHP page</h1>
<?php
echo "Hello World!";
?>
</body>
</html>
[2 marks]
Note: or any other working code
c. The round() function in PHP is used to round a floating-point number. It can be used to define   5
a specific precision value which rounds number according to that precision value.Precision can
be also negative or zero.
The round() function in PHP has 3 parameters which are number, precision, and mode among
which the latter two are optional parameters.The round() function returns the rounded value of
the argument passed.
float round($number, $precision, $mode);
<!DOCTYPE html>
<html>
<head>
<title>PHP round() Function Example</title>
</head>
<body>
<h2>Rounding Function</h2>
<?php
$num1 = 4.7;
$num2 = 4.3;
echo "<p>Round $num1: " . round($num1) . "</p>";
echo "<p>Round $num2: " . round($num2) . "</p>";
?>
</body>
</html>
[2.5 marks]
The rand() function is used to generate a random integer number.
It is commonly used in applications like games, OTP generation, and simulations.
he rand() is an inbuilt function in PHP used to generate a random number ie., it can generate a
random integer value in the range [min, max].
Page 10 of 13
--- page 11 ---
rand();
rand(min,max);
min: It is an optional parameter that specifies the lowest value that will be returned. The
default value is 0.
max: It is an optional parameter that specifies the highest value to be returned.
<!DOCTYPE html>
<html>
<head>
<title>PHP rand() Function Example</title>
</head>
<body>
<h2>Random Number Generator</h2>
<?php
$min = 1;
$max = 100;
echo "<p>Random number between $min and $max: " . rand($min, $max) . "</p>";
?>
</body>
</html>
[2.5 marks]
Note: or any other working code
d. <!DOCTYPE html>   5
<html>
<head>
<title>PHP Regex - Replace Digits</title>
</head>
<body>
<h2>Replace Digits with ?</h2>
<?php
function replaceDigits($string) {
$pattern = "/\d/";
$newString = preg_replace($pattern, "?", $string);
echo "<p>Modified String: $newString</p>";
}
$text = "My phone number is 12345";
replaceDigits($text);
?>
Page 11 of 13
--- page 12 ---
</body>
</html>
[5 marks]
Note: or any other working code
e. <!DOCTYPE html>   5
<html>
<head>
<title>Area of Rectangle</title>
</head>
<body>
<h2>Area of Rectangle</h2>
<?php
// Function to calculate area of rectangle
function areaOfRectangle($length, $breadth)
{
$area = $length * $breadth;
return $area;
}
// Given values
$length = 10;
$breadth = 5;
// Function call
$result = areaOfRectangle($length, $breadth);
// Display result
echo "Length = $length <br>";
echo "Breadth = $breadth <br>";
echo "Area of Rectangle = " . $result;
?>
</body>
</html>
[5 marks]
Note: or any other working code
Page 12 of 13
--- page 13 ---
f. <?php   5
$speed = 45;
switch (true) {
case ($speed >= 0 && $speed <= 5):
echo "Very Slow Internet";
break;
case ($speed >= 6 && $speed <= 20):
echo "Slow Internet";
break;
case ($speed >= 21 && $speed <= 50):
echo "Moderate Internet";
break;
case ($speed >= 51 && $speed <= 100):
echo "Fast Internet";
break;
case ($speed > 100):
echo "Very Fast Internet";
break;
default:
echo "Invalid speed";
}
?>
[5 marks]
Note: or any other working code
Page 13 of 13
````
