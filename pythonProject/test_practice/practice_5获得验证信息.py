# -- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver5 = webdriver.Chrome()
driver5.maximize_window()
driver5.get('https://www.baidu.com')
# 打印当前页面title
print(driver5.title)
# 打印当前页面url
print(driver5.current_url)
driver5.find_element(By.ID, 'kw').send_keys('selenium')
driver5.find_element(By.ID, 'su').click()

num = driver5.window_handles
driver5.switch_to.window(num[0])
# 再次打印页面title
print('title:', driver5.title)
# 再次打印页面url
print('url:', driver5.current_url)
sleep(5)
# 获取搜索页面搜索条数
len1 = driver5.find_element(By.CSS_SELECTOR, "#tsn_inner > div:nth-child(2) > span").text
print(len1)


driver5.quit()






