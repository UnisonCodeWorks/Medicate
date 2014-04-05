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


c.execute('''CREATE TABLE if not exists clinic(place text, contact_no int, address text, name text, unique_id int, primary key(unique_id))''')


c.execute('''CREATE TABLE if not exists doctor_timings(doc_email text, clinic_unique_id int, from_time time, upto time, days int, primary key(clinic_unique_id), foreign key(clinic_unique_id) references clinic(unique_id), foreign key (doc_email) references doctor(doc_email))''')


c.execute('''CREATE TABLE if not exists person(name text, email text, password text, DOB text, address text, contact_no int, blood_group text, primary key (email))''')


c.execute('''CREATE TABLE if not exists disease(disease_name text, disease_id int, primary key(disease_id))''')


c.execute('''CREATE TABLE if not exists disease_symptoms(disease_id int, symptom text, primary key( disease_id), foreign key (disease_id) references disease(disease_id))''')


c.execute('''CREATE TABLE if not exists patient_record(patient_id int, doc_email int, disease_id int, from_date date, to_date date, patient_record_id int, primary key(patient_record_id), foreign key (patient_id) references person(email), foreign key(doc_email) references doctor(doc_email), foreign key(disease_id) references disease)''')


c.execute('''CREATE TABLE if not exists symptoms_discovered(patient_record_id int, symptom text, foreign key(patient_record_id) references patient_record)''')


c.execute('''CREATE TABLE if not exists drugs_used(patient_record_id int, drug_name text, foreign key(patient_record_id) references patient_record)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
