# DevSecOps: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e43e6d3778c0

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CyberSecurity_7010/DevSecOps/ANS_DevSecOps(702IT0E031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2025
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: DevSecOps
Date: 25 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure on the right-hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
Q 1   Answer briefly:
a.   Artifacts of Scrum methodology.
▪   Product Backlog: A prioritized list of user stories, features, and enhancements. It
represents the requirements and desired functionality of the product.
▪   Sprint Backlog: A subset of the product backlog containing the selected user stories
and tasks that the Development Team commits to completing during the sprint.
▪   Increment: At the end of each sprint, the Development Team delivers a potentially
shippable product increment. It is a working and potentially releasable version of the
software that adds value to the product.
Ceremonies of Scrum methodology.
▪   Sprint Planning: The Product Owner and Development Team collaborate to determine
CO - 1;   [05]
BL- 2   which product backlog items to work on during the upcoming sprint. The work is
broken down into tasks and estimated.
▪   Daily Scrum: A daily stand-up meeting where the Development Team synchronizes
their work. Each member shares progress, discusses challenges, and plans for the day.
▪   Sprint Review: At the end of each sprint, the Development Team presents the
completed work to stakeholders and gathers feedback. The Product Owner reviews
and adjusts the product backlog accordingly.
▪   Sprint Retrospective: A reflection meeting held by the Development Team at the end
of each sprint to identify what went well, areas for improvement, and actionable steps
to enhance processes and teamwork.
CO - 2;   b.   Secret sprawl   [05]
BL – 2
********** 1 **********
--- page 2 ---
•   Secrets sprawl is when an organization stores secrets throughout the network, without
using a solution to organize, manage and secure them.
• Widespread adoption of SaaS apps and cloud-native development models have
dramatically increased the number of secrets organizations have, while decentralizing
their storage.
•   In this type of environment, DevSecOps teams lack the visibility and uniform
management policies they need to get their secrets under control, which expands the
organization’s attack surface and increases the risk of data breach.
Secret rotation
1. Automatic Updates
Secrets (passwords, keys, tokens) are automatically changed at scheduled intervals without
manual intervention.
2. Shortened Risk Window
Regular rotation limits damage from compromised credentials by making stolen secrets
quickly expire.
3. Versioned Transition
New secrets are deployed alongside old ones during a grace period to prevent application
downtime.
4. Compliance Requirement
Mandated by security standards (PCI-DSS, HIPAA, SOC 2) to maintain certification and
audit trails.
5. Centralized Management
Enabled by secrets management tools (HashiCorp Vault, AWS Secrets Manager) that
handle the entire rotation lifecycle.
Secret as code
1. Version-Controlled & Auditable
Secrets are stored in encrypted files within Git, providing full history of who changed
what and when.
2. Automated Deployment
Secrets are deployed automatically through CI/CD pipelines, eliminating manual handling
and human error.
3. Environment Consistency
The same automated process applies secrets consistently across development, staging, and
production environments.
4. Developer-Friendly Access
********** 2 **********
--- page 3 ---
Developers can safely work with encrypted secrets in their workflows without accessing
actual credentials.
5. Integrated Security
Combines encryption tools (SOPS, Vault) with existing development tools for end-to-end
secret management.
c. Main characteristics of containerd
▪   Execution and supervision of containers
▪ Image distribution
CO -3;   [05]
BL – 2   ▪ Network interface management
▪   Local storage
▪   Native plumbing API
d. The application performance metrics used to monitor applications in Docker containers.
▪   Metrics that refer to the performance of the applications running inside Docker
containers. Some examples are:
▪ Response time: The time it takes for the containerized application to respond to a
CO - 3;   request. Tracking response time can help identify performance issues and ensure that [05]
BL- 2
the application is responsive to end users
▪ Request rate: The number of requests being handled by the containerized application
per second
▪   Error rate: The number of errors encountered by the containerized application
a.   ▪   Culture: It emphasizes fostering a collaborative and transparent work environment
where teams collaborate, share knowledge, and take ownership. A culture of trust,
continuous learning, and innovation promotes business agility.
▪   Collaboration: Collaboration is key to breaking down silos and promoting cross-
functional teamwork. Collaboration between development, operations, quality
assurance, and other stakeholders facilitates communication, information sharing, and
decision-making. Collaborative teams can respond faster to changes and work
together towards common goals.
Q 2   ▪ Communication: Effective communication   is   vital for successful DevOps
[10]
CO - 1;   implementation. Clear and open communication channels between team members,
BL- 3
departments, and stakeholders ensure shared understanding of goals, requirements,
and challenges. Good communication enhances alignment and enables timely and
effective decision-making.
▪ Continuous Integration: Continuous Integration (CI) is a practice that involves
frequently integrating code changes into a shared repository. CI helps identify
integration issues early on, ensures code quality through automated testing, and
maintains a deployable codebase. It promotes agility by reducing risks and enabling
faster and more frequent software releases.
********** 3 **********
--- page 4 ---
▪ Continuous Delivery: Builds upon CI by automating the process of releasing software
to production environments. CDs ensure that the software is always in a deployable
state and enable organizations to deliver changes rapidly and reliably. It facilitates
business agility by shortening the time from idea to deployment.
▪ Continuous Deployment: Continuous Deployment extends the concept of Continuous
Delivery by automatically deploying the software to production after passing
predefined quality   criteria.   It minimizes manual intervention and enables
organizations to release new features or fixes quickly, enhancing business agility and
responsiveness to market demands.
▪ Continuous Monitoring: Continuous Monitoring involves real-time monitoring of
software applications, infrastructure, and user experience. It provides insights into
system health, performance, and user behavior. Continuous monitoring helps identify
issues, detect anomalies, and optimize system performance, ensuring business agility
by proactively addressing problems and improving user satisfaction.
b.   Benefits of a DAST Tool
1. Finds Runtime & Environment-Specific Flaws: DAST tests the running application
from the outside, just like a real attacker. It can find vulnerabilities that only exist in a
live, configured environment, such as server misconfigurations, weak TLS/SSL settings,
and issues with authentication mechanisms that SAST (which only looks at source code)
cannot detect.
2. Identifies Business Logic Flaws: This is the primary weakness of SAST. DAST tools
can be configured to mimic complex, multi-step user workflows to uncover flaws in the
application's logic—exactly like the breach in the scenario. For example, it can test if a
user can bypass a payment step or access another user's data by manipulating the flow.
3. Provides a Hacker's-Eye View: It assesses the application without access to the source
Q 2   code (a "black-box" test). This gives a true picture of the application's external attack
CO - 2;   surface and identifies what an attacker can actually exploit, providing a realistic risk [10]
BL- 3   assessment.
4. Detects Vulnerabilities in All Components: SAST only analyzes your custom code.
DAST tests the entire deployed application, including all third-party components,
libraries, frameworks, and the web server itself, which may have their own vulnerabilities.
5. Validates Overall Security Posture: It helps verify that all the secure coding practices
identified by SAST and code reviews have been implemented correctly in the final,
compiled application and are effectively protecting against real-world attacks.
Limitations of a DAST Tool
1. Limited Code Coverage & Inability to Pinpoint Root Cause: DAST can only test the
parts of the application it can find and interact with. If a feature is hidden behind a
complex login, it might be missed. Furthermore, it can report that a vulnerability exists
but not where in the source code the flaw is, making it harder for developers to fix.
********** 4 **********
--- page 5 ---
2. Resource-Intensive and Can Impact Performance: DAST tools work by aggressively
fuzzing the application with thousands of malicious requests. Scanning a production
system during peak hours could slow it down or even cause a denial-of-service, requiring
dedicated test windows and environments.
3. Higher Rate of False Positives: DAST can sometimes report vulnerabilities that are
not actually exploitable because it lacks the application's internal context. This requires
manual security expertise to triage and verify findings, which can be time-consuming.
4. Limited Scope to Discoverable Content: The tool's effectiveness is limited to what it
can "crawl" or discover. Applications with complex, non-standard interfaces (like heavy
use of JavaScript) may require significant manual configuration to ensure complete test
coverage.
5. Later-Stage Feedback ("Shift-Right"): Unlike SAST, which provides feedback early
in the development cycle ("shift-left"), DAST typically finds issues after the application
is built and deployed. This means fixes can be more costly and time-consuming than if
they were caught during the coding phase.
a.   Primary Purpose
OWASP Dependency Check is a Software Composition Analysis (SCA) tool. Its primary
purpose is to automatically identify and report on known vulnerabilities within a project's
third-party dependencies (libraries, frameworks) by cross-referencing them against
databases of published Common Vulnerabilities and Exposures (CVEs).
Key Benefits of Integrating it into the CI/CD Pipeline
1. Proactive Vulnerability Discovery: It automatically scans all dependencies on every
build, catching newly discovered vulnerabilities as soon as they are added to the National
Vulnerability Database (NVD). This prevents the scenario where a team is unaware of a
critical vulnerability, as described in the audit.
2. Enforces Security Gates: It can be configured to break the build or cause the pipeline
Q 3
to fail if vulnerabilities above a certain severity threshold (e.g., Critical or High) are [10]
CO - 2;
BL- 3   found. This ensures that no new code with known critical flaws can be deployed, enforcing
a "secure by default" pipeline.
3. Creates an Auditable Software Bill of Materials (SBOM): It generates a detailed report
listing all dependencies and their associated vulnerabilities. This provides a continuous,
up-to-date SBOM, which is crucial for compliance, audits, and rapid incident response.
4. Shifts Security Left: It brings security feedback directly to developers in their natural
workflow. Developers receive immediate feedback on their code commits, allowing them
to fix vulnerable dependencies early in the development lifecycle when it is fastest and
cheapest, rather than after a production deployment.
5. Cost-Effective and Open Source: As a free and open-source tool, it provides a powerful
security control without a direct financial cost for licensing, making it an easier
********** 5 **********
--- page 6 ---
justification for the business and lowering the barrier to entry for implementing Software
Composition Analysis.
Potential Limitations in the CI/CD Pipeline
1. False Positives and Noise: The tool may report vulnerabilities in a dependency that
your application does not actually use in an exploitable way (e.g., the vulnerable function
is never called). This can create "alert fatigue" and waste developer time on triaging non-
issues.
2. Lag Time in Vulnerability Data: There can be a delay (hours to days) between a CVE
being published and it being fully analysed and added to the NVD database that
Dependency Check uses. This creates a brief window where a new, critical vulnerability
would not be detected.
3. Performance Impact on Build Times: The scanning process, especially for large
projects with hundreds of dependencies, can add several minutes to the build time. This
can slow down the overall CI/CD pipeline, potentially impacting developer productivity
and the speed of delivery.
4. Limited to Known Vulnerabilities: It can only find vulnerabilities that have been
assigned a CVE and published to its data sources. It cannot find vulnerabilities in
dependencies that are unknown to the public (zero-days) or malicious packages that have
not yet been identified as malicious.
5. Requires Tuning and Maintenance: To be effective and not overly noisy, the tool
requires initial configuration and ongoing maintenance. This includes tuning suppression
files for false positives, updating the tool itself, and ensuring its local vulnerability
database is kept up to date, which adds administrative overhead.
b.   ▪ Using secrets:
▪ Do not storing objects with sensitive data like passwords, SSH keys, or OAuth tokens
in the clear.
▪   Firewall ports:
▪   This security practice is frequently used since it is not advisable to expose a port that
does not need to be exposed. It is best to define the port’s exposure to prevent this
from happening. The first thing you should do is check the existence of some interface
Q 3   or define an IP to link the service; for example, the localhost interface 127.0.0.1. Some
[10]
CO - 3;   processes are opening so many ports on all interfaces that they should rather have a
BL- 3
public access firewall. Although they only allow purely confidential information, they
also allow you direct access to your set of computers.
▪   Restrict the Docker pull command:
▪ Docker is a resource that can sometimes be uncontrolled by the ease of access it has.
That is, anyone with access to the Kubernetes API or Docker connector can obtain the
image they want, generating traffic from infected images or serious security problems
for Kubernetes. Many clusters have also become a network of Bitcoin miners.
********** 6 **********
--- page 7 ---
▪ Although it is a problem that seems not to be solved, the Image Policy plugin can
significantly improve that situation, connecting directly with the Docker API. This
plugin imposes a series of strict security rules that reflect a black and white list of
images that can be extracted. Another solution is to use the Image Policy Webhook
through Admission Controller, which intercepts all image extractions and takes care
of security just like the plugin mentioned earlier.
a. Problem 1: Protecting the Public-Facing Website
a) Recommended Tool: Cloudflare
b) Justification: Cloudflare is a cloud-based service that acts as a reverse proxy and a Web
Application Firewall (WAF). It is specifically designed to protect websites from DDoS
attacks by absorbing and scrubbing malicious traffic across its global network before it
reaches DataSecure's origin server. It also mitigates layer 7 attacks (like SQL injection)
through its WAF rulesets.
c) Implementation Consideration: Configuration Complexity. Simply proxying traffic
through Cloudflare is not enough. The security team must actively configure and tune the
WAF rules, DDoS protection settings, and rate-limiting policies. Incorrect configuration
could lead to blocking legitimate customer traffic (false positives) or leaving attack
vectors open.
Problem 2: Securing the Remote Workforce's Endpoints
a) Recommended Tool: Syxsense
Q 4   b) Justification: Syxsense is a unified endpoint management (UEM) and security platform.
[10]
CO - 2;   It directly addresses the inconsistent security posture by allowing DataSecure to enforce
BL- 3
security policies (like disk encryption, firewall settings) across all devices, regardless of
ownership (BYOD or corporate). It provides continuous vulnerability scanning and can
automatically deploy patches to operating systems and third-party applications, closing
security gaps that attackers exploit.
c) Implementation Consideration: User Privacy & Compliance. For personally-owned
(BYOD) devices, DataSecure must carefully define and communicate which aspects of
the device will be monitored and controlled by Syxsense. They need a clear acceptable
use policy to respect user privacy and comply with data protection regulations, ensuring
they only manage corporate data and applications, not personal user data.
Problem 3: Monitoring On-Premise Server Infrastructure
a) Recommended Tool: Nagios
b) Justification: Nagios is a powerful, open-source infrastructure monitoring tool. It is
designed to continuously monitor the health, performance, and availability of on-premise
servers, services, and network protocols. It can alert the IT team before a full outage
********** 7 **********
--- page 8 ---
occurs—for example, by warning of high CPU load, low disk space, or a critical service
stopping—allowing for proactive intervention and reducing unpredictable downtime.
c) Implementation Consideration: Administrative Overhead. Nagios requires significant
manual setup and ongoing maintenance to configure monitors (checks) for all critical
services and to fine-tune alert thresholds. Without a dedicated administrator, the team
risks being flooded with false alarms or missing critical alerts, which can lead to "alert
fatigue" and defeat the purpose of the tool.
b.
Q 4
[10]
CO - 3;
BL- 3
The Docker Daemon is the persistent background process that manages Docker objects
such as images, containers, networks, and volumes. It is responsible for the core lifecycle
of a container, including:
1. Pulling images.
2. Creating, starting, stopping, and deleting containers.
3. Managing network configuration and port bindings.
a. DevSecOps Maturity Model provides a structured approach to assess an organization's
DevSecOps capabilities and maturity. It helps organizations identify gaps in their
security practices and define a roadmap for improvement. The model typically consists
of multiple levels, from ad hoc security practices to fully integrated and mature
DevSecOps processes.
Q 5
[10]
CO - 1;
BL- 3
********** 8 **********

