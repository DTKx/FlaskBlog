from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()
print(bcrypt.generate_password_hash('testing'))#B STANDS for bytes, GENERATES NEW HASHES EVERY TIME
print(bcrypt.generate_password_hash('testing').decode('utf-8'))#Now it is converted to string
hashed_pw=bcrypt.generate_password_hash('testing')
# AS it changes every time I need a method to verify if the password is actually this.
print(bcrypt.check_password_hash(hashed_pw,'password'))
print(bcrypt.check_password_hash(hashed_pw,'testing'))
