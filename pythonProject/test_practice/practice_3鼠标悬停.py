# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver3 = webdriver.Chrome()
driver3.get("https://www.baidu.com")
driver3.maximize_window()

above = driver3.find_element(By.CSS_SELECTOR, "#s-usersetting-top")
ActionChains(driver3).move_to_element(above).perform()
driver3.find_element(By.LINK_TEXT, "搜索设置").click()
driver3.find_element(By.CSS_SELECTOR, '.s-skin-close').click()
#ActionChains(driver3).move_to_element(av).click().perform()

time.sleep(2)
driver3.quit()
# ActionChains(driver3).context_click()













