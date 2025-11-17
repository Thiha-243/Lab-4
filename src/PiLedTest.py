import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

import hal_led as led

def main():
    led.init()

    

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        led.set_output(0)
        sleep(0.1)
        led.set_output(1)
        sleep(0.1)
        ret = 1

    return ret


