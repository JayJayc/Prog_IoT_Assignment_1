import time
import sqlite3
import bluetooth
from sense_hat import SenseHat


dbname = 'names.db'


# get data from SenseHat sensor
def getSenseHatData():
    sense = SenseHat()
    temp = sense.get_temperature()
    try:
        temp = round(temp, 1)
        return (temp)
    except ValueError:
        print('Non-numeric data found in the file.')
    except TypeError:
        print('a type error has occurred')


# get names from Database
def getName():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    names = []
    curs.execute("SELECT name FROM NAMES")
    rows = curs.fetchall()
    for row in rows:
        names.append(row[0])
    conn.close()
    print(names)
    return names
# code to get name


# Search for device based on device's name
def search(device_names):
    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        # Sleep three seconds
        time.sleep(3)
        nearby_devices = bluetooth.discover_devices()
        # search for the device
        try:
            for mac_address in nearby_devices:
                for i in range(len(device_names)):
                    if device_names[i] == bluetooth.lookup_name(
                            mac_address,
                            timeout=5
                            ):
                        device_address = mac_address
                        name = device_names[i]
                        break
                break
        except ValueError:
            print('Non-numeric data found in the file.')
        except TypeError:
            print('a type error has occurred')

        if device_address is not None:
            return name
        else:
            print("Could not find target device nearby...")


def main():
    sense = SenseHat()
    names = getName()
    name = search(names)
    temp = getSenseHatData()
    if name is not None:
        sense.show_message(
            "Hi {}! Current Temp is {} C".format(name, temp),
            scroll_speed=0.15
            )


main()
