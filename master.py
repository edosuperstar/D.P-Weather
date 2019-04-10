import pzgram
import paho.mqtt.client as mqtt
import threading

def on_connect(client, userdata, flags, rc):
	print('Connessione al server Calvino...: {}'.format(mqtt.connack_string(rc)))
	client.subscribe('/#', qos = 0)

def on_subscribe(client, userdata, mid, granted_qos):
	print('Avviato con QoS: {}'.format(granted_qos[0]))

def on_message(client, userdata, msg):
    global temperatura, altitudine, pressione, luce
    if msg.topic == "/calvino-04/temperatura":
        temperatura=msg.payload.decode()
    elif msg.topic == "/calvino-04/altitudine":
        altitudine=msg.payload.decode()
    elif msg.topic == "/calvino-04/pressione":
        pressione=msg.payload.decode()
    elif msg.topic == "/calvino-04/luce":
        luce = msg.payload.decode()

def mqttStart():
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


def SetBot(chat):
    button1 = pzgram.create_button("Temperatura", data="temperatura")
    button2 = pzgram.create_button("Pressione", data="pressione")
    button3 = pzgram.create_button("Luce", data="luce")
    button4 = pzgram.create_button("Altitudine", data="altitudine")

    k = [[button1, button2,button3,button4]]

    keyboard = pzgram.create_inline(k)

    chat.send("Bot per il controllo remoto dei dati dei sensori della scuola Calvino: ")
    chat.send("Seleziona un dato da controllare: ", reply_markup=keyboard)


def sendTemperatura(chat):
    chat.send(temperatura+" °C")

def sendPressione(chat):
    chat.send(pressione+" Pa")

def sendLuce(chat):
    chat.send(luce+" Lux")

def sendAltitudine(chat):
    chat.send(altitudine+ " Metri")

def LaunchBot():
    bot.set_query({"temperatura": sendTemperatura, "pressione": sendPressione,"luce": sendLuce, "altitudine": sendAltitudine})
    bot.set_commands({"stats": SetBot})
    bot.run()

if __name__ == '__main__':
    bot = pzgram.Bot("883446648:AAHGWLcnWooHtKjxk43isvh_2Y3k8kGAz6o")
    mqttThread = threading.Thread(target=mqttStart)
    mqttThread.setDaemon(True)
    mqttThread.start()
    botThread = threading.Thread(target=LaunchBot)
    botThread.start()
