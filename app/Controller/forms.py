from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import  DataRequired, Length
from app.Model.models import ResearchPost




class ReasearchPostForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   description = StringField('Title', validators=[DataRequired()])
   qualifications = StringField('Title', validators=[DataRequired()])
   major = SelectField('Sort',choices = [(1, 'Computer Science'), (2, 'Mechiancial Engineering'), (3,'Biology'),(4,'Electrical Engineering')])
   submit =SubmitField('Submit')

    
