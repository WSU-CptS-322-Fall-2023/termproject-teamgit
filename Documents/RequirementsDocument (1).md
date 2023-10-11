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

Students and falucucty handling reasearch posistions. Statkeholders is WSU becuase they provided a platform to thier constituents.

----
## 2.2 Use Cases


| Use case # 1      |   |
| ------------------ |--|
| Name              | "Create Research Position"  |
| Users             | "Faculty"  |
| Rationale         | "When a research position opens within a department a faculty member needs to find students. By creating a research post on a research platform, it allows students to see the position requirements and qualifications and allows faculty to find qualified applicants"|
| Triggers          | "Create research button is pressed"  |
| Preconditions     | "Is faculty member, web page rendered"  |
| Actions           | "Faculty inputs data into form with validator catches. Fields could be Title,Qualifications,Skills,Description,Major,ETC 2. Then the user could submit with the submit button"|
| Alternative paths | "If information in form is left blank or major isn't found, user will be prompted to change into accurate information,2. The Faculty can also abandon creation and go back to home"  |
| Postconditions    | "Position is created "  |
| Acceptance tests  | "Form is validated and submitted correctly"  |
| Iteration         | "1"  |



| Use case # 2    |   |
| ------------------ |--|
| Name              | "Main page, view all research post"  |
| Users             | "Students & Faculty"  |
| Rationale         | "view all open Research Posts"  |
| Triggers          | "clicking a link to the post description"  |
| Preconditions     | "Being a wsu student or faculty, posts are loaded in"  |
| Actions           | "clicking on the post"  |
| Alternative paths | "return back to main page or go back to main page"  |
| Postconditions    | "Research Post description page"  |
| Acceptance tests  | "url link works"  |
| Iteration         | "Iteration 1"  |

| Use case # 3     |   |
| ------------------ |--|
| Name              | "View Post"  |
| Users             | "Faculty,Student"  |
| Rationale         | "as a student look more indepth for details of post/position. as faculty see how you post looks/is doing"  |
| Triggers          | "Click view post button on post"  |
| Preconditions     | "webpage is rendered"  |
| Actions           | "View details about post, and later add functionality to apply" |
| Alternative paths | "Abort and find other posts or go back to main page "  |
| Postconditions    | "Post details should be rendered to screen"  |
| Acceptance tests  | "the post renders with correct information"  |
| Iteration         | "1" |



| Use case # 4      |   |
| ------------------ |--|
| Name              | "Apply for research position"  |
| Users             | "Students"  |
| Rationale         | "Student can apply for research position"  |
| Triggers          | "Student click the submit button"  |
| Preconditions     | "Be a wsu student and have to be in the description post page."  |
| Actions           | "1.Student will have to write a brief statement on why they want to apply  2.Student will provide both name and email of one faculty member who can provide a reference for the position."  |
| Alternative paths | "Cancel application or go back to the main page."  |
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
| Name              | "View research position and the status"  |
| Users             | "Students"  |
| Rationale         | "View research position applied for and the status of them"  |
| Triggers          | ""  |
| Preconditions     | "be logged in as a wsu student"  |
| Actions           | "1.applications will be displayed to the user 2.applications shall display the status, either being pending, approved for interview, hired, and not hired"  |
| Alternative paths | "main page or profile page"  |
| Postconditions    | "render applications and there status  |
| Acceptance tests  | "render the page"  |
| Iteration         | "Iteration 3"  |


| Use case # 12     |   |
| ------------------ |--|
| Name              | "Withdraw pending applications"  |
| Users             | "wsu Students"  |
| Rationale         | "Student is no longer interested in a research position, so they withdraw the application"  |
| Triggers          | "click withdraw button"  |
| Preconditions     | "be logged in a wsu student account and already have a pending application"  |
| Actions           | "1. Click on the withdraw button"  |
| Alternative paths | "cancel the withdraw"  |
| Postconditions    | "pending application will be deleted and no longer there"  |
| Acceptance tests  | "validate on submit and check if application is deleted"  |
| Iteration         | "Iteration 3"  |


| Use case # 13      |   |
| ------------------ |--|
| Name              | "approve research position application"  |
| Users             | "WSU faculty"  |
| Rationale         | "The faculty approves of student trying to apple for the research position and want to interview said student."  |
| Triggers          | "click submit button"  |
| Preconditions     | "Be logged in a wsu faculty account, already have a research positon post, and have a pending research position application on said post. "  |
| Actions           | "1. Faculty will have to first have to click on the select box for approved for interview on the research application of the student 2.Then click submit to update the application."  |
| Alternative paths | "cancel/update application"  |
| Postconditions    | "Students should have there pending application updated to Approved for Interview."  |
| Acceptance tests  | "Both faculty and student should see the application was approved for interview"  |
| Iteration         | "Iteration 3"  |


| Use case # 14      |   |
| ------------------ |--|
| Name              | “Hired not hired for student"  |
| Users             | "Students "  |
| Rationale         | "Student checking application status of research position they applied for"  |
| Triggers          | "Student is accepted or denied for a position"  |
| Preconditions     | "post is created and student has applied and is reviewed by faculty"  |
| Actions           | "Tells user what their application status is via a notification. "  |
| Alternative paths | "Main Page, apply to other posts,"  |
| Postconditions    | "Post is removed from applied posts"  |
| Acceptance tests  | "Was post denied or accept info correct, is post removed from current applications "  |
| Iteration         | "3"  |

| Use case # 15     |   |
| ------------------ |--|
| Name              | "Faculty can delete existing post
"  |
| Users             | "Faculty"  |
| Rationale         | "As a faculty member remove post either because they have fulfilled the position or position falls through"  |
| Triggers          | "Post requirements for students meet or faculty decides to remove position"  |
| Preconditions     | "Post is created and students have applied "  |
| Actions           | "delete post, all unaccepted students are send denied”  |
| Alternative paths | "view posts, homepage, edit post"  |
| Postconditions    | "Post is removed from db, and students are sent denied"  |
| Acceptance tests  | "check student status should be now denied ."  |
| Iteration         | "3"  |


## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. Account Security: All accounts login information will be confidenital
2. Web Browser Avalability: Research Scout will run on Google Chrome, Safari, and Edge
3. Computer First Design: Research Scout will be a web app designed for computers and laptops not mobile
4. User Accounts: Users will be able to create, add to and chnage details regarding their accounts. Ie: email username, address etc
5. Posts CRUD: Webapp will be able to supoort the creation, retrival, updating and deletion of research position posts
6. Search functionailty: Users will be able to search for specfic posts using keywords
7. Sort functionaility: Users will be able to filter for different reseach positions to help find relevant postions. Ie: Major,pay,location etc
8. Student applications: Students can apply to posts and thus can be reviewed by the Faculty advertising the position
----
# 3. User Interface

Here you should include the sketches or mockups for the main parts of the interface.

----
# 4. Product Backlog

https://github.com/WSU-CptS-322-Fall-2023/termproject-teamgit/issues/1

----
# 5. References

CPTS 322 Lecture, Sakire Arslan Ay
CPTS 322 SmileAPP
CPTS 322 StudentAPP
Flask Documentation
HTML/CSS Documentation 