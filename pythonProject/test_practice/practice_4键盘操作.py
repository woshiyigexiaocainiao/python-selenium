# -- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver4 = webdriver.Chrome()
driver4.get('https://www.baidu.com')
# 在输入框输入内容
driver4.find_element(By.ID, 'kw').send_keys('seleniumm')
# 删除多输入的M
driver4.find_element(By.ID, 'kw').send_keys(Keys.BACKSPACE)
sleep(2)
# 输入空格键+“教程”
driver4.find_element(By.ID, 'kw').send_keys(Keys.SPACE)
driver4.find_element(By.ID, 'kw').send_keys('教程')
# 输入组合键CTRL+A，全选输入框内容
driver4.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')
# 输入组合键CTRL+X，剪切输入框内容
driver4.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'x')
# 输入组合键CTRL+V,粘贴内容到输入框
driver4.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'v')
# 用回车键代替单击操作
driver4.find_element(By.ID, 'su').send_keys(Keys.ENTER)

driver4.quit()

















