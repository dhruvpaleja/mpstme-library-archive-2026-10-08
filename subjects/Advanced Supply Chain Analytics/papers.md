# Advanced Supply Chain Analytics: question papers in full

3 unique papers · 2017-18 to 2018-19 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2018-19 · Final-Exam · paper 3143fd6732f5

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/ADVANCED SUPPLY CHAIN ANALYTICS/Advanced Supply Chain Analytics 2018-19 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 April 2019
- Text: ocr (3 pages), mean OCR confidence 93.4

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT &/2n

Programme: M. Tech Data Science (Business Analytics) Year:I Se
Academic Year: 2018-2019

Subject: Advanced Supply ¢ Chain Analytics

Marks: 100
Date: 26 April 2019 Time: 2.00 pm to 5.00 pm
So Durations: 3 (Hrs) ~

No. of Pages : Or
Final-Examination (2018-19)
€

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume suitable data if necessary.

Q-1 Go through the following case let (There are two questions that follow, each of ten marks):
. (Total: 20 marks)

During the last two decades, auto making has been transformed as manufacturers have outsourced
production of parts and components to outside contractors. Many of those suppliers have been
encouraged to cluster around assembly plants for quick pickup and delivery to the assembly line.
Automakers were in the vanguard among users of third party logistics services, hiring 3PLs to coordinate
just-in-time delivery of components sequenced for delivery within time windows as short as 15 minutes.
Some "transplant" factories went a big step further. Companies such as Toyota arranged international
supply chains to supply their U.S. plants with just-in-time delivery of components from Japanese
suppliers. Now automobile companies are pushing their supply chains farther overseas. "Just about
everything can be sourced overseas." said Mixer. An auto analyst at Global Insight. "China is supplying
engines to the Chevy Equinox, for example." It is observed that a decade ago, 60 percent of the value
of an average North American vehicle was created by outside suppliers. Now that percentage is
between 65 and 68 percent. "By 2015, between 76 and 78 percent of the average vehicle's value will be
delivered by the automobile supply chain," he said. "As the supplier base adds more value, the brand
owners are gradually adding less value." Although no statistics are available. It is observed that a
growing portion of that value comes from suppliers in other countries, and that in the future, "There
will be a lot less assembly and less manufacturing in the U.S. Domestic automakers will still design and
engineer new products, market them, and manage after-sale relationships with customers, but that

V/s
--- page 2 ---
automakers will follow the lead of makers of personal computers and cell phones and use final assembly
points mainly for customization to meet fickle consumer demand. "The new product must have
something new and unique," Mixer said. "It's driven by marketing, like a cell phone that has new
features is driven by marketing." Beth Enslow, vice president of enterprise research at Aberdeen Group,
said international sourcing offers savings but adds complexity. "When the shipment misses the boat
overseas, there may not be another boat for another seven or 14 days after that," she said.

Longer supply chains are a special headache for automakers, who may have more suppliers than any
other industry, Mixer said. Automakers such as Ford and General Motors have between 4.000 and 6,000
production suppliers, as well as 180 "prime production suppliers." The average vehicle has more than
40,000 individual parts, he said.

Q-1 a) Are there any potential risk associated with too much emphasis on outsourcing? (10 marks)

Q-1 b) What steps in SCM Analytics can help US automakers do to manage increasing complexity in
their supply chains and out-do any outsourcing risks? (10 marks)

Q-2 You are chief data scientist at wine distribution company outside India wherein you may sell wine
over online portals including home delivery or a retail model or a mix of both. Your organization is
considering an online distribution portal for the wines along with traditional retail model. Discuss the
ideas that managers should consider to make better supply chain network design decisions under
uncertainty and how analytics may help in each of the case or options you consider. (20 marks)

Q-3 a) The XYZ Company has a choice between two warehouses. A lease at location A costs $1000 per
month with a payment of $2000 up front to guarantee the 3 year lease. Location B would cost $1200
per month and would be leased from month to month. The anticipated revenue in either location is
$1500 per month. The estimated rate of return is 10% per year. Using net present value, determine
which location would be the better choice. (10 marks)

Q-3 b) DMart needs 1000 coffee makers per year. The cost of each coffee maker is INR 7800. Ordering
cost is INR 106 per order. Carrying cost is 1% of per unit cost. Lead time is 5 days. DMart is open 365
days/yr. What is the optimal order quantity & ROP (Reorder Point- Demand over lead time)? (10 marks)

