#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)

while True:
	state1 = GPIO.input(26)
	state2 = GPIO.input(19)
	state3 = GPIO.input(13)	
	state4 = GPIO.input(6)

#	print(state1)
#	print(state2)
#	print(state3)
#	print(state4)

	if state1 == 0:
		GPIO.output(5,True)
	elif state2 == 0:
		GPIO.output(5,True)
	elif state3 == 0:
		GPIO.output(5,True)
	elif state4 == 0:
		GPIO.output(5,True)

	if state1 == 1:
		if state2 == 1:
			if state3 == 1:
				if state4 == 1:
					GPIO.output(5,False)
	time.sleep(1)
