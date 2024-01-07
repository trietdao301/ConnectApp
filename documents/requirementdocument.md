![d_CVE0dh7V](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/ead41d7a-271f-4a6b-818c-154564b4d309)# Software Requirements Specification

## Research Connect with Undergrads
--------
Prepared by: TeamGLAD

* `<Gurman Grewal>`,`<WSU>`
* `<Nathan Lee>`,`<WSU>`
* `<Ebenezer Abate>`,`<WSU>`
* `<Triet Minh Dao>`,`<WSU>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Research Connect with Undergrads](#research-connect-with-undergrads)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [| Iteration         | Iteration 3  |](#-iteration----------iteration-3--)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

The requirements document will outline specific user stories (how user's will interact with our software) and provide a guide towards the end product

## 1.1 Document Purpose
The purpose of the Software Requirement Specification is to layout what is required of the software to ensure that the developers meet specification for the end product.

## 1.2 Product Scope
The purpose of this product is to create a platform that connects 2 groups of people, faculty and undergraduate students. It allows for faculty members that don't teach lower-level courses to be able to come into contact with the likes of sophomore and junior year undergrads and offer them the opportunity to take part in research positions.
## 1.3 Document Overview
The rest of the document will cover who the customers, stakeholders, and users are. We will also cover the specific use cases of our software. A mockup of the user interface and the product backlog will also be included.

----
# 2. Requirements Specification

## 2.1 Customer, Users, and Stakeholders

The customers and users of our software will be undergraduate students and faculty of Washington State University in the Computer Science or Software Engineering department that are intrested in research. The stakeholders of this software are Professor Sakire and the TA's of Fall 2023 CptS 322.

----
## 2.2 Use Cases
The student user should be able to login and see the research opportunities available and apply. Whereas the faculty user group should be able to register and login and create said research opportunites for the student group to apply to.

| Use case # 1      |   |
| ------------------ |--|
| Name              | "Student Registration"  |
| Users             | "Students"  |
| Rationale         | "Student needs to create a student account to enter their profile information like name, last name, WSU ID, GPA, familiar programming languages, etc."  |
| Triggers          | "Student fills all required inputs and press Register button."  |
| Preconditions     | "None"  |
| Actions           | "1. Student enters their WSU email and sets a password. <br>2. Student enters contact information, major, GPA, etc.<br>3. Student selects research topics and programming languages. <br>4. Student describes prior research experience."  |
| Alternative paths | "None"  |
| Postconditions    | "Student account is created."  |
| Acceptance tests  | "1.Check if the provided information matches with created account.<br> 2. Check if the student can log in with the new account credentials."  |
| Iteration         | "Iteration 2"  |

| Use case # 2      |   |
| ------------------ |--|
| Name              | "Student Login"  |
| Users             | "Students"  |
| Rationale         | "Student needs to be able to access their accounts."  |
| Triggers          | "Student fills out login form and press login button."  |
| Preconditions     | "Student account has to be registered before."  |
| Actions           | "1. Student enters their username (WSU email) and password."  |
| Alternative paths | "None"  |
| Postconditions    | "Student account is created."  |
| Acceptance tests  | "1.Check if the provided username and password match with registered account"  |
| Iteration         | "Iteration 2"  |

| Use case # 3      |   |
| ------------------ |--|
| Name              | "View Open Research Positions"  |
| Users             | "Students"  |
| Rationale         | "Student needs to be able to view available research positions to apply for positions."  |
| Triggers          | "Student presses on view open research positions button to view."  |
| Preconditions     | "Student is logged into their account."  |
| Actions           | "1. The application lists all open research positions.<br>2. The application identifies and lists positions matching the student's research interests as "Recommended Research Positions."  |
| Alternative paths | "None"  |
| Postconditions    | "Student can see the list of open positions and the list of "Recommended Research Positions"."  |
| Acceptance tests  | "1. Verify that students can view all open positions. <br>2.Verify that recommended positions match the student's research interests."  |
| Iteration         | "Iteration 1, 3"  |

| Use case # 4      |   |
| ------------------ |--|
| Name              | "View Research Position Details"  |
| Users             | "Students"  |
| Rationale         | "Student needs to learn more about a specific research position."  |
| Triggers          | "Student presses on view more detail button on specific position."  |
| Preconditions     | "Student is logged into their account."  |
| Actions           | "1. Display research project title, description, start/end dates, required time commitment, research fields, programming languages, qualifications, and faculty contact information for the selected position."  |
| Alternative paths | "None"  |
| Postconditions    | "Student can see detailed information about the selected position."  |
| Acceptance tests  | "Verify that students can access and view details of a specific research position."  |
| Iteration         | "Iteration 1"  |

| Use case # 5      |   |
| ------------------ |--|
| Name              | "Apply for Research Position"  |
| Users             | "Students"  |
| Rationale         | "Student needs to apply for research positions."  |
| Triggers          | "Student presses on apply button."  |
| Preconditions     | "Student are logged into their account."  |
| Actions           | "1. Student submits a statement of interest and provides a reference faculty member's name and email."  |
| Alternative paths | "None"  |
| Postconditions    | "Application status changes to "Pending"."  |
| Acceptance tests  | "Verify that the application is sent and that the faculty can see the pending application."  |
| Iteration         | "Iteration 1"  |

| Use case # 6      |   |
| ------------------ |--|
| Name              | "View Applied Research Positions and Application Status"  |
| Users             | "Students"  |
| Rationale         | "Students need to see the positions they have applied for and their application statuses."  |
| Triggers          | "Student selects the option to view their applied positions."  |
| Preconditions     | "Student is logged into their account and has applied for one or more position."  |
| Actions           | "1. Display a list of positions the student has applied for, along with their respective application statuses."  |
| Alternative paths | "None"  |
| Postconditions    | "Students can view their applied positions and application statuses."  |
| Acceptance tests  | "1. Check if student can see their applied position. <br>2. Check if student can see application statues."  |
| Iteration         | "Iteration 3"  |

| Use case # 7      |   |
| ------------------ |--|
| Name              | Withdraw pending applications  |
| Users             | Students |
| Rationale         | students should be able to withdraw pending applications as their availability and interest changes |
| Triggers          | Student selects withdraw option |
| Preconditions     | Student has applications that are in pending stage |
| Actions           | 1. Student selects withdraw application option <br> 2. System removes pending application |
| Alternative paths | None  |
| Postconditions    | pending application is removed  |
| Acceptance tests  | 1. Check if student can see the removed pending application <br>2. Check if faculty can see the removed pending application  |
| Iteration         | Iteration 3  |

| Use case # 8      |   |
| ------------------ |--|
| Name              | "View User Profile"  |
| Users             | "Students "  |
| Rationale         | "Students need to be able to view their own profile."  |
| Triggers          | "Student selects the option to view the student profile."  |
| Preconditions     | "Student is logged into their account."  |
| Actions           | "1. Display the student profile along with information as to how to edit and save changes."  |
| Alternative paths | "None"  |
| Postconditions    | "Students can now view and edit their profile."  |
| Acceptance tests  | "1. Check if student can see their profile."  |
| Iteration         | "Iteration 3"  |

| Use case # 9      |   |
| ------------------ |--|
| Name              | "Edit User Profile"  |
| Users             | "Students "  |
| Rationale         | "Students need to be able to change/edit their own profile incase students had commited a mistake while providing information or there seems to be a change in information."  |
| Triggers          | "Student selects the option to edit the student profile."  |
| Preconditions     | "Student is logged into their account and can view their profile."  |
| Actions           | "1. Make profile forms ready to accept changes, display edit button and display save changes button."  |
| Alternative paths | "None"  |
| Postconditions    | "Students can now edit their profile and save any changes that the student has made."  |
| Acceptance tests  | "1. Check if student can edit their profile and then save the changes."  |
| Iteration         | "Iteration 3"  |

| Use case # 10      |   |
| ------------------ |--|
| Name              | Faculty Register  |
| Users             | Faculty |
| Rationale         | Faculty should be able to create an account so that they can post research positions |
| Triggers          | Faculty fills in required inputs and hits register |
| Preconditions     | None |
| Actions           | 1. Faculty enters their WSU email and sets a password. <br>2. Faculty enters contact information, major, GPA, etc. |
| Alternative paths | None  |
| Postconditions    | Faculty account is created  |
| Acceptance tests  | 1. Check if faculty account information matches information given<br>2. Check if faculty can login with new credentials  |
| Iteration         | Iteration 2  |

| Use case # 11      |   |
| ------------------ |--|
| Name              | Faculty Login  |
| Users             | Faculty Members  |
| Rationale         | Faculty members need to access their accounts to post and manage research positions.  |
| Triggers          | Faculty member presses login button and initialize login process.  |
| Preconditions     | Faculty member account is registered. |
| Actions           | 1. Faculty enters their username (WSU email) and password.  |
| Alternative paths | None  |
| Postconditions    | Faculty is logged into their account.  |
| Acceptance tests  | 1. Verify that faculty members can log in with their credentials.  |
| Iteration         | Iteration 2  |

| Use case # 12      |   |
| ------------------ |--|
| Name              | Create Undergraduate Research Positions  |
| Users             | Faculty  |
| Rationale         | Faculty needs to add new research positions to attract students.  |
| Triggers          | Faculty decides to offer new research opportunities. |
| Preconditions     | Faculty is logged into the system. |
| Actions           | 1. Faculty clicks on "Create Research Position" option.<br> 2. Faculty provides the following information for each position. <br> 3. Faculty confirms and submits the new research position.  |
| Alternative paths | None  |
| Postconditions    | New undergraduate research positions are added to the system.  |
| Acceptance tests  | 1. Faculty can see the newly created research positions in the system.<br>2. Students can view and apply for these positions.  |
| Iteration         | Iteration 1  |

| Use case # 13      |   |
| ------------------ |--|
| Name              | View Students Who Applied for Positions  |
| Users             | Faculty  |
| Rationale         | Faculty needs to manage and evaluate student applications for research positions.  |
| Triggers          | Faculty clicks view button to trigger. |
| Preconditions     | Faculty is logged into the system. |
| Actions           | 1. Faculty clicks on the "View Applicants" option for a specific research position.<br> 2. The system displays a list of students who have applied for the position. <br> 3.  The list includes information about each student's application status, such as "Pending," "Approved for Interview," or "Hired" (if applicable).<br> 4. Faculty can click on individual student profiles to view more details.  |
| Alternative paths | None  |
| Postconditions    | Faculty can review the list of students who applied for the position.  |
| Acceptance tests  | 1. Faculty can see the list of applicants and their application statuses.  |
| Iteration         | Iteration 2  |

| Use case # 14      |   |
| ------------------ |--|
| Name              | View Student Qualifications  |
| Users             | Faculty  |
| Rationale         | Faculty needs to evaluate student qualifications for research positions.  |
| Triggers          | Faculty wants to assess the qualifications of individual students. |
| Preconditions     | Faculty is logged into the system. |
| Actions           | 1. Faculty clicks on an individual student's profile..<br> 2. The system displays the qualifications of the selected student.  |
| Alternative paths | None  |
| Postconditions    | Faculty can assess the qualifications of the selected student.  |
| Acceptance tests  | 1. Faculty can assess the qualifications of the selected student.  |
| Iteration         | Iteration 2  |

| Use case # 15      |   |
| ------------------ |--|
| Name              | Approve Application  |
| Users             | Faculty  |
| Rationale         | Faculty members should be able to approve an application to continue into interviews  |
| Triggers          | User presses Approve button  |
| Preconditions     | Student application exists  |
| Actions           | 1. User presses Approve button <br>2. Software updates application status to approved  |
| Alternative paths | |
| Postconditions    | Student application is changed to "Approved for interview"  |
| Acceptance tests  | Check whether the student application status is changed to approve after pressing approve button  |
| Iteration         | Iteration 3  |

| Use case # 16      |   |
| ------------------ |--|
| Name              | Update Application  |
| Users             | Faculty  |
| Rationale         | After an interview with a student, the faculty member will want to update the application to inform the student whether they are hired or not  |
| Triggers          | User presses hire/reject button  |
| Preconditions     | Student application exists and are approved  |
| Actions           | 1. User presses hire button <br>2. Software updates application status to Hired  |
| Alternative paths | 1. User presses reject button <br>2. Software updates application status to Not Hired  |
| Postconditions    | Student application is changed to "Hired" or "Not Hired"  |
| Acceptance tests  | Check whether the student application is changed to the correct status based on the button pressed  |
| Iteration         | Iteration 3  |

| Use case # 17      |   |
| ------------------ |--|
| Name              | Delete Research Position  |
| Users             | Faculty  |
| Rationale         | Users should be able to delete research positions once positions are filled up or research is completed.  |
| Triggers          | user presses delete position button |
| Preconditions     | research position exists and is posted by current user |
| Actions           | 1. User presses delete position <br>2. Software removes the option to be able to apply for position <br>3. Software changes student application statuses to "Position is not available" |
| Alternative paths |  |
| Postconditions    | Position is deleted and all student applications updated to "Position is not available"  |
| Acceptance tests  | Check whether students can apply for position and whether student applications for the position were updated to "Position is not available"  |
| Iteration         | Iteration 3  |
----

Swimlane Activity diagram for the use cases


![d_CVE0dh7V-1](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/29818f32-37a2-4d5b-be7b-b727ff56e400)



## 2.3 Non-Functional Requirements

1.  Compatibility Requirements: Able to run on latest versions of Chrome, Firefox, Safari, and Edge.
2.  Security: Only users that are authenticated have access to the correct pages.
3.  Performance: The system should populate the page within 5 seconds to ensure smooth user experience.

----
# 3. User Interface

![image](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/fd734042-bdde-40e5-a15b-7ce7cf99e06e)
![image](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/25401f46-1b42-4f8b-b86d-0246f5d8beba)

----
# 4. Product Backlog

https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/issues

----
# 4. References



----
----
