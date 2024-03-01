from flask import Flask
import paho.mqtt.client as mqtt

app = Flask(__name__)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



@app.route('/')
def hello_world():
    mqttc.publish("test", "{\"message\": \"Hello, World!\"}")
    return 'Hello, World!'

if __name__ == '__main__':
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.connect("localhost", 1883, 60)

    app.run(debug=True, port=5001)
    mqttc.loop_forever()    