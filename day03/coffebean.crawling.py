#Selenium사용 웹페이지 사용

#패키지로드
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeeBeanStoreInfo(result):
    # chrome webdriver 객체 생성
    wd = webdriver.Chrome('C:/Users/admin/Desktop/chromedriver.exe') #경로조심!
    time.sleep(1)
    wd.get('https://www.coffeebeankorea.com/store/store.asp')

    for i in range(1,11):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')

        try:
            wd.execute_script(f"storePop2('{i}')")
            time.sleep(0.5) #팜업표시후에 크롤링이 안되서 브라우저가 닫힌느 것을 방지
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip() #strip 공백 제거
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])
        except Exception as e:
            print(e)
            continue
def main():
    result = []
    print('커피빈 매장 크롤링>>>')
    getCoffeeBeanStoreInfo(result)

    # #판다스 데이터프레임생성
    columns = ['store','address','phone']
    coffeebean_df = pd.DataFrame(result, columns=columns)
    # #csv저장
    # # hollys_df.to_csv('C:/localRepository/StudyBigData/holly_shop_info2_csv', index=True, encoding='utf-8')
    coffeebean_df.to_csv('./coffeebean_shop_info_csv', index=True, encoding='utf-8') 
    print('저장완료')

    del result[:]

if __name__=='__main__':
    main()