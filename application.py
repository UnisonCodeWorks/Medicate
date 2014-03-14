from flask import *
import time
import os
import sys

app = Flask(__name__)

app.debug = True

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/trend')
def trend():
    return render_template("trend.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

if __name__ == '__main__':
    app.run(threaded=True)
