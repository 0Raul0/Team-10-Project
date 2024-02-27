# Software Requirements Specification
## For the Technical Talent Finding System

Version 0.1  
Prepared by Jack Harris
Team 10 of the 2024 Oxford CompSci Second Year Group Design Practical  
created 2024/02/27

Table of Contents
=================
* [Revision History](#revision-history)
* 1 [Introduction](#1-introduction)
  * 1.1 [Document Purpose](#11-document-purpose)
  * 1.2 [Product Scope](#12-product-scope)
  * 1.3 [Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  * 1.4 [References](#14-references)
  * 1.5 [Document Overview](#15-document-overview)
* 2 [Product Overview](#2-product-overview)
  * 2.1 [Product Perspective](#21-product-perspective)
  * 2.2 [Product Functions](#22-product-functions)
  * 2.3 [Product Constraints](#23-product-constraints)
  * 2.4 [User Characteristics](#24-user-characteristics)
  * 2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
  * 2.6 [Apportioning of Requirements](#26-apportioning-of-requirements)
* 3 [Requirements](#3-requirements)
  * 3.1 [External Interfaces](#31-external-interfaces)
    * 3.1.1 [User Interfaces](#311-user-interfaces)
    * 3.1.2 [Hardware Interfaces](#312-hardware-interfaces)
    * 3.1.3 [Software Interfaces](#313-software-interfaces)
  * 3.2 [Functional](#32-functional)
  * 3.3 [Quality of Service](#33-quality-of-service)
    * 3.3.1 [Performance](#331-performance)
    * 3.3.2 [Security](#332-security)
    * 3.3.3 [Reliability](#333-reliability)
    * 3.3.4 [Availability](#334-availability)
  * 3.4 [Compliance](#34-compliance)
  * 3.5 [Design and Implementation](#35-design-and-implementation)
    * 3.5.1 [Installation](#351-installation)
    * 3.5.2 [Distribution](#352-distribution)
    * 3.5.3 [Maintainability](#353-maintainability)
    * 3.5.4 [Reusability](#354-reusability)
    * 3.5.5 [Portability](#355-portability)
    * 3.5.6 [Cost](#356-cost)
    * 3.5.7 [Deadline](#357-deadline)
    * 3.5.8 [Proof of Concept](#358-proof-of-concept)
* 4 [Verification](#4-verification)
* 5 [Appendixes](#5-appendixes)

## Revision History
| Name | Date    | Reason For Changes  | Version   |
| ---- | ------- | ------------------- | --------- |
|      |         |                     |           |
|      |         |                     |           |
|      |         |                     |           |

## 1. Introduction
This document will act as the specification from which Team 10 shall produce a talent finding system for Microsoft. This system will enable Microsoft to find talented individuals who would be suited to working in a software development role, and it will do so in ways specified in this document.

### 1.1 Document Purpose
The purpose of this document is twofold: to provide a specification from which the developers can produce the intended software, and to provide a specification of the system on which the developers and the client agree.

### 1.2 Product Scope
The purpose of the product is to enable Microsoft to find talented potential hires for graduate software development roles. It will do so by providing a series of puzzles which test algorithmic thinking and advanced coding, similar to those found on websites like [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/) and [AlgoExpert](https://www.algoexpert.io/product). It will also provide ranking metrics for the performance of the users of the system, alongside an overall ranking of the users. There will also be gamified elements which provide extrinsic rewards for the users.

### 1.3 Definitions, Acronyms and Abbreviations
"The developers", "Team 10", "we": The development team for the project, consisting of Jack Harris, Rory Kemp, Raul Sheth, Luke Tan, Nathan Hardcastle and Georgi Petkov.

"The client", "Microsoft": The client for this project, consisting primarily of Lilia Georgieva, but including Microsoft as a whole.

"The users", "the applicants", "the candidates": The people who will be solving the puzzles in this system and participating in the rankings. In other words, the people the client will want to consider as potential applicants for graduate software roles.

### 1.4 References
[UML Use Case Diagrams]

### 1.5 Document Overview
Describe what the rest of the document contains and how it is organized.

## 2. Product Overview
> This section should describe the general factors that affect the product and its requirements. This section does not state specific requirements. Instead, it provides a background for those requirements, which are defined in detail in Section 3, and makes them easier to understand.

### 2.1 Product Perspective
This product is being produced as part of the 2024 Group Design Practicals done by students in their second year of a Computer Science course at the University of Oxford. It emulates the interview process of most software companies, wherein candidates are asked a number of technical questions and puzzles in order for the interviewer to assess the ability of the candidate. The product shall be completely standalone, and not be part of any wider project.

### 2.2 Product Functions
The product shall:
* Provide a series of puzzles to the user for them to complete
* Provide a place for users to upload their code for their answers

* Provide a series of metrics from which the users' performance can be assessed
* Provide an overall ranking of the users

* Provide a login/accounts system for the users, so their progress can be kept between sessions
* Provide gamified elements within the puzzle to provide extra rewards to users and motivate them to keep trying the puzzles.


### 2.3 Product Constraints
The product will have the following constraints:
* The product will have to run in the web browser.
* The product will have to have its backend running on a lightweight server.
* The product will have to be developed within 2 months.
* The product will have to be GDPR-compliant.
* The product will be developed by six second-year undergraduates. 

### 2.4 User Characteristics
Identify the various user classes that you anticipate will use this product. User classes may be differentiated based on frequency of use, subset of product functions used, technical expertise, security or privilege levels, educational level, or experience. Describe the pertinent characteristics of each user class. Certain requirements may pertain only to certain user classes. Distinguish the most important user classes for this product from those who are less important to satisfy.

**User Class 1: Candidates**
These users will primarily be computer science graduates. They will be proficient in algorithmic thinking, and will have enough capability in a programming language to be able to produce computer programs that allow them to answer the puzzles. 

**User Class 2: Employers**
These will primarily be recruiters at Microsoft looking for hidden talent. They will be very proficient in algorithmic thinking and will have some degree of experience within the software industry. They will be able to assess the quality of the code of applicants.

### 2.5 Assumptions and Dependencies
The following assumptions are present:
* Candidates will have access to the internet and a web browser
* The metrics specified in this document will be useful in assessing the ability of users.

Since we will be making most of this from scratch, there are very few external assumptions about the operation of other software components.


### 2.6 Apportioning of Requirements
Apportion the software requirements to software elements. For requirements that will require implementation over multiple software elements, or when allocation to a software element is initially undefined, this should be so stated. A cross reference table by function and software element should be used to summarize the apportioning.

| Requirement | Software Element | 
| ----------- | ---------------- | 
|             |                  |           
|             |                  | 
|             |                  |           



Identify requirements that may be delayed until future versions of the system (e.g., blocks and/or increments).

## 3. Requirements
> This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

> The specific requirements should:
* Be uniquely identifiable.
* State the subject of the requirement (e.g., system, software, etc.) and what shall be done.
* Optionally state the conditions and constraints, if any.
* Describe every input (stimulus) into the software system, every output (response) from the software system, and all functions performed by the software system in response to an input or in support of an output.
* Be verifiable (e.g., the requirement realization can be proven to the customer's satisfaction)
* Conform to agreed upon syntax, keywords, and terms.

**Requirement Template**
**Requirement Name**:
**Requirement Number**: 
**Requirement Type**: 
**Use Cases**:

**Description**:

**Rationale**:

**Fit Criterion**:

**Priority**:

**Conflicts**:

**Dependencies**:

### 3.1 External Interfaces
> This subsection defines all the inputs into and outputs requirements of the software system. Each interface defined may include the following content:
* Name of item
* Source of input or destination of output
* Valid range, accuracy, and/or tolerance
* Units of measure
* Timing
* Relationships to other inputs/outputs
* Screen formats/organization
* Window formats/organization
* Data formats
* Command formats
* End messages

#### 3.1.1 User interfaces
Define the software components for which a user interface is needed. Describe the logical characteristics of each interface between the software product and the users. This may include sample screen images, any GUI standards or product family style guides that are to be followed, screen layout constraints, standard buttons and functions (e.g., help) that will appear on every screen, keyboard shortcuts, error message display standards, and so on. Details of the user interface design should be documented in a separate user interface specification.

Could be further divided into Usability and Convenience requirements.



#### 3.1.2 Hardware interfaces
Describe the logical and physical characteristics of each interface between the software product and the hardware components of the system. This may include the supported device types, the nature of the data and control interactions between the software and the hardware, and communication protocols to be used.

#### 3.1.3 Software interfaces
Describe the connections between this product and other specific software components (name and version), including databases, operating systems, tools, libraries, and integrated commercial components. Identify the data items or messages coming into the system and going out and describe the purpose of each. Describe the services needed and the nature of communications. Refer to documents that describe detailed application programming interface protocols. Identify data that will be shared across software components. If the data sharing mechanism must be implemented in a specific way (for example, use of a global data area in a multitasking operating system), specify this as an implementation constraint.

### 3.2 Functional
> This section specifies the requirements of functional effects that the software-to-be is to have on its environment.

### 3.3 Quality of Service
> This section states additional, quality-related property requirements that the functional effects of the software should present.

#### 3.3.1 Performance
If there are performance requirements for the product under various circumstances, state them here and explain their rationale, to help the developers understand the intent and make suitable design choices. Specify the timing relationships for real time systems. Make such requirements as specific as possible. You may need to state performance requirements for individual functional requirements or features.

#### 3.3.2 Security
Specify any requirements regarding security or privacy issues surrounding use of the product or protection of the data used or created by the product. Define any user identity authentication requirements. Refer to any external policies or regulations containing security issues that affect the product. Define any security or privacy certifications that must be satisfied.

#### 3.3.3 Reliability
Specify the factors required to establish the required reliability of the software system at time of delivery.

#### 3.3.4 Availability
Specify the factors required to guarantee a defined availability level for the entire system such as checkpoint, recovery, and restart.

### 3.4 Compliance
Specify the requirements derived from existing standards or regulations, including:  
* Report format
* Data naming
* Accounting procedures
* Audit tracing

For example, this could specify the requirement for software to trace processing activity. Such traces are needed for some applications to meet minimum regulatory or financial standards. An audit trace requirement may, for example, state that all changes to a payroll database shall be recorded in a trace file with before and after values.

### 3.5 Design and Implementation

#### 3.5.1 Installation
Constraints to ensure that the software-to-be will run smoothly on the target implementation platform.

#### 3.5.2 Distribution
Constraints on software components to fit the geographically distributed structure of the host organization, the distribution of data to be processed, or the distribution of devices to be controlled.

#### 3.5.3 Maintainability
Specify attributes of software that relate to the ease of maintenance of the software itself. These may include requirements for certain modularity, interfaces, or complexity limitation. Requirements should not be placed here just because they are thought to be good design practices.

#### 3.5.4 Reusability
<!-- TODO: come up with a description -->

#### 3.5.5 Portability
Specify attributes of software that relate to the ease of porting the software to other host machines and/or operating systems.

#### 3.5.6 Cost
Specify monetary cost of the software product.

#### 3.5.7 Deadline
Specify schedule for delivery of the software product.

#### 3.5.8 Proof of Concept
<!-- TODO: come up with a description -->

## 4. Verification
> This section provides the verification approaches and methods planned to qualify the software. The information items for verification are recommended to be given in a parallel manner with the requirement items in Section 3. The purpose of the verification process is to provide objective evidence that a system or system element fulfills its specified requirements and characteristics.

<!-- TODO: give more guidance, similar to section 3 -->
<!-- ieee 15288:2015 -->

## 5. Appendixes