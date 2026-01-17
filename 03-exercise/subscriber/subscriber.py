import paho.mqtt.client as mqtt
import sys

BROKER = "mosquitto"
PORT = 1883
TOPIC = "demo/topic"

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")
    sys.stdout.flush()


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(BROKER, PORT, 60)

client.loop_start()
client.subscribe(TOPIC)
print("Waiting for message...")
sys.stdout.flush()
client.loop_forever()