# Software Requirements Specification

## ReasearchScout

Prepared by:

* `<Kyan Kotschevar-Smead>`,`<TeamGit>`
* `<Elliot Perez>`,`<TeamGit>`
* `<Fredy Fernandez>`,`<TeamGit>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

This section should provide an overview of the entire document

This document lists everything you would need to know about out implementation of Reasearch Scout, which includes,
Document Purpose, project scope, scoucment overview, requiremwents pecifications whihc consists of customers users and stakeholders, use cases non function requirements, user interface, product backlog, and refferences.
## 1.1 Document Purpose

This document is the preempt of our program. Every feature implentation and action can be traced back to this document. This document is an agreement for our Stakeholders for what the program should up like.
## 1.2 Product Scope


Research Scout is a Reserach posting platform where undergrad students can apply for various research postions offered by faculty. It will allow applicants to provide relevent resume information in a organized streamlined way. It also allows faculty to distingush thier reasearch postion by making a post to get qualifed applicants.


## 1.3 Document Overview

The rest of the document entails details regarding program implemention such as requirements specifications, user interface, profuct backlog, and References.
----
# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.


## 2.1 Customer, Users, and Stakeholders

Our Customer is Sakire, as she have given us instructions for how she wants her Research App. The Voiland College of engineering is a stakeholder as there will be more cohesion between students and faculty. Students will benefit as users becuase they will have easy and open acsess to view and apply to reserach oppertunies. Faculty will have a platform to recurit qualfied canadites for there positions.
----
## 2.2 Use Cases


| Use case # 1      |   |
| ------------------ |--|
| Name              | "Create Research Position"  |
| Users             | "Faculty"  |
| Rationale         | "When a research position opens within a department a faculty member needs to find students. By creating a research post on a research platform, it allows students to see the position requirements and qualifications and allows faculty to find qualified applicants"|
| Triggers          | "Create new Reseach option is selected"  |
| Preconditions     | "Is faculty member, web page rendered, Create new Reseach option is selected"  |
| Actions           | "Faculty inputs data into form with validator catches. Fields could be Title,Qualifications,Skills,Description,Major,ETC 2. Then the user could submit with the submit button"|
| Alternative paths | "If information in form is left blank or major isn't found, user will be prompted to change into accurate information,2. The Faculty can also abandon creation and go back to homepage"  |
| Postconditions    | "Position is created"  |
| Acceptance tests  | "Form is validated and submitted correctly"  |
| Iteration         | "1"  |



| Use case # 2    |   |
| ------------------ |--|
| Name              | "View all research posts"  |
| Users             | "Students"  |
| Rationale         | "As a Student i want to go through all research postion posts to see what is the right fit for me"  |
| Triggers          | "Main page  is rendered with posts"  |
| Preconditions     | "Being a wsu student, and all posts are rendered"  |
| Actions           | "View all research posts"  |
| Alternative paths | "View Specfic Position, Profile, Main Page"  |
| Postconditions    | "Research Post description page"  |
| Acceptance tests  | "Are all posts rendered"  |
| Iteration         | "Iteration 1"  |

| Use case # 3     |   |
| ------------------ |--|
| Name              | "View Specfic Research Post"  |
| Users             | "Faculty,Student"  |
| Rationale         | "as a student look more indepth for details of post/position. as faculty see how your post looks/is doing"  |
| Triggers          | "User selects view post option"  |
| Preconditions     | " Posts loaded and redered with correct info, User selects view post option"  |
| Actions           | "View details about post" |
| Alternative paths | "Abort and find other posts, Apply"  |
| Postconditions    | "Post details should be rendered to screen"  |
| Acceptance tests  | "the post renders with correct information"  |
| Iteration         | "1" |



| Use case # 4      |   |
| ------------------ |--|
| Name              | "Apply for research position"  |
| Users             | "Students"  |
| Rationale         | "Student can apply for research position"  |
| Triggers          | "Student selects apply option   |
| Preconditions     | "Be a wsu student and have to be in the description post page."  |
| Actions           | "1.Student will have to write a brief statement on why they want to apply  2.Student will provide both name and email of one faculty member who can provide a reference for the position. , 3. Student selects apply option"  |
| Alternative paths | "Cancel application, View post"  |
| Postconditions    | "position application sent to Faculty"  |
| Acceptance tests  | "Form is validated and submitted correctly"  |
| Iteration         | "Iteration 1"  |




| Use case # 5     |   |
| ------------------ |--|
| Name              | "Create student account"  |
| Users             | "student"  |
| Rationale         | "create an student account to apply for research positions"  |
| Triggers          | "Click to Register for students"  |
| Preconditions     | "Be wsu student and render register page"  |
| Actions           | "1.enter an account username that should be wsu email 2.enter account password. 3.enter contact information first & last name, wsu ID, email, phone."  |
| Alternative paths | "Go back to Sign In"  |
| Postconditions    | "Created a student account and sent to the db"  |
| Acceptance tests  | "Form is validated and submitted correctly"  |
| Iteration         | "Iteration 2"  |


| Use case # 6      |   |
| ------------------ |--|
| Name              | "Student Login"  |
| Users             | "Student"  |
| Rationale         | "Login to Student account in order to apply for research positions"  |
| Triggers          | "login button"  |
| Preconditions     | "Have a registered account as a wsu student member"  |
| Actions           | "1.Fill in login and password"  |
| Alternative paths | "Sign in page"  |
| Postconditions    | "Logged in and render main page"  |
| Acceptance tests  | "Form is validated and submitted correctly and student account is in the registered in the db"  |
| Iteration         | "Iteration 2"  |

| Use case # 7      |   |
| ------------------ |--|
| Name              | "Create faculty account"  |
| Users             | "Faculty"  |
| Rationale         | "create an faculty account to post research positions"  |
| Triggers          | "Click to Register for faculty"  |
| Preconditions     | "Be wsu Faculty and render register page"  |
| Actions           | "1.enter an account username that should be wsu email 2.enter account password. 3.enter contact informationfirst & last name, wsu ID, email, phone."  |
| Alternative paths | "Go back to Sign In"  |
| Postconditions    | "Created a Faculty account and sent to the db"  |
| Acceptance tests  | "Form is validated and submitted correctly & a Faculty member"  |
| Iteration         | "Iteration 2"  |

| Use case # 8      |   |
| ------------------ |--|
| Name              | "Faculty Login"  |
| Users             | "Faculty"  |
| Rationale         | "Login to Faculty account in order to access research posts and applications"  |
| Triggers          | "login button"  |
| Preconditions     | "Have a registered account as a wsu faculty member"  |
| Actions           | "1.Fill in login and password"  |
| Alternative paths | "Sign in page"  |
| Postconditions    | "Logged in and render main page"  |
| Acceptance tests  | "Form is validated and submitted correctly and faculty account is in the registered in the db"  |
| Iteration         | "Iteration 2"  |



| Use case # 9      |   |
| ------------------ |--|
| Name              | "See list of students who applied "  |
| Users             | "Faculty"  |
| Rationale         | "As a Faculty I want the best candidate possible for my research position. Thus i need to view all applicants thoroughly to determine the best"  |
| Triggers          | "see students button"  |
| Preconditions     | "Is signed in as faculty and has at least one post,post has applicants ."  |
| Actions           | "view specific applicant"  |
| Alternative paths | "Homepage, see a different applicant"  |
| Postconditions    | "be able to accept or deny students immediately"  |
| Acceptance tests  | "Is list of students accurate. "  |
| Iteration         | "2"  |




| Use case # 10      |   |
| ------------------ |--|
| Name              | "View qualifications of each student"  |
| Users             | "Faculty"  |
| Rationale         | "As Faculty Needs to see student profile of who applied to check if they are qualified for position via post"  |
| Triggers          | "Student applies on post allowing faculty to look"  |
| Preconditions     | "Post is created with student applied"  |
| Actions           | "Be able to accept application, or deny"  |
| Alternative paths | "back out to list of students, go to homepage"  |
| Postconditions    | "N/A"  |
| Acceptance tests  | "Is student info"  |
| Iteration         | "2"  |

| Use case # 11      |   |
| ------------------ |--|
| Name              | "View research position applied for and the status of them"  |
| Users             | "Students"  |
| Rationale         | "Students would like to see all of their research position applications and the status of them."  |
| Triggers          | "User would initate a link to profile which would direct it to the profile page"  |
| Preconditions     | "be logged in as a wsu student, profile page would have to render, student would also have already applied for a research position"  |
| Actions           | "1.Profile page would have to render, then there will be a list of applied research applications where the user can view and see the status of their application. "  |
| Alternative paths | "User can also see the more info of the research position application they sent."  |
| Postconditions    | "render applications and there status  |
| Acceptance tests  | "render the page"  |
| Iteration         | "Iteration 3"  |


| Use case # 12     |   |
| ------------------ |--|
| Name              | "Withdraw pending research position applications"  |
| Users             | "wsu Students"  |
| Rationale         | "Student is no longer interested in a research position, so they withdraw the application"  |
| Triggers          | "user initates withdraw"  |
| Preconditions     | "be logged in a wsu student account, be in the profile page, already have a pending application"  |
| Actions           | "User would have to render in the profile page where the list of research position will be displayed. The user then would initate the withdraw on the research position application."  |
| Alternative paths | "User can either initate the more info tab the research position application where it will direct the user to more information about the research position application."  |
| Postconditions    | "pending research position application will be deleted from the db, the faculty memember will no longer see the students research position application either."  |
| Acceptance tests  | "validate on submit and check if application is deleted"  |
| Iteration         | "Iteration 3"  |

| Use case # 13      |   |
| ------------------ |--|
| Name              | "Research position application status"  |
| Users             | "WSU faculty"  |
| Rationale         | "The faculty will have options of updating the status of the research position application of a student with the either approved for interview, Hired, or not hired"  |
| Triggers          | "user chooses either one of the three options to updated the status of the research position application"  |
| Preconditions     | "Be logged in a wsu faculty account, already have a research positon post, and have a pending research position application on said post, be on my applicants page "  |
| Actions           | "User will have displayed the list of pending research position applicants. each applications will have  more info box which will direct the user to the application descriptino of the applicant. After user gets the description applicaiton page then the user have a select box catagory which the user will initate. If user initates the Interview category then they will initate the update status which will update the application status. "  |
| Alternative paths | "If user chooses a different category for the status update like Hired then the status of the application should then change to hired, the same would go to not hired"  |
| Postconditions    | "Students should have there pending application status updated to either Approved for Interview, hired, or not hired. Faculty should have their applicants status updated as well."  |
| Acceptance tests  | "Both faculty and student should see the application was approved for interview"  |
| Iteration         | "Iteration 3"  |


| Use case # 14     |   |
| ------------------ |--|
| Name              | "Faculty can delete existing post
"  |
| Users             | "Faculty"  |
| Rationale         | "As a faculty member remove post either because they have fulfilled the position or position falls through"  |
| Triggers          | "Post requirements for students meet or faculty decides to remove position"  |
| Preconditions     | "Faculy is logged in into an account, their should be a research post, and be in the faculty page which shows all of their research position openings"  |
| Actions           | "User has the list of research position openings displayed. For each of the post there'll be delete option on them. The user can the choose to initate the delete option that will delete said post from the db."  |
| Alternative paths | ""  |
| Postconditions    | "Research application post is then deleted from the db and the students who applied for the research position application will then get a status updated that should say Position is not available"  |
| Acceptance tests  | "check of the research position post is delete from the db and if the students status is updated to position not available."  |
| Iteration         | "3"  |


## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. Account Security: All accounts login information will be confidenital
2. Web Browser Avalability: Research Scout will run on Google Chrome, Safari, and Edge
3. Computer First Design: Research Scout will be a web app designed for computers and laptops not mobile
4. Interfacing: Interface is easy to use and can be completed with clicks
----
# 3. User Interface
![Faculty Register](\Images\FacReg.png)
![Main](\Images\main.png)
![Sign-in](\Images\Sign-in.png)
![Student Details #1](\Images\stupro1.png)
![Student Details #2](\Images\stupro2.png)
![Student Registration](\Images\stuReg.png)
----
# 4. Product Backlog

https://github.com/WSU-CptS-322-Fall-2023/termproject-teamgit/issues/
# 5. References

CPTS 322 Lecture, Sakire Arslan Ay
CPTS 322 SmileAPP
CPTS 322 StudentAPP
Flask Documentation
HTML/CSS Documentation 