Q-4 While working at Amazon analytics services, you have three areas where you have to suggest
analytical strategies and techniques. The areas are:
1. Anticipatory Shipping Model

2. Price Optimization
3. Personalized Recommendation System
Elaborate the algorithms and key operational measures that may help Amazon fully harness the

analytics capabilities (20 marks)
--- page 3 ---
Q-5 Complete the code which tries to optimize a network flow in supply chain
the code with blanks filled in marked as res

proc optmodel;
/* declare sets and parameters */
___ ?? ORIGINS = /Chicago Detroit/;
set DESTINATIONS = /Boston Newark Toronto/;
num supply {ORIGINS} = [200 150];
num demand {DESTINATIONS} = [50 150 100];
___?? unit_cost {ORIGINS, DESTINATIONS} =

[40 25 15 30 15 10];

/* declare variables */
2? NumShip {ORIGINS, DESTINATIONS} >= 0;

?? FlowOut {i in ORIGINS} =
sum {j in DESTINATIONS} NumShip[i,j];
2? Flowin {j in DESTINATIONS} =
sum {i in ORIGINS} NumShip{i,j];

/* declare constraints */
?? Supply_con {i in ORIGINS}:

FlowOut{[i] <= 2?
?? Demand_con {j in DESTINATIONS}:
FlowIn{[j] >= ??

/* declare objective */
2? TotalCost = sum {i in ORIGINS, j in DESTINATIONS}

unit_cost[i,j] * ??
save ?? transport;
quit;

Q-6 Write a short note on each technique with applications in SCM.
1. Support Vector Machines
2. Neural Networks
3. Random Forrest
4. CHAID/CART

. You have to rewrite
(20 marks)

(20 marks)
````

## 2017-18 · Final-Exam · paper 83737de35c38

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/ADVANCED SUPPLY CHAIN ANALYTICS/Advanced Supply Chain Analytics 2017-18 Final.pdf`
- Printed on paper: max marks: 70; duration hours: 3; exam date: 17 May 2018
- Text: ocr (2 pages), mean OCR confidence 92.5

````text
SVKM’s NMIMS “aie
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT seExconserang
4 d ~ bs

fot” ‘io
Programme:M.Tech DATA SCIENCE Year: I Se = @Ster: Fall Sem IP a
vat ;
Academic Year: 2017-2018 =~ Jj
Va uA 4é
Subject:Advanced Supply Chain Analytics ig hang aee™
: Marks:70
Date:17 May 2018 Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs) _
No. of Pages :_2
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No.__1__ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall__5___ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume -suitable data if necessary.

Qu!. Read the caselet enclosed and answer the questions given at the end of the case . (14 marks)
Qu. 2(a) A company makes standard 110 inch wide rolls of thin sheet metal and slits them into smaller rolls to meet
customer orders for width of 12, 15 and 30 inches. The demand for these widths vary from week to week.

From a 110 inch roll, there are many different ways to slit 12, 15 and 30 inch pieces. A cutting pattern is a
configuration of the number of smaller rolls of each type that are cut from the raw stock but each cutting pattern

generates a different scrap which needs to be minimized. (7 marks)

Pattern 12 inch 15 inch 30 inch Scrap

1 0 7 0 5

2 0 1 3 5

3 1 0 3 8

4 9 0 0 2

5 2 1 2 11

6 7 1 0 11

Demand for the coming week are : 500 for 12 inch roll , 715 for 15 inch roll, 630 for 30 inch roll.
How many 110 inch rolls to be cut into each of the six patterns in order to meet the demand and reduce the scrap?

Qu.2(b) Explain the following Forecasting methods in brief with example(any two) (7 marks)
Holt winters Method, Croston’s Algorithm , Mean Linear Regression

Qu. 3(a) Explain Sales and Operations Planning and Aggregate Planning process with steps. (7 marks)

PAGE 1/2
--- page 2 ---
Qu. 3(b) Briefly explain different scheduling Algorithms /Heuristics with your Data . (7 marks)

Qu.4(a) A purchaser for Infinity Mall has to decide on the quantity of a high priced hand bag which is (7 marks)
procured from Italy for the next New Tear season. The unit cost of the handbag to the store is $ 25

and the handbag will sell at $ 140. Handbags that remains unsold during the season can be sold to a discount shop at

$20. Historical Data shows that the handbag sales has a Normal distribution with Mean 150 and standard deviation

of 20. What is the optimal number number of bags to be purchased ?

Qu.4(b) Explain Part Period Balancing and Least Cost method of Ordering with your own example . (7 marks)
Qu5. Write short notes on any four of the following (14 marks)

a) Cross Docking

b) Postpdnment and Mass Customization

c) Bull whip effect

d) Lean system and Value Stream Mapping
e) Distribution Resource Planning

f) Efficient and Responsive Supply Chain

Qué. (a) The supply of a special product has the following price schedule : (7 marks)

0-99 items ....Rs. 1000 100 items andabove Rs. 950
The inventory holding costs are estimated to be 30% of the value of the inventory . The ordering cost is estimated to
be Rs. 3000 per order . If the annual requirement is 400, Compute the Economic Order Quantity and the Total Cost.

Qu.6(b) The same vendor is proposing that EOQ Quantity be increased by 10% and he is willing to give a price
discount of 2% . Analyze the proposal critically. (7 marks)

Qu. 7(a) AnAsian Paint Retailer has the following demand for an item (SKU) with Mean demand /day 30 cans with a
Standard deviation of 5. The Lead Time for receiving a new order is 10 days . Determine the Reorder Point
and safety stock if the store wants a service level of 95% with the probability of stockout equals to 5%. (7 marks)

Qu7(b) Mr. Lev Yasin , Manager of a Football Club wants to order a particular type of Jersey for the Team
members . He has made the following demand estimate

Demand Probability Cumulative Probability
80 0.20 0.20

81 0.25, 0.45

90 0.25, 0.70

100 0.20 0.90

110 0.10 1.00

His supplier is giving the Jersey at $7 but he intends to sell them at $23. If any Jersey remains unsold , they can
be sold at $2 to a nearby store. How many Jersey Mr. Lev Yasin should order ? (7 marks)

PAGE 2/2.
````

## 2017-18 · Re-Exam · paper d21613e7040b

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/ADVANCED SUPPLY CHAIN ANALYTICS/Advanced Supply Chain Analytics Batch 2017-18 Re Exam.pdf`
- Printed on paper: exam date: 02 July 2018
- Text: ocr (4 pages), mean OCR confidence 90.1

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M.Tech Data Science Year: I Semester: Fall Sem II
Batch: 2017-18

Academic Year: 2017-2018
Subject: Advanced Supply Chain Analytics

Date: 02 July 2018

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. ___1__ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall__5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qul. Read the caselet enclosed and answer the questions given at the end of the case . (14 marks)

Qu.2 (a) A purchaser for Infinity Mall has to decide on the quantity of 4 high priced hand bag which is (7 marks)
procured from Italy for the next New Tear season. The unit cost of the handbag to the store is $ 25

and the handbag will sell at $ 140. Handbags that remains unsold during the season can be sold to a discount shop at

$20. Historical Data shows that the handbag sales has a Normal distribution with Mean 150 and standard deviation

of 20. What is the optimal number number of bags to be purchased ?

(b) Explain Part Period Balancing and Least Cost method of Ordering with your own example . (7 marks)
Qu3. Write short notes on any four of the following - ( 14 marks)

a) Cross Docking

b) Postponment

