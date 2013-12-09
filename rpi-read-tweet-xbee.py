#!/usr/bin/env python
import sys
from twython import Twython
import os
import time
import serial
import RPi.GPIO as GPIO

CONSUMER_KEY = 'YOUR USER DATA'
CONSUMER_SECRET = 'YOUR USER DATA'
ACCESS_KEY = 'YOUR USER DATA'
ACCESS_SECRET = 'YOUR USER DATA'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

GPIO.setmode(GPIO.BOARD)

# set up GPIO 11 as output
GPIO.setup(11,GPIO.OUT)

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
        
    user_timeline = api.get_user_timeline(screen_name="YOUR USER IDA",count=1)
    time.sleep(2)    

    for tweet in user_timeline:
	tweet['text'] = Twython.html_for_tweet(tweet)
	print tweet['text']
        
    if (tweet['text'] == "RPi ON"):
    	ser.write('H')
    if (tweet['text'] == "RPi OFF"):
	ser.write('L')

GPIO.cleanup()	
