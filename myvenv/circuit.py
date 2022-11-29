import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008

# 초음파 센서
trig = 20   # 20번 핀 사용
echo = 16   # 16번 핀 사용
GPIO.setmode(GPIO.BCM)  # BCM 모드 작동
GPIO.setwarnings(False) # 경고글 출력 안 함
GPIO.setup(trig, GPIO.OUT)  # trig 20 으로 출력 지정
GPIO.setup(echo, GPIO.IN)   # echo 16 으로 입력 지정
GPIO.output(trig, False)

# 거리 측정 함수
def measureDistance():
    global trig, echo
    GPIO.output(trig, True) # 신호 1 발생
    time.sleep(0.00001) # falling edge 만들기 위해 짧은 시간 후 감소시킴
    GPIO.output(trig, False)    # 신호 0 발생, falling edge

    while(GPIO.input(echo) == 0):
        pass
    pulse_start = time.time()   # 초음파 발사 순간, 발생 시작
    while(GPIO.input(echo) == 1):
        pass
    pulse_end = time.time() # 초음파 도착 순간, 수신 완료

    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration # cm 로 거리 계산한 값 반환

# 조도 측정 함수
def measureMcp():
    mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)
    return mcp.read_adc(0)

# LED
ledGreen = 5    # 5번 초록 LED 핀 지정
ledRed = 6  # 6번 빨간 LED 핀 지정
GPIO.setup(ledGreen, GPIO.OUT)  # 5번 핀 출력 지정
GPIO.setup(ledRed, GPIO.OUT)   # 6번 핀 출력 지정
pwm_ledGreen = GPIO.PWM(ledGreen, 500)  # PWM 세팅
pwm_ledRed = GPIO.PWM(ledRed,500)   # PWM 세팅
pwm_ledGreen.start(100) # 출력 사이클 지정
pwm_ledRed.start(100)   # 출력 사이클 지정

# LED 밝기 조절 함수
def controllLED(brightness):
    pwm_ledGreen.ChangeDutyCycle(brightness)
    pwm_ledRed.ChangeDutyCycle(brightness)
