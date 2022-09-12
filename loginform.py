from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name = StringField("UserName", validators = [DataRequired()])
    password = PasswordField("Password",validators = [DataRequired()])
    submit = SubmitField("Sign In")

class SignupForm(FlaskForm):
    user_name = StringField("UserName", validators = [DataRequired()])
    password = PasswordField("Password",validators = [DataRequired()])
    vpassword = PasswordField("Validate Password", validators = [DataRequired()])
    submit = SubmitField("Sign Up")

class SearchForm(FlaskForm):
    search = StringField("Enter a Player Name to Search:", validators = [DataRequired()])
    submit = SubmitField("Search")

class ScoreForm(FlaskForm):
    h1 = IntegerField("", validators = [DataRequired()])
    h2 = IntegerField("", validators = [DataRequired()])
    h3 = IntegerField("", validators = [DataRequired()])
    h4 = IntegerField("", validators = [DataRequired()])
    h5 = IntegerField("", validators = [DataRequired()])
    h6 = IntegerField("", validators = [DataRequired()])
    h7 = IntegerField("", validators = [DataRequired()])
    h8 = IntegerField("", validators = [DataRequired()])
    h9 = IntegerField("", validators = [DataRequired()])
    h10 = IntegerField("", validators = [DataRequired()])
    h11 = IntegerField("", validators = [DataRequired()])
    h12 = IntegerField("", validators = [DataRequired()])
    h13 = IntegerField("", validators = [DataRequired()])
    h14 = IntegerField("", validators = [DataRequired()])
    h15 = IntegerField("", validators = [DataRequired()])
    h16 = IntegerField("", validators = [DataRequired()])
    h17 = IntegerField("", validators = [DataRequired()])
    h18 = IntegerField("", validators = [DataRequired()])
    tscore = IntegerField("", validators = [DataRequired()])
    submit = SubmitField("Subit Score")
    fields = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,tscore]
