from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,BooleanField, TextAreaField
from wtforms.validators import  DataRequired, Length, Email
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from app.Model.models import ResearchPost,Tag
def get_tag():
    return Tag.query.all()

def get_taglabel(theTag):
    return theTag.name


class ReasearchPostForm(FlaskForm):
   title = StringField('Title', validators=[DataRequired()])
   description = StringField('Description', validators=[DataRequired()])
   qualifications = StringField('Qualification', validators=[DataRequired()])
   major = SelectField('Sort',choices = [('CS', 'Computer Science'), ('ME', 'Mechiancial Engineering'), ('BIO','Biology'),('EE','Electrical Engineering')])
   tag = QuerySelectMultipleField( 'Tag', query_factory= get_tag, get_label=get_taglabel, widget=ListWidget(prefix_label=False),option_widget=CheckboxInput() )
   submit =SubmitField('Submit')

    
class SortForm(FlaskForm):
    myposts = BooleanField('Display my posts only ')
    submit = SubmitField('Refresh')


class ApplicationForm(FlaskForm):
   research_topic = StringField('Research Topic', validators=[DataRequired()])
   statement = TextAreaField('Personal Statement', validators=[DataRequired()])
   faculty_name = StringField('Faculty Name', validators=[DataRequired()])
   faculty_email = StringField('Faculty Email', validators=[DataRequired(), Email()])
   submit = SubmitField('Apply')
