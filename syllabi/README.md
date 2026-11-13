# Syllabi and teaching schemes

All **4,003** documents in the archive's syllabus sections (1,860 syllabi, 1,255 teaching schemes, and 888 exam papers and answer keys the portal filed there; 38,605 pages) read into text, from `04_Syllabi_Archive/`, `01_Current_Electives_2026-27/` and syllabi kept only inside the portal's ZIP downloads. Syllabus documents were split into **12,814 course sections**; 10,212 belong to a subject that has past papers and are also in that subject's folder as `syllabus.md`, next to its question papers.

- `<Programme>/courses.jsonl`: one record per course section (course, code, subject, programme, branch, batch, semester, source, text).
- [`documents.jsonl`](documents.jsonl): one record per document, with every path it is stored under.
- Text quality: 3,993 documents read cleanly, 9 are poor scans (mean OCR confidence below 60), 1 gave no text.
- Teaching schemes are mostly scanned tables; their OCR text is kept in full in the branch files (`<Programme>/<Branch>.md`) but is not split into courses.
- Exam papers and answer keys found among the syllabi (file names such as `..._Final_Exam_...`, or the same file filed as a paper elsewhere) are not split into courses: each is in the question bank under its subject (`subjects/`), and its branch-file entry links there.

## Programmes

| Programme | Documents | Branches |
| --- | ---: | --- |
| [B TECH](B%20TECH/README.md) | 1812 | All branches, Artificial Intelligence, Civil, Computer Engineering, Computer Science, Computer Science and Business Systems, Cyber Security, Data Science, Electrical, Electronics, Electronics and Telecommunication, IBM, Information Technology, Mechanical, Mechatronics, Open Electives |
| [B TECH INTEGRATED](B%20TECH%20INTEGRATED/README.md) | 562 | Civil, Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology, Mechanical |
| [B TECH WORK IN PROCESS](B%20TECH%20WORK%20IN%20PROCESS/README.md) | 569 | All branches, Artificial Intelligence, Civil, Computer Engineering, Computer Science, Computer Science and Business Systems, Cyber Security, Data Science, Electronics and Telecommunication, Information Technology, Mechanical, Mechatronics |
| [Current electives 2026-27](Current%20electives%202026-27/README.md) | 6 | Big Data, Blockchain, Cloud, HCI, IoT, Recommendation Systems |
| [DIPLOMA](DIPLOMA/README.md) | 26 | Computer Engineering, CSE, Information Technology, Mechanical |
| [M Tech](M%20Tech/README.md) | 118 | Artificial Intelligence, Data Science |
| [MBA Tech](MBA%20Tech/README.md) | 779 | All branches, Artificial Intelligence, Chemical, Civil, Computer Engineering, Data Science, Electrical, Electronics and Telecommunication, IBM, Information Technology, Management, Mechanical, Open Electives |
| [MCA](MCA/README.md) | 96 | All branches |
| [PGDM](PGDM/README.md) | 14 | All branches |
| [Ph D](Ph%20D/README.md) | 21 | All branches |

## Courses

Every course found in the syllabi. Courses with past papers link to the subject folder's `syllabus.md`.

