import threading
import time
import db_conn as db
import RPi.GPIO as GPIO
import time

#센서 및 액츄에이터 작동용 파일들
import temp
import flame
import gas
import pumpbuzz
import rgb

global temperature   
global gas_value 
global flameValue

def interval_interrupt():
    # 1분마다 인터럽트 함수 호출하는 쓰레드
    threading.Timer(60.0, interval_interrupt).start()
    #print("interrupt occur!")
    #print(temperature, gas_value, flameValue)
    
    #온도, 가스농도, 불꽃 감지 결과를 db에 삽입
    if temperature != 0:
        db.insert(temperature, gas_value, flameValue)

def main():    
    global temperature
    global gas_value
    global flameValue

    temperature = 0.0
    gas_value = 0
    flameValue = 0

    interval_interrupt()    # 1분마다 인터럽트 함수 호출 시작
    
    try:
        while True:
            print('======================')
            gas_value = gas.detect_gas_ad()              #가스 농도 측정
            print("가스 농도 :", gas_value)

            temperature = round(temp.get_temp(),1)       #온도 측정
            print("측정 온도:", temperature)

            flameValue=flame.detect_flame()              #불꽃 감지
            
            if flameValue == 0 :                         #화재 감지 시
                print("화재 감지")
                pumpbuzz.on()
                rgb.off()

            elif flameValue != 0 and gas_value >= 200:    #가스 농도가 임계값 이상 올라갔을 때
                print("경고")
                pumpbuzz.off()
                rgb.on()

            else:                                          #평상시
                print("화재 미감지")                      
                pumpbuzz.off()
                rgb.off()
            print('======================') 

            time.sleep(2)                                #루틴이 끝날 때마다 2초 대기

    except KeyboardInterrupt:
        # 프로그램 종료 시 GPIO 클린업
        GPIO.cleanup()
        
# 메인 함수 호출
if __name__ == '__main__':
    main()