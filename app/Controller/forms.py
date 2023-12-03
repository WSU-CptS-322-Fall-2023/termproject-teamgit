from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,BooleanField, TextAreaField
from wtforms.validators import  DataRequired, Length, Email
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from app.Model.models import researchinterest, researchskills

def get_researchinterest():
    return researchinterest.query.all()

def get_researchinterestlabel(theresearchinterest):
    return theresearchinterest.name

def get_researchskills():
    return researchskills.query.all()

def get_researchskillslabel(theresearchskills):
    return theresearchskills.name


class ReasearchPostForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   description = StringField('Description', validators=[DataRequired()])
   qualifications = StringField('Qualification', validators=[DataRequired()])
   major = SelectField('Sort',choices = [('CS', 'Computer Science'), ('ME', 'Mechiancial Engineering'), ('BIO','Biology'),('EE','Electrical Engineering')])
   tag = QuerySelectMultipleField( 'Research Interest', query_factory= get_researchinterest, get_label=get_researchinterestlabel, widget=ListWidget(prefix_label=False),option_widget=CheckboxInput() )
   tag2 = QuerySelectMultipleField( 'Research Skills', query_factory= get_researchskills, get_label=get_researchskillslabel, widget=ListWidget(prefix_label=False),option_widget=CheckboxInput() )
   submit =SubmitField('Submit')

    
class SortForm(FlaskForm):
    choices = SelectField('Choices', choices=['Machine Learning','High Performance Computing', 'Bioinformatics', 'Software Engineering', 'Electronic Design Automation'])
    submit = SubmitField('Refresh')


class ApplicationForm(FlaskForm):
   statement = TextAreaField('Personal Statement', validators=[DataRequired()])
   faculty_name = StringField('Faculty Name', validators=[DataRequired()])
   faculty_email = StringField('Faculty Email', validators=[DataRequired(), Email()])
   status = StringField('')
   submit = SubmitField('Apply')
