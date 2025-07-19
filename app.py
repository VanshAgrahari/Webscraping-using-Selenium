from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time

s=Service('C:/Users/Vansh Agrahari/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get('https://www.smartprix.com/mobiles')


time.sleep(2) 
out_stock= driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span')
out_stock.click()

time.sleep(3)
exclude_upcoming=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span')
exclude_upcoming.click()

time.sleep(5)

old_height=driver.execute_script('return document.body.scrollHeight')
count=0

time.sleep(2)


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    load=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
    load.click()
    time.sleep(3)

    new_height=driver.execute_script('return document.body.scrollHeight')
    print(old_height,new_height)
    if old_height==new_height:
        break

    old_height=new_height
    count+=1
    
html=driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)


time.sleep(30)
