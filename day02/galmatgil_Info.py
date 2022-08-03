#부산 갈맷길 정보 API 크롤링
import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd 
import pymysql

#키 내꺼
serviceKey ='eSqGdRlWlkTFGdivTT298g9crQFPG86Xfe2izgQ91K7fa9JWzhFzmB7yuaR4CboNrMKzPbaMUXd%2FHJK6Te%2FU7Q%3D%3D'


def getRequestUrl(url):

    '''
    URL 접속 요청 후 응답함수
    -----------------
    parammeter : url -> OpenAPI
    전체URL
    '''
    req = urllib.request.Request(url)

    try: #request가 끊기면 오류가 생겼을 때, 처리하는 방법 정의
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: #200은 ok이고, 400번대는 일반 error, 500번대는 server error
            print(f'[({datetime.datetime.now()})] Url Request success')
            return res.read().decode('utf-8') #에러가 날만한 상황을 제시함
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None # 에러가 나면 이렇게 해라고 지정

def getGalmatgilInfo():
    service_url = 'http://apis.data.go.kr/6260000/fbusangmgcourseinfo/getgmgcourseinfo'
    params = f'?serviceKey={serviceKey}'
    params +='&numOfRows=10'
    params +='&pageNo=1'
    params +='&resultType=json'

    url = service_url + params

    retData = getRequestUrl(url)

    if retData == None:
        return None
    else:
         return json.loads(retData)

    
def getGalmetgilService():
    result=[]

    jsonData = getGalmatgilInfo()
    # print(jsonData)
    if jsonData['getgmgcourseinfo']['header']['code'] == '00':
        if jsonData['getgmgcourseinfo']['item'] == '':
            print('서비스 오류!!!')
        else:
            for item in jsonData['getgmgcourseinfo']['item']:
                seq = item['seq']
                course_nm = item['course_nm']
                gugan_nm = item['gugan_nm']
                gm_range = item['gm_range']
                gm_degree = item['gm_degree']
                start_pls = item['start_pls']
                start_addr = item['start_addr']
                middle_pls = item['middle_pls']
                middle_adr = item['middle_adr']
                end_pls = item['end_pls']
                end_addr = item['end_addr']
                gm_course = item['gm_course']
                gm_text = item['gm_text']

                result.append([seq, course_nm, gugan_nm, gm_range, gm_degree, start_pls, start_addr, middle_pls, middle_adr, end_pls, end_addr, gm_course, gm_text])
            
    return result

def main():
    result = []

    print('부산 갈맷길코스 조회합니다')
    result = getGalmetgilService()

    if len(result) > 0:
        #csv파일저장
        columns = ['seq', 'course_nm', 'gugan_nm', 'gm_range', 'gm_degree', 'start_pls', 'start_addr', 'middle_pls', 'middle_adr', 'end_pls', 'end_addr', 'gm_course', 'gm_text']
        result_df = pd.DataFrame(result, columns=columns)
        result_df.to_csv(f'./부산갈맷길정보.csv', index=False,
                        encoding='utf-8')

        print('csv파일 저장완료!')

        #DB 저장
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='1234',
                                    db='crawling_data')
        cursor = connection.cursor()

        #칼럼명 만드기
        cols='`,`'.join([str(i) for i in result_df.columns.tolist()])

        for i, row in result_df.iterrows():
            sql = 'INSERT INTO `galmatgil_info` (`' + cols +'`) VALUES (' + '%s, '*(len(row)-1)+'%s)'
            cursor.execute(sql, tuple(row))

        connection.commit()
        connection.close()

        print('DB저장완료')

if __name__=='__main__':

    main()