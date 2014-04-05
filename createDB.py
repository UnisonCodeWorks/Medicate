import sqlite3

conn = sqlite3.connect('Databa.db')

c = conn.cursor()

#Drop Previous Tables
#c.execute('''drop table doctor''')
#c.execute('''drop table clinic''')
#c.execute('''drop table doctor_timings''')
#c.execute('''drop table person''')
#c.execute('''drop table disease''')
#c.execute('''drop table disease_symptoms''')
#c.execute('''drop table patient_record''')
#c.execute('''drop table symptoms_discovered''')
#c.execute('''drop table drugs_used''')

# Create table
c.execute('''CREATE TABLE if not exists doctor(name text, email text, password text, specialization text, contact_no int, PRIMARY KEY (email))''')


#c.execute('''CREATE TABLE if not exists clinic(place text, contact_no int, address text, name text, unique_id int, primary key(unique_id))''')


#c.execute('''CREATE TABLE if not exists doctor_timings(doc_email text, clinic_unique_id int, from_time time, upto time, days int, primary key(clinic_unique_id), foreign key(clinic_unique_id) references clinic(unique_id), foreign key (doc_email) references doctor(doc_email))''')


c.execute('''CREATE TABLE if not exists patient(name text, email text, password text, DOB date, address text, contact_no int, blood_group text, PRIMARY KEY(email))''')


c.execute('''CREATE TABLE if not exists patientRecord(id int, email text, doc_email text, disease text, start date, end date,  PRIMARY KEY(id), FOREIGN KEY(email) REFERENCES patient(email), FOREIGN KEY(doc_email) REFERENCES doctor(email))''')


c.execute('''CREATE TABLE if not exists patientSymptom(id int, symptom text, FOREIGN KEY(id) REFERENCES patientRecord(id))''')


c.execute('''CREATE TABLE if not exists patientDrugs(id int, drugs text, FOREIGN KEY(id) REFERENCES patientRecord(id))''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
