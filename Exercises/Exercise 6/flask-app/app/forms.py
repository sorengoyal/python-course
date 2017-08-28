from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired()])
