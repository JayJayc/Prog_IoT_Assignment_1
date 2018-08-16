import time
import sqlite3
from sense_hat import SenseHat
dbname='data_logger.db'

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
	
    if temp is not None:
        temp = round(temp, 1)
        logData (temp)


# log sensor data on database
def logData (temp):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()


# main function
def main():
    getSenseHatData()


# Execute program 
main()
