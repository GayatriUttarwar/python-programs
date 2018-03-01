import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import urllib2
import smtplib
import datetime

today=datetime.date.today()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
sensor =  Adafruit_DHT.DHT11
pin = 17
GPIO.setmode(GPIO.BCM)
count = 0
abc = 'https://thingspeak.com/update?key=YVDUGDVOCJ6UDYG9'
server.login("gayatri.rasberrypi@gmail.com","rasberrypi#08")
while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    while (GPIO.input(4)==False):
        count=count+1
    print count,today
    count=0
    
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    if humidity is not None and temperature is not None:
        print humidity
        print temperature
    time.sleep(1)
    
    print 'sending email'
    mylink = abc+'&field1='+str(count)+'&field2='+str(temperature)+'&field3='+str(humidity)
    #print mylink
    response=urllib2.urlopen(mylink)
    print response.code
    mymsg = 'Ldr count is '+str(count)+'\nTemperature is '+str(temperature)+'\nHumidity is '+str(humidity)
    server.sendmail("gayatri.rasberrypi@gmail.com","Rpi.tests.readings@gmail.com",mymsg)
    server.sendmail("gayatri.rasberrypi@gmail.com","gayatri.rasberrypi@gmail.com",mymsg)
    print 'sent !!!'
    time.sleep(10)
    count=0
    
