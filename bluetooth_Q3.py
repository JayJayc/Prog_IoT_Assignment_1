import time
import sqlite3
import bluetooth
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
            for i in device_names:
                if device_names[i] == bluetooth.lookup_name(mac_address, timeout=5):
                    device_address = mac_address
                    name = device_names[i]
                    break
            break        
        if device_address is not None:
            print("Hi! Your phone ({}) has the MAC address: {}".format( device_name, device_address))
            sendMessage(name,device_address)
    
        else:
            print("Could not find target device nearby...")

# Html code to be send to user
def htmlOutput():
    # html_str = """
    # <html>
    # <header>
    #     <style type="text/css">
    #         h1 {
    #             color: DeepSkyBlue;
    #             font-family: "Times New Roman", Times, serif;
    #         }
    #     </style>
    # </header>
    # <body>
    # <h1>Hello %s, the temp is %d<h1>
    # </body>
    # </html>
    # """

    # Format the html string with the name and temp variable 
    name = getName()
    temp = getSenseHatData()
    # html_str %(name, temp)
    html_str = name + " " + temp
    return html_str

# Write to html file
# def createHtml():
#     Html_file = open ("Greetings.html","w")
#     Html_file.write(htmlOutput(bluetoothId))
#     Html_file.close()

# Send html file
def sendMessage(name,address):
    sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

    bd_addr = address
    port = 0x1001

    sock.connect((bd_addr, port))

    sock.send(htmlOutput())

    sock.close()
    #code to send html file over bluetooth

def main():
    names = getName()
    search(names)

main()