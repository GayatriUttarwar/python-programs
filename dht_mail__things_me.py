import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import urllib2

sensor =  Adafruit_DHT.DHT11
pin = 17
GPIO.setmode(GPIO.BCM)
abc = 'https://thingspeak.com/update?key=YVDUGDVOCJ6UDYG9'

while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    count=0
    while (GPIO.input(4) == False ):
        count=count+1
    print count
    mylink = abc+'&field1='+str(count)
    print mylink
    response=urllib2.urlopen(mylink)
    print response.code
    time.sleep(10)
    count=0
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print humidity
        print temperature
        print '\n'
    time.sleep(2)
