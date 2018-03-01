from Adafruit_IO import *
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

aio = Client('136f6d80280a4233ac1011c47e392794')
sensor =  Adafruit_DHT.DHT11
pin = 17
count=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while (GPIO.input(4) == False ):
        count=count+1
    aio.send('ldr',count)
    print '\n'
    print 'LDR Reading - ',count
    count=0
    time.sleep(1)
    
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print 'Humidity - ',humidity
        print 'Temperature - ',temperature
    time.sleep(0.2)
    aio.send('temp',temperature)
    aio.send('hum',humidity)
    time.sleep(1)
    
    data1 = aio.receive('sw1')
    print '24 LED',data1.value
    time.sleep(1)
    if (data1.value=='OFF'):
        GPIO.output(24,GPIO.HIGH)
        time.sleep(1)
    else:
        GPIO.output(24,GPIO.LOW)
        time.sleep(1)
        
        
    data2 = aio.receive('sw2')
    print '25 LED',data2.value
    time.sleep(1)
    if (data2.value=='OFF'):
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
    else:
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)
        

    data = aio.receive('sw')
    print 'RELAY',data.value
    time.sleep(0.1)
    if (data.value=='ON'):
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)
    else:
        GPIO.output(27,GPIO.LOW)
        time.sleep(1)
    
    
