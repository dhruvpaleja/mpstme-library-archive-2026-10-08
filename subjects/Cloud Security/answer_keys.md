# Cloud Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 6cc53a684759

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CyberSecurity_7010/Cloud Security/ANS_Cloud Security(702IT0E002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Cloud Security
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures on the right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
Q 1   Answer briefly:
a.   Consideration   CSP   Customer
Of the Cloud/ In
Security of the cloud   Security in the cloud
the Cloud
Auditability of the cloud   Auditability of anything deployed on
Auditability   regions, datacenters,   their virtual private cloud, including the
hardware, and so on.   virtual network and infrastructure.
Of Cloud region, zone,   For identifying single points of failure
Availability   infrastructure, and service   in their deployed workloads and plan
CO - 1;   availability, the   for high availability   [05]
BL- 2
For PaaS and SaaS
Deployments on private Clouds
Governance   Combined
Provide alternatives to   Choose technologies that are largely
Interoperability   proprietary services,   platform and/or cloud agnostic.
Maintenance and
Of PaaS and SaaS services For IaaS (and some PaaS)
Versioning
for cloud’s infrastructure   for designing and architecting their
Performance   performance   cloud deployments
b. The specific malware protection feature that prevents unauthorized programs from
CO - 2;   creating new processes is best described as Process Spawning Control or Child Process   [05]
BL – 2
Prevention.
********** 1 **********
--- page 2 ---
This is a behavioural containment feature found in cloud. It blocks a parent application
(e.g., a script, a document, or a compromised application) from launching other
processes (child processes). This containment breaks a critical step in the cyber-attack
chain.
1. Policy-Based: Security policies are defined to specify which trusted applications are
allowed to create child processes and which are not.
2. Behavioural Monitoring: The security software monitors the system for process
creation attempts (often using APIs like CreateProcess in Windows).
3. Intervention: When an unauthorized application attempts to spawn a new process,
the security solution blocks the action.
c. The functional components of a Root of Trust for Update (RTU) are - Verification
CO -2;   component, Recovery component, Integrity component, Update component. Two points [05]
BL – 2
of each component to be described.
d. The significance of eDiscovery in the cloud can be broken down into four key areas: Legal
Compliance and Risk, Operational Efficiency, Cost Management, and Technical
Governance.
1. Legal Compliance and Risk Mitigation
Failure to manage eDiscovery can lead to severe legal penalties, sanctions, and loss of
cases.
Legal Duty Preserves: Courts mandate a "legal hold" or "litigation hold," requiring
organizations to preserve all relevant ESI the moment litigation is reasonably anticipated.
In the cloud, this data is scattered across emails, chats (Teams, Slack), files (SharePoint,
Drive), and structured databases.
Significance: Cloud eDiscovery tools provide a centralized, defensible way to issue and
manage these holds across all cloud data sources, proving to a court that you have not
CO - 3;   intentionally or negligently destroyed evidence (spoliation).   [05]
BL- 2
Meeting Tight Deadlines: Legal proceedings operate on strict deadlines for producing
evidence. Manually sifting through terabytes of cloud data is impossible.
Significance: Cloud-native eDiscovery tools can automatically index, search, and analyze
massive datasets quickly, allowing legal teams to meet court-imposed deadlines for
production.
Regulatory Adherence: Industries like finance (SEC, FINRA) and healthcare (HIPAA)
have strict data retention and production rules.
Significance: eDiscovery processes ensure that responsive data can be located and
produced in a format that complies with these regulations, while also protecting privileged
or personally identifiable information (PII).
2. Operational Efficiency and Scalability
The cloud's nature demands a modern approach to discovery.
********** 2 **********
--- page 3 ---
Centralized Management: Data is no longer in a single data center. It lives in SaaS
applications, IaaS storage buckets, and PaaS databases.
Significance: Cloud eDiscovery platforms (like Microsoft Purview or Google Vault) act
as a single pane of glass, allowing legal and IT teams to manage discovery across multiple
cloud services from one interface, eliminating the need for separate tools for each data
source.
Massive Scalability: Cloud datasets can be enormous and grow exponentially.
Significance: Cloud eDiscovery leverages the elastic compute power of the cloud itself.
Whether you need to search 10 GB or 10 TB of data, the cloud infrastructure can scale up
instantly to handle the processing load and scale down afterward, a capability
prohibitively expensive with on-premises hardware.
3. Cost Management and Predictability
Reduction in Physical Infrastructure: There is no need to maintain expensive, specialized
on-premises servers and storage just for legal holds and data processing.
Significance: eDiscovery becomes an operational expense (OpEx) rather than a large
capital expenditure (CapEx). Costs are incurred based on usage (data volume, compute
time).
Efficiency = Lower Review Costs: The most significant cost in eDiscovery is attorney
time for document review. Advanced cloud eDiscovery tools use AI, Machine Learning,
and Technology-Assisted Review (TAR) to automatically cull non-relevant data, identify
duplicates, and prioritize the most likely relevant documents.
Significance: This can reduce the dataset for human review by over 80%, leading to
massive savings in legal fees.
4. Technical and Data Governance
Proactive Data Mapping: To perform eDiscovery effectively in the cloud, an organization
must first know what data it has, where it is, and who owns it.
Significance: The need for eDiscovery forces companies to implement robust data
governance and classification policies, which in turn improves overall security and
compliance posture.
The Shared Responsibility Model: In the cloud, the provider is responsible for the
infrastructure's availability and resilience, but the customer is 100% responsible for the
data within it, including its preservation and production for legal purposes.
Significance: eDiscovery tools are the customer's mechanism for fulfilling their side of
the shared responsibility model in a legal context. You cannot blame the cloud provider
for failure to produce evidence.
a. The five essential characteristics of cloud computing, as defined by the National Institute
Q 2
of Standards and Technology (NIST), form the foundation that makes cloud-based [10]
CO - 1;
BL- 4   systems fundamentally different from traditional IT. They are: On-Demand Self-Service,
********** 3 **********
--- page 4 ---
Broad Network Access, Resource Pooling, Rapid Elasticity, and Measured Service.
Together, they act in concert to deliver unparalleled scalability, flexibility, and efficiency.
1. On-Demand Self-Service: Consumers can unilaterally provision computing
capabilities (e.g., server time, network storage) automatically without requiring human
interaction with the service provider.
Enhances Flexibility & Efficiency:
Flexibility: Development and operations teams are empowered to instantly access the
resources they need to experiment, develop, and deploy. This eliminates lengthy
procurement processes, enabling agile methodologies and faster time-to-market.
Efficiency: It removes administrative overhead and delays. A developer doesn't need to
file a ticket and wait for a system administrator to provision a server; they can do it in
minutes via a web console or API.
Example: A developer building a new microservice can instantly spin up a virtual machine
on AWS EC2 or a container cluster on Google Kubernetes Engine to test their code,
without any intervention from the cloud provider's sales or IT team.
2. Broad Network Access: Capabilities are available over the network and accessed
through standard mechanisms that promote use by heterogeneous thin or thick client
platforms (e.g., mobile phones, tablets, laptops, and workstations).
Enhances Flexibility & Efficiency:
Flexibility: This characteristic enables a truly distributed workforce and global user base.
Applications and data can be accessed from anywhere, on any device, supporting modern
work models like BYOD (Bring Your Own Device) and remote work.
Efficiency: It simplifies client-side requirements. Users only need a standard web browser
or a lightweight client app, reducing the cost and complexity of managing dedicated client
hardware and software.
Example: A company uses Salesforce (a SaaS application). Its sales team can access
customer records, update deals, and collaborate from their laptops in the office, their
tablets at home, or their smartphones while traveling, with a consistent experience across
all devices.
3. Resource Pooling: The provider’s computing resources are pooled to serve multiple
consumers using a multi-tenant model, with different physical and virtual resources
dynamically assigned and reassigned according to consumer demand.
Enhances Efficiency & Scalability:
Efficiency: This is the cornerstone of cloud economics. By serving many customers from
the same underlying physical infrastructure, providers achieve massive economies of
scale, which translates into lower costs for consumers. Resources are utilized at a much
higher rate than in underutilized, dedicated on-premise servers.
********** 4 **********
--- page 5 ---
Scalability: The pool of resources acts as a shared "reservoir" from which any tenant can
draw. When one tenant needs to scale, they are effectively borrowing from the unused
capacity of others in the pool.
Example: A web hosting company like WP Engine hosts thousands of separate WordPress
sites for different customers on a shared pool of servers, storage, and network hardware.
The resources for each site are dynamically allocated, ensuring no single server sits idle.
4. Rapid Elasticity: Capabilities can be elastically provisioned and released, in some cases
automatically, to scale rapidly outward and inward commensurate with demand.
Enhances Scalability & Efficiency:
Scalability: This is the most direct enabler of scalability. Systems can automatically
handle spikes in traffic by adding resources (scale-out) and reduce resources during lulls
(scale-in) to maintain performance and availability.
Efficiency: You only pay for what you use. A retail website doesn't need to provision and
pay for enough hardware to handle Black Friday traffic levels year-round. It can scale
elastically for that peak period and then scale down, optimizing costs.
Example: Netflix's streaming service. During peak evening hours, it automatically scales
up its compute resources in AWS to transcode videos and deliver streams to millions of
concurrent users. In the early morning, when demand is low, it scales down, minimizing
costs.
5. Measured Service: Cloud systems automatically control and optimize resource use by
leveraging a metering capability at some level of abstraction appropriate to the type of
service (e.g., storage, processing, bandwidth, active user accounts).
Enhances Efficiency:
Efficiency: This characteristic provides the transparency needed for cost optimization
(FinOps). Organizations can see exactly which departments, projects, or features are
consuming resources and incurring costs, enabling precise chargebacks and showbacks.
It turns IT infrastructure into a utility, much like electricity.
Example: An enterprise uses Microsoft Azure. They receive a detailed bill showing:
Compute Costs: for the number and size of VMs running and their uptime.
Storage Costs: for the gigabytes of data stored in Blob Storage.
Database Costs: for the throughput units (DTUs) consumed by their Azure SQL Database.
This allows them to identify that a development team left a non-production environment
running over the weekend, incurring unnecessary costs, and take corrective action.
The true power lies in how these characteristics interact to create a virtuous cycle:
1. To achieve `Scalability`, a system leverages Rapid Elasticity to grow, which is possible
because of the large Resource Pool available to draw from. This is all initiated via On-
Demand Self-Service (manually or through automation) and delivered via Broad Network
Access.
********** 5 **********
--- page 6 ---
2. To achieve `Flexibility`, a team uses On-Demand Self-Service to choose the right tool
for the job and Broad Network Access to make it available everywhere. They can afford
to experiment because Measured Service ensures they only pay for the experiment's
duration.
3. To achieve `Efficiency`, Resource Pooling drives down the base cost, Rapid Elasticity
ensures you only use what you need, and Measured Service provides the data to
continuously monitor, right-size, and eliminate waste.
b.   In cloud environments, data is both a critical asset and a significant liability. Data deletion
(the secure, permanent eradication of data) and data archiving (the secure, long-term
retention of inactive data) are not mere administrative tasks but fundamental strategic
practices. When executed properly, they form a dual-pronged approach that directly
enhances data security, ensures regulatory compliance, and optimizes costs.
1. Contribution to Data Security
a) Data Deletion: Minimizing the Attack Surface
Every piece of data stored in the cloud is a potential target for exfiltration or ransomware.
By systematically and securely deleting data that is no longer needed, organizations
actively reduce their "attack surface."
Example: A company decommissioning a customer-facing application must ensure that
all associated user databases, log files, and backup snapshots are permanently erased. If
only the application is shut down but the data persists, a future breach could expose this
stale, yet sensitive, information. Secure deletion, often using cryptographic "crypto-
Q 2   shredding" (deleting the encryption keys), renders this data unrecoverable.
CO - 2;   b) Data Archiving: Securing Inactive Data   [10]
BL- 4   Archiving moves inactive data that must be retained from primary, high-traffic storage
(e.g., a production database or hot blob storage) to a more secure, immutable, and access-
controlled archive tier.
Example: A financial institution archives completed transaction records after 90 days. The
archive is configured with Write-Once-Read-Many (WORM) policies to prevent
tampering or deletion, and access is restricted to a small, audited group of compliance
officers. This protects the historical data from being accidentally altered or maliciously
deleted by a broader set of users with access to the primary system.
2. Contribution to Regulatory Compliance
a) Data Deletion: Upholding "Right to be Forgotten" and Data Minimization
Regulations like the GDPR and CCPA grant individuals the "right to erasure."
Furthermore, the principle of "data minimization" mandates that organizations should not
retain personal data indefinitely beyond the purpose for which it was collected.
Example: Upon receiving a valid erasure request from a former customer under GDPR, a
company must have a verifiable procedure to delete that individual's data not only from
********** 6 **********
--- page 7 ---
its primary CRM (like Salesforce) but also from all backups, data warehouses, and
analytics platforms. A failure to do so can result in massive fines.
b) Data Archiving: Fulfilling Data Retention Mandates
Regulations like SEC Rule 17a-4 (for broker-dealers) or HIPAA (for healthcare records)
require data to be retained for a specific number of years in a non-rewritable, non-erasable
format.
Example: A publicly traded company must retain all business emails for seven years for
legal discovery. Instead of keeping them in the primary, expensive Exchange Online
mailbox, they use a feature like Microsoft Purview to automatically move emails older
than one year to an Immutable Archive. This ensures compliance with retention laws and
prevents users from permanently deleting emails that must be kept.
3. Contribution to Cost Efficiency
a) Data Deletion: Eliminating Unnecessary Storage Costs
In the cloud, you pay for storage by the gigabyte per month. Retaining redundant,
obsolete, or trivial (ROT) data incurs a direct and ongoing financial cost with no business
value.
Example: A video streaming service generates petabytes of temporary log files for
debugging. Implementing a data lifecycle policy in cloud storage (e.g., Amazon S3
Lifecycle) to automatically delete these logs after 30 days prevents them from
accumulating indefinitely, resulting in substantial monthly savings.
b) Data Archiving: Leveraging Tiered Storage for Massive Savings
Cloud providers offer tiered storage, where archival tiers (e.g., AWS Glacier, Azure
Archive Storage) are orders of magnitude cheaper than hot or cool storage tiers. The trade-
off is higher retrieval costs and latency, which is acceptable for data that is rarely
accessed.
Example: A media company archives all its raw film footage after a project is completed.
Storing this multi-petabyte dataset on standard hot storage would cost tens of thousands
of dollars per month. By moving it to an archive storage tier, they reduce this cost by ~70-
80%. They accept that if they need the footage for a sequel in two years, it will take several
hours to retrieve, which is a manageable business trade-off for the savings.
Synthesis: The Interplay of Deletion and Archiving
A mature data governance strategy uses deletion and archiving in concert, guided by a
Data Lifecycle Management (DLM) policy. This policy defines the journey of data from
creation to destruction.
Example Workflow for an Employee Record:
1. Active (Hot Storage): Employee is active. Record is in the primary HR database (e.g.,
Workday). High performance and cost.
********** 7 **********
--- page 8 ---
2. Inactive / Archive (Cool/Archive Storage): Employee leaves the company. After 90
days, the record is automatically moved to a secure archive to meet 7-year legal retention
requirements. Costs drop significantly.
3. Deletion (Secure Erasure): Seven years and one day after the employee's departure,
the archived record is automatically and permanently deleted via a configured policy. Cost
drops to zero, and compliance risk is eliminated.
a.   In this scenario, the roles and their corresponding responsibilities for the data deletion
request are as follows:
1. Data Controller: FinServe
The Data Controller is the entity that determines the why (purpose) and the how (means)
of the data processing.
Role Justification: FinServe is the Data Controller because it decides to use client
personal data for "credit scoring." It defines the purpose of the processing and has the
direct relationship with the data subjects (its clients).
Responsibilities in this Case:
Obligation to Respond: FinServe is legally obligated to comply with the client's valid
request for deletion (a "Right to be Forgotten" under regulations like GDPR). The
request is made to FinServe, and FinServe is accountable for its fulfillment.
Instruction: FinServe must formally instruct its Data Processor (CloudCorp) to delete all
instances of the client's data. This instruction should be part of a legally binding data
processing agreement (DPA).
Q 3   Verification: FinServe is responsible for verifying that CloudCorp has successfully and
[10]
CO - 3;   completely deleted the data. This may involve requesting and reviewing a certificate of
BL- 3
deletion or conducting an audit.
2. Data Processor: CloudCorp
The Data Processor is the entity that processes personal data on behalf of the Data
Controller, following the Controller's instructions.
Role Justification: CloudCorp is the Data Processor because it is providing a "cloud
service to analyze" the data. It is acting under the instructions of FinServe and has no
independent purpose for processing the client data.
Responsibilities in this Case:
Act on Instruction: Upon receiving a valid, documented instruction from FinServe,
CloudCorp must promptly and securely delete the client's data from all its systems. This
includes primary storage, backups, caches, and any other environments where the data
resides.
Assist the Controller: CloudCorp must provide the necessary tools and capabilities to
FinServe to enable this deletion. It must also assist FinServe in demonstrating
compliance, for example, by providing confirmation that the deletion was carried out.
********** 8 **********
--- page 9 ---
Secure Deletion: CloudCorp is responsible for ensuring that its deletion process is
secure and permanent, following industry best practices to prevent any possible
recovery of the data.
3. Data Owner: The Client
The Data Owner is the individual (data subject) to whom the personal data relates.
Role Justification: The client is the Data Owner because the personal data (name,
financial information, etc.) is about them. They are the ultimate stakeholder of that
information.
Responsibilities in this Case:
Rights, Not Responsibilities: The Data Owner does not have "responsibilities" in the
operational sense. Instead, they possess rights over their data.
Right to Initiate: In this scenario, the client exercises their fundamental right to erasure
(the "Right to be Forgotten") by initiating the deletion request with FinServe, the Data
Controller they have a relationship with.
Summary of the Data Deletion Process Flow:
1. Initiation: The Data Owner (Client) submits a formal request to the Data Controller
(FinServe) to have their data deleted.
2. Instruction: The Data Controller (FinServe) validates the request and, based on its
legal obligations, issues a formal deletion instruction to the Data Processor
(CloudCorp).
3. Execution: The Data Processor (CloudCorp) executes the deletion across all relevant
systems and confirms completion to the Data Controller.
4. Verification & Accountability: The Data Controller (FinServe) verifies the deletion
and confirms to the Data Owner (Client) that their request has been fulfilled. FinServe
remains ultimately accountable for the entire process.
b. The action taken by the cloud provider's administrator directly creates two distinct threats
for MediCare:
1. Rogue Administrator: This is a specific type of internal threat where a privileged user
(like a system administrator) within the cloud provider's organization abuses their
authorized access to perform malicious or unauthorized actions. In this case, the
administrator secretly moved data without MediCare's knowledge or consent.
Q 3   2. Regulatory Violation: This threat occurs when an organization fails to comply with
[10]
CO - 2;   legal, industry, or governmental regulations. By moving the patient data to an offshore
BL- 3
data center, the action directly breaches the national healthcare law that mandates
domestic storage of patient health records.
Explanation of MediCare's Critical Position
Despite the breach being entirely the cloud provider's fault, MediCare is placed in a
critically vulnerable position due to the principle of legal accountability and the cloud
shared responsibility model.
********** 9 **********
--- page 10 ---
Here’s a breakdown of why:
1. MediCare is the Legally Accountable "Data Controller":
In the eyes of the law and regulators, MediCare is the "Data Controller." This means it
determines why and how patient data is processed and is ultimately responsible for
protecting that data and ensuring its compliance with regulations like the national
healthcare law.The government will hold MediCare—not the cloud provider—
accountable for the violation. This can result in severe consequences for MediCare,
including:
Heavy financial fines imposed by regulatory bodies.
Legal action and lawsuits from affected patients or government agencies.
Loss of accreditation or licenses to operate as a healthcare provider.
Irreparable damage to its reputation and a loss of public trust.
2. The Shared Responsibility Model Places the Compliance Burden on the Customer:
The cloud operates on a shared responsibility model: the provider (cloud provider) is
responsible for the security of the cloud (the infrastructure), while the customer
(MediCare) is responsible for security in the cloud (how they configure and use the
services) and, crucially, data governance and compliance.
While the provider's "Rogue Administrator" is a failure of their duty to secure the
infrastructure, the resulting "Regulatory Violation" falls squarely on MediCare's duty to
govern its data. MediCare failed to ensure its provider had sufficient controls to prevent
this and failed to monitor the data's location.
In essence: MediCare outsourced the storage of its data, but it cannot outsource its legal
liability. The cloud provider's failure becomes MediCare’s compliance failure, placing
the hospital in a critical position of facing direct legal and financial penalties for an action
it did not directly commit. This scenario highlights the paramount importance of rigorous
due diligence, strong contractual agreements (with clear penalties for such breaches), and
continuous compliance monitoring when using cloud services for regulated data.
a.   (a) A company builds and deploys apps without managing servers.
Service Model: Platform as a Service (PaaS)
Deployment Model: Public Cloud
Justification: PaaS is the correct service model because it provides a platform (including
runtime, middleware, and development tools) allowing companies to build and deploy
Q 4   applications without worrying about the underlying infrastructure like servers, storage, or
[10]
CO -1;   operating systems. This perfectly matches the requirement of "without managing servers."
BL- 3
The Public Cloud is the most fitting deployment model as it offers the on-demand,
scalable, and cost-effective platform services needed for application development and
deployment, which is the core offering of PaaS providers like Google App Engine,
Microsoft Azure App Service, or Heroku.
(b) A hospital stores sensitive patient data on its own cloud.
********** 10 **********
--- page 11 ---
Service Model: Infrastructure as a Service (IaaS)
Deployment Model: Private Cloud
Justification: IaaS is ideal because it gives the hospital full control over the infrastructure
(servers, storage, networking) where the data resides. This allows them to implement
specific, stringent security controls, encryption, and access policies required for sensitive
patient data under regulations like HIPAA.
A Private Cloud is mandatory here. It implies the cloud infrastructure is provisioned for
exclusive use by the hospital, ensuring that sensitive patient data is physically and
logically separated from other organizations, maximizing security, compliance, and
control.
(c) A small business uses online accounting software via a browser.
Service Model: Software as a Service (SaaS)
Deployment Model: Public Cloud
Justification: SaaS is the definitive model here. The accounting software is a ready-to-use
application delivered over the internet and accessed via a web browser. The small business
has no concern for the underlying platform or infrastructure; they are simply consuming
the software. Examples include QuickBooks Online, Xero, or FreshBooks.
The Public Cloud is the inherent deployment model for SaaS, as the software vendor hosts
and manages the application in their own data centre, making it available to all their
customers over the public internet.
(d) Multiple universities share cloud resources for research.
Service Model: Platform as a Service (PaaS)
Deployment Model: Community Cloud
Justification: The service model is PaaS as they need a shared platform for collaborative
data analysis. The key is the shared, specific purpose.
A Community Cloud is the best fit. It is a multi-tenant model shared by several
organizations (the universities) with a common mission. It allows them to share costs and
resources (like datasets and high-performance computing clusters) while maintaining a
level of security and policy control.
(e) A retailer combines its data centre with a public cloud for peak loads.
Service Model: IaaS
Deployment Model: Hybrid Cloud
Justification: IaaS is the most common service model in this scenario because it allows
the retailer to easily extend its on-premise data centre capacity by provisioning virtual
machines and storage in the public cloud that can seamlessly connect to their internal
systems.
This is a textbook definition of a Hybrid Cloud. It is a composition of a private
infrastructure (the retailer's own data center) and a public cloud, with orchestration
between them. The primary goal is to handle fluctuating demand ("peak loads" like
********** 11 **********
--- page 12 ---
holiday sales) by "cloud bursting" from the private to the public cloud, maintaining
performance during spikes without over-provisioning their own data center.
b. Draw and explain the NIST Risk Management Framework
Q 4
[10]
CO - 3;
BL- 3
a. The most common and effective combination is SAML for authentication/SSO and OAuth
for authorization.
1. Security Assertion Markup Language (SAML 2.0)
Q 5   Primary Role: Authentication & SSO. It is the cornerstone for achieving classic enterprise
[10]
CO - 2;   SSO.
BL- 3
How it Works: SAML allows an identity provider (IdP) to pass a "security assertion" (a
digitally signed token) to a service provider (SP) to authenticate a user. The user only logs
into the IdP once.
********** 12 **********
--- page 13 ---
Use Case: An employee logs into their company's internal portal (the IdP, like Okta or
Azure AD). When they click a link to Salesforce or Workday (the SP), they are logged in
automatically without entering credentials again. SAML proves who the user is.
Key Strength: Excellent for establishing trust between an organization (IdP) and cloud
applications (SP) for user logins.
2. OAuth 2.0 / OpenID Connect (OIDC)
Primary Role: Authorization (OAuth 2.0) and Authentication (OpenID Connect). They
are often used together.
OAuth 2.0: A framework that allows an application to obtain limited access
(authorization) to a user's resources on another service without sharing the user's
password. It's about what the app can do.
OpenID Connect (OIDC): A simple identity layer built on top of OAuth 2.0. It provides
authentication by verifying the user's identity and returning basic profile information in a
JSON Web Token (JWT).
How it Works: A user grants a client application (e.g., a marketing tool) permission to
access specific resources they own in a resource server (e.g., their Google Drive). OAuth
handles the permission, and OIDC can be used to log the user into the marketing tool in
the first place.
Use Case: "Log in with Google" is a classic example of OIDC for authentication. Granting
a mobile app permission to post to your LinkedIn feed is OAuth for authorization.
3. WS-Federation
Primary Role: Authentication & SSO. It serves a similar purpose to SAML but uses a
different, older standard based on SOAP web services.
How it Works: Like SAML, it allows for identity and security information to be shared
across different security domains.
Use Case: Primarily used in Microsoft environments (e.g., Active Directory Federation
Services). While still supported, SAML and OIDC are more modern and widely adopted
for web-based SSO scenarios.
How They Work Together in a Typical Enterprise Scenario:
A company would implement these standards not in isolation, but as complementary parts
of an Identity and Access Management (IAM) strategy.
1.   Initial Login (SSO & Authentication): An employee goes to a cloud app like
Salesforce. Salesforce redirects them to the company's Identity Provider (e.g., Azure AD).
2. SAML/OIDC in Action: The employee authenticates with the IdP. The IdP then sends
a SAML assertion (or an OIDC ID Token) back, saying "This user is authenticated." The
user is now logged in.
3. API Access (Authorization): Later, the employee uses an internal dashboard that needs
to pull data from Salesforce's API. The dashboard uses OAuth 2.0 to obtain an access
token. It presents this token to the Salesforce API to authorize the data request.
********** 13 **********
--- page 14 ---
b.   Protocol: Remote Desktop Protocol (RDP)
RDP is a proprietary protocol developed by Microsoft that provides a user with a graphical
interface to connect to another computer over a network connection. Its security is not
inherent but is achieved through several built-in and configurable features:
1. Encryption: RDP uses standard cryptographic protocols to encrypt all data transmitted
between the client and the server, including screen updates, mouse movements, and
keystrokes. This prevents eavesdropping (man-in-the-middle   attacks) on the
communication channel.
How it works: By default, it uses native RDP encryption, but it can be configured to use
the more robust TLS/SSL (Transport Layer Security/Secure Sockets Layer) encryption,
like what secures HTTPS websites, ensuring a strongly encrypted tunnel.
2. Authentication: Before a session is established, RDP requires the user to authenticate
themselves to the remote virtual machine.
How it works: It integrates with Windows' standard authentication mechanisms (like
Q 5   NTLM or Kerberos). The user must provide valid credentials (username and password)
[10]
CO - 2;   that exist on the target VM or in its trusted domain. This ensures that only authorized
BL- 3
personnel can gain access.
3. Network-Level Authentication (NLA): This is a critical security enhancement.
How it works: NLA requires the user to authenticate before a full Remote Desktop session
is established. This protects the remote computer from malicious users or denial-of-
service attacks that could exploit the RDP service itself, as the authentication happens at
the network level prior to the resource-intensive process of loading the full graphical user
interface.
A cloud administrator would use an RDP client application (such as the built-in Remote
Desktop Connection on Windows or Microsoft Remote Desktop on macOS) on their local
machine. They would enter the IP address or hostname of the target virtual machine in the
private cloud. The RDP protocol then manages the secure, encrypted connection,
authenticates the administrator, and finally presents the full Windows desktop interface
of the remote VM on their local screen, allowing them to perform graphical configuration
tasks as if they were physically seated in front of it.
a. The Four Main Phases of Business Continuity Planning
For a financial company like SecureFund, these phases are critical to ensure they are
prepared for an event like a major power outage.
Q 6   Phase 1: Business Impact Analysis (BIA)
Objective: Identify and prioritize critical business functions and the impact of their [10]
CO - 2;
BL- 3   disruption.
Specific Action for Preparedness:
SecureFund would conduct a BIA to determine that their core banking transaction
processing and online customer portal are Mission-Critical systems with a Recovery Time
********** 14 **********
--- page 15 ---
Objective (RTO) of minutes. In contrast, their internal HR portal might have an RTO of
days. This analysis directly informs where to invest in redundancy and recovery solutions
before the power outage happens.
Phase 2: Disaster Recovery Plan (DRP) Development
Objective: Create the detailed technical procedures to recover IT infrastructure, data, and
applications.
Specific Action for Preparedness:
Based on the BIA, SecureFund would develop a detailed DRP that includes a step-by-step
procedure for failing over their core banking database and application servers from the
primary data center to a secondary site with independent power grids. This plan would
include specific runbooks for the IT team to execute when the outage occurs.
Phase 3: Disaster Recovery Team Training and Testing
Objective: Ensure the DR team is familiar with the plan and can execute it effectively
under pressure.
Specific Action for Preparedness:
SecureFund would conduct a scheduled disaster recovery drill every six months. During
this drill, the recovery team would practice executing the failover procedure from Phase
2 in a isolated environment. This testing validates the plan, builds muscle memory, and
identifies any gaps or issues in the procedure, ensuring a smooth response during a real
power outage.
Phase 4: Plan Maintenance
Objective: Keep the BCP and DRP updated to reflect changes in the business, technology,
and infrastructure.
Specific Action for Preparedness:
Whenever SecureFund deploys a new banking software update or modifies its server
infrastructure, it must formally update the DRP documentation and runbooks to reflect
those changes. A quarterly review would ensure that the plan remains accurate and viable,
so when a power outage strikes, the team is following a plan that matches the current IT
environment.
b.
SAS 70 (Type   Trust Services
Feature   ISO 27001
II)   (SOC 2)
Q 6   Historic
Status   Current   Current   [10]
CO - 3;   (Superseded)
BL- 3
Security,
Primary   Financial   Information Security
Availability,
Focus   controls   Management System
Confidentiality
********** 15 **********
--- page 16 ---
Governing
AICPA   AICPA   ISO
Body
Output   Audit Report   Audit Report   Certification
Financial
Scope   Operational controls   Comprehensive ISMS
reporting
Global   Very High
Limited (US)   High (Tech sector)
Recognition   (International)
Certification   No   No   Yes
Framework   Auditing
Trust criteria   Management system
Type   standard
Q 7   a.   Features of Hash Function   [10]
CO - 2;   ▪   Arbitrary to fixed length so called hashing the data
BL- 3
▪ Long input to small data so called compression functions
▪ Small representation of lot of data so called Digest
▪   Faster than symmetric encryption functions
Properties of Hash Function
Pre-Image Resistance
This property means that it should be computationally hard to reverse a hash function.
In other words, if a hash function h produced a hash value z, then it should be a difficult
process to find any input value x that hashes to z. This property protects against an attacker
who only has a hash value and is trying to find the input.
Second Pre-Image Resistance
This property means given an input and its hash, it should be hard to find a different input
with the same hash. In other words, if a hash function h for an input x produces hash value
h(x), then it should be difficult to find any other input value y such that h(y) = h(x).
This property of hash function protects against an attacker who has an input value and its
hash and wants to substitute different value as legitimate value in place of original input
value.
Collision Resistance
This property means it should be hard to find two different inputs of any length that result
in the same hash. This property is also referred to as collision free hash function. In other
words, for a hash function h, it is hard to find any two different inputs x and y such that
h(x) = h(y). Since, hash function is compressing function with fixed hash length, it is
impossible for a hash function not to have collisions. This property of collision free only
confirms that these collisions should be hard to find. This property makes it very difficult
for an attacker to find two input values with the same hash. Also, if a hash function is
collision-resistant then it is second pre-image resistant.
********** 16 **********
--- page 17 ---
Q 7   b. The Strategy: "Define, Enforce, Monitor, and Remediate"   [10]
CO - 2;   This approach moves beyond manual checks to an automated, continuous security posture.
BL- 3
I. Proactive Compliance: Establishing the Secure Baseline
1. Create Hardened OS Images (Golden Images):Build and maintain a pre-configured,
security-hardened virtual machine image for each operating system.
How it ensures compliance: This image serves as the secure starting point for all
deployments. It includes:
Latest security patches.
Removed unnecessary services and software.
Pre-configured OS-specific security settings (e.g., password policies, firewall rules,
disabled default accounts).
Installed and configured monitoring/security agents.
2. Define Configuration Standards: Codify your security policies into machine-readable
standards.
How it ensures compliance: Use established benchmarks like the CIS (Center for Internet
Security) Benchmarks to define the specific security settings for your OS. These provide
a clear, industry-accepted definition of a secure configuration.
II. Automated Enforcement: "Shift-Left" Security
Prevent non-compliant systems from being deployed and automatically correct drift in
existing systems.
3. Implement Infrastructure as Code (IaC) Scanning: Scan your IaC templates (Terraform,
CloudFormation, ARM) before deployment for security misconfigurations.
How it ensures compliance: This "shifts security left" by catching policy violations (e.g.,
a VM configured with a public IP, disabled disk encryption) before the resource is ever
created. Tools like Checkov, Terrascan, or AWS Config Rules can do this.
4. Use Automated Configuration Management: Utilize tools like Ansible, Chef, or Puppet
to define and enforce the desired state of your VMs.
How it ensures compliance: If a setting is manually changed (e.g., the firewall is turned
off), these tools can automatically revert it to the compliant state, correcting configuration
drift.
********** 17 **********
--- page 18 ---
III. Continuous Monitoring and Assessment: Gaining Visibility
Continuously verify that your running assets remain compliant.
5. Leverage Cloud-Native Compliance Tools (CSPM): Implement a Cloud Security
Posture Management (CSPM) tool.
How it monitors deviations: Services like AWS Security Hub, Azure Policy, and GCP
Security Command Center continuously scan your cloud environment. They compare your
VMs' configurations against your defined policies (e.g., CIS Benchmarks) and generate
alerts for any deviations, such as:
Unencrypted storage disks.
Security groups allowing unrestricted access.
Missing required tags.
OS vulnerabilities.
6. Deploy a Vulnerability Management Solution: Use a dedicated tool to scan VMs for
known software vulnerabilities and missing patches.
How it monitors deviations: Tools like Qualys VMDR, Tenable.io, or cloud-native
scanners (like Azure Defender for Servers) regularly inspect your VMs. They provide
reports on CVEs, severity scores, and often direct links to patches.
7. Utilize SIEM for Centralized Logging and Alerting: Aggregate OS security logs
(Windows Event Logs, Linux auditd) to a central Security Information and Event
Management (SIEM) system.
How it monitors deviations: The SIEM uses correlation rules to detect suspicious activity
that indicates a compliance deviation, such as:
Multiple failed login attempts.
Changes to user privilege groups.
Unauthorized processes are being spawned.
IV. Automated Remediation: Closing the Loop
Reduce the time between detection and fix.
8. Implement Automated Remediation Workflows: Use cloud-native automation services
(e.g., AWS Lambda, Azure Automation Runbooks, GCP Cloud Functions) to
automatically fix common, low-risk compliance failures.
Examples:
Trigger: A CSPM tool detects an unencrypted disk.
Action: An automation runbook is triggered to enable encryption on the disk.
Trigger: A VM is found without the required monitoring agent.
Action: A script automatically installs the agent.
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper a112afe6b71a

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CyberSecurity_7010/Cloud Security/ANS_Cloud Security(702IT0E002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (22 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Cloud Security
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures on the right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
Q 1   Answer briefly:
a.   Use case   Description
Cloud bursting   Provisioning resources for a limited time from a public
cloud to handle peak workloads
Web application hosting   Hosting less critical applications such as e-commerce
CO - 1;   [05]
BL- 2   applications on the public cloud
Migrating packaged   Migrating standard packaged applications such as
applications   email to the public cloud
Application development   Developing and testing applications in the public cloud
and testing   before launching them
b. Attacks on the Hypervisor Instead of attacking a virtualized instance, which might only
result in successfully breaching the content of one (virtualized) workstation, malicious
actors might attempt to penetrate the hypervisor, which is the system that acts as the
interface and controller between the virtualized instances and the resources of the given
host devices on which they reside.
CO - 2;   [05]
BL – 2   There are two types of hypervisors, known as Type 1 and Type 2. Type 1 is also called a
bare-metal or hardware hypervisor. It resides directly on the host machine, often as
bootable software. Type 2 is a software hypervisor, and it runs on top of the OS that runs
on a host device. Attackers prefer Type 2 hypervisors because of the larger surface area.
They can attack the hypervisor itself, the underlying OS, and the machine directly,
********** 1 **********
--- page 2 ---
whereas Type 1 attacks are restricted to the hypervisor and the machine. OSs are also
more complex than hypervisors, creating the increased potential for included
vulnerabilities.
Guest Escape An improperly designed or poorly configured virtualized machine or
hypervisor might allow for a user to leave the confines of their own virtualized instance.
This is referred to as guest escape or virtual machine (VM) escape. A user who has
successfully performed guest escape might be able to access other virtualized instances
on the same host and view, copy, or modify data stored there. Worse, the user might be
able to access the host itself and therefore be able to affect all the instances on the
machine. And the worst potential situation is known as host escape, where a user can not
only leave their own virtualized instance, they can even leave the host machine, accessing
other devices on the network. This may be unlikely, as it would only result from some
rather egregious failures in hardware, software, policy, and personnel performance (or
significant combinations thereof), but it is a risk and must be considered.
Information Bleed This is another risk stemming from malfunctions or failures. The
possibility exists that processing performed on one virtualized instance may be detected,
in whole or in part, by other instances on the same host. In order for this risk to be
detrimental, the loss does not even have to involve the raw data itself. It might instead be
only indicative of the processing occurring on the affected instance. For example, it might
be possible to detect that a certain operation is happening on the affected instance and that
the operation lasts for a specific duration. This kind of process-specific information can
tell a malicious actor about the types of security controls on the instance or what kind of
operations are being conducted. This can provide the attacker with an advantage because
they might be able to narrow down a list of possible attack vectors to only those that will
function in that circumstance, or they might gain an insight into what types of material
might be acquired from a successful attack. This tactic is often referred to as a side channel
or covert channel attack.
Data Seizure Legal activity might result in a host machine being confiscated or inspected
by law enforcement or plaintiffs’ attorneys, and the host machine might include
virtualized instances belonging to your organization, even though your organization was
not the target. Cloud data centers can be perceived as similar to DMZs in legacy
enterprises. Because everything in the cloud can be accessed remotely, it can be
considered exposed to the Internet, to a greater or lesser extent. Instead of the discrete
perimeter of a private network, cloud configurations may be more porous or might be
considered to have no specific perimeter boundary at all.
c. The ingress and egress rules of a VPC Security Group act as a fundamental, stateful
CO -2;   firewall that controls the flow of traffic to and from your cloud resources.   [05]
BL – 2
1. The Role of Ingress Rules: The "Bouncer" at the Door
********** 2 **********
--- page 3 ---
Ingress rules control incoming traffic to your cloud resources (like EC2 instances, RDS
databases). Their primary role is to prevent unauthorized access and reduce the attack
surface.
How They Protect Resources: Principle of Least Privilege: They enforce the rule that only
specific, allowed sources can talk to a resource on specific ports.
Example: A web server should only allow ingress traffic on port `80` (HTTP) and `443`
(HTTPS) from the public internet (`0.0.0.0/0`), and perhaps on port `22` (SSH) only from
your corporate IP address. It should not allow RDP (port `3389`) from the entire internet.
Segmentation: They enable micro-segmentation within your VPC. A database Security
Group should only allow ingress on port `3306` (MySQL) from the specific application
server's Security Group—not from the entire web server tier or the internet.
Mitigating Attack Vectors: By blocking all ports by default and only opening necessary
ones, they protect against port scanning, brute-force attacks, and exploitation of
vulnerabilities on unauthorized services.
2. The Role of Egress Rules: The "Prison Warden" Controlling Exits
Egress rules control outgoing traffic from your cloud resources. Their primary role is to
contain breaches, prevent data exfiltration, and control external communications.
How They Protect Resources: Containing Compromised Systems: If a hacker
compromises a web server, their next step is often to "call home" to a command-and-
control (C2) server or to exfiltrate stolen data. Strict egress rules can block this.
Example: A web server typically only needs to make outbound calls on port `443`
(HTTPS) to download patches or connect to an external API. Its egress rules should reflect
this. It should not be allowed to make outbound connections on unusual ports like `6667`
(IRC, often used for C2) or to every IP on the internet.
Data Loss Prevention (DLP): They can be configured to only allow connections to
specific, trusted destinations. For instance, a server processing credit cards might only be
allowed access to a specific Payment Gateway IP range on port `443`, preventing it from
sending data to an unknown server.
Controlling Lateral Movement: In a multi-tier architecture, you can use egress rules to
prevent a compromised server in one tier from probing or attacking servers in another.
For example, a web server shouldn't be able to initiate a connection to a database server;
only the app server should.
d. Cloud Security Auditing Challenges
Transparency : In a cloud environment, cloud providers control most of the operational
and forensic data. This data is critical for auditing purposes. Audits must have a
CO - 3;   comprehensive inventory of cloud resources and data, access to security policies, and [05]
BL- 2
direct access to relevant forensic data. This requires coordination with cloud providers
and the organization’s IT operations staff.
Encryption: There are a two main options for encrypting data in the cloud:
********** 3 **********
--- page 4 ---
You can encrypt data on-premises and then send it to the cloud, but this runs the risk of
rogue insiders abusing their privileges.
You can leave encryption to the cloud provider, but then you will be at risk of breaches
within the cloud provider’s environment.
From an auditing perspective, it is almost always better to encrypt data on-premise and
manage encryption keys in-house. Auditing can be extremely difficult, even impossible
in some cases, if encryption keys are managed by the cloud provider. The PCI DSS Cloud
Special Interest Group encourages organizations to store and manage encryption keys
independently from the cloud provider.
Colocation : In a cloud environment, it is very common for several environments to share
the same physical systems. This creates security issues and makes it more difficult to audit
the physical environment. If it is not possible to run services on physically separate
devices, the cloud provider must provide proof that it can prevent any user of the system
from gaining administrative privileges on the machine.
Scale, Scope, and Complexity : In a traditional data center, there was a finite number of
servers, which auditors could review and report on. In a cloud environment, there can be
exponential growth in the number of audited entities, which may include physical hosts,
virtual machines (VMs), managed databases, containers, and serverless functions. It can
be very difficult to audit all these entities, especially considering new entities are added
and removed daily.
The key to making a cloud environment auditable is to standardize workloads. For
example, if containers are only created using a limited, controlled set of images, auditors
can focus their testing on those approved container images. Similarly, VMs should be
created from a limited pool of machine images that can be reviewed by auditors.
a.   1. Cloud Migration: The process of moving digital assets—such as data, applications, and
IT processes—from on-premises infrastructure or one cloud environment to another.
Example: A bank decides to shut down its private data center. It moves its customer-
facing mobile app, along with its associated databases, to Amazon Web Services (AWS).
The app servers are migrated as virtual machines (lift-and-shift), while the database is
migrated to a managed AWS service like Amazon RDS. This migration reduces the bank's
Q 2   hardware maintenance costs and allows it to scale easily during peak transaction times.
[10]
CO - 1;   2. Multi-tenancy: An architecture where a single instance of a software application and
BL- 4
its underlying infrastructure serves multiple customers ("tenants").
Example: Salesforce, a SaaS CRM platform, uses multi-tenancy. Thousands of different
companies all use the same Salesforce application code and infrastructure. However,
Company A's sales data is completely walled off and inaccessible to Company B, even
though they are using the same platform. This model allows Salesforce to achieve
economies of scale and offer the service at a lower cost.
********** 4 **********
--- page 5 ---
3. Cost-Benefit Analysis: A financial process used to evaluate the potential costs and
benefits of a proposed project, such as a cloud migration, to determine its economic
feasibility.
Example: A company considers migrating its email server to Microsoft 365 (a SaaS
solution).
Costs: Monthly subscription fees, migration project costs, training for IT staff.
Benefits: Elimination of server hardware costs, reduced IT staff time for maintenance and
patches, improved collaboration features, enhanced security and uptime.
The analysis would compare the 3-year total cost of ownership (TCO) of the on-premises
server against the 3-year TCO of the cloud subscription to see which is more financially
sound.
4. Vendor Lock-In / Lock-Out: The situation where a customer becomes dependent on a
single cloud provider's technologies and services, making it difficult, costly, or impossible
to migrate to another provider.
Example (Lock-In): A startup builds its entire application using AWS-specific services
like Amazon DynamoDB (database), Amazon S3 (storage), and AWS Lambda (serverless
computing). To move this application to Google Cloud, they would need to re-write
significant portions of their code to use equivalent Google services like Cloud Firestore,
Cloud Storage, and Cloud Functions. This high switching cost creates strong vendor lock-
in.
Example (Lock-Out): A developer accidentally misconfigures a script, leading to a
massive, unexpected bill that exceeds their credit limit. The cloud provider's automated
system suspends the account to prevent further charges, instantly locking the developer
out of their virtual servers and data until the bill is paid.
5. Managed Service Provider (MSP): A third-party company that remotely manages a
customer's IT infrastructure and end-user systems on a proactive basis.
Example: A small e-commerce business uses AWS but lacks a dedicated IT team. They
hire an MSP. The MSP's responsibilities include:
Monitoring the website's cloud servers 24/7.
Applying critical security patches.
Managing backups and ensuring disaster recovery is in place.
Providing support and optimizing costs.
This allows the business owners to focus on marketing and sales, not on managing cloud
infrastructure.
b. Two-Step Technical Approach for Data Security
Q 2   This strategy employs "defense in depth," protecting data both in transit to the cloud and
CO - 2;   at rest within the cloud.   [10]
BL- 4   Step 1: Prevent Upload of Sensitive Data
Specific Technique: Implement a Cloud Data Loss Prevention (DLP)
********** 5 **********
--- page 6 ---
Justification: A Cloud DLP tool is specifically designed to discover, classify, and protect
sensitive data. It solves the first requirement by acting as a gatekeeper.
How it works: SafeBank would deploy the DLP solution at the network egress point (or
as an API-based scanner) to inspect all outbound data destined for the cloud database.
Action: The DLP tool would be configured with a policy to scan for patterns that match
credit card numbers (Primary Account Numbers or PANs), such as the 16-digit Luhn-
validated format. When a match is found, the tool can block the upload in real-time,
quarantine the data, and alert the security team.
Result: This prevents unauthorized or accidental uploads of credit card data, ensuring it
never reaches the cloud database in its raw, cleartext form. It enforces data handling
policies at the point of egress.
Step 2: Render Stored Data Useless to Attackers
Specific Technique: Implement Tokenization
Justification: While encryption is a valid security control, tokenization is superior for this
specific use case of protecting a structured data field like a credit card number. It directly
ensures that a breach of the database does not compromise the actual PANs.
How it works: The system is designed so that any credit card data that is approved for
storage is immediately sent to a highly secure, separate tokenization service (either cloud-
based or on-premises). This service replaces the sensitive PAN with a random, non-
sensitive equivalent called a token, which has no mathematical relationship to the original
number. The token is what gets stored in the cloud database. The vault securely stores the
mapping between the token and the original PAN.
Result: In the event of a cloud database breach, the attackers only steal these meaningless
tokens. Without access to the separate, heavily fortified tokenization vault, they cannot
reverse-engineer or decrypt the tokens to obtain the real credit card numbers. The actual
data remains safe, fulfilling the second requirement.
Why is this effective:
Step 1 (DLP) is a proactive, preventive control that minimizes risk and exposure.
Step 2 (Tokenization) is a defensive, resilient control that assumes a breach will happen
and ensures the impact is negligible.
This two-layered approach ensures that SafeBank's sensitive customer data is protected
by both a "guard at the gate" and an "impenetrable safe," providing comprehensive
security throughout the data lifecycle.
a.   ShopBay's move to a hybrid cloud introduces both agility and complex security
challenges. An ISMS, particularly one aligned with the ISO/IEC 27001 standard, provides
Q 3   the necessary framework to manage these risks systematically. The goal is to create a
[10]
CO - 3;   unified security posture that spans both private and public clouds, ensuring PCI DSS
BL- 3
compliance and resilience against cyber threats.
Core Components of the Hybrid Cloud ISMS
********** 6 **********
--- page 7 ---
1. Establish a Unified Governance and Risk Management Framework
The foundation of the ISMS must be a single, overarching governance model that treats
both cloud environments as parts of one system.
Action: Define a Single Set of Security Policies: Create information security policies that
apply equally to both the private and public cloud. These policies must explicitly address
data classification, access control, encryption, and incident response, regardless of where
the data resides.
Formalize the Shared Responsibility Model: Document, in detail, the security
responsibilities of ShopBay (the customer) and the public cloud provider. For the private
cloud, ShopBay retains full responsibility. This clarity is critical for PCI DSS compliance.
2. Data Security and PCI DSS Compliance
This is the core of protecting customer data and meeting PCI DSS requirements.
Action: Data Classification and Flow Mapping: Clearly classify all data, with "Cardholder
Data" (CHD) as the highest priority. Map exactly how CHD flows through the hybrid
architecture, identifying every touchpoint in both clouds. This is the prerequisite for all
other controls.
Strict Data Segmentation: Mandate that all CHD is stored and processed exclusively in
the private cloud. The public cloud should only handle web traffic, product catalogues,
and other non-sensitive data. This drastically reduces the scope for PCI DSS auditing.
End-to-End Encryption:
In Transit: Enforce TLS 1.2+ encryption for all data moving between the public and
private cloud, and to end-users.
At Rest: Implement strong encryption (AES-256) for all CHD in the private cloud. For
the public cloud, use the cloud provider's encryption services but manage the encryption
keys yourself using a Cloud Hardware Security Module (HSM) or a dedicated key
management service.
3. Access Control and Identity Management
Prevent unauthorized access across both environments.
Action: Implement a Centralized Identity and Access Management (IAM) Solution: Use
a single identity provider (e.g., Azure Active Directory) to manage user access to both
clouds. Enforce Multi-Factor Authentication (MFA) for all administrative access and any
access to systems handling CHD.
Principle of Least Privilege: Configure granular access controls. Users and systems in the
public cloud should have minimal to no access rights to the private cloud where CHD
resides.
4. Continuous Monitoring and Threat Detection
Gain visibility and proactively identify threats across the hybrid environment.
Action: Deploy a Unified Security Monitoring Platform: Implement a Cloud Security
Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) solution.
********** 7 **********
--- page 8 ---
The CSPM will continuously check both environments for misconfigurations (e.g., a
mistakenly public storage bucket), while the CWPP will monitor the workloads
themselves for malicious activity.
Centralized Logging and SIEM: Aggregate logs from all components—public cloud
services, private cloud hypervisors, firewalls, and applications—into a central Security
Information and Event Management (SIEM) system. Use this to create correlated alerts
for suspicious activities, such as a brute-force attack originating from the public web tier
against the private data tier.
5. Incident Response and Business Continuity
Prepare for and respond to security incidents effectively.
Action: Update the Incident Response Plan: Ensure the plan explicitly covers scenarios in
the hybrid cloud, such as a breach of the public web tier or a ransomware attack on the
private data cloud. Define clear procedures for containment that may involve isolating
one cloud from the other.
Hybrid Backup and DR Strategy: Implement a robust backup strategy. Critical data from
the private cloud should be replicated to a secure, isolated location. Regularly test failover
procedures to ensure business continuity in the event of an outage or attack.
b. Two Risks are Contractual Failure and Legal Seizure.
As GlobalCorp's Chief Compliance Officer, follow the comprehensive strategy to mitigate
the risks of Contractual Failure (where the provider is forced to violate its service
agreement) and Legal Seizure of our data.
Two-Pronged Risk Mitigation Strategy
This strategy focuses on maintaining control of our data through technical and contractual
means, ensuring its confidentiality and availability even if the provider is compelled to
act against us.
1. Mitigating Risk of Legal Seizure: Make the Data Useless to Third Parties
Specific Technique: Implement Client-Side Encryption with Customer-Managed Keys
Q 3
(CMK) and a Hybrid Cloud Architecture.   [10]
CO - 2;
BL- 3   Justification & Implementation:
1. Encryption Before Upload: All sensitive data (manufacturing IP and customer
information) must be encrypted before it leaves GlobalCorp's network and is uploaded to
the public cloud. The encryption keys must be generated and stored exclusively within
our on-premises infrastructure or in a Cloud Hardware Security Module (HSM) service
that we manage in a different legal jurisdiction.
2. Render Seized Data Irrelevant: If the government seizes the physical servers in the
data center, they will only get encrypted, unreadable data blobs. Without access to the
encryption keys (which are outside their legal jurisdiction and our direct control), the data
is commercially worthless and provides no intellectual property or customer details.
********** 8 **********
--- page 9 ---
3. Hybrid Data Residency: For our most critical "crown jewel" assets, we can augment
this by keeping the only master, unencrypted copy in a private, on-premises data
warehouse within our headquarters' country. The public cloud would then be used for
processing encrypted data or for less sensitive, non-mission-critical workloads.
2. Mitigating Risk of Contractual Failure: Ensure Operational Resilience and Legal
Recourse
Specific Technique: Implement a Multi-Cloud Architecture and strengthen Contractual &
Due Diligence Measures.
Justification & Implementation:
1. Multi-Cloud Distribution: We must avoid dependency on a single cloud provider in a
single legal jurisdiction. We will architect our systems to run across at least two different
public cloud providers (e.g., AWS in Region A and Google Cloud in Region B). This
ensures that if one provider is forced to shut down our services, we can automatically
failover to the other, maintaining business continuity. Data should be asynchronously
replicated between these environments.
2. Contractual Safeguards:
"Notice of Legal Request" Clause: Re-negotiate the contract to include a clause that
legally obligates the provider to notify us of any government or legal request for our data
before complying, unless explicitly prohibited by law. This provides a critical early
warning.
Data Portability & Exit Clauses: Contracts will explicitly state our right to retrieve all our
data and the provider's obligation to assist in a secure and timely manner, especially in a
termination scenario.
Financial Penalties: The contract must include severe financial penalties for the provider
if they breach the agreement due to a contractual failure, creating a strong disincentive.
3. Enhanced Due Diligence: We will immediately conduct a review of our current and
potential future cloud providers, prioritizing those with a strong public track record of
challenging government overreach and transparent reporting on legal requests.
a. Recommended Cloud Service Model: Platform as a Service (PaaS)
Justification: The university's needs perfectly align with the core value proposition of
PaaS.
No Server, OS, or Runtime Management: The PaaS provider (e.g., Microsoft Azure App
Q 4   Service, Google App Engine, AWS Elastic Beanstalk) fully manages the underlying
infrastructure—including servers, storage, networking, and operating systems—as well as [10]
CO -1;
BL- 3   the runtime environment (e.g., .NET, Node.js, Python). This frees the IT department from
all patching, maintenance, and capacity planning for the infrastructure.
Full Control over Application and Configuration: Unlike SaaS (Software as a Service),
where you get a pre-built application, PaaS provides a platform for deploying custom
code. The university's IT developers retain full control over the application's codebase,
********** 9 **********
--- page 10 ---
feature set, and application-level configuration settings (e.g., environment variables,
connection strings, scaling rules).
Cost-Effective: PaaS is more cost-effective than IaaS (Infrastructure as a Service) for this
use case because the university does not pay for dedicated virtual machines that might sit
idle. They primarily pay for the compute and resources consumed by the application itself,
leading to better resource utilization and lower management overhead.
PaaS gives the developers exactly what they want—a place to deploy and run their custom
application—while taking away exactly what they don't want—the burden of managing
the platform it runs on.
Recommended Cloud Deployment Model: Public Cloud
Justification: A public cloud deployment is the most suitable model for this scenario.
Cost-Effective and Shared: The public cloud is inherently designed as a multi-tenant
environment where infrastructure is shared among many customers. This model achieves
the highest economies of scale, which is passed on to the customer as lower costs, directly
meeting the "cost-effective" requirement.
"Shared Across Multiple Departments": A public cloud service is perfectly suited for an
application that needs to be accessed by multiple university departments (e.g., students,
faculty, administration) over the public internet. Access control is managed at the
application and identity level, not the network level.
Elastic Scaling: The student portal will likely have variable traffic (high during course
registration, low during holidays). The public cloud allows the application to scale
automatically, ensuring performance during peaks and cost savings during lulls.
b. SIX Steps to Conducting a Cloud Security Audit
1. Evaluate the Cloud Provider’s Security Posture
The first step of a cloud security audit is evaluating the cloud provider’s security posture,
and establishing a relationship with cloud provider staff to receive the necessary
information. As part of your audit, evaluate security procedures and policies, and work to
determine the risk inherent in cloud systems, based on reliable data from cloud systems.
Q 4   2. Determine The Attack Surface
[10]
CO - 3;   Cloud environments are complex and have low visibility. Use modern cloud monitoring
BL- 3
and observability technology to identify the attack surface, prioritize assets at higher risk,
and focus remediation efforts.
Understand what applications are running within cloud instances and containers, and
whether they are approved by the organization, or represent shadow IT. All workloads
must be standardized and must have the appropriate security measures to ensure
compliance.
********** 10 **********
--- page 11 ---
This type of monitoring can address the difficulties of the shared responsibility model, by
providing visibility into the security profile of the cloud assets you manage on an ongoing
basis.
3. Set Strong Access Controls
Access management breaches are one of the most prevalent cloud security risks. There
are many ways in which credentials to critical cloud resources can fall into the wrong
hands. Here are some steps you can take to minimize risk from your side:
Create strong password standards and policies
Make multi-factor authentication (MFA) a must
Limit administrative privileges
Practice the least privilege principle for all cloud assets
4. Develop External Sharing Standards
You must implement standards for data sharing via shared drives, calendars, files, and
folders. The best approach is to begin with the strictest standards and loosen security
restrictions if there is a special need.
Folders and files featuring the most sensitive data, including personally identifiable
information (PII), financial, and protected medical information (PHI), should not be
permitted for external access and sharing, except in special circumstances.
5. Automate Patching
You should regularly patch to ensure your cloud environment is secure. However,
mastering patch management can be challenging for security and IT teams. Multiple
studies found that it takes organizations over a month on average to patch a security
weakness.
The key to effective patching is to prioritize the most important patches, and ensure that
critical assets are patched automatically on a regular basis. Complement automation with
regular manual reviews to ensure that patching mechanisms are functioning properly.
6. Use SIEM to Standardize Cloud Logs
Security information and event management (SIEM) systems can help organizations
comply with many industry standards and regulations. Log management, a function of
SIEM, is an industry-standard approach for auditing activity on an IT network. SIEM
systems can collect cloud logs in a standardized format, and allow editors to explore log
data, and automatically generate reports needed for various compliance standards.
Significance of internal auditing in cloud.
The Significance of Internal Auditing in the Cloud
An internal cloud audit is a systematic, independent assessment of an organization's cloud
environment, controls, and processes. Its significance is multi-faceted:
1. Proactive Risk Management and Continuous Compliance
********** 11 **********
--- page 12 ---
Significance: Cloud environments are dynamic; a configuration that was secure yesterday
can be non-compliant today due to a minor change. Internal audits provide a continuous
feedback loop.
How it works: Auditors don't just check a static snapshot. They verify that continuous
compliance monitoring tools (like AWS Security Hub or Azure Policy) are properly
configured and that alerts are being acted upon. This proactively identifies
misconfigurations, security gaps, and policy violations before they are exploited or
discovered in an external audit.
2. Validating the Shared Responsibility Model
Significance: This is the single most crucial cloud-specific function. The cloud operates
on a "Shared Responsibility Model," where the provider is responsible for the security of
the cloud, and the customer is responsible for security in the cloud. Internal auditing is
the primary mechanism for validating that the customer is upholding their side of this
model.
How it works: The audit tests customer-controlled configurations, such as:
Are S3 buckets encrypted and not publicly accessible?
Are security group (firewall) rules following the principle of least privilege?
Is IAM (Identity and Access Management) properly configured without excessive
permissions?
This ensures the organization is not operating under a false sense of security, believing
the cloud provider is handling everything.
3. Cost Optimization and Financial Governance (FinOps)
Significance: In the cloud, wasted resources directly translate to wasted money. Internal
auditing is a cornerstone of FinOps, the practice of bringing financial accountability to
cloud spending.
How it works: Auditors analyze cloud spending and resource utilization to identify:
Orphaned Resources: Unattached storage volumes or unused virtual machines.
Over-Provisioning: Instances that are too large for their workload.
Inefficient Pricing Models: Failure to use savings plans or spot instances.
This provides actionable insights to right-size resources and eliminate waste, directly
impacting the bottom line.
4. Building a Culture of Security and Accountability
Significance: Internal auditing moves cloud security from being solely the IT team's
responsibility to an organization-wide accountability.
How it works: By regularly reviewing and reporting on cloud practices, the audit process:
Educates developers and other teams on secure configurations.
Creates clear lines of ownership for cloud resources through tagging and policy.
Ensures that security is "baked in" from the start (Shift-Left), rather than being an
afterthought.
********** 12 **********
--- page 13 ---
5. Ensuring Operational Resilience and Business Continuity
Significance: The business impact of a cloud outage or data loss can be catastrophic.
Internal auditing verifies that the organization is prepared to withstand and recover from
incidents.
How it works: The audit assesses:
Backup and Recovery Procedures: Are backups automated, encrypted, and tested
regularly?
Disaster Recovery (DR) Plans: Is there a documented and practiced DR plan? Does it
meet the Recovery Time and Point Objectives (RTO/RPO)?
High Availability Configurations: Is the architecture designed to avoid single points of
failure?
6. Preparing for External Audits and Maintaining Trust
Significance: A robust internal audit program is the best preparation for mandatory
external audits (e.g., for SOC 2, ISO 27001, PCI DSS, HIPAA).
How it works: By continuously gathering evidence and refining controls, the organization
enters an external audit with confidence. This minimizes last-minute scrambles, reduces
audit fees, and successfully achieves compliance certifications. These certifications are
essential for building trust with customers, partners, and regulators.
a.   Two-Part Solution for Comprehensive Cloud Security
This two-layered approach protects the application at the entry point and secures the data
at its core.
Part 1: Web Application Firewall (WAF)
Purpose: To protect the web application from external attacks by filtering and monitoring
HTTP/HTTPS traffic.
How it Works: A WAF acts as a shield in front of the web application, inspecting all
incoming traffic for malicious patterns. It uses a set of rules (often based on the OWASP
Top 10) to identify and block common attacks before they reach the application servers.
Q 5   Specific Threats it Mitigates:
SQL Injection (SQLi): Prevents attackers from inserting malicious SQL code into input [10]
CO - 2;
BL- 3   fields to manipulate the database.
Cross-Site Scripting (XSS): Blocks scripts injected by attackers from executing in a user's
browser.
Cross-Site Request Forgery (CSRF): Stops unauthorized commands from being
transmitted from a user that the web application trusts.
Other OWASP Top 10 threats like security misconfigurations and known vulnerabilities.
Justification: A WAF is a critical first line of defense. It is specifically designed to
understand web traffic and application logic, making it highly effective at stopping the
most common and damaging web-based attacks that traditional firewalls miss.
Part 2: Database Activity Monitoring (DAM) Tool
********** 13 **********
--- page 14 ---
Purpose: To monitor, record, and analyze all database activity in real-time, providing an
audit trail and detecting anomalous behavior.
How it Works: A DAM tool sits between the database and the users/applications accessing
it. It logs all transactions, queries, and access attempts—whether they come from the web
application, an administrator, or a compromised account. It uses behavioral analytics to
establish a baseline and alert on unusual activity.
Specific Capabilities and Benefits:
Audit Trail: Creates an immutable log of "who did what, when, and how" on the database,
which is essential for compliance (e.g., PCI DSS, SOX, GDPR).
Privileged User Monitoring: Tracks the activity of powerful users (like DBAs) to prevent
insider threats or misuse of credentials.
Data Exfiltration Detection: Alerts on unusually large data exports or access patterns that
suggest someone is stealing information.
Blocking and Alerting: Can be configured to send real-time alerts or even block suspicious
queries in real-time.
Justification: While a WAF protects the front door, a DAM tool protects the vault. If an
attacker bypasses the WAF (e.g., through a zero-day vulnerability) or if a threat comes
from inside, the DAM tool provides the last line of defense for the data itself. It ensures
visibility and accountability for all data access.
b. VXLAN (Virtual Extensible LAN) is a network virtualization technology that creates a
Layer 2 overlay network on top of a Layer 3 (IP) underlay network. It's fundamental to
modern cloud architecture.
1. The Core Problem it Solves:
Cloud providers have a massive scale of tenants. Traditional VLANs (Virtual LANs) are
limited to 4,096 unique IDs (VLAN tags), which is insufficient for a multi-tenant cloud.
VXLAN solves this by creating a much larger logical address space.
2. Key Components & The Overlay Network:
VTEP (VXLAN Tunnel Endpoint): This is the most critical component. A VTEP is a
Q 5   virtual or physical switch that encapsulates and de-encapsulates VXLAN traffic.
[10]
CO - 2;   In the Cloud, a hypervisor's virtual switch (e.g., vSphere Distributed Switch, Azure
BL- 3
Hyper-V vSwitch) acts as the VTEP for each virtual machine (VM).
Cloud Example: In AWS, the underlying host (Nitro system) acts as the VTEP for your
EC2 instances. In Azure, every VM's virtual network interface has a VTEP function.
VXLAN Network Identifier (VNI): This is a 24-bit segment ID, allowing for over 16
million unique networks (2^24), compared to VLAN's 4,096. This VNI segregates traffic
for different tenants or applications.
Cloud Example: Each customer's Virtual Private Cloud (VPC) or Virtual Network (VNet)
uses unique VNIs internally to keep their traffic completely isolated from millions of other
customers.
********** 14 **********
--- page 15 ---
Encapsulation: When VM-A in VNI 5001 wants to send a frame to VM-B in the same
VNI but on a different physical host, the process is:
1. VM-A sends a standard Ethernet frame.
2. The source VTEP encapsulates this entire Layer 2 frame inside a VXLAN header
(which contains the VNI) and a UDP header.
3. This UDP packet is then placed inside a standard IP packet, using the IP addresses of
the source and destination VTEPs.
4. This IP packet is routed through the underlying physical network (the underlay) to the
destination VTEP.
5. The destination VTEP de-encapsulates the packet, reads the VNI to ensure it's correct,
and forwards the original Ethernet frame to VM-B.
3. Typical Cloud Implementation Flow:
1. A tenant provisions a virtual network (e.g., an AWS VPC).
2. The cloud provider's control plane automatically assigns a VNI to this network.
3. When a VM is launched in this network, the hypervisor's VTEP is programmed with
the VNI.
4. All communication between VMs in this network, even across different physical racks
and availability zones, is seamlessly encapsulated and tunneled using VXLAN.
Advantages of VXLAN
1. Massive Scale: The 24-bit VNI allows for up to 16 million logical networks, which is
essential for large public clouds serving millions of customers.
2. Overcomes Physical Network Limitations: It enables Layer 2 connectivity between
hosts that are geographically separated across a Layer 3 IP network. This allows for:
Workload Mobility: VMs can live-migrate (e.g., vMotion) between different IP subnets
without changing their IP address.
Elasticity: A single logical network can span multiple availability zones or data centers.
3. Optimized Network Utilization: VXLAN uses IP routing in the underlay, allowing for
efficient use of equal-cost multi-path (ECMP) routing to maximize bandwidth and provide
redundancy.
4. Strong Tenant Isolation: The VNI provides logical separation that is as effective as
VLANs but on a much larger scale, ensuring multi-tenancy security.
Disadvantages of VXLAN
1.   Complexity: The overlay/underlay model introduces significant complexity in
management, troubleshooting, and monitoring. Network engineers must debug both the
physical underlay and the virtual overlay.
2. Performance Overhead (Data Plane Offloads):
Encapsulation/Decapsulation: Adding VXLAN, UDP, and IP headers (typically 50+
bytes) to every packet increases CPU load on the VTEPs.
********** 15 **********
--- page 16 ---
Mitigation: Modern cloud infrastructure uses specialized hardware (NICs with VXLAN
offloading) to perform this encapsulation in hardware, minimizing the performance
penalty. Without this, software-based encapsulation can impact throughput and latency.
3. Broadcast, Unknown Unicast, and Multicast (BUM) Traffic Handling:
VXLAN relies on the underlay network to efficiently replicate BUM traffic (like ARP
requests) to all VTEPs in the same VNI. This can be challenging to configure and scale.
Many cloud providers use head-end replication or centralized controllers instead of native
multicast.
4. Potential for Misconfiguration: The flexibility of creating large overlay networks can
lead to complex security group and routing policies that, if misconfigured, can
inadvertently expose resources.
a.   Potential emergent BIA concerns include, but are not limited to, the following:
New Dependencies Your data and operations will be reliant on external parties in whole
new ways after migration. Not only will you have to depend on the cloud provider to meet
your organization’s needs, but all the downstream and upstream dependencies associated
with the provider as well, including the provider’s vendors, suppliers, utilities, personnel,
and so on. The BIA should consider possibilities involving the provider’s inability to meet
service requirements in addition to similar failings on the part of any of the provider’s
requisite entities.
Regulatory Failure The efficiency and ease of data distribution in the cloud enhances
potential violations of regulations as users and administrators alike promulgate and
disseminate data in new ways. The cloud provider presents another potential point of
failure for regulatory compliance as well. Even if your organization is fully compliant
internally, the provider might be unable or unwilling to adhere to your policies.
Q 6   Regulatory failures could include insufficient protection for PII/ePHI data to comply with
[10]
CO - 2;   statutory requirements such as GDPR, GLBA, HIPAA, FERPA, or SOX, and they might
BL- 3
also take the form of contractual inadequacies, such as copyright licensing violations. The
BIA needs to include discussion of possible impacts from this situation.
Data Breach/Inadvertent Disclosure Cloud computing magnifies the likelihood and
impact of two existing risks: internal personnel and remote access. Moreover, because full
legal liability for breaches of PII can’t be transferred to the provider, the cloud customer
must reassess the potential impact and effect of an unauthorized disclosure, especially in
terms of costs resulting from data breach notification legislative mandates. Other potential
adverse results from breaches that should be addressed in the revised BIA include, but
aren’t limited to, public disclosure of deleterious internal communication and reporting;
loss of competitive advantage; negative effect on customer, supplier, and vendor
goodwill; and contractual violations.
Vendor Lock-In/Lock-Out The BIA should take these risks into account for any
operations migrated to the cloud. Much of the data for this part of the report should
********** 16 **********
--- page 17 ---
be readily available and won’t have to be re-created for the BIA as it should have been
performed as part of the cost-benefit analysis when the organization first considered
migration.
There are three general means of using cloud backups for BC/DR. The basic ways of using
cloud backups for BC/DR include the following:
Private Architecture, Cloud Service as Backup If the organization maintains its own
traditional IT data center for the primary production environment, BC/DR plans can
include the use of a cloud provider as the backup. Negotiations with providers will have
to include periodic upload bandwidth costs (which often include monthly caps as the
limiting factor); frequency of backups; whether the organization will use a full,
incremental, or differential backup schedule; the security of the data and systems at the
backup data center; and ISP costs. In this methodology, the customer should determine
when failover will occur—that is, the customer can decide what constitutes an emergency
situation and when normal (internal) operations will cease and the backup will be utilized
as the operational network. This may involve a formal declaration to include notifying the
provider and will almost certainly require additional cost for the duration of the crisis
event. Failover might take the form of using the cloud service as a remote network (in an
IaaS, PaaS, or SaaS arrangement), or it might require downloading the backup data from
the cloud to another physical production site for contingency operations. The negotiation
between customer and provider should determine how and when that download occurs,
how long it should take, and how
and when data will be restored to the normal operations location at the end of the crisis
event.
Cloud Operations, Cloud Provider as Backup One of the attractive benefits of cloud
operations is the resiliency and redundancy offered by cloud data centers, especially from
market leaders. Cloud providers might offer a backup solution as a feature of their
service—a backup located at another data center owned by the provider in case of disaster-
level events. In this motif, the provider will have all the responsibility for determining the
location and configuration of the backup and most of the responsibility for assessing and
declaring disaster events. The customer may have some minimal participation in the
failover process, but that’s the exception rather than the rule. BC/DR activity, including
failover, should usually be transparent to the customer in this case. Moreover, if this
feature is offered as part of the normal cloud operation, it will usually be at no or little
additional cost.
Cloud Operations, Third-Party Cloud Backup Provider In this situation, regular
operations are hosted by one cloud provider, but contingency operations require failover
to another cloud provider. The customer may opt for this selection in order to distribute
risk, enhance redundancy, or preemptively attenuate the possibility of vendor lock-
out/lock-in. This may be the most complicated BC/DR arrangement to negotiate because
********** 17 **********
--- page 18 ---
it will have to involve preparations and coordination between all three parties and roles
and responsibilities must be explicitly and thoroughly delineated. Under this arrangement,
both the primary cloud provider and the cloud customer will take part in emergency
assessment and declaration, and failover may require joint effort. This can impede the
process, especially during crises when cooperation and clear communication is most
difficult. The cloud customer will also have to negotiate all the terms in the first model in
this list (private architecture, cloud service as a backup), with both the primary and backup
cloud providers. Usually, this will also be a relatively expensive methodology—the
backup provider will not be a cost bundled with other features offered by the primary
provider, and both failover and contingency operations will entail additional expenses.
(However, some of the increased costs might be offset by payments from the primary
provider if conditions of SLAs are not met because of the crisis event.) Also, data
format/system interoperability may
be a significant concern; the customer may need to perform additional activity when
porting data from one cloud provider to another in order for the data to be used properly
at the destination.
Declaration- The declaration of disaster events is a crucial step in the BC/DR process.
The cloud customer and provider must decide, prior to the contingency, who specifically
will be authorized to make this decision and the explicit process for communicating when
it has been made. Within the customer organization, this authority should be formally
assigned to a specific office or person, and there should be a deputy or backup named in
case the primary is unavailable. Both the primary and backups should receive detailed
emergency operations training that should include extensive and thorough understanding
of the organization’s specific BC/DR plan. The persons selected for this authority should
be empowered by senior management to have the full capability to declare the emergency
and initiate failover procedures.
The organization should have a warning system in place to assess impending disaster
situations. This is not always possible with certain kinds of contingencies, but some may
be anticipated with at least slight notice. The organization should be prepared to fail over
in advance of the actual crisis event in order to maintain continuity of operations. The
customer and the provider must agree on what will constitute formal notice so that failover
occurs, but they may set up a preliminary schedule of preparatory communications before
formal declaration is finalized and announced. If the cloud provider has to conduct some
failover activity, the contract should stipulate the time in which this has to be done after
notice has been received (for example, within 10 minutes of formal declaration). If
failover is automated and fully controlled by the customer, that should also be expressly
detailed in the contract. Resumption of normal activities following a contingency event
will likewise require formal notification. Early return to operations may cause an
extension of the disaster or result in the loss of data or assets. As with emergency
********** 18 **********
--- page 19 ---
declaration, return to normal operations should be tasked to a specific entity within the
customer’s organization, and the person making that decision should be fully aware of the
risks and implications inherent in it. The process for doing so should also be enumerated
within the contract.
Testing - Having backups is an admirable practice, fulfills statutory requirements, and
satisfies some legal due care obligations. However, merely creating a backup is not
sufficient. If you never try to use your backups until an actual crisis event, you have no
assurance that they will function as planned. Failover testing (and return to normal
operations) must be performed in order to demonstrate the efficacy of the plan and
procedures. It also hones the skills of the personnel involved and allows for additional
training opportunities. Of course, the testing itself constitutes an interruption in normal
service and ought not be taken lightly. There is risk and cost involved with performing
the test. Most industry guidance stipulates that such testing occur at least annually. This
amount might be increased depending on the nature of the organization and its operations.
BC/DR testing will have to be coordinated with the cloud provider. This should be
planned well in advance of the scheduled testing. Care should be taken to determine and
assign specific responsibilities to participants, and all liability for problems incurred
during the failover or in returning to normal operations should be detailed in the contract.
b. Advantages of Gap Analysis
•   Know your strengths, weakness, opportunities and threats
•   Consider Budgetary restraints
•   Understand regulatory restraints
•   Streamline all the processes
•   Achieve competitive advantage
Q 6   •   Create new training and feedback methods
[10]
CO - 3;   Disadvantages of Gap Analysis
BL- 3
•   No assessment function
•   Does not include any recommended steps
•   Exact values are not determined
•   No consideration of environmental dynamics
•   Misunderstanding or misinterpretation
•   Increases production and training costs
Q 7   a.   Interference with automatic resource allocation: Because IRM often involves preventing [10]
CO - 2;   unauthorized duplication, and the cloud necessitates creating, closing, and replicating
BL- 3
virtualized host instances (including user-specific content stored locally on the virtual
host)
Jurisdictional Conflicts The cloud extends across boundaries and borders, often in a
manner unknown or uncontrolled by the data owner, which can pose problems when
intellectual property rights are restricted by locale.
********** 19 **********
--- page 20 ---
Agent/Enterprise Conflicts IRM solutions that require local installation of software agents
for enforcement purposes might not always function properly in the cloud environment,
with virtualization engines, or with the various platforms used in a bring your own device
(BYOD) enterprise.
Mapping Identity and Access Management (IAM) and IRM Because of the extra layer of
access control (often involving content-specific access control lists, or ACLs), the IRM
IAM processes might conflict or not work properly with the enterprise/cloud IAM. A
conflict is even more possible when cloud IAM functions are outsourced to a third party,
such as a cloud access security broker (CASB).
API Conflicts Because the IRM tool is often incorporated into the content, usage of the
material might not offer the same level of performance across different applications, such
as content readers or media players. In general terms, IRM should provide the following
functions, regardless of type of content
or format:
Persistent Protection The IRM should follow the content it protects, regardless of where
that content is located, whether it is a duplicate copy or the original fi le, or how it is being
utilized. This protection should not be easy to circumvent.
Dynamic Policy Control The IRM tool should allow content creators and data owners to
modify ACLs and permissions for the protected data under their control.
Automatic Expiration Because of the nature of some legal protections of intellectual
property (described earlier in this chapter), a signifi cant amount of digital content will
not be protected in perpetuity. The IRM protections should cease when the legal
protections cease. Conversely, licenses also expire; access and permissions for protected
content should likewise expire, no matter where that content exists at the end of the license
period.
Continuous Auditing The IRM should allow for comprehensive monitoring of the
content’s use and access history.
Replication Restrictions Much of the purpose of IRM is to restrict illegal or unauthorized
duplication of protected content. Therefore, IRM solutions should enforce these
restrictions across the many forms of copying that exist, to include screen-scraping,
printing, electronic duplication, email attachments, and so on.
API Conflicts Because the IRM tool is often incorporated into the content, usage of the
material might not offer the same level of performance across different applications, such
as content readers or media players. In general terms, IRM should provide the following
functions, regardless of type of content
or format:
Persistent Protection The IRM should follow the content it protects, regardless of where
that content is located, whether it is a duplicate copy or the original fi le, or how it is being
utilized. This protection should not be easy to circumvent.
********** 20 **********
--- page 21 ---
Dynamic Policy Control The IRM tool should allow content creators and data owners to
modify ACLs and permissions for the protected data under their control.
Automatic Expiration Because of the nature of some legal protections of intellectual
property (described earlier in this chapter), a signifi cant amount of digital content will
not be protected in perpetuity. The IRM protections should cease when the legal
protections cease. Conversely, licenses also expire; access and permissions for protected
content should likewise expire, no matter where that content exists at the end of the license
period.
Continuous Auditing The IRM should allow for comprehensive monitoring of the
content’s use and access history.
Remote Rights Revocation The owner of the rights to specific intellectual property should
have the ability to revoke those rights at any time; this capability might be used as a result
of litigation or infringement.
Q 7   b. A two-phased approach: an Emergency Response for the immediate crisis and a Long- [10]
CO - 2;   Term Strategic Overhaul to prevent future exposure.
BL- 3
Phase 1: Emergency Response to the Zero-Day Vulnerability
This phase is about speed, precision, and minimizing downtime.
Step 1: Immediate Assessment & Prioritization
Action: Immediately scan the entire cloud environment using a vulnerability management
tool (e.g., Qualys, Tenable, or cloud-native tools like AWS Inspector) to identify all
instances affected by this specific zero-day.
Output: A prioritized list of assets, focusing first on internet-facing systems and servers
handling sensitive client data.
Step 2: Rapid Patch Testing & Deployment
Action:
1. Test: Quickly deploy the patch to a isolated, non-production environment that mirrors
the live setup. Run a critical smoke test to ensure core trading platform functionality
remains stable.
2. Deploy: Bypass the monthly maintenance window. Use an automated deployment
service to roll out the patch.
Cloud-Native Tooling: Use AWS Systems Manager (SSM) or Azure Automation Update
Management. These services can target server groups and apply patches across the entire
estate in a controlled manner.
Process: Deploy to a small, non-critical batch of servers first (Canary Deployment),
monitor for minutes, and then proceed to the entire fleet.
Step 3: Verification and Monitoring
Action: Re-scan the patched systems to confirm the vulnerability is remediated. Increase
monitoring and alerting on these systems for any anomalous behavior that might indicate
exploitation attempts or instability caused by the patch.
********** 21 **********
--- page 22 ---
Phase 2: Long-Term Strategic Overhaul of Patch Management
This phase transforms patch management from a reactive, high-risk activity to a proactive,
automated control.
Step 1: Implement a Centralized Patch Management Policy
Action: Define and enforce a clear policy using a cloud-native tool. The policy should
categorize systems based on criticality:
Critical/Security Patches: Deploy automatically within 24-48 hours of release.
All Other Patches: Deploy during a defined, frequent maintenance window (e.g., weekly).
Step 2: Automate the Entire Patch Workflow
Action: Leverage cloud automation to create a "hands-off" pipeline.
1.   Assessment: Use AWS Systems Manager Patch Manager or Azure Update
Management to automatically scan for missing patches on a daily basis.
2. Approval & Deployment: Configure the system to auto-approve critical security
patches and deploy them according to the policy. This eliminates the human delay that
creates exposure to windows.
Step 3: Leverage Immutable Infrastructure Principles
Action: For the highest level of consistency and security, shift from patching existing
servers to replacing them.
Process: Use a tool like Hashicorp Packer to create a new, patched "Golden Image" of
your server. Then, automatically deploy this image to replace old, vulnerable instances.
Benefit: This ensures every deployment is in a known, secure state and eliminates
configuration drift. Services like AWS Auto Scaling Groups can seamlessly roll out the
new instances.
Step 4: Establish Continuous Compliance Monitoring
Action: Implement a Cloud Security Posture Management (CSPM) tool like AWS
Security Hub or Azure Security Center.
Function: These tools continuously monitor your environment, not just for vulnerabilities,
but also for compliance with your own patch management policy. They will generate
alerts if any server is found to be non-compliant, providing real-time assurance.
********** 22 **********
````
