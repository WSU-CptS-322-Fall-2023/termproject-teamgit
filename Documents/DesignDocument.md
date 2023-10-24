# Design Document

## Your Project Title
--------
Prepared by:

* `<Kyan Kotschevar-Smead>`,`<TeamGit>`
* `<Elliot Perez>`,`<TeamGit>`
* `<Fredy Fernandez>`,`<TeamGit>`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Your Project Title](#your-project-title)
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
|Revision 1 |2021-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |


# 1. Introduction

Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

At the end of the introduction, provide an overview of the document outline.

[Section II](#2-architectural-and-component-level-design) includes …

[Section III](#22-subsystem-design) includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure

 ![UML Compoent diagram](Images\UMLMVC.png)
 
 We adopted the MVC pattern for our architecture. Our model is responsible for data retrieval, manipulation, and processing and works closly with the controller. The View is responsible for presenting the data to the user and handling the user interface elements. It is responsible for the visual and interactive parts. The controller is the middle man in between the two, where it handles user action logic and communicates with the Model to create, retrieve, update, or destroy the data accordingly.


By abstracting out system in 3 compoents we designate responsibilies. This when we for say want to change a visual element in the view, it wont effect how the Model and Controller functions. Thus reducing coupling. As for reuse posts Models are used in many controllers and usecases can be reused in simalar cases


## 2.2 Subsystem Design 

(**Note1**: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

(**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.)

### 2.2.1 Model

Briefly explain the role of the model. 

(***in iteration-1***) Include a list of the tables (models) in your database and explain the role of each table. Provide the attributes of the tables (including relationships).

| ResearchPost                  |
|-------------------------|
|ResearchPost is the table for each research post position |
| - id: int <br> - title: string <br> - description: string <br> - qualifications: string <br> - major: string <br> - timestamp: datetime <br> +/- applications: relationship |
||

| Apply                  |
|-------------------------|
|Apply is the table that holds the data of the application for the researchpost. |
| - id: int <br> - research_topic: string <br> - statement: string <br> - faculty_name: string <br> - faculty_email: string <br> +/- researchpost_id: int  |
||

(***in iteration -2***) Revise the database model. Provide a UML diagram of your database model showing the associations and relationships among tables. Your UML diagram should also show the methods of your models.

### 2.2.2 Controller

Briefly explain the role of the controller. If your controller is decomposed into smaller subsystems (similar to the Smile App design we discussed in class), list each of those subsystems as subsections. 

For each subsystem:
 * Explain the role of the subsystem (component) and its responsibilities.
 * 	Provide a detailed description of the subsystem interface, i.e., 
    * which other subsystems does it interact with?  
    * what are the interdependencies between them? 

**Note:** Some of your subsystems will interact with the Web clients (browsers). Make sure to include a detailed description of the routes your application will implement. For each route specify its “methods”, “URL path”, and “a description of the operation it implements”.  
You can use the following table template to list your route specifications. 

(***in iteration-1***) Brainstorm with your team members and identify all routes you need to implement for the completed application and explain each route briefly. If you included most of the major routes but you missed only a few, it maybe still acceptable. 

(***in iteration-2***) Revise your route specifications, add the missing routes to your list, and update the routes you modified. Make sure to provide sufficient detail for each route. In iteration-2, you will be deducted points if you don’t include all major routes needed for implementing the required use-cases or if you haven’t described them in detail.

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. |                   |            |              |
|2. |                   |            |              |
|3. |                   |            |              |
|4. |                   |            |              |
|5. |                   |            |              |
|6. |                   |            |              |


### 2.2.3 View and User Interface Design 

The View is responsible for presenting the data to the user and handling the user interface elements. The way we would like to design our user interface would be with bootstrap styling.  

Provide a list of the page templates you plan to create (or you already created). Briefly describe the information that will be displayed on those pages and the forms that will be rendered (i.e., explain the input and output for each page). Make sure to mention which use-cases in your “Requirements Specification” document will utilize these interfaces for user interaction. You can supplement your description with UI sketches or screenshots. 

#### Faculty & Student Login page
On the faculty & student Login page the user can dedcide to login with either student credentils or faculty creditentials. If the user is an excsitingh user for either fauclty or students then they will be redirected to their home page. If not then they will be denied access. If they're not a member they have the options of registering as a student or faculty. If they chose oone then they will be redirected to the registration page for student or faculty. The use case for this page is #6 and #8.
![Faculty/StudentPage](Images\Sign-in.png)

#### Faculty Register page
On the faculty registration page, it shall display a form that will ask the user to input their first name, last name, email, password, confirm password, and phone number. once the form is validated then the faculty shall be able to be registered in the db and be redirected to the facult home page. The use case for this page #7.
![FacultyPage](Images\FacReg.png)

#### Student Register page
On the student registration page, it shal display a form that will ask the user to input their first name, last name, email, password, confirm password, phone number, major, com. GPA, EGD, research interests, programming L., and prior research Experience. Once the form is validated then the student shall be able to be registered in the db and be redirected to the student home page. The use case for this page #5.
![StudentPage](Images\stuReg.png)
![StudentPage](Images\stupro1.png)
![StudentPage](Images\stupro2.png)

#### Faculty home page
On the faculty home page it shall display the research posts of the faculty and have the option to delete the post as will as will the faculty member will have a tab bar where they have the options of either going create posting, View Applicaitions, or Edit Profile. Chosing either options wil redirect the Faculty member to a different page. The use case #3 and #2 are to view a research post on the main faculty home page.
![FacultyPage](Images\main.png)

#### Student home page
On the student home page it shall display the research post postions that are available and will have the option od only displaying the research position posts that match you intersts. There will also be a tab bar that the student cas choose of either being at the home page, My Applications, or Edit Profile and each tab will redirect the student to a different page. The use case #3 and #2 are to view a research post on the main student home page.
![StudentPage](Images\stuHome.png)

#### apply page
On the apply page shal display a form where the student can input their research topic, personal statement, faculty name, and faculty email. Once the form is validated then the application will be sent to the corresponding faculty who had the research post. The use case that is in this page is use case #4
![StudentPage](Images\apply.png)

#### details page
On the details page it shal display the post analytics which is the number of applicants and list of applicants. The post details shall also be shown here as will.The use case that is in this page is use case #3
![StudentPage](Images\details.png)

#### creating post page
On the creating post page it will display a form toi create a research post that the user will input a title, description, qaulifivations, and research topic. Once the form is validated then the form will be sent to the db. It'll then be displayed on the Home page. The use case that is in this page is use case #1.
![FacultyPage](Images\createpost.png)

#### My profile Page
On the profile page it shall display the users information being their first name, last name, email, password, and phone number. You will also have the option to edit the user information.

#### my applications page
On the my applications page it will display the applications of the student the he/she applied for. It will also give the student the ability to cancel or delete the pending application as will. If the user deletes pending post then on the faculty my applicants page the applicant will no longer display there.The use case that is in this page is use case #12, #11, #9

#### my applicants page
On the my applicants page it will display a list of all the applicants tha applied to the research post positions. The faculty member will have options to update the status of the application as well.The use case that is in this page is use case #14, #13.



(***in iteration-1***) Brainstorm with your team members and identify the pages that you think should be created.  If you included most of the major pages, it will be acceptable. 




# 3. Progress Report

Write a short paragraph summarizing your progress in iteration1 / iteration2.

Iteration 1: Iteration 1 went smothly but there were some problems with branches and miscommunication. Even so we made sure to get everyone involved and made sure that everyone wasn't stuck with any problems. We currently have to many templates that can be shorten if we add logins/users to the application but nontheless we managed to give out a running demo.

# 4. Testing Plan



(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? 
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)

# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

CPTS 322 Lecture, Sakire Arslan Ay
CPTS 322 SmileAPP
CPTS 322 StudentAPP
Flask Documentation
HTML/CSS Documentation 


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