#To run:
# Activate venv
# CMD set FLASK_APP=flaskblog.py
# CMD flask run
# Open the http server, note that the http://(ipaddress):5000 can be replaced by http://localhost:5000/ for security issues
# Note: To avoid restarting server every time we modify, we can view in debug mode
# CMD set FLASK_DEBUG=1
# Note: To run directly and protecting for the script being run directly use if __name__ then all one has to do is run the script
from flask import Flask
app=Flask(__name__)

@app.route("/")#ROOT PAGE OF OUR PAGE
@app.route("/home")#home also would work
def hello():
    return "<h1>Home Page</h1>"#Header

@app.route("/about")#ROOT PAGE OF OUR PAGE
def about():
    return "<h1>About Page</h1>"#Header

if __name__ == "__main__":#This is only true if we run the script directly
    app.run(debug=True)