# -- coding: utf-8 --
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver8 = webdriver.Chrome()
driver8.maximize_window()
driver8.get('https://www.baidu.com')
time.sleep(2)
# 获取当前页面句柄
now_handle = driver8.current_window_handle

# 登录百度账号
# driver8.find_element(By.ID, "s-top-longinbtn").click()
driver8.find_element(By.LINK_TEXT, '登录').click()
time.sleep(10)
driver8.find_element(By.ID, 'TANGRAM__PSP_11__regLink').click()
# 获取全部页面句柄
handles = driver8.window_handles
# 进入注册窗口
for handle in handles:
    if handle != now_handle:
        driver8.switch_to.window(handle)
        title1 = driver8.title
        print(title1)
        driver8.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('caicai')
        driver8.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys(17888826671)
        driver8.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys('cxc851123')
        time.sleep(2)
        # 获取警告框
        alert = driver8.switch_to.alert
        # 获取警告框信息
        print(alert.text)
        # 取消警告框
        alert.dismiss()
        time.sleep(5)
        driver8.close()
driver8.switch_to.window(now_handle)
title0 = driver8.title
print(title0)
time.sleep(2)
driver8.find_element(By.ID, 'TANGRAM__PSP_4__closeBtn').click()
"""login_frame = driver8.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_5__ > iframe')
driver8.switch_to.frame(login_frame)
print(driver8.title)
time.sleep(5)"""
"""driver8.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('17888826576')
driver8.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('cxc851123')
driver8.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()"""
time.sleep(3)
# driver8.switch_to.default_content()

driver8.quit()


















