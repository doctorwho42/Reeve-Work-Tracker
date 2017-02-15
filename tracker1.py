#!/usr/bin/env python
import RPi.GPIO as GPIO
import datetime
import time
import sys
import pickle
from Adafruit_LED_Backpack import SevenSegment

GPIO.setmode(GPIO.BCM)

display = SevenSegment.SevenSegment()
display.begin()

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state1 = GPIO.input(26)
state2 = GPIO.input(19)
state3 = GPIO.input(13)
state4 = GPIO.input(6)
keys = False
#write values to LED Display- (d4 d3: d2 d1) - (43:21) - d4=4,d3=3,d2=2,d1=1
def ledoutput(d1,d2,d3,d4):
	display.clear()
	display.set_digit(0,d4)
	display.set_digit(1,d3)
	display.set_digit(2,d2)
	display.set_digit(3,d1)
	display.set_colon(True)
	display.write_display()

#Example read/write pickle 
#	with open('/home/pi/pythoncode/worktracker/tracking.p', 'w') as write:
#		pickle.dump([write1, write2, write3, write4], write)

#	with open('/home/pi/pythoncode/worktracker/tracking.p') as read:
#		read1, read2, read3, read4 = pickle.load(read)

with open('/home/pi/pythoncode/worktracker/tracking.p') as read:
	read1,read2,read3,read4,read5= pickle.load(read)
x1 = read1 #lowest digit
x2 = read2 #second lowest digit
x3 = read3 #second highest digit
x4 = read4 #highest digit
crap = read5 #rob has worked over 99H:99M in a week,then this will =1

if state1 == 0:
	keys = True
elif state2 == 0:
	keys = True
elif state3 == 0:
	keys = True
elif state4 == 0:
	keys = True
#print(keys)
if keys==True:

	if x1<=8:
		x1 = x1 + 1
	elif x1==9:
		x1 = 0
		x2 = x2 + 1

	if x3==9 and x2==6:
		x3 = 0
		x2 = 0
		if x4==9:
			crap = 1	
		elif x4<=8:
			x4 = x4 + 1
	if x2==6:
		x2=0
		x3=x3+1


ledoutput(x1,x2,x3,x4)

if crap== 1:
	display.set_decimal(0,True)
	display.set_decimal(1,True)
	display.set_decimal(2,True)
	display.set_decimal(3,True)
	display.write_display()

#ledoutput(x1,x2,x3,x4)
	
with open('/home/pi/pythoncode/worktracker/tracking.p', 'w') as write:
	pickle.dump([x1,x2,x3,x4,crap], write)


