import paho.mqtt.client as mqtt

global temperatura,altitudine,pressione,luce

def on_connect(client, userdata, flags, rc):
	print('result from connect: {}'.format(mqtt.connack_string(rc)))
	client.subscribe('/#', qos = 0)

def on_subscribe(client, userdata, mid, granted_qos):
	print('subscribed topic with QoS: {}'.format(granted_qos[0]))

def on_message(client, userdata, msg):
	if msg.topic == "/calvino-04/temperatura":
		temperatura=msg.payload.decode()
	elif msg.topic == "/calvino-04/altitudine":
		altitudine=msg.payload.decode()
	elif msg.topic == "/calvino-04/pressione":
		pressione=msg.payload.decode()
	elif msg.topic == "/calvino-04/luce":
		luce = msg.payload.decode()
	#print('msg: {} from topic: {}'.format(msg.payload.decode(), msg.topic))


def main():
	client = mqtt.Client(protocol = mqtt.MQTTv311)
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message
	client.username_pw_set("calvino00","0123456789")

	client.connect(host = 'broker.shiftr.io', port = 1883, keepalive = 60)

	try:
		client.loop_forever()
	except KeyboardInterrupt:
		print()

if __name__ == '__main__':
	main()