import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

def create_table():
##	c.execute('DROP TABLE stuffToPlot')
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145123542,'2016-01-01','Python',5)")
    conn.commit()

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix,datestamp,keyword,value) VALUES (?,?,?,?)",(unix,date,keyword,value))
    conn.commit()

def read_from_db():
    # c.execute("SELECT * FROM stuffToPlot WHERE value=5 AND keyword='Python'")
    c.execute("SELECT * FROM stuffToPlot")
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('SELECT unix,value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        # print(row)
        # print(datetime.datetime.fromtimestamp(row[1]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot(dates,values, '-')
    plt.show()

try:
	conn = sqlite3.connect('test.db')
	c=conn.cursor()
	create_table()
	for i in range(10):
		dynamic_data_entry()
		time.sleep(0.5)
	read_from_db()
	graph_data()
except Exception as e:
	print(e)
finally:
	c.close()
	conn.close()
