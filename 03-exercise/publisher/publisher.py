import time
import paho.mqtt.client as mqtt

BROKER = "mosquitto"
PORT = 1883
TOPIC = "demo/topic"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

for _ in range(10):                         # retry loop because broker may not be ready yet
    try:
        client.connect(BROKER, PORT, 60)
        break
    except ConnectionRefusedError:
        time.sleep(1)

time.sleep(2)
client.publish(TOPIC, "Hello from publisher container.", retain = True)     # 'retain = True', retains the message in the topic and does not discart it right away.
print("Message sent")

client.disconnect()