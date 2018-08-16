import time
import sqlite3
import bluetooth, subprocess
from sense_hat import SenseHat


dbname='names.db'

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
	
    if temp is not None:
        temp = round(temp, 1)
        return (temp)

# get names from Database
def getName():	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    names = []
    curs.execute("SELECT name FROM NAMES")
    rows = curs.fetchall()
    for row in rows:
        print(row)
        names.append(row[0])
    conn.close()
    print (names)
    return names
# code to get name

# Search for device based on device's name
def search(device_names):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        for mac_address in nearby_devices:
            for i in range(len(device_names)):
                if device_names[i] == bluetooth.lookup_name(mac_address, timeout=5):
                    device_address = mac_address
                    name = device_names[i]
                    break
            break        
        if device_address is not None:
            return name
    
        else:
            print("Could not find target device nearby...")

def main():
    sense = SenseHat()
    names = getName()
    name = search(names)
    temp = getSenseHatData()
    if name != None:
        sense.show_message("Hi {}! Current Temp is {}*c".format(name, temp), scroll_speed=0.05)

main()