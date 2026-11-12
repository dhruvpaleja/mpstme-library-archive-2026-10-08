# Supervisory Control and Data Acquisition: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d5702cd3168a

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a   Explanation of the different debugging processes in LabVIEW.   (05)
2;
SO-
1 ;   Fixing Broken VIs
BL-
2
If a VI does not run, it is a broken, or nonexecutable, VI. The Run button appears broken
when the VI you are creating or editing contains errors..
Broken Run Button
Generally, this means that a required input is not wired, or a wire is broken. Press the
broken Run button to access the Error list window. The Error list window lists each error
and describes the problem. You can double-click an error to go directly to the error.
Warnings do not prevent you from running a VI. They are designed to help you avoid
potential problems in VIs. Errors, however, can break a VI. You must resolve any errors
before you can run the VI.
Finding Causes for Broken VIs
Click the broken Run button or select View>>Error to find out why a VI is broken. The
Error list window lists all the errors. The Items with errors section lists the names of all
items in memory, such as VIs and project libraries that have errors. If two or more items
have the same name, this section shows the specific application instance for each item.
The errors and warnings section lists the errors and warnings for the VI you select in the
Items with errors section. The Details section describes the errors and in some cases
********** 1 **********
--- page 2 ---
recommends how to correct the errors. Click the Help button to display a topic in the
LabVIEW Help that describes the error in detail and includes step-by-step instructions for
correcting the error.
Click the Show Error button or double-click the error description to highlight the area on
the block diagram or front panel that contains the error.
Figure 1: The Error list dialog box lists each error and describes the problem.
Common Causes of Broken VIs
The following list contains common reasons why a VI is broken while you edit it:
▪ The block diagram contains a broken wire because of a mismatch of data types or a
loose, unconnected end. Refer to the Correcting Broken VIs topic of the LabVIEW Help
for information about correcting broken wires.
▪ A required block diagram terminal is unwired. Refer to the Using Wires to Link Block
Diagram Objects topic of the LabVIEW Help for information about setting required
inputs and outputs.
▪ A subVI is broken or you edited its connector pane after you placed its icon on the
block diagram of the VI.
Back to top
********** 2 **********
--- page 3 ---
Fixing Incorrect Behavior
If your VI runs but produces incorrect results then you have a functional error in your
code. LabVIEW provides several tools to help you analyze where your VI is not behaving
as expected.
Block Diagram Toolbar
When you run a VI, buttons appear on the block diagram toolbar that you can use to
debug the VI. The following toolbar appears on the block diagram.
Click the Highlight Execution button to display an animation of the block diagram
execution when you run the VI. Notice the flow of data through the block diagram. Click
the button again to disable execution highlighting.
Highlight Execution
Execution highlighting shows the movement of data on the block diagram from one
node to another using bubbles that move along the wires. Use execution highlighting in
conjunction with single-stepping to see how data values move from node to node
through a VI.
Note: Execution highlighting greatly reduces the speed at which the VI runs.
********** 3 **********
--- page 4 ---
Figure 2: Execution highlighting shows the movement of data.
You can pause the execution of a VI at any time by choosing the pause button on the
toolbar.
Execution Pause
The color of the button turns to red when the VI is paused. Once you pause the VI, you
can use the tools below to gain additional insight into the execution of your application.
Click the Retain Wire Values button to save the wire values at each point in the flow of
execution so that when you place a probe on the wire you can immediately retain the
most recent value of the data that passed through the wire.
Retain Wire Values
You must successfully run the VI at least once before you can retain the wire values.
Click the Step Into button to open a node and pause.
Step Into
When you click the Step Into button again, it executes the first action and pauses at the
next action of the subVI or structure. You also can press the ctrl and down arrow keys.
Single-stepping through a VI steps through the VI node by node. Each node blinks to
denote when it is ready to execute.
Click the Step Over button to execute a node and pause at the next node.
Step Over
You also can press the ctrl and right arrow keys. By stepping over the node, you execute
the node without single-stepping through the node.
Click the Step Out button to finish executing the current node and pause.
Step Out
When the VI finishes executing, the Step Out button is dimmed. You also can press the
ctrl and up arrow keys. By stepping out of a node, you complete single-stepping through
the node and navigate to the next node.
********** 4 **********
--- page 5 ---
The Warning button appears if a VI includes a warning and you placed a checkmark in
the Show Warnings checkbox in the Error list window.
Warning
A warning indicates there is a potential problem with the block diagram, but it does not
stop the VI from running.
Probe Watch Window
Use the Probe tool (View>>Probe Watch Window) to check intermediate values on a
wire as a VI runs. Move your cursor over a wire while the VI is running or right-click on
the wire and choose Probe to generate a probe. Use the Probe tool if you have a
complicated block diagram with a series of operations, any one of which might return
incorrect data. Use the Probe tool with execution highlighting, single-stepping, and
breakpoints to determine if and where data is incorrect. If data is available, the probe
immediately updates and displays the data in the Probe Watch Window during execution
highlighting, single-stepping, or when you pause at a breakpoint.
Figure 3: The Probe Watch Window displays any and all probes active in your project.
When execution pauses at a node because of single-stepping or a breakpoint, you also
can probe the wire that just executed to see the value that flowed through that wire.
Breakpoint Manager
You can use the Breakpoint Manager (View>>Breakpoint Manager) to view, add, or
delete breakpoints from your code. A breakpoint will pause the execution of the VI when
that specific object is executed. You can place a VI, structure, wire, or operator.
********** 5 **********
--- page 6 ---
Figure 4: You can use the Breakpoint Manager to add, delete, or view breakpoints in
your code.
CO-   b   Explanation of for loop in LabVIEW :   (05)
3;
SO-   FOR LOOPS
1 ;   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
BL-4
LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The For
Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop from the
palette and use the cursor to drag a selection rectangle to create a new For Loop or around the section
of the block diagram you want to repeat. You also can place a While Loop on the block diagram,
right-click the border of the While Loop, and select Replace with For Loop from the shortcut menu to
change a While Loop to a For Loop.
********** 6 **********
--- page 7 ---
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat the
subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top side of
the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is explained in chapter
5. A VI will not run if it contains a For Loop that does not have a numeric value wired to the count
terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations. The
iteration count always starts at zero. During the first iteration, the iteration terminal returns 0. Figure
4.2 shows a simple For Loop which generates 10 random numbers and displays in the Random Number
Indicator.
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- c   Explanation of Local variable   (05)
1;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a
local variable are right-click on an object’s terminal and select Create»Local Variable. A local
variable icon for the object appears on the block diagram as shown in Figure 4.23.
********** 7 **********
--- page 8 ---
(2.5)
d. Outline the objectives of Data Acquisition System.
Ans: Objectives of Data Acquisition System
1. It must acquire the necessary data, at correct speed and at the correct time.
CO-   2. Use of all data efficiently to inform the operator about the state of the system.
3 ;   3. It must monitor the complete plant operation to maintain on-line optimum and safe operations.
SO-   4. It must be able to collect, summarize and store data for diagnosis of operation and record purpose.
1 ;   (05)
5. It must be able to compute unit performance indices using online, real-time data.
BL-   6. It must be flexible and capable of being expanded for future require.
1   7. It must be reliable, and not have a down time greater than 0.1%.
8. It must provide an effective human communication system and be able to identify problem areas, there by
minimizing unit availability and maximizing unit through point at minimum cost.
Any 05 points from above (or any other suitable points)   1*05=05
Q.2
CO- a   Explanation of the three methods of grounding of DAQ devices.   (07)
4;
SO-   Having selected an appropriate board based on the resolution required, speed, etc., the next
1 ;   issue the user has to address is the type of connection to use.
BL-   The selection of input type is intimately linked to the issue of grounding and is discussed
2
together in some detail. As is mentioned earlier, there are three ground points to consider:
(i) Safety Ground: This is connected to the ground of the mains. As the name implies this
is a safety line and is not suitable for signal lines.
(ii) Digital Ground: This is a signal ground defined for digital signals and should be used
as such. Connecting analog signals to this line is not desirable.
(iii) Analog Ground or Reference: This is also referred to as signal ground. This is the
ground to be used with all the analog signals.
Grounding considerations can form the text matter for a book by itself. Let us consider the
various types of connections in detail. The interface card has the safety (or system) ground,
analog ground, digital ground and the signal sense (analog reference) lines. The analog and
digital grounds are connected to the safety ground at some (ideally only one) point.
There are three options available (National Instruments nomenclature in parentheses):
1. Differential (Differential—DI)
2. Referenced to a common signal reference (Non-Referenced Single Ended—NRSE)
3. Referenced to the safety ground (Referenced Single Ended—RSE)
********** 8 **********
--- page 9 ---
Figure 4.4 Differential Connection.
The multiplexer is in two halves which are operated in a linked pair for differential input.
For the other two connections, the multiplexer is connected as a single body. This
immediately brings out the main drawback in the DI connection. Half the input channels
are lost to the user, i.e., a 16-channel board when used in a differential configuration
can accept at most 8 inputs. It is good practice to ground the unused input connections,
though one must add that this advice is more often than not followed in the breach. The
configuration of the multiplexer and the various signal lines in a differential connection is
shown in Fig. 4.4 For a 16-channel board, the input lines corresponding to channel n are n
and (n + 8) pin numbers. As has been stated earlier, the board capacity in terms of the
number of channels is reduced by a factor of two. Any signal arriving on both the input
lines (common-mode signal) will be rejected by the amplifier which is set up to operate as
a differential amplifier. The output of the amplifier is referenced to the analog ground. The
signal sense line is not used. In this configuration, the safety ground of the system will at
some point be connected to the signal ground. For the average user, some simple thumb
rules can be prescribed:
The differential configuration is by far the best from the noise point of view. However, the
loss of 50% capacity in terms of the number of channels is a serious handicap.
The DI connection is the only one useable for floating signals, as is invariably the case in
bridge connections. Also, for low-level signals, e.g., thermocouple (typical output 6–50μ
V/°C), the differential connection is the only one suitable due to noise considerations. In
many transducers which are now available with built-in electronics (e.g., dc–dc LVDTs),
the signals are floating and hence have to be used with the DI connection.
********** 9 **********
--- page 10 ---
Figure 4.5 NRSE Connection.
Differences between the NRSE and RSE signals are more subtle. These are illustrated in
figures 4.5 and 4.6, respectively. Close examination would reveal the following. First, the
two halves of the multiplexer are operating as a single unit providing the full complement
of 16 channels. Second, while in NRSE all signals are referenced to the signal sense (or
common) line, in RSE the signal ground is used instead. Consequently, in an NRSE or RSE,
the user loses the benefit of rejection of the common-mode signal. In RSE the risk of ground
loops is far higher.
Figure 4.6 RSE Connection.
CO- b Write a note on Polymorphism in Array Operations.   (07)
3;
SO-   By definition polymorphism is said to be the ability of a numeric function to adjust to input data of
1 ;
BL-   different data structures. Polymorphism of LabVIEW is applicable to arrays as well. Hence, one can
2   add a scalar to an array or add two arrays using the same function. It is important to note that for the
********** 10 **********
--- page 11 ---
same function different types of operations are performed for different combinations. For example, if
a scalar and an array are added, the scalar is added to each element of the array. However, when two
arrays are added, each element of one array is added to the corresponding element of the other array.
All LabVIEW arithmetic functions are polymorphic. This means that the inputs to these functions can
be   different   data   structures   such   as   scalar   values   and   arrays.
For example, the Add function can be used in the following ways.
1. Scalar + Scalar = Scalar addition.
2. Scalar + Array = The scalar is added to each element of array.
3. Array + Array = Each element of one array is added to the corresponding element of other array.
********** 11 **********
--- page 12 ---
Figure 5.15 (a) Adding two scalar values, (b) adding a scalar value with an array, (c) adding two arrays of the
same size and (d) adding two arrays of different sizes.
In Figure 5.15(a), two scalar values are added which results in a scalar output. In Figure 5.15(b), an
array is added with a scalar value. The function adds the scalar value to each element of the array and
returns the array output. In Figure 5.15(c), two arrays are added. The function adds each element of
one array to the corresponding element of the other array and returns the array output. In Figure 5.15(d),
two arrays of different sizes (i.e. number of elements) are added. The function adds corresponding
elements and returns the output array, with the size of the smaller input array. The first array consists
of three elements and the second consists of four elements. First three elements of both the arrays are
added. The fourth element of the second array is not considered. Polymorphism does not perform matrix
arithmetic when inputs are two-dimensional arrays (for example, two two-dimensional array inputs to
a multiply function do element by element multiplication, not matrix multiplication).
CO- c   Explanation of the common standards of serial port communication   (06)
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse,
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections
between PC serial ports and devices. RS-232 is the connector found on most PCs. This is a
single-ended communication method where only one device can be connected per port. Two
connector types are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and
multidrop capability make RS-485 an attractive choice in industrial applications that require
many distributed devices networked to a PC or other controller for data collection and other
operations.
Q.3
CO- a   Explanation of Measurement and Automation Explorer in detail.   (07)
4;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all device
1 ;   and channel configuration parameters. After installing a DAQ device in the computer, you must
BL-   run this configuration utility. MAX reads the information the Device Manager records in the
2
Windows Registry and assigns a logical device number to each DAQ device. Use the device
number to refer to the device in LabVIEW. Access MAX either by double-clicking the icon on
the desktop or selecting Tools»Measurement & Automation Explorer in LabVIEW. The device
parameters that you can set using the configuration utility depend on the device. MAX saves
the logical device number and the configuration parameters in the Windows Registry. The plug
and play capability of Windows automatically detects and configures switchless DAQ devices,
such as the PCI-6024E. When you install a device in the computer, the device is automatically
detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation of
********** 12 **********
--- page 13 ---
NI-DAQ. MAX is used primarily to configure and test National Instruments hardware, but it
offers other functionality, such as checking to see if you have the latest version of NI-DAQ
installed. The functionality of MAX is divided into four categories—Data Neighborhood,
Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc., which
may have been installed. Devices and Interfaces lists various options like DAQ boards (under
DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc. The Legacy option
has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred. The
Software function helps to launch and update various software items from NI. Remote Systems,
which is a top-level option, at par with My System, provides access to various DAQ systems
connected through the Ethernet, or other parts.
CO- b   Explanation of data types and the importance of them with colors in LabVIEW programs   (06)
2;
SO-   Data Type   Details   Color
1 ;   Boolean   Booleans have   only   two   possible Green
BL-
values: True or False .
2
Integers   Integers can   Blue
be signed or unsigned whole numbers
Doubles   Doubles and Singles are signed numbers Orange
with a decimal component
Strings   Strings are sequences of characters   Pink
Clusters   Clusters are groups of various data Thick Brown
types
Path   Path is location of file on local PC Dark Green
System
CO- c   Explanation of the basic difference between the traditional instruments and software-based (07)
1;   virtual instruments.
SO-   Block diagram   (02)
1 ;
********** 13 **********
--- page 14 ---
BL-
2   A traditional instrument is designed to collect data from an environment, or from a unit under
test, and to display information to a user based on the collected data. Such an instrument may
employ a transducer to sense changes in a physical parameter such as temperature or pressure,
and to convert the sensed information into electrical signals such as voltage or frequency
variations. The term “instrument” may also cover a physical or software device that performs
an analysis on data acquired from another instrument and then outputs the processed data to
display or recording means. This second category of instruments includes oscilloscopes,
spectrum analyzers and digital millimeters. The types of source data collected and analyzed by
instruments may thus vary widely, including both physical parameters such as temperature,
pressure, distance, light and sound frequencies and amplitudes, and also electrical parameters
including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements defines
general-purpose measurement and   control hardware   functionality. With   virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have used
virtual instrumentation to downsize automated test equipment (ATE) while experiencing up to
a several times increase in productivity gains at a fraction of the cost of traditional instrument
solutions. Virtual instrumentation is necessary because it is flexible. It delivers instrumentation
with the rapid adaptability required for today’s concept, product and process design,
development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of features
that are rarely, if ever used. Most conventional instruments do not have any computational
power as compared to a virtual instrument. Since the virtual instrument is part of a person
computer configuration, the personal computer’s computational as well as controlling
capability can be applied into a test configuration. Virtual instruments are compatible with
traditional instruments almost without exception. Virtual instrumentation software typically
provides libraries for interfacing with common ordinary instrument buses such as GPIB, serial
or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt the
instrument to our particular needs. A traditional instrument might contain an integrated circuit
to perform a particular set of data processing functions; in a virtual instrument, these functions
would be performed by software running on the PC processor. We can extend the set of
functions easily, limited only by the power of the software used. By employing virtual
instrumentation solutions, we can lower capital costs, system development costs, and system
maintenance costs, while improving time to market and the quality of our own products.
********** 14 **********
--- page 15 ---
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
Q.4
a   Explain with the help of suitable diagram any 02 Cluster operations.
Ans:
Bundle: The Bundle function assembles individual components into a single new cluster and also allows one to
replace elements in an existing order. Initially, the function shows only two inputs, which can be increased by
dragging a corner of the function. As each input terminal is wired, a symbol representing the data type of the
wired element appears on the empty terminal. The order of the resultant cluster will be the order of inputs to the
bundle. The cluster input at the centre of the function is used only when one or more elements of the cluster are
to be replaced. Hence, this terminal is ignored while creating a new cluster. When the above function is used to
replace an element, the number of input terminals must match with those in the cluster. However, one needs to
wire only the new value(s) of the element(s) to be replaced.
CO-
2;
SO-
1 ;   [07]
BL-
2   Fig. 5.10 Bundle Function
Unbundle: The Unbundle function splits a cluster into its individual components. The output components are
arranged top to bottom in the same order that they have in the cluster. If the elements have the same data type,
the order of the elements in the cluster is the only way one can distinguish between them. It is important to resize
the function to contain the same number of outputs as there are elements in the input cluster.
Fig. 5.11 Unbundle Function
********** 15 **********
--- page 16 ---
Bundle by Name: When it is required to operate on a few elements and not the entire cluster elements, you use
the Bundle By Name function. In the Bundle by Name function elements are referenced by names rather than by
position. Here one can access only the elements needed. Also, this function cannot create new clusters, but can
only replace an element in an existing cluster. The only prerequisite, for the Bundle by Name function to work is
that all the elements must have names.
Fig. 5.12 Bundle by Name Function
Unbundle by Name: The Unbundle by Name function returns the cluster elements whose names are specified.
The major advantage of this function is that one does not have to keep track of the order of the elements within
the cluster. Also, this function does not require the number of elements to match the number in the cluster.
Fig. 5.13 Unbundle by Name Function
Any 02 from above
Description   02*2.5=05Marks
Diagram   02*01= 02Marks
CO- b   Explanation of any Two File Formats in detail.   03 Marks X 02 = 06 Marks (06)
3;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally   it becomes the most commonly used format, especially in
instrumentation applications. Needless to say, one has to convert all data to ASCII
strings before saving data. The major disadvantage of this format is that the text
files tend to be larger than the other formats. At one time this was a major
handicap, but with the ever-increasing capacity of storage media, this is no longer
a major handicap. Another disadvantage was speed, since the conversion of binary
data (internal format) to ASCII, and the transfer of the larger volume of data to
the disk were both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
********** 16 **********
--- page 17 ---
text files and reading and writing operations can be done with little data
conversion. Binary file format is useful in applications requiring writing and
reading of large chunks of data due to its size advantage. However, with the
increasing availability of large storage devices at reasonable cost, this advantage
is being progressively lost. Also, binary format is often system (or processor)
dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single
arbitrary data type specified during creation of the file. The data is indexed in
terms of these records. Each record in a measurement file must have the same data
types associated with it. One interesting feature of these files is that timestamps
are also included with each record. Also, LabVIEW allows random read access to
the binary versions of these files.
CO- c   Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by itself
2
does not provide instrumentation programming capability. VISA is a high-level API that calls
low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based
instruments and makes the appropriate driver calls depending on the type of instrument used.
When debugging VISA problems, remember that an apparent VISA problem could be an
installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If
the LabVIEW instrument driver was written with functions on the Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers
use VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend
required the definition of hardware standards to ensure the compatibility between different
modules. This was one of the factors leading to the development of the VXI specification. But
even with these improved hardware standards, a system was time consuming and expensive to
put together. Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
********** 17 **********
--- page 18 ---
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
Q.5
CO- a   Explain Industry Standard Architecture (ISA) in detail.   (07)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in 1987
2
when the IEEE (Institute of Electrical and Electronics Engineers) formally documented
standards governing its 16-bit implementation. AT version of the bus is called the AT bus
and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most common
type of early expansion bus, which was designed for use in the original IBM PC. The IBM
PC-XT used an 8-bit bus design. This means that the data transfers take place in 8 bit chunks
(i.e. one byte at a time) across the bus. The ISA bus ran at a clock speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits of
data at a time, was announced. The 16-bit version of the ISA bus is sometimes known as the
AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as the
processor. It was improved over the years and eventually the AT bus ran at a clock speed of
8MHz.
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single user
systems with 80386 and 80486 processors. There are 24 address lines and 16 data lines in it.
It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The data transfer rate
of the system is less when 8-bit. ISA bus is used with 32 bit processor having 32 bit address
and data bus. So, 16 bit ISA bus is used to transfer data. Many peripherals such as disk
controller, printer, and scanner can be connected to ISA bus.
CO- b   Explanation of Event Structure   (05)
2;   Example   (02)
SO-
1 ;
********** 18 **********
--- page 19 ---
BL-   a. Event Structure:
2
The Event structure waits until an event happens and then executes the
appropriate case to handle that event. Right-click the structure border to add new
event cases and configure which events to handle. Wire a value to the Timeout
terminal as shown at the top left of the Event structure to specify the number of
milliseconds the Event structure should wait for an event to occur. The default
is –1, indicating never to time out. The Event Data Node is attached to the inside
left and right borders of each event case. The node identifies the data LabVIEW
returns when an event occurs. The node displays data that is different in each
case of the Event structure depending on which event(s) you configure that case
to handle. If you configure a single case to handle multiple events, only the data
that is common to all handled event types is available. When you place an Event
structure on the block diagram, the Timeout event case is the default case. When
you place an Event structure on the block diagram from the Application
Control»Events palette, the structure displays the Event Dynamic Registration
terminals. When you place an Event structure on the block diagram from the
Structures palette, the structure does not display the terminals.
CO- c   Explaination of Express VI and Sub VI.   (06)
2;
SO-   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
1 ;   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
BL-   block diagram, its front panel and block diagram appear. The front panel includes controls and
4   indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as
a subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement
tasks. You can save the configuration of an Express VI as a subVI.
Express VIs are interactive VIs with configurable dialog page but Standard VIs are
modularized VIs customized by wiring. LabVIEW uses colored icons to distinguish between
Express VIs, VIs and functions on the block diagram. By default, icons for Express VIs appear
on the block diagram as expandable nodes with icons surrounded by a blue field. Icons for VIs
have white backgrounds, and icons for functions have pale yellow backgrounds. By default,
most functions and VIs on the block diagram appear as icons that are not expandable, unlike
Express VIs.
Q6   Open a blank VI and Build a VI to add or subtract two numbers. Use Case structures and text   (20)
CO-   ring to switch between addition and subtraction.
2   a. Save the VI as menu_tee.vi on desktop
&5;   b. Print the VI by selecting option Icon, description, panel and diagram in Print contents.
SO-
1;
********** 19 **********
--- page 20 ---
BL-   Ans :
6
Q.7
Open a blank VI and Build a VI to create a 2D numeric array (5 X 5) containing random   (20)
CO-   numbers as well as to find its transpose.
2   a. Build the front panel and the block diagram to create a 2D numeric array (5 X 5)
&5;   containing random numbers as well as to find its transpose.
SO-   b. Save the VI as quad_tee.vi on desktop
1;   c. Print the VI by selecting option Icon, description, panel and diagram in Print contents
BL-
6
Ans :
Fig a . Front Panel
********** 20 **********
--- page 21 ---
Fig b . Block Diagram
Please note that In front panel, 5 X 5 Matrix is random generated so it will be different for
users.
Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 712baf9d4b7b

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a   Explanation of the different debugging processes in LabVIEW.   (05)
2;
SO-
1 ;   Fixing Broken VIs
BL-
2
If a VI does not run, it is a broken, or nonexecutable, VI. The Run button appears broken
when the VI you are creating or editing contains errors..
Broken Run Button
Generally, this means that a required input is not wired, or a wire is broken. Press the
broken Run button to access the Error list window. The Error list window lists each error
and describes the problem. You can double-click an error to go directly to the error.
Warnings do not prevent you from running a VI. They are designed to help you avoid
potential problems in VIs. Errors, however, can break a VI. You must resolve any errors
before you can run the VI.
Finding Causes for Broken VIs
Click the broken Run button or select View>>Error to find out why a VI is broken. The
Error list window lists all the errors. The Items with errors section lists the names of all
items in memory, such as VIs and project libraries that have errors. If two or more items
have the same name, this section shows the specific application instance for each item.
The errors and warnings section lists the errors and warnings for the VI you select in the
Items with errors section. The Details section describes the errors and in some cases
********** 1 **********
--- page 2 ---
recommends how to correct the errors. Click the Help button to display a topic in the
LabVIEW Help that describes the error in detail and includes step-by-step instructions for
correcting the error.
Click the Show Error button or double-click the error description to highlight the area on
the block diagram or front panel that contains the error.
Figure 1: The Error list dialog box lists each error and describes the problem.
Common Causes of Broken VIs
The following list contains common reasons why a VI is broken while you edit it:
▪ The block diagram contains a broken wire because of a mismatch of data types or a
loose, unconnected end. Refer to the Correcting Broken VIs topic of the LabVIEW Help
for information about correcting broken wires.
▪ A required block diagram terminal is unwired. Refer to the Using Wires to Link Block
Diagram Objects topic of the LabVIEW Help for information about setting required
inputs and outputs.
▪ A subVI is broken or you edited its connector pane after you placed its icon on the
block diagram of the VI.
Back to top
********** 2 **********
--- page 3 ---
Fixing Incorrect Behavior
If your VI runs but produces incorrect results then you have a functional error in your
code. LabVIEW provides several tools to help you analyze where your VI is not behaving
as expected.
Block Diagram Toolbar
When you run a VI, buttons appear on the block diagram toolbar that you can use to
debug the VI. The following toolbar appears on the block diagram.
Click the Highlight Execution button to display an animation of the block diagram
execution when you run the VI. Notice the flow of data through the block diagram. Click
the button again to disable execution highlighting.
Highlight Execution
Execution highlighting shows the movement of data on the block diagram from one
node to another using bubbles that move along the wires. Use execution highlighting in
conjunction with single-stepping to see how data values move from node to node
through a VI.
Note: Execution highlighting greatly reduces the speed at which the VI runs.
********** 3 **********
--- page 4 ---
Figure 2: Execution highlighting shows the movement of data.
You can pause the execution of a VI at any time by choosing the pause button on the
toolbar.
Execution Pause
The color of the button turns to red when the VI is paused. Once you pause the VI, you
can use the tools below to gain additional insight into the execution of your application.
Click the Retain Wire Values button to save the wire values at each point in the flow of
execution so that when you place a probe on the wire you can immediately retain the
most recent value of the data that passed through the wire.
Retain Wire Values
You must successfully run the VI at least once before you can retain the wire values.
Click the Step Into button to open a node and pause.
Step Into
When you click the Step Into button again, it executes the first action and pauses at the
next action of the subVI or structure. You also can press the ctrl and down arrow keys.
Single-stepping through a VI steps through the VI node by node. Each node blinks to
denote when it is ready to execute.
Click the Step Over button to execute a node and pause at the next node.
Step Over
You also can press the ctrl and right arrow keys. By stepping over the node, you execute
the node without single-stepping through the node.
Click the Step Out button to finish executing the current node and pause.
Step Out
When the VI finishes executing, the Step Out button is dimmed. You also can press the
ctrl and up arrow keys. By stepping out of a node, you complete single-stepping through
the node and navigate to the next node.
********** 4 **********
--- page 5 ---
The Warning button appears if a VI includes a warning and you placed a checkmark in
the Show Warnings checkbox in the Error list window.
Warning
A warning indicates there is a potential problem with the block diagram, but it does not
stop the VI from running.
Probe Watch Window
Use the Probe tool (View>>Probe Watch Window) to check intermediate values on a
wire as a VI runs. Move your cursor over a wire while the VI is running or right-click on
the wire and choose Probe to generate a probe. Use the Probe tool if you have a
complicated block diagram with a series of operations, any one of which might return
incorrect data. Use the Probe tool with execution highlighting, single-stepping, and
breakpoints to determine if and where data is incorrect. If data is available, the probe
immediately updates and displays the data in the Probe Watch Window during execution
highlighting, single-stepping, or when you pause at a breakpoint.
Figure 3: The Probe Watch Window displays any and all probes active in your project.
When execution pauses at a node because of single-stepping or a breakpoint, you also
can probe the wire that just executed to see the value that flowed through that wire.
Breakpoint Manager
You can use the Breakpoint Manager (View>>Breakpoint Manager) to view, add, or
delete breakpoints from your code. A breakpoint will pause the execution of the VI when
that specific object is executed. You can place a VI, structure, wire, or operator.
********** 5 **********
--- page 6 ---
Figure 4: You can use the Breakpoint Manager to add, delete, or view breakpoints in
your code.
CO-   b   Explanation of for loop in LabVIEW :   (05)
3;
SO-   FOR LOOPS
1 ;   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
BL-4
LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The For
Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop from the
palette and use the cursor to drag a selection rectangle to create a new For Loop or around the section
of the block diagram you want to repeat. You also can place a While Loop on the block diagram,
right-click the border of the While Loop, and select Replace with For Loop from the shortcut menu to
change a While Loop to a For Loop.
********** 6 **********
--- page 7 ---
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat the
subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top side of
the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is explained in chapter
5. A VI will not run if it contains a For Loop that does not have a numeric value wired to the count
terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations. The
iteration count always starts at zero. During the first iteration, the iteration terminal returns 0. Figure
4.2 shows a simple For Loop which generates 10 random numbers and displays in the Random Number
Indicator.
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- c   Explanation of Local variable   (05)
1;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a
local variable are right-click on an object’s terminal and select Create»Local Variable. A local
variable icon for the object appears on the block diagram as shown in Figure 4.23.
********** 7 **********
--- page 8 ---
(2.5)
d. Outline the objectives of Data Acquisition System.
Ans: Objectives of Data Acquisition System
1. It must acquire the necessary data, at correct speed and at the correct time.
CO-   2. Use of all data efficiently to inform the operator about the state of the system.
3 ;   3. It must monitor the complete plant operation to maintain on-line optimum and safe operations.
SO-   4. It must be able to collect, summarize and store data for diagnosis of operation and record purpose.
1 ;   (05)
5. It must be able to compute unit performance indices using online, real-time data.
BL-   6. It must be flexible and capable of being expanded for future require.
1   7. It must be reliable, and not have a down time greater than 0.1%.
8. It must provide an effective human communication system and be able to identify problem areas, there by
minimizing unit availability and maximizing unit through point at minimum cost.
Any 05 points from above (or any other suitable points)   1*05=05
Q.2
CO- a   Explanation of the three methods of grounding of DAQ devices.   (07)
4;
SO-   Having selected an appropriate board based on the resolution required, speed, etc., the next
1 ;   issue the user has to address is the type of connection to use.
BL-   The selection of input type is intimately linked to the issue of grounding and is discussed
2
together in some detail. As is mentioned earlier, there are three ground points to consider:
(i) Safety Ground: This is connected to the ground of the mains. As the name implies this
is a safety line and is not suitable for signal lines.
(ii) Digital Ground: This is a signal ground defined for digital signals and should be used
as such. Connecting analog signals to this line is not desirable.
(iii) Analog Ground or Reference: This is also referred to as signal ground. This is the
ground to be used with all the analog signals.
Grounding considerations can form the text matter for a book by itself. Let us consider the
various types of connections in detail. The interface card has the safety (or system) ground,
analog ground, digital ground and the signal sense (analog reference) lines. The analog and
digital grounds are connected to the safety ground at some (ideally only one) point.
There are three options available (National Instruments nomenclature in parentheses):
1. Differential (Differential—DI)
2. Referenced to a common signal reference (Non-Referenced Single Ended—NRSE)
3. Referenced to the safety ground (Referenced Single Ended—RSE)
********** 8 **********
--- page 9 ---
Figure 4.4 Differential Connection.
The multiplexer is in two halves which are operated in a linked pair for differential input.
For the other two connections, the multiplexer is connected as a single body. This
immediately brings out the main drawback in the DI connection. Half the input channels
are lost to the user, i.e., a 16-channel board when used in a differential configuration
can accept at most 8 inputs. It is good practice to ground the unused input connections,
though one must add that this advice is more often than not followed in the breach. The
configuration of the multiplexer and the various signal lines in a differential connection is
shown in Fig. 4.4 For a 16-channel board, the input lines corresponding to channel n are n
and (n + 8) pin numbers. As has been stated earlier, the board capacity in terms of the
number of channels is reduced by a factor of two. Any signal arriving on both the input
lines (common-mode signal) will be rejected by the amplifier which is set up to operate as
a differential amplifier. The output of the amplifier is referenced to the analog ground. The
signal sense line is not used. In this configuration, the safety ground of the system will at
some point be connected to the signal ground. For the average user, some simple thumb
rules can be prescribed:
The differential configuration is by far the best from the noise point of view. However, the
loss of 50% capacity in terms of the number of channels is a serious handicap.
The DI connection is the only one useable for floating signals, as is invariably the case in
bridge connections. Also, for low-level signals, e.g., thermocouple (typical output 6–50μ
V/°C), the differential connection is the only one suitable due to noise considerations. In
many transducers which are now available with built-in electronics (e.g., dc–dc LVDTs),
the signals are floating and hence have to be used with the DI connection.
********** 9 **********
--- page 10 ---
Figure 4.5 NRSE Connection.
Differences between the NRSE and RSE signals are more subtle. These are illustrated in
figures 4.5 and 4.6, respectively. Close examination would reveal the following. First, the
two halves of the multiplexer are operating as a single unit providing the full complement
of 16 channels. Second, while in NRSE all signals are referenced to the signal sense (or
common) line, in RSE the signal ground is used instead. Consequently, in an NRSE or RSE,
the user loses the benefit of rejection of the common-mode signal. In RSE the risk of ground
loops is far higher.
Figure 4.6 RSE Connection.
CO- b Write a note on Polymorphism in Array Operations.   (07)
3;
SO-   By definition polymorphism is said to be the ability of a numeric function to adjust to input data of
1 ;
BL-   different data structures. Polymorphism of LabVIEW is applicable to arrays as well. Hence, one can
2   add a scalar to an array or add two arrays using the same function. It is important to note that for the
********** 10 **********
--- page 11 ---
same function different types of operations are performed for different combinations. For example, if
a scalar and an array are added, the scalar is added to each element of the array. However, when two
arrays are added, each element of one array is added to the corresponding element of the other array.
All LabVIEW arithmetic functions are polymorphic. This means that the inputs to these functions can
be   different   data   structures   such   as   scalar   values   and   arrays.
For example, the Add function can be used in the following ways.
1. Scalar + Scalar = Scalar addition.
2. Scalar + Array = The scalar is added to each element of array.
3. Array + Array = Each element of one array is added to the corresponding element of other array.
********** 11 **********
--- page 12 ---
Figure 5.15 (a) Adding two scalar values, (b) adding a scalar value with an array, (c) adding two arrays of the
same size and (d) adding two arrays of different sizes.
In Figure 5.15(a), two scalar values are added which results in a scalar output. In Figure 5.15(b), an
array is added with a scalar value. The function adds the scalar value to each element of the array and
returns the array output. In Figure 5.15(c), two arrays are added. The function adds each element of
one array to the corresponding element of the other array and returns the array output. In Figure 5.15(d),
two arrays of different sizes (i.e. number of elements) are added. The function adds corresponding
elements and returns the output array, with the size of the smaller input array. The first array consists
of three elements and the second consists of four elements. First three elements of both the arrays are
added. The fourth element of the second array is not considered. Polymorphism does not perform matrix
arithmetic when inputs are two-dimensional arrays (for example, two two-dimensional array inputs to
a multiply function do element by element multiplication, not matrix multiplication).
CO- c   Explanation of the common standards of serial port communication   (06)
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse,
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections
between PC serial ports and devices. RS-232 is the connector found on most PCs. This is a
single-ended communication method where only one device can be connected per port. Two
connector types are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and
multidrop capability make RS-485 an attractive choice in industrial applications that require
many distributed devices networked to a PC or other controller for data collection and other
operations.
Q.3
CO- a   Explanation of Measurement and Automation Explorer in detail.   (07)
4;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all device
1 ;   and channel configuration parameters. After installing a DAQ device in the computer, you must
BL-   run this configuration utility. MAX reads the information the Device Manager records in the
2
Windows Registry and assigns a logical device number to each DAQ device. Use the device
number to refer to the device in LabVIEW. Access MAX either by double-clicking the icon on
the desktop or selecting Tools»Measurement & Automation Explorer in LabVIEW. The device
parameters that you can set using the configuration utility depend on the device. MAX saves
the logical device number and the configuration parameters in the Windows Registry. The plug
and play capability of Windows automatically detects and configures switchless DAQ devices,
such as the PCI-6024E. When you install a device in the computer, the device is automatically
detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation of
********** 12 **********
--- page 13 ---
NI-DAQ. MAX is used primarily to configure and test National Instruments hardware, but it
offers other functionality, such as checking to see if you have the latest version of NI-DAQ
installed. The functionality of MAX is divided into four categories—Data Neighborhood,
Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc., which
may have been installed. Devices and Interfaces lists various options like DAQ boards (under
DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc. The Legacy option
has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred. The
Software function helps to launch and update various software items from NI. Remote Systems,
which is a top-level option, at par with My System, provides access to various DAQ systems
connected through the Ethernet, or other parts.
CO- b   Explanation of data types and the importance of them with colors in LabVIEW programs   (06)
2;
SO-   Data Type   Details   Color
1 ;   Boolean   Booleans have   only   two   possible Green
BL-
values: True or False .
2
Integers   Integers can   Blue
be signed or unsigned whole numbers
Doubles   Doubles and Singles are signed numbers Orange
with a decimal component
Strings   Strings are sequences of characters   Pink
Clusters   Clusters are groups of various data Thick Brown
types
Path   Path is location of file on local PC Dark Green
System
CO- c   Explanation of the basic difference between the traditional instruments and software-based (07)
1;   virtual instruments.
SO-   Block diagram   (02)
1 ;
********** 13 **********
--- page 14 ---
BL-
2   A traditional instrument is designed to collect data from an environment, or from a unit under
test, and to display information to a user based on the collected data. Such an instrument may
employ a transducer to sense changes in a physical parameter such as temperature or pressure,
and to convert the sensed information into electrical signals such as voltage or frequency
variations. The term “instrument” may also cover a physical or software device that performs
an analysis on data acquired from another instrument and then outputs the processed data to
display or recording means. This second category of instruments includes oscilloscopes,
spectrum analyzers and digital millimeters. The types of source data collected and analyzed by
instruments may thus vary widely, including both physical parameters such as temperature,
pressure, distance, light and sound frequencies and amplitudes, and also electrical parameters
including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements defines
general-purpose measurement and   control hardware   functionality. With   virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have used
virtual instrumentation to downsize automated test equipment (ATE) while experiencing up to
a several times increase in productivity gains at a fraction of the cost of traditional instrument
solutions. Virtual instrumentation is necessary because it is flexible. It delivers instrumentation
with the rapid adaptability required for today’s concept, product and process design,
development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of features
that are rarely, if ever used. Most conventional instruments do not have any computational
power as compared to a virtual instrument. Since the virtual instrument is part of a person
computer configuration, the personal computer’s computational as well as controlling
capability can be applied into a test configuration. Virtual instruments are compatible with
traditional instruments almost without exception. Virtual instrumentation software typically
provides libraries for interfacing with common ordinary instrument buses such as GPIB, serial
or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt the
instrument to our particular needs. A traditional instrument might contain an integrated circuit
to perform a particular set of data processing functions; in a virtual instrument, these functions
would be performed by software running on the PC processor. We can extend the set of
functions easily, limited only by the power of the software used. By employing virtual
instrumentation solutions, we can lower capital costs, system development costs, and system
maintenance costs, while improving time to market and the quality of our own products.
********** 14 **********
--- page 15 ---
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
Q.4
a   Explain with the help of suitable diagram any 02 Cluster operations.
Ans:
Bundle: The Bundle function assembles individual components into a single new cluster and also allows one to
replace elements in an existing order. Initially, the function shows only two inputs, which can be increased by
dragging a corner of the function. As each input terminal is wired, a symbol representing the data type of the
wired element appears on the empty terminal. The order of the resultant cluster will be the order of inputs to the
bundle. The cluster input at the centre of the function is used only when one or more elements of the cluster are
to be replaced. Hence, this terminal is ignored while creating a new cluster. When the above function is used to
replace an element, the number of input terminals must match with those in the cluster. However, one needs to
wire only the new value(s) of the element(s) to be replaced.
CO-
2;
SO-
1 ;   [07]
BL-
2   Fig. 5.10 Bundle Function
Unbundle: The Unbundle function splits a cluster into its individual components. The output components are
arranged top to bottom in the same order that they have in the cluster. If the elements have the same data type,
the order of the elements in the cluster is the only way one can distinguish between them. It is important to resize
the function to contain the same number of outputs as there are elements in the input cluster.
Fig. 5.11 Unbundle Function
********** 15 **********
--- page 16 ---
Bundle by Name: When it is required to operate on a few elements and not the entire cluster elements, you use
the Bundle By Name function. In the Bundle by Name function elements are referenced by names rather than by
position. Here one can access only the elements needed. Also, this function cannot create new clusters, but can
only replace an element in an existing cluster. The only prerequisite, for the Bundle by Name function to work is
that all the elements must have names.
Fig. 5.12 Bundle by Name Function
Unbundle by Name: The Unbundle by Name function returns the cluster elements whose names are specified.
The major advantage of this function is that one does not have to keep track of the order of the elements within
the cluster. Also, this function does not require the number of elements to match the number in the cluster.
Fig. 5.13 Unbundle by Name Function
Any 02 from above
Description   02*2.5=05Marks
Diagram   02*01= 02Marks
CO- b   Explanation of any Two File Formats in detail.   03 Marks X 02 = 06 Marks (06)
3;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally   it becomes the most commonly used format, especially in
instrumentation applications. Needless to say, one has to convert all data to ASCII
strings before saving data. The major disadvantage of this format is that the text
files tend to be larger than the other formats. At one time this was a major
handicap, but with the ever-increasing capacity of storage media, this is no longer
a major handicap. Another disadvantage was speed, since the conversion of binary
data (internal format) to ASCII, and the transfer of the larger volume of data to
the disk were both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
********** 16 **********
--- page 17 ---
text files and reading and writing operations can be done with little data
conversion. Binary file format is useful in applications requiring writing and
reading of large chunks of data due to its size advantage. However, with the
increasing availability of large storage devices at reasonable cost, this advantage
is being progressively lost. Also, binary format is often system (or processor)
dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single
arbitrary data type specified during creation of the file. The data is indexed in
terms of these records. Each record in a measurement file must have the same data
types associated with it. One interesting feature of these files is that timestamps
are also included with each record. Also, LabVIEW allows random read access to
the binary versions of these files.
CO- c   Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by itself
2
does not provide instrumentation programming capability. VISA is a high-level API that calls
low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based
instruments and makes the appropriate driver calls depending on the type of instrument used.
When debugging VISA problems, remember that an apparent VISA problem could be an
installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If
the LabVIEW instrument driver was written with functions on the Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers
use VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend
required the definition of hardware standards to ensure the compatibility between different
modules. This was one of the factors leading to the development of the VXI specification. But
even with these improved hardware standards, a system was time consuming and expensive to
put together. Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
********** 17 **********
--- page 18 ---
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
Q.5
CO- a   Explain Industry Standard Architecture (ISA) in detail.   (07)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in 1987
2
when the IEEE (Institute of Electrical and Electronics Engineers) formally documented
standards governing its 16-bit implementation. AT version of the bus is called the AT bus
and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most common
type of early expansion bus, which was designed for use in the original IBM PC. The IBM
PC-XT used an 8-bit bus design. This means that the data transfers take place in 8 bit chunks
(i.e. one byte at a time) across the bus. The ISA bus ran at a clock speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits of
data at a time, was announced. The 16-bit version of the ISA bus is sometimes known as the
AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as the
processor. It was improved over the years and eventually the AT bus ran at a clock speed of
8MHz.
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single user
systems with 80386 and 80486 processors. There are 24 address lines and 16 data lines in it.
It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The data transfer rate
of the system is less when 8-bit. ISA bus is used with 32 bit processor having 32 bit address
and data bus. So, 16 bit ISA bus is used to transfer data. Many peripherals such as disk
controller, printer, and scanner can be connected to ISA bus.
CO- b   Explanation of Event Structure   (05)
2;   Example   (02)
SO-
1 ;
********** 18 **********
--- page 19 ---
BL-   a. Event Structure:
2
The Event structure waits until an event happens and then executes the
appropriate case to handle that event. Right-click the structure border to add new
event cases and configure which events to handle. Wire a value to the Timeout
terminal as shown at the top left of the Event structure to specify the number of
milliseconds the Event structure should wait for an event to occur. The default
is –1, indicating never to time out. The Event Data Node is attached to the inside
left and right borders of each event case. The node identifies the data LabVIEW
returns when an event occurs. The node displays data that is different in each
case of the Event structure depending on which event(s) you configure that case
to handle. If you configure a single case to handle multiple events, only the data
that is common to all handled event types is available. When you place an Event
structure on the block diagram, the Timeout event case is the default case. When
you place an Event structure on the block diagram from the Application
Control»Events palette, the structure displays the Event Dynamic Registration
terminals. When you place an Event structure on the block diagram from the
Structures palette, the structure does not display the terminals.
CO- c   Explaination of Express VI and Sub VI.   (06)
2;
SO-   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
1 ;   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
BL-   block diagram, its front panel and block diagram appear. The front panel includes controls and
4   indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as
a subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement
tasks. You can save the configuration of an Express VI as a subVI.
Express VIs are interactive VIs with configurable dialog page but Standard VIs are
modularized VIs customized by wiring. LabVIEW uses colored icons to distinguish between
Express VIs, VIs and functions on the block diagram. By default, icons for Express VIs appear
on the block diagram as expandable nodes with icons surrounded by a blue field. Icons for VIs
have white backgrounds, and icons for functions have pale yellow backgrounds. By default,
most functions and VIs on the block diagram appear as icons that are not expandable, unlike
Express VIs.
Q6   Open a blank VI and Build a VI to add or subtract two numbers. Use Case structures and text   (20)
CO-   ring to switch between addition and subtraction.
2   a. Save the VI as menu_tee.vi on desktop
&5;   b. Print the VI by selecting option Icon, description, panel and diagram in Print contents.
SO-
1;
********** 19 **********
--- page 20 ---
BL-   Ans :
6
Q.7
Open a blank VI and Build a VI to create a 2D numeric array (5 X 5) containing random   (20)
CO-   numbers as well as to find its transpose.
2   a. Build the front panel and the block diagram to create a 2D numeric array (5 X 5)
&5;   containing random numbers as well as to find its transpose.
SO-   b. Save the VI as quad_tee.vi on desktop
1;   c. Print the VI by selecting option Icon, description, panel and diagram in Print contents
BL-
6
Ans :
Fig a . Front Panel
********** 20 **********
--- page 21 ---
Fig b . Block Diagram
Please note that In front panel, 5 X 5 Matrix is random generated so it will be different for
users.
Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 05435cd7db5d

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a   Explanation of the different debugging processes in LabVIEW.   (05)
2;
SO-
1 ;   Fixing Broken VIs
BL-
2
If a VI does not run, it is a broken, or nonexecutable, VI. The Run button appears broken
when the VI you are creating or editing contains errors..
Broken Run Button
Generally, this means that a required input is not wired, or a wire is broken. Press the
broken Run button to access the Error list window. The Error list window lists each error
and describes the problem. You can double-click an error to go directly to the error.
Warnings do not prevent you from running a VI. They are designed to help you avoid
potential problems in VIs. Errors, however, can break a VI. You must resolve any errors
before you can run the VI.
Finding Causes for Broken VIs
Click the broken Run button or select View>>Error to find out why a VI is broken. The
Error list window lists all the errors. The Items with errors section lists the names of all
items in memory, such as VIs and project libraries that have errors. If two or more items
have the same name, this section shows the specific application instance for each item.
The errors and warnings section lists the errors and warnings for the VI you select in the
Items with errors section. The Details section describes the errors and in some cases
********** 1 **********
--- page 2 ---
recommends how to correct the errors. Click the Help button to display a topic in the
LabVIEW Help that describes the error in detail and includes step-by-step instructions for
correcting the error.
Click the Show Error button or double-click the error description to highlight the area on
the block diagram or front panel that contains the error.
Figure 1: The Error list dialog box lists each error and describes the problem.
Common Causes of Broken VIs
The following list contains common reasons why a VI is broken while you edit it:
▪ The block diagram contains a broken wire because of a mismatch of data types or a
loose, unconnected end. Refer to the Correcting Broken VIs topic of the LabVIEW Help
for information about correcting broken wires.
▪ A required block diagram terminal is unwired. Refer to the Using Wires to Link Block
Diagram Objects topic of the LabVIEW Help for information about setting required
inputs and outputs.
▪ A subVI is broken or you edited its connector pane after you placed its icon on the
block diagram of the VI.
Back to top
********** 2 **********
--- page 3 ---
Fixing Incorrect Behavior
If your VI runs but produces incorrect results then you have a functional error in your
code. LabVIEW provides several tools to help you analyze where your VI is not behaving
as expected.
Block Diagram Toolbar
When you run a VI, buttons appear on the block diagram toolbar that you can use to
debug the VI. The following toolbar appears on the block diagram.
Click the Highlight Execution button to display an animation of the block diagram
execution when you run the VI. Notice the flow of data through the block diagram. Click
the button again to disable execution highlighting.
Highlight Execution
Execution highlighting shows the movement of data on the block diagram from one
node to another using bubbles that move along the wires. Use execution highlighting in
conjunction with single-stepping to see how data values move from node to node
through a VI.
Note: Execution highlighting greatly reduces the speed at which the VI runs.
********** 3 **********
--- page 4 ---
Figure 2: Execution highlighting shows the movement of data.
You can pause the execution of a VI at any time by choosing the pause button on the
toolbar.
Execution Pause
The color of the button turns to red when the VI is paused. Once you pause the VI, you
can use the tools below to gain additional insight into the execution of your application.
Click the Retain Wire Values button to save the wire values at each point in the flow of
execution so that when you place a probe on the wire you can immediately retain the
most recent value of the data that passed through the wire.
Retain Wire Values
You must successfully run the VI at least once before you can retain the wire values.
Click the Step Into button to open a node and pause.
Step Into
When you click the Step Into button again, it executes the first action and pauses at the
next action of the subVI or structure. You also can press the ctrl and down arrow keys.
Single-stepping through a VI steps through the VI node by node. Each node blinks to
denote when it is ready to execute.
Click the Step Over button to execute a node and pause at the next node.
Step Over
You also can press the ctrl and right arrow keys. By stepping over the node, you execute
the node without single-stepping through the node.
Click the Step Out button to finish executing the current node and pause.
Step Out
When the VI finishes executing, the Step Out button is dimmed. You also can press the
ctrl and up arrow keys. By stepping out of a node, you complete single-stepping through
the node and navigate to the next node.
********** 4 **********
--- page 5 ---
The Warning button appears if a VI includes a warning and you placed a checkmark in
the Show Warnings checkbox in the Error list window.
Warning
A warning indicates there is a potential problem with the block diagram, but it does not
stop the VI from running.
Probe Watch Window
Use the Probe tool (View>>Probe Watch Window) to check intermediate values on a
wire as a VI runs. Move your cursor over a wire while the VI is running or right-click on
the wire and choose Probe to generate a probe. Use the Probe tool if you have a
complicated block diagram with a series of operations, any one of which might return
incorrect data. Use the Probe tool with execution highlighting, single-stepping, and
breakpoints to determine if and where data is incorrect. If data is available, the probe
immediately updates and displays the data in the Probe Watch Window during execution
highlighting, single-stepping, or when you pause at a breakpoint.
Figure 3: The Probe Watch Window displays any and all probes active in your project.
When execution pauses at a node because of single-stepping or a breakpoint, you also
can probe the wire that just executed to see the value that flowed through that wire.
Breakpoint Manager
You can use the Breakpoint Manager (View>>Breakpoint Manager) to view, add, or
delete breakpoints from your code. A breakpoint will pause the execution of the VI when
that specific object is executed. You can place a VI, structure, wire, or operator.
********** 5 **********
--- page 6 ---
Figure 4: You can use the Breakpoint Manager to add, delete, or view breakpoints in
your code.
CO-   b   Explanation of for loop in LabVIEW :   (05)
3;
SO-   FOR LOOPS
1 ;   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
BL-4
LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The For
Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop from the
palette and use the cursor to drag a selection rectangle to create a new For Loop or around the section
of the block diagram you want to repeat. You also can place a While Loop on the block diagram,
right-click the border of the While Loop, and select Replace with For Loop from the shortcut menu to
change a While Loop to a For Loop.
********** 6 **********
--- page 7 ---
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat the
subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top side of
the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is explained in chapter
5. A VI will not run if it contains a For Loop that does not have a numeric value wired to the count
terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations. The
iteration count always starts at zero. During the first iteration, the iteration terminal returns 0. Figure
4.2 shows a simple For Loop which generates 10 random numbers and displays in the Random Number
Indicator.
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- c   Explanation of Local variable   (05)
1;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a
local variable are right-click on an object’s terminal and select Create»Local Variable. A local
variable icon for the object appears on the block diagram as shown in Figure 4.23.
********** 7 **********
--- page 8 ---
(2.5)
d. Outline the objectives of Data Acquisition System.
Ans: Objectives of Data Acquisition System
1. It must acquire the necessary data, at correct speed and at the correct time.
CO-   2. Use of all data efficiently to inform the operator about the state of the system.
3 ;   3. It must monitor the complete plant operation to maintain on-line optimum and safe operations.
SO-   4. It must be able to collect, summarize and store data for diagnosis of operation and record purpose.
1 ;   (05)
5. It must be able to compute unit performance indices using online, real-time data.
BL-   6. It must be flexible and capable of being expanded for future require.
1   7. It must be reliable, and not have a down time greater than 0.1%.
8. It must provide an effective human communication system and be able to identify problem areas, there by
minimizing unit availability and maximizing unit through point at minimum cost.
Any 05 points from above (or any other suitable points)   1*05=05
Q.2
CO- a   Explanation of the three methods of grounding of DAQ devices.   (07)
4;
SO-   Having selected an appropriate board based on the resolution required, speed, etc., the next
1 ;   issue the user has to address is the type of connection to use.
BL-   The selection of input type is intimately linked to the issue of grounding and is discussed
2
together in some detail. As is mentioned earlier, there are three ground points to consider:
(i) Safety Ground: This is connected to the ground of the mains. As the name implies this
is a safety line and is not suitable for signal lines.
(ii) Digital Ground: This is a signal ground defined for digital signals and should be used
as such. Connecting analog signals to this line is not desirable.
(iii) Analog Ground or Reference: This is also referred to as signal ground. This is the
ground to be used with all the analog signals.
Grounding considerations can form the text matter for a book by itself. Let us consider the
various types of connections in detail. The interface card has the safety (or system) ground,
analog ground, digital ground and the signal sense (analog reference) lines. The analog and
digital grounds are connected to the safety ground at some (ideally only one) point.
There are three options available (National Instruments nomenclature in parentheses):
1. Differential (Differential—DI)
2. Referenced to a common signal reference (Non-Referenced Single Ended—NRSE)
3. Referenced to the safety ground (Referenced Single Ended—RSE)
********** 8 **********
--- page 9 ---
Figure 4.4 Differential Connection.
The multiplexer is in two halves which are operated in a linked pair for differential input.
For the other two connections, the multiplexer is connected as a single body. This
immediately brings out the main drawback in the DI connection. Half the input channels
are lost to the user, i.e., a 16-channel board when used in a differential configuration
can accept at most 8 inputs. It is good practice to ground the unused input connections,
though one must add that this advice is more often than not followed in the breach. The
configuration of the multiplexer and the various signal lines in a differential connection is
shown in Fig. 4.4 For a 16-channel board, the input lines corresponding to channel n are n
and (n + 8) pin numbers. As has been stated earlier, the board capacity in terms of the
number of channels is reduced by a factor of two. Any signal arriving on both the input
lines (common-mode signal) will be rejected by the amplifier which is set up to operate as
a differential amplifier. The output of the amplifier is referenced to the analog ground. The
signal sense line is not used. In this configuration, the safety ground of the system will at
some point be connected to the signal ground. For the average user, some simple thumb
rules can be prescribed:
The differential configuration is by far the best from the noise point of view. However, the
loss of 50% capacity in terms of the number of channels is a serious handicap.
The DI connection is the only one useable for floating signals, as is invariably the case in
bridge connections. Also, for low-level signals, e.g., thermocouple (typical output 6–50μ
V/°C), the differential connection is the only one suitable due to noise considerations. In
many transducers which are now available with built-in electronics (e.g., dc–dc LVDTs),
the signals are floating and hence have to be used with the DI connection.
********** 9 **********
--- page 10 ---
Figure 4.5 NRSE Connection.
Differences between the NRSE and RSE signals are more subtle. These are illustrated in
figures 4.5 and 4.6, respectively. Close examination would reveal the following. First, the
two halves of the multiplexer are operating as a single unit providing the full complement
of 16 channels. Second, while in NRSE all signals are referenced to the signal sense (or
common) line, in RSE the signal ground is used instead. Consequently, in an NRSE or RSE,
the user loses the benefit of rejection of the common-mode signal. In RSE the risk of ground
loops is far higher.
Figure 4.6 RSE Connection.
CO- b Write a note on Polymorphism in Array Operations.   (07)
3;
SO-   By definition polymorphism is said to be the ability of a numeric function to adjust to input data of
1 ;
BL-   different data structures. Polymorphism of LabVIEW is applicable to arrays as well. Hence, one can
2   add a scalar to an array or add two arrays using the same function. It is important to note that for the
********** 10 **********
--- page 11 ---
same function different types of operations are performed for different combinations. For example, if
a scalar and an array are added, the scalar is added to each element of the array. However, when two
arrays are added, each element of one array is added to the corresponding element of the other array.
All LabVIEW arithmetic functions are polymorphic. This means that the inputs to these functions can
be   different   data   structures   such   as   scalar   values   and   arrays.
For example, the Add function can be used in the following ways.
1. Scalar + Scalar = Scalar addition.
2. Scalar + Array = The scalar is added to each element of array.
3. Array + Array = Each element of one array is added to the corresponding element of other array.
********** 11 **********
--- page 12 ---
Figure 5.15 (a) Adding two scalar values, (b) adding a scalar value with an array, (c) adding two arrays of the
same size and (d) adding two arrays of different sizes.
In Figure 5.15(a), two scalar values are added which results in a scalar output. In Figure 5.15(b), an
array is added with a scalar value. The function adds the scalar value to each element of the array and
returns the array output. In Figure 5.15(c), two arrays are added. The function adds each element of
one array to the corresponding element of the other array and returns the array output. In Figure 5.15(d),
two arrays of different sizes (i.e. number of elements) are added. The function adds corresponding
elements and returns the output array, with the size of the smaller input array. The first array consists
of three elements and the second consists of four elements. First three elements of both the arrays are
added. The fourth element of the second array is not considered. Polymorphism does not perform matrix
arithmetic when inputs are two-dimensional arrays (for example, two two-dimensional array inputs to
a multiply function do element by element multiplication, not matrix multiplication).
CO- c   Explanation of the common standards of serial port communication   (06)
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse,
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections
between PC serial ports and devices. RS-232 is the connector found on most PCs. This is a
single-ended communication method where only one device can be connected per port. Two
connector types are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and
multidrop capability make RS-485 an attractive choice in industrial applications that require
many distributed devices networked to a PC or other controller for data collection and other
operations.
Q.3
CO- a   Explanation of Measurement and Automation Explorer in detail.   (07)
4;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all device
1 ;   and channel configuration parameters. After installing a DAQ device in the computer, you must
BL-   run this configuration utility. MAX reads the information the Device Manager records in the
2
Windows Registry and assigns a logical device number to each DAQ device. Use the device
number to refer to the device in LabVIEW. Access MAX either by double-clicking the icon on
the desktop or selecting Tools»Measurement & Automation Explorer in LabVIEW. The device
parameters that you can set using the configuration utility depend on the device. MAX saves
the logical device number and the configuration parameters in the Windows Registry. The plug
and play capability of Windows automatically detects and configures switchless DAQ devices,
such as the PCI-6024E. When you install a device in the computer, the device is automatically
detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation of
********** 12 **********
--- page 13 ---
NI-DAQ. MAX is used primarily to configure and test National Instruments hardware, but it
offers other functionality, such as checking to see if you have the latest version of NI-DAQ
installed. The functionality of MAX is divided into four categories—Data Neighborhood,
Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc., which
may have been installed. Devices and Interfaces lists various options like DAQ boards (under
DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc. The Legacy option
has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred. The
Software function helps to launch and update various software items from NI. Remote Systems,
which is a top-level option, at par with My System, provides access to various DAQ systems
connected through the Ethernet, or other parts.
CO- b   Explanation of data types and the importance of them with colors in LabVIEW programs   (06)
2;
SO-   Data Type   Details   Color
1 ;   Boolean   Booleans have   only   two   possible Green
BL-
values: True or False .
2
Integers   Integers can   Blue
be signed or unsigned whole numbers
Doubles   Doubles and Singles are signed numbers Orange
with a decimal component
Strings   Strings are sequences of characters   Pink
Clusters   Clusters are groups of various data Thick Brown
types
Path   Path is location of file on local PC Dark Green
System
CO- c   Explanation of the basic difference between the traditional instruments and software-based (07)
1;   virtual instruments.
SO-   Block diagram   (02)
1 ;
********** 13 **********
--- page 14 ---
BL-
2   A traditional instrument is designed to collect data from an environment, or from a unit under
test, and to display information to a user based on the collected data. Such an instrument may
employ a transducer to sense changes in a physical parameter such as temperature or pressure,
and to convert the sensed information into electrical signals such as voltage or frequency
variations. The term “instrument” may also cover a physical or software device that performs
an analysis on data acquired from another instrument and then outputs the processed data to
display or recording means. This second category of instruments includes oscilloscopes,
spectrum analyzers and digital millimeters. The types of source data collected and analyzed by
instruments may thus vary widely, including both physical parameters such as temperature,
pressure, distance, light and sound frequencies and amplitudes, and also electrical parameters
including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements defines
general-purpose measurement and   control hardware   functionality. With   virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have used
virtual instrumentation to downsize automated test equipment (ATE) while experiencing up to
a several times increase in productivity gains at a fraction of the cost of traditional instrument
solutions. Virtual instrumentation is necessary because it is flexible. It delivers instrumentation
with the rapid adaptability required for today’s concept, product and process design,
development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of features
that are rarely, if ever used. Most conventional instruments do not have any computational
power as compared to a virtual instrument. Since the virtual instrument is part of a person
computer configuration, the personal computer’s computational as well as controlling
capability can be applied into a test configuration. Virtual instruments are compatible with
traditional instruments almost without exception. Virtual instrumentation software typically
provides libraries for interfacing with common ordinary instrument buses such as GPIB, serial
or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt the
instrument to our particular needs. A traditional instrument might contain an integrated circuit
to perform a particular set of data processing functions; in a virtual instrument, these functions
would be performed by software running on the PC processor. We can extend the set of
functions easily, limited only by the power of the software used. By employing virtual
instrumentation solutions, we can lower capital costs, system development costs, and system
maintenance costs, while improving time to market and the quality of our own products.
********** 14 **********
--- page 15 ---
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
Q.4
a   Explain with the help of suitable diagram any 02 Cluster operations.
Ans:
Bundle: The Bundle function assembles individual components into a single new cluster and also allows one to
replace elements in an existing order. Initially, the function shows only two inputs, which can be increased by
dragging a corner of the function. As each input terminal is wired, a symbol representing the data type of the
wired element appears on the empty terminal. The order of the resultant cluster will be the order of inputs to the
bundle. The cluster input at the centre of the function is used only when one or more elements of the cluster are
to be replaced. Hence, this terminal is ignored while creating a new cluster. When the above function is used to
replace an element, the number of input terminals must match with those in the cluster. However, one needs to
wire only the new value(s) of the element(s) to be replaced.
CO-
2;
SO-
1 ;   [07]
BL-
2   Fig. 5.10 Bundle Function
Unbundle: The Unbundle function splits a cluster into its individual components. The output components are
arranged top to bottom in the same order that they have in the cluster. If the elements have the same data type,
the order of the elements in the cluster is the only way one can distinguish between them. It is important to resize
the function to contain the same number of outputs as there are elements in the input cluster.
Fig. 5.11 Unbundle Function
********** 15 **********
--- page 16 ---
Bundle by Name: When it is required to operate on a few elements and not the entire cluster elements, you use
the Bundle By Name function. In the Bundle by Name function elements are referenced by names rather than by
position. Here one can access only the elements needed. Also, this function cannot create new clusters, but can
only replace an element in an existing cluster. The only prerequisite, for the Bundle by Name function to work is
that all the elements must have names.
Fig. 5.12 Bundle by Name Function
Unbundle by Name: The Unbundle by Name function returns the cluster elements whose names are specified.
The major advantage of this function is that one does not have to keep track of the order of the elements within
the cluster. Also, this function does not require the number of elements to match the number in the cluster.
Fig. 5.13 Unbundle by Name Function
Any 02 from above
Description   02*2.5=05Marks
Diagram   02*01= 02Marks
CO- b   Explanation of any Two File Formats in detail.   03 Marks X 02 = 06 Marks (06)
3;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally   it becomes the most commonly used format, especially in
instrumentation applications. Needless to say, one has to convert all data to ASCII
strings before saving data. The major disadvantage of this format is that the text
files tend to be larger than the other formats. At one time this was a major
handicap, but with the ever-increasing capacity of storage media, this is no longer
a major handicap. Another disadvantage was speed, since the conversion of binary
data (internal format) to ASCII, and the transfer of the larger volume of data to
the disk were both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
********** 16 **********
--- page 17 ---
text files and reading and writing operations can be done with little data
conversion. Binary file format is useful in applications requiring writing and
reading of large chunks of data due to its size advantage. However, with the
increasing availability of large storage devices at reasonable cost, this advantage
is being progressively lost. Also, binary format is often system (or processor)
dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single
arbitrary data type specified during creation of the file. The data is indexed in
terms of these records. Each record in a measurement file must have the same data
types associated with it. One interesting feature of these files is that timestamps
are also included with each record. Also, LabVIEW allows random read access to
the binary versions of these files.
CO- c   Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by itself
2
does not provide instrumentation programming capability. VISA is a high-level API that calls
low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based
instruments and makes the appropriate driver calls depending on the type of instrument used.
When debugging VISA problems, remember that an apparent VISA problem could be an
installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If
the LabVIEW instrument driver was written with functions on the Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers
use VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend
required the definition of hardware standards to ensure the compatibility between different
modules. This was one of the factors leading to the development of the VXI specification. But
even with these improved hardware standards, a system was time consuming and expensive to
put together. Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
********** 17 **********
--- page 18 ---
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
Q.5
CO- a   Explain Industry Standard Architecture (ISA) in detail.   (07)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in 1987
2
when the IEEE (Institute of Electrical and Electronics Engineers) formally documented
standards governing its 16-bit implementation. AT version of the bus is called the AT bus
and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most common
type of early expansion bus, which was designed for use in the original IBM PC. The IBM
PC-XT used an 8-bit bus design. This means that the data transfers take place in 8 bit chunks
(i.e. one byte at a time) across the bus. The ISA bus ran at a clock speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits of
data at a time, was announced. The 16-bit version of the ISA bus is sometimes known as the
AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as the
processor. It was improved over the years and eventually the AT bus ran at a clock speed of
8MHz.
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single user
systems with 80386 and 80486 processors. There are 24 address lines and 16 data lines in it.
It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The data transfer rate
of the system is less when 8-bit. ISA bus is used with 32 bit processor having 32 bit address
and data bus. So, 16 bit ISA bus is used to transfer data. Many peripherals such as disk
controller, printer, and scanner can be connected to ISA bus.
CO- b   Explanation of Event Structure   (05)
2;   Example   (02)
SO-
1 ;
********** 18 **********
--- page 19 ---
BL-   a. Event Structure:
2
The Event structure waits until an event happens and then executes the
appropriate case to handle that event. Right-click the structure border to add new
event cases and configure which events to handle. Wire a value to the Timeout
terminal as shown at the top left of the Event structure to specify the number of
milliseconds the Event structure should wait for an event to occur. The default
is –1, indicating never to time out. The Event Data Node is attached to the inside
left and right borders of each event case. The node identifies the data LabVIEW
returns when an event occurs. The node displays data that is different in each
case of the Event structure depending on which event(s) you configure that case
to handle. If you configure a single case to handle multiple events, only the data
that is common to all handled event types is available. When you place an Event
structure on the block diagram, the Timeout event case is the default case. When
you place an Event structure on the block diagram from the Application
Control»Events palette, the structure displays the Event Dynamic Registration
terminals. When you place an Event structure on the block diagram from the
Structures palette, the structure does not display the terminals.
CO- c   Explaination of Express VI and Sub VI.   (06)
2;
SO-   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
1 ;   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
BL-   block diagram, its front panel and block diagram appear. The front panel includes controls and
4   indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as
a subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement
tasks. You can save the configuration of an Express VI as a subVI.
Express VIs are interactive VIs with configurable dialog page but Standard VIs are
modularized VIs customized by wiring. LabVIEW uses colored icons to distinguish between
Express VIs, VIs and functions on the block diagram. By default, icons for Express VIs appear
on the block diagram as expandable nodes with icons surrounded by a blue field. Icons for VIs
have white backgrounds, and icons for functions have pale yellow backgrounds. By default,
most functions and VIs on the block diagram appear as icons that are not expandable, unlike
Express VIs.
Q6   Open a blank VI and Build a VI to add or subtract two numbers. Use Case structures and text   (20)
CO-   ring to switch between addition and subtraction.
2   a. Save the VI as menu_tee.vi on desktop
&5;   b. Print the VI by selecting option Icon, description, panel and diagram in Print contents.
SO-
1;
********** 19 **********
--- page 20 ---
BL-   Ans :
6
Q.7
Open a blank VI and Build a VI to create a 2D numeric array (5 X 5) containing random   (20)
CO-   numbers as well as to find its transpose.
2   a. Build the front panel and the block diagram to create a 2D numeric array (5 X 5)
&5;   containing random numbers as well as to find its transpose.
SO-   b. Save the VI as quad_tee.vi on desktop
1;   c. Print the VI by selecting option Icon, description, panel and diagram in Print contents
BL-
6
Ans :
Fig a . Front Panel
********** 20 **********
--- page 21 ---
Fig b . Block Diagram
Please note that In front panel, 5 X 5 Matrix is random generated so it will be different for
users.
Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 98812d54fb47

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechanical_7003/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a   Explanation of the different debugging processes in LabVIEW.   (05)
2;
SO-
1 ;   Fixing Broken VIs
BL-
2
If a VI does not run, it is a broken, or nonexecutable, VI. The Run button appears broken
when the VI you are creating or editing contains errors..
Broken Run Button
Generally, this means that a required input is not wired, or a wire is broken. Press the
broken Run button to access the Error list window. The Error list window lists each error
and describes the problem. You can double-click an error to go directly to the error.
Warnings do not prevent you from running a VI. They are designed to help you avoid
potential problems in VIs. Errors, however, can break a VI. You must resolve any errors
before you can run the VI.
Finding Causes for Broken VIs
Click the broken Run button or select View>>Error to find out why a VI is broken. The
Error list window lists all the errors. The Items with errors section lists the names of all
items in memory, such as VIs and project libraries that have errors. If two or more items
have the same name, this section shows the specific application instance for each item.
The errors and warnings section lists the errors and warnings for the VI you select in the
Items with errors section. The Details section describes the errors and in some cases
********** 1 **********
--- page 2 ---
recommends how to correct the errors. Click the Help button to display a topic in the
LabVIEW Help that describes the error in detail and includes step-by-step instructions for
correcting the error.
Click the Show Error button or double-click the error description to highlight the area on
the block diagram or front panel that contains the error.
Figure 1: The Error list dialog box lists each error and describes the problem.
Common Causes of Broken VIs
The following list contains common reasons why a VI is broken while you edit it:
▪ The block diagram contains a broken wire because of a mismatch of data types or a
loose, unconnected end. Refer to the Correcting Broken VIs topic of the LabVIEW Help
for information about correcting broken wires.
▪ A required block diagram terminal is unwired. Refer to the Using Wires to Link Block
Diagram Objects topic of the LabVIEW Help for information about setting required
inputs and outputs.
▪ A subVI is broken or you edited its connector pane after you placed its icon on the
block diagram of the VI.
Back to top
********** 2 **********
--- page 3 ---
Fixing Incorrect Behavior
If your VI runs but produces incorrect results then you have a functional error in your
code. LabVIEW provides several tools to help you analyze where your VI is not behaving
as expected.
Block Diagram Toolbar
When you run a VI, buttons appear on the block diagram toolbar that you can use to
debug the VI. The following toolbar appears on the block diagram.
Click the Highlight Execution button to display an animation of the block diagram
execution when you run the VI. Notice the flow of data through the block diagram. Click
the button again to disable execution highlighting.
Highlight Execution
Execution highlighting shows the movement of data on the block diagram from one
node to another using bubbles that move along the wires. Use execution highlighting in
conjunction with single-stepping to see how data values move from node to node
through a VI.
Note: Execution highlighting greatly reduces the speed at which the VI runs.
********** 3 **********
--- page 4 ---
Figure 2: Execution highlighting shows the movement of data.
You can pause the execution of a VI at any time by choosing the pause button on the
toolbar.
Execution Pause
The color of the button turns to red when the VI is paused. Once you pause the VI, you
can use the tools below to gain additional insight into the execution of your application.
Click the Retain Wire Values button to save the wire values at each point in the flow of
execution so that when you place a probe on the wire you can immediately retain the
most recent value of the data that passed through the wire.
Retain Wire Values
You must successfully run the VI at least once before you can retain the wire values.
Click the Step Into button to open a node and pause.
Step Into
When you click the Step Into button again, it executes the first action and pauses at the
next action of the subVI or structure. You also can press the ctrl and down arrow keys.
Single-stepping through a VI steps through the VI node by node. Each node blinks to
denote when it is ready to execute.
Click the Step Over button to execute a node and pause at the next node.
Step Over
You also can press the ctrl and right arrow keys. By stepping over the node, you execute
the node without single-stepping through the node.
Click the Step Out button to finish executing the current node and pause.
Step Out
When the VI finishes executing, the Step Out button is dimmed. You also can press the
ctrl and up arrow keys. By stepping out of a node, you complete single-stepping through
the node and navigate to the next node.
********** 4 **********
--- page 5 ---
The Warning button appears if a VI includes a warning and you placed a checkmark in
the Show Warnings checkbox in the Error list window.
Warning
A warning indicates there is a potential problem with the block diagram, but it does not
stop the VI from running.
Probe Watch Window
Use the Probe tool (View>>Probe Watch Window) to check intermediate values on a
wire as a VI runs. Move your cursor over a wire while the VI is running or right-click on
the wire and choose Probe to generate a probe. Use the Probe tool if you have a
complicated block diagram with a series of operations, any one of which might return
incorrect data. Use the Probe tool with execution highlighting, single-stepping, and
breakpoints to determine if and where data is incorrect. If data is available, the probe
immediately updates and displays the data in the Probe Watch Window during execution
highlighting, single-stepping, or when you pause at a breakpoint.
Figure 3: The Probe Watch Window displays any and all probes active in your project.
When execution pauses at a node because of single-stepping or a breakpoint, you also
can probe the wire that just executed to see the value that flowed through that wire.
Breakpoint Manager
You can use the Breakpoint Manager (View>>Breakpoint Manager) to view, add, or
delete breakpoints from your code. A breakpoint will pause the execution of the VI when
that specific object is executed. You can place a VI, structure, wire, or operator.
********** 5 **********
--- page 6 ---
Figure 4: You can use the Breakpoint Manager to add, delete, or view breakpoints in
your code.
CO-   b   Explanation of for loop in LabVIEW :   (05)
3;
SO-   FOR LOOPS
1 ;   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
BL-4
LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The For
Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop from the
palette and use the cursor to drag a selection rectangle to create a new For Loop or around the section
of the block diagram you want to repeat. You also can place a While Loop on the block diagram,
right-click the border of the While Loop, and select Replace with For Loop from the shortcut menu to
change a While Loop to a For Loop.
********** 6 **********
--- page 7 ---
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat the
subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top side of
the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is explained in chapter
5. A VI will not run if it contains a For Loop that does not have a numeric value wired to the count
terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations. The
iteration count always starts at zero. During the first iteration, the iteration terminal returns 0. Figure
4.2 shows a simple For Loop which generates 10 random numbers and displays in the Random Number
Indicator.
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- c   Explanation of Local variable   (05)
1;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a
local variable are right-click on an object’s terminal and select Create»Local Variable. A local
variable icon for the object appears on the block diagram as shown in Figure 4.23.
********** 7 **********
--- page 8 ---
(2.5)
d. Outline the objectives of Data Acquisition System.
Ans: Objectives of Data Acquisition System
1. It must acquire the necessary data, at correct speed and at the correct time.
CO-   2. Use of all data efficiently to inform the operator about the state of the system.
3 ;   3. It must monitor the complete plant operation to maintain on-line optimum and safe operations.
SO-   4. It must be able to collect, summarize and store data for diagnosis of operation and record purpose.
1 ;   (05)
5. It must be able to compute unit performance indices using online, real-time data.
BL-   6. It must be flexible and capable of being expanded for future require.
1   7. It must be reliable, and not have a down time greater than 0.1%.
8. It must provide an effective human communication system and be able to identify problem areas, there by
minimizing unit availability and maximizing unit through point at minimum cost.
Any 05 points from above (or any other suitable points)   1*05=05
Q.2
CO- a   Explanation of the three methods of grounding of DAQ devices.   (07)
4;
SO-   Having selected an appropriate board based on the resolution required, speed, etc., the next
1 ;   issue the user has to address is the type of connection to use.
BL-   The selection of input type is intimately linked to the issue of grounding and is discussed
2
together in some detail. As is mentioned earlier, there are three ground points to consider:
(i) Safety Ground: This is connected to the ground of the mains. As the name implies this
is a safety line and is not suitable for signal lines.
(ii) Digital Ground: This is a signal ground defined for digital signals and should be used
as such. Connecting analog signals to this line is not desirable.
(iii) Analog Ground or Reference: This is also referred to as signal ground. This is the
ground to be used with all the analog signals.
Grounding considerations can form the text matter for a book by itself. Let us consider the
various types of connections in detail. The interface card has the safety (or system) ground,
analog ground, digital ground and the signal sense (analog reference) lines. The analog and
digital grounds are connected to the safety ground at some (ideally only one) point.
There are three options available (National Instruments nomenclature in parentheses):
1. Differential (Differential—DI)
2. Referenced to a common signal reference (Non-Referenced Single Ended—NRSE)
3. Referenced to the safety ground (Referenced Single Ended—RSE)
********** 8 **********
--- page 9 ---
Figure 4.4 Differential Connection.
The multiplexer is in two halves which are operated in a linked pair for differential input.
For the other two connections, the multiplexer is connected as a single body. This
immediately brings out the main drawback in the DI connection. Half the input channels
are lost to the user, i.e., a 16-channel board when used in a differential configuration
can accept at most 8 inputs. It is good practice to ground the unused input connections,
though one must add that this advice is more often than not followed in the breach. The
configuration of the multiplexer and the various signal lines in a differential connection is
shown in Fig. 4.4 For a 16-channel board, the input lines corresponding to channel n are n
and (n + 8) pin numbers. As has been stated earlier, the board capacity in terms of the
number of channels is reduced by a factor of two. Any signal arriving on both the input
lines (common-mode signal) will be rejected by the amplifier which is set up to operate as
a differential amplifier. The output of the amplifier is referenced to the analog ground. The
signal sense line is not used. In this configuration, the safety ground of the system will at
some point be connected to the signal ground. For the average user, some simple thumb
rules can be prescribed:
The differential configuration is by far the best from the noise point of view. However, the
loss of 50% capacity in terms of the number of channels is a serious handicap.
The DI connection is the only one useable for floating signals, as is invariably the case in
bridge connections. Also, for low-level signals, e.g., thermocouple (typical output 6–50μ
V/°C), the differential connection is the only one suitable due to noise considerations. In
many transducers which are now available with built-in electronics (e.g., dc–dc LVDTs),
the signals are floating and hence have to be used with the DI connection.
********** 9 **********
--- page 10 ---
Figure 4.5 NRSE Connection.
Differences between the NRSE and RSE signals are more subtle. These are illustrated in
figures 4.5 and 4.6, respectively. Close examination would reveal the following. First, the
two halves of the multiplexer are operating as a single unit providing the full complement
of 16 channels. Second, while in NRSE all signals are referenced to the signal sense (or
common) line, in RSE the signal ground is used instead. Consequently, in an NRSE or RSE,
the user loses the benefit of rejection of the common-mode signal. In RSE the risk of ground
loops is far higher.
Figure 4.6 RSE Connection.
CO- b Write a note on Polymorphism in Array Operations.   (07)
3;
SO-   By definition polymorphism is said to be the ability of a numeric function to adjust to input data of
1 ;
BL-   different data structures. Polymorphism of LabVIEW is applicable to arrays as well. Hence, one can
2   add a scalar to an array or add two arrays using the same function. It is important to note that for the
********** 10 **********
--- page 11 ---
same function different types of operations are performed for different combinations. For example, if
a scalar and an array are added, the scalar is added to each element of the array. However, when two
arrays are added, each element of one array is added to the corresponding element of the other array.
All LabVIEW arithmetic functions are polymorphic. This means that the inputs to these functions can
be   different   data   structures   such   as   scalar   values   and   arrays.
For example, the Add function can be used in the following ways.
1. Scalar + Scalar = Scalar addition.
2. Scalar + Array = The scalar is added to each element of array.
3. Array + Array = Each element of one array is added to the corresponding element of other array.
********** 11 **********
--- page 12 ---
Figure 5.15 (a) Adding two scalar values, (b) adding a scalar value with an array, (c) adding two arrays of the
same size and (d) adding two arrays of different sizes.
In Figure 5.15(a), two scalar values are added which results in a scalar output. In Figure 5.15(b), an
array is added with a scalar value. The function adds the scalar value to each element of the array and
returns the array output. In Figure 5.15(c), two arrays are added. The function adds each element of
one array to the corresponding element of the other array and returns the array output. In Figure 5.15(d),
two arrays of different sizes (i.e. number of elements) are added. The function adds corresponding
elements and returns the output array, with the size of the smaller input array. The first array consists
of three elements and the second consists of four elements. First three elements of both the arrays are
added. The fourth element of the second array is not considered. Polymorphism does not perform matrix
arithmetic when inputs are two-dimensional arrays (for example, two two-dimensional array inputs to
a multiply function do element by element multiplication, not matrix multiplication).
CO- c   Explanation of the common standards of serial port communication   (06)
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse,
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections
between PC serial ports and devices. RS-232 is the connector found on most PCs. This is a
single-ended communication method where only one device can be connected per port. Two
connector types are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and
multidrop capability make RS-485 an attractive choice in industrial applications that require
many distributed devices networked to a PC or other controller for data collection and other
operations.
Q.3
CO- a   Explanation of Measurement and Automation Explorer in detail.   (07)
4;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all device
1 ;   and channel configuration parameters. After installing a DAQ device in the computer, you must
BL-   run this configuration utility. MAX reads the information the Device Manager records in the
2
Windows Registry and assigns a logical device number to each DAQ device. Use the device
number to refer to the device in LabVIEW. Access MAX either by double-clicking the icon on
the desktop or selecting Tools»Measurement & Automation Explorer in LabVIEW. The device
parameters that you can set using the configuration utility depend on the device. MAX saves
the logical device number and the configuration parameters in the Windows Registry. The plug
and play capability of Windows automatically detects and configures switchless DAQ devices,
such as the PCI-6024E. When you install a device in the computer, the device is automatically
detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation of
********** 12 **********
--- page 13 ---
NI-DAQ. MAX is used primarily to configure and test National Instruments hardware, but it
offers other functionality, such as checking to see if you have the latest version of NI-DAQ
installed. The functionality of MAX is divided into four categories—Data Neighborhood,
Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc., which
may have been installed. Devices and Interfaces lists various options like DAQ boards (under
DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc. The Legacy option
has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred. The
Software function helps to launch and update various software items from NI. Remote Systems,
which is a top-level option, at par with My System, provides access to various DAQ systems
connected through the Ethernet, or other parts.
CO- b   Explanation of data types and the importance of them with colors in LabVIEW programs   (06)
2;
SO-   Data Type   Details   Color
1 ;   Boolean   Booleans have   only   two   possible Green
BL-
values: True or False .
2
Integers   Integers can   Blue
be signed or unsigned whole numbers
Doubles   Doubles and Singles are signed numbers Orange
with a decimal component
Strings   Strings are sequences of characters   Pink
Clusters   Clusters are groups of various data Thick Brown
types
Path   Path is location of file on local PC Dark Green
System
CO- c   Explanation of the basic difference between the traditional instruments and software-based (07)
1;   virtual instruments.
SO-   Block diagram   (02)
1 ;
********** 13 **********
--- page 14 ---
BL-
2   A traditional instrument is designed to collect data from an environment, or from a unit under
test, and to display information to a user based on the collected data. Such an instrument may
employ a transducer to sense changes in a physical parameter such as temperature or pressure,
and to convert the sensed information into electrical signals such as voltage or frequency
variations. The term “instrument” may also cover a physical or software device that performs
an analysis on data acquired from another instrument and then outputs the processed data to
display or recording means. This second category of instruments includes oscilloscopes,
spectrum analyzers and digital millimeters. The types of source data collected and analyzed by
instruments may thus vary widely, including both physical parameters such as temperature,
pressure, distance, light and sound frequencies and amplitudes, and also electrical parameters
including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements defines
general-purpose measurement and   control hardware   functionality. With   virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have used
virtual instrumentation to downsize automated test equipment (ATE) while experiencing up to
a several times increase in productivity gains at a fraction of the cost of traditional instrument
solutions. Virtual instrumentation is necessary because it is flexible. It delivers instrumentation
with the rapid adaptability required for today’s concept, product and process design,
development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of features
that are rarely, if ever used. Most conventional instruments do not have any computational
power as compared to a virtual instrument. Since the virtual instrument is part of a person
computer configuration, the personal computer’s computational as well as controlling
capability can be applied into a test configuration. Virtual instruments are compatible with
traditional instruments almost without exception. Virtual instrumentation software typically
provides libraries for interfacing with common ordinary instrument buses such as GPIB, serial
or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt the
instrument to our particular needs. A traditional instrument might contain an integrated circuit
to perform a particular set of data processing functions; in a virtual instrument, these functions
would be performed by software running on the PC processor. We can extend the set of
functions easily, limited only by the power of the software used. By employing virtual
instrumentation solutions, we can lower capital costs, system development costs, and system
maintenance costs, while improving time to market and the quality of our own products.
********** 14 **********
--- page 15 ---
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
Q.4
a   Explain with the help of suitable diagram any 02 Cluster operations.
Ans:
Bundle: The Bundle function assembles individual components into a single new cluster and also allows one to
replace elements in an existing order. Initially, the function shows only two inputs, which can be increased by
dragging a corner of the function. As each input terminal is wired, a symbol representing the data type of the
wired element appears on the empty terminal. The order of the resultant cluster will be the order of inputs to the
bundle. The cluster input at the centre of the function is used only when one or more elements of the cluster are
to be replaced. Hence, this terminal is ignored while creating a new cluster. When the above function is used to
replace an element, the number of input terminals must match with those in the cluster. However, one needs to
wire only the new value(s) of the element(s) to be replaced.
CO-
2;
SO-
1 ;   [07]
BL-
2   Fig. 5.10 Bundle Function
Unbundle: The Unbundle function splits a cluster into its individual components. The output components are
arranged top to bottom in the same order that they have in the cluster. If the elements have the same data type,
the order of the elements in the cluster is the only way one can distinguish between them. It is important to resize
the function to contain the same number of outputs as there are elements in the input cluster.
Fig. 5.11 Unbundle Function
********** 15 **********
--- page 16 ---
Bundle by Name: When it is required to operate on a few elements and not the entire cluster elements, you use
the Bundle By Name function. In the Bundle by Name function elements are referenced by names rather than by
position. Here one can access only the elements needed. Also, this function cannot create new clusters, but can
only replace an element in an existing cluster. The only prerequisite, for the Bundle by Name function to work is
that all the elements must have names.
Fig. 5.12 Bundle by Name Function
Unbundle by Name: The Unbundle by Name function returns the cluster elements whose names are specified.
The major advantage of this function is that one does not have to keep track of the order of the elements within
the cluster. Also, this function does not require the number of elements to match the number in the cluster.
Fig. 5.13 Unbundle by Name Function
Any 02 from above
Description   02*2.5=05Marks
Diagram   02*01= 02Marks
CO- b   Explanation of any Two File Formats in detail.   03 Marks X 02 = 06 Marks (06)
3;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally   it becomes the most commonly used format, especially in
instrumentation applications. Needless to say, one has to convert all data to ASCII
strings before saving data. The major disadvantage of this format is that the text
files tend to be larger than the other formats. At one time this was a major
handicap, but with the ever-increasing capacity of storage media, this is no longer
a major handicap. Another disadvantage was speed, since the conversion of binary
data (internal format) to ASCII, and the transfer of the larger volume of data to
the disk were both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
********** 16 **********
--- page 17 ---
text files and reading and writing operations can be done with little data
conversion. Binary file format is useful in applications requiring writing and
reading of large chunks of data due to its size advantage. However, with the
increasing availability of large storage devices at reasonable cost, this advantage
is being progressively lost. Also, binary format is often system (or processor)
dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single
arbitrary data type specified during creation of the file. The data is indexed in
terms of these records. Each record in a measurement file must have the same data
types associated with it. One interesting feature of these files is that timestamps
are also included with each record. Also, LabVIEW allows random read access to
the binary versions of these files.
CO- c   Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by itself
2
does not provide instrumentation programming capability. VISA is a high-level API that calls
low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based
instruments and makes the appropriate driver calls depending on the type of instrument used.
When debugging VISA problems, remember that an apparent VISA problem could be an
installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If
the LabVIEW instrument driver was written with functions on the Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers
use VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend
required the definition of hardware standards to ensure the compatibility between different
modules. This was one of the factors leading to the development of the VXI specification. But
even with these improved hardware standards, a system was time consuming and expensive to
put together. Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
********** 17 **********
--- page 18 ---
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
Q.5
CO- a   Explain Industry Standard Architecture (ISA) in detail.   (07)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in 1987
2
when the IEEE (Institute of Electrical and Electronics Engineers) formally documented
standards governing its 16-bit implementation. AT version of the bus is called the AT bus
and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most common
type of early expansion bus, which was designed for use in the original IBM PC. The IBM
PC-XT used an 8-bit bus design. This means that the data transfers take place in 8 bit chunks
(i.e. one byte at a time) across the bus. The ISA bus ran at a clock speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits of
data at a time, was announced. The 16-bit version of the ISA bus is sometimes known as the
AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as the
processor. It was improved over the years and eventually the AT bus ran at a clock speed of
8MHz.
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single user
systems with 80386 and 80486 processors. There are 24 address lines and 16 data lines in it.
It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The data transfer rate
of the system is less when 8-bit. ISA bus is used with 32 bit processor having 32 bit address
and data bus. So, 16 bit ISA bus is used to transfer data. Many peripherals such as disk
controller, printer, and scanner can be connected to ISA bus.
CO- b   Explanation of Event Structure   (05)
2;   Example   (02)
SO-
1 ;
********** 18 **********
--- page 19 ---
BL-   a. Event Structure:
2
The Event structure waits until an event happens and then executes the
appropriate case to handle that event. Right-click the structure border to add new
event cases and configure which events to handle. Wire a value to the Timeout
terminal as shown at the top left of the Event structure to specify the number of
milliseconds the Event structure should wait for an event to occur. The default
is –1, indicating never to time out. The Event Data Node is attached to the inside
left and right borders of each event case. The node identifies the data LabVIEW
returns when an event occurs. The node displays data that is different in each
case of the Event structure depending on which event(s) you configure that case
to handle. If you configure a single case to handle multiple events, only the data
that is common to all handled event types is available. When you place an Event
structure on the block diagram, the Timeout event case is the default case. When
you place an Event structure on the block diagram from the Application
Control»Events palette, the structure displays the Event Dynamic Registration
terminals. When you place an Event structure on the block diagram from the
Structures palette, the structure does not display the terminals.
CO- c   Explaination of Express VI and Sub VI.   (06)
2;
SO-   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
1 ;   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
BL-   block diagram, its front panel and block diagram appear. The front panel includes controls and
4   indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as
a subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement
tasks. You can save the configuration of an Express VI as a subVI.
Express VIs are interactive VIs with configurable dialog page but Standard VIs are
modularized VIs customized by wiring. LabVIEW uses colored icons to distinguish between
Express VIs, VIs and functions on the block diagram. By default, icons for Express VIs appear
on the block diagram as expandable nodes with icons surrounded by a blue field. Icons for VIs
have white backgrounds, and icons for functions have pale yellow backgrounds. By default,
most functions and VIs on the block diagram appear as icons that are not expandable, unlike
Express VIs.
Q6   Open a blank VI and Build a VI to add or subtract two numbers. Use Case structures and text   (20)
CO-   ring to switch between addition and subtraction.
2   a. Save the VI as menu_tee.vi on desktop
&5;   b. Print the VI by selecting option Icon, description, panel and diagram in Print contents.
SO-
1;
********** 19 **********
--- page 20 ---
BL-   Ans :
6
Q.7
Open a blank VI and Build a VI to create a 2D numeric array (5 X 5) containing random   (20)
CO-   numbers as well as to find its transpose.
2   a. Build the front panel and the block diagram to create a 2D numeric array (5 X 5)
&5;   containing random numbers as well as to find its transpose.
SO-   b. Save the VI as quad_tee.vi on desktop
1;   c. Print the VI by selecting option Icon, description, panel and diagram in Print contents
BL-
6
Ans :
Fig a . Front Panel
********** 20 **********
--- page 21 ---
Fig b . Block Diagram
Please note that In front panel, 5 X 5 Matrix is random generated so it will be different for
users.
Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper ba509b9af23e

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechatronics_7004/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: mixed (21 pages), mean OCR confidence 61.6

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
a Explain the important function of SCADA
Ans:
CO   The important functions of an SCADA are listed below
-1 ;   1. Data Acquisition
SO   2. Information Display
-1 ;   3. Supervisory Control   (05)
4. Alarm Processing
BL   5. Information Storage and Reports
-2   6. Sequence of Event Acquisition
7. Data Calculation
8. Special RTU Processing/Control
CO- b Explanation of the basic difference between the traditional instruments and software-based (04)
1;   virtual instruments.
SO-   Block diagram   (01)
1 ;
BL-   A traditional instrument is designed to collect data from an environment, or from a unit
2
under test, and to display information to a user based on the collected data. Such an
instrument may employ a transducer to sense changes in a physical parameter such as
temperature or pressure, and to convert the sensed information into electrical signals such
as voltage or frequency variations. The term “instrument” may also cover a physical or
software device that performs an analysis on data acquired from another instrument and
then outputs the processed data to display or recording means. This second category of
instruments includes oscilloscopes, spectrum analyzers and digital millimeters. The types
of source data collected and analyzed by instruments may thus vary widely, including both
physical parameters such as temperature, pressure, distance, light and sound frequencies
and amplitudes, and also electrical parameters including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
********** 1 **********
--- page 2 ---
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements
defines general-purpose measurement and control hardware functionality. With virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have
used virtual instrumentation to downsize automated test equipment (ATE) while
experiencing up to a several times increase in productivity gains at a fraction of the cost of
traditional instrument solutions. Virtual instrumentation is necessary because it is flexible.
It delivers instrumentation with the rapid adaptability required for today’s concept, product
and process design, development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of
features that are rarely, if ever used. Most conventional instruments do not have any
computational power as compared to a virtual instrument. Since the virtual instrument is
part of a person computer configuration, the personal computer’s computational as well as
controlling capability can be applied into a test configuration. Virtual instruments are
compatible with traditional instruments almost without exception. Virtual instrumentation
software typically provides libraries for interfacing with common ordinary instrument
buses such as GPIB, serial or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt
the instrument to our particular needs. A traditional instrument might contain an integrated
circuit to perform a particular set of data processing functions; in a virtual instrument, these
functions would be performed by software running on the PC processor. We can extend
the set of functions easily, limited only by the power of the software used. By employing
virtual instrumentation solutions, we can lower capital costs, system development costs,
and system maintenance costs, while improving time to market and the quality of our own
products.
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
********** 2 **********
--- page 3 ---
CO- c Explanation of for loop in LabVIEW :   (05)
2;
SO-   FOR LOOPS
1 ;
BL-   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
2   LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The
For Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop
from the palette and use the cursor to drag a selection rectangle to create a new For Loop or
around the section of the block diagram you want to repeat. You also can place a While Loop on
the block diagram, right-click the border of the While Loop, and select Replace with For Loop
from the shortcut menu to change a While Loop to a For Loop.
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat
the subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top
side of the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is
explained in chapter 5. A VI will not run if it contains a For Loop that does not have a numeric
value   wired   to   the   count   terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations.
The iteration count always starts at zero. During the first iteration, the iteration terminal returns 0.
Figure 4.2 shows a simple For Loop which generates 10 random numbers and displays in the
Random Number Indicator.
********** 3 **********
--- page 4 ---
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- d Explanation of the classification of signals in the data acquisition system.   (05)
3;
SO-   1) Signals: The appropriate transducer converts the physical phenomena into
1 ;   measurable signals. However, different signals need to be measured in different
BL-   ways. For this reason, it is important to understand the different types of signals
2
and their corresponding attributes. Signals can be categorized into two groups:
analog and digital.
a) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load.
The three primary characteristics of an analog signal include level, shape and
frequency as shown in Figure 4.2.
Figure 4.2 Primary characteristics of an analog signal.
********** 4 **********
--- page 5 ---
Level gives vital information about the measured analog signal since analog
signals can take on any value. The intensity of a light source, the temperature in a room,
and the pressure inside a chamber are all examples that demonstrate the importance of the
level of a signal. When measuring the level of a signal, the signal generally does not change
quickly with respect to time. The accuracy of the measurement, however, is very important.
A DAQ system that yields maximum accuracy should be chosen to aid in analog level
measurements.
b) Digital Signals : A digital signal cannot take on any value with respect to time.
Instead, a digital signal has two possible levels: high and low. Digital signals
generally conform to certain specifications that define the characteristics of the
signal. Digital signals are commonly referred to as Transistor-to-Transistor Logic
(TTL). TTL specifications indicate a digital signal to be low when the level falls
within 0 to 0.8 volts, and the signal is high between 2 to 5 volts. The useful
information that can be measured from a digital signal includes the state and the
rate as shown in Figure 4.3.
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or
low. Monitoring the state of a switch—open or closed—is a common application showing
the importance of knowing the state of a digital signal.
Q.2
a Outline the merits of Virtual Instruments and explain each merit in detail.
Ans:
1. Performance: In terms of performance, LabVIEW includes a compiler that produces native code for the
CO   CPU platform. The graphical code is translated into executable machine code by interpreting the syntax and
-1;
SO   by compilation. The run-time engine and its libraries can be provided freely along with the executable.
-1 ;   2. Platform-Independent Nature: A benefit of the LabVIEW environment is the platform-independent   (08)
nature of the G-code, which is (with the exception of a few platform specific functions) portable between
BL   the different LabVIEW systems for different operating systems (Windows, MacOSX, and Linux).
-4
3. Flexibility: The general architecture of stand-alone instruments is very similar to that of a PC-based
virtual instrument. Both require one or more microprocessors, communication ports (for example, serial
and GPIB), and display capabilities, as well as data acquisition modules. These devices differ from one
********** 5 **********
--- page 6 ---
another in their flexibility and the fact that these devices can be modified and adapted to the particular
needs. A traditional instrument might contain an integrated circuit to perform a particular set of data
processing functions; in a virtual instrument, these functions would be performed by software running on
the PC processor.
4. Lower Cost: By employing virtual instrumentation solutions, lower capital costs, system development
costs, and system maintenance costs are reduced, increasing the time to market and improving the quality
of our own products.
5. Plug-In and Networked Hardware: There is a wide variety of available hardware that can either be
plugged into the computer or accessed through a network. These devices offer a wide range of data
acquisition capabilities at a significantly lower cost than that of dedicated devices. As integrated circuit
technology advances, and off-the-shelf components become cheaper and more powerful, so do the boards
that use them. With these advances in technology there arises an increase in data acquisition rates,
measurement accuracy, precision, and better signal isolation. Depending on the particular application, the
hardware we choose might include analog input or output, digital input or output, counters, timers, filters,
simultaneous sampling, and waveform generation capabilities. The wide gamut of boards and hardware
could include any one of these features or a combination of them.
6. The Costs of a Measurement Application: The costs involved in the development of a measurement
application can be divided into five distinct areas composed of hardware and software prices and several
time costs. The price of the hardware and software was considered as the single largest cost of their most
recent test or measurement system. However, the cumulative time costs in the other areas make up the
largest portion of the total application cost.
7. Reducing System Specification Time Cost: Deciding the types of measurements to take and the types
of analysis to perform takes time. Once the user has set the measurement specifications, the user must then
determine exactly the method to implement the measurement system. The time taken to perform these two
steps equals the system specification time.
8. Lowering the Cost of Hardware and Software: The price of measurement hardware and software is
undoubtedly the most visible cost of a data-acquisition system. Many people attempt to save money in this
area without considering the effect on the total development cost. The price of hardware and software, on
an average, makes up about 36 per cent of the total application cost. However, the time and money spent in
other areas of the development process make up the majority of the total application cost. VI lowers not
only time costs but it also helps to minimize hardware and software costs.
9. Minimizing Set-Up and Configuration Time Costs: Once the users have specified and purchased
measurement hardware, the real task of developing the application begins. However, the user must first
install the hardware and software, configure any necessary setting and ensure that all pieces of the system
function properly. This set-up and configuration stage also includes any necessary fixturing, such as sensor
connection, wiring and any preparation of the unit under test. Therefore, saving time in set-up and
configuration can result in a large reduction in the total application cost. VI again delivers this cost
reduction with a combination of off-the-shelf technology and intelligent software.
10. Decreasing Application Software Development Time Costs: Developing the measurement
application code typically consumes about 30%, which can be sometimes as high as 50% of the overall
measurement application cost. Time-saving application development tools can often greatly reduce costs in
this stage.
********** 6 **********
--- page 7 ---
Any 08 points from above (or any other suitable points)   1*08=08
b Explanation of Usage of SCADA
1. Electric power generation, transmission and distribution: Electric utilities use
SCADA
systems to detect current flow and line voltage, to monitor the operation of circuit
breakers, and to take sections of the power grid online or offline.
2. Water and sewage: State and municipal water utilities use SCADA to monitor and
CO-   regulate water flow, reservoir levels, pipe pressure and other factors.
1;   3. Buildings, facilities and environments: Facility managers use SCADA to control
SO-   HVAC,
(06)
1 ;   refrigeration units, lighting and entry systems.
BL-   4. Manufacturing: SCADA systems manage parts inventories for just-in-time
2   manufacturing,
regulate industrial automation and robots, and monitor process and quality control.
5. Mass transit: Transit authorities use SCADA to regulate electricity to subways, trams
and trolley buses; to automate traffic signals for rail systems; to track and locate trains
and buses; and to control railroad crossing gates.
6. Traffic signals: SCADA regulates traffic lights, controls traffic flow and detects out-of-
order signals.
c With the help of suitable diagram, write about
a. Write to Text File.
b. Read from Text File.
Ans:
Write to Text File
The Write to Text File function intermediate VI writes a string of characters or an array of strings as lines
to a file. If path to the file is not given the VI would open a file dialog. Appending to an existing file can be
done by setting the file position to the end of the file by using the Set File Position function. Similarly, file
position needs to be set appropriately for performing random access file reads or writes.
CO
-2 ;
SO
-1 ;   (06)
BL
-2   Read from Text File
The Read from Text File function intermediate VI reads a specified number of characters or lines from a
byte stream file. Count input is the maximum number of characters or lines the function reads. In the
default mode, count specifies the number of characters to be read. By right-clicking on the function count
could be changed to specify the number of lines. If count is < 0, the function reads the entire file.
Description 1.5 Marks   02*1.5 Marks = 03 Marks
Diagram   1.5 Marks   02*1.5 Marks = 03 Marks
Q.3
********** 7 **********
--- page 8 ---
CO- a Explanation of Measurement and Automation Explorer in detail.   (06)
3;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all
1 ;   device and channel configuration parameters. After installing a DAQ device in the
BL-   computer, you must run this configuration utility. MAX reads the information the Device
2
Manager records in the Windows Registry and assigns a logical device number to each
DAQ device. Use the device number to refer to the device in LabVIEW. Access MAX
either by double-clicking the icon on the desktop or selecting Tools»Measurement &
Automation Explorer in LabVIEW. The device parameters that you can set using the
configuration utility depend on the device. MAX saves the logical device number and the
configuration parameters in the Windows Registry. The plug and play capability of
Windows automatically detects and configures switchless DAQ devices, such as the PCI-
6024E. When you install a device in the computer, the device is automatically detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you
access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation
of NI-DAQ. MAX is used primarily to configure and test National Instruments hardware,
but it offers other functionality, such as checking to see if you have the latest version of
NI-DAQ installed. The functionality of MAX is divided into four categories—Data
Neighborhood, Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc.,
which may have been installed. Devices and Interfaces lists various options like DAQ
boards (under DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc.
The Legacy option has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred.
The Software function helps to launch and update various software items from NI. Remote
Systems, which is a top-level option, at par with My System, provides access to various
DAQ systems connected through the Ethernet, or other parts.
CO b Define SCADA. Explain the block diagram of SCADA in detail.
-1 ;
SO   Ans:
-1 ;
********** 8 **********
--- page 9 ---
Definition of SCADA: A collection of equipment that will provide an operator at remote location with enough
BL   information to determine the status of a particular piece of a equipment or entire substation and cause actions (01
-2
to take place regarding the equipment or network.
)
Consider the block diagram of SCADA system shown in the figure which consists of
different blocks, namely Human-machine Interface (HMI), Supervisory system, Remote
terminal units, PLCs, Communication infrastructure and SCADA Programming.
Block Diagram
(01
)
(01
)
1. Human-machine Interface (HMI)
It is an input-output device that presents the process data to be controlled by a human
operator. It is used by linking to the SCADA system’s software programs and databases
for providing the management information, including the scheduled maintenance
procedures, detailed schematics, logistic information, trending and diagnostic data for
a specific sensor or machine. HMI systems facilitate the operating personnel to see the
information graphically.
********** 9 **********
--- page 10 ---
Human-Machine Interface
(01
2. Supervisory System
)
Supervisory system is used as server for communicating between the equipment of the
SCADA system such as RTUs, PLCs and sensors, etc., and the HMI software used in
the control room workstations. Master station or supervisory station comprises a single
PC in smaller SCADA systems and, in case of larger SCADA systems, supervisory
system comprises distributed software applications, disaster recovery sites and multiple
servers. These multiple servers are configured in a hot-standby formation or dual-
redundant, which continuously controls and monitors in case of a server failure for
increasing the integrity of the system.
3. Remote Terminal Units
(01
Physical objects in the SCADA systems are interfaced with the microprocessor
controlled electronic devices called as Remote Terminal Units (RTUs). These units are   )
used to transmit telemetry data to the supervisory system and receive the messages
from the master system for controlling the connected objects. Hence, these are also
called as Remote Telemetry Units.
4. Programmable Logic Controllers
In SCADA systems, PLCs are connected to the sensors for collecting the sensor output
signals in order to convert the sensor signals into digital data. PLCs are used instead of
RTUs because of the advantages of PLCs like flexibility, configuration, versatile and
affordability compared to RTUs.   (01
)
Programmable Logic Controllers
5. Communication Infrastructure
Generally the combination of radio and direct wired connections is used for SCADA
systems, but in case of large systems like power stations and railways SONET/SDH are
frequently used. Among the very compact SCADA protocols used in SCADA systems –
a few communication protocols, which are standardized and recognized by SCADA
vendors – send information only when the supervisory station polls the RTUs.
********** 10 **********
--- page 11 ---
6. SCADA Programming   (01
SCADA programming in a master or HMI is used for creating maps and diagrams which   )
will give an important situational information in case of an event failure or process
failure. Standard interfaces are used for programming most commercial SCADA
systems. SCADA programming can be done using derived programming language or C
language.   (01
)
CO- c Explanation of Sub VI   (04)
2;   Example   (02)
SO-
1 ;   SubVIs are VIs that you build to use inside of another VI or that you access on the
BL-   Functions
2
palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on
the block diagram, its front panel and block diagram appear. The front panel includes
controls and indicators. The block diagram includes wires, front panel icons, functions,
possibly subVIs and other LabVIEW objects. The upper-right corner of the front panel and
block diagram displays the icon for the VI. This is the icon that appears when you place
the VI on a block diagram as a subVI. SubVIs also can be Express VIs. Express VIs are
nodes that require minimal wiring because you configure them with dialog boxes. Use
Express VIs for common measurement tasks. You can save the configuration of an Express
VI as a subVI.
Q.4
CO- a Explanation of the various types of graphs and charts in LabVIEW.   (04)
2;   Explanation of basic difference between Graphs from chart.   (04)
SO-
1 ;   GRAPHS AND CHARTS
BL-
2   Displaying data is equally important and sometimes even more important than acquiring it.
Therefore, good display tools are a necessity. More often than not data needs to be presented
graphically. Also, when data is being analyzed graphical output of the analysis is often required.
The graphical display of data is a very important aspect of programming in LabVIEW. In most
situations, two-dimensional X-Y displays are required. LabVIEW provides three tools for this,
namely, the waveform chart, the waveform graph, and the X-Y graph. While the first two deals
with data which is equally spaced along the X-axis, the last is especially for situations where the
X-intervals are not equal. All these objects can be accessed from the panel through either the
Express VI function on the Graph Indicators palette, or through the All Controls palette and the
Graph Menu. VI’s with graph usually collects the data in an array and then plots the data to the
graph to obtain a waveform.
Charts and graphs let you display plots of data in a graphical form. Charts interactively plot data,
appending new data to old so that you can see the current value in the context of previous data, as
the new data become available. Graphs plot pre-generated arrays of values in a more traditional
fashion without retaining previously-generated data.
********** 11 **********
--- page 12 ---
WAVEFORM GRAPHS
LabVIEW includes the waveform graph and chart to display data typically acquired at a constant
rate. The waveform graph displays one or more plots of evenly sampled measurements. The
waveform graph plots only single-valued functions, as in y = f (x), with points evenly distributed
along the x-axis, such as acquired time-varying waveforms. Figure 7.1 shows an example of a
waveform graph. The waveform graph can display plots containing any number of points. The
graph also accepts several data types, which minimizes the extent to which you must manipulate
data before you display it.
Figure 7.1 Waveform Graph.
WAVEFORM CHARTS
The waveform chart is a special type of numeric indicator that displays one or more plots of data
typically acquired at a constant rate. Waveform charts can display single or multiple plots. Figure
7.3 shows the elements of a multiplot waveform chart. Two plots are displayed: Raw Data and
Running Avg.
The waveform chart maintains a history of data or buffer from previous updates.
Figure 7.3 A waveform chart.
CO- b Explanation of PC based DAQ system   (04)
3;   Block diagram.   (02)
SO-
1 ;
BL-   ➢ Data Acquisition (DAQ) System
2
********** 12 **********
--- page 13 ---
The fundamental task of a DAQ (Data Acquisition) system is to measure or generate real-
world physical signals. Data acquisition involves gathering signals from measurement
sources and digitizing the signal for storage, analysis and presentation on a personal
computer (PC). Data acquisition systems come in many different PC technology forms for
great flexibility. The five components to be considered when building a basic DAQ system
as shown in Figure 4.1 are transducers, signals, signal conditioning, DAQ hardware, and
driver and application software.
Figure 4.1 Data acquisition system.
2) A transducer: It is a device that converts a physical phenomenon into a measurable
electrical signal, such as voltage or current. The ability of a DAQ system to measure
different phenomena depends on the transducers to convert the physical phenomena
into signals measurable by the DAQ hardware. Transducers are synonymous with
sensors in DAQ systems. There are specific transducers for many different
applications, such as measuring temperature, pressure or fluid flow. Table 4.1
shows a short list of some common transducers and the phenomena they can
measure.
TABLE 4.1 Phenomena and existing transducers
3) Signals: The appropriate transducer converts the physical phenomena into
measurable signals. However, different signals need to be measured in different
ways. For this reason, it is important to understand the different types of signals
and their corresponding attributes. Signals can be categorized into two groups:
analog and digital.
********** 13 **********
--- page 14 ---
c) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load.
The three primary characteristics of an analog signal include level, shape and
frequency as shown in Figure 4.2.
Figure 4.2 Primary characteristics of an analog signal.
Level gives vital information about the measured analog signal since analog
signals can take on any value. The intensity of a light source, the temperature in a room,
and the pressure inside a chamber are all examples that demonstrate the importance of the
level of a signal. When measuring the level of a signal, the signal generally does not change
quickly with respect to time. The accuracy of the measurement, however, is very important.
A DAQ system that yields maximum accuracy should be chosen to aid in analog level
measurements.
d) Digital Signals : A digital signal cannot take on any value with respect to time.
Instead, a digital signal has two possible levels: high and low. Digital signals
generally conform to certain specifications that define the characteristics of the
signal. Digital signals are commonly referred to as Transistor-to-Transistor Logic
(TTL). TTL specifications indicate a digital signal to be low when the level falls
within 0 to 0.8 volts, and the signal is high between 2 to 5 volts. The useful
information that can be measured from a digital signal includes the state and the
rate as shown in Figure 4.3.
********** 14 **********
--- page 15 ---
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or
low. Monitoring the state of a switch—open or closed—is a common application showing
the importance of knowing the state of a digital signal.
4) Signal conditioning: Signal conditioning is the process of measuring and
manipulating signals to improve accuracy, isolation, filtering, and so on. Many
stand-alone instruments and DAQ devices have built-in signal conditioning. Signal
conditioning also can be applied externally, by designing a circuit to condition the
signal or by using devices specifically made for signal conditioning. National
Instruments has SCXI devices and other devices that are designed for this purpose.
Signal conditioning accessories can be used in a variety of important applications.
Signal conditioning accessories amplify low-level signals and then isolate and filter
them for more accurate measurements. In addition, some transducers use voltage
or current excitation to generate a voltage output. Common types of signal
conditioning are amplification, isolation, multiplexing, filtering, transducer
excitation and linearization.
a) Amplification:
Amplification is the most common type of signal conditioning. Amplifying
electrical signals improves accuracy in the resulting digitized signal and reduces
the effects of noise. Signals should be amplified as close to the signal source as
possible.
b) Isolation
Another common signal conditioning application is isolating the transducer signals
from the computer for safety purposes. The system being monitored may contain
high-voltage transients that could damage the computer without signal
conditioning.
c) Multiplexing
A common technique for measuring several signals with a single measuring device
is multiplexing. Signal conditioning hardware for analog signals often provides
multiplexing for use with slowly changing signals like temperature.
d) Filtering
The purpose of a filter is to remove unwanted signals from the signal that you are
trying
********** 15 **********
--- page 16 ---
to measure.
e) Transduces Excitation
Signal conditioning systems can generate excitation, which some transducers
require for operation. Strain gauges and RTDs require external voltage and
currents, respectively, to excite their circuitry into measuring physical
phenomena.
f) Linearization
Another common signal conditioning function is linearization. Many
transducers, such as thermocouples, have a nonlinear response to changes in the
physical phenomena you measure. LabVIEW can linearize the voltage levels
from transducers so you can scale the voltages to the measured phenomena.
LabVIEW provides scaling functions to convert voltages from strain gages,
RTDs, thermocouples, and thermistors.
5) DAQ Hardware Configuration: Before using a data acquisition board, you must
confirm that the software can communicate with the board by configuring the
devices. The Windows Configuration Manager keeps track of all the hardware
installed in the computer, including National Instruments DAQ devices. If you have
a Plug & Play (PnP) device, such as an E Series MIO device, the Windows
Configuration Manager automatically detects and configures the device. If you
have a non-PnP device, or legacy device, you must configure the device manually
using the Add New Hardware option in the Control Panel. You can verify the
Windows Configuration by accessing the Device Manager.
CO- c Explanation of RS-232 and RS-485 standards of serial port communication.
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a (03)
1 ;   mouse, printer, or modem. It is also used with industrial instrumentation. Because of
BL-   improvements in line drivers and cables, applications often increase the performance of
2
RS-232 beyond the distance and speed in the standards list. RS-232 is limited to point-to-
point connections between PC serial ports and devices. RS-232 is the connector found on
most PCs. This is a single-ended communication method where only one device can be
connected per port. Two connector types are 9 or 25-pin. Two configurations are DCE or
DTE.
(03)
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure
adequate signal voltages under maximum load. With this enhanced multidrop capability,
you can create networks of devices connected to a single RS-485 serial port. The noise
immunity and multidrop capability make RS-485 an attractive choice in industrial
applications that require many distributed devices networked to a PC or other controller
for data collection and other operations.
Q5
CO- a Explanation of VISA   (06)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by
2
itself does not provide instrumentation programming capability. VISA is a high-level API
that calls low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or
********** 16 **********
--- page 17 ---
computer-based instruments and makes the appropriate driver calls depending on the type
of instrument used. When debugging VISA problems, remember that an apparent VISA
problem could be an installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB,
serial, VXI and computer-based instruments. You do not need to use separate I/O palettes
to program an instrument. For example, some instruments give you a choice for the type
of interface. If the LabVIEW instrument driver was written with functions on the
Functions»All Functions»Instrument I/O»GPIB palette, those instrument driver VIs would
not work for the instrument with the serial port interface. VISA solves this problem by
providing a single set of functions that work for any type of interface. Therefore, many
LabVIEW instrument drivers use VISA as the I/O language. For many years, industry has
moved toward purchasing instrumentation from a variety of vendors. This allows engineers
to select the best possible equipment for their applications without being locked into a
specific vendor. This trend required the definition of hardware standards to ensure the
compatibility between different modules. This was one of the factors leading to the
development of the VXI specification. But even with these improved hardware standards,
a system was time consuming and expensive to put together. Successful integration of a
multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
b Write about Block Diagram Window of LabVIEW.
Ans:
The block diagrams accompany the program for the front panel. Front panel objects appear as terminals on
the block diagram and the components wired together. After the front panel is built, codes are added using
CO   graphical representations of functions in the block diagram to control the front panel objects. The block
-1 ;   diagram contains the graphical source code composed of nodes, terminals, and wires. The block diagram is
SO   the actual executable program as shown in Figure 2.2. The components of a block diagram are lower-level
-1 ;   (08)
VIs, built-in functions, constants and program execution control structures. Wires have to be drawn to
BL   connect the corresponding objects together to indicate the flow of data between each of them. Front panel
-2   objects have analogous terminals on the block diagram so that data can pass easily from the user to the
program and back to the user. Use Express VIs, standard VIs and functions on the block diagram to create
our measurement code. Block diagram objects include the terminals, subVIs, functions, constants,
structures and wires. LabVIEW is the easiest, most powerful tool for acquiring, analyzing and presenting
real-world data. Terminals are entry and exit ports that exchange information between the panel and the
********** 17 **********
--- page 18 ---
diagram. Terminals are analogous to parameters and constants in text-based programming languages.
Right-click the block diagram objects and select View As icon to change the icon view.
Description   03
Diagram   03
CO- c Explain Industry Standard Architecture (ISA) in detail.   (04)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in
2
1987 when the IEEE (Institute of Electrical and Electronics Engineers) formally
documented standards governing its 16-bit implementation. AT version of the bus is
called the AT bus and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most
common type of early expansion bus, which was designed for use in the original IBM
PC. The IBM PC-XT used an 8-bit bus design. This means that the data transfers take
place in 8 bit chunks (i.e. one byte at a time) across the bus. The ISA bus ran at a clock
speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits
of data at a time, was announced. The 16-bit version of the ISA bus is sometimes known
as the AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as
the processor. It was improved over the years and eventually the AT bus ran at a clock
speed of 8MHz.
********** 18 **********
--- page 19 ---
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single
user systems with 80386 and 80486 processors. There are 24 address lines and 16 data
lines in it. It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The
data transfer rate of the system is less when 8-bit. ISA bus is used with 32 bit processor
having 32 bit address and data bus. So, 16 bit ISA bus is used to transfer data. Many
peripherals such as disk controller, printer, and scanner can be connected to ISA bus.
Q6   Create a VI to find the roots of a quadratic equation. Display both the values of the roots   (20
and the nature of the roots whether roots are real or complex or equal.   )
CO-
2 &   a. Build the front panel as shown in Figure a
b. Build the block diagram to find the roots of a quadratic equation
5;   c. Save the VI as quad_tee.vi on desktop
SO-   d. Print the VI by selecting option Icon, description, panel and diagram in Print
contents
1 ;
BL-
6
Figure a
Ans :
********** 19 **********
--- page 20 ---
Front Panel   : 06 Marks
Block Diagram : 10 Marks
Correct Output : 04 Marks
Q7   Open a blank VI and Build a VI that generates 50 random numbers and plot it on a   (20
waveform chart using For Loop. Accumulate the random numbers into an array and
)
display it on waveform.
a. Save the VI as for_tee.vi on desktop
CO-
b. Print the VI by selecting option Icon, description, panel and diagram in Print
2 &   contents.
5;
Ans :
SO-
1 ;
BL-
6
********** 20 **********
--- page 21 ---
Using For Loop

