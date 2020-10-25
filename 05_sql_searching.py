import sqlite3 

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	try: 
		# for row in c.execute("SELECT firstname,lastname FROM employees"):
		# 	print(row)
		c.execute("SELECT firstname,lastname FROM employees")
		rows = c.fetchall()
		for r in rows:
			print(r[0], r[1])
	except sqlite3.OperationalError as oe:
		print("The following error occured : {}".format(oe))
