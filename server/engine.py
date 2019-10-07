#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  engine.py
#  
#  
#  
import RPi.GPIO as GPIO
import time

servoPIN = 21
p = None

def initialize():
    global p
    if p is None:
        print("Ini engine")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        p = GPIO.PWM(servoPIN, 50)
        p.start(11.1) # Initialization
        time.sleep(0.5)        
		
def open_door():
    global p
    initialize()
    p.ChangeDutyCycle(7.5) #Izquirerda 90
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

def close_door():
    global p
    initialize()
    p.ChangeDutyCycle(11.1) #Centrar
    time.sleep(0.5)
    p.ChangeDutyCycle(0)