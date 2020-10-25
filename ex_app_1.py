## add 100 random integers, ranging from 0 to 100 to newnum.db 

import sqlite3 
import random

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor() 
    try:
    # create table integers with a single column integer
        c.execute("""CREATE TABLE integers(integer INT)""")
    except sqlite3.OperationalError as oe:
        print("The following error occured while creating the integers table : {}".format(oe))

    # insert random integers into the new table
    try:    
        for i in range(100):
            random_int = (random.randint(0,100),) 
            print(random_int)
            c.execute("INSERT INTO integers VALUES (?)", random_int)
    except sqlite3.OperationalError as oe:
        print("The following error occured while populating the integers table : {}".format(oe))
