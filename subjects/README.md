# PYQs by subject

All **25,064** question-paper files in the archive (`02_Question_Papers/`, 19,168 unique) sorted into **1,126 subjects**. Spelling variants of one subject are merged, e.g. `APPLIED MATHEMATICES II` and `Applied Mathematics II`. Each folder below has a README listing every paper for that subject by year, exam, semester and programme.

The PDFs themselves stay in the private release (18.6 GiB; too large for git). To get a subject's papers on your machine, sorted into folders:

```powershell
gh auth login                     # once, with an account that can read this private repository
gh repo clone dhruvpaleja/mpstme-library-archive-2026-10-08
cd mpstme-library-archive-2026-10-08
python organize_by_subject.py list --search "operating"
python organize_by_subject.py restore --destination D:/Study --subject "Operating Systems" --subject "Computer Networks"
```

Already restored the full library? Build the whole subject tree with hard links (no extra space on NTFS):

```powershell
python organize_by_subject.py link --library D:/MPSTME_Library_Restored
```

Either way you get `PYQs_By_Subject/<Subject>/<Academic year>/<paper>`. Newer portal papers are named `<Exam> <QP|Answers> - <Programme>.pdf`; older papers keep their original names.

| Subject | Files | Unique | Years | Programmes |
| --- | ---: | ---: | --- | ---: |
| [3D Printing](3D%20Printing/README.md) | 58 | 28 | 2022-23 to 2025-26 | 20 |
| [Accounting and Taxation](Accounting%20and%20Taxation/README.md) | 5 | 5 | 2016 to 2019-20 | 1 |
| [Actuarial Science](Actuarial%20Science/README.md) | 24 | 7 | 2022-23 to 2025-26 | 13 |
| [Additive Manufacturing](Additive%20Manufacturing/README.md) | 29 | 23 | 2016-17 to 2025-26 | 6 |
| [Advance Chemistry II](Advance%20Chemistry%20II/README.md) | 6 | 6 | 2005-06 to 2009-10 | 1 |
| [Advance Computing Application](Advance%20Computing%20Application/README.md) | 2 | 2 | 2007-08 to 2008-09 | 1 |
| [Advance Data Structure for Analytics](Advance%20Data%20Structure%20for%20Analytics/README.md) | 24 | 20 | 2022-23 to 2025-26 | 7 |
| [Advance Database Techniques](Advance%20Database%20Techniques/README.md) | 7 | 6 | 2008-09 to 2012-13 | 1 |
| [Advance DSP](Advance%20DSP/README.md) | 15 | 12 | 2010-11 to 2016-17 | 2 |
| [Advance Manufacturing Processes](Advance%20Manufacturing%20Processes/README.md) | 3 | 3 | 2022 to 2023-24 | 1 |
| [Advance Mathematics](Advance%20Mathematics/README.md) | 15 | 8 | 2010-11 to 2012-13 | 2 |
| [Advance Mathematics I](Advance%20Mathematics%20I/README.md) | 24 | 13 | 2010-11 to 2012-13 | 3 |
| [Advance Microprocessors](Advance%20Microprocessors/README.md) | 3 | 3 | 2013-14 | 1 |
| [Advance Operating Systems](Advance%20Operating%20Systems/README.md) | 5 | 5 | 2011-12 to 2012-13 | 1 |
| [Advanced Artificial Intelligence and Deep Learning](Advanced%20Artificial%20Intelligence%20and%20Deep%20Learning/README.md) | 5 | 5 | 2024-25 to 2025-26 | 2 |
| [Advanced Business Analytics in Python and R](Advanced%20Business%20Analytics%20in%20Python%20and%20R/README.md) | 1 | 1 | 2024-25 | 1 |
| [Advanced Business Communication](Advanced%20Business%20Communication/README.md) | 9 | 9 | 2013-14 to 2016-17 | 1 |
| [Advanced Chemistry](Advanced%20Chemistry/README.md) | 1 | 1 | 2019-20 | 1 |
| [Advanced Communication Networks](Advanced%20Communication%20Networks/README.md) | 6 | 6 | 2013-14 to 2016-17 | 1 |
| [Advanced Computer Networks](Advanced%20Computer%20Networks/README.md) | 26 | 25 | 2006-07 to 2018-19 | 3 |
| [Advanced Computer Vision](Advanced%20Computer%20Vision/README.md) | 5 | 5 | 2019-20 to 2024-25 | 2 |
| [Advanced Construction Techniques](Advanced%20Construction%20Techniques/README.md) | 7 | 5 | 2017-18 to 2021-22 | 3 |
| [Advanced Data Analysis and Programming](Advanced%20Data%20Analysis%20and%20Programming/README.md) | 7 | 7 | 2024-25 to 2025-26 | 2 |
| [Advanced Data Structures](Advanced%20Data%20Structures/README.md) | 20 | 10 | 2022-23 to 2025-26 | 5 |
| [Advanced Database Management Systems](Advanced%20Database%20Management%20Systems/README.md) | 85 | 70 | 2013-14 to 2025-26 | 17 |
| [Advanced Databases](Advanced%20Databases/README.md) | 1 | 1 | 2017-18 | 1 |
| [Advanced Design of Concrete Structures](Advanced%20Design%20of%20Concrete%20Structures/README.md) | 11 | 10 | 2013-14 to 2018-19 | 1 |
| [Advanced Digital Communication](Advanced%20Digital%20Communication/README.md) | 27 | 19 | 2007-08 to 2016-17 | 2 |
| [Advanced Economics](Advanced%20Economics/README.md) | 2 | 1 | 2007-08 | 2 |
| [Advanced Embedded Systems](Advanced%20Embedded%20Systems/README.md) | 3 | 3 | 2014-15 to 2016-17 | 1 |
| [Advanced Geotechnical Engineering](Advanced%20Geotechnical%20Engineering/README.md) | 6 | 4 | 2021-22 to 2023-24 | 3 |
| [Advanced Image Processing](Advanced%20Image%20Processing/README.md) | 24 | 24 | 2007-08 to 2018-19 | 3 |
| [Advanced Java](Advanced%20Java/README.md) | 36 | 35 | 2008-09 to 2025-26 | 2 |
| [Advanced Mathematics II](Advanced%20Mathematics%20II/README.md) | 24 | 6 | 2010-11 to 2012-13 | 5 |
| [Advanced Medical Electronics](Advanced%20Medical%20Electronics/README.md) | 4 | 4 | 2010-11 to 2012-13 | 1 |
| [Advanced Microcontrollers](Advanced%20Microcontrollers/README.md) | 14 | 14 | 2013-14 to 2018-19 | 4 |
| [Advanced Microwave Engineering](Advanced%20Microwave%20Engineering/README.md) | 13 | 13 | 2007-08 to 2016-17 | 1 |
| [Advanced Modeling for Business Analytics](Advanced%20Modeling%20for%20Business%20Analytics/README.md) | 6 | 6 | 2022-23 to 2025-26 | 2 |
| [Advanced Project Management](Advanced%20Project%20Management/README.md) | 18 | 10 | 2013-14 to 2025-26 | 6 |
| [Advanced Social, Text and Media Analytics](Advanced%20Social%2C%20Text%20and%20Media%20Analytics/README.md) | 15 | 15 | 2022-23 to 2025-26 | 2 |
| [Advanced Statistical Analysis](Advanced%20Statistical%20Analysis/README.md) | 25 | 9 | 2007-08 to 2012-13 | 3 |
| [Advanced Statistical Learning](Advanced%20Statistical%20Learning/README.md) | 9 | 9 | 2017-18 to 2023-24 | 2 |
| [Advanced Statistics](Advanced%20Statistics/README.md) | 3 | 3 | 2022-23 to 2023-24 | 1 |
| [Advanced Structural Analysis](Advanced%20Structural%20Analysis/README.md) | 13 | 12 | 2013-14 to 2019-20 | 2 |
| [Advanced Structural Mechanics](Advanced%20Structural%20Mechanics/README.md) | 2 | 2 | 2013-14 | 1 |
| [Advanced Supply Chain Analytics](Advanced%20Supply%20Chain%20Analytics/README.md) | 3 | 3 | 2017-18 to 2018-19 | 1 |
| [Advanced Surveying](Advanced%20Surveying/README.md) | 2 | 2 | 2013-14 | 1 |
| [Advanced System Security](Advanced%20System%20Security/README.md) | 1 | 1 | 2017-18 | 1 |
| [Advanced Topics in Machine Learning](Advanced%20Topics%20in%20Machine%20Learning/README.md) | 29 | 28 | 2023-24 to 2025-26 | 7 |
| [Advanced Turbomachinery](Advanced%20Turbomachinery/README.md) | 1 | 1 | 2019-20 | 1 |
| [Advanced VLSI System Design](Advanced%20VLSI%20System%20Design/README.md) | 3 | 3 | 2013-14 to 2015-16 | 1 |
| [Advanced Web Programming](Advanced%20Web%20Programming/README.md) | 8 | 5 | 2021-22 to 2024-25 | 3 |
| [Advanced Web Technologies](Advanced%20Web%20Technologies/README.md) | 3 | 3 | 2023-24 to 2024-25 | 1 |
| [Advances in IC Engines](Advances%20in%20IC%20Engines/README.md) | 9 | 8 | 2023-24 to 2025-26 | 5 |
| [Advertising and Public Relations](Advertising%20and%20Public%20Relations/README.md) | 106 | 47 | 2022-23 to 2025-26 | 31 |
| [Aerodynamics in Flight Design](Aerodynamics%20in%20Flight%20Design/README.md) | 14 | 10 | 2022-23 to 2025-26 | 5 |
| [Agile Product Development with DevOps](Agile%20Product%20Development%20with%20DevOps/README.md) | 17 | 16 | 2024-25 to 2025-26 | 6 |
| [AI and ML for Cybersecurity](AI%20and%20ML%20for%20Cybersecurity/README.md) | 9 | 7 | 2022-23 to 2025-26 | 2 |
| [AI and Robotics](AI%20and%20Robotics/README.md) | 13 | 7 | 2022-23 to 2025-26 | 5 |
| [Air Pollution and Controls](Air%20Pollution%20and%20Controls/README.md) | 1 | 1 | year not stated | 1 |
| [Air Quality Management](Air%20Quality%20Management/README.md) | 2 | 2 | 2019-20 | 2 |
| [Algorithm Trading](Algorithm%20Trading/README.md) | 20 | 11 | 2022-23 to 2024-25 | 4 |
| [Alternative Fuels](Alternative%20Fuels/README.md) | 15 | 10 | 2024-25 to 2025-26 | 4 |
| [An Introduction to Artificial Intelligence and AI](An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI/README.md) | 1 | 1 | year not stated | 1 |
| [An Introduction to Artificial Intelligence and AI Framework](An%20Introduction%20to%20Artificial%20Intelligence%20and%20AI%20Framework/README.md) | 4 | 3 | 2018-19 to 2023-24 | 1 |
| [Analog and Digital Communication](Analog%20and%20Digital%20Communication/README.md) | 32 | 27 | 2013-14 to 2021-22 | 3 |
| [Analog and Integrated Circuits](Analog%20and%20Integrated%20Circuits/README.md) | 6 | 6 | 2005-06 to 2009-10 | 1 |
| [Analog Circuits Analysis and Design](Analog%20Circuits%20Analysis%20and%20Design/README.md) | 21 | 16 | 2021-22 to 2025-26 | 3 |
| [Analog Devices and Circuits](Analog%20Devices%20and%20Circuits/README.md) | 1 | 1 | 2019-20 | 1 |
| [Analog Integrated Circuits and Applications](Analog%20Integrated%20Circuits%20and%20Applications/README.md) | 52 | 48 | 2010-11 to 2018-19 | 5 |
| [Analysing Unstructured Data](Analysing%20Unstructured%20Data/README.md) | 16 | 16 | 2024-25 to 2025-26 | 6 |
| [Analysis of Structures](Analysis%20of%20Structures/README.md) | 19 | 17 | 2012-13 to 2022-23 | 2 |
| [Analysis of Transportation System](Analysis%20of%20Transportation%20System/README.md) | 6 | 6 | 2015-16 to 2022 | 2 |
| [Analytics for Strategic Marketing Decisions](Analytics%20for%20Strategic%20Marketing%20Decisions/README.md) | 21 | 21 | 2019-20 to 2025-26 | 6 |
| [Analytics in Operations and Supply Chain Management](Analytics%20in%20Operations%20and%20Supply%20Chain%20Management/README.md) | 28 | 27 | 2017-18 to 2025-26 | 8 |
| [Android Application Development](Android%20Application%20Development/README.md) | 1 | 1 | 2021-22 | 1 |
| [Android Operating System](Android%20Operating%20System/README.md) | 2 | 1 | 2018-19 | 1 |
| [Antenna and Wave Propagation](Antenna%20and%20Wave%20Propagation/README.md) | 18 | 17 | 2013-14 to 2016-17 | 2 |
| [Antenna System Design](Antenna%20System%20Design/README.md) | 4 | 4 | 2013-14 to 2015-16 | 1 |
| [Antenna Theory and Design](Antenna%20Theory%20and%20Design/README.md) | 1 | 1 | 2007-08 | 1 |
| [Application Architecture and Deployment](Application%20Architecture%20and%20Deployment/README.md) | 9 | 9 | 2024-25 to 2025-26 | 4 |
| [Application of Power Electronics in Power Systems](Application%20of%20Power%20Electronics%20in%20Power%20Systems/README.md) | 3 | 3 | 2018-19 to 2019-20 | 1 |
| [Application Security Testing](Application%20Security%20Testing/README.md) | 9 | 9 | 2022-23 to 2025-26 | 3 |
| [Applications of Machine Learning](Applications%20of%20Machine%20Learning/README.md) | 21 | 17 | 2022-23 to 2025-26 | 6 |
| [Applied Artificial Intelligence](Applied%20Artificial%20Intelligence/README.md) | 27 | 17 | 2022-23 to 2025-26 | 7 |
| [Applied Chemistry](Applied%20Chemistry/README.md) | 54 | 46 | 2006-07 to 2025-26 | 6 |
| [Applied Chemistry I](Applied%20Chemistry%20I/README.md) | 16 | 16 | 2004-05 to 2012-13 | 1 |
| [Applied Chemistry II](Applied%20Chemistry%20II/README.md) | 21 | 21 | 2004-05 to 2012-13 | 1 |
| [Applied Machine Learning](Applied%20Machine%20Learning/README.md) | 6 | 6 | 2024-25 to 2025-26 | 2 |
| [Applied Mathematics for Data Science](Applied%20Mathematics%20for%20Data%20Science/README.md) | 2 | 2 | 2024-25 to 2025-26 | 1 |
| [Applied Mathematics I](Applied%20Mathematics%20I/README.md) | 51 | 47 | 2004-05 to 2013-14 | 3 |
| [Applied Mathematics II](Applied%20Mathematics%20II/README.md) | 58 | 47 | 2004-05 to 2017-18 | 3 |
| [Applied Mathematics III](Applied%20Mathematics%20III/README.md) | 31 | 27 | 2004-05 to 2019-20 | 2 |
| [Applied Mathematics IV](Applied%20Mathematics%20IV/README.md) | 1 | 1 | 2019-20 | 1 |
| [Applied Physics I](Applied%20Physics%20I/README.md) | 71 | 57 | 2004-05 to 2025-26 | 7 |
| [Applied Physics II](Applied%20Physics%20II/README.md) | 47 | 41 | 2004-05 to 2025-26 | 5 |
| [Applied Satellite Communication](Applied%20Satellite%20Communication/README.md) | 13 | 12 | 2006-07 to 2016-17 | 1 |
| [Applied Statistics](Applied%20Statistics/README.md) | 1 | 1 | 2024-25 | 1 |
| [Applied Statistics and Time Series Forecasting](Applied%20Statistics%20and%20Time%20Series%20Forecasting/README.md) | 2 | 2 | 2024 to 2025-26 | 1 |
| [Applied Thermodynamics](Applied%20Thermodynamics/README.md) | 38 | 33 | 2011-12 to 2025-26 | 5 |
| [Applied Time Series Analysis](Applied%20Time%20Series%20Analysis/README.md) | 29 | 19 | 2022 to 2025-26 | 9 |
| [Artificial Intelligence](Artificial%20Intelligence/README.md) | 138 | 114 | 2006-07 to 2025-26 | 28 |
| [Artificial Intelligence - Deep Learning and Generative AI](Artificial%20Intelligence%20-%20Deep%20Learning%20and%20Generative%20AI/README.md) | 5 | 5 | 2024-25 to 2025-26 | 2 |
| [Artificial Intelligence and Machine Learning](Artificial%20Intelligence%20and%20Machine%20Learning/README.md) | 19 | 19 | 2022-23 to 2025-26 | 4 |
| [Artificial Intelligence and Robotics](Artificial%20Intelligence%20and%20Robotics/README.md) | 3 | 2 | 2021-22 | 2 |
| [Artificial Intelligence for Mechanical Engineers](Artificial%20Intelligence%20for%20Mechanical%20Engineers/README.md) | 1 | 1 | 2022-23 | 1 |
| [Artificial Intelligence in Automation](Artificial%20Intelligence%20in%20Automation/README.md) | 3 | 3 | 2014-15 to 2016-17 | 1 |
| [Automatic Control Systems](Automatic%20Control%20Systems/README.md) | 4 | 4 | 2022-23 to 2025-26 | 1 |
| [Automation and Control Engineering](Automation%20and%20Control%20Engineering/README.md) | 4 | 4 | 2011-12 to 2012-13 | 1 |
| [Automation in Manufacturing](Automation%20in%20Manufacturing/README.md) | 2 | 2 | 2025-26 | 1 |
| [Automation in Manufacturing Systems](Automation%20in%20Manufacturing%20Systems/README.md) | 2 | 2 | 2014-15 to 2016-17 | 1 |
| [Automotive Electronics](Automotive%20Electronics/README.md) | 1 | 1 | 2022-23 | 1 |
| [Automotive Engineering](Automotive%20Engineering/README.md) | 21 | 21 | 2013-14 to 2025-26 | 5 |
| [Autonomous Navigation of Electric Vehicles](Autonomous%20Navigation%20of%20Electric%20Vehicles/README.md) | 8 | 4 | 2022-23 to 2024-25 | 3 |
| [B2B Marketing](B2B%20Marketing/README.md) | 56 | 56 | 2013-14 to 2025-26 | 8 |
| [Basic Control Systems](Basic%20Control%20Systems/README.md) | 34 | 31 | 2013-14 to 2019-20 | 4 |
| [Basic Data Structures](Basic%20Data%20Structures/README.md) | 31 | 25 | 2022 to 2025-26 | 6 |
| [Basic Decision Making with Spreadsheet](Basic%20Decision%20Making%20with%20Spreadsheet/README.md) | 51 | 33 | 2022-23 to 2025-26 | 9 |
| [Basic Electrical and Electronics Engineering](Basic%20Electrical%20and%20Electronics%20Engineering/README.md) | 158 | 134 | 2021-22 to 2025-26 | 20 |
| [Basic Electrical Engineering](Basic%20Electrical%20Engineering/README.md) | 103 | 90 | 2004-05 to 2025-26 | 2 |
| [Basic Electronics](Basic%20Electronics/README.md) | 137 | 109 | 2004-05 to 2024-25 | 4 |
| [Basic Engineering Drawing I](Basic%20Engineering%20Drawing%20I/README.md) | 1 | 1 | 2014-15 | 1 |
| [Basic Manufacturing Processes](Basic%20Manufacturing%20Processes/README.md) | 2 | 2 | 2025-26 | 1 |
| [Basic Marketing](Basic%20Marketing/README.md) | 1 | 1 | 2019-20 | 1 |
| [Basic of Engineering Chemistry](Basic%20of%20Engineering%20Chemistry/README.md) | 5 | 4 | 2021-22 to 2023-24 | 2 |
| [Basic Thermodynamics](Basic%20Thermodynamics/README.md) | 12 | 12 | 2021-22 to 2025-26 | 3 |
| [Basic Web Programming](Basic%20Web%20Programming/README.md) | 3 | 3 | 2010-11 to 2011-12 | 1 |
| [Basics of Machine Drawing](Basics%20of%20Machine%20Drawing/README.md) | 4 | 4 | 2021-22 to 2024-25 | 1 |
| [Basics of Manufacturing Engineering](Basics%20of%20Manufacturing%20Engineering/README.md) | 4 | 4 | 2024-25 | 1 |
| [Basics of Operations and Supply Chain Management](Basics%20of%20Operations%20and%20Supply%20Chain%20Management/README.md) | 2 | 2 | 2018-19 to 2019-20 | 1 |
| [Basics of Python](Basics%20of%20Python/README.md) | 6 | 3 | 2022-23 to 2024-25 | 2 |
| [Basics of Web Development](Basics%20of%20Web%20Development/README.md) | 3 | 3 | 2023-24 to 2024-25 | 1 |
| [Behavioral Economics](Behavioral%20Economics/README.md) | 1 | 1 | 2024-25 | 1 |
| [Best Practices in Operations](Best%20Practices%20in%20Operations/README.md) | 6 | 6 | 2017-18 to 2024-25 | 1 |
| [Big Data](Big%20Data/README.md) | 2 | 2 | 2021-22 | 1 |
| [Big Data Analytics](Big%20Data%20Analytics/README.md) | 51 | 26 | 2023-24 to 2025-26 | 18 |
| [Big Data Technology](Big%20Data%20Technology/README.md) | 14 | 14 | 2015-16 to 2024-25 | 3 |
| [Bio Chemical Engineering](Bio%20Chemical%20Engineering/README.md) | 1 | 1 | 2012-13 | 1 |
| [Biology for Engineers](Biology%20for%20Engineers/README.md) | 2 | 2 | 2021-22 | 1 |
| [Biomechanics](Biomechanics/README.md) | 10 | 5 | 2023-24 to 2025-26 | 4 |
| [Biomedical Instrumentation](Biomedical%20Instrumentation/README.md) | 7 | 7 | 2024-25 to 2025-26 | 2 |
| [Biometrics](Biometrics/README.md) | 39 | 28 | 2010-11 to 2025-26 | 12 |
| [Biometrics Applications](Biometrics%20Applications/README.md) | 1 | 1 | 2012-13 | 1 |
| [Block Chain](Block%20Chain/README.md) | 1 | 1 | 2022-23 | 1 |
| [Blockchain Security and Forensics](Blockchain%20Security%20and%20Forensics/README.md) | 5 | 5 | 2022-23 to 2025-26 | 2 |
| [Blockchain Technology](Blockchain%20Technology/README.md) | 56 | 37 | 2022-23 to 2025-26 | 24 |
| [Brand Management](Brand%20Management/README.md) | 47 | 45 | 2008-09 to 2025-26 | 10 |
| [Bridge Engineering](Bridge%20Engineering/README.md) | 7 | 5 | 2022-23 to 2025-26 | 4 |
| [Broadband Technology](Broadband%20Technology/README.md) | 4 | 4 | 2014-15 to 2016-17 | 1 |
| [Building Byelaws and Statutory Approvals](Building%20Byelaws%20and%20Statutory%20Approvals/README.md) | 7 | 7 | 2015-16 to 2018-19 | 1 |
| [Building Construction](Building%20Construction/README.md) | 6 | 6 | 2015 to 2018-19 | 1 |
| [Building Design and Drawing](Building%20Design%20and%20Drawing/README.md) | 9 | 9 | 2023-24 to 2025-26 | 2 |
| [Building Design and Drawing I](Building%20Design%20and%20Drawing%20I/README.md) | 37 | 33 | 2013-14 to 2019-20 | 3 |
| [Building Design and Drawing II](Building%20Design%20and%20Drawing%20II/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Building Materials and Construction](Building%20Materials%20and%20Construction/README.md) | 31 | 29 | 2013-14 to 2018-19 | 2 |
| [Building Planning and Design](Building%20Planning%20and%20Design/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Building Services](Building%20Services/README.md) | 6 | 6 | 2016-17 to 2019-20 | 1 |
| [Building Utilities and Services](Building%20Utilities%20and%20Services/README.md) | 40 | 35 | 2013-14 to 2025-26 | 4 |
| [Business Analytics](Business%20Analytics/README.md) | 68 | 68 | 2010-11 to 2025-26 | 8 |
| [Business Analytics for Decision Making](Business%20Analytics%20for%20Decision%20Making/README.md) | 2 | 2 | 2018-19 | 1 |
| [Business Calculus](Business%20Calculus/README.md) | 11 | 11 | 2022-23 to 2024-25 | 2 |
| [Business Communication](Business%20Communication/README.md) | 78 | 34 | 2007-08 to 2018-19 | 8 |
| [Business Communication and Value Science I](Business%20Communication%20and%20Value%20Science%20I/README.md) | 9 | 9 | 2019-20 to 2024-25 | 2 |
| [Business Communication and Value Science II](Business%20Communication%20and%20Value%20Science%20II/README.md) | 7 | 7 | 2022-23 to 2024-25 | 2 |
| [Business Communication and Value Science III](Business%20Communication%20and%20Value%20Science%20III/README.md) | 4 | 4 | 2021-22 to 2023-24 | 1 |
| [Business Communications I](Business%20Communications%20I/README.md) | 6 | 4 | 2011-12 to 2012-13 | 2 |
| [Business Communications III](Business%20Communications%20III/README.md) | 9 | 5 | 2009-10 to 2011-12 | 4 |
| [Business Economics](Business%20Economics/README.md) | 54 | 29 | 2006-07 to 2019-20 | 7 |
| [Business Information Visualization and Analysis](Business%20Information%20Visualization%20and%20Analysis/README.md) | 14 | 9 | 2022-23 to 2024-25 | 4 |
| [Business Intelligence and Analytics](Business%20Intelligence%20and%20Analytics/README.md) | 6 | 5 | 2025-26 | 2 |
| [Business Model in Infrastructure Management](Business%20Model%20in%20Infrastructure%20Management/README.md) | 2 | 2 | 2016-17 to 2017-18 | 1 |
| [Business Models in Digital Economy](Business%20Models%20in%20Digital%20Economy/README.md) | 9 | 9 | 2008-09 to 2015-16 | 1 |
| [Business Process Management](Business%20Process%20Management/README.md) | 8 | 8 | 2011-12 to 2016-17 | 1 |
| [Business Process Re Engineering](Business%20Process%20Re%20Engineering/README.md) | 4 | 4 | 2008-09 to 2010-11 | 1 |
| [Business Research Methods](Business%20Research%20Methods/README.md) | 47 | 47 | 2021-22 to 2025-26 | 8 |
| [Business Statistics](Business%20Statistics/README.md) | 25 | 19 | 2018-19 to 2025-26 | 6 |
| [Business Strategy](Business%20Strategy/README.md) | 10 | 10 | 2022-23 to 2025-26 | 2 |
| [Buyer Behaviour](Buyer%20Behaviour/README.md) | 25 | 19 | 2015-16 to 2025-26 | 7 |
| [C Programming](C%20Programming/README.md) | 21 | 16 | 2007-08 to 2024-25 | 3 |
| [CAD](CAD/README.md) | 5 | 5 | 2007-08 to 2016-17 | 2 |
| [CAD CAM](CAD%20CAM/README.md) | 9 | 9 | 2006-07 to 2024-25 | 2 |
| [CAD CAM CAE](CAD%20CAM%20CAE/README.md) | 25 | 23 | 2013-14 to 2025-26 | 3 |
| [CAD CAM CIM](CAD%20CAM%20CIM/README.md) | 29 | 26 | 2017-18 to 2025-26 | 6 |
| [Calculus](Calculus/README.md) | 193 | 143 | 2022 to 2025-26 | 26 |
| [Capital Market and Real Estate](Capital%20Market%20and%20Real%20Estate/README.md) | 2 | 2 | 2017-18 to 2018-19 | 1 |
| [Cases in Internet of Things Management](Cases%20in%20Internet%20of%20Things%20Management/README.md) | 3 | 3 | 2015-16 to 2016-17 | 1 |
| [Catalytic Science and Engineering](Catalytic%20Science%20and%20Engineering/README.md) | 1 | 1 | 2022-23 | 1 |
| [Chemical Engineering Thermodynamics](Chemical%20Engineering%20Thermodynamics/README.md) | 24 | 23 | 2005-06 to 2019-20 | 1 |
| [Chemical Process](Chemical%20Process/README.md) | 12 | 12 | 2006-07 to 2012-13 | 1 |
| [Chemical Process II](Chemical%20Process%20II/README.md) | 19 | 19 | 2007-08 to 2018-19 | 1 |
| [Chemical Processes I](Chemical%20Processes%20I/README.md) | 11 | 11 | 2014-15 to 2019-20 | 1 |
| [Chemical Project Engineering and Economics](Chemical%20Project%20Engineering%20and%20Economics/README.md) | 3 | 3 | 2021-22 to 2023-24 | 1 |
| [Chemical Reaction Engineering](Chemical%20Reaction%20Engineering/README.md) | 19 | 19 | 2006-07 to 2022-23 | 1 |
| [Chemical Reaction Engineering II](Chemical%20Reaction%20Engineering%20II/README.md) | 2 | 2 | 2021-22 | 1 |
| [Chemistry](Chemistry/README.md) | 40 | 26 | 2021-22 to 2025-26 | 11 |
| [Chemistry I](Chemistry%20I/README.md) | 21 | 20 | 2014-15 to 2023-24 | 1 |
| [Chemistry II](Chemistry%20II/README.md) | 47 | 38 | 2014-15 to 2024-25 | 9 |
| [Circuit and Network Theory](Circuit%20and%20Network%20Theory/README.md) | 16 | 15 | 2019-20 to 2025-26 | 4 |
| [Classical Control Systems](Classical%20Control%20Systems/README.md) | 6 | 6 | 2023-24 to 2025-26 | 2 |
| [Classical Physics](Classical%20Physics/README.md) | 21 | 15 | 2021-22 to 2025-26 | 4 |
| [Cloud Computing](Cloud%20Computing/README.md) | 105 | 74 | 2013-14 to 2025-26 | 29 |
| [Cloud Computing and IoT](Cloud%20Computing%20and%20IoT/README.md) | 2 | 2 | 2021-22 | 1 |
| [Cloud Microservices and Application](Cloud%20Microservices%20and%20Application/README.md) | 2 | 2 | 2022-23 | 1 |
| [Cloud Security](Cloud%20Security/README.md) | 8 | 8 | 2022-23 to 2025-26 | 2 |
| [Cloud Technology](Cloud%20Technology/README.md) | 4 | 4 | 2022-23 to 2023-24 | 1 |
| [Cognitive Science and Analytics](Cognitive%20Science%20and%20Analytics/README.md) | 14 | 14 | 2022-23 to 2025-26 | 2 |
| [Communication Skills](Communication%20Skills/README.md) | 80 | 72 | 2007-08 to 2024-25 | 4 |
| [Communication Skills I](Communication%20Skills%20I/README.md) | 4 | 4 | 2024-25 | 1 |
| [Communication Skills II](Communication%20Skills%20II/README.md) | 11 | 10 | 2021-22 to 2024-25 | 2 |
| [Communication Systems](Communication%20Systems/README.md) | 22 | 15 | 2005-06 to 2018-19 | 4 |
| [Communication Techniques](Communication%20Techniques/README.md) | 12 | 12 | 2005-06 to 2012-13 | 1 |
| [Communication Technology for IoT](Communication%20Technology%20for%20IoT/README.md) | 2 | 2 | 2022-23 to 2023-24 | 1 |
| [Communication Theory and Systems](Communication%20Theory%20and%20Systems/README.md) | 17 | 12 | 2021-22 to 2025-26 | 3 |
| [Compiler Construction](Compiler%20Construction/README.md) | 2 | 1 | 2018-19 | 1 |
| [Compiler Design](Compiler%20Design/README.md) | 17 | 16 | 2022-23 to 2025-26 | 4 |
| [Complex Variables and Transforms](Complex%20Variables%20and%20Transforms/README.md) | 89 | 46 | 2022-23 to 2025-26 | 19 |
| [Composite Materials](Composite%20Materials/README.md) | 11 | 9 | 2022 to 2025-26 | 4 |
| [Computational Analytics for Marketing](Computational%20Analytics%20for%20Marketing/README.md) | 5 | 5 | 2021-22 to 2023-24 | 2 |
| [Computational Finance and Modeling](Computational%20Finance%20and%20Modeling/README.md) | 3 | 3 | 2022-23 to 2024-25 | 1 |
| [Computational Fluid Dynamics](Computational%20Fluid%20Dynamics/README.md) | 8 | 7 | 2013-14 to 2025-26 | 4 |
| [Computational Methods](Computational%20Methods/README.md) | 2 | 2 | 2021-22 | 1 |
| [Computational Neuroscience](Computational%20Neuroscience/README.md) | 7 | 5 | 2021-22 to 2024-25 | 3 |
| [Computational Statistics](Computational%20Statistics/README.md) | 12 | 12 | 2022-23 to 2025-26 | 2 |
| [Computational Thinking for Problem Solving](Computational%20Thinking%20for%20Problem%20Solving/README.md) | 76 | 54 | 2025-26 | 20 |
| [Computer Applications and Numerical Techniques](Computer%20Applications%20and%20Numerical%20Techniques/README.md) | 12 | 11 | 2004-05 to 2009-10 | 1 |
| [Computer Architecture](Computer%20Architecture/README.md) | 26 | 16 | 2022-23 to 2025-26 | 6 |
| [Computer Communication Networks](Computer%20Communication%20Networks/README.md) | 30 | 26 | 2013-14 to 2018-19 | 5 |
| [Computer Fundamental](Computer%20Fundamental/README.md) | 12 | 10 | 2004-05 to 2009-10 | 1 |
| [Computer Graphics](Computer%20Graphics/README.md) | 43 | 38 | 2013-14 to 2025-26 | 7 |
| [Computer Networking](Computer%20Networking/README.md) | 7 | 7 | 2008-09 to 2012-13 | 2 |
| [Computer Networking and Design Principles](Computer%20Networking%20and%20Design%20Principles/README.md) | 7 | 7 | 2013-14 to 2015-16 | 2 |
| [Computer Networks](Computer%20Networks/README.md) | 279 | 162 | 2011-12 to 2025-26 | 39 |
| [Computer Organization and Architecture](Computer%20Organization%20and%20Architecture/README.md) | 166 | 127 | 2007-08 to 2025-26 | 25 |
| [Computer Organization and Machine Learning](Computer%20Organization%20and%20Machine%20Learning/README.md) | 2 | 1 | 2022-23 | 2 |
| [Computer Programming](Computer%20Programming/README.md) | 72 | 62 | 2004-05 to 2024-25 | 5 |
| [Computer Programming I](Computer%20Programming%20I/README.md) | 9 | 9 | 2012-13 to 2017-18 | 2 |
| [Computer Programming II](Computer%20Programming%20II/README.md) | 53 | 46 | 2006-07 to 2019-20 | 3 |
| [Computer Programming III](Computer%20Programming%20III/README.md) | 13 | 13 | 2015-16 to 2018-19 | 1 |
| [Computer Simulation and Modeling](Computer%20Simulation%20and%20Modeling/README.md) | 42 | 33 | 2006-07 to 2019-20 | 3 |
| [Computer System Architecture](Computer%20System%20Architecture/README.md) | 10 | 10 | 2025-26 | 3 |
| [Computer Vision](Computer%20Vision/README.md) | 85 | 55 | 2018-19 to 2025-26 | 27 |
| [Computer Vision and Applications](Computer%20Vision%20and%20Applications/README.md) | 11 | 10 | 2022-23 to 2025-26 | 6 |
| [Concrete Technology](Concrete%20Technology/README.md) | 57 | 54 | 2012-13 to 2025-26 | 4 |
| [Constitution of India](Constitution%20of%20India/README.md) | 10 | 4 | 2008-09 to 2009-10 | 4 |
| [Construction Contracts and Administration](Construction%20Contracts%20and%20Administration/README.md) | 21 | 15 | 2015-16 to 2025-26 | 4 |
| [Construction Economics and Finance Management](Construction%20Economics%20and%20Finance%20Management/README.md) | 13 | 12 | 2015-16 to 2024-25 | 3 |
| [Construction Engineering](Construction%20Engineering/README.md) | 7 | 7 | 2015-16 to 2018-19 | 1 |
| [Construction Equipment and Techniques](Construction%20Equipment%20and%20Techniques/README.md) | 13 | 9 | 2015-16 to 2021-22 | 2 |
| [Construction Law](Construction%20Law/README.md) | 5 | 5 | 2015-16 to 2018-19 | 1 |
| [Construction Logistics](Construction%20Logistics/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Construction Material Management](Construction%20Material%20Management/README.md) | 7 | 4 | 2022-23 to 2023-24 | 2 |
| [Construction Materials](Construction%20Materials/README.md) | 6 | 6 | 2015-16 to 2018-19 | 1 |
| [Construction Project Management](Construction%20Project%20Management/README.md) | 13 | 12 | 2013-14 to 2022-23 | 1 |
| [Construction Project Management and Finance](Construction%20Project%20Management%20and%20Finance/README.md) | 22 | 17 | 2018-19 to 2025-26 | 4 |
| [Construction Quality Control and Assurance](Construction%20Quality%20Control%20and%20Assurance/README.md) | 8 | 8 | 2017-18 to 2025-26 | 2 |
| [Construction Safety](Construction%20Safety/README.md) | 5 | 5 | 2016-17 to 2018-19 | 2 |
| [Construction Techniques](Construction%20Techniques/README.md) | 1 | 1 | 2012-13 | 1 |
| [Construction Techniques and Safety](Construction%20Techniques%20and%20Safety/README.md) | 3 | 3 | 2013-14 | 2 |
| [Construction Technology](Construction%20Technology/README.md) | 21 | 18 | 2021-22 to 2025-26 | 4 |
| [Consumer Behaviour](Consumer%20Behaviour/README.md) | 8 | 8 | 2008-09 to 2014-15 | 1 |
| [Contemporary Practices in Management](Contemporary%20Practices%20in%20Management/README.md) | 7 | 7 | 2015-16 to 2016-17 | 1 |
| [Contemporary Short Fiction](Contemporary%20Short%20Fiction/README.md) | 50 | 31 | 2023-24 to 2025-26 | 26 |
| [Contract, Competition and Consumer Laws](Contract%2C%20Competition%20and%20Consumer%20Laws/README.md) | 39 | 39 | 2024-25 to 2025-26 | 8 |
| [Contracts and Claims Management](Contracts%20and%20Claims%20Management/README.md) | 4 | 4 | 2010-11 to 2013-14 | 1 |
| [Control System](Control%20System/README.md) | 2 | 2 | 2018-19 | 1 |
| [Control System Engineering](Control%20System%20Engineering/README.md) | 22 | 20 | 2017-18 to 2025-26 | 4 |
| [Control System I](Control%20System%20I/README.md) | 5 | 5 | 2017-18 to 2019-20 | 1 |
| [Control Systems II](Control%20Systems%20II/README.md) | 2 | 2 | 2018-19 | 1 |
| [Convex Optimization](Convex%20Optimization/README.md) | 3 | 3 | 2021-22 to 2023-24 | 1 |
| [Core Java](Core%20Java/README.md) | 27 | 27 | 2010-11 to 2018-19 | 2 |
| [Corporate and Personal Tax Planning](Corporate%20and%20Personal%20Tax%20Planning/README.md) | 1 | 1 | year not stated | 1 |
| [Corporate Finance](Corporate%20Finance/README.md) | 6 | 4 | 2007-08 to 2023-24 | 4 |
| [Corporate Social Responsibility](Corporate%20Social%20Responsibility/README.md) | 30 | 14 | 2008-09 to 2014-15 | 4 |
| [Corporate Tax Planning](Corporate%20Tax%20Planning/README.md) | 2 | 2 | 2008-09 to 2009-10 | 1 |
| [Cost Accounting](Cost%20Accounting/README.md) | 45 | 27 | 2007-08 to 2015-16 | 5 |
| [Cost and Management Accounting](Cost%20and%20Management%20Accounting/README.md) | 10 | 9 | 2015-16 to 2018-19 | 2 |
| [Cost Estimation](Cost%20Estimation/README.md) | 7 | 7 | 2012-13 to 2013-14 | 2 |
| [Creativity and Ethics in Marketing](Creativity%20and%20Ethics%20in%20Marketing/README.md) | 91 | 58 | 2021-22 to 2025-26 | 30 |
| [Critical Thinking in Humanities](Critical%20Thinking%20in%20Humanities/README.md) | 10 | 10 | 2021-22 to 2024-25 | 2 |
| [Cryptography](Cryptography/README.md) | 1 | 1 | 2022-23 | 1 |
| [Cryptography and Network Security](Cryptography%20and%20Network%20Security/README.md) | 49 | 15 | 2023-24 to 2025-26 | 18 |
| [CSEH](CSEH/README.md) | 2 | 1 | 2022-23 | 2 |
| [Customer Relationship Management](Customer%20Relationship%20Management/README.md) | 3 | 3 | 2008-09 to 2017-18 | 1 |
| [Cyber Forensics](Cyber%20Forensics/README.md) | 35 | 23 | 2021-22 to 2025-26 | 17 |
| [Cyber Physical Systems Security](Cyber%20Physical%20Systems%20Security/README.md) | 3 | 3 | 2024-25 | 2 |
| [Cyber Security](Cyber%20Security/README.md) | 40 | 28 | 2017-18 to 2025-26 | 10 |
| [Cyber Security and Ethical Hacking](Cyber%20Security%20and%20Ethical%20Hacking/README.md) | 9 | 6 | 2021-22 to 2022-23 | 2 |
| [Cyber Security for Non-IT](Cyber%20Security%20for%20Non-IT/README.md) | 1 | 1 | 2021-22 | 1 |
| [Cyber Security Management](Cyber%20Security%20Management/README.md) | 2 | 2 | 2016-17 to 2017-18 | 1 |
| [Cybersecurity Fundamentals](Cybersecurity%20Fundamentals/README.md) | 12 | 12 | 2022-23 to 2025-26 | 2 |
| [Cybersecurity Risk Management](Cybersecurity%20Risk%20Management/README.md) | 7 | 7 | 2023-24 to 2025-26 | 2 |
| [Data Analysis with Python](Data%20Analysis%20with%20Python/README.md) | 3 | 3 | 2023-24 to 2024-25 | 1 |
| [Data Analytics](Data%20Analytics/README.md) | 21 | 11 | 2022-23 to 2025-26 | 6 |
| [Data Communication and Computer Networks](Data%20Communication%20and%20Computer%20Networks/README.md) | 7 | 7 | 2025-26 | 4 |
| [Data Driven Program Analysis](Data%20Driven%20Program%20Analysis/README.md) | 17 | 11 | 2022-23 to 2025-26 | 6 |
| [Data Encryption and Network Security](Data%20Encryption%20and%20Network%20Security/README.md) | 16 | 13 | 2013-14 to 2021-22 | 2 |
| [Data Engineering](Data%20Engineering/README.md) | 10 | 8 | 2024-25 to 2025-26 | 4 |
| [Data Gathering and Cleaning - ETL Process](Data%20Gathering%20and%20Cleaning%20-%20ETL%20Process/README.md) | 2 | 1 | year not stated | 1 |
| [Data Gathering Cleaning](Data%20Gathering%20Cleaning/README.md) | 7 | 7 | 2015-16 to 2022-23 | 1 |
| [Data Handling and Visualization](Data%20Handling%20and%20Visualization/README.md) | 11 | 8 | 2022-23 to 2024-25 | 5 |
| [Data Mining](Data%20Mining/README.md) | 10 | 10 | 2010-11 to 2023-24 | 3 |
| [Data Mining and Analytics](Data%20Mining%20and%20Analytics/README.md) | 20 | 14 | 2016-17 to 2025-26 | 6 |
| [Data Privacy](Data%20Privacy/README.md) | 5 | 5 | 2022-23 to 2024-25 | 1 |
| [Data Science](Data%20Science/README.md) | 1 | 1 | 2017-18 | 1 |
| [Data Science and Big Data Analytics](Data%20Science%20and%20Big%20Data%20Analytics/README.md) | 7 | 7 | 2015-16 to 2022-23 | 3 |
| [Data Science I](Data%20Science%20I/README.md) | 4 | 4 | 2015-16 to 2017-18 | 1 |
| [Data Science II](Data%20Science%20II/README.md) | 2 | 2 | 2015-16 | 1 |
| [Data Science III](Data%20Science%20III/README.md) | 2 | 2 | 2018-19 to 2019-20 | 1 |
| [Data Structures](Data%20Structures/README.md) | 37 | 34 | 2013-14 to 2025-26 | 7 |
| [Data Structures and Algorithms](Data%20Structures%20and%20Algorithms/README.md) | 287 | 200 | 2005-06 to 2025-26 | 45 |
| [Data Warehouse Design](Data%20Warehouse%20Design/README.md) | 1 | 1 | 2013-14 | 1 |
| [Data Warehousing and Mining](Data%20Warehousing%20and%20Mining/README.md) | 111 | 93 | 2006-07 to 2025-26 | 14 |
| [Data Warehousing Mining and Business Intelligence](Data%20Warehousing%20Mining%20and%20Business%20Intelligence/README.md) | 7 | 7 | 2007-08 to 2011-12 | 1 |
| [Data Wrangling](Data%20Wrangling/README.md) | 46 | 31 | 2022-23 to 2025-26 | 13 |
| [Data Wrangling Data Gathering and Cleaning ETL Process](Data%20Wrangling%20Data%20Gathering%20and%20Cleaning%20ETL%20Process/README.md) | 1 | 1 | 2022-23 | 1 |
| [Database Administration](Database%20Administration/README.md) | 18 | 14 | 2023-24 to 2025-26 | 6 |
| [Database Management Systems](Database%20Management%20Systems/README.md) | 268 | 197 | 2005-06 to 2025-26 | 41 |
| [Database System Essentials](Database%20System%20Essentials/README.md) | 10 | 10 | 2023-24 to 2025-26 | 2 |
| [Deep Learning](Deep%20Learning/README.md) | 108 | 62 | 2018-19 to 2025-26 | 28 |
| [Design an Art for Consumers](Design%20an%20Art%20for%20Consumers/README.md) | 3 | 3 | 2022-23 to 2023-24 | 2 |
| [Design and Analysis of Algorithms](Design%20and%20Analysis%20of%20Algorithms/README.md) | 117 | 87 | 2007-08 to 2025-26 | 18 |
| [Design and Applications of Internet of Things](Design%20and%20Applications%20of%20Internet%20of%20Things/README.md) | 6 | 6 | 2022-23 to 2025-26 | 2 |
| [Design and Drafting of Industrial Buildings](Design%20and%20Drafting%20of%20Industrial%20Buildings/README.md) | 4 | 3 | 2013-14 | 1 |
| [Design Aspects of Industrial Automation](Design%20Aspects%20of%20Industrial%20Automation/README.md) | 3 | 3 | 2014-15 to 2016-17 | 1 |
| [Design for Consumers](Design%20for%20Consumers/README.md) | 2 | 2 | 2024-25 to 2025-26 | 2 |
| [Design of Hydraulic Structures](Design%20of%20Hydraulic%20Structures/README.md) | 5 | 4 | 2022-23 to 2024-25 | 2 |
| [Design of Machine Components](Design%20of%20Machine%20Components/README.md) | 9 | 8 | 2022-23 to 2025-26 | 2 |
| [Design of Machine Elements](Design%20of%20Machine%20Elements/README.md) | 29 | 25 | 2012-13 to 2025-26 | 5 |
| [Design of Machine Elements I](Design%20of%20Machine%20Elements%20I/README.md) | 39 | 33 | 2013-14 to 2022 | 3 |
| [Design of Machine Elements II](Design%20of%20Machine%20Elements%20II/README.md) | 31 | 29 | 2013-14 to 2022-23 | 3 |
| [Design of Machine Elements III](Design%20of%20Machine%20Elements%20III/README.md) | 8 | 8 | 2018-19 to 2025-26 | 1 |
| [Design of Mechanical Systems](Design%20of%20Mechanical%20Systems/README.md) | 17 | 17 | 2013-14 to 2023-24 | 3 |
| [Design of Reinforced Concrete Structures](Design%20of%20Reinforced%20Concrete%20Structures/README.md) | 17 | 13 | 2021-22 to 2025-26 | 5 |
| [Design of Steel Structures](Design%20of%20Steel%20Structures/README.md) | 62 | 55 | 2013-14 to 2025-26 | 4 |
| [Design of Transmission Systems](Design%20of%20Transmission%20Systems/README.md) | 13 | 8 | 2023-24 to 2025-26 | 5 |
| [Design Thinking](Design%20Thinking/README.md) | 1 | 1 | 2022-23 | 1 |
| [Designing with IC](Designing%20with%20IC/README.md) | 4 | 4 | 2005-06 to 2007-08 | 1 |
| [DevOps](DevOps/README.md) | 16 | 10 | 2023-24 to 2025-26 | 6 |
| [DevSecOps](DevSecOps/README.md) | 4 | 4 | 2025-26 | 1 |
| [Digital Circuits and Computer Architecture](Digital%20Circuits%20and%20Computer%20Architecture/README.md) | 8 | 8 | 2024-25 to 2025-26 | 4 |
| [Digital Circuits and Systems](Digital%20Circuits%20and%20Systems/README.md) | 7 | 7 | 2016-17 to 2017-18 | 2 |
| [Digital Communication](Digital%20Communication/README.md) | 45 | 42 | 2006-07 to 2018-19 | 5 |
| [Digital Design](Digital%20Design/README.md) | 31 | 28 | 2006-07 to 2017-18 | 2 |
| [Digital Design and Microprocessor](Digital%20Design%20and%20Microprocessor/README.md) | 8 | 8 | 2005-06 to 2009-10 | 1 |
| [Digital Electronics](Digital%20Electronics/README.md) | 14 | 11 | 2014-15 to 2019-20 | 1 |
| [Digital Forensics](Digital%20Forensics/README.md) | 2 | 2 | 2022-23 to 2023-24 | 1 |
| [Digital Forensics and Incident Response](Digital%20Forensics%20and%20Incident%20Response/README.md) | 9 | 9 | 2022-23 to 2025-26 | 3 |
| [Digital Image and Video Forensics](Digital%20Image%20and%20Video%20Forensics/README.md) | 4 | 4 | 2025-26 | 1 |
| [Digital Image Processing](Digital%20Image%20Processing/README.md) | 1 | 1 | 2025-26 | 1 |
| [Digital Logic Design](Digital%20Logic%20Design/README.md) | 202 | 122 | 2010-11 to 2025-26 | 23 |
| [Digital Logic Design and Analysis](Digital%20Logic%20Design%20and%20Analysis/README.md) | 8 | 7 | 2016-17 to 2019-20 | 1 |
| [Digital Marketing](Digital%20Marketing/README.md) | 32 | 32 | 2021-22 to 2025-26 | 8 |
| [Digital Signal and Image Processing](Digital%20Signal%20and%20Image%20Processing/README.md) | 16 | 15 | 2013-14 to 2025-26 | 3 |
| [Digital Signal Processing](Digital%20Signal%20Processing/README.md) | 105 | 91 | 2005-06 to 2019-20 | 10 |
| [Digital System Design](Digital%20System%20Design/README.md) | 10 | 9 | 2017-18 to 2019-20 | 2 |
| [Digital Techniques](Digital%20Techniques/README.md) | 12 | 8 | 2025-26 | 3 |
| [Digital Television Systems](Digital%20Television%20Systems/README.md) | 6 | 6 | 2017-18 to 2021-22 | 2 |
| [Digital Voice and Broadband Communication](Digital%20Voice%20and%20Broadband%20Communication/README.md) | 24 | 21 | 2017-18 to 2025-26 | 6 |
| [Digital Voice Communication](Digital%20Voice%20Communication/README.md) | 13 | 13 | 2013-14 to 2025-26 | 2 |
| [Disaster Management](Disaster%20Management/README.md) | 102 | 59 | 2022-23 to 2025-26 | 26 |
| [Discrete Mathematics](Discrete%20Mathematics/README.md) | 227 | 135 | 2007-08 to 2025-26 | 35 |
| [Discrete Structures](Discrete%20Structures/README.md) | 28 | 24 | 2013-14 to 2019-20 | 2 |
| [Discrete Time Signal Processing](Discrete%20Time%20Signal%20Processing/README.md) | 47 | 28 | 2017-18 to 2025-26 | 4 |
| [Distributed Computing](Distributed%20Computing/README.md) | 117 | 103 | 2006-07 to 2025-26 | 16 |
| [Distributed Data Processing](Distributed%20Data%20Processing/README.md) | 5 | 5 | 2024-25 to 2025-26 | 2 |
| [Distributed System](Distributed%20System/README.md) | 28 | 23 | 2006-07 to 2018-19 | 3 |
| [Docks and Harbour Engineering](Docks%20and%20Harbour%20Engineering/README.md) | 9 | 5 | 2023-24 to 2024-25 | 3 |
| [Drone Technology](Drone%20Technology/README.md) | 56 | 50 | 2022-23 to 2025-26 | 20 |
| [Dynamic System Modeling and Analysis](Dynamic%20System%20Modeling%20and%20Analysis/README.md) | 7 | 6 | 2017-18 to 2022-23 | 2 |
| [Dynamic Systems Analysis](Dynamic%20Systems%20Analysis/README.md) | 3 | 3 | 2023-24 to 2025-26 | 2 |
| [Dynamic Systems Modeling](Dynamic%20Systems%20Modeling/README.md) | 14 | 14 | 2022-23 to 2025-26 | 2 |
| [Dynamics of Machinery](Dynamics%20of%20Machinery/README.md) | 3 | 3 | 2021-22 | 1 |
| [E-Business](E-Business/README.md) | 32 | 11 | 2007-08 to 2012-13 | 3 |
| [E-Commerce](E-Commerce/README.md) | 29 | 27 | 2013-14 to 2025-26 | 8 |
| [E-Commerce Technologies](E-Commerce%20Technologies/README.md) | 2 | 2 | 2012-13 | 1 |
| [Earthquake Engineering](Earthquake%20Engineering/README.md) | 8 | 7 | 2014-15 to 2023-24 | 2 |
| [Economics of Chemical Projects](Economics%20of%20Chemical%20Projects/README.md) | 12 | 12 | 2011-12 to 2018-19 | 1 |
| [Economics of Housing](Economics%20of%20Housing/README.md) | 5 | 5 | 2015 to 2018-19 | 1 |
| [Edge Computing](Edge%20Computing/README.md) | 3 | 3 | 2024-25 to 2025-26 | 2 |
| [Electric and Hybrid Automotive Technology](Electric%20and%20Hybrid%20Automotive%20Technology/README.md) | 20 | 15 | 2022 to 2025-26 | 7 |
| [Electric and Hybrid Electric Vehicle Technology](Electric%20and%20Hybrid%20Electric%20Vehicle%20Technology/README.md) | 3 | 3 | 2018-19 to 2019-20 | 1 |
| [Electrical Drive](Electrical%20Drive/README.md) | 1 | 1 | 2018-19 | 1 |
| [Electrical Drives and Traction](Electrical%20Drives%20and%20Traction/README.md) | 2 | 2 | 2017-18 to 2018-19 | 1 |
| [Electrical Machine II](Electrical%20Machine%20II/README.md) | 4 | 3 | 2017-18 to 2019-20 | 2 |
| [Electrical Machines I](Electrical%20Machines%20I/README.md) | 5 | 5 | 2016-17 to 2017-18 | 2 |
| [Electrical Network Analysis and Synthesis](Electrical%20Network%20Analysis%20and%20Synthesis/README.md) | 38 | 37 | 2010-11 to 2018-19 | 2 |
| [Electrical Power](Electrical%20Power/README.md) | 2 | 2 | 2018-19 | 1 |
| [Electrical Power I](Electrical%20Power%20I/README.md) | 4 | 4 | 2017-18 to 2019-20 | 1 |
| [Electrical System Design](Electrical%20System%20Design/README.md) | 2 | 2 | 2018-19 to 2019-20 | 1 |
| [Electrical Technology](Electrical%20Technology/README.md) | 12 | 11 | 2015-16 to 2019-20 | 1 |
| [Electromagnetic Field Theory](Electromagnetic%20Field%20Theory/README.md) | 54 | 49 | 2010-11 to 2022-23 | 6 |
| [Electromagnetic Wave Theory](Electromagnetic%20Wave%20Theory/README.md) | 9 | 8 | 2021-22 to 2024-25 | 2 |
| [Electronic Circuit Analysis and Design](Electronic%20Circuit%20Analysis%20and%20Design/README.md) | 25 | 23 | 2010-11 to 2018-19 | 1 |
| [Electronic Circuit Analysis and Design I](Electronic%20Circuit%20Analysis%20and%20Design%20I/README.md) | 4 | 4 | 2016-17 to 2018-19 | 1 |
| [Electronic Circuit Analysis and Design II](Electronic%20Circuit%20Analysis%20and%20Design%20II/README.md) | 4 | 4 | 2016-17 to 2018-19 | 1 |
| [Electronic Circuit and Design](Electronic%20Circuit%20and%20Design/README.md) | 20 | 20 | 2013-14 to 2018-19 | 1 |
| [Electronic Commerce](Electronic%20Commerce/README.md) | 14 | 14 | 2013-14 to 2019-20 | 2 |
| [Electronic Devices](Electronic%20Devices/README.md) | 3 | 2 | 2019-20 | 3 |
| [Electronic Devices and Circuits](Electronic%20Devices%20and%20Circuits/README.md) | 28 | 25 | 2014-15 to 2024-25 | 2 |
| [Electronic Instrumentation](Electronic%20Instrumentation/README.md) | 5 | 5 | 2016-17 to 2018-19 | 1 |
| [Electronic Instrumentation and Control](Electronic%20Instrumentation%20and%20Control/README.md) | 3 | 3 | 2013-14 | 1 |
| [Electronic Materials and Components](Electronic%20Materials%20and%20Components/README.md) | 19 | 12 | 2015-16 to 2019-20 | 2 |
| [Electronic Power II](Electronic%20Power%20II/README.md) | 2 | 2 | 2017-18 to 2018-19 | 1 |
| [Electronic Systems](Electronic%20Systems/README.md) | 13 | 13 | 2022-23 to 2025-26 | 2 |
| [Electronics in Defence Systems](Electronics%20in%20Defence%20Systems/README.md) | 1 | 1 | 2015-16 | 1 |
| [Electronics Simulation and Modeling](Electronics%20Simulation%20and%20Modeling/README.md) | 1 | 1 | 2010-11 | 1 |
| [Elementary Algebra, Probability and Statistics](Elementary%20Algebra%2C%20Probability%20and%20Statistics/README.md) | 4 | 2 | 2021-22 | 2 |
| [Elements of Automation](Elements%20of%20Automation/README.md) | 34 | 22 | 2022-23 to 2025-26 | 7 |
| [Elements of Biology](Elements%20of%20Biology/README.md) | 216 | 180 | 2019-20 to 2025-26 | 36 |
| [Elements of Electrical Engineering](Elements%20of%20Electrical%20Engineering/README.md) | 17 | 16 | 2014-15 to 2021-22 | 1 |
| [Elements of Mechanical Engineering](Elements%20of%20Mechanical%20Engineering/README.md) | 9 | 9 | 2022 to 2025-26 | 2 |
| [Elements of Project Management](Elements%20of%20Project%20Management/README.md) | 65 | 46 | 2021-22 to 2025-26 | 18 |
| [Embedded Processors and Real-Time Systems](Embedded%20Processors%20and%20Real-Time%20Systems/README.md) | 5 | 5 | 2025-26 | 2 |
| [Embedded System Design](Embedded%20System%20Design/README.md) | 13 | 13 | 2013-14 to 2025-26 | 5 |
| [Embedded Systems](Embedded%20Systems/README.md) | 53 | 38 | 2011-12 to 2025-26 | 13 |
| [Emerging Technologies in Key Industry Sectors](Emerging%20Technologies%20in%20Key%20Industry%20Sectors/README.md) | 1 | 1 | 2017-18 | 1 |
| [Emerging Trends in Technology](Emerging%20Trends%20in%20Technology/README.md) | 2 | 2 | 2017-18 | 1 |
| [Energy Economics Politics and Management](Energy%20Economics%20Politics%20and%20Management/README.md) | 1 | 1 | 2022-23 | 1 |
| [Energy Management](Energy%20Management/README.md) | 9 | 9 | 2008-09 to 2021-22 | 2 |
| [Energy Management and Audit](Energy%20Management%20and%20Audit/README.md) | 2 | 1 | 2018-19 | 2 |
| [Energy Resources and Generation](Energy%20Resources%20and%20Generation/README.md) | 5 | 5 | 2016-17 to 2017-18 | 2 |
| [Energy System Design](Energy%20System%20Design/README.md) | 8 | 8 | 2013-14 to 2019-20 | 1 |
| [Engineering and Solid Mechanics](Engineering%20and%20Solid%20Mechanics/README.md) | 1 | 1 | 2019-20 | 1 |
| [Engineering Chemistry](Engineering%20Chemistry/README.md) | 50 | 49 | 2013-14 to 2019-20 | 3 |
| [Engineering Drawing](Engineering%20Drawing/README.md) | 21 | 21 | 2004-05 to 2024-25 | 4 |
| [Engineering Economics and Accounting](Engineering%20Economics%20and%20Accounting/README.md) | 11 | 11 | 2013-14 to 2018-19 | 1 |
| [Engineering Economics, Costing and Accounting](Engineering%20Economics%2C%20Costing%20and%20Accounting/README.md) | 3 | 3 | 2018-19 to 2022-23 | 1 |
| [Engineering Geology](Engineering%20Geology/README.md) | 36 | 32 | 2013-14 to 2018-19 | 3 |
| [Engineering Graphics](Engineering%20Graphics/README.md) | 3 | 3 | 2022-23 to 2024-25 | 1 |
| [Engineering Graphics and Design](Engineering%20Graphics%20and%20Design/README.md) | 8 | 6 | 2022-23 to 2024-25 | 2 |
| [Engineering Mathematics I](Engineering%20Mathematics%20I/README.md) | 47 | 46 | 2013-14 to 2020-21 | 2 |
| [Engineering Mathematics II](Engineering%20Mathematics%20II/README.md) | 37 | 33 | 2013-14 to 2018-19 | 2 |
| [Engineering Mathematics III](Engineering%20Mathematics%20III/README.md) | 188 | 59 | 2013-14 to 2019-20 | 16 |
| [Engineering Mathematics IV](Engineering%20Mathematics%20IV/README.md) | 123 | 40 | 2010-11 to 2022-23 | 12 |
| [Engineering Mechanics](Engineering%20Mechanics/README.md) | 180 | 123 | 2004-05 to 2025-26 | 17 |
| [Engineering Mechanics I](Engineering%20Mechanics%20I/README.md) | 39 | 39 | 2013-14 to 2017-18 | 2 |
| [Engineering Mechanics II](Engineering%20Mechanics%20II/README.md) | 34 | 31 | 2013-14 to 2017-18 | 2 |
| [Engineering Metrology and Measurements](Engineering%20Metrology%20and%20Measurements/README.md) | 2 | 2 | 2025-26 | 1 |
| [Engineering Physics](Engineering%20Physics/README.md) | 57 | 53 | 2013-14 to 2019-20 | 3 |
| [Engineering Physics II](Engineering%20Physics%20II/README.md) | 3 | 3 | 2021-22 to 2022-23 | 2 |
| [Engineering Thermodynamics](Engineering%20Thermodynamics/README.md) | 68 | 54 | 2013-14 to 2025-26 | 5 |
| [English](English/README.md) | 5 | 5 | 2018-19 to 2019-20 | 2 |
| [English Communication](English%20Communication/README.md) | 7 | 4 | 2021-22 to 2022-23 | 3 |
| [Enterprise Planning System](Enterprise%20Planning%20System/README.md) | 35 | 14 | 2008-09 to 2014-15 | 4 |
| [Enterprise System](Enterprise%20System/README.md) | 4 | 4 | 2022-23 to 2024-25 | 1 |
| [Entrepreneurship Development](Entrepreneurship%20Development/README.md) | 5 | 5 | 2016-17 to 2019-20 | 1 |
| [Entrepreneurship Development and Startups](Entrepreneurship%20Development%20and%20Startups/README.md) | 8 | 8 | 2025-26 | 4 |
| [Entrepreneurship Management](Entrepreneurship%20Management/README.md) | 13 | 13 | 2008-09 to 2015-16 | 1 |
| [Environment Management](Environment%20Management/README.md) | 114 | 60 | 2008-09 to 2025-26 | 33 |
| [Environmental Engineening and Management](Environmental%20Engineening%20and%20Management/README.md) | 5 | 5 | 2011-12 to 2012-13 | 1 |
| [Environmental Engineering](Environmental%20Engineering/README.md) | 34 | 28 | 2007-08 to 2022-23 | 4 |
| [Environmental Engineering and Management Systems](Environmental%20Engineering%20and%20Management%20Systems/README.md) | 15 | 14 | 2013-14 to 2019-20 | 2 |
| [Environmental Engineering I](Environmental%20Engineering%20I/README.md) | 22 | 20 | 2011-12 to 2019-20 | 2 |
| [Environmental Engineering II](Environmental%20Engineering%20II/README.md) | 25 | 20 | 2014-15 to 2018-19 | 2 |
| [Environmental Impact Assessment and Auditing](Environmental%20Impact%20Assessment%20and%20Auditing/README.md) | 6 | 6 | 2013-14 to 2025-26 | 2 |
| [Ergonomics in Design](Ergonomics%20in%20Design/README.md) | 22 | 15 | 2023-24 to 2025-26 | 5 |
| [Essentials of Computer Science](Essentials%20of%20Computer%20Science/README.md) | 4 | 4 | 2025-26 | 1 |
| [Ethical Hacking](Ethical%20Hacking/README.md) | 41 | 18 | 2021-22 to 2025-26 | 12 |
| [Ethics in Data Science](Ethics%20in%20Data%20Science/README.md) | 3 | 3 | 2024-25 | 2 |
| [ETL-Data Gathering and Loading](ETL-Data%20Gathering%20and%20Loading/README.md) | 7 | 7 | 2024-25 | 4 |
| [Event Driven and UI Programming](Event%20Driven%20and%20UI%20Programming/README.md) | 16 | 16 | 2023-24 to 2025-26 | 3 |
| [Evolutionary Computing](Evolutionary%20Computing/README.md) | 11 | 10 | 2023-24 to 2025-26 | 4 |
| [Facilities Management](Facilities%20Management/README.md) | 2 | 2 | 2016-17 to 2018-19 | 1 |
| [Fiber Optic Communication and Networks](Fiber%20Optic%20Communication%20and%20Networks/README.md) | 21 | 16 | 2021-22 to 2025-26 | 4 |
| [Film Appreciation](Film%20Appreciation/README.md) | 67 | 13 | 2022 to 2025-26 | 30 |
| [Finance Analytics](Finance%20Analytics/README.md) | 8 | 8 | 2015-16 to 2023-24 | 1 |
| [Financial Accounting](Financial%20Accounting/README.md) | 62 | 41 | 2009-10 to 2019-20 | 6 |
| [Financial Accounting and Analysis](Financial%20Accounting%20and%20Analysis/README.md) | 16 | 13 | 2025-26 | 5 |
| [Financial Analysis and Accounting](Financial%20Analysis%20and%20Accounting/README.md) | 59 | 28 | 2007-08 to 2024-25 | 5 |
| [Financial Analysis and Working Capital Management](Financial%20Analysis%20and%20Working%20Capital%20Management/README.md) | 19 | 18 | 2015-16 to 2023-24 | 1 |
| [Financial Analytics](Financial%20Analytics/README.md) | 3 | 3 | 2017-18 to 2018-19 | 1 |
| [Financial Analytics using Time Series and LSTM](Financial%20Analytics%20using%20Time%20Series%20and%20LSTM/README.md) | 4 | 4 | 2019-20 to 2024-25 | 1 |
| [Financial and Cost Accounting](Financial%20and%20Cost%20Accounting/README.md) | 12 | 11 | 2021-22 to 2025-26 | 2 |
| [Financial Derivatives](Financial%20Derivatives/README.md) | 83 | 68 | 2022-23 to 2025-26 | 20 |
| [Financial Engineering](Financial%20Engineering/README.md) | 39 | 39 | 2008-09 to 2025-26 | 7 |
| [Financial Institutions and Markets](Financial%20Institutions%20and%20Markets/README.md) | 20 | 19 | 2008-09 to 2021-22 | 3 |
| [Financial Institutions, Markets, Instruments and Services](Financial%20Institutions%2C%20Markets%2C%20Instruments%20and%20Services/README.md) | 88 | 54 | 2021-22 to 2025-26 | 26 |
| [Financial Management](Financial%20Management/README.md) | 125 | 102 | 2008-09 to 2025-26 | 16 |
| [Financial Markets and Risk Analytics](Financial%20Markets%20and%20Risk%20Analytics/README.md) | 7 | 4 | 2022-23 to 2023-24 | 2 |
| [Financial Planning and Portfolio Management](Financial%20Planning%20and%20Portfolio%20Management/README.md) | 44 | 43 | 2015-16 to 2025-26 | 8 |
| [Financial Risk Management](Financial%20Risk%20Management/README.md) | 72 | 57 | 2010-11 to 2025-26 | 8 |
| [Financial Technology](Financial%20Technology/README.md) | 19 | 19 | 2017-18 to 2025-26 | 6 |
| [Finite Element Analysis](Finite%20Element%20Analysis/README.md) | 52 | 47 | 2013-14 to 2025-26 | 8 |
| [Finite Element Analysis in Civil Engineering](Finite%20Element%20Analysis%20in%20Civil%20Engineering/README.md) | 2 | 2 | 2019-20 | 2 |
| [Finite Element Methods](Finite%20Element%20Methods/README.md) | 5 | 5 | 2012-13 | 2 |
| [Flexible Manufacturing Systems](Flexible%20Manufacturing%20Systems/README.md) | 4 | 4 | 2016-17 to 2019-20 | 1 |
| [Fluid Machinery](Fluid%20Machinery/README.md) | 38 | 38 | 2011-12 to 2021-22 | 3 |
| [Fluid Mechanics](Fluid%20Mechanics/README.md) | 142 | 125 | 2005-06 to 2025-26 | 10 |
| [Fluid Mechanics and Hydraulic Machinery](Fluid%20Mechanics%20and%20Hydraulic%20Machinery/README.md) | 2 | 2 | 2025-26 | 1 |
| [Fluid Mechanics and Hydraulics](Fluid%20Mechanics%20and%20Hydraulics/README.md) | 16 | 15 | 2022-23 to 2025-26 | 3 |
| [Fluid Mechanics and Machinery](Fluid%20Mechanics%20and%20Machinery/README.md) | 12 | 10 | 2014-15 to 2018-19 | 1 |
| [Fluid Mechanics I](Fluid%20Mechanics%20I/README.md) | 16 | 15 | 2013-14 to 2019-20 | 2 |
| [Fluid Mechanics II](Fluid%20Mechanics%20II/README.md) | 8 | 8 | 2011-12 to 2018-19 | 2 |
| [Fluid Power Automation](Fluid%20Power%20Automation/README.md) | 9 | 9 | 2014-15 to 2025-26 | 3 |
| [Food and Process Engineering](Food%20and%20Process%20Engineering/README.md) | 1 | 1 | 2010-11 | 1 |
| [Food Processing](Food%20Processing/README.md) | 10 | 10 | 2010-11 to 2018-19 | 1 |
| [Food Processing and Technology](Food%20Processing%20and%20Technology/README.md) | 2 | 2 | year not stated | 1 |
| [Formal Language and Automata Theory](Formal%20Language%20and%20Automata%20Theory/README.md) | 10 | 10 | 2022-23 to 2025-26 | 3 |
| [Foundation Engineering](Foundation%20Engineering/README.md) | 10 | 7 | 2022-23 to 2025-26 | 3 |
| [Foundations of Business](Foundations%20of%20Business/README.md) | 12 | 11 | 2022-23 to 2024-25 | 2 |
| [Foundations of Entrepreneurship](Foundations%20of%20Entrepreneurship/README.md) | 11 | 11 | 2022-23 to 2025-26 | 3 |
| [Foundations of Machine Learning](Foundations%20of%20Machine%20Learning/README.md) | 14 | 7 | 2022-23 to 2025-26 | 5 |
| [French](French/README.md) | 24 | 8 | 2023-24 to 2025-26 | 15 |
| [Fundamentals of Blockchain](Fundamentals%20of%20Blockchain/README.md) | 2 | 2 | 2022-23 | 1 |
| [Fundamentals of Calculus and Vector Algebra](Fundamentals%20of%20Calculus%20and%20Vector%20Algebra/README.md) | 3 | 3 | 2021-22 | 1 |
| [Fundamentals of Climate Change](Fundamentals%20of%20Climate%20Change/README.md) | 93 | 61 | 2021-22 to 2025-26 | 27 |
| [Fundamentals of Computer Science](Fundamentals%20of%20Computer%20Science/README.md) | 3 | 3 | 2019-20 to 2022-23 | 1 |
| [Fundamentals of Control Systems](Fundamentals%20of%20Control%20Systems/README.md) | 3 | 3 | 2021-22 to 2022-23 | 1 |
| [Fundamentals of Digital Transformation](Fundamentals%20of%20Digital%20Transformation/README.md) | 4 | 2 | 2022 to 2022-23 | 2 |
| [Fundamentals of E-Commerce](Fundamentals%20of%20E-Commerce/README.md) | 26 | 22 | 2022-23 to 2025-26 | 4 |
| [Fundamentals of Economics](Fundamentals%20of%20Economics/README.md) | 7 | 7 | 2021-22 to 2024-25 | 2 |
| [Fundamentals of Engineering Design](Fundamentals%20of%20Engineering%20Design/README.md) | 14 | 14 | 2022-23 to 2025-26 | 2 |
| [Fundamentals of Engineering Mechanics](Fundamentals%20of%20Engineering%20Mechanics/README.md) | 17 | 16 | 2014-15 to 2021-22 | 1 |
| [Fundamentals of Financial Accounting](Fundamentals%20of%20Financial%20Accounting/README.md) | 8 | 3 | 2012-13 | 3 |
| [Fundamentals of Fuels and Lubricants](Fundamentals%20of%20Fuels%20and%20Lubricants/README.md) | 1 | 1 | 2021-22 | 1 |
| [Fundamentals of Linux and Shell Scripting](Fundamentals%20of%20Linux%20and%20Shell%20Scripting/README.md) | 1 | 1 | 2025-26 | 1 |
| [Fundamentals of Machine Learning](Fundamentals%20of%20Machine%20Learning/README.md) | 10 | 10 | 2022-23 to 2025-26 | 2 |
| [Fundamentals of Management](Fundamentals%20of%20Management/README.md) | 8 | 7 | 2022-23 to 2025-26 | 1 |
| [Fundamentals of Mechanics-Statics](Fundamentals%20of%20Mechanics-Statics/README.md) | 11 | 11 | 2022-23 to 2023-24 | 3 |
| [Fundamentals of Microwave Engineering](Fundamentals%20of%20Microwave%20Engineering/README.md) | 33 | 27 | 2007-08 to 2019-20 | 4 |
| [Fundamentals of Operating Systems](Fundamentals%20of%20Operating%20Systems/README.md) | 10 | 10 | 2023-24 to 2025-26 | 2 |
| [Fundamentals of Physics](Fundamentals%20of%20Physics/README.md) | 1 | 1 | 2019-20 | 1 |
| [Fundamentals of Structural Analysis](Fundamentals%20of%20Structural%20Analysis/README.md) | 1 | 1 | 2016-17 | 1 |
| [Fundamentals of Web Technology](Fundamentals%20of%20Web%20Technology/README.md) | 21 | 20 | 2013-14 to 2019-20 | 2 |
| [Fuzzy Logic and Neural Networks](Fuzzy%20Logic%20and%20Neural%20Networks/README.md) | 13 | 12 | 2006-07 to 2018-19 | 3 |
| [Game Design](Game%20Design/README.md) | 16 | 9 | 2022-23 to 2024-25 | 4 |
| [Gender Communication](Gender%20Communication/README.md) | 70 | 23 | 2022-23 to 2025-26 | 29 |
| [Generative Adversarial Networks](Generative%20Adversarial%20Networks/README.md) | 6 | 6 | 2024-25 to 2025-26 | 2 |
| [Generative AI](Generative%20AI/README.md) | 9 | 9 | 2025-26 | 3 |
| [Generative AI for Business](Generative%20AI%20for%20Business/README.md) | 8 | 8 | 2025-26 | 4 |
| [Generative AI with Large Language Models](Generative%20AI%20with%20Large%20Language%20Models/README.md) | 7 | 5 | 2024-25 to 2025-26 | 2 |
| [Geographical Information System](Geographical%20Information%20System/README.md) | 4 | 4 | 2013-14 | 1 |
| [Geology](Geology/README.md) | 23 | 21 | 2013-14 to 2025-26 | 4 |
| [Geotech I](Geotech%20I/README.md) | 5 | 5 | 2011-12 to 2012-13 | 1 |
| [Geotech II](Geotech%20II/README.md) | 7 | 7 | 2011-12 | 1 |
| [Geotechnical Engineering I](Geotechnical%20Engineering%20I/README.md) | 48 | 44 | 2013-14 to 2019-20 | 3 |
| [Geotechnical Engineering II](Geotechnical%20Engineering%20II/README.md) | 35 | 30 | 2013-14 to 2019-20 | 3 |
| [German](German/README.md) | 89 | 55 | 2022 to 2025-26 | 28 |
| [Global Navigation Satellite Systems](Global%20Navigation%20Satellite%20Systems/README.md) | 5 | 3 | 2021-22 to 2022-23 | 2 |
| [Global Supply Chain Management](Global%20Supply%20Chain%20Management/README.md) | 8 | 8 | 2025-26 | 4 |
| [Global Trends in Infrastructure Management](Global%20Trends%20in%20Infrastructure%20Management/README.md) | 4 | 4 | 2017-18 to 2025-26 | 2 |
| [Governance Legal and Ethical Aspects](Governance%20Legal%20and%20Ethical%20Aspects/README.md) | 1 | 1 | 2017-18 | 1 |
| [Graph Theory and Applications](Graph%20Theory%20and%20Applications/README.md) | 10 | 5 | 2022-23 to 2023-24 | 2 |
| [Graphology for Personal Development](Graphology%20for%20Personal%20Development/README.md) | 17 | 4 | 2022-23 to 2023-24 | 13 |
| [Green and Intelligent Buildings](Green%20and%20Intelligent%20Buildings/README.md) | 20 | 18 | 2014-15 to 2025-26 | 3 |
| [Happiness at Work](Happiness%20at%20Work/README.md) | 41 | 18 | 2023-24 to 2025-26 | 16 |
| [Heat Transfer](Heat%20Transfer/README.md) | 68 | 59 | 2013-14 to 2025-26 | 5 |
| [Heat Transfer Operations](Heat%20Transfer%20Operations/README.md) | 26 | 26 | 2005-06 to 2019-20 | 1 |
| [High Performance Computing](High%20Performance%20Computing/README.md) | 1 | 1 | 2017-18 | 1 |
| [High Voltage Engineering](High%20Voltage%20Engineering/README.md) | 2 | 2 | 2018-19 | 1 |
| [Highway and Railway Engineering](Highway%20and%20Railway%20Engineering/README.md) | 28 | 25 | 2013-14 to 2019-20 | 2 |
| [HRD and Professional Ethics](HRD%20and%20Professional%20Ethics/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Human and Legal Aspects of Cybersecurity](Human%20and%20Legal%20Aspects%20of%20Cybersecurity/README.md) | 8 | 8 | 2023-24 to 2025-26 | 2 |
| [Human Centered Cyber Security](Human%20Centered%20Cyber%20Security/README.md) | 5 | 5 | 2022-23 to 2024-25 | 2 |
| [Human Computer Interaction](Human%20Computer%20Interaction/README.md) | 87 | 69 | 2010-11 to 2025-26 | 24 |
| [Human Computer Interface](Human%20Computer%20Interface/README.md) | 16 | 16 | 2013-14 to 2025-26 | 2 |
| [Human Machine Interface](Human%20Machine%20Interface/README.md) | 7 | 6 | 2022-23 to 2025-26 | 2 |
| [Human Machine Interface and Data Acquisition](Human%20Machine%20Interface%20and%20Data%20Acquisition/README.md) | 2 | 1 | 2022-23 | 2 |
| [Human Resource Management](Human%20Resource%20Management/README.md) | 67 | 51 | 2007-08 to 2025-26 | 12 |
| [Hydraulic and Pneumatic Systems](Hydraulic%20and%20Pneumatic%20Systems/README.md) | 10 | 10 | 2015-16 to 2024-25 | 3 |
| [Hydraulic and Pneumatics](Hydraulic%20and%20Pneumatics/README.md) | 2 | 2 | year not stated | 1 |
| [Hydraulic Engineering](Hydraulic%20Engineering/README.md) | 41 | 37 | 2013-14 to 2019-20 | 3 |
| [Hydraulic Machinery](Hydraulic%20Machinery/README.md) | 37 | 34 | 2011-12 to 2021-22 | 3 |
| [Hydraulics and Fluid Machinery](Hydraulics%20and%20Fluid%20Machinery/README.md) | 13 | 12 | 2022-23 to 2025-26 | 3 |
| [Hydrogeology and Groundwater Modelling](Hydrogeology%20and%20Groundwater%20Modelling/README.md) | 1 | 1 | 2023-24 | 1 |
| [Hydrology](Hydrology/README.md) | 3 | 3 | 2011-12 | 1 |
| [I C Engines](I%20C%20Engines/README.md) | 31 | 26 | 2011-12 to 2021-22 | 3 |
| [Image and Signal Processing](Image%20and%20Signal%20Processing/README.md) | 1 | 1 | 2019-20 | 1 |
| [Image and Video Processing](Image%20and%20Video%20Processing/README.md) | 68 | 39 | 2017-18 to 2025-26 | 11 |
| [Image Processing](Image%20Processing/README.md) | 60 | 55 | 2006-07 to 2023-24 | 8 |
| [Image Processing and Pattern Recognition](Image%20Processing%20and%20Pattern%20Recognition/README.md) | 1 | 1 | 2022-23 | 1 |
| [Indian Financial System](Indian%20Financial%20System/README.md) | 16 | 16 | 2018-19 to 2025-26 | 4 |
| [Indian Knowledge System](Indian%20Knowledge%20System/README.md) | 39 | 8 | 2024-25 to 2025-26 | 17 |
| [Industrial Automation](Industrial%20Automation/README.md) | 2 | 2 | 2011-12 to 2012-13 | 1 |
| [Industrial Automation and Robotics](Industrial%20Automation%20and%20Robotics/README.md) | 17 | 7 | 2022 to 2025-26 | 5 |
| [Industrial Data Communication](Industrial%20Data%20Communication/README.md) | 4 | 4 | 2022-23 to 2024-25 | 1 |
| [Industrial Drivers and Control Systems](Industrial%20Drivers%20and%20Control%20Systems/README.md) | 3 | 3 | 2014-15 to 2016-17 | 1 |
| [Industrial Drives](Industrial%20Drives/README.md) | 21 | 21 | 2015-16 to 2025-26 | 2 |
| [Industrial Economics and Management](Industrial%20Economics%20and%20Management/README.md) | 43 | 37 | 2013-14 to 2022-23 | 6 |
| [Industrial Electronics](Industrial%20Electronics/README.md) | 38 | 37 | 2013-14 to 2019-20 | 4 |
| [Industrial Engineering](Industrial%20Engineering/README.md) | 53 | 51 | 2013-14 to 2025-26 | 6 |
| [Industrial Engineering and Ergonomics](Industrial%20Engineering%20and%20Ergonomics/README.md) | 10 | 9 | 2022-23 to 2025-26 | 2 |
| [Industrial Engineering and Quality Management](Industrial%20Engineering%20and%20Quality%20Management/README.md) | 2 | 2 | 2022-23 | 1 |
| [Industrial IoT](Industrial%20IoT/README.md) | 17 | 4 | 2022-23 to 2023-24 | 13 |
| [Industrial IoT Markets and Project Planning](Industrial%20IoT%20Markets%20and%20Project%20Planning/README.md) | 9 | 5 | 2021-22 to 2022-23 | 2 |
| [Industrial Marketing](Industrial%20Marketing/README.md) | 21 | 10 | 2007-08 to 2012-13 | 3 |
| [Industrial Psychology](Industrial%20Psychology/README.md) | 3 | 3 | 2022-23 to 2024-25 | 1 |
| [Industrial Relations and Peace](Industrial%20Relations%20and%20Peace/README.md) | 10 | 6 | 2022-23 to 2025-26 | 3 |
| [Industrial Relations and Peace Studies](Industrial%20Relations%20and%20Peace%20Studies/README.md) | 26 | 26 | 2025-26 | 13 |
| [Industrial Robotics](Industrial%20Robotics/README.md) | 7 | 7 | 2014-15 to 2018-19 | 2 |
| [Industrial Robotics and Control](Industrial%20Robotics%20and%20Control/README.md) | 3 | 2 | 2021-22 to 2022-23 | 2 |
| [Industrial Robotics and Motion Control](Industrial%20Robotics%20and%20Motion%20Control/README.md) | 4 | 4 | 2023-24 to 2025-26 | 1 |
| [Industrial Safety](Industrial%20Safety/README.md) | 20 | 20 | 2006-07 to 2022-23 | 1 |
| [Industrial Waste Management](Industrial%20Waste%20Management/README.md) | 6 | 4 | 2023-24 to 2024-25 | 2 |
| [Industrial Waste Treatment](Industrial%20Waste%20Treatment/README.md) | 4 | 4 | 2013-14 to 2024-25 | 1 |
| [Information and Communication Technology Management](Information%20and%20Communication%20Technology%20Management/README.md) | 13 | 12 | 2015-16 to 2017-18 | 1 |
| [Information Security](Information%20Security/README.md) | 59 | 58 | 2008-09 to 2025-26 | 8 |
| [Information Security and Privacy](Information%20Security%20and%20Privacy/README.md) | 27 | 16 | 2022-23 to 2025-26 | 6 |
| [Information Security Assistance and Forensics](Information%20Security%20Assistance%20and%20Forensics/README.md) | 7 | 7 | 2013-14 to 2018-19 | 1 |
| [Information Storage and Management](Information%20Storage%20and%20Management/README.md) | 26 | 24 | 2012-13 to 2019-20 | 7 |
| [Information System for Managers](Information%20System%20for%20Managers/README.md) | 34 | 16 | 2007-08 to 2014-15 | 5 |
| [Information System Management](Information%20System%20Management/README.md) | 53 | 52 | 2012-13 to 2025-26 | 9 |
| [Information Systems](Information%20Systems/README.md) | 2 | 2 | 2007-08 to 2008-09 | 1 |
| [Information Systems Audit](Information%20Systems%20Audit/README.md) | 12 | 12 | 2023-24 to 2025-26 | 4 |
| [Information Systems Security](Information%20Systems%20Security/README.md) | 15 | 10 | 2023-24 to 2025-26 | 4 |
| [Information Technology Project Management](Information%20Technology%20Project%20Management/README.md) | 2 | 2 | 2022-23 | 1 |
| [Information Theory and Coding](Information%20Theory%20and%20Coding/README.md) | 10 | 5 | 2005-06 to 2009-10 | 2 |
| [Infrastructure Development](Infrastructure%20Development/README.md) | 6 | 6 | 2011-12 to 2014-15 | 2 |
| [Infrastructure Management in Industry](Infrastructure%20Management%20in%20Industry/README.md) | 2 | 2 | 2016-17 to 2017-18 | 1 |
| [Innovations Management](Innovations%20Management/README.md) | 1 | 1 | 2016-17 | 1 |
| [Inorganic Process Technologies](Inorganic%20Process%20Technologies/README.md) | 1 | 1 | 2021-22 | 1 |
| [Instrumentation](Instrumentation/README.md) | 37 | 36 | 2013-14 to 2019-20 | 3 |
| [Instrumentation and Process Control](Instrumentation%20and%20Process%20Control/README.md) | 29 | 27 | 2006-07 to 2022-23 | 1 |
| [Instrumentation Fundamentals](Instrumentation%20Fundamentals/README.md) | 22 | 20 | 2004-05 to 2012-13 | 1 |
| [Integral Transforms](Integral%20Transforms/README.md) | 45 | 24 | 2021-22 to 2025-26 | 11 |
| [Integrated Marketing Communication](Integrated%20Marketing%20Communication/README.md) | 32 | 26 | 2008-09 to 2025-26 | 7 |
| [Intellectual Property Management](Intellectual%20Property%20Management/README.md) | 29 | 11 | 2008-09 to 2012-13 | 4 |
| [Intelligent Systems](Intelligent%20Systems/README.md) | 25 | 25 | 2013-14 to 2025-26 | 7 |
| [Intelligent Systems I](Intelligent%20Systems%20I/README.md) | 24 | 22 | 2022-23 to 2025-26 | 4 |
| [Intelligent Systems II](Intelligent%20Systems%20II/README.md) | 16 | 10 | 2023-24 to 2025-26 | 4 |
| [Interior Design](Interior%20Design/README.md) | 79 | 40 | 2022-23 to 2025-26 | 23 |
| [International Finance](International%20Finance/README.md) | 51 | 43 | 2008-09 to 2025-26 | 9 |
| [International Marketing](International%20Marketing/README.md) | 46 | 46 | 2008-09 to 2025-26 | 8 |
| [International Project Management](International%20Project%20Management/README.md) | 1 | 1 | 2014-15 | 1 |
| [International Sourcing](International%20Sourcing/README.md) | 8 | 8 | 2011-12 to 2014-15 | 1 |
| [Internet of Things](Internet%20of%20Things/README.md) | 35 | 23 | 2018-19 to 2025-26 | 11 |
| [Internet of Things Analytics](Internet%20of%20Things%20Analytics/README.md) | 9 | 8 | 2022-23 to 2023-24 | 2 |
| [Introduction to 3D Printing Technology](Introduction%20to%203D%20Printing%20Technology/README.md) | 10 | 10 | 2022 to 2025-26 | 2 |
| [Introduction to App Development](Introduction%20to%20App%20Development/README.md) | 1 | 1 | year not stated | 1 |
| [Introduction to Automation](Introduction%20to%20Automation/README.md) | 21 | 20 | 2013-14 to 2019-20 | 4 |
| [Introduction to Blockchain](Introduction%20to%20Blockchain/README.md) | 9 | 6 | 2022-23 | 3 |
| [Introduction to Business Analytics and Business Intelligence](Introduction%20to%20Business%20Analytics%20and%20Business%20Intelligence/README.md) | 9 | 9 | 2022-23 to 2024-25 | 2 |
| [Introduction to Business Analytics Modeling](Introduction%20to%20Business%20Analytics%20Modeling/README.md) | 4 | 4 | 2021-22 to 2022-23 | 2 |
| [Introduction to Business Statistics, Analytics and Modeling I](Introduction%20to%20Business%20Statistics%2C%20Analytics%20and%20Modeling%20I/README.md) | 9 | 9 | 2021 to 2024-25 | 2 |
| [Introduction to Business Statistics, Analytics and Modeling II](Introduction%20to%20Business%20Statistics%2C%20Analytics%20and%20Modeling%20II/README.md) | 11 | 11 | 2023 to 2025-26 | 3 |
| [Introduction to Chemistry](Introduction%20to%20Chemistry/README.md) | 16 | 15 | 2021-22 to 2025-26 | 3 |
| [Introduction to Cloud Computing](Introduction%20to%20Cloud%20Computing/README.md) | 32 | 29 | 2013-14 to 2022-23 | 7 |
| [Introduction to Cloud Computing and Blockchain](Introduction%20to%20Cloud%20Computing%20and%20Blockchain/README.md) | 2 | 2 | 2023-24 to 2025-26 | 1 |
| [Introduction to Cloud Computing and Blockchain Technology](Introduction%20to%20Cloud%20Computing%20and%20Blockchain%20Technology/README.md) | 10 | 10 | 2023-24 to 2025-26 | 2 |
| [Introduction to Cryptography](Introduction%20to%20Cryptography/README.md) | 30 | 25 | 2021-22 to 2025-26 | 11 |
| [Introduction to Cybersecurity](Introduction%20to%20Cybersecurity/README.md) | 4 | 4 | 2021-22 to 2022-23 | 2 |
| [Introduction to Data Communication and Networks](Introduction%20to%20Data%20Communication%20and%20Networks/README.md) | 10 | 10 | 2023-24 to 2025-26 | 2 |
| [Introduction to Data, Signal and Image Analysis](Introduction%20to%20Data%2C%20Signal%20and%20Image%20Analysis/README.md) | 32 | 22 | 2021-22 to 2025-26 | 7 |
| [Introduction to Database Management System](Introduction%20to%20Database%20Management%20System/README.md) | 6 | 6 | 2025-26 | 3 |
| [Introduction to Digital Systems](Introduction%20to%20Digital%20Systems/README.md) | 7 | 7 | 2022-23 to 2024-25 | 1 |
| [Introduction to Electrical and Electronics Engineering](Introduction%20to%20Electrical%20and%20Electronics%20Engineering/README.md) | 26 | 26 | 2022-23 to 2025-26 | 6 |
| [Introduction to Forensic Science](Introduction%20to%20Forensic%20Science/README.md) | 88 | 42 | 2023-24 to 2025-26 | 25 |
| [Introduction to GIS](Introduction%20to%20GIS/README.md) | 51 | 40 | 2022-23 to 2025-26 | 26 |
| [Introduction to Infrastructure Management](Introduction%20to%20Infrastructure%20Management/README.md) | 1 | 1 | 2017-18 | 1 |
| [Introduction to Innovation, IP Management and Entrepreneurship](Introduction%20to%20Innovation%2C%20IP%20Management%20and%20Entrepreneurship/README.md) | 11 | 11 | 2021-22 to 2025-26 | 2 |
| [Introduction to International Business](Introduction%20to%20International%20Business/README.md) | 12 | 9 | 2021-22 to 2025-26 | 3 |
| [Introduction to IoT](Introduction%20to%20IoT/README.md) | 3 | 3 | 2022 to 2022-23 | 2 |
| [Introduction to IT Infrastructure Landscape](Introduction%20to%20IT%20Infrastructure%20Landscape/README.md) | 7 | 7 | 2023-24 to 2024-25 | 2 |
| [Introduction to Linux](Introduction%20to%20Linux/README.md) | 1 | 1 | 2023-24 | 1 |
| [Introduction to Modern Application Development](Introduction%20to%20Modern%20Application%20Development/README.md) | 15 | 10 | 2022-23 to 2025-26 | 3 |
| [Introduction to Network Security](Introduction%20to%20Network%20Security/README.md) | 4 | 4 | 2022 to 2022-23 | 1 |
| [Introduction to Operating Systems](Introduction%20to%20Operating%20Systems/README.md) | 9 | 9 | 2025-26 | 4 |
| [Introduction to Optimization Techniques](Introduction%20to%20Optimization%20Techniques/README.md) | 2 | 2 | 2025-26 | 1 |
| [Introduction to Philosophy](Introduction%20to%20Philosophy/README.md) | 12 | 7 | 2023-24 to 2024-25 | 2 |
| [Introduction to Real Estate Sector](Introduction%20to%20Real%20Estate%20Sector/README.md) | 4 | 4 | 2016-17 to 2018-19 | 1 |
| [Introduction to Soft Computing Techniques](Introduction%20to%20Soft%20Computing%20Techniques/README.md) | 12 | 12 | 2023-24 to 2025-26 | 2 |
| [Introduction to Software Development](Introduction%20to%20Software%20Development/README.md) | 2 | 2 | 2025-26 | 1 |
| [Introduction to Statistical Learning for Data Science](Introduction%20to%20Statistical%20Learning%20for%20Data%20Science/README.md) | 2 | 2 | 2025-26 | 1 |
| [Introduction to Virtual Reality and Augmented Reality](Introduction%20to%20Virtual%20Reality%20and%20Augmented%20Reality/README.md) | 83 | 68 | 2022-23 to 2025-26 | 28 |
| [Introduction to VLSI Technology](Introduction%20to%20VLSI%20Technology/README.md) | 5 | 5 | 2025-26 | 2 |
| [Introductory Psychology](Introductory%20Psychology/README.md) | 8 | 8 | 2022-23 to 2024-25 | 2 |
| [Investment Analysis](Investment%20Analysis/README.md) | 3 | 3 | 2024-25 to 2025-26 | 2 |
| [Investment Banking](Investment%20Banking/README.md) | 32 | 31 | 2010-11 to 2025-26 | 7 |
| [Investment Banking and Financial Services](Investment%20Banking%20and%20Financial%20Services/README.md) | 10 | 10 | 2015-16 to 2024-25 | 1 |
| [IoT and Applications](IoT%20and%20Applications/README.md) | 20 | 11 | 2023-24 to 2025-26 | 10 |
| [IoT for Smart Cities](IoT%20for%20Smart%20Cities/README.md) | 1 | 1 | 2023-24 | 1 |
| [IoT Security](IoT%20Security/README.md) | 5 | 5 | 2023-24 to 2025-26 | 3 |
| [IoT System Architecture](IoT%20System%20Architecture/README.md) | 3 | 3 | 2022 to 2023-24 | 1 |
| [IP Traffic Engineering](IP%20Traffic%20Engineering/README.md) | 2 | 2 | 2010-11 to 2012-13 | 1 |
| [Irrigation Engineering](Irrigation%20Engineering/README.md) | 31 | 28 | 2013-14 to 2021-22 | 3 |
| [IT Project Management](IT%20Project%20Management/README.md) | 8 | 8 | 2023-24 to 2025-26 | 2 |
| [IT Workshop](IT%20Workshop/README.md) | 2 | 2 | 2023-24 to 2024-25 | 1 |
| [Japanese A1](Japanese%20A1/README.md) | 13 | 13 | 2025-26 | 5 |
| [Java and Web Technologies](Java%20and%20Web%20Technologies/README.md) | 6 | 5 | 2008-09 to 2012-13 | 1 |
| [Java Programming](Java%20Programming/README.md) | 17 | 17 | 2021-22 to 2025-26 | 3 |
| [Journalism and Mass Media](Journalism%20and%20Mass%20Media/README.md) | 40 | 11 | 2023-24 to 2025-26 | 15 |
| [Kinematics and Dynamics of Machines](Kinematics%20and%20Dynamics%20of%20Machines/README.md) | 17 | 12 | 2021 to 2025-26 | 4 |
| [Knowledge Management](Knowledge%20Management/README.md) | 9 | 9 | 2008-09 to 2016-17 | 1 |
| [Large Language Models](Large%20Language%20Models/README.md) | 2 | 2 | 2024-25 | 1 |
| [Leadership](Leadership/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Leadership in Organization](Leadership%20in%20Organization/README.md) | 11 | 11 | 2009-10 to 2015-16 | 1 |
| [Leading Through Life Skills](Leading%20Through%20Life%20Skills/README.md) | 103 | 83 | 2022-23 to 2025-26 | 23 |
| [Lean Manufacturing](Lean%20Manufacturing/README.md) | 12 | 6 | 2023-24 to 2025-26 | 5 |
| [Legal Aspects of Business](Legal%20Aspects%20of%20Business/README.md) | 57 | 29 | 2007-08 to 2019-20 | 4 |
| [Legal Aspects of Construction](Legal%20Aspects%20of%20Construction/README.md) | 6 | 6 | 2016-17 to 2019-20 | 1 |
| [Limit State Design of Reinforced Concrete Structures](Limit%20State%20Design%20of%20Reinforced%20Concrete%20Structures/README.md) | 31 | 30 | 2013-14 to 2022 | 3 |
| [Linear Algebra](Linear%20Algebra/README.md) | 10 | 10 | 2021-22 to 2024-25 | 2 |
| [Linear Algebra and Differential Equations](Linear%20Algebra%20and%20Differential%20Equations/README.md) | 183 | 154 | 2021-22 to 2025-26 | 28 |
| [Linear Integrated Circuits and Applications](Linear%20Integrated%20Circuits%20and%20Applications/README.md) | 11 | 10 | 2015-16 to 2019-20 | 1 |
| [Linux and Secure OS for Business](Linux%20and%20Secure%20OS%20for%20Business/README.md) | 10 | 9 | 2023-24 to 2025-26 | 4 |
| [Logic Design and Computer Organization](Logic%20Design%20and%20Computer%20Organization/README.md) | 4 | 4 | 2023-24 to 2024-25 | 2 |
| [Logistics and Supply Chain Management](Logistics%20and%20Supply%20Chain%20Management/README.md) | 31 | 27 | 2007-08 to 2025-26 | 11 |
| [Machine Drawing](Machine%20Drawing/README.md) | 7 | 3 | 2023-24 to 2024-25 | 2 |
| [Machine Learning](Machine%20Learning/README.md) | 136 | 110 | 2017-18 to 2025-26 | 31 |
| [Machine Learning Algorithms](Machine%20Learning%20Algorithms/README.md) | 19 | 14 | 2022-23 to 2025-26 | 6 |
| [Machine Learning and Data Mining](Machine%20Learning%20and%20Data%20Mining/README.md) | 6 | 6 | 2015-16 to 2023-24 | 1 |
| [Machine Learning Optimization Algorithms](Machine%20Learning%20Optimization%20Algorithms/README.md) | 4 | 4 | 2022-23 to 2023-24 | 1 |
| [Macroeconomics](Macroeconomics/README.md) | 25 | 23 | 2016-17 to 2025-26 | 6 |
| [Maintenance Engineering and Management](Maintenance%20Engineering%20and%20Management/README.md) | 9 | 7 | 2007-08 to 2012-13 | 1 |
| [Management Accounting for Engineers](Management%20Accounting%20for%20Engineers/README.md) | 217 | 110 | 2021-22 to 2025-26 | 47 |
| [Management Control System](Management%20Control%20System/README.md) | 4 | 4 | 2008-09 to 2011-12 | 1 |
| [Management Information System](Management%20Information%20System/README.md) | 34 | 27 | 2006-07 to 2025-26 | 7 |
| [Management of Commercial Banks](Management%20of%20Commercial%20Banks/README.md) | 11 | 10 | 2008-09 to 2014-15 | 1 |
| [Management of Innovation](Management%20of%20Innovation/README.md) | 33 | 14 | 2008-09 to 2014-15 | 4 |
| [Management of Mergers and Acquisitions](Management%20of%20Mergers%20and%20Acquisitions/README.md) | 15 | 15 | 2008-09 to 2019-20 | 1 |
| [Management of Real Estate Business](Management%20of%20Real%20Estate%20Business/README.md) | 1 | 1 | 2017-18 | 1 |
| [Management of Technology](Management%20of%20Technology/README.md) | 40 | 18 | 2007-08 to 2018-19 | 4 |
| [Management of Technology Acquisition and Transfer](Management%20of%20Technology%20Acquisition%20and%20Transfer/README.md) | 10 | 10 | 2008-09 to 2014-15 | 1 |
| [Management of Technology and Emerging Trends](Management%20of%20Technology%20and%20Emerging%20Trends/README.md) | 2 | 2 | 2016-17 | 1 |
| [Management of Technology and Innovation](Management%20of%20Technology%20and%20Innovation/README.md) | 29 | 21 | 2015-16 to 2025-26 | 7 |
| [Management Through Movies](Management%20Through%20Movies/README.md) | 149 | 95 | 2021-22 to 2025-26 | 36 |
| [Managerial Communication](Managerial%20Communication/README.md) | 2 | 2 | 2008-09 to 2009-10 | 1 |
| [Managerial Economics](Managerial%20Economics/README.md) | 2 | 2 | 2018-19 | 1 |
| [Managing Cloud Computing](Managing%20Cloud%20Computing/README.md) | 5 | 5 | 2015-16 to 2017-18 | 1 |
| [Managing Uncertainty](Managing%20Uncertainty/README.md) | 35 | 17 | 2017-18 to 2025-26 | 7 |
| [Manufacturing Management](Manufacturing%20Management/README.md) | 15 | 13 | 2013-14 to 2018-19 | 2 |
| [Manufacturing Processes](Manufacturing%20Processes/README.md) | 27 | 27 | 2014-15 to 2025-26 | 3 |
| [Manufacturing Processes I](Manufacturing%20Processes%20I/README.md) | 74 | 56 | 2011-12 to 2025-26 | 5 |
| [Manufacturing Processes II](Manufacturing%20Processes%20II/README.md) | 51 | 45 | 2011-12 to 2025-26 | 5 |
| [Marine Structures](Marine%20Structures/README.md) | 3 | 2 | 2022-23 to 2024-25 | 3 |
| [Marketing Analytics](Marketing%20Analytics/README.md) | 2 | 2 | 2015-16 to 2018-19 | 2 |
| [Marketing Analytics for Strategic Decision](Marketing%20Analytics%20for%20Strategic%20Decision/README.md) | 1 | 1 | 2018-19 | 1 |
| [Marketing Management](Marketing%20Management/README.md) | 83 | 65 | 2008-09 to 2025-26 | 16 |
| [Marketing Management and Marketing Research](Marketing%20Management%20and%20Marketing%20Research/README.md) | 1 | 1 | 2022-23 | 1 |
| [Marketing of Technology Products](Marketing%20of%20Technology%20Products/README.md) | 21 | 21 | 2008-09 to 2024-25 | 5 |
| [Marketing Research](Marketing%20Research/README.md) | 4 | 2 | 2007-08 | 2 |
| [Marketing Research and Marketing Management](Marketing%20Research%20and%20Marketing%20Management/README.md) | 1 | 1 | 2022-23 | 1 |
| [Marketing Strategy](Marketing%20Strategy/README.md) | 36 | 36 | 2013-14 to 2025-26 | 8 |
| [Marketing Strategy and Analytics](Marketing%20Strategy%20and%20Analytics/README.md) | 13 | 11 | 2022-23 to 2025-26 | 5 |
| [Mass Transfer Operations I](Mass%20Transfer%20Operations%20I/README.md) | 26 | 25 | 2005-06 to 2018-19 | 1 |
| [Mass Transfer Operations II](Mass%20Transfer%20Operations%20II/README.md) | 27 | 25 | 2006-07 to 2022-23 | 1 |
| [Material and Energy Balance Computation](Material%20and%20Energy%20Balance%20Computation/README.md) | 1 | 1 | 2019-20 | 1 |
| [Material and Structure](Material%20and%20Structure/README.md) | 1 | 1 | 2011-12 | 1 |
| [Material Management](Material%20Management/README.md) | 4 | 4 | 2016-17 to 2018-19 | 1 |
| [Material of Construction](Material%20of%20Construction/README.md) | 4 | 4 | 2011-12 to 2012-13 | 1 |
| [Material Sciences](Material%20Sciences/README.md) | 20 | 19 | 2005-06 to 2012-13 | 1 |
| [Material Selection](Material%20Selection/README.md) | 12 | 12 | 2013-14 to 2018-19 | 1 |
| [Materials Engineering](Materials%20Engineering/README.md) | 70 | 54 | 2011-12 to 2025-26 | 5 |
| [Materials Engineering and Metallurgy](Materials%20Engineering%20and%20Metallurgy/README.md) | 2 | 2 | 2025-26 | 1 |
| [Mathematics I](Mathematics%20I/README.md) | 60 | 54 | 2014-15 to 2025-26 | 7 |
| [Mathematics II](Mathematics%20II/README.md) | 58 | 54 | 2014-15 to 2025-26 | 6 |
| [Mathematics III](Mathematics%20III/README.md) | 40 | 29 | 2016-17 to 2025-26 | 13 |
| [Mathematics IV](Mathematics%20IV/README.md) | 27 | 18 | 2022-23 to 2024-25 | 8 |
| [Measurements and Instrumentation](Measurements%20and%20Instrumentation/README.md) | 6 | 6 | 2017-18 | 2 |
| [Mechanical Measurements and Instrumentation](Mechanical%20Measurements%20and%20Instrumentation/README.md) | 2 | 2 | 2021-22 | 1 |
| [Mechanical Measurements and Metrology](Mechanical%20Measurements%20and%20Metrology/README.md) | 46 | 40 | 2013-14 to 2025-26 | 5 |
| [Mechanics of Materials](Mechanics%20of%20Materials/README.md) | 10 | 10 | 2021-22 to 2025-26 | 2 |
| [Mechatronic Systems Design](Mechatronic%20Systems%20Design/README.md) | 9 | 9 | 2014-15 to 2025-26 | 4 |
| [Mechatronics](Mechatronics/README.md) | 9 | 9 | 2011-12 to 2018-19 | 3 |
| [Mechatronics and Controls](Mechatronics%20and%20Controls/README.md) | 30 | 29 | 2013-14 to 2019-20 | 2 |
| [Media Marketing](Media%20Marketing/README.md) | 6 | 6 | 2011-12 to 2014-15 | 1 |
| [Media Planning](Media%20Planning/README.md) | 27 | 27 | 2015-16 to 2025-26 | 7 |
| [Medical Electronics](Medical%20Electronics/README.md) | 5 | 5 | 2013-14 to 2015-16 | 1 |
| [Mergers and Acquisitions](Mergers%20and%20Acquisitions/README.md) | 32 | 24 | 2022-23 to 2025-26 | 9 |
| [Micro and Nano Manufacturing](Micro%20and%20Nano%20Manufacturing/README.md) | 12 | 9 | 2023-24 to 2025-26 | 4 |
| [Microcontroller and Embedded Programming](Microcontroller%20and%20Embedded%20Programming/README.md) | 3 | 3 | 2011-12 | 1 |
| [Microcontrollers](Microcontrollers/README.md) | 5 | 5 | 2013-14 | 2 |
| [Microcontrollers and Embedded Systems](Microcontrollers%20and%20Embedded%20Systems/README.md) | 26 | 22 | 2013-14 to 2018-19 | 4 |
| [Microeconomics](Microeconomics/README.md) | 21 | 21 | 2015-16 to 2025-26 | 5 |
| [Microelectromechanical Systems](Microelectromechanical%20Systems/README.md) | 14 | 14 | 2013-14 to 2025-26 | 3 |
| [Microprocessor](Microprocessor/README.md) | 24 | 11 | 2008-09 to 2012-13 | 3 |
| [Microprocessor and Microcontroller](Microprocessor%20and%20Microcontroller/README.md) | 96 | 79 | 2013-14 to 2025-26 | 13 |
| [Microprocessor Based Systems](Microprocessor%20Based%20Systems/README.md) | 24 | 22 | 2013-14 to 2019-20 | 3 |
| [Microprocessor Systems and Interfacing](Microprocessor%20Systems%20and%20Interfacing/README.md) | 11 | 11 | 2021-22 to 2025-26 | 2 |
| [Microprocessors and Interfacing](Microprocessors%20and%20Interfacing/README.md) | 10 | 10 | 2014-15 to 2018-19 | 1 |
| [Microservices and Architecture](Microservices%20and%20Architecture/README.md) | 34 | 28 | 2023-24 to 2025-26 | 9 |
| [Microservices Software Architecture](Microservices%20Software%20Architecture/README.md) | 1 | 1 | 2022 | 1 |
| [Microwave and Antenna Theory](Microwave%20and%20Antenna%20Theory/README.md) | 22 | 16 | 2021-22 to 2025-26 | 4 |
| [Microwave Integrated Circuits](Microwave%20Integrated%20Circuits/README.md) | 12 | 11 | 2006-07 to 2012-13 | 2 |
| [MLOps](MLOps/README.md) | 11 | 6 | 2023-24 to 2025-26 | 3 |
| [Mobile and Ad Hoc Networks](Mobile%20and%20Ad%20Hoc%20Networks/README.md) | 4 | 3 | 2023-24 | 2 |
| [Mobile Computing](Mobile%20Computing/README.md) | 61 | 56 | 2011-12 to 2024-25 | 10 |
| [Mobile Computing and Wireless Networking](Mobile%20Computing%20and%20Wireless%20Networking/README.md) | 11 | 10 | 2006-07 to 2013-14 | 2 |
| [Mobile Device Security and Forensics](Mobile%20Device%20Security%20and%20Forensics/README.md) | 16 | 12 | 2022-23 to 2025-26 | 6 |
| [Mobile Game Development](Mobile%20Game%20Development/README.md) | 2 | 2 | 2021-22 | 1 |
| [Modelling and Simulation](Modelling%20and%20Simulation/README.md) | 46 | 35 | 2015-16 to 2025-26 | 13 |
| [Modern Construction Equipment and Techniques](Modern%20Construction%20Equipment%20and%20Techniques/README.md) | 6 | 6 | 2022-23 to 2025-26 | 2 |
| [Modern Construction Techniques](Modern%20Construction%20Techniques/README.md) | 4 | 4 | 2015 to 2018-19 | 1 |
| [Modern Control Systems](Modern%20Control%20Systems/README.md) | 4 | 4 | 2022-23 to 2024-25 | 1 |
| [Modern Day Robotics and Its Industrial Applications](Modern%20Day%20Robotics%20and%20Its%20Industrial%20Applications/README.md) | 4 | 4 | 2023-24 to 2025-26 | 1 |
| [Modern Digital Signal Processing](Modern%20Digital%20Signal%20Processing/README.md) | 4 | 4 | 2006-07 to 2009-10 | 1 |
| [Modern Web Applications](Modern%20Web%20Applications/README.md) | 3 | 3 | 2021-22 to 2024-25 | 1 |
| [Multimedia](Multimedia/README.md) | 10 | 10 | 2009-10 to 2012-13 | 1 |
| [Multimedia and Animation](Multimedia%20and%20Animation/README.md) | 9 | 6 | 2023-24 to 2024-25 | 3 |
| [Multimedia and Virtual Reality](Multimedia%20and%20Virtual%20Reality/README.md) | 3 | 3 | 2021 to 2021-22 | 1 |
| [Multimedia Signal Compression](Multimedia%20Signal%20Compression/README.md) | 4 | 4 | 2018-19 to 2019-20 | 2 |
| [Multimedia System and Virtual Reality](Multimedia%20System%20and%20Virtual%20Reality/README.md) | 7 | 7 | 2012-13 to 2018-19 | 2 |
| [Multimedia System Design and Applications](Multimedia%20System%20Design%20and%20Applications/README.md) | 4 | 4 | 2006-07 to 2009-10 | 1 |
| [Multimedia Systems](Multimedia%20Systems/README.md) | 16 | 15 | 2013-14 to 2018-19 | 3 |
| [Multimedia Systems and Communication](Multimedia%20Systems%20and%20Communication/README.md) | 7 | 7 | 2006-07 to 2010-11 | 1 |
| [Nano Technology](Nano%20Technology/README.md) | 2 | 2 | 2018-19 to 2022-23 | 2 |
| [Natural Language Processing](Natural%20Language%20Processing/README.md) | 98 | 52 | 2018-19 to 2025-26 | 29 |
| [Network Design and Planning](Network%20Design%20and%20Planning/README.md) | 16 | 16 | 2013-14 to 2018-19 | 2 |
| [Network Programming](Network%20Programming/README.md) | 1 | 1 | 2009-10 | 1 |
| [Network Security](Network%20Security/README.md) | 14 | 14 | 2022 to 2025-26 | 4 |
| [Networks Analysis and Synthesis](Networks%20Analysis%20and%20Synthesis/README.md) | 7 | 7 | 2016-17 to 2017-18 | 2 |
| [Networks and Telecommunications](Networks%20and%20Telecommunications/README.md) | 12 | 12 | 2022-23 to 2025-26 | 2 |
| [Neural Networks and Deep Learning](Neural%20Networks%20and%20Deep%20Learning/README.md) | 17 | 16 | 2018-19 to 2025-26 | 7 |
| [New Product Development](New%20Product%20Development/README.md) | 13 | 13 | 2008-09 to 2015-16 | 1 |
| [Next Generation Wireless Communications](Next%20Generation%20Wireless%20Communications/README.md) | 7 | 6 | 2023-24 to 2025-26 | 4 |
| [Non Conventional Energy Sources](Non%20Conventional%20Energy%20Sources/README.md) | 8 | 8 | 2013-14 to 2017-18 | 2 |
| [Numerical and Computational Techniques](Numerical%20and%20Computational%20Techniques/README.md) | 11 | 11 | 2007-08 to 2011-12 | 1 |
| [Numerical and Statistical Methods](Numerical%20and%20Statistical%20Methods/README.md) | 12 | 12 | 2012-13 to 2018-19 | 1 |
| [Numerical Methods](Numerical%20Methods/README.md) | 7 | 6 | 2018-19 to 2019-20 | 5 |
| [Numerical Modeling of Groundwater Flow and Transport](Numerical%20Modeling%20of%20Groundwater%20Flow%20and%20Transport/README.md) | 4 | 4 | 2015-16 to 2018-19 | 1 |
| [Numerical Techniques](Numerical%20Techniques/README.md) | 11 | 9 | 2015-16 to 2018-19 | 1 |
| [Nutrition for Health](Nutrition%20for%20Health/README.md) | 84 | 38 | 2023-24 to 2025-26 | 31 |
| [Object Oriented Modeling and Design](Object%20Oriented%20Modeling%20and%20Design/README.md) | 29 | 25 | 2008-09 to 2022-23 | 3 |
| [Object Oriented Programming](Object%20Oriented%20Programming/README.md) | 51 | 39 | 2015-16 to 2025-26 | 17 |
| [Object Oriented Programming and Design](Object%20Oriented%20Programming%20and%20Design/README.md) | 5 | 5 | 2023-24 to 2024-25 | 2 |
| [Object Oriented Programming Through Java](Object%20Oriented%20Programming%20Through%20Java/README.md) | 14 | 6 | 2022-23 to 2024-25 | 4 |
| [Object Oriented Programming using C++](Object%20Oriented%20Programming%20using%20C%2B%2B/README.md) | 27 | 23 | 2007-08 to 2022-23 | 5 |
| [Object Oriented Programming with Java](Object%20Oriented%20Programming%20with%20Java/README.md) | 2 | 1 | 2024-25 | 2 |
| [Object Oriented Software Engineering](Object%20Oriented%20Software%20Engineering/README.md) | 37 | 37 | 2011-12 to 2023-24 | 5 |
| [Online Marketing](Online%20Marketing/README.md) | 8 | 8 | 2013-14 to 2018-19 | 1 |
| [Operating Systems](Operating%20Systems/README.md) | 252 | 176 | 2005-06 to 2025-26 | 36 |
| [Operating Systems and Database Security](Operating%20Systems%20and%20Database%20Security/README.md) | 2 | 2 | 2022-23 to 2023-24 | 1 |
| [Operation and Supply Chain Analytics](Operation%20and%20Supply%20Chain%20Analytics/README.md) | 1 | 1 | 2016-17 | 1 |
| [Operation Planning and Control](Operation%20Planning%20and%20Control/README.md) | 37 | 31 | 2011-12 to 2025-26 | 9 |
| [Operation Research for Chemical Engineers](Operation%20Research%20for%20Chemical%20Engineers/README.md) | 2 | 2 | 2022-23 | 1 |
| [Operations and Supply Chain Management](Operations%20and%20Supply%20Chain%20Management/README.md) | 70 | 48 | 2022-23 to 2025-26 | 21 |
| [Operations Management](Operations%20Management/README.md) | 88 | 55 | 2007-08 to 2025-26 | 11 |
| [Operations Research](Operations%20Research/README.md) | 132 | 100 | 2006-07 to 2025-26 | 19 |
| [Operations Strategy](Operations%20Strategy/README.md) | 25 | 19 | 2010-11 to 2025-26 | 5 |
| [Optical Communication and Networks](Optical%20Communication%20and%20Networks/README.md) | 4 | 4 | 2006-07 to 2009-10 | 1 |
| [Optical Fiber Communication](Optical%20Fiber%20Communication/README.md) | 36 | 35 | 2006-07 to 2022-23 | 6 |
| [Optical Fiber Communication and Network](Optical%20Fiber%20Communication%20and%20Network/README.md) | 7 | 7 | 2011-12 to 2016-17 | 2 |
| [Optimization for Decision Making](Optimization%20for%20Decision%20Making/README.md) | 11 | 5 | 2021-22 to 2022-23 | 2 |
| [Optimization Methods](Optimization%20Methods/README.md) | 40 | 24 | 2022-23 to 2025-26 | 8 |
| [Optimization Techniques](Optimization%20Techniques/README.md) | 29 | 24 | 2021-22 to 2025-26 | 6 |
| [Organic Process Technologies](Organic%20Process%20Technologies/README.md) | 1 | 1 | 2022-23 | 1 |
| [Organisation Design and Development](Organisation%20Design%20and%20Development/README.md) | 2 | 2 | 2016-17 | 1 |
| [Organizational Behaviour](Organizational%20Behaviour/README.md) | 98 | 80 | 2007-08 to 2025-26 | 12 |
| [Parallel Computing](Parallel%20Computing/README.md) | 25 | 22 | 2011-12 to 2018-19 | 4 |
| [Parallel Processing](Parallel%20Processing/README.md) | 15 | 13 | 2006-07 to 2013-14 | 4 |
| [Pattern and Anomaly Detection](Pattern%20and%20Anomaly%20Detection/README.md) | 12 | 2 | 2023-24 | 6 |
| [Pattern Recognition](Pattern%20Recognition/README.md) | 3 | 3 | 2010-11 to 2012-13 | 1 |
| [Pavement Design and Construction](Pavement%20Design%20and%20Construction/README.md) | 21 | 14 | 2013-14 to 2025-26 | 4 |
| [Pavement Management System](Pavement%20Management%20System/README.md) | 5 | 3 | 2021-22 | 2 |
| [Pavement Subgrade and Materials](Pavement%20Subgrade%20and%20Materials/README.md) | 4 | 3 | 2013-14 to 2019-20 | 2 |
| [People Analytics](People%20Analytics/README.md) | 8 | 8 | 2018-19 to 2025-26 | 4 |
| [Petroleum Refining Technology](Petroleum%20Refining%20Technology/README.md) | 12 | 12 | 2011-12 to 2021-22 | 1 |
| [Physics](Physics/README.md) | 165 | 105 | 2022-23 to 2025-26 | 20 |
| [Physics for Computing Science](Physics%20for%20Computing%20Science/README.md) | 11 | 11 | 2022-23 to 2024-25 | 2 |
| [Physics I](Physics%20I/README.md) | 28 | 28 | 2014-15 to 2023-24 | 1 |
| [Physics II](Physics%20II/README.md) | 29 | 27 | 2014-15 to 2023-24 | 2 |
| [Physics III](Physics%20III/README.md) | 37 | 26 | 2022 to 2024-25 | 9 |
| [Physics IV](Physics%20IV/README.md) | 23 | 16 | 2022-23 to 2024-25 | 9 |
| [Plant Utilities](Plant%20Utilities/README.md) | 13 | 13 | 2013-14 to 2021-22 | 1 |
| [Plant Utilities and Piping](Plant%20Utilities%20and%20Piping/README.md) | 9 | 9 | 2006-07 to 2012-13 | 1 |
| [PLC and Data Acquisition](PLC%20and%20Data%20Acquisition/README.md) | 11 | 10 | 2015-16 to 2021-22 | 1 |
| [PLCs and Instrumentation](PLCs%20and%20Instrumentation/README.md) | 10 | 10 | 2022-23 to 2025-26 | 2 |
| [Portfolio and Asset Management](Portfolio%20and%20Asset%20Management/README.md) | 1 | 1 | 2017-18 | 1 |
| [Power Electronics](Power%20Electronics/README.md) | 17 | 16 | 2013-14 to 2017-18 | 4 |
| [Power Electronics System Design](Power%20Electronics%20System%20Design/README.md) | 23 | 20 | 2011-12 to 2012-13 | 1 |
| [Power System Operation and Control](Power%20System%20Operation%20and%20Control/README.md) | 5 | 4 | 2018-19 to 2019-20 | 2 |
| [Power System Planning and Reliability](Power%20System%20Planning%20and%20Reliability/README.md) | 3 | 3 | 2018-19 | 1 |
| [Power System Stability](Power%20System%20Stability/README.md) | 4 | 2 | 2018-19 | 2 |
| [Predictive Analysis](Predictive%20Analysis/README.md) | 21 | 13 | 2023-24 to 2025-26 | 9 |
| [Predictive Analytics](Predictive%20Analytics/README.md) | 17 | 17 | 2023-24 to 2025-26 | 5 |
| [Presentation and Communication Techniques](Presentation%20and%20Communication%20Techniques/README.md) | 24 | 16 | 2013-14 to 2018-19 | 3 |
| [Prestressed Concrete](Prestressed%20Concrete/README.md) | 6 | 3 | 2022-23 to 2023-24 | 2 |
| [Principles and Practices of Management](Principles%20and%20Practices%20of%20Management/README.md) | 77 | 23 | 2006-07 to 2014-15 | 7 |
| [Principles of Accounting I](Principles%20of%20Accounting%20I/README.md) | 10 | 10 | 2021-22 to 2024-25 | 2 |
| [Principles of Accounting II](Principles%20of%20Accounting%20II/README.md) | 13 | 12 | 2022-23 to 2025-26 | 3 |
| [Principles of Artificial Intelligence](Principles%20of%20Artificial%20Intelligence/README.md) | 27 | 19 | 2021-22 to 2025-26 | 7 |
| [Principles of Chemical Reactions](Principles%20of%20Chemical%20Reactions/README.md) | 2 | 2 | 2017-18 | 1 |
| [Principles of Communication Engineering](Principles%20of%20Communication%20Engineering/README.md) | 55 | 49 | 2010-11 to 2018-19 | 5 |
| [Principles of Communication Systems](Principles%20of%20Communication%20Systems/README.md) | 2 | 2 | 2011-12 | 1 |
| [Principles of Compiler Design](Principles%20of%20Compiler%20Design/README.md) | 2 | 2 | 2015-16 | 1 |
| [Principles of Cryptography](Principles%20of%20Cryptography/README.md) | 2 | 1 | 2023-24 | 2 |
| [Principles of Economics and Management](Principles%20of%20Economics%20and%20Management/README.md) | 232 | 127 | 2013-14 to 2025-26 | 46 |
| [Principles of Economics I](Principles%20of%20Economics%20I/README.md) | 10 | 10 | 2021-22 to 2024-25 | 2 |
| [Principles of Economics II](Principles%20of%20Economics%20II/README.md) | 15 | 15 | 2022-23 to 2025-26 | 3 |
| [Principles of Electrical Engineering](Principles%20of%20Electrical%20Engineering/README.md) | 11 | 10 | 2019-20 to 2024-25 | 2 |
| [Principles of Electronics Engineering](Principles%20of%20Electronics%20Engineering/README.md) | 10 | 9 | 2021-22 to 2024-25 | 2 |
| [Principles of Management](Principles%20of%20Management/README.md) | 36 | 31 | 2007-08 to 2025-26 | 10 |
| [Principles of Valuation in Real Estate](Principles%20of%20Valuation%20in%20Real%20Estate/README.md) | 4 | 4 | 2016-17 to 2018-19 | 1 |
| [Probability and Random Processes](Probability%20and%20Random%20Processes/README.md) | 41 | 37 | 2013-14 to 2018-19 | 2 |
| [Probability and Random Variables](Probability%20and%20Random%20Variables/README.md) | 43 | 28 | 2021-22 to 2024-25 | 6 |
| [Probability and Statistics](Probability%20and%20Statistics/README.md) | 162 | 97 | 2018-19 to 2025-26 | 35 |
| [Probability and Stochastic Processes](Probability%20and%20Stochastic%20Processes/README.md) | 3 | 3 | 2022 to 2022-23 | 1 |
| [Problem Solving and Programming using C](Problem%20Solving%20and%20Programming%20using%20C/README.md) | 4 | 4 | 2012-13 | 1 |
| [Process Calculation II](Process%20Calculation%20II/README.md) | 7 | 7 | 2013-14 to 2018-19 | 1 |
| [Process Calculations](Process%20Calculations/README.md) | 11 | 10 | 2005-06 to 2012-13 | 1 |
| [Process Calculations I](Process%20Calculations%20I/README.md) | 11 | 11 | 2013-14 to 2018-19 | 1 |
| [Process Concept to Commercialization](Process%20Concept%20to%20Commercialization/README.md) | 1 | 1 | 2022-23 | 1 |
| [Process Equipment and Accessories Design](Process%20Equipment%20and%20Accessories%20Design/README.md) | 25 | 25 | 2006-07 to 2021-22 | 1 |
| [Process Optimization and Simulation](Process%20Optimization%20and%20Simulation/README.md) | 7 | 7 | 2013-14 to 2018-19 | 1 |
| [Process Simulation](Process%20Simulation/README.md) | 2 | 2 | 2021-22 | 1 |
| [Product Design and Development](Product%20Design%20and%20Development/README.md) | 43 | 39 | 2010-11 to 2025-26 | 7 |
| [Production Drawing](Production%20Drawing/README.md) | 2 | 1 | 2025-26 | 1 |
| [Production Management](Production%20Management/README.md) | 40 | 18 | 2021-22 to 2025-26 | 19 |
| [Production Technology](Production%20Technology/README.md) | 8 | 8 | 2022 to 2025-26 | 2 |
| [Professional Communication and Soft Skills](Professional%20Communication%20and%20Soft%20Skills/README.md) | 3 | 3 | 2024-25 to 2025-26 | 2 |
| [Professional Ethics and Legal Aspects](Professional%20Ethics%20and%20Legal%20Aspects/README.md) | 4 | 1 | year not stated | 4 |
| [Program Management](Program%20Management/README.md) | 3 | 3 | 2013-14 to 2014-15 | 1 |
| [Programming Concept using C](Programming%20Concept%20using%20C/README.md) | 12 | 12 | 2010-11 to 2012-13 | 1 |
| [Programming for Analytics](Programming%20for%20Analytics/README.md) | 14 | 10 | 2022-23 to 2025-26 | 5 |
| [Programming for Problem Solving](Programming%20for%20Problem%20Solving/README.md) | 158 | 101 | 2018-19 to 2025-26 | 41 |
| [Programming in Java](Programming%20in%20Java/README.md) | 20 | 17 | 2013-14 to 2018-19 | 3 |
| [Project and Process Engineering](Project%20and%20Process%20Engineering/README.md) | 11 | 11 | 2010-11 to 2019-20 | 1 |
| [Project Appraisal and Financing](Project%20Appraisal%20and%20Financing/README.md) | 24 | 24 | 2024-25 to 2025-26 | 7 |
| [Project Closure](Project%20Closure/README.md) | 3 | 3 | 2016-17 to 2018-19 | 1 |
| [Project Configuration and Change Management](Project%20Configuration%20and%20Change%20Management/README.md) | 2 | 2 | 2013-14 to 2014-15 | 1 |
| [Project Contracts and Claims Management](Project%20Contracts%20and%20Claims%20Management/README.md) | 6 | 6 | 2013-14 to 2016-17 | 1 |
| [Project Infrastructure](Project%20Infrastructure/README.md) | 3 | 3 | 2015-16 to 2018-19 | 1 |
| [Project Infrastructure and Finances](Project%20Infrastructure%20and%20Finances/README.md) | 12 | 12 | 2008-09 to 2021-22 | 1 |
| [Project Management](Project%20Management/README.md) | 109 | 83 | 2006-07 to 2025-26 | 14 |
| [Project Portfolio and Program Management](Project%20Portfolio%20and%20Program%20Management/README.md) | 1 | 1 | 2016-17 | 1 |
| [Project Procurement and Planning](Project%20Procurement%20and%20Planning/README.md) | 2 | 2 | 2013-14 | 1 |
| [Project Procurement Management](Project%20Procurement%20Management/README.md) | 11 | 8 | 2015-16 to 2024-25 | 1 |
| [Project Procurement Management, Contract Administration and Claims Management](Project%20Procurement%20Management%2C%20Contract%20Administration%20and%20Claims%20Management/README.md) | 24 | 24 | 2024 to 2025 | 8 |
| [Project Risk and Insurance Management](Project%20Risk%20and%20Insurance%20Management/README.md) | 3 | 3 | 2008-09 | 1 |
| [Project Risk Management](Project%20Risk%20Management/README.md) | 16 | 16 | 2013-14 to 2025-26 | 2 |
| [Property Documentation](Property%20Documentation/README.md) | 5 | 5 | 2015-16 to 2018-19 | 1 |
| [Python for Data Analysis](Python%20for%20Data%20Analysis/README.md) | 8 | 7 | 2022-23 to 2024-25 | 3 |
| [Python Fundamentals](Python%20Fundamentals/README.md) | 3 | 3 | 2023-24 to 2024-25 | 1 |
| [Python Programming](Python%20Programming/README.md) | 24 | 5 | 2022-23 to 2024-25 | 12 |
| [Quality Management](Quality%20Management/README.md) | 4 | 2 | 2022-23 | 2 |
| [Quality Management and Services](Quality%20Management%20and%20Services/README.md) | 12 | 12 | 2007-08 to 2012-13 | 1 |
| [Quality Management in Construction](Quality%20Management%20in%20Construction/README.md) | 2 | 1 | 2022-23 | 2 |
| [Quality Management System and Practices](Quality%20Management%20System%20and%20Practices/README.md) | 26 | 26 | 2007-08 to 2017-18 | 2 |
| [Quantitative Finance](Quantitative%20Finance/README.md) | 15 | 13 | 2022-23 to 2025-26 | 6 |
| [Quantitative Insights into Supply Chain and Operations](Quantitative%20Insights%20into%20Supply%20Chain%20and%20Operations/README.md) | 7 | 7 | 2021-22 to 2023-24 | 2 |
| [Quantitative Techniques](Quantitative%20Techniques/README.md) | 28 | 23 | 2018-19 to 2025-26 | 7 |
| [Quantity Surveying and Estimation](Quantity%20Surveying%20and%20Estimation/README.md) | 7 | 7 | 2016-17 to 2019-20 | 1 |
| [Quantity Surveying and Valuation](Quantity%20Surveying%20and%20Valuation/README.md) | 4 | 4 | 2013-14 to 2014-15 | 1 |
| [Quantity Surveying, Estimation and Valuation](Quantity%20Surveying%2C%20Estimation%20and%20Valuation/README.md) | 35 | 30 | 2015-16 to 2025-26 | 4 |
| [Quantum and Statistical Physics](Quantum%20and%20Statistical%20Physics/README.md) | 53 | 49 | 2021-22 to 2024-25 | 12 |
| [Quantum Computing and Technologies](Quantum%20Computing%20and%20Technologies/README.md) | 40 | 24 | 2023-24 to 2025-26 | 14 |
| [Quantum Physics](Quantum%20Physics/README.md) | 57 | 46 | 2025-26 | 13 |
| [R R Studio SPSS and Tableau Programming](R%20R%20Studio%20SPSS%20and%20Tableau%20Programming/README.md) | 8 | 7 | 2015-16 to 2023-24 | 1 |
| [Radar Engineering](Radar%20Engineering/README.md) | 1 | 1 | 2009-10 | 1 |
| [Radiating Systems and Wave Propagation](Radiating%20Systems%20and%20Wave%20Propagation/README.md) | 8 | 6 | 2017-18 to 2019-20 | 2 |
| [Random Processes and Estimation Techniques](Random%20Processes%20and%20Estimation%20Techniques/README.md) | 48 | 23 | 2022-23 to 2025-26 | 9 |
| [Rapid Prototyping and Tooling](Rapid%20Prototyping%20and%20Tooling/README.md) | 1 | 1 | 2014-15 | 1 |
| [Reaction Kinetics](Reaction%20Kinetics/README.md) | 29 | 29 | 2006-07 to 2021-22 | 1 |
| [Real Estate Investment](Real%20Estate%20Investment/README.md) | 4 | 4 | 2017-18 to 2023-24 | 1 |
| [Real Estate Valuation](Real%20Estate%20Valuation/README.md) | 2 | 2 | 2017-18 to 2018-19 | 1 |
| [Recommendation Systems](Recommendation%20Systems/README.md) | 12 | 10 | 2023-24 to 2025-26 | 3 |
| [Refrigeration and Air Conditioning](Refrigeration%20and%20Air%20Conditioning/README.md) | 26 | 24 | 2013-14 to 2021-22 | 4 |
| [Reinforcement Learning](Reinforcement%20Learning/README.md) | 29 | 19 | 2023-24 to 2025-26 | 11 |
| [Renewable Energy](Renewable%20Energy/README.md) | 4 | 4 | 2017-18 to 2019-20 | 2 |
| [Renewable Energy Sources](Renewable%20Energy%20Sources/README.md) | 90 | 73 | 2018-19 to 2025-26 | 22 |
| [Research Methodology](Research%20Methodology/README.md) | 112 | 62 | 2008-09 to 2025-26 | 27 |
| [Retail Management](Retail%20Management/README.md) | 11 | 10 | 2008-09 to 2013-14 | 1 |
| [Reverse Engineering and Malware Analysis](Reverse%20Engineering%20and%20Malware%20Analysis/README.md) | 13 | 7 | 2022-23 to 2025-26 | 5 |
| [RF Circuit Design](RF%20Circuit%20Design/README.md) | 22 | 20 | 2013-14 to 2018-19 | 3 |
| [Risk and Reliability Engineering](Risk%20and%20Reliability%20Engineering/README.md) | 2 | 2 | 2013-14 | 1 |
| [Risk Management](Risk%20Management/README.md) | 6 | 3 | 2021-22 to 2022-23 | 2 |
| [Robotic Process Automation](Robotic%20Process%20Automation/README.md) | 31 | 18 | 2022-23 to 2024-25 | 7 |
| [Robotic Systems Design](Robotic%20Systems%20Design/README.md) | 7 | 7 | 2021-22 to 2025-26 | 2 |
| [Robotics](Robotics/README.md) | 50 | 46 | 2013-14 to 2025-26 | 13 |
| [Robotics and Automation](Robotics%20and%20Automation/README.md) | 24 | 20 | 2021-22 to 2025-26 | 7 |
| [Robotics Computational Motion Planning](Robotics%20Computational%20Motion%20Planning/README.md) | 1 | 1 | 2023-24 | 1 |
| [Rock Mechanics](Rock%20Mechanics/README.md) | 11 | 9 | 2018-19 to 2025-26 | 4 |
| [Safety, Health Environmental Management System](Safety%2C%20Health%20Environmental%20Management%20System/README.md) | 19 | 11 | 2010-11 to 2014-15 | 6 |
| [Sales and Distribution Management](Sales%20and%20Distribution%20Management/README.md) | 32 | 32 | 2008-09 to 2025-26 | 7 |
| [SAS Programming](SAS%20Programming/README.md) | 2 | 2 | 2015-16 to 2016-17 | 1 |
| [Satellite Communication and Radar](Satellite%20Communication%20and%20Radar/README.md) | 10 | 10 | 2016-17 to 2022-23 | 3 |
| [Science](Science/README.md) | 1 | 1 | 2023-24 | 1 |
| [Science, Technology and Society](Science%2C%20Technology%20and%20Society/README.md) | 10 | 6 | 2021-22 to 2023-24 | 4 |
| [Security Analysis](Security%20Analysis/README.md) | 12 | 12 | 2015-16 to 2024-25 | 1 |
| [Security and Portfolio Management](Security%20and%20Portfolio%20Management/README.md) | 15 | 14 | 2008-09 to 2014-15 | 1 |
| [Security Essentials in Applied AI](Security%20Essentials%20in%20Applied%20AI/README.md) | 6 | 6 | 2024-25 to 2025-26 | 2 |
| [Sensors](Sensors/README.md) | 2 | 2 | 2022 to 2023-24 | 1 |
| [Sensors and Transducers](Sensors%20and%20Transducers/README.md) | 2 | 2 | 2022 to 2023-24 | 1 |
| [Sensors in Manufacturing](Sensors%20in%20Manufacturing/README.md) | 3 | 3 | 2014-15 to 2016-17 | 1 |
| [Sensors in Wearable Technology](Sensors%20in%20Wearable%20Technology/README.md) | 1 | 1 | 2021-22 | 1 |
| [Sentiment, Web and Text Analytics](Sentiment%2C%20Web%20and%20Text%20Analytics/README.md) | 5 | 5 | 2018-19 to 2024-25 | 1 |
| [Service Oriented Architecture](Service%20Oriented%20Architecture/README.md) | 35 | 35 | 2011 to 2019-20 | 4 |
| [Services Marketing](Services%20Marketing/README.md) | 18 | 17 | 2008-09 to 2024-25 | 2 |
| [Services Operations Management](Services%20Operations%20Management/README.md) | 13 | 12 | 2010-11 to 2025-26 | 2 |
| [Services Science and Service Operational Management](Services%20Science%20and%20Service%20Operational%20Management/README.md) | 13 | 12 | 2022-23 to 2025-26 | 2 |
| [Signal and Image Processing](Signal%20and%20Image%20Processing/README.md) | 28 | 20 | 2021-22 to 2025-26 | 6 |
| [Signals and Systems](Signals%20and%20Systems/README.md) | 186 | 127 | 2010-11 to 2025-26 | 19 |
| [Simulated Mixed Reality](Simulated%20Mixed%20Reality/README.md) | 2 | 2 | 2023-24 to 2025-26 | 1 |
| [Simulation Modeling](Simulation%20Modeling/README.md) | 3 | 3 | 2014-15 to 2015-16 | 1 |
| [Smart Antennas](Smart%20Antennas/README.md) | 2 | 2 | 2021-22 | 1 |
| [Smart Cities](Smart%20Cities/README.md) | 75 | 57 | 2023-24 to 2025-26 | 25 |
| [Smart Cities Planning and Technology](Smart%20Cities%20Planning%20and%20Technology/README.md) | 10 | 8 | 2015-16 to 2022-23 | 3 |
| [Smart Grids](Smart%20Grids/README.md) | 4 | 2 | 2018-19 | 2 |
| [Smart Manufacturing and Internet of Things](Smart%20Manufacturing%20and%20Internet%20of%20Things/README.md) | 13 | 10 | 2022 to 2025-26 | 4 |
| [Smart System Communication](Smart%20System%20Communication/README.md) | 5 | 5 | 2023-24 to 2025-26 | 1 |
| [Social Media and Web Analytics](Social%20Media%20and%20Web%20Analytics/README.md) | 10 | 10 | 2025-26 | 5 |
| [Soft Computing](Soft%20Computing/README.md) | 15 | 15 | 2014-15 to 2022-23 | 3 |
| [Software Architecture](Software%20Architecture/README.md) | 21 | 20 | 2006-07 to 2017-18 | 5 |
| [Software Architecture and Project Management](Software%20Architecture%20and%20Project%20Management/README.md) | 4 | 3 | 2006-07 to 2009-10 | 1 |
| [Software Design with UML](Software%20Design%20with%20UML/README.md) | 8 | 8 | 2021-22 to 2025-26 | 2 |
| [Software Engineering](Software%20Engineering/README.md) | 180 | 127 | 2005-06 to 2025-26 | 24 |
| [Software Engineering I](Software%20Engineering%20I/README.md) | 10 | 6 | 2005-06 to 2008-09 | 2 |
| [Software Engineering Methodology](Software%20Engineering%20Methodology/README.md) | 13 | 13 | 2007-08 to 2011-12 | 2 |
| [Software Project Management](Software%20Project%20Management/README.md) | 20 | 17 | 2013-14 to 2023-24 | 5 |
| [Software Quality Assurance](Software%20Quality%20Assurance/README.md) | 39 | 32 | 2011-12 to 2025-26 | 11 |
| [Software Quality Assurance and Testing](Software%20Quality%20Assurance%20and%20Testing/README.md) | 20 | 18 | 2012-13 to 2022-23 | 4 |
| [Software Security](Software%20Security/README.md) | 1 | 1 | 2023-24 | 1 |
| [Software Technology](Software%20Technology/README.md) | 1 | 1 | 2023-24 | 1 |
| [Software Testing](Software%20Testing/README.md) | 17 | 15 | 2007-08 to 2025-26 | 4 |
| [Soil Dynamics](Soil%20Dynamics/README.md) | 5 | 5 | 2018-19 to 2019-20 | 2 |
| [Soil Mechanics](Soil%20Mechanics/README.md) | 15 | 12 | 2021-22 to 2025-26 | 3 |
| [Solid Fluid Mechanical Operations](Solid%20Fluid%20Mechanical%20Operations/README.md) | 26 | 26 | 2005-06 to 2021-22 | 1 |
| [Solid Mechanics](Solid%20Mechanics/README.md) | 12 | 12 | 2021-22 to 2025-26 | 3 |
| [Speech and Natural Language Processing](Speech%20and%20Natural%20Language%20Processing/README.md) | 15 | 7 | 2023-24 to 2025-26 | 5 |
| [Speech Processing](Speech%20Processing/README.md) | 8 | 8 | 2009-10 to 2021-22 | 1 |
| [Speech Recognition](Speech%20Recognition/README.md) | 4 | 4 | 2018-19 to 2024-25 | 2 |
| [Statistical Learning](Statistical%20Learning/README.md) | 5 | 5 | 2018-19 to 2023-24 | 1 |
| [Statistical Method I](Statistical%20Method%20I/README.md) | 2 | 2 | 2021-22 to 2022-23 | 1 |
| [Statistical Methods](Statistical%20Methods/README.md) | 138 | 84 | 2006-07 to 2025-26 | 20 |
| [Statistical Methods II](Statistical%20Methods%20II/README.md) | 2 | 1 | 2018-19 | 1 |
| [Statistical Methods of Analysis](Statistical%20Methods%20of%20Analysis/README.md) | 12 | 9 | 2013-14 to 2022-23 | 3 |
| [Statistical Signal Analysis](Statistical%20Signal%20Analysis/README.md) | 5 | 5 | 2013-14 to 2015-16 | 1 |
| [Statistical Structures in Data and Inference](Statistical%20Structures%20in%20Data%20and%20Inference/README.md) | 26 | 16 | 2021-22 to 2025-26 | 6 |
| [Statistics and Numerical Methods](Statistics%20and%20Numerical%20Methods/README.md) | 2 | 2 | 2021-22 | 1 |
| [Statistics, Probability and Calculus](Statistics%2C%20Probability%20and%20Calculus/README.md) | 14 | 11 | 2021-22 to 2024-25 | 2 |
| [Stochastic Processes](Stochastic%20Processes/README.md) | 11 | 8 | 2023-24 to 2025-26 | 3 |
| [Stochastic Processes and Applications](Stochastic%20Processes%20and%20Applications/README.md) | 29 | 22 | 2021-22 to 2025-26 | 6 |
| [Strategic Management](Strategic%20Management/README.md) | 77 | 59 | 2008-09 to 2025-26 | 11 |
| [Strength of Materials](Strength%20of%20Materials/README.md) | 157 | 135 | 2005-06 to 2025-26 | 12 |
| [Strength of Materials and Fabrication](Strength%20of%20Materials%20and%20Fabrication/README.md) | 11 | 11 | 2012-13 to 2017-18 | 1 |
| [Structural Analysis I](Structural%20Analysis%20I/README.md) | 43 | 37 | 2013-14 to 2018-19 | 3 |
| [Structural Analysis II](Structural%20Analysis%20II/README.md) | 34 | 31 | 2014-15 to 2019-20 | 2 |
| [Structural Dynamics](Structural%20Dynamics/README.md) | 6 | 6 | 2016-17 to 2018-19 | 2 |
| [Structured System Analysis and Design](Structured%20System%20Analysis%20and%20Design/README.md) | 23 | 22 | 2007-08 to 2016-17 | 2 |
| [Structures Analysis and Design](Structures%20Analysis%20and%20Design/README.md) | 2 | 2 | 2012-13 | 1 |
| [Supervisory Control and Data Acquisition](Supervisory%20Control%20and%20Data%20Acquisition/README.md) | 43 | 32 | 2022 to 2025-26 | 10 |
| [Supplier Management](Supplier%20Management/README.md) | 6 | 6 | 2011-12 to 2014-15 | 1 |
| [Supply Chain Analytics](Supply%20Chain%20Analytics/README.md) | 27 | 20 | 2021-22 to 2025-26 | 7 |
| [Supply Chain and Logistics Management](Supply%20Chain%20and%20Logistics%20Management/README.md) | 19 | 19 | 2016-17 to 2024-25 | 6 |
| [Supply Chain Management](Supply%20Chain%20Management/README.md) | 54 | 24 | 2008-09 to 2025-26 | 6 |
| [Surveying](Surveying/README.md) | 17 | 15 | 2011-12 to 2025-26 | 4 |
| [Surveying I](Surveying%20I/README.md) | 41 | 38 | 2013-14 to 2023-24 | 3 |
| [Surveying II](Surveying%20II/README.md) | 33 | 28 | 2013-14 to 2019-20 | 3 |
| [Sustainable Business Management Practices](Sustainable%20Business%20Management%20Practices/README.md) | 39 | 39 | 2016-17 to 2025-26 | 8 |
| [Sustainable Development](Sustainable%20Development/README.md) | 5 | 5 | 2016-17 to 2018-19 | 1 |
| [Sustainable Energy Technologies](Sustainable%20Energy%20Technologies/README.md) | 100 | 53 | 2021-22 to 2025-26 | 27 |
| [Switchgear and Protection](Switchgear%20and%20Protection/README.md) | 5 | 4 | 2017-18 to 2018-19 | 2 |
| [System and Network Security](System%20and%20Network%20Security/README.md) | 11 | 11 | 2010-11 to 2016-17 | 2 |
| [System Approach to Organization Design](System%20Approach%20to%20Organization%20Design/README.md) | 4 | 4 | 2013-14 to 2014-15 | 1 |
| [System Programming](System%20Programming/README.md) | 28 | 26 | 2013-14 to 2021-22 | 2 |
| [System Security](System%20Security/README.md) | 26 | 26 | 2011-12 to 2022-23 | 3 |
| [Systems Analysis and Design](Systems%20Analysis%20and%20Design/README.md) | 18 | 18 | 2008-09 to 2025-26 | 5 |
| [Systems Architecture and Programming](Systems%20Architecture%20and%20Programming/README.md) | 6 | 5 | 2005-06 to 2010-11 | 1 |
| [Technical Communication and Leadership Skills](Technical%20Communication%20and%20Leadership%20Skills/README.md) | 6 | 6 | 2024-25 to 2025-26 | 3 |
| [Technical Writing](Technical%20Writing/README.md) | 48 | 18 | 2022 to 2025-26 | 19 |
| [Technology and Innovation for Marketing](Technology%20and%20Innovation%20for%20Marketing/README.md) | 22 | 15 | 2022-23 to 2025-26 | 7 |
| [Technology Forecasting Assessment and Evaluation](Technology%20Forecasting%20Assessment%20and%20Evaluation/README.md) | 8 | 8 | 2008-09 to 2014-15 | 1 |
| [Technology Management](Technology%20Management/README.md) | 1 | 1 | 2018-19 | 1 |
| [Telecom and Computer Networks](Telecom%20and%20Computer%20Networks/README.md) | 7 | 7 | 2006-07 to 2009-10 | 1 |
| [Telecom Network Management](Telecom%20Network%20Management/README.md) | 3 | 3 | 2006-07 to 2012-13 | 1 |
| [Testing Commissioning](Testing%20Commissioning/README.md) | 3 | 3 | 2018-19 to 2019-20 | 1 |
| [Testing Commissioning and Maintenance](Testing%20Commissioning%20and%20Maintenance/README.md) | 1 | 1 | 2019-20 | 1 |
| [Testing Commissioning and Maintenance of Electrical Equipment](Testing%20Commissioning%20and%20Maintenance%20of%20Electrical%20Equipment/README.md) | 1 | 1 | 2018-19 | 1 |
| [Theoretical Computer Science](Theoretical%20Computer%20Science/README.md) | 73 | 58 | 2013-14 to 2025-26 | 9 |
| [Theory of Machines](Theory%20of%20Machines/README.md) | 2 | 2 | 2025-26 | 1 |
| [Theory of Machines and Mechanisms](Theory%20of%20Machines%20and%20Mechanisms/README.md) | 15 | 15 | 2022 to 2025-26 | 3 |
| [Theory of Machines I](Theory%20of%20Machines%20I/README.md) | 49 | 45 | 2011-12 to 2018-19 | 3 |
| [Theory of Machines II](Theory%20of%20Machines%20II/README.md) | 43 | 40 | 2011-12 to 2022-23 | 4 |
| [Theory of Machines III](Theory%20of%20Machines%20III/README.md) | 4 | 4 | 2017-18 to 2019-20 | 1 |
| [Theory of Reinforced Concrete and Prestressed Concrete](Theory%20of%20Reinforced%20Concrete%20and%20Prestressed%20Concrete/README.md) | 34 | 32 | 2014-15 to 2019-20 | 3 |
| [Theory of Structures](Theory%20of%20Structures/README.md) | 25 | 20 | 2013-14 to 2025-26 | 4 |
| [Thermal Engineering](Thermal%20Engineering/README.md) | 35 | 35 | 2011-12 to 2019-20 | 2 |
| [Thermodynamics](Thermodynamics/README.md) | 11 | 9 | 2022-23 to 2025-26 | 2 |
| [Thermodynamics and Heat Transfer](Thermodynamics%20and%20Heat%20Transfer/README.md) | 17 | 14 | 2014-15 to 2022-23 | 1 |
| [Total Quality Management](Total%20Quality%20Management/README.md) | 29 | 28 | 2013-14 to 2025-26 | 6 |
| [Total Quality Management-Department Elective IV](Total%20Quality%20Management-Department%20Elective%20IV/README.md) | 2 | 2 | 2022-23 to 2023-24 | 1 |
| [TQM and MIS in Construction](TQM%20and%20MIS%20in%20Construction/README.md) | 2 | 1 | 2021-22 | 2 |
| [Traffic Analysis and Design](Traffic%20Analysis%20and%20Design/README.md) | 11 | 8 | 2015-16 to 2022-23 | 3 |
| [Transform and Series](Transform%20and%20Series/README.md) | 7 | 4 | 2021-22 to 2022-23 | 2 |
| [Transportation Engineering](Transportation%20Engineering/README.md) | 31 | 30 | 2013-14 to 2025-26 | 3 |
| [Transportation Engineering I](Transportation%20Engineering%20I/README.md) | 3 | 3 | 2017-18 to 2019-20 | 1 |
| [Transportation Engineering II](Transportation%20Engineering%20II/README.md) | 7 | 7 | 2017-18 to 2023-24 | 1 |
| [Tribology](Tribology/README.md) | 1 | 1 | year not stated | 1 |
| [TV and Video Engineering](TV%20and%20Video%20Engineering/README.md) | 15 | 14 | 2011-12 to 2017-18 | 3 |
| [UI and UX Design](UI%20and%20UX%20Design/README.md) | 16 | 9 | 2022-23 to 2025-26 | 6 |
| [Unit Processing in Chemical Industries](Unit%20Processing%20in%20Chemical%20Industries/README.md) | 20 | 20 | 2010-11 to 2018-19 | 1 |
| [Universal Human Values II](Universal%20Human%20Values%20II/README.md) | 67 | 34 | 2024-25 to 2025-26 | 25 |
| [Unix Programming](Unix%20Programming/README.md) | 19 | 17 | 2013-14 to 2021-22 | 4 |
| [Unmanned Aerial Vehicles](Unmanned%20Aerial%20Vehicles/README.md) | 9 | 8 | 2023-24 to 2025-26 | 4 |
| [Unsorted Papers](Unsorted%20Papers/README.md) | 1 | 1 | year not stated | 1 |
| [Urban and Infrastructure Development](Urban%20and%20Infrastructure%20Development/README.md) | 1 | 1 | 2013-14 | 1 |
| [Urban Development](Urban%20Development/README.md) | 7 | 7 | 2015 to 2018-19 | 1 |
| [Urban Infrastructure Planning](Urban%20Infrastructure%20Planning/README.md) | 3 | 1 | 2022-23 | 2 |
| [Urban Transportation Systems Planning](Urban%20Transportation%20Systems%20Planning/README.md) | 1 | 1 | 2018-19 | 1 |
| [Usability Design of Software Applications](Usability%20Design%20of%20Software%20Applications/README.md) | 4 | 4 | 2025-26 | 1 |
| [Value Engineering](Value%20Engineering/README.md) | 4 | 4 | 2006-07 to 2009-10 | 1 |
| [Value Management](Value%20Management/README.md) | 1 | 1 | 2018-19 | 1 |
| [Vibration Engineering](Vibration%20Engineering/README.md) | 50 | 47 | 2013-14 to 2025-26 | 5 |
| [Virtual Design and Manufacturing](Virtual%20Design%20and%20Manufacturing/README.md) | 1 | 1 | 2024-25 | 1 |
| [Virtual Instrumentation](Virtual%20Instrumentation/README.md) | 2 | 2 | 2017-18 to 2022-23 | 1 |
| [Virtual Reality and Augmented Reality](Virtual%20Reality%20and%20Augmented%20Reality/README.md) | 8 | 7 | 2022-23 to 2025-26 | 1 |
| [Virtualization and Cloud Computing](Virtualization%20and%20Cloud%20Computing/README.md) | 20 | 15 | 2022-23 to 2025-26 | 4 |
| [Visual Analytics](Visual%20Analytics/README.md) | 2 | 2 | 2023-24 | 1 |
| [VLSI Design](VLSI%20Design/README.md) | 14 | 11 | 2007-08 to 2012-13 | 2 |
| [VLSI Design and Technology](VLSI%20Design%20and%20Technology/README.md) | 13 | 13 | 2013-14 to 2016-17 | 3 |
| [Vulnerability Assessment and Penetration Testing](Vulnerability%20Assessment%20and%20Penetration%20Testing/README.md) | 3 | 3 | 2023-24 to 2024-25 | 1 |
| [Waste Management](Waste%20Management/README.md) | 47 | 18 | 2022-23 to 2025-26 | 13 |
| [Water and Wastewater Engineering](Water%20and%20Wastewater%20Engineering/README.md) | 10 | 10 | 2018-19 to 2025-26 | 3 |
| [Water Conveyance and Distribution Systems](Water%20Conveyance%20and%20Distribution%20Systems/README.md) | 7 | 6 | 2023-24 to 2025-26 | 3 |
| [Water Distribution System](Water%20Distribution%20System/README.md) | 5 | 5 | 2015-16 to 2019-20 | 1 |
| [Water Resources and Management](Water%20Resources%20and%20Management/README.md) | 2 | 2 | 2011-12 | 1 |
| [Web Architecture and Design](Web%20Architecture%20and%20Design/README.md) | 1 | 1 | 2012-13 | 1 |
| [Web Programming](Web%20Programming/README.md) | 28 | 11 | 2022-23 to 2024-25 | 10 |
| [Web Programming I](Web%20Programming%20I/README.md) | 11 | 11 | 2013-14 to 2019-20 | 1 |
| [Web Programming II](Web%20Programming%20II/README.md) | 8 | 8 | 2013-14 to 2018-19 | 1 |
| [Web Technologies](Web%20Technologies/README.md) | 5 | 3 | 2023-24 to 2024-25 | 1 |
| [Web Technology and Application](Web%20Technology%20and%20Application/README.md) | 4 | 4 | 2011-12 | 1 |
| [Wind Turbine Technology](Wind%20Turbine%20Technology/README.md) | 6 | 5 | 2025-26 | 4 |
| [Wireless and Mobile Communication System](Wireless%20and%20Mobile%20Communication%20System/README.md) | 5 | 5 | 2006-07 to 2010-11 | 1 |
| [Wireless Communication](Wireless%20Communication/README.md) | 22 | 20 | 2010-11 to 2024-25 | 6 |
| [Wireless Communication and Networks](Wireless%20Communication%20and%20Networks/README.md) | 6 | 6 | 2013-14 to 2016-17 | 1 |
| [Wireless Communication I](Wireless%20Communication%20I/README.md) | 12 | 12 | 2006-07 to 2012-13 | 1 |
| [Wireless Communication II](Wireless%20Communication%20II/README.md) | 4 | 3 | 2010-11 to 2011-12 | 2 |
| [Wireless Communication Systems](Wireless%20Communication%20Systems/README.md) | 4 | 4 | 2010-11 to 2012-13 | 1 |
| [Wireless Communication Technology](Wireless%20Communication%20Technology/README.md) | 45 | 42 | 2013-14 to 2025-26 | 5 |
| [Wireless Networking](Wireless%20Networking/README.md) | 23 | 22 | 2013-14 to 2019-20 | 2 |
| [Wireless Security](Wireless%20Security/README.md) | 2 | 1 | 2023-24 | 2 |
| [Wireless Technology](Wireless%20Technology/README.md) | 8 | 8 | 2009-10 to 2012-13 | 1 |
| [Work Study and Ergonomics](Work%20Study%20and%20Ergonomics/README.md) | 4 | 4 | 2005-06 to 2008-09 | 1 |
| [World Class Manufacturing](World%20Class%20Manufacturing/README.md) | 3 | 3 | 2011-12 to 2012-13 | 1 |
| [World Class Manufacturing Practices](World%20Class%20Manufacturing%20Practices/README.md) | 2 | 2 | 2015-16 to 2016-17 | 1 |
