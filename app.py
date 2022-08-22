from flask import Flask, render_template, redirect, flash, session
from flask_cors import CORS, cross_origin
from functions import *
from loginform import LoginForm, SignupForm, SearchForm
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
    message = ''
    if form.validate_on_submit():
        message = user_login(form.user_name.data, hashlib.md5(form.password.data.encode()).hexdigest())
        if message == 'SUCCESS':
            session['user'] = form.user_name.data
            flash("Login Successful")
            return redirect('index')
    
    return render_template('login.html', form=form, message=message)
   
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    message = ''
    if form.validate_on_submit():
        #open database
        #check for user entry
        #create user entry
        #hash password
        #commit & close DB
        message = new_user_reg(form.user_name.data, hashlib.md5(form.password.data.encode()).hexdigest())
        if message=='SUCCESS':
            session['user'] = form.user_name.data
            flash("Welcome!")
            return redirect('/index')
        
    return render_template('signup.html', form=form, message=message)

@app.route('/logout', methods={'GET'})
def logout():
    session.pop("user", None)
    return redirect('login')

@app.route('/profile',methods={'GET'})
def profile():
    if 'user' not in session:
        return redirect('login')

    data = get_player_data(session['user'])
    if data == []:
        return f"<h1> Player '{session['user']}' not found in database.</h1><br> <a href='home'>Return to homepage</a>"
    return render_template('player.html', data=data)

@app.route('/search', methods={'GET','POST'})
def search():
    form = SearchForm()
    message = ''
    if form.validate_on_submit():
        if 'drop' in form.search.data or 'DROP' in form.search.data  or '*' in form.search.data or 'SELECT' in form.search.data or 'select' in form.search.data:
            return redirect('logout')
        data = get_player_data(form.search.data)
        if data == []:
            message = f"Player '{form.search.data}' not found"
            return render_template('search.html', form=form, message=message)
        return render_template('player.html', data=data)
    return render_template('search.html', form=form, message=message)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
