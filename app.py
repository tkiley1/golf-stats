from flask import Flask, render_template, redirect, flash, session
from flask_cors import CORS, cross_origin
from functions import *
from loginform import LoginForm, SignupForm
import hashlib

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = "Wii Golf"


@app.route('/')
@app.route('/index')
@cross_origin(supports_credentials = True)
def hello():
    if "user" not in session:
        return redirect('login')
    return render_template('home.html', data = get_match_data())

    #return str(get_match_data())

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if user_login(form.user_name.data, hashlib.md5(form.password.data.encode()).hexdigest()):
            session['user'] = form.user_name.data
            flash("Login Successful")
            return redirect('index')
    flash("login Incorrect")
    return render_template('login.html', form=form)
   
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        #open database
        #check for user entry
        #create user entry
        #hash password
        #commit & close DB
        if new_user_reg(form.user_name.data, hashlib.md5(form.password.data.encode()).hexdigest()):
            session['user'] = form.user_name.data
            flash("Welcome!")
            return redirect('/index')
    flash("Username taken.  Try a different one.")
    return render_template('signup.html', form=form)

@app.route('/logout', methods={'GET'})
def logout():
    session.pop("user", None)
    return redirect('login')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
