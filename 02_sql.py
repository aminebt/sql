import sqlite3 

# conn = sqlite3.connect("new.db")

# cur = conn.cursor()

# cur.execute("INSERT INTO population VALUES ('New York City', 'NY', 8400000)")
# cur.execute("INSERT INTO population VALUES ('San Francisco', 'CA', 8000000)")

# conn.commit()

# conn.close()


with sqlite3.connect("new.db") as conn:
	c = conn.cursor() 
	c.execute("INSERT INTO population VALUES ('New York City2', 'NY', 8400000)")
	c.execute("INSERT INTO population VALUES ('San Francisco2', 'CA', 8000000)")	


