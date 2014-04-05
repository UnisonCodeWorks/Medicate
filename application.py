from flask import *
import time
import os
import sys
import sqlite3

app = Flask(__name__)
app.debug = True

#Creating Database
conn = sqlite3.connect('Database.db')
c = conn.cursor()

#Creating tables

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
    return render_template("login.html", errorVar="")

@app.route('/loggedin', methods=['POST'])
def loggedin():
	email = request.form["email"]
	password = request.form["password"]
	value = request.form["optionsRadios"]
	conn = sqlite3.connect('Databa.db')
	c = conn.cursor()
	if value=="patient":
		result = c.execute('select count(*) from person where email = ? and password = ?', (email, password,))
		for row in result:
			if row[0] == 1:
				conn.close()
				return render_template("pDashboard.html")
			else:
				conn.close()
				return render_template("login.html", errorVar="""Record not found. Try again.""")
	else:
		result = c.execute('select count(*) from doctor where email = ? and password = ?', (email, password,))
		for row in result:
			if row[0] == 1:
				conn.close()
				return render_template("dDashboard.html")
			else:
				conn.close()
				return render_template("login.html", errorVar="""Record not found. Try again.""")
	

@app.route('/registration')
def registration():
    return render_template("registration.html", errorVar="")

@app.route('/docRegistration')
def docRegistration():
    return render_template("docRegistration.html", errorVar="")

@app.route('/register', methods=['POST'])
def register():
	name = request.form["name"]
	email = request.form["email"]
	password = request.form["password"]
	dob = request.form["dob"]
	address = request.form["address"]
	contact = request.form["contact"]
	blood = request.form["optionsRadios"]
	
	conn = sqlite3.connect('Databa.db')
	c = conn.cursor()
	result = c.execute('select count(*) from person where email = ? ', (email,))
	for row in result:
		if row[0]==1:
			conn.close()
			return render_template("registration.html", errorVar="Email address already in use.")
		else:
			c.execute('INSERT INTO person VALUES (?,?,?,?,?,?,?)', (name, email, password, dob, address, contact, blood))
			conn.commit()
			conn.close()
			return render_template("pDashboard.html")

@app.route('/docRegister', methods=['POST'])
def docRegister():
	name = request.form["name"]
	email = request.form["email"]
	password = request.form["password"]
	specialisation = request.form["specialisation"]
	contact = request.form["contact"]
	
	conn = sqlite3.connect('Databa.db')
	c = conn.cursor()
	result = c.execute('select count(*) from doctor where email = ? ', (email,))
	for row in result:
		if row[0]==1:
			conn.close()
			return render_template("docRegistration.html", errorVar="Email address already in use.")
		else:
			c.execute('INSERT INTO doctor VALUES (?,?,?,?,?)', (name, email, password, specialisation, contact))
			conn.commit()
			conn.close()
			return render_template("dDashboard.html")

if __name__ == '__main__':
    app.run(threaded=True)
