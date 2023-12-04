from datetime import datetime
from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

postInterest=db.Table('postInterest',
                  db.Column('researchpost_id',db.Integer,db.ForeignKey('research_post.id')),
                  db.Column('researchinterest_id',db.Integer,db.ForeignKey('researchinterest.id')))

userInterest=db.Table('userInterest',
                  db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                  db.Column('researchinterest_id',db.Integer,db.ForeignKey('researchinterest.id')))

postSkill=db.Table('postSkill',
                  db.Column('researchpost_id',db.Integer,db.ForeignKey('research_post.id')),
                  db.Column('researchskills_id',db.Integer,db.ForeignKey('researchskills.id')))

userSkill=db.Table('userSkill',
                  db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                  db.Column('researchskills_id',db.Integer,db.ForeignKey('researchskills.id')))

class ResearchPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(30))
    Description =  db.Column(db.String(100)) 
    Qualifications = db.Column(db.String(30)) 
    Major = db.Column(db.String(20)) 
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    applications = db.relationship('Apply', backref='research_post', lazy=True)
    interests = db.relationship('researchinterest', secondary = postInterest,primaryjoin=(postInterest.c.researchpost_id == id), backref=db.backref('postInterest', lazy='dynamic'), lazy='dynamic')
    skills = db.relationship('researchskills', secondary = postSkill,primaryjoin=(postSkill.c.researchpost_id == id), backref=db.backref('postSkill', lazy='dynamic'), lazy='dynamic')
    def get_interests(self):
        return self.interests
    
    def get_skills(self):
        return self.skills


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
studentpost = db.Table(
    'student_researchpost_association',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('appun_id', db.Integer, db.ForeignKey('appun.id'))
)

class Faculty(User):
    __tablename__='faculty'
    id = db.Column(db.ForeignKey("user.id"), primary_key =True)
    title = db.Column(db.String(64))
    research_posts = db.relationship('ResearchPost', secondary=Facultypost, backref='faculties')
    posts = db.relationship('ResearchPost',backref='writer',lazy='dynamic')
    def get_user_posts(self):
        return self.posts
    __mapper_args__ ={
        'polymorphic_identity': 'Faculty'
    }

class Student(User):
    __tablename__='student'
    id = db.Column(db.ForeignKey("user.id"), primary_key =True)
    GPA = db.Column(db.String(64))
    Major = db.Column(db.String(64))
    Year =  db.Column(db.String(64))
    posts = db.relationship('appun',backref='writer',lazy='dynamic')
    applications = db.relationship('Apply', secondary=Studentapp, backref='students')
    interests = db.relationship('researchinterest', secondary = userInterest,primaryjoin=(userInterest.c.student_id == id), backref=db.backref('userInterest', lazy='dynamic'), lazy='dynamic')
    skills = db.relationship('researchskills', secondary = userSkill,primaryjoin=(userSkill.c.student_id == id), backref=db.backref('userSkill', lazy='dynamic'), lazy='dynamic')
    def get_user_app(self):
        return self.posts
    
    def userapply(self,post):
        for t in self.applications:
            if t.research_post.id == post.id:
                return 0

        return 1
    
    def userstatus(self,post):
        for t in self.applications:
            if t.research_post.id == post.id:
                return t.status
            
    def userwith(self,post):
        for t in self.applications:
            if t.research_post.id == post.id:
                return t.id
    
    def get_user_posts(self):
        return self.posts
    
    def get_interests(self):
        return self.interests
    
    def get_skills(self):
        return self.skills

    __mapper_args__ ={
        'polymorphic_identity': 'Student'
    }


class Apply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    research_topic =  db.Column(db.String(30))
    statement =  db.Column(db.String(100))
    faculty_name = db.Column(db.String(30))
    faculty_email = db.Column(db.String(30))
    researchpost_id = db.Column(db.Integer, db.ForeignKey('research_post.id'), nullable=False)
    status= db.Column(db.String(30))

class appun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    research_topic =  db.Column(db.String(30))
    statement =  db.Column(db.String(100))
    faculty_name = db.Column(db.String(30))
    faculty_email = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status= db.Column(db.String(30))
    
class researchinterest(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    def __repr__(self):
        return 'RI ID: {}, RI Name {}'.format(self.id,self.name)
    
class researchskills(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    def __repr__(self):
        return 'RS ID: {}, RS Name {}'.format(self.id,self.name)