| Course | Past papers | Versions | Programmes | Batches / years |
| --- | --- | ---: | --- | --- |
| [(BSC) - Fundamentals of Fuels and Lubricants](courses/%28BSC%29%20-%20Fundamentals%20of%20Fuels%20and%20Lubricants.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [(BSC) - Modelling and Simulation](courses/%28BSC%29%20-%20Modelling%20and%20Simulation.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [(BSC) - Optimization for Decision Making](courses/%28BSC%29%20-%20Optimization%20for%20Decision%20Making.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [(BSC) - Polymers in Engineering](courses/%28BSC%29%20-%20Polymers%20in%20Engineering.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [(BSC) - Science, Technology and Society](courses/%28BSC%29%20-%20Science%2C%20Technology%20and%20Society.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [1V (Environmental Impact Assessment and Audit)](courses/1V%20%28Environmental%20Impact%20Assessment%20and%20Audit%29.md) | — | 2 | B TECH WORK IN PROCESS | 2015-2019 |
| [3-D Printing Technology](courses/3-D%20Printing%20Technology.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [[] (Distributed Systems)](courses/%5B%5D%20%28Distributed%20Systems%29.md) | — | 2 | B TECH WORK IN PROCESS | 2013-2017 to 2018-2022 |
| [[Il Operations Research](courses/%5BIl%20Operations%20Research.md) | — | 1 | MBA Tech | 2018-2023 |
| [[V (Environmental Impact](courses/%5BV%20%28Environmental%20Impact.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2016-17 |
| [Access Web Page, Example](courses/Access%20Web%20Page%2C%20Example.md) | — | 2 | B TECH, MBA Tech | 2020-2025 to AY 2021-22 |
| [Accounting and Taxation](../subjects/Accounting%20and%20Taxation/syllabus.md) | [yes](../subjects/Accounting%20and%20Taxation/README.md) | 1 | PGDM | — |
| [Actuarial Science](../subjects/Actuarial%20Science/syllabus.md) | [yes](../subjects/Actuarial%20Science/README.md) | 1 | B TECH | AY 2024-25 |
| [Adaptive Signal Processing](courses/Adaptive%20Signal%20Processing.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Additive Manufacturing](../subjects/Additive%20Manufacturing/syllabus.md) | [yes](../subjects/Additive%20Manufacturing/README.md) | 46 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Adhoc and Sensor Networks](courses/Adhoc%20and%20Sensor%20Networks.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Administration in Teamcenter](courses/Administration%20in%20Teamcenter.md) | — | 1 | B TECH | AY 2025-26 |
| [Advance Data Structure for Analytics](../subjects/Advance%20Data%20Structure%20for%20Analytics/syllabus.md) | [yes](../subjects/Advance%20Data%20Structure%20for%20Analytics/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Advance Finance](courses/Advance%20Finance.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Advance Manufacturing Processes](../subjects/Advance%20Manufacturing%20Processes/syllabus.md) | [yes](../subjects/Advance%20Manufacturing%20Processes/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Advanced Algorithms](courses/Advanced%20Algorithms.md) | — | 3 | MBA Tech | 2015-2020 to 2017-2022 |
| [Advanced Applied Mathematics](courses/Advanced%20Applied%20Mathematics.md) | — | 1 | B TECH | AY 2018-19 |
| [Advanced Artificial Intelligence and Deep Learning](../subjects/Advanced%20Artificial%20Intelligence%20and%20Deep%20Learning/syllabus.md) | [yes](../subjects/Advanced%20Artificial%20Intelligence%20and%20Deep%20Learning/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Advanced Business Analytics in Python and R](../subjects/Advanced%20Business%20Analytics%20in%20Python%20and%20R/syllabus.md) | [yes](../subjects/Advanced%20Business%20Analytics%20in%20Python%20and%20R/README.md) | 2 | B TECH | AY 2024-25 to AY 2026-27 |
| [Advanced Business Computing and](courses/Advanced%20Business%20Computing%20and.md) | — | 2 | B TECH | AY 2022-23 to AY 2023-24 |
| [Advanced Chemistry](../subjects/Advanced%20Chemistry/syllabus.md) | [yes](../subjects/Advanced%20Chemistry/README.md) | 1 | MBA Tech | 2018-2023 |
| [Advanced Computer Architecture](courses/Advanced%20Computer%20Architecture.md) | — | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2017-2023 |
| [Advanced Computer Architecture (Department](courses/Advanced%20Computer%20Architecture%20%28Department.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Advanced Computer Networks](../subjects/Advanced%20Computer%20Networks/syllabus.md) | [yes](../subjects/Advanced%20Computer%20Networks/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Advanced Computer Networks (Department](courses/Advanced%20Computer%20Networks%20%28Department.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Advanced Computer Networks (Dept](courses/Advanced%20Computer%20Networks%20%28Dept.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Advanced Computer Networks I](courses/Advanced%20Computer%20Networks%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Advanced Computer Vision](../subjects/Advanced%20Computer%20Vision/syllabus.md) | [yes](../subjects/Advanced%20Computer%20Vision/README.md) | 12 | B TECH, B TECH INTEGRATED, M Tech, MBA Tech | 2018-2020 to AY 2025-26 |
| [Advanced Construction Techniques](../subjects/Advanced%20Construction%20Techniques/syllabus.md) | [yes](../subjects/Advanced%20Construction%20Techniques/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Advanced Data Analysis and Programming](../subjects/Advanced%20Data%20Analysis%20and%20Programming/syllabus.md) | [yes](../subjects/Advanced%20Data%20Analysis%20and%20Programming/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Advanced Data Mining for AI](courses/Advanced%20Data%20Mining%20for%20AI.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Advanced Data Structures](../subjects/Advanced%20Data%20Structures/syllabus.md) | [yes](../subjects/Advanced%20Data%20Structures/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Advanced Database Management](courses/Advanced%20Database%20Management.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Advanced Database Management System (Department](courses/Advanced%20Database%20Management%20System%20%28Department.md) | — | 4 | MCA | 2022-2024 to 2025-2027 |
| [Advanced Database Management Systems](../subjects/Advanced%20Database%20Management%20Systems/syllabus.md) | [yes](../subjects/Advanced%20Database%20Management%20Systems/README.md) | 41 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2025-26 |
| [Advanced DatabaseManagement I](courses/Advanced%20DatabaseManagement%20I.md) | — | 1 | B TECH | — |
| [Advanced Design](courses/Advanced%20Design.md) | — | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Advanced Design of Concrete Structures](../subjects/Advanced%20Design%20of%20Concrete%20Structures/syllabus.md) | [yes](../subjects/Advanced%20Design%20of%20Concrete%20Structures/README.md) | 4 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2018-2024 |
| [Advanced Financial Analytics](courses/Advanced%20Financial%20Analytics.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Advanced Geotechnical Engineering](../subjects/Advanced%20Geotechnical%20Engineering/syllabus.md) | [yes](../subjects/Advanced%20Geotechnical%20Engineering/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Advanced Image Processing](../subjects/Advanced%20Image%20Processing/syllabus.md) | [yes](../subjects/Advanced%20Image%20Processing/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2019-2024 |
| [Advanced Industrial Marketing](courses/Advanced%20Industrial%20Marketing.md) | — | 1 | MBA Tech | 2022-2027 |
| [Advanced Java](../subjects/Advanced%20Java/syllabus.md) | [yes](../subjects/Advanced%20Java/README.md) | 9 | MCA | 2013-2016 to 2025-2027 |
| [Advanced Machine Learning](courses/Advanced%20Machine%20Learning.md) | — | 7 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2025-26 |
| [Advanced Marketing Analytics](courses/Advanced%20Marketing%20Analytics.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Advanced Microcontroller and Embedded System](../subjects/Advanced%20Microcontroller%20and%20Embedded%20System/syllabus.md) | [yes](../subjects/Advanced%20Microcontroller%20and%20Embedded%20System/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Advanced Microcontrollers](../subjects/Advanced%20Microcontrollers/syllabus.md) | [yes](../subjects/Advanced%20Microcontrollers/README.md) | 5 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | AY 2014-15 to 2016-2020 |
| [Advanced Modeling for Business Analytics](../subjects/Advanced%20Modeling%20for%20Business%20Analytics/syllabus.md) | [yes](../subjects/Advanced%20Modeling%20for%20Business%20Analytics/README.md) | 4 | B TECH | AY 2022-23 to AY 2026-27 |
| [Advanced Neural Network](../subjects/Advanced%20Neural%20Network/syllabus.md) | [yes](../subjects/Advanced%20Neural%20Network/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Advanced Operations and Supply Chain Analytics](courses/Advanced%20Operations%20and%20Supply%20Chain%20Analytics.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Advanced Power Electronics](courses/Advanced%20Power%20Electronics.md) | — | 2 | B TECH | AY 2019-20 to AY 2020-21 |
| [Advanced Programming Laboratory](courses/Advanced%20Programming%20Laboratory.md) | — | 2 | MBA Tech | 2013-2018 to 2014-2019 |
| [Advanced Project Management](../subjects/Advanced%20Project%20Management/syllabus.md) | [yes](../subjects/Advanced%20Project%20Management/README.md) | 18 | MBA Tech | 2014-2019 to 2022-2027 |
| [Advanced Separation Techniques](courses/Advanced%20Separation%20Techniques.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Advanced Social, Text and Media](courses/Advanced%20Social%2C%20Text%20and%20Media.md) | — | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Advanced Statistical Learning](../subjects/Advanced%20Statistical%20Learning/syllabus.md) | [yes](../subjects/Advanced%20Statistical%20Learning/README.md) | 11 | M Tech | 2017-2019 to 2023-2025 |
| [Advanced Statistics](../subjects/Advanced%20Statistics/syllabus.md) | [yes](../subjects/Advanced%20Statistics/README.md) | 2 | M Tech | 2022-2024 to 2023-2025 |
| [Advanced Structural Analysis](../subjects/Advanced%20Structural%20Analysis/syllabus.md) | [yes](../subjects/Advanced%20Structural%20Analysis/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2015-16 to 2019-2024 |
| [Advanced Structural Mechanics](../subjects/Advanced%20Structural%20Mechanics/syllabus.md) | [yes](../subjects/Advanced%20Structural%20Mechanics/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2013-14 to 2019-2025 |
| [Advanced Supply Chain Analytics](../subjects/Advanced%20Supply%20Chain%20Analytics/syllabus.md) | [yes](../subjects/Advanced%20Supply%20Chain%20Analytics/README.md) | 4 | M Tech | 2017-2019 to 2020-2022 |
| [Advanced Surveying](../subjects/Advanced%20Surveying/syllabus.md) | [yes](../subjects/Advanced%20Surveying/README.md) | 1 | MBA Tech | 2011-2016 |
| [Advanced Topics in Machine Learning](../subjects/Advanced%20Topics%20in%20Machine%20Learning/syllabus.md) | [yes](../subjects/Advanced%20Topics%20in%20Machine%20Learning/README.md) | 5 | B TECH, MBA Tech | 2021-2026 to AY 2025-26 |
| [Advanced Turbomachinery](../subjects/Advanced%20Turbomachinery/syllabus.md) | [yes](../subjects/Advanced%20Turbomachinery/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Advanced Water and Wastewater Treatment](courses/Advanced%20Water%20and%20Wastewater%20Treatment.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Advanced Web](courses/Advanced%20Web.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Advanced Web Programming](../subjects/Advanced%20Web%20Programming/syllabus.md) | [yes](../subjects/Advanced%20Web%20Programming/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2024-25 |
| [Advanced Web Technologies](../subjects/Advanced%20Web%20Technologies/syllabus.md) | [yes](../subjects/Advanced%20Web%20Technologies/README.md) | 4 | MCA | 2022-2024 to 2025-2027 |
| [Advances in IC Engines](../subjects/Advances%20in%20IC%20Engines/syllabus.md) | [yes](../subjects/Advances%20in%20IC%20Engines/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Advertising and Public Relations](../subjects/Advertising%20and%20Public%20Relations/syllabus.md) | [yes](../subjects/Advertising%20and%20Public%20Relations/README.md) | 4 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Aerodynamics in Flight Design](../subjects/Aerodynamics%20in%20Flight%20Design/syllabus.md) | [yes](../subjects/Aerodynamics%20in%20Flight%20Design/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2025-26 |
| [Agile Product Development with DevOps](../subjects/Agile%20Product%20Development%20with%20DevOps/syllabus.md) | [yes](../subjects/Agile%20Product%20Development%20with%20DevOps/README.md) | 2 | B TECH | AY 2024-25 to AY 2025-26 |
| [AI and ML for Cybersecurity](../subjects/AI%20and%20ML%20for%20Cybersecurity/syllabus.md) | [yes](../subjects/AI%20and%20ML%20for%20Cybersecurity/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [AI and Robotics](../subjects/AI%20and%20Robotics/syllabus.md) | [yes](../subjects/AI%20and%20Robotics/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [AI in Chemometrics](courses/AI%20in%20Chemometrics.md) | — | 1 | B TECH | — |
| [Air Pollution and Controls](../subjects/Air%20Pollution%20and%20Controls/syllabus.md) | [yes](../subjects/Air%20Pollution%20and%20Controls/README.md) | 2 | MBA Tech | 2019-2024 to 2020-2025 |
| [Air Quality Management](../subjects/Air%20Quality%20Management/syllabus.md) | [yes](../subjects/Air%20Quality%20Management/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2024 |
| [Aircraft Design](courses/Aircraft%20Design.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Algorithm Trading](../subjects/Algorithm%20Trading/syllabus.md) | [yes](../subjects/Algorithm%20Trading/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2020-2024 to AY 2026-27 |
| [Alternative Fuels](../subjects/Alternative%20Fuels/syllabus.md) | [yes](../subjects/Alternative%20Fuels/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2026-27 |
| [An Introduction to Artificial Intelligence and AI](../subjects/An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI/syllabus.md) | [yes](../subjects/An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI/README.md) | 3 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2021-22 |
| [An Introduction to Artificial Intelligence and AI Framework](../subjects/An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI%20Framework/syllabus.md) | [yes](../subjects/An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI%20Framework/README.md) | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Analog and Digital Communication](../subjects/Analog%20and%20Digital%20Communication/syllabus.md) | [yes](../subjects/Analog%20and%20Digital%20Communication/README.md) | 15 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Analog and Digital Communications II](courses/Analog%20and%20Digital%20Communications%20II.md) | — | 1 | B TECH | AY 2013-14 |
| [Analog Circuits](courses/Analog%20Circuits.md) | — | 4 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2020-21 |
| [Analog Circuits Analysis and Design](../subjects/Analog%20Circuits%20Analysis%20and%20Design/syllabus.md) | [yes](../subjects/Analog%20Circuits%20Analysis%20and%20Design/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Analog Devices and Circuits](../subjects/Analog%20Devices%20and%20Circuits/syllabus.md) | [yes](../subjects/Analog%20Devices%20and%20Circuits/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Analog Integrated Circuits and Applications](../subjects/Analog%20Integrated%20Circuits%20and%20Applications/syllabus.md) | [yes](../subjects/Analog%20Integrated%20Circuits%20and%20Applications/README.md) | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2019-2025 |
| [Analysing Unstructured Data](../subjects/Analysing%20Unstructured%20Data/syllabus.md) | [yes](../subjects/Analysing%20Unstructured%20Data/README.md) | 5 | MBA Tech | 2020-2025 to 2022-2027 |
| [Analysis of Fluid Machines](courses/Analysis%20of%20Fluid%20Machines.md) | — | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Analysis of Structures](../subjects/Analysis%20of%20Structures/syllabus.md) | [yes](../subjects/Analysis%20of%20Structures/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to 2019-2025 |
| [Analysis of Transportation](courses/Analysis%20of%20Transportation.md) | — | 1 | B TECH WORK IN PROCESS | 2016-2020 |
| [Analysis of Transportation System](../subjects/Analysis%20of%20Transportation%20System/syllabus.md) | [yes](../subjects/Analysis%20of%20Transportation%20System/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to 2019-2024 |
| [Analytics for Strategic](courses/Analytics%20for%20Strategic.md) | — | 1 | MBA Tech | 2014-2019 |
| [Analytics for Strategic Marketing Decisions](../subjects/Analytics%20for%20Strategic%20Marketing%20Decisions/syllabus.md) | [yes](../subjects/Analytics%20for%20Strategic%20Marketing%20Decisions/README.md) | 14 | MBA Tech | 2015-2020 to 2022-2027 |
| [Analytics in Operations and Supply Chain Management](../subjects/Analytics%20in%20Operations%20and%20Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Analytics%20in%20Operations%20and%20Supply%20Chain%20Management/README.md) | 18 | MBA Tech | 2014-2019 to 2022-2027 |
| [Android Application Development](../subjects/Android%20Application%20Development/syllabus.md) | [yes](../subjects/Android%20Application%20Development/README.md) | 1 | B TECH | AY 2021-22 |
| [Antenna and Wave Propagation](../subjects/Antenna%20and%20Wave%20Propagation/syllabus.md) | [yes](../subjects/Antenna%20and%20Wave%20Propagation/README.md) | 3 | B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to 2013-2017 |
| [Application Architecture](courses/Application%20Architecture.md) | — | 5 | M Tech | 2024-2026 to 2026-2028 |
| [Application Architecture and Deployment](../subjects/Application%20Architecture%20and%20Deployment/syllabus.md) | [yes](../subjects/Application%20Architecture%20and%20Deployment/README.md) | 1 | M Tech | 2024-2026 |
| [Application of Artificial Intelligence I](courses/Application%20of%20Artificial%20Intelligence%20I.md) | — | 1 | M Tech | 2019-2021 |
| [Application of Artificial Intelligence II](courses/Application%20of%20Artificial%20Intelligence%20II.md) | — | 1 | M Tech | 2019-2021 |
| [Application of Power Electronics in Power Systems](../subjects/Application%20of%20Power%20Electronics%20in%20Power%20Systems/syllabus.md) | [yes](../subjects/Application%20of%20Power%20Electronics%20in%20Power%20Systems/README.md) | 1 | B TECH | AY 2018-19 |
| [Application of Predictive Modeling](courses/Application%20of%20Predictive%20Modeling.md) | — | 1 | MBA Tech | 2013-2018 |
| [Application Security Testing](../subjects/Application%20Security%20Testing/syllabus.md) | [yes](../subjects/Application%20Security%20Testing/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Applications of Machine Learning](../subjects/Applications%20of%20Machine%20Learning/syllabus.md) | [yes](../subjects/Applications%20of%20Machine%20Learning/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Applications of Power](courses/Applications%20of%20Power.md) | — | 1 | B TECH | AY 2019-20 |
| [Applications of Power Electronics](courses/Applications%20of%20Power%20Electronics.md) | — | 1 | B TECH | AY 2020-21 |
| [Applied Artificial Intelligence](../subjects/Applied%20Artificial%20Intelligence/syllabus.md) | [yes](../subjects/Applied%20Artificial%20Intelligence/README.md) | 4 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2024-25 |
| [Applied Artificial Intelligence and Agentic System](courses/Applied%20Artificial%20Intelligence%20and%20Agentic%20System.md) | — | 2 | B TECH, B TECH INTEGRATED | 2022-2028 to AY 2026-27 |
| [Applied Calculus](courses/Applied%20Calculus.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Applied Chemistry](../subjects/Applied%20Chemistry/syllabus.md) | [yes](../subjects/Applied%20Chemistry/README.md) | 2 | DIPLOMA | 2024-2027 to 2025-2028 |
| [Applied Chemistry Lab](courses/Applied%20Chemistry%20Lab.md) | — | 2 | DIPLOMA | 2024-2027 to 2025-2028 |
| [Applied Cryptography](courses/Applied%20Cryptography.md) | — | 4 | MBA Tech | 2018-2023 to 2019-2024 |
| [Applied Machine Learning](../subjects/Applied%20Machine%20Learning/syllabus.md) | [yes](../subjects/Applied%20Machine%20Learning/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Applied Mathematics - IIT](courses/Applied%20Mathematics%20-%20IIT.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Applied Mathematics for Data Science](../subjects/Applied%20Mathematics%20for%20Data%20Science/syllabus.md) | [yes](../subjects/Applied%20Mathematics%20for%20Data%20Science/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Applied Mathematics II](../subjects/Applied%20Mathematics%20II/syllabus.md) | [yes](../subjects/Applied%20Mathematics%20II/README.md) | 1 | B TECH | AY 2018-19 |
| [Applied Mathematics III](../subjects/Applied%20Mathematics%20III/syllabus.md) | [yes](../subjects/Applied%20Mathematics%20III/README.md) | 2 | B TECH, B TECH WORK IN PROCESS | AY 2018-19 to 2019-2023 |
| [Applied Mathematics IV](../subjects/Applied%20Mathematics%20IV/syllabus.md) | [yes](../subjects/Applied%20Mathematics%20IV/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Applied Physics](courses/Applied%20Physics.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Applied Physics I](../subjects/Applied%20Physics%20I/syllabus.md) | [yes](../subjects/Applied%20Physics%20I/README.md) | 2 | DIPLOMA | 2024-2027 to 2025-2028 |
| [Applied Physics II](../subjects/Applied%20Physics%20II/syllabus.md) | [yes](../subjects/Applied%20Physics%20II/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Applied Physics-I Lab](courses/Applied%20Physics-I%20Lab.md) | — | 2 | DIPLOMA | 2024-2027 to 2025-2028 |
| [Applied Physics-II Lab](courses/Applied%20Physics-II%20Lab.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Applied Statistics and Time Series Forecasting](../subjects/Applied%20Statistics%20and%20Time%20Series%20Forecasting/syllabus.md) | [yes](../subjects/Applied%20Statistics%20and%20Time%20Series%20Forecasting/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Applied Thermodynamics](../subjects/Applied%20Thermodynamics/syllabus.md) | [yes](../subjects/Applied%20Thermodynamics/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Applied Time Series Analysis](../subjects/Applied%20Time%20Series%20Analysis/syllabus.md) | [yes](../subjects/Applied%20Time%20Series%20Analysis/README.md) | 16 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2020-2024 to AY 2026-27 |
| [Applied Vector and Linear](courses/Applied%20Vector%20and%20Linear.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Artificial Intelligence](../subjects/Artificial%20Intelligence/syllabus.md) | [yes](../subjects/Artificial%20Intelligence/README.md) | 79 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2011-2016 to AY 2025-26 |
| [Artificial Intelligence - Deep Learning and Generative AI](../subjects/Artificial%20Intelligence%20-%20Deep%20Learning%20and%20Generative%20AI/syllabus.md) | [yes](../subjects/Artificial%20Intelligence%20-%20Deep%20Learning%20and%20Generative%20AI/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Artificial Intelligence and Machine Learning](../subjects/Artificial%20Intelligence%20and%20Machine%20Learning/syllabus.md) | [yes](../subjects/Artificial%20Intelligence%20and%20Machine%20Learning/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, M Tech | 2018-2022 to 2026-2028 |
| [Artificial Intelligence and Robotics](../subjects/Artificial%20Intelligence%20and%20Robotics/syllabus.md) | [yes](../subjects/Artificial%20Intelligence%20and%20Robotics/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Artificial Intelligence for Mechanical Engineers](../subjects/Artificial%20Intelligence%20for%20Mechanical%20Engineers/syllabus.md) | [yes](../subjects/Artificial%20Intelligence%20for%20Mechanical%20Engineers/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Augmented and Virtual Reality](courses/Augmented%20and%20Virtual%20Reality.md) | — | 2 | MCA | 2020-2023 to 2021-2024 |
| [Automatic Control](courses/Automatic%20Control.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Automatic Control Systems](../subjects/Automatic%20Control%20Systems/syllabus.md) | [yes](../subjects/Automatic%20Control%20Systems/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Automation in Manufacturing](../subjects/Automation%20in%20Manufacturing/syllabus.md) | [yes](../subjects/Automation%20in%20Manufacturing/README.md) | 8 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2026-27 |
| [Automotive Electronics](../subjects/Automotive%20Electronics/syllabus.md) | [yes](../subjects/Automotive%20Electronics/README.md) | 9 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2022 |
| [Automotive Engineering](../subjects/Automotive%20Engineering/syllabus.md) | [yes](../subjects/Automotive%20Engineering/README.md) | 31 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2023-2029 |
| [Autonomous Navigation of Electric Vehicles](../subjects/Autonomous%20Navigation%20of%20Electric%20Vehicles/syllabus.md) | [yes](../subjects/Autonomous%20Navigation%20of%20Electric%20Vehicles/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2025-26 |
| [B2B Marketing](../subjects/B2B%20Marketing/syllabus.md) | [yes](../subjects/B2B%20Marketing/README.md) | 22 | MBA Tech | 2017-2022 to 2022-2027 |
| [BA for Industries](courses/BA%20for%20Industries.md) | — | 2 | B TECH, MBA Tech | 2018-2023 |
| [Base Programing](courses/Base%20Programing.md) | — | 1 | MBA Tech | 2014-2019 |
| [Basic Computer Hardware and Troubleshooting](courses/Basic%20Computer%20Hardware%20and%20Troubleshooting.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Basic Control Systems](../subjects/Basic%20Control%20Systems/syllabus.md) | [yes](../subjects/Basic%20Control%20Systems/README.md) | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Basic Data Structures](../subjects/Basic%20Data%20Structures/syllabus.md) | [yes](../subjects/Basic%20Data%20Structures/README.md) | 8 | B TECH INTEGRATED | 2019-2025 to 2023-2029 |
| [Basic Decision Making with Spreadsheet](../subjects/Basic%20Decision%20Making%20with%20Spreadsheet/syllabus.md) | [yes](../subjects/Basic%20Decision%20Making%20with%20Spreadsheet/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2020-2024 to AY 2026-27 |
| [Basic Electrical and Electronics](courses/Basic%20Electrical%20and%20Electronics.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Basic Electrical and Electronics Engineering](../subjects/Basic%20Electrical%20and%20Electronics%20Engineering/syllabus.md) | [yes](../subjects/Basic%20Electrical%20and%20Electronics%20Engineering/README.md) | 27 | B TECH, B TECH WORK IN PROCESS, MBA Tech | AY 2020-21 to AY 2026-27 |
| [Basic Electrical Engineering](../subjects/Basic%20Electrical%20Engineering/syllabus.md) | [yes](../subjects/Basic%20Electrical%20Engineering/README.md) | 10 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to 2020-2025 |
| [Basic Electrical Engineering Brciioon](courses/Basic%20Electrical%20Engineering%20Brciioon.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Basic Electrical Engineering I](courses/Basic%20Electrical%20Engineering%20I.md) | — | 1 | B TECH WORK IN PROCESS | 2013-2017 |
| [Basic Electrical Engineering Sat](courses/Basic%20Electrical%20Engineering%20Sat.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Basic Electrical Engineering SE Gaal](courses/Basic%20Electrical%20Engineering%20SE%20Gaal.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Basic Electronics](../subjects/Basic%20Electronics/syllabus.md) | [yes](../subjects/Basic%20Electronics/README.md) | 21 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2023-2029 |
| [Basic Manufacturing Processes](../subjects/Basic%20Manufacturing%20Processes/syllabus.md) | [yes](../subjects/Basic%20Manufacturing%20Processes/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Basic Marketing](../subjects/Basic%20Marketing/syllabus.md) | [yes](../subjects/Basic%20Marketing/README.md) | 3 | M Tech | 2019-2021 to 2021-2023 |
| [Basic of Engineering Chemistry](../subjects/Basic%20of%20Engineering%20Chemistry/syllabus.md) | [yes](../subjects/Basic%20of%20Engineering%20Chemistry/README.md) | 1 | B TECH INTEGRATED | 2020-2026 |
| [Basic Thermodynamics](../subjects/Basic%20Thermodynamics/syllabus.md) | [yes](../subjects/Basic%20Thermodynamics/README.md) | 5 | B TECH INTEGRATED, DIPLOMA | 2020-2026 to 2024-2027 |
| [Basics of Computer System](courses/Basics%20of%20Computer%20System.md) | — | 4 | B TECH INTEGRATED | 2015-2021 to 2019-2025 |
| [Basics of Engineering](courses/Basics%20of%20Engineering.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Basics of Machine Drawing](../subjects/Basics%20of%20Machine%20Drawing/syllabus.md) | [yes](../subjects/Basics%20of%20Machine%20Drawing/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Basics of Manufacturing Engineering](../subjects/Basics%20of%20Manufacturing%20Engineering/syllabus.md) | [yes](../subjects/Basics%20of%20Manufacturing%20Engineering/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Basics of Mechanical Engineering](courses/Basics%20of%20Mechanical%20Engineering.md) | — | 1 | B TECH INTEGRATED | 2023-2029 |
| [Basics of Multimedia and Animation](courses/Basics%20of%20Multimedia%20and%20Animation.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Basics of Operations and Supply Chain](courses/Basics%20of%20Operations%20and%20Supply%20Chain.md) | — | 1 | M Tech | 2017-2019 |
| [Basics of Operations and Supply Chain Management](../subjects/Basics%20of%20Operations%20and%20Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Basics%20of%20Operations%20and%20Supply%20Chain%20Management/README.md) | 4 | M Tech | 2018-2020 to 2021-2023 |
| [Basics of Python](../subjects/Basics%20of%20Python/syllabus.md) | [yes](../subjects/Basics%20of%20Python/README.md) | 4 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Basics of Web Development](../subjects/Basics%20of%20Web%20Development/syllabus.md) | [yes](../subjects/Basics%20of%20Web%20Development/README.md) | 2 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Behavioral Economics](../subjects/Behavioral%20Economics/syllabus.md) | [yes](../subjects/Behavioral%20Economics/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2026-27 |
| [Best Practices in Operations](../subjects/Best%20Practices%20in%20Operations/syllabus.md) | [yes](../subjects/Best%20Practices%20in%20Operations/README.md) | 18 | MBA Tech | 2014-2019 to 2022-2027 |
| [Big Data](../subjects/Big%20Data/syllabus.md) | [yes](../subjects/Big%20Data/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Big Data Analytics](../subjects/Big%20Data%20Analytics/syllabus.md) | [yes](../subjects/Big%20Data%20Analytics/README.md) | 28 | B TECH, B TECH INTEGRATED, Current electives 2026-27, MBA Tech, MCA | 2020-2025 to AY 2026-27 |
| [Big Data Technology](../subjects/Big%20Data%20Technology/syllabus.md) | [yes](../subjects/Big%20Data%20Technology/README.md) | 29 | M Tech, MBA Tech | 2014-2019 to 2023-2025 |
| [Big Data Technology (Computational Technique](courses/Big%20Data%20Technology%20%28Computational%20Technique.md) | — | 3 | M Tech | 2015-2017 to 2016-2018 |
| [Big Data with Hadoop](courses/Big%20Data%20with%20Hadoop.md) | — | 5 | B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to 2019-2023 |
| [Bio Chemical Engineering](../subjects/Bio%20Chemical%20Engineering/syllabus.md) | [yes](../subjects/Bio%20Chemical%20Engineering/README.md) | 3 | MBA Tech | 2014-2019 to 2017-2022 |
| [Bio Informatics (Trealve- 111)](courses/Bio%20Informatics%20%28Trealve-%20111%29.md) | — | 1 | B TECH | — |
| [Bio-Energetic Architecture and Built Environment](courses/Bio-Energetic%20Architecture%20and%20Built%20Environment.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Bio-Mimicry](courses/Bio-Mimicry.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Biology for Engineers](../subjects/Biology%20for%20Engineers/syllabus.md) | [yes](../subjects/Biology%20for%20Engineers/README.md) | 1 | MBA Tech | 2020-2025 |
| [Biomechanics](../subjects/Biomechanics/syllabus.md) | [yes](../subjects/Biomechanics/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2026-27 |
| [Biomedical Instrumentation](../subjects/Biomedical%20Instrumentation/syllabus.md) | [yes](../subjects/Biomedical%20Instrumentation/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Biometrics](../subjects/Biometrics/syllabus.md) | [yes](../subjects/Biometrics/README.md) | 27 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Biometrics (Department](courses/Biometrics%20%28Department.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Biometrics Applications](../subjects/Biometrics%20Applications/syllabus.md) | [yes](../subjects/Biometrics%20Applications/README.md) | 4 | MBA Tech | 2013-2018 to 2017-2022 |
| [Biometrics(E1ective-Ill) I I](courses/Biometrics%28E1ective-Ill%29%20I%20I.md) | — | 1 | B TECH | — |
| [Block Chain](../subjects/Block%20Chain/syllabus.md) | [yes](../subjects/Block%20Chain/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Blockchain Security and Forensics](../subjects/Blockchain%20Security%20and%20Forensics/syllabus.md) | [yes](../subjects/Blockchain%20Security%20and%20Forensics/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Blockchain Technology](../subjects/Blockchain%20Technology/syllabus.md) | [yes](../subjects/Blockchain%20Technology/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, Current electives 2026-27, MBA Tech, MCA | 2020-2024 to AY 2026-27 |
| [Brand Management](../subjects/Brand%20Management/syllabus.md) | [yes](../subjects/Brand%20Management/README.md) | 13 | MBA Tech | 2014-2019 to 2022-2027 |
| [Brand Management Module Codé¢](courses/Brand%20Management%20Module%20Cod%C3%A9%C2%A2.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Bridge Engineering](../subjects/Bridge%20Engineering/syllabus.md) | [yes](../subjects/Bridge%20Engineering/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Broadband Technology](../subjects/Broadband%20Technology/syllabus.md) | [yes](../subjects/Broadband%20Technology/README.md) | 8 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2015-16 |
| [Building Construction](../subjects/Building%20Construction/syllabus.md) | [yes](../subjects/Building%20Construction/README.md) | 2 | PGDM | AY 2017-18 to AY 2018-19 |
| [Building Design and Drawing](../subjects/Building%20Design%20and%20Drawing/syllabus.md) | [yes](../subjects/Building%20Design%20and%20Drawing/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2015-2020 to AY 2026-27 |
| [Building Design and Drawing I](../subjects/Building%20Design%20and%20Drawing%20I/syllabus.md) | [yes](../subjects/Building%20Design%20and%20Drawing%20I/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2018-19 |
| [Building Design and Drawing II](../subjects/Building%20Design%20and%20Drawing%20II/syllabus.md) | [yes](../subjects/Building%20Design%20and%20Drawing%20II/README.md) | 12 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2017-2023 |
| [Building Materials and Construction](../subjects/Building%20Materials%20and%20Construction/syllabus.md) | [yes](../subjects/Building%20Materials%20and%20Construction/README.md) | 11 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2018-19 |
| [Building Services](../subjects/Building%20Services/syllabus.md) | [yes](../subjects/Building%20Services/README.md) | 1 | PGDM | — |
| [Building Utilities and Services](../subjects/Building%20Utilities%20and%20Services/syllabus.md) | [yes](../subjects/Building%20Utilities%20and%20Services/README.md) | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2026-27 |
| [Business Analytics](../subjects/Business%20Analytics/syllabus.md) | [yes](../subjects/Business%20Analytics/README.md) | 18 | MBA Tech | 2018-2023 to 2022-2027 |
| [Business Analytics for Decision Making](../subjects/Business%20Analytics%20for%20Decision%20Making/syllabus.md) | [yes](../subjects/Business%20Analytics%20for%20Decision%20Making/README.md) | 13 | MBA Tech | 2015-2020 to 2017-2022 |
| [Business Calculus](../subjects/Business%20Calculus/syllabus.md) | [yes](../subjects/Business%20Calculus/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Business Communication](../subjects/Business%20Communication/syllabus.md) | [yes](../subjects/Business%20Communication/README.md) | 6 | B TECH, MBA Tech | 2017-2022 to AY 2025-26 |
| [Business Communication and Value](courses/Business%20Communication%20and%20Value.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Business Communication and Value Science](courses/Business%20Communication%20and%20Value%20Science.md) | — | 2 | B TECH WORK IN PROCESS | 2019-2023 |
| [Business Communication and Value Science I](../subjects/Business%20Communication%20and%20Value%20Science%20I/syllabus.md) | [yes](../subjects/Business%20Communication%20and%20Value%20Science%20I/README.md) | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2024-25 |
| [Business Communication and Value Science II](../subjects/Business%20Communication%20and%20Value%20Science%20II/syllabus.md) | [yes](../subjects/Business%20Communication%20and%20Value%20Science%20II/README.md) | 7 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2023-24 |
| [Business Communication and Value Science III](../subjects/Business%20Communication%20and%20Value%20Science%20III/syllabus.md) | [yes](../subjects/Business%20Communication%20and%20Value%20Science%20III/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2023-24 |
| [Business Communication and Value Science IV](courses/Business%20Communication%20and%20Value%20Science%20IV.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2023-24 |
| [Business Economics](../subjects/Business%20Economics/syllabus.md) | [yes](../subjects/Business%20Economics/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Business Information Visualization and Analysis](../subjects/Business%20Information%20Visualization%20and%20Analysis/syllabus.md) | [yes](../subjects/Business%20Information%20Visualization%20and%20Analysis/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Business Model in Infrastructure Management](../subjects/Business%20Model%20in%20Infrastructure%20Management/syllabus.md) | [yes](../subjects/Business%20Model%20in%20Infrastructure%20Management/README.md) | 14 | MBA Tech | 2014-2019 to 2022-2027 |
| [Business Models for Circular Economy](courses/Business%20Models%20for%20Circular%20Economy.md) | — | 3 | MBA Tech | 2021-2026 to 2022-2027 |
| [Business Problem Solving](courses/Business%20Problem%20Solving.md) | — | 1 | MBA Tech | 2018-2023 |
| [Business Research Methods](../subjects/Business%20Research%20Methods/syllabus.md) | [yes](../subjects/Business%20Research%20Methods/README.md) | 23 | MBA Tech | 2016-2021 to 2022-2027 |
| [Business Simulation](courses/Business%20Simulation.md) | — | 17 | MBA Tech | 2014-2019 to 2022-2027 |
| [Business Statistics](../subjects/Business%20Statistics/syllabus.md) | [yes](../subjects/Business%20Statistics/README.md) | 21 | MBA Tech | 2016-2021 to 2025-2030 |
| [Business Strategy](../subjects/Business%20Strategy/syllabus.md) | [yes](../subjects/Business%20Strategy/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Business Visualization](courses/Business%20Visualization.md) | — | 57 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2013-2017 to AY 2024-25 |
| [Buyer Behaviour](../subjects/Buyer%20Behaviour/syllabus.md) | [yes](../subjects/Buyer%20Behaviour/README.md) | 15 | MBA Tech | 2014-2019 to 2022-2027 |
| [C Programming](../subjects/C%20Programming/syllabus.md) | [yes](../subjects/C%20Programming/README.md) | 5 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [CAD Advanced Processes](courses/CAD%20Advanced%20Processes.md) | — | 3 | B TECH | AY 2025-26 to AY 2026-27 |
| [CAD CAM CAE](../subjects/CAD%20CAM%20CAE/syllabus.md) | [yes](../subjects/CAD%20CAM%20CAE/README.md) | 5 | B TECH, MBA Tech | 2011-2016 to AY 2015-16 |
| [CAD CAM CIM](../subjects/CAD%20CAM%20CIM/syllabus.md) | [yes](../subjects/CAD%20CAM%20CIM/README.md) | 33 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [CAD Fundamental Processes](courses/CAD%20Fundamental%20Processes.md) | — | 3 | B TECH | AY 2025-26 to AY 2026-27 |
| [Cad/Cami/Cim](courses/Cad-Cami-Cim.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Calculus](../subjects/Calculus/syllabus.md) | [yes](../subjects/Calculus/README.md) | 39 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2026 to AY 2026-27 |
| [Capital Market and Real Estate](../subjects/Capital%20Market%20and%20Real%20Estate/syllabus.md) | [yes](../subjects/Capital%20Market%20and%20Real%20Estate/README.md) | 1 | PGDM | AY 2018-19 |
| [Capstone Project](courses/Capstone%20Project.md) | — | 81 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2016-2021 to AY 2026-27 |
| [Capstone Project I](courses/Capstone%20Project%20I.md) | — | 3 | MBA Tech | 2016-2021 to 2017-2022 |
| [Capstone Project II](courses/Capstone%20Project%20II.md) | — | 2 | MBA Tech | 2017-2022 |
| [Capstone Project on Design of Structures](courses/Capstone%20Project%20on%20Design%20of%20Structures.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Career Development and Professional Skills](courses/Career%20Development%20and%20Professional%20Skills.md) | — | 6 | M Tech | 2024-2026 to 2026-2028 |
| [Careers in Business Information Technology](courses/Careers%20in%20Business%20Information%20Technology.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Catalytic Science and Engineering](../subjects/Catalytic%20Science%20and%20Engineering/syllabus.md) | [yes](../subjects/Catalytic%20Science%20and%20Engineering/README.md) | 1 | MBA Tech | 2020-2025 |
| [Change Management and Organisational Development](courses/Change%20Management%20and%20Organisational%20Development.md) | — | 1 | MBA Tech | 2022-2027 |
| [Chemical Engineering Thermodynamics](../subjects/Chemical%20Engineering%20Thermodynamics/syllabus.md) | [yes](../subjects/Chemical%20Engineering%20Thermodynamics/README.md) | 3 | MBA Tech | 2016-2021 to 2018-2023 |
| [Chemical Process II](../subjects/Chemical%20Process%20II/syllabus.md) | [yes](../subjects/Chemical%20Process%20II/README.md) | 2 | MBA Tech | 2015-2020 to 2016-2021 |
| [Chemical Processes I](../subjects/Chemical%20Processes%20I/syllabus.md) | [yes](../subjects/Chemical%20Processes%20I/README.md) | 3 | MBA Tech | 2015-2020 to 2017-2022 |
| [Chemical Project Engineering](courses/Chemical%20Project%20Engineering.md) | — | 1 | MBA Tech | 2018-2023 |
| [Chemical Project Engineering and Economics](../subjects/Chemical%20Project%20Engineering%20and%20Economics/syllabus.md) | [yes](../subjects/Chemical%20Project%20Engineering%20and%20Economics/README.md) | 2 | MBA Tech | 2019-2024 to 2020-2025 |
| [Chemical Reaction Engineering](../subjects/Chemical%20Reaction%20Engineering/syllabus.md) | [yes](../subjects/Chemical%20Reaction%20Engineering/README.md) | 3 | MBA Tech | 2015-2020 to 2020-2025 |
| [Chemical Reaction Engineering I](courses/Chemical%20Reaction%20Engineering%20I.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Chemical Reaction Engineering II](../subjects/Chemical%20Reaction%20Engineering%20II/syllabus.md) | [yes](../subjects/Chemical%20Reaction%20Engineering%20II/README.md) | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Chemistry](../subjects/Chemistry/syllabus.md) | [yes](../subjects/Chemistry/README.md) | 24 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Chemistry I](../subjects/Chemistry%20I/syllabus.md) | [yes](../subjects/Chemistry%20I/README.md) | 6 | B TECH INTEGRATED | 2015-2021 to 2023-2029 |
| [Chemistry II](../subjects/Chemistry%20II/syllabus.md) | [yes](../subjects/Chemistry%20II/README.md) | 15 | B TECH INTEGRATED | 2014-2020 to 2023-2029 |
| [Circuit and Network Theory](../subjects/Circuit%20and%20Network%20Theory/syllabus.md) | [yes](../subjects/Circuit%20and%20Network%20Theory/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Civil Engineering Workshop](courses/Civil%20Engineering%20Workshop.md) | — | 1 | B TECH | AY 2012-13 |
| [Classical Control Systems](../subjects/Classical%20Control%20Systems/syllabus.md) | [yes](../subjects/Classical%20Control%20Systems/README.md) | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Classical Physics](../subjects/Classical%20Physics/syllabus.md) | [yes](../subjects/Classical%20Physics/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Cloud Computing](../subjects/Cloud%20Computing/syllabus.md) | [yes](../subjects/Cloud%20Computing/README.md) | 53 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, Current electives 2026-27, M Tech, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Cloud Computing and IoT](../subjects/Cloud%20Computing%20and%20IoT/syllabus.md) | [yes](../subjects/Cloud%20Computing%20and%20IoT/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Cloud Microservices and Application](../subjects/Cloud%20Microservices%20and%20Application/syllabus.md) | [yes](../subjects/Cloud%20Microservices%20and%20Application/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2021-22 |
| [Cloud Security](../subjects/Cloud%20Security/syllabus.md) | [yes](../subjects/Cloud%20Security/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Cloud Technology](../subjects/Cloud%20Technology/syllabus.md) | [yes](../subjects/Cloud%20Technology/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2017-2023 to 2019-2025 |
| [Cognitive Science and Analytics](../subjects/Cognitive%20Science%20and%20Analytics/syllabus.md) | [yes](../subjects/Cognitive%20Science%20and%20Analytics/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Communication Skills](../subjects/Communication%20Skills/syllabus.md) | [yes](../subjects/Communication%20Skills/README.md) | 19 | B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech, MCA | 2013-2017 to 2025-2028 |
| [Communication Skills I](../subjects/Communication%20Skills%20I/syllabus.md) | [yes](../subjects/Communication%20Skills%20I/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Communication Skills II](../subjects/Communication%20Skills%20II/syllabus.md) | [yes](../subjects/Communication%20Skills%20II/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Communication Skills Sia](courses/Communication%20Skills%20Sia.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Communication Technology for IoT](../subjects/Communication%20Technology%20for%20IoT/syllabus.md) | [yes](../subjects/Communication%20Technology%20for%20IoT/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Communication Theory and Systems](../subjects/Communication%20Theory%20and%20Systems/syllabus.md) | [yes](../subjects/Communication%20Theory%20and%20Systems/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2024-25 |
| [Compiler Design](../subjects/Compiler%20Design/syllabus.md) | [yes](../subjects/Compiler%20Design/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2025-26 |
| [Complex Analysis and Discrete](courses/Complex%20Analysis%20and%20Discrete.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Complex Variables and Transforms](../subjects/Complex%20Variables%20and%20Transforms/syllabus.md) | [yes](../subjects/Complex%20Variables%20and%20Transforms/README.md) | 28 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [Composite Materials](../subjects/Composite%20Materials/syllabus.md) | [yes](../subjects/Composite%20Materials/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Computational Analytics for Marketing](../subjects/Computational%20Analytics%20for%20Marketing/syllabus.md) | [yes](../subjects/Computational%20Analytics%20for%20Marketing/README.md) | 5 | M Tech | 2021-2023 to 2023-2025 |
| [Computational Finance and Modeling](../subjects/Computational%20Finance%20and%20Modeling/syllabus.md) | [yes](../subjects/Computational%20Finance%20and%20Modeling/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2026-27 |
| [Computational Fluid Dynamics](../subjects/Computational%20Fluid%20Dynamics/syllabus.md) | [yes](../subjects/Computational%20Fluid%20Dynamics/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to AY 2026-27 |
| [Computational Linguistic and Natural Language Processing](courses/Computational%20Linguistic%20and%20Natural%20Language%20Processing.md) | — | 1 | B TECH | — |
| [Computational Methods](../subjects/Computational%20Methods/syllabus.md) | [yes](../subjects/Computational%20Methods/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Computational Methods in Engineering](courses/Computational%20Methods%20in%20Engineering.md) | — | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Computational Neuroscience](../subjects/Computational%20Neuroscience/syllabus.md) | [yes](../subjects/Computational%20Neuroscience/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2024-25 |
| [Computational Statistics](../subjects/Computational%20Statistics/syllabus.md) | [yes](../subjects/Computational%20Statistics/README.md) | 8 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Computational Thinking for Problem Solving](../subjects/Computational%20Thinking%20for%20Problem%20Solving/syllabus.md) | [yes](../subjects/Computational%20Thinking%20for%20Problem%20Solving/README.md) | 10 | B TECH, MBA Tech | AY 2025-26 to AY 2026-27 |
| [Computer](courses/Computer.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2020-21 |
| [Computer 1 Organization and Architecture](courses/Computer%201%20Organization%20and%20Architecture.md) | — | 1 | B TECH | AY 2013-14 |
| [Computer Aided Building Drawing](courses/Computer%20Aided%20Building%20Drawing.md) | — | 5 | B TECH INTEGRATED | 2014-2020 to 2018-2024 |
| [Computer Aided Design and Drafting](courses/Computer%20Aided%20Design%20and%20Drafting.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Computer Aided Power](courses/Computer%20Aided%20Power.md) | — | 1 | B TECH | AY 2019-20 |
| [Computer Aided Power System Analysis](courses/Computer%20Aided%20Power%20System%20Analysis.md) | — | 4 | B TECH, MBA Tech | 2015-2020 to AY 2020-21 |
| [Computer Applications in Civil Engineering I](courses/Computer%20Applications%20in%20Civil%20Engineering%20I.md) | — | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2025-26 |
| [Computer Applications in Civil Engineering II](courses/Computer%20Applications%20in%20Civil%20Engineering%20II.md) | — | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [Computer Architecture](../subjects/Computer%20Architecture/syllabus.md) | [yes](../subjects/Computer%20Architecture/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Computer Communication](courses/Computer%20Communication.md) | — | 1 | B TECH | AY 2019-20 |
| [Computer Communication Networks](../subjects/Computer%20Communication%20Networks/syllabus.md) | [yes](../subjects/Computer%20Communication%20Networks/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2016-2022 |
| [Computer Graphics](../subjects/Computer%20Graphics/syllabus.md) | [yes](../subjects/Computer%20Graphics/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2016-2020 to AY 2024-25 |
| [Computer Hardware and Maintenance](courses/Computer%20Hardware%20and%20Maintenance.md) | — | 5 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Computer Networks](../subjects/Computer%20Networks/syllabus.md) | [yes](../subjects/Computer%20Networks/README.md) | 67 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2026-27 |
| [Computer Networks I](courses/Computer%20Networks%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Computer Organization](courses/Computer%20Organization.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to 2022-2026 |
| [Computer Organization 4° Architecturé](courses/Computer%20Organization%204%C2%B0%20Architectur%C3%A9.md) | — | 1 | B TECH | AY 2017-18 |
| [Computer Organization and Architecture](../subjects/Computer%20Organization%20and%20Architecture/syllabus.md) | [yes](../subjects/Computer%20Organization%20and%20Architecture/README.md) | 65 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | AY 2011-12 to AY 2026-27 |
| [Computer Programming](../subjects/Computer%20Programming/syllabus.md) | [yes](../subjects/Computer%20Programming/README.md) | 9 | B TECH INTEGRATED, DIPLOMA, MCA | 2014-2017 to 2025-2028 |
| [Computer Programming I](../subjects/Computer%20Programming%20I/syllabus.md) | [yes](../subjects/Computer%20Programming%20I/README.md) | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2015-2019 to 2019-2025 |
| [Computer Programming II](../subjects/Computer%20Programming%20II/syllabus.md) | [yes](../subjects/Computer%20Programming%20II/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2018-19 |
| [Computer Programming III](../subjects/Computer%20Programming%20III/syllabus.md) | [yes](../subjects/Computer%20Programming%20III/README.md) | 4 | B TECH INTEGRATED | 2015-2021 to 2018-2024 |
| [Computer Simulation and Modeling](../subjects/Computer%20Simulation%20and%20Modeling/syllabus.md) | [yes](../subjects/Computer%20Simulation%20and%20Modeling/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2019-20 |
| [Computer Simulation and Modeling I I](courses/Computer%20Simulation%20and%20Modeling%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Computer System Architecture](../subjects/Computer%20System%20Architecture/syllabus.md) | [yes](../subjects/Computer%20System%20Architecture/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Computer Vision](../subjects/Computer%20Vision/syllabus.md) | [yes](../subjects/Computer%20Vision/README.md) | 38 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2018-2020 to AY 2026-27 |
| [Computer Vision (Department](courses/Computer%20Vision%20%28Department.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Computer Vision and Applications](../subjects/Computer%20Vision%20and%20Applications/syllabus.md) | [yes](../subjects/Computer%20Vision%20and%20Applications/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Concrete Technology](../subjects/Concrete%20Technology/syllabus.md) | [yes](../subjects/Concrete%20Technology/README.md) | 27 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Constitution of India](../subjects/Constitution%20of%20India/syllabus.md) | [yes](../subjects/Constitution%20of%20India/README.md) | 84 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to AY 2026-27 |
| [Constitution of India I](courses/Constitution%20of%20India%20I.md) | — | 1 | B TECH WORK IN PROCESS | 2013-2017 |
| [Constitution of India Ptceros Stato](courses/Constitution%20of%20India%20Ptceros%20Stato.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Constitution of India SE Iae RaTies](courses/Constitution%20of%20India%20SE%20Iae%20RaTies.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Constitution of Lndia (Only for 2013-14)](courses/Constitution%20of%20Lndia%20%28Only%20for%202013-14%29.md) | — | 1 | B TECH | AY 2013-14 |
| [Construction Contracts and Administration](../subjects/Construction%20Contracts%20and%20Administration/syllabus.md) | [yes](../subjects/Construction%20Contracts%20and%20Administration/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2015-2021 to AY 2026-27 |
| [Construction Economics and](courses/Construction%20Economics%20and.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Construction Economics and Finance Management](../subjects/Construction%20Economics%20and%20Finance%20Management/syllabus.md) | [yes](../subjects/Construction%20Economics%20and%20Finance%20Management/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to AY 2026-27 |
| [Construction Engineering](../subjects/Construction%20Engineering/syllabus.md) | [yes](../subjects/Construction%20Engineering/README.md) | 5 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Construction Equipment and Techniques](../subjects/Construction%20Equipment%20and%20Techniques/syllabus.md) | [yes](../subjects/Construction%20Equipment%20and%20Techniques/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019 |
| [Construction Logistics](../subjects/Construction%20Logistics/syllabus.md) | [yes](../subjects/Construction%20Logistics/README.md) | 1 | PGDM | AY 2018-19 |
| [Construction Machinery and Equipment](courses/Construction%20Machinery%20and%20Equipment.md) | — | 2 | B TECH, MBA Tech | 2012-2017 to AY 2015-16 |
| [Construction Material Management](../subjects/Construction%20Material%20Management/syllabus.md) | [yes](../subjects/Construction%20Material%20Management/README.md) | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Construction Materials](../subjects/Construction%20Materials/syllabus.md) | [yes](../subjects/Construction%20Materials/README.md) | 8 | B TECH INTEGRATED, PGDM | 2014-2020 to 2019-2025 |
| [Construction Project Management](../subjects/Construction%20Project%20Management/syllabus.md) | [yes](../subjects/Construction%20Project%20Management/README.md) | 2 | B TECH | AY 2013-14 to AY 2014-15 |
| [Construction Project Management and Finance](../subjects/Construction%20Project%20Management%20and%20Finance/syllabus.md) | [yes](../subjects/Construction%20Project%20Management%20and%20Finance/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Construction Quality Control](courses/Construction%20Quality%20Control.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2017-2023 |
| [Construction Quality Control and Assurance](../subjects/Construction%20Quality%20Control%20and%20Assurance/syllabus.md) | [yes](../subjects/Construction%20Quality%20Control%20and%20Assurance/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2026-27 |
| [Construction Safety](../subjects/Construction%20Safety/syllabus.md) | [yes](../subjects/Construction%20Safety/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2018-2024 |
| [Construction Techniques and Safety](../subjects/Construction%20Techniques%20and%20Safety/syllabus.md) | [yes](../subjects/Construction%20Techniques%20and%20Safety/README.md) | 1 | MBA Tech | 2011-2016 |
| [Construction Technology](../subjects/Construction%20Technology/syllabus.md) | [yes](../subjects/Construction%20Technology/README.md) | 9 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Contemporary Short Fiction](../subjects/Contemporary%20Short%20Fiction/syllabus.md) | [yes](../subjects/Contemporary%20Short%20Fiction/README.md) | 5 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [Contract, Competition and Consumer Laws](../subjects/Contract%2C%20Competition%20and%20Consumer%20Laws/syllabus.md) | [yes](../subjects/Contract%2C%20Competition%20and%20Consumer%20Laws/README.md) | 11 | MBA Tech | 2021-2026 to 2022-2027 |
| [Control System](../subjects/Control%20System/syllabus.md) | [yes](../subjects/Control%20System/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Control System Engineering](../subjects/Control%20System%20Engineering/syllabus.md) | [yes](../subjects/Control%20System%20Engineering/README.md) | 16 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2016-2020 to AY 2024-25 |
| [Control System I](../subjects/Control%20System%20I/syllabus.md) | [yes](../subjects/Control%20System%20I/README.md) | 1 | MBA Tech | 2016-2021 |
| [Control Systems II](../subjects/Control%20Systems%20II/syllabus.md) | [yes](../subjects/Control%20Systems%20II/README.md) | 1 | MBA Tech | 2016-2021 |
| [Conventional Energy and Process Integration](courses/Conventional%20Energy%20and%20Process%20Integration.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Convex Optimization](../subjects/Convex%20Optimization/syllabus.md) | [yes](../subjects/Convex%20Optimization/README.md) | 3 | M Tech | 2021-2023 to 2023-2025 |
| [Core Java](../subjects/Core%20Java/syllabus.md) | [yes](../subjects/Core%20Java/README.md) | 6 | MCA | 2014-2017 to 2019-2022 |
| [Corporate Brand Strategy](courses/Corporate%20Brand%20Strategy.md) | — | 1 | MBA Tech | 2022-2027 |
| [Corporate Communication](courses/Corporate%20Communication.md) | — | 4 | MBA Tech | 2016-2021 to 2018-2023 |
| [Corporate Finance](../subjects/Corporate%20Finance/syllabus.md) | [yes](../subjects/Corporate%20Finance/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Cost and Management Accounting](../subjects/Cost%20and%20Management%20Accounting/syllabus.md) | [yes](../subjects/Cost%20and%20Management%20Accounting/README.md) | 3 | MBA Tech | 2016-2021 to 2017-2022 |
| [Cost and Management Accounting for Engineers](courses/Cost%20and%20Management%20Accounting%20for%20Engineers.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Cost Estimation](../subjects/Cost%20Estimation/syllabus.md) | [yes](../subjects/Cost%20Estimation/README.md) | 1 | MBA Tech | 2011-2016 |
| [Creativity and Ethics in Marketing](../subjects/Creativity%20and%20Ethics%20in%20Marketing/syllabus.md) | [yes](../subjects/Creativity%20and%20Ethics%20in%20Marketing/README.md) | 10 | B TECH, MBA Tech | 2018-2023 to AY 2024-25 |
| [Critical Thinking](courses/Critical%20Thinking.md) | — | 33 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Critical Thinking in Humanities](../subjects/Critical%20Thinking%20in%20Humanities/syllabus.md) | [yes](../subjects/Critical%20Thinking%20in%20Humanities/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Cryptography and Network Security](../subjects/Cryptography%20and%20Network%20Security/syllabus.md) | [yes](../subjects/Cryptography%20and%20Network%20Security/README.md) | 21 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2026-27 |
| [Cryptology](courses/Cryptology.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Customizing Active Workspace](courses/Customizing%20Active%20Workspace.md) | — | 1 | B TECH | AY 2026-27 |
| [Cyber Forensics](../subjects/Cyber%20Forensics/syllabus.md) | [yes](../subjects/Cyber%20Forensics/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Cyber Physical Systems Security](../subjects/Cyber%20Physical%20Systems%20Security/syllabus.md) | [yes](../subjects/Cyber%20Physical%20Systems%20Security/README.md) | 6 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2026-27 |
| [Cyber Security](../subjects/Cyber%20Security/syllabus.md) | [yes](../subjects/Cyber%20Security/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MCA | 2015-2018 to AY 2025-26 |
| [Cyber Security and Ethical Hacking](../subjects/Cyber%20Security%20and%20Ethical%20Hacking/syllabus.md) | [yes](../subjects/Cyber%20Security%20and%20Ethical%20Hacking/README.md) | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Cyber Security for Non-IT](../subjects/Cyber%20Security%20for%20Non-IT/syllabus.md) | [yes](../subjects/Cyber%20Security%20for%20Non-IT/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Cybersecurity Fundamentals](../subjects/Cybersecurity%20Fundamentals/syllabus.md) | [yes](../subjects/Cybersecurity%20Fundamentals/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Cybersecurity Risk Management](../subjects/Cybersecurity%20Risk%20Management/syllabus.md) | [yes](../subjects/Cybersecurity%20Risk%20Management/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Data Analysis and Mining](courses/Data%20Analysis%20and%20Mining.md) | — | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Data Analysis and Visualization](courses/Data%20Analysis%20and%20Visualization.md) | — | 3 | DIPLOMA | 2024-2027 |
| [Data Analysis with Python](../subjects/Data%20Analysis%20with%20Python/syllabus.md) | [yes](../subjects/Data%20Analysis%20with%20Python/README.md) | 4 | MCA | 2022-2024 to 2025-2027 |
| [Data Analytics](../subjects/Data%20Analytics/syllabus.md) | [yes](../subjects/Data%20Analytics/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Data Communication and Computer Networks](../subjects/Data%20Communication%20and%20Computer%20Networks/syllabus.md) | [yes](../subjects/Data%20Communication%20and%20Computer%20Networks/README.md) | 3 | DIPLOMA | 2024-2027 |
| [Data Driven Program Analysis](../subjects/Data%20Driven%20Program%20Analysis/syllabus.md) | [yes](../subjects/Data%20Driven%20Program%20Analysis/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Data Encryption and Network I](courses/Data%20Encryption%20and%20Network%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Data Encryption and Network Security](../subjects/Data%20Encryption%20and%20Network%20Security/syllabus.md) | [yes](../subjects/Data%20Encryption%20and%20Network%20Security/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Data Engineering](../subjects/Data%20Engineering/syllabus.md) | [yes](../subjects/Data%20Engineering/README.md) | 6 | M Tech | 2024-2026 to 2026-2028 |
| [Data Extraction and Processing](courses/Data%20Extraction%20and%20Processing.md) | — | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2026 to AY 2025-26 |
| [Data Gathering and Cleaning - ETL](courses/Data%20Gathering%20and%20Cleaning%20-%20ETL.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2022-23 |
| [Data Gathering and Cleaning - ETL Process](../subjects/Data%20Gathering%20and%20Cleaning%20-%20ETL%20Process/syllabus.md) | [yes](../subjects/Data%20Gathering%20and%20Cleaning%20-%20ETL%20Process/README.md) | 6 | B TECH, B TECH WORK IN PROCESS, M Tech | 2015-2017 to 2022-2024 |
| [Data Gathering Cleaning](../subjects/Data%20Gathering%20Cleaning/syllabus.md) | [yes](../subjects/Data%20Gathering%20Cleaning/README.md) | 7 | B TECH WORK IN PROCESS, M Tech | 2016-2018 to 2021-2023 |
| [Data Handling and Visualization](../subjects/Data%20Handling%20and%20Visualization/syllabus.md) | [yes](../subjects/Data%20Handling%20and%20Visualization/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Data Management](courses/Data%20Management.md) | — | 3 | M Tech | 2021-2023 to 2023-2025 |
| [Data Mining](../subjects/Data%20Mining/syllabus.md) | [yes](../subjects/Data%20Mining/README.md) | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Data Mining and Analytics](../subjects/Data%20Mining%20and%20Analytics/syllabus.md) | [yes](../subjects/Data%20Mining%20and%20Analytics/README.md) | 21 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2014-2019 to AY 2024-25 |
| [Data Mining and Analytics (Department](courses/Data%20Mining%20and%20Analytics%20%28Department.md) | — | 1 | B TECH | AY 2025-26 |
| [Data Privacy](../subjects/Data%20Privacy/syllabus.md) | [yes](../subjects/Data%20Privacy/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Data Science Analytics using R and Python](courses/Data%20Science%20Analytics%20using%20R%20and%20Python.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2021-22 |
| [Data Science and Big Data Analytics](../subjects/Data%20Science%20and%20Big%20Data%20Analytics/syllabus.md) | [yes](../subjects/Data%20Science%20and%20Big%20Data%20Analytics/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2012-2017 to 2019-2022 |
| [Data Science Ethics](courses/Data%20Science%20Ethics.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Data Science I](../subjects/Data%20Science%20I/syllabus.md) | [yes](../subjects/Data%20Science%20I/README.md) | 3 | M Tech | 2015-2017 to 2016-2018 |
| [Data Science II](../subjects/Data%20Science%20II/syllabus.md) | [yes](../subjects/Data%20Science%20II/README.md) | 3 | M Tech | 2015-2017 to 2016-2018 |
| [Data Science III](../subjects/Data%20Science%20III/syllabus.md) | [yes](../subjects/Data%20Science%20III/README.md) | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Data Struc](courses/Data%20Struc.md) | — | 1 | MBA Tech | 2014-2019 |
| [Data Structures](../subjects/Data%20Structures/syllabus.md) | [yes](../subjects/Data%20Structures/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2013-2017 to 2024-2027 |
| [Data Structures and Algorithms](../subjects/Data%20Structures%20and%20Algorithms/syllabus.md) | [yes](../subjects/Data%20Structures%20and%20Algorithms/README.md) | 80 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | AY 2012-13 to AY 2026-27 |
| [Data Structures and Algorithms Lab](courses/Data%20Structures%20and%20Algorithms%20Lab.md) | — | 13 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Data Visualization](courses/Data%20Visualization.md) | — | 2 | B TECH, MBA Tech | 2025-2030 to AY 2026-27 |
| [Data Visualization for Business Decisions](courses/Data%20Visualization%20for%20Business%20Decisions.md) | — | 5 | MBA Tech | 2020-2025 to 2022-2027 |
| [Data Visualization with Tableau](courses/Data%20Visualization%20with%20Tableau.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2021-22 |
| [Data Warehousing and Mining](../subjects/Data%20Warehousing%20and%20Mining/syllabus.md) | [yes](../subjects/Data%20Warehousing%20and%20Mining/README.md) | 42 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2012-2017 to AY 2025-26 |
| [Data Warehousing and Mining I](courses/Data%20Warehousing%20and%20Mining%20I.md) | — | 1 | B TECH | — |
| [Data Warehousing and Multidimensional Modeling](courses/Data%20Warehousing%20and%20Multidimensional%20Modeling.md) | — | 6 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Data Wrangling](../subjects/Data%20Wrangling/syllabus.md) | [yes](../subjects/Data%20Wrangling/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2021-2025 to AY 2026-27 |
| [Data Wrangling Fundamentals and Practices](courses/Data%20Wrangling%20Fundamentals%20and%20Practices.md) | — | 1 | B TECH INTEGRATED | 2023-2029 |
| [Database Administration](../subjects/Database%20Administration/syllabus.md) | [yes](../subjects/Database%20Administration/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2024-25 |
| [Database Management Systems](../subjects/Database%20Management%20Systems/syllabus.md) | [yes](../subjects/Database%20Management%20Systems/README.md) | 94 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to 2026-2028 |
| [Database Management Systems I I](courses/Database%20Management%20Systems%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Database Security](courses/Database%20Security.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Database Security (Department](courses/Database%20Security%20%28Department.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Database System Essentials](../subjects/Database%20System%20Essentials/syllabus.md) | [yes](../subjects/Database%20System%20Essentials/README.md) | 2 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [DE I - Conventional Energy](courses/DE%20I%20-%20Conventional%20Energy.md) | — | 1 | MBA Tech | 2020-2025 |
| [DE I - Petroleum Refining Technology](courses/DE%20I%20-%20Petroleum%20Refining%20Technology.md) | — | 1 | MBA Tech | 2020-2025 |
| [DE I - Process Concept to Commercialization](courses/DE%20I%20-%20Process%20Concept%20to%20Commercialization.md) | — | 1 | MBA Tech | 2020-2025 |
| [DE II - Energy Economics, Politics and Management](courses/DE%20II%20-%20Energy%20Economics%2C%20Politics%20and%20Management.md) | — | 1 | MBA Tech | 2020-2025 |
| [DE II - Fundamentals of Biotechnology and Biochemical Engineering](courses/DE%20II%20-%20Fundamentals%20of%20Biotechnology%20and%20Biochemical%20Engineering.md) | — | 1 | MBA Tech | 2020-2025 |
| [DE II - Programming for Chemical Engineers](courses/DE%20II%20-%20Programming%20for%20Chemical%20Engineers.md) | — | 1 | MBA Tech | 2020-2025 |
| [Deep Learning](../subjects/Deep%20Learning/syllabus.md) | [yes](../subjects/Deep%20Learning/README.md) | 69 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2017-2023 to AY 2026-27 |
| [Descriptive Analytics](courses/Descriptive%20Analytics.md) | — | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2020-21 |
| [Design an Art for Consumers](../subjects/Design%20an%20Art%20for%20Consumers/syllabus.md) | [yes](../subjects/Design%20an%20Art%20for%20Consumers/README.md) | 2 | B TECH | AY 2022-23 to AY 2023-24 |
| [Design and Analysis of Algorithms](../subjects/Design%20and%20Analysis%20of%20Algorithms/syllabus.md) | [yes](../subjects/Design%20and%20Analysis%20of%20Algorithms/README.md) | 41 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Design Experience I](courses/Design%20Experience%20I.md) | — | 14 | B TECH, B TECH INTEGRATED, MBA Tech | 2022-2028 to AY 2025-26 |
| [Design Experience II](courses/Design%20Experience%20II.md) | — | 11 | B TECH, B TECH INTEGRATED, MBA Tech | 2022-2028 to AY 2026-27 |
| [Design for Consumers](../subjects/Design%20for%20Consumers/syllabus.md) | [yes](../subjects/Design%20for%20Consumers/README.md) | 2 | B TECH | AY 2024-25 to AY 2026-27 |
| [Design of Bridge Structures](courses/Design%20of%20Bridge%20Structures.md) | — | 2 | B TECH | AY 2013-14 to AY 2014-15 |
| [Design of Heat Exchangers](courses/Design%20of%20Heat%20Exchangers.md) | — | 9 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2026-27 |
| [Design of Hydraulic Stru](courses/Design%20of%20Hydraulic%20Stru.md) | — | 1 | B TECH INTEGRATED | 2014-2020 |
| [Design of Hydraulic Structures](../subjects/Design%20of%20Hydraulic%20Structures/syllabus.md) | [yes](../subjects/Design%20of%20Hydraulic%20Structures/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2013-14 to AY 2026-27 |
| [Design of Liquid Retaining Structures](courses/Design%20of%20Liquid%20Retaining%20Structures.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Design of Machine Components](../subjects/Design%20of%20Machine%20Components/syllabus.md) | [yes](../subjects/Design%20of%20Machine%20Components/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Design of Machine Elements](../subjects/Design%20of%20Machine%20Elements/syllabus.md) | [yes](../subjects/Design%20of%20Machine%20Elements/README.md) | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Design of Machine Elements - I1 Teachin Evaluation Scheme](courses/Design%20of%20Machine%20Elements%20-%20I1%20Teachin%20Evaluation%20Scheme.md) | — | 1 | MBA Tech | 2011-2016 |
| [Design of Machine Elements Gode](courses/Design%20of%20Machine%20Elements%20Gode.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Design of Machine Elements I](../subjects/Design%20of%20Machine%20Elements%20I/syllabus.md) | [yes](../subjects/Design%20of%20Machine%20Elements%20I/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Design of Machine Elements II](../subjects/Design%20of%20Machine%20Elements%20II/syllabus.md) | [yes](../subjects/Design%20of%20Machine%20Elements%20II/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Design of Machine Elements III](../subjects/Design%20of%20Machine%20Elements%20III/syllabus.md) | [yes](../subjects/Design%20of%20Machine%20Elements%20III/README.md) | 3 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Design of MechanicaI Systems Teachine Scheme I Evaluation Scheme](courses/Design%20of%20MechanicaI%20Systems%20Teachine%20Scheme%20I%20Evaluation%20Scheme.md) | — | 1 | B TECH | AY 2013-14 |
| [Design of Mechanical Systems](../subjects/Design%20of%20Mechanical%20Systems/syllabus.md) | [yes](../subjects/Design%20of%20Mechanical%20Systems/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2020-21 |
| [Design of Reinforced Concrete Structures](../subjects/Design%20of%20Reinforced%20Concrete%20Structures/syllabus.md) | [yes](../subjects/Design%20of%20Reinforced%20Concrete%20Structures/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Design of Steel Structures](../subjects/Design%20of%20Steel%20Structures/syllabus.md) | [yes](../subjects/Design%20of%20Steel%20Structures/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2025-26 |
| [Design of Transmission Systems](../subjects/Design%20of%20Transmission%20Systems/syllabus.md) | [yes](../subjects/Design%20of%20Transmission%20Systems/README.md) | 7 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2026-27 |
| [Design Report I](courses/Design%20Report%20I.md) | — | 2 | MBA Tech | 2015-2020 to 2016-2021 |
| [Design Report II](courses/Design%20Report%20II.md) | — | 1 | MBA Tech | 2016-2021 |
| [Design Thinking](../subjects/Design%20Thinking/syllabus.md) | [yes](../subjects/Design%20Thinking/README.md) | 50 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2018-2022 to 2026-2028 |
| [Design Thinking and Innovation](courses/Design%20Thinking%20and%20Innovation.md) | — | 3 | MBA Tech | 2015-2020 to 2016-2021 |
| [Design Thinking and Innovation I](courses/Design%20Thinking%20and%20Innovation%20I.md) | — | 22 | MBA Tech | 2017-2022 to 2020-2025 |
| [Design Thinking and Innovation II](courses/Design%20Thinking%20and%20Innovation%20II.md) | — | 7 | MBA Tech | 2018-2023 to 2020-2025 |
| [DevOps](../subjects/DevOps/syllabus.md) | [yes](../subjects/DevOps/README.md) | 13 | B TECH, B TECH INTEGRATED, MBA Tech, MCA | 2021-2026 to AY 2025-26 |
| [DevSecOps](../subjects/DevSecOps/syllabus.md) | [yes](../subjects/DevSecOps/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Digital - Signal - Processing I](courses/Digital%20-%20Signal%20-%20Processing%20I.md) | — | 2 | B TECH | AY 2013-14 |
| [Digital Capability Model](courses/Digital%20Capability%20Model.md) | — | 8 | MBA Tech | 2018-2023 to 2022-2027 |
| [Digital Circuits and Computer](courses/Digital%20Circuits%20and%20Computer.md) | — | 2 | B TECH WORK IN PROCESS | 2022-2026 |
| [Digital Circuits and Computer Architecture](../subjects/Digital%20Circuits%20and%20Computer%20Architecture/syllabus.md) | [yes](../subjects/Digital%20Circuits%20and%20Computer%20Architecture/README.md) | 3 | B TECH | AY 2023-24 to AY 2026-27 |
| [Digital Circuits and Systems](../subjects/Digital%20Circuits%20and%20Systems/syllabus.md) | [yes](../subjects/Digital%20Circuits%20and%20Systems/README.md) | 2 | B TECH, MBA Tech | 2016-2021 to AY 2017-18 |
| [Digital Communication](../subjects/Digital%20Communication/syllabus.md) | [yes](../subjects/Digital%20Communication/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2019-20 |
| [Digital Communication I](courses/Digital%20Communication%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Digital Design](../subjects/Digital%20Design/syllabus.md) | [yes](../subjects/Digital%20Design/README.md) | 3 | B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2015-2020 |
| [Digital Design I](courses/Digital%20Design%20I.md) | — | 2 | B TECH, MBA Tech | 2012-2017 to AY 2013-14 |
| [Digital Electronics](../subjects/Digital%20Electronics/syllabus.md) | [yes](../subjects/Digital%20Electronics/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to 2019-2023 |
| [Digital Electronics and Microprocessor](courses/Digital%20Electronics%20and%20Microprocessor.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Digital Forensics](../subjects/Digital%20Forensics/syllabus.md) | [yes](../subjects/Digital%20Forensics/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Digital Forensics and Incident Response](../subjects/Digital%20Forensics%20and%20Incident%20Response/syllabus.md) | [yes](../subjects/Digital%20Forensics%20and%20Incident%20Response/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Digital Image and Video Forensics](../subjects/Digital%20Image%20and%20Video%20Forensics/syllabus.md) | [yes](../subjects/Digital%20Image%20and%20Video%20Forensics/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Digital Image Video Processing](courses/Digital%20Image%20Video%20Processing.md) | — | 2 | B TECH | AY 2022-23 to AY 2023-24 |
| [Digital Logic and System Design](courses/Digital%20Logic%20and%20System%20Design.md) | — | 4 | B TECH WORK IN PROCESS | 2018-2022 to 2020-2024 |
| [Digital Logic Design](../subjects/Digital%20Logic%20Design/syllabus.md) | [yes](../subjects/Digital%20Logic%20Design/README.md) | 48 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2009-10 to AY 2025-26 |
| [Digital Logic Design and Analysis](../subjects/Digital%20Logic%20Design%20and%20Analysis/syllabus.md) | [yes](../subjects/Digital%20Logic%20Design%20and%20Analysis/README.md) | 4 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Digital Logic Design Module](courses/Digital%20Logic%20Design%20Module.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Digital Manufacturing Laboratory](courses/Digital%20Manufacturing%20Laboratory.md) | — | 12 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2022-2026 to AY 2024-25 |
| [Digital Marketing](../subjects/Digital%20Marketing/syllabus.md) | [yes](../subjects/Digital%20Marketing/README.md) | 14 | MBA Tech | 2015-2020 to 2022-2027 |
| [Digital Signal and Image Processing](../subjects/Digital%20Signal%20and%20Image%20Processing/syllabus.md) | [yes](../subjects/Digital%20Signal%20and%20Image%20Processing/README.md) | 7 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2025-26 |
| [Digital Signal and Image Processing I](courses/Digital%20Signal%20and%20Image%20Processing%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Digital Signal Processing](../subjects/Digital%20Signal%20Processing/syllabus.md) | [yes](../subjects/Digital%20Signal%20Processing/README.md) | 21 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2020-21 |
| [Digital System Design](../subjects/Digital%20System%20Design/syllabus.md) | [yes](../subjects/Digital%20System%20Design/README.md) | 10 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to 2019-2025 |
| [Digital Techniques](../subjects/Digital%20Techniques/syllabus.md) | [yes](../subjects/Digital%20Techniques/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Digital Television Systems](../subjects/Digital%20Television%20Systems/syllabus.md) | [yes](../subjects/Digital%20Television%20Systems/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to AY 2019-20 |
| [Digital Voice and Broadband Communication](../subjects/Digital%20Voice%20and%20Broadband%20Communication/syllabus.md) | [yes](../subjects/Digital%20Voice%20and%20Broadband%20Communication/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to AY 2024-25 |
| [Digital Voice Communication](../subjects/Digital%20Voice%20Communication/syllabus.md) | [yes](../subjects/Digital%20Voice%20Communication/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2014-15 |
| [Digital Watermarking and Steganography](courses/Digital%20Watermarking%20and%20Steganography.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Disaster Management](../subjects/Disaster%20Management/syllabus.md) | [yes](../subjects/Disaster%20Management/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Discrete Mathematics](../subjects/Discrete%20Mathematics/syllabus.md) | [yes](../subjects/Discrete%20Mathematics/README.md) | 59 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2014-2017 to AY 2026-27 |
| [Discrete Structures](../subjects/Discrete%20Structures/syllabus.md) | [yes](../subjects/Discrete%20Structures/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2018-19 |
| [Discrete Time Signal Processing](../subjects/Discrete%20Time%20Signal%20Processing/syllabus.md) | [yes](../subjects/Discrete%20Time%20Signal%20Processing/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to AY 2025-26 |
| [Distributed Computing](../subjects/Distributed%20Computing/syllabus.md) | [yes](../subjects/Distributed%20Computing/README.md) | 49 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2025-26 |
| [Distributed Computing -rmG%-!](courses/Distributed%20Computing%20-rmG%25-%21.md) | — | 1 | B TECH | AY 2013-14 |
| [Distributed Computing I](courses/Distributed%20Computing%20I.md) | — | 1 | B TECH | — |
| [Distributed Data Processing](../subjects/Distributed%20Data%20Processing/syllabus.md) | [yes](../subjects/Distributed%20Data%20Processing/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Distributed System](../subjects/Distributed%20System/syllabus.md) | [yes](../subjects/Distributed%20System/README.md) | 6 | B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to 2019-2023 |
| [Docks and Harbour Engineering](../subjects/Docks%20and%20Harbour%20Engineering/syllabus.md) | [yes](../subjects/Docks%20and%20Harbour%20Engineering/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [Drone Technology](../subjects/Drone%20Technology/syllabus.md) | [yes](../subjects/Drone%20Technology/README.md) | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2024-25 |
| [Dynamic](courses/Dynamic.md) | — | 1 | MBA Tech | 2018-2023 |
| [Dynamic System Modeling and Analysis](../subjects/Dynamic%20System%20Modeling%20and%20Analysis/syllabus.md) | [yes](../subjects/Dynamic%20System%20Modeling%20and%20Analysis/README.md) | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Dynamic Systems Analysis](../subjects/Dynamic%20Systems%20Analysis/syllabus.md) | [yes](../subjects/Dynamic%20Systems%20Analysis/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Dynamic Systems Modeling](../subjects/Dynamic%20Systems%20Modeling/syllabus.md) | [yes](../subjects/Dynamic%20Systems%20Modeling/README.md) | 27 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Dynamics of Machinery](../subjects/Dynamics%20of%20Machinery/syllabus.md) | [yes](../subjects/Dynamics%20of%20Machinery/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [E-Commerce](../subjects/E-Commerce/syllabus.md) | [yes](../subjects/E-Commerce/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2025-26 |
| [E-Commerce I](courses/E-Commerce%20I.md) | — | 1 | B TECH | — |
| [Earth Retaining Structures](courses/Earth%20Retaining%20Structures.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Earthquake Engineering](../subjects/Earthquake%20Engineering/syllabus.md) | [yes](../subjects/Earthquake%20Engineering/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Ecological Engineering](courses/Ecological%20Engineering.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Ecology and Conservation Practice](courses/Ecology%20and%20Conservation%20Practice.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Economics of Chemical Projects](../subjects/Economics%20of%20Chemical%20Projects/syllabus.md) | [yes](../subjects/Economics%20of%20Chemical%20Projects/README.md) | 3 | MBA Tech | 2014-2019 to 2017-2022 |
| [Edge Computing](../subjects/Edge%20Computing/syllabus.md) | [yes](../subjects/Edge%20Computing/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Electiye I- Project Management](courses/Electiye%20I-%20Project%20Management.md) | — | 1 | B TECH INTEGRATED | 2016-2022 |
| [Electric](courses/Electric.md) | — | 3 | B TECH INTEGRATED, MBA Tech | 2018-2023 to 2019-2024 |
| [Electric and Hybrid Automotive Technology](../subjects/Electric%20and%20Hybrid%20Automotive%20Technology/syllabus.md) | [yes](../subjects/Electric%20and%20Hybrid%20Automotive%20Technology/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Electric and Hybrid Electric](courses/Electric%20and%20Hybrid%20Electric.md) | — | 1 | B TECH | AY 2019-20 |
| [Electric and Hybrid Electric Vehicle Technology](../subjects/Electric%20and%20Hybrid%20Electric%20Vehicle%20Technology/syllabus.md) | [yes](../subjects/Electric%20and%20Hybrid%20Electric%20Vehicle%20Technology/README.md) | 2 | B TECH | AY 2018-19 to AY 2020-21 |
| [Electric Vehicle Technology](courses/Electric%20Vehicle%20Technology.md) | — | 1 | B TECH | AY 2026-27 |
| [Electrical and Computer Workshop](courses/Electrical%20and%20Computer%20Workshop.md) | — | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Electrical and Electronics Workshop](courses/Electrical%20and%20Electronics%20Workshop.md) | — | 13 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2022-2026 to AY 2024-25 |
| [Electrical Drives and Traction](../subjects/Electrical%20Drives%20and%20Traction/syllabus.md) | [yes](../subjects/Electrical%20Drives%20and%20Traction/README.md) | 1 | MBA Tech | 2016-2021 |
| [Electrical Machine II](../subjects/Electrical%20Machine%20II/syllabus.md) | [yes](../subjects/Electrical%20Machine%20II/README.md) | 1 | MBA Tech | 2016-2021 |
| [Electrical Machines I](../subjects/Electrical%20Machines%20I/syllabus.md) | [yes](../subjects/Electrical%20Machines%20I/README.md) | 2 | B TECH, MBA Tech | 2015-2020 to AY 2017-18 |
| [Electrical Network Analvsis and I](courses/Electrical%20Network%20Analvsis%20and%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Electrical Network Analysis and Synthesis](../subjects/Electrical%20Network%20Analysis%20and%20Synthesis/syllabus.md) | [yes](../subjects/Electrical%20Network%20Analysis%20and%20Synthesis/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2018-19 |
| [Electrical Power I](../subjects/Electrical%20Power%20I/syllabus.md) | [yes](../subjects/Electrical%20Power%20I/README.md) | 1 | MBA Tech | 2016-2021 |
| [Electrical System Design](../subjects/Electrical%20System%20Design/syllabus.md) | [yes](../subjects/Electrical%20System%20Design/README.md) | 2 | B TECH | AY 2019-20 to AY 2020-21 |
| [Electrical Technology](../subjects/Electrical%20Technology/syllabus.md) | [yes](../subjects/Electrical%20Technology/README.md) | 5 | B TECH INTEGRATED | 2014-2020 to 2018-2024 |
| [Electro-Mechanical Workshop](courses/Electro-Mechanical%20Workshop.md) | — | 8 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to 2019-2023 |
| [Electromagnetic Field Theory](../subjects/Electromagnetic%20Field%20Theory/syllabus.md) | [yes](../subjects/Electromagnetic%20Field%20Theory/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Electromagnetic Field Theory I](courses/Electromagnetic%20Field%20Theory%20I.md) | — | 2 | B TECH, MBA Tech | 2012-2017 to AY 2013-14 |
| [Electromagnetic Wave Theory](../subjects/Electromagnetic%20Wave%20Theory/syllabus.md) | [yes](../subjects/Electromagnetic%20Wave%20Theory/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2024-25 |
| [Electronic Circuit Analysis and Design](../subjects/Electronic%20Circuit%20Analysis%20and%20Design/syllabus.md) | [yes](../subjects/Electronic%20Circuit%20Analysis%20and%20Design/README.md) | 16 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Electronic Commerce](../subjects/Electronic%20Commerce/syllabus.md) | [yes](../subjects/Electronic%20Commerce/README.md) | 10 | B TECH, B TECH WORK IN PROCESS, MCA | AY 2013-14 to 2021-2024 |
| [Electronic Devices](../subjects/Electronic%20Devices/syllabus.md) | [yes](../subjects/Electronic%20Devices/README.md) | 4 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Electronic Devices and Circuits](../subjects/Electronic%20Devices%20and%20Circuits/syllabus.md) | [yes](../subjects/Electronic%20Devices%20and%20Circuits/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2024-25 |
| [Electronic Instrumentation](../subjects/Electronic%20Instrumentation/syllabus.md) | [yes](../subjects/Electronic%20Instrumentation/README.md) | 1 | B TECH INTEGRATED | 2016-2022 |
| [Electronic Materials and Components](../subjects/Electronic%20Materials%20and%20Components/syllabus.md) | [yes](../subjects/Electronic%20Materials%20and%20Components/README.md) | 11 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Electronic Systems](../subjects/Electronic%20Systems/syllabus.md) | [yes](../subjects/Electronic%20Systems/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Elementary Algebra, Probability](courses/Elementary%20Algebra%2C%20Probability.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Elementary Algebra, Probability and Statistics](../subjects/Elementary%20Algebra%2C%20Probability%20and%20Statistics/syllabus.md) | [yes](../subjects/Elementary%20Algebra%2C%20Probability%20and%20Statistics/README.md) | 1 | B TECH INTEGRATED | 2020-2026 |
| [Elements of Automation](../subjects/Elements%20of%20Automation/syllabus.md) | [yes](../subjects/Elements%20of%20Automation/README.md) | 13 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2025-26 |
| [Elements of Biology](../subjects/Elements%20of%20Biology/syllabus.md) | [yes](../subjects/Elements%20of%20Biology/README.md) | 70 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2015-2019 to AY 2026-27 |
| [Elements of Electrical](courses/Elements%20of%20Electrical.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Elements of Electrical <N Ars](courses/Elements%20of%20Electrical%20-N%20Ars.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Elements of Electrical Engineering](../subjects/Elements%20of%20Electrical%20Engineering/syllabus.md) | [yes](../subjects/Elements%20of%20Electrical%20Engineering/README.md) | 4 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Elements of Mechanical Engineering](../subjects/Elements%20of%20Mechanical%20Engineering/syllabus.md) | [yes](../subjects/Elements%20of%20Mechanical%20Engineering/README.md) | 5 | B TECH INTEGRATED, DIPLOMA | 2020-2026 to 2024-2027 |
| [Elements of Project Management](../subjects/Elements%20of%20Project%20Management/syllabus.md) | [yes](../subjects/Elements%20of%20Project%20Management/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Elliptic Curve Cryptography](courses/Elliptic%20Curve%20Cryptography.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Embedded System Design](../subjects/Embedded%20System%20Design/syllabus.md) | [yes](../subjects/Embedded%20System%20Design/README.md) | 6 | B TECH, MBA Tech | AY 2015-16 to AY 2025-26 |
| [Embedded Systems](../subjects/Embedded%20Systems/syllabus.md) | [yes](../subjects/Embedded%20Systems/README.md) | 39 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Emerging Technologies](courses/Emerging%20Technologies.md) | — | 1 | B TECH INTEGRATED | 2023-2029 |
| [Energy Management](../subjects/Energy%20Management/syllabus.md) | [yes](../subjects/Energy%20Management/README.md) | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Energy Management and Audit](../subjects/Energy%20Management%20and%20Audit/syllabus.md) | [yes](../subjects/Energy%20Management%20and%20Audit/README.md) | 3 | B TECH, MBA Tech | 2015-2020 to AY 2019-20 |
| [Energy Storage](courses/Energy%20Storage.md) | — | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2017-2023 to 2019-2023 |
| [Energy System Design](../subjects/Energy%20System%20Design/syllabus.md) | [yes](../subjects/Energy%20System%20Design/README.md) | 4 | MBA Tech | 2014-2019 to 2017-2022 |
| [Engineerin G Chemis](courses/Engineerin%20G%20Chemis.md) | — | 1 | B TECH INTEGRATED | 2015-2021 |
| [Engineering](courses/Engineering.md) | — | 4 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2019-2025 |
| [Engineering and Solid Mechanics](../subjects/Engineering%20and%20Solid%20Mechanics/syllabus.md) | [yes](../subjects/Engineering%20and%20Solid%20Mechanics/README.md) | 1 | MBA Tech | 2018-2023 |
| [Engineering Chemistry](../subjects/Engineering%20Chemistry/syllabus.md) | [yes](../subjects/Engineering%20Chemistry/README.md) | 25 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Engineering Chemistry Ere](courses/Engineering%20Chemistry%20Ere.md) | — | 1 | B TECH INTEGRATED | 2018-2024 |
| [Engineering Drawing](../subjects/Engineering%20Drawing/syllabus.md) | [yes](../subjects/Engineering%20Drawing/README.md) | 11 | B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2014-2018 to 2025-2028 |
| [Engineering Drawing I](courses/Engineering%20Drawing%20I.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2019-2025 |
| [Engineering Drawing II](courses/Engineering%20Drawing%20II.md) | — | 6 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Engineering Drawing-I Caer Berens](courses/Engineering%20Drawing-I%20Caer%20Berens.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Engineering Drawing-II afadateiCoies Een](courses/Engineering%20Drawing-II%20afadateiCoies%20Een.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Engineering Economics](courses/Engineering%20Economics.md) | — | 5 | B TECH INTEGRATED | 2014-2020 to 2018-2024 |
| [Engineering Economics and Accounting](../subjects/Engineering%20Economics%20and%20Accounting/syllabus.md) | [yes](../subjects/Engineering%20Economics%20and%20Accounting/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2015-16 |
| [Engineering Economics, Costing and Accounting](../subjects/Engineering%20Economics%2C%20Costing%20and%20Accounting/syllabus.md) | [yes](../subjects/Engineering%20Economics%2C%20Costing%20and%20Accounting/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to AY 2020-21 |
| [Engineering Ethics](courses/Engineering%20Ethics.md) | — | 10 | B TECH, MBA Tech | AY 2025-26 to AY 2026-27 |
| [Engineering Geology](../subjects/Engineering%20Geology/syllabus.md) | [yes](../subjects/Engineering%20Geology/README.md) | 10 | B TECH, B TECH INTEGRATED, MBA Tech | 2011-2016 to 2019-2025 |
| [Engineering Graphics](../subjects/Engineering%20Graphics/syllabus.md) | [yes](../subjects/Engineering%20Graphics/README.md) | 4 | B TECH, B TECH INTEGRATED | 2021-2027 to AY 2025-26 |
| [Engineering Graphics and Design](../subjects/Engineering%20Graphics%20and%20Design/syllabus.md) | [yes](../subjects/Engineering%20Graphics%20and%20Design/README.md) | 38 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Engineering Graphics and Design BT-C101004](courses/Engineering%20Graphics%20and%20Design%20BT-C101004.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Engineering Graphics and Design BTCI0100 4, BTMA0100 4](courses/Engineering%20Graphics%20and%20Design%20BTCI0100%204%2C%20BTMA0100%204.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Engineering Materials for Daily Life](courses/Engineering%20Materials%20for%20Daily%20Life.md) | — | 1 | B TECH | AY 2026-27 |
| [Engineering Mathematics](courses/Engineering%20Mathematics.md) | — | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2020-2024 |
| [Engineering Mathematics - [V](courses/Engineering%20Mathematics%20-%20%5BV.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Engineering Mathematics - IIT](courses/Engineering%20Mathematics%20-%20IIT.md) | — | 2 | B TECH WORK IN PROCESS | 2015-2019 to 2019-2023 |
| [Engineering Mathematics I](../subjects/Engineering%20Mathematics%20I/syllabus.md) | [yes](../subjects/Engineering%20Mathematics%20I/README.md) | 20 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Engineering Mathematics II](../subjects/Engineering%20Mathematics%20II/syllabus.md) | [yes](../subjects/Engineering%20Mathematics%20II/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to 2019-2025 |
| [Engineering Mathematics III](../subjects/Engineering%20Mathematics%20III/syllabus.md) | [yes](../subjects/Engineering%20Mathematics%20III/README.md) | 38 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2021-22 |
| [Engineering Mathematics IV](../subjects/Engineering%20Mathematics%20IV/syllabus.md) | [yes](../subjects/Engineering%20Mathematics%20IV/README.md) | 34 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Engineering Mathematics-I11 I](courses/Engineering%20Mathematics-I11%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Engineering Mathematics-II] ~ \|@Ade](courses/Engineering%20Mathematics-II%5D%20~%20-%40Ade.md) | — | 1 | MBA Tech | 2013-2018 |
| [Engineering Mechanics](../subjects/Engineering%20Mechanics/syllabus.md) | [yes](../subjects/Engineering%20Mechanics/README.md) | 42 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2014-2020 to AY 2026-27 |
| [Engineering Mechanics I](../subjects/Engineering%20Mechanics%20I/syllabus.md) | [yes](../subjects/Engineering%20Mechanics%20I/README.md) | 2 | B TECH WORK IN PROCESS | 2013-2017 to 2015-2019 |
| [Engineering Mechanics II](../subjects/Engineering%20Mechanics%20II/syllabus.md) | [yes](../subjects/Engineering%20Mechanics%20II/README.md) | 3 | B TECH WORK IN PROCESS, MBA Tech | 2015-2019 to 2017-2022 |
| [Engineering Metrology and Measurements](../subjects/Engineering%20Metrology%20and%20Measurements/syllabus.md) | [yes](../subjects/Engineering%20Metrology%20and%20Measurements/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Engineering Physics](../subjects/Engineering%20Physics/syllabus.md) | [yes](../subjects/Engineering%20Physics/README.md) | 29 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Engineering Physics I](courses/Engineering%20Physics%20I.md) | — | 2 | B TECH INTEGRATED | 2020-2026 |
| [Engineering Physics II](../subjects/Engineering%20Physics%20II/syllabus.md) | [yes](../subjects/Engineering%20Physics%20II/README.md) | 2 | B TECH INTEGRATED | 2020-2026 |
| [Engineering Thermodynamics](../subjects/Engineering%20Thermodynamics/syllabus.md) | [yes](../subjects/Engineering%20Thermodynamics/README.md) | 30 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2025-26 |
| [Engineering Workshop](courses/Engineering%20Workshop.md) | — | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2026-27 |
| [Engineering Workshop Practice](courses/Engineering%20Workshop%20Practice.md) | — | 2 | DIPLOMA | 2024-2027 to 2025-2028 |
| [English](../subjects/English/syllabus.md) | [yes](../subjects/English/README.md) | 9 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2020-2025 |
| [English Communication](../subjects/English%20Communication/syllabus.md) | [yes](../subjects/English%20Communication/README.md) | 42 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2020-2026 to AY 2026-27 |
| [Enterprise Data Management](courses/Enterprise%20Data%20Management.md) | — | 5 | MBA Tech | 2020-2025 to 2022-2027 |
| [Enterprise Planning System](../subjects/Enterprise%20Planning%20System/syllabus.md) | [yes](../subjects/Enterprise%20Planning%20System/README.md) | 17 | MBA Tech | 2014-2019 to 2022-2027 |
| [Enterprise System](../subjects/Enterprise%20System/syllabus.md) | [yes](../subjects/Enterprise%20System/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2026-27 |
| [Entrepreneurship](courses/Entrepreneurship.md) | — | 18 | B TECH INTEGRATED, MBA Tech | 2014-2019 to 2023-2029 |
| [Entrepreneurship Development](../subjects/Entrepreneurship%20Development/syllabus.md) | [yes](../subjects/Entrepreneurship%20Development/README.md) | 1 | PGDM | — |
| [Entrepreneurship Development and Startups](../subjects/Entrepreneurship%20Development%20and%20Startups/syllabus.md) | [yes](../subjects/Entrepreneurship%20Development%20and%20Startups/README.md) | 4 | DIPLOMA | 2024-2027 |
| [Entrepreneurship Management](../subjects/Entrepreneurship%20Management/syllabus.md) | [yes](../subjects/Entrepreneurship%20Management/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | AY 2014-15 to AY 2019-20 |
| [Environment Management](../subjects/Environment%20Management/syllabus.md) | [yes](../subjects/Environment%20Management/README.md) | 7 | B TECH, MBA Tech | 2014-2019 to AY 2024-25 |
| [Environmental Engineering](../subjects/Environmental%20Engineering/syllabus.md) | [yes](../subjects/Environmental%20Engineering/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2019 to 2020-2025 |
| [Environmental Engineering and Management Systems](../subjects/Environmental%20Engineering%20and%20Management%20Systems/syllabus.md) | [yes](../subjects/Environmental%20Engineering%20and%20Management%20Systems/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2018-19 |
| [Environmental Engineering I](../subjects/Environmental%20Engineering%20I/syllabus.md) | [yes](../subjects/Environmental%20Engineering%20I/README.md) | 2 | B TECH, MBA Tech | 2015-2020 to AY 2019-20 |
| [Environmental Engineering II](../subjects/Environmental%20Engineering%20II/syllabus.md) | [yes](../subjects/Environmental%20Engineering%20II/README.md) | 4 | B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2016-2021 |
| [Environmental Impact](courses/Environmental%20Impact.md) | — | 3 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Environmental Impact Assessment and Auditing](../subjects/Environmental%20Impact%20Assessment%20and%20Auditing/syllabus.md) | [yes](../subjects/Environmental%20Impact%20Assessment%20and%20Auditing/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2013-14 to AY 2026-27 |
| [Environmental Science](courses/Environmental%20Science.md) | — | 57 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2026-27 |
| [Environmental Studies](../subjects/Environmental%20Studies/syllabus.md) | [yes](../subjects/Environmental%20Studies/README.md) | 54 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Ergonomics in Design](../subjects/Ergonomics%20in%20Design/syllabus.md) | [yes](../subjects/Ergonomics%20in%20Design/README.md) | 9 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2026-27 |
| [Essence of Indian Knowledge Tradition](courses/Essence%20of%20Indian%20Knowledge%20Tradition.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Essence of Indian Traditional](courses/Essence%20of%20Indian%20Traditional.md) | — | 2 | B TECH, MBA Tech | 2019-2024 to AY 2020-21 |
| [Essence of Indian Traditional Knowledge](courses/Essence%20of%20Indian%20Traditional%20Knowledge.md) | — | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2023-24 |
| [Essential Electronics Practices](courses/Essential%20Electronics%20Practices.md) | — | 9 | B TECH, MBA Tech | AY 2025-26 to AY 2026-27 |
| [Ethical Hacking](../subjects/Ethical%20Hacking/syllabus.md) | [yes](../subjects/Ethical%20Hacking/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Ethics for IT Organization](courses/Ethics%20for%20IT%20Organization.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2014-15 |
| [Ethics for IT Users](courses/Ethics%20for%20IT%20Users.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2014-15 |
| [Ethics for IT Users and IT Organizations](courses/Ethics%20for%20IT%20Users%20and%20IT%20Organizations.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2016-2020 to AY 2020-21 |
| [Ethics in Data Science](../subjects/Ethics%20in%20Data%20Science/syllabus.md) | [yes](../subjects/Ethics%20in%20Data%20Science/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [ETL-Data Gathering and Loading](../subjects/ETL-Data%20Gathering%20and%20Loading/syllabus.md) | [yes](../subjects/ETL-Data%20Gathering%20and%20Loading/README.md) | 17 | MBA Tech | 2014-2019 to 2022-2027 |
| [Event Driven and UI Programming](../subjects/Event%20Driven%20and%20UI%20Programming/syllabus.md) | [yes](../subjects/Event%20Driven%20and%20UI%20Programming/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Evolutionary Computing](../subjects/Evolutionary%20Computing/syllabus.md) | [yes](../subjects/Evolutionary%20Computing/README.md) | 4 | B TECH | AY 2023-24 to AY 2025-26 |
| [Excel for Engineers](courses/Excel%20for%20Engineers.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Experimental Stress Analysis](courses/Experimental%20Stress%20Analysis.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Facilities Management](../subjects/Facilities%20Management/syllabus.md) | [yes](../subjects/Facilities%20Management/README.md) | 1 | PGDM | AY 2018-19 |
| [Fiber Optic Communication and Networks](../subjects/Fiber%20Optic%20Communication%20and%20Networks/syllabus.md) | [yes](../subjects/Fiber%20Optic%20Communication%20and%20Networks/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2025-26 |
| [Field Visits and Reports II](courses/Field%20Visits%20and%20Reports%20II.md) | — | 2 | PGDM | AY 2016-17 to AY 2018-19 |
| [Film Appreciation](../subjects/Film%20Appreciation/syllabus.md) | [yes](../subjects/Film%20Appreciation/README.md) | 9 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [Finance Analytics](../subjects/Finance%20Analytics/syllabus.md) | [yes](../subjects/Finance%20Analytics/README.md) | 13 | M Tech | 2015-2017 to 2026-2028 |
| [Financial Accounting](../subjects/Financial%20Accounting/syllabus.md) | [yes](../subjects/Financial%20Accounting/README.md) | 13 | MBA Tech, MCA | 2013-2016 to 2019-2022 |
| [Financial Accounting and Analysis](../subjects/Financial%20Accounting%20and%20Analysis/syllabus.md) | [yes](../subjects/Financial%20Accounting%20and%20Analysis/README.md) | 6 | MBA Tech | 2021-2026 to 2023-2028 |
| [Financial Analysis and Working Capital Management](../subjects/Financial%20Analysis%20and%20Working%20Capital%20Management/syllabus.md) | [yes](../subjects/Financial%20Analysis%20and%20Working%20Capital%20Management/README.md) | 25 | MBA Tech | 2016-2021 to 2020-2025 |
| [Financial Analysis and Working Capital Management Cones Rirabie](courses/Financial%20Analysis%20and%20Working%20Capital%20Management%20Cones%20Rirabie.md) | — | 1 | MBA Tech | 2015-2020 |
| [Financial Analytics](../subjects/Financial%20Analytics/syllabus.md) | [yes](../subjects/Financial%20Analytics/README.md) | 16 | MBA Tech | 2014-2019 to 2021-2026 |
| [Financial Analytics using Time](courses/Financial%20Analytics%20using%20Time.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Financial Analytics using Time Series and LSTM](../subjects/Financial%20Analytics%20using%20Time%20Series%20and%20LSTM/syllabus.md) | [yes](../subjects/Financial%20Analytics%20using%20Time%20Series%20and%20LSTM/README.md) | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Financial and Cost Accounting](../subjects/Financial%20and%20Cost%20Accounting/syllabus.md) | [yes](../subjects/Financial%20and%20Cost%20Accounting/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Financial Derivatives](../subjects/Financial%20Derivatives/syllabus.md) | [yes](../subjects/Financial%20Derivatives/README.md) | 4 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Financial Econometrics](courses/Financial%20Econometrics.md) | — | 14 | MBA Tech | 2015-2020 to 2022-2027 |
| [Financial Engineering](../subjects/Financial%20Engineering/syllabus.md) | [yes](../subjects/Financial%20Engineering/README.md) | 16 | MBA Tech | 2014-2019 to 2021-2026 |
| [Financial Engineering and Risk](courses/Financial%20Engineering%20and%20Risk.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Financial Engineering and Risk Management](../subjects/Financial%20Engineering%20and%20Risk%20Management/syllabus.md) | [yes](../subjects/Financial%20Engineering%20and%20Risk%20Management/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2021-22 |
| [Financial Institutions and Markets](../subjects/Financial%20Institutions%20and%20Markets/syllabus.md) | [yes](../subjects/Financial%20Institutions%20and%20Markets/README.md) | 15 | B TECH, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2017-2019 to AY 2021-22 |
| [Financial Institutions, Markets, Instruments and Services](../subjects/Financial%20Institutions%2C%20Markets%2C%20Instruments%20and%20Services/syllabus.md) | [yes](../subjects/Financial%20Institutions%2C%20Markets%2C%20Instruments%20and%20Services/README.md) | 4 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Financial Management](../subjects/Financial%20Management/syllabus.md) | [yes](../subjects/Financial%20Management/README.md) | 33 | B TECH, B TECH WORK IN PROCESS, MBA Tech, PGDM | 2015-2020 to AY 2026-27 |
| [Financial Markets and Risk Analytics](../subjects/Financial%20Markets%20and%20Risk%20Analytics/syllabus.md) | [yes](../subjects/Financial%20Markets%20and%20Risk%20Analytics/README.md) | 4 | M Tech | 2022-2024 to 2023-2025 |
| [Financial Planning and Portfolio Management](../subjects/Financial%20Planning%20and%20Portfolio%20Management/syllabus.md) | [yes](../subjects/Financial%20Planning%20and%20Portfolio%20Management/README.md) | 16 | MBA Tech | 2014-2019 to 2021-2026 |
| [Financial Risk Management](../subjects/Financial%20Risk%20Management/syllabus.md) | [yes](../subjects/Financial%20Risk%20Management/README.md) | 16 | MBA Tech | 2014-2019 to 2021-2026 |
| [Financial Technology](../subjects/Financial%20Technology/syllabus.md) | [yes](../subjects/Financial%20Technology/README.md) | 15 | MBA Tech | 2014-2019 to 2021-2026 |
| [Finite Element Analysis](../subjects/Finite%20Element%20Analysis/syllabus.md) | [yes](../subjects/Finite%20Element%20Analysis/README.md) | 37 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2026-27 |
| [Finite Element Analysis Assessment (Icai](courses/Finite%20Element%20Analysis%20Assessment%20%28Icai.md) | — | 1 | B TECH | AY 2013-14 |
| [Finite Element Analysis in Civil Engineering](../subjects/Finite%20Element%20Analysis%20in%20Civil%20Engineering/syllabus.md) | [yes](../subjects/Finite%20Element%20Analysis%20in%20Civil%20Engineering/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2018 to 2018-2024 |
| [Flexible Manufacturing Systems](../subjects/Flexible%20Manufacturing%20Systems/syllabus.md) | [yes](../subjects/Flexible%20Manufacturing%20Systems/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2015-2019 to AY 2020-21 |
| [Flexible Manufacturing Systems Elective Il)](courses/Flexible%20Manufacturing%20Systems%20Elective%20Il%29.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2017-18 |
| [Fluid Machinery](../subjects/Fluid%20Machinery/syllabus.md) | [yes](../subjects/Fluid%20Machinery/README.md) | 30 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2025-26 |
| [Fluid Mechanics](../subjects/Fluid%20Mechanics/syllabus.md) | [yes](../subjects/Fluid%20Mechanics/README.md) | 46 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2026-27 |
| [Fluid Mechanics and Achiner](courses/Fluid%20Mechanics%20and%20Achiner.md) | — | 1 | B TECH WORK IN PROCESS | 2013-2017 |
| [Fluid Mechanics and Hydraulic Machinery](../subjects/Fluid%20Mechanics%20and%20Hydraulic%20Machinery/syllabus.md) | [yes](../subjects/Fluid%20Mechanics%20and%20Hydraulic%20Machinery/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Fluid Mechanics and Hydraulics](../subjects/Fluid%20Mechanics%20and%20Hydraulics/syllabus.md) | [yes](../subjects/Fluid%20Mechanics%20and%20Hydraulics/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Fluid Mechanics and Machinery](../subjects/Fluid%20Mechanics%20and%20Machinery/syllabus.md) | [yes](../subjects/Fluid%20Mechanics%20and%20Machinery/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2014-2018 to 2019-2023 |
| [Fluid Mechanics I](../subjects/Fluid%20Mechanics%20I/syllabus.md) | [yes](../subjects/Fluid%20Mechanics%20I/README.md) | 6 | B TECH INTEGRATED, MBA Tech | 2015-2021 to 2018-2024 |
| [Fluid Mechanics II](../subjects/Fluid%20Mechanics%20II/syllabus.md) | [yes](../subjects/Fluid%20Mechanics%20II/README.md) | 3 | B TECH INTEGRATED, MBA Tech | 2016-2021 to 2017-2023 |
| [Fluid Power Automation](../subjects/Fluid%20Power%20Automation/syllabus.md) | [yes](../subjects/Fluid%20Power%20Automation/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2025-26 |
| [Fluidization Engineering](courses/Fluidization%20Engineering.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Food Processing](../subjects/Food%20Processing/syllabus.md) | [yes](../subjects/Food%20Processing/README.md) | 3 | MBA Tech | 2014-2019 to 2017-2022 |
| [Food Processing and Technology](../subjects/Food%20Processing%20and%20Technology/syllabus.md) | [yes](../subjects/Food%20Processing%20and%20Technology/README.md) | 3 | MBA Tech | 2018-2023 to 2020-2025 |
| [Forecasting Analytics](courses/Forecasting%20Analytics.md) | — | 2 | MBA Tech | 2021-2026 |
| [Foreign Language - Chinese](courses/Foreign%20Language%20-%20Chinese.md) | — | 11 | MBA Tech | 2014-2019 to 2020-2025 |
| [Foreign Language- German](courses/Foreign%20Language-%20German.md) | — | 11 | MBA Tech | 2014-2019 to 2020-2025 |
| [Foreign Language- Spanish](courses/Foreign%20Language-%20Spanish.md) | — | 11 | MBA Tech | 2014-2019 to 2020-2025 |
| [Forensic Geotechnical Engineering](courses/Forensic%20Geotechnical%20Engineering.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Formal Language and Automata Theory](../subjects/Formal%20Language%20and%20Automata%20Theory/syllabus.md) | [yes](../subjects/Formal%20Language%20and%20Automata%20Theory/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2024 to AY 2025-26 |
| [Foundation Engineering](../subjects/Foundation%20Engineering/syllabus.md) | [yes](../subjects/Foundation%20Engineering/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Foundation of Information Systems](courses/Foundation%20of%20Information%20Systems.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Foundations](courses/Foundations.md) | — | 1 | B TECH | AY 2021-22 |
| [Foundations of Business](../subjects/Foundations%20of%20Business/syllabus.md) | [yes](../subjects/Foundations%20of%20Business/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Foundations of Entrepreneurship](../subjects/Foundations%20of%20Entrepreneurship/syllabus.md) | [yes](../subjects/Foundations%20of%20Entrepreneurship/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2024-25 |
| [Foundations of Information Theory for AI](courses/Foundations%20of%20Information%20Theory%20for%20AI.md) | — | 2 | B TECH, MBA Tech | 2025-2030 to AY 2026-27 |
| [Foundations of Machine Learning](../subjects/Foundations%20of%20Machine%20Learning/syllabus.md) | [yes](../subjects/Foundations%20of%20Machine%20Learning/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Free and Open Source Softwares- Lab](courses/Free%20and%20Open%20Source%20Softwares-%20Lab.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [French](../subjects/French/syllabus.md) | [yes](../subjects/French/README.md) | 1 | B TECH | AY 2024-25 |
| [Fundamentals of Accounting](../subjects/Fundamentals%20of%20Accounting/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Accounting/README.md) | 7 | MBA Tech | 2019-2024 to 2020-2025 |
| [Fundamentals of Automation](courses/Fundamentals%20of%20Automation.md) | — | 2 | B TECH, B TECH INTEGRATED | 2023-2029 to AY 2026-27 |
| [Fundamentals of Blockchain](../subjects/Fundamentals%20of%20Blockchain/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Blockchain/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Fundamentals of Calculus and Vector Algebra](../subjects/Fundamentals%20of%20Calculus%20and%20Vector%20Algebra/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Calculus%20and%20Vector%20Algebra/README.md) | 2 | B TECH INTEGRATED | 2020-2026 |
| [Fundamentals of Climate Change](../subjects/Fundamentals%20of%20Climate%20Change/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Climate%20Change/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Fundamentals of Computer Networks](courses/Fundamentals%20of%20Computer%20Networks.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Fundamentals of Computer Networks Module](courses/Fundamentals%20of%20Computer%20Networks%20Module.md) | — | 1 | B TECH INTEGRATED | 2018-2024 |
| [Fundamentals of Computer Science](../subjects/Fundamentals%20of%20Computer%20Science/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Computer%20Science/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2023-24 |
| [Fundamentals of Digital Transformation](../subjects/Fundamentals%20of%20Digital%20Transformation/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Digital%20Transformation/README.md) | 7 | B TECH, MBA Tech | 2018-2023 to AY 2024-25 |
| [Fundamentals of E-Commerce](../subjects/Fundamentals%20of%20E-Commerce/syllabus.md) | [yes](../subjects/Fundamentals%20of%20E-Commerce/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Fundamentals of Economics](../subjects/Fundamentals%20of%20Economics/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Economics/README.md) | 8 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2023-24 |
| [Fundamentals of Engineering](courses/Fundamentals%20of%20Engineering.md) | — | 1 | B TECH INTEGRATED | 2018-2024 |
| [Fundamentals of Engineering Design](../subjects/Fundamentals%20of%20Engineering%20Design/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Engineering%20Design/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Fundamentals of Engineering Mechanics](../subjects/Fundamentals%20of%20Engineering%20Mechanics/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Engineering%20Mechanics/README.md) | 4 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Fundamentals of Fuels and Lubricants](../subjects/Fundamentals%20of%20Fuels%20and%20Lubricants/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Fuels%20and%20Lubricants/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2021-22 to AY 2024-25 |
| [Fundamentals of Machine Learning](../subjects/Fundamentals%20of%20Machine%20Learning/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Machine%20Learning/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Fundamentals of Management](../subjects/Fundamentals%20of%20Management/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Management/README.md) | 7 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Fundamentals of Mechanics-Statics](../subjects/Fundamentals%20of%20Mechanics-Statics/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Mechanics-Statics/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Fundamentals of Microwave 1 Engineering](courses/Fundamentals%20of%20Microwave%201%20Engineering.md) | — | 2 | B TECH, MBA Tech | 2011-2016 to AY 2013-14 |
| [Fundamentals of Microwave En: Ineering](courses/Fundamentals%20of%20Microwave%20En-%20Ineering.md) | — | 1 | MBA Tech | 2015-2020 |
| [Fundamentals of Microwave Engineering](../subjects/Fundamentals%20of%20Microwave%20Engineering/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Microwave%20Engineering/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2019-20 |
| [Fundamentals of Operating Systems](../subjects/Fundamentals%20of%20Operating%20Systems/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Operating%20Systems/README.md) | 4 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2027 to AY 2026-27 |
| [Fundamentals of Physics](../subjects/Fundamentals%20of%20Physics/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Physics/README.md) | 2 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2023 to 2020-2026 |
| [Fundamentals of Structural Analysis](../subjects/Fundamentals%20of%20Structural%20Analysis/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Structural%20Analysis/README.md) | 4 | B TECH INTEGRATED | 2015-2021 to 2018-2024 |
| [Fundamentals of Web Technology](../subjects/Fundamentals%20of%20Web%20Technology/syllabus.md) | [yes](../subjects/Fundamentals%20of%20Web%20Technology/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2017-2023 |
| [Fundamentals of Website Designing](courses/Fundamentals%20of%20Website%20Designing.md) | — | 6 | B TECH INTEGRATED | 2018-2024 to 2023-2029 |
| [Fundamentals of Website Designing Module](courses/Fundamentals%20of%20Website%20Designing%20Module.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Fundamentalsof Web Technology I](courses/Fundamentalsof%20Web%20Technology%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Fuzzy Logic and](courses/Fuzzy%20Logic%20and.md) | — | 1 | B TECH | AY 2013-14 |
| [Fuzzy Logic and Neural Networks](../subjects/Fuzzy%20Logic%20and%20Neural%20Networks/syllabus.md) | [yes](../subjects/Fuzzy%20Logic%20and%20Neural%20Networks/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [Fuzzy Logicand Neural Networks](courses/Fuzzy%20Logicand%20Neural%20Networks.md) | — | 1 | B TECH WORK IN PROCESS | 2014-2018 |
| [Game Design](../subjects/Game%20Design/syllabus.md) | [yes](../subjects/Game%20Design/README.md) | 14 | B TECH, B TECH WORK IN PROCESS, MBA Tech, MCA | 2018-2022 to AY 2026-27 |
| [Gender Communication](../subjects/Gender%20Communication/syllabus.md) | [yes](../subjects/Gender%20Communication/README.md) | 4 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [Generative Adversarial Networks](../subjects/Generative%20Adversarial%20Networks/syllabus.md) | [yes](../subjects/Generative%20Adversarial%20Networks/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Generative AI](../subjects/Generative%20AI/syllabus.md) | [yes](../subjects/Generative%20AI/README.md) | 6 | B TECH, M Tech, MBA Tech | 2022-2027 to AY 2026-27 |
| [Generative AI for Business](../subjects/Generative%20AI%20for%20Business/syllabus.md) | [yes](../subjects/Generative%20AI%20for%20Business/README.md) | 2 | MBA Tech | 2021-2026 |
| [Generative AI with Large Language Models](../subjects/Generative%20AI%20with%20Large%20Language%20Models/syllabus.md) | [yes](../subjects/Generative%20AI%20with%20Large%20Language%20Models/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Geographical Information System](../subjects/Geographical%20Information%20System/syllabus.md) | [yes](../subjects/Geographical%20Information%20System/README.md) | 1 | B TECH | — |
| [Geographiml Information %Stem I CodcBTCOOSoll](courses/Geographiml%20Information%20%25Stem%20I%20CodcBTCOOSoll.md) | — | 1 | B TECH | — |
| [Geology](../subjects/Geology/syllabus.md) | [yes](../subjects/Geology/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Geotechnical Earthquake Engineering](courses/Geotechnical%20Earthquake%20Engineering.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | AY 2013-14 to 2019-2024 |
| [Geotechnical Engineering](courses/Geotechnical%20Engineering.md) | — | 3 | B TECH, B TECH INTEGRATED | 2017-2023 to AY 2019-20 |
| [Geotechnical Engineering I](../subjects/Geotechnical%20Engineering%20I/syllabus.md) | [yes](../subjects/Geotechnical%20Engineering%20I/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2017-2023 |
| [Geotechnical Engineering II](../subjects/Geotechnical%20Engineering%20II/syllabus.md) | [yes](../subjects/Geotechnical%20Engineering%20II/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2018-2024 |
| [German](../subjects/German/syllabus.md) | [yes](../subjects/German/README.md) | 8 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [GIS and Remote Sensing](courses/GIS%20and%20Remote%20Sensing.md) | — | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2018 to AY 2020-21 |
| [Git and Cuda Programming](courses/Git%20and%20Cuda%20Programming.md) | — | 2 | B TECH, MBA Tech | 2025-2030 to AY 2026-27 |
| [Global Navigation Satellite Systems](../subjects/Global%20Navigation%20Satellite%20Systems/syllabus.md) | [yes](../subjects/Global%20Navigation%20Satellite%20Systems/README.md) | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Global Supply Chain Management](../subjects/Global%20Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Global%20Supply%20Chain%20Management/README.md) | 2 | MBA Tech | 2021-2026 |
| [Global Trends in Infrastructure Management](../subjects/Global%20Trends%20in%20Infrastructure%20Management/syllabus.md) | [yes](../subjects/Global%20Trends%20in%20Infrastructure%20Management/README.md) | 16 | MBA Tech | 2014-2019 to 2021-2026 |
| [Graphology for Personal Development](../subjects/Graphology%20for%20Personal%20Development/syllabus.md) | [yes](../subjects/Graphology%20for%20Personal%20Development/README.md) | 3 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Green and Intelligent Buildings](../subjects/Green%20and%20Intelligent%20Buildings/syllabus.md) | [yes](../subjects/Green%20and%20Intelligent%20Buildings/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2018 to AY 2026-27 |
| [Ground Improvement Techniques](courses/Ground%20Improvement%20Techniques.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [H (Green and Intelligent Buildings)](courses/H%20%28Green%20and%20Intelligent%20Buildings%29.md) | — | 1 | B TECH WORK IN PROCESS | 2013-2017 |
| [Happiness at Work](../subjects/Happiness%20at%20Work/syllabus.md) | [yes](../subjects/Happiness%20at%20Work/README.md) | 1 | B TECH | AY 2024-25 |
| [Health and Safety](courses/Health%20and%20Safety.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to 2019-2025 |
| [Heat Flow Analysis](courses/Heat%20Flow%20Analysis.md) | — | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Heat Transfer](../subjects/Heat%20Transfer/syllabus.md) | [yes](../subjects/Heat%20Transfer/README.md) | 31 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Heat Transfer Operations](../subjects/Heat%20Transfer%20Operations/syllabus.md) | [yes](../subjects/Heat%20Transfer%20Operations/README.md) | 3 | MBA Tech | 2016-2021 to 2018-2023 |
| [High Performance Computing](../subjects/High%20Performance%20Computing/syllabus.md) | [yes](../subjects/High%20Performance%20Computing/README.md) | 2 | MCA | 2020-2023 to 2021-2024 |
| [High Speed Networking Architecture and Protocols](courses/High%20Speed%20Networking%20Architecture%20and%20Protocols.md) | — | 7 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [High Voltage Engineering](../subjects/High%20Voltage%20Engineering/syllabus.md) | [yes](../subjects/High%20Voltage%20Engineering/README.md) | 2 | B TECH | AY 2019-20 to AY 2020-21 |
| [Highway and Railway Engineering](../subjects/Highway%20and%20Railway%20Engineering/syllabus.md) | [yes](../subjects/Highway%20and%20Railway%20Engineering/README.md) | 5 | B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2016-2021 |
| [HRD and Professional Ethics](../subjects/HRD%20and%20Professional%20Ethics/syllabus.md) | [yes](../subjects/HRD%20and%20Professional%20Ethics/README.md) | 1 | PGDM | AY 2018-19 |
| [Human and Legal Aspects of Cybersecurity](../subjects/Human%20and%20Legal%20Aspects%20of%20Cybersecurity/syllabus.md) | [yes](../subjects/Human%20and%20Legal%20Aspects%20of%20Cybersecurity/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Human Centered Cyber Security](../subjects/Human%20Centered%20Cyber%20Security/syllabus.md) | [yes](../subjects/Human%20Centered%20Cyber%20Security/README.md) | 6 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2026-27 |
| [Human Computer Interaction](../subjects/Human%20Computer%20Interaction/syllabus.md) | [yes](../subjects/Human%20Computer%20Interaction/README.md) | 36 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, Current electives 2026-27, MBA Tech, MCA | 2014-2017 to AY 2026-27 |
| [Human Computer Interface](../subjects/Human%20Computer%20Interface/syllabus.md) | [yes](../subjects/Human%20Computer%20Interface/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2024 |
| [Human Computer Interface(HC1) I](courses/Human%20Computer%20Interface%28HC1%29%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Human Machine Interface](../subjects/Human%20Machine%20Interface/syllabus.md) | [yes](../subjects/Human%20Machine%20Interface/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Human Machine Interface and Data Acquisition](../subjects/Human%20Machine%20Interface%20and%20Data%20Acquisition/syllabus.md) | [yes](../subjects/Human%20Machine%20Interface%20and%20Data%20Acquisition/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2022 |
| [Human Resource Analytics](courses/Human%20Resource%20Analytics.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Human Resource Management](../subjects/Human%20Resource%20Management/syllabus.md) | [yes](../subjects/Human%20Resource%20Management/README.md) | 16 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2015-2020 to AY 2026-27 |
| [Human Resource Management Module'](courses/Human%20Resource%20Management%20Module%27.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Human Resources Management in Construction](courses/Human%20Resources%20Management%20in%20Construction.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to 2019-2025 |
| [Hydraulic and Pneumatic Systems](../subjects/Hydraulic%20and%20Pneumatic%20Systems/syllabus.md) | [yes](../subjects/Hydraulic%20and%20Pneumatic%20Systems/README.md) | 16 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Hydraulic Engineering](../subjects/Hydraulic%20Engineering/syllabus.md) | [yes](../subjects/Hydraulic%20Engineering/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2018-2024 |
| [Hydraulic Machinery](../subjects/Hydraulic%20Machinery/syllabus.md) | [yes](../subjects/Hydraulic%20Machinery/README.md) | 3 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2016-2020 to AY 2019-20 |
| [Hydraulics and Fluid Machinery](../subjects/Hydraulics%20and%20Fluid%20Machinery/syllabus.md) | [yes](../subjects/Hydraulics%20and%20Fluid%20Machinery/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Hydrogeology and Groundwater Modelling](../subjects/Hydrogeology%20and%20Groundwater%20Modelling/syllabus.md) | [yes](../subjects/Hydrogeology%20and%20Groundwater%20Modelling/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [I C Engines](../subjects/I%20C%20Engines/syllabus.md) | [yes](../subjects/I%20C%20Engines/README.md) | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2019-20 |
| [I Presentation 7 and Communication I Techiqnues](courses/I%20Presentation%207%20and%20Communication%20I%20Techiqnues.md) | — | 1 | B TECH | AY 2013-14 |
| [I1 - Rapid](courses/I1%20-%20Rapid.md) | — | 1 | B TECH | AY 2013-14 |
| [ICT for Development](courses/ICT%20for%20Development.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [If (Urban Transportation Systems Planning)](courses/If%20%28Urban%20Transportation%20Systems%20Planning%29.md) | — | 1 | B TECH WORK IN PROCESS | 2014-2018 |
| [III (Structural Dynamics)](courses/III%20%28Structural%20Dynamics%29.md) | — | 2 | B TECH | AY 2015-16 to AY 2020-21 |
| [Image and Signal Processing](../subjects/Image%20and%20Signal%20Processing/syllabus.md) | [yes](../subjects/Image%20and%20Signal%20Processing/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Image and Video Analysis](courses/Image%20and%20Video%20Analysis.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Image and Video Processing](../subjects/Image%20and%20Video%20Processing/syllabus.md) | [yes](../subjects/Image%20and%20Video%20Processing/README.md) | 35 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to AY 2026-27 |
| [Image Processing](../subjects/Image%20Processing/syllabus.md) | [yes](../subjects/Image%20Processing/README.md) | 32 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2011-2016 to 2021-2024 |
| [Image Processing and Pattern](courses/Image%20Processing%20and%20Pattern.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Image Processing I](courses/Image%20Processing%20I.md) | — | 2 | B TECH | AY 2013-14 |
| [Implementation of Technology](courses/Implementation%20of%20Technology.md) | — | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Implementation of Technology I](courses/Implementation%20of%20Technology%20I.md) | — | 5 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | AY 2013-14 to AY 2018-19 |
| [Implementation of Technology II](courses/Implementation%20of%20Technology%20II.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2016-2022 |
| [In- Phase I](courses/In-%20Phase%20I.md) | — | 1 | B TECH INTEGRATED | 2017-2023 |
| [In-Plant Training Phase](courses/In-Plant%20Training%20Phase.md) | — | 1 | B TECH INTEGRATED | 2015-2021 |
| [In-Plant Training Phase I](courses/In-Plant%20Training%20Phase%20I.md) | — | 17 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [In-Plant Training Phase II](courses/In-Plant%20Training%20Phase%20II.md) | — | 21 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Indian Constitution](courses/Indian%20Constitution.md) | — | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2021-22 |
| [Indian Financial System](../subjects/Indian%20Financial%20System/syllabus.md) | [yes](../subjects/Indian%20Financial%20System/README.md) | 15 | MBA Tech | 2014-2019 to 2021-2026 |
| [Indian Knowledge System](../subjects/Indian%20Knowledge%20System/syllabus.md) | [yes](../subjects/Indian%20Knowledge%20System/README.md) | 8 | B TECH, MBA Tech | AY 2025-26 to AY 2026-27 |
| [Industrial Applications of HVAC](courses/Industrial%20Applications%20of%20HVAC.md) | — | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2025-26 |
| [Industrial Automation](../subjects/Industrial%20Automation/syllabus.md) | [yes](../subjects/Industrial%20Automation/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Industrial Automation and Robotics](../subjects/Industrial%20Automation%20and%20Robotics/syllabus.md) | [yes](../subjects/Industrial%20Automation%20and%20Robotics/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2026-27 |
| [Industrial Data Communication](../subjects/Industrial%20Data%20Communication/syllabus.md) | [yes](../subjects/Industrial%20Data%20Communication/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2025-26 |
| [Industrial Drives](../subjects/Industrial%20Drives/syllabus.md) | [yes](../subjects/Industrial%20Drives/README.md) | 9 | B TECH, B TECH WORK IN PROCESS | 2014-2018 to AY 2025-26 |
| [Industrial Economics and 1 Management](courses/Industrial%20Economics%20and%201%20Management.md) | — | 2 | B TECH | AY 2013-14 |
| [Industrial Economics and Management](../subjects/Industrial%20Economics%20and%20Management/syllabus.md) | [yes](../subjects/Industrial%20Economics%20and%20Management/README.md) | 27 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MCA | 2013-2016 to 2022-2024 |
| [Industrial Electronics](../subjects/Industrial%20Electronics/syllabus.md) | [yes](../subjects/Industrial%20Electronics/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Industrial Electronics and Applications](courses/Industrial%20Electronics%20and%20Applications.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2015-16 |
| [Industrial Electronics and Drives](courses/Industrial%20Electronics%20and%20Drives.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Industrial Electronics I](courses/Industrial%20Electronics%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Industrial Engineering](../subjects/Industrial%20Engineering/syllabus.md) | [yes](../subjects/Industrial%20Engineering/README.md) | 41 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2025-26 |
| [Industrial Engineering and Ergonomics](../subjects/Industrial%20Engineering%20and%20Ergonomics/syllabus.md) | [yes](../subjects/Industrial%20Engineering%20and%20Ergonomics/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Industrial Engineering and Quality Management](../subjects/Industrial%20Engineering%20and%20Quality%20Management/syllabus.md) | [yes](../subjects/Industrial%20Engineering%20and%20Quality%20Management/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2022 |
| [Industrial Ergonomics](courses/Industrial%20Ergonomics.md) | — | 1 | B TECH | AY 2026-27 |
| [Industrial Internship with Project](courses/Industrial%20Internship%20with%20Project.md) | — | 2 | M Tech | 2024-2026 to 2025-2027 |
| [Industrial IoT](../subjects/Industrial%20IoT/syllabus.md) | [yes](../subjects/Industrial%20IoT/README.md) | 4 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2022-23 |
| [Industrial IoT Markets and Project Planning](../subjects/Industrial%20IoT%20Markets%20and%20Project%20Planning/syllabus.md) | [yes](../subjects/Industrial%20IoT%20Markets%20and%20Project%20Planning/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Industrial loT Markets and Project Planning](courses/Industrial%20loT%20Markets%20and%20Project%20Planning.md) | — | 1 | MBA Tech | 2018-2023 |
| [Industrial Marketing](../subjects/Industrial%20Marketing/syllabus.md) | [yes](../subjects/Industrial%20Marketing/README.md) | 4 | MBA Tech | 2015-2020 to 2016-2021 |
| [Industrial Psychology](../subjects/Industrial%20Psychology/syllabus.md) | [yes](../subjects/Industrial%20Psychology/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2026-27 |
| [Industrial Relations and Peace Studies](../subjects/Industrial%20Relations%20and%20Peace%20Studies/syllabus.md) | [yes](../subjects/Industrial%20Relations%20and%20Peace%20Studies/README.md) | 4 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [Industrial Robotics](../subjects/Industrial%20Robotics/syllabus.md) | [yes](../subjects/Industrial%20Robotics/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [Industrial Robotics and Control](../subjects/Industrial%20Robotics%20and%20Control/syllabus.md) | [yes](../subjects/Industrial%20Robotics%20and%20Control/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2022 |
| [Industrial Robotics and Motion Control](../subjects/Industrial%20Robotics%20and%20Motion%20Control/syllabus.md) | [yes](../subjects/Industrial%20Robotics%20and%20Motion%20Control/README.md) | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Industrial Safety](../subjects/Industrial%20Safety/syllabus.md) | [yes](../subjects/Industrial%20Safety/README.md) | 5 | MBA Tech | 2015-2020 to 2020-2025 |
| [Industrial Waste Management](../subjects/Industrial%20Waste%20Management/syllabus.md) | [yes](../subjects/Industrial%20Waste%20Management/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [Industrial Waste Treatment](../subjects/Industrial%20Waste%20Treatment/syllabus.md) | [yes](../subjects/Industrial%20Waste%20Treatment/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [Industrial Waste Treatment and Management](courses/Industrial%20Waste%20Treatment%20and%20Management.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Industry 4.0](courses/Industry%204.0.md) | — | 14 | MBA Tech | 2015-2020 to 2021-2026 |
| [Industry Internship and Project](courses/Industry%20Internship%20and%20Project.md) | — | 7 | MCA | 2014-2017 to 2019-2022 |
| [Information Security](../subjects/Information%20Security/syllabus.md) | [yes](../subjects/Information%20Security/README.md) | 18 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2025-26 |
| [Information Security and Privacy](../subjects/Information%20Security%20and%20Privacy/syllabus.md) | [yes](../subjects/Information%20Security%20and%20Privacy/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Information Security Assurance and](courses/Information%20Security%20Assurance%20and.md) | — | 1 | B TECH WORK IN PROCESS | 2016-2020 |
| [Information Security Assurance and Forensics](courses/Information%20Security%20Assurance%20and%20Forensics.md) | — | 6 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [Information Storage and Management](../subjects/Information%20Storage%20and%20Management/syllabus.md) | [yes](../subjects/Information%20Storage%20and%20Management/README.md) | 30 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to 2021-2024 |
| [Information Storage and Management Elective - I I](courses/Information%20Storage%20and%20Management%20Elective%20-%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Information Storageand Management](courses/Information%20Storageand%20Management.md) | — | 1 | B TECH | — |
| [Information Storaqe - and Management I](courses/Information%20Storaqe%20-%20and%20Management%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Information System Management](../subjects/Information%20System%20Management/syllabus.md) | [yes](../subjects/Information%20System%20Management/README.md) | 36 | MBA Tech | 2015-2020 to 2022-2027 |
| [Information Systems Audit](../subjects/Information%20Systems%20Audit/syllabus.md) | [yes](../subjects/Information%20Systems%20Audit/README.md) | 6 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2026-27 |
| [Information Systems Security](../subjects/Information%20Systems%20Security/syllabus.md) | [yes](../subjects/Information%20Systems%20Security/README.md) | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2026 to AY 2025-26 |
| [Information Theory and Coding](../subjects/Information%20Theory%20and%20Coding/syllabus.md) | [yes](../subjects/Information%20Theory%20and%20Coding/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2025-26 |
| [Infrastructure Finance](courses/Infrastructure%20Finance.md) | — | 3 | MBA Tech | 2014-2019 to 2015-2020 |
| [Infrastructure Management](courses/Infrastructure%20Management.md) | — | 1 | MBA Tech | 2014-2019 |
| [Infrastructure Management in Industry Sector Energy, Transportation and Real Estate](courses/Infrastructure%20Management%20in%20Industry%20Sector%20Energy%2C%20Transportation%20and%20Real%20Est.md) | — | 2 | MBA Tech | 2015-2020 |
| [Inorganic Process Technologies](../subjects/Inorganic%20Process%20Technologies/syllabus.md) | [yes](../subjects/Inorganic%20Process%20Technologies/README.md) | 3 | MBA Tech | 2018-2023 to 2020-2025 |
| [Instrumentation](../subjects/Instrumentation/syllabus.md) | [yes](../subjects/Instrumentation/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to AY 2019-20 |
| [Instrumentation and Process Control](../subjects/Instrumentation%20and%20Process%20Control/syllabus.md) | [yes](../subjects/Instrumentation%20and%20Process%20Control/README.md) | 5 | MBA Tech | 2015-2020 to 2020-2025 |
| [Instrumentation I](courses/Instrumentation%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Integral Transforms](../subjects/Integral%20Transforms/syllabus.md) | [yes](../subjects/Integral%20Transforms/README.md) | 8 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2024-25 |
| [Integrated Humanities](courses/Integrated%20Humanities.md) | — | 1 | Ph D | 2025-2026 |
| [Integrated Marketing Communication](../subjects/Integrated%20Marketing%20Communication/syllabus.md) | [yes](../subjects/Integrated%20Marketing%20Communication/README.md) | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Integrated Marketing Communication Module Codd](courses/Integrated%20Marketing%20Communication%20Module%20Codd.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Intelligence of Biological](courses/Intelligence%20of%20Biological.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Intelligence of Biological Systems](courses/Intelligence%20of%20Biological%20Systems.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2021-22 |
| [Intelligent Systems](../subjects/Intelligent%20Systems/syllabus.md) | [yes](../subjects/Intelligent%20Systems/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2015-16 |
| [Intelligent Systems I](../subjects/Intelligent%20Systems%20I/syllabus.md) | [yes](../subjects/Intelligent%20Systems%20I/README.md) | 5 | B TECH, MBA Tech | 2021-2026 to AY 2025-26 |
| [Intelligent Systems II](../subjects/Intelligent%20Systems%20II/syllabus.md) | [yes](../subjects/Intelligent%20Systems%20II/README.md) | 4 | B TECH | AY 2023-24 to AY 2026-27 |
| [Interior Design](../subjects/Interior%20Design/syllabus.md) | [yes](../subjects/Interior%20Design/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2025 to AY 2025-26 |
| [Internal Combustion Engines](courses/Internal%20Combustion%20Engines.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [International Finance](../subjects/International%20Finance/syllabus.md) | [yes](../subjects/International%20Finance/README.md) | 15 | MBA Tech | 2014-2019 to 2021-2026 |
| [International Marketing](../subjects/International%20Marketing/syllabus.md) | [yes](../subjects/International%20Marketing/README.md) | 15 | MBA Tech | 2014-2019 to 2021-2026 |
| [Internet of Things](../subjects/Internet%20of%20Things/syllabus.md) | [yes](../subjects/Internet%20of%20Things/README.md) | 36 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, Current electives 2026-27, MBA Tech, MCA | 2013-2017 to AY 2025-26 |
| [Internet of Things (Department](courses/Internet%20of%20Things%20%28Department.md) | — | 4 | MCA | 2022-2024 to 2025-2027 |
| [Internet of Things Analytics](../subjects/Internet%20of%20Things%20Analytics/syllabus.md) | [yes](../subjects/Internet%20of%20Things%20Analytics/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Internship](courses/Internship.md) | — | 5 | DIPLOMA, PGDM | AY 2018-19 to 2024-2027 |
| [Internship/ Project](courses/Internship-%20Project.md) | — | 9 | M Tech | 2018-2020 to 2023-2025 |
| [Interpersonal Skills](courses/Interpersonal%20Skills.md) | — | 38 | B TECH, B TECH INTEGRATED, MBA Tech, MCA | 2020-2026 to AY 2026-27 |
| [Introduction](courses/Introduction.md) | — | 2 | B TECH | AY 2020-21 to AY 2021-22 |
| [Introduction to 3D Printing Technology](../subjects/Introduction%20to%203D%20Printing%20Technology/syllabus.md) | [yes](../subjects/Introduction%20to%203D%20Printing%20Technology/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Introduction to App Development](../subjects/Introduction%20to%20App%20Development/syllabus.md) | [yes](../subjects/Introduction%20to%20App%20Development/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Introduction to Automation](../subjects/Introduction%20to%20Automation/syllabus.md) | [yes](../subjects/Introduction%20to%20Automation/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2020-21 |
| [Introduction to Blockchain](../subjects/Introduction%20to%20Blockchain/syllabus.md) | [yes](../subjects/Introduction%20to%20Blockchain/README.md) | 10 | B TECH, MBA Tech | 2015-2020 to AY 2023-24 |
| [Introduction to Blockchain (Open](courses/Introduction%20to%20Blockchain%20%28Open.md) | — | 4 | B TECH, MBA Tech | 2018-2023 to AY 2021-22 |
| [Introduction to Business](courses/Introduction%20to%20Business.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2021-22 |
| [Introduction to Business Analytics and Business Intelligence](../subjects/Introduction%20to%20Business%20Analytics%20and%20Business%20Intelligence/syllabus.md) | [yes](../subjects/Introduction%20to%20Business%20Analytics%20and%20Business%20Intelligence/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Introduction to Business Statistics](courses/Introduction%20to%20Business%20Statistics.md) | — | 2 | B TECH, B TECH WORK IN PROCESS | 2022-2026 to AY 2024-25 |
| [Introduction to Business Statistics, Analytics and Modeling II](../subjects/Introduction%20to%20Business%20Statistics%2C%20Analytics%20and%20Modeling%20II/syllabus.md) | [yes](../subjects/Introduction%20to%20Business%20Statistics%2C%20Analytics%20and%20Modeling%20II/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2024-25 |
| [Introduction to Chemistry](../subjects/Introduction%20to%20Chemistry/syllabus.md) | [yes](../subjects/Introduction%20to%20Chemistry/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Introduction to Civil Engineering](courses/Introduction%20to%20Civil%20Engineering.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Introduction to Cloud Computing](../subjects/Introduction%20to%20Cloud%20Computing/syllabus.md) | [yes](../subjects/Introduction%20to%20Cloud%20Computing/README.md) | 33 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to 2021-2024 |
| [Introduction to Cloud Computing and Blockchain Technology](../subjects/Introduction%20to%20Cloud%20Computing%20and%20Blockchain%20Technology/syllabus.md) | [yes](../subjects/Introduction%20to%20Cloud%20Computing%20and%20Blockchain%20Technology/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Introduction to Cryptography](../subjects/Introduction%20to%20Cryptography/syllabus.md) | [yes](../subjects/Introduction%20to%20Cryptography/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2024 to AY 2025-26 |
| [Introduction to Cybersecurity](../subjects/Introduction%20to%20Cybersecurity/syllabus.md) | [yes](../subjects/Introduction%20to%20Cybersecurity/README.md) | 4 | B TECH WORK IN PROCESS, MCA | 2018-2022 to 2021-2024 |
| [Introduction to Data and Signal Analysis](courses/Introduction%20to%20Data%20and%20Signal%20Analysis.md) | — | 3 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Introduction to Data Communication and Networks](../subjects/Introduction%20to%20Data%20Communication%20and%20Networks/syllabus.md) | [yes](../subjects/Introduction%20to%20Data%20Communication%20and%20Networks/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Introduction to Data Engineering](courses/Introduction%20to%20Data%20Engineering.md) | — | 3 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Introduction to Data, Signal and Image Analysis](../subjects/Introduction%20to%20Data%2C%20Signal%20and%20Image%20Analysis/syllabus.md) | [yes](../subjects/Introduction%20to%20Data%2C%20Signal%20and%20Image%20Analysis/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Introduction to Database Management System](../subjects/Introduction%20to%20Database%20Management%20System/syllabus.md) | [yes](../subjects/Introduction%20to%20Database%20Management%20System/README.md) | 3 | DIPLOMA | 2024-2027 |
| [Introduction to Digital Systems](../subjects/Introduction%20to%20Digital%20Systems/syllabus.md) | [yes](../subjects/Introduction%20to%20Digital%20Systems/README.md) | 1 | B TECH WORK IN PROCESS | 2021-2025 |
| [Introduction to Earth Sciences](courses/Introduction%20to%20Earth%20Sciences.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Introduction to Electrical and Electronics Engineering](../subjects/Introduction%20to%20Electrical%20and%20Electronics%20Engineering/syllabus.md) | [yes](../subjects/Introduction%20to%20Electrical%20and%20Electronics%20Engineering/README.md) | 5 | B TECH INTEGRATED, DIPLOMA | 2021-2027 to 2024-2027 |
| [Introduction to Forensic Science](../subjects/Introduction%20to%20Forensic%20Science/syllabus.md) | [yes](../subjects/Introduction%20to%20Forensic%20Science/README.md) | 3 | B TECH | AY 2023-24 to AY 2024-25 |
| [Introduction to GIS](../subjects/Introduction%20to%20GIS/syllabus.md) | [yes](../subjects/Introduction%20to%20GIS/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2025 to AY 2025-26 |
| [Introduction to Infrastructure Management](../subjects/Introduction%20to%20Infrastructure%20Management/syllabus.md) | [yes](../subjects/Introduction%20to%20Infrastructure%20Management/README.md) | 5 | MBA Tech | 2014-2019 to 2015-2020 |
| [Introduction to Innovation, IP Management and Entrepreneurship](../subjects/Introduction%20to%20Innovation%2C%20IP%20Management%20and%20Entrepreneurship/syllabus.md) | [yes](../subjects/Introduction%20to%20Innovation%2C%20IP%20Management%20and%20Entrepreneurship/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Introduction to International Business](../subjects/Introduction%20to%20International%20Business/syllabus.md) | [yes](../subjects/Introduction%20to%20International%20Business/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Introduction to IoT](../subjects/Introduction%20to%20IoT/syllabus.md) | [yes](../subjects/Introduction%20to%20IoT/README.md) | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2024 to 2020-2024 |
| [Introduction to IT Infrastructure Landscape](../subjects/Introduction%20to%20IT%20Infrastructure%20Landscape/syllabus.md) | [yes](../subjects/Introduction%20to%20IT%20Infrastructure%20Landscape/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Introduction to IT Systems](courses/Introduction%20to%20IT%20Systems.md) | — | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Introduction to Linux](../subjects/Introduction%20to%20Linux/syllabus.md) | [yes](../subjects/Introduction%20to%20Linux/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Introduction to Modern Application Development](../subjects/Introduction%20to%20Modern%20Application%20Development/syllabus.md) | [yes](../subjects/Introduction%20to%20Modern%20Application%20Development/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Introduction to Nano Technology](../subjects/Introduction%20to%20Nano%20Technology/syllabus.md) | [yes](../subjects/Introduction%20to%20Nano%20Technology/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Introduction to Nano-Electronics](courses/Introduction%20to%20Nano-Electronics.md) | — | 1 | MBA Tech | 2018-2023 |
| [Introduction to Network Security](../subjects/Introduction%20to%20Network%20Security/syllabus.md) | [yes](../subjects/Introduction%20to%20Network%20Security/README.md) | 1 | B TECH INTEGRATED | 2018-2024 |
| [Introduction to Object Oriented Programming](courses/Introduction%20to%20Object%20Oriented%20Programming.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Introduction to Open Source Software](courses/Introduction%20to%20Open%20Source%20Software.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Introduction to Operating Systems](../subjects/Introduction%20to%20Operating%20Systems/syllabus.md) | [yes](../subjects/Introduction%20to%20Operating%20Systems/README.md) | 3 | DIPLOMA | 2024-2027 |
| [Introduction to Optimization Techniques](../subjects/Introduction%20to%20Optimization%20Techniques/syllabus.md) | [yes](../subjects/Introduction%20to%20Optimization%20Techniques/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Introduction to Philosophy](../subjects/Introduction%20to%20Philosophy/syllabus.md) | [yes](../subjects/Introduction%20to%20Philosophy/README.md) | 3 | B TECH | AY 2023-24 to AY 2024-25 |
| [Introduction to Programming in Python](courses/Introduction%20to%20Programming%20in%20Python.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2024-25 |
| [Introduction to Python Programming](courses/Introduction%20to%20Python%20Programming.md) | — | 12 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2021-22 |
| [Introduction to Real Estate Sector](../subjects/Introduction%20to%20Real%20Estate%20Sector/syllabus.md) | [yes](../subjects/Introduction%20to%20Real%20Estate%20Sector/README.md) | 2 | PGDM | AY 2017-18 to AY 2018-19 |
| [Introduction to Soft Computing](courses/Introduction%20to%20Soft%20Computing.md) | — | 1 | B TECH INTEGRATED | 2023-2029 |
| [Introduction to Soft Computing Techniques Techniques](courses/Introduction%20to%20Soft%20Computing%20Techniques%20Techniques.md) | — | 1 | B TECH INTEGRATED | 2021-2027 |
| [Introduction to Software Development](../subjects/Introduction%20to%20Software%20Development/syllabus.md) | [yes](../subjects/Introduction%20to%20Software%20Development/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Introduction to Software Engineering](courses/Introduction%20to%20Software%20Engineering.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Introduction to Solid Modeling](courses/Introduction%20to%20Solid%20Modeling.md) | — | 1 | B TECH INTEGRATED | 2023-2029 |
| [Introduction to Vehicle Systems Engineering](courses/Introduction%20to%20Vehicle%20Systems%20Engineering.md) | — | 2 | B TECH, B TECH INTEGRATED | 2023-2029 to AY 2026-27 |
| [Introduction to Virtual Reality and Augmented Reality](../subjects/Introduction%20to%20Virtual%20Reality%20and%20Augmented%20Reality/syllabus.md) | [yes](../subjects/Introduction%20to%20Virtual%20Reality%20and%20Augmented%20Reality/README.md) | 14 | B TECH, B TECH INTEGRATED, MCA | 2018-2024 to AY 2025-26 |
| [Introductory Psychology](../subjects/Introductory%20Psychology/syllabus.md) | [yes](../subjects/Introductory%20Psychology/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Investment Analysis](../subjects/Investment%20Analysis/syllabus.md) | [yes](../subjects/Investment%20Analysis/README.md) | 4 | MBA Tech | 2020-2025 to 2021-2026 |
| [Investment Banking](../subjects/Investment%20Banking/syllabus.md) | [yes](../subjects/Investment%20Banking/README.md) | 15 | MBA Tech | 2014-2019 to 2021-2026 |
| [IoT and Applications](../subjects/IoT%20and%20Applications/syllabus.md) | [yes](../subjects/IoT%20and%20Applications/README.md) | 15 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2026-27 |
| [IoT Security](../subjects/IoT%20Security/syllabus.md) | [yes](../subjects/IoT%20Security/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [IoT System Architecture](../subjects/IoT%20System%20Architecture/syllabus.md) | [yes](../subjects/IoT%20System%20Architecture/README.md) | 1 | B TECH INTEGRATED | 2018-2024 |
| [Irrigation Engineering](../subjects/Irrigation%20Engineering/syllabus.md) | [yes](../subjects/Irrigation%20Engineering/README.md) | 7 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2019-2024 |
| [IT (Pavement Subgrade Materials)](courses/IT%20%28Pavement%20Subgrade%20Materials%29.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2018-2023 |
| [IT Project Management](../subjects/IT%20Project%20Management/syllabus.md) | [yes](../subjects/IT%20Project%20Management/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2026-27 |
| [IT Workshop](../subjects/IT%20Workshop/syllabus.md) | [yes](../subjects/IT%20Workshop/README.md) | 2 | B TECH | AY 2023-24 to AY 2024-25 |
| [IT Workshop Skylab MATLAB](../subjects/IT%20Workshop%20Skylab%20MATLAB/syllabus.md) | [yes](../subjects/IT%20Workshop%20Skylab%20MATLAB/README.md) | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [ITI - Total Quality Management](courses/ITI%20-%20Total%20Quality%20Management.md) | — | 1 | MBA Tech | 2018-2023 |
| [IV (Construction Contracts and Adininistration)](courses/IV%20%28Construction%20Contracts%20and%20Adininistration%29.md) | — | 1 | B TECH WORK IN PROCESS | 2014-2018 |
| [J- Project Management](courses/J-%20Project%20Management.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Java Programming](../subjects/Java%20Programming/syllabus.md) | [yes](../subjects/Java%20Programming/README.md) | 10 | B TECH INTEGRATED, DIPLOMA, MCA | 2020-2023 to 2026-2028 |
| [JoT System Architecture](courses/JoT%20System%20Architecture.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Journalism and Mass Media](../subjects/Journalism%20and%20Mass%20Media/syllabus.md) | [yes](../subjects/Journalism%20and%20Mass%20Media/README.md) | 1 | B TECH | AY 2024-25 |
| [Kinematics and Dynamics of Machines](../subjects/Kinematics%20and%20Dynamics%20of%20Machines/syllabus.md) | [yes](../subjects/Kinematics%20and%20Dynamics%20of%20Machines/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Kinematics of Machinery](courses/Kinematics%20of%20Machinery.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Knowledge Management](../subjects/Knowledge%20Management/syllabus.md) | [yes](../subjects/Knowledge%20Management/README.md) | 7 | MBA Tech | 2018-2023 to 2021-2026 |
| [Lab - 1: Applied Machine Learning Lab](courses/Lab%20-%201-%20Applied%20Machine%20Learning%20Lab.md) | — | 2 | M Tech | 2025-2027 to 2026-2028 |
| [Lab - 1: Applied ML Lab](courses/Lab%20-%201-%20Applied%20ML%20Lab.md) | — | 1 | M Tech | 2024-2026 |
| [Lab - 2: Data Science Lab](courses/Lab%20-%202-%20Data%20Science%20Lab.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Lab - 3: Building Generative AI Based Applications](courses/Lab%20-%203-%20Building%20Generative%20AI%20Based%20Applications.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Lab - 4: Large Language Models Lab](courses/Lab%20-%204-%20Large%20Language%20Models%20Lab.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Lab – 1: Visual Analytics Lab](courses/Lab%20%E2%80%93%201-%20Visual%20Analytics%20Lab.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Lab – 2: AI ML Lab](courses/Lab%20%E2%80%93%202-%20AI%20ML%20Lab.md) | — | 1 | M Tech | 2024-2026 |
| [Lab – 2: Artificial Intelligence Machine Learning Lab](courses/Lab%20%E2%80%93%202-%20Artificial%20Intelligence%20Machine%20Learning%20Lab.md) | — | 2 | M Tech | 2025-2027 to 2026-2028 |
| [Lab – 3: Artificial Intelligence Applications Lab](courses/Lab%20%E2%80%93%203-%20Artificial%20Intelligence%20Applications%20Lab.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Lab – 4: Artificial Intelligence Deep Learning and Edge Lab](courses/Lab%20%E2%80%93%204-%20Artificial%20Intelligence%20Deep%20Learning%20and%20Edge%20Lab.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Large Language Models](../subjects/Large%20Language%20Models/syllabus.md) | [yes](../subjects/Large%20Language%20Models/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Leadership](../subjects/Leadership/syllabus.md) | [yes](../subjects/Leadership/README.md) | 13 | MBA Tech | 2014-2019 to 2021-2026 |
| [Leadership in Digital Business](courses/Leadership%20in%20Digital%20Business.md) | — | 7 | MBA Tech | 2018-2023 to 2021-2026 |
| [Leadership in Digital Transformation](courses/Leadership%20in%20Digital%20Transformation.md) | — | 1 | MBA Tech | 2017-2022 |
| [Leading Through Life Skills](../subjects/Leading%20Through%20Life%20Skills/syllabus.md) | [yes](../subjects/Leading%20Through%20Life%20Skills/README.md) | 5 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Lean Manufacturing](../subjects/Lean%20Manufacturing/syllabus.md) | [yes](../subjects/Lean%20Manufacturing/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Leave Application for 3 Months](courses/Leave%20Application%20for%203%20Months.md) | — | 1 | B TECH | — |
| [Legal Aspects of Business](../subjects/Legal%20Aspects%20of%20Business/syllabus.md) | [yes](../subjects/Legal%20Aspects%20of%20Business/README.md) | 13 | MBA Tech | 2015-2020 to 2017-2022 |
| [Legal Aspects of Construction](../subjects/Legal%20Aspects%20of%20Construction/syllabus.md) | [yes](../subjects/Legal%20Aspects%20of%20Construction/README.md) | 1 | PGDM | — |
| [Life Skills](courses/Life%20Skills.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Limit State Design of Reinforced](courses/Limit%20State%20Design%20of%20Reinforced.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Limit State Design of Reinforced Concrete Structures](../subjects/Limit%20State%20Design%20of%20Reinforced%20Concrete%20Structures/syllabus.md) | [yes](../subjects/Limit%20State%20Design%20of%20Reinforced%20Concrete%20Structures/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to 2018-2024 |
| [Linear Algebra](../subjects/Linear%20Algebra/syllabus.md) | [yes](../subjects/Linear%20Algebra/README.md) | 7 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2023-24 |
| [Linear Algebra and Differential Equations](../subjects/Linear%20Algebra%20and%20Differential%20Equations/syllabus.md) | [yes](../subjects/Linear%20Algebra%20and%20Differential%20Equations/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2026 to AY 2025-26 |
| [Linear Algebra and Ordinary Differential Equations](courses/Linear%20Algebra%20and%20Ordinary%20Differential%20Equations.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to 2021-2026 |
| [Linear Integrated Circuits and Applications](../subjects/Linear%20Integrated%20Circuits%20and%20Applications/syllabus.md) | [yes](../subjects/Linear%20Integrated%20Circuits%20and%20Applications/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2019-20 |
| [Linux and Secure OS for Business](../subjects/Linux%20and%20Secure%20OS%20for%20Business/syllabus.md) | [yes](../subjects/Linux%20and%20Secure%20OS%20for%20Business/README.md) | 2 | B TECH | AY 2024-25 to AY 2025-26 |
| [Lnformation Security Assurance and Forensics I I](courses/Lnformation%20Security%20Assurance%20and%20Forensics%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Logic Design and Computer Organization](../subjects/Logic%20Design%20and%20Computer%20Organization/syllabus.md) | [yes](../subjects/Logic%20Design%20and%20Computer%20Organization/README.md) | 1 | B TECH | AY 2024-25 |
| [Logistics and Supply Chain Management](../subjects/Logistics%20and%20Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Logistics%20and%20Supply%20Chain%20Management/README.md) | 16 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2022-2027 |
| [Machine Drawing](../subjects/Machine%20Drawing/syllabus.md) | [yes](../subjects/Machine%20Drawing/README.md) | 25 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Machine Drawing and Computer Graphics](courses/Machine%20Drawing%20and%20Computer%20Graphics.md) | — | 6 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Machine Drawing and Computer Graphics I](courses/Machine%20Drawing%20and%20Computer%20Graphics%20I.md) | — | 2 | B TECH, MBA Tech | 2012-2017 to AY 2013-14 |
| [Machine Learning](../subjects/Machine%20Learning/syllabus.md) | [yes](../subjects/Machine%20Learning/README.md) | 67 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2014-2019 to AY 2026-27 |
| [Machine Learning (Department](courses/Machine%20Learning%20%28Department.md) | — | 3 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Machine Learning Algorithms](../subjects/Machine%20Learning%20Algorithms/syllabus.md) | [yes](../subjects/Machine%20Learning%20Algorithms/README.md) | 4 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2024-25 |
| [Machine Learning and Data Mining](../subjects/Machine%20Learning%20and%20Data%20Mining/syllabus.md) | [yes](../subjects/Machine%20Learning%20and%20Data%20Mining/README.md) | 10 | M Tech | 2015-2017 to 2023-2025 |
| [Machine Learning Operations](courses/Machine%20Learning%20Operations.md) | — | 3 | M Tech | 2024-2026 to 2025-2027 |
| [Machine Learning Optimization Algorithms](../subjects/Machine%20Learning%20Optimization%20Algorithms/syllabus.md) | [yes](../subjects/Machine%20Learning%20Optimization%20Algorithms/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Machine Shop](courses/Machine%20Shop.md) | — | 4 | B TECH, B TECH INTEGRATED, MBA Tech | 2012-2017 to AY 2019-20 |
| [Machine Shop I](courses/Machine%20Shop%20I.md) | — | 32 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2026-27 |
| [Machine Shop II](courses/Machine%20Shop%20II.md) | — | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Macroeconomics](../subjects/Macroeconomics/syllabus.md) | [yes](../subjects/Macroeconomics/README.md) | 6 | MBA Tech | 2021-2026 to 2023-2028 |
| [Management](courses/Management.md) | — | 1 | B TECH | AY 2013-14 |
| [Management Accounting for Engineers](../subjects/Management%20Accounting%20for%20Engineers/syllabus.md) | [yes](../subjects/Management%20Accounting%20for%20Engineers/README.md) | 87 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2026-27 |
| [Management Information System](../subjects/Management%20Information%20System/syllabus.md) | [yes](../subjects/Management%20Information%20System/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2026-27 |
| [Management of Mergers and Acquisitions](../subjects/Management%20of%20Mergers%20and%20Acquisitions/syllabus.md) | [yes](../subjects/Management%20of%20Mergers%20and%20Acquisitions/README.md) | 8 | MBA Tech | 2014-2019 to 2017-2022 |
| [Management of Real Estate Business](../subjects/Management%20of%20Real%20Estate%20Business/syllabus.md) | [yes](../subjects/Management%20of%20Real%20Estate%20Business/README.md) | 3 | MBA Tech | 2014-2019 to 2015-2020 |
| [Management of Technology and Innovation](../subjects/Management%20of%20Technology%20and%20Innovation/syllabus.md) | [yes](../subjects/Management%20of%20Technology%20and%20Innovation/README.md) | 5 | MBA Tech | 2018-2023 to 2022-2027 |
| [Management Through Movies](../subjects/Management%20Through%20Movies/syllabus.md) | [yes](../subjects/Management%20Through%20Movies/README.md) | 11 | B TECH, MBA Tech | 2018-2023 to AY 2024-25 |
| [Managerial Economics, Indian Economy and Policy](courses/Managerial%20Economics%2C%20Indian%20Economy%20and%20Policy.md) | — | 1 | MBA Tech | 2017-2022 |
| [Managing Innovation](courses/Managing%20Innovation.md) | — | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Managing Innovation Module Cpde](courses/Managing%20Innovation%20Module%20Cpde.md) | — | 1 | MBA Tech | 2018-2023 |
| [Managing Uncertainty](../subjects/Managing%20Uncertainty/syllabus.md) | [yes](../subjects/Managing%20Uncertainty/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Mandarin](courses/Mandarin.md) | — | 3 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Manufacturing Engineering](courses/Manufacturing%20Engineering.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Manufacturing Management](../subjects/Manufacturing%20Management/syllabus.md) | [yes](../subjects/Manufacturing%20Management/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Manufacturing Processes](../subjects/Manufacturing%20Processes/syllabus.md) | [yes](../subjects/Manufacturing%20Processes/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2025-26 |
| [Manufacturing Processes I](../subjects/Manufacturing%20Processes%20I/syllabus.md) | [yes](../subjects/Manufacturing%20Processes%20I/README.md) | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Manufacturing Processes II](../subjects/Manufacturing%20Processes%20II/syllabus.md) | [yes](../subjects/Manufacturing%20Processes%20II/README.md) | 31 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Manufacturing Processes-I 4](courses/Manufacturing%20Processes-I%204.md) | — | 1 | B TECH WORK IN PROCESS | 2014-2018 |
| [Manufacturing Workshop](courses/Manufacturing%20Workshop.md) | — | 3 | B TECH INTEGRATED, DIPLOMA | 2022-2028 to 2024-2027 |
| [Manufacturing Workshop I](courses/Manufacturing%20Workshop%20I.md) | — | 2 | B TECH INTEGRATED | 2020-2026 to 2021-2027 |
| [Manufacturing Workshop II](courses/Manufacturing%20Workshop%20II.md) | — | 2 | B TECH INTEGRATED | 2020-2026 to 2021-2027 |
| [Marine Structures](../subjects/Marine%20Structures/syllabus.md) | [yes](../subjects/Marine%20Structures/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Marketing Analytics](../subjects/Marketing%20Analytics/syllabus.md) | [yes](../subjects/Marketing%20Analytics/README.md) | 11 | B TECH, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2014-2019 to 2023-2025 |
| [Marketing Analytics De Teaching Scheme Evaluation Scheme](courses/Marketing%20Analytics%20De%20Teaching%20Scheme%20Evaluation%20Scheme.md) | — | 1 | M Tech | 2020-2022 |
| [Marketing Analytics for Marketing Mix](courses/Marketing%20Analytics%20for%20Marketing%20Mix.md) | — | 3 | MBA Tech | 2015-2020 to 2017-2022 |
| [Marketing Analytics for Marketing Mix Decisions](courses/Marketing%20Analytics%20for%20Marketing%20Mix%20Decisions.md) | — | 11 | MBA Tech | 2015-2020 to 2021-2026 |
| [Marketing Analytics for Strategic Decision](../subjects/Marketing%20Analytics%20for%20Strategic%20Decision/syllabus.md) | [yes](../subjects/Marketing%20Analytics%20for%20Strategic%20Decision/README.md) | 1 | M Tech | 2018-2020 |
| [Marketing Management](../subjects/Marketing%20Management/syllabus.md) | [yes](../subjects/Marketing%20Management/README.md) | 45 | B TECH, B TECH WORK IN PROCESS, MBA Tech, PGDM | 2015-2020 to AY 2026-27 |
| [Marketing of Technology Products](../subjects/Marketing%20of%20Technology%20Products/syllabus.md) | [yes](../subjects/Marketing%20of%20Technology%20Products/README.md) | 14 | MBA Tech | 2014-2019 to 2021-2026 |
| [Marketing Research and Marketing](courses/Marketing%20Research%20and%20Marketing.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Marketing Strategy](../subjects/Marketing%20Strategy/syllabus.md) | [yes](../subjects/Marketing%20Strategy/README.md) | 13 | MBA Tech | 2014-2019 to 2021-2026 |
| [Marketing Strategy and Analytics](../subjects/Marketing%20Strategy%20and%20Analytics/syllabus.md) | [yes](../subjects/Marketing%20Strategy%20and%20Analytics/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Markov Chains for Business Applications](courses/Markov%20Chains%20for%20Business%20Applications.md) | — | 3 | M Tech | 2021-2023 to 2023-2025 |
| [Mass Transfer Operations](courses/Mass%20Transfer%20Operations.md) | — | 2 | MBA Tech | 2015-2020 to 2016-2021 |
| [Mass Transfer Operations I](../subjects/Mass%20Transfer%20Operations%20I/syllabus.md) | [yes](../subjects/Mass%20Transfer%20Operations%20I/README.md) | 4 | MBA Tech | 2016-2021 to 2019-2024 |
| [Mass Transfer Operations II](../subjects/Mass%20Transfer%20Operations%20II/syllabus.md) | [yes](../subjects/Mass%20Transfer%20Operations%20II/README.md) | 4 | MBA Tech | 2017-2022 to 2020-2025 |
| [Material and Energy Balance Computation](../subjects/Material%20and%20Energy%20Balance%20Computation/syllabus.md) | [yes](../subjects/Material%20and%20Energy%20Balance%20Computation/README.md) | 1 | MBA Tech | 2018-2023 |
| [Material Management](../subjects/Material%20Management/syllabus.md) | [yes](../subjects/Material%20Management/README.md) | 2 | PGDM | AY 2016-17 to AY 2018-19 |
| [Material Sciences](../subjects/Material%20Sciences/syllabus.md) | [yes](../subjects/Material%20Sciences/README.md) | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Material Selection](../subjects/Material%20Selection/syllabus.md) | [yes](../subjects/Material%20Selection/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Material Testing and Workshop II](courses/Material%20Testing%20and%20Workshop%20II.md) | — | 1 | PGDM | — |
| [Material Testing Workshop I](courses/Material%20Testing%20Workshop%20I.md) | — | 2 | PGDM | AY 2017-18 to AY 2018-19 |
| [Materials Engineering](../subjects/Materials%20Engineering/syllabus.md) | [yes](../subjects/Materials%20Engineering/README.md) | 33 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Materials Engineering 0](courses/Materials%20Engineering%200.md) | — | 1 | MBA Tech | 2013-2018 |
| [Materials Engineering and Metallurgy](../subjects/Materials%20Engineering%20and%20Metallurgy/syllabus.md) | [yes](../subjects/Materials%20Engineering%20and%20Metallurgy/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Math Tics I](courses/Math%20Tics%20I.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Mathematics for AI](courses/Mathematics%20for%20AI.md) | — | 4 | M Tech, MBA Tech | 2018-2023 to 2023-2025 |
| [Mathematics I](../subjects/Mathematics%20I/syllabus.md) | [yes](../subjects/Mathematics%20I/README.md) | 14 | B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2018-2022 to 2025-2028 |
| [Mathematics II](../subjects/Mathematics%20II/syllabus.md) | [yes](../subjects/Mathematics%20II/README.md) | 15 | B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2014-2020 to 2024-2027 |
| [Mathematics III](../subjects/Mathematics%20III/syllabus.md) | [yes](../subjects/Mathematics%20III/README.md) | 29 | B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2017-2023 to 2024-2027 |
| [Mathematics IV](../subjects/Mathematics%20IV/syllabus.md) | [yes](../subjects/Mathematics%20IV/README.md) | 12 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2022 to 2023-2029 |
| [Mathematics-II Btcioos](courses/Mathematics-II%20Btcioos.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Mathematics-II Ie Cede EEE](courses/Mathematics-II%20Ie%20Cede%20EEE.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Matrix](courses/Matrix.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Measurements and Instrumentation](../subjects/Measurements%20and%20Instrumentation/syllabus.md) | [yes](../subjects/Measurements%20and%20Instrumentation/README.md) | 2 | B TECH, MBA Tech | AY 2015-16 to 2016-2021 |
| [Mechanical Measurement and Metrology I](courses/Mechanical%20Measurement%20and%20Metrology%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Mechanical Measurements and](courses/Mechanical%20Measurements%20and.md) | — | 1 | MBA Tech | 2018-2023 |
| [Mechanical Measurements and Instrumentation](../subjects/Mechanical%20Measurements%20and%20Instrumentation/syllabus.md) | [yes](../subjects/Mechanical%20Measurements%20and%20Instrumentation/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Mechanical Measurements and Metrology](../subjects/Mechanical%20Measurements%20and%20Metrology/syllabus.md) | [yes](../subjects/Mechanical%20Measurements%20and%20Metrology/README.md) | 28 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2026-27 |
| [Mechanical Workshop](courses/Mechanical%20Workshop.md) | — | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Mechanics of Materials](../subjects/Mechanics%20of%20Materials/syllabus.md) | [yes](../subjects/Mechanics%20of%20Materials/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Mechatronic Systems Design](../subjects/Mechatronic%20Systems%20Design/syllabus.md) | [yes](../subjects/Mechatronic%20Systems%20Design/README.md) | 16 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Mechatronics](../subjects/Mechatronics/syllabus.md) | [yes](../subjects/Mechatronics/README.md) | 5 | B TECH, B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Mechatronics and Controls](../subjects/Mechatronics%20and%20Controls/syllabus.md) | [yes](../subjects/Mechatronics%20and%20Controls/README.md) | 13 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2019-20 |
| [Media Planning](../subjects/Media%20Planning/syllabus.md) | [yes](../subjects/Media%20Planning/README.md) | 14 | MBA Tech | 2014-2019 to 2021-2026 |
| [Medical Electronics](../subjects/Medical%20Electronics/syllabus.md) | [yes](../subjects/Medical%20Electronics/README.md) | 3 | B TECH | AY 2014-15 to AY 2015-16 |
| [Mergers and Acquisitions](../subjects/Mergers%20and%20Acquisitions/syllabus.md) | [yes](../subjects/Mergers%20and%20Acquisitions/README.md) | 7 | MBA Tech | 2018-2023 to 2021-2026 |
| [Metal Forming Processes](courses/Metal%20Forming%20Processes.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Metaverse](courses/Metaverse.md) | — | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2026 to AY 2025-26 |
| [Micro and Nano Manufacturing](../subjects/Micro%20and%20Nano%20Manufacturing/syllabus.md) | [yes](../subjects/Micro%20and%20Nano%20Manufacturing/README.md) | 10 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2026-27 |
| [Microcontrollers and Embedded](courses/Microcontrollers%20and%20Embedded.md) | — | 5 | MBA Tech | 2012-2017 to 2019-2024 |
| [Microcontrollers and Embedded 1 System](courses/Microcontrollers%20and%20Embedded%201%20System.md) | — | 1 | B TECH | AY 2013-14 |
| [Microcontrollers and Embedded Systems](../subjects/Microcontrollers%20and%20Embedded%20Systems/syllabus.md) | [yes](../subjects/Microcontrollers%20and%20Embedded%20Systems/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Microeconomics](../subjects/Microeconomics/syllabus.md) | [yes](../subjects/Microeconomics/README.md) | 1 | B TECH | AY 2025-26 |
| [Microelectromechanical Systems](../subjects/Microelectromechanical%20Systems/syllabus.md) | [yes](../subjects/Microelectromechanical%20Systems/README.md) | 12 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2025-26 |
| [MicroElectroMechanical Systems I](courses/MicroElectroMechanical%20Systems%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Microprocessor](../subjects/Microprocessor/syllabus.md) | [yes](../subjects/Microprocessor/README.md) | 5 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [Microprocessor and Course](courses/Microprocessor%20and%20Course.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to 2020-2025 |
| [Microprocessor and Microcontroller](../subjects/Microprocessor%20and%20Microcontroller/syllabus.md) | [yes](../subjects/Microprocessor%20and%20Microcontroller/README.md) | 28 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2013-2017 to AY 2025-26 |
| [Microprocessor and Real Time](courses/Microprocessor%20and%20Real%20Time.md) | — | 1 | MBA Tech | 2016-2021 |
| [Microprocessor Based Systems](../subjects/Microprocessor%20Based%20Systems/syllabus.md) | [yes](../subjects/Microprocessor%20Based%20Systems/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2019-20 |
| [Microprocessor Based Systems I](courses/Microprocessor%20Based%20Systems%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Microprocessor Systems and Interfacing](../subjects/Microprocessor%20Systems%20and%20Interfacing/syllabus.md) | [yes](../subjects/Microprocessor%20Systems%20and%20Interfacing/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Microprocessors and Interfacing](../subjects/Microprocessors%20and%20Interfacing/syllabus.md) | [yes](../subjects/Microprocessors%20and%20Interfacing/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2018-19 |
| [Microservices and Architecture](../subjects/Microservices%20and%20Architecture/syllabus.md) | [yes](../subjects/Microservices%20and%20Architecture/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MCA | 2020-2024 to AY 2025-26 |
| [Microservices Software Architecture](../subjects/Microservices%20Software%20Architecture/syllabus.md) | [yes](../subjects/Microservices%20Software%20Architecture/README.md) | 2 | MCA | 2020-2023 to 2021-2024 |
| [Microwave and Antenna Theory](../subjects/Microwave%20and%20Antenna%20Theory/syllabus.md) | [yes](../subjects/Microwave%20and%20Antenna%20Theory/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2025-26 |
| [Mini Project](courses/Mini%20Project.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MCA | 2019-2023 to 2025-2027 |
| [Mini-Projects on Building Planning and Design](courses/Mini-Projects%20on%20Building%20Planning%20and%20Design.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2018-2023 |
| [Minor Project](courses/Minor%20Project.md) | — | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | AY 2014-15 to 2021-2024 |
| [MLOps](../subjects/MLOps/syllabus.md) | [yes](../subjects/MLOps/README.md) | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2026 to AY 2025-26 |
| [Mobile and Ad Hoc Networks](../subjects/Mobile%20and%20Ad%20Hoc%20Networks/syllabus.md) | [yes](../subjects/Mobile%20and%20Ad%20Hoc%20Networks/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Mobile Application Development](courses/Mobile%20Application%20Development.md) | — | 55 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2026-27 |
| [Mobile Application Development Lab](courses/Mobile%20Application%20Development%20Lab.md) | — | 1 | MBA Tech | 2014-2019 |
| [Mobile Computing](../subjects/Mobile%20Computing/syllabus.md) | [yes](../subjects/Mobile%20Computing/README.md) | 34 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2025-26 |
| [Mobile Device Security and Forensics](../subjects/Mobile%20Device%20Security%20and%20Forensics/syllabus.md) | [yes](../subjects/Mobile%20Device%20Security%20and%20Forensics/README.md) | 5 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2024 to AY 2025-26 |
| [Mobile Game Development](../subjects/Mobile%20Game%20Development/syllabus.md) | [yes](../subjects/Mobile%20Game%20Development/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Modelling and Simulation](../subjects/Modelling%20and%20Simulation/syllabus.md) | [yes](../subjects/Modelling%20and%20Simulation/README.md) | 12 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2024-25 |
| [Modern Construction Equipment and Techniques](../subjects/Modern%20Construction%20Equipment%20and%20Techniques/syllabus.md) | [yes](../subjects/Modern%20Construction%20Equipment%20and%20Techniques/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2025 to AY 2026-27 |
| [Modern Control Systems](../subjects/Modern%20Control%20Systems/syllabus.md) | [yes](../subjects/Modern%20Control%20Systems/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Modern Day Robotics and Its Industrial](courses/Modern%20Day%20Robotics%20and%20Its%20Industrial.md) | — | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Modern Web Applications](../subjects/Modern%20Web%20Applications/syllabus.md) | [yes](../subjects/Modern%20Web%20Applications/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Multimedia %Stems I](courses/Multimedia%20%25Stems%20I.md) | — | 1 | B TECH | — |
| [Multimedia and Animation](../subjects/Multimedia%20and%20Animation/syllabus.md) | [yes](../subjects/Multimedia%20and%20Animation/README.md) | 7 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Multimedia and Virtual Reality](../subjects/Multimedia%20and%20Virtual%20Reality/syllabus.md) | [yes](../subjects/Multimedia%20and%20Virtual%20Reality/README.md) | 1 | B TECH INTEGRATED | 2020-2026 |
| [Multimedia Signal Compression](../subjects/Multimedia%20Signal%20Compression/syllabus.md) | [yes](../subjects/Multimedia%20Signal%20Compression/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2018 to AY 2020-21 |
| [Multimedia System and Virtual Reality](../subjects/Multimedia%20System%20and%20Virtual%20Reality/syllabus.md) | [yes](../subjects/Multimedia%20System%20and%20Virtual%20Reality/README.md) | 5 | MBA Tech | 2013-2018 to 2017-2022 |
| [Multimedia Systems](../subjects/Multimedia%20Systems/syllabus.md) | [yes](../subjects/Multimedia%20Systems/README.md) | 19 | B TECH, B TECH WORK IN PROCESS, MCA | 2013-2016 to AY 2020-21 |
| [Nano Technology](../subjects/Nano%20Technology/syllabus.md) | [yes](../subjects/Nano%20Technology/README.md) | 7 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2020-2025 |
| [Natural Language Processing](../subjects/Natural%20Language%20Processing/syllabus.md) | [yes](../subjects/Natural%20Language%20Processing/README.md) | 48 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2018-2020 to AY 2026-27 |
| [Nature Inspired Algorithms](courses/Nature%20Inspired%20Algorithms.md) | — | 2 | B TECH, MBA Tech | 2025-2030 to AY 2026-27 |
| [Network Analytics](courses/Network%20Analytics.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Network Design](courses/Network%20Design.md) | — | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Network Design and Planning](../subjects/Network%20Design%20and%20Planning/syllabus.md) | [yes](../subjects/Network%20Design%20and%20Planning/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2020-21 |
| [Network Security](../subjects/Network%20Security/syllabus.md) | [yes](../subjects/Network%20Security/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Networks Analysis and Synthesis](../subjects/Networks%20Analysis%20and%20Synthesis/syllabus.md) | [yes](../subjects/Networks%20Analysis%20and%20Synthesis/README.md) | 3 | B TECH, MBA Tech | 2015-2020 to AY 2017-18 |
| [Networks and Telecommunications](../subjects/Networks%20and%20Telecommunications/syllabus.md) | [yes](../subjects/Networks%20and%20Telecommunications/README.md) | 4 | B TECH | AY 2022-23 to AY 2025-26 |
| [Neural Networks and Deep](courses/Neural%20Networks%20and%20Deep.md) | — | 1 | MBA Tech | 2014-2019 |
| [Neural Networks and Deep Learning](../subjects/Neural%20Networks%20and%20Deep%20Learning/syllabus.md) | [yes](../subjects/Neural%20Networks%20and%20Deep%20Learning/README.md) | 20 | B TECH, B TECH INTEGRATED, MBA Tech | 2015-2020 to AY 2025-26 |
| [Next Generation Wireless Communications](../subjects/Next%20Generation%20Wireless%20Communications/syllabus.md) | [yes](../subjects/Next%20Generation%20Wireless%20Communications/README.md) | 7 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2024-25 |
| [Non Conventional Energy Sources](../subjects/Non%20Conventional%20Energy%20Sources/syllabus.md) | [yes](../subjects/Non%20Conventional%20Energy%20Sources/README.md) | 7 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2015-16 |
| [Non-Parametric Statistical Inference](courses/Non-Parametric%20Statistical%20Inference.md) | — | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Numerical and Statistical Methods](../subjects/Numerical%20and%20Statistical%20Methods/syllabus.md) | [yes](../subjects/Numerical%20and%20Statistical%20Methods/README.md) | 14 | B TECH, B TECH WORK IN PROCESS, MBA Tech, MCA | 2014-2017 to AY 2019 |
| [Numerical Methods](../subjects/Numerical%20Methods/syllabus.md) | [yes](../subjects/Numerical%20Methods/README.md) | 3 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2015-2019 to AY 2019-20 |
| [Numerical Modeling of Groundwater Flow and Transport](../subjects/Numerical%20Modeling%20of%20Groundwater%20Flow%20and%20Transport/syllabus.md) | [yes](../subjects/Numerical%20Modeling%20of%20Groundwater%20Flow%20and%20Transport/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2018-2024 |
| [Numerical Techniques](../subjects/Numerical%20Techniques/syllabus.md) | [yes](../subjects/Numerical%20Techniques/README.md) | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [Numerical Tedlniques](courses/Numerical%20Tedlniques.md) | — | 1 | B TECH | AY 2013-14 |
| [Nutrition for Health](../subjects/Nutrition%20for%20Health/syllabus.md) | [yes](../subjects/Nutrition%20for%20Health/README.md) | 2 | B TECH, B TECH INTEGRATED | 2019-2025 to AY 2024-25 |
| [NX Line Designer](courses/NX%20Line%20Designer.md) | — | 1 | B TECH | AY 2025-26 |
| [O E- II Environment Management](courses/O%20E-%20II%20Environment%20Management.md) | — | 1 | MBA Tech | 2020-2025 |
| [Object Oriented](courses/Object%20Oriented.md) | — | 1 | B TECH | AY 2020-21 |
| [Object Oriented Analysis and Design](courses/Object%20Oriented%20Analysis%20and%20Design.md) | — | 5 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2019-20 |
| [Object Oriented Modeling and Design](../subjects/Object%20Oriented%20Modeling%20and%20Design/syllabus.md) | [yes](../subjects/Object%20Oriented%20Modeling%20and%20Design/README.md) | 2 | B TECH | AY 2013-14 |
| [Object Oriented Programming](../subjects/Object%20Oriented%20Programming/syllabus.md) | [yes](../subjects/Object%20Oriented%20Programming/README.md) | 49 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Object Oriented Programming and Design](../subjects/Object%20Oriented%20Programming%20and%20Design/syllabus.md) | [yes](../subjects/Object%20Oriented%20Programming%20and%20Design/README.md) | 1 | B TECH | AY 2024-25 |
| [Object Oriented Programming Lab](courses/Object%20Oriented%20Programming%20Lab.md) | — | 8 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Object Oriented Programming Through](courses/Object%20Oriented%20Programming%20Through.md) | — | 1 | B TECH WORK IN PROCESS | 2021-2025 |
| [Object Oriented Programming Through Java](../subjects/Object%20Oriented%20Programming%20Through%20Java/syllabus.md) | [yes](../subjects/Object%20Oriented%20Programming%20Through%20Java/README.md) | 4 | B TECH, B TECH INTEGRATED | 2020-2026 to AY 2025-26 |
| [Object Oriented Software](courses/Object%20Oriented%20Software.md) | — | 2 | MCA | 2013-2016 to 2014-2017 |
| [Object Oriented Software Engineering](../subjects/Object%20Oriented%20Software%20Engineering/syllabus.md) | [yes](../subjects/Object%20Oriented%20Software%20Engineering/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to 2021-2024 |
| [Object Oriented Software Engineering (Dept](courses/Object%20Oriented%20Software%20Engineering%20%28Dept.md) | — | 1 | MBA Tech | 2018-2023 |
| [Oe-I: Sustainable Energy Technologies](courses/Oe-I-%20Sustainable%20Energy%20Technologies.md) | — | 1 | MBA Tech | 2020-2025 |
| [Online Marketing](../subjects/Online%20Marketing/syllabus.md) | [yes](../subjects/Online%20Marketing/README.md) | 3 | MBA Tech | 2014-2019 to 2015-2020 |
| [Open Channel Flow](courses/Open%20Channel%20Flow.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to 2019-2025 |
| [Open Elective Course — I](courses/Open%20Elective%20Course%20%E2%80%94%20I.md) | — | 1 | MBA Tech | 2018-2023 |
| [Operating Systems](../subjects/Operating%20Systems/syllabus.md) | [yes](../subjects/Operating%20Systems/README.md) | 75 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Operating Systems and Database](courses/Operating%20Systems%20and%20Database.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Operation and Supply Chain Analytics](../subjects/Operation%20and%20Supply%20Chain%20Analytics/syllabus.md) | [yes](../subjects/Operation%20and%20Supply%20Chain%20Analytics/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Operation Planning and Control](../subjects/Operation%20Planning%20and%20Control/syllabus.md) | [yes](../subjects/Operation%20Planning%20and%20Control/README.md) | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Operation Planning and Control Moduld](courses/Operation%20Planning%20and%20Control%20Moduld.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Operation Research for Chemical Engineers](../subjects/Operation%20Research%20for%20Chemical%20Engineers/syllabus.md) | [yes](../subjects/Operation%20Research%20for%20Chemical%20Engineers/README.md) | 3 | MBA Tech | 2018-2023 to 2020-2025 |
| [Operation Research I](courses/Operation%20Research%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Operations and Supply](courses/Operations%20and%20Supply.md) | — | 1 | B TECH | AY 2021-22 |
| [Operations and Supply Chain](courses/Operations%20and%20Supply%20Chain.md) | — | 1 | B TECH WORK IN PROCESS | 2021-2025 |
| [Operations and Supply Chain Management](../subjects/Operations%20and%20Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Operations%20and%20Supply%20Chain%20Management/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Operations Management](../subjects/Operations%20Management/syllabus.md) | [yes](../subjects/Operations%20Management/README.md) | 26 | MBA Tech | 2015-2020 to 2023-2028 |
| [Operations Management Madule](courses/Operations%20Management%20Madule.md) | — | 5 | MBA Tech | 2019-2024 |
| [Operations Research](../subjects/Operations%20Research/syllabus.md) | [yes](../subjects/Operations%20Research/README.md) | 60 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2013-2016 to AY 2025-26 |
| [Operations Strategy](../subjects/Operations%20Strategy/syllabus.md) | [yes](../subjects/Operations%20Strategy/README.md) | 14 | MBA Tech | 2014-2019 to 2021-2026 |
| [Optical Fiber Communication](../subjects/Optical%20Fiber%20Communication/syllabus.md) | [yes](../subjects/Optical%20Fiber%20Communication/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Optical Fiber Communication I](courses/Optical%20Fiber%20Communication%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Optimization](courses/Optimization.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Optimization for Decision Making](../subjects/Optimization%20for%20Decision%20Making/syllabus.md) | [yes](../subjects/Optimization%20for%20Decision%20Making/README.md) | 1 | B TECH WORK IN PROCESS | AY 2021-22 |
| [Optimization Methods](../subjects/Optimization%20Methods/syllabus.md) | [yes](../subjects/Optimization%20Methods/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2023 to AY 2025-26 |
| [Optimization Techniques](../subjects/Optimization%20Techniques/syllabus.md) | [yes](../subjects/Optimization%20Techniques/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2024-25 |
| [Organic Process Technologies](../subjects/Organic%20Process%20Technologies/syllabus.md) | [yes](../subjects/Organic%20Process%20Technologies/README.md) | 3 | MBA Tech | 2018-2023 to 2020-2025 |
| [Organizational Behaviour](../subjects/Organizational%20Behaviour/syllabus.md) | [yes](../subjects/Organizational%20Behaviour/README.md) | 38 | B TECH INTEGRATED, MBA Tech, MCA | 2013-2016 to 2022-2027 |
| [Parallel Computing](../subjects/Parallel%20Computing/syllabus.md) | [yes](../subjects/Parallel%20Computing/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MCA | 2013-2016 to AY 2019-20 |
| [Parallel Computing(Eledive-II1) I](courses/Parallel%20Computing%28Eledive-II1%29%20I.md) | — | 1 | B TECH | — |
| [Parallel Processing](../subjects/Parallel%20Processing/syllabus.md) | [yes](../subjects/Parallel%20Processing/README.md) | 5 | MBA Tech | 2012-2017 to 2017-2022 |
| [Partial Differential Equations and Laplace Transforms](courses/Partial%20Differential%20Equations%20and%20Laplace%20Transforms.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to 2020-2025 |
| [Particle and Fluid Particle Processing](courses/Particle%20and%20Fluid%20Particle%20Processing.md) | — | 1 | MBA Tech | 2018-2023 |
| [Pattern and Anomaly Detection](../subjects/Pattern%20and%20Anomaly%20Detection/syllabus.md) | [yes](../subjects/Pattern%20and%20Anomaly%20Detection/README.md) | 1 | B TECH | — |
| [Pavement Design and Construction](../subjects/Pavement%20Design%20and%20Construction/syllabus.md) | [yes](../subjects/Pavement%20Design%20and%20Construction/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2013-14 to AY 2026-27 |
| [Pavement Management System](../subjects/Pavement%20Management%20System/syllabus.md) | [yes](../subjects/Pavement%20Management%20System/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Pavement Subgrade and Materials](../subjects/Pavement%20Subgrade%20and%20Materials/syllabus.md) | [yes](../subjects/Pavement%20Subgrade%20and%20Materials/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [People Analytics](../subjects/People%20Analytics/syllabus.md) | [yes](../subjects/People%20Analytics/README.md) | 13 | MBA Tech | 2014-2019 to 2021-2026 |
| [Personal Skills for Business](courses/Personal%20Skills%20for%20Business.md) | — | 19 | MBA Tech | 2015-2020 to 2022-2027 |
| [Petroleum Refining Technology](../subjects/Petroleum%20Refining%20Technology/syllabus.md) | [yes](../subjects/Petroleum%20Refining%20Technology/README.md) | 5 | MBA Tech | 2014-2019 to 2019-2024 |
| [Physics](../subjects/Physics/syllabus.md) | [yes](../subjects/Physics/README.md) | 40 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2023 to AY 2026-27 |
| [Physics for Computing Science](../subjects/Physics%20for%20Computing%20Science/syllabus.md) | [yes](../subjects/Physics%20for%20Computing%20Science/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Physics I](../subjects/Physics%20I/syllabus.md) | [yes](../subjects/Physics%20I/README.md) | 4 | B TECH INTEGRATED | 2015-2021 to 2023-2029 |
| [Physics II](../subjects/Physics%20II/syllabus.md) | [yes](../subjects/Physics%20II/README.md) | 8 | B TECH INTEGRATED | 2014-2020 to 2023-2029 |
| [Physics III](../subjects/Physics%20III/syllabus.md) | [yes](../subjects/Physics%20III/README.md) | 11 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Physics IV](../subjects/Physics%20IV/syllabus.md) | [yes](../subjects/Physics%20IV/README.md) | 8 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Physics Pra. Bemad Moos](courses/Physics%20Pra.%20Bemad%20Moos.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Planning and Design](courses/Planning%20and%20Design.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Planning and Design of Environmental Facilities](courses/Planning%20and%20Design%20of%20Environmental%20Facilities.md) | — | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2018-2024 |
| [Plant Simulation](courses/Plant%20Simulation.md) | — | 1 | B TECH | AY 2026-27 |
| [Plant Utilities](../subjects/Plant%20Utilities/syllabus.md) | [yes](../subjects/Plant%20Utilities/README.md) | 6 | MBA Tech | 2015-2020 to 2020-2025 |
| [PLC and Data Acquisition](../subjects/PLC%20and%20Data%20Acquisition/syllabus.md) | [yes](../subjects/PLC%20and%20Data%20Acquisition/README.md) | 8 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2021-22 |
| [PLCs and Instrumentation](../subjects/PLCs%20and%20Instrumentation/syllabus.md) | [yes](../subjects/PLCs%20and%20Instrumentation/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Polymer Technology](courses/Polymer%20Technology.md) | — | 3 | MBA Tech | 2018-2023 to 2020-2025 |
| [Portfolio and Asset Management](../subjects/Portfolio%20and%20Asset%20Management/syllabus.md) | [yes](../subjects/Portfolio%20and%20Asset%20Management/README.md) | 4 | MBA Tech | 2014-2019 to 2015-2020 |
| [Power Electronics](../subjects/Power%20Electronics/syllabus.md) | [yes](../subjects/Power%20Electronics/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2014-15 to 2019-2024 |
| [Power Electronics I](courses/Power%20Electronics%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Power Plant Engineering](courses/Power%20Plant%20Engineering.md) | — | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Power System Operation and Control](../subjects/Power%20System%20Operation%20and%20Control/syllabus.md) | [yes](../subjects/Power%20System%20Operation%20and%20Control/README.md) | 5 | B TECH, MBA Tech | 2015-2020 to AY 2020-21 |
| [Power System Planning and Reliability](../subjects/Power%20System%20Planning%20and%20Reliability/syllabus.md) | [yes](../subjects/Power%20System%20Planning%20and%20Reliability/README.md) | 3 | B TECH | AY 2018-19 to AY 2020-21 |
| [Power System Stability](../subjects/Power%20System%20Stability/syllabus.md) | [yes](../subjects/Power%20System%20Stability/README.md) | 5 | B TECH, MBA Tech | 2015-2020 to AY 2020-21 |
| [Predictive Analysis](../subjects/Predictive%20Analysis/syllabus.md) | [yes](../subjects/Predictive%20Analysis/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Predictive Analytics](../subjects/Predictive%20Analytics/syllabus.md) | [yes](../subjects/Predictive%20Analytics/README.md) | 7 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2024-25 |
| [Predictive Modelling](courses/Predictive%20Modelling.md) | — | 21 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2021-22 |
| [Preparatory Course in English](courses/Preparatory%20Course%20in%20English.md) | — | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Presentation and Communication Techniques](../subjects/Presentation%20and%20Communication%20Techniques/syllabus.md) | [yes](../subjects/Presentation%20and%20Communication%20Techniques/README.md) | 55 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Presentation and Communication Techniques Teachins Scheme Evaluation Scheme](courses/Presentation%20and%20Communication%20Techniques%20Teachins%20Scheme%20Evaluation%20Scheme.md) | — | 1 | B TECH | AY 2016-17 |
| [Prestressed Concrete](../subjects/Prestressed%20Concrete/syllabus.md) | [yes](../subjects/Prestressed%20Concrete/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Principles of Accounting I](../subjects/Principles%20of%20Accounting%20I/syllabus.md) | [yes](../subjects/Principles%20of%20Accounting%20I/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Principles of Accounting II](../subjects/Principles%20of%20Accounting%20II/syllabus.md) | [yes](../subjects/Principles%20of%20Accounting%20II/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2024-25 |
| [Principles of Artificial Intelligence](../subjects/Principles%20of%20Artificial%20Intelligence/syllabus.md) | [yes](../subjects/Principles%20of%20Artificial%20Intelligence/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Principles of Chemical Reactions](../subjects/Principles%20of%20Chemical%20Reactions/syllabus.md) | [yes](../subjects/Principles%20of%20Chemical%20Reactions/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Principles of Communication](courses/Principles%20of%20Communication.md) | — | 3 | B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to 2019-2023 |
| [Principles of Communication (En Ineering](courses/Principles%20of%20Communication%20%28En%20Ineering.md) | — | 1 | B TECH | AY 2013-14 |
| [Principles of Communication 1 Engineering](courses/Principles%20of%20Communication%201%20Engineering.md) | — | 1 | MBA Tech | 2012-2017 |
| [Principles of Communication Engineering](../subjects/Principles%20of%20Communication%20Engineering/syllabus.md) | [yes](../subjects/Principles%20of%20Communication%20Engineering/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, MBA Tech | AY 2012-13 to AY 2018-19 |
| [Principles of Compiler Design](../subjects/Principles%20of%20Compiler%20Design/syllabus.md) | [yes](../subjects/Principles%20of%20Compiler%20Design/README.md) | 11 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2017-2023 |
| [Principles of Cryptography](../subjects/Principles%20of%20Cryptography/syllabus.md) | [yes](../subjects/Principles%20of%20Cryptography/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Principles of Economics and](courses/Principles%20of%20Economics%20and.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Principles of Economics and Management](../subjects/Principles%20of%20Economics%20and%20Management/syllabus.md) | [yes](../subjects/Principles%20of%20Economics%20and%20Management/README.md) | 81 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Principles of Economics I](../subjects/Principles%20of%20Economics%20I/syllabus.md) | [yes](../subjects/Principles%20of%20Economics%20I/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2020-21 to AY 2024-25 |
| [Principles of Economics II](../subjects/Principles%20of%20Economics%20II/syllabus.md) | [yes](../subjects/Principles%20of%20Economics%20II/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2024-25 |
| [Principles of Electrical Engineering](../subjects/Principles%20of%20Electrical%20Engineering/syllabus.md) | [yes](../subjects/Principles%20of%20Electrical%20Engineering/README.md) | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2024-25 |
| [Principles of Electronics Engineering](../subjects/Principles%20of%20Electronics%20Engineering/syllabus.md) | [yes](../subjects/Principles%20of%20Electronics%20Engineering/README.md) | 8 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2023-24 |
| [Principles of Management](../subjects/Principles%20of%20Management/syllabus.md) | [yes](../subjects/Principles%20of%20Management/README.md) | 13 | B TECH, MBA Tech, PGDM | 2016-2021 to AY 2026-27 |
| [Principles of Operating System](courses/Principles%20of%20Operating%20System.md) | — | 1 | B TECH INTEGRATED | 2019-2025 |
| [Principles of Operating System Module](courses/Principles%20of%20Operating%20System%20Module.md) | — | 1 | B TECH INTEGRATED | 2018-2024 |
| [Principles of Valuation in Real Estate](../subjects/Principles%20of%20Valuation%20in%20Real%20Estate/syllabus.md) | [yes](../subjects/Principles%20of%20Valuation%20in%20Real%20Estate/README.md) | 2 | PGDM | AY 2016-17 to AY 2018-19 |
| [Probabilistic Robotics](courses/Probabilistic%20Robotics.md) | — | 3 | M Tech | 2018-2020 to 2020-2022 |
| [Probability and Random Processes](../subjects/Probability%20and%20Random%20Processes/syllabus.md) | [yes](../subjects/Probability%20and%20Random%20Processes/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2018-19 |
| [Probability and Random Processes I](courses/Probability%20and%20Random%20Processes%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Probability and Random Variables](../subjects/Probability%20and%20Random%20Variables/syllabus.md) | [yes](../subjects/Probability%20and%20Random%20Variables/README.md) | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2023-24 |
| [Probability and Statistics](../subjects/Probability%20and%20Statistics/syllabus.md) | [yes](../subjects/Probability%20and%20Statistics/README.md) | 52 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2017-2019 to AY 2026-27 |
| [Probability and Stochastic Processes](../subjects/Probability%20and%20Stochastic%20Processes/syllabus.md) | [yes](../subjects/Probability%20and%20Stochastic%20Processes/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2020-21 |
| [Probability Theory and Statistical Methods](courses/Probability%20Theory%20and%20Statistical%20Methods.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Probability Theory and Stochastic Processes](courses/Probability%20Theory%20and%20Stochastic%20Processes.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to 2020-2025 |
| [Process Calculation II](../subjects/Process%20Calculation%20II/syllabus.md) | [yes](../subjects/Process%20Calculation%20II/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Process Calculations I](../subjects/Process%20Calculations%20I/syllabus.md) | [yes](../subjects/Process%20Calculations%20I/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Process Equipment and Accessories](courses/Process%20Equipment%20and%20Accessories.md) | — | 1 | MBA Tech | 2015-2020 |
| [Process Equipment and Accessories Design](../subjects/Process%20Equipment%20and%20Accessories%20Design/syllabus.md) | [yes](../subjects/Process%20Equipment%20and%20Accessories%20Design/README.md) | 5 | MBA Tech | 2016-2021 to 2020-2025 |
| [Process Optimization](courses/Process%20Optimization.md) | — | 1 | MBA Tech | 2016-2021 |
| [Process Optimization and Simulation](../subjects/Process%20Optimization%20and%20Simulation/syllabus.md) | [yes](../subjects/Process%20Optimization%20and%20Simulation/README.md) | 2 | MBA Tech | 2014-2019 to 2015-2020 |
| [Process Simulate Standalone Basic Robotic Simulation](courses/Process%20Simulate%20Standalone%20Basic%20Robotic%20Simulation.md) | — | 1 | B TECH | AY 2025-26 |
| [Process Simulation](../subjects/Process%20Simulation/syllabus.md) | [yes](../subjects/Process%20Simulation/README.md) | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Product Design](courses/Product%20Design.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Product Design and Development](../subjects/Product%20Design%20and%20Development/syllabus.md) | [yes](../subjects/Product%20Design%20and%20Development/README.md) | 35 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2025-26 |
| [Product Life Cycle Management](courses/Product%20Life%20Cycle%20Management.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Product Realization](courses/Product%20Realization.md) | — | 1 | B TECH | AY 2025-26 |
| [Production Drawing](../subjects/Production%20Drawing/syllabus.md) | [yes](../subjects/Production%20Drawing/README.md) | 1 | DIPLOMA | 2024-2027 |
| [Production Management](../subjects/Production%20Management/syllabus.md) | [yes](../subjects/Production%20Management/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Production Technology](../subjects/Production%20Technology/syllabus.md) | [yes](../subjects/Production%20Technology/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Professional Communication and Personal Effectiveness](courses/Professional%20Communication%20and%20Personal%20Effectiveness.md) | — | 1 | PGDM | AY 2018-19 |
| [Professional Communication and Soft Skills](../subjects/Professional%20Communication%20and%20Soft%20Skills/syllabus.md) | [yes](../subjects/Professional%20Communication%20and%20Soft%20Skills/README.md) | 2 | B TECH | AY 2024-25 to AY 2025-26 |
| [Professional Ethics](courses/Professional%20Ethics.md) | — | 58 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to 2025-2027 |
| [Professional Ethics and Legal Aspects](../subjects/Professional%20Ethics%20and%20Legal%20Aspects/syllabus.md) | [yes](../subjects/Professional%20Ethics%20and%20Legal%20Aspects/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2021-22 |
| [Professional Skills](courses/Professional%20Skills.md) | — | 6 | M Tech | 2024-2026 to 2026-2028 |
| [Programing for Analytics I](courses/Programing%20for%20Analytics%20I.md) | — | 1 | MBA Tech | 2014-2019 |
| [Programming for Analytics](../subjects/Programming%20for%20Analytics/syllabus.md) | [yes](../subjects/Programming%20for%20Analytics/README.md) | 51 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2014-2018 to 2026-2028 |
| [Programming for Data Analysis](courses/Programming%20for%20Data%20Analysis.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Programming for Problem](courses/Programming%20for%20Problem.md) | — | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2020-21 |
| [Programming for Problem Solving](../subjects/Programming%20for%20Problem%20Solving/syllabus.md) | [yes](../subjects/Programming%20for%20Problem%20Solving/README.md) | 25 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2024-25 |
| [Programming in Java](../subjects/Programming%20in%20Java/syllabus.md) | [yes](../subjects/Programming%20in%20Java/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to 2016-2020 |
| [Programming inJAVA](courses/Programming%20inJAVA.md) | — | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2016-2022 |
| [Programming Lab-IH(Proposed)](courses/Programming%20Lab-IH%28Proposed%29.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Programming Lab-III(Proposed)](courses/Programming%20Lab-III%28Proposed%29.md) | — | 1 | B TECH WORK IN PROCESS | 2016-2020 |
| [Programming Laboratory](courses/Programming%20Laboratory.md) | — | 2 | B TECH INTEGRATED, MBA Tech | 2016-2021 to 2018-2024 |
| [Programming Laboratory I](courses/Programming%20Laboratory%20I.md) | — | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to 2019-2025 |
| [Programming Laboratory II](courses/Programming%20Laboratory%20II.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2016-2020 to 2019-2025 |
| [Programming Laboratory III](courses/Programming%20Laboratory%20III.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2015-2020 to 2017-2022 |
| [Programming Language](courses/Programming%20Language.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Programming with Python](courses/Programming%20with%20Python.md) | — | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Programming Workshop](courses/Programming%20Workshop.md) | — | 17 | B TECH, B TECH WORK IN PROCESS, MBA Tech, MCA | AY 2012-13 to 2019-2022 |
| [Programming Workshop I](courses/Programming%20Workshop%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Project](courses/Project.md) | — | 35 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MCA | 2013-2017 to AY 2025-26 |
| [Project and Process Engineering](../subjects/Project%20and%20Process%20Engineering/syllabus.md) | [yes](../subjects/Project%20and%20Process%20Engineering/README.md) | 3 | MBA Tech | 2015-2020 to 2017-2022 |
| [Project Appraisal and Financing](../subjects/Project%20Appraisal%20and%20Financing/syllabus.md) | [yes](../subjects/Project%20Appraisal%20and%20Financing/README.md) | 6 | MBA Tech | 2019-2024 to 2021-2026 |
| [Project Closure](../subjects/Project%20Closure/syllabus.md) | [yes](../subjects/Project%20Closure/README.md) | 1 | PGDM | AY 2018-19 |
| [Project Evaluation I](courses/Project%20Evaluation%20I.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2024-25 |
| [Project Evaluation– II](courses/Project%20Evaluation%E2%80%93%20II.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2024-25 |
| [Project I](courses/Project%20I.md) | — | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Project II](courses/Project%20II.md) | — | 31 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2021-22 |
| [Project Infrastructure and Finances](../subjects/Project%20Infrastructure%20and%20Finances/syllabus.md) | [yes](../subjects/Project%20Infrastructure%20and%20Finances/README.md) | 10 | MBA Tech | 2014-2019 to 2016-2021 |
| [Project Management](../subjects/Project%20Management/syllabus.md) | [yes](../subjects/Project%20Management/README.md) | 60 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA, PGDM | 2013-2016 to AY 2025-26 |
| [Project Methodology](courses/Project%20Methodology.md) | — | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Project Part](courses/Project%20Part.md) | — | 1 | B TECH | AY 2013-14 |
| [Project Part I](courses/Project%20Part%20I.md) | — | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2012-13 to AY 2020-21 |
| [Project Part II](courses/Project%20Part%20II.md) | — | 16 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | AY 2012-13 to AY 2020-21 |
| [Project Phase](courses/Project%20Phase.md) | — | 10 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2020-21 |
| [Project Phase 11 I](courses/Project%20Phase%2011%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Project Phase I](courses/Project%20Phase%20I.md) | — | 36 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2022 |
| [Project Phase II](courses/Project%20Phase%20II.md) | — | 30 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2021-22 |
| [Project Procurement](courses/Project%20Procurement.md) | — | 2 | MBA Tech | 2014-2019 |
| [Project Procurement Management](../subjects/Project%20Procurement%20Management/syllabus.md) | [yes](../subjects/Project%20Procurement%20Management/README.md) | 13 | MBA Tech | 2015-2020 to 2021-2026 |
| [Project Risk Management](../subjects/Project%20Risk%20Management/syllabus.md) | [yes](../subjects/Project%20Risk%20Management/README.md) | 14 | MBA Tech | 2014-2019 to 2021-2026 |
| [Project Workshop](courses/Project%20Workshop.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2014-15 |
| [Project — Part III](courses/Project%20%E2%80%94%20Part%20III.md) | — | 1 | B TECH | AY 2012-13 |
| [Projects on Building Planning and Design](courses/Projects%20on%20Building%20Planning%20and%20Design.md) | — | 3 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2019 |
| [Projed Workshop I](courses/Projed%20Workshop%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Python for Data Analysis](../subjects/Python%20for%20Data%20Analysis/syllabus.md) | [yes](../subjects/Python%20for%20Data%20Analysis/README.md) | 8 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2023-24 |
| [Python for Mechanical Engineers](courses/Python%20for%20Mechanical%20Engineers.md) | — | 7 | B TECH, B TECH INTEGRATED | 2020-2026 to AY 2026-27 |
| [Python Fundamentals](../subjects/Python%20Fundamentals/syllabus.md) | [yes](../subjects/Python%20Fundamentals/README.md) | 3 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Python Programming](../subjects/Python%20Programming/syllabus.md) | [yes](../subjects/Python%20Programming/README.md) | 38 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech, MCA | 2015-2020 to AY 2023-24 |
| [Python Programming Essentials](courses/Python%20Programming%20Essentials.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Python Programming for Analytics](courses/Python%20Programming%20for%20Analytics.md) | — | 3 | M Tech | 2021-2023 to 2023-2025 |
| [Quality Control](courses/Quality%20Control.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Quality Management](../subjects/Quality%20Management/syllabus.md) | [yes](../subjects/Quality%20Management/README.md) | 2 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Quantitative Finance](../subjects/Quantitative%20Finance/syllabus.md) | [yes](../subjects/Quantitative%20Finance/README.md) | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Quantitative Insights into Supply Chain and Operations](../subjects/Quantitative%20Insights%20into%20Supply%20Chain%20and%20Operations/syllabus.md) | [yes](../subjects/Quantitative%20Insights%20into%20Supply%20Chain%20and%20Operations/README.md) | 5 | M Tech | 2021-2023 to 2023-2025 |
| [Quantitative Techniques](../subjects/Quantitative%20Techniques/syllabus.md) | [yes](../subjects/Quantitative%20Techniques/README.md) | 26 | MBA Tech | 2014-2019 to 2023-2028 |
| [Quantity Surveying and Estimation](../subjects/Quantity%20Surveying%20and%20Estimation/syllabus.md) | [yes](../subjects/Quantity%20Surveying%20and%20Estimation/README.md) | 1 | PGDM | — |
| [Quantity Surveying and Valuation](../subjects/Quantity%20Surveying%20and%20Valuation/syllabus.md) | [yes](../subjects/Quantity%20Surveying%20and%20Valuation/README.md) | 2 | B TECH | AY 2013-14 to AY 2014-15 |
| [Quantity Surveying, Estimation and Valuation](../subjects/Quantity%20Surveying%2C%20Estimation%20and%20Valuation/syllabus.md) | [yes](../subjects/Quantity%20Surveying%2C%20Estimation%20and%20Valuation/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2025-26 |
| [Quantum and Statistical Physics](../subjects/Quantum%20and%20Statistical%20Physics/syllabus.md) | [yes](../subjects/Quantum%20and%20Statistical%20Physics/README.md) | 8 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2023-24 |
| [Quantum and Statistical Physics Oaule Sowe](courses/Quantum%20and%20Statistical%20Physics%20Oaule%20Sowe.md) | — | 1 | B TECH WORK IN PROCESS | 2021-2025 |
| [Quantum Computation and Quantum](courses/Quantum%20Computation%20and%20Quantum.md) | — | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Quantum Computing and Technologies](../subjects/Quantum%20Computing%20and%20Technologies/syllabus.md) | [yes](../subjects/Quantum%20Computing%20and%20Technologies/README.md) | 3 | B TECH | AY 2023-24 to AY 2024-25 |
| [Quantum Machine Learning](courses/Quantum%20Machine%20Learning.md) | — | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2026 to AY 2025-26 |
| [Quantum Physics](../subjects/Quantum%20Physics/syllabus.md) | [yes](../subjects/Quantum%20Physics/README.md) | 1 | B TECH | AY 2025-26 |
| [R and Tableau Programming](courses/R%20and%20Tableau%20Programming.md) | — | 1 | M Tech | 2017-2019 |
| [R R Studio SPSS and Tableau Programming](../subjects/R%20R%20Studio%20SPSS%20and%20Tableau%20Programming/syllabus.md) | [yes](../subjects/R%20R%20Studio%20SPSS%20and%20Tableau%20Programming/README.md) | 3 | M Tech | 2015-2017 to 2016-2018 |
| [R/R Studio and Tableau Programming](courses/R-R%20Studio%20and%20Tableau%20Programming.md) | — | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Radiating Systems and Wave](courses/Radiating%20Systems%20and%20Wave.md) | — | 1 | B TECH | AY 2019-20 |
| [Radiating Systems and Wave Propagation](../subjects/Radiating%20Systems%20and%20Wave%20Propagation/syllabus.md) | [yes](../subjects/Radiating%20Systems%20and%20Wave%20Propagation/README.md) | 8 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to 2017-2022 |
| [Random Processes and Estimation Techniques](../subjects/Random%20Processes%20and%20Estimation%20Techniques/syllabus.md) | [yes](../subjects/Random%20Processes%20and%20Estimation%20Techniques/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Rapid Prototyping and Tooling](../subjects/Rapid%20Prototyping%20and%20Tooling/syllabus.md) | [yes](../subjects/Rapid%20Prototyping%20and%20Tooling/README.md) | 2 | B TECH | AY 2014-15 to AY 2015-16 |
| [Reaction Kinetics](../subjects/Reaction%20Kinetics/syllabus.md) | [yes](../subjects/Reaction%20Kinetics/README.md) | 4 | MBA Tech | 2015-2020 to 2020-2025 |
| [Real Estate Investment](../subjects/Real%20Estate%20Investment/syllabus.md) | [yes](../subjects/Real%20Estate%20Investment/README.md) | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Real Estate Investment Module'](courses/Real%20Estate%20Investment%20Module%27.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Real Estate Valuation](../subjects/Real%20Estate%20Valuation/syllabus.md) | [yes](../subjects/Real%20Estate%20Valuation/README.md) | 1 | PGDM | AY 2018-19 |
| [Recommendation Systems](../subjects/Recommendation%20Systems/syllabus.md) | [yes](../subjects/Recommendation%20Systems/README.md) | 6 | B TECH, Current electives 2026-27, MBA Tech | 2021-2026 to AY 2026-27 |
| [Refrigeration and Air](courses/Refrigeration%20and%20Air.md) | — | 1 | B TECH | AY 2015-16 |
| [Refrigeration and Air Conditioning](../subjects/Refrigeration%20and%20Air%20Conditioning/syllabus.md) | [yes](../subjects/Refrigeration%20and%20Air%20Conditioning/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2020-21 |
| [Refrigerationand Air Conditioning I](courses/Refrigerationand%20Air%20Conditioning%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Reinforcement Learning](../subjects/Reinforcement%20Learning/syllabus.md) | [yes](../subjects/Reinforcement%20Learning/README.md) | 20 | B TECH, B TECH INTEGRATED, M Tech, MBA Tech | 2018-2024 to AY 2026-27 |
| [Reliabili](courses/Reliabili.md) | — | 1 | B TECH | AY 2013-14 |
| [Reliability Engineering](courses/Reliability%20Engineering.md) | — | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [Remote Sensing, GIS](courses/Remote%20Sensing%2C%20GIS.md) | — | 6 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Renewable Energy](../subjects/Renewable%20Energy/syllabus.md) | [yes](../subjects/Renewable%20Energy/README.md) | 2 | MBA Tech | 2016-2021 to 2018-2023 |
| [Renewable Energy Sources](../subjects/Renewable%20Energy%20Sources/syllabus.md) | [yes](../subjects/Renewable%20Energy%20Sources/README.md) | 42 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2019 to AY 2026-27 |
| [Repairs and](courses/Repairs%20and.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [Repairs and Restoration of Structures](courses/Repairs%20and%20Restoration%20of%20Structures.md) | — | 4 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2023 to 2019-2025 |
| [Research and Publication Ethics](courses/Research%20and%20Publication%20Ethics.md) | — | 4 | Ph D | 2022-2023 to 2025-2026 |
| [Research Methodology](../subjects/Research%20Methodology/syllabus.md) | [yes](../subjects/Research%20Methodology/README.md) | 53 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, Ph D | 2013-2017 to AY 2025-26 |
| [Research Project](courses/Research%20Project.md) | — | 10 | M Tech, MBA Tech | 2015-2020 to 2023-2025 |
| [Research Project – I](courses/Research%20Project%20%E2%80%93%20I.md) | — | 4 | M Tech | 2020-2022 to 2023-2025 |
| [Research Project – II](courses/Research%20Project%20%E2%80%93%20II.md) | — | 4 | M Tech | 2020-2022 to 2023-2025 |
| [Reverse Engineering and Malware Analysis](../subjects/Reverse%20Engineering%20and%20Malware%20Analysis/syllabus.md) | [yes](../subjects/Reverse%20Engineering%20and%20Malware%20Analysis/README.md) | 5 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2024 to AY 2025-26 |
| [RF Circuit Design](../subjects/RF%20Circuit%20Design/syllabus.md) | [yes](../subjects/RF%20Circuit%20Design/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2016-2022 |
| [RF Circuit Design I](courses/RF%20Circuit%20Design%20I.md) | — | 1 | MBA Tech | 2011-2016 |
| [Risk and Reliability Engineering](../subjects/Risk%20and%20Reliability%20Engineering/syllabus.md) | [yes](../subjects/Risk%20and%20Reliability%20Engineering/README.md) | 2 | B TECH | AY 2012-13 |
| [Risk in Construction](courses/Risk%20in%20Construction.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Risk Management](../subjects/Risk%20Management/syllabus.md) | [yes](../subjects/Risk%20Management/README.md) | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Robotic Process Automation](../subjects/Robotic%20Process%20Automation/syllabus.md) | [yes](../subjects/Robotic%20Process%20Automation/README.md) | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2024 to AY 2026-27 |
| [Robotic Systems Design](../subjects/Robotic%20Systems%20Design/syllabus.md) | [yes](../subjects/Robotic%20Systems%20Design/README.md) | 6 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2025-26 |
| [Robotics](../subjects/Robotics/syllabus.md) | [yes](../subjects/Robotics/README.md) | 62 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Robotics and Automation](../subjects/Robotics%20and%20Automation/syllabus.md) | [yes](../subjects/Robotics%20and%20Automation/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MCA | 2017-2023 to AY 2024-25 |
| [Rock Mechanics](../subjects/Rock%20Mechanics/syllabus.md) | [yes](../subjects/Rock%20Mechanics/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to AY 2026-27 |
| [Safcty Int Onstruction](courses/Safcty%20Int%20Onstruction.md) | — | 1 | B TECH | — |
| [Safety Health and Environmental Engineering](courses/Safety%20Health%20and%20Environmental%20Engineering.md) | — | 6 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2018-19 |
| [Sales and Distribution Management](../subjects/Sales%20and%20Distribution%20Management/syllabus.md) | [yes](../subjects/Sales%20and%20Distribution%20Management/README.md) | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Sales and Distribution Management Module Chde](courses/Sales%20and%20Distribution%20Management%20Module%20Chde.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [SAS Programming](../subjects/SAS%20Programming/syllabus.md) | [yes](../subjects/SAS%20Programming/README.md) | 3 | M Tech | 2015-2017 to 2016-2018 |
| [Satellite Communication](courses/Satellite%20Communication.md) | — | 4 | B TECH, MBA Tech | 2020-2025 to AY 2025-26 |
| [Satellite Communication and Radar](../subjects/Satellite%20Communication%20and%20Radar/syllabus.md) | [yes](../subjects/Satellite%20Communication%20and%20Radar/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2020-21 |
| [Satellite Communication and Radar I](courses/Satellite%20Communication%20and%20Radar%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Science, Technology and Society](../subjects/Science%2C%20Technology%20and%20Society/syllabus.md) | [yes](../subjects/Science%2C%20Technology%20and%20Society/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | AY 2021-22 to AY 2024-25 |
| [Secure Coding](courses/Secure%20Coding.md) | — | 5 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Security Analysis](../subjects/Security%20Analysis/syllabus.md) | [yes](../subjects/Security%20Analysis/README.md) | 10 | MBA Tech | 2014-2019 to 2019-2024 |
| [Security Analysis Module](courses/Security%20Analysis%20Module.md) | — | 1 | MBA Tech | 2015-2020 |
| [Security Essentials in Applied AI](../subjects/Security%20Essentials%20in%20Applied%20AI/syllabus.md) | [yes](../subjects/Security%20Essentials%20in%20Applied%20AI/README.md) | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Security of Data Science](courses/Security%20of%20Data%20Science.md) | — | 3 | M Tech | 2024-2026 to 2026-2028 |
| [Seminar I](courses/Seminar%20I.md) | — | 2 | MBA Tech | 2014-2019 to 2015-2020 |
| [Seminar Research/Survey Manuscript](courses/Seminar%20Research-Survey%20Manuscript.md) | — | 1 | Ph D | 2022-2023 |
| [Sensors](../subjects/Sensors/syllabus.md) | [yes](../subjects/Sensors/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Sensors and Transducers](../subjects/Sensors%20and%20Transducers/syllabus.md) | [yes](../subjects/Sensors%20and%20Transducers/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Sensors in Wearable Technology](../subjects/Sensors%20in%20Wearable%20Technology/syllabus.md) | [yes](../subjects/Sensors%20in%20Wearable%20Technology/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2017-2023 to 2019-2023 |
| [Sentiment, Web and Text Analytics](../subjects/Sentiment%2C%20Web%20and%20Text%20Analytics/syllabus.md) | [yes](../subjects/Sentiment%2C%20Web%20and%20Text%20Analytics/README.md) | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Service Oriented Architecture](../subjects/Service%20Oriented%20Architecture/syllabus.md) | [yes](../subjects/Service%20Oriented%20Architecture/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2026-27 |
| [Services Marketing](../subjects/Services%20Marketing/syllabus.md) | [yes](../subjects/Services%20Marketing/README.md) | 14 | MBA Tech | 2014-2019 to 2021-2026 |
| [Services Operations Management](../subjects/Services%20Operations%20Management/syllabus.md) | [yes](../subjects/Services%20Operations%20Management/README.md) | 12 | MBA Tech | 2014-2019 to 2021-2026 |
| [Services Operations Management Modulé](courses/Services%20Operations%20Management%20Modul%C3%A9.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Services Science and Service Operational](courses/Services%20Science%20and%20Service%20Operational.md) | — | 6 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Signal and Image Processing](../subjects/Signal%20and%20Image%20Processing/syllabus.md) | [yes](../subjects/Signal%20and%20Image%20Processing/README.md) | 7 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2026-27 |
| [Signals and Systems](../subjects/Signals%20and%20Systems/syllabus.md) | [yes](../subjects/Signals%20and%20Systems/README.md) | 65 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2026-27 |
| [Signals and Systems I](courses/Signals%20and%20Systems%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Simulated Mixed Reality](../subjects/Simulated%20Mixed%20Reality/syllabus.md) | [yes](../subjects/Simulated%20Mixed%20Reality/README.md) | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Simulation Modeling](../subjects/Simulation%20Modeling/syllabus.md) | [yes](../subjects/Simulation%20Modeling/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Simulation Modelling and Analysis](courses/Simulation%20Modelling%20and%20Analysis.md) | — | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Simulation of Electrical Circuits](courses/Simulation%20of%20Electrical%20Circuits.md) | — | 2 | B TECH | AY 2015-16 to AY 2017-18 |
| [Smart Antennas](../subjects/Smart%20Antennas/syllabus.md) | [yes](../subjects/Smart%20Antennas/README.md) | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Smart Cities](../subjects/Smart%20Cities/syllabus.md) | [yes](../subjects/Smart%20Cities/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Smart Cities Planning and Technology](../subjects/Smart%20Cities%20Planning%20and%20Technology/syllabus.md) | [yes](../subjects/Smart%20Cities%20Planning%20and%20Technology/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2018-2024 |
| [Smart Grids](../subjects/Smart%20Grids/syllabus.md) | [yes](../subjects/Smart%20Grids/README.md) | 4 | B TECH, MBA Tech | 2015-2020 to AY 2020-21 |
| [Smart Manufacturing and Internet of Things](../subjects/Smart%20Manufacturing%20and%20Internet%20of%20Things/syllabus.md) | [yes](../subjects/Smart%20Manufacturing%20and%20Internet%20of%20Things/README.md) | 9 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2026-27 |
| [Smart Materials](courses/Smart%20Materials.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Smart System Communication](../subjects/Smart%20System%20Communication/syllabus.md) | [yes](../subjects/Smart%20System%20Communication/README.md) | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Social and Life Skills](courses/Social%20and%20Life%20Skills.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Social Media and Web Analytics](../subjects/Social%20Media%20and%20Web%20Analytics/syllabus.md) | [yes](../subjects/Social%20Media%20and%20Web%20Analytics/README.md) | 2 | MBA Tech | 2021-2026 |
| [Soft Computing](../subjects/Soft%20Computing/syllabus.md) | [yes](../subjects/Soft%20Computing/README.md) | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2024 |
| [Software Architecture](../subjects/Software%20Architecture/syllabus.md) | [yes](../subjects/Software%20Architecture/README.md) | 15 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2019-2023 |
| [Software Design with UML](../subjects/Software%20Design%20with%20UML/syllabus.md) | [yes](../subjects/Software%20Design%20with%20UML/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Software Engineering](../subjects/Software%20Engineering/syllabus.md) | [yes](../subjects/Software%20Engineering/README.md) | 66 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to AY 2026-27 |
| [Software Engineering I I](courses/Software%20Engineering%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Software Project Management](../subjects/Software%20Project%20Management/syllabus.md) | [yes](../subjects/Software%20Project%20Management/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2024-25 |
| [Software Quality Assurance](../subjects/Software%20Quality%20Assurance/syllabus.md) | [yes](../subjects/Software%20Quality%20Assurance/README.md) | 19 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to AY 2025-26 |
| [Software Quality Assurance and Testing](../subjects/Software%20Quality%20Assurance%20and%20Testing/syllabus.md) | [yes](../subjects/Software%20Quality%20Assurance%20and%20Testing/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2017 to 2019-2024 |
| [Software Security](../subjects/Software%20Security/syllabus.md) | [yes](../subjects/Software%20Security/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Software Teamcenter and NX CAD](courses/Software%20Teamcenter%20and%20NX%20CAD.md) | — | 2 | B TECH | AY 2025-26 to AY 2026-27 |
| [Software Testing](../subjects/Software%20Testing/syllabus.md) | [yes](../subjects/Software%20Testing/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2025-26 |
| [Soil Dynamics](../subjects/Soil%20Dynamics/syllabus.md) | [yes](../subjects/Soil%20Dynamics/README.md) | 11 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to 2019-2024 |
| [Soil Investigation and Instrumentation](courses/Soil%20Investigation%20and%20Instrumentation.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Soil Mechanics](../subjects/Soil%20Mechanics/syllabus.md) | [yes](../subjects/Soil%20Mechanics/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to AY 2025-26 |
| [Solid and Hazardous Waste Management](courses/Solid%20and%20Hazardous%20Waste%20Management.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Solid Fluid Mechanical Operations](../subjects/Solid%20Fluid%20Mechanical%20Operations/syllabus.md) | [yes](../subjects/Solid%20Fluid%20Mechanical%20Operations/README.md) | 4 | MBA Tech | 2016-2021 to 2020-2025 |
| [Solid Mechanics](../subjects/Solid%20Mechanics/syllabus.md) | [yes](../subjects/Solid%20Mechanics/README.md) | 5 | B TECH INTEGRATED, DIPLOMA | 2020-2026 to 2024-2027 |
| [Speech and Natural Language Processing](../subjects/Speech%20and%20Natural%20Language%20Processing/syllabus.md) | [yes](../subjects/Speech%20and%20Natural%20Language%20Processing/README.md) | 6 | B TECH, B TECH INTEGRATED, MBA Tech | 2021-2026 to AY 2025-26 |
| [Speech Processing](../subjects/Speech%20Processing/syllabus.md) | [yes](../subjects/Speech%20Processing/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2025-26 |
| [Speech Processing I](courses/Speech%20Processing%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Speech Recognition](../subjects/Speech%20Recognition/syllabus.md) | [yes](../subjects/Speech%20Recognition/README.md) | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Spreadsheet Modelling](courses/Spreadsheet%20Modelling.md) | — | 13 | MBA Tech | 2018-2023 to 2023-2028 |
| [Spreadsheet-Based Data Analysis](courses/Spreadsheet-Based%20Data%20Analysis.md) | — | 3 | B TECH, B TECH INTEGRATED, MBA Tech | 2023-2029 to AY 2026-27 |
| [Statistical Learning](../subjects/Statistical%20Learning/syllabus.md) | [yes](../subjects/Statistical%20Learning/README.md) | 6 | M Tech | 2018-2020 to 2023-2025 |
| [Statistical Method I](../subjects/Statistical%20Method%20I/syllabus.md) | [yes](../subjects/Statistical%20Method%20I/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | AY 2018-19 to AY 2019-20 |
| [Statistical Methods](../subjects/Statistical%20Methods/syllabus.md) | [yes](../subjects/Statistical%20Methods/README.md) | 10 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2024-25 |
| [Statistical Methods II](../subjects/Statistical%20Methods%20II/syllabus.md) | [yes](../subjects/Statistical%20Methods%20II/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Statistical Methods of Analysis](../subjects/Statistical%20Methods%20of%20Analysis/syllabus.md) | [yes](../subjects/Statistical%20Methods%20of%20Analysis/README.md) | 14 | B TECH WORK IN PROCESS, MBA Tech, Ph D | 2018-2022 to 2025-2026 |
| [Statistical Modelling](courses/Statistical%20Modelling.md) | — | 1 | B TECH WORK IN PROCESS | 2019-2023 |
| [Statistical Structures in Data](courses/Statistical%20Structures%20in%20Data.md) | — | 1 | B TECH | AY 2021-22 |
| [Statistical Structures in Data and Inference](../subjects/Statistical%20Structures%20in%20Data%20and%20Inference/syllabus.md) | [yes](../subjects/Statistical%20Structures%20in%20Data%20and%20Inference/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Statistics and Numerical Methods](../subjects/Statistics%20and%20Numerical%20Methods/syllabus.md) | [yes](../subjects/Statistics%20and%20Numerical%20Methods/README.md) | 1 | B TECH INTEGRATED | 2019-2025 |
| [Statistics, Probability and Calculus](../subjects/Statistics%2C%20Probability%20and%20Calculus/syllabus.md) | [yes](../subjects/Statistics%2C%20Probability%20and%20Calculus/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2021-2025 to AY 2024-25 |
| [Stochastic Image Processing](courses/Stochastic%20Image%20Processing.md) | — | 3 | M Tech | 2021-2023 to 2023-2025 |
| [Stochastic Processes](../subjects/Stochastic%20Processes/syllabus.md) | [yes](../subjects/Stochastic%20Processes/README.md) | 2 | B TECH | AY 2024-25 to AY 2025-26 |
| [Stochastic Processes and Applications](../subjects/Stochastic%20Processes%20and%20Applications/syllabus.md) | [yes](../subjects/Stochastic%20Processes%20and%20Applications/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to AY 2025-26 |
| [Strategic Management](../subjects/Strategic%20Management/syllabus.md) | [yes](../subjects/Strategic%20Management/README.md) | 11 | MBA Tech | 2014-2019 to 2021-2026 |
| [Strength of Materials](../subjects/Strength%20of%20Materials/syllabus.md) | [yes](../subjects/Strength%20of%20Materials/README.md) | 61 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Strength of Materials and Fabrication](../subjects/Strength%20of%20Materials%20and%20Fabrication/syllabus.md) | [yes](../subjects/Strength%20of%20Materials%20and%20Fabrication/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Strength of Materials I](courses/Strength%20of%20Materials%20I.md) | — | 2 | B TECH, MBA Tech | 2012-2017 to AY 2013-14 |
| [Strength of Materials Teachin Scheme](courses/Strength%20of%20Materials%20Teachin%20Scheme.md) | — | 1 | MBA Tech | 2012-2017 |
| [Structural Analysis](courses/Structural%20Analysis.md) | — | 4 | B TECH, MBA Tech | 2012-2017 to AY 2019-20 |
| [Structural Analysis I](../subjects/Structural%20Analysis%20I/syllabus.md) | [yes](../subjects/Structural%20Analysis%20I/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2018 to AY 2018-19 |
| [Structural Analysis II](../subjects/Structural%20Analysis%20II/syllabus.md) | [yes](../subjects/Structural%20Analysis%20II/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2018-2024 |
| [Structural Dynamics](../subjects/Structural%20Dynamics/syllabus.md) | [yes](../subjects/Structural%20Dynamics/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2020 to 2019-2024 |
| [Studio on Construction Project Management](courses/Studio%20on%20Construction%20Project%20Management.md) | — | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Study of Emerging Technologies](courses/Study%20of%20Emerging%20Technologies.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2015-16 |
| [Study of Technology Trends](courses/Study%20of%20Technology%20Trends.md) | — | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to AY 2020-21 |
| [Supervisory Control and Data Acquisition](../subjects/Supervisory%20Control%20and%20Data%20Acquisition/syllabus.md) | [yes](../subjects/Supervisory%20Control%20and%20Data%20Acquisition/README.md) | 14 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Supplementary Instructions on Water Resources](courses/Supplementary%20Instructions%20on%20Water%20Resources.md) | — | 2 | MBA Tech | 2018-2023 to 2019-2024 |
| [Supplementary Instructions on Water Resources and Environmental Engineering](courses/Supplementary%20Instructions%20on%20Water%20Resources%20and%20Environmental%20Engineering.md) | — | 2 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2018-2022 to 2019-2025 |
| [Supply Chain Analytics](../subjects/Supply%20Chain%20Analytics/syllabus.md) | [yes](../subjects/Supply%20Chain%20Analytics/README.md) | 24 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, M Tech, MBA Tech | 2018-2022 to AY 2026-27 |
| [Supply Chain and](courses/Supply%20Chain%20and.md) | — | 3 | MBA Tech | 2015-2020 |
| [Supply Chain and Logistics Management](../subjects/Supply%20Chain%20and%20Logistics%20Management/syllabus.md) | [yes](../subjects/Supply%20Chain%20and%20Logistics%20Management/README.md) | 8 | MBA Tech | 2014-2019 to 2020-2025 |
| [Supply Chain Management](../subjects/Supply%20Chain%20Management/syllabus.md) | [yes](../subjects/Supply%20Chain%20Management/README.md) | 1 | MBA Tech | 2020-2025 |
| [Surveying](../subjects/Surveying/syllabus.md) | [yes](../subjects/Surveying/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2026-27 |
| [Surveying I](../subjects/Surveying%20I/syllabus.md) | [yes](../subjects/Surveying%20I/README.md) | 10 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2019-2025 |
| [Surveying II](../subjects/Surveying%20II/syllabus.md) | [yes](../subjects/Surveying%20II/README.md) | 4 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | AY 2013-14 to 2018-2024 |
| [Sustainable Business Management Practices](../subjects/Sustainable%20Business%20Management%20Practices/syllabus.md) | [yes](../subjects/Sustainable%20Business%20Management%20Practices/README.md) | 5 | MBA Tech | 2019-2024 to 2021-2026 |
| [Sustainable Energy Systems](courses/Sustainable%20Energy%20Systems.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Sustainable Energy Technologies](../subjects/Sustainable%20Energy%20Technologies/syllabus.md) | [yes](../subjects/Sustainable%20Energy%20Technologies/README.md) | 6 | B TECH, MBA Tech | 2018-2023 to AY 2024-25 |
| [Switchgear and Protection](../subjects/Switchgear%20and%20Protection/syllabus.md) | [yes](../subjects/Switchgear%20and%20Protection/README.md) | 1 | MBA Tech | 2016-2021 |
| [System Administration](courses/System%20Administration.md) | — | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to AY 2025-26 |
| [System Programming](../subjects/System%20Programming/syllabus.md) | [yes](../subjects/System%20Programming/README.md) | 10 | B TECH INTEGRATED, B TECH WORK IN PROCESS | 2013-2017 to 2020-2026 |
| [System Security](../subjects/System%20Security/syllabus.md) | [yes](../subjects/System%20Security/README.md) | 17 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2025 |
| [System Security I](courses/System%20Security%20I.md) | — | 1 | B TECH | — |
| [Systems Analysis and Design](../subjects/Systems%20Analysis%20and%20Design/syllabus.md) | [yes](../subjects/Systems%20Analysis%20and%20Design/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [T! - Project Management](courses/T%21%20-%20Project%20Management.md) | — | 1 | B TECH | AY 2015-16 |
| [Teamcenter Customization](courses/Teamcenter%20Customization.md) | — | 1 | B TECH | AY 2025-26 |
| [Technical Communication](courses/Technical%20Communication.md) | — | 52 | B TECH, B TECH INTEGRATED, MBA Tech, MCA | 2020-2026 to AY 2026-27 |
| [Technical Communication and Leadership Skills](../subjects/Technical%20Communication%20and%20Leadership%20Skills/syllabus.md) | [yes](../subjects/Technical%20Communication%20and%20Leadership%20Skills/README.md) | 2 | B TECH | AY 2024-25 to AY 2025-26 |
| [Technical Internship Program](courses/Technical%20Internship%20Program.md) | — | 2 | B TECH WORK IN PROCESS | 2018-2022 to 2019-2023 |
| [Technical Paper Reading and Writing Skills](courses/Technical%20Paper%20Reading%20and%20Writing%20Skills.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Technical Project](courses/Technical%20Project.md) | — | 8 | B TECH INTEGRATED | 2021-2027 to 2023-2029 |
| [Technical Seminar I](courses/Technical%20Seminar%20I.md) | — | 6 | M Tech | 2024-2026 to 2026-2028 |
| [Technical Seminar II](courses/Technical%20Seminar%20II.md) | — | 3 | M Tech | 2024-2026 to 2025-2027 |
| [Technical Writing](../subjects/Technical%20Writing/syllabus.md) | [yes](../subjects/Technical%20Writing/README.md) | 5 | B TECH, B TECH INTEGRATED | 2018-2024 to AY 2024-25 |
| [Technology and Innovation for Marketing](../subjects/Technology%20and%20Innovation%20for%20Marketing/syllabus.md) | [yes](../subjects/Technology%20and%20Innovation%20for%20Marketing/README.md) | 4 | B TECH, MBA Tech | 2019-2024 to AY 2024-25 |
| [Technology Management](../subjects/Technology%20Management/syllabus.md) | [yes](../subjects/Technology%20Management/README.md) | 8 | MBA Tech | 2015-2020 to 2017-2022 |
| [Testing Commissioning and Maintenance of Electrical Equipment](../subjects/Testing%20Commissioning%20and%20Maintenance%20of%20Electrical%20Equipment/syllabus.md) | [yes](../subjects/Testing%20Commissioning%20and%20Maintenance%20of%20Electrical%20Equipment/README.md) | 3 | B TECH, MBA Tech | 2015-2020 to AY 2019-20 |
| [Testing, Commissioning and Maintenance of Electrical](courses/Testing%2C%20Commissioning%20and%20Maintenance%20of%20Electrical.md) | — | 2 | B TECH | AY 2018-19 to AY 2020-21 |
| [Theoretical Computer Science](../subjects/Theoretical%20Computer%20Science/syllabus.md) | [yes](../subjects/Theoretical%20Computer%20Science/README.md) | 21 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [Theoretical Computer Science Course](courses/Theoretical%20Computer%20Science%20Course.md) | — | 2 | B TECH WORK IN PROCESS, MBA Tech | 2020-2024 to 2020-2025 |
| [Theorv of Machines - I I](courses/Theorv%20of%20Machines%20-%20I%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Theory of Machine-IIl](courses/Theory%20of%20Machine-IIl.md) | — | 1 | B TECH INTEGRATED | 2015-2021 |
| [Theory of Machines](../subjects/Theory%20of%20Machines/syllabus.md) | [yes](../subjects/Theory%20of%20Machines/README.md) | 9 | B TECH, B TECH WORK IN PROCESS, DIPLOMA, MBA Tech | 2012-2017 to 2024-2027 |
| [Theory of Machines and Mechanisms](../subjects/Theory%20of%20Machines%20and%20Mechanisms/syllabus.md) | [yes](../subjects/Theory%20of%20Machines%20and%20Mechanisms/README.md) | 4 | B TECH INTEGRATED | 2020-2026 to 2023-2029 |
| [Theory of Machines I](../subjects/Theory%20of%20Machines%20I/syllabus.md) | [yes](../subjects/Theory%20of%20Machines%20I/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to 2019-2024 |
| [Theory of Machines II](../subjects/Theory%20of%20Machines%20II/syllabus.md) | [yes](../subjects/Theory%20of%20Machines%20II/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2019-2024 |
| [Theory of Machines III](../subjects/Theory%20of%20Machines%20III/syllabus.md) | [yes](../subjects/Theory%20of%20Machines%20III/README.md) | 3 | B TECH INTEGRATED | 2014-2020 to 2017-2023 |
| [Theory of Reinforced Concrete](courses/Theory%20of%20Reinforced%20Concrete.md) | — | 5 | B TECH WORK IN PROCESS, MBA Tech | 2014-2019 to 2017-2022 |
| [Theory of Reinforced Concrete and Prestressed Concrete](../subjects/Theory%20of%20Reinforced%20Concrete%20and%20Prestressed%20Concrete/syllabus.md) | [yes](../subjects/Theory%20of%20Reinforced%20Concrete%20and%20Prestressed%20Concrete/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2019-20 |
| [Theory of Structures](../subjects/Theory%20of%20Structures/syllabus.md) | [yes](../subjects/Theory%20of%20Structures/README.md) | 12 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2025-26 |
| [Thermal Engineering](../subjects/Thermal%20Engineering/syllabus.md) | [yes](../subjects/Thermal%20Engineering/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2012-2017 to AY 2019-20 |
| [Thermodynamics](../subjects/Thermodynamics/syllabus.md) | [yes](../subjects/Thermodynamics/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2021-2025 to AY 2025-26 |
| [Thermodynamics and Heat Transfer](../subjects/Thermodynamics%20and%20Heat%20Transfer/syllabus.md) | [yes](../subjects/Thermodynamics%20and%20Heat%20Transfer/README.md) | 7 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to 2019-2023 |
| [Threat Modelling and Intelligence](courses/Threat%20Modelling%20and%20Intelligence.md) | — | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [To View the Status](courses/To%20View%20the%20Status.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2019-2023 to 2019-2024 |
| [Total Quality Management](../subjects/Total%20Quality%20Management/syllabus.md) | [yes](../subjects/Total%20Quality%20Management/README.md) | 29 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2026-27 |
| [TQM and MIS in Construction](../subjects/TQM%20and%20MIS%20in%20Construction/syllabus.md) | [yes](../subjects/TQM%20and%20MIS%20in%20Construction/README.md) | 5 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2021-22 |
| [Traffic Analysis and Design](../subjects/Traffic%20Analysis%20and%20Design/syllabus.md) | [yes](../subjects/Traffic%20Analysis%20and%20Design/README.md) | 14 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2021-22 |
| [Transforming Ideas to Innovation](courses/Transforming%20Ideas%20to%20Innovation.md) | — | 5 | B TECH, B TECH INTEGRATED | 2023-2029 to AY 2026-27 |
| [Transportation Engineering](../subjects/Transportation%20Engineering/syllabus.md) | [yes](../subjects/Transportation%20Engineering/README.md) | 22 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2026-27 |
| [Transportation Engineering I](../subjects/Transportation%20Engineering%20I/syllabus.md) | [yes](../subjects/Transportation%20Engineering%20I/README.md) | 5 | B TECH INTEGRATED | 2014-2020 to 2018-2024 |
| [Transportation Engineering II](../subjects/Transportation%20Engineering%20II/syllabus.md) | [yes](../subjects/Transportation%20Engineering%20II/README.md) | 4 | B TECH INTEGRATED | 2014-2020 to 2018-2024 |
| [Tribology](../subjects/Tribology/syllabus.md) | [yes](../subjects/Tribology/README.md) | 15 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2020-21 |
| [TV and Video Engineering](../subjects/TV%20and%20Video%20Engineering/syllabus.md) | [yes](../subjects/TV%20and%20Video%20Engineering/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2014-15 |
| [UI and UX Design](../subjects/UI%20and%20UX%20Design/syllabus.md) | [yes](../subjects/UI%20and%20UX%20Design/README.md) | 8 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to AY 2025-26 |
| [Unit Processing in Chemical Industries](../subjects/Unit%20Processing%20in%20Chemical%20Industries/syllabus.md) | [yes](../subjects/Unit%20Processing%20in%20Chemical%20Industries/README.md) | 2 | MBA Tech | 2016-2021 to 2017-2022 |
| [Universal Human Values II](../subjects/Universal%20Human%20Values%20II/syllabus.md) | [yes](../subjects/Universal%20Human%20Values%20II/README.md) | 1 | B TECH | AY 2024-25 |
| [Unix Proarammina " I](courses/Unix%20Proarammina%20-%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Unix Programming](../subjects/Unix%20Programming/syllabus.md) | [yes](../subjects/Unix%20Programming/README.md) | 23 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | 2013-2016 to AY 2019-20 |
| [Unmanned Aerial Vehicles](../subjects/Unmanned%20Aerial%20Vehicles/syllabus.md) | [yes](../subjects/Unmanned%20Aerial%20Vehicles/README.md) | 8 | B TECH, B TECH INTEGRATED, MBA Tech | 2018-2024 to AY 2025-26 |
| [Urban and Infrastructure Development](../subjects/Urban%20and%20Infrastructure%20Development/syllabus.md) | [yes](../subjects/Urban%20and%20Infrastructure%20Development/README.md) | 1 | B TECH | AY 2013-14 |
| [Urban Development](../subjects/Urban%20Development/syllabus.md) | [yes](../subjects/Urban%20Development/README.md) | 2 | PGDM | AY 2017-18 to AY 2018-19 |
| [Urban Infrastructure Planning](../subjects/Urban%20Infrastructure%20Planning/syllabus.md) | [yes](../subjects/Urban%20Infrastructure%20Planning/README.md) | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Urban Transportation Systems](courses/Urban%20Transportation%20Systems.md) | — | 1 | B TECH WORK IN PROCESS | 2015-2019 |
| [Urban Transportation Systems Planning](../subjects/Urban%20Transportation%20Systems%20Planning/syllabus.md) | [yes](../subjects/Urban%20Transportation%20Systems%20Planning/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to 2018-2024 |
| [Usability Design of Software Applications](../subjects/Usability%20Design%20of%20Software%20Applications/syllabus.md) | [yes](../subjects/Usability%20Design%20of%20Software%20Applications/README.md) | 4 | B TECH, B TECH WORK IN PROCESS | 2019-2023 to AY 2025-26 |
| [Value Management](../subjects/Value%20Management/syllabus.md) | [yes](../subjects/Value%20Management/README.md) | 1 | PGDM | AY 2018-19 |
| [Verb Agreement](courses/Verb%20Agreement.md) | — | 1 | MBA Tech | 2021-2026 |
| [Verb Agreement E Classroom Teaching TBI](courses/Verb%20Agreement%20E%20Classroom%20Teaching%20TBI.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Vibration Engineering](../subjects/Vibration%20Engineering/syllabus.md) | [yes](../subjects/Vibration%20Engineering/README.md) | 33 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2025-26 |
| [Virtual Design and Manufacturing](../subjects/Virtual%20Design%20and%20Manufacturing/syllabus.md) | [yes](../subjects/Virtual%20Design%20and%20Manufacturing/README.md) | 3 | B TECH | AY 2023-24 to AY 2025-26 |
| [Virtual Instrumentation](../subjects/Virtual%20Instrumentation/syllabus.md) | [yes](../subjects/Virtual%20Instrumentation/README.md) | 9 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2021-22 |
| [Virtualization and Cloud Computing](../subjects/Virtualization%20and%20Cloud%20Computing/syllabus.md) | [yes](../subjects/Virtualization%20and%20Cloud%20Computing/README.md) | 6 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2020-2024 to AY 2026-27 |
| [Visual Analytics](../subjects/Visual%20Analytics/syllabus.md) | [yes](../subjects/Visual%20Analytics/README.md) | 14 | B TECH, B TECH INTEGRATED, M Tech, MBA Tech | 2015-2017 to AY 2026-27 |
| [VLSI Design and Technology](../subjects/VLSI%20Design%20and%20Technology/syllabus.md) | [yes](../subjects/VLSI%20Design%20and%20Technology/README.md) | 20 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2020-21 |
| [VLSI Design and Technology -. I Elective --I)](courses/VLSI%20Design%20and%20Technology%20-.%20I%20Elective%20--I%29.md) | — | 1 | B TECH | AY 2013-14 |
| [VLSl Design and Technology](courses/VLSl%20Design%20and%20Technology.md) | — | 1 | B TECH | AY 2013-14 |
| [Vulnerability Assessment and Penetration Testing](../subjects/Vulnerability%20Assessment%20and%20Penetration%20Testing/syllabus.md) | [yes](../subjects/Vulnerability%20Assessment%20and%20Penetration%20Testing/README.md) | 3 | B TECH, B TECH WORK IN PROCESS | 2020-2024 to AY 2025-26 |
| [Waste Management](../subjects/Waste%20Management/syllabus.md) | [yes](../subjects/Waste%20Management/README.md) | 13 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2025 to AY 2025-26 |
| [Water and Wastewater Engineering](../subjects/Water%20and%20Wastewater%20Engineering/syllabus.md) | [yes](../subjects/Water%20and%20Wastewater%20Engineering/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2014-2020 to AY 2025-26 |
| [Water Conveyance and Distribution Systems](../subjects/Water%20Conveyance%20and%20Distribution%20Systems/syllabus.md) | [yes](../subjects/Water%20Conveyance%20and%20Distribution%20Systems/README.md) | 9 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2019-2025 to AY 2026-27 |
| [Water Distribution System](../subjects/Water%20Distribution%20System/syllabus.md) | [yes](../subjects/Water%20Distribution%20System/README.md) | 11 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2014-2018 to 2019-2024 |
| [Water Quality Modelling and Management](courses/Water%20Quality%20Modelling%20and%20Management.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Web Analytics](courses/Web%20Analytics.md) | — | 4 | B TECH, B TECH WORK IN PROCESS | 2018-2022 to AY 2021-22 |
| [Web Development](courses/Web%20Development.md) | — | 1 | B TECH | AY 2025-26 |
| [Web Programming](../subjects/Web%20Programming/syllabus.md) | [yes](../subjects/Web%20Programming/README.md) | 30 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech, MCA | AY 2013-14 to AY 2025-26 |
| [Web Programming I](../subjects/Web%20Programming%20I/syllabus.md) | [yes](../subjects/Web%20Programming%20I/README.md) | 4 | MCA | 2013-2016 to 2019-2022 |
| [Web Programming II](../subjects/Web%20Programming%20II/syllabus.md) | [yes](../subjects/Web%20Programming%20II/README.md) | 5 | MCA | 2013-2016 to 2018-2021 |
| [Web Programming Z Teaching Scheme Evaluation Scheme](courses/Web%20Programming%20Z%20Teaching%20Scheme%20Evaluation%20Scheme.md) | — | 1 | B TECH WORK IN PROCESS | 2016-2020 |
| [Web Progranuning I](courses/Web%20Progranuning%20I.md) | — | 1 | MCA | 2014-2017 |
| [Web Security](courses/Web%20Security.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Web Technologies](../subjects/Web%20Technologies/syllabus.md) | [yes](../subjects/Web%20Technologies/README.md) | 8 | B TECH INTEGRATED, MCA | 2019-2025 to 2026-2028 |
| [Website Designing](courses/Website%20Designing.md) | — | 1 | DIPLOMA | 2024-2027 |
| [Website Designing and Development](courses/Website%20Designing%20and%20Development.md) | — | 1 | B TECH | AY 2026-27 |
| [Wind Turbine Technology](../subjects/Wind%20Turbine%20Technology/syllabus.md) | [yes](../subjects/Wind%20Turbine%20Technology/README.md) | 7 | B TECH, B TECH INTEGRATED, MBA Tech | 2020-2025 to AY 2026-27 |
| [Wireless Ad Hoc Networks](courses/Wireless%20Ad%20Hoc%20Networks.md) | — | 5 | B TECH, MBA Tech | 2020-2025 to AY 2024-25 |
| [Wireless Communication](../subjects/Wireless%20Communication/syllabus.md) | [yes](../subjects/Wireless%20Communication/README.md) | 6 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2025 |
| [Wireless Communication Technology](../subjects/Wireless%20Communication%20Technology/syllabus.md) | [yes](../subjects/Wireless%20Communication%20Technology/README.md) | 18 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2011-2016 to AY 2025-26 |
| [Wireless Communication Technology I](courses/Wireless%20Communication%20Technology%20I.md) | — | 1 | B TECH | AY 2013-14 |
| [Wireless Networking](../subjects/Wireless%20Networking/syllabus.md) | [yes](../subjects/Wireless%20Networking/README.md) | 5 | B TECH, B TECH WORK IN PROCESS | 2013-2017 to AY 2019-20 |
| [Wireless Security](../subjects/Wireless%20Security/syllabus.md) | [yes](../subjects/Wireless%20Security/README.md) | 2 | B TECH INTEGRATED | 2018-2024 to 2019-2025 |
| [Wireless Sensor Networks](courses/Wireless%20Sensor%20Networks.md) | — | 3 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2017-2023 to 2019-2024 |
| [Wireless Sensors for Mobile Applications](courses/Wireless%20Sensors%20for%20Mobile%20Applications.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Workshop (Electronics and](courses/Workshop%20%28Electronics%20and.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Workshop (Electronics and Computer Hardware](courses/Workshop%20%28Electronics%20and%20Computer%20Hardware.md) | — | 1 | B TECH WORK IN PROCESS | 2020-2024 |
| [Workshop / Manufacturing](courses/Workshop%20-%20Manufacturing.md) | — | 7 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2020-2025 |
| [Workshop / Manufacturing Practices](courses/Workshop%20-%20Manufacturing%20Practices.md) | — | 2 | MBA Tech | 2018-2023 |
| [Workshop I](courses/Workshop%20I.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Workshop II](courses/Workshop%20II.md) | — | 1 | B TECH INTEGRATED | 2020-2026 |
| [Workshop on Building Planning and Design](courses/Workshop%20on%20Building%20Planning%20and%20Design.md) | — | 7 | B TECH, B TECH INTEGRATED, B TECH WORK IN PROCESS | 2019-2025 to AY 2025-26 |
| [Workshop on Foundation Engineering](courses/Workshop%20on%20Foundation%20Engineering.md) | — | 5 | B TECH INTEGRATED, B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2025 |
| [Workshop on RCC and Structural Steel Detailing](courses/Workshop%20on%20RCC%20and%20Structural%20Steel%20Detailing.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2019-2024 |
| [Workshop Practice](courses/Workshop%20Practice.md) | — | 16 | B TECH, B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to AY 2021-22 |
| [Workshop Practice I](courses/Workshop%20Practice%20I.md) | — | 4 | B TECH INTEGRATED | 2015-2021 to 2019-2025 |
| [Workshop Practice II](courses/Workshop%20Practice%20II.md) | — | 5 | B TECH INTEGRATED | 2014-2020 to 2019-2025 |
| [— I (Health and Safety](courses/%E2%80%94%20I%20%28Health%20and%20Safety.md) | — | 1 | MBA Tech | 2018-2023 |
| [— I (Open Channel Flow)](courses/%E2%80%94%20I%20%28Open%20Channel%20Flow%29.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2018-2022 to 2018-2023 |
| [— II (Health and Safety](courses/%E2%80%94%20II%20%28Health%20and%20Safety.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
| [— II (Human Resources Management in Construction)](courses/%E2%80%94%20II%20%28Human%20Resources%20Management%20in%20Construction%29.md) | — | 4 | B TECH WORK IN PROCESS, MBA Tech | 2013-2017 to 2018-2023 |
| [—II (Construction](courses/%E2%80%94II%20%28Construction.md) | — | 1 | B TECH WORK IN PROCESS | 2018-2022 |
