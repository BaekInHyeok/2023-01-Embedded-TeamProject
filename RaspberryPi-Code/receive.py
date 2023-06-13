import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):        #연결 되었을 경우 호출(콜백 함수)
    print("Connected with result code "+str(rc))
    client.subscribe("device/data")  # 채널 설정

def on_message(client, userdata, msg):              #메세지를 수신하였을 경우 호출(콜백 함수)
    print("Received message: " + str(msg.payload.decode()))

client = mqtt.Client()              #클라이언트 객체 및 콜백함수 설정
client.on_connect = on_connect
client.on_message = on_message

# AWS IoT Core에 연결하기 위한 인증서 및 엔드포인트 정보
ca_file = "./rootCA.pem"
cert_file = "./6a17cffffe220b9d3a3baed6f4394123e01b9c253a1dac027f3de6f1eb01b4c5-certificate.pem.crt"
key_file = "./6a17cffffe220b9d3a3baed6f4394123e01b9c253a1dac027f3de6f1eb01b4c5-private.pem.key"
iot_endpoint = "a2qvqhctw3m8w9-ats.iot.eu-north-1.amazonaws.com"
port = 8883

client.tls_set(ca_certs=ca_file, certfile=cert_file, keyfile=key_file, tls_version=ssl.PROTOCOL_SSLv23)
client.connect(iot_endpoint, port=port, keepalive=60)       #포트번호 8883 연결

client.loop_forever()           #루프를 돌면서 계속 디바이스의 메세지를 수신받음