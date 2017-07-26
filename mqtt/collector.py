import paho.mqtt.client as mqtt


#https://github.com/eclipse/paho.mqtt.python/tree/master/examples

REMOTE_BROKER_HOST="10.140.1.17"

class Collector:
    def __init__(self):
        pass

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        ###client.subscribe("$SYS/#")
        client.subscribe("testtopic")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def start(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(REMOTE_BROKER_HOST, 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()

collector = Collector()
collector.start()