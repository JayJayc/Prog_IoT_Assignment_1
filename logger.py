#!/usr/bin/env python3
from datetime import datetime
import sqlite3
from sense_hat import SenseHat

dbname = '/home/pi/IoT/Assignment1/data_logger.db'


# get data from SenseHat sensor
def getSenseHatData():
    sense = SenseHat()
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    try:
        if temp and hum is not None:
            temp = round(temp, 1)
            hum = round(hum, 1)
            data = [temp, hum]
            logData(data)
    except ValueError:
        print('Non-numeric data found in the file.')
    except TypeError:
        print('a type error has occurred') 
    


# log sensor data on database
def logData(data):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO SENSEHAT_data values(datetime(?), (?), (?))", (
            datetime.now(),
            data[0],
            data[1],
        )
    )
    conn.commit()
    conn.close()


# main function
def main():
    getSenseHatData()


# Execute program
main()
