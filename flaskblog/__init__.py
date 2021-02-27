from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='4ebebae9544f86c19558bc018c7ea517'# Secret Key protect form modified cookies,forgery attacks etc
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'# Location of our sqllite, /// represents a relative path this means that our file should be created in the module we are currently in right now.
db=SQLAlchemy(app)
from flaskblog import routes 