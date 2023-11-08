from datetime import datetime
from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(120),unique=True,index=True)
    email = db.Column(db.String(120), unique =True, index = True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    user_type =db.Column(db.String(50))

    __mapper_args__ ={
        'polymorphic_identity': 'User', 'polymorphic_on':user_type
    }

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def get_password(self,password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "User %s" % self.name

Studentapp = db.Table(
    'student_apply_association',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('apply_id', db.Integer, db.ForeignKey('apply.id'))
)

Facultypost = db.Table(
    'faculty_researchpost_association',
    db.Column('faculty_id', db.Integer, db.ForeignKey('faculty.id')),
    db.Column('researchpost_id', db.Integer, db.ForeignKey('research_post.id'))
)

class Faculty(User):
    __tablename__='faculty'
    id = db.Column(db.ForeignKey("user.id"), primary_key =True)
    title = db.Column(db.String(64))
    research_posts = db.relationship('ResearchPost', secondary=Facultypost, backref='faculties')
    __mapper_args__ ={
        'polymorphic_identity': 'Faculty'
    }

class Student(User):
    __tablename__='student'
    id = db.Column(db.ForeignKey("user.id"), primary_key =True)
    GPA = db.Column(db.String(64))
    Major = db.Column(db.String(64))
    Year =  db.Column(db.String(64))
    Skills =  db.Column(db.String(300))
    applications = db.relationship('Apply', secondary=Studentapp, backref='students')

    __mapper_args__ ={
        'polymorphic_identity': 'Student'
    }

class ResearchPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(30))
    Description =  db.Column(db.String(100)) 
    Qualifications = db.Column(db.String(30)) 
    Major = db.Column(db.String(20)) 
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    applications = db.relationship('Apply', backref='research_post', lazy=True)


class Apply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    research_topic =  db.Column(db.String(30))
    statement =  db.Column(db.String(100))
    faculty_name = db.Column(db.String(30))
    faculty_email = db.Column(db.String(30))
    researchpost_id = db.Column(db.Integer, db.ForeignKey('research_post.id'), nullable=False)
