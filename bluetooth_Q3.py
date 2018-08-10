import time
import sqlite3
from sense_hat import 

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
	
    if temp is not None:
        temp = round(temp, 1)
        return (temp)

# get name from Database based on bluetooth ID
def getName(bluetoothId):	
# code to get name



# Html code to be send to user
def htmlOutput():
    html_str = """
    <html>
    <header>
        <style type="text/css">
            h1 {
                color: DeepSkyBlue;
                font-family: "Times New Roman", Times, serif;
            }
        </style>
    </header>
    <body>
    <h1>Hello %s, the temp is %d<h1>
    </body>
    </html>
    """

    # Format the html string with the name and temp variable 
    name = getName(bluetoothId)
    temp = getSenseHatData()
    html_str %(name, temp)
    return html_str

# Write to html file
def createHtml():
    Html_file = open ("Greetings.html","w")
    Html_file.write(htmlOutput(bluetoothId))
    Html_file.close()

# Send html file
def sendMessage():
    #code to send html file over bluetooth