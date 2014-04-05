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

#Global Variables
recordID = 0

#Creating tables

@app.route('/')
@app.route('/index')
def index():
	email = request.cookies.get("email")
	value = request.cookies.get("value")
	if email==None or value==None:
		resp = make_response(render_template("index.html"))
		resp.set_cookie('email', '', expires=0)
		resp.set_cookie('value', '', expires=0)
		return resp
	else:
		if value=="patient":
			return render_template("pDashboard.html")
		elif value=="doctor":
			return render_template("dDashboard.html")
		else:
			resp = make_response(render_template("index.html"))
			resp.set_cookie('email', '', expires=0)
			resp.set_cookie('value', '', expires=0)
			return resp

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/trend')
def trend():
    return render_template("trend.html")

@app.route('/login')
def login():
    return render_template("login.html", errorVar="")

@app.route('/logout')
def logout():
    resp = make_response(render_template("index.html"))
    resp.set_cookie('email', '', expires=0)
    resp.set_cookie('value', '', expires=0)
    return resp

@app.route('/loggedin', methods=['POST'])
def loggedin():
	email = request.form["email"]
	password = request.form["password"]
	value = request.form["optionsRadios"]
	conn = sqlite3.connect('Databa.db')
	c = conn.cursor()
	if value=="patient":
		result = c.execute('select count(*) from patient where email = ? and password = ?', (email, password,))
		for row in result:
			if row[0] == 1:
				conn.close()
				resp = make_response(render_template("pDashboard.html"))
				resp.set_cookie("email", email, 1800)
				resp.set_cookie("value", value, 1800)
				return resp
			else:
				conn.close()
				return render_template("login.html", errorVar="""Record not found. Try again.""")
	else:
		result = c.execute('select count(*) from doctor where email = ? and password = ?', (email, password,))
		for row in result:
			if row[0] == 1:
				conn.close()
				resp = make_response(render_template("dDashboard.html"))
				resp.set_cookie("email", email, 1800)
				resp.set_cookie("value", value, 1800)
				return resp
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
	result = c.execute('select count(*) from patient where email = ? ', (email,))
	for row in result:
		if row[0]==1:
			conn.close()
			return render_template("registration.html", errorVar="Email address already in use.")
		else:
			c.execute('INSERT INTO patient VALUES (?,?,?,?,?,?,?)', (name, email, password, dob, address, contact, blood))
			conn.commit()
			conn.close()
			resp = make_response(render_template("pDashboard.html"))
			resp.set_cookie("email", email, 1800)
			resp.set_cookie("value", "patient", 1800)
			return resp

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
			resp = make_response(render_template("dDashboard.html"))
			resp.set_cookie("email", email, 1800)
			resp.set_cookie("value", "doctor", 1800)
			return resp


@app.route('/newEntry')
def newEntry():
	email = request.cookies.get("email")
	value = request.cookies.get("value")
	if email==None or value==None:
		resp = make_response(render_template("login.html"))
		resp.set_cookie('email', '', expires=0)
		resp.set_cookie('value', '', expires=0)
		return resp
	else:
		if value=="patient":
			return render_template("pNewEntry.html")
		elif value=="doctor":
			return render_template("dNewEntry.html")
		else:
			resp = make_response(render_template("login.html"))
			resp.set_cookie('email', '', expires=0)
			resp.set_cookie('value', '', expires=0)
			return resp

@app.route('/submitEntry', methods=['POST'])
def submitEntry():
	global recordID
	email = request.cookies.get("email")
	value = request.cookies.get("value")
	if email==None or value==None:
		resp = make_response(render_template("login.html"))
		resp.set_cookie('email', '', expires=0)
		resp.set_cookie('value', '', expires=0)
		return resp
	else:
		if value=="patient":
			doc_email = request.form["email"]
			startDate = request.form["startDate"]
			endDate = request.form["endDate"]
			disease = request.form["disease"]
			drugs = request.form["drugs"]
			symptoms = request.form["symptoms"]
			conn = sqlite3.connect('Databa.db')
			c = conn.cursor()
			c.execute('INSERT INTO patientRecord VALUES (?,?,?,?,?,?)', (recordID, email, doc_email, disease, startDate, endDate))
			for it in symptoms.split(','):
				c.execute('INSERT INTO patientSymptom VALUES (?,?)', (recordID, it))
			for it in drugs.split(','):
				c.execute('INSERT INTO patientDrugs VALUES (?,?)', (recordID, it))
			conn.commit()
			conn.close()
			recordID += 1
			return render_template("pDashboard.html")
		elif value=="doctor":
			doc_email = email
			email = request.form["email"]
			startDate = request.form["startDate"]
			endDate = request.form["endDate"]
			disease = request.form["disease"]
			drugs = request.form["drugs"]
			symptoms = request.form["symptoms"]
			conn = sqlite3.connect('Databa.db')
			c = conn.cursor()
			c.execute('INSERT INTO patientRecord VALUES (?,?,?,?,?,?)', (recordID, email, doc_email, disease, startDate, endDate))
			for it in symptoms.split(','):
				c.execute('INSERT INTO patientSymptom VALUES (?,?)', (recordID, it))
			for it in drugs.split(','):
				c.execute('INSERT INTO patientDrugs VALUES (?,?)', (recordID, it))
			conn.commit()
			conn.close()
			recordID += 1
			return render_template("dDashboard.html")
		else:
			resp = make_response(render_template("login.html"))
			resp.set_cookie('email', '', expires=0)
			resp.set_cookie('value', '', expires=0)
			return resp


if __name__ == '__main__':
    app.run(threaded=True)
