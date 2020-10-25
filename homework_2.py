## Insert 5 records in cars table
import sqlite3 

cars = [
	('Ford', 'Fiesta', 12),
	('Ford', 'Loca', 10),
	('Honda', 'CRV', 55),
	('Honda', 'Civic', 34),
	('Ford', 'Rabiosa', 2)
]

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	try:
		c.executemany("INSERT INTO inventory VALUES (?,?,?)", cars)
	except sqlite3.OperationalError as oe:
		print("The following error occured: {}".format(oe))
