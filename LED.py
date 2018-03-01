import RPi.GPIO as GPIO
import time
led=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
while True:
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    print 'on'
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)