[Text in pictures on this page, read by OCR]
Shift Left" to bake in security right from the beginning |

Source
Adhoc

Practice

Continuo' Artifact

Continuous Continuous
Monitoring Improvement

Code

Integration Management
Management

Local Development, Version Control Build per commit, Version builds, From Periodic Dashboards, 4 Incident review,
‘Manual testing -> Peer Review Continuous testing, Dependency release to golden signals Blameless
Unit testing & ‘Small batch ‘management, Any time release SRE, Dora 4KM_ postmortem,

Automated testing Signed builds
--- page 9 ---
▪ Reduced Costs: DevSecOps enables any vulnerabilities identified to be remediated
quickly, shortening the development lifecycle and eliminating issues before they arise
in production. More efficient use of resources reduces development costs, and
reduction of post-launch issues results in operational savings.
▪   Delivery Velocity: By integrating security into the software development lifecycle,
application builds progress more quickly. Vulnerabilities can be identified and
remediated as they are introduced by the teams closest to the code at that lifecycle
stage. Making security part of the workflow instead of a quality gate at the end of the
process increases product confidence and enables a more efficient release schedule.
▪ Improved Security: Integrating security into the SDLC results in software that is
secure at every development stage, as well as secure in transit between deployment
environments thanks to CI/CD pipeline scanning tools. Better collaboration and
transparency between teams reduces risk, as well as making any risks identified easier
to mitigate.
▪   Better Customer Experience: DevSecOps delivers software that is more secure and of
better quality, with shorter development processes resulting in more frequent release
and updates, which deliver improved value. Customers will experience and report
fewer issues, and feel confident that your products are efficient, safe, and secure.
b. Rancher is an open-source platform that simplifies the management of Kubernetes clusters
in production environments. Developed by Rancher Labs, it provides a comprehensive
suite of tools to deploy, manage, and monitor Kubernetes clusters across multiple cloud
providers or on-premises infrastructure.
Key Features of Docker Rancher:
1. Multi-Cluster Management: Rancher allows users to manage multiple Kubernetes
clusters from a single pane of glass. This capability is particularly useful for organizations
that operate hybrid or multi-cloud environments.
2. User Management and RBAC: Rancher offers built-in support for role-based access
Q 5   control (RBAC) and user management, enabling fine-grained control over who can access
and manage specific resources within Kubernetes clusters.   [10]
CO - 3;
BL- 3   3. Application Catalog: Rancher includes an application catalog that provides access to a
wide range of pre-configured, production-ready applications. These can be deployed
easily onto Kubernetes clusters with minimal configuration.
4. Cross-Platform Support: Rancher can be used to manage Kubernetes clusters across
different environments, including on-premises data centers, public clouds (AWS, Azure,
GCP), and edge locations.
5. Simplified Kubernetes Operations: Rancher abstracts much of the complexity
associated with Kubernetes, making it easier for DevOps teams to manage containerized
applications. It provides tools for cluster provisioning, upgrades, monitoring, and logging,
all within an intuitive web interface.
********** 9 **********
--- page 10 ---
Use Cases:
Rancher is well-suited for organizations looking to simplify Kubernetes management,
especially in multi-cluster, multi-cloud environments. It helps reduce the operational
overhead associated with running Kubernetes at scale and provides enterprise-grade
features like centralized security, observability, and compliance management.
a.   ▪   Git is a version control system used for tracking changes in computer files. It is
generally used for source code management in software development.
▪   Git is used to tracking changes in the source code
▪ The distributed version control tool is used for source code management
▪   It allows multiple developers to work together
▪   It supports non-linear development through its thousands of parallel branches
Q 6
[10]
CO - 2;
BL- 3
The GIT workflow is divided into three states:
▪ Working directory - Modify files in your working directory
▪   Staging area (Index) - Stage the files and add snapshots of them to your staging area
▪ GIT directory (Repository) - Perform a commit that stores the snapshots permanently
to your GIT directory. Checkout any existing version, make changes, stage them and
commit.
b.   ▪ Swarm is the solution proposed by Docker to solve tasks related to orchestrating and
planning containers through many servers.
▪ Swarm comes bundled with the Docker engine from version 1.12.0 and offers many
Q 6   advanced integrated features, like service discovery, load balancing, scaling, and
security.   [10]
CO - 3;
BL- 3   ▪ Swarm follows Docker’s philosophy of focusing on the simplicity and experience of
the developer, and we could say that it’s easier to use than other solutions like
Kubernetes. This solution it’s not as powerful and not adopted by many companies,
cloud providers, or by the community.
********** 10 **********

