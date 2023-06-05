import RPi.GPIO as GPIO

FLAME_PIN = 23  #불꽃 감지 센서는 GPIO 23번과 연결

#불꽃 미감지 : 1 반환
#불꽃 감지 : 0 반환

def detect_flame():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLAME_PIN, GPIO.IN)
    return GPIO.input(FLAME_PIN)    #불꽃감지 센서의 감지 결과값을 반환