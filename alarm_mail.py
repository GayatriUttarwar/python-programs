import RPi.GPIO as GPIO
import smtplib
import time
import datetime

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
today=datetime.date.today()
while True:
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)
    print 'Ringing'
    GPIO.output(18,GPIO.HIGH)
    print 'sending email....'
    server.login("gayatri.rasberrypi@gmail.com","rasberrypi#08")
    mymsg = 'Times Up !!!'+'\n As of '+str(today)
    server.sendmail("gayatri.rasberrypi@gmail.com","Rpi.tests.readings@gmail.com",mymsg)
    print 'mail sent !!'
    time.sleep(5)
    GPIO.output(18,GPIO.LOW)
    time.sleep(5)
    print 'band'
    
    
