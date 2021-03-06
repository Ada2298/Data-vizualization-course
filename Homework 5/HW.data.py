import sqlite3
import numpy as np
import time
import scipy.stats as stats

## Connection to sql server
connection = sqlite3.connect('data_db.db')
c = connection.cursor()

# Table creation
c.execute("DROP TABLE IF EXISTS values_")
c.execute("DROP TABLE IF EXISTS averages")
c.execute("DROP TABLE IF EXISTS p_values")

c.execute("CREATE TABLE values_ (Id int,throw_id int, value int)")
c.execute("CREATE TABLE averages (Id int, value real)")
c.execute("CREATE TABLE p_values (Id int, p_value real)")

i = 0
j = 0
a = 0

# Data generation. You have a perfect dice (6 sided). In each trial you roll it 7 times. 
# We have data for dice rolls outputs(table values_) and mean of that outputs(table averages)

while True:
	b = 0
	j += 1
	for counter in range(0,7): 
		i += 1
		a = np.random.randint(1,7)
		b += a
		c.execute("INSERT INTO values_ values ({},{},{})".format(i,j,a))
		#connection.commit()
	b = b / 7
	c.execute("INSERT INTO averages values ({},{})".format(j,b))
	connection.commit()

	time.sleep(0.5)