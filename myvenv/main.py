import picamera
from flask import Flask, render_template, request
import os
import time
import temperatureManager

app = Flask(__name__, static_folder = './static')

@app.route("/index")
def main():
    temp = temperatureManager.getTemperature()
    humi = temperatureManager.getHumidity()
    return render_template('index.html', temperature = temp, humidity = humi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
