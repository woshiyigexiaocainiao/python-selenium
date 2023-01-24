# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import *
import time
"""
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top").click()
driver.find_element(By.LINK_TEXT, "搜索设置").click()
sleep(2)
driver.quit()
"""

print(time.time())
dt = datetime.now()
print(dt)
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
print(dt.strftime('%c'))
t = dt.weekday()
print(t)





