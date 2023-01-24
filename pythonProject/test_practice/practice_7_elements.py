# -- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver7 = webdriver.Chrome()
driver7.maximize_window()
driver7.get('https://www.baidu.com')
# 打印当前页面title
# print(driver5.title)
# 打印当前页面url
# print(driver5.current_url)
driver7.find_element(By.ID, 'kw').send_keys('selenium')
driver7.find_element(By.ID, 'su').click()
# 定位一组元素
texts = driver7.find_elements(By.XPATH, "//*[@id='2']/div/div/h3/a")

# \32  > div > div > div.c-row.c-gap-top-small > div.c-span9.c-span-last.main-info_4Q_kj > div.catalog-list_iR5a4 > div
# 计算定位元素的数量
print(len(texts))
# 打印出元素的标题
for t in texts:
    print(t.text)

driver7.quit()


























