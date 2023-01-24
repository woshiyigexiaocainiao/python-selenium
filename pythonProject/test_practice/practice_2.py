# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver2 = webdriver.Chrome()
driver2.get("https://www.baidu.com")
driver2.maximize_window()
# 获取文本框的尺寸
size = driver2.find_element(By.CSS_SELECTOR, "[name='wd']").size
print(size)
# 获取百度页面底部备案信息
text = driver2.find_element(By.CSS_SELECTOR, "#bottom_layer > div").text
print(text)
# 返回元素的属性值，可以是id，name，type或其他任意属性
attribute = driver2.find_element(By.CSS_SELECTOR, "#kw").get_attribute("type")
print(attribute)
# 返回元素的结果是否可见，返回结果为True或False
result = driver2.find_element(By.CLASS_NAME, "s_ipt").is_displayed()
print(result)

driver2.find_element(By.XPATH, "//span[contains(@class,'s_ipt_wr')]/input").clear()
driver2.find_element(By.XPATH, "//input[@class='s_ipt']").send_keys("selenium")
time.sleep(1)
# submit()与click()有时可以互换使用，当不提供搜索按钮，而是通过回车键完成搜索提交，这时可以用submit()，但click()单击元素使用更广
driver2.find_element(By.XPATH, "//input[@value='百度一下']").submit()
driver2.quit()

# bottom_layer > div > p:nth-child(9) > span

























