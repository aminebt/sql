import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor() 

	try: 
		c.execute("""CREATE TABLE inventory
			(Make TEXT, Model TEXT, Quantity INT)
			""")
	except sqlite3.OperationalError as oe:
		print(oe)