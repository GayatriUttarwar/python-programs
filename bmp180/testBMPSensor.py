 
import Adafruit_BMP.BMP085 as BMP085
from time import sleep
sensor = BMP085.BMP085()

while True:
    temperature = sensor.read_temperature()
    print "Temperature is "+str(temperature) +" DegreeC"
    
    pressure = sensor.read_pressure()
    print "Pressure is " +str(pressure) + " Pa"

    altitude = sensor.read_altitude()
    altitude = round(altitude,2)
    print str(altitude) + "- Altitude"

    sea_level = sensor.read_sealevel_pressure()
    print str(sea_level)+ "- Sea level Pressure"
    sleep(5)
    print "\n"
#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
#print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
