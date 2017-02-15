import time
from Adafruit_LED_Backpack import SevenSegment

display = SevenSegment.SevenSegment()

display.begin()

#colon on
#colon = True
#Left side of colon - turn on = true
#display.set_left_colon(True)
display.clear()
display.set_decimal(0,True)
display.set_digit_raw(1,0x60)
display.set_digit_raw(2,0x36)
display.set_digit_raw(3,0x66)
display.set_colon(True)

display.write_display()
		

