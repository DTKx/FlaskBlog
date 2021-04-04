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

# Part 5
# Structure to Package
import timeit
from flaskblog import app

if __name__ == "__main__":#This is only true if we run the script directly
    app.run(debug=True)