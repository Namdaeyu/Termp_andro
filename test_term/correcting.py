from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup as BS4
import re
import sys

def htmlcleaner(string):
    string = re.sub('<.+?>', '', string, 0).strip()
    return string

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
#창을 안켜고 Chrome을 실행

driver = webdriver.Chrome('C://Users//USER//Desktop//chromedriver.exe',options = options)
#webdriver실행, 위치는 자기 컴퓨터에 chromedriver.exe를 둔 장소
text="안녕하세요 김태호 입니다."
driver.get('https://www.incruit.com/tools/spell/')
#driver가 맞춤법 검사기 사이트에 접근
driver.implicitly_wait(3)
#암묵적으로 3초 기다린다
driver.find_element_by_xpath('//*[@id="spellcontent"]').click()
#사이트에서 글쓰는 부분을 클릭 
##driver.find_element_by_xpath('//*[@id="spellcontent"]').send_keys(sys.argv[1].decode('utf-8'))
driver.find_element_by_xpath('//*[@id="spellcontent"]').send_keys(text)
#입력받은 문자열을 사이트에 적는다, 나중에 통신할 때 값을 받아올 것
driver.find_element_by_xpath('//*[@id="buttonCheckSpell"]/img').click()
driver.find_element_by_xpath('//*[@id="buttonModify"]/img').click()
#맞춤법 검사 버튼 클

try:
    alert = driver.switch_to.alert
except:
    print("에러발생")
    exit()
alert.accept()
#알림, 경고창 무시

clean_str = ""
html = driver.page_source

soup = BS4(html,'html.parser')
for content in soup.find_all('p', id='spellingAll'):
    content_str = str(content)

    for string in content_str.split('<br/>'):
        clean_str=htmlcleaner(string) #순수 한글문자열만 남김
print(clean_str) #이 부분 나중에 통신할 때 값으로 넘겨줄 것
driver.quit()

