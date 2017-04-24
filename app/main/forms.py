from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