Eo}

ca ¥}

Navetorm
@ chat
[=> dost
To

Maveform|
Graph
foot

' ' ' t 1 ' t 1 ' ' 1
0 5 10 15 20 25 30 35 40 45 SO
Time

(a) Front panel (b) Block diagram

FI ICR D7 FAC HOH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper debc4f5f9a51

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a   Explanation of the different debugging processes in LabVIEW.   (05)
2;
SO-
1 ;   Fixing Broken VIs
BL-
2
If a VI does not run, it is a broken, or nonexecutable, VI. The Run button appears broken
when the VI you are creating or editing contains errors..
Broken Run Button
Generally, this means that a required input is not wired, or a wire is broken. Press the
broken Run button to access the Error list window. The Error list window lists each error
and describes the problem. You can double-click an error to go directly to the error.
Warnings do not prevent you from running a VI. They are designed to help you avoid
potential problems in VIs. Errors, however, can break a VI. You must resolve any errors
before you can run the VI.
Finding Causes for Broken VIs
Click the broken Run button or select View>>Error to find out why a VI is broken. The
Error list window lists all the errors. The Items with errors section lists the names of all
items in memory, such as VIs and project libraries that have errors. If two or more items
have the same name, this section shows the specific application instance for each item.
The errors and warnings section lists the errors and warnings for the VI you select in the
Items with errors section. The Details section describes the errors and in some cases
********** 1 **********
--- page 2 ---
recommends how to correct the errors. Click the Help button to display a topic in the
LabVIEW Help that describes the error in detail and includes step-by-step instructions for
correcting the error.
Click the Show Error button or double-click the error description to highlight the area on
the block diagram or front panel that contains the error.
Figure 1: The Error list dialog box lists each error and describes the problem.
Common Causes of Broken VIs
The following list contains common reasons why a VI is broken while you edit it:
▪ The block diagram contains a broken wire because of a mismatch of data types or a
loose, unconnected end. Refer to the Correcting Broken VIs topic of the LabVIEW Help
for information about correcting broken wires.
▪ A required block diagram terminal is unwired. Refer to the Using Wires to Link Block
Diagram Objects topic of the LabVIEW Help for information about setting required
inputs and outputs.
▪ A subVI is broken or you edited its connector pane after you placed its icon on the
block diagram of the VI.
Back to top
********** 2 **********
--- page 3 ---
Fixing Incorrect Behavior
If your VI runs but produces incorrect results then you have a functional error in your
code. LabVIEW provides several tools to help you analyze where your VI is not behaving
as expected.
Block Diagram Toolbar
When you run a VI, buttons appear on the block diagram toolbar that you can use to
debug the VI. The following toolbar appears on the block diagram.
Click the Highlight Execution button to display an animation of the block diagram
execution when you run the VI. Notice the flow of data through the block diagram. Click
the button again to disable execution highlighting.
Highlight Execution
Execution highlighting shows the movement of data on the block diagram from one
node to another using bubbles that move along the wires. Use execution highlighting in
conjunction with single-stepping to see how data values move from node to node
through a VI.
Note: Execution highlighting greatly reduces the speed at which the VI runs.
********** 3 **********
--- page 4 ---
Figure 2: Execution highlighting shows the movement of data.
You can pause the execution of a VI at any time by choosing the pause button on the
toolbar.
Execution Pause
The color of the button turns to red when the VI is paused. Once you pause the VI, you
can use the tools below to gain additional insight into the execution of your application.
Click the Retain Wire Values button to save the wire values at each point in the flow of
execution so that when you place a probe on the wire you can immediately retain the
most recent value of the data that passed through the wire.
Retain Wire Values
You must successfully run the VI at least once before you can retain the wire values.
Click the Step Into button to open a node and pause.
Step Into
When you click the Step Into button again, it executes the first action and pauses at the
next action of the subVI or structure. You also can press the ctrl and down arrow keys.
Single-stepping through a VI steps through the VI node by node. Each node blinks to
denote when it is ready to execute.
Click the Step Over button to execute a node and pause at the next node.
Step Over
You also can press the ctrl and right arrow keys. By stepping over the node, you execute
the node without single-stepping through the node.
Click the Step Out button to finish executing the current node and pause.
Step Out
When the VI finishes executing, the Step Out button is dimmed. You also can press the
ctrl and up arrow keys. By stepping out of a node, you complete single-stepping through
the node and navigate to the next node.
********** 4 **********
--- page 5 ---
The Warning button appears if a VI includes a warning and you placed a checkmark in
the Show Warnings checkbox in the Error list window.
Warning
A warning indicates there is a potential problem with the block diagram, but it does not
stop the VI from running.
Probe Watch Window
Use the Probe tool (View>>Probe Watch Window) to check intermediate values on a
wire as a VI runs. Move your cursor over a wire while the VI is running or right-click on
the wire and choose Probe to generate a probe. Use the Probe tool if you have a
complicated block diagram with a series of operations, any one of which might return
incorrect data. Use the Probe tool with execution highlighting, single-stepping, and
breakpoints to determine if and where data is incorrect. If data is available, the probe
immediately updates and displays the data in the Probe Watch Window during execution
highlighting, single-stepping, or when you pause at a breakpoint.
Figure 3: The Probe Watch Window displays any and all probes active in your project.
When execution pauses at a node because of single-stepping or a breakpoint, you also
can probe the wire that just executed to see the value that flowed through that wire.
Breakpoint Manager
You can use the Breakpoint Manager (View>>Breakpoint Manager) to view, add, or
delete breakpoints from your code. A breakpoint will pause the execution of the VI when
that specific object is executed. You can place a VI, structure, wire, or operator.
********** 5 **********
--- page 6 ---
Figure 4: You can use the Breakpoint Manager to add, delete, or view breakpoints in
your code.
CO-   b   Explanation of for loop in LabVIEW :   (05)
3;
SO-   FOR LOOPS
1 ;   A For Loop executes a subdiagram, a set number of times. Figure 4.1(a) shows a For Loop in
BL-4
LabVIEW and Figure 4.1(b) shows the flow chart equivalent of the For Loop functionality. The For
Loop is located on the Functions>>Programming>>Structures Palette. Select the For Loop from the
palette and use the cursor to drag a selection rectangle to create a new For Loop or around the section
of the block diagram you want to repeat. You also can place a While Loop on the block diagram,
right-click the border of the While Loop, and select Replace with For Loop from the shortcut menu to
change a While Loop to a For Loop.
********** 6 **********
--- page 7 ---
The value in the count terminal ‘N’ (an input terminal) indicates how many times to repeat the
subdiagram. Set the count explicitly by wiring a value from outside the loop to the left or top side of
the count terminal, or set the count implicitly with auto-indexing. Auto-indexing is explained in chapter
5. A VI will not run if it contains a For Loop that does not have a numeric value wired to the count
terminal.
The iteration terminal ‘i’ (an output terminal) contains the number of completed iterations. The
iteration count always starts at zero. During the first iteration, the iteration terminal returns 0. Figure
4.2 shows a simple For Loop which generates 10 random numbers and displays in the Random Number
Indicator.
Both the count and iteration terminals are 32-bit signed integers. If you wire a floating-point
number to the count terminal, LabVIEW rounds it and coerces it to within range. If you wire 0 or
a negative number to the count terminal, the loop does not execute and the outputs contain the
default data for that data type. A For Loop can only execute an integer a number of times.
CO- c   Explanation of Local variable   (05)
1;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a
local variable are right-click on an object’s terminal and select Create»Local Variable. A local
variable icon for the object appears on the block diagram as shown in Figure 4.23.
********** 7 **********
--- page 8 ---
(2.5)
d. Outline the objectives of Data Acquisition System.
Ans: Objectives of Data Acquisition System
1. It must acquire the necessary data, at correct speed and at the correct time.
CO-   2. Use of all data efficiently to inform the operator about the state of the system.
3 ;   3. It must monitor the complete plant operation to maintain on-line optimum and safe operations.
SO-   4. It must be able to collect, summarize and store data for diagnosis of operation and record purpose.
1 ;   (05)
5. It must be able to compute unit performance indices using online, real-time data.
BL-   6. It must be flexible and capable of being expanded for future require.
1   7. It must be reliable, and not have a down time greater than 0.1%.
8. It must provide an effective human communication system and be able to identify problem areas, there by
minimizing unit availability and maximizing unit through point at minimum cost.
Any 05 points from above (or any other suitable points)   1*05=05
Q.2
CO- a   Explanation of the three methods of grounding of DAQ devices.   (07)
4;
SO-   Having selected an appropriate board based on the resolution required, speed, etc., the next
1 ;   issue the user has to address is the type of connection to use.
BL-   The selection of input type is intimately linked to the issue of grounding and is discussed
2
together in some detail. As is mentioned earlier, there are three ground points to consider:
(i) Safety Ground: This is connected to the ground of the mains. As the name implies this
is a safety line and is not suitable for signal lines.
(ii) Digital Ground: This is a signal ground defined for digital signals and should be used
as such. Connecting analog signals to this line is not desirable.
(iii) Analog Ground or Reference: This is also referred to as signal ground. This is the
ground to be used with all the analog signals.
Grounding considerations can form the text matter for a book by itself. Let us consider the
various types of connections in detail. The interface card has the safety (or system) ground,
analog ground, digital ground and the signal sense (analog reference) lines. The analog and
digital grounds are connected to the safety ground at some (ideally only one) point.
There are three options available (National Instruments nomenclature in parentheses):
1. Differential (Differential—DI)
2. Referenced to a common signal reference (Non-Referenced Single Ended—NRSE)
3. Referenced to the safety ground (Referenced Single Ended—RSE)
********** 8 **********
--- page 9 ---
Figure 4.4 Differential Connection.
The multiplexer is in two halves which are operated in a linked pair for differential input.
For the other two connections, the multiplexer is connected as a single body. This
immediately brings out the main drawback in the DI connection. Half the input channels
are lost to the user, i.e., a 16-channel board when used in a differential configuration
can accept at most 8 inputs. It is good practice to ground the unused input connections,
though one must add that this advice is more often than not followed in the breach. The
configuration of the multiplexer and the various signal lines in a differential connection is
shown in Fig. 4.4 For a 16-channel board, the input lines corresponding to channel n are n
and (n + 8) pin numbers. As has been stated earlier, the board capacity in terms of the
number of channels is reduced by a factor of two. Any signal arriving on both the input
lines (common-mode signal) will be rejected by the amplifier which is set up to operate as
a differential amplifier. The output of the amplifier is referenced to the analog ground. The
signal sense line is not used. In this configuration, the safety ground of the system will at
some point be connected to the signal ground. For the average user, some simple thumb
rules can be prescribed:
The differential configuration is by far the best from the noise point of view. However, the
loss of 50% capacity in terms of the number of channels is a serious handicap.
The DI connection is the only one useable for floating signals, as is invariably the case in
bridge connections. Also, for low-level signals, e.g., thermocouple (typical output 6–50μ
V/°C), the differential connection is the only one suitable due to noise considerations. In
many transducers which are now available with built-in electronics (e.g., dc–dc LVDTs),
the signals are floating and hence have to be used with the DI connection.
********** 9 **********
--- page 10 ---
Figure 4.5 NRSE Connection.
Differences between the NRSE and RSE signals are more subtle. These are illustrated in
figures 4.5 and 4.6, respectively. Close examination would reveal the following. First, the
two halves of the multiplexer are operating as a single unit providing the full complement
of 16 channels. Second, while in NRSE all signals are referenced to the signal sense (or
common) line, in RSE the signal ground is used instead. Consequently, in an NRSE or RSE,
the user loses the benefit of rejection of the common-mode signal. In RSE the risk of ground
loops is far higher.
Figure 4.6 RSE Connection.
CO- b Write a note on Polymorphism in Array Operations.   (07)
3;
SO-   By definition polymorphism is said to be the ability of a numeric function to adjust to input data of
1 ;
BL-   different data structures. Polymorphism of LabVIEW is applicable to arrays as well. Hence, one can
2   add a scalar to an array or add two arrays using the same function. It is important to note that for the
********** 10 **********
--- page 11 ---
same function different types of operations are performed for different combinations. For example, if
a scalar and an array are added, the scalar is added to each element of the array. However, when two
arrays are added, each element of one array is added to the corresponding element of the other array.
All LabVIEW arithmetic functions are polymorphic. This means that the inputs to these functions can
be   different   data   structures   such   as   scalar   values   and   arrays.
For example, the Add function can be used in the following ways.
1. Scalar + Scalar = Scalar addition.
2. Scalar + Array = The scalar is added to each element of array.
3. Array + Array = Each element of one array is added to the corresponding element of other array.
********** 11 **********
--- page 12 ---
Figure 5.15 (a) Adding two scalar values, (b) adding a scalar value with an array, (c) adding two arrays of the
same size and (d) adding two arrays of different sizes.
In Figure 5.15(a), two scalar values are added which results in a scalar output. In Figure 5.15(b), an
array is added with a scalar value. The function adds the scalar value to each element of the array and
returns the array output. In Figure 5.15(c), two arrays are added. The function adds each element of
one array to the corresponding element of the other array and returns the array output. In Figure 5.15(d),
two arrays of different sizes (i.e. number of elements) are added. The function adds corresponding
elements and returns the output array, with the size of the smaller input array. The first array consists
of three elements and the second consists of four elements. First three elements of both the arrays are
added. The fourth element of the second array is not considered. Polymorphism does not perform matrix
arithmetic when inputs are two-dimensional arrays (for example, two two-dimensional array inputs to
a multiply function do element by element multiplication, not matrix multiplication).
CO- c   Explanation of the common standards of serial port communication   (06)
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse,
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections
between PC serial ports and devices. RS-232 is the connector found on most PCs. This is a
single-ended communication method where only one device can be connected per port. Two
connector types are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and
multidrop capability make RS-485 an attractive choice in industrial applications that require
many distributed devices networked to a PC or other controller for data collection and other
operations.
Q.3
CO- a   Explanation of Measurement and Automation Explorer in detail.   (07)
4;
SO-   LabVIEW installs Measurement & Automation Explorer (MAX) which establishes all device
1 ;   and channel configuration parameters. After installing a DAQ device in the computer, you must
BL-   run this configuration utility. MAX reads the information the Device Manager records in the
2
Windows Registry and assigns a logical device number to each DAQ device. Use the device
number to refer to the device in LabVIEW. Access MAX either by double-clicking the icon on
the desktop or selecting Tools»Measurement & Automation Explorer in LabVIEW. The device
parameters that you can set using the configuration utility depend on the device. MAX saves
the logical device number and the configuration parameters in the Windows Registry. The plug
and play capability of Windows automatically detects and configures switchless DAQ devices,
such as the PCI-6024E. When you install a device in the computer, the device is automatically
detected.
Measurement & Automation Explorer, or MAX, is a software interface that gives you access
to all National Instruments DAQ, GPIB, IMAQ, IVI, Motion, VISA, and VXI devices
connected to your system. The shortcut to MAX is placed on the desktop during installation of
********** 12 **********
--- page 13 ---
NI-DAQ. MAX is used primarily to configure and test National Instruments hardware, but it
offers other functionality, such as checking to see if you have the latest version of NI-DAQ
installed. The functionality of MAX is divided into four categories—Data Neighborhood,
Devices and Interfaces, Scales and Software.
MAX when fired up shows the various options shown in Fig. 4.7.
Figure 4.7 Options in MAX.
The Data Neighborhood function deals with various systems like CAN, Fieldpoint, etc., which
may have been installed. Devices and Interfaces lists various options like DAQ boards (under
DAQmx as well as Legacy NIDAQ devices), PXI crates, serial ports, etc. The Legacy option
has to be installed by the user, and is not there by default.
Some versions of the drivers demand that the hardware not be present in the system when
Legacy drivers are installed. The Scales function helps to change the scaling of various
channels. This includes the definition of polynomial scales, look-up tables, etc. However,
unless it is a totally dedicated system, data manipulation in LabVIEW code is preferred. The
Software function helps to launch and update various software items from NI. Remote Systems,
which is a top-level option, at par with My System, provides access to various DAQ systems
connected through the Ethernet, or other parts.
CO- b   Explanation of data types and the importance of them with colors in LabVIEW programs   (06)
2;
SO-   Data Type   Details   Color
1 ;   Boolean   Booleans have   only   two   possible Green
BL-
values: True or False .
2
Integers   Integers can   Blue
be signed or unsigned whole numbers
Doubles   Doubles and Singles are signed numbers Orange
with a decimal component
Strings   Strings are sequences of characters   Pink
Clusters   Clusters are groups of various data Thick Brown
types
Path   Path is location of file on local PC Dark Green
System
CO- c   Explanation of the basic difference between the traditional instruments and software-based (07)
1;   virtual instruments.
SO-   Block diagram   (02)
1 ;
********** 13 **********
--- page 14 ---
BL-
2   A traditional instrument is designed to collect data from an environment, or from a unit under
test, and to display information to a user based on the collected data. Such an instrument may
employ a transducer to sense changes in a physical parameter such as temperature or pressure,
and to convert the sensed information into electrical signals such as voltage or frequency
variations. The term “instrument” may also cover a physical or software device that performs
an analysis on data acquired from another instrument and then outputs the processed data to
display or recording means. This second category of instruments includes oscilloscopes,
spectrum analyzers and digital millimeters. The types of source data collected and analyzed by
instruments may thus vary widely, including both physical parameters such as temperature,
pressure, distance, light and sound frequencies and amplitudes, and also electrical parameters
including voltage, current and frequency.
A virtual instrument (VI) is defined as an industry-standard computer equipped with user
friendly application software, cost-effective hardware and driver software that together
perform the functions of traditional instruments. Simulated physical instruments are called
virtual instruments (VIs). Virtual instrumentation software based on user requirements defines
general-purpose measurement and   control hardware   functionality. With   virtual
instrumentation, engineers and scientists reduce development time, design higher quality
products, and lower their design costs. In test, measurement and control, engineers have used
virtual instrumentation to downsize automated test equipment (ATE) while experiencing up to
a several times increase in productivity gains at a fraction of the cost of traditional instrument
solutions. Virtual instrumentation is necessary because it is flexible. It delivers instrumentation
with the rapid adaptability required for today’s concept, product and process design,
development and delivery.
Traditional instruments and software-based virtual instruments largely share the same
architectural components, but radically different philosophies as shown in Figure 3.
Conventional instruments as compared to a virtual instrumentation can be very large and
cumbersome. They also require a lot of power, and often have excessive amounts of features
that are rarely, if ever used. Most conventional instruments do not have any computational
power as compared to a virtual instrument. Since the virtual instrument is part of a person
computer configuration, the personal computer’s computational as well as controlling
capability can be applied into a test configuration. Virtual instruments are compatible with
traditional instruments almost without exception. Virtual instrumentation software typically
provides libraries for interfacing with common ordinary instrument buses such as GPIB, serial
or Ethernet.
Except for the specialized components and circuitry found in traditional instruments, the
general architecture of stand-alone instruments is very similar to that of a PC-based virtual
instrument. Both require one or more microprocessors, communication ports (for example,
serial and GPIB), and display capabilities, as well as data acquisition modules. What makes
one different from the other is their flexibility and the fact that we can modify and adapt the
instrument to our particular needs. A traditional instrument might contain an integrated circuit
to perform a particular set of data processing functions; in a virtual instrument, these functions
would be performed by software running on the PC processor. We can extend the set of
functions easily, limited only by the power of the software used. By employing virtual
instrumentation solutions, we can lower capital costs, system development costs, and system
maintenance costs, while improving time to market and the quality of our own products.
********** 14 **********
--- page 15 ---
FIG.3: Traditional instruments (left) and software based virtual instruments (right).
Q.4
a   Explain with the help of suitable diagram any 02 Cluster operations.
Ans:
Bundle: The Bundle function assembles individual components into a single new cluster and also allows one to
replace elements in an existing order. Initially, the function shows only two inputs, which can be increased by
dragging a corner of the function. As each input terminal is wired, a symbol representing the data type of the
wired element appears on the empty terminal. The order of the resultant cluster will be the order of inputs to the
bundle. The cluster input at the centre of the function is used only when one or more elements of the cluster are
to be replaced. Hence, this terminal is ignored while creating a new cluster. When the above function is used to
replace an element, the number of input terminals must match with those in the cluster. However, one needs to
wire only the new value(s) of the element(s) to be replaced.
CO-
2;
SO-
1 ;   [07]
BL-
2   Fig. 5.10 Bundle Function
Unbundle: The Unbundle function splits a cluster into its individual components. The output components are
arranged top to bottom in the same order that they have in the cluster. If the elements have the same data type,
the order of the elements in the cluster is the only way one can distinguish between them. It is important to resize
the function to contain the same number of outputs as there are elements in the input cluster.
Fig. 5.11 Unbundle Function
********** 15 **********
--- page 16 ---
Bundle by Name: When it is required to operate on a few elements and not the entire cluster elements, you use
the Bundle By Name function. In the Bundle by Name function elements are referenced by names rather than by
position. Here one can access only the elements needed. Also, this function cannot create new clusters, but can
only replace an element in an existing cluster. The only prerequisite, for the Bundle by Name function to work is
that all the elements must have names.
Fig. 5.12 Bundle by Name Function
Unbundle by Name: The Unbundle by Name function returns the cluster elements whose names are specified.
The major advantage of this function is that one does not have to keep track of the order of the elements within
the cluster. Also, this function does not require the number of elements to match the number in the cluster.
Fig. 5.13 Unbundle by Name Function
Any 02 from above
Description   02*2.5=05Marks
Diagram   02*01= 02Marks
CO- b   Explanation of any Two File Formats in detail.   03 Marks X 02 = 06 Marks (06)
3;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally   it becomes the most commonly used format, especially in
instrumentation applications. Needless to say, one has to convert all data to ASCII
strings before saving data. The major disadvantage of this format is that the text
files tend to be larger than the other formats. At one time this was a major
handicap, but with the ever-increasing capacity of storage media, this is no longer
a major handicap. Another disadvantage was speed, since the conversion of binary
data (internal format) to ASCII, and the transfer of the larger volume of data to
the disk were both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
********** 16 **********
--- page 17 ---
text files and reading and writing operations can be done with little data
conversion. Binary file format is useful in applications requiring writing and
reading of large chunks of data due to its size advantage. However, with the
increasing availability of large storage devices at reasonable cost, this advantage
is being progressively lost. Also, binary format is often system (or processor)
dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single
arbitrary data type specified during creation of the file. The data is indexed in
terms of these records. Each record in a measurement file must have the same data
types associated with it. One interesting feature of these files is that timestamps
are also included with each record. Also, LabVIEW allows random read access to
the binary versions of these files.
CO- c   Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the
BL-   LabVIEW instrument driver VIs that communicates with the driver software. VISA by itself
2
does not provide instrumentation programming capability. VISA is a high-level API that calls
low-level drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based
instruments and makes the appropriate driver calls depending on the type of instrument used.
When debugging VISA problems, remember that an apparent VISA problem could be an
installation problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If
the LabVIEW instrument driver was written with functions on the Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers
use VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend
required the definition of hardware standards to ensure the compatibility between different
modules. This was one of the factors leading to the development of the VXI specification. But
even with these improved hardware standards, a system was time consuming and expensive to
put together. Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
********** 17 **********
--- page 18 ---
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the
alliance are to ensure multivendor interoperability for VXI systems and to reduce the
development time for an operational system.
Q.5
CO- a   Explain Industry Standard Architecture (ISA) in detail.   (07)
4;
SO-   The Industry Standard Architecture or ISA bus began as part of IBM’s revolutionary
1 ;
BL-   PC/XT and PC/AT released in 1981. However, it was officially recognized as “ISA” in 1987
2
when the IEEE (Institute of Electrical and Electronics Engineers) formally documented
standards governing its 16-bit implementation. AT version of the bus is called the AT bus
and became a de facto industry standard.
It was the original IBM expansion bus and initially no standard was assigned to it. Its first
version was the 8 bit bus and it ran at the speed of about 7 MHz. This is the most common
type of early expansion bus, which was designed for use in the original IBM PC. The IBM
PC-XT used an 8-bit bus design. This means that the data transfers take place in 8 bit chunks
(i.e. one byte at a time) across the bus. The ISA bus ran at a clock speed of 4.77 MHz.
For the 80286-based IBM PC-AT, an improved bus design, which could transfer 16-bits of
data at a time, was announced. The 16-bit version of the ISA bus is sometimes known as the
AT bus. (AT-Advanced Technology).
The improved AT bus also provided a total of 24 address lines, which allowed 16MB of
memory to be addressed. The AT bus was backward compatible with its 8-bit predecessor
and allowed 8-bit cards to be used in 16-bit expansion slots.
When it first appeared the 8-bit ISA bus ran at a speed of 4.77MHZ – the same speed as the
processor. It was improved over the years and eventually the AT bus ran at a clock speed of
8MHz.
ISA bus architecture
ISA bus architecture is the basis of personal computer. 8-bit ISA bus is used in single user
systems with 80386 and 80486 processors. There are 24 address lines and 16 data lines in it.
It operates at 8 MHz and 2 to 8 clock cycles are needed to transfer data. The data transfer rate
of the system is less when 8-bit. ISA bus is used with 32 bit processor having 32 bit address
and data bus. So, 16 bit ISA bus is used to transfer data. Many peripherals such as disk
controller, printer, and scanner can be connected to ISA bus.
CO- b   Explanation of Event Structure   (05)
2;   Example   (02)
SO-
1 ;
********** 18 **********
--- page 19 ---
BL-   a. Event Structure:
2
The Event structure waits until an event happens and then executes the
appropriate case to handle that event. Right-click the structure border to add new
event cases and configure which events to handle. Wire a value to the Timeout
terminal as shown at the top left of the Event structure to specify the number of
milliseconds the Event structure should wait for an event to occur. The default
is –1, indicating never to time out. The Event Data Node is attached to the inside
left and right borders of each event case. The node identifies the data LabVIEW
returns when an event occurs. The node displays data that is different in each
case of the Event structure depending on which event(s) you configure that case
to handle. If you configure a single case to handle multiple events, only the data
that is common to all handled event types is available. When you place an Event
structure on the block diagram, the Timeout event case is the default case. When
you place an Event structure on the block diagram from the Application
Control»Events palette, the structure displays the Event Dynamic Registration
terminals. When you place an Event structure on the block diagram from the
Structures palette, the structure does not display the terminals.
CO- c   Explaination of Express VI and Sub VI.   (06)
2;
SO-   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
1 ;   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
BL-   block diagram, its front panel and block diagram appear. The front panel includes controls and
4   indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as
a subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement
tasks. You can save the configuration of an Express VI as a subVI.
Express VIs are interactive VIs with configurable dialog page but Standard VIs are
modularized VIs customized by wiring. LabVIEW uses colored icons to distinguish between
Express VIs, VIs and functions on the block diagram. By default, icons for Express VIs appear
on the block diagram as expandable nodes with icons surrounded by a blue field. Icons for VIs
have white backgrounds, and icons for functions have pale yellow backgrounds. By default,
most functions and VIs on the block diagram appear as icons that are not expandable, unlike
Express VIs.
Q6   Open a blank VI and Build a VI to add or subtract two numbers. Use Case structures and text   (20)
CO-   ring to switch between addition and subtraction.
2   a. Save the VI as menu_tee.vi on desktop
&5;   b. Print the VI by selecting option Icon, description, panel and diagram in Print contents.
SO-
1;
********** 19 **********
--- page 20 ---
BL-   Ans :
6
Q.7
Open a blank VI and Build a VI to create a 2D numeric array (5 X 5) containing random   (20)
CO-   numbers as well as to find its transpose.
2   a. Build the front panel and the block diagram to create a 2D numeric array (5 X 5)
&5;   containing random numbers as well as to find its transpose.
SO-   b. Save the VI as quad_tee.vi on desktop
1;   c. Print the VI by selecting option Icon, description, panel and diagram in Print contents
BL-
6
Ans :
Fig a . Front Panel
********** 20 **********
--- page 21 ---
Fig b . Block Diagram
Please note that In front panel, 5 X 5 Matrix is random generated so it will be different for
users.
Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]
********** 21 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 5aab5406b096

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_DS_7009/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: mixed (22 pages), mean OCR confidence 66.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a Explanation of Sub VI   (03)
1;   Example   (02)
SO-
1 ;   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
BL-   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
2   block diagram, its front panel and block diagram appear. The front panel includes controls and
indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as a
subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement tasks.
You can save the configuration of an Express VI as a subVI.
CO- b Explanation of Stacked Sequence Structure   (05)
2;
SO-   a. Sequence Structure:
1 ;   A sequence structure contains one or more subdiagrams, or frames, that execute in
BL-   equential order. Within each frame of a sequence structure, as in the rest of the block diagram,
2
data dependency determines the execution order of nodes. Sequence structures are not used
commonly in LabVIEW. Use the sequence structures to control the execution order when natural
data dependency does not exist and flow-through parameters are not available. There are two
types of sequence structures— the Flat Sequence structure and the Stacked Sequence structure.
• Stacked Sequece Structure
The Stacked Sequence structure, shown as follows, stacks each frame so you see
only one frame at a time and executes frame 0, then frame 1, and so on until the
********** 1 **********
--- page 2 ---
last frame executes. The Stacked Sequence structure returns data only after the
last frame executes. Use the Stacked Sequence structure if you want to conserve
space on the block diagram. To convert a Stacked Sequence structure to a Flat
Sequence structure, right-click the Stacked Sequence structure and select
Replace»Replace with Flat Sequence from the shortcut menu. The sequence
selector identifier, shown as follows, at the top of the Stacked Sequence structure
contains the current frame number and range of frames.
CO- c Explanation of Local variable   (05)
2;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a local
variable are right-click on an object’s terminal and select Create»Local Variable. A local variable icon
for the object appears on the block diagram as shown in Figure 4.23.
CO- d Explanation of the classification of signals in the data acquisition system.   (05)
3;
SO-   1) Signals: The appropriate transducer converts the physical phenomena into measurable
1 ;   signals. However, different signals need to be measured in different ways. For this reason,
BL-   it is important to understand the different types of signals and their corresponding
2
attributes. Signals can be categorized into two groups: analog and digital.
a) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load. The
three primary characteristics of an analog signal include level, shape and frequency as
shown in Figure 4.2.
********** 2 **********
--- page 3 ---
Figure 4.2 Primary characteristics of an analog signal.
Level gives vital information about the measured analog signal since analog signals can
take on any value. The intensity of a light source, the temperature in a room, and the pressure
inside a chamber are all examples that demonstrate the importance of the level of a signal. When
measuring the level of a signal, the signal generally does not change quickly with respect to time.
The accuracy of the measurement, however, is very important. A DAQ system that yields
maximum accuracy should be chosen to aid in analog level measurements.
b) Digital Signals : A digital signal cannot take on any value with respect to time. Instead,
a digital signal has two possible levels: high and low. Digital signals generally conform
to certain specifications that define the characteristics of the signal. Digital signals are
commonly referred to as Transistor-to-Transistor Logic (TTL). TTL specifications
indicate a digital signal to be low when the level falls within 0 to 0.8 volts, and the signal
is high between 2 to 5 volts. The useful information that can be measured from a digital
signal includes the state and the rate as shown in Figure 4.3.
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or low.
Monitoring the state of a switch—open or closed—is a common application showing the
importance of knowing the state of a digital signal.
Q.2
********** 3 **********
--- page 4 ---
CO- a Explanation of PC based DAQ system   (05)
3;   Block diagram.   (02)
SO-
1 ;
BL-   ➢ Data Acquisition (DAQ) System
2
The fundamental task of a DAQ (Data Acquisition) system is to measure or generate real-world
physical signals. Data acquisition involves gathering signals from measurement sources and
digitizing the signal for storage, analysis and presentation on a personal computer (PC). Data
acquisition systems come in many different PC technology forms for great flexibility. The five
components to be considered when building a basic DAQ system as shown in Figure 4.1 are
transducers, signals, signal conditioning, DAQ hardware, and driver and application software.
Figure 4.1 Data acquisition system.
2) A transducer: It is a device that converts a physical phenomenon into a measurable
electrical signal, such as voltage or current. The ability of a DAQ system to measure
different phenomena depends on the transducers to convert the physical phenomena into
signals measurable by the DAQ hardware. Transducers are synonymous with sensors in
DAQ systems. There are specific transducers for many different applications, such as
measuring temperature, pressure or fluid flow. Table 4.1 shows a short list of some
common transducers and the phenomena they can measure.
TABLE 4.1 Phenomena and existing transducers
3) Signals: The appropriate transducer converts the physical phenomena into measurable
signals. However, different signals need to be measured in different ways. For this reason,
********** 4 **********
--- page 5 ---
it is important to understand the different types of signals and their corresponding
attributes. Signals can be categorized into two groups: analog and digital.
c) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load. The
three primary characteristics of an analog signal include level, shape and frequency as
shown in Figure 4.2.
Figure 4.2 Primary characteristics of an analog signal.
Level gives vital information about the measured analog signal since analog signals can
take on any value. The intensity of a light source, the temperature in a room, and the pressure
inside a chamber are all examples that demonstrate the importance of the level of a signal. When
measuring the level of a signal, the signal generally does not change quickly with respect to time.
The accuracy of the measurement, however, is very important. A DAQ system that yields
maximum accuracy should be chosen to aid in analog level measurements.
d) Digital Signals : A digital signal cannot take on any value with respect to time. Instead,
a digital signal has two possible levels: high and low. Digital signals generally conform
to certain specifications that define the characteristics of the signal. Digital signals are
commonly referred to as Transistor-to-Transistor Logic (TTL). TTL specifications
indicate a digital signal to be low when the level falls within 0 to 0.8 volts, and the signal
is high between 2 to 5 volts. The useful information that can be measured from a digital
signal includes the state and the rate as shown in Figure 4.3.
********** 5 **********
--- page 6 ---
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or low.
Monitoring the state of a switch—open or closed—is a common application showing the
importance of knowing the state of a digital signal.
4) Signal conditioning: Signal conditioning is the process of measuring and manipulating
signals to improve accuracy, isolation, filtering, and so on. Many stand-alone instruments
and DAQ devices have built-in signal conditioning. Signal conditioning also can be
applied externally, by designing a circuit to condition the signal or by using devices
specifically made for signal conditioning. National Instruments has SCXI devices and
other devices that are designed for this purpose. Signal conditioning accessories can be
used in a variety of important applications. Signal conditioning accessories amplify low-
level signals and then isolate and filter them for more accurate measurements. In addition,
some transducers use voltage or current excitation to generate a voltage output. Common
types of signal conditioning are amplification, isolation, multiplexing, filtering,
transducer excitation and linearization.
a) Amplification:
Amplification is the most common type of signal conditioning. Amplifying electrical
signals improves accuracy in the resulting digitized signal and reduces the effects of
noise. Signals should be amplified as close to the signal source as possible.
b) Isolation
Another common signal conditioning application is isolating the transducer signals from
the computer for safety purposes. The system being monitored may contain high-voltage
transients that could damage the computer without signal conditioning.
c) Multiplexing
A common technique for measuring several signals with a single measuring device is
multiplexing. Signal conditioning hardware for analog signals often provides
multiplexing for use with slowly changing signals like temperature.
d) Filtering
The purpose of a filter is to remove unwanted signals from the signal that you are trying
to measure.
e) Transduces Excitation
********** 6 **********
--- page 7 ---
Signal conditioning systems can generate excitation, which some transducers require
for operation. Strain gauges and RTDs require external voltage and currents,
respectively, to excite their circuitry into measuring physical phenomena.
f) Linearization
Another common signal conditioning function is linearization. Many transducers,
such as thermocouples, have a nonlinear response to changes in the physical
phenomena you measure. LabVIEW can linearize the voltage levels from transducers
so you can scale the voltages to the measured phenomena. LabVIEW provides scaling
functions to convert voltages from strain gages, RTDs, thermocouples, and
thermistors.
5) DAQ Hardware Configuration: Before using a data acquisition board, you must
confirm that the software can communicate with the board by configuring the devices.
The Windows Configuration Manager keeps track of all the hardware installed in the
computer, including National Instruments DAQ devices. If you have a Plug & Play (PnP)
device, such as an E Series MIO device, the Windows Configuration Manager
automatically detects and configures the device. If you have a non-PnP device, or legacy
device, you must configure the device manually using the Add New Hardware option in
the Control Panel. You can verify the Windows Configuration by accessing the Device
Manager.
CO- b Explanation of array and cluster.   (05)
2;   Arrays   Clusters   (02)
SO-   Array is a homogenous collection (i.e., all of the   A cluster is also a data structure that groups data.
1 ;   same type) of data elements.
BL-   An array can have one or more dimensions and up   a cluster can group data of different types.
2   to 231 elements per dimension (subject to the
memory capacity).
An array data element can be of any type except   In LabVIEW A cluster may be thought of as a
another array, a chart or a graph. An array with n   bundle of wires and is shown as a ‘rope’ in the
elements is indexed from 0 to (n-1) , with the first   block diagram.
element at index 0 and last one at index (n-1).
Clusters reduce wire clutter and the number of
connector terminals in a sub VI. On the block
diagram one can connect cluster terminals with
another cluster wire only if they have the same
type, the same number of elements and the same
order of elements. The cluster elements can be
accessed by unbundling them all at once or by
indexing one at a time.
Clusters are commonly used to pass a record
across VI’s. Clusters are also used for passing
error information between multiple VIs in a block
diagram.
any array can be converted into a cluster (in   A cluster can only be converted to an array when
a priori)   all the elements are of the same kind.
Made up of either controls or indicators.   Made up of either controls or indicators.
CO- c Explanation of RS-232 and RS-485 standards of serial port communication.
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse, (03)
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections between
PC serial ports and devices. RS-232 is the connector found on most PCs. This is a single-ended
********** 7 **********
--- page 8 ---
communication method where only one device can be connected per port. Two connector types
are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32 (03)
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and multidrop
capability make RS-485 an attractive choice in industrial applications that require many
distributed devices networked to a PC or other controller for data collection and other operations.
Q.3
CO- a Explanation of State Machine   (05)
2;   In its simplest form, a state machine comprises of a while loop, with a shift register
SO- 1 ;   and a case structure (Fig.1). The code starts by initialising the shift register to the
BL-   initial state of the system (from outside the while loop) which is entered into by the
2   case structure. At the end of the execution of the code corresponding to this state,
the case structure then sends the next state to the shift register. Then in the
following iteration of the while loop, this state is executed. This continues until the
While loop is terminated by the case structure. Note that the code is no longer
constrained to operate in a linear fashion, but can progress from state to state in a
non-linear manner. What is required is that the various states of the system must
be clearly defined. The next state can also be decided by the previous state,
depending on the logic in it. In the above example, a user acquiring data can easily
select options to acquire more data, change the configuration, save the data, analyse
the data, or stop the program and output the code of the appropriate case to the shift
register. Coding all these possibilities normally would be very difficult, if not
impossible. The labyrinth of the various possible transitions will render the code a
nightmare to develop, understand and debug. Developing and debugging such a
code is a Herculean task. Add similar sets of possibilities to other options and the
complexity of the task can be well imagined.
********** 8 **********
--- page 9 ---
(02)
Fig.1 Components of a State Machine
However, using the state machine, such a code can be easily developed and
debugged. The code for each state becomes an independent VI. These can be
developed and tested individually and subsequently combined in a state machine.
There is nothing to stop any particular state from spawning a state machine of
its own. The possibilities are mind-boggling.
Example
CO- b Explanation Formula Node with example   (04)
2;   FORMULA NODE
SO-
1 ;   Sometimes there is a requirement to program a piece of code in a conventional or quasi-
BL-   conventional way. This is possible in LabVIEW through the use of the Formula Node. The Formula
2
Node is a resizable box that you use to enter algebraic formulas directly into the block diagram. This
feature extremely useful when you have a long formula to solve.
Users envisaging the use of Formula Nodes are faced with the issue of reconciling the graphical
symbolism of LabVIEW with the alphanumeric representation in text based languages.
With the Formula Node, you can directly enter a formula or formulas, in lieu of creating complex block
diagram subsections. Simply enter the formula inside the box. You create the input and output terminals
of the Formula Node by popping up on the border of the node and choosing Add Input or Add Output
from the pop-up menu. Then enter variable names into the input and output terminals. Names are case
sensitive, and each formula statement must terminate with a semicolon (;).
You will find the Formula Node in the Programming>>Structures subpalette of the Functions
palette.
These operators and functions are available inside the Formula Node.
********** 9 **********
--- page 10 ---
As expected in a DataFlow environment, separate nodes have to be associated with the input and output
lists, i.e. if the user changes the value of an input variable inside the formula node the output has to be
done through a separate node.
Fig. 4.3 Formula node
Furthermore, a formula node does not support multithreading, i.e., as long as the formula node is
executing, operation of other blocks of code is not permitted. This is seldom a constraint since very
rarely does the code in the formula node takes any appreciable time to execute. Any complex coding is
best left for linking through DLLs or CINs. A single line formula node is also available for
convenience.
(02)
Example
CO- c Differentiate between text-based programming and graphical programming.   (07)
1;
SO-   Text-based programming   Graphical programming
1 ;
BL-   ● Syntax must be known to do programming. ●Syntax is knowledge but is not required for
4   ●The execution of the program is from top to Programming.
bottom.   ●The execution of program is from left to
●To check for the error the program has to be right.
compiled or executed.   ●Errors are indicated as we wire the blocks.
●Front panel design needs extra coding or ●Front   panel   design   is   a   part   of
needs extra work.   programming.
●Text-based programming is non interactive. ●Graphical   programming   is   highly
●This is text-based programming where the   interactive.
Programming is a conventional method.   ●The   programming   is   Data   Flow
●Logical Error finding is easy in large Programming.
programs.   ● Logical Error finding in large programs is
●Program flow is not visible.   quiet complicated.
●It is test-based programming.   ● Data flow is visible.
●Passing parameters to sub routine   is ● It is icon-based programming and wiring.
difficult.   ● Passing parameters to sub VI is easy.
Q.4
********** 10 **********
--- page 11 ---
CO- a Explanation of the various types of graphs and charts in LabVIEW.   (03)
2;   Explanation of basic difference between Graphs from chart.   (04)
SO-
1 ;   GRAPHS AND CHARTS
BL-
2   Displaying data is equally important and sometimes even more important than acquiring it. Therefore,
good display tools are a necessity. More often than not data needs to be presented graphically. Also,
when data is being analyzed graphical output of the analysis is often required. The graphical display of
data is a very important aspect of programming in LabVIEW. In most situations, two-dimensional X-Y
displays are required. LabVIEW provides three tools for this, namely, the waveform chart, the
waveform graph, and the X-Y graph. While the first two deals with data which is equally spaced along
the X-axis, the last is especially for situations where the X-intervals are not equal. All these objects can
be accessed from the panel through either the Express VI function on the Graph Indicators palette, or
through the All Controls palette and the Graph Menu. VI’s with graph usually collects the data in an
array and then plots the data to the graph to obtain a waveform.
Charts and graphs let you display plots of data in a graphical form. Charts interactively plot data,
appending new data to old so that you can see the current value in the context of previous data, as the
new data become available. Graphs plot pre-generated arrays of values in a more traditional fashion
without retaining previously-generated data.
WAVEFORM GRAPHS
LabVIEW includes the waveform graph and chart to display data typically acquired at a constant rate.
The waveform graph displays one or more plots of evenly sampled measurements. The waveform graph
plots only single-valued functions, as in y = f (x), with points evenly distributed along the x-axis, such as
acquired time-varying waveforms. Figure 7.1 shows an example of a waveform graph. The waveform
graph can display plots containing any number of points. The graph also accepts several data types,
which minimizes the extent to which you must manipulate data before you display it.
Figure 7.1 Waveform Graph.
WAVEFORM CHARTS
The waveform chart is a special type of numeric indicator that displays one or more plots of data typically
acquired at a constant rate. Waveform charts can display single or multiple plots. Figure 7.3 shows the
elements of a multiplot waveform chart. Two plots are displayed: Raw Data and Running Avg.
********** 11 **********
--- page 12 ---
The waveform chart maintains a history of data or buffer from previous updates.
Figure 7.3 A waveform chart.
CO- b Explanation of Any three String Functions   02 Marks X 3 = 06 Marks   (06)
2;   1) String Length: This function (Fig. 13) gives the number of characters
SO-   (bytes) in the input string. Being a polymorphic function, the length output
1 ;
BL-   has the same structure as the input.
2
Fig. 10 String Length function
2) Concatenate Strings: The Concatenate Strings function (Fig. 14) is useful
in concatenating input strings into a single output string. In addition to
simple strings one-dimensional arrays of strings can also be wired as inputs;
the output will be a single string containing a concatenation of all the strings
in the order they are connected, top to bottom, left to right. This function can
be used to concatenate strings to be written as text in files. In addition to the
text or characters indicating the application, string constants such as tab, line
feed, end of line, etc. can also be appended to the characters as required by
the application. This function is used very often to assemble commands for
instruments. In these cases (especially in serial interfacing) the string often
has to be terminated with an appropriate character or characters.
********** 12 **********
--- page 13 ---
Fig. 11 Concatenate Strings function
Similarly, for preparing data for writing to a file < TAB > is used as a
separator between items, and a terminator (an < EOL > is preferred to < CR
> and/or < LF >) since this makes the code platform independent.
3) Match Pattern: This function (Fig. 15) searches for a string pattern
(regular expression) in the input string beginning at offset, and if it finds a
match, it splits the string into three substrings, viz., before-substring,
match-substring and after-substring. If the Function does not find the
regular expression string pattern, match-substring is empty, before-
substring will have the entire string, after-substring is empty, and offset
past match is –1. The offset past match output is useful as an offset input
for another match pattern search.
Fig. 12 Match Pattern function
4) String Subset: The String Subset function (Fig. 16) returns the substring
of the input string beginning at offset and containing number of characters as
specified by length input. This function is useful to remove unwanted header/
data in a string.
Fig. 13 String Subset function
5) Get Date/Time String: The Get Date/Time String function (Fig. 17) is
available on the Timing & Dialog palette. It converts a time stamp value or
a numeric value to a date and time string in the time zone configured for
the computer.
********** 13 **********
--- page 14 ---
Fig. 14 Get Date/Time String (timing dialog palette)
CO- c Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the LabVIEW
BL-   instrument driver VIs that communicates with the driver software. VISA by itself does not
2
provide instrumentation programming capability. VISA is a high-level API that calls low-level
drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based instruments
and makes the appropriate driver calls depending on the type of instrument used. When
debugging VISA problems, remember that an apparent VISA problem could be an installation
problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If the
LabVIEW   instrument   driver was   written with   functions on   the   Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers use
VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend required
the definition of hardware standards to ensure the compatibility between different modules. This
was one of the factors leading to the development of the VXI specification. But even with these
improved hardware standards, a system was time consuming and expensive to put together.
Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the alliance
are to ensure multivendor interoperability for VXI systems and to reduce the development time
for an operational system.
Q5
CO- a Explanation of Versa Modular Eurocard bus.   (07)
4;
SO-   VME bus is a bus system (or a computer path system) for industrial applications such as
1 ;
BL-   VME power supplies, embedded single board computers (SBC), actuators automation, etc. It
2
was originally developed by Motorola technical employees in Germany (yr. 1980) and soon
after, also adopted by Signetics, Philips, Thomson, and Mostek.
********** 14 **********
--- page 15 ---
It was designed as a flexible interconnection between multiple master and slave devices using a
variety of address and data precisions, and has become a popular standard bus used in a variety
of products.
VME Features
A VME bus is a set of parallel conductors that interconnect multiple processing devices.
The devices can exchange data in units of 8, 16, 32 or 64 bits during a bus cycle.
VME Address Spaces
Each VME device identifies itself with a range of bus addresses. A bus address has either 16,
24, or 32 bits of precision. Each address width forms a separate address space. That is, the
same numeric value can refer to one device in the 24-bit address space but a different device in
the 32-bit address space. Typically, a device operates in only one address space, but some
devices can be configured to respond to addresses in multiple spaces.
Each VME bus cycle contains the bits of an address. The address is qualified by sets of
address-modifier bits that specify the following:
•   the address space (A16, A24, or A32).
• whether the operation is single or a block transfer.
• whether the access is to what, in the MC68000 architecture, would be data or code, in a
supervisor or user area (Silicon Graphics systems support only supervisor-data and
user-data requests).
Master and Slave Devices
Each VME device acts as either a bus master or a bus slave. Typically a bus master is a device
with some level of programmability, usually a microprocessor. A disk controller is an example
of a master device. A slave device is typically a nonprogrammable device like a memory board.
Each data transfer is initiated by a master device. The master
•   asserts ownership of the bus.
•   specifies the address modifier bits for the transfer, including the address space,
single/block mode, and supervisor/normal mode.
•   specifies the address for the transfer.
•   specifies the data unit size for the transfer (8, 16, 32 or 64 bits).
•   specifies the direction of the transfer with respect to the master.
The VME bus design permits multiple master devices to use the bus, and provides a hardware-
based arbitration system so that they can use the bus in alternation.
********** 15 **********
--- page 16 ---
A slave device responds to a master when the master specifies the slave's address. The
addressed slave accepts data, or provides data, as directed.
VME Transactions
The VME design allows for four types of data transfer bus cycles:
• A read cycle returns data from the slave to the master.
• A write cycle sends data from the master to the slave.
• A read-modify-write cycle takes data from the slave, and on the following bus cycle
sends it back to the same address, possibly altered.
• A block-transfer transaction sends multiple data units to adjacent addresses in a burst of
consecutive bus cycles.
The VME design also allows for interrupts. A device can raise an interrupt on any of
seven interrupt levels. The interrupt is acknowledged by a bus master. The bus master
interrogates the interrupting device in an interrupt-acknowledge bus cycle, and the device
returns an interrupt vector number.
VME Bus in Silicon Graphics Systems
The VME bus was designed as the system backplane for a workstation, supporting one or more
CPU modules along with the memory and I/O modules they used. However, no Silicon
Graphics computer uses the VME bus as the system backplane. In all Silicon Graphics
computers, the main system bus that connects CPUs to memory is a proprietary bus design,
with higher speed and sometimes wider data units than the VME bus provides. The VME bus is
attached to the system as an I/O device.
The VME Bus Controller
A VME bus controller is attached to the system bus to act as a bridge between the system bus
and the VME bus. This arrangement is shown in Figure 13-1.
********** 16 **********
--- page 17 ---
Figure 13-1. Relationship of VME Bus to System Bus
On the Silicon Graphics system bus, the VME bus controller acts as an I/O device. On the
VME bus, the bus controller acts as a VME bus master.
The VME controller has several tasks. Its most important task is mapping; that is, translating
some range of physical addresses in the Silicon Graphics system address space to a range
of VME bus addresses. The VME controller performs a variety of other duties for different
kinds of VME access.
VME PIO Operations
During programmed I/O (PIO) to the VME bus, software in the CPU loads or stores the
contents of CPU registers to a device on the VME bus. The operation of a CPU load from a
VME device register is as follows:
1. The CPU executes a load from a system physical address.
2. The system recognizes the physical address as one of its own.
3. The system translates the physical address into a VME bus address.
4. Acting as a VME bus master, the system starts a read cycle on the VME bus.
5. A slave device on the VME bus responds to the VME address and returns data.
6. The VME controller initiates a system bus cycle to return the data packet to the CPU,
thus completing the load operation.
********** 17 **********
--- page 18 ---
A store to a VME device is similar except that it performs a VME bus write, and no data is
returned.
PIO input requires two system bus cycles—one to request the data and one to return it—
separated by the cycle time of the VME bus. PIO output takes only one system bus cycle, and
the VME bus write cycle run concurrently with the next system bus cycle. As a result, PIO
input always takes at least twice as much time as PIO output.
CO- b Explanation of Any Two File Formats:   3.5 Marks X 2 = 07 Marks   (07)
2;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally it becomes the most commonly used format, especially in instrumentation
applications. Needless to say, one has to convert all data to ASCII strings before
saving data. The major disadvantage of this format is that the text files tend to be
larger than the other formats. At one time this was a major handicap, but with the
ever-increasing capacity of storage media, this is no longer a major handicap.
Another disadvantage was speed, since the conversion of binary data (internal
format) to ASCII, and the transfer of the larger volume of data to the disk were
both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
text files and reading and writing operations can be done with little data conversion.
Binary file format is useful in applications requiring writing and reading of large
chunks of data due to its size advantage. However, with the increasing availability
of large storage devices at reasonable cost, this advantage is being progressively
lost. Also, binary format is often system (or processor) dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single arbitrary
data type specified during creation of the file. The data is indexed in terms of these
records. Each record in a measurement file must have the same data types
associated with it. One interesting feature of these files is that timestamps are also
included with each record. Also, LabVIEW allows random read access to the
binary versions of these files.
********** 18 **********
--- page 19 ---
CO- c Explanation of Any Three Front Panel Toolbar Buttons with symbol. 02 Marks X 3 = 06 Marks (06)
1;
SO-
1 ;
BL-
2
Q.6
CO-   Open a blank VI and Build a VI that generates 50 random numbers and plot it on a waveform   (20
2   chart using While Loop. Accumulate the random numbers into an array and display it on
)
waveform graph.
&5;   a. Save the VI as while_tee.vi on desktop
SO-   b. Print the VI by selecting option Icon, description, panel and diagram in Print
contents.
1;
BL-
6   Ans :
********** 19 **********
--- page 20 ---
Q.7   (20
)
CO-   Open a blank VI and Build a VI to find the roots of a quadratic equation with complex roots. (20
2   Input the coefficients of x2, x and constant as A, B and C respectively. The LED should glow
)
when roots are real and different or roots are real and equal or when the roots are complex.
&5;   Display the message ‘A’ should not be zero for quadratic expression” if the coefficient of x2 is
SO-   zero.
1;
a. Build the front panel as shown in Figure a
BL-   b. Build the block diagram to find the roots of a quadratic equation
6   c. Save the VI as quad_tee.vi on desktop
d. Print the VI by selecting option Icon, description, panel and diagram in Print contents
********** 20 **********
--- page 21 ---
Figure a

