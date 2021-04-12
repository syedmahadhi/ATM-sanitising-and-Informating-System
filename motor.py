import RPi.GPO as GPIO
import time

motorPin1 = 13
motorPin2 = 11
enablePin = 15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorPin1, GPIO.OUT)
    GPIO.setup(motorPin2, GPIO.OUT)
    GPIO.setup(enablePin, GPIO.OUT)
    GPIO.output(enablePin, GPIO.LOW)
    GPIO.output(motorPin1, GPIO.LOW)
    GPIO.output(motorPin2, GPIO.LOW)

def loop():
    GPIO.output(enablePin, GPIO.HIGH)
    while True:
        GPIO.output(motorPin2, GPIO.LOW)
        GPIO.output(motorPin1, GPIO.HIGH)