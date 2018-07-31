import httplib
import urllib
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

sense = SenseHat()
temp = None
if(sense):
    temp = sense.get_temperature()
else:
    temp = 20
print(int(temp))
message = "Temperature is: "+str(int(temp))


m = PushoverSender("u3rxb16wvd6a65afq3ncdfyopt35id","apj8741z2fgjv1gtu9seybng46ybcg")
m.send_notification(message)