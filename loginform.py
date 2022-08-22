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

class SearchForm(FlaskForm):
    search = StringField("Enter a Player Name to Search:", validators = [DataRequired()])
    submit = SubmitField("Search")
