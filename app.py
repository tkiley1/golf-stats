from flask import Flask, render_template, redirect, flash, session
from flask_cors import CORS, cross_origin
from functions import *
from loginform import LoginForm

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = "Wii Golf"


@app.route('/')
@app.route('/index')
@cross_origin(supports_credentials = True)
def hello():
    if "user" not in session:
        return redirect('login')
    return str(get_match_data())

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print (form.user_name.data)
        session['user'] = form.user_name.data
        flash("Login Successful")
        return redirect('index')
    
    return render_template('login.html', form=form)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0')
