from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,BooleanField
from wtforms.validators import  DataRequired, Length
from app.Model.models import ResearchPost




class ReasearchPostForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   description = StringField('Description', validators=[DataRequired()])
   qualifications = StringField('Qualification', validators=[DataRequired()])
   major = SelectField('Sort',choices = [('CS', 'Computer Science'), ('ME', 'Mechiancial Engineering'), ('BIO','Biology'),('EE','Electrical Engineering')])
   submit =SubmitField('Submit')

    
class SortForm(FlaskForm):
    myposts = BooleanField('Display my posts only ')
    submit = SubmitField('Refresh')