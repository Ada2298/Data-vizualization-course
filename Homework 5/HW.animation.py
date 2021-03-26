import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import statsmodels.api as sm
import scipy.stats as stats
from scipy.stats import shapiro
from statsmodels.graphics.gofplots import qqplot
import time
import sqlite3

connection = sqlite3.connect('data_db.db')
c = connection.cursor()

 ## Shapiro_Wilk test for our data, returns statistics and p-value for the test
pValue_counter = 0

def test():
	connection = sqlite3.connect('data_db.db')
	c = connection.cursor()
	global pValue_counter
	pValue_counter += 1
	query1 = ('SELECT * FROM averages')
	data = pd.read_sql_query(query1, connection)
	roll_mean  = data.value
	stat, p = shapiro(roll_mean)
	stat = round(stat, 4)
	query2 = ("INSERT INTO p_values values ({}, {})".format(pValue_counter, p))
	c.execute(query2)
	connection.commit()
	return stat, p

### This method expects p-value from Shapiro_Wilk test and returns a formatted string
def getstring(b):
	mytext = "p-value = {}".format(b)
	return mytext
### Drawing charts. Here we have 2x3 figure with 5 charts.
### chart 1 here we have the histogram of the means
### chart 2 here we have the QQ plot
### chart 3 this should be a chart, where will display the results of the Shapiro-Wilk Test (only text, so get rid of the x and y axis). You can add also skewness and kurtosis values too.
### chart 4 this should be a chart for p-values from Shapiro-Wilk Test
### chart 5 the original distribution
fig = plt.figure(constrained_layout=True, figsize=(13,8))
plt.axis('off')

gs = fig.add_gridspec(2, 3)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,0])
ax4 = fig.add_subplot(gs[1,1])
ax5 = fig.add_subplot(gs[0:,-1])

def animate(i):
	query1 = ('SELECT * FROM values_')
	query2 = ('SELECT * FROM averages')

	data1 = pd.read_sql_query(query1, connection)
	data2 = pd.read_sql_query(query2, connection)
# x1 is our outputs of dice's rolls, x2- is mean of that rolls
	x1 = data1.value
	x2 = data2.value

	ax1.cla()
	ax1.hist(x2)
	ax1.title.set_text('Distribution of means')

	ax2.cla()
	stats.probplot(x2, plot = ax2)
	ax2.title.set_text('Probability plot')
	
	a,b = test()
	ax3.cla()
	ax3.text(0.07,0.64,getstring(b))
	ax3.title.set_text('Normality test p-value')
	ax3.axis('off')

	ax4.cla()
	query_id = ('SELECT id FROM p_values')
	query_p_value = ('SELECT p-value FROM p_values')
	p_values_id = pd.read_sql_query(query_id, connection)
	p_values_value = pd.read_sql_query(query_id, connection)
	#roll_mean  = data.value
	##  Imagine that here we have line plot, but something goes wrong with my code  :)) 
	ax4.plot(p_values_id, p_values_value)
	ax4.title.set_text("Distributison of p-values")

	ax5.cla()
	ax5.hist(x1)
	ax5.title.set_text('Distribution of outputs')

	plt.legend()
	

anim = FuncAnimation(fig, animate, interval = 500)
plt.show()
