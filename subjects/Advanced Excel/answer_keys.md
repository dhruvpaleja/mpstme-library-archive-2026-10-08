# Advanced Excel: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper ea3b86756f3a

- Departments: Commerce
- Programmes: Bachelor of Commerce - 45611
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/Bachelor of Commerce - 45611/Advanced Excel/ANS_Final-Exam_Advanced Excel(NAAEX155)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 27 Mar 2026
- Text: mixed (6 pages), mean OCR confidence 88.6

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Commerce
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Advanced Excel
Date: 27 Mar 2026   Time: 08:00 am - 09:00 am (01:00 Hrs.)
Max Marks: 30
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 6 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume data wherever required
1.   Answer the following questions (Attempt Any 2 Questions)   15
a.   7.5
Page 1 of 6
--- page 2 ---
Solution
i) To Find the Lowest Score in Column F 1.35 Mk

1. Click on cell F2.
2. Enter the formula:

3. =MIN(B2:E2)
4. Press Enter.

5. Drag the fill handle from F2 down to F5 to copy the formula for all players.

ii) To Find the Second Lowest Score in Column G 1.5 Mk

1. Click on cell G2.
2. Enter the formula:
3. =SMALL(B2:E2,2)
4. Press Enter.
5. Drag the fill handle from G2 down to GS.
iii) To Calculate Average Scorein Column H 1.5 Mk

1. Click on cell H2.

2. Enter the formula:

3. =AVERAGE(B2:E2)

4. Press Enter.

5. Drag the fill handle from H2 down to H5.

iv) To Assign Ranking in Column I Using LOOKUP 3 Mk
Use approximate match based on average score.
1. Click on cell 22.
2. Enter the formula:
3. =HLOOKUP(H2,$M$1:$0$2,2, TRUE)
4. Press Enter.
5. Drag the fill handle from 2 down to I5.

Page 2 of 6

75
--- page 3 ---
Sol

Pivot Table steps
1. Enter the above data in Excel with proper column headings.
2. Select any one cell from the data table.
3. Click on the Insert tab.
4. Click on PivotTable. [1 MARKS]
5. A dialog box appears — click OK. [1 MARKS]
6. Inthe PivotTable Fields panel:
o Drag Course Name to the Rows area. [1 MARKS]
o Drag Fees to the Values area. [1 MARKS]
7. Make sure the Values field shows Sum of Fees. [0.5 MARKS]
8. The Pivot Table showing course-wise total fees is created.
Subtotal Steps
1. Selectthe entire data table.
2. Click on the Data tab.
3. Click on Sort. [1 MARKS]
4. Sort the data by Month Name and click OK.
5. Goto Data— Subtotal. [1 MARKS]
6. Inthe Subtotal dialog box:
o Ateach changein — Month Name
o Use function > Sum
o Add subtotal to — Fees
7. Click OK. [1 MARKS]
8. Course-wise subtotals are displayed in the worksheet.

Page 3 of 6

75
--- page 4 ---
ANSWER:

1) CEILINGQ Rounds a number up to the nearest multiple of a specified significance.
Syntax:
=CEILING(number, significance) Where:

number = Value to be rounded

significance = Multiple to which you want to round
Example:

=CEILING(17, 5) Output: 20

11) PVQ Calculates the present value of an investment or loan, i-e.. the current worth of future
payments.

Syntax:
=PV(rate, nper, pmt, [fv]. [type]) Where:
tate = Interest rate per period
nper = Total number of periods
pmt = Payment per peniod
fv = Future value (optional)
type = 0 (end of period), 1 (beginning)
Example:
Monthly EMI = @2.000, interest rate = 10% annually. period = 3 years:
=PV(10%/12. 36, -2000) Output: Present value of the loan.

ii1) DAYS360(Calculates the number of days between two dates based on a 360-day year (used in
financial calculations).
Syntax:
=DAYS360(start_date. end_date, [method]) Where:

start_date = Starting date

end_date = Ending date

method = FALSE (US method), TRUE (European method)
Example

=DAYS360("01-01-2026", "31-03-2026") Output: 90
iv) SMALLO Returns the k-th smallest value in a data set.
Syntax:
=SMALL(array, k) Where:

