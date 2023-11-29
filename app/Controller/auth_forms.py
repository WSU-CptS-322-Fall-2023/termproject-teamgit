from flask_wtf import FlaskForm
from app.Model.models import User
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
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

class FacultyRegForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    firstname= StringField('First Name', validators=[DataRequired()])
    lastname= StringField('Last Name', validators=[DataRequired()])
    title= StringField('Title', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    password2 = PasswordField("Repeat Password", validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register ')

    def validate_username(self,username):
        username = User.query.filter_by(username=username.data).first()
        if username is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self,email):
        useremail = User.query.filter_by(email=email.data).first()
        if useremail is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        
class StudentRegForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    firstname= StringField('First Name', validators=[DataRequired()])
    lastname= StringField('Last Name', validators=[DataRequired()])
    GPA= StringField('GPA', validators=[DataRequired()])
    Major = StringField('Major', validators=[DataRequired()])
    Year = StringField('Grade Level', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    password2 = PasswordField("Repeat Password", validators= [DataRequired(), EqualTo('password')])
    tag = QuerySelectMultipleField( 'Research Interest', query_factory= get_researchinterest, get_label=get_researchinterestlabel, widget=ListWidget(prefix_label=False),option_widget=CheckboxInput() )
    tag2 = QuerySelectMultipleField( 'Research Skills', query_factory= get_researchskills, get_label=get_researchskillslabel, widget=ListWidget(prefix_label=False),option_widget=CheckboxInput() )
    submit = SubmitField('Register')

    def validate_username(self,username):
        username = User.query.filter_by(username=username.data).first()
        if username is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self,email):
        useremail = User.query.filter_by(email=email.data).first()
        if useremail is not None:
            raise ValidationError('The email already exists! Please use a different email address.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')