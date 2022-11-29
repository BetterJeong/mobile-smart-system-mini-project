from adafruit_htu21d import HTU21D
import busio

# 온, 습도
sda = 2 # sda 2번 핀 지정
scl = 3 # scl 3번 핀 지정
i2c = busio.I2C(scl, sda)
sensor = HTU21D(i2c)    # HTU21D 장치를 제어하는 객체 리턴

# 온도 측정 함수
def getTemperature():
    return float(sensor.temperature)

# 습도 측정 함수
def getHumidity():
    return float(sensor.relative_humidity)
