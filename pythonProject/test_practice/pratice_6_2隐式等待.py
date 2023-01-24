# -- coding: utf-8 --
import selenium.common
from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver.common.by import By
webdriver6_2 = webdriver.Chrome()
webdriver6_2.implicitly_wait(10)
webdriver6_2.get('https://www.baidu.com')

try:
    print(ctime())
    webdriver6_2.find_element(By.ID, 'kw1').send_keys('selenium')

except selenium.common.exceptions.NoSuchElementException as NSE:
    print(NSE)

finally:
    print(ctime())
webdriver6_2.quit()
















