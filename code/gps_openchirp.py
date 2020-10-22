#!/usr/bin/python
import sys
import busio
import digitalio
import board
import time
import RPi.GPIO as GPIO
from gps import *
import time, inspect
import numpy as np

import paho.mqtt.client as mqtt


class Device(mqtt.Client):
    def __init__(self, username, password):
        super(Device, self).__init__()
        self.host = "mqtt.openchirp.io"
        self.port = 8883
        self.keepalive = 300
        self.username = username
        self.password = password
        
        # Set access credential
        self.username_pw_set(username, password) #set username and pass
        self.tls_set('cacert.pem')
        
        # Create a dictionary to save all transducer states
        self.device_state = dict()
        
        # Connect to the Broker, i.e. the OpenChirp server
        self.connect(self.host, self.port, self.keepalive)
        self.loop_start()
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection Successful")
        else:
            print("Connection Unsucessful, rc code = {}".format(rc))
        # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
        self.subscribe("openchirp/device/"+self.username+"/#") # Subscribe to all tranducers

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload.decode()))
        # Save device state
        transducer = msg.topic.split("/")[-1]
        self.device_state[transducer] = msg.payload.decode()

    def on_publish(self, client, userdata, result):
        print("Data published")

# Modify here based on your own device
username = '5f76006b004d6e55c61dd480' # Use Device ID as Username
password = 'EDQerEKhaPDHT2JYL89WOPZak8w3Epo' # Use Token as Password

# Instantiate your own device
Patrolman = Device(username, password)

# Set up GPIO

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

def main():

    sensor1 = "lat"
    sensor2 = "lon"
    
    # Initialize
    Patrolman.device_state[sensor1] = 0
    Patrolman.device_state[sensor2] = 0
    
    while True:
        report = gpsd.next() #
        # Read from sensor
        sensor1_reading = str(getattr(report,'lat',0.0))
        sensor2_reading = str(getattr(report,'lon',0.0))
        print(sensor_reading)
        Patrolman.publish("openchirp/device/"+username+"/"+sensor1, payload=sensor1_reading, qos=0, retain=True)
        # Update device state
        Patrolman.device_state[sensor1] = sensor1_reading
        Patrolman.publish("openchirp/device/"+username+"/"+sensor2, payload=sensor2_reading, qos=0, retain=True)
        # Update device state
        Patrolman.device_state[sensor1] = sensor2_reading
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)



