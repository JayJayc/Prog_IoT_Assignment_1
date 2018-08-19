#!/usr/bin/env python3
import os
import sys
import sqlite3
from flask import Flask, render_template, request

dbname='/home/pi/IoT/Assignment1/data_logger.db'

app = Flask(__name__)

'''Uncomment if you dont want to see console print out'''
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

def getData():
	conn = sqlite3.connect(dbname)
	curs = conn.cursor()

	temps = []
	times = []
	hums = []
	data = []

	curs.execute("SELECT * FROM SENSEHAT_data")
	rows = curs.fetchall()

	for row in rows:
		times.append(row[0])
		temps.append(row[1])
		hums.append(row[2])
	conn.close()

	data.append(times)
	data.append(temps)
	data.append(hums)
	return data

# main route 
@app.route("/")
def index():	
	data = getData()
	times = data[0]
	temps = data[1]
	hums = data[2]
	templateData = {
		'times': times,
		'temps': temps,
		'hums': hums
	}

	return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
