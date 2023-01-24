# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get("https://www.baidu.com")
# web.find_element(By.ID, 'kw').send_keys('大象')

web.find_element("s_ipt").send_keys('seleniumm')
web.find_element(By.ID, 'su').click()





