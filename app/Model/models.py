from datetime import datetime
from app import db

class ResearchPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(30))
    Description =  db.Column(db.String(100)) 
    Qualifiications = db.Column(db.String(30)) 
    Major = db.Column(db.String(20)) 
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
