from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pyperclip
import time

def copy_input(xpath, Input):
    pyperclip.copy(Input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    

driver = webdriver.Chrome('C:/Users/USER/Desktop/chromedriver.exe')

driver.implicitly_wait(3)
ID='201824458'
pw='imthebest02@'

driver.get('https://lib.pusan.ac.kr/login/?redirect_to=https%3A%2F%2Flib.pusan.ac.kr%2F')
copy_input('//*[@id="id"]',ID)
copy_input('//*[@id="pw"]',pw)
driver.find_element_by_xpath('//*[@id="do_login"]').click()
time.sleep(5)
for i in range(7411250,7411300):
    try:
        driver.get('http://www.dbpia.co.kr.ssl.eproxy.pusan.ac.kr/pdf/pdfView.do?nodeId=NODE0'+str(i))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="#pub_modalTxtView"]/span').click()
        time.sleep(1)
        p=driver.find_element_by_xpath('//*[@id="textViewContents"]').text
        f=open("G:/dataset/"+str(i)+".txt",'w',encoding="utf-8")
        f.write(p)
        f.close()
        time.sleep(5)
    except:
        continue
    
