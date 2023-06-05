import RPi.GPIO as GPIO

# BLUE_PIN = 5
# GREEN_PIN = 6
RED_PIN = 21

#설정
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_PIN, GPIO.OUT)
    # GPIO.setup(GREEN_PIN, GPIO.OUT)
    # GPIO.setup(BLUE_PIN, GPIO.OUT)

#RGB ON
def on():
    GPIO.setwarnings(False)
    setup()
    print("경고등 ON")
    GPIO.output(RED_PIN, GPIO.HIGH)

#RGG OFF
def off():
    GPIO.setwarnings(False)
    setup()
    print("경고등 OFF")
    GPIO.output(RED_PIN, GPIO.LOW)