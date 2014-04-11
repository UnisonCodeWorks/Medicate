import sys
import sqlite3

def main():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')



	conn.commit()
	conn.close()

if __name__=='__main__':
	main()