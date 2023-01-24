# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 控制浏览器

driver = webdriver.Chrome()
# 进入百度首页
baidu_url = "https://m.baidu.com"
driver.get(baidu_url)
print("设置浏览器宽480，高800显示")
# 控制浏览器大小
driver.set_window_size(480, 800)
time.sleep(1)
# 窗口最大化
driver.maximize_window()
time.sleep(1)
# 点击百度一下图标
driver.find_element(By.XPATH, "//div[@id='logo']/a/img").click()
# 返回到百度首页
print(f"back to {baidu_url}")
driver.back()
# 前进到百度一下
driver.forward()
# 刷新当前页面
driver.refresh()
time.sleep(2)
driver.quit()

























