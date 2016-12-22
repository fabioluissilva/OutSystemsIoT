#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Ping(Resource):
	def get(self):
		return {'value':'helloworld'}

api.add_resource(Ping,'/ping')

class Lock(Resource):
	def get(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(11,GPIO.OUT)	
		GPIO.output(11,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(11,GPIO.LOW)	
		GPIO.cleanup()
		return {'value':'lockopen_success'}

api.add_resource(Lock,'/lock')

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=80)
