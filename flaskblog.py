# Part 1
#To run:
# Activate venv
# CMD set FLASK_APP=flaskblog.py
# CMD flask run
# Open the http server, note that the http://(ipaddress):5000 can be replaced by http://localhost:5000/ for security issues
# Note: To avoid restarting server every time we modify, we can view in debug mode
# CMD set FLASK_DEBUG=1
# Note: To run directly and protecting for the script being run directly use if __name__ then all one has to do is run the script

# Part 2
# Use html Templates
# Use template inheritance to avoid repeat code
# Use a bootstrap example for a quick framework https://getbootstrap.com/docs/5.0/getting-started/introduction/#quick-start
# Add some buttons

# Part 3
# Forms and User Input
# Create a registration page, leverage from extensions that makes all 

# Part 4
# Client database
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY']='4ebebae9544f86c19558bc018c7ea517'# Secret Key protect form modified cookies,forgery attacks etc
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'# Location of our sqllite, /// represents a relative path this means that our file should be created in the module we are currently in right now.
db=SQLAlchemy(app)

# Creates user models
class User(db.Model):
    # Creates Columns of our database
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)#nullable, means we need to have one
    email=db.Column(db.String(120),unique=True,nullable=False)#nullable, means we need to have one
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)#It will be hashable
    posts=db.relationship('Post',backref='author',lazy=True)#One to many, backref allows retrieve all authors, lazy allow to query. Under the hood this is actually creating a sql query. Post is upper case becauese we are referencing the class

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)#nullable each post have an author, user is lower case because we are referencing a table name that is automatically lowered

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


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

if __name__ == "__main__":#This is only true if we run the script directly
    app.run(debug=True)