c) Bull whip effect

d) Lean system and Value Stream Mapping
e) Distribution Resource Planning

f) Efficient and Responsive Supply Chain

Qu4. (a) The supply of a special product has the following price schedule : (7 marks)
0-99 items ....Rs. 1000 100 items andabove Rs. 950

The inventory holding costs are estimated to be 30% of the value of the inventory . The ordering cost is estimated to

be Rs. 3000 per order . If the annual requirement is 400, Compute the Economic Order Quantity and the Total Cost.

PAGE Ys
--- page 2 ---
Qu.4(b) The same vendor is proposing that EOQ Quantity be increased by 10% and he is willing to give a price
discount of 2% . Analyze the proposal critically. (7 marks)

Qu. 5(a) AsAsian Paint Retailer has the following demand for an item (SKU) with Mean demand /day 30 cans with a
Standard deviation of 5. The Lead Time for receiving a new order is 10 days . Determine the Reorder Point
and safety stock if the store wants a service level of 95% with the probability of stockout equals to 5%. (7 marks)

Qu5(b) Mr. Lev Yasin , Manager of a Football Club wants to order a particular type of Jersey for the Team
members . He has made the following demand estimate

Demand Probability Cumulative Probability
80 0.20 0.20
81. 0.25, 0.45
90 0.25, 0.70
100 0.20 0.90
{110 0.10 * 1.00

His supplier is giving the Jersey at $7 but he intends to sell them at $23. If any Jersey remains unsold , they can
be sold at $2 to a nearby store. How many Jersey Mr. Lev Yasin should order ? (7 marks)

Qu. 6(a) A company makes standard 110 inch wide rolls of thin sheet metal and slits them into smaller rolls to meet
customer orders for width of 12, 15 and 30 inches. The demand for these widths vary from week to week.

From a 110 inch roll, there are many different ways to slit 12, 15 and 30 inch pieces. A cutting pattern is a
configuration of the number of smaller rolls of each type that are cut from the raw stock but each cutting pattern

generates a different scrap which needs to be minimized. (7 marks)

Pattern 12 inch 15 inch 30 inch Scrap
1 0 7 0 5

2 0 1 3 5

3 1 0 3 8

4 9 0 0 2

5 2 1 2 ll

6 7 1 0 ll

Deweand for the coming week are : 500 for 12 inch roll, 715 for 15 inch roll, 630 for 30 inch roll.
How many 110 inch rolls to be cut into each of the six patterns in order to meet the demand and reduce the scrap?

Qu.6(b) Explain the following Forecasting methods in brief with example(any two) (7 marks)

Holt winters Method, Croston’s Algorithm , Mean Linear Regression
Qu. 7(a) Explain Sales and Operations Planning and Master Planning process with steps. (7 marks)

Qu. 7(b) Briefly explain any four scheduling Algorithms /Heuristics with your Data . (7 marks)

PAGE of
--- page 3 ---
Chapter 12 * Managing Uncertainty in a Supply Chain: Safety Inventory 373

ene
+ COst
Case Study 1
t Orion | Managing Inventories at ALKO Inc.
annual a F . . +
ALKO began in 1943 in a garage workshop set up by The Current Distribution System
John Williams at his Cleveland home. John had always 5
Ponent . y — ee ome onn WAYS The task force noted that ALKO had 100 products in its
riants? enjoyed tinkering, and in February 1948 he obtained a : . pan
. “ ma Mann Pas tiaintiens 2009 line. All production occurred at three facilities located
\crease patent for one of his designs for lighting fixtures. He :
ae . 5 Rs _ in the Cleveland area. For sales purposes, the contiguous
onality decided to produce it in his workshop and tried market- i reed eee : :
Soe . . ; United States was divided into five regions, as shown in
; ing it in the Cleveland area. The product sold well, and Fi 12-7. A DC d by ALKO operated in eacl
onallity by 1957 ALKO had grown to a $3 million company. Its eure te OMNES ee Operaiee' ip sacs
lichtine fixtures were well known for their ovtstandin of these regions. Customers placed orders with the DCs,
ponent i — then it sold a total of five products 8 which tried to supply them from product in inventory. As
8. How ane “fn John took the compan pole Since then the inventory for any product diminished, the DC in turn
chieve | ks, as examen! pee : ordered from the plants. The plants scheduled production
olding i lesa nas been very successiul, nd the company has based on DC orders. Orders were transported from plants
tified? Staudell tshiitnating tie jpooeiiie AAUOMRCE, de RERTPE to the DCs in TL quantities because order sizes tended to
ss the tition intensified in the 1980s, ALKO introduced many que . " ——

be large. On the other hand, shipments from the DC to
the customer were LTL. ALKO used a third-party trucking
company for both transportation legs. In 2009, TL costs
from the plants to DCs averaged $0.09 per unit. LTL ship-
ping costs from a DC to a customer averaged $0.10 per
unit. On average, five days were necessary between the
time a DC placed an order with a plant and the time the
order was delivered from the plant.

The policy in 2009 was to stock each item in every
DC. A detailed study of the product line had shown that
there were three basic categories of products in terms of
the volume of sales. They were categorized as types High,
Medium, and Low. Demand data for a representative prod-
uct in each category is shown in Table 12-8. Products |,
3, and 7 are representative of High, Medium, and Low
demand products, respectively. Of the 100 products that
ALKO sold, 10 were of type High, 20 of type Medium,
and 70 of type Low. Each of their demands was identical to
those of the representative products |, 3, and 7, respectively.

new lighting fixture designs. The company’s profitability,
however, began to worsen despite the fact that ALKO
had taken great care to ensure that product quality did
not suffer. The problem was that margins had begun to
shrink as competition in the market intensified. At this
point, the board decided that a complete reorganization
was needed, starting at the top. Gary Fisher was hired to
reorganize and restructure the company.

When Fisher arrived in 2009, he found a comipa-
ny teetering on the edge. He spent his first few months
trying to understand the company business and the way
it was structured. Fisher realized that the key was in
the operating performance. Although the company had
always been outstanding at developing and producing
new products, it had historically ignored its distribution
system. The belief within the company was that once you
hain make a good product, the rest takes care of itself. Fisher
vie set up a task force to review the company’s current dis-

ckard rae a 1
n for tribution system and come up with recommendations.

Burr
‘A).”

