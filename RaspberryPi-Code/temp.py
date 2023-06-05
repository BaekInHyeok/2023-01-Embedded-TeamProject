import Adafruit_DHT #Adafruit_DHT 라이브러리를 사용

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 20    #온습도 센서는 GPIO 20번에 연결

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)    #습도와 온도의 측정값
    return temperature  #온도만 반환