[Text in pictures on this page, read by OCR]
clone operation

* edit, add, move files

update operation

Modify working copy

status and diff operation
Review changes

commit and push operation

push operation

Commit changes

amend and push operation

push operation

Review changes
--- page 11 ---
▪ Swarm master: Is responsible for the entire cluster and manages the resources of
several Docker hosts. In this model, services are orchestrated instead of running
container commands.
▪ Swarm worker nodes: Each node of the cluster must be accessible by the master. Each
node executes an agent so that it registers the Docker daemon referenced, monitors,
and updates the backend with the node state. Nodes can be distributed on premises or
in a public cloud provider.
▪ Swarm discovery: By default, Swarm uses a discovery service based on Docker Hub,
using a token to discover the nodes that are part of a cluster. It also supports other
discovery services like etcd https://etcd.io, Consul https://www.consul.io, and
Zookeeper https://zookeeper.apache.org.
▪ Swarm strategy: Swarm has multiple strategies for the classification of nodes. When
a new container is executed, the Swarm decides to locate it in the node with the
highest-ranking calculated for its chosen strategy.
▪ Swarm networking: It is fully compatible with the new overlay network model of
Docker.
a.   1. Feature: Pipeline-as-Code (using Jenkinsfile)
Problem Solved: "Fragmented and manual process," "long release cycles," and lack of
standardization ("it works on my machine").
Explanation & Example: This feature allows the entire CI/CD pipeline (build, test,
deploy) to be defined as code in a text file (`Jenkinsfile`) stored in the same repository as
the application. This makes the process repeatable, version-controlled, and transparent.
Q 7
This eliminates manual handoffs and ensures every change follows the same path to [10]
CO – 2;
BL- 3   production.
2. Feature: Extensive Plugin Ecosystem
Problem Solved: The need to integrate with diverse tools (e.g., version control, testing
frameworks, deployment platforms) without building custom integrations.
Explanation & Example: Jenkins has over 1,800 plugins that provide pre-built integrations
for almost every tool in the modern DevOps stack.
********** 11 **********
--- page 12 ---
Example: Company can use the GitHub plugin to automatically trigger builds on every
code commit. They can use the JUnit plugin to automatically capture test results and report
on trends, and the Kubernetes plugin to dynamically provision build agents as needed.
This allows them to create a sophisticated, integrated pipeline without writing complex
integration code from scratch.
b) Advantage and Challenge
Significant Advantage over Cloud-Native Services: Vendor Neutrality and Flexibility.
Explanation: Unlike cloud-native CI/CD services (e.g., AWS CodePipeline, Azure
DevOps) that are tightly coupled to their respective cloud platforms, Jenkins is vendor-
agnostic. It can orchestrate workflows that span multiple clouds (AWS, Azure, GCP) and
on-premise infrastructure with equal ease. This prevents Company from being "locked in"
to a single cloud provider and gives them unparalleled flexibility to adapt their pipeline
to any technology.
Challenge to Anticipate: Operational Overhead.
Explanation: Jenkins is a self-managed tool. Company will be responsible for installing,
securing, scaling, updating, and maintaining the Jenkins server(s) and its plugins. This
requires dedicated operational effort and expertise, unlike a fully managed cloud service
where the provider handles the underlying infrastructure. Failure to manage this properly
can lead to security vulnerabilities or downtime.
b.   ▪ Requirements and Design: Security considerations should be integrated into the initial
requirements and design phases. This involves identifying potential security threats,
defining security controls, and establishing security requirements that the software
must meet.
▪   Threat Modeling: A threat model is created to assess potential security risks and
vulnerabilities specific to the software being developed. This involves identifying
potential attackers, their motivations, and potential attack vectors.
▪   Secure Coding: Developers follow coding practices that prioritize security. This
includes using secure coding guidelines and best practices, avoiding common
Q 7
vulnerabilities such as injection attacks (SQL, code, etc.), cross-site scripting (XSS), [10]
CO – 1;
BL- 3   and more.
▪   Static Analysis and Code Review: Automated tools and manual code reviews are
conducted to analyze the code for vulnerabilities, weaknesses, and deviations from
secure coding standards. This stage helps catch issues before they make it to the
testing phase.
▪ Dynamic Analysis and Testing: The software is tested in dynamic environments to
identify vulnerabilities that might only manifest during runtime. This includes
security testing techniques like penetration testing, vulnerability scanning, and
security-focused testing methodologies.
********** 12 **********
--- page 13 ---
▪   Security Testing: Rigorous security testing techniques are applied, such as fuzz
testing, penetration testing, and vulnerability assessments. These tests identify
potential vulnerabilities and weaknesses in the software that could be exploited by
attackers.
▪   Secure Deployment: Security considerations continue during the deployment phase.
Properly configuring servers, databases, and other components is essential to ensure
that the software operates securely in a production environment.
▪ Continuous Monitoring and Maintenance: Once the software is deployed, ongoing
monitoring and maintenance are crucial. Regular security updates, patches, and
vulnerability assessments are performed to ensure that the software remains secure as
new threats emerge.
▪   Secure Updates and Patch Management: When vulnerabilities are identified post-
release, they need to be patched promptly. A well-defined process for handling
updates and patches ensures that security issues are addressed in a timely manner.
▪   Education and Training: Developers and other stakeholders involved in the SDLC
need to be educated about secure coding practices, common vulnerabilities, and the
importance of security. Regular training helps create a security-aware development
team.
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper cced21be25d1

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CyberSecurity_7010/DevSecOps/ANS_DevSecOps(702IT0E031)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: DevSecOps
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure on the right-hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
Q 1   Answer briefly:
a.   Advantages of Agile Methodology
▪   It responds to the needs and changes more adaptively and suitably
▪   Fixing the errors at the early phase of development helps the process to be more
cost-efficient.
▪   It enhances the quality of the product and thus makes them error-free.
▪   It permits direct communication among the people who are involved in the Software
Development project.
CO - 1;   ▪   It is highly recommended for the big and long-term projects.   [05]
BL- 2
▪   Also, the Agile model needs only minimum resources and this is very easy to handle
Disadvantages of Agile Methodology.
▪   It is highly dependent on the customer’s needs.
▪   It is not easier to predict the effort and time of the bigger projects.
▪   It is not preferable for complex projects.
▪   It struggles more with document efficiency.
▪   It helps in maintaining the risks.
b. Unique features of GIT
1. Delta Compression
Concept: Delta compression is a method Git uses to save space by storing changes
CO - 2;   [05]
BL – 2   between file versions rather than the entire file contents. When you commit a change, Git
calculates the difference (or "delta") between the new version of a file and its previous
version, and it stores only that difference.
********** 1 **********
--- page 2 ---
How It Works: Instead of saving entire file snapshots for each commit, Git stores just the
changes made since the last commit. If a file is changed only slightly, the delta is small,
leading to significant storage savings.
Benefits: This process reduces the amount of data Git needs to store, making repositories
smaller and more efficient. It is especially useful in large projects with many small
changes.
2. Shallow Cloning
Concept: Shallow cloning is a way to clone a Git repository without downloading the
entire history. It allows users to clone only the most recent commits, reducing the amount
of data transferred and speeding up the cloning process.
How It Works: When performing a shallow clone, Git only retrieves the most recent
commit(s) rather than the entire commit history. This is achieved using the --depth
parameter, where you specify the number of commits you want.
Use Cases: Shallow cloning is particularly useful in CI/CD pipelines where the full history
is not necessary, or when you need to quickly clone a large repository for a specific task.
Example: git clone --depth 1 <repository-url> clones the repository with only the latest
commit.
3. Object Storage Optimization
Concept: Object storage optimization in Git refers to the way Git efficiently stores and
manages objects (like commits, trees, and blobs) within the repository to save space and
improve performance.
How It Works: Git stores all files and their metadata as objects in a .git/objects directory.
Over time, Git performs optimizations like packing these objects into a single pack file,
applying delta compression, and garbage collection to remove unnecessary objects.
Garbage Collection: Git runs a garbage collection process (git gc) that compresses and
removes unreachable objects, effectively reducing the size of the repository. This process
also includes repacking objects to optimize storage and access speed.
Benefits: These optimizations ensure that the repository remains fast and efficient, even
as it grows over time.
c.   Tasks performed by Docker container orchestrator
▪ Deployment and raised automatic container-based services
CO -3;   ▪   Self-scaling and load balancing   [05]
BL – 2
▪   Control of the “health” of each container
▪   Secrets management in parameters and configurations
d. The Kubernetes monitoring allows us to
▪ Ensure resources are consumed optimally by teams or applications
CO - 3;   ▪   Automatically utilize new resources when a new node joins a cluster   [05]
BL- 2
▪ Redeploy workloads to available nodes when hosts go down
▪   Provisioning updates and rollbacks more efficiently
********** 2 **********
--- page 3 ---
a. Recommended DevOps Principles & Solutions:
1. Implement Continuous Integration & Continuous Delivery (CI/CD)
Problem Addressed: The 3-month "big bang" release cycle.
Solution: Automate the build, test, and deployment process.
Outcome: Enables frequent, small, low-risk releases. Bugs are caught early and fixed
immediately, reducing the volume of issues at release and eliminating overnight
firefighting.
2. Foster a Culture of Shared Responsibility & Blameless Collaboration
Problem Addressed: The siloed teams and culture of conflict.
Solution: Break down silos by creating cross-functional teams where both Dev and Ops
Q 2
are jointly accountable for the entire software lifecycle—from feature development to [10]
CO - 1;
BL- 3   stability in production.
Outcome: Replaces blame with collaboration. Developers gain awareness of operational
concerns, leading to more stable code, while Ops is involved earlier in the process.
3. Embrace Proactive Monitoring & Feedback Loops
Problem Addressed: Reacting to customer complaints and bugs after release.
Solution: Implement application performance monitoring (APM) and centralized logging
to gain real-time visibility into application health and user experience in production.
Outcome: Provides immediate feedback on new releases. Teams can detect and often auto-
remediate issues before users are affected, transforming a reactive posture into a proactive
one.
b.   Static Application Security Testing (SAST) offers several benefits for organizations
looking to improve the security of their software applications throughout the development
lifecycle. Here are some key benefits of SAST testing:
1. Early Detection of Vulnerabilities: SAST analyzes the source code of an application
statically, enabling the detection of security vulnerabilities and coding errors early in the
development process. By identifying issues at the source code level, SAST helps prevent
security vulnerabilities from propagating and becoming more costly to fix later in the
Q 2   software lifecycle.
CO - 2;   2. Shift-Left Security: SAST promotes shift-left security practices by integrating security [10]
BL- 3   testing into the early stages of the development lifecycle. By identifying and addressing
security vulnerabilities during the development phase, SAST enables organizations to
address security issues proactively and reduce the risk of security breaches in production.
3. Automated Security Testing: SAST automates the process of security testing by
scanning the source code or compiled bytecode of an application for potential security
vulnerabilities and coding errors. This automation reduces the manual effort required for
security testing, accelerates the testing process, and enables developers to focus on
remediation activities.
********** 3 **********
--- page 4 ---
4. Continuous Integration and Delivery (CI/CD) Integration: SAST seamlessly integrates
with CI/CD pipelines, allowing organizations to incorporate security testing into their
automated build and deployment processes. By integrating SAST into CI/CD pipelines,
organizations can ensure that security testing is performed consistently and continuously
throughout the software development lifecycle.
5. Comprehensive Coverage: SAST provides comprehensive coverage of security
vulnerabilities and coding errors by analyzing the entire source code of an application,
including all its components such as scripts, libraries, and configuration files. This
comprehensive analysis enables SAST to identify a wide range of security issues,
including common vulnerabilities such as SQL injection, cross-site scripting (XSS), and
insecure authentication.
6. Customizable Rulesets: SAST offers customizable rulesets or rule engines that allow
organizations to define their own security rules and policies. Organizations can configure
SAST to enforce coding standards, best practices, and security guidelines specific to their
industry or regulatory requirements. This customization enables organizations to tailor
SAST analysis to their unique security requirements and compliance mandates.
7. Reduced Security Risks: By identifying and remediating security vulnerabilities early
in the development process, SAST helps organizations reduce the risk of security breaches
and data breaches. By addressing security issues before they are deployed to production,
organizations can minimize the impact of security incidents on their business operations,
reputation, and bottom line.
8. Cost Savings: SAST helps organizations save costs associated with security
vulnerabilities by addressing issues early in the development process when they are less
expensive to fix. By reducing the number of security vulnerabilities that make it into
production, organizations can avoid the costs associated with security incidents,
regulatory fines, and reputational damage.
Overall, Static Application Security Testing (SAST) offers several benefits for
organizations looking to improve the security of their software applications. By detecting
security vulnerabilities early in the development process, automating security testing,
integrating with CI/CD pipelines, providing comprehensive coverage, offering
customizable rulesets, reducing security risks, and saving costs, SAST helps organizations
enhance the security posture of their applications and mitigate the risk of security
breaches.
While Static Application Security Testing (SAST) offers numerous benefits, it also has
several limitations that organizations should be aware of. Here are some common
limitations of SAST testing:
1. Limited Scope: SAST analyzes the source code or compiled bytecode of an application
statically, which means it only examines the application's codebase and does not consider
runtime behavior or environment-specific configurations. As a result, SAST may miss
********** 4 **********
--- page 5 ---
security vulnerabilities that can only be detected through dynamic testing or runtime
analysis, such as vulnerabilities introduced by third-party libraries, configuration errors,
or security misconfigurations in the deployment environment.
2. False Negatives: Conversely, SAST tools may also produce false negative findings,
where genuine security vulnerabilities are overlooked or not detected by the analysis.
False negatives can occur due to limitations in the SAST tool's detection capabilities,
incomplete code coverage, or complex code patterns that are not effectively analyzed.
False negatives can leave organizations vulnerable to security risks that go undetected and
unaddressed.
3. Code Quality vs. Security: SAST tools primarily focus on identifying security
vulnerabilities and coding errors, often at the expense of code quality and maintainability
considerations. As a result, SAST may produce findings that prioritize security concerns
over other aspects of software development, such as code readability, performance
optimization, or architectural design principles. This narrow focus on security may lead
to tensions between security and development teams, particularly if security findings
require significant code changes or refactoring efforts.
4. Limited Language Support: SAST tools may have limited support for programming
languages, frameworks, and technologies, which can restrict their applicability to specific
projects or development environments. Some SAST tools excel in analyzing certain
languages or platforms but struggle with others, leading to disparities in coverage and
effectiveness.
5. High False Positive Rate: SAST tools often produce a high volume of findings, many
of which may be false positives or low-priority issues that do not pose significant security
risks. Sorting through and prioritizing these findings can be challenging, especially in
large codebases or complex applications. High false positive rates can lead to alert fatigue,
where security teams become overwhelmed by the sheer volume of findings and struggle
to distinguish genuine security risks from noise.
6. Limited Remediation Guidance: While SAST tools excel at identifying security
vulnerabilities, they may provide limited guidance or context on how to remediate the
issues effectively. Remediation guidance may be generic or lacking in actionable
recommendations, making it difficult for developers to understand the root cause of the
vulnerabilities and implement appropriate fixes. This can result in delays in addressing
security issues and increased risk exposure.
7. Lack of Coverage for Third-Party Code: SAST tools may have limited visibility into
third-party libraries, frameworks, or components used in an application, especially if the
source code is not available or accessible. As a result, SAST may not detect vulnerabilities
introduced by third-party dependencies or provide accurate risk assessments for
components that are not analyzed statically. This blind spot can leave organizations
vulnerable to supply chain attacks and security risks originating from third-party code.
********** 5 **********
--- page 6 ---
a.
Infrastructure monitoring
▪   Infrastructure monitoring involves real-time tracking of the computer systems,
servers, processes and equipment that make up the computing network in an
enterprise. With infrastructure monitoring tools, information is collected from
specific IT components, including software and hardware units, virtual machines,
data centers, networks, disk storage etc.
▪ These continuous monitoring tools ‘supervise’ the computing network
environment, helping IT teams identify and address any resource or performance
issues more effectively. Not only does this improve internal efficiency, but it can
facilitate product and user experience improvement too.
Network monitoring
▪ Within the concept of IT infrastructure monitoring is network monitoring, which
Q 3   refers to tracking the health and performance of a network and its related
[10]
CO - 2;   components. Network monitoring tools help to identify network performance
BL- 3
issues by evaluating servers, switches, routers, firewalls and virtual machines.
Metrics such as bandwidth, uptime (availability) and hardware failures are
instrumental in measuring and correcting network issues.
Application performance monitoring (APM)
▪   It involves measuring the performance and availability of specific applications.
Application performance monitoring tools track metrics such as:
▪ API responses and transactions
▪ System responses
▪   Real-user monitoring (RUM)
Synthetic monitoring
▪   Synthetic monitoring is a form of software testing that uses behavioral scripts to
simulate real end-user interactions with an application or website. The goal is to
understand how a user would experience an app or website, measuring the
performance, speed, and functionality of a particular system or system
component.
▪   Synthetic monitoring tools for DevSecOps help you identify and fix issues before
they impact users, in addition to helping to establish future performance
benchmarks.
********** 6 **********
--- page 7 ---
b.   1. Avoid Root Permissions
•   Running a Docker container with root permissions may be the easiest way to get it to
function properly, as you don’t have to deal with complex permission management.
However, there are few justifications for running containers as root in a production
environment.
•   Docker containers don’t run as root by default, so you don’t have to change the default
configuration, but you should avoid giving root permissions. When using Kubernetes,
you can increase security by creating a pod security policy with the
MustRunAsNonRoot directive—this   explicitly blocks admins from starting
containers with root privileges.
2. Use Secure Container Registries
•   Container registries allow you to download container images easily from a central
repository, making them both convenient and potentially risky. For this reason, it is
better to stick to trusted registries like Docker Trusted Registry. You should assess
Q 3   the security of any registry you use and install it behind a firewall to protect against
[10]
CO - 3;   web-based breaches.
BL- 3
• Avoid letting anyone download or upload container images from your registry.
Implement role-based access control (RBAC) to define which users can access what
resources and block all other access. It may be inconvenient to manage and configure
access rules for new users, but this can help you prevent a registry breach.
5. Build Your Networks and APIs for Security
•   Docker containers use networks and application programming interfaces (APIs) to
communicate with each other. This communication allows containers to run properly
but also requires proper monitoring and security policies. You should design these
resources to facilitate monitoring and allow you to block breaches quickly.
6. Docker Container Monitoring
•   Monitoring is an essential part of any security strategy. In a containerized application,
monitoring can be challenging, because of the large number of moving parts and the
use of immutable components. Specialized container monitoring tools can help you
gain visibility and achieve observability over containerized workloads.
a.   Vagrant is a versatile DevOps tool that can be used in various use cases to streamline
development, testing, and deployment processes. Here are some common use cases of
Vagrant:
Q   1. Local Development Environments: One of the primary use cases of Vagrant is to create
4
consistent and reproducible development environments on developers' local machines. [10]
CO - 2;
BL- 3   Developers can use Vagrant to quickly spin up virtualized environments that mirror
production setups, including specific operating systems, software versions, and
configurations. This ensures that developers work in a consistent environment regardless
of their underlying host OS.
********** 7 **********
--- page 8 ---
2. Continuous Integration (CI) Testing: Vagrant is often used in CI workflows to automate
the creation of testing environments. CI servers can use Vagrant to spin up isolated
environments, execute automated tests, and tear down the environments once testing is
complete. This ensures that tests are run in a controlled and reproducible environment,
leading to more reliable test results.
3. Cross-Platform Development: Vagrant can be used to facilitate cross-platform
development by providing a consistent environment across different operating systems.
Developers working on Windows, macOS, or Linux machines can use Vagrant to create
identical development environments, eliminating compatibility issues and ensuring
consistent behavior across platforms.
4. Prototyping and Proof of Concepts: Vagrant is well-suited for quickly prototyping and
testing new ideas or proof of concepts. Developers can use Vagrant to spin up disposable
environments, experiment with different configurations, and validate concepts without
affecting their production or development environments.
5. Training and Education: Vagrant can be used as a teaching tool in educational settings
to provide students with hands-on experience in setting up and managing virtualized
environments. Instructors can use Vagrant to distribute pre-configured VMs or Docker
containers containing course materials, ensuring a consistent learning experience for all
students.
6. Demos and Presentations: Vagrant is useful for creating demo environments or
conducting presentations where a consistent and controlled environment is required.
Presenters can use Vagrant to quickly set up demo environments with specific
configurations, software stacks, and data sets, ensuring a smooth and predictable
demonstration experience.
7. Microservices Development: Vagrant can be used to set up and manage local
development environments for microservices-based applications. Developers can use
Vagrant to spin up separate VMs or containers for each microservice, enabling
independent development, testing, and debugging of individual components.
8. Infrastructure as Code (IaC) Development: Vagrant can be integrated into infrastructure
as code (IaC) workflows to automate the provisioning and configuration of development,
testing, and staging environments. Developers can use Vagrant alongside tools like
Ansible, Chef, or Puppet to define infrastructure configurations in code and manage
environment lifecycles programmatically.
9. Collaborative Development: Vagrant facilitates collaborative development by
providing a consistent environment that can be easily shared among team members.
Developers can share Vagrant configurations via version control systems like Git,
allowing team members to spin up identical environments with a single command and
collaborate on projects seamlessly.
********** 8 **********
--- page 9 ---
b.
Q 4
[10]
CO - 3;
BL- 3
Explain each component. Since web users are affected the issue is with Kube Proxy.
a.   1. Identification
▪ The Center for Internet Security advises performing automated vulnerability scans at
least once per week. Organizations with CI/CD development pipelines may need to
scan for vulnerabilities in their code and components several times a day.
▪   Organizations need to map out IT assets and may need to use different vulnerability
scanners for each type of asset:
▪ Open-source components
▪   Proprietary code
▪ Running applications
▪   Operating systems
▪ Cloud native infrastructure
Q 5   2. Evaluation
▪ Once the organization has a list of vulnerabilities discovered across its systems, it is   [10]
CO - 1;
BL- 3   important to classify and prioritize them using factors such as:
▪ CVSS severity scores
▪ Ease of exploitation
▪ The business impact of a breach
▪ Compensating security controls
▪   Penetration testing can help identify which vulnerabilities have the biggest real-world
impact and can facilitate damaging data breaches.
3. Remediation
▪   Vulnerability management tools typically recommend a remediation for each
vulnerability. There are three options for each vulnerability you discover:
▪ Remediate: Fix the vulnerability by applying a patch, replacing a vulnerable
component, etc., and rerunning the vulnerability scan to validate the fix.
********** 9 **********
--- page 10 ---
▪   Mitigate: Taking steps to reduce the impact of a vulnerability until it can be fixed, for
example, isolating affected systems from the network.
▪ No action: In reality it is impossible for organizations to remediate all vulnerabilities.
Some vulnerabilities which have lower severity or impact can be safely ignored.
4. Reporting
Vulnerability management systems can provide automated reports that show which
vulnerabilities were discovered and which were remediated across all IT systems. This
can facilitate periodic review of vulnerability status, planning for remediation efforts,
reporting to management, and addressing compliance obligations.
b.   ▪ Nomad is a flexible scheduler and workload orchestrator that enables you to deploy
and manage any application across on-premise and cloud infrastructure at scale.
▪   Efficient resource usage - Nomad optimizes the available cluster resources by
efficiently placing the workloads onto the client nodes of the cluster through a process
known as bin packing.
▪   Self-healing - Nomad constantly monitors and detects if tasks stop responding and
takes appropriate actions to reschedule them for high uptime.
▪ Zero downtime deployments - Nomad supports several update strategies including
rolling, blue/green, and canary deployments to make sure your applications are
updated with zero downtime to your users.
Q 5   ▪   Different workload types - Nomad's flexibility comes from its use of task drivers and
[10]
CO - 3;   allows orchestration of Docker and other containers, as well as Java Jar files, QEMU
BL- 3
virtual machines, raw commands with the exec driver, and more. Additionally, users
can create their own task driver plugins for customized workloads.
▪ Cross platform support - Nomad runs as a single binary and allows you to orchestrate
your application across macOS, Windows, and Linux clients running on-premises, in
the cloud, or on the edge.
▪   Single unified and declarative workflow - Regardless of the workload type, the
workflow for deploying and maintaining applications on Nomad is unified within a
declarative job specification that outlines important attributes like workload type and
configuration, service definitions for communication between components, and
location values such as region and datacentre.
a.   Secure CI/CD pipelines:
▪   Popular CI/CD pipeline tools such as Jenkins, Ansible, Puppet and Chef are
Q 6   designed for efficiency and speed but can present new security challenges. These
automated configuration management tools require secrets to access protected   [10]
CO - 2;
BL- 3   resources like databases, SSH servers and HTTPs services.
▪ These secrets are often insecurely hard-coded or stored in configuration files or code
for these tools (e.g., JenkinsFiles, playbooks, scripts, or source code).
********** 10 **********
--- page 11 ---
▪   Effective secrets management allows organizations to remove these hard-coded
secrets from DevOps tools within the CI/CD pipeline while providing full audit
trails, policy-based RBAC and secrets rotation.
Secure containers:
▪ DevSecOps and engineering teams increasingly rely on containers to accelerate
development and improve portability and productivity. Containers require secrets to
access critical and sensitive information.
▪   But, since containers are ephemeral (or short-lived), they can be difficult to track
and access to specific resources can be hard to manage and secure.
▪   Secrets management security measures enable teams to authenticate container
requests for secrets with native container platform attributes and manage secrets
with RBAC policy for granular control.
Manage elastic and auto-scale environments:
▪ Cloud providers offer auto-scaling capabilities to support elasticity (ephemeral) and
pay-as-you-grow economics.
▪ While this improves efficiency, it also creates new security management
challenges—particularly around scalability.
▪ By implementing secrets management best practices, organizations can eliminate the
need to have human operators manually apply policies to each new host by
assigning an identity to the host in real time and securely authenticating the calling
application based on the predefined security policy.
Secure internally developed applications and Commercial off-the-shelf (COTS)
applications:
▪   Internally developed applications and scripts, along with third-party tools and
solutions such as security tools, Robotic process automation (RPA), automation
tools, and IT management tools often require high levels of privileged access across
the enterprise’s infrastructure to complete their defined tasks.
▪   Effective secrets management practices require the removal of hardcoded credentials
from internally developed applications and scripts and that all secrets be centrally
stored, managed, and rotated to minimize risk.
b.   ▪ Use a minimal base image: Choose a base image with only the essential components
required for your application, such as Alpine Linux-based images.
▪   Utilize multi-stage builds: Multi-stage builds allow you to create smaller and more
Q 6   efficient images by copying only the necessary files and artifacts from one stage to
[10]
CO - 3;   another.
BL- 3
▪ Combine RUN commands: Each RUN command creates a new layer in the image.
Combining multiple commands using the && operator can reduce the number of
layers and the image size.
********** 11 **********
--- page 12 ---
▪ Clean up temporary files: Remove temporary files, caches, and build artifacts that are
not required for the final image.
▪ Keep secrets out of images: Avoid including sensitive information like passwords and
API keys in your images. Use environment variables or Docker secrets instead.
a.   Tool   Supported IaC   Key Features   Pricing
Terraform,
1000+   built-in   policies, Free (OSS), Paid
CloudFormation,
Checkov   CI/CD integration, custom (via   Prisma
Kubernetes, ARM,
rules   Cloud)
Docker
Static analysis, fast scans,
tfsec / Trivy   Terraform   Free (OSS)
module support
Terraform,   OPA policies, 500+ built-
Q 7   Terrascan   Kubernetes, Helm,   in   rules,   admission Free (OSS)
[10]
CO – 2;   CloudFormation   controller
BL- 3
Keeping   Terraform,
2000+   queries,
Infrastructure Kubernetes,
customizable rules, wide Free (OSS)
as   Code Docker,   Ansible,
IaC coverage
Secure(KICS) CloudFormation
Terraform,
IDE/CI   integrations,
Kubernetes,   Free   (limited),
Snyk IaC   custom rules, compliance
CloudFormation,   Paid
mapping
ARM
b. CAMS emphasizes the cultural aspects of DevOps adoption and the importance of
collaboration, automation, and sharing knowledge.
▪   Culture: Culture is a critical component of DevOps. CAMS highlights the need for a
culture of collaboration, trust, and shared responsibility between development and
operations teams. This cultural shift promotes open communication, breaking down
silos, and fostering a mindset of continuous learning and improvement.
Q 7   ▪ Automation: Automation plays a vital role in DevOps. CAMS emphasizes the
[10]
CO – 1;   automation of manual, repetitive, and error-prone tasks throughout the software
BL- 3
development lifecycle. By automating processes like build, testing, deployment, and
infrastructure provisioning, organizations can reduce human error, increase
efficiency, and accelerate the delivery of software.
▪ Measurement: Measurement refers to the collection and analysis of data to gain
insights into the performance and effectiveness of the software delivery process.
CAMS emphasizes the importance of measuring key performance indicators (KPIs)
********** 12 **********
--- page 13 ---
such as lead time, cycle time, deployment frequency, and mean time to recover
(MTTR). These metrics help teams identify bottlenecks, track progress, and make
data-driven decisions for improvement.
▪   Sharing: Sharing knowledge and experiences is a fundamental aspect of DevOps.
CAMS encourages teams to share information, best practices, and lessons learned to
foster a culture of continuous learning and improvement. This includes sharing
documentation, code, tools, and expertise among team members and across
departments.
********** 13 **********
````