array = Range of values

k = Position (1 = smallest, 2 = second smallest, etc.)
Example:
If A1:A6 contain: 10, 25, 5, 30, 15, 20
=SMALL(A1-A6, 2) Output: 10 (second smallest number)

v)MIDO Extracts a specified number of characters from the middle of a text string.

Syntax:
=MID(text, start_num, num_chars) Where:
¢ text = Onginal text
¢ — start_num = Starting position
* = num_chars = Number of characters to extract
Example:
=MID("MICROSOFT", 3. 4) Output: CROS
[1.5 Marks for each subparts]

Page 4 of 6
--- page 5 ---
2.

Answer the following questions (Attempt Any 2 Questions)

Sol Step 1: Create the Worksheet
1. Enter the following column headings:
Al —- Player Name
Bl - Match 1
C1 - Match 2
D1 - Match 3
2. Enter the given data from Row 2 to Row 11.

Step 2: Calculate Best Average

3. In cell El, type: Best Average
4. Click on cell E2 and enter the formula:
=(SUM(B2:D2)-MIN(B2:D2))/2 _[2 MARKS]
5. Press Enter.
6. Drag the fill handle from E2 down to E11 to copy the formula. [0.5 MARKS]

Il) Step 3: Determine Result 1 (CONSISTENT / NOT CONSISTENT)

7. In cell F1, type: Result 1

8. Click on cell F2 and enter the formula:
=IF(AND(B2>=30,C2>=30,D2>=30),"CONSISTENT","NOT CONSISTENT")

9. Press Enter. [2 MARKS]

10. Drag the fill handle from F2 down to F11. [0.5 MARKS]

Step 4: Determine Result 2 (STAR PLAYER / NOT STAR)

11. In cell G1, type: Result 2
12. Click on cell G2 and enter the formula:
=IF(AND(B2>=40,C2>=40,D2>=40,E2>=60),"STAR PLAYER","NOT STAR")_
2 MARKS]
13. Press Enter.
14. Drag the fill handle from G2 down to G11. [0.5 MARKS]

Page 5 of 6

15

75

75
--- page 6 ---
Solution:
Step 1: Create a table in worksheet as follows:

A B
1 | Budget 500000
2 | Venue charges | 120000
3 | Decoration 80000
4 | Promotion 50000

5 | Reserve fund 250000

Step 2: Use formula to calculate Reserve fund= Budget— Venue charges- Decoration —
Promotion = B1 — B2 —- B3 - B4

Step 3: Click the data tab -> What if Analysis -> Scenario Manager.

Step 4: A scenario manager window will pop up then click add -> scenario name: Worst case.
Step 5: In option by changing cell -> click B2, B3, B4 -> ok

Step 6: Scenario values: B2 = 200,000, B3 = 1,20,000, B4 = 80,000.

Step 7: Click Summary -> In Result cell click BS. A table of summary is displayedin new
worksheet, 3.5 marks-----

Goal Seek

Step 1: Assume Venue charges = Rs 100,000, Given values -> Decoration= Rs. 80,000,
Promotion= Rs. 50,000.

Step 2: Calculate Reserve fund= Budget — Venue charges- Decoration — Promotion = B1-B2-
B3-B4

Step 3: Click on data tab -> What if Analysis -> Goal Seek.

Step 4: A dialogue box will appear. In set cell click BS -> with values 1,50,000 -> by changing
click B2.

Step 5: A dialogue box will appear -> after BS values get changed -> Click OK.

woeeee 3 marks

Solution:

SELECT D2 AND TYPE =B2*C2 AND DRAGIT TILL D4.

FIND THE TOTAL IN CELL B5 TYPE=SUM(B2:B4) AND IN D5 TYPE=SUM(D2:D4) (1 mark)
SELECT D5 AND FROM DATA TAB SELECT SOLVER. IN THE DIALOG BOX IN THE ‘SET
OBJECTIVE’ OPTION THE CELL D5 IS ALREADY SELECTED. (1 mark)

IN THE ‘TO’ OPTION SELECT ‘MAX?.

IN THE OPTION ‘BY CHANGING VARIABLE CELLS’ TEXT BOX ENTER B2:B4. (1 mark)

