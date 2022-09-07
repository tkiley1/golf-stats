from flask import Flask, render_template, redirect, flash, session
from flask_cors import CORS, cross_origin
from functions import *
from loginform import LoginForm, SignupForm, SearchForm, ScoreForm
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
        if hashlib.md5(form.password.data.encode()).hexdigest() == hashlib.md5(form.vpassword.data.encode()).hexdigest():
            message = new_user_reg(form.user_name.data, hashlib.md5(form.password.data.encode()).hexdigest())
            if message=='SUCCESS':
                session['user'] = form.user_name.data
                flash("Welcome!")
                return redirect('/index')
        else:
            message = "Passwords do not match."
        
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

@app.route('/score', methods ={'GET','POST'})
def score():
    form = ScoreForm()
    message = ''
    if form.validate_on_submit():
        check = insert_player_data(session['user'],form.h1.data,form.h2.data,form.h3.data,form.h4.data,form.h5.data,form.h6.data,form.h7.data,form.h8.data,form.h9.data,form.h10.data,form.h11.data,form.h12.data,form.h13.data,form.h14.data,form.h15.data,form.h16.data,form.h17.data,form.h18.data,form.tscore.data)
        if check:
            return render_template('score.html', form=form, message="Success")
        else:
            return render_template('score.html',form=form, message="Error")
    return render_template('score.html', form=form, message=message)



if __name__ == '__main__':
    app.run(host="0.0.0.0")
