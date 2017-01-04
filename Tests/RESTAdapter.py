#!/usr/bin/python
import paho.mqtt.client as mqtt
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
                client.publish("OutsystemsTest","open_lock")
                return {'value':'lockopen_success'}

api.add_resource(Lock,'/lock')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("OutsystemsTest")

if __name__ == '__main__':
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect("iot.eclipse.org", 1883, 60)
        app.run(debug=True,host='0.0.0.0',port=8080)
