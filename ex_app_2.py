# based on the db and table created in ex_app1.py
# Prompt the user whether they would like to perform an aggregation (AVG, MAX, MIN, or SUM) or exit the program altogether


import sqlite3 

while True:
	operation = input("Please choose an operation to perform (AVG, MAX, MIN, SUM) or type something else to exit the program : ")
	if operation.upper() in ['AVG', 'MAX', 'MIN', 'SUM']:
		# generate the query to pass 
		sql_query = "SELECT " + operation.lower() + "(integer) FROM integers" 
	else:
		print("Thank you. See you next time!")
		exit()

	with sqlite3.connect("newnum.db") as conn:
		c = conn.cursor() 
		try:
			c.execute(sql_query)
			result = c.fetchone() 
			print(result[0])
		except sqlite3.OperationalError as oe:
			print("The following error occured while computing the metric {} : \n {}".format(operation.upper(), oe))


#coulbe enhanced by 
	#asking the user a choce between numbers corresponding tooperations (and 5 corresponding to exit) 
	#maybe it is better to handle the connection closing manually instead of the with statement (with the method above maybe we're opening and closing the connection too many times)