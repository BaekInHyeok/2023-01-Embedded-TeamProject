import pymysql
from datetime import datetime

#DB 연결 설정
host = '192.168.77.230' 
user = 'root'  
password = '1234'  
database = 'embeded'  

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

#온도, 가스농도, 불꽃감지 측정 데이터 삽입 함수
def insert(temperature, gas, flame):
    try:
        cursor = connection.cursor()    #커서 생성

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO data (timestamp, temp, gas, flame) VALUES (%s, %s, %s, %s)"    #인자 설정, 쿼리문 작성
        cursor.execute(query, (current_time, temperature, gas, flame))                      #쿼리문 실행
        connection.commit() #커밋

    except Exception as e:  #예외처리
        print("오류 발생:", e)