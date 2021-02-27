from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post


posts=[
    {
        'author':'Debora Kohara',
        'title':'Blog Post 1',
        'content': 'First post content: Hey you made this :) !',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Debora 2',
        'title':'Blog Post 2',
        'content': 'Second post content: Hey you made this :) !',
        'date_posted':'April 22,2018'
    }
]
@app.route("/")#ROOT PAGE OF OUR PAGE
@app.route("/home")#home also would work
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")#ROOT PAGE OF OUR PAGE
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])#ROOT PAGE OF OUR PAGE
# @app.route("/register")#ROOT PAGE OF OUR PAGE
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])#ROOT PAGE OF OUR PAGE
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)
