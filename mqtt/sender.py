
import paho.mqtt.publish as publish
import time

REMOTE_BROKER_HOST="10.140.1.17"

class Sender:
    def __init__(self):
        pass

    def start(self):
        for i in range(1,1000, 1):
            publish.single("testtopic", "boo" + str(i), hostname=REMOTE_BROKER_HOST, port=1883)
            time.sleep(1)


sender = Sender()
sender.start()