import sqlite3

conn = sqlite3.connect("new.db")

cur = conn.cursor()

#populationS does not exist
try:
	cur.execute("INSERT INTO populations VALUES ('New York City', 'NY', 8400000)")
	cur.execute("INSERT INTO populations VALUES ('San Francisco', 'CA', 8000000)")
	conn.commit()

except sqlite3.OperationalError as oe:
	print("Oops! The following error occured : {}".format(oe))

conn.close()