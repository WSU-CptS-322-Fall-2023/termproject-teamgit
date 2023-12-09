"""
This file contains the functional tests for the routes.
These tests use GETs and POSTs to different URLs to check for the proper behavior.
Resources:
    https://flask.palletsprojects.com/en/1.1.x/testing/ 
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/ 
"""
import os
import pytest
from app import create_app, db
from app.Model.models import User, Faculty, Student, ResearchPost, Apply, researchinterest, researchskills
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True



@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield  testing_client 
    # this is where the testing happens!
 
    ctx.pop()

def new_faculty(uname, ufirst,ulast, uemail,utitle, passwd):
    user = Faculty(username=uname,firstname=ufirst,lastname=ulast,email=uemail,title = utitle, user_type="Faculty" )
    user.set_password(passwd)
    return user

def new_student(uname,ufirst,ulast,uGPA,umajor, uyear, uemail,passwd):
    user = Student(username=uname, firstname=ufirst,lastname=ulast, 
                   GPA=uGPA, email=uemail, Major = umajor, Year = uyear,user_type="Student")
    user.set_password(passwd)
    return user


def init_interest():
    # initialize the 
    if researchinterest.query.count() == 0:
        tags = ['Machine Learning','High Performance Computing', 'Bioinformatics', 'Software Engineering', 'Electronic Design Automation']
        for t in tags:
            db.session.add(researchinterest(name=t))
        db.session.commit()
        print(tags)
    return None

def init_skills():
    # initialize the 
    if researchskills.query.count() == 0:
        tags = ['Python','Java', 'C', 'C++', 'C#']
        for t in tags:
            db.session.add(researchskills(name=t))
        db.session.commit()
        print(tags)
    return None

@pytest.fixture
def init_database():
    # Create the database and the database table
    db.create_all()
    # initialize the skills
    init_skills()
    # initialize the interests
    init_interest()
    #add a faculty   
    user1 = new_faculty(uname='fred', ufirst='fredword',ulast='fernan',uemail='fred@wsu.edu',utitle='Engineering',passwd='1234')
    # Insert user data
    db.session.add(user1)
    #add a student   
    user2 = new_student(uname='rudy', ufirst='rowdy',ulast='leonardo',uemail='rudy@wsu.edu',uGPA='3.45',umajor= 'Computer Science',uyear= '2024',passwd='1234')
    # Insert user data
    db.session.add(user2)
    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

