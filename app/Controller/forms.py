from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import  DataRequired, Length

from app.Model.models import Post

