from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name = StringField("UserName", validators = [DataRequired()])
    password = PasswordField("Password",validators = [DataRequired()])
    submit = SubmitField("Sign In")

class SignupForm(FlaskForm):
    user_name = StringField("UserName", validators = [DataRequired()])
    password = PasswordField("Password",validators = [DataRequired()])
    submit = SubmitField("Sign In")
