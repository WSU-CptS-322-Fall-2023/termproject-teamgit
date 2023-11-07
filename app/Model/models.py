from datetime import datetime
from app import db

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
