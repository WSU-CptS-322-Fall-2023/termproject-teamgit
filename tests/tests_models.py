import warnings

warnings.filterwarnings("ignore")
import os

basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import (
    ResearchPost,
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

    def test_research_post_creation(self):
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

    def test_apply_creation(self):
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


if __name__ == "__main__":
    unittest.main()