Ans.:

FI ICR D7 FAC HOH
--- page 22 ---
‘4’ should not be 2ero For quadratic expression 1s
[om

Figure b Block Diagram

Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]

FIR ICR DAC HH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 1c3c3c25ad93

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Supervisory Control and Data Acquisition/ANS_Supervisory Control and Data Acquisition(702MH0I001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: mixed (22 pages), mean OCR confidence 66.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (MECH)/MBA Tech
(Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Supervisory Control and Data Acquisition
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q.1   Attempt the following.   (20)
CO- a Explanation of Sub VI   (03)
1;   Example   (02)
SO-
1 ;   SubVIs are VIs that you build to use inside of another VI or that you access on the Functions
BL-   palette. Any VI has the potential to be used as a subVI. When you double-click a subVI on the
2   block diagram, its front panel and block diagram appear. The front panel includes controls and
indicators. The block diagram includes wires, front panel icons, functions, possibly subVIs and
other LabVIEW objects. The upper-right corner of the front panel and block diagram displays
the icon for the VI. This is the icon that appears when you place the VI on a block diagram as a
subVI. SubVIs also can be Express VIs. Express VIs are nodes that require minimal wiring
because you configure them with dialog boxes. Use Express VIs for common measurement tasks.
You can save the configuration of an Express VI as a subVI.
CO- b Explanation of Stacked Sequence Structure   (05)
2;
SO-   a. Sequence Structure:
1 ;   A sequence structure contains one or more subdiagrams, or frames, that execute in
BL-   equential order. Within each frame of a sequence structure, as in the rest of the block diagram,
2
data dependency determines the execution order of nodes. Sequence structures are not used
commonly in LabVIEW. Use the sequence structures to control the execution order when natural
data dependency does not exist and flow-through parameters are not available. There are two
types of sequence structures— the Flat Sequence structure and the Stacked Sequence structure.
• Stacked Sequece Structure
The Stacked Sequence structure, shown as follows, stacks each frame so you see
only one frame at a time and executes frame 0, then frame 1, and so on until the
********** 1 **********
--- page 2 ---
last frame executes. The Stacked Sequence structure returns data only after the
last frame executes. Use the Stacked Sequence structure if you want to conserve
space on the block diagram. To convert a Stacked Sequence structure to a Flat
Sequence structure, right-click the Stacked Sequence structure and select
Replace»Replace with Flat Sequence from the shortcut menu. The sequence
selector identifier, shown as follows, at the top of the Stacked Sequence structure
contains the current frame number and range of frames.
CO- c Explanation of Local variable   (05)
2;
SO-   LOCAL VARIABLES
1 ;
BL-   Local variables transfer data within a single VI and allow data to be passed between parallel loops as
2   shown in Figure 4.22. They also break the dataflow programming paradigm. Two ways to create a local
variable are right-click on an object’s terminal and select Create»Local Variable. A local variable icon
for the object appears on the block diagram as shown in Figure 4.23.
CO- d Explanation of the classification of signals in the data acquisition system.   (05)
3;
SO-   1) Signals: The appropriate transducer converts the physical phenomena into measurable
1 ;   signals. However, different signals need to be measured in different ways. For this reason,
BL-   it is important to understand the different types of signals and their corresponding
2
attributes. Signals can be categorized into two groups: analog and digital.
a) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load. The
three primary characteristics of an analog signal include level, shape and frequency as
shown in Figure 4.2.
********** 2 **********
--- page 3 ---
Figure 4.2 Primary characteristics of an analog signal.
Level gives vital information about the measured analog signal since analog signals can
take on any value. The intensity of a light source, the temperature in a room, and the pressure
inside a chamber are all examples that demonstrate the importance of the level of a signal. When
measuring the level of a signal, the signal generally does not change quickly with respect to time.
The accuracy of the measurement, however, is very important. A DAQ system that yields
maximum accuracy should be chosen to aid in analog level measurements.
b) Digital Signals : A digital signal cannot take on any value with respect to time. Instead,
a digital signal has two possible levels: high and low. Digital signals generally conform
to certain specifications that define the characteristics of the signal. Digital signals are
commonly referred to as Transistor-to-Transistor Logic (TTL). TTL specifications
indicate a digital signal to be low when the level falls within 0 to 0.8 volts, and the signal
is high between 2 to 5 volts. The useful information that can be measured from a digital
signal includes the state and the rate as shown in Figure 4.3.
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or low.
Monitoring the state of a switch—open or closed—is a common application showing the
importance of knowing the state of a digital signal.
Q.2
********** 3 **********
--- page 4 ---
CO- a Explanation of PC based DAQ system   (05)
3;   Block diagram.   (02)
SO-
1 ;
BL-   ➢ Data Acquisition (DAQ) System
2
The fundamental task of a DAQ (Data Acquisition) system is to measure or generate real-world
physical signals. Data acquisition involves gathering signals from measurement sources and
digitizing the signal for storage, analysis and presentation on a personal computer (PC). Data
acquisition systems come in many different PC technology forms for great flexibility. The five
components to be considered when building a basic DAQ system as shown in Figure 4.1 are
transducers, signals, signal conditioning, DAQ hardware, and driver and application software.
Figure 4.1 Data acquisition system.
2) A transducer: It is a device that converts a physical phenomenon into a measurable
electrical signal, such as voltage or current. The ability of a DAQ system to measure
different phenomena depends on the transducers to convert the physical phenomena into
signals measurable by the DAQ hardware. Transducers are synonymous with sensors in
DAQ systems. There are specific transducers for many different applications, such as
measuring temperature, pressure or fluid flow. Table 4.1 shows a short list of some
common transducers and the phenomena they can measure.
TABLE 4.1 Phenomena and existing transducers
3) Signals: The appropriate transducer converts the physical phenomena into measurable
signals. However, different signals need to be measured in different ways. For this reason,
********** 4 **********
--- page 5 ---
it is important to understand the different types of signals and their corresponding
attributes. Signals can be categorized into two groups: analog and digital.
c) Analog Signals: An analog signal can be at any value with respect to time. A few
examples of analog signals include voltage, temperature, pressure, sound and load. The
three primary characteristics of an analog signal include level, shape and frequency as
shown in Figure 4.2.
Figure 4.2 Primary characteristics of an analog signal.
Level gives vital information about the measured analog signal since analog signals can
take on any value. The intensity of a light source, the temperature in a room, and the pressure
inside a chamber are all examples that demonstrate the importance of the level of a signal. When
measuring the level of a signal, the signal generally does not change quickly with respect to time.
The accuracy of the measurement, however, is very important. A DAQ system that yields
maximum accuracy should be chosen to aid in analog level measurements.
d) Digital Signals : A digital signal cannot take on any value with respect to time. Instead,
a digital signal has two possible levels: high and low. Digital signals generally conform
to certain specifications that define the characteristics of the signal. Digital signals are
commonly referred to as Transistor-to-Transistor Logic (TTL). TTL specifications
indicate a digital signal to be low when the level falls within 0 to 0.8 volts, and the signal
is high between 2 to 5 volts. The useful information that can be measured from a digital
signal includes the state and the rate as shown in Figure 4.3.
********** 5 **********
--- page 6 ---
Figure 4.3 Primary characteristics of a digital signal.
The state of a digital signal is essentially the level of the signal—on or off, high or low.
Monitoring the state of a switch—open or closed—is a common application showing the
importance of knowing the state of a digital signal.
4) Signal conditioning: Signal conditioning is the process of measuring and manipulating
signals to improve accuracy, isolation, filtering, and so on. Many stand-alone instruments
and DAQ devices have built-in signal conditioning. Signal conditioning also can be
applied externally, by designing a circuit to condition the signal or by using devices
specifically made for signal conditioning. National Instruments has SCXI devices and
other devices that are designed for this purpose. Signal conditioning accessories can be
used in a variety of important applications. Signal conditioning accessories amplify low-
level signals and then isolate and filter them for more accurate measurements. In addition,
some transducers use voltage or current excitation to generate a voltage output. Common
types of signal conditioning are amplification, isolation, multiplexing, filtering,
transducer excitation and linearization.
a) Amplification:
Amplification is the most common type of signal conditioning. Amplifying electrical
signals improves accuracy in the resulting digitized signal and reduces the effects of
noise. Signals should be amplified as close to the signal source as possible.
b) Isolation
Another common signal conditioning application is isolating the transducer signals from
the computer for safety purposes. The system being monitored may contain high-voltage
transients that could damage the computer without signal conditioning.
c) Multiplexing
A common technique for measuring several signals with a single measuring device is
multiplexing. Signal conditioning hardware for analog signals often provides
multiplexing for use with slowly changing signals like temperature.
d) Filtering
The purpose of a filter is to remove unwanted signals from the signal that you are trying
to measure.
e) Transduces Excitation
********** 6 **********
--- page 7 ---
Signal conditioning systems can generate excitation, which some transducers require
for operation. Strain gauges and RTDs require external voltage and currents,
respectively, to excite their circuitry into measuring physical phenomena.
f) Linearization
Another common signal conditioning function is linearization. Many transducers,
such as thermocouples, have a nonlinear response to changes in the physical
phenomena you measure. LabVIEW can linearize the voltage levels from transducers
so you can scale the voltages to the measured phenomena. LabVIEW provides scaling
functions to convert voltages from strain gages, RTDs, thermocouples, and
thermistors.
5) DAQ Hardware Configuration: Before using a data acquisition board, you must
confirm that the software can communicate with the board by configuring the devices.
The Windows Configuration Manager keeps track of all the hardware installed in the
computer, including National Instruments DAQ devices. If you have a Plug & Play (PnP)
device, such as an E Series MIO device, the Windows Configuration Manager
automatically detects and configures the device. If you have a non-PnP device, or legacy
device, you must configure the device manually using the Add New Hardware option in
the Control Panel. You can verify the Windows Configuration by accessing the Device
Manager.
CO- b Explanation of array and cluster.   (05)
2;   Arrays   Clusters   (02)
SO-   Array is a homogenous collection (i.e., all of the   A cluster is also a data structure that groups data.
1 ;   same type) of data elements.
BL-   An array can have one or more dimensions and up   a cluster can group data of different types.
2   to 231 elements per dimension (subject to the
memory capacity).
An array data element can be of any type except   In LabVIEW A cluster may be thought of as a
another array, a chart or a graph. An array with n   bundle of wires and is shown as a ‘rope’ in the
elements is indexed from 0 to (n-1) , with the first   block diagram.
element at index 0 and last one at index (n-1).
Clusters reduce wire clutter and the number of
connector terminals in a sub VI. On the block
diagram one can connect cluster terminals with
another cluster wire only if they have the same
type, the same number of elements and the same
order of elements. The cluster elements can be
accessed by unbundling them all at once or by
indexing one at a time.
Clusters are commonly used to pass a record
across VI’s. Clusters are also used for passing
error information between multiple VIs in a block
diagram.
any array can be converted into a cluster (in   A cluster can only be converted to an array when
a priori)   all the elements are of the same kind.
Made up of either controls or indicators.   Made up of either controls or indicators.
CO- c Explanation of RS-232 and RS-485 standards of serial port communication.
4;
SO-   ● RS-232 (ANSI/EIA-232 Standard) is used for many purposes such as connecting a mouse, (03)
1 ;   printer, or modem. It is also used with industrial instrumentation. Because of improvements in
BL-   line drivers and cables, applications often increase the performance of RS-232 beyond the
2
distance and speed in the standards list. RS-232 is limited to point-to-point connections between
PC serial ports and devices. RS-232 is the connector found on most PCs. This is a single-ended
********** 7 **********
--- page 8 ---
communication method where only one device can be connected per port. Two connector types
are 9 or 25-pin. Two configurations are DCE or DTE.
● RS-485 (EIA-485 Standard) is a variation of RS-422 that allows you to connect up to 32 (03)
devices to a single port and define the necessary electrical characteristics to ensure adequate
signal voltages under maximum load. With this enhanced multidrop capability, you can create
networks of devices connected to a single RS-485 serial port. The noise immunity and multidrop
capability make RS-485 an attractive choice in industrial applications that require many
distributed devices networked to a PC or other controller for data collection and other operations.
Q.3
CO- a Explanation of State Machine   (05)
2;   In its simplest form, a state machine comprises of a while loop, with a shift register
SO- 1 ;   and a case structure (Fig.1). The code starts by initialising the shift register to the
BL-   initial state of the system (from outside the while loop) which is entered into by the
2   case structure. At the end of the execution of the code corresponding to this state,
the case structure then sends the next state to the shift register. Then in the
following iteration of the while loop, this state is executed. This continues until the
While loop is terminated by the case structure. Note that the code is no longer
constrained to operate in a linear fashion, but can progress from state to state in a
non-linear manner. What is required is that the various states of the system must
be clearly defined. The next state can also be decided by the previous state,
depending on the logic in it. In the above example, a user acquiring data can easily
select options to acquire more data, change the configuration, save the data, analyse
the data, or stop the program and output the code of the appropriate case to the shift
register. Coding all these possibilities normally would be very difficult, if not
impossible. The labyrinth of the various possible transitions will render the code a
nightmare to develop, understand and debug. Developing and debugging such a
code is a Herculean task. Add similar sets of possibilities to other options and the
complexity of the task can be well imagined.
********** 8 **********
--- page 9 ---
(02)
Fig.1 Components of a State Machine
However, using the state machine, such a code can be easily developed and
debugged. The code for each state becomes an independent VI. These can be
developed and tested individually and subsequently combined in a state machine.
There is nothing to stop any particular state from spawning a state machine of
its own. The possibilities are mind-boggling.
Example
CO- b Explanation Formula Node with example   (04)
2;   FORMULA NODE
SO-
1 ;   Sometimes there is a requirement to program a piece of code in a conventional or quasi-
BL-   conventional way. This is possible in LabVIEW through the use of the Formula Node. The Formula
2
Node is a resizable box that you use to enter algebraic formulas directly into the block diagram. This
feature extremely useful when you have a long formula to solve.
Users envisaging the use of Formula Nodes are faced with the issue of reconciling the graphical
symbolism of LabVIEW with the alphanumeric representation in text based languages.
With the Formula Node, you can directly enter a formula or formulas, in lieu of creating complex block
diagram subsections. Simply enter the formula inside the box. You create the input and output terminals
of the Formula Node by popping up on the border of the node and choosing Add Input or Add Output
from the pop-up menu. Then enter variable names into the input and output terminals. Names are case
sensitive, and each formula statement must terminate with a semicolon (;).
You will find the Formula Node in the Programming>>Structures subpalette of the Functions
palette.
These operators and functions are available inside the Formula Node.
********** 9 **********
--- page 10 ---
As expected in a DataFlow environment, separate nodes have to be associated with the input and output
lists, i.e. if the user changes the value of an input variable inside the formula node the output has to be
done through a separate node.
Fig. 4.3 Formula node
Furthermore, a formula node does not support multithreading, i.e., as long as the formula node is
executing, operation of other blocks of code is not permitted. This is seldom a constraint since very
rarely does the code in the formula node takes any appreciable time to execute. Any complex coding is
best left for linking through DLLs or CINs. A single line formula node is also available for
convenience.
(02)
Example
CO- c Differentiate between text-based programming and graphical programming.   (07)
1;
SO-   Text-based programming   Graphical programming
1 ;
BL-   ● Syntax must be known to do programming. ●Syntax is knowledge but is not required for
4   ●The execution of the program is from top to Programming.
bottom.   ●The execution of program is from left to
●To check for the error the program has to be right.
compiled or executed.   ●Errors are indicated as we wire the blocks.
●Front panel design needs extra coding or ●Front   panel   design   is   a   part   of
needs extra work.   programming.
●Text-based programming is non interactive. ●Graphical   programming   is   highly
●This is text-based programming where the   interactive.
Programming is a conventional method.   ●The   programming   is   Data   Flow
●Logical Error finding is easy in large Programming.
programs.   ● Logical Error finding in large programs is
●Program flow is not visible.   quiet complicated.
●It is test-based programming.   ● Data flow is visible.
●Passing parameters to sub routine   is ● It is icon-based programming and wiring.
difficult.   ● Passing parameters to sub VI is easy.
Q.4
********** 10 **********
--- page 11 ---
CO- a Explanation of the various types of graphs and charts in LabVIEW.   (03)
2;   Explanation of basic difference between Graphs from chart.   (04)
SO-
1 ;   GRAPHS AND CHARTS
BL-
2   Displaying data is equally important and sometimes even more important than acquiring it. Therefore,
good display tools are a necessity. More often than not data needs to be presented graphically. Also,
when data is being analyzed graphical output of the analysis is often required. The graphical display of
data is a very important aspect of programming in LabVIEW. In most situations, two-dimensional X-Y
displays are required. LabVIEW provides three tools for this, namely, the waveform chart, the
waveform graph, and the X-Y graph. While the first two deals with data which is equally spaced along
the X-axis, the last is especially for situations where the X-intervals are not equal. All these objects can
be accessed from the panel through either the Express VI function on the Graph Indicators palette, or
through the All Controls palette and the Graph Menu. VI’s with graph usually collects the data in an
array and then plots the data to the graph to obtain a waveform.
Charts and graphs let you display plots of data in a graphical form. Charts interactively plot data,
appending new data to old so that you can see the current value in the context of previous data, as the
new data become available. Graphs plot pre-generated arrays of values in a more traditional fashion
without retaining previously-generated data.
WAVEFORM GRAPHS
LabVIEW includes the waveform graph and chart to display data typically acquired at a constant rate.
The waveform graph displays one or more plots of evenly sampled measurements. The waveform graph
plots only single-valued functions, as in y = f (x), with points evenly distributed along the x-axis, such as
acquired time-varying waveforms. Figure 7.1 shows an example of a waveform graph. The waveform
graph can display plots containing any number of points. The graph also accepts several data types,
which minimizes the extent to which you must manipulate data before you display it.
Figure 7.1 Waveform Graph.
WAVEFORM CHARTS
The waveform chart is a special type of numeric indicator that displays one or more plots of data typically
acquired at a constant rate. Waveform charts can display single or multiple plots. Figure 7.3 shows the
elements of a multiplot waveform chart. Two plots are displayed: Raw Data and Running Avg.
********** 11 **********
--- page 12 ---
The waveform chart maintains a history of data or buffer from previous updates.
Figure 7.3 A waveform chart.
CO- b Explanation of Any three String Functions   02 Marks X 3 = 06 Marks   (06)
2;   1) String Length: This function (Fig. 13) gives the number of characters
SO-   (bytes) in the input string. Being a polymorphic function, the length output
1 ;
BL-   has the same structure as the input.
2
Fig. 10 String Length function
2) Concatenate Strings: The Concatenate Strings function (Fig. 14) is useful
in concatenating input strings into a single output string. In addition to
simple strings one-dimensional arrays of strings can also be wired as inputs;
the output will be a single string containing a concatenation of all the strings
in the order they are connected, top to bottom, left to right. This function can
be used to concatenate strings to be written as text in files. In addition to the
text or characters indicating the application, string constants such as tab, line
feed, end of line, etc. can also be appended to the characters as required by
the application. This function is used very often to assemble commands for
instruments. In these cases (especially in serial interfacing) the string often
has to be terminated with an appropriate character or characters.
********** 12 **********
--- page 13 ---
Fig. 11 Concatenate Strings function
Similarly, for preparing data for writing to a file < TAB > is used as a
separator between items, and a terminator (an < EOL > is preferred to < CR
> and/or < LF >) since this makes the code platform independent.
3) Match Pattern: This function (Fig. 15) searches for a string pattern
(regular expression) in the input string beginning at offset, and if it finds a
match, it splits the string into three substrings, viz., before-substring,
match-substring and after-substring. If the Function does not find the
regular expression string pattern, match-substring is empty, before-
substring will have the entire string, after-substring is empty, and offset
past match is –1. The offset past match output is useful as an offset input
for another match pattern search.
Fig. 12 Match Pattern function
4) String Subset: The String Subset function (Fig. 16) returns the substring
of the input string beginning at offset and containing number of characters as
specified by length input. This function is useful to remove unwanted header/
data in a string.
Fig. 13 String Subset function
5) Get Date/Time String: The Get Date/Time String function (Fig. 17) is
available on the Timing & Dialog palette. It converts a time stamp value or
a numeric value to a date and time string in the time zone configured for
the computer.
********** 13 **********
--- page 14 ---
Fig. 14 Get Date/Time String (timing dialog palette)
CO- c Explanation of VISA   (05)
4;   Block diagram.   (02)
SO-
1 ;   Virtual Instrument Software Architecture (VISA) is the lower layer of functions in the LabVIEW
BL-   instrument driver VIs that communicates with the driver software. VISA by itself does not
2
provide instrumentation programming capability. VISA is a high-level API that calls low-level
drivers. As shown in Figure VISA can control VXI, GPIB, serial, or computer-based instruments
and makes the appropriate driver calls depending on the type of instrument used. When
debugging VISA problems, remember that an apparent VISA problem could be an installation
problem with one of the drivers that VISA calls.
Figure Virtual Instrument Software Architecture.
In LabVIEW, VISA is a single library of functions you use to communicate with GPIB, serial,
VXI and computer-based instruments. You do not need to use separate I/O palettes to program
an instrument. For example, some instruments give you a choice for the type of interface. If the
LabVIEW   instrument   driver was   written with   functions on   the   Functions»All
Functions»Instrument I/O»GPIB palette, those instrument driver VIs would not work for the
instrument with the serial port interface. VISA solves this problem by providing a single set of
functions that work for any type of interface. Therefore, many LabVIEW instrument drivers use
VISA as the I/O language. For many years, industry has moved toward purchasing
instrumentation from a variety of vendors. This allows engineers to select the best possible
equipment for their applications without being locked into a specific vendor. This trend required
the definition of hardware standards to ensure the compatibility between different modules. This
was one of the factors leading to the development of the VXI specification. But even with these
improved hardware standards, a system was time consuming and expensive to put together.
Successful integration of a multivendor system
requires all hardware and software products work together, eliminating system-level
compatibility issues for end-users. National Instruments initially addressed the software
problems with instrument drivers, which helped reduce both integration time and software
development costs. In 1993, National Instruments joined with GenRad, Racal Instruments,
Tektronix and Wavetek to form the VXI plug & play Systems Alliance. The goals of the alliance
are to ensure multivendor interoperability for VXI systems and to reduce the development time
for an operational system.
Q5
CO- a Explanation of Versa Modular Eurocard bus.   (07)
4;
SO-   VME bus is a bus system (or a computer path system) for industrial applications such as
1 ;
BL-   VME power supplies, embedded single board computers (SBC), actuators automation, etc. It
2
was originally developed by Motorola technical employees in Germany (yr. 1980) and soon
after, also adopted by Signetics, Philips, Thomson, and Mostek.
********** 14 **********
--- page 15 ---
It was designed as a flexible interconnection between multiple master and slave devices using a
variety of address and data precisions, and has become a popular standard bus used in a variety
of products.
VME Features
A VME bus is a set of parallel conductors that interconnect multiple processing devices.
The devices can exchange data in units of 8, 16, 32 or 64 bits during a bus cycle.
VME Address Spaces
Each VME device identifies itself with a range of bus addresses. A bus address has either 16,
24, or 32 bits of precision. Each address width forms a separate address space. That is, the
same numeric value can refer to one device in the 24-bit address space but a different device in
the 32-bit address space. Typically, a device operates in only one address space, but some
devices can be configured to respond to addresses in multiple spaces.
Each VME bus cycle contains the bits of an address. The address is qualified by sets of
address-modifier bits that specify the following:
•   the address space (A16, A24, or A32).
• whether the operation is single or a block transfer.
• whether the access is to what, in the MC68000 architecture, would be data or code, in a
supervisor or user area (Silicon Graphics systems support only supervisor-data and
user-data requests).
Master and Slave Devices
Each VME device acts as either a bus master or a bus slave. Typically a bus master is a device
with some level of programmability, usually a microprocessor. A disk controller is an example
of a master device. A slave device is typically a nonprogrammable device like a memory board.
Each data transfer is initiated by a master device. The master
•   asserts ownership of the bus.
•   specifies the address modifier bits for the transfer, including the address space,
single/block mode, and supervisor/normal mode.
•   specifies the address for the transfer.
•   specifies the data unit size for the transfer (8, 16, 32 or 64 bits).
•   specifies the direction of the transfer with respect to the master.
The VME bus design permits multiple master devices to use the bus, and provides a hardware-
based arbitration system so that they can use the bus in alternation.
********** 15 **********
--- page 16 ---
A slave device responds to a master when the master specifies the slave's address. The
addressed slave accepts data, or provides data, as directed.
VME Transactions
The VME design allows for four types of data transfer bus cycles:
• A read cycle returns data from the slave to the master.
• A write cycle sends data from the master to the slave.
• A read-modify-write cycle takes data from the slave, and on the following bus cycle
sends it back to the same address, possibly altered.
• A block-transfer transaction sends multiple data units to adjacent addresses in a burst of
consecutive bus cycles.
The VME design also allows for interrupts. A device can raise an interrupt on any of
seven interrupt levels. The interrupt is acknowledged by a bus master. The bus master
interrogates the interrupting device in an interrupt-acknowledge bus cycle, and the device
returns an interrupt vector number.
VME Bus in Silicon Graphics Systems
The VME bus was designed as the system backplane for a workstation, supporting one or more
CPU modules along with the memory and I/O modules they used. However, no Silicon
Graphics computer uses the VME bus as the system backplane. In all Silicon Graphics
computers, the main system bus that connects CPUs to memory is a proprietary bus design,
with higher speed and sometimes wider data units than the VME bus provides. The VME bus is
attached to the system as an I/O device.
The VME Bus Controller
A VME bus controller is attached to the system bus to act as a bridge between the system bus
and the VME bus. This arrangement is shown in Figure 13-1.
********** 16 **********
--- page 17 ---
Figure 13-1. Relationship of VME Bus to System Bus
On the Silicon Graphics system bus, the VME bus controller acts as an I/O device. On the
VME bus, the bus controller acts as a VME bus master.
The VME controller has several tasks. Its most important task is mapping; that is, translating
some range of physical addresses in the Silicon Graphics system address space to a range
of VME bus addresses. The VME controller performs a variety of other duties for different
kinds of VME access.
VME PIO Operations
During programmed I/O (PIO) to the VME bus, software in the CPU loads or stores the
contents of CPU registers to a device on the VME bus. The operation of a CPU load from a
VME device register is as follows:
1. The CPU executes a load from a system physical address.
2. The system recognizes the physical address as one of its own.
3. The system translates the physical address into a VME bus address.
4. Acting as a VME bus master, the system starts a read cycle on the VME bus.
5. A slave device on the VME bus responds to the VME address and returns data.
6. The VME controller initiates a system bus cycle to return the data packet to the CPU,
thus completing the load operation.
********** 17 **********
--- page 18 ---
A store to a VME device is similar except that it performs a VME bus write, and no data is
returned.
PIO input requires two system bus cycles—one to request the data and one to return it—
separated by the cycle time of the VME bus. PIO output takes only one system bus cycle, and
the VME bus write cycle run concurrently with the next system bus cycle. As a result, PIO
input always takes at least twice as much time as PIO output.
CO- b Explanation of Any Two File Formats:   3.5 Marks X 2 = 07 Marks   (07)
2;
SO-   • ASCII Text-Format Files :
1 ;
BL-   ASCII text-format files store data in the ASCII format. This is the simplest format
2   and since most software packages can retrieve data from an ASCII text file,
naturally it becomes the most commonly used format, especially in instrumentation
applications. Needless to say, one has to convert all data to ASCII strings before
saving data. The major disadvantage of this format is that the text files tend to be
larger than the other formats. At one time this was a major handicap, but with the
ever-increasing capacity of storage media, this is no longer a major handicap.
Another disadvantage was speed, since the conversion of binary data (internal
format) to ASCII, and the transfer of the larger volume of data to the disk were
both slow. This is no longer so with modern systems.
• Binary-Format Files :
These files store data in binary form and look like an image of the data stored
in the computer’s memory. These files cannot be read by word processors. Also,
it is impossible to retrieve data from these files without detailed knowledge of the
file’s format. The main advantage of these files is that they are much smaller than
text files and reading and writing operations can be done with little data conversion.
Binary file format is useful in applications requiring writing and reading of large
chunks of data due to its size advantage. However, with the increasing availability
of large storage devices at reasonable cost, this advantage is being progressively
lost. Also, binary format is often system (or processor) dependent.
• LabVIEW Measurement Files:
LabVIEW measurement files are special files which are either text-based files
(.lvm) or binary files (.tdm or .tdms). Generally, these files are written and read
using Express VIs. Here data is stored as a sequence of records of a single arbitrary
data type specified during creation of the file. The data is indexed in terms of these
records. Each record in a measurement file must have the same data types
associated with it. One interesting feature of these files is that timestamps are also
included with each record. Also, LabVIEW allows random read access to the
binary versions of these files.
********** 18 **********
--- page 19 ---
CO- c Explanation of Any Three Front Panel Toolbar Buttons with symbol. 02 Marks X 3 = 06 Marks (06)
1;
SO-
1 ;
BL-
2
Q.6
CO-   Open a blank VI and Build a VI that generates 50 random numbers and plot it on a waveform   (20
2   chart using While Loop. Accumulate the random numbers into an array and display it on
)
waveform graph.
&5;   a. Save the VI as while_tee.vi on desktop
SO-   b. Print the VI by selecting option Icon, description, panel and diagram in Print
contents.
1;
BL-
6   Ans :
********** 19 **********
--- page 20 ---
Q.7   (20
)
CO-   Open a blank VI and Build a VI to find the roots of a quadratic equation with complex roots. (20
2   Input the coefficients of x2, x and constant as A, B and C respectively. The LED should glow
)
when roots are real and different or roots are real and equal or when the roots are complex.
&5;   Display the message ‘A’ should not be zero for quadratic expression” if the coefficient of x2 is
SO-   zero.
1;
a. Build the front panel as shown in Figure a
BL-   b. Build the block diagram to find the roots of a quadratic equation
6   c. Save the VI as quad_tee.vi on desktop
d. Print the VI by selecting option Icon, description, panel and diagram in Print contents
********** 20 **********
--- page 21 ---
Figure a

Ans.:

FI ICR D7 FAC HOH
--- page 22 ---
‘4’ should not be 2ero For quadratic expression 1s
[om

Figure b Block Diagram

Front Panel [ 10 Marks]
Block Diagram [ 10 Marks ]

FIR ICR DAC HH
````