IN THE ‘SUBJECT TO CONSTRAINTS’ SELECT ADD OPTION.

IN ‘CELL REFERENCE’ TYPE B2 AND IN CONSTRAINTS TYPE >=10 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPE B3 AND IN CONSTRAINTS TYPE ==15 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPE B4 AND IN CONSTRAINTS TYPE <=25 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPE B5 AND IN CONSTRAINTS TYPE =60 AND CLICK ON OK. (1
mark)

THEN CLICK ON SOLVE. (0.5 mark)

Page 6 of 6

75
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 1d5fcfb05479

- Departments: Commerce
- Programmes: Bachelor of Commerce - 45611
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Re-Exam/Bachelor of Commerce - 45611/Advanced Excel/ANS_Re-Exam_Advanced Excel(NAAEX155)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 30; duration hours: 1; exam date: 20 Jun 2026
- Text: mixed (6 pages), mean OCR confidence 87.7

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Commerce
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Advanced Excel
Date: 20 Jun 2026   Time: 10:30 am - 11:30 am (01:00 Hrs.)
Max Marks: 30
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 6 pages
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume data wherever required
1.   Answer the following questions (Attempt Any 2 Questions)   15
a.   7.5
Page 1 of 6
--- page 2 ---
Solution
i) To Find the Highest Temperature in Column F 1.35 Mk
1. Click on cell F2.
2. Enter the formula:
3. =MAX(B2:E2)
4. Press Enter.
5. Drag the fill handle from F2 down to FS to copy the formula for all cities.

ii) To Find the Second Highest Temperature in Column G 1.5 Mk
1. Click on cell G2.
2. Enter the formula:
3. =LARGE(B2:E2,2)
4. Press Enter.
5. Drag the fill handle from G2 down to G5.

iii) To Calculate Average Temperature in Column H 1.5 Mk
1. Click on cell H2.
2. Enter the formula:
3. =AVERAGE(B2:E2)
4. Press Enter.
5. Drag the fill handle from H2 down to H5.

iv) To Assign Climate Level in Column I Using LOOKUP 3 Mk
1. Click on cell 12.
2. Enter the formula:
3. =VLOOKUP(H2,$L$2:$M$4,2, TRUE)
4. Press Enter.
5. Drag the fill handle from 2 down to I5.

Page 2 of 6

75
--- page 3 ---
SOL

Pivot Table Steps
1. Enter the above datain Excel with proper column headings.
2. Select any one cell from the data table.
3. Click on the Insert tab.
4. Click on PivotTable. [1 MARKS]
5. In the dialog box, click OK. [1 MARKS]
6. Inthe PivotTable Fields panel:
o Drag Food Item to the Rows area. [1 MARKS]
o Drag Calories to the Values area. [1 MARES]
7. Make sure it shows Sum of Calories. [0.5 MARKS]

8. The Pivot Table showing food-item wise total calories is created.

Subtotal Steps
1. Seleetthe entire data table.
2. Click on the Data tab.
3. Click on Sort. [1 MARES]
4. Sort the data by Day and click OK.
5. Goto Data — Subtotal. [1 MARKS]
6. In the Subtotal dialog box:
o Ateach changein — Day
o Use function — Sum
o Add subtotal to — Calories
7. Click OK. [1 MARKS]
8. Food-item wise subtotals are displayed.

Page 3 of 6

75
--- page 4 ---
2.

ANSWER:

i)FVQ : Calculates the future value of an investment or loan based on a constant interest rate.
and regular payments

Syntax:
=FV(rate, nper, pmt, [pv], [type]) Where:
rate = Interest rate per period
npex = Total number of periods
pmt = Payment made each period
pv = Present value (optional)
type = 0 (end of period), 1 (beginning)
Example:
Monthly investment = 22,000, interest rate = 8% annually, period = 3 years:
=FV(8%/12, 36. -2000)
Output: Future value of the investment.
11)Roundup() Rounds a number upward (away from zero) to a specified number of digits.
Syntax:
=ROUNDUP(number, num_digits)

Where:

number = Number to round
num_digits = Number of digits
Example: =-ROUNDUP(12.341, 2) Output: 12.35

