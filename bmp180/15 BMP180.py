import time
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()


while True:
	temp = sensor.read_temperature()
	pressure = sensor.read_pressure()
	altitude= sensor.read_altitude()
	sea_level_p = sensor.read_sealevel_pressure()

	print temp
	print pressure
	print altitude
	print sea_level_p
	time.sleep(1)

