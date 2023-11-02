from flask_wtf import FlaskForm
from app.Model.models import User
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email

class FacultyRegForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    firstname= StringField('Firstname', validators=[DataRequired()])
    lastname= StringField('Lastname', validators=[DataRequired()])
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
    firstname= StringField('firstname', validators=[DataRequired()])
    lastname= StringField('lastname', validators=[DataRequired()])
    GPA= StringField('GPA', validators=[DataRequired()])
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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')