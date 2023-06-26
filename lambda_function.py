import json
import jwt
import os
import pymysql.cursors

def lambda_handler(event, context):
    
    # DB에 id와 password에 일치하는 정보가 존재하는지 조회
    
    
    connection = pymysql.connect(host=os.environ['RDS_HOST'],
                             user=os.environ['RDS_USER'],
                             password=os.environ['RDS_PASSWORD'],
                             database=os.environ['RDS_DATABASE'], 
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `ID`, `PWD` FROM `login` WHERE `ID` = %s and `PWD` = %s"
            cursor.execute(sql, (event['ID'], event['PWD'],))
            result = cursor.fetchone()
            print(result)
            
    
            if result:
                # 일치하는 정보가 존재하는 경우 JWT 토큰을 생성해서 반환
                payload = { 'ID': result['ID'], 'PWD': result['PWD'] }
                encoded = jwt.encode(payload, os.environ['secret_key'], algorithm="HS256")
                
                return {
                    'statusCode': 200, 
                    'body': encoded 
                }
            
            else:
                # 일치하는 정보가 존재하지 않는 경우 로그인 실패를 반환
                return {
                    'statusCode': 404,
                    'body': '일치하는 사용자가 존재하지 않습니다.'
                }
