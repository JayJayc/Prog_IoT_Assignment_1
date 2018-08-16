import time
import sqlite3
from sense_hat import SenseHat

dbname='data_logger.db'

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
    hum = sense.get_humidity()

    if temp and hum is not None:
        temp = round(temp, 1)
        hum = round(hum,1)
        data = [temp,hum]
        logData (data)


# log sensor data on database
def logData(data):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (data[0],data[1],))
    conn.commit()
    conn.close()


# main function
def main():
    getSenseHatData()


# Execute program 
main()
