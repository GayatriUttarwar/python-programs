from Adafruit_IO import *
import time
aio = Client('136f6d80280a4233ac1011c47e392794')
temp=45

while True:
    aio.send('temp',temp)
    data = aio.receive('sw')
    print data.value
    time.sleep(0.1)
    temp = temp + 2
