#!/usr/bin/python3

import paho.mqtt.client as mqtt
import math
from time import sleep
from move import Movement

# base_to_wheel_coefficient - defines, how many turns of the wheels are needed to make one full rotation of the drive base
wheel_diameter = 31.5
base_width = 157
number = 0
robot_number = 0
run_time = 3

base_circumference = base_width*math.pi

# distance_per_wheel_coefficient - defines how many milimeters of the distance are travelled in one full wheel rotation
wheel_circumference = wheel_diameter*math.pi

base_to_wheel_coefficient = base_circumference/wheel_circumference

speed_value_scale_coefficient = 9


def on_subscribe(client, userdata, mid, granted_qos):
	print('Successfully subscribed to the topic.')

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc) + ".")
	# client.subscribe("$SYS/#")
	print("Subscribing to topic...")
	client.subscribe('RobotTopic', 1) 

def on_publish(client, userdata, mid):
	print('Data published.')

def on_message(client, userdata, message):
	print("Received message: " + str(message.payload) + "on Topic: " + message.topic + " with QoS " + str(message.qos))
	if message.topic == 'RobotTopic':
		global robot_number
		divided = str(message.payload)[2:-1].split('#')  # split received message, message should have a format of b'command#wheel_velocity#argument'
		robot_number = int(divided[0])
		command = divided[1]
		wheel_velocity = int(divided[2])
		current_number = int(divided[4])
		global number
		
		if robot_number == 1:
			number = current_number
			if wheel_velocity >= 100 or wheel_velocity <= 0:  # wrong speed value received
				wheel_velocity = 0

			if command == 'gs':  # move forward
				print('move forward')
				movement.move_foward(3, wheel_velocity)
				sleep(run_time)
				movement.stop()

			elif command == 'gb':  # move backwards
				print('move backwards')
				movement.move_backward(3, wheel_velocity)
				sleep(run_time)
				movement.stop()

			elif command == 'rr':  # rotate right
				print('rotate right')
				movement.turn_right(3, wheel_velocity)
				sleep(run_time)
				movement.stop()

			elif command == 'rl':  # rotate left
				print('rotate left')
				movement.turn_left(3, wheel_velocity)
				sleep(run_time)
				movement.stop()

			elif command == 'stop':
				print('stop')
				movement.stop()

			elif command == 'shoot':
				print('shoot')
				

if __name__ == "__main__":
	movement = Movement()
	movement.setup()

	# initialize mqtt client
	client = mqtt.Client()

	# set mqtt client callbacks
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_publish = on_publish
	client.on_subscribe = on_subscribe

	# connect mqtt client
	client.connect('192.168.43.165',1883, 60)
	client.publish('RobotLogTopic', 'Robot1Ready', False)

	# run
	client.loop_forever(0.04, 10, False)
	