iti)MAX(QReturns the largest value from a given set of numbers.
Syntax:

=MAX(number1, [number?], ...)

Example:

If cells A1:A6 contain: 15, 42, 28, 35, 50,21
=MAX(A1:A6) Output: 50

iv) TODAY ()Returns the current date.
Syntax:
=TODAY(O)

Example: =TODAY()
Output: 18-02-2026

v)TRIM():-Removes extra spaces from text, leaving only single spaces between words.
Syntax:
=TRIM(text)
Example:
If Al contains: " Data Analysis ”
=TRIM(A1) Output: Data Analysis
[1.5 Marks for each subparts]

Answer the following questions (Attempt Any 2 Questions)

Page 4 of 6

15
--- page 5 ---
Sol
(i) Best Average Price
Definition: Average of the highest two closing prices out of three days.
Steps:
1. Inserta new columnin Column E and name it Best Average Price.
2. Incell E2, enter the formula:

=(SUM(B2:D2)-MIN(B2:D2))/2 [2 MARKS]
3 Press Enter.
4 Drag the formula down from E2 toES. [0.5 MARKS]
. (ii) Result (Stable Stock)

1. Incell F2, type:
2. =IF(AND(B2>=100,C2>=100,.D2>=100),"STABLE","NOT STABLE")

[2 MARKS]

3. Press Enter.
4. Drag down from F2 to FS. [0.5 MARKS]

Gii) Number of companies whose Day 3 closing price is above 120
Steps:

1. Clickin any empty cell.
2. Type the formula=COUNTIF(D2:D5,">120") [2.5 MARKS]

Page 5 of 6

75

75
--- page 6 ---
Solution: Step 1: Create a table in worksheet as follows:

A B
1 | cost price 80
2 | selling price 200
3 | No. of units sold 30
4 | profit/unit 120
5 | Total profit 3600

wenee 1 mark-----
Step 2: Use formula to calculate profit/unit= SP - CP= B2-B1, Total Profit= No. of units sold
* profit/unit = B3*B4.

Step 3: Click the data tab -> What is Analysis -> Scenario Manager.

Step 4: A scenario manager window will pop up then click add -> scenario name: Best case.
Step 5: By changing cell -> click B2, B3.

Step 6: Scenario values: B2 = 250, B3 = 50.

Step 7: Click Summary -> For Result cell click B5. A table of summary is displayed in new
worksheet.

Goal Seek

Step 1: Assume SP= Rs 200, Given values -> CP= Rs 80, No. of units Sold = 50.

Step 2: Calculate Profit= SP-CP=B2-B1, Total profit= Profit * No. of units sold = B3*B4
Step 3: Click on data tab -> Whatif Analysis -> Goal Seek.

Step 4: atmos box will appear. In set cell click B5 -> with values 10,000 -> by changing
click B2.

Step 5: A dialogue box will appear -> after B5 values get changed. Click OK.

Solution:

SELECT D2 AND TYPE=B2*C2 AND DRAGIT TILL D4.

FIND THE TOTAL IN CELL B5 TYPE=SUM(B2:B4) AND IN D5 TYPE=SUM(D2:D4) (1 mark)
SELECT D5 AND FROM DATA TAB SELECT SOLVER. IN THE DIALOG BOX IN THE ‘SET
OBJECTIVE’ OPTION THE CELL D5 IS ALREADY SELECTED. (1 mark)

IN THE ‘TO’ OPTION SELECT ‘MAX?.

IN THE OPTION ‘BY CHANGING VARIABLE CELLS’ TEXT BOX ENTER B2:B4. (1 mark)

IN THE ‘SUBJECT TO CONSTRAINTS’ SELECT ADD OPTION.

IN ‘CELL REFERENCE’ TYPE B2 AND IN CONSTRAINTS TYPE >=50 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPE B3 AND IN CONSTRAINTS TYPE <=150 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPE B4 AND IN CONSTRAINTS TYPE >=80 AND CLICK ON ADD.
(1 mark)

IN ‘CELL REFERENCE’ TYPEB5 AND IN CONSTRAINTS TYPE=300 AND CLICK ON OK. (1
mark)

THEN CLICK ON SOLVE. (0.5 mark)

Page 6 of 6

75
````
