import time
import paho.mqtt.client as mqtt
import ssl
import threading

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 23                        #온습도센서 D23연결

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#클라이언트 객체 및 콜백함수 설정
client = mqtt.Client()
client.on_connect = on_connect

#인증서
client.tls_set(ca_certs='./rootCA.pem', certfile='./b91377a604a8c59c1650b80d0a3e30540db09d31f90f0e1b377bcde92bf30fed-certificate.pem.crt', keyfile='./b91377a604a8c59c1650b80d0a3e30540db09d31f90f0e1b377bcde92bf30fed-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a2qvqhctw3m8w9-ats.iot.eu-north-1.amazonaws.com", 8883, 60)


def submit_data():          #반복문 돌면서 온도 측정 후 aws iot에 메세지 전달
    while (1):    	
        print("submit data" )
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        print(f"Temperature: {temperature:.1f} °C")
        client.publish("device/data", payload=f"{temperature:.1f}°C", qos=0, retain=False)      #채널 설정하여 해당 채널로 메세지 전달
        time.sleep(5)


submit_data()