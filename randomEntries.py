import sys
import sqlite3
import random

def main():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')
	"""
	for i in range(100000):
		c.execute("INSERT INTO patient VALUES (?,?,?,?,?,?,?)", ("Name"+str(i+1),"email@patient"+str(i+1),"pass"+str(i+1),"1993-01-01","address","NULL","NULL"))
	for i in range(1000):
		c.execute("INSERT INTO doctor VALUES (?,?,?,?,?)", ("NameDoc"+str(i+1),"email@doc"+str(i+1),"pass"+str(i+1),"specialization"+str(random.randint(1,100)),"NULL"))
	"""
	disease = open("Disease.txt").readlines()
	symptom = open("Symptom.txt").readlines()
	drug = open("Drug.txt").readlines()
	recordID = 0
	for i in range(1000):
		for j in range(random.randint(0,20)):
			k = random.randint(0,199)
			c.execute('INSERT INTO patientRecord2012 VALUES (?,?,?,?,?)', (recordID, "email@patient"+str(i+1), "email@doc"+str(random.randint(1,1000)), disease[k].strip().decode('utf-8'), "2012-"+str(random.randint(1,12))+"-"+str(random.randint(1,28))))
			for it in symptom[k].split(','):
				c.execute('INSERT INTO patientSymptom2012 VALUES (?,?)', (recordID, it.strip().decode('utf-8')))
			for it in drug[k].split(','):
				c.execute('INSERT INTO patientDrugs2012 VALUES (?,?)', (recordID, it.strip().decode('utf-8')))
			recordID += 1
		print "Doing "+str(i+1)
	conn.commit()
	conn.close()

if __name__=='__main__':
	main()