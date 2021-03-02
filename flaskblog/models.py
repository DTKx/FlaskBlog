from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flaskblog import db,login_manager

@login_manager.user_loader

def load_user(user_id):
    """Manages Login

    Args:
        user_id ([type]): [description]

    Returns:
        [type]: [description]
    """

    return User.query.get(int(user_id))

# Creates user models
class User(db.Model,UserMixin):
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
