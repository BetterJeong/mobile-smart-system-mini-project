import time
import RPi.GPIO as GPIO
import circuit  # 센서, LED 입출력 모듈

while (True):
    distance = circuit.measureDistance()
    mcp = circuit.measureMcp()
    
    # 거리가 20cm 보다 가까워지면 LED 켜기
    if distance <= 20:
        print(mcp)
        # 주변 밝기에 따라 LED 밝기 조절
        if mcp <= 500:
            circuit.controllLED(100)
        else:
            circuit.controllLED(10)
    else:
        circuit.controllLED(0)
   
