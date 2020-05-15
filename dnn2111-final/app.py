# *******************************************************
# app
# Name : David Nieto
# UNI : dnn2111
# Final
# ENGI E1006

# Uses Flask to create an HTML website.
# *******************************************************

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static routes
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def engi_homepage():
    return render_template("1006.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()