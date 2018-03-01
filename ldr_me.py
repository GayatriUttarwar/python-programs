import RPi.GPIO as GPIO
import time
count=0
GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while (GPIO.input(4) == False ):
        count=count+1
    print count
    count=0
    time.sleep(1)
