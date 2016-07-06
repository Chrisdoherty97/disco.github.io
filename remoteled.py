## Web-controlled LED

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode (GPIO.BCM)

LED_PIN = 4

GPIO.setup(LED_PIN,GPIO.OUT)


pubnub = Pubnub(publish_key='pub-c-61695fa6-317d-42aa-8f73-1bead73191ad', subscribe_key='sub-c-d5b343d8-3943-11e6-a169-02ee2ddab7fe')

channel = 'Disco'

def _callback(m, channel):
	print(m)
	if m['led'] == 1:
		for i in range(6):
		    GPIO.output(LED_PIN,True)
		    time.sleep(0.5)
		    GPIO.output(LED_PIN,False)
		    time.sleep(0.5)
		    print('blink')

def _error(m):
	print(m)
 
pubnub.subscribe(channels='Disco', callback=_callback, error=_error)

# Init PubNub


(_callback)
