from flask import Flask,render_template
import datetime
import Adafruit_BMP.BMP085 as BMP085
import time
sensor1 = BMP085.BMP085()
app = Flask(__name__)
@app.route("/")

def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    temperature = sensor1.read_temperature()
    pressure = sensor1.read_pressure()
    altitude = sensor1.read_altitude()
    altitude = round(altitude,2)
    sea_level = sensor1.read_sealevel_pressure()
    templateData = {
        'title' : 'HELLO !',
        'time' : timeString,
        'temp' : temperature,
        'humid' : pressure,
        'alti' : altitude,
        'sea' : sea_level
        }
    return render_template('sensor.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
