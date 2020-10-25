## Update 2 records then output all the records from cars table 
## Then output only records that are for Ford Vehicles 

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	try:
		c.execute("UPDATE inventory SET Quantity=0 WHERE Make='Ford' AND Model='Fiesta'")
		c.execute("UPDATE inventory SET Quantity=0 WHERE Make='Honda' AND Model='Civic'")

		c.execute("SELECT * FROM inventory")
		cars = c.fetchall() 

		for car in cars:
			print(car[0], car[1], car[2])
	except sqlite3.OperationalError as oe:
		print("The following error occured: {}".format(oe))

	print("outputing all Ford inventory")

	try:
		c.execute("SELECT * FROM inventory WHERE Make='Ford'")
		ford_cars = c.fetchall()
		for car in ford_cars:
			print(car[0], car[1], car[2])		
	except sqlite3.OperationalError as oe:
		print("The following error occured: {}".format(oe))