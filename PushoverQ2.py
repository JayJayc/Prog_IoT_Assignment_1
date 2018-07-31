import httplib
import urllib
import time
from sense_hat import SenseHat

class PushoverSender:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key
 
    def send_notification(self, text):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
        conn.request("POST", "/1/messages.json",
                     urllib.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})
        # print(conn.getresponse().read())


m = PushoverSender("u3rxb16wvd6a65afq3ncdfyopt35id","apj8741z2fgjv1gtu9seybng46ybcg")
sense = SenseHat()
temp = None


while (temp > 20 or temp == None):
    if(sense):
        temp = sense.get_temperature()
        print("Temp is "+int(temp))
        time.sleep(10)


message = "Temperature is below 20, don't forget to bring a sweater (Temp: "+str(int(temp))+")"

if (temp > 20):
    m.send_notification(message)
    time.sleep(60)