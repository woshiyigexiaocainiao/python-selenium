# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import ctime, sleep
driver6 = webdriver.Chrome()
driver6.get("https://www.baidu.com")
element1 = WebDriverWait(driver6, 5, 0.5).until(
    ec.visibility_of_element_located((By.CSS_SELECTOR, '#kw')))

driver6.find_element(By.ID, 'kw').send_keys('selenium')

print(ctime())

for i in range(10):
    try:
        el = driver6.find_element(By.ID, 'kw22')
        if el.is_displayed():
            break
    except BaseException:
        pass
    sleep(1)
else:
    print("没看到kw22")
print(ctime())

driver6.quit()









