#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import busio
import digitalio
import board
import time
import RPi.GPIO as GPIO
import smbus
import math

import paho.mqtt.client as mqtt

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

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


def read_byte(adr):
	return bus.read_byte_data(address, adr)
 
def read_word(adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr+1)
	val = (high << 8) + low
	return val
 
def read_word_2c(adr):
	val = read_word(adr)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val
 
def dist(a,b):
	return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
	radians = math.atan2(x, dist(y,z))
	return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
	radians = math.atan2(y, dist(x,z))
	return math.degrees(radians)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68 # This is the address value read via the i2cdetect command
 
# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

# Set up GPIO
GPIO.setmode(GPIO.BCM)

def main():

    sensor1 = "accel_x"
    sensor2 = "accel_y"
    sensor3 = "accel_z"
    
    # Initialize
    Patrolman.device_state[sensor1] = 0
    Patrolman.device_state[sensor2] = 0
    
    while True:
        time.sleep(0.1)
        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)
        # Read from sensor
        sensor1_reading = accel_xout / 16384.0
        sensor2_reading = accel_yout / 16384.0
        sensor3_reading = accel_zout / 16384.0
        
        Patrolman.publish("openchirp/device/"+username+"/"+sensor1, payload=sensor1_reading, qos=0, retain=True)
        # Update device state
        Patrolman.device_state[sensor1] = sensor1_reading
        Patrolman.publish("openchirp/device/"+username+"/"+sensor2, payload=sensor2_reading, qos=0, retain=True)
        # Update device state
        Patrolman.device_state[sensor2] = sensor2_reading
        Patrolman.publish("openchirp/device/"+username+"/"+sensor3, payload=sensor3_reading, qos=0, retain=True)
        # Update device state
        Patrolman.device_state[sensor3] = sensor3_reading
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)



