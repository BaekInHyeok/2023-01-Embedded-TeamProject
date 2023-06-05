import RPi.GPIO as GPIO
import spidev

gas_channel = 0 #가스센서는 ADC 0번 채널에 연결
    
def detect_gas_ad():
    # MCP3008의 SPI 버스 및 디바이스 설정
    spi = spidev.SpiDev()
    spi.open(0, 0)  # SPI 버스 0, 디바이스 0
    spi.max_speed_hz = 1350000

    # MCP3008로부터 아날로그 값을 읽어오는 함수
    data = 0
    adc = spi.xfer2([1, (8 + gas_channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data #아날로그 값 반환