uory
New

eds.
ston:

sly.”
02):

iton:

FIGURE 12-7 Sales Regions for ALKO
--- page 4 ---
374 Chapter 12 + Managing Uncertainty in a Supply Chain Safety Inventory

| Distribution of Daily Demand at ALKO

Region 1 Region 2 Region 3 Region 4 Region 5 S|
Part 1M 35.48 22.61 17.66 11.81 3.36 Pi
Part 1 SD 6.98 6.48 5.26 3.48 4.49 :
Part3M 2.48 4.15 6.15 6.16 7.49 1 O
Part 3 SD 3.16 6.20 6.39 6.76 3.56 4 ot
Part 7M 0.48 0.73 0.80 1.94 2.54

Part 7 SD 1.98 1.42 2.39 3.76 3.98
te
fe
The task force identified that plant capacities allowed (four days for production + one, day in transit). Given s

any reasonable order to be produced in four days. Thus, the increased average distance, however, the outbound

: C
a plant shipped out an order four days after receiving it. transportation cost to customers from the NDC would j

Ic
After one day in transit, the order reached the DC. The re- increase to $0.24 per unit. u
plenishment lead time was thus five days. The DCs ordered Other possibilities the task force considered include a
using a periodic review policy with a reorder interval of building a national distribution center while keeping 9
six days. The holding cost incurred was $0.15 per unit per — the regional DCs open. In this case, some products would
day whether the unit was in transit or in storage. All DCs be stocked at the regional DCs, whereas others would be t
carried safety inventories to ensure a CSL of 95 percent. stocked at the NDC. t
Fisher's Decision :
Alternative Distribution Systems l
Gary Fisher pondered the task force report. It had not t
The task force recommended that ALKO build a national detailed any of the numbers supporting the decision. He U
distribution center (NDC) outside Chicago. The task — qocided to evaluate the numbers before making his decision. t
force recommended that ALKO close its five DCs and . {
move all inventory to the NDC. Warehouse capacity was Questions \
measured in terms of the total number of units handled 1. What is the annual inventory and distribution cost of the cur- '
per year (L.e., the warehouse capacity was given in terms rent distribution system?
of the pai demand supplied from the warehouse). The 2+ What are the savings that would result from followi
cost of constructing a warehouse is shown in Figure 12-8. task force recommendation and setting up an NDE’ \
However, ALKO expected to recover $50,000 for each ate the savings as the correlation coefficient of demand in

warehouse that it closed. The CSL out of the NDC would any“ Pauro! meetons varies ec Oro Oh tO. Do yauwres
. ommend setting up an NDC?
continue to be 95 percent. . 3. Suggest other options that Fisher should consider, Evalu-
Given that Chicago is close to Cleveland, the ate cach option and recommend a distribution system for
inbound transportation cost from the plants to the NDC ALKO that would be most profitable. How dependent is
would fall to $0.05 per unit. The total replenishment

your recommendation on the correlation coefficient of de-
lead time for the Chicago NDC would still be five days mand across different regions’?

1400000
Z 1200000
& 1000000
% 800000
A 600000
400000,
200000
0 1 ! L ! !
0 200 400 600-800-1000 1200

Thousands of Units Sold Through DC
FIGURE 12-8 Construction Costs for NDC
````
