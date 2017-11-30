# Import delle Librerie Code
import onewire.ds18x20 as ds
import onewire.onewire as ow
import time
import uwebsockets.client as ws
import network
from machine import Pin

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

	dTempPin = ds.DS18X20(ow.OneWire(Pin(4)));
	with ws.connect('palermo.linked-data.eu', 8081, "") as wsClient:

		# Loop
		while (True):
			# Misurazione
			roms = dTempPin.scan()
			dTempPin.convert_temp()
			time.sleep_ms(750)
			for rom in roms:				
				temp = str(dTempPin.read_temp(rom))
			print('*-- Temperature read: ' + temp)

			# Manda al server WebSocket
			wsClient.send(temp)

			# Ricevi dal server WebSocket
			response = wsClient.recv()

			print('*-- WebSocketServer Response: ' + response)
			time.sleep(3)


if __name__ == "__main__":
    main()
