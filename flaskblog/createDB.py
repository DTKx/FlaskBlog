#Creates db file 
# It was runned in command line
from flaskblog import db,User,Post

db.create_all()

user_1=User(username='Corey',email='c@gmail.com',password='password')
db.session.add(user_1)
user_2=User(username='Debs',email='debs@gmail.com',password='password')
db.session.add(user_2)
db.session.commit() #Commit to the database

#Example of query to check
print(User.query.all())
print(User.query.first())
print(User.query.filter_by(username='Corey').all())
print(User.query.filter_by(username='Corey').first())
user_c=User.query.filter_by(username='Corey').first()
print(user_c)
print(user_c.id)
print(user_c.query.get(1))
print(user_c.posts)

post_1=Post(title='Blog1',content='First Post Content',user_id=user_c.id)
post_2=Post(title='Blog2',content='First Post Content',user_id=user_c.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()
print(user_c.posts)
for post in user_c.posts:
    print(post.title)
post_c=Post.query.first()
print(post_c.user_id)
print(post_c.author)#Works given backref
db.drop_all()#Drops all data so far
