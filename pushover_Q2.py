import http.client
import urllib
import time
from sense_hat import SenseHat


class PushoverSender:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key

    def send_notification(self, text):
        conn = http.client.HTTPSConnection(
            "api.pushover.net:443"
            )
        post_data = {
            'user': self.user_key,
            'token': self.api_key,
            'message': text
            }
        conn.request(
            "POST",
            "/1/messages.json",
            urllib.parse.urlencode(post_data),
            {"Content-type": "application/x-www-form-urlencoded"}
            )
        # print(conn.getresponse().read())


def tempCheck():
    sense = SenseHat()
    temp = None

    while (True):
        if(sense):
            temp = sense.get_temperature()
            try:
                print("Temp is "+str(int(temp)))
                if float(temp) < 40:
                    return temp
            except ValueError:
                print('Non-numeric data found in the file.')
            except TypeError:
                print('a type error has occurred')

            time.sleep(60)


def sendMessenge(temp):
    m = PushoverSender(
        "u3rxb16wvd6a65afq3ncdfyopt35id",
        "apj8741z2fgjv1gtu9seybng46ybcg"
        )
    message = "Temperature is below 20, don't forget to bring a sweater (Temp: "+str(int(temp))+")"
    m.send_notification(message)


def main():
    temp = tempCheck()
    sendMessenge(temp)


main()
