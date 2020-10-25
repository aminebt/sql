import sqlite3

conn = sqlite3.connect("new.db")

cur = conn.cursor()

cur.execute(""" CREATE TABLE population
			(city TEXT, state TEXT, population INT)
	""")

conn.close()
