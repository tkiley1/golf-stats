from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name = StringField("UserName", validators = [])
    password = PasswordField("Password",validators = [])
    submit = SubmitField("Sign In")
