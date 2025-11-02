#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Set ports
left_motor_port = Port.A
right_motor_port = Port.B
color_sensor_port = Port.S1
ultrasonic_sensor_port = Port.S2

# Set wheel diameter and exle track (in mm)
wheel_diameter = 56
axle_track = 144

# Initialize EV3Brick
ev3 = EV3Brick()
ev3.speaker.beep()

# Initilize motors
left_motor = Motor(left_motor_port)
right_motor = Motor(right_motor_port)

# Initialize sensors
color_sensor = ColorSensor(color_sensor_port)
ultrasonic_sensor = UltrasonicSensor(ultrasonic_sensor_port)

# Initialize robot
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

def cycle():
    while True:
        if color_sensor.color() == Color.WHITE:
            robot.stop()
            robot.turn(1800)
            continue
        first_distance = ultrasonic_sensor.distance()
            
