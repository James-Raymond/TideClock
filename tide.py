#!/usr/bin/python
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import socket

#  Initialize LCD (must specify pinout and dimensions)
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)

try:
    while 1:
        lcd.clear()
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message("HT: 12:00")

        sleep(1)
        
except KeyboardInterrupt:
    print('CTRL-C pressed.  Program exiting...')

finally:
    lcd.clear()