def test_register_page(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get('/faculty_reg')
    assert response.status_code == 200
    assert b"Register" in response.data

    response = test_client.get('/student_reg')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_register(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' form is submitted (POST)
    THEN check that the response is valid and the database is updated correctly
    """
    # Create a test client using the Flask application configured for testing
    # Faculty register
    response = test_client.post('/faculty_reg', 
                          data=dict(username='john', firstname='john',lastname='Adams',title='Engineering',email='john@wsu.edu',password="bad-bad-password",password2="bad-bad-password"),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(User.username=='john')
    assert s.first().email == 'john@wsu.edu'
    assert s.count() == 1
    assert b"Sign In" in response.data   
    assert b"Please log in to access this page." in response.data

    # Student register
    tags1 = list( map(lambda t: t.id, researchinterest.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags2 = list( map(lambda t: t.id, researchskills.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    print("TESTING********************: ", tags1)
    print("TESTING********************: ", tags2)
    response = test_client.post('/student_reg', 
                           data=dict(username='steve', firstname='steve',lastname='Adams',email='steve@wsu.edu',GPA='3.22',Major= 'computer science',Year='2024',tag=tags1,tag2=tags2, password="bad-bad-password",password2="bad-bad-password"),
                           follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(User.username=='steve')
    assert s.first().email == 'steve@wsu.edu'
    assert s.count() == 1
    assert b"Sign In" in response.data   
    assert b"Please log in to access this page." in response.data

def test_invalidlogin(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with wrong credentials
    THEN check that the response is valid and login is refused 
    """
    response = test_client.post('/login', 
                          data=dict(username='sakire', password='12345',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data  #You may update the assertion condition according to the content of your login page. 

def test_login_logout(request,test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with correct credentials
    THEN check that the response is valid and login is succesfull 
    """
    # Faculty Login/logout
    response = test_client.post('/login', 
                          data=dict(username='fred', password='1234',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
  #  assert b"Please log in to access this page." in response.data   #  #You may update the assertion condition according to the content of your  page. 

    # Student Login/Logout
    response = test_client.post('/login', 
                          data=dict(username='rudy', password='1234',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
  #  assert b"Please log in to access this page." in response.data   #  #You may update the assertion condition according to the content of your  page.





def test_postresearch(test_client,init_database):
    """
    GIVEN a Flask application configured for testing , after user logs in,
    WHEN the '/postsmile' page is requested (GET)  AND /PostForm' form is submitted (POST)
    THEN check that response is valid and the class is successfully created in the database
    """
    #login
    response = test_client.post('/login', 
                        data=dict(username='fred', password='1234',remember_me=False),
                        follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data
    
    #test the "PostSmile" form 
    response = test_client.get('/addReasearch')
    assert response.status_code == 200
    #assert b"Post New Research position" in response.data #You may update the assertion condition according to the content of your  page.
    
    #test posting a smile story
    tags1 = list( map(lambda t: t.id, researchinterest.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags2 = list( map(lambda t: t.id, researchskills.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    print("TESTING********************: ", tags1)
    print("TESTING********************: ", tags2)
    response = test_client.post('/addReasearch', 
                          data=dict(title='My test post', description='This is my first test post.',qualifications= '4.0 GPA',major= 'CS',tag=tags1, tag2=tags2 ),
                          follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data

    c = db.session.query(ResearchPost).filter(ResearchPost.title =='My test post')
    assert c.first().get_interests().count() == 3 #should have 3 tags
    assert c.first().get_skills().count() == 3 #should have 3 tags
    assert c.count() >= 1 #There should be at least one post with body "Here is another post."


    tags3 = list( map(lambda t: t.id, researchinterest.query.all()[1:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags4 = list( map(lambda t: t.id, researchskills.query.all()[1:3]))
    print("TESTING********************: ", tags3)
    print("TESTING********************: ", tags4)
    response = test_client.post('/addReasearch', 
                          data=dict(title='Second post', description='Here is another post.',qualifications= '4.0 GPA',major= 'ME',tag=tags3, tag2=tags4),
                          follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data

    c = db.session.query(ResearchPost).filter(ResearchPost.title =='Second post')
    assert c.first().get_interests().count() == 2  # Should have 2 tags
    assert c.first().get_skills().count() == 2  # Should have 2 tags
    assert c.count() >= 1 #There should be at least one post with body "Here is another post."

    assert db.session.query(ResearchPost).count() == 2

    #finally logout
    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
  #  assert b"Please log in to access this page." in response.data #  #You may update the assertion condition according to the content of your  page.

def test_applypost(test_client,init_database):
    """
    GIVEN a Flask application configured for testing , after user logs-in,
     /like form is submitted (POST)
    THEN check that response is valid and the like count is updated in the database
    """
    #login
    response = test_client.post('/login', 
                        data=dict(username='fred', password='1234',remember_me=False),
                        follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data
    
    #first post two smile stories
    response = test_client.get('/addResearch')
    tags1 = list( map(lambda t: t.id, researchinterest.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags2 = list( map(lambda t: t.id, researchskills.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    print("TESTING********************: ", tags1)
    print("TESTING********************: ", tags2)
    response = test_client.post('/addReasearch', 
                          data=dict(title='My test post', description='This is my first test post.',qualifications= '4.0 GPA',major= 'CS',tag=tags1, tag2=tags2 ),
                          follow_redirects = True)
    assert response.status_code == 200
    c1 = db.session.query(ResearchPost).filter(ResearchPost.title =='My test post')
    assert c1.count() >= 1 #There should be at least one post with body "Here is another post."


    tags3 = list( map(lambda t: t.id, researchinterest.query.all()[1:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags4 = list( map(lambda t: t.id, researchskills.query.all()[1:3]))
    print("TESTING********************: ", tags3)
    print("TESTING********************: ", tags4)
    response = test_client.post('/addReasearch', 
                          data=dict(title='Second post', description='Here is another post.',qualifications= '4.0 GPA',major= 'ME',tag=tags3, tag2=tags4),
                          follow_redirects = True)
    assert response.status_code == 200
    c2 = db.session.query(ResearchPost).filter(ResearchPost.Description =='Here is another post.')
    assert c2.count() >= 1 #There should be at least one post with body "Here is another post.
    assert db.session.query(ResearchPost).count() == 2

    #logout
    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data

    response = test_client.post('/login', 
                        data=dict(username='rudy', password='1234',remember_me=False),
                        follow_redirects = True)
    assert response.status_code == 200

    response = test_client.post('/apply/'+str(c1.first().id), 
                          data=dict(statement='I would Like to apply for this position', faculty_name= 'Sakire',faculty_email='sakire@wsu.edu'),
                          follow_redirects = True)
    assert response.status_code == 200
    c3 = db.session.query(Apply).filter(Apply.statement =='I would Like to apply for this position')
    assert c3.count() >= 1 #There should be at least one post with body "Here is another post.
    assert db.session.query(Apply).count() == 1

    #finally logout
    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data


    
def test_deletepost(test_client,init_database):
    """
    GIVEN a Flask application configured for testing , after user logs-in,
     /like form is submitted (POST)
    THEN check that response is valid and the like count is updated in the database
    """
    #login
    response = test_client.post('/login', 
                        data=dict(username='fred', password='1234',remember_me=False),
                        follow_redirects = True)
    assert response.status_code == 200
    #assert b"Welcome to the Research Portal" in response.data
    
    #first post two smile stories
    response = test_client.get('/addResearch')
    tags1 = list( map(lambda t: t.id, researchinterest.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags2 = list( map(lambda t: t.id, researchskills.query.all()[:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    print("TESTING********************: ", tags1)
    print("TESTING********************: ", tags2)
    response = test_client.post('/addReasearch', 
                          data=dict(title='My test post', description='This is my first test post.',qualifications= '4.0 GPA',major= 'CS',tag=tags1, tag2=tags2 ),
                          follow_redirects = True)
    assert response.status_code == 200
    c1 = db.session.query(ResearchPost).filter(ResearchPost.title =='My test post')
     #There should be at least one post with body "Here is another post."


    tags3 = list( map(lambda t: t.id, researchinterest.query.all()[1:3]))  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
    tags4 = list( map(lambda t: t.id, researchskills.query.all()[1:3]))
    print("TESTING********************: ", tags3)
    print("TESTING********************: ", tags4)
    response = test_client.post('/addReasearch', 
                          data=dict(title='Second post', description='Here is another post.',qualifications= '4.0 GPA',major= 'ME',tag=tags3, tag2=tags4),
                          follow_redirects = True)
    assert response.status_code == 200
    c2 = db.session.query(ResearchPost).filter(ResearchPost.Description =='Here is another post.')
     #There should be at least one post with body "Here is another post.
    assert db.session.query(ResearchPost).count() == 2

    #Delete one post
    response = test_client.post('/delete/'+str(c1.first().id), 
                          data={},
                          follow_redirects = True)
    assert response.status_code == 200
    #Check if there is one post
    assert c1.count() == 0
    assert db.session.query(ResearchPost).count() == 1










   

    