import datetime
import RPi.GPIO as GPIO
import time
count=0
GPIO.setmode(GPIO.BCM)
mylog = open("mylog.csv","w")
mylog.write('Light,Hour,Minute,Second,Year-Month-Date,Timestamp\n')
today=datetime.date.today()

while True:
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(4,GPIO.IN)
    mylog = open("mylog.csv","a")
    while (GPIO.input(4) == False ):
        count=count+1
        mytime=datetime.datetime.now()
        a=mytime.hour
        b=mytime.minute
        c=mytime.second
        d=time.time()
    print count,today,a,b,c,d
    now = str(count)+','+str(a)+','+str(b)+','+str(c)+','+str(today)+','+str(d)
    mylog.write(now + '\n')
    count=0
    time.sleep(1)
    mylog.flush()
    mylog.close()

