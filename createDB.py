import sqlite3

conn = sqlite3.connect('Database.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE if not exists doctor(name text, email text, password text, specialization text, contact_no int, PRIMARY KEY (email))''')
c.execute('''CREATE INDEX d_email ON doctor(email ASC)''')

c.execute('''CREATE TABLE if not exists patient(name text, email text, password text, DOB date, address text, contact_no int, blood_group text, PRIMARY KEY(email))''')
c.execute('''CREATE INDEX p_email ON patient(email ASC)''')

c.execute('''CREATE TABLE if not exists patientRecord2014(id int, email text, doc_email text, disease text, date date, PRIMARY KEY(id))''')
c.execute('''CREATE INDEX d_email_record2014 ON patientRecord2014(doc_email ASC)''')
c.execute('''CREATE INDEX p_email_record2014 ON patientRecord2014(email ASC)''')
c.execute('''CREATE INDEX date2014 ON patientRecord2014(date ASC)''')
c.execute('''CREATE INDEX disease2014 ON patientRecord2014(disease ASC)''')

c.execute('''CREATE TABLE if not exists patientSymptom2014(id int, symptom text, FOREIGN KEY(id) REFERENCES patientRecord2014(id))''')
c.execute('''CREATE INDEX id_symptom2014 ON patientSymptom2014(id ASC)''')

c.execute('''CREATE TABLE if not exists patientDrugs2014(id int, drugs text, FOREIGN KEY(id) REFERENCES patientRecord2014(id))''')
c.execute('''CREATE INDEX id_drugs2014 ON patientDrugs2014(id ASC)''')

c.execute('''CREATE TABLE if not exists patientRecord2013(id int, email text, doc_email text, disease text, date date, PRIMARY KEY(id))''')
c.execute('''CREATE INDEX d_email_record2013 ON patientRecord2013(doc_email ASC)''')
c.execute('''CREATE INDEX p_email_record2013 ON patientRecord2013(email ASC)''')
c.execute('''CREATE INDEX date2013 ON patientRecord2013(date ASC)''')
c.execute('''CREATE INDEX disease2013 ON patientRecord2013(disease ASC)''')

c.execute('''CREATE TABLE if not exists patientSymptom2013(id int, symptom text, FOREIGN KEY(id) REFERENCES patientRecord2013(id))''')
c.execute('''CREATE INDEX id_symptom2013 ON patientSymptom2013(id ASC)''')

c.execute('''CREATE TABLE if not exists patientDrugs2013(id int, drugs text, FOREIGN KEY(id) REFERENCES patientRecord2013(id))''')
c.execute('''CREATE INDEX id_drugs2013 ON patientDrugs2013(id ASC)''')

c.execute('''CREATE TABLE if not exists patientRecord2012(id int, email text, doc_email text, disease text, date date, PRIMARY KEY(id))''')
c.execute('''CREATE INDEX d_email_record2012 ON patientRecord2012(doc_email ASC)''')
c.execute('''CREATE INDEX p_email_record2012 ON patientRecord2012(email ASC)''')
c.execute('''CREATE INDEX date2012 ON patientRecord2012(date ASC)''')
c.execute('''CREATE INDEX disease2012 ON patientRecord2012(disease ASC)''')

c.execute('''CREATE TABLE if not exists patientSymptom2012(id int, symptom text, FOREIGN KEY(id) REFERENCES patientRecord2012(id))''')
c.execute('''CREATE INDEX id_symptom2012 ON patientSymptom2012(id ASC)''')

c.execute('''CREATE TABLE if not exists patientDrugs2012(id int, drugs text, FOREIGN KEY(id) REFERENCES patientRecord2012(id))''')
c.execute('''CREATE INDEX id_drugs2012 ON patientDrugs2012(id ASC)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
