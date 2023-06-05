import RPi.GPIO as GPIO

#릴레이 모듈은 HIGH 신호에서 전기를 끊고, LOW 신호에서 전원을 인가한다.
#따라서, 릴레이 모듈을 사용하면, 라즈베리파이에 직결하는 방식과 반대다.

RELAY_PIN1 = 17 #GPIO 17번과 연결되어 있는 릴레이 모듈은 워터펌프 제어
RELAY_PIN2 = 27 #GPIO 27번과 연결되어 있는 릴레이 모듈은 부저 제어

#작동 시작 함수
def on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(RELAY_PIN1, GPIO.OUT)
    GPIO.output(RELAY_PIN1, GPIO.LOW)#워터펌프에 전원 인가
    
    GPIO.setup(RELAY_PIN2, GPIO.OUT)
    GPIO.output(RELAY_PIN2, GPIO.LOW)#부저에 전원 인가
    
#작동 중단 함수
def off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RELAY_PIN1, GPIO.OUT)
    GPIO.output(RELAY_PIN1, GPIO.HIGH)#워터펌프 전원 중단
    
    GPIO.setup(RELAY_PIN2, GPIO.OUT)
    GPIO.output(RELAY_PIN2, GPIO.HIGH)#부저 전원 중단