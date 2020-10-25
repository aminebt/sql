import sqlite3 
import csv 

with open("employees.csv", mode="r", encoding="utf-8", newline="") as file:
	employees = csv.reader(file)

	with sqlite3.connect("new.db") as conn:
		c = conn.cursor() 
		c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
		c.executemany("INSERT INTO employees VALUES (?,?)", employees)