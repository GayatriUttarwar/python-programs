from espeak import espeak
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig=14
echo=15
distance=0
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
print 'Welcome to ultrasonic distance meter'
espeak.synth('Welcome to ultrasonic distance meter')
while True:
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.output(trig,False)
    #print 'waiting.....'
    time.sleep(0.1)
    GPIO.output(trig,True)
    time.sleep(0.0001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==False:
        start=time.time()
    #time.sleep(0.00000005)
    while GPIO.input(echo)==True:
        finish=time.time()
    duration=finish - start
    dist=duration * 17150
    dist=round(dist,2)
    if(dist<200 and dist>0):
        distance = dist
    #print 'distance is',distance,'cm \n'
    #time.sleep(1)
    inputval = GPIO.input(26)
    if (inputval == True):
        print 'distance is',distance,'cm \n'
        mystring= 'distance measured is '+ str(distance)
        espeak.synth(mystring)
