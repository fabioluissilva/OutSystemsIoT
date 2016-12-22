#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def activate(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(pin,GPIO.LOW)
	return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

activate(11)
GPIO.cleanup()
