# Import delle Librerie Code
from dht import DHT11
import time
import uwebsockets.client as ws
import network

def connectToWifi():
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	c = open('config.txt', 'rt')
	l = c.read()
	w = l.split('||')
	print(w)

	if not wlan.isconnected():
		print('*--- Connecting...')
		print('*----> \t SSID:\t' + w[0])
		print('*----> \t Password:\t' + w[1])
		#AP_NAME, AP_PASSWORD 
		wlan.connect(w[0], w[1])

	while not wlan.isconnected():
		pass
	print('*-- Connected!')
	return wlan

def main():
	wifi = connectToWifi()
	gc.collect()

	with ws.connect('palermo.linked-data.eu', 8081, "") as wsClient:

		# Loop
		while (True):
			temp = "2";
			# Manda al server WebSocket
			wsClient.send(temp)
			# Ricevi dal server WebSocket
			response = wsClient.recv()

			print('*-- response: '+response)
			time.sleep(.2)

if __name__ == "__main__":
    main()
