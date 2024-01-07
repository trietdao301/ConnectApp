# Design Document

## Research Connect with Undergrads
--------
Prepared by:

* `Gurman Grewal`,`WSU`
* `Nathan Lee`,`WSU`
* `Ebenezer Abate`,`WSU`
* `Triet Minh Dao`,`WSU`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Research Connect with Undergrads](#research-connect-with-undergrads)
  - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-24 |Initial draft | 1.0        |
| Revision 2 |2023-11-08 | Iteration 2 updates| 2.0        |
|      |      |         |         |


# 1. Introduction

This documentation provides the class level designs which specifies the structure of how our project will be written, implemented and function without actually writing the complete code(implementation).
It also provides the component-level and architectural design which sets the organization and structure the team will be following until the finalization of the project. It will also help in dividing workload between members.  

This project is a web application that will let authorized faculties from different departments advertise research positions so that students, after sign up then signing in, are able to apply to these advertised positions.

The end goal is to provide a reliable and appealing platform to the faculty and student of WSU so that student and faculty can interact through applications i.e., faculty reads student's application and then can decide to interview student or not for a research postion a student is interested in out of the ones available in the database.


At the end of the introduction, provide an overview of the document outline.

[Section II](#2-architectural-and-component-level-design) includes …

[Section III](#22-subsystem-design) includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure


![Architecture drawio](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/7707f9d2-2f18-4608-b627-f22e0100bb2d)

   Model - will be responsible for the state and data of the whole application. This subsystem will be highly dependent on the database and will draw directly from it. This is where all the database objects, we will be using for the entire web app will be.
   
   View - will be responsible rendering the appearance of the state and data from the model in the user interface. 
   
   Controller - related to controlling the interaction between the  model and view by also capturing user actions and translating it into operations on the model.

   Database - responsible for storing the data of the application which will then determine the state of the application. Highly connected with the model. In our case, this shall be hosted by SQLite

   Since our project will be a simple web application, this form of architecture assures low coupling in which the View will be linked to the Controller once and the Controller will be linked to the Model as displayed in the UML component diagram. As for re-use, we will be able to re-use the link between Model and Controller multipe times to bring about desired association between the two subsystems.

## 2.2 Subsystem Design 

![mermaid-diagram-2023-10-23-230913](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/82763493-384a-437c-9d47-e3f1d734512d)

### 2.2.1 Model

The model is the meat of this project since it is responsible for the state and data of the application. It is sort of the intermediary between the database and the rest of the project. This is what some might say "backend" of web application development.

![mermaid-diagram-2023-10-23-230913](https://github.com/WSU-CptS-322-Fall-2023/termproject-teamglad/assets/68701834/19db8a89-391c-4b32-945b-7cc45c7e438c)

### 2.2.2 Controller

Controller Role:
The controller serves as a connection between the view and the back-end logic including models, form, etc. Within the controller, various routes are defined to handle incoming HTTP requests, and it can interact with the database through query functions. When the client or UI sends an HTTP request, the controller receives the input data and processes it. Depending on the nature of the request, the controller may also send a response back to the client in the form of a new information template that meets the user's specific needs.

I. View subsystem:
  1. Display of all position:<br>
    This subsystem is responsible for presenting a list of all available research positions to the users, both students and faculty. It will generate HTML or other markup to display this information.<br>
    Interface: It interacts with the Controller (Position Manager) to retrieve the list of positions to be displayed. It also interacts with the data model (e.g., Position) to generate all position objects that need to be displayed. 

  2. Application Form: <br>
    This subsystem is responsible for collecting and validating user input in the application form. It retrieves input data to make a submission of position application. 
    Interface: It interacts with the Controller (Position Manager) and sends user-submitted data to it for processing.

  3. Post new position Form. <br>
     This subsystem is responsible for collecting and validating user input in the post new position form. It retrieves input data to make a submission of new position posting. 
     Interface: It interacts with the Model subsystem (Position Operation) and the Controller subsystem (Position Manager). It creates the new position data on submit which would be displayed on the view template. 

  4. Applicants Management: (Iteration 2) <br>
    This subsystem is responsible for showing the list of applicants as well as their application status and the qualification of each applicants. However, it only allows faculty who creates their own job to use this functionality. 
    Interact: It interacts with the Model subsystem (Student,Faculty) and the Controller (Login).

  5. Student Administration: (Iteration 2) <br>
     This subsystem handles administrative functions related to students, including enrollment, registration, record-keeping, and more. 
     Interact: It interacts with the Model System because it relies on the student records database for storing and retrieving student information.

II. Controller subsystem:
  1. Initialize App: <br>
  This subsystem is responsible for setting up the application, configuring routing, and initializing necessary components.
  Interface: It interacts with the View to render the initial view for users. It also interacts with the Model for any initial data setup, and it manages routes for all other subsystems. 

  2. Position Manager:<br>
  The Position Manager controls the application's research positions.
  Interface: It interacts with the View to provide position data for display and process user applications. It also interacts with the Model (Position Operation) to perform database operations on positions.

  3. Error handling: <br>
  The Error Handling subsystem deals with capturing and handling errors and exceptions that occur during application execution, ensuring meaningful error responses.
  Interface: It interacts with all other subsystems to capture errors and generate appropriate error responses. It can send error messages back to the View for user display.

  4. Login manager: (Iteration2)<br>
  The Login subsystem is responsible for the logging functionality of the application, it verifies the identity of student and faculty member and grants them access to the system. It ensures that only authorized users can interact with the system by validating their credentials. 
  Interface: It interacts with Student and Faculty database to verify the access. It also retrieves login credentials such as username and password from the user interface of the website. 

III. Model subsystem:
  1. Position Operation: <br>
  This subsystem is responsible for performing operations related to research positions, such as creating, reading, updating, and deleting positions in the database.
  Interface: It interacts with the Controller (Position Manager) to execute position-related database operations. It also interacts with the Initialize App subsystem to provide initial position data when the application starts.
  2. Data model: User, Student, Faculty, Position, Application:<br>
  These are representations of data entities within the application. The Data Model subsystem defines the structure of these entities and their relationships.
  Interface: The Data Model interacts with the Controller (Position Manager) to provide data for creating positions and processing applications.

|   | Methods           | URL Path                 | Description  |
|:--|:------------------|:-------------------------|:-------------|
|1. |   index           |/index                    |Render a template that displays all position and its information.              |
|2. |   post_position   |/postposition             |Render a template that displays a form to retrieve user input about the new position.              |
|3. |   apply           |'/apply/<int:position_id>'|Render a template that displays an application form to retrieve student inputs about their description and references.              |
|4. |   login           |'/login'|Render a form that retrieves login credentials such as username and password, then verifies them.        |
|5. |   applicants          |'/applicants/<positionid>'|Render a template that list all students who have applied for the current user's posted job.         |
|6. |    qualification  |'/qualification/<int:studentid>'|Render a template that shows all qualification of each applicants.        |
|7. |    register  |'/register'|Render a form that collects new user credentials to create a new account after successfully verifying the unique of the credentials input.        |
|8. |    profile  |'/profile'|Render a template that shows all current user's personaly information like name, major, GPA, etc.       |

### 2.2.3 View and User Interface Design 

View Role:

1. Display information to users, such as research positions, student profiles, and faculty information.
2. Provide forms for user input, including registration forms, application forms, and position creation forms.
3. Enable user interaction and navigation within the web application.

We will build the user interfaces using HTML and CSS 
List of page template:
1. Open Reseach position page: This will serve as the landing page for the web application. It also include a logout and registration option for both student and faculty user. This page will display all available research positions to the user 
Use-Cases: View open position and display information for each position.
2. Application Form Page: Students can fill out an application form for a research position on this page, including a statement of interest,faculty and email reference.
Use-Cases: Apply for research positions.
3. Post New Research Position Form Page: This form page allows faculty user to create new position. The form requires faculty user to provide the title, description, start and end date, required time commitment, etc before submitting it. 
4. Profile Page (use case 1, 9): This page will display the user's profile information, including their name, contact details, academic history, and any additional details relevant to the user. 
4. Login Page (use case 2, 10): This page contains a login form where users input their credentials to gain access to the system.
5. Register Page (use case 2, 10): This page will display a form with fields for user registration, including name, email, password, and other required information.
6. View all applicants Page (use case 12): This page lists all applicants, providing their names, and application status.
7. View qualification of each applicant Page (use case 13): This page displays detailed information about a specific applicant, including their qualifications, experience, and other relevant details.

# 3. Progress Report

In Iteration 1, we have completed four use cases. First, we have implemented displaying all open research positions. Second, we also allow the application to display various information for each research position. Third, our application allows student user to apply for research positions. Finally, faculty member can create and post undergraduate research positions that they have entered. 

In Iteration 2, we have completed the implementation of login and registration functionality for student and faculty. We also allow faculty members to see the list of students who apply for their jobs and to view the qualification of those applied students. 
# 4. Testing Plan
  
**Unit and Functional Testing**

We will be using the pytest framework to test the routes module. We will be checking for 200 http status code, as well as making sure that the correct html contents are displayed. Additionally for POST requests we will be making sure that the correct data is added into the database or the correct error messages are outputted.

**UI Testing**

We will test UI elements such as buttons by manually using them. We will make sure that we are redirected to the correct page after clicking the button as well as making sure that we aren't allowed to enter login required pages when not logged in.
# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? | 
| 10        | Is the controller explained in sufficient detail?  |
| 22        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
|           | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
| 3         | Is the document well formatted? (Make sure to check your document on GitHub. You will loose points if there are formatting issues in your document.  )  |
|           |  |
|           | **Total** |
|           |  |
