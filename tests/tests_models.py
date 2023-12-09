import warnings

warnings.filterwarnings("ignore")
import os

basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import (
    Faculty,
    ResearchPost,
    Student,
    User,
    researchinterest,
    researchskills,
    Apply,
    userInterest,
    userSkill,
)
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    ROOT_PATH = "..//" + basedir


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username="john", email="john.yates@wsu.edu")
        u.set_password("covid")
        self.assertFalse(u.get_password("flu"))
        self.assertTrue(u.get_password("covid"))

    def test_user_creation(self):
        user = User(username="testuser", email="test@example.com")
        user.set_password("testpassword")
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(user.id)

    def test_post_creation(self):
        post = ResearchPost(
            title="Test Post",
            Description="Test Description",
            Qualifications="Test Qualifications",
            Major="Test Major",
            timestamp=datetime.utcnow(),
        )
        db.session.add(post)
        db.session.commit()
        self.assertIsNotNone(post.id)

    def test_application_creation(self):
        post = ResearchPost(
            title="Test Post",
            Description="Test Description",
            Qualifications="Test Qualifications",
            Major="Test Major",
            timestamp=datetime.utcnow(),
        )
        db.session.add(post)
        db.session.commit()

        application = Apply(
            research_topic="Test Topic",
            statement="Test Statement",
            faculty_name="Test Faculty",
            faculty_email="faculty@example.com",
            researchpost_id=post.id,
            status="Pending",
        )
        db.session.add(application)
        db.session.commit()
        self.assertIsNotNone(application.id) #app is created
        self.assertIn(application, post.applications) #app is in the post


    def test_user_authentication(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        self.assertTrue(user.get_password('testpassword'))
        self.assertFalse(user.get_password('wrongpassword'))
    
    
    def test_student_creation(self):
        student = Student(username='student1', email='student1@example.com', GPA='3.5', Major='Computer Science', Year='Junior')
        student.set_password('student_password')
        db.session.add(student)
        db.session.commit()
        self.assertIsNotNone(student.id)


    def test_student_applications(self):
        student = Student(username='student1', email='student1@example.com', GPA='3.5', Major='Computer Science', Year='Junior')
        student.set_password('student_password')
        db.session.add(student)
        
        post1 = ResearchPost(title='Research Post 1', Description='Desc 1', Qualifications='Qualif 1', Major='Major 1', timestamp=datetime.utcnow())
        post2 = ResearchPost(title='Research Post 2', Description='Desc 2', Qualifications='Qualif 2', Major='Major 2', timestamp=datetime.utcnow())
        
        db.session.add(post1)
        db.session.add(post2)
        db.session.commit()

        application1 = Apply(research_topic='Topic 1', statement='Statement 1', faculty_name='Faculty 1', faculty_email='faculty1@example.com', researchpost_id=post1.id, status='Pending')
        application2 = Apply(research_topic='Topic 2', statement='Statement 2', faculty_name='Faculty 2', faculty_email='faculty2@example.com', researchpost_id=post2.id, status='Pending')
        
        db.session.add(application1)
        db.session.add(application2)
        db.session.commit()

        student.applications.append(application1)
        student.applications.append(application2)
        db.session.commit()

        self.assertEqual(len(student.applications), 2) # tests amount of posts
        self.assertIn(application2, student.applications) #compare element cuz cant compare app

    def test_faculty_creation(self):
        faculty_member = Faculty(username='faculty1', email='faculty1@gmail.com', title='Professor')
        faculty_member.set_password('faculty_password')
        db.session.add(faculty_member)
        db.session.commit()
        self.assertIsNotNone(faculty_member.id)

    def test_faculty_research_posts(self):
        faculty_member = Faculty(username='faculty1', email='faculty1@gmail.com', title='Professor')
        faculty_member.set_password('faculty_password')
        db.session.add(faculty_member)
        
        post1 = ResearchPost(title='Research Post 1', Description='Desc 1', Qualifications='Qualif 1', Major='Major 1', timestamp=datetime.utcnow())
        post2 = ResearchPost(title='Research Post 2', Description='Desc 2', Qualifications='Qualif 2', Major='Major 2', timestamp=datetime.utcnow())
        
        faculty_member.research_posts.append(post1)
        faculty_member.research_posts.append(post2)
        db.session.commit()

        self.assertEqual(len(faculty_member.research_posts), 2) #posts are associagted with faculty

if __name__ == "__main__":
    unittest.main()
