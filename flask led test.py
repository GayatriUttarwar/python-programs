import RPi.GPIO as GPIO
import time
from flask import Flask


GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return "LED Status of 4 LEDS and 1 RELAY !!"
@app.route("/l1f")
def hello1():
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(24,GPIO.LOW)
        time.sleep(1)
        GPIO.output(8,GPIO.LOW)
        time.sleep(1)
        GPIO.output(27,GPIO.HIGH)
    return "1st LED is on! \n2nd LED is off! \n3rd LED is on! \n4th LED is off \nRELAY is on"
@app.route("/l1o")
def hello2():
    while True:
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)
        GPIO.output(7,GPIO.LOW)
        time.sleep(1)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(27,GPIO.LOW)
    return "1st LED is off! \n2nd LED is on! \n3rd LED is off! \n4th LED is on \nReLAY is off"

if __name__ ==  "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)

