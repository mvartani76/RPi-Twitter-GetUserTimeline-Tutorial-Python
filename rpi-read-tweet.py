#!/usr/bin/env python
import sys
from twython import Twython
import os
import RPi.GPIO as GPIO

CONSUMER_KEY = 'YOUR DATA HERE'
CONSUMER_SECRET = 'YOUR DATA HERE'
ACCESS_KEY = 'YOUR DATA HERE'
ACCESS_SECRET = 'YOUR DATA HERE'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

GPIO.setmode(GPIO.BOARD)

# set up GPIO 11 as output
GPIO.setup(11,GPIO.OUT)

while True:
        
    user_timeline = api.get_user_timeline(screen_name="YOUR TWITTER USER NAME",count=1)
    time.sleep(2)    

    for tweet in user_timeline:
	tweet['text'] = Twython.html_for_tweet(tweet)
	print tweet['text']
        
    if (tweet['text'] == "RPi ON"):
    	GPIO.output(11,GPIO.HIGH)
    if (tweet['text'] == "RPi OFF"):
	GPIO.output(11,GPIO.LOW)

GPIO.cleanup()	
